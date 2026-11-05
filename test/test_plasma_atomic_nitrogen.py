"""Source-anchored resolved atomic nitrogen chemistry and wall conservation."""
import ast
import json
import math
from pathlib import Path

import numpy as np
import pytest

from rmgpy import constants
from rmgpy.chemkin import load_species_dictionary
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.kinetics import Arrhenius

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = 'PlasmaAtomicNitrogen'
LIBDIR = ROOT / 'input/kinetics/libraries' / LIBRARY
NA = 6.02214179e23
AR_TOTAL = 1.38e15 * 1e-12 / NA**2
RATES = {
    'N2A + N => N2 + N(2P)': 4.4e-17,
    'N(2D) + N2 => N + N2': 1.7e-20,
    'N(2P) + N2 => N + N2': 5e-23,
    'N(2P) + N => N + N': 4.5e-19,
    'N(2P) + N => N(2D) + N': 1.5e-19,
    'N + N + N2 => N2B + N2': 8.27e-46,
    'N + N + Ar => N2B + Ar': AR_TOTAL/2,
    'N + N + Ar => N2 + Ar': AR_TOTAL/2,
    'N(2D) => N': (4*(1.60e-5+4.34e-6)+6*(9.71e-7+6.59e-6))/10,
    'N(2P) => N': (4*6.5e-3+2*2.6e-3)/6,
    'N(2P) => N(2D)': (4*(1.02e-3+6.0e-2+1.81e-3+2.56e-2)
                       +2*(3.45e-2+1.13e-3+5.2e-2))/6,
}


@pytest.fixture(scope='module')
def library():
    db = KineticsDatabase()
    db.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=[LIBRARY])
    return db.libraries[LIBRARY]


def test_heavy_rates_sources_and_balance(library):
    thermal = {e.label: e for e in library.entries.values() if isinstance(e.data, Arrhenius)}
    assert set(thermal) == set(RATES)
    for label, rate in RATES.items():
        entry = thermal[label]
        assert not entry.item.reversible
        assert entry.item.is_balanced()
        assert 'doi:10.' in entry.long_desc
        assert 'convention' in entry.long_desc.lower()
        assert 'uncertainty' in entry.long_desc.lower()
        assert sum(s.get_net_charge() for s in entry.item.reactants) == sum(
            s.get_net_charge() for s in entry.item.products)
        for temperature in (300., 600.):
            expected = rate * (math.exp(500/temperature) if label == 'N + N + N2 => N2B + N2' else 1)
            actual = entry.data.get_rate_coefficient(temperature) / NA**(len(entry.item.reactants)-1)
            assert actual == pytest.approx(expected, rel=2e-14, abs=0), label
    ar = [e for label, e in thermal.items() if label.startswith('N + N + Ar')]
    assert sum(e.data.get_rate_coefficient(300)/NA**2 for e in ar) == pytest.approx(AR_TOTAL, rel=2e-14, abs=0)
    assert all('ThirdBody' not in type(e.data).__name__ for e in library.entries.values())


def test_resolved_identity_and_thermo():
    species = load_species_dictionary(str(LIBDIR / 'dictionary.txt'))
    air = load_species_dictionary(str(ROOT/'input/kinetics/libraries/PlasmaAir/dictionary.txt'))
    assert species['N'].is_isomorphic(air['N'])
    for first, second in [('N', 'N(2D)'), ('N', 'N(2P)'), ('N(2D)', 'N(2P)')]:
        assert not species[first].is_isomorphic(species[second])
    db = ThermoDatabase()
    db.load_libraries(str(ROOT/'input/thermo/libraries'), ['PlasmaAtomicNitrogenThermo'])
    entries = db.libraries['PlasmaAtomicNitrogenThermo'].entries
    levels = {
        'N': (0., 4),
        'N(2D)': ((6*19224.464+4*19233.177)/10, 10),
        'N(2P)': ((2*28838.920+4*28839.306)/6, 6),
    }
    for label, (level_cm, weight) in levels.items():
        assert species[label].molecule[0].is_isomorphic(entries[label].item)
        model = entries[label].data
        for temperature in (298.15, 300., 600.):
            expected_h = 472680 + constants.h*constants.c*100*constants.Na*level_cm + 2.5*constants.R*(temperature-298.15)
            assert model.get_enthalpy(temperature) == pytest.approx(expected_h, abs=1e-7)
            assert model.get_heat_capacity(temperature) == pytest.approx(2.5*constants.R, abs=1e-10)
            expected_s = 153.301 + constants.R*math.log(weight/4) + 2.5*constants.R*math.log(temperature/298.15)
            assert model.get_entropy(temperature) == pytest.approx(expected_s, abs=1e-10)


def test_no_overlap_with_molecular_libraries(library):
    db = KineticsDatabase()
    db.load_libraries(str(ROOT/'input/kinetics/libraries'), libraries=[
        'PlasmaNitrogen', 'PlasmaNitrogenExcited', 'PlasmaArgonExcited'])
    for new in library.entries.values():
        for old_library in db.libraries.values():
            assert not any(new.item.is_isomorphic(old.item, either_direction=False)
                           for old in old_library.entries.values()), new.label


