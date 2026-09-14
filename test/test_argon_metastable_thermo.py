#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for ``PlasmaExcitedNeutralThermo``, the metastable-argon thermochemistry entry.

The report is ``docs/argon-metastable-thermo/report.md``. This file is the executable half
of it: every number quoted there that can be re-derived is re-derived here, so a later
change that moves one fails a test rather than silently contradicting a document.

Five groups, in descending order of how much they would cost to be wrong about:

1. **Which state the entry is.** ``Ar u2 p3 c0`` is an adjacency list; it carries no orbital
   information, and at least three physically distinct argon levels answer to it. The entry
   is the 4s ``3P2`` metastable (Paschen 1s5) and nothing else. The level energy, its
   degeneracy, and the exclusion of the two resonant levels and of the ``3P0`` lump are each
   pinned, because an entry that drifted into meaning something else would still load, still
   match, and still look right.

2. **The three numbers**, each against the identity that produced it - the level energy from
   NIST ASD, ``R ln g`` on JANAF's ground-state entropy, and ``5/2 R`` - and ``E0 == H298``,
   which is an identity here and is not one for the argon cation.

3. **The whole path**: the library loads, the species perceives as ``Ar0e``, and
   ``get_thermo_data`` returns THIS entry rather than an estimator. Group 3 also pins the
   estimator's refusal, which is what makes the entry load-bearing rather than decorative.

4. **The lumping arithmetic**, including the correction this ticket made to it: the electronic
   entropy of a two-level manifold is ``R ln Q + R <E>/RT``, and the second term is 7x the
   first at 298.15 K.

5. **What did not change**: the argon cation's entry, and the fact that no deck, dictionary or
   kinetics file anywhere in this database mentions the metastable. Also pinned, as a
   disclosure rather than an approval, is the ground-state argon that a running mechanism
   actually resolves to - ``BurkeH2O2``'s 4-figure value, not JANAF's.

Run with the runtime pinned::

    cd /home/alon/Code/RMG-database-i221-argon-metastable-thermo
    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
        python -m pytest test/test_argon_metastable_thermo.py -q

