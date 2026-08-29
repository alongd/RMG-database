#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkali_Alkaline/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A + B <=> AB+ + e-

Where A is an alkali metal atom and B is an alkaline earth metal atom.
"""

template(reactants=["A", "B"], products=["AB+"], ownReverse=False)

reverse = "electron_absorbance_and_dissociation_2"

reversible = False
allowChargedSpecies = True
electrons = 1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 1],
    ['LOSE_RADICAL', '*2', 2],
    ['FORM_BOND', '*1', 1, '*2'],
    ['GAIN_CHARGE', '*2', 1],
])

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 [Li,Na,K,H] u1 px cx
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "alkali_A",
    group =
"""
1 *1 [Li,Na,K] u1 px cx
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "H_A",
    group =
"""
1 *1 H u1 px cx
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "B",
    group =
"""
1 *2 [Ca,Mg] u2 px cx
""",
    kinetics = None,
)

tree(
"""
L1: A
    L2: alkali_A
    L2: H_A
L1: B
"""
)
