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
* ``test_three_body_recombination_can_now_be_stored_and_the_remaining_blocker_is_data``
  pins the *reason* the dominant volume sink is absent. **That reason changed under
  I-226, and the test caught it.** It used to read ``..._still_cannot_be_stored_at_all``
  and pinned that ``TwoTemperaturePlasma`` carried no ``electrons`` field, so a
  three-body entry failed the loader's balance check before any question of data arose;
  it promised to fail if RMG-Py ever gave that rate law an electron count. RMG-Py then
  did (the merge *"give TwoTemperaturePlasma a signed-net electron count"*), the test
  fired as designed, and it is now re-pinned: a three-body entry declaring
  ``electrons=-1`` **stores**. But **storage is not representability**: the channel still
  cannot resolve, because no owner declares the ``(2, 1)`` shape it needs, and forcing it
  under the ``(1, 0)`` radiative declaration trips an active rate-order guard that says
  the rate would be wrong by a factor of the electron density. Five tests now cover what
  one did - storage, the wrong-sign refusal, the missing placement declaration, the
  rate-order guard, and a semantic "no third-order coefficient ships here" tripwire.
  Consequence for readers of ``docs/i119-recombination-loss.md``: that document's
  "blocked twice over" headline is still true in *count*, but its second blocker has
  changed identity - from "cannot be stored at all" to "has no placement declaration" -
  while its "Data alone would not unblock it" remains **correct**.

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

from plasma_library_selection import (  # noqa: E402
    assert_reactions_uniquely_keyed, reaction_for)
from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.data.kinetics.family import TemplateReaction  # noqa: E402
from rmgpy.electron_balance import (  # noqa: E402
    get_plasma_rate_order, get_species_electron_count,
)
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


def _reaction_for(library, reactant_label, product_label):
    """Select one library reaction by the channel it is: this reactant to this product.

    **Not** ``get_library_reactions()[0]``, which is what this file did until I-234: that
    form carried ``assert len(reactions) == 1`` inside the fixture, encoding "this library
    has exactly one entry" as a *precondition* of twenty tests rather than as a claim made
    by one. When the library grew a second entry those twenty became setup ERRORS, which
    pytest reports separately from failures -- so the suite lost twenty lithium assertions
    while still printing green for the rest.

    **And not the reactant alone**, which is what replaced it and is the same trap one door
    along. ``[Arp] => [Ar]`` and an excited-state ``[Arp] => Ar*`` share a reactant, so a
    reactant-keyed selector matches two, raises in the fixture, and every dependent test is
    an error again -- on work already queued for this library. The full argument, the
    measured reason the entry label is not usable as a key, and the one residual case are in
    ``plasma_library_selection``; the uniqueness of the key is itself asserted, once, in
    ``test_every_reaction_is_distinguishable_from_every_other``.
    """
    return reaction_for(library, [reactant_label], [product_label])


@pytest.fixture
def reaction(library):
    """The lithium reaction, fresh per test so mutation cannot leak between them."""
    return _reaction_for(library, '[Lip]', '[Li]')


@pytest.fixture
def argon_reaction(library):
    """The argon reaction (I-234), fresh per test. Mirrors ``reaction`` exactly."""
    return _reaction_for(library, '[Arp]', '[Ar]')


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

def test_library_loads_with_the_expected_coverage(library):
    """The one place the library's size is asserted, and it asserts *what* not just *how many*.

    Was ``test_library_loads_with_exactly_one_entry`` until I-234 added argon. A bare count
    is a weak claim -- it passes for any second entry, including a wrong one -- so this now
    pins the coverage set by reactant identity, and the count follows from it. Growing the
    library is meant to fail here, in one place, with a message naming what arrived.
    """
    assert library.label == LIBRARY
    covered = {tuple(s.label for s in r.reactants)
               for r in library.get_library_reactions()}
    assert covered == {('[Lip]',), ('[Arp]',)}, (
        'library coverage changed; update this test and add per-entry checks for the '
        'new entry rather than letting it ride on the existing ones')
    assert len(library.entries) == 2


