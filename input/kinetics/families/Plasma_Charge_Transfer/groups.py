#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Charge_Transfer/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A+ + B <=> A + B+  ;  A+ + B- <=> A + B  ;  A++ + B- <=> A+ + B
"""

template(reactants=["A", "B"], products=["A-", "B+"], ownReverse=False)

reverse = "Plasma_Charge_Transfer_Reverse"

reversible = True
custom_kinetics = False
allowChargedSpecies = True
product_electrons = 0

recipe(actions=[
    ['LOSE_CHARGE', '*1', 1],
    ['GAIN_CHARGE', '*2', 1],
])

# Root Definitions

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 R ux px c[+1,+2,+3,+4]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "B",
    group =
"""
1 *2 R ux px c[0,-1,-2,-3,-4]
""",
    kinetics = None,
)

# -----------------------------------------------------------------------------
# Tree for Cation (*1)
# -----------------------------------------------------------------------------

# --- Level 1: Main Atom Type ---

entry(
    index = 10,
    label = "H_cation",
    group =
"""
1 *1 H ux p0 c+1
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O_cation",
    group =
"""
1 *1 O ux px c+1
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "N_cation",
    group =
"""
1 *1 N ux px c+1
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Noble_cation",
    group =
"""
1 *1 [He,Ne,Ar] ux px c+1
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Metal_cation",
    group =
"""
1 *1 metal ux px c+1
""",
    kinetics = None,
)

# --- Level 2: Specific Structures ---

# Hydrogen Cations
entry(
    index = 101,
    label = "H_ion",
    group =
"""
1 *1 H u0 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "H2_ion",
    group =
"""
1 *1 H u0 p0 c+1 {2,S}
2    H u1 p0 c0  {1,S}
""",
    kinetics = None,
)

# Oxygen Cations
entry(
    index = 111,
    label = "O_atom_ion",
    group =
"""
1 *1 O u1 p2 c+1
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "OH_ion",
    group =
"""
1 *1 O u0 p2 c+1 {2,S}
2    H u0 p0 c0  {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "H2O_ion",
    group =
"""
1 *1 O u1 p1 c+1 {2,S} {3,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "O2_ion",
    group =
"""
1 *1 O u0 p2 c+1 {2,S}
2    O u1 p2 c0  {1,S}
""",
    kinetics = None,
)

# Nitrogen Cations
entry(
    index = 121,
    label = "N_atom_ion",
    group =
"""
1 *1 N u2 p1 c+1
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "NO_ion",
    group =
"""
1 *1 N u0 p1 c+1 {2,D}
2    O u0 p2 c0  {1,D}
""",
    kinetics = None,
)

# Noble Cations
entry(
    index = 131,
    label = "Ar_ion",
    group =
"""
1 *1 Ar u1 p3 c+1
""",
    kinetics = None,
)

# Metal Cations
entry(
    index = 141,
    label = "Li_ion",
    group =
"""
1 *1 Li u0 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Na_ion",
    group =
"""
1 *1 Na u0 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "K_ion",
    group =
"""
1 *1 K u0 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Mg_ion",
    group =
"""
1 *1 Mg u1 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Ca_ion",
    group =
"""
1 *1 Ca u1 p0 c+1
""",
    kinetics = None,
)

# -----------------------------------------------------------------------------
# Tree for Partner (*2)
# -----------------------------------------------------------------------------

# --- Level 1: Charge State ---

entry(
    index = 20,
    label = "Anion",
    group =
"""
1 *2 R ux px c-1
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Neutral",
    group =
"""
1 *2 R ux px c0
""",
    kinetics = None,
)

# --- Level 2: Specific Partners ---

# Anions
entry(
    index = 201,
    label = "H_anion",
    group =
"""
1 *2 H u0 px c-1
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "O_anion",
    group =
"""
1 *2 O ux px c-1
""",
    kinetics = None,
)

# Neutrals
entry(
    index = 211,
    label = "O_neutral",
    group =
"""
1 *2 O ux px c0
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "N_neutral",
    group =
"""
1 *2 N ux px c0
""",
    kinetics = None,
)

# -----------------------------------------------------------------------------
# Tree Definition
# -----------------------------------------------------------------------------

tree(
"""
L1: A
    L2: H_cation
        L3: H_ion
        L3: H2_ion
    L2: O_cation
        L3: O_atom_ion
        L3: OH_ion
        L3: H2O_ion
        L3: O2_ion
    L2: N_cation
        L3: N_atom_ion
        L3: NO_ion
    L2: Noble_cation
        L3: Ar_ion
    L2: Metal_cation
        L3: Li_ion
        L3: Na_ion
        L3: K_ion
        L3: Mg_ion
        L3: Ca_ion

L1: B
    L2: Anion
        L3: H_anion
        L3: O_anion
    L2: Neutral
        L3: O_neutral
        L3: N_neutral
"""
)
