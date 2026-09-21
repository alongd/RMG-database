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
#: (Paschen, LS, E cm^-1, g) for the whole 3p5.4s manifold.
LEVELS_4S = [('1s5', '3P2', ASD_1S5_3P2, 5),
             ('1s4', '3P1', ASD_1S4_3P1, 3),
             ('1s3', '3P0', ASD_1S3_3P0, 1),
             ('1s2', '1P1', ASD_1S2_1P1, 3)]
#: Ar II (3p5 2P*<3/2>) ionisation limit, same ASD retrieval.
ASD_AR_II_LIMIT = 127109.842  # cm^-1
#: Measured metastable lifetime, Katori & Shimizu, Phys. Rev. Lett. 70 (1993) 3545.
TAU_1S5_MEASURED = 38.0       # s

#: NIST-JANAF Ar-001 "Argon (Ar)", the element reference state this entry is anchored on.
JANAF_AR_S298 = 154.845       # J/(mol*K)
JANAF_AR_CP = 20.786          # J/(mol*K), at every tabulated T

#: What is actually in the file.
DERIVED_E0 = 1108.0496        # kJ/mol, what to_wilhoit() derives; the entry states no E0
ENTERED_H298 = 1114.247       # kJ/mol
ENTERED_S298 = 168.227        # J/(mol*K)
ENTERED_CP = 20.786           # J/(mol*K)

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'


def _species(adjacency_list, label=''):
    return Species(label=label,
                   molecule=[Molecule().from_adjacency_list(adjacency_list)])


def _levels_from_entry(entry):
    """The 3p5.4s level table as the SHIPPED entry states it: {Paschen: (E cm^-1, g,
    H298 kJ/mol, S298 J/(mol*K))}.

    Several checks in this file used to recompute their inputs from module constants and
    so could not fail on a wrong shipped value. Reading the table out of the entry is what
    makes them detectors rather than decoration. The regex is deliberately anchored on the
    Paschen label and ``J=``, so a reformatted table fails loudly here instead of silently
    matching the wrong row.
    """
    import re

    out = {}
    for line in entry.long_desc.splitlines():
        m = re.match(r'\s*(1s[2-5])\s+\S+\s+.*?J=\d+\s+([0-9.]+)\s+(\d+)\s+'
                     r'([0-9.]+)\s+([0-9.]+)', line)
        if m:
            out[m.group(1)] = (float(m.group(2)), int(m.group(3)),
                               float(m.group(4)), float(m.group(5)))
    assert set(out) == {'1s5', '1s4', '1s3', '1s2'}, (
        'the entry must state all four 3p5.4s levels; parsed %s' % sorted(out))
    return out


def _quoted(entry, pattern):
    """One float captured out of the entry's own prose, so a test can check the file
    against the engine rather than against a copy of itself."""
    import re

    m = re.search(pattern, entry.long_desc)
    assert m, 'the entry no longer states %r' % pattern
    return float(m.group(1))


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
    """H298 is the 1s5 level energy converted by an exact constant. Nothing else.

    The entry is a NASA, so there is no H298 FIELD to read -- the polynomial is evaluated
    at the reference temperature. That is the point of the form: the file and the API
    return the same number, with no 298-vs-298.15 field offset between them."""
    expected = ASD_1S5_3P2 * HC_NA / 1000.0
    assert expected == pytest.approx(1114.2468, abs=5e-4)
    assert entry.data.get_enthalpy(T0) / 1000.0 == pytest.approx(expected, abs=5e-4)
    assert entry.data.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=1e-6)


def test_e0_is_not_stated_so_there_is_exactly_one_source_of_truth_for_it(entry):
    """Round 55, HIGH-1. An earlier version of this entry stated E0 = H298 = 1114.247,
    reasoning that the spectroscopic term value IS a 0 K quantity and the thermochemical
    dfH(0) of this species IS 1114.247 by cancellation. Both of those are true and the
    field was still wrong, because RMG's E0 is a third quantity: the species' enthalpy at
    0 K obtained by integrating ITS OWN Cp down from the reference temperature, with no
    element correction. The two differ by exactly that correction.

    The field is now absent, so the derivation is the only source."""
    assert entry.data.E0 is None, (
        'E0 must not be stated; see "E0 IS DERIVED, NOT STATED" in the longDesc')
    for required in ('E0 IS DERIVED, NOT STATED', '1108.0527', 'to_wilhoit'):
        assert required in entry.long_desc, required


def test_both_api_paths_now_agree_on_one_e0(entry):
    """The disagreement measured in round 55 was 1114.2470 stored against a derived
    value. With the field gone there is one number, and it is the derived one."""
    derived = entry.data.to_wilhoit().E0.value_si / 1000.0
    assert derived == pytest.approx(DERIVED_E0, abs=1e-3)
    assert entry.data.E0 is None


def test_the_e0_gap_is_the_thermal_enthalpy_and_not_the_298_convention(entry):
    """Round 58 correction. The longDesc used to lean on the 298-vs-298.15 distinction as
    if it explained the ~6.19 kJ/mol gap. It does not, and this pins the arithmetic that
    shows why: the gap is 5/2*R*T, the WHOLE of it, while the 0.15 K of reference-temperature
    ambiguity is worth 3.118 J/mol -- three thousandths of a kJ, the last digit only.

    A test rather than prose because this is precisely the kind of plausible-but-wrong
    attribution that survives review."""
    derived = entry.data.to_wilhoit().E0.value_si / 1000.0
    gap = ENTERED_H298 - derived

    # The gap IS the monatomic thermal enthalpy at the reference temperature.
    assert gap == pytest.approx(2.5 * R * T0 / 1000.0, abs=2e-3)
    assert gap == pytest.approx(6.1974, abs=2e-3)

    # And the 298/298.15 choice is three orders of magnitude too small to explain it.
    convention = 2.5 * R * (T0 - 298.0)
    assert convention == pytest.approx(3.118, abs=1e-3)          # J/mol, not kJ/mol
    assert convention / 1000.0 < gap / 1000.0
    assert gap * 1000.0 / convention > 1000.0, (
        'the thermal enthalpy must dwarf the reference-temperature convention')


def test_the_cation_library_carries_the_same_unfixed_e0_collision(thermo_db):
    """Disclosure, not approval, and deliberately not fixed: PlasmaCationThermo is out of
    this ticket's scope. If someone repairs it, this fails and points them here."""
    arp = thermo_db.libraries[CATION_LIBRARY].entries['[Arp]']
    stated = arp.data.E0.value_si / 1000.0
    derived = arp.data.to_wilhoit(B=1000.0).E0.value_si / 1000.0
    assert stated == pytest.approx(1520.5730, abs=1e-3)
    assert derived == pytest.approx(1514.3867, abs=1e-3)
    assert stated - derived == pytest.approx(6.1863, abs=1e-3)


def test_s298_is_the_ground_state_plus_the_exact_degeneracy_term(entry):
    """S298 = S298(Ar, JANAF Ar-001) + R ln(g*/g0), with g = 2J+1 = 5 against 1.

    Exact, not approximate: translation, mass and standard state are identical between
    the two, so the entire difference is electronic and a single level contributes only
    R ln g."""
    r_ln_5 = R * math.log(5.0)
    assert r_ln_5 == pytest.approx(13.3816, abs=5e-4)
    assert JANAF_AR_S298 + r_ln_5 == pytest.approx(ENTERED_S298, abs=5e-4)
    assert entry.data.get_entropy(T0) == pytest.approx(ENTERED_S298, abs=1e-6)


def test_cp_is_exactly_five_halves_r_at_every_tabulated_temperature(entry):
    """A free monatomic species pinned to ONE electronic level has translation and
    nothing else - no rotation, no vibration, and no Schottky term. Contrast Ar+, whose
    Cp peaks at 22.773 J/(mol*K) near 1000 K precisely because it is a 2P term."""
    five_halves_r = 2.5 * R
    assert five_halves_r == pytest.approx(JANAF_AR_CP, abs=5e-4)
    # Flat across the WHOLE declared range, not merely on a grid of sampled points:
    # for a NASA this is a statement about the coefficients, since a2..a5 are zero.
    # Tolerance note: the entry's coefficients are derived with RMG's OWN gas constant
    # (rmgpy.constants.R = 8.314472, the older CODATA value), while R above is the current
    # 8.314462618. The two differ by 2.3e-5 in 5/2 R. That is the "which R" trap the
    # longDesc warns about, and it is why this is not asserted to 1e-6.
    for T in (200.0, T0, 300.0, 1000.0, 3000.0, 5000.0, 6000.0):
        assert entry.data.get_heat_capacity(T) == pytest.approx(five_halves_r, abs=5e-4)
    # Flatness itself, however, IS exact: every temperature returns the identical value.
    values = {entry.data.get_heat_capacity(T)
              for T in (200.0, T0, 1000.0, 3000.0, 6000.0)}
    assert len(values) == 1, 'Cp must be identical at every temperature, not merely close'
    poly = entry.data.polynomials[0]
    assert poly.c0 == pytest.approx(2.5, abs=1e-12)
    for coeff in (poly.c1, poly.c2, poly.c3, poly.c4):
        assert coeff == 0.0, 'a2..a5 must be identically zero for a constant Cp'
    assert entry.data.Cp0.value_si == pytest.approx(five_halves_r, abs=1e-3)
    assert entry.data.CpInf.value_si == pytest.approx(five_halves_r, abs=1e-3)


def test_the_level_energy_in_ev_matches_what_the_plasma_literature_quotes(entry):
    """A cross-check against an unrelated statement of the same physics, not a second
    measurement of it: 11.548 eV is the figure the discharge literature uses.

    Repointed at the SHIPPED entry. It used to read ``ASD_1S5_3P2 / CM_PER_EV``, two
    module constants, and so passed unchanged whatever the file said - a check that
    cannot fail in the direction the defect lies. The level energy is now recovered from
    the entry's own H298 through the identity that built it, so a wrong shipped H298 puts
    the eV figure out of range and this goes red."""
    shipped_cm = entry.data.get_enthalpy(T0) / HC_NA
    assert shipped_cm == pytest.approx(ASD_1S5_3P2, rel=1e-6), (
        'the shipped entry implies a level energy of %.4f cm^-1, not the ASD 1s5 value'
        % shipped_cm)
    assert shipped_cm / CM_PER_EV == pytest.approx(11.548, abs=1e-3)

    # The 1s3 partner is a property of the entry's own alternatives table, not of a
    # constant this file happens to hold.
    levels = _levels_from_entry(entry)
    assert levels['1s3'][0] / CM_PER_EV == pytest.approx(11.723, abs=1e-3)


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
    # A NASA has no 298 K FIELD to be referenced to the wrong temperature, so the API
    # returns exactly what the file writes. The ThermoData form of this entry did not:
    # it read 168.227 in the file and 168.2375 through the API. That offset is gone, and
    # asserting its absence is what keeps the form from silently reverting.
    assert data.get_entropy(T0) == pytest.approx(ENTERED_S298, abs=1e-6)
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=1e-6)
    thermo_data_offset = ENTERED_CP * math.log(T0 / 298.0)
    assert thermo_data_offset == pytest.approx(0.0105, abs=1e-3)
    assert abs(data.get_entropy(T0) - ENTERED_S298) < thermo_data_offset / 100.0, (
        'the ThermoData 298 K field offset must NOT be present on a NASA entry')
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