def test_every_reaction_is_distinguishable_from_every_other(library):
    """No two reactions here share both reactants and products.

    This is the claim that makes every fixture in this file safe. Both entries are
    recombinations of a cation, so they already collide under the reactant-only key this
    file used before round 66; they are separated by their products, and this test is what
    keeps that true. A future ``[Arp] => Ar*`` alongside ``[Arp] => [Ar]`` passes here and
    fails in ``test_library_loads_with_the_expected_coverage``, which is the correct pair
    of outcomes: the selector still works, and the coverage claim argues with you.
    """
    assert_reactions_uniquely_keyed(library)


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


def _write_three_body_trial(tmp_path, electrons_literal=None, name='ThreeBodyTrial'):
    """Write a minimal one-entry library whose rate law is a third-order
    ``TwoTemperaturePlasma``, optionally declaring ``electrons``. ``name`` is the library
    label, which is what ``LibraryReaction`` exposes as ``.family`` and hence what electron
    placement looks up. Returns the library root."""
    trial = tmp_path / name
    trial.mkdir()
    (trial / 'dictionary.txt').write_text(
        '[Lip]\n1 Li u0 p0 c+1\n\n[Li]\nmultiplicity 2\n1 Li u1 p0 c0\n\n')
    kinetics = ("TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,\n"
                "                                    Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol')")
    if electrons_literal is not None:
        kinetics += ', electrons=%s' % electrons_literal
    kinetics += ')'
    (trial / 'reactions.py').write_text(
        'name = "%s"\n'
        'shortDesc = u""\n'
        'longDesc = u""\n'
        'entry(\n'
        '    index = 0,\n'
        '    label = "[Lip] => [Li]",\n'
        '    degeneracy = 1,\n'
        '    reversible = False,\n'
        '    kinetics = %s,\n'
        '    shortDesc = u"Li+ + 2 e- => Li + e-",\n'
        '    longDesc = u"",\n'
        ')\n' % (name, kinetics))
    return trial


def test_three_body_recombination_can_now_be_stored_and_the_remaining_blocker_is_data(tmp_path):
    """THE TRIPWIRE FIRED, AND IT WAS RIGHT TO. This test has been re-pinned under I-226.

    **What this test was written for, and why it was right.** It pinned the *reason* the
    dominant volume sink is absent: ``TwoTemperaturePlasma`` is the only shipped rate law
    that can express a Te-dependent third-order coefficient, and it carried **no**
    ``electrons`` field. ``KineticsLibrary.load`` copies an electron count onto the reaction
    only from a rate law that declares one, so a three-body entry reached ``is_balanced``
    claiming zero electrons against a +1 -> 0 charge change and was refused as unbalanced -
    before any question of *data* arose. So the sink was blocked **twice over**: no shipped
    fit, and no way to store one. That is exactly what ``docs/i119-recombination-loss.md``
    records in its headline, and it was true when written.

    Its docstring then said, in terms: *"if RMG-Py ever gives that rate law an electron
    count, this test fails and whoever made that change is told to come back here."*

    **RMG-Py did exactly that.** The engine tip is the merge *"give TwoTemperaturePlasma a
    signed-net electron count"*. This test went red for precisely the reason it was built to
    go red for - it is a tripwire that worked, not a stale pin - and this re-pin is the
    "come back here" being honoured.

    **What is now measured** (``docs/argon-perception-pins/logs/probe_guarantee_stdout.log``):

      * ``TwoTemperaturePlasma`` **has** an ``electrons`` field, defaulting to ``0``;
      * it **is** in ``_NET_ELECTRON_KINETICS_CLASSES``;
      * a three-body entry declaring ``electrons=-1`` **loads and stores**, carrying
        ``electrons=-1`` onto both the kinetics and the reaction;
      * declaring nothing, or the wrong sign (``electrons=1``), is still refused as
        ``"was not balanced"`` - the balance check still does its job.

    **The STORAGE blocker is gone. The channel is still not representable.** An earlier draft
    of this re-pin said the block was now "data only". **That was wrong, and it is retracted
    here**, because storage is not representability. What I-178 did was lift one blocker and
    *narrow* the others, not remove them:

      * a three-body entry now **stores** (this test);
      * it then **fails electron placement**, because no owner declares the ``(2, 1)`` shape
        the channel needs - measured in
        ``test_three_body_recombination_has_no_placement_declaration_and_cannot_resolve``;
      * forced under an owner that *is* declared, it is refused again by an **active
        rate-order guard** - measured in
        ``test_forcing_three_body_under_the_radiative_declaration_trips_the_rate_order_guard``.

    So the missing pieces are a **placement declaration in RMG-Py** *and* a **sourced
    third-order coefficient**. A declaration is a line of engine code, not data, so "data
    alone" was wrong in kind rather than merely in degree.

    The engine says so itself, in the comment directly above ``FAMILY_ELECTRON_PLACEMENT``
    (``rmgpy/electron_placement.py``): three-body recombination *"would declare ``(2, 1)``.
    That declaration is absent, but the reason narrowed with I-178 ... the storage blocker is
    lifted; what remains absent is this placement declaration and a sourced third-order
    coefficient, neither of which I-178 adds."*

    **Consequence for ``docs/i119-recombination-loss.md``.** That document's "blocked twice
    over" headline is still *true in count*, but its second blocker has changed identity -
    from "cannot be stored at all" to "has no placement declaration" - and its line "Data
    alone would not unblock it" remains **correct**, which the earlier draft wrongly called
    inverted. The document is not edited from this branch; the recommended correction is
    written up in ``docs/argon-perception-pins/report.md``."""
    # The field the old tripwire guarded now exists, with a default of zero. It is a
    # ScalarQuantity, so it is compared through .value - the same convention this file
    # already uses at test_the_loader_copies_the_electron_count_onto_the_reaction.
    law = TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,
                               Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol'))
    assert hasattr(law, 'electrons')
    assert law.electrons.value == pytest.approx(0)
    assert 'TwoTemperaturePlasma' in electron_placement._NET_ELECTRON_KINETICS_CLASSES

    # Declaring the correct count, a three-body entry now STORES. Storage only - the two
    # tests below show it still cannot resolve.
    _write_three_body_trial(tmp_path, electrons_literal='-1')
    db = KineticsDatabase()
    db.load_libraries(str(tmp_path), libraries=['ThreeBodyTrial'])
    entries = list(db.libraries['ThreeBodyTrial'].entries.values())
    assert len(entries) == 1
    assert entries[0].data.electrons.value == pytest.approx(-1)   # ScalarQuantity
    assert entries[0].item.electrons == -1                        # plain int on the reaction

    # ... and the shape the channel would need is declared by nobody.
    assert (2, 1) not in electron_placement.FAMILY_ELECTRON_PLACEMENT.values()