``test/conftest.py`` pins ``database.directory`` to this worktree before collection; the
fixtures below assert that pin rather than trusting it.
"""

import math
import os

import pytest

from rmgpy import settings
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.exceptions import AtomTypeError
from rmgpy.molecule import Molecule
from rmgpy.species import Species

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,
                                             'input'))
LIBRARY_DIR = os.path.join(THIS_DATABASE, 'thermo', 'libraries')
GROUP_DIR = os.path.join(THIS_DATABASE, 'thermo', 'groups')
KINETICS_DIR = os.path.join(THIS_DATABASE, 'kinetics')

LIBRARY = 'PlasmaExcitedNeutralThermo'
LABEL = 'Ar(3P2)'
CATION_LIBRARY = 'PlasmaCationThermo'

R = 8.314462618
T0 = 298.15
#: CODATA: h*c*N_A, J/(mol*cm^-1), and cm^-1 per eV.
HC_NA = 11.9626565957
CM_PER_EV = 8065.543937

# --- NIST ASD ver. 5.12, doi:10.18434/T4W30F, Ar I levels (cm^-1), quoted so a test can
# --- check the file against the source rather than against itself.
ASD_1S5_3P2 = 93143.7600      # g = 5, metastable   <- THIS ENTRY
ASD_1S4_3P1 = 93750.5978      # g = 3, resonant, A(106.6660 nm) = 1.320e8 s^-1
ASD_1S3_3P0 = 94553.6652      # g = 1, metastable
ASD_1S2_1P1 = 95399.8276      # g = 3, resonant, A(104.8220 nm) = 5.32e8 s^-1
A_1S4 = 1.320e8               # s^-1
A_1S2 = 5.32e8                # s^-1
#: Measured metastable lifetime, Katori & Shimizu, Phys. Rev. Lett. 70 (1993) 3545.
TAU_1S5_MEASURED = 38.0       # s

#: NIST-JANAF Ar-001 "Argon (Ar)", the element reference state this entry is anchored on.
JANAF_AR_S298 = 154.845       # J/(mol*K)
JANAF_AR_CP = 20.786          # J/(mol*K), at every tabulated T

#: What is actually in the file.
ENTERED_H298 = 1114.247       # kJ/mol
ENTERED_S298 = 168.227        # J/(mol*K)
ENTERED_CP = 20.786           # J/(mol*K)

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'


def _species(adjacency_list, label=''):
    return Species(label=label,
                   molecule=[Molecule().from_adjacency_list(adjacency_list)])


def _electronic(levels, T):
    """(S_el, H_el, Cp_el) of a manifold ``levels`` = [(g, E in kJ/mol), ...] relative to
    its lowest level, in J/(mol*K), kJ/mol, J/(mol*K).

    Written out rather than imported because the point of the group-4 tests is that the
    two-term expression is right and the one-term one is not.
    """
    e0 = min(e for _g, e in levels)
    xs = [(g, (e - e0) * 1000.0 / (R * T)) for g, e in levels]
    q = sum(g * math.exp(-x) for g, x in xs)
    mean = sum(g * x * math.exp(-x) for g, x in xs) / q
    mean_sq = sum(g * x * x * math.exp(-x) for g, x in xs) / q
    return (R * (math.log(q) + mean),
            mean * R * T / 1000.0,
            R * (mean_sq - mean ** 2))


@pytest.fixture(scope='module')
def pinned():
    """Assert the pin rather than trusting it. A run against another checkout would
    otherwise produce a green that means nothing, which has happened on this campaign."""
    assert settings['database.directory'] == THIS_DATABASE, (
        f"database.directory is {settings['database.directory']!r}, not this worktree")
    return THIS_DATABASE


@pytest.fixture(scope='module')
def thermo_db(pinned):
    db = ThermoDatabase()
    db.load_libraries(LIBRARY_DIR)
    db.load_groups(GROUP_DIR)
    return db


@pytest.fixture(scope='module')
def estimator_only(pinned):
    """The same database with every library unloaded, so any answer it gives is group
    additivity and HBI rather than a lookup."""
    db = ThermoDatabase()
    db.load_libraries(LIBRARY_DIR)
    db.unload_libraries()
    db.load_groups(GROUP_DIR)
    assert not db.libraries
    return db


@pytest.fixture(scope='module')
def entry(thermo_db):
    return thermo_db.libraries[LIBRARY].entries[LABEL]


# =====================================================================================
# 1. Which state the entry is
# =====================================================================================

def test_the_entry_is_the_1s5_level_and_says_so(entry):
    """The whole ticket in one assertion. The label, the shortDesc and the longDesc all
    name the level; if any of them is edited into vagueness this fails."""
    assert entry.label == LABEL
    assert '3P2' in entry.short_desc and '1s5' in entry.short_desc
    assert str(int(ASD_1S5_3P2)) in entry.short_desc, (
        'the shortDesc must carry the level energy, not just a term symbol')
    for required in ('93143.7600', '2[3/2]*', 'J = 2', 'g = 5', 'Paschen 1s5'):
        assert required in entry.long_desc, required


def test_the_alternatives_are_named_with_their_numbers_so_the_choice_can_be_overruled(entry):
    """A decision recorded without its alternatives is an assertion, not a decision.
    All three rival levels must appear in the longDesc with their own energies."""
    for level in (ASD_1S4_3P1, ASD_1S3_3P0, ASD_1S2_1P1):
        assert '%.4f' % level in entry.long_desc, level


def test_the_structure_is_the_only_neutral_bond_free_p3_argon(pinned):
    """Why ``1P1`` is unrepresentable rather than merely declined: argon has 8 valence
    electrons, so with three lone pairs, no bonds and no charge the remaining two must be
    unpaired. RMG enforces this itself - ``ConsistencyChecker.check_partial_charge``
    rejects every other ``u`` at ``p3 c0`` as an invalid valency - so the singlet 4s level
    has no adjacency list at all, and the choice among the 4s levels is a choice among the
    three TRIPLETS only. Measured here rather than argued."""
    triplet = Molecule().from_adjacency_list(AR_META)
    assert triplet.multiplicity == 3
    assert triplet.get_net_charge() == 0
    assert triplet.atoms[0].radical_electrons == 2

    from rmgpy.exceptions import InvalidAdjacencyListError
    for u in (0, 1, 3, 4):
        with pytest.raises(InvalidAdjacencyListError):
            Molecule().from_adjacency_list(
                'multiplicity %d\n1 Ar u%d p3 c0\n' % (u + 1, u))


def test_the_resonant_levels_are_excluded_on_lifetime_not_on_taste(entry):
    """``3P1`` shares this adjacency list and is excluded because it is a radiative
    transient, not a reservoir: nine to ten orders of magnitude in lifetime."""
    tau_1s4 = 1.0 / A_1S4
    tau_1s2 = 1.0 / A_1S2
    assert tau_1s4 == pytest.approx(7.58e-9, rel=1e-2)
    assert tau_1s2 == pytest.approx(1.88e-9, rel=1e-2)
    assert TAU_1S5_MEASURED / tau_1s4 > 1e9
    for required in ('106.6660', '1.320e+08', 'Katori', 'Small-Warren'):
        assert required in entry.long_desc, required


def test_the_radiation_trapping_caveat_is_recorded(entry):
    """The one way the lifetime argument could be turned around - trapped resonance
    radiation makes 1s4/1s2 effectively long-lived at high density - must be in the
    entry, because a reader who knows it and does not find it will assume it was missed."""
    assert 'RADIATION-TRAPPED' in entry.long_desc or 'trapped' in entry.long_desc.lower()


# =====================================================================================
# 2. The three numbers
# =====================================================================================

def test_h298_is_the_level_energy_times_hc_na(entry):
    """H298 is the 1s5 level energy converted by an exact constant. Nothing else."""
    expected = ASD_1S5_3P2 * HC_NA / 1000.0
    assert expected == pytest.approx(1114.2468, abs=5e-4)
    assert entry.data.H298.value_si / 1000.0 == pytest.approx(expected, abs=5e-4)
    assert entry.data.H298.value_si / 1000.0 == ENTERED_H298


def test_h298_equals_e0_and_that_is_an_identity_not_a_coincidence(entry, thermo_db):
    """dfH(298.15) = dfH(0) + [H298-H0]_excited - [H298-H0]_ground, and both increments
    are 5/2 R T because a single level has no internal structure. They cancel exactly.

    The contrast is the argon cation, whose 2P fine structure makes its own increment
    6.206 rather than 6.197, so its H298 and E0 differ by 0.008 kJ/mol. If that contrast
    ever disappears, one of the two entries has been mis-edited."""
    assert entry.data.E0.value_si == entry.data.H298.value_si
    arp = thermo_db.libraries[CATION_LIBRARY].entries['[Arp]']
    assert (arp.data.H298.value_si - arp.data.E0.value_si) / 1000.0 == pytest.approx(
        0.008, abs=1e-3)


def test_s298_is_the_ground_state_plus_the_exact_degeneracy_term(entry):
    """S298 = S298(Ar, JANAF Ar-001) + R ln(g*/g0), with g = 2J+1 = 5 against 1.

    Exact, not approximate: translation, mass and standard state are identical between
    the two, so the entire difference is electronic and a single level contributes only
    R ln g."""
    r_ln_5 = R * math.log(5.0)
    assert r_ln_5 == pytest.approx(13.3816, abs=5e-4)
    assert JANAF_AR_S298 + r_ln_5 == pytest.approx(ENTERED_S298, abs=5e-4)
    assert entry.data.S298.value_si == pytest.approx(ENTERED_S298, abs=1e-9)


def test_cp_is_exactly_five_halves_r_at_every_tabulated_temperature(entry):
    """A free monatomic species pinned to ONE electronic level has translation and
    nothing else - no rotation, no vibration, and no Schottky term. Contrast Ar+, whose
    Cp peaks at 22.773 J/(mol*K) near 1000 K precisely because it is a 2P term."""
    five_halves_r = 2.5 * R
    assert five_halves_r == pytest.approx(JANAF_AR_CP, abs=5e-4)
    for cp in entry.data.Cpdata.value_si:
        assert cp == pytest.approx(ENTERED_CP, abs=1e-9)
    assert entry.data.Cp0.value_si == pytest.approx(five_halves_r, abs=1e-3)
    assert entry.data.CpInf.value_si == pytest.approx(five_halves_r, abs=1e-3)
    assert entry.data.Tdata.value_si[0] == pytest.approx(T0)
    assert entry.data.Tdata.value_si[-1] == pytest.approx(6000.0)


def test_the_level_energy_in_ev_matches_what_the_plasma_literature_quotes(pinned):
    """A cross-check against an unrelated statement of the same physics, not a second
    measurement of it: 11.548 eV is the figure the discharge literature uses."""
    assert ASD_1S5_3P2 / CM_PER_EV == pytest.approx(11.548, abs=1e-3)
    assert ASD_1S3_3P0 / CM_PER_EV == pytest.approx(11.723, abs=1e-3)


def test_the_entry_is_neutral_so_no_electron_convention_enters(entry):
    """PlasmaCationThermo's whole reference-state discussion turns on the electron being
    created or destroyed. Nothing is, here. If this species ever acquires charge, that
    discussion becomes load-bearing and this test is the tripwire."""
    assert entry.item.get_net_charge() == 0
    assert entry.item.multiplicity == 3


# =====================================================================================
# 3. The whole path: load, perceive, resolve
# =====================================================================================

def test_the_library_loads_alongside_every_other_thermo_library(thermo_db):
    on_disk = {f[:-3] for f in os.listdir(LIBRARY_DIR) if f.endswith('.py')}
    assert LIBRARY in on_disk
    assert len(thermo_db.libraries) == len(on_disk), (
        sorted(on_disk - set(thermo_db.libraries)))
    assert list(thermo_db.libraries[LIBRARY].entries) == [LABEL], (
        'the library carries exactly one entry; a second one needs its own level named')


def test_the_species_perceives_as_ar0e(pinned):
    mol = Molecule().from_adjacency_list(AR_META)
    assert mol.atoms[0].atomtype.label == 'Ar0e'
    assert not mol.is_isomorphic(Molecule().from_adjacency_list(AR))
    assert not mol.is_isomorphic(Molecule().from_adjacency_list(ARP))


def test_thermo_comes_from_this_entry_and_not_from_an_estimator(thermo_db):
    """The failure mode this whole file exists to catch is a library that parses and is
    never matched. Measured end to end, not asserted."""
    data = thermo_db.get_thermo_data(_species(AR_META, 'Ar(3P2)'))
    assert 'Thermo library: %s' % LIBRARY in data.comment
    assert 'group additivity' not in data.comment.lower()
    # The 298-vs-298.15 K offset below is RMG's, not this entry's: ThermoData's H298/S298
    # fields are referenced to 298 K (rmgpy/thermo/thermodata.pyx), while every
    # JANAF-sourced entry in this database writes the 298.15 K value into them.
    offset_s = ENTERED_CP * math.log(T0 / 298.0)
    offset_h = ENTERED_CP * 0.15 / 1000.0
    assert offset_s == pytest.approx(0.0105, abs=1e-3)
    assert data.get_entropy(T0) == pytest.approx(ENTERED_S298 + offset_s, abs=2e-3)
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298 + offset_h,
                                                           abs=2e-3)
    for T in (T0, 1000.0, 6000.0):
        assert data.get_heat_capacity(T) == pytest.approx(ENTERED_CP, abs=1e-3)


def test_without_this_library_the_species_cannot_exist_at_all(estimator_only):
    """Why the entry is load-bearing rather than decorative. Group additivity tries HBI,
    saturates the two radicals into an ``ArH2`` that has no atom type, and raises. That
    is a LOUD failure, which is the good kind - nothing is silently fabricated - but it
    is still a failure, and it is the one this library removes.

    Pinned as it is, not fixed: making group additivity answer for metastable argon would
    be inventing a number, which this database's plasma libraries forbid."""
    with pytest.raises(AtomTypeError) as excinfo:
        estimator_only.get_thermo_data(_species(AR_META, 'Ar(3P2)'))
    assert 'Ar' in str(excinfo.value) and '3 lone pairs' in str(excinfo.value)


