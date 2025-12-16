#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Ion_Molecule_Association/groups"
shortDesc = u""
longDesc = u"""
4.6.
This family describes reactions of the sort:

A+ + B (+M) <=> AB+ (+M)

If no training reactions are available, just use R Recombination instead
"""

template(reactants=["A", "B"], products=["AB+"], ownReverse=False)

reverse = "cation_dissociation"

reversible = True
custom_kinetics = False
allowChargedSpecies = True
product_electrons = 0

recipe(actions=[
    # ['LOSE_RADICAL', '*1', 2],
    ['LOSE_RADICAL', '*2', 1],
    ['FORM_BOND', '*1', 0, '*2'],
])

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 R ux px c[+1,+2,+3,+4,+5,+6,+7,+8]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "B",
    group =
"""
1 *2 R u[1,2,3,4] px c0
""",
    kinetics = None,
)

# -----------------------------------------------------------------------------
# Cation Tree (A)
# -----------------------------------------------------------------------------

entry(
    index = 10,
    label = "Alkali_Cation",
    group =
"""
1 *1 [Li,Na,K] u0 px c+1
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Li_Cation",
    group =
"""
1 *1 Li u0 px c+1
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Na_Cation",
    group =
"""
1 *1 Na u0 px c+1
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "AlkalineEarth_Cation",
    group =
"""
1 *1 [Mg,Ca] u1 px c+1
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Mg_Cation",
    group =
"""
1 *1 Mg u1 px c+1
""",
    kinetics = None,
)

# -----------------------------------------------------------------------------
# Neutral Tree (B)
# -----------------------------------------------------------------------------

entry(
    index = 100,
    label = "Hydrogen",
    group =
"""
1 *2 H u1 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: A
    L2: Alkali_Cation
        L3: Li_Cation
        L3: Na_Cation
    L2: AlkalineEarth_Cation
        L3: Mg_Cation
L1: B
    L2: Hydrogen
"""
)