@pytest.mark.parametrize('electrons_literal,why', [
    (None, 'declaring nothing leaves the default 0 against a +1 -> 0 charge change'),
    ('1', 'the wrong sign is a gain, not a loss, of an electron'),
])
def test_a_three_body_entry_with_the_wrong_electron_count_is_still_refused(
        tmp_path, electrons_literal, why):
    """The balance check did not become permissive when the field arrived - only reachable.

    Split out from the tripwire above under I-226. The original test could assert this only
    as "nothing can be stored"; now that the *correct* declaration stores, the fact that an
    *incorrect* one still does not is a separate and newly meaningful guarantee, and it is
    what stops the lifted representational block from becoming a way to ship an unbalanced
    reaction quietly."""
    _write_three_body_trial(tmp_path, electrons_literal=electrons_literal)
    db = KineticsDatabase()
    with pytest.raises(DatabaseError) as exc:
        db.load_libraries(str(tmp_path), libraries=['ThreeBodyTrial'])
    assert 'was not balanced' in str(exc.value), why


def _stored_three_body_reaction(tmp_path, owner):
    """Store the three-body trial under library label ``owner`` and return it as a
    ``LibraryReaction``, whose ``.family`` is that label - which is what the resolver reads.
    ``entry.item`` is a bare ``Reaction`` and carries no ``family``, so it will not do."""
    _write_three_body_trial(tmp_path, electrons_literal='-1', name=owner)
    db = KineticsDatabase()
    db.load_libraries(str(tmp_path), libraries=[owner])
    reactions = db.libraries[owner].get_library_reactions()
    assert len(reactions) == 1
    return reactions[0]


