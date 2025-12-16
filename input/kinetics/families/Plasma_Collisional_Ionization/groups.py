#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Collisional_Ionization/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A  + M => A+ + e- + M

*1 is always the reactive atom.

This is a heavy particle impact ionization, where M != e-
The case for M = e- is handled by the Plasma_Electron_Impact_Ionization family.

There are four distinct cases for M:
- Air species (N, O, NO)
- Alkali metals (Li, Na, K, Ca)
- Silicon chemistry group (Si, SiH_x)
- And noble gases (Ar, He).

Todo:
    Add more training reactions for the various groups.
    Create a tree below as needed according to training reactions.
"""

template(reactants=["A_rad", "M"], products=["A+", "e-", "M"], ownReverse=False)

reverse = "electron_cation_recombination"

reversible = False
custom_kinetics = False
allowChargedSpecies = True
product_electrons = 1

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
    label = "M",
    group = "OR{N2, N, O2, O, Ar, He}",
    kinetics = None,
)

entry(
    index = 2,
    label = "N2",
    group =
"""
1 *2 N u0 p1 c0 {2,T}
2    N u0 p1 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "N",
    group =
"""
1 *2 N u3 p1 c0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O2",
    group =
"""
1 *2 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O",
    group =
"""
1 *2 O u2 p2 c0
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Ar",
    group =
"""
1 *2 Ar ux px cx
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "He",
    group =
"""
1 *2 He ux px cx
""",
    kinetics = None,
)

tree(
"""
L1: A_rad
L1: M
    L2: N2
    L2: N
    L2: O2
    L2: O
    L2: Ar
    L2: He
"""
)
