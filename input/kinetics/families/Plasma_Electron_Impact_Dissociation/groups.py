#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Impact_Dissociation/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

AB + e- => A + B + e-
"""

template(reactants=["AB", "e-"], products=["A", "B", "e-"], ownReverse=False)

reverse = "electron_cation_recombination"

reversible = False
custom_kinetics = False
allowChargedSpecies = True
product_electrons = 1

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['GAIN_RADICAL', '*1', 1],
    ['GAIN_RADICAL', '*2', 1],
])

entry(
    index = 0,
    label = "AB",
    group =
"""
1 *1 R ux px c[0,+1,+2,+3,+4,+5,+6,+7,+8] {2,S}
2 *2 R ux px c[0,+1,+2,+3,+4,+5,+6,+7,+8] {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "e-",
    group =
"""
1 *3 e u1 p0 c-1
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "HH",
    group =
"""
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "OO",
    group =
"""
1 *1 O u1 p2 c0 {2,S}
2 *2 O u1 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "MM",
    group =
"""
1 *1 [Li,Na,K,Ca,Mg] u0 p0 c0 {2,S}
2 *2 [Li,Na,K,Ca,Mg] u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Na2",
    group =
"""
1 *1 Na u0 p0 c0 {2,S}
2 *2 Na u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "K2",
    group =
"""
1 *1 K u0 p0 c0 {2,S}
2 *2 K u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "NaK",
    group =
"""
1 *1 Na u0 p0 c0 {2,S}
2 *2 K u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: AB
    L2: HH
    L2: OO
    L2: MM
        L3: Na2
        L3: K2
        L3: NaK
L1: e-
"""
)