def test_the_two_metastable_levels_are_separated_by_the_asd_gap(entry):
    """Repointed at the shipped entry. This used to difference two module constants and
    could therefore not notice a wrong level table in the file.

    The gap is now taken from the entry's own alternatives table, and the table's 1s5 row
    is cross-checked against the entry's H298 - so a level energy that drifts anywhere in
    the file, in the table or in the data, makes this red."""
    levels = _levels_from_entry(entry)
    assert levels['1s5'][0] == pytest.approx(ASD_1S5_3P2, abs=1e-3)
    assert levels['1s3'][0] == pytest.approx(ASD_1S3_3P0, abs=1e-3)
    # the table's own 1s5 row must agree with the shipped data, not merely with ASD
    assert levels['1s5'][2] == pytest.approx(entry.data.get_enthalpy(T0) / 1000.0, abs=1e-3)
    assert levels['1s5'][1] == 5

    d_cm = levels['1s3'][0] - levels['1s5'][0]
    assert d_cm == pytest.approx(_quoted(entry, r'dE\(1s3 - 1s5\) = ([0-9.]+) cm\^-1'),
                                 abs=1e-4)
    assert d_cm / CM_PER_EV == pytest.approx(0.1748, abs=1e-4)
    assert d_cm * HC_NA / 1000.0 == pytest.approx(16.8662, abs=1e-3)
    assert R * T0 / 1000.0 == pytest.approx(2.478957, abs=1e-6)
    assert math.exp(-(d_cm * HC_NA) / (R * T0)) == pytest.approx(1.1096e-3, rel=1e-3)


def test_r_ln_q_alone_understates_the_lumping_difference_by_almost_eightfold(entry):
    """The correction this ticket returned. The electronic entropy of a manifold is
    ``R ln Q + R <E>/RT``; the brief's route carried only the first term. At 298.15 K
    the omitted term is seven times the one kept, because the second level is high and
    thinly populated - exactly the regime where the <E> term dominates.

    Repointed at the shipped entry twice over: the level energies come from the entry's
    own table, and the two term magnitudes are read out of the entry's own prose rather
    than retyped here. The arithmetic used to run entirely on module constants, so it
    proved the formula and said nothing about the file."""
    table = _levels_from_entry(entry)
    d_kj = (table['1s3'][0] - table['1s5'][0]) * HC_NA / 1000.0
    levels = [(table['1s5'][1], 0.0), (table['1s3'][1], d_kj)]
    s_lump, h_lump, cp_lump = _electronic(levels, T0)
    g_single = table['1s5'][1]
    s_single = R * math.log(g_single)
    q = g_single + math.exp(-d_kj * 1000.0 / (R * T0))

    r_ln_q_only = R * math.log(q / g_single)
    assert r_ln_q_only == pytest.approx(0.00185, abs=1e-5)
    assert s_lump - s_single == pytest.approx(0.01440, abs=1e-5)
    assert (s_lump - s_single) / r_ln_q_only == pytest.approx(7.8, abs=0.1)
    assert h_lump == pytest.approx(0.00374, abs=1e-5)
    assert cp_lump == pytest.approx(0.0854, abs=1e-3)

    # ... and the entry's own prose must carry the same three magnitudes, to the digits
    # it prints them at. This is the half that makes a wrong SHIPPED number red.
    assert _quoted(entry, r'298\.15 K :\s*([0-9.]+) J/\(mol\*K\)') == pytest.approx(
        s_lump - s_single, abs=5e-5)
    assert _quoted(entry, r'R\*ln term ([0-9.]+)') == pytest.approx(r_ln_q_only, abs=5e-5)
    assert _quoted(entry, r'<E>/RT term ([0-9.]+)') == pytest.approx(
        (s_lump - s_single) - r_ln_q_only, abs=5e-5)
    assert _quoted(entry, r'low by ([0-9.]+)x') == pytest.approx(
        (s_lump - s_single) / r_ln_q_only, abs=0.1)


def test_where_the_lumping_difference_crosses_the_precision_we_quote(entry):
    """S298 is written to 0.001 J/(mol*K) here. The lumping difference is BELOW that only
    under about 207 K - so at the reference temperature the choice is worth 14 last-digits,
    not the ~2 the brief's one-term arithmetic implied. It reaches 1 J/(mol*K) near 1561 K
    and 1.46 at 6000 K.

    Repointed at the shipped entry: the levels come from the entry's own table, the four
    crossing temperatures are read out of the entry's own sentence, and the precision the
    whole argument is measured against is taken from how many decimals the entry's S298 is
    actually written to. Previously all of that was module constants against module
    constants, which is an arithmetic check wearing a data check's name."""
    table = _levels_from_entry(entry)
    d_kj = (table['1s3'][0] - table['1s5'][0]) * HC_NA / 1000.0
    levels = [(table['1s5'][1], 0.0), (table['1s3'][1], d_kj)]
    s_single = R * math.log(table['1s5'][1])

    # The precision this test is named for, taken from the entry rather than asserted.
    shipped_s298 = entry.data.get_entropy(T0)
    assert shipped_s298 == pytest.approx(ENTERED_S298, abs=1e-3)
    quoted_precision = _quoted(entry, r'([0-9.]+) J/\(mol\*K\) precision at which S298')
    assert quoted_precision == pytest.approx(0.001, rel=1e-9)

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

    # ... and the entry must state the same four crossings, so the file and the
    # arithmetic cannot drift apart silently.
    assert _quoted(entry, r'below one last-digit only\s*\n?\s*under about ([0-9]+) K'
                   ) == pytest.approx(crossing(quoted_precision), abs=1.0)
    for threshold, pattern in ((0.01, r'It crosses 0\.01 at ([0-9]+) K'),
                               (0.1, r'0\.1 at ([0-9]+) K'),
                               (1.0, r'1\.0 at ([0-9]+) K')):
        assert _quoted(entry, pattern) == pytest.approx(crossing(threshold), abs=1.5)
    assert excess(6000.0) == pytest.approx(1.4594, abs=1e-3)


def test_the_lump_is_declined_as_conditional_not_as_fitted(entry):
    """Round 55 correction, in the entry's favour. An earlier draft called the Boltzmann
    state sum FITTED and refused it on charter grounds. That was wrong: the sum is
    analytical, has a closed form and no adjustable parameter, and this file's charter
    does not forbid it. It is declined for being CONDITIONAL on an equilibration that a
    low-pressure discharge does not provide - which is a narrower claim and, unlike the
    charter one, tells a reader when they MAY use it."""
    assert 'analytical, not fitted' in entry.long_desc.lower().replace('  ', ' ')
    assert 'CONDITIONAL' in entry.long_desc
    assert 'Boltzmann' in entry.long_desc
    # and the wrong reason must not have survived anywhere
    assert 'would be a FITTED' not in entry.long_desc


def test_the_lumping_cost_table_is_present_and_its_numbers_are_right(entry):
    """What a reader whose conditions DO justify lumping needs, and the answer depends on
    their temperature. Two-level is the two metastables; four-level is the whole 3p5.4s
    manifold. Re-derived here rather than quoted from the longDesc."""
    single = R * math.log(5.0)
    two = [(g, e) for _p, _t, e, g in LEVELS_4S if _p in ('1s5', '1s3')]
    four = [(g, e) for _p, _t, e, g in LEVELS_4S]

    def manifold(levels, T):
        e0 = min(e for _g, e in levels)
        xs = [(g, (e - e0) * HC_NA / (R * T)) for g, e in levels]
        q = sum(g * math.exp(-x) for g, x in xs)
        mean = sum(g * x * math.exp(-x) for g, x in xs) / q
        return R * (math.log(q) + mean), mean * R * T / 1000.0, q

    s2_298, h2_298, _ = manifold(two, T0)
    assert s2_298 - single == pytest.approx(0.0144, abs=1e-4)
    assert h2_298 == pytest.approx(0.0037, abs=1e-4)

    s2_6k, h2_6k, _ = manifold(two, 6000.0)
    assert s2_6k - single == pytest.approx(1.4594, abs=1e-3)
    assert h2_6k == pytest.approx(2.1053, abs=1e-3)

    s4_6k, h4_6k, q4_6k = manifold(four, 6000.0)
    assert s4_6k - single == pytest.approx(7.1004, abs=1e-3)
    assert h4_6k == pytest.approx(7.7578, abs=1e-3)
    # population of the whole 4s manifold relative to 1s5 alone
    assert q4_6k / 5.0 == pytest.approx(2.011, abs=1e-3)

    for required in ('WHAT LUMPING WOULD COST', '7.1004', '2.1053', '2.011'):
        assert required in entry.long_desc, required


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


#: Every loaded library that carries ground-state argon, with the S298 its entry gives
#: through the API. Measured; two camps 0.113 J/(mol*K) apart. Which one a mechanism gets
#: is decided purely by position in ``library_order``.
AR_CARRIERS = {
    'BurkeH2O2': 154.7348, 'JetSurF2.0': 154.7323, 'Narayanaswamy': 154.8459,
    'SulfurGlarborgMarshall': 154.8459, '2-BTP': 154.7323, 'primaryThermoLibrary': 154.8459,
    'Chernov': 154.7323, 'FFCM1(-)': 154.8459, 'Fluorine': 154.7323, 'USC-Mech-ii': 154.7323,
    'GRI-Mech3.0': 154.7323, 'Klippenstein_Glarborg2016': 154.8459, 'CurranPentane': 154.8459,
    'JetSurF1.0': 154.7323, 'NOx2018': 154.8462,
}


