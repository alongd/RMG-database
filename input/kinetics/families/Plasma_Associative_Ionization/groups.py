#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization/groups"
shortDesc = u""
longDesc = u"""
4.5.
This family describes reactions of the sort:

A + B <=> AB+ + e-

*1 looses two rads, one for forming a bond, one is the free electron.
*2 looses one rad, for forming the bond.
"""

template(reactants=["A", "B"], products=["AB+", "e-"], ownReverse=False)

reverse = "electron_absorbance_and_dissociation"

reversible = True
custom_kinetics = False
allowChargedSpecies = True
product_electrons = 1

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
    label = "B",
    group =
"""
1 *2 R u[1,2,3,4] px cx
""",
    kinetics = None,
)

tree(
"""
L1: A
L1: B
"""
)
