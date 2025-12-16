#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Impact_Ionization/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A  + e- => A+ + e- + e-

*1 is always the reactive atom, N and Z are determined by it.

Linked to the VoronovEIArrhenius kinetics object.
"""

template(reactants=["A_rad", "e-"], products=["A+", "e-", "e-"], ownReverse=False)

reverse = "electron_impact_attachment"

reversible = False
custom_kinetics = True
allowChargedSpecies = True
product_electrons = 2

recipe(actions=[
    ['LOSE_RADICAL', '*1', 1],
    ['GAIN_CHARGE', '*1', 1],
])

entry(
    index = 0,
    label = "A_rad",
    group =
"""
1 *1 R u[1,2,3,4] px c[0,+1,+2,+3,+4,+5,+6,+7,+8]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "e-",
    group =
"""
1 *2 e u1 p0 c-1
""",
    kinetics = None,
)

tree(
"""
L1: A_rad
L1: e-
"""
)