def test_the_ground_state_argon_an_entry_is_anchored_on_is_decided_by_library_order(pinned):
    """Round 55 MEDIUM: this used to hardcode whichever library won locally, so it tested
    the filesystem rather than precedence. It now SETS the order and asserts the rule.

    The finding it guards: an S298 built as "ground state + R ln g" is only as good as the
    ground state the runtime resolves, and fifteen libraries offer one, 0.113 J/(mol*K)
    apart. get_thermo_data_from_libraries returns on the first match over library_order."""
    from rmgpy.data.thermo import ThermoDatabase

    for winner in ('BurkeH2O2', 'primaryThermoLibrary', 'NOx2018'):
        db = ThermoDatabase()
        db.load_libraries(LIBRARY_DIR, libraries=[winner, LIBRARY])
        assert db.library_order[0] == winner
        ar = db.get_thermo_data(_species(AR, 'Ar'))
        assert 'Thermo library: %s' % winner in ar.comment
        assert ar.get_entropy(T0) == pytest.approx(AR_CARRIERS[winner], abs=2e-3)

        meta = db.get_thermo_data(_species(AR_META, 'Ar(3P2)'))
        assert 'Thermo library: %s' % LIBRARY in meta.comment
        d_h = (meta.get_enthalpy(T0) - ar.get_enthalpy(T0)) / 1000.0
        d_s = meta.get_entropy(T0) - ar.get_entropy(T0)
        # The excitation ENTHALPY is right to millijoules whichever ground state wins -
        # every carrier has dfH = 0 for argon, the element. The 0.003 kJ/mol tolerance is
        # the 298-vs-298.15 K field offset again, and it is present or absent depending on
        # whether the winner is a ThermoData (offset, cancels against this entry's) or a
        # NASA (no offset, does not cancel). Contrast the entropy below, which moves by
        # 0.11 - forty times larger - purely on which library won.
        assert d_h == pytest.approx(ASD_1S5_3P2 * HC_NA / 1000.0, abs=5e-3)
        # ... and the entropy error is exactly the winner's own departure from the JANAF
        # value this entry is anchored on, measured on the API scale.
        #
        # This identity got SIMPLER when the entry became a NASA. As a ThermoData it also
        # carried the +0.0105 J/(mol*K) 298-vs-298.15 K field offset, so the residual was
        # a sum of two unrelated traps - 0.110 of precedence plus 0.011 of field convention
        # - and the test needed a hand-added correction term to compare like for like. A
        # NASA has no 298 K field, so only the precedence term survives on this side. Any
        # offset left in the number now belongs to the WINNER, which may still be a
        # ThermoData; that asymmetry is real and is why AR_CARRIERS holds API values.
        assert d_s - R * math.log(5.0) == pytest.approx(
            JANAF_AR_S298 - AR_CARRIERS[winner], abs=1e-3)


def test_with_every_library_loaded_the_anchor_is_whatever_os_walk_put_first(thermo_db):
    """The state of the world as shipped, separate from the rule above.

    Round 58 MEDIUM: this used to assert `Thermo library: BurkeH2O2` outright. That is a
    claim about the FILESYSTEM, not about RMG - load_libraries appends in os.walk order,
    so on a filesystem that enumerates alphabetically `2-BTP` wins instead and the old
    assertion failed for a reason that had nothing to do with this entry. Pinning a
    defect as if it were the design is worse than not pinning it at all.

    So this now asserts what is actually meant, in three parts: SOME carrier wins, the
    winner is the first Ar-carrying library in library_order (the rule), and the resulting
    error in the anchor is that winner's own departure from JANAF (the consequence). The
    identity of the winner is recorded for information and is deliberately not asserted."""
    ar = thermo_db.get_thermo_data(_species(AR, 'Ar'))
    assert 'Thermo library: ' in ar.comment
    assert LIBRARY not in ar.comment, 'this library must never win ground-state argon'

    winner = ar.comment.split('Thermo library: ')[1].split('\n')[0].strip()
    assert winner in AR_CARRIERS, (
        'ground-state argon resolved to %r, which is not a known carrier; the carrier '
        'census in AR_CARRIERS needs updating' % winner)

    # The rule: first Ar-carrying library in library_order wins, whatever that order is.
    carriers_in_order = [lib for lib in thermo_db.library_order if lib in AR_CARRIERS]
    assert carriers_in_order, 'no known argon carrier was loaded at all'
    assert winner == carriers_in_order[0], (
        'get_thermo_data_from_libraries must return on the FIRST match over library_order; '
        'got %r but %r comes first' % (winner, carriers_in_order[0]))

    # The consequence: the anchor error is the winner's own departure from JANAF.
    meta = thermo_db.get_thermo_data(_species(AR_META, 'Ar(3P2)'))
    d_h = (meta.get_enthalpy(T0) - ar.get_enthalpy(T0)) / 1000.0
    d_s = meta.get_entropy(T0) - ar.get_entropy(T0)
    assert d_h == pytest.approx(ASD_1S5_3P2 * HC_NA / 1000.0, abs=5e-3)
    assert d_s - R * math.log(5.0) == pytest.approx(
        JANAF_AR_S298 - AR_CARRIERS[winner], abs=1e-3)

    # And the finding itself: the two camps are ~0.113 J/(mol*K) apart, so WHICH one wins
    # is worth forty times more than any rounding question in this entry.
    spread = max(AR_CARRIERS.values()) - min(AR_CARRIERS.values())
    assert spread == pytest.approx(0.1136, abs=2e-3)
    print('\n  ground-state argon anchor resolved to %r (S298 = %.4f J/(mol*K)); '
          'carrier spread %.4f' % (winner, AR_CARRIERS[winner], spread))


def test_the_anchor_error_the_engine_delivers_is_the_one_the_library_discloses(entry, thermo_db):
    """The detector the load-order hazard did not have.

    The two tests above pin the RULE (first carrier in library_order wins) and the
    IDENTITY (the residual is that winner's own departure from JANAF). Neither notices
    if the anchor moves: both are satisfied by whichever library happens to win. So the
    hazard was disclosed in the entry, correct at the time of writing, and nothing would
    have gone red when it stopped being correct - which is exactly how the superseded
    ``dS = 13.5027 / +0.1211`` pair survived the move to a ``NASA`` form and sat in the
    file beside the new numbers.

    This reads the pair the entry DISCLOSES out of its own text and compares it with what
    the engine delivers right now, with every library loaded. It goes red when either
    moves: when the file drifts from the measurement, and when the resolved ground state
    changes. The identity of the winner is deliberately still not asserted - what is
    asserted is that the file and the runtime agree about the consequence.

    This does NOT close the hazard. Closing it means either re-anchoring ``BurkeH2O2`` or
    giving RMG a way to require a ground-state anchor, and both are other tickets. It
    makes the hazard loud."""
    import re

    text = entry.long_desc
    assert '13.5027' not in text and '+0.1211' not in text, (
        'the superseded ThermoData-form anchor numbers are still in the file, next to '
        'the current ones - a reader now has two and no way to tell which is live')

    d_h_match = re.search(r'dH298\(Ar -> Ar\(3P2\)\)\s*=\s*([0-9.]+)\s*kJ/mol', text)
    d_s_match = re.search(r'dS298\(Ar -> Ar\(3P2\)\)\s*=\s*([0-9.]+)\s*J/\(mol\*K\)', text)
    assert d_h_match and d_s_match, 'the entry must disclose the delivered dH298 and dS298'
    disclosed_h = float(d_h_match.group(1))
    disclosed_s = float(d_s_match.group(1))

    ar = thermo_db.get_thermo_data(_species(AR, 'Ar'))
    meta = thermo_db.get_thermo_data(_species(AR_META, 'Ar(3P2)'))
    winner = ar.comment.split('Thermo library: ')[1].split('\n')[0].strip()
    measured_h = (meta.get_enthalpy(T0) - ar.get_enthalpy(T0)) / 1000.0
    measured_s = meta.get_entropy(T0) - ar.get_entropy(T0)

    moved = ('the ground-state anchor now resolves to %r (S298 = %.4f). The entry '
             'discloses dH = %.4f / dS = %.4f; the engine delivers %.4f / %.4f. Either '
             'the anchor moved or the disclosure drifted - re-measure it and rewrite the '
             'paragraph, do not widen this tolerance.'
             % (winner, ar.get_entropy(T0), disclosed_h, disclosed_s,
                measured_h, measured_s))
    assert measured_h == pytest.approx(disclosed_h, abs=1e-3), moved
    assert measured_s == pytest.approx(disclosed_s, abs=1e-3), moved

    # ... and the residual the entry quotes is the one that follows from the pair.
    residual = measured_s - R * math.log(5.0)
    assert '+%.4f' % residual in text, (
        'the entry quotes an entropy residual that is not %+.4f' % residual)
    print('\n  anchor %r: delivered dH = %.4f kJ/mol, dS = %.4f J/(mol*K), '
          'residual %+.4f - and the entry says so' % (winner, measured_h, measured_s,
                                                      residual))


def test_the_only_kinetics_files_that_MENTION_the_metastable_are_the_five_containments(pinned):
    """A weak but still meaningful check: nothing in the kinetics tree ships this structure
    as a named species or a reacting group.

    It is NOT a reachability check, and an earlier version of this file wrongly used it as
    one. Families match GROUPS, so a literal search cannot see a template match. The real
    question is answered by generation, below.

    The expected set is no longer empty, and that is the point of the change it records:
    five ordinary families now carry a ``forbidden`` group for this structure. Those five
    lines are the ONLY places it may appear - a sixth would mean something started
    declaring metastable argon as reacting chemistry, which is exactly what this check is
    for. The assertion is against the set, not against emptiness, so it fails either way:
    if one of the five disappears, or if a sixth arrives."""
    declared = []
    for root, _dirs, files in os.walk(KINETICS_DIR):
        for name in files:
            if not name.endswith(('.py', '.txt', '.yaml', '.yml')):
                continue
            path = os.path.join(root, name)
            with open(path, encoding='utf-8', errors='replace') as handle:
                lines = handle.read().splitlines()
            for line in lines:
                if 'Ar u2 p3 c0' not in line:
                    continue
                stripped = line.strip()
                if stripped.split(maxsplit=1)[0].rstrip('.').isdigit():
                    declared.append((os.path.relpath(path, THIS_DATABASE), stripped))

    expected = sorted(
        ('kinetics/families/%s/groups.py' % family, '1 %s Ar u2 p3 c0' % label)
        for family, label in CONTAINED_FAMILIES.items())
    assert sorted(declared) == expected, sorted(declared)

    # ... and each of those lines is inside a forbidden() block, not a reacting group.
    for family in CONTAINED_FAMILIES:
        path = os.path.join(KINETICS_DIR, 'families', family, 'groups.py')
        with open(path, encoding='utf-8') as handle:
            text = handle.read()
        head, _sep, tail = text.partition('1 %s Ar u2 p3 c0' % CONTAINED_FAMILIES[family])
        assert head.rstrip().endswith('"""'), family
        assert 'forbidden(' in head.rsplit('entry(', 1)[-1], (
            '%s: the argon group must sit in a forbidden() block, not an entry()' % family)
        assert tail.lstrip().startswith('"""'), family


# ---- reachability: the round-55 HIGH-2 measurement -----------------------------------

PLASMA_FAMILIES = ['Plasma_Electron_Impact_Ionization',
                   'Plasma_Electron_Attachment',
                   'Plasma_Radiative_Recombination',
                   'Plasma_Associative_Ionization_Alkali_Alkali',
                   'Plasma_Associative_Ionization_Alkali_Alkaline',
                   'Plasma_Associative_Ionization_Alkaline_Alkaline']
