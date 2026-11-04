"""Native owner, state-data, network-continuity and refusal checks for tranche A."""
from copy import deepcopy
import math
from pathlib import Path
import sys

import pytest
import yaml
from rmgpy import constants
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.data.rmg import RMGDatabase
import rmgpy.data.rmg as rmg_data_module
from rmgpy.data.transport import TransportDatabase
from rmgpy.kinetics import EEDFChannel
from rmgpy.molecule import Molecule
from rmgpy.rmg.model import CoreEdgeReactionModel
from rmgpy.thermo.state import require_state_thermo
from rmgpy.tools.eedf.channel_map import _owner_problem

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'input'
STATES = [(87, 'Ars', '3P2', 3, 5, 93143.7600),
          (94, 'Ar(1s4)', '3P1', 3, 3, 93750.5978),
          (95, 'Ar(1s3)', '3P0', 3, 1, 94553.6652),
          (96, 'Ar(1s2)', '1P1', 1, 3, 95399.8276)]


@pytest.fixture(scope='module')
def database():
    previous = rmg_data_module.database
    hub = RMGDatabase()
    hub.thermo = ThermoDatabase()
    hub.thermo.load_libraries(str(DATA / 'thermo/libraries'), ['PlasmaExcitedNeutralThermo'])
    hub.transport = TransportDatabase()
    hub.transport.load(str(DATA / 'transport'), libraries=['PrimaryTransportLibrary'])
    db = KineticsDatabase()
    hub.kinetics = db
    db.load_libraries(str(DATA / 'kinetics/libraries'), libraries=['PlasmaArgon', 'PlasmaArgonDimer', 'PlasmaOxygenHeavy'])
    try:
        yield db
    finally:
        rmg_data_module.database = previous


def state_species(library, index):
    return next(s for s in library.entries[index].item.products if s.label != 'e-')


def test_literal_owners_and_distinct_states(database):
    lib = database.libraries['PlasmaArgon']
    cascade_ids = {1000 + channel * 4 + offset for channel in range(6, 39)
                   for offset in range(4)}
    assert set(lib.entries) == {86, 87, 94, 95, 96} | cascade_ids
    frozen = yaml.safe_load((DATA / 'eedf/argon_channel_map.yaml').read_text())
    assert frozen['class_counts'] == {'A': 152, 'B': 5, 'C': 0, 'D': 0}
    yields = yaml.safe_load((DATA / 'eedf/argon_cascade_yields.yaml').read_text())
    for c in yields['channels']:
        physical = next(row for row in frozen['channels'] if row['id'] == c['id'])
        assert c['process'] == physical['loki_process']
        assert c['threshold_eV'] == physical['threshold_eV']
    for cid, index in [(2, 87), (3, 94), (4, 95), (5, 96), (39, 86)]:
        row = next(c for c in frozen['channels'] if c['id'] == cid)
        assert row['rmg']['index'] == index and row['rmg']['status'] == 'present'
        assert _owner_problem(row, lib) is None
        entry = lib.entries[index]
        assert isinstance(entry.data, EEDFChannel)
        assert entry.data.process == row['loki_process']
        assert entry.data.collision_set == 'IST-Lisbon-Ar-2021' and entry.data.side == 'ine'
        assert not entry.item.reversible
    assert lib.entries[94].label == 'Ar + e- => Ar(1s4) + e-'
    assert lib.entries[94].data.process == 'e + Ar(1S0) -> e + Ar(3P1), Excitation'
    species = [state_species(lib, row[0]) for row in STATES]
    for i, (s, (_, label, term, mult, _, _)) in enumerate(zip(species, STATES)):
        assert s.label == label and s.molecule[0].electronic_state == term
        assert s.molecule[0].multiplicity == mult
        assert not s.molecule[0].is_isomorphic(Molecule().from_adjacency_list('1 Ar u0 p4 c0'))
        for other in species[i+1:]:
            assert not s.is_isomorphic(other)
    assert [c['id'] for c in frozen['channels'][:39] if c.get('rmg', {}).get('status') == 'absent'] == list(range(6, 39))
    absent = deepcopy(lib)
    del absent.entries[94]
    assert _owner_problem(next(c for c in frozen['channels'] if c['id'] == 3), absent)


def test_shared_metastable_is_one_runtime_species(database):
    model = CoreEdgeReactionModel()
    produced = state_species(database.libraries['PlasmaArgon'], 87)
    canonical, new = model.make_new_species(produced, generate_thermo=False)
    assert new
    for name in ['PlasmaArgonDimer', 'PlasmaOxygenHeavy']:
        participants = [s for e in database.libraries[name].entries.values()
                        for s in e.item.reactants + e.item.products if s.label == 'Ars']
        assert participants, name
        for s in participants:
            assert s.is_isomorphic(produced)
            same, new = model.make_new_species(s, generate_thermo=False)
            assert same is canonical and not new
    for index in [94, 95, 96]:
        other, new = model.make_new_species(state_species(database.libraries['PlasmaArgon'], index), generate_thermo=False)
        assert new and other is not canonical


