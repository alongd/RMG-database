#!/usr/bin/env python
# encoding: utf-8

name = "Fixture_Inert_Recipe/groups"
shortDesc = u"Test fixture: an INERT family. Its recipe is a no-op, so it generates nothing."
longDesc = u"""
NOT CHEMISTRY. This is test data for check_family_generates.py. The rate is a placeholder.

THE DEFECT THIS FIXTURE CARRIES: a recipe made only of charge actions.

It is identical to Fixture_Healthy except for the recipe, which is LOSE_CHARGE *1 + GAIN_CHARGE *2.
Charge in RMG is DERIVED, not stored: Atom.decrement_charge/increment_charge set atom.charge and
touch nothing else, apply_recipe then calls struct.update_charge(), and Atom.update_charge
recomputes charge from valence, bond order, radicals and lone pairs -- none of which the recipe
changed. The charge goes straight back where it started, the products come out isomorphic to the
reactants, and _create_reaction discards a reaction whose products are its reactants.

Result: ZERO reactions, from a family that looks entirely reasonable and passes all twelve
standard family checks. kinetics_check_sample_can_react is the only one of the twelve that runs
the recipe at all, and it asserts only that nothing throws.

The check should report this fixture as INERT and exit 1.

BOTH ROOTS SAY `R` HERE, AND THEY HAVE TO. A charge action forces the root's atom types to be
charge-resolvable: `generate_product_template` applies the recipe to the ROOT GROUPS at load time
(family.py:717 -> 1077), and `GroupAtom._lose_charge` raises ActionError -- "Unknown atom type
produced from set [H, O, metal]" -- because RMG defines charge-specific atom types for only six
species. So a charge-only recipe and an element-named root cannot coexist: the family will not
load at all.

That is worth knowing in its own right. It means the element narrowing in Fixture_Healthy would
have caught the inert recipe LOUDLY, at load time, rather than silently -- the two defects these
fixtures carry are not independent, and the broad `R` root is what let the inert one hide.
"""

template(reactants=["A", "B"], products=["A-", "B+"], ownReverse=False)

reverse = "Fixture_Inert_Recipe_Reverse"
reversible = False

allowChargedSpecies = True
electrons = 0

# THE DEFECT. Charge actions alone move nothing -- see the longDesc above. Deliberately wrong.
recipe(actions=[
    ['LOSE_CHARGE', '*1', 1],
    ['GAIN_CHARGE', '*2', 1],
])

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 R ux p[0,2] c[+1,+2,+3,+4]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "B",
    group =
"""
1 *2 R u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]
""",
    kinetics = None,
)

tree(
"""
L1: A
L1: B
"""
)