EII = 'Plasma_Electron_Impact_Ionization'


@pytest.fixture(scope='module')
def kinetics_db(pinned):
    from rmgpy.data.kinetics.database import KineticsDatabase
    db = KineticsDatabase()
    db.load_families(os.path.join(THIS_DATABASE, 'kinetics', 'families'),
                     families=PLASMA_FAMILIES, depositories=['training'])
    return db


def test_exactly_one_PLASMA_family_reaches_it_which_is_not_the_same_as_one_family(kinetics_db):
    """Round 55, HIGH-2, kept - and renamed, because its old name overstated it.

    Loading this library does not add an isolated number: it activates a stepwise
    ionisation channel for argon. Measured by generating, not by grepping - an earlier
    version of this check searched kinetics files for the literal adjacency text, which
    could never have found a template match because families match groups.

    What this test measures is a statement about the SIX PLASMA families, and that is all
    it ever measured. It used to be called ``..._and_exactly_one_family_reaches_it`` and
    the library repeated that phrasing; with six of 140 families loaded, the denominator
    was never there. The all-families measurement is the next test, and it finds five
    more. Both are true; only one of them was being quoted."""
    hits = {}
    for name in PLASMA_FAMILIES:
        reactions = kinetics_db.generate_reactions_from_families(
            [_species(AR_META, 'Ar(3P2)')], products=None, only_families=[name],
            resonance=True)
        if reactions:
            hits[name] = reactions
    assert list(hits) == [EII], sorted(hits)
    assert len(PLASMA_FAMILIES) == 6, 'the denominator this test speaks for'

    reactions = hits[EII]
    assert len(reactions) == 1
    rxn = reactions[0]
    assert [g if isinstance(g, str) else g.label for g in rxn.template] == ['A_rad']
    assert rxn.degeneracy == pytest.approx(1.0)
    assert rxn.electrons == +1
    assert rxn.reversible is False
    assert len(rxn.products) == 1
    product = rxn.products[0].molecule[0]
    assert product.is_isomorphic(Molecule().from_adjacency_list(ARP))


# ---- reachability over ALL families: the measurement with its denominator ------------
#
# The block above is a measurement of six families. This one is the measurement of the
# database, and it finds five more - every one of them an ordinary combustion family that
# builds a covalently bonded argon and then dies in get_thermo_data. Full sweep, 50
# partners, in docs/argon-metastable-thermo/{all_family_reachability,silent_number}_probe.py;
# the tests here use the minimum partner set that exhibits each of the five, so the suite
# does not pay for the full sweep on every run.

#: One partner per ordinary family that reaches this species, chosen to be the cheapest
#: witness of each. The full 50-partner sweep is in the probes.
ORDINARY_WITNESSES = [
    ('H', 'multiplicity 2\n1 H u1 p0 c0\n', 'Birad_R_Recombination'),
    ('N2', '1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}\n', 'R_Addition_MultipleBond'),
    ('C2H5', 'multiplicity 2\n1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n'
             '2 C u1 p0 c0 {1,S} {6,S} {7,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'
             '5 H u0 p0 c0 {1,S}\n6 H u0 p0 c0 {2,S}\n7 H u0 p0 c0 {2,S}\n',
     'Disproportionation'),
    ('HCO', 'multiplicity 2\n1 C u1 p0 c0 {2,D} {3,S}\n2 O u0 p2 c0 {1,D}\n'
            '3 H u0 p0 c0 {1,S}\n', 'CO_Disproportionation'),
    ('HCl', '1 Cl u0 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n', 'Cl_Abstraction'),
]


@pytest.fixture(scope='module')
def all_families_db(pinned):
    """Every family this database ships, not a hand-picked subset. The whole point."""
    from rmgpy.data.kinetics.database import KineticsDatabase
    db = KineticsDatabase()
    db.load_families(os.path.join(THIS_DATABASE, 'kinetics', 'families'),
                     families='all', depositories=['training'])
    return db


CONTAINED_FAMILIES = {'Birad_R_Recombination': '*2',
                      'R_Addition_MultipleBond': '*3',
                      'Disproportionation': '*1',
                      'CO_Disproportionation': '*1',
                      'Cl_Abstraction': '*3'}
CONTAINMENT = 'Ar_metastable_biradical'

#: What each contained family exists FOR. If the containment moves one of these it is not a
#: containment, it is a regression. Birad_R_Recombination's three are the ones its own
#: forbidden-group longDesc names.
CONTAINMENT_CONTROLS = [
    ('Birad_R_Recombination', 'multiplicity 3\n1 O u2 p2 c0\n',
     'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
     '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'),
    ('Birad_R_Recombination', 'multiplicity 3\n1 S u2 p2 c0\n',
     'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
     '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'),
    ('Birad_R_Recombination', 'multiplicity 3\n1 N u2 p1 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n',
     'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
     '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'),
    ('R_Addition_MultipleBond', 'multiplicity 2\n1 H u1 p0 c0\n',
     '1 C u0 p0 c0 {2,D} {3,S} {4,S}\n2 C u0 p0 c0 {1,D} {5,S} {6,S}\n'
     '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n5 H u0 p0 c0 {2,S}\n6 H u0 p0 c0 {2,S}\n'),
    ('Disproportionation', 'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n'
     '2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n',
     'multiplicity 2\n1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n'
     '2 C u1 p0 c0 {1,S} {6,S} {7,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'
     '5 H u0 p0 c0 {1,S}\n6 H u0 p0 c0 {2,S}\n7 H u0 p0 c0 {2,S}\n'),
    ('CO_Disproportionation', 'multiplicity 2\n1 H u1 p0 c0\n',
     'multiplicity 2\n1 C u1 p0 c0 {2,D} {3,S}\n2 O u0 p2 c0 {1,D}\n3 H u0 p0 c0 {1,S}\n'),
    ('Cl_Abstraction', 'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n'
     '2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n',
     '1 Cl u0 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n'),
]


def _detach_containment(db):
    """Lift the five ``forbidden`` entries off the LOADED objects, touching no file.

    Used to show that the containment is what is doing the work - and, in the crash test,
    to reach the failure it prevents. The same trick ``test_eii_quarantine`` uses for the
    quarantine manifest, and for the same reason: the evidence that justifies a guard has
    to stay reproducible after the guard exists."""
    saved = {}
    for family in CONTAINED_FAMILIES:
        if family not in db.families:
            continue                       # this caller loaded a subset; nothing to lift
        forbidden = db.families[family].forbidden
        saved[family] = forbidden.entries.pop(CONTAINMENT)
    assert saved, 'nothing was detached, so whatever follows measures nothing'
    return saved


def _reattach_containment(db, saved):
    for family, entry in saved.items():
        db.families[family].forbidden.entries[CONTAINMENT] = entry


def test_the_containment_is_written_where_each_family_already_says_it_belongs(all_families_db):
    """Five ordinary families carry one ``forbidden`` entry each for metastable argon.

    The label is asserted because it is load-bearing and silently so:
    ``ForbiddenStructures.is_molecule_forbidden`` honours atom labels, so an UNLABELLED
    ``1 Ar u2 p3 c0`` group matches nothing during generation - the molecule's argon is
    already tagged by then and cannot map to an unlabelled group atom. Measured both ways
    while writing this: unlabelled left every reaction in place.

    Also asserted: ``Birad_R_Recombination``'s pre-existing forbidden groups still carry
    the sentence that licenses the addition. If that charter is ever rewritten, the
    justification for the new entry needs rewriting with it."""
    assert len(all_families_db.families) >= 140, (
        'the denominator: %d families loaded' % len(all_families_db.families))
    for family, label in sorted(CONTAINED_FAMILIES.items()):
        forbidden = all_families_db.families[family].forbidden
        assert forbidden is not None and CONTAINMENT in forbidden.entries, family
        group = forbidden.entries[CONTAINMENT].item
        assert sorted(group.get_all_labeled_atoms()) == [label], (
            '%s: the forbidden group must be labelled %s or it matches nothing'
            % (family, label))

    charter = all_families_db.families['Birad_R_Recombination'].forbidden
    licence = ' '.join(e.long_desc or '' for e in charter.entries.values()).split()
    assert 'instances' in licence and 'lone' in licence and 'forbidden' in licence, (
        "Birad_R_Recombination's own forbidden groups used to say that instances with a "
        "different number of lone pairs are forbidden; that sentence is the licence for "
        "the argon entry and it is no longer there")


def test_no_ordinary_family_reaches_the_metastable_any_more(all_families_db):
    """The containment, measured - and measured to be the CAUSE, not a coincidence.

    Three parts, and the middle one is what stops this being a check that cannot fail:

      1. with the containment in place, no ordinary family generates from Ar(3P2);
      2. with it detached from the loaded objects, all five come back - so the assertion
         in (1) is doing work rather than describing a database that never matched;
      3. the intended Plasma_Electron_Impact_Ionization channel is untouched throughout.

    Full 50-partner sweep in docs/argon-metastable-thermo/containment_probe.py; the
    witnesses here are the cheapest exhibit of each family."""
    meta = _species(AR_META, 'Ar(3P2)')

    def reached():
        found = {}
        for label, adj, _family in ORDINARY_WITNESSES:
            for rxn in all_families_db.generate_reactions_from_families(
                    [meta, _species(adj, label)], products=None, resonance=True):
                found.setdefault(rxn.family, set()).add(label)
        return found

    # 1. contained
    contained = reached()
    assert sorted(set(contained) - {EII}) == [], (
        'these ordinary families still reach Ar(3P2): %s' % sorted(contained))

    # 2. and the containment is why
    saved = _detach_containment(all_families_db)
    try:
        uncontained = reached()
    finally:
        _reattach_containment(all_families_db, saved)
    assert sorted(set(uncontained) - {EII}) == sorted(CONTAINED_FAMILIES), (
        'detaching the forbidden entries must bring all five families back; got %s'
        % sorted(uncontained))
    for label, _adj, family in ORDINARY_WITNESSES:
        assert label in uncontained[family], (label, family)

    # 3. re-attached, and the one channel this species is supposed to have still works
    assert sorted(set(reached()) - {EII}) == []
    uni = all_families_db.generate_reactions_from_families(
        [meta], products=None, resonance=True)
    assert [r.family for r in uni] == [EII]


def test_the_containment_does_not_move_the_chemistry_those_families_exist_for(all_families_db):
    """A containment that took real chemistry with it would be a regression wearing a
    fix's name. Each pair below is chemistry the family is FOR, and each must generate.

    ``[H] + HCl`` under ``Cl_Abstraction`` is deliberately NOT in this list: it generates
    zero reactions with the containment and generated zero without it too - it is the
    degenerate identity reaction. That was measured on the reverted file rather than
    assumed, and it is recorded in ``containment_probe.py`` rather than quietly dropped."""
    for family, adj_a, adj_b in CONTAINMENT_CONTROLS:
        rxns = [r for r in all_families_db.generate_reactions_from_families(
            [_species(adj_a, 'a'), _species(adj_b, 'b')], products=None, resonance=True)
            if r.family == family]
        assert rxns, '%s lost %s + %s' % (family, adj_a.split()[-4], adj_b.split()[-4])


