#!/usr/bin/env python
# encoding: utf-8

"""How the plasma library tests pick the one reaction each test is about (I-234).

This exists because the same defect has now been fixed twice, and the second fix was a
narrower version of the first one's mistake.

**Round 1 (the original defect).** The fixtures read
``reactions = library.get_library_reactions(); assert len(reactions) == 1; return reactions[0]``.
Growing a library from one entry to two made that assertion fail *inside a fixture*, and
pytest reports a raise during setup as an ERROR, not a failure. Twenty checks about lithium
stopped asserting and the run still printed green for everything else. A failure argues with
you; a setup error just removes the check.

**Round 2 (the repair that moved the trap).** The fix selected by *reactant labels* instead,
which survives a library growing a reaction about some other species -- and collides the
moment the library grows a second channel of the SAME reactant. ``Ar+ => Ar`` and
``Ar+ => Ar*`` share the reactant ``[Arp]``, so the selector matches two, raises in the
fixture, and every dependent test is a setup ERROR again. That is not hypothetical: the next
library ticket in this campaign appends argon chemistry including excited-state channels.

So the key here is **reactants AND products**, which distinguishes channels that differ only
in where they land. Two notes on why it is that and not the entry label, which would also be
unique:

* the entry label is not reachable from what the fixtures select over.
  ``KineticsLibrary.get_library_reactions`` rebuilds every ``LibraryReaction`` from
  ``entry.item`` and never propagates the label; measured, ``r.label`` is ``''`` on every
  reaction these libraries return, while ``library.entries`` is keyed ``'[Arp] => [Ar]'``.
* a label is free text that can be reworded without touching the chemistry. The channel is
  what a test is about.

**The residual, and how it is actually handled.** A genuine ``duplicate=True`` pair -- same
reactants, same products, two rates -- collides under this key too, and no key drawn from the
reaction can separate it, because in that case the test genuinely cannot know which entry it
means. Two things cover it, and round 3 of this defect was the discovery that only having the
first is not enough:

* ``assert_reactions_uniquely_keyed``, called from one dedicated test per file, so a collision
  of any kind is announced once, by name, in a test whose failure says exactly what happened;
* ``reaction_for`` **does not raise** on an ambiguous selection. It returns an
  ``AmbiguousSelection``, which raises on first use *inside the test body*. An earlier version
  of this module claimed the uniqueness test meant "the setup-error failure mode is
  unreachable"; that was false. The uniqueness test adds one failure, it does not stop the
  selector raising in every other fixture, so a duplicate pair would have produced the named
  failure **plus** the whole crop of setup errors the module exists to prevent. The guarantee
  is now carried by the selector's own failure path rather than asserted about it.

So: the key makes collisions rare, the uniqueness test makes them loud, and the stand-in makes
them survivable. All three, and the third is the one that makes the claim true.

Exercised end-to-end, against the collision case specifically, by
``docs/argon-radiative-recombination/logs/probe_fixture_survives_growth.py``, which imports
these functions rather than reimplementing them -- the previous probe kept its own copy of the
selector, and a copy is free to stay correct while the shipped one is not.
"""

import copy


def reaction_for_isolated(library, reactants, products):
    """``reaction_for``, deep-copied, so a test cannot mutate the shared library.

    ``get_library_reactions`` rebuilds the reaction objects on every call but **shares the
    ``Species``**: the participant lists are new, the molecules in them are not. Several
    reactor tests assign ``species.thermo`` to drive ``initialize_model``, and that write
    lands on the module-scoped library's own species, visible to every test that runs after
    it. Nothing depends on it today, which is precisely what makes it worth removing -- it
    is an order-dependent coupling waiting for a test that reads what an earlier one wrote.

    The fixtures' promise of a fresh reaction per test was false until this existed; it said
    so in three docstrings.
    """
    selected = reaction_for(library, reactants, products)
    if isinstance(selected, AmbiguousSelection):
        return selected
    return copy.deepcopy(selected)


def reaction_key(reaction):
    """The identity a test selects on: what goes in and what comes out.

    Sorted within each side, because the order two reactants are written in is not a
    property of the chemistry and a test should not break when an entry is retyped.
    """
    return (tuple(sorted(s.label for s in reaction.reactants)),
            tuple(sorted(s.label for s in reaction.products)))


def format_key(key):
    reactants, products = key
    return '{0} => {1}'.format(' + '.join(reactants), ' + '.join(products))


class AmbiguousSelection(object):
    """Stands in for a reaction that could not be selected, and fails on first use.

    This exists because of where the two previous fixes stopped. A fixture that *raises*
    produces a pytest setup ERROR, and an error asserts nothing and is reported in its own
    section -- which is the entire defect this module is about. Returning this object
    instead moves the moment of failure from setup into the test body, where pytest
    records a FAILURE against the test's own name.

    Every attribute access, comparison, iteration and truth test raises ``AssertionError``
    carrying the selection message, so a test cannot quietly proceed on a stand-in. ``repr``
    is deliberately the one safe operation: pytest calls it while formatting reports, and a
    raise there would turn the failure back into the internal error this class exists to
    avoid.
    """

    def __init__(self, message):
        self.__dict__['_message'] = message

    def _fail(self, *args, **kwargs):
        raise AssertionError(self.__dict__['_message'])

    def __getattr__(self, name):
        self._fail()

    def __setattr__(self, name, value):
        self._fail()

    __eq__ = __ne__ = __iter__ = __len__ = __bool__ = __call__ = __getitem__ = _fail
    __hash__ = None

    def __repr__(self):
        return '<AmbiguousSelection: {0}>'.format(self.__dict__['_message'])


def reaction_for(library, reactants, products):
    """Return the one library reaction with these reactants and these products.

    When there is not exactly one, this does **not** raise. It returns an
    ``AmbiguousSelection``, which raises on first use inside the test body -- so an
    ambiguous or missing selection is reported as a FAILURE of the test that needed it,
    never as a setup error that removes the test from the run. That is the difference this
    module exists to defend, applied to its own failure path.
    """
    wanted = (tuple(sorted(reactants)), tuple(sorted(products)))
    matches = [r for r in library.get_library_reactions() if reaction_key(r) == wanted]
    if len(matches) == 1:
        return matches[0]
    return AmbiguousSelection(
        'expected exactly one reaction {0!r} in {1}, found {2}. Present: {3}'.format(
            format_key(wanted), library.label, len(matches),
            sorted(format_key(reaction_key(r)) for r in library.get_library_reactions())))


def assert_reactions_uniquely_keyed(library):
    """Every reaction in the library is distinguishable from every other one.

    Call this from exactly one test per library. When it holds, no fixture in the file can
    match two reactions. When it stops holding, it stops holding HERE first -- as a failure
    someone has to answer, with a message naming the colliding channels.

    What it does **not** do, because an earlier version of this docstring claimed otherwise:
    it does not prevent ``reaction_for`` from failing elsewhere in the same run. It is one
    named failure, not a gate on the other tests. What keeps those other tests reporting as
    failures rather than setup errors is ``AmbiguousSelection``, not this assertion.
    """
    seen = {}
    for reaction in library.get_library_reactions():
        seen.setdefault(reaction_key(reaction), []).append(reaction)
    collisions = {k: v for k, v in seen.items() if len(v) > 1}
    assert not collisions, (
        'these reactions in {0} are indistinguishable by reactants and products, so any '
        'fixture selecting one of them would raise during setup and silently turn its '
        'tests into errors: {1}'.format(
            library.label, [format_key(k) for k in collisions]))
