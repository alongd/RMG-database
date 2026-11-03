"""Frozen NO metadata and refusals; local archive is opt-in and never enters git.

Set EEDF_NO_HAYASHI to the local Hayashi.zip to run regeneration and CLI checks.
Use the built plasma RMG-Py on PYTHONPATH for species identity and library loading.
"""

import copy
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import gen_eedf_channel_map as gen  # noqa: E402
import gen_no_eedf_channel_map as no  # noqa: E402

MAP = ROOT / 'input/eedf/no_channel_map.yaml'
OVERLAY = ROOT / 'input/eedf/no_channel_overlay.yaml'
ARCHIVE = os.environ.get('EEDF_NO_HAYASHI')
needs_source = pytest.mark.skipif(not ARCHIVE, reason='set EEDF_NO_HAYASHI to the local Hayashi.zip')


@pytest.fixture(scope='module')
def doc():
    return yaml.safe_load(MAP.read_text())


@pytest.fixture(scope='module')
def source():
    with zipfile.ZipFile(ARCHIVE) as z:
        return z.read(no.MEMBER)


def test_committed_map_matches_overlay_and_has_ten_unique_channels(doc):
    overlay, _, problems = gen.load_overlay_document(OVERLAY)
    assert not problems
    assert len(doc['channels']) == len(overlay) == 10
    assert len({c['source_process'] for c in doc['channels']}) == 10
    assert {c['source_process'] for c in doc['channels']} == set(overlay)
    for c in doc['channels']:
        entry = overlay[c['source_process']]
        assert c['class'] == entry['class']
        assert c.get('rmg', {}).get('reaction') == entry['reaction']
    assert doc['class_counts'] == {'A': 2, 'B': 8, 'C': 0, 'D': 0}


def test_v_groups_have_no_populations_and_all_loss_goes_to_heating(doc):
    channels = [c for c in doc['channels'] if c['family'] == 'lumped vibrational']
    assert {c['group']: c['threshold_eV'] for c in channels} == {
        'V1': 0.232, 'V2': 0.455, 'V3': 0.677, 'V4': 0.896, 'V5': 1.11}
    for c in channels:
        assert c['class'] == 'B' and c['owner'] is None and 'rmg' not in c
        assert c['energy_loss_eV'] == c['threshold_eV']
        assert c['energy_sink'] == 'gas_heating'
        for phrase in ('lumped', 'Report-10', 'no vibrational populations', 'V-T', 'residence time'):
            assert phrase in c['reason']
    convention = next(c for c in doc['declared_conventions'] if c['name'] == 'LUMPED_VIBRATIONAL_GAS_HEATING')
    assert convention['applies_to'] == [c['id'] for c in channels]


def test_electronic_channels_are_ownerless_and_effective_is_distinct(doc):
    electronic = [c for c in doc['channels'] if c['family'] == 'electronic excitation']
    assert {c['group']: c['threshold_eV'] for c in electronic} == {'e1': 5.45, 'e2': 6.58}
    for c in electronic:
        assert c['class'] == 'B' and c['owner'] is None and 'rmg' not in c
        assert 'no sourced NO electronic species' in c['reason']
        assert c['energy_sink'] == 'ownerless_electronic_energy'
    effective, = [c for c in doc['channels'] if c['kind'] == 'EFFECTIVE']
    assert effective['threshold_eV'] is None
    assert effective['mass_ratio'] == 0.0000182694
    assert 'energy_loss_eV' not in effective
    assert effective['energy_sink'] == 'effective_momentum_transfer'


def test_attachment_is_dissociative_and_param_is_not_a_threshold(doc):
    c, = [c for c in doc['channels'] if c['kind'] == 'ATTACHMENT']
    assert c['energy_loss_eV'] == 0 and c['threshold_eV'] is None
    assert c['comment_onset_eV'] == 6.6
    assert c['source_comment'] == 'Threshold 6.6eV.'
    assert c['physical_products'] == ['N', 'O-']
    assert c['rmg']['reaction'] == 'NO + e- => N + O-'
    assert c['rmg']['species']['O-'] == ['PlasmaAir', 'PlasmaOxygenHeavy']
    assert c['rmg']['status'] == 'absent' and c['rmg']['matches'] == []
    assert 'PM-approved' in c['product_interpretation']
    assert 'does not identify the physical products' in c['product_interpretation']
    assert 'NO-' not in c['rmg']['species']


def test_ionization_has_species_but_no_reaction_owner(doc):
    c, = [c for c in doc['channels'] if c['kind'] == 'IONIZATION']
    assert c['threshold_eV'] == 9.26
    assert c['rmg']['reaction'] == 'NO + e- => NOp + e- + e-'
    assert c['rmg']['species']['NOp'] == ['PlasmaAir']
    assert c['rmg']['status'] == 'absent' and c['rmg']['matches'] == []


@needs_source
def test_source_metadata_thresholds_and_full_regeneration(source, doc):
    # Independently read source PARAM fields and line offsets rather than trust the generator's output.
    lines = source.decode().splitlines()
    for c in doc['channels']:
        start = c['source']['line'] - 1
        assert lines[start] == c['kind']
        block = lines[start:start + 9]
        assert 'PROCESS: ' + c['source_process'] in block
        param, = [s for s in block if s.startswith('PARAM.:')]
        if c['kind'] == 'EFFECTIVE':
            assert float(param.split('m/M = ')[1].split(',')[0]) == c['mass_ratio']
        else:
            assert float(param.split('E = ')[1].split(' eV')[0]) == c['energy_loss_eV']
    attribution, = doc['sources'].values()
    assert hashlib.sha256(Path(ARCHIVE).read_bytes()).hexdigest() == attribution['sha256']
    assert hashlib.sha256(source).hexdigest() == attribution['member_sha256']
    text, problems, _, labels = no.generate(OVERLAY, ARCHIVE, ROOT / 'input')
    assert not problems and len(labels) == 10
    assert text.encode() == MAP.read_bytes()