def test_the_products_those_families_used_to_build_still_have_no_thermo(all_families_db,
                                                                        thermo_db):
    """The containment hides the crash; it does not make the structures representable.

    With the forbidden entries detached, every argon-bearing product these families build
    still raises ``AtomTypeError`` in ``get_thermo_data``. That is the finding the
    containment is a response to, and it stays measurable after the response exists -
    otherwise the only evidence for the fix would be the fix."""
    meta = _species(AR_META, 'Ar(3P2)')
    saved = _detach_containment(all_families_db)
    try:
        crashed = 0
        for label, adj, family in ORDINARY_WITNESSES:
            rxns = [r for r in all_families_db.generate_reactions_from_families(
                [meta, _species(adj, label)], products=None, resonance=True)
                if r.family == family]
            assert rxns, '%s + %s generated nothing to test' % (family, label)
            for rxn in rxns:
                argon = [p for p in rxn.products
                         if any(a.element.symbol == 'Ar' for a in p.molecule[0].atoms)]
                assert argon, '%s + %s produced no argon at all' % (family, label)
                for prod in argon:
                    fresh = Species(molecule=[prod.molecule[0].copy(deep=True)])
                    with pytest.raises(AtomTypeError):
                        thermo_db.get_thermo_data(fresh)
                    crashed += 1
    finally:
        _reattach_containment(all_families_db, saved)
    assert crashed >= 5, crashed


def test_a_covalent_neutral_argon_cannot_be_given_a_number_by_construction(thermo_db):
    """The "silent bad rate" question, answered structurally rather than by exhaustion.

    A crash stops a job. A NUMBER would be far worse - it reaches a published mechanism
    with nothing raising - so the question is whether any of these paths can produce one.
    It cannot, and the reason does not depend on which partners anyone tried:

      1. RMG refuses ``1 Ar u0 p3 c0 {2,S}`` as an invalid valency, so a neutral argon
         carrying a covalent bond is necessarily a RADICAL;
      2. a radical's thermo is estimated by HBI, which saturates the radical site first;
      3. saturating a one-bond argon gives a two-bond argon, which has no atom type.

    All three are asserted. The 50-partner sweep agrees (``silent_number_probe.py``:
    exactly one of 67 reactions has all products resolvable, and it is the intended
    ionisation channel, which is quarantined).

    Negative control included: an ordinary radical must come back with a number, or this
    test is measuring its own setup."""
    from rmgpy.exceptions import InvalidAdjacencyListError

    # (0) control
    control = thermo_db.get_thermo_data(_species(
        'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
        '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n', 'CH3'))
    assert control.get_enthalpy(T0) > 0.0

    # (1) a closed-shell singly-bonded neutral argon does not exist
    with pytest.raises(InvalidAdjacencyListError):
        Molecule().from_adjacency_list('1 Ar u0 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n')

    # (2)+(3) so every covalent neutral argon is a radical, and HBI kills it
    for adj in ('multiplicity 2\n1 Ar u1 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n',
                'multiplicity 3\n1 Ar u1 p3 c0 {2,S}\n2 Ar u1 p3 c0 {1,S}\n',
                'multiplicity 2\n1 Ar u1 p3 c0 {2,S}\n2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}\n'
                '3 H u0 p0 c0 {2,S}\n4 H u0 p0 c0 {2,S}\n5 H u0 p0 c0 {2,S}\n'):
        mol = Molecule().from_adjacency_list(adj)
        assert [a.atomtype.label for a in mol.atoms][0] == 'Ar0s', (
            'the molecule itself types fine; the failure is downstream, in HBI')
        with pytest.raises(AtomTypeError):
            thermo_db.get_thermo_data(Species(molecule=[mol]))

    # ... and the thing HBI builds is itself unconstructible, which is the mechanism
    with pytest.raises(AtomTypeError):
        Molecule().from_adjacency_list(
            '1 Ar u0 p3 c0 {2,S} {3,S}\n2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n')

    # The one bond-free argon a family does produce is the one that DOES resolve, and it
    # is the intended channel - so the contrast is pinned rather than assumed.
    arp = thermo_db.get_thermo_data(_species(ARP, 'Ar+'))
    assert 'Thermo library: %s' % CATION_LIBRARY in arp.comment


def test_the_crash_would_fire_before_any_kinetics_quarantine_could_intercept_it(pinned):
    """Why "quarantine the families that turned red" was never an available fix, measured
    rather than argued - and why the containment had to be a ``forbidden`` group instead.

    The quarantine gate lives in ``apply_kinetics_to_reaction``. Product thermo is
    generated earlier, inside ``make_new_species`` (``model.py:569`` -> ``:401``), which
    ``make_new_reaction`` calls before it reaches the kinetics gate. So a manifest on
    ``Birad_R_Recombination`` would have refused a rate the job never survives to ask for.
    A ``forbidden`` group runs earlier still, during generation, which is why it works.

    Run through the shipped enlargement path with nothing patched but two recorders, with
    an ordinary reaction as the control, and with the containment detached so the failure
    it prevents is still reachable and still measured."""
    pytest.importorskip('rmgpy.rmg.model')
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy.rmg.model import CoreEdgeReactionModel

    db = RMGDatabase()
    db.load(THIS_DATABASE,
            thermo_libraries=['primaryThermoLibrary', LIBRARY, CATION_LIBRARY],
            kinetics_families=['Birad_R_Recombination', 'R_Recombination'],
            reaction_libraries=[], seed_mechanisms=[], kinetics_depositories=['training'],
            depository=False, solvation=True, surface=False)
    # The containment now prevents the reaction that produces the crash, so it is lifted
    # off the loaded object to reach the failure it exists to prevent. Touches no file.
    saved = _detach_containment(db.kinetics)

    order = []
    orig_thermo = CoreEdgeReactionModel.generate_thermo
    orig_kinetics = CoreEdgeReactionModel.apply_kinetics_to_reaction

    def traced_thermo(self, spc, rename=False):
        order.append('generate_thermo')
        return orig_thermo(self, spc, rename=rename)

    def traced_kinetics(self, reaction):
        order.append('apply_kinetics_to_reaction')
        return orig_kinetics(self, reaction)

    CoreEdgeReactionModel.generate_thermo = traced_thermo
    CoreEdgeReactionModel.apply_kinetics_to_reaction = traced_kinetics
    try:
        def run(reactants):
            del order[:]
            cerm = CoreEdgeReactionModel()
            cerm.kinetics_estimator = 'rate rules'
            rxns = db.kinetics.generate_reactions_from_families(
                reactants, products=None, resonance=True)
            assert rxns, 'nothing generated, so this measures nothing'
            cerm.process_new_reactions(rxns, reactants[0])

        # control: an ordinary pair must go through, and must show the ordering
        h = _species('multiplicity 2\n1 H u1 p0 c0\n', 'H')
        ch3 = _species('multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n'
                       '2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n', 'CH3')
        run([ch3, h])
        assert order, 'nothing was recorded'
        assert order[0] == 'generate_thermo', order[:4]
        assert 'apply_kinetics_to_reaction' in order
        assert order.index('generate_thermo') < order.index('apply_kinetics_to_reaction'), (
            'product thermo must run BEFORE the kinetics gate, or a quarantine could help')

        # the real case: the same path raises, and raises in thermo
        with pytest.raises(AtomTypeError):
            run([_species(AR_META, 'Ar(3P2)'), h])
        assert 'apply_kinetics_to_reaction' not in order, (
            'the job died before the kinetics gate was ever reached')
    finally:
        CoreEdgeReactionModel.generate_thermo = orig_thermo
        CoreEdgeReactionModel.apply_kinetics_to_reaction = orig_kinetics
        _reattach_containment(db.kinetics, saved)


def test_the_library_retracts_the_one_family_claim_and_carries_the_reach_figure(entry):
    """A measurement that is not written down where the reader is does not protect
    anybody. The entry's own text must carry the retraction, the denominator, the named
    families, and the instruction that follows from them."""
    text = entry.long_desc
    assert 'RETRACTED' in text
    assert '140' in text, 'the denominator must be stated, not implied'
    for family in sorted(CONTAINED_FAMILIES):
        assert family in text, family
    assert 'AtomTypeError' in text
    assert 'default' in text, 'whether a plain deck gets these families is the whole point'
    # the silent-number question, answered in the file rather than only in a log
    assert 'silent bad rate' in text
    # the containment, what it is not, and what happens if its commit is dropped
    assert 'forbidden' in text
    assert 'its own commit' in text
    # Round 60. This assertion used to read `'atomtype.py' in text` with the message "the
    # root cause must be named where the reader is", and it was pinning a false claim in
    # place: the owner ruled the atom types correct, so the containment is the fix and not
    # a holding action. What has to be findable now is the opposite statement, and the
    # arithmetic that licenses it.
    assert 'not a workaround' in text.lower(), (
        'the entry must say the containment IS the fix; round 59 said the engine owed one')
    assert '8 - c = bonds + 2p + u' in text, (
        'the arithmetic is what makes the atom types correct; state it where the reader is')
    assert 'root cause' not in text.lower(), (
        'no passage may name a root cause elsewhere; there is none')


def test_a_bond_free_neutral_argon_at_p3_is_u2_or_it_does_not_exist():
    """The arithmetic the whole round-60 framing rests on, pinned against the engine.

    ``8 - c = bonds + 2p + u``, so a bond-free neutral argon with three lone pairs has u2
    and no choice about it. That is why ``Ar0e`` in a MOLECULE is metastable argon
    uniquely, why a family's generic ``u2`` site is RIGHT to match this species, and
    therefore why the five ``forbidden`` blocks are the fix rather than a workaround for
    an engine defect. If a future engine admits a second (u, p, c) at this atom type, the
    argument changes and this goes red - which is the point of asserting it here rather
    than only in a probe log.

    Note what this test is NOT: it is not a claim that ``Ar0e`` constrains ``u``. It does
    not. ``get_atomtype`` never sees ``u``; the adjacency-list VALENCY CHECK is what
    refuses the other four. The two are easy to confuse and the confusion is what round 59
    got wrong, so both halves are exercised below.

    Measured in full by ``docs/argon-metastable-thermo/atomtype_u_determined_probe.py``."""
    built = {}
    for u in range(5):
        adj = 'multiplicity %d\n1 Ar u%d p3 c0\n' % (u + 1, u)
        try:
            mol = Molecule().from_adjacency_list(adj)
            mol.update_atomtypes()
        except Exception:                                # noqa: BLE001 - a refusal is the datum
            continue
        built[u] = mol.atoms[0].atomtype.label

    # positive control first: if NOTHING built, this test is broken and is about to report
    # its own bug as a fact about the database. That is exactly how the probe failed once.
    assert built, 'no argon built at all; the test is broken, not the database'
    assert list(built) == [2], 'only u2 may exist at bond-free p3 c0; built %s' % built
    assert built[2] == 'Ar0e'

    # the other half: perception really does ignore u, so the uniqueness above comes from
    # the valency check and not from the atom type being narrow.
    meta = Molecule().from_adjacency_list('multiplicity 3\n1 Ar u2 p3 c0\n')
    meta.update_atomtypes()
    atom = meta.atoms[0]
    bonds = sum(bond.order for bond in atom.bonds.values())
    assert 8 - atom.charge == bonds + 2 * atom.lone_pairs + atom.radical_electrons
    assert 'R!H' in [generic.label for generic in atom.atomtype.generic], (
        'Ar0e is still generic under R!H - that is correct, and is why the statement of '
        'scope belongs to the families rather than to the atom type')