# =====================================================================================
# 4. The lumping arithmetic, and the correction this ticket made to it
# =====================================================================================

def test_the_two_metastable_levels_are_separated_by_the_asd_gap():
    d_cm = ASD_1S3_3P0 - ASD_1S5_3P2
    assert d_cm == pytest.approx(1409.9052, abs=1e-4)
    assert d_cm / CM_PER_EV == pytest.approx(0.1748, abs=1e-4)
    assert d_cm * HC_NA / 1000.0 == pytest.approx(16.8662, abs=1e-3)
    assert R * T0 / 1000.0 == pytest.approx(2.478957, abs=1e-6)
    assert math.exp(-(d_cm * HC_NA) / (R * T0)) == pytest.approx(1.1096e-3, rel=1e-3)


def test_r_ln_q_alone_understates_the_lumping_difference_by_almost_eightfold():
    """The correction this ticket returned. The electronic entropy of a manifold is
    ``R ln Q + R <E>/RT``; the brief's route carried only the first term. At 298.15 K
    the omitted term is seven times the one kept, because the second level is high and
    thinly populated - exactly the regime where the <E> term dominates."""
    d_kj = (ASD_1S3_3P0 - ASD_1S5_3P2) * HC_NA / 1000.0
    levels = [(5, 0.0), (1, d_kj)]
    s_lump, h_lump, cp_lump = _electronic(levels, T0)
    s_single = R * math.log(5.0)
    q = 5.0 + math.exp(-d_kj * 1000.0 / (R * T0))

    r_ln_q_only = R * math.log(q / 5.0)
    assert r_ln_q_only == pytest.approx(0.00185, abs=1e-5)
    assert s_lump - s_single == pytest.approx(0.01440, abs=1e-5)
    assert (s_lump - s_single) / r_ln_q_only == pytest.approx(7.8, abs=0.1)
    assert h_lump == pytest.approx(0.00374, abs=1e-5)
    assert cp_lump == pytest.approx(0.0854, abs=1e-3)


