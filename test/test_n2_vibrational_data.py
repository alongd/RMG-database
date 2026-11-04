"""Source and fixed-v thermo checks for the generated N2(X,v) database inputs."""
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import zipfile

import pytest
from rmgpy import constants


REPO = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPO / 'input/eedf/n2_vibrational'
LEVELS_PATH = SOURCE_DIR / 'levels.json'
SOURCES_PATH = SOURCE_DIR / 'sources.json'
THERMO_PATH = REPO / 'input/thermo/libraries/N2Vibrational.py'
R = constants.R
AVOGADRO_EV = constants.Na * constants.e


def _local_root():
    configured = os.environ.get('EEDF_DATA_ROOT')
    if not configured:
        pytest.skip('EEDF_DATA_ROOT unset; local LXCat source store unavailable')
    root = Path(configured).expanduser()
    if not root.is_dir():
        pytest.skip(f'EEDF_DATA_ROOT path absent at {root}; local LXCat source store unavailable')
    return root


def _load_check_module():
    script = REPO / 'scripts/check_n2_vibrational_data.py'
    spec = importlib.util.spec_from_file_location('n2_vibrational_data_check', script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _source_text(root, source):
    path = root / source['path']
    if source.get('member'):
        with zipfile.ZipFile(path) as archive:
            return archive.read(source['member']).decode('utf-8')
    return path.read_text(encoding='utf-8')


def _numeric_excitation_blocks(text):
    blocks = {}
    for raw in re.split(r'(?m)(?=^EXCITATION\s*$)', text):
        lines = raw.splitlines()
        if not lines or lines[0].strip() != 'EXCITATION':
            continue
        match = re.fullmatch(r'N2\(X,v=(\d+)\) -> N2\(X,v=(\d+)\)', lines[1].strip())
        if not match:
            continue
        pair = tuple(map(int, match.groups()))
        threshold = float(lines[2].split()[0])
        first_dash = next(i for i, line in enumerate(lines[3:], 3)
                          if re.fullmatch(r'-{5,}', line.strip()))
        numeric_rows = []
        for line in lines[first_dash + 1:]:
            if re.fullmatch(r'-{5,}', line.strip()):
                break
            if line.strip():
                numeric_rows.append(tuple(map(float, line.split())))
        blocks[pair] = (threshold, tuple(numeric_rows))
    return blocks


def _vibrational_partition(energies_eV, temperature):
    energies = [energy * AVOGADRO_EV for energy in energies_eV]
    weights = [math.exp(-energy / (R * temperature)) for energy in energies]
    q = sum(weights)
    mean = sum(e * w for e, w in zip(energies, weights)) / q
    variance = sum((e - mean) ** 2 * w for e, w in zip(energies, weights)) / q
    return variance / (R * temperature ** 2), mean, R * math.log(q) + mean / temperature


def test_source_manifest_hashes_coverage_and_v3_overlap():
    root = _local_root()
    record = json.loads(SOURCES_PATH.read_bytes())
    assert record['source_domain'] == {'initial_levels': list(range(30)), 'final_v': 58}
    assert record['uncovered_initial_levels'] == list(range(30, 59))
    assert record['dissociation_absence'] == {
        'name': 'resonant e-V dissociation: not in the source set', 'channel_emitted': False}
    for source in record['sources']:
        path = root / source['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256']

    batch1, batch2 = record['sources']
    v3_batch1 = {pair: values for pair, values in _numeric_excitation_blocks(_source_text(root, batch1)).items()
                 if pair[0] == 3}
    v3_batch2 = {pair: values for pair, values in _numeric_excitation_blocks(_source_text(root, batch2)).items()
                 if pair[0] == 3}
    assert len(v3_batch1) == 36
    assert len(v3_batch2) == 56
    assert v3_batch1.keys() <= v3_batch2.keys()
    assert all(v3_batch1[pair] == v3_batch2[pair] for pair in v3_batch1)
    assert record['source_assignments']['3'] == 'laporta_batch2'

    checker = _load_check_module()
    resolved = checker.resolve_generator_manifest(root)
    from rmgpy.tools.eedf.n2_vibrational import read_cross_sections
    sections = [section for pin in resolved['cross_sections'] for section in read_cross_sections(pin)
                if resolved['source_assignments'].get(str(section['initial_v'])) == section['source']['source_id']]
    assert len(sections) == 1335


def test_recorded_energies_equal_laporta_ground_thresholds_exactly():
    root = _local_root()
    record = json.loads(LEVELS_PATH.read_bytes())
    checker = _load_check_module()
    resolved = checker.resolve_generator_manifest(root)
    from rmgpy.tools.eedf.n2_vibrational import read_cross_sections
    sections = [section for pin in resolved['cross_sections'] for section in read_cross_sections(pin)
                if pin['source_id'] == 'laporta_batch1']
    thresholds = {section['final_v']: section['threshold_eV'] for section in sections
                  if section['initial_v'] == 0}
    assert record['levels'][0]['energy_eV'] == 0.0
    assert set(thresholds) == set(range(59))
    for v, level in enumerate(record['levels']):
        assert level['v'] == v
        assert level['energy_eV'] == thresholds[v]
        assert level['statistical_weight'] == 1
        assert (level['thermo_entry'] == f'N2v{v}') is (v <= 30)
    comparison = record['provenance']['independent_check']['comparison']
    assert len(comparison) == 31
    assert max(abs(row['difference_laporta_minus_dunham_eV']) for row in comparison[1:21]) <= 0.001
    assert comparison[21]['difference_laporta_minus_dunham_eV'] == pytest.approx(-0.00176014667)
    assert record['provenance']['independent_check']['agreement_gate'] == (
        'agreement <= 0.001 eV for v<=21; larger high-v deviations attributed to Dunham truncation')


def test_fixed_v_thermo_invariants_and_nonvibrational_anchor():
    from rmgpy.data.thermo import ThermoDatabase, ThermoLibrary

    db = ThermoDatabase()
    primary = ThermoLibrary(label='primaryThermoLibrary')
    primary.load(str(REPO / 'input/thermo/libraries/primaryThermoLibrary.py'), db.local_context, {})
    ground = primary.entries['N2'].data
    fixed_library = ThermoLibrary(label='N2Vibrational')
    fixed_library.load(str(THERMO_PATH), db.local_context, {})
    levels = json.loads(LEVELS_PATH.read_bytes())['levels']
    fixed = [fixed_library.entries[f'N2v{v}'].data for v in range(31)]

    cp_nodes = [298,300,400,500,600,800,1000,1500,2000,2500,3000,3500,
                4000,4500,5000,5500,6000]
    for temperature in cp_nodes:
        cvib = _vibrational_partition([level['energy_eV'] for level in levels], temperature)[0]
        expected = ground.get_heat_capacity(temperature) - cvib
        assert fixed[0].get_heat_capacity(temperature) == pytest.approx(expected, abs=2e-9)

    cvib, hvib, svib = _vibrational_partition([level['energy_eV'] for level in levels], 298)
    assert fixed[0].get_enthalpy(298) == pytest.approx(ground.get_enthalpy(298) - hvib, abs=2e-7)
    assert fixed[0].get_entropy(298) == pytest.approx(ground.get_entropy(298) - svib, abs=2e-9)
    assert cvib > 0  # the removed contribution is the ensemble vibration term

    for temperature in [298, 298.15, 500, 1000, 2500, 4000, 6000]:
        for v, thermo in enumerate(fixed):
            assert thermo.get_heat_capacity(temperature) == pytest.approx(
                fixed[0].get_heat_capacity(temperature), abs=1e-12)
            assert thermo.get_enthalpy(temperature) - fixed[0].get_enthalpy(temperature) == pytest.approx(
                levels[v]['energy_eV'] * AVOGADRO_EV, abs=2e-7)
            assert thermo.get_entropy(temperature) == pytest.approx(fixed[0].get_entropy(temperature), abs=1e-12)


def test_fixed_v_library_rebuild_is_reproducible():
    generated = REPO / 'scripts/generate_n2_vibrational_thermo.py'
    import subprocess
    import sys
    result = subprocess.run([sys.executable, str(generated), '--check'], cwd=REPO,
                            capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    assert 'reproducible' in result.stdout


def test_real_generator_k10_k29_digest_and_k30_refusal():
    result = _load_check_module().check_ladder_inputs(_local_root())
    by_k = {item['K']: item for item in result['ladders']}
    assert set(by_k) == {10, 29}
    assert (by_k[10]['states'], by_k[10]['source_records'], by_k[10]['forward_channels'],
            by_k[10]['superelastic_channels'], by_k[10]['top_leak_records']) == (11,1335,594,55,528)
    assert (by_k[29]['states'], by_k[29]['source_records'], by_k[29]['forward_channels'],
            by_k[29]['superelastic_channels'], by_k[29]['top_leak_records']) == (30,1335,1335,435,870)
    assert all(item['runtime_ready'] is False for item in by_k.values())
    assert all(item['runtime_requirements'] == [
        'coupling automatically executes D6 regeneration before accepting a run',
        'physical Ar+N2 arm qualification requires complete channel maps and class-A owners in their configured per-gas libraries'] for item in by_k.values())
    assert 'uncovered initial v=30' in result['K30_refusal']
    repeated = _load_check_module().check_ladder_inputs(_local_root())
    assert [item['sha256'] for item in result['ladders']] == [item['sha256'] for item in repeated['ladders']]


def test_owner_d6_policy_is_pinned_in_source_manifest():
    expected = {
        'set_by': 'owner',
        'owner_decision': 'Owner decision 2026-11-04',
        'top_fraction_limit': 0.01,
        'top_leak_share_limit': 0.05,
        'K_step': 5,
    }
    record = json.loads(SOURCES_PATH.read_bytes())
    assert record['D6'] == expected


def test_checker_resolves_owner_d6_policy():
    root = _local_root()
    expected = json.loads(SOURCES_PATH.read_bytes())['D6']
    assert _load_check_module().resolve_generator_manifest(root)['D6'] == expected