def test_three_body_recombination_has_no_placement_declaration_and_cannot_resolve(
        tmp_path, electron):
    """Blocker two, after I-178 narrowed it: the channel stores, then fails to resolve.

    The shape three-body recombination needs is ``(2, 1)`` - two electrons incident, one
    liberated. Nothing declares it, and ``resolve_electron_placement`` refuses to infer a
    placement from the net count alone, so an entry under an undeclared owner dies with a
    named error. This is what makes "data alone is what is missing" false: the missing piece
    here is a line in RMG-Py's ``FAMILY_ELECTRON_PLACEMENT``, not a number from a paper.

    Measured in ``docs/argon-perception-pins/logs/probe_threebody_stdout.log``."""
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    assert (2, 1) not in registry.values()
    assert [owner for owner, decl in registry.items() if decl == (2, 1)] == []

    owner = 'PlasmaThreeBodyRecombination'
    assert owner not in registry, 'an owner appeared; see docs/i119-recombination-loss.md'
    reaction = _stored_three_body_reaction(tmp_path, owner)
    assert reaction.family == owner
    assert reaction.electrons == -1

    species_list = list(reaction.reactants) + list(reaction.products) + [electron]
    with pytest.raises(ElectronPlacementError) as exc:
        electron_placement.resolve_electron_placement(reaction, species_list)
    assert 'no electron-placement declaration' in str(exc.value)


def test_forcing_three_body_under_the_radiative_declaration_trips_the_rate_order_guard(
        tmp_path, electron, declaration):
    """The rate-order guard is an ACTIVE REFUSAL, not an open question.

    An earlier draft of this ticket framed "does the reactor multiply through by ``n_e`` the
    right number of times?" as an unmeasured engine question. It is not open: the engine
    already guards it, and the guard fires here.

    ``PlasmaRadiativeRecombination`` is declared ``(1, 0)``, whose **net** (-1) matches a
    three-body entry exactly - so net-charge balance alone cannot tell the two apart. What
    separates them is the **incident order**: the declaration builds a two-reactant view,
    while the coefficient is order 3. The engine cross-checks the two and refuses, saying in
    its own message that the rate would otherwise be *"wrong by a factor of the electron
    density while the reaction looks well formed"*.

    So an ad-hoc attempt to smuggle three-body recombination in under the existing
    declaration does not silently produce a wrong rate - it is caught. Pinned so that
    remains true."""
    decl, _was_shipped = declaration
    assert decl == (1, 0)

    owner = 'PlasmaRadiativeRecombination'
    reaction = _stored_three_body_reaction(tmp_path, owner)
    assert reaction.family == owner
    # The net matches the declaration, which is exactly why this case needs its own guard.
    assert reaction.electrons == decl[1] - decl[0] == -1
    assert get_plasma_rate_order(reaction.kinetics) == 3

    species_list = list(reaction.reactants) + list(reaction.products) + [electron]
    with pytest.raises(ElectronPlacementError) as exc:
        electron_placement.resolve_electron_placement(reaction, species_list)
    message = str(exc.value)
    assert 'rate coefficient of order 3' in message
    assert 'electron density' in message


