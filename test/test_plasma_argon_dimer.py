import os

import pytest

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy import constants

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))
settings['database.directory'] = THIS_DATABASE
LIBRARY = 'PlasmaArgonDimer'


@pytest.fixture(scope='module')
def library():
    db = KineticsDatabase()
    db.load_libraries(os.path.join(THIS_DATABASE, 'kinetics', 'libraries'), libraries=[LIBRARY])
    return db.libraries[LIBRARY]


def test_library_has_exactly_three_entries_and_required_metadata(library):
    assert len(library.entries) == 3
    assert {e.label for e in library.entries.values()} == {
        'Arp + Ar + Ar <=> Ar2p + Ar',
        'Ar2p + e- => Ars + Ar',
        'Ar2p + e- => Arp + Ar + e-',
    }
    assert 'UNSOURCED Tg DEPENDENCE' in library.entries[1].long_desc
    assert 'EXTRAPOLATED DISSOCIATIVE-RECOMBINATION RATE' in library.entries[1].long_desc
    assert 'BULK-MEAN ELECTRON-ENERGY APPROXIMATION' in library.entries[1].long_desc


def test_dr_unit_gate_in_source_and_internal_units(library):
    kinetics = library.entries[1].data
    expected = {300: 9.100000e-7, 8500: 1.183422e-7,
                10444: 1.043702e-7, 13462: 8.939815e-8}
    for te, source in expected.items():
        source_value = 9.1e-7 * (300.0 / te) ** 0.61
        internal = kinetics.get_rate_coefficient_two_temp(298.15, te)
        assert source_value == pytest.approx(source, rel=1e-6)
        assert internal == pytest.approx(source * 1e-6 * constants.Na, rel=1e-6)


def test_conversion_forward_rate_and_source_range(library):
    conversion = library.entries[0].data
    assert conversion.get_rate_coefficient(298.15) == pytest.approx(8.18011e4, rel=1e-6)
    assert conversion.Tmin.value_si == 150
    assert conversion.Tmax.value_si == 300
