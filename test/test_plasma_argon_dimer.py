import math
import os

import pytest

from rmgpy import settings
from rmgpy.chemkin import load_species_dictionary
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.kinetics.arrhenius import Arrhenius, TwoTemperaturePlasma
from rmgpy import constants

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))
settings['database.directory'] = THIS_DATABASE
LIBRARY = 'PlasmaArgonDimer'
LIBRARY_DIR = os.path.join(THIS_DATABASE, 'kinetics', 'libraries', LIBRARY)


@pytest.fixture(scope='module')
def library():
    db = KineticsDatabase()
    db.load_libraries(os.path.join(THIS_DATABASE, 'kinetics', 'libraries'), libraries=[LIBRARY])
    return db.libraries[LIBRARY]


def test_library_has_exactly_three_entries_and_required_metadata(library):
    assert len(library.entries) == 3
    # Every other test reads kinetics by index, so bind each index to its reaction.
    assert library.entries[0].label == 'Arp + Ar + Ar <=> Ar2p + Ar'
    assert library.entries[1].label == 'Ar2p + e- => Ars + Ar'
    assert library.entries[2].label == 'Ar2p + e- => Arp + Ar + e-'
    assert sorted(s.label for s in library.entries[1].item.products) == ['Ar', 'Ars']
    assert sorted(s.label for s in library.entries[2].item.products) == ['Ar', 'Arp', 'e-']
    assert {e.label for e in library.entries.values()} == {
        'Arp + Ar + Ar <=> Ar2p + Ar',
        'Ar2p + e- => Ars + Ar',
        'Ar2p + e- => Arp + Ar + e-',
    }
    for entry in library.entries.values():
        assert entry.short_desc.strip(), 'entry {0!r} has an empty shortDesc'.format(entry.label)
        assert entry.long_desc.strip(), 'entry {0!r} has an empty longDesc'.format(entry.label)
        assert 'UNSOURCED Tg DEPENDENCE' in entry.long_desc
        assert '65%' in entry.long_desc and 'vibrationally excited' in entry.long_desc, (
            'entry {0!r} longDesc is missing the 65% vibrational-excitation warning'.format(entry.label))

    dr_entry = library.entries[1]
    assert 'EXTRAPOLATED DISSOCIATIVE-RECOMBINATION RATE' in dr_entry.long_desc
    assert 'BULK-MEAN ELECTRON-ENERGY APPROXIMATION' in dr_entry.long_desc

    dei_entry = library.entries[2]
    assert '298.15' in dei_entry.short_desc


def test_conversion_entry_pinned_metadata_and_rate(library):
    """index 0: three-body conversion Arp + Ar + Ar <=> Ar2p + Ar."""
    entry = library.entries[0]
    kinetics = entry.data
    assert isinstance(kinetics, Arrhenius)
    assert entry.item.reversible is True
    assert kinetics.Tmin.value_si == pytest.approx(150.0)
    assert kinetics.Tmax.value_si == pytest.approx(300.0)

    # Pin the individual Arrhenius parameters, in SI, rather than only the composite rate.
    assert kinetics.A.value_si == pytest.approx(2.25e-31 * 1e-12 * constants.Na ** 2, rel=1e-6)
    assert kinetics.n.value_si == pytest.approx(-0.4)
    assert kinetics.Ea.value_si == pytest.approx(0.0)
    assert kinetics.T0.value_si == pytest.approx(300.0)

    for T in (150.0, 200.0, 298.15, 300.0):
        # 2.25e-31 (T/300)^-0.4 cm^6/(molecule^2*s) -> m^6/(mol^2*s):
        # cm^6 -> m^6 is 1e-12; per two molecules squared -> per mol^2 is Na^2.
        expected = 2.25e-31 * (T / 300.0) ** -0.4 * 1e-12 * constants.Na ** 2
        assert kinetics.get_rate_coefficient(T) == pytest.approx(expected, rel=1e-6)