def test_this_repository_still_ships_no_three_body_coefficient(library):
    """The data blocker that remains, pinned semantically rather than by grepping the file.

    This is the new tripwire, and it fires in the direction the campaign actually wants: if
    somebody gives ``PlasmaRadiativeRecombination`` a third-order coefficient, this test
    fails and sends them to ``docs/i119-recombination-loss.md`` to confirm the coefficient is
    *sourced* - and to
    ``test_forcing_three_body_under_the_radiative_declaration_trips_the_rate_order_guard``,
    which shows that adding one here without a ``(2, 1)`` declaration cannot resolve anyway.

    **Why it is not a text search.** The first version of this test read ``reactions.py`` as
    raw characters and asserted an ``entry(`` count of one, no ``TwoTemperaturePlasma``, and
    no ``cm^6``. Review pointed out that such a check is walked past by a coefficient written
    in ``m^6``, by a third-order rate expressed through a different kinetics class, and -
    likeliest of the three - by somebody editing the *existing* entry to third order without
    adding a second ``entry(`` at all. A tripwire a unit change defeats is not a tripwire.

    This version loads the library and asks the engine for the reaction order implied by each
    coefficient's units. ``get_plasma_rate_order`` recognises ``m^6`` and ``cm^6``, per mole
    and per molecule alike (measured, ``logs/probe_threebody_stdout.log`` section D), so no
    spelling of a third-order coefficient slips through. An **unrecognised** unit returns
    ``None``, which this test also refuses: a coefficient whose order the engine cannot
    determine is exactly the case that must not pass silently.

    **The entry count is deliberately not asserted here** (I-234). It was, and that made this
    test fail merely because the library grew a second *second-order* entry -- which is not
    what it is about. The claim is "no coefficient in this library is third order", and it is
    strictly stronger when it loops over every entry the library happens to hold than when it
    first insists there is only one. Coverage changes are caught by
    ``test_library_loads_with_the_expected_coverage``, which is the right place for them.
    """
    entries = list(library.entries.values())
    assert entries, 'library loaded no entries at all'

    for entry in entries:
        kinetics = entry.data
        order = get_plasma_rate_order(kinetics)
        assert order is not None, (
            'the order of %s (A units %r) cannot be determined by the engine, so this '
            'tripwire cannot tell whether it is third order; see '
            'docs/i119-recombination-loss.md'
            % (kinetics.__class__.__name__, getattr(getattr(kinetics, 'A', None), 'units', None)))
        assert order == 2, (
            'a rate coefficient of order %d appeared in this library - a three-body '
            'coefficient needs a sourced value AND a (2, 1) placement declaration in '
            'RMG-Py; see docs/i119-recombination-loss.md' % order)


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

    Coverage is {Li+, Ar+} since I-234. The claim is unchanged by argon's arrival: what is
    entered gets a rate, what is not entered gets nothing at all -- no template, no tree
    descent, no averaged estimate. Argon widens the set by one and makes the point no
    weaker, because the 300-odd other cations in the shipped tables still get nothing.
    """
    entered = set()
    for reaction in library.get_library_reactions():
        for species in reaction.reactants:
            entered.add(species.molecule[0].to_smiles())
    assert entered == {'[Li+]', '[Ar+]'}


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


# ===========================================================================
# I-234 - the argon entry, Ar+ + e- => Ar + hv
#
# Deliberately mirrors the lithium checks above rather than sampling a few of
# them. The argon entry differs from lithium in three ways that each defeat a
# check written only for lithium -- a different kinetics class, a transcribed
# rather than table-loaded coefficient, and a two-temperature evaluator instead
# of an electron-temperature one -- so "the lithium tests cover it" would have
# been false in exactly the places that matter.
# ===========================================================================

# Shull & Van Steenberg 1982, ApJS 48, 95, Table 2 row AR1. Repeated here on
# purpose: the entry is a TRANSCRIPTION, not a table lookup like lithium's
# BadnellRRArrhenius(Z=3, N=2), so there is no shipped file to pin it against
# and the published row is the only external referent available.
SVS82_A_RAD = 3.77e-13      # cm^3/(molecule*s)
SVS82_X_RAD = 0.651         # dimensionless; the entry carries n = -X_rad
SVS82_T0 = 1.0e4            # K, the paper's own normalisation


def test_argon_entry_is_cation_recombination_written_without_an_explicit_electron(
        argon_reaction):
    """Canonical database form ``Ar+ => Ar``: no electron among the participants."""
    assert [s.label for s in argon_reaction.reactants] == ['[Arp]']
    assert [s.label for s in argon_reaction.products] == ['[Ar]']
    assert argon_reaction.reactants[0].molecule[0].get_net_charge() == +1
    assert argon_reaction.products[0].molecule[0].get_net_charge() == 0
    assert not any(s.is_electron()
                   for s in list(argon_reaction.reactants) + list(argon_reaction.products))


def test_argon_reactant_is_the_gas_phase_ground_state_cation(argon_reaction):
    """``1 Ar u1 p3 c+1`` -- 3s2 3p5, one unpaired electron.

    Pinned as an adjacency list rather than via SMILES because this database's monatomic
    ion SMILES round trip is lossy (``[Ar+]`` parses back as a dication). The *write*
    direction is sound, which is why the coverage test above can still use ``to_smiles``;
    the read direction is what must never be relied on, and pinning the adjacency list
    here is what keeps a future SMILES-based rewrite of this entry honest.

    This ``u1`` is also the whole reason the entry lives in a library: the family root
    demands ``u0`` and therefore cannot match this species at all (I-236).
    """
    cation = argon_reaction.reactants[0].molecule[0]
    neutral = argon_reaction.products[0].molecule[0]
    assert cation.to_adjacency_list().strip().endswith('Ar u1 p3 c+1')
    assert neutral.to_adjacency_list().strip().endswith('Ar u0 p4 c0')
    assert cation.atoms[0].radical_electrons == 1
    assert neutral.atoms[0].radical_electrons == 0


def test_argon_kinetics_are_the_transcribed_shull_van_steenberg_row(argon_reaction):
    """Every parameter pinned against the published row, in the paper's own units.

    ``A`` is written into the entry as ``cm^3/(molecule*s)`` so RMG performs the unit
    conversion and no arithmetic is done by hand; this asserts both that the SI value is
    the correct conversion of the published figure and that ``n`` is ``-X_rad``. If
    somebody re-derives, re-fits or rounds any of these, this fails.
    """
    kinetics = argon_reaction.kinetics
    assert isinstance(kinetics, TwoTemperaturePlasma)
    assert kinetics.A.value_si == pytest.approx(SVS82_A_RAD * 1e-6 * 6.02214076e23)
    assert kinetics.n.value_si == pytest.approx(-SVS82_X_RAD)
    assert kinetics.T0.value_si == pytest.approx(SVS82_T0)
    # both activation energies are zero, which is what collapses the Kossyi form to the
    # paper's bare power law -- see the exactness test below
    assert kinetics.Ea_g.value_si == pytest.approx(0.0)
    assert kinetics.Ea_e.value_si == pytest.approx(0.0)


def test_argon_rate_law_is_an_exact_representation_of_the_published_power_law(
        argon_reaction):
    """``k(T,Te)`` reproduces ``alpha = A_rad (Te/1e4)^-X_rad`` to numerical precision.

    Not an approximation of the published form but an algebraic identity: with
    ``Ea_g = Ea_e = 0`` both exponentials in the Kossyi expression become 1 and what is
    left is the power law. Checked across four decades of Te so that a stray dependence
    on the gas temperature, or a lost normalisation, cannot hide at a single point.
    """
    kinetics = argon_reaction.kinetics
    for te_ev in (0.3, 0.5, 1.0, 2.0, 3.0, 5.0, 20.0):
        Te = te_ev * EV
        published = SVS82_A_RAD * (Te / SVS82_T0) ** (-SVS82_X_RAD)   # cm^3/s
        delivered = kinetics.get_rate_coefficient_two_temp(298.15, Te)  # m^3/(mol*s)
        assert delivered / 6.02214076e23 * 1e6 == pytest.approx(published, rel=1e-12)


def test_argon_rate_reads_the_electron_temperature_and_not_the_gas_temperature(
        argon_reaction):
    """The load-bearing check for a two-temperature system.

    Holding Te fixed and sweeping the gas temperature over three decades must change
    nothing; holding Tgas fixed and changing Te must change everything. At the 5 torr
    deck's own conditions the two readings differ by a factor of 22.2, so an entry that
    silently read Tgas would be wrong in the dangerous direction -- high.
    """
    kinetics = argon_reaction.kinetics
    Te = 3.0 * EV

    at_te = [kinetics.get_rate_coefficient_two_temp(Tgas, Te)
             for Tgas in (100.0, 298.15, 1000.0, 10000.0)]
    assert at_te == pytest.approx([at_te[0]] * len(at_te), rel=1e-12)

    assert (kinetics.get_rate_coefficient_two_temp(298.15, 2.0 * EV)
            != pytest.approx(kinetics.get_rate_coefficient_two_temp(298.15, 3.0 * EV)))

    two_temperature = kinetics.get_rate_coefficient_two_temp(298.15, Te)
    gas_collapse = kinetics.get_rate_coefficient(298.15)   # k(T, Te=T); never used by the reactor
    assert gas_collapse / two_temperature == pytest.approx(22.17, rel=1e-3)


def test_argon_declares_the_electron_temperature_dependence_the_solver_dispatches_on(
        argon_reaction):
    """``PlasmaReactor`` routes on ``uses_electron_temperature``, so the flag must be set.

    Its evaluator is ``get_rate_coefficient_two_temp`` rather than lithium's
    ``get_rate_coefficient_electron_temp``; the reactor accepts either, and pinning which
    one this class offers is what would catch the flag being set on a class with neither.
    """
    kinetics = argon_reaction.kinetics
    assert kinetics.uses_electron_temperature
    assert hasattr(kinetics, 'get_rate_coefficient_two_temp')


def test_argon_electron_count_is_propagated_off_the_rate_law_onto_the_reaction(
        argon_reaction):
    """``TwoTemperaturePlasma`` defaults ``electrons`` to 0, so the entry must set it.

    Strictly stronger than the lithium equivalent: ``BadnellRRArrhenius`` supplies -1 by
    itself, so lithium would balance even if the entry said nothing. Argon would not --
    the generic two-temperature form asserts no intrinsic electron chemistry -- which
    makes this the test that catches a dropped ``electrons = -1``.
    """
    assert argon_reaction.kinetics.electrons.value == pytest.approx(-1)
    assert argon_reaction.electrons == -1


def test_argon_entry_is_one_way(argon_reaction):
    assert argon_reaction.reversible is False


def test_argon_canonical_reaction_balances(argon_reaction):
    """Atoms balance trivially; charge closes only via the metadata electron."""
    assert argon_reaction.is_balanced()
    assert sum(s.molecule[0].get_net_charge() for s in argon_reaction.reactants) == +1
    assert sum(s.molecule[0].get_net_charge() for s in argon_reaction.products) == 0


def test_argon_reaction_carries_the_library_label_as_its_placement_key(argon_reaction):
    assert argon_reaction.family == LIBRARY
    assert argon_reaction.library == LIBRARY


def test_argon_placement_resolves_to_cation_plus_electron_gives_the_neutral(
        argon_reaction, electron, declaration):
    view = electron_placement.resolve_electron_placement(
        argon_reaction,
        list(argon_reaction.reactants) + list(argon_reaction.products) + [electron])
    assert [s.label for s in view.reactants] == ['[Arp]', 'e']
    assert [s.label for s in view.products] == ['[Ar]']
    assert sum(1 for s in view.reactants if s.is_electron()) == 1
    assert sum(1 for s in view.products if s.is_electron()) == 0
    assert view.electrons == 0
    assert view.reversible is False


def test_argon_resolved_view_balances_in_the_E_pseudo_element(
        argon_reaction, electron, declaration):
    """Zero bound-electron imbalance on both sides: the captured electron fills the
    cation's deficit exactly, counted by the rule the Chemkin and Cantera writers use."""
    view = electron_placement.resolve_electron_placement(
        argon_reaction,
        list(argon_reaction.reactants) + list(argon_reaction.products) + [electron])
    assert (sum(get_species_electron_count(s) for s in view.reactants)
            == sum(get_species_electron_count(s) for s in view.products) == 0)


