"""N2 channel inventory, owner metadata and fate provenance checks."""
from copy import deepcopy
import hashlib
import os
from pathlib import Path
import subprocess
import sys

import pytest
import yaml
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.rmg import RMGDatabase
import rmgpy.data.rmg as rmg_data_module
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.kinetics import EEDFChannel
from rmgpy.kinetics import Arrhenius
from rmgpy.rmg.model import CoreEdgeReactionModel

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'input'
SOURCE = os.environ.get('EEDF_N2_LXCAT_SOURCE')
sys.path.insert(0, str(ROOT / 'scripts'))
import gen_nitrogen_channel_map as generator  # noqa: E402


def test_committed_map_and_complete_channel_inventory():
    """Portable assertions: the committed map and its owners need no LXCat file."""
    frozen = yaml.safe_load(
        (DATA / 'eedf/nitrogen_channel_map.yaml').read_text())
    assert frozen['class_counts'] == {'A': 12, 'B': 14, 'C': 0, 'D': 0}
    assert len(frozen['channels']) == 26
    assert len({row['process'] for row in frozen['channels']}) == 26
    assert all(row['reason'] for row in frozen['channels'])
    class_a = [row for row in frozen['channels'] if row['class'] == 'A']
    assert len(class_a) == 12
    assert all(row['owner_index'] and row['owner_library']
               == 'PlasmaNitrogen' for row in class_a)
    assert all(row['owner_index']
               is None for row in frozen['channels'] if row['class'] != 'A')


@pytest.mark.skipif(not SOURCE,
                    reason='set EEDF_N2_LXCAT_SOURCE for source regeneration')
def test_generator_regenerates_from_opt_in_source():
    subprocess.run(
        [sys.executable, str(ROOT / 'scripts/gen_nitrogen_channel_map.py'),
         '--source', SOURCE, '--check'], check=True, cwd=ROOT
    )


def _synthetic_overlay_files(tmp_path, owner_overrides=None, duplicate=False):
    frozen = yaml.safe_load(
        (DATA / 'eedf/nitrogen_channel_map.yaml').read_text())
    owner = next(row for row in frozen['channels'] if row['class'] == 'A')
    channel = {key: owner[key] for key in (
        'id', 'process', 'threshold_eV', 'class', 'owner_index',
        'owner_library', 'owner_label', 'reason')}
    channel.update(owner_overrides or {})
    source = tmp_path / 'source.txt'
    source.write_text('Excitation\nheader\n5.0\nPROCESS: test process\n')
    overlay = tmp_path / 'overlay.yaml'
    payload = {
        'schema': 'eedf-channel-overlay/1',
        'collision_set': 'synthetic-test-set',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'channels': [{**channel, 'id': 1, 'process': 'test process',
                      'threshold_eV': 5.0}],
    }
    text = yaml.safe_dump(payload, sort_keys=False)
    if duplicate:
        text = text.replace('schema: eedf-channel-overlay/1\n',
                            'schema: eedf-channel-overlay/1\nschema: duplicate\n')
    overlay.write_text(text)
    return source, overlay


@pytest.mark.parametrize(('field', 'value'), [
    ('owner_index', True), ('owner_library', ''), ('owner_label', ''),
])
def test_generator_rejects_malformed_class_a_owner_metadata(
        tmp_path, field, value):
    source, overlay = _synthetic_overlay_files(
        tmp_path, {field: value})
    with pytest.raises(ValueError, match='class A requires'):
        generator.generate(source, overlay)


def test_generator_rejects_owner_that_does_not_load_as_named_entry(tmp_path):
    source, overlay = _synthetic_overlay_files(
        tmp_path, {'owner_label': 'not-the-library-label'})
    with pytest.raises(ValueError, match='does not load as label'):
        generator.generate(source, overlay)


def test_generator_rejects_duplicate_yaml_keys(tmp_path):
    source, overlay = _synthetic_overlay_files(tmp_path, duplicate=True)
    with pytest.raises(yaml.YAMLError, match='duplicate key'):
        generator.generate(source, overlay)


