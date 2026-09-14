#!/usr/bin/env python
# encoding: utf-8

name = "Fixture_Own_Product_Raises/groups"
shortDesc = u"Test fixture: a family that generates fine, then ABORTS on the species it just made."
longDesc = u"""
NOT CHEMISTRY. This is test data for check_family_generates.py. The rate is a placeholder.

THE DEFECT THIS FIXTURE CARRIES: a root broader than its own subtree, which makes the family
unable to survive its own product.

It is identical to Fixture_Healthy except for root A, which says `R` instead of `[H,O,metal]`.
A group constrains ATOMS, not molecules, so `R ux p[0,2] c[+1,+2,+3,+4]` does not mean "a cation";
it means "contains a formally positive atom". The family's OWN product N2+ is
`N u1 p0 c+1 {2,T} | N u0 p1 c0 {1,T}`, and its charged nitrogen matches. GAIN_RADICAL *1 then
makes `N u2 p0 c0` holding a triple bond, which has no atom type, so update_atomtypes raises and
generate_reactions propagates the AtomTypeError to the caller.

THIS ABORTS THE JOB. It does not omit a reaction. And it is unreachable from the reactant side:
the family generates its training reaction perfectly. RMG puts the product into the core and hands
it back to react() on the NEXT iteration, which is where it dies -- so a probe that drives only
training reactants sees a clean family. The gap between "safe on its reactants" and "safe" is
exactly one RMG iteration wide, and nothing in the twelve standard family checks is on the product
side at all.

The check should report this fixture as FAIL -- 1 of its own products RAISE when fed back in --
and exit 1.
"""

template(reactants=["A", "B"], products=["A-", "B+"], ownReverse=False)

reverse = "Fixture_Own_Product_Raises_Reverse"
reversible = False

allowChargedSpecies = True
electrons = 0

# The electron is moved in the STRUCTURE, not by a charge action: *1 takes it as a radical, *2
# gives one up by breaking a lone pair. update_charge derives both charges afterwards.
recipe(actions=[
    ['GAIN_RADICAL', '*1', 1],
    ['GAIN_RADICAL', '*2', 1],
    ['LOSE_PAIR', '*2', 1],
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
1 *2 [H,O,N] u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]
""",
    kinetics = None,
)

tree(
"""
L1: A
L1: B
"""
)
