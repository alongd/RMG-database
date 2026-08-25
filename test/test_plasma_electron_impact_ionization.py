#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``PlasmaElectronImpactIonization`` kinetics library.

This library is the database owner of electron-impact ionization. The decision to
make it a library rather than a reaction family is argued from evidence in
``docs/i114-ionisation-owner.md``; the tests here pin the consequences of that
decision that a reader could otherwise only take on trust.

The path under test is four steps long and each is asserted separately, because
each can fail on its own and three of them fail quietly:

1. **load**       - the entry parses, finds its species, and picks up the Voronov
                    fit from ``input/kinetics/voronov.yaml`` by ``(Z, N)``.
2. **balance**    - ``Reaction.is_balanced`` closes the 0 -> +1 charge gap using
                    the ``electrons = +1`` propagated off the rate law.
3. **placement**  - ``resolve_electron_placement`` turns the canonical
                    ``Li => Li+`` into the reactor-facing ``Li + e- => Li+ + 2 e-``
                    from this library's ``(1, 2)`` declaration, and the canonical
                    reaction is left untouched.
4. **acceptance** - ``PlasmaReactor.initialize_model`` accepts the result and
                    evaluates it at the Voronov rate for the reactor's Te.

Two rules the assertions follow:

* **Assert the number, not just the absence of an exception.** The reactor's ``kf``
  is compared against ``VoronovEIArrhenius.get_rate_coefficient_electron_temp(Te)``
  directly. A view that resolves but is evaluated at the wrong order is exactly the
  failure the two-sided declaration exists to prevent, and it does not raise.
* **A negative control runs on both sides of the change.** The two pre-existing
  declarations are resolved before and after this library's declaration is added,
  and the resulting views are compared, so "attachment still works" is a
  measurement rather than an assumption.

WHERE THE DECLARATION LIVES
---------------------------
``FAMILY_ELECTRON_PLACEMENT`` is a module-level dict in RMG-Py
(``rmgpy/electron_placement.py``); a database repository cannot ship an entry in it.
``LibraryReaction.__init__`` sets ``self.family = library`` (``rmgpy/data/kinetics/
library.py``), so a *library label* is a valid key there and the one-line addition is

    'PlasmaElectronImpactIonization': (1, 2),

which lives on RMG-Py branch ``i114-ionisation-declaration``, stacked on
``i113-placement-widening``.

The ``declaration`` fixture below uses that shipped entry when the runtime carries it
and otherwise injects it for the duration of the test, restoring the registry
afterwards. Both paths assert the value is ``(1, 2)``, so this file is green against
either runtime -- which is the point, since the two halves of this ticket live in
different repositories and can merge at different times. The corollary is worth stating
because it bounds what a green run here proves: passing does NOT establish that the
RMG-Py entry exists.

Run with the runtime pinned to a branch carrying the widened two-sided declaration --
``i114-ionisation-declaration`` for the shipped path, ``i113-placement-widening`` for
the injected one::

    cd /home/alon/Code/RMG-database-i114-ionisation
    PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH \\
    PYTHONPATH=/home/alon/Code/RMG-Py-i114-ionisation-declaration \\
      python -m pytest test/test_plasma_electron_impact_ionization.py -v
"""

import os

import pytest

from rmgpy import settings

LIBRARY = 'PlasmaElectronImpactIonization'
DECLARATION = (1, 2)

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

# Pin before anything imports a database-reading module. RMG's rmgrc resolution
# ends in `return  # fail silently`, and the rmgrc on the runtime branch points at
# the *shared* plasma database, so leaving this to discovery would silently test a
# checkout that does not contain this library.
settings['database.directory'] = THIS_DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.electron_balance import get_species_electron_count  # noqa: E402
from rmgpy.exceptions import ElectronPlacementError  # noqa: E402
from rmgpy.kinetics import Arrhenius, VoronovEIArrhenius  # noqa: E402
from rmgpy.molecule import Molecule  # noqa: E402
from rmgpy.data.kinetics.family import TemplateReaction  # noqa: E402
from rmgpy.species import Species  # noqa: E402
from rmgpy.thermo import NASA, NASAPolynomial  # noqa: E402

import rmgpy.electron_placement as electron_placement  # noqa: E402


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
    """Guarantee the ``(1, 2)`` declaration is in the registry for the test's duration.

    Yields ``(declaration, was_shipped)``. When RMG-Py already carries the entry the
    registry is left exactly as it was; otherwise it is injected and removed again,
    so no test can observe a registry this fixture has permanently altered.
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

    The reactor's electron-placement and rate-order acceptance path is what is under
    test; nothing here depends on the thermochemistry being the real one, and the
    reaction is irreversible so no Keq is ever formed from it.
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