def test_each_contained_family_says_the_block_is_the_fix_not_a_workaround(all_families_db):
    """Round 60. The five ``forbidden`` blocks shipped with a paragraph headed "NOT THE
    ROOT CAUSE, AND NOT A SUBSTITUTE FOR IT", which named ``Ar0e``'s genericity as the
    root cause and this entry as a stopgap. The owner ruled that wrong. A retraction that
    lives only in a report does not reach the person reading the family file, so each of
    the five must carry the corrected framing in its own longDesc."""
    for family in sorted(CONTAINED_FAMILIES):
        text = all_families_db.families[family].forbidden.entries[CONTAINMENT].long_desc
        assert 'NOT THE ROOT CAUSE' not in text, (
            '%s still carries the retracted framing' % family)
        assert '8 - c = bonds + 2p + u' in text, family
        assert 'THIS IS THE FIX' in text, family
        # the incompleteness caveat survives, with its meaning changed
        assert 'NOT COMPLETE' in text, family
        assert 'same defect as this one' in text, (
            '%s must say a sixth family would be a family-authoring defect, not an '
            'engine defect returning' % family)


def test_four_of_the_five_ordinary_families_are_in_the_default_recommended_set(pinned):
    """What decides whether this is exotic or routine. ``recommended.py``'s ``default`` is
    the set a deck gets when it names no families at all, and four of the five ordinary
    families that reach this species are in it. Read from the database's own file, so it
    cannot drift from what RMG would load."""
    namespace = {}
    with open(os.path.join(KINETICS_DIR, 'families', 'recommended.py'),
              encoding='utf-8') as handle:
        exec(handle.read(), namespace)                       # noqa: S102
    default = namespace['default']
    ordinary = ['Birad_R_Recombination', 'R_Addition_MultipleBond', 'Disproportionation',
                'CO_Disproportionation', 'Cl_Abstraction']
    in_default = [f for f in ordinary if f in default]
    assert len(in_default) == 4, in_default
    assert 'Cl_Abstraction' not in default, (
        'the one exception, named in the entry; if it joins default, say so there')


def test_the_rate_that_channel_is_handed_is_a_rank_10_lithium_placeholder(kinetics_db):
    """What a user actually gets, and its provenance. The rule is honest about itself -
    its own shortDesc says ESTIMATE - and this pins that honesty in place so that if the
    rule is ever quietly promoted, or re-anchored, this fails."""
    family = kinetics_db.families[EII]
    rules = [e for entries in family.rules.entries.values() for e in entries]
    assert len(rules) == 1, [e.label for e in rules]
    rule = rules[0]
    assert rule.rank == 10
    assert 'ESTIMATE' in rule.short_desc
    assert rule.data.A.value_si == pytest.approx(1.292979e+08, rel=1e-6)
    for required in ('Voronov', 'lithium', 'PLACEHOLDER'):
        assert required in rule.long_desc or required in rule.long_desc.lower(), required


def test_that_rules_premise_that_the_family_cannot_generate_argon_is_now_false(kinetics_db):
    """The rule's longDesc argues its anchor choice partly from "this family CANNOT
    generate argon at all". That was true when written - ground-state argon is u0, outside
    the u[1,2,3,4] template - and this library falsifies it.

    Both halves are pinned: the ground state still generates nothing, and the metastable
    generates one. Fixing the rule's prose is a kinetics ticket this work does not hold, so
    this test is the referral, deliberately failing-visible rather than silent."""
    family = kinetics_db.families[EII]
    ground = kinetics_db.generate_reactions_from_families(
        [_species(AR, 'Ar')], products=None, only_families=[EII], resonance=True)
    assert ground == [], 'ground-state argon should still be outside the template'
    meta = kinetics_db.generate_reactions_from_families(
        [_species(AR_META, 'Ar(3P2)')], products=None, only_families=[EII], resonance=True)
    assert len(meta) == 1
    rule = [e for entries in family.rules.entries.values() for e in entries][0]
    assert 'CANNOT generate argon at all' in rule.long_desc, (
        'the stale premise sentence has moved or been fixed; revisit the disclosure in '
        'PlasmaExcitedNeutralThermo.longDesc with it')


def test_the_metastables_ionisation_threshold_is_below_lithiums(entry):
    """The arithmetic that runs in the rule's favour, and the reason the placeholder is
    not as bad for this species as the rule's own warning implies.

    The rule warns it over-predicts for high-threshold species and names argon at 15.76 eV.
    That is GROUND-STATE argon. Ionising an already-excited atom costs only what is left,
    and 4.21 eV is below the 5.4 eV lithium the estimate is built on - so by the rule's own
    criterion this species is inside its stated range, not outside it."""
    threshold_ev = (ASD_AR_II_LIMIT - ASD_1S5_3P2) / CM_PER_EV
    assert threshold_ev == pytest.approx(4.2113, abs=1e-3)
    assert threshold_ev < 5.4
    assert ASD_AR_II_LIMIT / CM_PER_EV == pytest.approx(15.7596, abs=1e-3)
    assert '4.2113 eV' in entry.long_desc
    assert 'INERT ISLAND' in entry.long_desc


def test_the_island_claim_is_retracted_in_the_file_itself(entry):
    """The retraction has to live where the wrong claim lived, not only in a report."""
    assert 'inert, unreachable island' not in entry.long_desc
    assert 'no channel populates it' not in entry.long_desc
    for required in ('That was false', 'Absence of a string is not absence of a channel'):
        assert required in entry.long_desc, required


# ---- the temperature range actually delivered: round-55 HIGH-3 -----------------------

def test_the_advertised_6000_K_now_survives_normal_processing(thermo_db):
    """Round 58 HIGH-3, INVERTED by the form change.

    The ThermoData form of this entry was refit by process_thermo_data to a hard-coded
    100-5000 K (thermoengine.py:86-99), so the 6000 K it advertised was never delivered.
    The justification for that form - that emitting NASA would mean fitting coefficients -
    was false: for a CONSTANT Cp the coefficients follow algebraically. The entry is now a
    NASA and the range is real. This is the tripwire against reverting the form."""
    pytest.importorskip('rmgpy.thermo.thermoengine')
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy.thermo import NASA
    from rmgpy.thermo.thermoengine import process_thermo_data

    full = RMGDatabase()
    full.load(THIS_DATABASE, thermo_libraries=None, kinetics_families=[EII],
              reaction_libraries=[], seed_mechanisms=[], kinetics_depositories=['training'],
              depository=False, solvation=True, surface=False)
    spc = _species(AR_META, 'Ar(3P2)')
    resolved = full.thermo.get_thermo_data(spc)
    assert isinstance(resolved, NASA), 'the entry must stay a NASA or the range is lost'
    nasa = process_thermo_data(spc, resolved, thermo_class=NASA)

    assert nasa.Tmax.value_si == pytest.approx(6000.0), (
        'processing must preserve the declared ceiling; it does that only for a NASA '
        'whose comment marks it as library-sourced (thermoengine.py:93)')
    assert nasa.get_heat_capacity(6000.0) == pytest.approx(2.5 * R, abs=1e-3)
    assert nasa.get_enthalpy(6000.0) / 1000.0 == pytest.approx(1232.7667, abs=1e-2)
    assert nasa.get_entropy(6000.0) == pytest.approx(230.6254, abs=1e-2)

    # and the derived E0 is what reaches the conformer, on this same path
    assert nasa.E0.value_si / 1000.0 == pytest.approx(DERIVED_E0, abs=1e-2)
    assert spc.conformer.E0.value_si / 1000.0 == pytest.approx(DERIVED_E0, abs=1e-2)
    # the degeneracy RMG carries here is NOT the 5 this entry's S298 assumes
    assert spc.conformer.spin_multiplicity == 1
    assert spc.molecule[0].multiplicity == 3


def test_being_a_nasa_is_not_enough_the_library_comment_is_the_gate(entry):
    """The preservation above is gated on a condition that is easy to satisfy by accident
    and easy to lose (thermoengine.py:93):

        if "Thermo library" in thermo0.comment and isinstance(thermo0, NASA):

    A bare NASA with no library comment is refit to 100-5000 K regardless of its declared
    range. Pinned because "it is a NASA, so the range is safe" is the wrong rule."""
    pytest.importorskip('rmgpy.thermo.thermoengine')
    import copy
    from rmgpy.thermo import NASA
    from rmgpy.thermo.thermoengine import process_thermo_data

    class _Shim(object):
        def __init__(self):
            self.thermo = None
            self.conformer = None

    bare = copy.deepcopy(entry.data)
    bare.comment = ''
    refit = process_thermo_data(_Shim(), bare, thermo_class=NASA)
    assert refit.Tmax.value_si == pytest.approx(5000.0)
    with pytest.raises(ValueError):
        refit.get_entropy(6000.0)

    stamped = copy.deepcopy(entry.data)
    stamped.comment = 'Thermo library: %s' % LIBRARY
    kept = process_thermo_data(_Shim(), stamped, thermo_class=NASA)
    assert kept.Tmax.value_si == pytest.approx(6000.0)


