"""Source-anchored N2 electronic-state thermo and energy-leak checks."""
from pathlib import Path

import pytest
from rmgpy.data.thermo import ThermoDatabase

ROOT = Path(__file__).resolve().parents[1]
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


def test_n2plus_b_absolute_offset_is_ionization_plus_b_x_energy(thermo_db):
    n2 = thermo_db.libraries['primaryThermoLibrary'].entries['N2'].data
    ion_b = thermo_db.libraries['PlasmaThermo'].entries['[N2pB]'].data
    expected = (15.5808 + 25461.46 / CM_PER_EV) * 96485.33212331
    for temperature in (200.0, 298.15, 500.0, 1000.0, 2500.0, 6000.0):
        difference = (ion_b.get_enthalpy(temperature)
                      - n2.get_enthalpy(temperature))
        assert difference == pytest.approx(expected, abs=1e-5)
        assert ion_b.get_heat_capacity(temperature) == pytest.approx(
            n2.get_heat_capacity(temperature), abs=1e-10)


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
