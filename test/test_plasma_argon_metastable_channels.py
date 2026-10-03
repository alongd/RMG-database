#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the metastable-argon channels of ``PlasmaArgon`` (I-232).

Six loss channels of ``Ars`` (the 4s metastable group) were appended at indices 88-93:

* 88 stepwise ionisation ``Ars + e- => Arp + e- + e-``, Ali--Stone BEB Maxwellian fit m3/s;
* 89 electron quenching ``Ars + e- => Ar + e-``, 4.3e-16 Te^0.74 m3/s, one-way;
* 90 pooling ``Ars + Ars => Arp + Ar + e-``, 6.2e-16 m3/s, gas-temperature (constant);
* 91 metastable-to-resonance mixing, entered as ``Ars + e- => Ar + e-`` (the resonance level
  assumed to decay promptly), 2.0e-13 m3/s, Te-independent -- a sensitivity case, not a bound;
* 92 two-body quenching ``Ars + Ar => Ar + Ar``, 3e-15 cm3/s, gas-temperature (constant);
* 93 three-body quenching ``Ars + Ar + Ar => Ar + Ar + Ar``, 1.1e-31 cm6/s, gas-temperature
  (constant), the Ar2 excimer collapsed to its prompt radiative products.

88 is a 5:1-weighted 1s5/1s3 analytic-BEB Maxwellian fit from Ali & Stone 2008. 89 and 91
are Ashida, Lee & Lieberman 1995 as tabulated in Rehman et al. 2016, Table 1; 90, 92 and 93
are Lymberopoulos & Economou 1993, Table I.

The hand-value expectations for entries 88--93 below are arithmetic from their coefficients
at Te = 0.900 eV (10442.07 K), times Avogadro, not the code's own output. The ten stepwise
ionisation expectations at 0.5--6 eV are instead independent BEB Maxwellian quadrature targets.

* 88: fitted BEB law at 0.9 eV = 8.62545e-16 m3/s = 5.19437e8 m3/(mol*s)
* 89: 4.3e-16 * 0.9^0.74                  = 3.97748e-16 m3/s = 2.39529e8 m3/(mol*s)
* 90: 6.2e-16                              = 6.2e-16 m3/s     = 3.73373e8 m3/(mol*s)
* 91: 2.0e-13                              = 2.0e-13 m3/s     = 1.204428e11 m3/(mol*s)
* 92: 3e-15 cm3/s                          = 3e-21 m3/s       = 1.806642e3 m3/(mol*s)
* 93: 1.1e-31 cm6/s                        = 1.1e-43 m6/s     = 3.98928e4 m6/(mol2*s)

89 and 91 share reactants and products, so no reactant/product key can pick one of them; the
tests select them by their pre-exponential factor instead, and require that both survive the
load as separate entries (a MultiArrhenius fold would make 91 impossible to drop on its own).