def test_thermodata_freezes_entropy_whenever_the_last_cp_slope_is_nonpositive(entry):
    """Round 58 MEDIUM, raised in severity and broadened.

    This entry no longer suffers from it - that is one of the reasons for the NASA form -
    but the defect is worth pinning because the obvious reading of it is too narrow on two
    counts. ThermoData freezes S whenever the FINAL Cp SLOPE is nonpositive, which means:

      * it can fire INSIDE a declared Tmax, whenever the tabulated grid ends earlier; and
      * is_temperature_valid cannot repair it, because that guard tests the DECLARED range,
        which is not the condition that triggers the freeze.

    A flat Cp - exactly right for any monatomic species - is a nonpositive slope, so this
    is not an exotic case. Constructed on ThermoData so it stays true of the CLASS rather
    than of this entry.

    Repointed: the ``entry`` argument used to be declared and never touched, so this test
    could not have noticed a wrong shipped value at all. The surrogate ThermoData is now
    built from the SHIPPED Cp, H298 and S298, and the first thing asserted is that the
    entry as shipped does NOT suffer from the defect - which is the reason it is a NASA,
    and is the claim a reader of the longDesc is relying on."""
    from rmgpy.thermo import NASA, ThermoData

    # The shipped entry is a NASA, and out of range a NASA RAISES where a ThermoData
    # silently freezes S and keeps returning numbers. That contrast is the whole reason
    # this entry is immune, so it is asserted first: if the entry ever reverts to a
    # ThermoData, these two lines fail before the class-level demonstration below runs.
    assert isinstance(entry.data, NASA)
    assert entry.data.get_entropy(6000.0) > entry.data.get_entropy(T0)
    for T in (8000.0, 10000.0):
        with pytest.raises(ValueError):
            entry.data.get_entropy(T)

    shipped_cp = entry.data.get_heat_capacity(T0)
    shipped_h298 = entry.data.get_enthalpy(T0) / 1000.0
    shipped_s298 = entry.data.get_entropy(T0)
    assert shipped_cp == pytest.approx(2.5 * R, abs=1e-3)

    def _flat(grid, tmax):
        return ThermoData(
            Tdata=(list(grid), 'K'),
            Cpdata=([shipped_cp] * len(grid), 'J/(mol*K)'),
            H298=(shipped_h298, 'kJ/mol'), S298=(shipped_s298, 'J/(mol*K)'),
            Cp0=(shipped_cp, 'J/(mol*K)'), CpInf=(shipped_cp, 'J/(mol*K)'),
            Tmin=(298.15, 'K'), Tmax=(tmax, 'K'))

    # (a) The grid reaching the declared ceiling: the freeze starts at the ceiling, and
    #     this reproduces the magnitude quoted in the longDesc.
    to_6000 = _flat([298.15, 300.0, 400.0, 500.0, 600.0, 800.0, 1000.0,
                     1500.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0], 6000.0)
    frozen = to_6000.get_entropy(6000.0)
    for T, expected in ((8000.0, 47.838), (10000.0, 106.180)):
        assert to_6000.get_entropy(T) == pytest.approx(frozen, abs=1e-6)
        # H keeps climbing correctly, which is exactly what makes the PAIR wrong.
        assert to_6000.get_enthalpy(T) > to_6000.get_enthalpy(6000.0)
        d_gibbs = T * (2.5 * R * math.log(T / 6000.0)) / 1000.0
        assert d_gibbs == pytest.approx(expected, rel=0.02), (
            'Gibbs error at %.0f K should be ~%.3f kJ/mol' % (T, expected))

    # (b) The grid ending EARLY: the freeze now fires inside the declared Tmax, and
    #     is_temperature_valid still says the temperature is fine. This is the part that
    #     makes the defect broader than "it misbehaves above Tmax".
    to_3000 = _flat([298.15, 500.0, 1000.0, 2000.0, 3000.0], 6000.0)
    early_frozen = to_3000.get_entropy(3000.0)
    for T in (4000.0, 5000.0, 6000.0):
        assert to_3000.is_temperature_valid(T) is True, (
            'the guard reports %.0f K as in range' % T)
        assert to_3000.get_entropy(T) == pytest.approx(early_frozen, abs=1e-6), (
            'S is frozen at %.0f K despite a declared Tmax of 6000' % T)
    # ... and the error is already large well inside the advertised range.
    assert 6000.0 * (2.5 * R * math.log(6000.0 / 3000.0)) / 1000.0 > 80.0


def test_three_different_electronic_state_counts_coexist_for_this_species(entry, thermo_db):
    """Round 55 MEDIUM. g = 5 is what S298 is built on (2J+1 for J = 2); RMG's
    spin_multiplicity is 2S+1 and says 3; an untouched Conformer says 1. They disagree
    because they count different things, and an adjacency list has no J to fix it with.

    Not fixable from the database side - pinned as a disclosure and a tripwire."""
    from rmgpy.statmech import Conformer
    assert Conformer().spin_multiplicity == 1
    spc = _species(AR_META, 'Ar(3P2)')
    assert spc.molecule[0].multiplicity == 3
    assert R * math.log(5.0 / 3.0) == pytest.approx(4.2472, abs=1e-3)
    assert R * math.log(5.0) == pytest.approx(13.3816, abs=1e-3)
    for required in ('RMG GIVES THREE DIFFERENT ANSWERS', '4.2472', 'Is it fixable'):
        assert required in entry.long_desc, required


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


# ---- what the channel actually DELIVERS: round-58 HIGH ------------------------------
#
# Round 58's central finding, and the reason these tests exist in this shape: the previous
# rate test inspected the RULE - its rank, its A factor, its provenance - and never carried
# the reaction through model admission or solver evaluation. A rule-level assertion cannot
# see a defect that happens after the rule is read, and that is exactly where this one
# lives. Inspecting the rule is necessary and is not sufficient.

ELECTRON = '1 e u0 p0 c-1\n'
EV_K = 11604.518          # K per eV
PUBLISHED_EII_3EV = 2.0583e10   # m^3/(mol*s), published state-resolved argon model


@pytest.fixture(scope='module')
def admitted(pinned):
    """The one reaction this library unlocks, carried all the way through the model
    admission path that a real run uses: rate-rule estimate -> fix_barrier_height."""
    pytest.importorskip('rmgpy.rmg.model')
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy.rmg.model import CoreEdgeReactionModel

    db = RMGDatabase()
    db.load(THIS_DATABASE,
            thermo_libraries=['primaryThermoLibrary', LIBRARY, CATION_LIBRARY],
            kinetics_families=[EII], reaction_libraries=[], seed_mechanisms=[],
            kinetics_depositories=['training'], depository=False, solvation=True,
            surface=False)
    fam = db.kinetics.families[EII]
    try:
        fam.add_rules_from_training(thermo_database=db.thermo)
    except Exception:                                            # noqa: BLE001
        pass
    fam.fill_rules_by_averaging_up(verbose=True)

    def generated():
        reactions = db.kinetics.generate_reactions_from_families(
            [_species(AR_META, 'Ar(3P2)')], products=None, only_families=[EII],
            resonance=True)
        assert len(reactions) == 1
        one = reactions[0]
        for s in list(one.reactants) + list(one.products):
            if s.is_electron():
                continue
            if not s.label:
                s.label = str(s)
            s.thermo = db.thermo.get_thermo_data(s)
        return one

    rxn = generated()

    cerm = CoreEdgeReactionModel()
    cerm.kinetics_estimator = 'rate rules'

    # The family now carries a quarantine manifest, written BECAUSE of what the tests below
    # measure, so admission refuses before any of it can be measured. Assert the refusal
    # here rather than suppressing it - a fixture that quietly swallowed the exception would
    # keep passing after the gate stopped firing - then detach the quarantine on the loaded
    # object, which touches no file, so the evidence that justifies the manifest stays
    # reproducible now that the manifest exists. The gate itself is tested in
    # test/test_eii_quarantine.py.
    from rmgpy.exceptions import QuarantinedKineticsError
    quarantine = db.kinetics.families[EII].quarantine
    assert quarantine is not None, (
        'this family must carry a quarantine manifest; without it the rate these tests '
        'measure would be admitted to a real mechanism')
    with pytest.raises(QuarantinedKineticsError):
        cerm.apply_kinetics_to_reaction(rxn)
    assert rxn.kinetics is None, 'a refused reaction must be left exactly as generated'

    db.kinetics.families[EII].quarantine = None
    try:
        rxn = generated()
        cerm.apply_kinetics_to_reaction(rxn)
    finally:
        db.kinetics.families[EII].quarantine = quarantine
    estimated_class = rxn.kinetics.__class__.__name__
    estimated_comment = rxn.kinetics.comment
    rxn.fix_barrier_height(force_positive=True, solvent="")
    return db, rxn, estimated_class, estimated_comment


def test_the_estimate_arrives_as_an_ordinary_arrhenius_with_no_electron_temperature(admitted):
    """The mechanism of the defect, pinned at its origin.

    A rate-rule estimate is an ArrheniusEP, which fix_barrier_height converts to an ordinary
    Arrhenius. Neither carries uses_electron_temperature. Only four classes set that flag
    anywhere in rmgpy/kinetics/arrhenius.pyx, and - measured, not assumed - none of them is
    a superclass of Arrhenius, so no estimate can ever inherit it."""
    from rmgpy.kinetics.arrhenius import (Arrhenius, ArrheniusEP, TwoTemperaturePlasma,
                                          ElectronCollisionPlasma, BadnellRRArrhenius,
                                          VoronovEIArrhenius)
    _db, rxn, estimated_class, _comment = admitted

    assert estimated_class == 'ArrheniusEP'
    assert isinstance(rxn.kinetics, Arrhenius)
    assert getattr(rxn.kinetics, 'uses_electron_temperature', False) is False, (
        'an ordinary Arrhenius must not claim electron-temperature dependence')

    flagged = (TwoTemperaturePlasma, ElectronCollisionPlasma, BadnellRRArrhenius,
               VoronovEIArrhenius)
    for cls in flagged:
        assert not issubclass(cls, Arrhenius), (
            '%s must not be a subclass of Arrhenius, or an estimate could inherit the flag'
            % cls.__name__)
    assert not issubclass(ArrheniusEP, Arrhenius)


def test_the_barrier_is_set_by_the_mixed_sibling_e0_convention(admitted):
    """Round 58 correction to the review question, and a finding in its own right.

    fix_barrier_height raises an endothermic barrier to the reaction enthalpy at ZERO K
    (rmgpy/reaction.py:1401-1403), where a species with no stated E0 falls back to
    to_wilhoit().E0. PlasmaCationThermo STATES E0 and this library DERIVES it, so the two
    siblings are read on two different conventions inside a single subtraction, and the
    inconsistency lands directly in an activation energy.

    The review question expected 406.334 kJ/mol - which is dHrxn(298), the value both
    conventions agree on. The delivered barrier is 412.5234, and the 6.1863 difference is
    exactly the cation library's own stated-minus-derived gap.

    The tolerances are deliberately tight. Both absolute numbers moved by +0.0031 kJ/mol
    when this entry became a NASA - that is 5/2*R*0.15, the 298-vs-298.15 K field offset
    ThermoData carried - and the abs=5e-3 this test first used was wide enough to keep
    passing across that move while pinning the superseded value. A tolerance larger than
    the effect under test is not a tolerance. The LEAK is the invariant: it did not move,
    because it belongs to the cation library and not to this one."""
    _db, rxn, _cls, _comment = admitted

    ea = rxn.kinetics.Ea.value_si / 1000.0
    d_h298 = rxn.get_enthalpy_of_reaction(298.0) / 1000.0
    assert d_h298 == pytest.approx(406.3371, abs=1e-3)
    assert ea == pytest.approx(412.5234, abs=1e-3)

    leak = ea - d_h298
    assert leak == pytest.approx(6.1863, abs=1e-3)

    # ... and that leak is the cation library's collision, not a new number.
    arp = _db.thermo.libraries[CATION_LIBRARY].entries['[Arp]']
    stated = arp.data.E0.value_si / 1000.0
    derived = arp.data.to_wilhoit(B=1000.0).E0.value_si / 1000.0
    assert stated - derived == pytest.approx(leak, abs=5e-3)


