#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``PlasmaRadiativeRecombination`` kinetics library.

This library is the database owner of radiative recombination, the electron *sink*
that pairs with the electron *source* pinned in
``test_plasma_electron_impact_ionization.py``. The inventory that chose it, and the
measurements behind the boundary it draws, are in ``docs/i119-recombination-loss.md``.

The path under test is the same four steps the forward half asserts, and each is
asserted separately because each can fail on its own:

1. **load**       - the entry parses, finds its species, and picks up the Badnell fit
                    from ``input/kinetics/badnell.yaml`` by ``(Z, N)``.
2. **balance**    - ``Reaction.is_balanced`` closes the +1 -> 0 charge gap using the
                    ``electrons = -1`` propagated off the rate law.
3. **placement**  - ``resolve_electron_placement`` turns the canonical ``Li+ => Li``
                    into the reactor-facing ``Li+ + e- => Li`` from this library's
                    ``(1, 0)`` declaration, leaving the canonical reaction untouched.
4. **acceptance** - ``PlasmaReactor.initialize_model`` accepts the result and evaluates
                    it at the Badnell rate for the reactor's Te.

WHAT THIS FILE IS ALSO FOR: PINNING A BOUNDARY
----------------------------------------------
Radiative recombination is **not the dominant electron sink** and this suite says so in
assertions rather than only in prose. Two of the tests below exist to keep a later reader
from over-reading a green run:

* ``test_the_implementable_sink_is_three_orders_weaker_than_the_source`` pins
  k_ion/k_RR ~ 1e3 at Te = 1 eV. The channel that ships cannot hold the electron
  density down; it only fixes where the ionisation balance lands.
* ``test_three_body_recombination_still_cannot_be_stored_at_all`` pins the *reason* the
  dominant volume sink is absent - ``TwoTemperaturePlasma`` carries no ``electrons``
  field, so a three-body entry fails the loader's balance check before any question of
  data arises. If RMG-Py ever gives that rate law an electron count, this test fails and
  whoever made that change is told to come back here.

WHERE THE DECLARATION LIVES
---------------------------
``FAMILY_ELECTRON_PLACEMENT`` is a module-level dict in RMG-Py
(``rmgpy/electron_placement.py``); a database repository cannot ship an entry in it.
``LibraryReaction.__init__`` sets ``self.family = library``, so a *library label* is a
valid key there and the one-line addition is

    'PlasmaRadiativeRecombination': (1, 0),

The ``declaration`` fixture below uses that shipped entry when the runtime carries it and
otherwise injects it for the duration of the test, restoring the registry afterwards.
Both paths assert the value is ``(1, 0)``, so this file is green against either runtime --
which is the point, since the two halves of this ticket live in different repositories and
can merge at different times. The corollary bounds what a green run proves: passing does
NOT establish that the RMG-Py entry exists.

Run with the runtime pinned to a branch carrying the widened two-sided declaration::

    cd /home/alon/Code/RMG-database-i119-recombination
    PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH \\
    PYTHONPATH=/home/alon/Code/RMG-Py-i116-ionisation-registry \\
      python -m pytest test/test_plasma_radiative_recombination.py -v