def test_dr_entry_pinned_metadata_and_rate(library):
    """index 1: dissociative recombination Ar2p + e- => Ars + Ar."""
    entry = library.entries[1]
    kinetics = entry.data
    assert isinstance(kinetics, TwoTemperaturePlasma)
    assert entry.item.reversible is False
    assert kinetics.Tmin.value_si == pytest.approx(300.0)
    assert kinetics.Tmax.value_si == pytest.approx(8500.0)

    # Pin the individual TwoTemperaturePlasma parameters, in SI.
    # A = 9.1e-7 cm^3/(molecule*s) -> m^3/(mol*s) is *1e-6*Na.
    assert kinetics.A.value_si == pytest.approx(9.1e-7 * 1e-6 * constants.Na, rel=1e-6)
    assert kinetics.n.value_si == pytest.approx(-0.61)
    assert kinetics.T0.value_si == pytest.approx(300.0)
    assert kinetics.Ea_g.value_si == pytest.approx(0.0)
    assert kinetics.Ea_e.value_si == pytest.approx(0.0)

    expected = {300: 9.100000e-7, 8500: 1.183422e-7,
                10444: 1.043702e-7, 13462: 8.939815e-8}
    for te, source in expected.items():
        source_value = 9.1e-7 * (300.0 / te) ** 0.61
        internal = kinetics.get_rate_coefficient_two_temp(298.15, te)
        assert source_value == pytest.approx(source, rel=1e-6)
        assert internal == pytest.approx(source * 1e-6 * constants.Na, rel=1e-6)

    # With Ea_g == Ea_e == 0, the closed-form rate has no Tg dependence at all: the rate at a
    # given Te must be identical regardless of Tg.
    for te in (300.0, 8500.0, 10444.0):
        rate_at_298 = kinetics.get_rate_coefficient_two_temp(298.15, te)
        rate_at_1000 = kinetics.get_rate_coefficient_two_temp(1000.0, te)
        assert rate_at_1000 == pytest.approx(rate_at_298, rel=1e-9), (
            'DR rate at Te={0} K depends on Tg, but Ea_g == Ea_e == 0 should cancel Tg entirely'.format(te))


def test_dei_entry_pinned_metadata_and_rate(library):
    """index 2: electron-impact dissociation Ar2p + e- => Arp + Ar + e-."""
    entry = library.entries[2]
    kinetics = entry.data
    assert isinstance(kinetics, TwoTemperaturePlasma)
    assert entry.item.reversible is False
    assert kinetics.Tmin.value_si == pytest.approx(298.15)
    assert kinetics.Tmax.value_si == pytest.approx(298.15)
    assert kinetics.n.value_si == pytest.approx(0.0)

    # A = 1.11e-12 m^3/(molecule*s) -> internal m^3/(mol*s) is *Na.
    assert kinetics.A.value_si == pytest.approx(1.11e-12 * constants.Na, rel=1e-6)

    # Ea_g == Ea_e == 2.94092 eV/molecule -> J/mol is *e*Na.
    expected_Ea_si = 2.94092 * constants.e * constants.Na
    assert kinetics.Ea_g.value_si == pytest.approx(expected_Ea_si, rel=1e-6)
    assert kinetics.Ea_e.value_si == pytest.approx(expected_Ea_si, rel=1e-6)

    # Closed-form rate, computed independently of get_rate_coefficient_two_temp: since
    # Ea_g == Ea_e == E and n == 0, k(Tg, Te) = A_si * (Te/T0)^0 * exp(-E/(R Tg))
    # * exp(E (Te-Tg)/(R Tg Te)) algebraically simplifies (the Tg-dependence cancels) to
    # k(Tg, Te) = A_si * exp(-E / (R * Te)).
    Tg, Te = 298.15, 10444.0
    A_si = 1.11e-12 * constants.Na
    expected = A_si * math.exp(-expected_Ea_si / (constants.R * Te))
    assert kinetics.get_rate_coefficient_two_temp(Tg, Te) == pytest.approx(expected, rel=1e-6)


