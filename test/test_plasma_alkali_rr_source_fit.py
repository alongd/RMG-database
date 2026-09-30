"""Regression tests for the PlasmaAlkali Verner--Ferland RR fits."""

import math
import os
import re

import pytest

from rmgpy import settings
from rmgpy.constants import Na
from rmgpy.data.kinetics.database import KineticsDatabase


LIBRARY = "PlasmaAlkali"
EXPECTED = {
    1: (1.0e3, 1.0e5, 1.762351),
    2: (1.0e3, 1.0e5, 3.132286),
    45: (1.0e3, 1.0e5, 2.746092),
}
DENSE_GRID_SIZE = 1001
PARAMETERS = re.compile(
    r"Fit Parameters: a=([0-9.e+-]+), b=([0-9.e+-]+), "
    r"T0=([0-9.e+-]+), T1=([0-9.e+-]+)"
)
FIT = re.compile(
    r"Verner-Ferland fit: Te=([0-9.e+-]+)-([0-9.e+-]+) K; "
    r"maximum relative error=([0-9.e+-]+)%"
)


@pytest.fixture(scope="module")
def entries():
    database = KineticsDatabase()
    libraries_dir = os.path.join(settings["database.directory"], "kinetics", "libraries")
    database.load_libraries(libraries_dir, libraries=[LIBRARY])
    library = database.libraries[LIBRARY]
    return {entry.index: entry for entry in library.entries.values() if entry.index in EXPECTED}


def _source_rate(temperature, parameters):
    a, b, t0, t1 = parameters
    return a / (
        math.sqrt(temperature / t0)
        * (1.0 + math.sqrt(temperature / t0)) ** (1.0 - b)
        * (1.0 + math.sqrt(temperature / t1)) ** (1.0 + b)
    )


def _loaded_rate(entry, temperature):
    # TwoTemperaturePlasma returns m^3/(mol*s); source tables are cm^3/s.
    return entry.data.get_rate_coefficient_two_temp(temperature, temperature) * 1.0e6 / Na


def _log_grid(start, end, count):
    return tuple(start * (end / start) ** (i / (count - 1)) for i in range(count))


@pytest.mark.parametrize("index", (1, 2, 45))
def test_loaded_rate_matches_verner_ferland_fit(entries, index):
    entry = entries[index]
    parameters = tuple(float(value) for value in PARAMETERS.search(entry.long_desc).groups())
    fit_start, fit_end, stated_error = (float(value) for value in FIT.search(entry.long_desc).groups())
    expected_start, expected_end, expected_error = EXPECTED[index]
    assert (fit_start, fit_end) == (expected_start, expected_end)
    assert stated_error == pytest.approx(expected_error, abs=0.05)
    assert entry.data.Tmin.value_si == pytest.approx(fit_start)
    assert entry.data.Tmax.value_si == pytest.approx(fit_end)
    assert entry.data.T0.value_si == pytest.approx(1.0)

    errors = []
    for temperature in _log_grid(fit_start, fit_end, DENSE_GRID_SIZE):
        source = _source_rate(temperature, parameters)
        loaded = _loaded_rate(entry, temperature)
        errors.append(abs(loaded / source - 1.0) * 100.0)
    assert max(errors) <= 5.0
    assert stated_error == pytest.approx(max(errors), abs=0.05)


@pytest.mark.parametrize("index", (1, 2, 45))
def test_loaded_rate_is_independent_of_gas_temperature(entries, index):
    entry = entries[index]
    for electron_temperature in (5000.0, 11600.0, 30000.0):
        rates = [entry.data.get_rate_coefficient_two_temp(gas_temperature, electron_temperature)
                 for gas_temperature in (298.0, 600.0, 1000.0)]
        assert rates[1] == pytest.approx(rates[0], rel=1.0e-12)
        assert rates[2] == pytest.approx(rates[0], rel=1.0e-12)
