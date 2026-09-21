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

BOTH ROOTS SAY `R` HERE, AND THEY HAVE TO -- BUT THE REASON IS NARROWER THAN IT FIRST LOOKS.

`generate_product_template` applies the recipe to the ROOT GROUPS at load time (family.py:717 ->
1077). With root A narrowed to `[H,O,metal]`, `GroupAtom._lose_charge` raises
`ActionError: Unknown atom type produced from set [H, O, metal]` and the family will not load.

The correct statement of the rule is about TRANSITIONS, not about element lists:

    a charge action requires every atom type the root admits to have a charge transition
    available from it.

It is NOT "element-named roots and charge actions cannot coexist". A charge-only family whose
roots name the six atom types that DO carry charge transitions -- `Li+ Na+ K+ Mg+ Ca+ Ar+` -- loads
perfectly well, and stays just as inert. The owner verified both halves of this independently, by
narrowing a copy of this fixture's root A to `[H,O]` (refuses to load, same ActionError) and by
building the six-type variant (loads, inert). An earlier version of this file drew the wider
conclusion from the first half alone.

What survives, and is still worth having: the broad `R` root is what let the inert recipe hide
here. Narrowing root A by element in THIS family would have surfaced the dead recipe loudly at
load time instead of silently. That is a property of these two defects together, not a general
incompatibility.
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
