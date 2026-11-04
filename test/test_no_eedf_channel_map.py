"""Source fidelity, owner identities and deterministic generation for the NO converter map."""

import ast
import hashlib
import json
import os
from pathlib import Path
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
ARCHIVE = os.environ.get('EEDF_NO_HAYASHI', '/home/alon/Data/lxcat/incoming/Hayashi.zip')
STORE = os.environ.get('EEDF_LXCAT_ASSEMBLED')
needs_store = pytest.mark.skipif(not (STORE and Path(STORE).is_dir()),
                                 reason='NO assembled store is unset (EEDF_LXCAT_ASSEMBLED)')
needs_archive = pytest.mark.skipif(not Path(ARCHIVE).is_file(), reason='local Hayashi archive is unavailable')


@pytest.fixture(scope='module')
def doc():
    return yaml.safe_load(MAP.read_text())


def test_map_is_converter_schema_two_and_inventory_is_classified_once(doc):
    assert doc['schema'] == 'eedf-channel-map/2'
    assert doc['states'] == {'NO(X)': {
        'paschen': 'ground', 'g': 4, 'excitation_eV': 0.0, 'rmg_species': 'NO',
        'source': no.NO_GROUND_STATE_SOURCE}}
    assert 'X $^2\\Pi$' in no.NO_GROUND_STATE_SOURCE
    assert 'g=(2S+1)(2Λ+1)=4' in no.NO_GROUND_STATE_SOURCE
    channels = doc['channels']
    assert len(channels) == 10
    assert [channel['id'] for channel in channels] == list(range(1, 11))
    assert len({channel['source']['block'] for channel in channels}) == 10
    assert doc['class_counts'] == {'A': 2, 'B': 8, 'C': 0, 'D': 0}
    assert len({channel['loki_process'] for channel in channels}) == 10
    overlay, _, problems = gen.load_overlay_document(OVERLAY)
    assert not problems
    assert set(overlay) == {channel['loki_process'] for channel in channels}
    assert all(overlay[c['loki_process']]['class'] == c['class'] for c in channels)


def test_v1_v5_keep_ownerless_energy_loss_to_one_no_specific_heating_group(doc):
    channels = [c for c in doc['channels'] if c.get('group') in {'V1', 'V2', 'V3', 'V4', 'V5'}]
    assert {c['group']: c['threshold_eV'] for c in channels} == {
        'V1': 0.232, 'V2': 0.455, 'V3': 0.677, 'V4': 0.896, 'V5': 1.11}
    assert {c['flux_group'] for c in channels} == {'NO_lumped_vibrational_heating'}
    for channel in channels:
        assert channel['class'] == 'B' and channel['rmg'] is None
        assert channel['energy_sink'] == 'gas_heating'
        assert channel['energy_loss_eV'] == channel['threshold_eV']
        assert 'lumped' in channel['reason'] and 'Report-10' in channel['reason']
        assert 'NO has no vibrational populations' in channel['reason']
        assert 'V-T relaxation is fast relative to the residence time' in channel['reason']
    convention, = [c for c in doc['declared_conventions'] if c['name'] == 'LUMPED_VIBRATIONAL_GAS_HEATING']
    assert convention['applies_to'] == [c['id'] for c in channels]


def test_electronic_channels_and_effective_channel_keep_inventory_classifications(doc):
    electronic = [c for c in doc['channels'] if c.get('group') in {'e1', 'e2'}]
    assert {c['group']: c['threshold_eV'] for c in electronic} == {'e1': 5.45, 'e2': 6.58}
    for channel in electronic:
        assert channel['class'] == 'B' and channel['rmg'] is None
        assert channel['energy_sink'] == 'ownerless_electronic_energy'
        assert 'no sourced NO electronic species' in channel['reason']
    effective, = [c for c in doc['channels'] if c['kind'] == 'EFFECTIVE']
    assert effective['class'] == 'B' and effective['threshold_eV'] == 0.0
    assert effective['energy_sink'] == 'effective_momentum_transfer'
    assert effective['energy_loss_eV'] is None


def test_attachment_and_ionization_have_exact_species_and_resolved_owners(doc):
    attachment, = [c for c in doc['channels'] if c['kind'] == 'ATTACHMENT']
    ionization, = [c for c in doc['channels'] if c['kind'] == 'IONIZATION']
    assert attachment['loki_process'] == 'e + NO(X) -> N(4S) + O(-,gnd), Attachment'
    assert attachment['rmg']['reaction'] == 'NO + e- => N + O-'
    assert attachment['rmg']['library'] == 'PlasmaNitricOxide'
    assert attachment['rmg']['status'] == 'present' and attachment['rmg']['index'] == 1
    assert attachment['threshold_eV'] == attachment['energy_loss_eV'] == 0.0
    assert attachment['comment_onset_eV'] == 6.6
    assert 'PM-approved' in no.ATTACHMENT_RULING
    assert ionization['loki_process'] == 'e + NO(X) -> e + e + NO(+,gnd), Ionization'
    assert ionization['rmg']['reaction'] == 'NO + e- => NOp + e- + e-'
    assert ionization['rmg']['library'] == 'PlasmaNitricOxide'
    assert ionization['rmg']['status'] == 'present' and ionization['rmg']['index'] == 2
    assert ionization['threshold_eV'] == 9.26
    for label in ('NO', 'NOp', 'N', 'O-', 'e-'):
        assert doc['species'][label]['libraries'] == ['PlasmaNitricOxide']


