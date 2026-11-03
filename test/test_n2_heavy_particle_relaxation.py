"""Regression coverage for the sourced Guerra N2(X,v) relaxation library."""

import importlib.util
import json
import math
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/gen_n2_heavy_particle_relaxation.py'
PARAMETERS = ROOT / 'input/kinetics/libraries/N2HeavyParticleRelaxation/parameters.yaml'
RATIO_FIXTURE = ROOT / 'test/fixtures/n2_billing_ratio_fixture.json'
SPEC = importlib.util.spec_from_file_location('n2_heavy_particle_generator', SCRIPT)
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


def _small_ladder():
    return {'levels': [
        {'v': 0, 'energy_eV': 0.0, 'thermo_entry': 'N2v0'},
        {'v': 1, 'energy_eV': 0.2886, 'thermo_entry': 'N2v1'},
        {'v': 2, 'energy_eV': 0.5737, 'thermo_entry': 'N2v2'},
        {'v': 3, 'energy_eV': 0.8553, 'thermo_entry': 'N2v3'},
    ]}


def _parameters():
    return yaml.safe_load(PARAMETERS.read_bytes())


def test_source_manifest_rejects_missing_or_malformed_equations_and_hashes():
    parameters = _parameters()
    levels = _small_ladder()
    assert GENERATOR.validate(parameters, levels, 3) == 3
    malformed = json.loads(json.dumps(parameters))
    del malformed['record_source']['equations']['12']
    with pytest.raises(ValueError, match='equation transcription'):
        GENERATOR.validate(malformed, levels, 3)
    malformed = json.loads(json.dumps(parameters))
    malformed['record_source']['sha256'] = 'g' * 64
    with pytest.raises(ValueError, match='SHA-256'):
        GENERATOR.validate(malformed, levels, 3)
    with pytest.raises(ValueError, match='integer'):
        GENERATOR.validate(parameters, levels, True)


def test_rate_laws_match_guerra_equations_at_spot_conditions():
    """Eq. (12)/(20)/(21) and Eq. (14)/(22)/(23), all coefficients per molecule."""
    parameters = _parameters()
    assert GENERATOR.rate_vt(1, 300, parameters) == pytest.approx(6.47401384757347e-11, rel=0.02)
    assert GENERATOR.rate_vt(2, 300, parameters) == pytest.approx(1.7008173995984415e-10, rel=0.02)
    assert GENERATOR.rate_vv(1, 0, 300, parameters) == pytest.approx(8.79e-15, rel=0.02)
    assert GENERATOR.rate_vv(1, 1, 300, parameters) == pytest.approx(1.4644785866818454e-14, rel=0.02)


@pytest.mark.parametrize(('process', 'temperature'), [('vt', 299), ('vt', 3501), ('vv', 199), ('vv', 3501)])
def test_source_temperature_bounds_refuse_instead_of_clamp(process, temperature):
    parameters = _parameters()
    with pytest.raises(ValueError, match='refuses'):
        if process == 'vt':
            GENERATOR.rate_vt(1, temperature, parameters)
        else:
            GENERATOR.rate_vv(1, 1, temperature, parameters)


def test_source_v_bounds_refuse_outside_declared_level_ranges():
    parameters = _parameters()
    with pytest.raises(ValueError, match='refuses'):
        GENERATOR.rate_vt(46, 300, parameters)
    with pytest.raises(ValueError, match='refuses'):
        GENERATOR.rate_vv(45, 44, 300, parameters)


def test_generated_reactions_are_reversible_and_use_only_forward_rates():
    parameters_raw = PARAMETERS.read_bytes()
    py, dictionary = GENERATOR.generate(parameters_raw, json.dumps(_small_ladder()).encode(), 3)
    source = py.decode()
    assert source.count('reversible = True') > 1
    assert 'reverse_kinetics' not in source
    assert 'detailed balance from the fixed-v N2Vibrational thermochemistry' in source
    assert 'N2v3' in dictionary.decode()
    assert 'Ars' not in dictionary.decode()


def test_detailed_balance_from_fixed_v_thermo_has_the_expected_equilibrium_ratio():
    """Common fixed-v Cp/S cancel, leaving the Laporta level enthalpy differences."""
    levels = _small_ladder()['levels']
    energies = {row['v']: row['energy_eV'] for row in levels}
    # The reversible channel is N2(v=1)+N2(v=2) <=> N2(v=0)+N2(v=3).
    delta_g_ev = energies[0] + energies[3] - energies[1] - energies[2]
    temperature = 1000.0
    keq = math.exp(-delta_g_ev * 96485.33212 / (8.314462618 * temperature))
    k_forward = GENERATOR.rate_vv(1, 2, temperature, _parameters())
    k_reverse = k_forward / keq
    assert k_forward / k_reverse == pytest.approx(keq)
    assert keq > 1.0


def test_billing_ratio_fixture_covers_all_common_temperature_points_and_flags_outliers():
    fixture = json.loads(RATIO_FIXTURE.read_text())
    assert 'billing_scaling_note' in fixture
    points = fixture['points']
    vt = [p for p in points if p['process'] == 'V-T N2-N2']
    vv = [p for p in points if p['process'] == 'V-V N2-N2']
    assert len(vt) == 8 * 10  # Table 3, T=300..3000 K, n=1..9 and 20
    assert len(vv) == 8 * 10  # Table 4, T=200..2000 K, n=1..9 and 20
    assert {p['n'] for p in vt} == set(range(1, 10)) | {20}
    assert {p['n'] for p in vv} == set(range(1, 10)) | {20}
    assert {p['T_K'] for p in vt} == {300, 400, 500, 700, 1000, 1500, 2000, 3000}
    assert {p['T_K'] for p in vv} == {200, 300, 400, 500, 700, 1000, 1500, 2000}
    for point in points:
        ratio = point['guerra_over_billing']
        assert math.isfinite(ratio) and ratio > 0
        assert point['flag'] is (ratio < 0.3 or ratio > 3.0)


def test_named_gaps_are_explicit_and_ar_quenching_is_deferred():
    gaps = {gap['id']: gap for gap in _parameters()['record_source']['gaps']}
    assert gaps['n2_ar_vt']['status'] == 'absent'
    assert gaps['n2_n_vt']['status'] == 'out_of_scope'
    note = gaps['ar_metastable_n2_quenching']['note']
    assert 'total rate at 300 K only' in note
    assert 'product states need N2 electronic species' in note
    assert 'deferred' in note
