#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Attachment/groups"
shortDesc = u"Non-dissociative electron attachment forming a negative ion"
longDesc = u"""
Non-dissociative (radiative or three-body-stabilized) electron attachment:

    A(*1) + e-  =>  A-(*1)

A neutral species captures a free electron and becomes a mono-anion. No bond is
made or broken, so this family covers *only* the non-dissociative channel;
dissociative attachment (A + e- => B- + C) breaks a bond and is a different
recipe, deliberately out of scope here.

The recipe is LOSE_RADICAL + GAIN_PAIR on the attaching atom *1. Charge in RMG
is derived from the electron count, never declared, so the pair
(-1 unpaired electron, +1 lone pair) is what adds one electron to *1 and drives
its formal charge to -1. Using LOSE_CHARGE instead would silently return the
neutral radical.

    O2  [O][O]         u1 p2 c0  ->  u0 p3 c-1   =>  O2- (O0sc + O2s)
    OH  [O]H           u1 p2 c0  ->  u0 p3 c-1   =>  OH- (O0sc)
    O   [O]            u2 p2 c0  ->  u1 p3 c-1   =>  O-  (O0sc)

Consequences of that recipe, stated explicitly because they bound the family:

1. LOSE_RADICAL requires at least one unpaired electron on *1, so the root group
   carries u[1,2,3,4]. Closed-shell attachers (SF6, CO2, N2O, ...) cannot be
   matched by this recipe at all. That is a recipe limitation, not an oversight.
2. GAIN_PAIR must be a legal action on the *generic* atomtype of *1, because the
   product template is built by applying the recipe to the root group itself.
   `ATOMTYPES['F'].increment_lone_pair` is empty (atomtype.py:853), as are H's and
   Cl's, so F cannot appear in this root group *even though the F0sc anion
   atomtype exists*. The elements that work are C, N, O, P and S. H-, Cl-, Br-
   and I- do not resolve at all. If RMG-Py gains a generic "any singly-negative
   atom" charge-class parent atomtype, the single element list on the root
   group's line 1 is the only line that needs to change.

KNOWN LIMITATION - the root group cannot require a neutral reactant. RMG groups
match subgraphs, so no group can express "the whole molecule is neutral": the
radical oxygen of O2- (u1 p2 c0) is locally identical to an oxygen of O2, and a
single-atom group cannot exclude a bonded context either. `allowChargedSpecies`
is two-sided (it permits charged reactants *and* products together, family.py
line ~1714), and `generatedSpeciesConstraints` has no charge key. The family
therefore also generates O2- + e- => O2(2-), which is spurious. Blocking it needs
a one-sided neutral-reactant check in RMG-Py; the behaviour is pinned by
test/test_plasma_electron_attachment.py so the fix will be visible when it lands.

The electron is not a template reactant. It is carried by `electrons = -1`, the
same mechanism the Surface_Proton_Electron_Reduction_* families use, which is
what lets the charge balance close (reactant net charge 0 + (-1) = -1 = product
net charge) without leaving an unconsumed electron fragment on the product side.
"""

template(reactants=["Attacher"], products=["Anion"], ownReverse=False)

reversible = False

reactantNum = 1
productNum = 1

allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 1],
    ['GAIN_PAIR', '*1', 1],
])

entry(
    index = 1,
    label = "Attacher",
    group =
"""
1 *1 [C,N,O,P,S] u[1,2,3,4] px c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "O_attacher",
    group =
"""
1 *1 O u[1,2] p2 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O_atom",
    group =
"""
1 *1 O u2 p2 c0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O_monoradical",
    group =
"""
1 *1 O u1 p2 c0 {2,S}
2    R u[0,1] px c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O_in_OH",
    group =
"""
1 *1 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O_in_O2",
    group =
"""
1 *1 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Attacher
    L2: O_attacher
        L3: O_atom
        L3: O_monoradical
            L4: O_in_OH
            L4: O_in_O2
"""
)