def test_entry_is_lithium_first_ionization_written_without_an_explicit_electron(reaction):
    """The canonical database form: ``Li => Li+``, no electron among the participants.

    The electron is metadata here on purpose. Writing it explicitly *and* keeping a
    nonzero count is double representation, which the resolver refuses outright
    (``resolve_electron_placement`` step 2), and writing it explicitly with a zero
    count would put the database representation out of step with every other
    electron-carrying entry.
    """
    assert [s.label for s in reaction.reactants] == ['[Li]']
    assert [s.label for s in reaction.products] == ['[Lip]']
    assert reaction.reactants[0].molecule[0].get_net_charge() == 0
    assert reaction.products[0].molecule[0].get_net_charge() == +1
    assert not any(s.is_electron() for s in list(reaction.reactants) + list(reaction.products))


def test_kinetics_come_from_the_shipped_voronov_table_not_from_transcribed_numbers(reaction):
    """``VoronovEIArrhenius(Z=3, N=3)`` reads ``input/kinetics/voronov.yaml`` at load.

    Pinned against the table's own Li I -> Li II row rather than against numbers
    repeated here: dE = 5.4 eV, P = 0, X = 0.438, K = 0.41. If someone edits the entry
    to inline an A-factor, or points it at a different stage, this fails.
    """
    kinetics = reaction.kinetics
    assert isinstance(kinetics, VoronovEIArrhenius)
    assert kinetics.dE == pytest.approx(5.4)
    assert kinetics.P.value_si == pytest.approx(0.0, abs=1e-12)
    assert kinetics.X.value_si == pytest.approx(0.438)
    assert kinetics.K.value_si == pytest.approx(0.41)
    assert kinetics.A.units in ('cm^3/(mol*s)', 'cm^3/(molecule*s)',
                                'm^3/(mol*s)', 'm^3/(molecule*s)')
    assert kinetics.uses_electron_temperature
    assert kinetics.uses_electron_density


def test_the_electron_count_is_propagated_off_the_rate_law_onto_the_reaction(reaction):
    """``KineticsLibrary.load`` copies ``kinetics.electrons`` onto ``Reaction.electrons``.

    ``load_entry`` takes no electron argument, so without that copy the reaction would
    reach the balance check declaring zero electrons and a perfectly balanced charged
    entry would be rejected.
    """
    assert reaction.kinetics.electrons.value == pytest.approx(+1)
    assert reaction.electrons == +1


def test_the_entry_is_one_way(reaction):
    """Irreversible by construction, for two independent reasons.

    The binding ruling requires forward and reverse to be stated as separate one-way
    processes; and ``PlasmaReactor`` refuses a reversible electron-temperature-dependent
    reaction outright, because kf(Tgas, Te)/Keq(Tgas) mixes two thermal closures.
    """
    assert reaction.reversible is False


# ---------------------------------------------------------------------------
# Step 2 - balance
# ---------------------------------------------------------------------------

def test_the_canonical_reaction_balances(reaction):
    """Charge closes only because ``electrons = +1`` is folded in.

    Atoms balance trivially (one Li each side); the charge does not - 0 on the left,
    +1 on the right - and ``is_balanced`` closes it with the metadata electron.
    """
    assert reaction.is_balanced()
    assert sum(s.molecule[0].get_net_charge() for s in reaction.reactants) == 0
    assert sum(s.molecule[0].get_net_charge() for s in reaction.products) == +1


# ---------------------------------------------------------------------------
# Step 3 - electron placement
# ---------------------------------------------------------------------------

def test_a_library_label_is_a_valid_placement_key(reaction):
    """``LibraryReaction.family`` is the library label, which is what makes this work.

    The registry is keyed on ``reaction.family``, and ``LibraryReaction.__init__``
    sets ``self.family = library``. Without this, a library could never own an
    electron-placed reaction and the family-vs-library decision would have been made
    by the code rather than by the chemistry.
    """
    assert reaction.family == LIBRARY
    assert reaction.library == LIBRARY


