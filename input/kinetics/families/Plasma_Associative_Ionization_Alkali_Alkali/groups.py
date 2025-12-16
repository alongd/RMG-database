#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkali_Alkali/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A + B <=> AB+ + e-

Where both A and B are alkali atoms with one unpaired electron (Li, Na, K).
"""

template(reactants=["A", "B"], products=["AB+", "e-"], ownReverse=False)

reverse = "electron_absorbance_and_dissociation_1"

reversible = False
custom_kinetics = False
allowChargedSpecies = True
product_electrons = 1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 1],
    ['GAIN_CHARGE', '*1', 1],
    ['FORM_BOND', '*1', 0, '*2'],
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
    label = "alkali",
    group =
"""
1 *1 [Li,Na,K] u1 px cx
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Li_A",
    group =
"""
1 *1 Li u1 px cx
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Na_A",
    group =
"""
1 *1 Na u1 px cx
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "K_A",
    group =
"""
1 *1 K u1 px cx
""",
    kinetics = None,
)

entry(
    index = 5,
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
1 *2 alkali u1 px cx
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Li_B",
    group =
"""
1 *2 Li u1 px cx
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Na_B",
    group =
"""
1 *2 Na u1 px cx
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "K_B",
    group =
"""
1 *2 K u1 px cx
""",
    kinetics = None,
)

tree(
"""
L1: A
    L2: alkali
        L3: Li_A
        L3: Na_A
        L3: K_A
    L2: H_A
L1: B
    L2: Li_B
    L2: Na_B
    L2: K_B
"""
)