def test_the_delivered_rate_is_evaluated_at_the_GAS_temperature(admitted):
    """The finding the rule-level tests could not see, measured through actual reactor
    initialisation rather than by reading the rule.

    PlasmaReactor.generate_rate_coefficients branches on
    getattr(kin, 'uses_electron_temperature', False) (rmgpy/solver/plasma.pyx:875). An
    estimate has no such attribute, so it falls to the else branch and is evaluated at
    self.T - the GAS temperature (plasma.pyx:886). An electron-impact ionisation with a
    412 kJ/mol barrier, evaluated at room temperature, is zero.

    The direction matters: the hazard is NOT that the lithium-anchored placeholder is too
    large. It is that the delivered number is ~24 orders of magnitude too SMALL and does
    not depend on Te at all. Re-anchoring the rule would not move it."""
    pytest.importorskip('rmgpy.solver.plasma')
    from rmgpy.solver.plasma import PlasmaReactor
    _db, rxn, _cls, _comment = admitted

    rxn.reversible = False
    electron = _species(ELECTRON, 'e-')
    core = list(rxn.reactants) + list(rxn.products) + [electron]
    seen, uniq = set(), []
    for s in core:
        if id(s) not in seen:
            seen.add(id(s))
            uniq.append(s)
    core = uniq
    for i, s in enumerate(core):
        s.index = i + 1
    fractions = {s: (1e-6 if (s.is_electron() or '+' in str(s)) else 1.0) for s in core}
    total = sum(fractions.values())
    fractions = {s: v / total for s, v in fractions.items()}

    def delivered(t_gas, te_ev):
        reactor = PlasmaReactor(T=(t_gas, 'K'), P=(1.0, 'bar'),
                                initial_mole_fractions=dict(fractions),
                                Te=(te_ev * EV_K, 'K'), charge_balance_species=electron)
        reactor.initialize_model(core_species=core, core_reactions=[rxn],
                                 edge_species=[], edge_reactions=[])
        reactor.generate_rate_coefficients([rxn], [])
        return reactor.kf[reactor.reaction_index[rxn]]

    k300_1ev = delivered(300.0, 1.0)
    k300_3ev = delivered(300.0, 3.0)
    k1000_1ev = delivered(1000.0, 1.0)
    k1000_3ev = delivered(1000.0, 3.0)

    # 1. Te does not enter. This is the whole defect in one assertion.
    assert k300_1ev == k300_3ev, 'tripling Te must not leave the rate unchanged'
    assert k1000_1ev == k1000_3ev

    # 2. The delivered value tracks the GAS temperature instead.
    assert k1000_3ev > k300_3ev * 1e40, (
        'the rate responds to Tgas, which is what proves it is evaluated there')
    # Tolerances tight enough to notice a barrier shift: 5% spans 0.4 kJ/mol at 1000 K and
    # would have absorbed the 0.0031 kJ/mol convention offset that moved these very numbers
    # when the entry became a NASA (they were 1.936048e-64 and 3.665970e-14 on the earlier
    # ThermoData form). 0.2% is still loose against any real regression here, since every
    # input is a fixed constant, and tight enough that the next such shift fails loudly.
    assert k300_3ev == pytest.approx(1.933634e-64, rel=2e-3)
    assert k1000_3ev == pytest.approx(3.664598e-14, rel=2e-3)

    # 3. The direction and scale of the error, against a published value at the same Te.
    assert k1000_3ev < PUBLISHED_EII_3EV
    orders_low = math.log10(PUBLISHED_EII_3EV / k1000_3ev)
    assert orders_low > 20.0, (
        'under-delivered by %.1f orders of magnitude at 1000 K gas' % orders_low)

    # 4. What the same Arrhenius would give if it ever saw the electron temperature.
    at_te = rxn.kinetics.get_rate_coefficient(3.0 * EV_K)
    assert at_te > k1000_3ev * 1e19


def test_nothing_at_the_point_of_use_says_the_rate_is_a_placeholder(admitted):
    """The runtime comment on the generated reaction reads 'Exact match', with no mention
    of rank 10, of the rule being a placeholder, or of lithium. A reader inspecting the
    generated mechanism sees a confident phrase attached to a rate that is wrong by orders
    of magnitude. Pinned as disclosure: if the comment ever gains a qualification, this
    fails and the longDesc paragraph should be revisited with it."""
    _db, _rxn, _cls, comment = admitted
    assert 'Exact match' in comment
    for absent in ('placeholder', 'rank', 'lithium', 'Li', 'estimate'):
        assert absent not in comment, (
            'the point-of-use comment now mentions %r - update the disclosure' % absent)


# ---- the Q = 0 path, and the save/reload round trip ---------------------------------

def test_an_arkane_structure_only_declaration_reports_ready_with_a_zero_partition_function(entry):
    """Round 58 HIGH-2, the part that was missing from both the disclosure and the tests.

    Species.has_statmech takes a shortcut for single-atom species (rmgpy/species.py:528):
    it checks ONLY that conformer.E0 is not None - not that the conformer has modes, and
    not that spin_multiplicity is physical. An ordinary Arkane structure-only species
    declaration defaults spin_multiplicity to 0 (arkane/input.py:157). Compose the two and
    the species reports itself READY while its partition function is exactly zero and its
    conformer entropy is minus infinity. Nothing raises."""
    from rmgpy.statmech import Conformer

    spc = _species(AR_META, 'Ar(3P2)')
    spc.thermo = entry.data
    e0 = entry.data.to_wilhoit().E0.value_si

    spc.conformer = Conformer(E0=(e0, 'J/mol'), modes=[], spin_multiplicity=0,
                              optical_isomers=1)

    assert len(spc.molecule[0].atoms) == 1, 'the shortcut only applies to atomics'
    assert spc.has_statmech() is True, (
        'this is the defect: a zero-multiplicity, mode-less conformer reports READY')

    for T in (T0, 1000.0):
        assert spc.conformer.get_partition_function(T) == 0.0
        assert spc.conformer.get_entropy(T) == float('-inf')

    # The shortcut is what lets it through: with modes required, it would fail.
    assert spc.conformer.E0 is not None
    assert spc.conformer.modes == []


def test_the_conformer_degeneracy_scales_rates_while_library_entropy_does_not_move(entry):
    """The three coexisting counts reach calculations rather than sitting in a field.
    Q is LINEAR in spin_multiplicity, so a TST rate or density of states built from the
    conformer is wrong by 5x against the g = 5 this entry's S298 asserts, or 5/3 once
    statmech has run - while get_entropy, which reads the thermo, does not move at all."""
    from rmgpy.statmech import Conformer

    q = {}
    for g in (1, 3, 5):
        c = Conformer(E0=(0.0, 'J/mol'), modes=[], spin_multiplicity=g, optical_isomers=1)
        q[g] = c.get_partition_function(T0)
        assert q[g] == pytest.approx(float(g), abs=1e-9)

    assert q[5] / q[1] == pytest.approx(5.0, abs=1e-9)
    assert q[5] / q[3] == pytest.approx(5.0 / 3.0, abs=1e-9)

    # ... while the library entropy is untouched by any of it.
    assert entry.data.get_entropy(T0) == pytest.approx(ENTERED_S298, abs=1e-6)


def test_the_entry_survives_a_save_reload_round_trip(entry, tmp_path):
    """The ThermoData branch of the database writer (rmgpy/data/thermo.py:89-99) emits only
    Tdata/Cpdata/H298/S298/Tmin/Tmax - it DROPS Cp0 and CpInf - so a ThermoData library that
    was saved and reloaded produced entries whose to_wilhoit() raised AttributeError, while
    the file on disk looked fine. The NASA branch (thermo.py:113-125) writes both.

    This entry states both and is a NASA, so it round-trips. Pinned because the failure is
    silent until something calls to_wilhoit, which is the E0 path this entry depends on."""
    from rmgpy.data.thermo import ThermoLibrary

    original = entry.data
    assert original.Cp0 is not None and original.CpInf is not None

    out = ThermoLibrary(label=LIBRARY)
    out.load_entry(index=0, label='Ar(3P2)', molecule=AR_META, thermo=original,
                   shortDesc=entry.short_desc, longDesc=entry.long_desc)
    path = str(tmp_path / 'RoundTrip.py')
    out.save(path)

    from rmgpy.data.thermo import ThermoDatabase
    contexts = ThermoDatabase()
    back = ThermoLibrary(label='RoundTrip')
    back.load(path, contexts.local_context, contexts.global_context)
    restored = back.entries['Ar(3P2)'].data

    assert restored.Cp0 is not None, 'Cp0 must survive the writer'
    assert restored.CpInf is not None, 'CpInf must survive the writer'
    assert restored.to_wilhoit().E0.value_si / 1000.0 == pytest.approx(DERIVED_E0, abs=1e-2)
    assert restored.Tmax.value_si == pytest.approx(6000.0)

    # The round trip is NOT bit-exact, and the size of the loss is worth knowing. The writer
    # emits the polynomial through repr(), at SIX significant figures:
    #
    #     a6  133267.5845721773  ->  133268
    #
    # so H298 comes back 3.45 J/mol high and S298 2.4e-5 J/(mol*K) low. The entropy error is
    # negligible against anything this entry cares about; the ENTHALPY error is not quite -
    # 3.45 J/mol exceeds the 1 J/mol (0.001 kJ/mol) precision at which H298 is quoted, and is
    # comparable to the 3.118 J/mol reference-temperature convention documented elsewhere.
    #
    # It does not affect the shipped library, which is hand-maintained and never written by
    # the writer. It WOULD affect anyone who round-trips this library programmatically, so it
    # is pinned rather than left to be discovered.
    assert restored.get_entropy(T0) == pytest.approx(ENTERED_S298, abs=1e-4)
    assert restored.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=5e-3)
    d_h = abs(restored.get_enthalpy(T0) - ENTERED_H298 * 1000.0)
    assert d_h == pytest.approx(3.45, abs=0.5), (
        'the writer truncates a6 to six significant figures; if this changes, the '
        'round-trip precision caveat in the longDesc needs revisiting')
    assert restored.get_entropy(T0) != pytest.approx(ENTERED_S298, abs=1e-9)
