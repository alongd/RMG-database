#!/usr/bin/env python
# encoding: utf-8

name = "Fixture_Wrong_Products/groups"
shortDesc = u"Test fixture: a family that generates its training reaction and survives its product."
longDesc = u"""
NOT CHEMISTRY. This is test data for check_family_generates.py. The rate is a placeholder.

The reference fixture. It carries one real charge-transfer reaction, O+ + N2 -> N2+ + O, and both
of the check's assertions hold on it:

    it generates that reaction from its own training reactants          -> not INERT
    its product N2+, fed back in as a reactant, does not raise          -> survives itself

Its two siblings differ from it by exactly one line each. See ../README.md.

Both roots name the elements their own subtrees use. That is the point of the fixture: a root
written as `R` is broader than the chemistry underneath it, and generation matches the ROOT.
"""

template(reactants=["A", "B"], products=["A-", "B+"], ownReverse=False)

reverse = "Fixture_Wrong_Products_Reverse"
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
1 *1 [H,O,metal] ux p[0,2] c[+1,+2,+3,+4]
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
