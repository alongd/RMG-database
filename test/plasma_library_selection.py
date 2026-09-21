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

**The residual, stated rather than hidden.** A genuine ``duplicate=True`` pair -- same
reactants, same products, two rates -- collides under this key too, and no key drawn from the
reaction can separate it, because in that case the test genuinely cannot know which entry it
means. That case is why ``assert_reactions_uniquely_keyed`` exists: each test file calls it in
one dedicated test, so a collision of any kind arrives as a **failure in a named test** rather
than as a setup error scattered across every test that happens to use a fixture. The selector
makes collisions rare; the uniqueness test makes them loud. Only the second is a guarantee.

Exercised end-to-end, against the collision case specifically, by
``docs/argon-radiative-recombination/logs/probe_fixture_survives_growth.py``, which imports
these functions rather than reimplementing them -- the previous probe kept its own copy of the
selector, and a copy is free to stay correct while the shipped one is not.
"""


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


def reaction_for(library, reactants, products):
    """Return the one library reaction with these reactants and these products.

    Raises ``AssertionError`` when there is not exactly one. Inside a fixture that is a
    setup error, which is exactly the failure mode this module exists to make rare -- hence
    ``assert_reactions_uniquely_keyed``, which turns the remaining cases into a loud failure
    in one place.
    """
    wanted = (tuple(sorted(reactants)), tuple(sorted(products)))
    matches = [r for r in library.get_library_reactions() if reaction_key(r) == wanted]
    assert len(matches) == 1, (
        'expected exactly one reaction {0!r} in {1}, found {2}. Present: {3}'.format(
            format_key(wanted), library.label, len(matches),
            sorted(format_key(reaction_key(r)) for r in library.get_library_reactions())))
    return matches[0]


def assert_reactions_uniquely_keyed(library):
    """Every reaction in the library is distinguishable from every other one.

    Call this from exactly one test per library. It is the claim that makes selection by
    identity safe: if it holds, no fixture in the file can match two reactions, and the
    setup-error failure mode is unreachable. When it stops holding, it stops holding HERE,
    as a failure someone has to answer, instead of silently converting the file's other
    tests into errors nobody reads.
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