The two electron-impact channels must be read at Te and NOT at the gas temperature: the
test evaluates them at two gas temperatures and requires the same answer.
"""

import os

import pytest

from rmgpy import settings

LIBRARY = 'PlasmaArgon'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

# Pin before anything imports a database-reading module (see test/conftest.py for why).
settings['database.directory'] = THIS_DATABASE

from plasma_library_selection import reaction_for_isolated  # noqa: E402
from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.kinetics.arrhenius import Arrhenius, TwoTemperaturePlasma  # noqa: E402

TE_EV = 0.900
TE_K = TE_EV * 11604.51812

STEPWISE = (['Ars', 'e-'], ['Arp', 'e-', 'e-'])
QUENCHING = (['Ars', 'e-'], ['Ar', 'e-'])
QUENCHING_A = 4.3e-16
MIXING_A = 2.0e-13
AVOGADRO = 6.02214076e23
POOLING = (['Ars', 'Ars'], ['Ar', 'Arp', 'e-'])
TWO_BODY = (['Ar', 'Ars'], ['Ar', 'Ar'])
THREE_BODY = (['Ar', 'Ar', 'Ars'], ['Ar', 'Ar', 'Ar'])


@pytest.fixture(scope='module')
def library():
    """The loaded library. Load failures surface here, not inside a test."""
    assert settings['database.directory'] == THIS_DATABASE, (
        'RMG resolved database.directory to {0!r}, not this worktree ({1!r}).'.format(
            settings['database.directory'], THIS_DATABASE))
    db = KineticsDatabase()
    db.load_libraries(os.path.join(settings['database.directory'], 'kinetics', 'libraries'),
                      libraries=[LIBRARY])
    return db.libraries[LIBRARY]


def ars_electron_to_ar(library, a_si):
    """The ``Ars + e- => Ar + e-`` entry whose pre-exponential factor is ``a_si`` m3/s per
    molecule (RMG stores it per mole)."""
    pair = [r for r in library.get_library_reactions()
            if sorted(s.label for s in r.reactants) == sorted(QUENCHING[0])
            and sorted(s.label for s in r.products) == sorted(QUENCHING[1])]
    matches = [r for r in pair if r.kinetics.A.value_si == pytest.approx(a_si * AVOGADRO, rel=1e-6)]
    assert len(matches) == 1, [r.kinetics for r in pair]
    return matches[0]


def select(library, channel):
    if channel == 'quenching':
        return ars_electron_to_ar(library, QUENCHING_A)
    if channel == 'mixing':
        return ars_electron_to_ar(library, MIXING_A)
    return reaction_for_isolated(library, *channel)


@pytest.mark.parametrize('channel, expected', [
    (STEPWISE, 5.19437e8),
    ('quenching', 2.39529e8),
    ('mixing', 1.204428e11),
])
def test_electron_impact_channels_are_read_at_te_not_tgas(library, channel, expected):
    """Hand value at Te = 0.900 eV, and the same value at two very different gas temperatures."""
    reaction = select(library, channel)
    assert isinstance(reaction.kinetics, TwoTemperaturePlasma)
    assert reaction.kinetics.uses_electron_temperature
    cold = reaction.kinetics.get_rate_coefficient_two_temp(298.15, TE_K)
    hot = reaction.kinetics.get_rate_coefficient_two_temp(1000.0, TE_K)
    assert cold == pytest.approx(expected, rel=1e-5)
    assert hot == pytest.approx(cold, rel=1e-12)  # float rounding only; a Tgas term would be O(1)


@pytest.mark.parametrize('te_ev, expected', [
    (0.5, 8.90864142e6),
    (1.0, 8.62226844e8),
    (1.5, 4.31046612e9),
    (2.0, 9.96459070e9),
    (2.5, 1.67453719e10),
    (3.0, 2.38845340e10),
    (3.5, 3.09508330e10),
    (4.0, 3.77277889e10),
    (5.0, 5.00976288e10),
    (6.0, 6.08387920e10),
])
def test_stepwise_ionisation_matches_weighted_beb_maxwellian(library, te_ev, expected):
    """5:1-weighted Ali--Stone Eq. 3/Table 4 Maxwellian targets in molar SI.

    These targets are quadrature outputs, not fitted-law outputs. The 4% relative tolerance
    exceeds the independently measured 3.8678% maximum fit error over the validated 0.5--6 eV
    interval, while rejecting the documented endpoint counterexample.
    """
    rate = select(library, STEPWISE).kinetics.get_rate_coefficient_two_temp(298.15, te_ev * 11604.51812)
    assert rate == pytest.approx(expected, rel=0.04, abs=1.0e3)


def test_pooling_is_a_gas_temperature_constant(library):
    """Heavy-particle collision: no electron temperature, and no temperature dependence at all."""
    reaction = reaction_for_isolated(library, *POOLING)
    assert isinstance(reaction.kinetics, Arrhenius)
    assert not getattr(reaction.kinetics, 'uses_electron_temperature', False)
    assert reaction.kinetics.get_rate_coefficient(298.15) == pytest.approx(3.73373e8, rel=1e-5)
    assert reaction.kinetics.get_rate_coefficient(1000.0) == pytest.approx(3.73373e8, rel=1e-5)


@pytest.mark.parametrize('channel, expected', [
    (TWO_BODY, 1.806642e3),
    (THREE_BODY, 3.98928e4),  # RMG's older Avogadro puts it 3.4e-7 high; rel 1e-6 absorbs it
])
def test_neutral_quenching_is_a_gas_temperature_constant(library, channel, expected):
    """Heavy-particle quenching by ground-state argon: plain Arrhenius, no Te, no T dependence."""
    reaction = reaction_for_isolated(library, *channel)
    assert type(reaction.kinetics) is Arrhenius
    assert not getattr(reaction.kinetics, 'uses_electron_temperature', False)
    for t in (298.15, 1000.0):
        assert reaction.kinetics.get_rate_coefficient(t) == pytest.approx(expected, rel=1e-6)


def test_three_body_quenching_is_explicitly_termolecular(library):
    """The third partner is in the label, not a ThirdBody collider the reactor would refuse."""
    reaction = reaction_for_isolated(library, *THREE_BODY)
    assert len(reaction.reactants) == 3 and len(reaction.products) == 3
    assert reaction.kinetics.A.units == 'm^6/(mol^2*s)' or \
        reaction.kinetics.A.value_si == pytest.approx(3.98928e4, rel=1e-6)


def test_mixing_does_not_depend_on_te(library):
    """91 is Te-independent in the source: the same value at Te = 0.3, 0.9 and 3 eV."""
    kinetics = select(library, 'mixing').kinetics
    for te_ev in (0.3, 0.9, 3.0):
        assert kinetics.get_rate_coefficient_two_temp(298.15, te_ev * 11604.51812) == \
            pytest.approx(1.204428e11, rel=1e-6)


def test_quenching_and_mixing_stay_separate_entries(library):
    """Both survive the load as their own TwoTemperaturePlasma reactions, not one Multi."""
    pair = [ars_electron_to_ar(library, a) for a in (QUENCHING_A, MIXING_A)]
    assert all(type(r.kinetics) is TwoTemperaturePlasma for r in pair)
    assert pair[0] is not pair[1]


@pytest.mark.parametrize('channel', [STEPWISE, 'quenching', 'mixing', POOLING, TWO_BODY, THREE_BODY])
def test_channels_are_irreversible_and_balanced(library, channel):
    """The plasma reactor refuses reversible Te-dependent reactions, and quenching is one-way
    by the brief; pooling is irreversible because its reverse is not a channel anyone holds."""
    reaction = select(library, channel)
    assert not reaction.reversible
    assert reaction.is_balanced()


@pytest.mark.parametrize('channel', ['quenching', 'mixing'])
def test_ars_to_ar_channels_carry_the_duplicate_flag(library, channel):
    """89 and 91 duplicate each other. Their reverse direction is also excitation
    ``Ar + e- => Ars + e-`` (I-231, index 87), and the library's load-time duplicate check
    matches in either direction; without the flag the library would not load."""
    assert select(library, channel).duplicate
