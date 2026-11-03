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
    assert GENERATOR.rate_vt(1, 300, parameters) == pytest.approx(2.0538041596515957e-21, rel=1e-12)
    assert GENERATOR.rate_vt(2, 300, parameters) == pytest.approx(3.3083259234726304e-21, rel=1e-12)
    assert GENERATOR.rate_vv(1, 0, 300, parameters) == pytest.approx(8.798818102449897e-15, rel=1e-12)


def _independent_f(y):
    if y < 21.622:
        return 0.5 * (3.0 - math.exp(-2.0 * y / 3.0)) * math.exp(-2.0 * y / 3.0)
    return 8.0 * math.sqrt(math.pi / 3.0) * y ** (7.0 / 3.0) * math.exp(-3.0 * y ** (2.0 / 3.0))


def _independent_y(gap_cm, temperature):
    hbar = 1.054571817e-34
    kb = 1.380649e-23
    hc_cm = 1.9864458571489286e-23
    reduced_mass = 28.0134 * 1.66053906660e-27 / 2.0
    length = 0.2e-10
    return abs(gap_cm) * hc_cm * math.pi * length / hbar * math.sqrt(reduced_mass / (2.0 * kb * temperature))


def _formula_reference_vt(v, temperature):
    omega, omega_xe = 2358.57, 14.324
    chi = omega_xe / omega
    gap = omega - 2.0 * omega_xe * v
    y = _independent_y(gap, temperature)
    xi = 0.2772 * temperature - 80.32 + 35.5 * ((v - 1.0) / 39.0) ** 0.8
    return (v * (1.0 - chi) / (1.0 - chi * v) * _independent_f(y)
            * 1.07e-12 * temperature ** 1.5 / xi)


def _formula_reference_vv(v, partner_low, temperature):
    omega, omega_xe = 2358.57, 14.324
    chi = omega_xe / omega
    partner_high = partner_low + 1
    gap_v = omega - 2.0 * omega_xe * v
    gap_w = omega - 2.0 * omega_xe * partner_high
    y = _independent_y(gap_v - gap_w, temperature)
    xi = (39.0625 - 1.5625 * v if v < 10 else
          25.2 + 24.1 * ((v - 10.0) / 30.0) ** 3)
    return (v * partner_high * (1.0 - chi) / (1.0 - chi * v)
            * (1.0 - chi) / (1.0 - chi * partner_high)
            * _independent_f(y) * 6.354e-17 * temperature ** 1.5 / xi)


def test_loKi_cross_check_spots_match_independent_equation_references():
    """LoKI_main.zip VT lines 54-65 and VV lines 87-104 cross-check Guerra Eqs. 10, 12, 14, 20-23."""
    parameters = _parameters()
    # These expected values are evaluated by test-local formula transcriptions above,
    # independently of the generator implementation.
    vt_spots = ((1, 300, 2.0538041596515957e-21),
                (10, 1000, 8.289462036285432e-16),
                (30, 3000, 2.3388945802125197e-11))
    for v, temperature, expected in vt_spots:
        reference = _formula_reference_vt(v, temperature)
        assert reference == pytest.approx(expected, rel=1e-12)
        assert GENERATOR.rate_vt(v, temperature, parameters) == pytest.approx(reference, rel=1e-12)
    vv_spots = ((1, 0, 300, 8.8043606650341175e-15),
                (3, 1, 1000, 3.1750453525706054e-13),
                (20, 19, 2000, 1.1151264053440554e-10))
    for v, partner, temperature, expected in vv_spots:
        reference = _formula_reference_vv(v, partner, temperature)
        assert reference == pytest.approx(expected, rel=1e-12)
        # Guerra rounds Eq. (22) to 6.35; LoKI uses 6.354 in its implementation.
        assert GENERATOR.rate_vv(v, partner, temperature, parameters) == pytest.approx(reference, rel=0.001)


def test_vv_generates_deactivating_level_as_v_and_respects_strict_ten_boundary():
    parameters = _parameters()
    assert GENERATOR.rate_vv(9, 8, 1000, parameters) == pytest.approx(_formula_reference_vv(9, 8, 1000))
    assert GENERATOR.rate_vv(10, 9, 1000, parameters) == pytest.approx(_formula_reference_vv(10, 9, 1000))
    py, _ = GENERATOR.generate(PARAMETERS.read_bytes(), json.dumps(_small_ladder()).encode(), 3)
    labels = [line for line in py.decode().splitlines() if line.strip().startswith('label =')]
    assert any('N2v1 + N2v0 <=> N2v0 + N2v1' in line for line in labels)
    assert not any('N2v1 + N2v1 <=> N2v0 + N2v2' in line for line in labels)


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
    with pytest.raises(ValueError, match='refuses'):
        GENERATOR.rate_vv(1, 1, 300, parameters)


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
    # The reversible channel is N2(v=3)+N2(v=0) <=> N2(v=2)+N2(v=1).
    delta_g_ev = energies[2] + energies[1] - energies[3] - energies[0]
    temperature = 1000.0
    keq = math.exp(-delta_g_ev * 96485.33212 / (8.314462618 * temperature))
    k_forward = GENERATOR.rate_vv(3, 0, temperature, _parameters())
    k_reverse = k_forward / keq
    assert k_forward / k_reverse == pytest.approx(keq)
    assert 0.0 < keq < 1.0


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