def test_an_undeclared_library_is_refused_by_name_never_guessed_from_the_net_count(reaction, electron):
    """No silent fallback: absence of a declaration is a named failure.

    This is the state of the world before the declaration is added, and it is the
    guarantee that answers "what happens to a species the fits do not cover" at the
    code level as well as the data level - an owner that is not declared does not
    resolve at all.
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


def test_the_declaration_is_one_electron_in_two_out(declaration):
    """``(1, 2)``: incident order 1, net production +1. Neither number implies the other.

    ``electrons = +1`` alone is equally consistent with ``Li -> Li+ + e-`` (order 1,
    units s^-1) and ``Li + e- -> Li+ + 2 e-`` (order 2, units cm^3/(molecule*s)).
    Only the pair distinguishes them, which is why the declaration is two-sided.
    """
    value, _shipped = declaration
    assert value == DECLARATION
    reactant_count, product_count = value
    assert reactant_count == 1
    assert product_count - reactant_count == +1


def test_the_declaration_validates_against_the_reactions_own_electron_count(reaction, declaration):
    """The declared net change and the reaction's scalar must agree, and do."""
    (reactant_count, product_count), _shipped = declaration
    assert product_count - reactant_count == reaction.electrons


def test_placement_resolves_to_lithium_plus_electron_gives_cation_plus_two_electrons(
        reaction, electron, declaration):
    view = electron_placement.resolve_electron_placement(
        reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    assert [s.label for s in view.reactants] == ['[Li]', 'e']
    assert [s.label for s in view.products] == ['[Lip]', 'e', 'e']
    assert sum(1 for s in view.reactants if s.is_electron()) == 1
    assert sum(1 for s in view.products if s.is_electron()) == 2
    assert view.electrons == 0
    assert view.reversible is False


def test_the_resolved_view_balances_in_the_E_pseudo_element(reaction, electron, declaration):
    """The structural proof that the declared *sides* were the right sides.

    Counted with ``get_species_electron_count``, the rule the Chemkin and Cantera
    writers use, so the reactor boundary and the export boundary cannot disagree
    about what balances. Moving n electrons across changes the imbalance by 2n, so a
    balanced view is only possible for one assignment of sides.
    """
    view = electron_placement.resolve_electron_placement(
        reaction, list(reaction.reactants) + list(reaction.products) + [electron])
    assert (sum(get_species_electron_count(s) for s in view.reactants)
            == sum(get_species_electron_count(s) for s in view.products) == 1)


def test_the_rate_order_cross_check_agrees_at_order_two(reaction, electron, declaration):
    """The view has two reactants and the Voronov A-factor is a second-order coefficient.

    This is a cross-check, never an order source. It matters because it is the thing
    that catches a wrong-shaped declaration whose *net* count is nevertheless right -
    ``(0, 1)`` would give the same net +1 against the same order-2 coefficient, and
    the rate would be wrong by a factor of the electron density with the reaction
    still looking well formed.
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
    ((0, 1), 'right net, wrong order: one reactant against an order-2 coefficient'),
    ((2, 3), 'right net, wrong order: three reactants against an order-2 coefficient'),
    ((1, 3), 'wrong net: declares +2 against a reaction carrying +1'),
    ((1, 0), 'the attachment declaration: net -1 against a reaction carrying +1'),
])
def test_a_declaration_that_does_not_match_this_reaction_is_refused(
        reaction, electron, wrong, why):
    """Every wrong two-sided declaration is caught, by one of two distinct guards.

    The net-count guard catches a wrong ``product_count - reactant_count``; the
    rate-order cross-check catches a declaration whose net is right but whose incident
    order is not. Neither subsumes the other, and the ``(0, 1)`` case is the one that
    only the second can see.
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

def test_the_plasma_reactor_accepts_the_reaction_and_evaluates_it_at_the_voronov_rate(
        reaction, electron, declaration):
    """The whole point: acceptance *and* the right number.

    ``PlasmaReactor.initialize_model`` resolves placement itself, so handing it the
    canonical reaction exercises the same path a real model would take. Asserting only
    that it did not raise would miss a view evaluated at the wrong reaction order,
    which is silent; the ``kf`` comparison is what makes it visible.
    """
    from rmgpy.solver.plasma import PlasmaReactor

    Te = 10000.0
    lithium, cation = reaction.reactants[0], reaction.products[0]
    for species in (lithium, cation, electron):
        species.thermo = _flat_thermo()

    reactor = PlasmaReactor(T=(1000, 'K'), P=(1, 'bar'), Te=(Te, 'K'),
                            initial_mole_fractions={lithium: 1.0, cation: 1e-12,
                                                    electron: 1e-12},
                            termination=[])
    reactor.initialize_model(core_species=[lithium, cation, electron],
                             core_reactions=[reaction],
                             edge_species=[], edge_reactions=[])

    assert reactor.electron_index == 2
    assert len(reactor.kf) == 1
    assert reactor.kf[0] == pytest.approx(
        reaction.kinetics.get_rate_coefficient_electron_temp(Te), rel=1e-12)


def test_the_reactor_would_refuse_the_reaction_without_a_declaration(reaction, electron):
    """Without the declaration the reactor refuses, rather than falling back.

    The reactor's own guard rejects a metadata-only electron count, so the failure a
    missing declaration produces is a refusal - never a reaction quietly evaluated at
    first order in Li with no electron density in it at all.
    """
    from rmgpy.solver.plasma import PlasmaReactor

    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    saved = registry.pop(LIBRARY, None)
    lithium, cation = reaction.reactants[0], reaction.products[0]
    for species in (lithium, cation, electron):
        species.thermo = _flat_thermo()
    try:
        reactor = PlasmaReactor(T=(1000, 'K'), P=(1, 'bar'), Te=(10000, 'K'),
                                initial_mole_fractions={lithium: 1.0, cation: 1e-12,
                                                        electron: 1e-12},
                                termination=[])
        with pytest.raises(ElectronPlacementError):
            reactor.initialize_model(core_species=[lithium, cation, electron],
                                     core_reactions=[reaction],
                                     edge_species=[], edge_reactions=[])
    finally:
        if saved is not None:
            registry[LIBRARY] = saved


# ---------------------------------------------------------------------------
# Coverage: what happens to a species the fits do not cover
# ---------------------------------------------------------------------------

def test_a_species_outside_the_fits_gets_no_reaction_at_all_and_no_rate(library):
    """A library has no template, so an uncovered species gets nothing - not an estimate.

    This is the property the family-vs-library decision was made on. The check is
    deliberately structural rather than a generation run: there is no matcher to run,
    which is exactly the claim. Argon is in the Voronov table and RMG can build it, and
    it still gets nothing here, because coverage is the entry list and nothing else.
    """
    entered = set()
    for reaction in library.get_library_reactions():
        for species in reaction.reactants:
            entered.add(species.molecule[0].to_smiles())
    assert entered == {'[Li]'}
    for smiles in ('[Ar]', '[N]', '[O]', '[He]', 'C', 'N#N'):
        assert smiles not in entered


def test_the_voronov_table_holds_far_more_than_this_library_claims():
    """The gap between the data and the entry list is real and is stated, not hidden.

    13 elements and 134 (Z, N) stages are in the table; one is claimed here. The
    difference is not a family's worth of missing generativity - it is species RMG
    cannot build (Na, Mg, Al, K, Ca have no atom types) or cations this database has
    no thermochemistry for. Both are named in ``docs/i114-ionisation-owner.md``.
    """
    import yaml
    path = os.path.join(settings['database.directory'], 'kinetics', 'voronov.yaml')
    with open(path) as handle:
        table = yaml.safe_load(handle)
    blocks = table['coefficients']
    assert len(blocks) == 13
    assert sum(len(block['entries']) for block in blocks) == 134
    # one neutral -> +1 stage per element: N (electrons before ionization) == Z
    assert sum(1 for block in blocks
               if any(int(e['N']) == block['Z'] for e in block['entries'])) == 13


@pytest.mark.parametrize('symbol', ['Na', 'Mg', 'Al', 'K', 'Ca'])
def test_five_covered_elements_cannot_be_built_by_rmg_at_all(symbol):
    """Not a database gap - RMG has no atom types for these elements.

    Named here so that "the library covers one species" is not read as a database
    omission that a family would have fixed. A family could not have reached them
    either.
    """
    with pytest.raises(Exception):
        Molecule().from_adjacency_list('1 {0} u1 p0 c0'.format(symbol))


# ---------------------------------------------------------------------------
# Negative control: the two pre-existing declarations are untouched
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
    """``Li+ + CH3 + e- => CH3Li`` in canonical form, in the family-forward orientation."""
    cation = Species(label='Lip', molecule=[Molecule().from_adjacency_list('1 Li u0 p0 c+1')])
    methyl = Species(label='CH3', molecule=[Molecule().from_smiles('[CH3]')])
    product = Species(label='CH3Li', molecule=[Molecule().from_smiles('C[Li]')])
    return TemplateReaction(
        reactants=[cation, methyl], products=[product], electrons=-1, reversible=False,
        family='Cation_R_Recombination',
        kinetics=Arrhenius(A=(1.0e10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol')))


def test_the_two_pre_existing_declarations_still_read_one_in_none_out():
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

    Each shape is resolved twice - once with the ionization declaration absent from
    the registry and once with it present - and the two views are compared
    participant by participant. Adding a key to a dict should not perturb the others,
    but this is the assertion that says so rather than assuming it.
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
        with_ionization = resolve()
    finally:
        registry.pop(LIBRARY, None)
        if saved is not None:
            registry[LIBRARY] = saved

    assert without == with_ionization
    assert without[0] == expected_reactants
    assert without[1] == expected_products
    assert without[2] == 0