"""

import os

import pytest

from rmgpy import settings

LIBRARY = 'PlasmaRadiativeRecombination'
DECLARATION = (1, 0)
IONIZATION_LIBRARY = 'PlasmaElectronImpactIonization'
IONIZATION_DECLARATION = (1, 2)

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

# Pin before anything imports a database-reading module. RMG's rmgrc resolution ends in
# `return  # fail silently`, and the rmgrc on the runtime branch points at the *shared*
# plasma database, so leaving this to discovery would silently test a checkout that does
# not contain this library.
settings['database.directory'] = THIS_DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.data.kinetics.family import TemplateReaction  # noqa: E402
from rmgpy.electron_balance import get_species_electron_count  # noqa: E402
from rmgpy.exceptions import DatabaseError, ElectronPlacementError  # noqa: E402
from rmgpy.kinetics import (  # noqa: E402
    Arrhenius, BadnellRRArrhenius, TwoTemperaturePlasma, VoronovEIArrhenius)
from rmgpy.molecule import Molecule  # noqa: E402
from rmgpy.species import Species  # noqa: E402
from rmgpy.thermo import NASA, NASAPolynomial  # noqa: E402

import rmgpy.electron_placement as electron_placement  # noqa: E402


EV = 11604.518  #: kelvin per electronvolt, for stating Te the way the plasma literature does


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

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


@pytest.fixture
def reaction(library):
    """A fresh ``LibraryReaction`` per test, so mutation cannot leak between them."""
    reactions = library.get_library_reactions()
    assert len(reactions) == 1
    return reactions[0]


@pytest.fixture
def electron():
    return Species(label='e', molecule=[Molecule().from_adjacency_list('1 e u0 p0 c-1')])


@pytest.fixture
def declaration():
    """Guarantee the ``(1, 0)`` declaration is in the registry for the test's duration.

    Yields ``(declaration, was_shipped)``. When RMG-Py already carries the entry the
    registry is left exactly as it was; otherwise it is injected and removed again, so no
    test can observe a registry this fixture has permanently altered.
    """
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    was_shipped = LIBRARY in registry
    if was_shipped:
        yield registry[LIBRARY], True
    else:
        registry[LIBRARY] = DECLARATION
        try:
            yield DECLARATION, False
        finally:
            del registry[LIBRARY]


def _flat_thermo():
    """A constant-Cp NASA polynomial, enough for the reactor to pack a model.

    The reactor's electron-placement and rate-order acceptance path is what is under test;
    nothing here depends on the thermochemistry being the real one, and the reaction is
    irreversible so no Keq is ever formed from it.
    """
    coeffs = [2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    return NASA(
        polynomials=[NASAPolynomial(coeffs=coeffs, Tmin=(100, 'K'), Tmax=(5000, 'K')),
                     NASAPolynomial(coeffs=coeffs, Tmin=(5000, 'K'), Tmax=(20000, 'K'))],
        Tmin=(100, 'K'), Tmax=(20000, 'K'))


# ---------------------------------------------------------------------------
# Step 1 - load
# ---------------------------------------------------------------------------

def test_library_loads_with_exactly_one_entry(library):
    assert library.label == LIBRARY
    assert len(library.entries) == 1


def test_entry_is_lithium_cation_recombination_written_without_an_explicit_electron(reaction):
    """The canonical database form: ``Li+ => Li``, no electron among the participants.

    The electron is metadata here on purpose. Writing it explicitly *and* keeping a
    nonzero count is double representation, which the resolver refuses outright, and
    writing it explicitly with a zero count would put the database representation out of
    step with every other electron-carrying entry.
    """
    assert [s.label for s in reaction.reactants] == ['[Lip]']
    assert [s.label for s in reaction.products] == ['[Li]']
    assert reaction.reactants[0].molecule[0].get_net_charge() == +1
    assert reaction.products[0].molecule[0].get_net_charge() == 0
    assert not any(s.is_electron() for s in list(reaction.reactants) + list(reaction.products))


def test_kinetics_come_from_the_shipped_badnell_table_not_from_transcribed_numbers(reaction):
    """``BadnellRRArrhenius(Z=3, N=2)`` reads ``input/kinetics/badnell.yaml`` at load.

    Pinned against the table's own Li II -> Li I row rather than against numbers repeated
    here: A = 8.7e-12 cm^3/(molecule*s), B = 0.364, T0 = 147 K, T1 = 7.153e6 K,
    C = 0.1508, T2 = 7.154e5 K. If someone edits the entry to inline an A-factor, or
    points it at a different stage, this fails.
    """
    kinetics = reaction.kinetics
    assert isinstance(kinetics, BadnellRRArrhenius)
    assert kinetics.A.value_si == pytest.approx(8.7e-12 * 1e-6 * 6.02214076e23)
    assert kinetics.B.value_si == pytest.approx(0.364)
    assert kinetics.T0.value_si == pytest.approx(147.0)
    assert kinetics.T1.value_si == pytest.approx(7.153e6)
    assert kinetics.C.value_si == pytest.approx(0.1508)
    assert kinetics.T2.value_si == pytest.approx(7.154e5)
    assert kinetics.uses_electron_temperature
    assert kinetics.uses_electron_density


def test_the_stage_index_means_electrons_before_recombination_so_N_is_two_for_lithium():
    """``N`` counts electrons *prior to* recombination, per the table's own ``notes``.

    Off by one here and the entry silently becomes a different ion's fit: ``N = 3`` is
    neutral Li recombining to Li-, which is not a channel at all, and ``N = 1`` is Li2+.
    The three Li stages carry visibly different A-factors, so the assertion is on the
    number rather than on the index alone.
    """
    import yaml
    path = os.path.join(settings['database.directory'], 'kinetics', 'badnell.yaml')
    with open(path) as handle:
        table = yaml.safe_load(handle)
    block = next(b for b in table['coefficients'] if b['Z'] == 3)
    stages = {int(e['N']): e for e in block['entries']}
    assert sorted(stages) == [0, 1, 2]
    assert float(stages[2]['A']) == pytest.approx(8.7e-12)
    assert 'prior to recombination' in table['notes']


def test_the_electron_count_is_propagated_off_the_rate_law_onto_the_reaction(reaction):
    """``KineticsLibrary.load`` copies ``kinetics.electrons`` onto ``Reaction.electrons``.

    ``load_entry`` takes no electron argument, so without that copy the reaction would
    reach the balance check declaring zero electrons and a perfectly balanced charged
    entry would be rejected. That is not hypothetical - it is exactly what happens to
    three-body recombination, pinned below.
    """
    assert reaction.kinetics.electrons.value == pytest.approx(-1)
    assert reaction.electrons == -1


def test_the_entry_is_one_way(reaction):
    """Irreversible by construction, for two independent reasons.

    The binding ruling requires forward and reverse to be stated as separate one-way
    processes; and ``PlasmaReactor`` refuses a reversible electron-temperature-dependent
    reaction outright, because kf(Tgas, Te)/Keq(Tgas) mixes two thermal closures. The
    inverse of *this* channel is photoionisation, which needs a radiation field the
    reactor does not have, so there is nothing to write even if it were permitted.
    """
    assert reaction.reversible is False


# ---------------------------------------------------------------------------
# Step 2 - balance
# ---------------------------------------------------------------------------

def test_the_canonical_reaction_balances(reaction):
    """Charge closes only because ``electrons = -1`` is folded in.

    Atoms balance trivially (one Li each side); the charge does not - +1 on the left, 0 on
    the right - and ``is_balanced`` closes it with the metadata electron.
    """
    assert reaction.is_balanced()
    assert sum(s.molecule[0].get_net_charge() for s in reaction.reactants) == +1
    assert sum(s.molecule[0].get_net_charge() for s in reaction.products) == 0


# ---------------------------------------------------------------------------
# Step 3 - electron placement
# ---------------------------------------------------------------------------

def test_a_library_label_is_a_valid_placement_key(reaction):
    """``LibraryReaction.family`` is the library label, which is what makes this work."""
    assert reaction.family == LIBRARY
    assert reaction.library == LIBRARY


def test_an_undeclared_library_is_refused_by_name_never_guessed_from_the_net_count(
        reaction, electron):
    """No silent fallback: absence of a declaration is a named failure.

    Worth pinning separately from the ionisation suite's equivalent, because this
    reaction's ``electrons = -1`` is attachment-shaped and ``Plasma_Electron_Attachment``
    already declares ``(1, 0)``. Nothing inherits: an undeclared owner with a shape some
    *other* owner has declared still resolves to nothing.
    """
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.pop(LIBRARY, None)
    try:
        with pytest.raises(ElectronPlacementError) as exc:
            electron_placement.resolve_electron_placement(
                reaction, list(reaction.reactants) + list(reaction.products) + [electron])
        assert 'no electron-placement declaration' in str(exc.value)
    finally:
        if saved is not None:
            registry[LIBRARY] = saved


def test_the_declaration_is_one_electron_in_none_out(declaration):
    """``(1, 0)``: incident order 1, net consumption -1 - the degenerate case.

    Radiative recombination captures its electron, so it has no spectator and the two
    numbers the two-sided schema keeps apart happen to coincide. Recorded as an assertion
    rather than a coincidence: it is why a one-sided declaration served for as long as
    attachment was the only shape, and it is the sanity check that this entry is *not*
    ionisation-shaped.
    """
    value, _shipped = declaration
    assert value == DECLARATION
    reactant_count, product_count = value
    assert reactant_count == 1
    assert product_count == 0
    assert product_count - reactant_count == -1


def test_the_declaration_validates_against_the_reactions_own_electron_count(
        reaction, declaration):
    """The declared net change and the reaction's scalar must agree, and do."""
    (reactant_count, product_count), _shipped = declaration
    assert product_count - reactant_count == reaction.electrons == -1