def test_argon_rate_order_cross_check_agrees_at_order_two(
        argon_reaction, electron, declaration):
    """Two reactants against a ``cm^3/(molecule*s)`` coefficient.

    This is the guard that catches a declaration with the right net count and the wrong
    incident order -- an error otherwise visible only as a rate wrong by a factor of the
    electron density.
    """
    assert get_plasma_rate_order(argon_reaction.kinetics) == 2
    view = electron_placement.resolve_electron_placement(
        argon_reaction,
        list(argon_reaction.reactants) + list(argon_reaction.products) + [electron])
    assert electron_placement.RATE_ORDER_AGREES in view.comment
    assert 'order 2' in view.comment


def test_argon_canonical_reaction_is_not_mutated_by_resolution(
        argon_reaction, electron, declaration):
    before = (argon_reaction.electrons,
              [s.label for s in argon_reaction.reactants],
              [s.label for s in argon_reaction.products])
    electron_placement.resolve_electron_placement(
        argon_reaction,
        list(argon_reaction.reactants) + list(argon_reaction.products) + [electron])
    assert (argon_reaction.electrons,
            [s.label for s in argon_reaction.reactants],
            [s.label for s in argon_reaction.products]) == before


def test_argon_undeclared_library_is_refused_by_name(argon_reaction, electron):
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.pop(LIBRARY, None)
    try:
        with pytest.raises(ElectronPlacementError) as exc:
            electron_placement.resolve_electron_placement(
                argon_reaction,
                list(argon_reaction.reactants) + list(argon_reaction.products) + [electron])
        assert 'no electron-placement declaration' in str(exc.value)
    finally:
        if saved is not None:
            registry[LIBRARY] = saved


