#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkaline_Alkaline/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A + B <=> AB+ + e-

Where both A and B are alkaline earth metal atoms (Mg, Ca) carrying two unpaired electrons.
Here Atom A is less electronegative and looses two radicals (one for bonding), while Atom B looses one radical to form the bond.

Both top groups were `R u[2,3,4] px cx` until I-224. That matched any species carrying an atom
with 2-4 unpaired electrons -- C and N atoms, S, triplet carbenes, a carbene site inside an
arbitrary polyatomic, and (once the metastable-argon atom type lands) Ar u2 p3 c0 -- all of which
entered the family, descended to the generic top, and generated a bonded cation. The tops are now
the `alkaline` atom type at u2, which is exactly Mg and Ca (rmgpy/molecule/atomtype.py, the
`alkaline` specific list).

`alkaline` IS A MOVING TARGET. The narrowing says "whatever the `alkaline` atom type resolves to",
not "Mg and Ca" -- it is Mg and Ca today (atomtype.py:388-389, with their charge and spin variants).
If Be, Sr or Ba are ever added to that atom type, these tops widen to admit them with no edit to
this file and no check failing. The two training entries below are Mg and Ca only, so a widening of
the atom type would outrun the data before it outran the name.

The former children `alkaline_A` / `alkaline_B` carried that restriction one level down. They are
gone because the restriction now lives at the top: a child repeating its parent fails
`kinetics_check_groups_nonidentical`, and the pre-I-224 child, being broader in radical count than
the narrowed top, would fail `kinetics_check_child_parent_relationships`. The two-bare-roots shape
matches the sibling family Plasma_Associative_Ionization_Alkali_Alkaline, whose B top likewise
carries no children.

WHAT THIS NARROWING COST. The docstring above used to read "e.g.: alkaline earth metal atoms or O
atoms", and `training/reactions.py` entry 1 was O + O <=> O2+ + e- with a rank-6 literature rate
[Aiken2025]. O is not in the `alkaline` specific list, so under these tops the family can no longer
template that reaction. It was MOVED OUT, not deleted, and now lives verbatim at
`docs/i224-alkaline-family-top/held-back/Plasma_Associative_Ionization_Alkaline_Alkaline/training/`
with its species; the surviving entries keep indices 2 and 3. Leaving it here was not an option: an
unreachable training entry escapes `add_rules_from_training` as an `UndeterminableKineticsError` on
the path `rmgpy/rmg/main.py:590` takes, while every database check stays green. O + O associative
ionization is real chemistry and still needs a home in a family named for it.

WHY THE `*1` TOP COULD NOT SIMPLY NAME OXYGEN. The recipe applies GAIN_CHARGE to *1, and
`GroupAtom._gain_charge` (rmgpy/molecule/group.py:362-385) raises ActionError unless *every* atom
type in the group carries an `increment_charge` action. No neutral oxygen atom type in RMG-Py has
one: `ATOMTYPES['O']` has `increment_charge=[]` and `decrement_charge=[]`, while its bond, radical
and lone-pair actions are all self-preserving -- the charge row alone is missing. So a *1 top that
names O cannot be loaded at all, and the pre-I-224 wildcard may have been a workaround for that
engine gap rather than carelessness. Fixing the atom-type action table is RMG-Py work and is owned
elsewhere; it is the prerequisite for giving O + O a correctly-named home.

NEUTRAL REACTANTS ONLY - `allowChargedReactants = False`, declared below beside
`allowChargedSpecies`. This family associates two neutral atoms into a cation, so it must not
consume a species that already carries a net charge. `allowChargedSpecies` cannot say that on its
own: it is two-sided, gating reactants and products together, and the charged product is the whole
point, so it stays True. `allowChargedReactants` is the one-sided companion - RMG-Py reads it into
`allow_charged_reactants` (family.py:693-695, inheriting `allowChargedSpecies` when undeclared) and
applies `is_charged_reactant_forbidden` to the forward reactants inside `_create_reaction`
(family.py:1726-1740, 1788-1792), rejecting on whole-molecule net charge of either sign. The groups
cannot say it either: RMG groups match subgraphs, so a `c0` written on *1 constrains that atom and
never the molecule around it.

MEASURED: the declaration changes nothing today, and the reason is worth keeping. Exhaustively,
the only constructible (Mg or Ca, u2) atom is neutral with zero bonds - every other charge and
bond count in -1..+2 x 0..2 bonds is refused by RMG's valency model - so any *connected* molecule
matching these tops IS a bare neutral atom. A net charge can therefore only ride on a separate,
disconnected fragment, and such a reactant is already refused one layer earlier: the merged product
then splits into two structures against a template declaring one product, so `apply_recipe` returns
None at family.py:1525-1532 before any charge policy is consulted. Generation is 6 reactions over
the 17-species probe set either way. The declaration is kept because it becomes load-bearing the
moment either of those accidents changes - a widened radical count, a bonded group, or a second
declared product - and because a scope the family states is worth more than one it merely happens
to have. It is a family-local restriction, not a claim that associative ionization of an ion is
impossible chemistry.
"""

template(reactants=["A", "B"], products=["AB+"], ownReverse=False)

reverse = "electron_absorbance_and_dissociation_3"

reversible = False
allowChargedSpecies = True
allowChargedReactants = False
electrons = 1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 2],
    ['LOSE_RADICAL', '*2', 1],
    ['FORM_BOND', '*1', 1, '*2'],
    ['GAIN_CHARGE', '*1', 1],
])

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 alkaline u2 px cx
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "B",
    group =
"""
1 *2 alkaline u2 px cx
""",
    kinetics = None,
)

tree(
"""
L1: A
L1: B
"""
)
