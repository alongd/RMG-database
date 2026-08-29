#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkaline_Alkaline/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A + B <=> AB+ + e-

Where both A and B have two radicals, e.g.: alkaline earth metal atoms or O atoms.
Here Atom A is less electronegative and looses two radicals (one for bonding), while Atom B looses one radical to form the bond.
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
1 *1 R u[2,3,4] px cx
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "alkaline_A",
    group =
"""
1 *1 alkaline u[2,3,4] px cx
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "B",
    group =
"""
1 *2 R u[2,3,4] px cx
""",
    kinetics = None,
)
entry(
    index = 11,
    label = "alkaline_B",
    group =
"""
1 *2 alkaline u[2,3,4] px cx
""",
    kinetics = None,
)

tree(
"""
L1: A
    L2: alkaline_A
L1: B
    L2: alkaline_B
"""
)