def test_where_the_lumping_difference_crosses_the_precision_we_quote():
    """S298 is written to 0.001 J/(mol*K) here. The lumping difference is BELOW that only
    under about 207 K - so at the reference temperature the choice is worth 14 last-digits,
    not the ~2 the brief's one-term arithmetic implied. It reaches 1 J/(mol*K) near 1561 K
    and 1.46 at 6000 K."""
    d_kj = (ASD_1S3_3P0 - ASD_1S5_3P2) * HC_NA / 1000.0
    levels = [(5, 0.0), (1, d_kj)]
    s_single = R * math.log(5.0)

    def excess(T):
        return _electronic(levels, T)[0] - s_single

    def crossing(threshold):
        lo, hi = 20.0, 20000.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if excess(mid) < threshold:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    assert crossing(0.001) == pytest.approx(207.1, abs=0.5)
    assert crossing(0.01) == pytest.approx(281.0, abs=0.5)
    assert crossing(0.1) == pytest.approx(449.1, abs=0.5)
    assert crossing(1.0) == pytest.approx(1560.5, abs=1.0)
    assert excess(6000.0) == pytest.approx(1.4594, abs=1e-3)


def test_the_lump_is_rejected_for_being_fitted_not_for_being_large(entry):
    """The magnitudes above argue mildly FOR lumping being harmless, so the reason it is
    declined has to be stated and has to be the real one: a degeneracy-weighted lump
    assumes the two metastables are Boltzmann-distributed at the GAS temperature, which
    in a discharge they are not - that ratio is an output of the plasma kinetics."""
    assert 'FITTED' in entry.long_desc
    assert 'Boltzmann' in entry.long_desc