def test_exact_state_thermo_and_transport(database):
    thermo = ThermoDatabase()
    thermo.load_libraries(str(DATA / 'thermo/libraries'), ['PlasmaExcitedNeutralThermo'])
    transport = TransportDatabase()
    transport.load(str(DATA / 'transport'), libraries=['PrimaryTransportLibrary'])
    for index, label, term, mult, g, energy in STATES:
        species = deepcopy(state_species(database.libraries['PlasmaArgon'], index))
        td, owner, entry = thermo.get_thermo_data_from_libraries(species)
        assert entry.item.electronic_state == term
        species.thermo = td
        require_state_thermo(species, thermo)
        h = energy * 100 * 6.62607015e-34 * 299792458 * 6.02214076e23
        s = 154.845 + 1.380649e-23 * 6.02214076e23 * math.log(g)
        # Historical 1s5 coefficients retain their published rounding.
        assert td.get_enthalpy(298.15) == pytest.approx(h, abs=0.2)
        assert td.get_entropy(298.15) == pytest.approx(s, abs=0.0005)
        assert td.get_heat_capacity(1000) == pytest.approx(2.5 * constants.R)
        tr, owner, entry = transport.get_transport_properties(species)
        assert entry.item.electronic_state == term
        assert tr.epsilon.value_si == pytest.approx(1134.93)
        assert tr.sigma.value_si == pytest.approx(3.33e-10)
        assert tr.polarizability.value_si == pytest.approx(1.64e-30, abs=1e-40)


def test_new_states_have_no_loss(database):
    for label in ['Ar(1s4)', 'Ar(1s3)', 'Ar(1s2)']:
        assert any(s.label == label for e in database.libraries['PlasmaArgon'].entries.values() for s in e.item.products)
        assert not any(s.label == label for lib in database.libraries.values() for e in lib.entries.values() for s in e.item.reactants)


def test_converter_refuses_removed_resonant_owner(database):
    """Exercise the canonical converter using the opt-in, pinned physical table spec."""
    import os
    from rmgpy.tools.eedf.channel_map import convert_channel_map, MissingOwners
    from rmgpy.tools.eedf.schema import load_spec
    path = os.environ.get('EEDF_BASE_SPEC')
    if not path:
        pytest.skip('EEDF_BASE_SPEC not set to the pinned pure-Ar base spec')
    spec = load_spec(path)
    frozen = yaml.safe_load((DATA / 'eedf/argon_channel_map.yaml').read_text())
    library = deepcopy(database.libraries['PlasmaArgon'])
    from rmgpy.tools.eedf.ownership import load_cascade_yields
    cascade_yields = load_cascade_yields(
        DATA / 'eedf/argon_cascade_yields.yaml', DATA / 'eedf/argon_radiative_data.yaml')
    converted, report = convert_channel_map(
        spec, frozen, library, 'IST-Lisbon-Ar-2021', cascade_yields)
    assert len(converted) == 39  # One row per physical collision, including elastic
    assert report['missing_owners'] == []
    assert report['shared_owners'] == []
    del library.entries[94]
    with pytest.raises(MissingOwners) as caught:
        convert_channel_map(spec, frozen, library, 'IST-Lisbon-Ar-2021', cascade_yields)
    assert [row['id'] for row in caught.value.report['missing_owners']] == [3]
    assert caught.value.report['shared_owners'] == []


def test_cascade_library_owners_are_one_sourced_family_per_channel(database):
    from rmgpy.tools.eedf.ownership import load_cascade_yields, make_branch_family
    lib = database.libraries['PlasmaArgon']
    snapshot = load_cascade_yields(
        DATA / 'eedf/argon_cascade_yields.yaml', DATA / 'eedf/argon_radiative_data.yaml')
    for channel_id in range(6, 39):
        row = next(item for item in snapshot['channels'] if item['id'] == channel_id)
        reactions = [lib.entries[1000 + channel_id * 4 + offset].item for offset in range(4)]
        owners = [('PlasmaArgon', 1000 + channel_id * 4 + offset,
                   reaction, lib.entries[1000 + channel_id * 4 + offset].data)
                  for offset, reaction in enumerate(reactions)]
        family = make_branch_family(snapshot, channel_id, row['process'], row['threshold_eV'],
                                    'IST-Lisbon-Ar-2021', owners)
        assert family['product_yields'] == row['product_yields']
        assert [lib.entries[1000 + channel_id * 4 + offset].data.branch_product
                for offset in range(4)] == [
            'Ar(1s5)', 'Ar(1s4)', 'Ar(1s3)', 'Ar(1s2)']
        assert all(not reaction.reversible for reaction in reactions)
        assert all(reaction.duplicate for reaction in reactions)