def test_dictionary_species_match_source_libraries():
    dimer_dict = load_species_dictionary(os.path.join(LIBRARY_DIR, 'dictionary.txt'))
    argon_dict = load_species_dictionary(
        os.path.join(THIS_DATABASE, 'kinetics', 'libraries', 'PlasmaArgon', 'dictionary.txt'))

    dimer_blocks = _parse_dictionary_blocks(os.path.join(LIBRARY_DIR, 'dictionary.txt'))
    argon_blocks = _parse_dictionary_blocks(
        os.path.join(THIS_DATABASE, 'kinetics', 'libraries', 'PlasmaArgon', 'dictionary.txt'))

    assert set(dimer_dict) == {'Ar', 'Arp', 'Ars', 'Ar2p', 'e-'}

    for label in ('Ar', 'Arp', 'Ars', 'e-'):
        assert label in argon_dict, '{0!r} missing from PlasmaArgon/dictionary.txt'.format(label)
        assert dimer_dict[label].is_isomorphic(argon_dict[label]), (
            '{0!r} in PlasmaArgonDimer is not isomorphic to PlasmaArgon'.format(label))
        assert dimer_blocks[label] == argon_blocks[label], (
            '{0!r} adjacency-list text differs between PlasmaArgonDimer and PlasmaArgon'.format(label))

    thermo_path = os.path.join(THIS_DATABASE, 'thermo', 'libraries', 'PlasmaThermo.py')
    ar2p_thermo_entry = _find_thermo_entry_species(thermo_path, '[Ar2p]')
    assert dimer_dict['Ar2p'].is_isomorphic(ar2p_thermo_entry), (
        'Ar2p in PlasmaArgonDimer is not isomorphic to [Ar2p] in PlasmaThermo')

    ar2p_thermo_adjlist = _find_thermo_entry_adjlist_text(thermo_path, '[Ar2p]')
    assert _normalize_adjlist_text(dimer_blocks['Ar2p']) == _normalize_adjlist_text(ar2p_thermo_adjlist), (
        'Ar2p adjacency-list text in PlasmaArgonDimer/dictionary.txt differs from '
        '[Ar2p] in PlasmaThermo.py')


def _parse_dictionary_blocks(path):
    """Return {label: adjacency-list-text} parsed the same way RMG dictionaries are
    written: blank-line-separated blocks, first line of each block is the label."""
    with open(path) as f:
        text = f.read()
    blocks = {}
    for raw_block in text.strip('\n').split('\n\n'):
        raw_block = raw_block.strip('\n')
        if not raw_block.strip():
            continue
        lines = raw_block.split('\n')
        label = lines[0].strip()
        blocks[label] = '\n'.join(lines[1:])
    return blocks


def _find_thermo_entry_adjlist_text(path, entry_label):
    with open(path) as f:
        text = f.read()
    marker = 'label = "{0}"'.format(entry_label)
    idx = text.index(marker)
    molecule_marker = text.index('molecule =', idx)
    triple_quote_start = text.index('"""', molecule_marker) + 3
    triple_quote_end = text.index('"""', triple_quote_start)
    return text[triple_quote_start:triple_quote_end]


def _find_thermo_entry_species(path, entry_label):
    from rmgpy.species import Species
    adjlist = _find_thermo_entry_adjlist_text(path, entry_label)
    species = Species()
    species.from_adjacency_list(adjlist)
    return species


def _normalize_adjlist_text(text):
    """Normalize whitespace per line (strip each line, collapse internal runs of
    whitespace to a single space, drop blank lines) so that formatting differences
    that do not change the adjacency list's meaning do not fail the comparison."""
    lines = []
    for raw_line in text.splitlines():
        line = ' '.join(raw_line.split())
        if line:
            lines.append(line)
    return '\n'.join(lines)