def test_placement_resolves_to_cation_plus_electron_gives_the_neutral(
        reaction, electron, declaration):
    view = electron_placement.resolve_electron_placement(
        reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    assert [s.label for s in view.reactants] == ['[Lip]', 'e']
    assert [s.label for s in view.products] == ['[Li]']
    assert sum(1 for s in view.reactants if s.is_electron()) == 1
    assert sum(1 for s in view.products if s.is_electron()) == 0
    assert view.electrons == 0
    assert view.reversible is False


def test_the_resolved_view_balances_in_the_E_pseudo_element(reaction, electron, declaration):
    """The structural proof that the declared *sides* were the right sides.

    Counted with ``get_species_electron_count``, the rule the Chemkin and Cantera writers
    use, so the reactor boundary and the export boundary cannot disagree about what
    balances. The count is zero on both sides here rather than one, as it is for
    ionisation: a captured electron is a bound electron, and the cation's deficit is
    exactly what it fills.
    """
    view = electron_placement.resolve_electron_placement(
        reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    assert (sum(get_species_electron_count(s) for s in view.reactants)
            == sum(get_species_electron_count(s) for s in view.products) == 0)


def test_the_rate_order_cross_check_agrees_at_order_two(reaction, electron, declaration):
    """The view has two reactants and the Badnell A-factor is a second-order coefficient.

    A cross-check, never an order source. It is what would catch a declaration whose net
    count is right but whose incident order is not - the error that is otherwise silent
    and shows up only as a rate wrong by a factor of the electron density.
    """
    view = electron_placement.resolve_electron_placement(
        reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    assert electron_placement.RATE_ORDER_AGREES in view.comment
    assert 'order 2' in view.comment


def test_the_canonical_reaction_is_not_mutated_by_resolution(reaction, electron, declaration):
    """The database representation survives the trip; the view is reactor-facing only."""
    before = (reaction.electrons,
              [s.label for s in reaction.reactants],
              [s.label for s in reaction.products])
    electron_placement.resolve_electron_placement(
        reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    assert (reaction.electrons,
            [s.label for s in reaction.reactants],
            [s.label for s in reaction.products]) == before


@pytest.mark.parametrize('wrong,why', [
    ((2, 1), 'right net, wrong order: three reactants against an order-2 coefficient'),
    ((0, 1), 'wrong net: declares +1 against a reaction carrying -1'),
    ((1, 2), 'the ionisation declaration: net +1 against a reaction carrying -1'),
    ((2, 0), 'wrong net: declares -2 against a reaction carrying -1'),
    ((1, 1), 'wrong net: declares 0 against a reaction carrying -1'),
])
def test_a_declaration_that_does_not_match_this_reaction_is_refused(
        reaction, electron, wrong, why):
    """Every wrong two-sided declaration is caught, by one of two distinct guards.

    The net-count guard catches a wrong ``product_count - reactant_count``; the view-shape
    guard catches ``(2, 1)``, whose net is correctly -1 but which would make the reaction
    third order against a ``cm^3/(molecule*s)`` coefficient. Neither subsumes the other,
    and ``(2, 1)`` is the one only the second can see - which matters here more than
    anywhere, because ``(2, 1)`` is precisely the declaration *three-body* recombination
    would carry, and a copy-paste between the two entries is the plausible mistake.
    """
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.get(LIBRARY)
    registry[LIBRARY] = wrong
    try:
        with pytest.raises(ElectronPlacementError):
            electron_placement.resolve_electron_placement(
                reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    finally:
        if saved is None:
            del registry[LIBRARY]
        else:
            registry[LIBRARY] = saved


# ---------------------------------------------------------------------------
# Step 4 - the plasma reactor accepts it
# ---------------------------------------------------------------------------

def test_the_plasma_reactor_accepts_the_reaction_and_evaluates_it_at_the_badnell_rate(
        reaction, electron, declaration):
    """The whole point: acceptance *and* the right number.

    ``PlasmaReactor.initialize_model`` resolves placement itself, so handing it the
    canonical reaction exercises the same path a real model would take. Asserting only
    that it did not raise would miss a view evaluated at the wrong reaction order, which
    is silent; the ``kf`` comparison is what makes it visible.
    """
    from rmgpy.solver.plasma import PlasmaReactor

    Te = 1.0 * EV
    cation, neutral = reaction.reactants[0], reaction.products[0]
    for species in (cation, neutral, electron):
        species.thermo = _flat_thermo()

    reactor = PlasmaReactor(T=(1000, 'K'), P=(1, 'bar'), Te=(Te, 'K'),
                            initial_mole_fractions={cation: 1e-6, neutral: 1.0,
                                                    electron: 1e-6},
                            termination=[])
    reactor.initialize_model(core_species=[cation, neutral, electron],
                             core_reactions=[reaction],
                             edge_species=[], edge_reactions=[])

    assert reactor.electron_index == 2
    assert len(reactor.kf) == 1
    assert reactor.kf[0] == pytest.approx(
        reaction.kinetics.get_rate_coefficient_electron_temp(Te), rel=1e-12)


def test_the_reactor_would_refuse_the_reaction_without_a_declaration(reaction, electron):
    """Without the declaration the reactor refuses, rather than falling back."""
    from rmgpy.solver.plasma import PlasmaReactor

    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.pop(LIBRARY, None)
    cation, neutral = reaction.reactants[0], reaction.products[0]
    for species in (cation, neutral, electron):
        species.thermo = _flat_thermo()
    try:
        reactor = PlasmaReactor(T=(1000, 'K'), P=(1, 'bar'), Te=(1.0 * EV, 'K'),
                                initial_mole_fractions={cation: 1e-6, neutral: 1.0,
                                                        electron: 1e-6},
                                termination=[])
        with pytest.raises(ElectronPlacementError):
            reactor.initialize_model(core_species=[cation, neutral, electron],
                                     core_reactions=[reaction],
                                     edge_species=[], edge_reactions=[])
    finally:
        if saved is not None:
            registry[LIBRARY] = saved


# ---------------------------------------------------------------------------
# The boundary: this sink is real, and it is not the dominant one
# ---------------------------------------------------------------------------

def test_the_implementable_sink_is_three_orders_weaker_than_the_source(reaction):
    """k_ion/k_RR ~ 1e3 at Te = 1 eV, and the ratio is steeply Te-dependent.

    The single most important number this ticket returns, pinned so a later reader cannot
    mistake "the mechanism now has a sink" for "the mechanism now has a sufficient sink".
    Radiative recombination can only balance ionisation once the neutral fraction has
    fallen below k_RR/k_ion - about 1 part in 1000 at Te = 1 eV - so the fixed point this
    two-channel mechanism reaches is near-complete ionisation of the lithium.

    At Te = 0.3 eV the ranking inverts (the 5.4 eV ionisation threshold shuts the source
    off), which is why the conclusion is flagged sensitive to the unratified Te.
    """
    ionization = VoronovEIArrhenius(Z=3, N=3)
    recombination = reaction.kinetics
    at = lambda k, ev: k.get_rate_coefficient_electron_temp(ev * EV)  # noqa: E731

    assert at(ionization, 1.0) / at(recombination, 1.0) == pytest.approx(993.5, rel=1e-3)
    assert at(ionization, 2.0) / at(recombination, 2.0) > 3e4
    # below the threshold the source, not the sink, is the weak one
    assert at(ionization, 0.3) / at(recombination, 0.3) < 1e-3


def test_three_body_recombination_still_cannot_be_stored_at_all(tmp_path):
    """The dominant volume sink is blocked by representation, not only by missing data.

    ``TwoTemperaturePlasma`` is the only shipped rate law that can express a
    Te-dependent third-order coefficient, and it carries no ``electrons`` field.
    ``KineticsLibrary.load`` copies an electron count onto the reaction only from a rate
    law that declares one, and ``load_entry`` takes no electron argument, so a three-body
    entry arrives at ``is_balanced`` claiming zero electrons against a +1 -> 0 charge
    change and is rejected before anything about the *number* is asked.

    This is a tripwire, not a wish: if RMG-Py gives ``TwoTemperaturePlasma`` an
    ``electrons`` field, this test fails, and whoever made that change is pointed at
    ``docs/i119-recombination-loss.md`` to finish the job with a sourced coefficient.
    """
    assert not hasattr(TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,
                                            Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol')),
                       'electrons')
    assert 'TwoTemperaturePlasma' not in electron_placement._NET_ELECTRON_KINETICS_CLASSES

    trial = tmp_path / 'ThreeBodyTrial'
    trial.mkdir()
    (trial / 'dictionary.txt').write_text(
        '[Lip]\n1 Li u0 p0 c+1\n\n[Li]\nmultiplicity 2\n1 Li u1 p0 c0\n\n')
    (trial / 'reactions.py').write_text(
        'name = "ThreeBodyTrial"\n'
        'shortDesc = u""\n'
        'longDesc = u""\n'
        'entry(\n'
        '    index = 0,\n'
        '    label = "[Lip] => [Li]",\n'
        '    degeneracy = 1,\n'
        '    reversible = False,\n'
        "    kinetics = TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,\n"
        "                                    Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol')),\n"
        '    shortDesc = u"Li+ + 2 e- => Li + e-",\n'
        '    longDesc = u"",\n'
        ')\n')

    db = KineticsDatabase()
    with pytest.raises(DatabaseError) as exc:
        db.load_libraries(str(tmp_path), libraries=['ThreeBodyTrial'])
    assert 'was not balanced' in str(exc.value)


# ---------------------------------------------------------------------------
# Coverage: what the table holds and what this library claims
# ---------------------------------------------------------------------------

def test_the_badnell_table_holds_far_more_than_this_library_claims():
    """The gap between the data and the entry list is real and is stated, not hidden.

    33 nuclear charges and 318 (Z, N) stages are in the table; one is claimed here. Only
    ``N = Z - 1`` - a singly charged cation capturing to the neutral - is representable at
    all, and that is present for just 12 of the 33. The rest are multiply charged ions,
    which is a separate representational problem this ticket does not open.
    """
    import yaml
    path = os.path.join(settings['database.directory'], 'kinetics', 'badnell.yaml')
    with open(path) as handle:
        table = yaml.safe_load(handle)
    blocks = table['coefficients']
    assert len(blocks) == 33
    assert sum(len(block['entries']) for block in blocks) == 318
    cation_to_neutral = [b['Z'] for b in blocks
                         if any(int(e['N']) == b['Z'] - 1 for e in b['entries'])]
    assert cation_to_neutral == list(range(1, 13))


def test_argon_can_be_ionised_here_but_cannot_be_radiatively_recombined():
    """The two shipped tables are asymmetric, and the asymmetry lands on the bath gas.

    Ar is this campaign's benchmark bath and ``voronov.yaml`` carries its neutral -> +1
    stage, but ``badnell.yaml``'s Ar block stops at N = 11, so there is no Ar+ + e- => Ar
    fit at all. Five elements are ionisable-but-not-recombinable this way (Al, Si, Ar, K,
    Ca). Pinned because it is a data hole that reads as a modelling choice: an Ar-bath
    mechanism built from these two libraries would create argon ions it can never remove.
    """
    import yaml
    directory = os.path.join(settings['database.directory'], 'kinetics')
    with open(os.path.join(directory, 'voronov.yaml')) as handle:
        voronov = yaml.safe_load(handle)['coefficients']
    with open(os.path.join(directory, 'badnell.yaml')) as handle:
        badnell = yaml.safe_load(handle)['coefficients']

    ionisable = {b['Z'] for b in voronov if any(int(e['N']) == b['Z'] for e in b['entries'])}
    recombinable = {b['Z'] for b in badnell
                    if any(int(e['N']) == b['Z'] - 1 for e in b['entries'])}

    assert 18 in ionisable and 18 not in recombinable          # Ar
    assert sorted(ionisable - recombinable) == [13, 14, 18, 19, 20]   # Al, Si, Ar, K, Ca
    assert sorted(ionisable & recombinable) == [1, 2, 3, 6, 7, 8, 11, 12]


def test_a_species_outside_the_fits_gets_no_reaction_at_all_and_no_rate(library):
    """A library has no template, so an uncovered cation gets nothing - not an estimate.

    This is the property the family-vs-library decision was made on. The check is
    deliberately structural rather than a generation run: there is no matcher to run,
    which is exactly the claim.
    """
    entered = set()
    for reaction in library.get_library_reactions():
        for species in reaction.reactants:
            entered.add(species.molecule[0].to_smiles())
    assert entered == {'[Li+]'}


@pytest.mark.parametrize('symbol,error', [
    ('Be', 'KeyError'),
    ('B', 'KeyError'),
    ('Mg', 'InvalidAdjacencyListError'),
])
def test_three_covered_elements_cannot_be_built_by_rmg_at_all(symbol, error):
    """Not a database gap - RMG cannot build these as the neutral radical ``X u1 p0 c0``.

    Named here so that "the library covers one species" is not read as a database omission
    a family would have fixed. A family could not have reached them either. The exception
    type is pinned per element because the two reasons are distinct and drift between them is
    the class of change this baseline caught: Be and B have no atom type at all
    (``KeyError``); Mg was given an alkaline-earth atom type by RMG-Py commit ``e918cafdd``
    but that odd-electron adjacency list is still rejected (``InvalidAdjacencyListError``).

    Na left this set when ``e918cafdd`` added its atom type - the neutral radical now builds
    - and is pinned by ``test_sodium_now_builds_since_the_atom_type_port``.
    """
    with pytest.raises(Exception) as excinfo:
        Molecule().from_adjacency_list('1 {0} u1 p0 c0'.format(symbol))
    assert type(excinfo.value).__name__ == error


def test_sodium_now_builds_since_the_atom_type_port():
    """The capability the test above used to deny for Na, now pinned so it cannot regress.

    RMG-Py commit ``e918cafdd`` ("Give RMG alkali and alkaline-earth atom types") added Na,
    so the neutral radical ``Na u1 p0 c0`` now constructs to the ``Na0`` atom type rather
    than raising. The library still claims one species and a family still could not have
    reached this - construction is not coverage - but the construction gate is gone,
    deliberately.
    """
    neutral = Molecule().from_adjacency_list('1 Na u1 p0 c0')
    assert neutral.atoms[0].element.symbol == 'Na'
    assert neutral.atoms[0].atomtype.label == 'Na0'


def test_dissociative_recombination_has_no_reactant_to_write():
    """``Li2+`` cannot be constructed, so the channel is blocked at the molecule layer.

    Dissociative recombination ``Li2+ + e- => Li + Li*`` is the dominant electron sink in
    a molecular plasma, and for lithium it is unreachable for a reason that has nothing to
    do with data: ``ATOMTYPES`` has ``Li``, ``Li+`` and ``Li0``, and none of them accepts a
    *bonded* Li+. Neutral Li2 builds fine, which is what makes this a representational
    limit rather than a chemistry one.
    """
    Molecule().from_adjacency_list(
        'multiplicity 1\n1 Li u0 p0 c0 {2,S}\n2 Li u0 p0 c0 {1,S}\n')
    with pytest.raises(Exception):
        Molecule().from_adjacency_list(
            'multiplicity 2\n1 Li u1 p0 c0 {2,S}\n2 Li u0 p0 c+1 {1,S}\n')


# ---------------------------------------------------------------------------
# Negative control: everything that already worked still does
# ---------------------------------------------------------------------------

def _attachment_reaction():
    """``O2 + e- => O2-`` in canonical form, attributed to the attachment family."""
    o2 = Species(label='O2', molecule=[Molecule().from_adjacency_list(
        'multiplicity 3\n1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}\n')])
    anion = Species(label='O2-', molecule=[Molecule().from_adjacency_list(
        'multiplicity 2\n1 O u1 p2 c0 {2,S}\n2 O u0 p3 c-1 {1,S}\n')])
    return TemplateReaction(
        reactants=[o2], products=[anion], electrons=-1, reversible=False,
        family='Plasma_Electron_Attachment',
        kinetics=Arrhenius(A=(1.0e10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol')))


def _cation_recombination_reaction():
    """``Li+ + CH3 + e- => CH3Li`` in canonical form, in the family-forward orientation.

    A control only. ``Cation_R_Recombination`` is a quarantined legacy battery-SEI family
    under a binding ruling; it is not plasma recombination and is not a model for this
    library. It appears here solely to show that adding a registry key did not perturb it.
    """
    cation = Species(label='Lip', molecule=[Molecule().from_adjacency_list('1 Li u0 p0 c+1')])
    methyl = Species(label='CH3', molecule=[Molecule().from_smiles('[CH3]')])
    product = Species(label='CH3Li', molecule=[Molecule().from_smiles('C[Li]')])
    return TemplateReaction(
        reactants=[cation, methyl], products=[product], electrons=-1, reversible=False,
        family='Cation_R_Recombination',
        kinetics=Arrhenius(A=(1.0e10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol')))


def test_the_two_pre_existing_family_declarations_still_read_one_in_none_out():
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    assert registry['Plasma_Electron_Attachment'] == (1, 0)
    assert registry['Cation_R_Recombination'] == (1, 0)


@pytest.mark.parametrize('build,expected_reactants,expected_products', [
    (_attachment_reaction, ['O2', 'e'], ['O2-']),
    (_cation_recombination_reaction, ['Lip', 'CH3', 'e'], ['CH3Li']),
])
def test_attachment_and_cation_recombination_resolve_identically_with_and_without_this_library(
        electron, build, expected_reactants, expected_products):
    """The control that makes "unchanged" a measurement.

    Each shape is resolved twice - once with this library's declaration absent from the
    registry and once with it present - and the two views are compared participant by
    participant. Adding a key to a dict should not perturb the others, and this is doubly
    worth asserting here because the key being added carries the *same* ``(1, 0)`` value
    both of these do.
    """
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.pop(LIBRARY, None)

    def resolve():
        reaction = build()
        species_list = list(reaction.reactants) + list(reaction.products) + [electron]
        view = electron_placement.resolve_electron_placement(reaction, species_list)
        return ([s.label for s in view.reactants],
                [s.label for s in view.products],
                view.electrons)

    try:
        without = resolve()
        registry[LIBRARY] = DECLARATION
        with_recombination = resolve()
    finally:
        registry.pop(LIBRARY, None)
        if saved is not None:
            registry[LIBRARY] = saved

    assert without == with_recombination
    assert without[0] == expected_reactants
    assert without[1] == expected_products
    assert without[2] == 0


def test_the_ionisation_channel_resolves_unchanged_with_this_library_declared(electron):
    """The forward half is untouched: same view, same rate, with and without this key.

    Verifier item 6 in full. The ionisation library is loaded from disk rather than
    reconstructed, so this also catches an accidental edit to the entry on this base -
    which is explicitly out of scope for this ticket.
    """
    db = KineticsDatabase()
    db.load_libraries(os.path.join(settings['database.directory'], 'kinetics', 'libraries'),
                      libraries=[IONIZATION_LIBRARY])
    ionization_library = db.libraries[IONIZATION_LIBRARY]
    assert len(ionization_library.entries) == 1

    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved_ionization = registry.get(IONIZATION_LIBRARY)
    saved_recombination = registry.pop(LIBRARY, None)
    registry[IONIZATION_LIBRARY] = IONIZATION_DECLARATION

    def resolve():
        reaction = ionization_library.get_library_reactions()[0]
        species_list = list(reaction.reactants) + list(reaction.products) + [electron]
        view = electron_placement.resolve_electron_placement(reaction, species_list)
        return ([s.label for s in view.reactants],
                [s.label for s in view.products],
                view.electrons,
                reaction.electrons,
                reaction.kinetics.get_rate_coefficient_electron_temp(1.0 * EV))

    try:
        without = resolve()
        registry[LIBRARY] = DECLARATION
        with_recombination = resolve()
    finally:
        registry.pop(LIBRARY, None)
        if saved_recombination is not None:
            registry[LIBRARY] = saved_recombination
        if saved_ionization is None:
            registry.pop(IONIZATION_LIBRARY, None)
        else:
            registry[IONIZATION_LIBRARY] = saved_ionization

    assert without == with_recombination
    assert without[0] == ['[Li]', 'e']
    assert without[1] == ['[Lip]', 'e', 'e']
    assert without[2] == 0
    assert without[3] == +1