def cli(output, *args):
    return subprocess.run([sys.executable, str(ROOT / 'scripts/gen_eedf_channel_map.py'), '--gas', 'no',
                           '--overlay', str(OVERLAY), '--source', ARCHIVE, '--output', str(output), *args],
                          capture_output=True, text=True)


@needs_source
def test_check_is_byte_exact_and_does_not_write(tmp_path):
    assert cli(MAP, '--check').returncode == 0
    output = tmp_path / 'map.yaml'
    assert cli(output).returncode == 0
    assert output.read_bytes() == MAP.read_bytes()
    changed = output.read_bytes().replace(b'gas_heating', b'wrong_sink', 1)
    output.write_bytes(changed)
    result = cli(output, '--check')
    assert result.returncode == 1 and 'differs from its regeneration' in result.stdout
    assert output.read_bytes() == changed
    missing = tmp_path / 'missing.yaml'
    assert cli(missing, '--check').returncode == 1 and not missing.exists()


@needs_source
@pytest.mark.parametrize('mutation', ['missing', 'extra', 'duplicate', 'wrong_class', 'wrong_reaction'])
def test_overlay_mutations_are_refused_without_writing(tmp_path, mutation):
    overlay = yaml.safe_load(OVERLAY.read_text())
    label = next(iter(overlay['collisions']))
    if mutation == 'missing':
        del overlay['collisions'][label]
    elif mutation == 'extra':
        overlay['collisions']['unknown NO process'] = {'class': 'B'}
    elif mutation == 'wrong_class':
        overlay['collisions'][label]['class'] = 'B'
    elif mutation == 'wrong_reaction':
        overlay['collisions'][label]['reaction'] = 'NO + e- => NO-'
    path = tmp_path / 'overlay.yaml'
    text = yaml.safe_dump(overlay, sort_keys=False)
    if mutation == 'duplicate':
        text += '  ' + repr(label) + ': {class: A}\n'
    path.write_text(text)
    output = tmp_path / 'output.yaml'
    output.write_text('keep existing artifact\n')
    result = cli(output, '--overlay', str(path))
    assert result.returncode == 1 and 'RESULT: FAIL' in result.stdout
    assert result.stderr == ''
    expected = {'missing': 'coverage differs', 'extra': 'coverage differs', 'duplicate': 'appears twice',
                'wrong_class': 'disagrees with NO policy', 'wrong_reaction': 'disagrees with NO policy'}
    assert expected[mutation] in result.stdout
    assert output.read_text() == 'keep existing artifact\n'


@needs_source
@pytest.mark.parametrize('mutation', ['threshold', 'duplicate_block', 'missing_block', 'unknown_state',
                                     'no_onset', 'wrong_process'])
def test_source_inconsistencies_are_refused(source, mutation):
    text = source.decode().replace('\r\n', '\n')
    if mutation == 'threshold':
        text = text.replace('E = 0.232 eV', 'E = 0.233 eV')
    elif mutation in ('duplicate_block', 'missing_block'):
        block = next(raw for _, _, raw in gen.blocks(text) if raw.startswith('EXCITATION\nNO -> NO(V1)'))
        text = text + '\n' + block if mutation == 'duplicate_block' else text.replace(block, '')
    elif mutation == 'unknown_state':
        text = text.replace('NO(V1)', 'NO(V6)')
    elif mutation == 'no_onset':
        text = text.replace('COMMENT: Threshold 6.6eV.', 'COMMENT: unspecified')
    else:
        text = text.replace('PROCESS: E + NO -> E + NO(V1)', 'PROCESS: E + NO -> E + NO(V2)')
    with pytest.raises(ValueError):
        no.source_channels(text.encode())


def test_named_species_are_checked_by_rmg_identity(tmp_path):
    database = tmp_path / 'input'
    for library in no.LIBRARIES:
        folder = Path('kinetics/libraries') / library
        shutil.copytree(ROOT / 'input' / folder, database / folder)
    _, references, problems = gen.load_overlay_document(OVERLAY)
    assert not problems
    libraries, owners = no.ownership(database, references)
    assert len(libraries) == 2 and owners['O-']['libraries'] == list(no.LIBRARIES)
    broken = copy.deepcopy(references)
    broken['O-'] = 'multiplicity 3\n1 O u2 p2 c0\n'
    with pytest.raises(ValueError, match='PlasmaAir/O-'):
        no.ownership(database, broken)


@needs_source
def test_new_owner_reaction_clears_the_named_absence(tmp_path):
    database = tmp_path / 'input'
    for library in no.LIBRARIES:
        folder = Path('kinetics/libraries') / library
        shutil.copytree(ROOT / 'input' / folder, database / folder)
    reactions = database / 'kinetics/libraries/PlasmaAir/reactions.py'
    with reactions.open('a') as out:
        out.write('''\nentry(
    index = 9999,
    label = "NO + e- => N + O-",
    reversible = False,
    kinetics = Arrhenius(A=(1.0, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol')),
)\n''')
    text, problems, _, _ = no.generate(OVERLAY, ARCHIVE, database)
    assert not problems and text.encode() != MAP.read_bytes()
    c, = [c for c in yaml.safe_load(text)['channels'] if c['kind'] == 'ATTACHMENT']
    assert c['rmg']['status'] == 'present'
    assert c['rmg']['matches'] == [{'library': 'PlasmaAir', 'index': 9999}]
    assert 'Named absence' not in c['reason'] and 'is present' in c['reason']