@pytest.mark.parametrize('wrong,why', [
    ((2, 1), 'right net, wrong order: three reactants against an order-2 coefficient'),
    ((0, 1), 'wrong net: declares +1 against a reaction carrying -1'),
    ((1, 2), 'the ionisation declaration: net +1 against a reaction carrying -1'),
    ((2, 0), 'wrong net: declares -2 against a reaction carrying -1'),
    ((1, 1), 'wrong net: declares 0 against a reaction carrying -1'),
])
def test_argon_a_declaration_that_does_not_match_this_reaction_is_refused(
        argon_reaction, electron, wrong, why):
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.get(LIBRARY)
    registry[LIBRARY] = wrong
    try:
        with pytest.raises(ElectronPlacementError):
            electron_placement.resolve_electron_placement(
                argon_reaction,
                list(argon_reaction.reactants) + list(argon_reaction.products) + [electron])
    finally:
        if saved is None:
            del registry[LIBRARY]
        else:
            registry[LIBRARY] = saved


def test_the_plasma_reactor_accepts_argon_and_evaluates_it_at_the_two_temperature_rate(
        argon_reaction, electron, declaration):
    """Acceptance *and* the right number, at the 5 torr deck's own (Tgas, Te).

    The reactor is given a gas temperature far from Te on purpose: if it evaluated the
    rate at Tgas the comparison below fails by the factor of 22 pinned above, so this is
    the end-to-end form of the electron-temperature check.
    """
    from rmgpy.solver.plasma import PlasmaReactor

    Tgas, Te = 298.15, 3.0 * EV
    cation, neutral = argon_reaction.reactants[0], argon_reaction.products[0]
    for species in (cation, neutral, electron):
        species.thermo = _flat_thermo()

    reactor = PlasmaReactor(T=(Tgas, 'K'), P=(5 * 133.322368, 'Pa'), Te=(Te, 'K'),
                            initial_mole_fractions={cation: 1e-6, neutral: 1.0,
                                                    electron: 1e-6},
                            termination=[])
    reactor.initialize_model(core_species=[cation, neutral, electron],
                             core_reactions=[argon_reaction],
                             edge_species=[], edge_reactions=[])

    assert len(reactor.kf) == 1
    assert reactor.kf[0] == pytest.approx(
        argon_reaction.kinetics.get_rate_coefficient_two_temp(Tgas, Te), rel=1e-12)
    # and it is the published number, not merely self-consistent
    assert reactor.kf[0] / 6.02214076e23 * 1e6 == pytest.approx(
        SVS82_A_RAD * (Te / SVS82_T0) ** (-SVS82_X_RAD), rel=1e-12)


