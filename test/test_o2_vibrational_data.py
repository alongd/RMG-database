"""O2 threshold coverage, fixed-level thermo, and the real coupling adapter."""
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

import pytest

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / 'input/eedf/o2_vibrational'
COMPANION = Path(os.environ['RMG_PY_O2_SOURCE']) if os.environ.get('RMG_PY_O2_SOURCE') else None


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _manifest():
    return json.loads((DATA / 'sources.json').read_bytes())


def test_every_upward_ist_pair_is_present_and_both_label_spellings_parse():
    root = Path(os.environ['EEDF_DATA_ROOT'])
    record = _manifest()
    source = record['sources'][0]
    raw = root / source['path']
    assert hashlib.sha256(raw.read_bytes()).hexdigest() == source['sha256']
    assert COMPANION is not None, 'set RMG_PY_O2_SOURCE to the companion checkout'
    generator = _module('o2_test_generator', COMPANION / 'rmgpy/tools/eedf/n2_vibrational.py')
    pin = {'source_id': source['source_id'], 'path': str(raw), 'sha256': source['sha256'],
           'citation': source['citation'], 'provenance': 'sourced'}
    sections = generator.read_cross_sections(pin, molecule='O2')
    observed = {(section['initial_v'], section['final_v']) for section in sections}
    expected = {(v, w) for v in range(41) for w in range(v + 1, 42)}
    assert observed == expected
    assert len(observed) == 861
    assert {(7, 18), (7, 19)} <= observed
    assert source['process_count'] == source['selected_process_count'] == 861


def test_o2_adapter_accepts_the_real_k10_ladder_and_plain_ground_species():
    root = Path(os.environ['EEDF_DATA_ROOT'])
    assert COMPANION is not None, 'set RMG_PY_O2_SOURCE to the companion checkout'
    checker = _module('o2_test_checker', REPO / 'scripts/check_o2_vibrational_data.py')
    generator = checker._generator()
    resolved = checker.resolve_generator_manifest(root)
    expected_digest = json.loads((DATA / 'ladder_k10.sha256.json').read_bytes())['sha256']
    assert checker.artifact_digest(root) == expected_digest
    # The adapter validates the runtime D6 gate; these explicit test limits
    # exercise that contract without asserting owner production thresholds.
    resolved['D6'].update(top_fraction_limit=1.0, top_leak_share_limit=1.0)
    output = generator.generate(resolved, 10, False, molecule='O2')
    manifest = json.loads(output['manifest.json'])
    audit = manifest['transition_audit']
    source_hash = resolved['cross_sections'][0]['sha256']
    bindings = [{'source_sha256': source_hash, 'source_block': pair['source_block'],
                 'description': f"e + O2(X,v={pair['initial_v']}) <-> e + O2(X,v={pair['final_v']}), Vibrational"}
                for pair in audit]
    vibrational_path = COMPANION / 'rmgpy/tools/eedf/vibrational.py'
    adapter = _module('rmgpy.tools.eedf.vibrational', vibrational_path)
    ladder = adapter.ladder_coupling(manifest, bindings, axis='o2_v', parent='O2(X)')
    adapter.validate_ladders([ladder])
    assert len(ladder['channels']) == 861
    assert 'vibrationallevel' not in manifest['states'][0]['adjacency_list']
    assert manifest['states'][0]['label'] == 'O2'
    assert manifest['states'][1]['label'] == 'O2v1'
    from rmgpy.molecule.molecule import Molecule
    from rmgpy.species import Species
    species = [Species(label=state['label'], molecule=[Molecule().from_adjacency_list(
        state['adjacency_list'])]) for state in manifest['states']]
    assert adapter.resolve_levels(ladder, species) == tuple(range(11))


def test_nist_dunham_comparison_is_recorded_with_signed_threshold_residuals():
    levels = json.loads((DATA / 'levels.json').read_bytes())
    rows = levels['provenance']['independent_check']['comparison']
    assert len(rows) == 42
    assert all(row['threshold_minus_term_eV'] == pytest.approx(
        row['ist_threshold_eV'] - row['nist_dunham_eV'], abs=1e-15) for row in rows)
    worst = max(rows, key=lambda row: abs(row['threshold_minus_term_eV']))
    assert worst['v'] == 41
    assert worst['threshold_minus_term_eV'] == pytest.approx(-0.90096039218, abs=1e-10)


def test_fixed_level_thermo_preserves_energy_offsets_and_heat_capacity():
    from rmgpy.data.thermo import ThermoDatabase, ThermoLibrary
    from rmgpy import constants

    library = ThermoLibrary(label='O2Vibrational')
    library.load(str(REPO / 'input/thermo/libraries/O2Vibrational.py'),
                 ThermoDatabase().local_context, {})
    terms = json.loads((DATA / 'levels.json').read_bytes())['levels']
    data = [library.entries[f'O2v{v}'].data for v in range(11)]
    primary = ThermoLibrary(label='primaryThermoLibrary')
    primary.load(str(REPO / 'input/thermo/libraries/primaryThermoLibrary.py'),
                 ThermoDatabase().local_context, {})
    ground = primary.entries['O2'].data
    ev_mol = constants.Na * constants.e
    energies = [level['energy_eV'] * ev_mol for level in terms]
    gas_constant = constants.R
    for temperature in (300, 500, 1000, 1500):
        weights = [math.exp(-energy / (gas_constant * temperature)) for energy in energies]
        partition = sum(weights)
        mean = sum(e * w for e, w in zip(energies, weights)) / partition
        variance = sum((e - mean) ** 2 * w for e, w in zip(energies, weights)) / partition
        cvib = variance / (gas_constant * temperature ** 2)
        assert data[0].get_heat_capacity(temperature) == pytest.approx(
            ground.get_heat_capacity(temperature) - cvib, abs=2e-9)
    weights_298 = [math.exp(-energy / (gas_constant * 298)) for energy in energies]
    q_298 = sum(weights_298)
    h_vib_298 = sum(e * w for e, w in zip(energies, weights_298)) / q_298
    s_vib_298 = gas_constant * math.log(q_298) + h_vib_298 / 298
    assert data[0].get_enthalpy(298) == pytest.approx(
        ground.get_enthalpy(298) - h_vib_298, abs=2e-7)
    assert data[0].get_entropy(298) == pytest.approx(
        ground.get_entropy(298) - s_vib_298, abs=2e-9)
    for temperature in (300, 500, 1000, 2500, 4000, 6000):
        for v in range(11):
            assert data[v].get_heat_capacity(temperature) == pytest.approx(
                data[0].get_heat_capacity(temperature), abs=1e-12)
            assert data[v].get_enthalpy(temperature) - data[0].get_enthalpy(temperature) == pytest.approx(
                terms[v]['energy_eV'] * ev_mol, abs=2e-7)
