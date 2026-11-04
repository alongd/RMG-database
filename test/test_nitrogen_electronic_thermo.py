"""Source-anchored N2 electronic-state thermo and energy-leak checks."""
import json
from pathlib import Path

import pytest
from rmgpy.constants import R as R_RUNTIME
from rmgpy.data.thermo import ThermoDatabase

ROOT = Path(__file__).resolve().parents[1]
N2P_REFERENCE = json.loads(
    (ROOT / 'test/nitrogen_cation_janaf_reference.json').read_text())
LIB = ROOT / 'input/thermo/libraries'
CM_PER_EV = 8065.543937
NIST_NEUTRAL_CM = {
    'N2(A)': 50203.63,
    'N2(B)': 59619.35,
    'N2(C)': 89136.88,
    "N2(a')": 68152.66,
    'N2(a)': 69283.06,
    'N2(w)': 72097.4,
}


@pytest.fixture(scope='module')
def thermo_db():
    db = ThermoDatabase()
    db.load_libraries(
        str(LIB), libraries=['primaryThermoLibrary',
                             'PlasmaExcitedNeutralThermo', 'PlasmaThermo'])
    return db


def test_neutral_state_enthalpy_offsets_and_cp_match_n2(thermo_db):
    n2 = thermo_db.libraries['primaryThermoLibrary'].entries['N2'].data
    excited = thermo_db.libraries['PlasmaExcitedNeutralThermo'].entries
    for label, term_origin in NIST_NEUTRAL_CM.items():
        state = excited[label].data
        expected = term_origin / CM_PER_EV * 96485.33212331
        temperatures = (200.0, 298.15, 500.0, 999.0, 1000.0, 2500.0, 6000.0)
        for temperature in temperatures:
            difference = (state.get_enthalpy(temperature)
                          - n2.get_enthalpy(temperature))
            assert difference == pytest.approx(expected, abs=1e-5)
            assert state.get_heat_capacity(temperature) == pytest.approx(
                n2.get_heat_capacity(temperature), abs=1e-10)


def test_n2plus_x_reproduces_nist_janaf_columns_and_ion_convention(thermo_db):
    entry = thermo_db.libraries['PlasmaThermo'].entries['[N2p]']
    ion_x = entry.data
    reference = N2P_REFERENCE
    expected_h298 = (reference['electron_convention_h298_kJ_mol']
                     - reference['ion_convention_electron_h_correction_kJ_mol'])
    assert ion_x.get_enthalpy(298.15) / 1000 == pytest.approx(
        expected_h298, abs=1e-8)
    assert 'ion convention' in entry.long_desc
    assert 'electron H=S=Cp=0' in entry.long_desc
    # NIST-JANAF N-024 prints S(200 K) as 197.660, identical to S(298.15 K),
    # although its 100 K row is 165.859. Preserve and document the source row;
    # do not force a discontinuous entropy fit to reproduce the apparent typo.
    assert reference['printed_200_k_entropy_j_mol_k'] == reference['s298_j_mol_k']
    assert reference['printed_100_k_entropy_j_mol_k'] < reference[
        'printed_200_k_entropy_j_mol_k']
    assert '200 K entropy row prints 197.660' in entry.long_desc
    for temperature_text, row in reference['rows'].items():
        temperature = float(temperature_text)
        assert ion_x.get_heat_capacity(temperature) == pytest.approx(
            row['cp'], abs=0.20)
        assert ion_x.get_entropy(temperature) == pytest.approx(
            row['s'], abs=0.06)
        expected_h = expected_h298 + row['dh_kj_mol']
        assert ion_x.get_enthalpy(temperature) / 1000 == pytest.approx(
            expected_h, abs=0.06)


def test_n2plus_b_is_x_thermo_plus_webbook_b_x_energy(thermo_db):
    plasma = thermo_db.libraries['PlasmaThermo'].entries
    ion_x = plasma['[N2p]'].data
    ion_b = plasma['[N2pB]'].data
    expected = 25461.46 / CM_PER_EV * 96485.33212331
    for temperature in (200.0, 298.15, 400.0, 1000.0, 2500.0, 6000.0):
        assert (ion_b.get_enthalpy(temperature)
                - ion_x.get_enthalpy(temperature)) == pytest.approx(
                    expected, abs=1e-5)
        assert ion_b.get_heat_capacity(temperature) == pytest.approx(
            ion_x.get_heat_capacity(temperature), abs=1e-10)
        assert ion_b.get_entropy(temperature) == pytest.approx(
            ion_x.get_entropy(temperature), abs=1e-10)
    for x_poly, b_poly in zip(ion_x.polynomials, ion_b.polynomials):
        assert list(b_poly.coeffs[:5]) == pytest.approx(
            list(x_poly.coeffs[:5]), abs=0)
        assert b_poly.coeffs[6] == pytest.approx(x_poly.coeffs[6], abs=0)
        assert b_poly.coeffs[5] - x_poly.coeffs[5] == pytest.approx(
            expected / R_RUNTIME, abs=1e-7)
    assert '25461.4_6' in plasma['[N2pB]'].long_desc


def test_n2plus_nasa_join_is_continuous(thermo_db):
    entry = thermo_db.libraries['PlasmaThermo'].entries['[N2p]'].data
    low, high = entry.polynomials
    for getter in ('get_heat_capacity', 'get_enthalpy', 'get_entropy'):
        # NASA switches polynomials at Tmid; evaluate both sides directly.
        low_value = getattr(low, getter)(1000.0)
        high_value = getattr(high, getter)(1000.0)
        assert low_value == pytest.approx(high_value, abs=1e-4)


def test_three_a_band_energy_leaks_are_preserved():
    import yaml
    ledger = yaml.safe_load(
        (ROOT / 'input/eedf/nitrogen_energy_leaks.yaml').read_text())
    a_rows = [row for row in ledger['channels'] if 'A3Su+' in row['process']]
    assert [row['threshold_eV'] for row in a_rows] == [6.2, 7.0, 7.8]
    assert all(row['mapped_state'] == 'N2(A)' for row in a_rows)
    assert [row['threshold_minus_T_e_eV'] for row in a_rows] == pytest.approx(
        [-0.024456824, 0.775543176, 1.575543176], abs=1e-9)
    assert max(abs(row['threshold_minus_T_e_eV'])
               for row in a_rows) == pytest.approx(1.575543176)