def test_the_declared_temperature_range_is_grid_membership_that_nothing_enforces(
        argon_reaction):
    """A referral pin, not a passing grade. Two separate facts, both measured.

    **One.** ``Tmin``/``Tmax`` on this entry are 1e4-1e8 K, which is the grid over which
    Shull & Van Steenberg exercise these rates (their Table 3 runs log T = 4.00 to 8.00).
    They are NOT a demonstrated accuracy bound -- the paper states no numerical validity
    range for the fits at all -- and the entry's longDesc says so. Pinned so that nobody
    later reads them as an accuracy claim the source did not make.

    **Two, and this is the referral.** Nothing checks either temperature against them
    during evaluation. ``is_temperature_valid`` knows the answer and no evaluation path
    consults it, so the rate is delivered silently from outside the declared range. Fixing
    that is an engine change and is out of scope here; this test exists so the day it is
    fixed, this assertion fails and sends someone to update the report rather than letting
    the behaviour change unnoticed.
    """
    kinetics = argon_reaction.kinetics
    assert kinetics.Tmin.value_si == pytest.approx(1.0e4)
    assert kinetics.Tmax.value_si == pytest.approx(1.0e8)

    # the gas temperature the deck runs at is outside the declared range ...
    assert kinetics.is_temperature_valid(298.15) is False
    # ... as is an electron temperature of 0.5 eV ...
    below = 0.5 * EV
    assert below < kinetics.Tmin.value_si
    assert kinetics.is_temperature_valid(below) is False
    # ... and the evaluator returns a number for it regardless, with no warning and no raise
    delivered = kinetics.get_rate_coefficient_two_temp(298.15, below)
    assert delivered > 0
    assert delivered / 6.02214076e23 * 1e6 == pytest.approx(
        SVS82_A_RAD * (below / SVS82_T0) ** (-SVS82_X_RAD), rel=1e-12)