def test_plasmanitricoxide_resolves_species_and_exact_solver_markers():
    reactions, species, problems = gen.load_library(ROOT / 'input', 'PlasmaNitricOxide')
    assert not problems
    assert set(species) == {'NO', 'N', 'O-', 'NOp', 'e-'}
    assert reactions[1].label == 'NO + e- => N + O-'
    assert reactions[1].eedf_process == 'e + NO(X) -> N(4S) + O(-,gnd), Attachment'
    assert reactions[1].eedf_collision_set == 'no-hayashi-v1'
    assert reactions[1].has_eedf_marker
    assert reactions[2].label == 'NO + e- => NOp + e- + e-'
    assert reactions[2].eedf_process == 'e + NO(X) -> e + e + NO(+,gnd), Ionization'
    assert reactions[2].eedf_collision_set == 'no-hayashi-v1'
    assert reactions[2].has_eedf_marker


def test_no_other_plasma_library_has_an_overlapping_no_electron_owner():
    owners = {'NO + e- => N + O-', 'NO + e- => NOp + e- + e-'}
    overlaps = []
    for path in sorted((ROOT / 'input/kinetics/libraries').glob('Plasma*/reactions.py')):
        if path.parent.name == 'PlasmaNitricOxide':
            continue
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name) or node.func.id != 'entry':
                continue
            label = next((kw.value.value for kw in node.keywords if kw.arg == 'label'
                          and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str)), None)
            if label in owners:
                overlaps.append(f'{path.parent.name}: {label}')
    assert not overlaps, 'NO + e- owner overlap would double-count when both libraries load: ' + repr(overlaps)


def test_argon_and_nitrogen_maps_remain_byte_identical_to_dispatch_base():
    for relative in ('input/eedf/argon_channel_map.yaml', 'input/eedf/nitrogen_channel_map.yaml'):
        committed = subprocess.run(['git', 'show', '278793a06:' + relative], cwd=ROOT,
                                   check=True, capture_output=True).stdout
        assert (ROOT / relative).read_bytes() == committed


@needs_archive
@needs_store
def test_source_hashes_thresholds_and_full_regeneration_match_bytes(doc):
    with zipfile.ZipFile(ARCHIVE) as archive:
        source = archive.read(no.MEMBER)
    source_channels, _ = no.source_channels(source)
    assert [channel['id'] for channel in source_channels] == [c['id'] for c in doc['channels']]
    for source_channel, map_channel in zip(source_channels, doc['channels']):
        assert source_channel['source']['block'] == map_channel['source']['block']
        assert source_channel['source']['line'] == map_channel['source']['line']
        assert source_channel['source']['block_sha256'] == map_channel['source']['block_sha256']
        if source_channel['kind'] == 'ATTACHMENT':
            assert map_channel['threshold_eV'] == source_channel['energy_loss_eV'] == 0.0
        elif source_channel['kind'] == 'EFFECTIVE':
            assert map_channel['threshold_eV'] == 0.0
        else:
            assert map_channel['threshold_eV'] == source_channel['threshold_eV']
    regenerated, problems, _, labels = no.generate(OVERLAY, ARCHIVE, STORE, ROOT / 'input')
    assert not problems
    assert len(labels) == 10
    assert regenerated.encode() == MAP.read_bytes()


@needs_archive
@needs_store
def test_no_map_cli_check_is_byte_exact_and_non_mutating(tmp_path):
    output = tmp_path / 'map.yaml'
    args = [sys.executable, str(ROOT / 'scripts/gen_eedf_channel_map.py'), '--gas', 'no',
            '--overlay', str(OVERLAY), '--source', ARCHIVE, '--assembled', STORE,
            '--database', str(ROOT / 'input'), '--output', str(output)]
    result = subprocess.run(args, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert output.read_bytes() == MAP.read_bytes()
    original = output.read_bytes()
    result = subprocess.run(args + ['--check'], capture_output=True, text=True)
    assert result.returncode == 0 and 'PASS (byte equality)' in result.stdout
    assert output.read_bytes() == original


@needs_archive
@needs_store
def test_assembled_named_missing_or_malformed_store_refuses_map_generation(tmp_path):
    output = tmp_path / 'out.yaml'
    args = [sys.executable, str(ROOT / 'scripts/gen_eedf_channel_map.py'), '--gas', 'no',
            '--overlay', str(OVERLAY), '--source', ARCHIVE, '--assembled', str(tmp_path / 'missing'),
            '--database', str(ROOT / 'input'), '--output', str(output)]
    result = subprocess.run(args, capture_output=True, text=True)
    assert result.returncode == 1 and 'not a directory' in result.stdout
    assert not output.exists()