# =====================================================================================
# 5. What did not change
# =====================================================================================

def test_the_argon_cation_entry_is_untouched(thermo_db):
    arp = thermo_db.libraries[CATION_LIBRARY].entries['[Arp]']
    assert arp.data.H298.value_si / 1000.0 == pytest.approx(1520.581, abs=1e-6)
    assert arp.data.S298.value_si == pytest.approx(166.404, abs=1e-6)
    assert arp.data.Cpdata.value_si[0] == pytest.approx(20.984, abs=1e-6)
    data = thermo_db.get_thermo_data(_species(ARP, 'Ar+'))
    assert 'Thermo library: %s' % CATION_LIBRARY in data.comment


def test_neutral_argon_still_resolves_to_burke_and_not_to_this_library(thermo_db):
    """Disclosure, not approval. The ground-state argon a running mechanism resolves to is
    ``BurkeH2O2``'s 4-figure combustion value (36.98 cal/(mol*K)), 0.110 J/(mol*K) below
    the JANAF Ar-001 figure this entry is anchored on. So the excitation step comes out
    with the right enthalpy and an entropy 0.121 J/(mol*K) high. Re-anchoring BurkeH2O2 is
    another ticket; this test exists so that if anyone does it, the disclosure in the
    longDesc gets revisited with it."""
    ar = thermo_db.get_thermo_data(_species(AR, 'Ar'))
    assert 'Thermo library: BurkeH2O2' in ar.comment
    assert LIBRARY not in ar.comment
    meta = thermo_db.get_thermo_data(_species(AR_META, 'Ar(3P2)'))

    d_h = (meta.get_enthalpy(T0) - ar.get_enthalpy(T0)) / 1000.0
    d_s = meta.get_entropy(T0) - ar.get_entropy(T0)
    assert d_h == pytest.approx(ASD_1S5_3P2 * HC_NA / 1000.0, abs=1e-3)
    assert d_s == pytest.approx(13.5027, abs=2e-3)
    assert d_s - R * math.log(5.0) == pytest.approx(0.1211, abs=2e-3)


