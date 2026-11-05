"""Optional dissociative pooling is an explicit model-transfer sensitivity."""
from pathlib import Path

import pytest

from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.kinetics import Arrhenius

ROOT = Path(__file__).resolve().parents[1]


def load():
    database = KineticsDatabase()
    database.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=[
        'PlasmaNitrogenDissociativePooling', 'PlasmaNitrogenExcited', 'PlasmaAtomicNitrogen'])
    return database.libraries


def test_pooling_rate_balance_and_event_convention():
    libraries = load()
    library = libraries['PlasmaNitrogenDissociativePooling']
    assert len(library.entries) == 1
    entry = next(iter(library.entries.values()))
    assert entry.label == 'N2A + N2A => N2 + N + N'
    assert isinstance(entry.data, Arrhenius)
    assert entry.item.is_balanced() and not entry.item.reversible
    assert sorted(s.label for s in entry.item.reactants) == ['N2A', 'N2A']
    assert sorted(s.label for s in entry.item.products) == ['N', 'N', 'N2']
    for temperature in (298., 300., 600.):
        rate = entry.data.get_rate_coefficient(temperature) / 6.02214179e23
        assert rate == pytest.approx(2e-16, rel=1e-14, abs=0.)
        event_rate = rate * (2e17)**2
        assert 2 * event_rate == pytest.approx(1.6e19, rel=1e-14)
    assert 'doi:10.1088/1361-6595/abcc7c' in entry.long_desc
    assert 'not an evaluated' in entry.long_desc.lower()
    assert 'uncertainty' in entry.long_desc.lower()
    for name in ('PlasmaNitrogenExcited', 'PlasmaAtomicNitrogen'):
        assert not any(entry.item.is_isomorphic(other.item, either_direction=False)
                       for other in libraries[name].entries.values())


def test_readme_labels_conditional_policy():
    text = (ROOT / 'input/kinetics/libraries/PlasmaNitrogenDissociativePooling/README.md').read_text()
    for phrase in ('not an evaluated', 'with and without', 'conditional', '1.73e-16',
                   '2e-17', 'gamma_N = 1e-4', '0.01', '0.05', '0.2'):
        assert phrase in text