def test_readme_wall_declaration_and_resolved_atom_conservation(monkeypatch):
    import rmgpy.data.rmg as data_module
    from rmgpy.solver.plasma import PlasmaReactor

    monkeypatch.setattr(data_module, 'database', None)
    fence = chr(96)*3
    snippet = (LIBDIR/'README.md').read_text().split(fence+'python\n', 1)[1].split(fence, 1)[0]
    assignment, = ast.parse(snippet).body
    declaration = ast.literal_eval(assignment.value)
    assert set(declaration) == {'N', 'N(2D)', 'N(2P)'}
    assert declaration['N']['recombinationProbability'] == 5e-5
    for label in ('N(2D)', 'N(2P)'):
        assert declaration[label] == {'product': 'N', 'diffusivity': (7.05616e20, '1/(m*s)')}
    dictionary = load_species_dictionary(str(LIBDIR/'dictionary.txt'))
    hub = data_module.RMGDatabase()
    thermo = hub.thermo = ThermoDatabase()
    argon = load_species_dictionary(str(ROOT/'input/kinetics/libraries/PlasmaArgon/dictionary.txt'))
    dictionary['Arp'] = argon['Arp']
    thermo.load_libraries(str(ROOT/'input/thermo/libraries'),
                          ['PlasmaAtomicNitrogenThermo', 'primaryThermoLibrary', 'PlasmaThermo', 'electrocatThermo'])
    core = [dictionary[label] for label in ('e-', 'Ar', 'N2', 'N', 'N(2D)', 'N(2P)', 'Arp')]
    for sp in core:
        sp.thermo = thermo.get_thermo_data(sp)
    fractions = dict(zip(core, [1e-10, .8999999998, .097, .001, .001, .001, 1e-10]))
    r = PlasmaReactor((300,'K'), (666.61184,'Pa'), fractions, (10000,'K'),
                      diffusion_length=(((2.405/.05)**2+(np.pi/.3)**2)**-.5,'m'),
                      ion_reduced_mobility=(1.535e-4,'m^2/(V*s)'),
                      wall_single_bath_approximation=True,
                      wall_neutralization_products={'Arp': 'Ar'},
                      wall_diffusion_components=((2.405/.05)**2,(np.pi/.3)**2),
                      wall_chamber_geometry={'shape':'cylinder','radius':.05,'length':.3},
                      wall_neutral_diffusion=declaration)
    r.initialize_model(core, [], [], [])
    residual = r.residual(0, r.y.copy(), np.zeros_like(r.y))[0]
    assert residual[4] < 0 and residual[5] < 0 and residual[2] > 0
    assert 2*residual[2]+sum(residual[3:6]) == pytest.approx(0, abs=1e-14)



def test_six_ordinary_atomic_electron_owners(library):
    from rmgpy.kinetics import EEDFChannel
    owners = [entry for entry in library.entries.values()
              if isinstance(entry.data, EEDFChannel) and entry.data.role == 'collision']
    assert len(owners) == 6
    pairs = [
        ('N','N(2D)','e + N(4S) <-> e + N(2D), Excitation',2.39071),
        ('N','N(2P)','e + N(4S) <-> e + N(2P), Excitation',3.5676),
        ('N(2D)','N(2P)','e + N(2D) <-> e + N(2P), Excitation',1.177),
    ]
    for lower, upper, process, threshold in pairs:
        selected = [e for e in owners if e.data.process == process]
        assert len(selected) == 2
        assert {e.data.side for e in selected} == {'ine','sup'}
        for entry in selected:
            source, target = (lower,upper) if entry.data.side == 'ine' else (upper,lower)
            assert sorted(s.label for s in entry.item.reactants) == sorted(['e-',source])
            assert sorted(s.label for s in entry.item.products) == sorted(['e-',target])
            assert entry.data.collision_set == 'IST-Lisbon-N-Wang2014'
            assert not entry.item.reversible and entry.item.is_balanced()
            assert 'doi:10.1103/PhysRevA.89.062714' in entry.long_desc
            assert str(threshold) in entry.long_desc
            assert 'ordinary' in entry.long_desc and 'electron energy' in entry.long_desc
            assert 'Convention' in entry.long_desc and 'Uncertainty' in entry.long_desc


def test_frozen_collision_map_covers_each_ordinary_owner_once(library):
    document = json.loads((ROOT / 'input/eedf/atomic_nitrogen_channel_map.json').read_text())
    assert document['class_counts'] == {'A': 3, 'B': 3, 'C': 0, 'D': 0}
    assert set(document['sources']) == {'N_LXCat.txt', 'N_LXCat_extra.txt'}
    assert len(document['channels']) == 6
    identities = []
    for channel in document['channels']:
        if channel['class'] == 'B':
            assert channel['rmg'] is None
            assert channel['loki_process'].endswith(', Elastic')
            continue
        for field, side in [('rmg', 'ine'), ('inverse', 'sup')]:
            owner = channel[field]
            assert owner['library'] == LIBRARY
            entry = library.entries[owner['index']]
            assert entry.label == owner['reaction']
            assert entry.data.process == channel['loki_process']
            assert entry.data.side == side
            assert entry.data.collision_set == document['set']
            identities.append(owner['index'])
    assert sorted(identities) == list(range(12, 18))


def test_two_rate_only_dissociation_owners(library):
    from rmgpy.kinetics import EEDFChannel
    owners = [e for e in library.entries.values()
              if isinstance(e.data, EEDFChannel) and getattr(e.data, 'role', None) == 'rate_only']
    assert {e.index for e in owners} == {18, 19}
    assert {e.label for e in owners} == {'e- + N2 => e- + N + N', 'e- + N2 => e- + N + N(2D)'}
    for entry in owners:
        assert entry.item.is_balanced() and not entry.item.reversible
        assert entry.data.side == 'ine'
        assert entry.data.branch_product is None
        assert 'doi:10.1063/1.464385' in entry.long_desc
        assert 'doi:10.1016/0032-0633(78)90066-1' in entry.long_desc
        assert 'approximation' in entry.long_desc.lower()
        assert 'uncertainty' in entry.long_desc.lower()
