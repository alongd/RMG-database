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

The former children `alkaline_A` / `alkaline_B` carried that restriction one level down. They are
gone because the restriction now lives at the top: a child repeating its parent fails
`kinetics_check_groups_nonidentical`, and the pre-I-224 child, being broader in radical count than
the narrowed top, would fail `kinetics_check_child_parent_relationships`. The two-bare-roots shape
matches the sibling family Plasma_Associative_Ionization_Alkali_Alkaline, whose B top likewise
carries no children.

WHAT THIS NARROWING COSTS. The docstring above used to read "e.g.: alkaline earth metal atoms or O
atoms", and `training/reactions.py` entry 1 is O + O <=> O2+ + e- with a rank-6 literature rate
[Aiken2025]. Under an `alkaline` top that reaction is ORPHANED: O is not in the `alkaline` specific
list, so the family can no longer generate its own training reaction. The entry is deliberately
kept, not deleted -- see the note in `training/reactions.py`. O + O associative ionization is real
chemistry and still needs a home in a family named for it.

WHY THE `*1` TOP COULD NOT SIMPLY NAME OXYGEN. The recipe applies GAIN_CHARGE to *1, and
`GroupAtom._gain_charge` (rmgpy/molecule/group.py:362-385) raises ActionError unless *every* atom
type in the group carries an `increment_charge` action. No neutral oxygen atom type in RMG-Py has
one: `ATOMTYPES['O']` has `increment_charge=[]` and `decrement_charge=[]`, while its bond, radical
and lone-pair actions are all self-preserving -- the charge row alone is missing. So a *1 top that
names O cannot be loaded at all, and the pre-I-224 wildcard may have been a workaround for that
engine gap rather than carelessness. Fixing the atom-type action table is RMG-Py work and is owned
elsewhere; it is the prerequisite for giving O + O a correctly-named home.
"""

template(reactants=["A", "B"], products=["AB+"], ownReverse=False)

reverse = "electron_absorbance_and_dissociation_3"

reversible = False
allowChargedSpecies = True
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