#: The one kinetics file that MENTIONS the structure, and does so only in prose: the
#: I-224 commentary recording that this family's old over-broad top would have matched
#: ``Ar u2 p3 c0`` once the atom type landed, and that it no longer does. A mention in a
#: docstring is not a presence in a mechanism; this test tells the two apart.
KINETICS_PROSE_MENTION = os.path.join(
    'kinetics', 'families', 'Plasma_Associative_Ionization_Alkaline_Alkaline', 'groups.py')


def test_no_deck_dictionary_or_kinetics_file_declares_the_metastable(pinned):
    """The species becomes constructible; it does not become present. If some later commit
    puts it into a mechanism, that is a kinetics decision and this test should be the thing
    that makes it deliberate.

    'Declares' means an adjacency-list line, i.e. a real structure in a species dictionary
    or a group. The single prose mention is allowed and is asserted to BE prose."""
    declared, mentioned = [], []
    for root, _dirs, files in os.walk(KINETICS_DIR):
        for name in files:
            if not name.endswith(('.py', '.txt', '.yaml', '.yml')):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, THIS_DATABASE)
            with open(path, encoding='utf-8', errors='replace') as handle:
                lines = handle.read().splitlines()
            for line in lines:
                if 'Ar u2 p3 c0' not in line and 'Ar0e' not in line:
                    continue
                mentioned.append(rel)
                # An adjacency-list line is the whole line, optionally numbered.
                stripped = line.strip()
                if stripped.split(maxsplit=1)[0].rstrip('.').isdigit():
                    declared.append((rel, stripped))
    assert declared == [], declared
    assert set(mentioned) == {KINETICS_PROSE_MENTION}, sorted(set(mentioned))


def test_plasma_air_advertises_metastable_quenching_but_carries_no_metastable(pinned):
    """Named because it is the file a reader will check first and be misled by: PlasmaAir's
    own longDesc says it includes 'metastable quenching', and its dictionary carries only
    ``Ar`` and ``Arp``. Nothing in this ticket changed that."""
    with open(os.path.join(KINETICS_DIR, 'libraries', 'PlasmaAir', 'reactions.py'),
              encoding='utf-8') as handle:
        assert 'metastable quenching' in handle.read()
    with open(os.path.join(KINETICS_DIR, 'libraries', 'PlasmaAir', 'dictionary.txt'),
              encoding='utf-8') as handle:
        dictionary = handle.read()
    assert '1 Ar u0 p4 c0' in dictionary
    assert '1 Ar u1 p3 c+1' in dictionary
    assert 'u2 p3 c0' not in dictionary
