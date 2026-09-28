"""Pinned LoKI Maxwellian rates for refitted and independently verified PlasmaAir fits."""
import json
from pathlib import Path

import pytest
from rmgpy import settings
from rmgpy.constants import Na, e, kB
from rmgpy.data.kinetics.database import KineticsDatabase

REF = json.loads((Path(__file__).parent / 'plasma_air_te_reference.json').read_text())
PINNED_REFITTED_AND_VERIFIED_INDICES = (2, 19, 20, 28, 37, 39, 40, 55, 58, 68, 69, 102)
PINNED_TE_EV = (0.5, 1.0, 2.0, 3.0, 5.0)
# These are part of the source-data fixture, not a global acceptance band.  In
# particular, the 0.32 fit error belongs only to O(1D), not every refit.
PINNED_TOLERANCES = {
    2: 0.18, 19: 0.02, 20: 0.02, 28: 0.04, 37: 0.04, 39: 0.04,
    40: 0.02, 55: 0.20, 58: 0.06, 68: 0.09, 69: 0.32, 102: 0.02,
}


@pytest.fixture(scope='module')
def entries():
    database = KineticsDatabase()
    path = Path(settings['database.directory']) / 'kinetics' / 'libraries'
    database.load_libraries(str(path), libraries=['PlasmaAir'])
    return {entry.index: entry for entry in database.libraries['PlasmaAir'].entries.values()}


def test_pinned_loki_maxwellian_rates_for_refitted_and_verified_fits(entries):
    """Changing a pinned refit or independently verified fit changes this comparison."""
    assert REF['loki_commit'] == '6aa3d52980'
    assert tuple(sorted(map(int, REF['entries']))) == PINNED_REFITTED_AND_VERIFIED_INDICES
    assert tuple(REF['te_eV']) == PINNED_TE_EV
    kelvin_per_ev = e / kB
    for index_text, reference in REF['entries'].items():
        index = int(index_text)
        assert len(reference['k']) == len(PINNED_TE_EV)
        assert reference['tol'] == PINNED_TOLERANCES[index]
        assert index in entries, 'pinned refitted or verified fit missing: {}'.format(index)
        kinetics = entries[index].data
        calculated = [kinetics.get_rate_coefficient_two_temp(298.15, te * kelvin_per_ev) * 1e6 / Na
                      for te in REF['te_eV']]
        assert len(calculated) == len(reference['k'])
        for value, expected in zip(calculated, reference['k']):
            assert value == pytest.approx(expected, rel=reference['tol'])


def test_tanarro_i6_and_n1_pins(entries):
    """I6 and N1 are independently pinned to their published Te-in-eV laws."""
    tev = (0.5, 1.0, 2.0, 3.0, 5.0)
    factor = e / kB
    i6 = entries[31].data
    n1 = entries[41].data
    # Tanarro I6's published particle-rate law is 3.12e-8 Te^0.17 exp(-20.07/Te)
    # cm^3/s.  The library stores its rounded molar A (1.88e16), so allow only
    # that molar-to-particle conversion/rounding difference.
    expected_i6 = [3.12e-8 * (t ** 0.17) * __import__('math').exp(-20.07 / t) for t in tev]
    expected_n1 = [7.51e-9 - 1.12e-9*t + 1.03e-10*t**2 - 4.15e-12*t**3 + 5.86e-14*t**4 for t in tev]
    got_i6 = [i6.get_rate_coefficient_two_temp(298.15, t * factor) * 1e6 / Na for t in tev]
    got_n1 = [n1.get_rate_coefficient_two_temp(298.15, t * factor) * 1e6 / Na for t in tev]
    assert got_i6 == pytest.approx(expected_i6, rel=1e-3)
    assert got_n1 == pytest.approx(expected_n1, rel=0.05)