def test_every_class_a_row_loads_with_exact_edf_metadata():
    db = KineticsDatabase()
    db.load_libraries(str(DATA / 'kinetics/libraries'),
                      libraries=['PlasmaAir', 'PlasmaNitrogen'])
    library = db.libraries['PlasmaNitrogen']
    frozen = yaml.safe_load(
        (DATA / 'eedf/nitrogen_channel_map.yaml').read_text())
    class_a = [row for row in frozen['channels'] if row['class'] == 'A']
    assert set(library.entries) == {row['owner_index'] for row in class_a}
    for row in class_a:
        entry = library.entries[row['owner_index']]
        assert isinstance(entry.data, EEDFChannel)
        assert entry.data.process == row['process']
        assert entry.data.collision_set == frozen['set']
        assert entry.data.side == 'ine'
        assert not entry.item.reversible
        process = row['process']
        if 'N2+(B)' in process:
            product_label, expected_state = 'N2pB', '2Sigma_u+'
        elif 'A3Su+' in process:
            product_label, expected_state = 'N2A', '3Sigma_u+'
        elif any(token in process for token in
                 ('(B3Pg)', '(W3Du)', '(B3Su-)')):
            product_label, expected_state = 'N2B', '3Pi_g'
        elif '(C3Pu)' in process:
            product_label, expected_state = 'N2C', '3Pi_u'
        elif '(a1Su-)' in process:
            product_label, expected_state = 'N2ap', '1Sigma_u-'
        elif '(a1Pg)' in process:
            product_label, expected_state = 'N2a', '1Pi_g'
        elif '(w1Du)' in process:
            product_label, expected_state = 'N2w', '1Delta_u'
        elif 'N2+(X)' in process:
            product_label, expected_state = 'N2p', None
        else:
            raise AssertionError(f'unexpected class-A process {process}')
        products = [species for species in entry.item.products
                    if species.label == product_label]
        assert len(products) == 1
        if expected_state is not None:
            assert products[0].molecule[0].electronic_state == expected_state


def test_fate_sources_and_named_absences_are_explicit():
    fates = yaml.safe_load((DATA / 'eedf/nitrogen_fates.yaml').read_text())
    absences = yaml.safe_load(
        (DATA / 'eedf/nitrogen_absences.yaml').read_text())
    assert {row['id'] for row in fates['radiative']} >= {
        'N2-C-to-B', 'N2-B-to-A', 'N2-a-to-X', 'N2-a-to-aprime', 'N2-w-to-a'}
    assert {row['id'] for row in fates['collisional']} >= {
        'N2-B-N2-to-A', 'N2-B-N2-to-X', 'N2-aprime-N2-to-B'}
    assert {row['id'] for row in fates['argon_quenching']} == {
        'Ar1s5-N2-total-quenching', 'Ar1s3-N2-total-quenching'}
    all_fates = (fates['radiative'] + fates['collisional']
                 + fates['argon_quenching'])
    assert all(row.get('source_table') for row in all_fates)
    assert all(row.get('blocks') for row in absences['absences'])
    w_to_b = next(row for row in fates['radiative']
                  if row['id'] == 'N2-W-to-B')
    assert w_to_b['value'] is None
    w_absence = next(row for row in absences['absences']
                     if row['id'] == 'N2-W-rapid-lumping-timescale')
    assert 'timescale' in w_absence['reason']
    assert any('Piper' in citation for citation in absences['download_list'])


def test_sample_owners_admit_with_real_thermo_and_arrhenius_rates():
    """Exercise CoreEdge admission while preserving real state thermo.

    EEDFChannel stores cross-section ownership metadata, not a rate expression.
    Use an Arrhenius rate stand-in only on deep copies for this engine admission
    check; the library-loaded owner entries remain EEDFChannel instances.
    """
    previous = rmg_data_module.database
    hub = RMGDatabase()
    hub.thermo = ThermoDatabase()
    hub.thermo.load_libraries(
        str(DATA / 'thermo/libraries'),
        ['primaryThermoLibrary', 'PlasmaExcitedNeutralThermo',
         'PlasmaThermo', 'electrocatThermo'])
    rmg_data_module.database = hub
    try:
        db = KineticsDatabase()
        db.load_libraries(str(DATA / 'kinetics/libraries'),
                          libraries=['PlasmaAir', 'PlasmaNitrogen'])
        hub.kinetics = db
        library = db.libraries['PlasmaNitrogen']
        model = CoreEdgeReactionModel()
        admitted = []
        expected_rates = {1: 123.0, 3: 456.0, 12: 789.0}
        for index, rate in expected_rates.items():
            loaded = next(reaction for reaction in library.get_library_reactions()
                          if reaction.entry.index == index)
            reaction = deepcopy(loaded)
            # Plain ground N2 intentionally has no vibrationallevel tag.
            for species in reaction.reactants + reaction.products:
                if species.is_electron():
                    continue
                species.thermo = hub.thermo.get_thermo_data_from_libraries(
                    species)[0]
            reaction.kinetics = Arrhenius(
                A=(rate, 'm^3/(mol*s)'),
                n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K'))
            result, is_new = model.make_new_reaction(
                reaction, generate_thermo=False, generate_kinetics=True)
            assert is_new
            admitted.append(result)
            assert result.kinetics.get_rate_coefficient(300.0) == pytest.approx(
                rate, rel=0, abs=0)
        assert len(admitted) == len(expected_rates)
        assert len(model.new_reaction_list) == len(expected_rates)
        assert all(species.thermo is not None for reaction in admitted
                   for species in reaction.reactants + reaction.products
                   if not species.is_electron())
        assert all(any(s.label == 'N2' and
                       not s.molecule[0].props.get('vibrationallevel')
                       for s in r.reactants + r.products)
                   for r in admitted)
    finally:
        rmg_data_module.database = previous
