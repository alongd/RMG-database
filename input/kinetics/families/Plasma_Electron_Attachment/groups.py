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

THE TREE MATCHES ONLY WHAT THE TRAINING SET SUPPORTS
----------------------------------------------------
Electron-attachment rate coefficients span many orders of magnitude between
species and track electron affinity and resonance structure, not the local
connectivity RMG can see. There is no group-additivity trend to interpolate
along, so an "estimate" produced by averaging these three entries is not an
uncertain number, it is a fabricated one - and in a plasma mechanism it lands
directly on the electron balance. This family therefore matches exactly the
three shapes it has data for and nothing else.

Two consequences are structural, and both are load-bearing:

1. The root `Attacher` is a union (LogicOr) of the three trained groups, not a
   single wide group. A single Group cannot express "atomic O, or the O of OH,
   or the O of O2" and exclude everything else: any plain group broad enough to
   cover atomic O (u2, no bonds) and the two monoradicals is also broad enough
   to cover HO2, CH3O and every other RO. Before this was a union, the root
   admitted `[C,N,O,P,S]` with an all-oxygen tree beneath it, and
   `fill_rules_by_averaging_up` handed the oxygen average to CH3, N, S and P.
   A LogicNode template reactant is a supported RMG construct - see
   `elec_def` in 1+2_Cycloaddition, and family.py `generate_product_template`,
   which expands LogicNodes explicitly.

2. `O_atom` is a member of that union but is deliberately NOT a node in the
   tree. `Database.descend_tree` returns the *root* when a structure matches it
   but matches none of its children, so atomic O resolves to `Attacher` itself
   and the O + e- => O- training reaction gives the root an exact rate rule.
   `KineticsRules.fill_rules_by_averaging_up` keeps any existing rule of rank>0
   rather than averaging over children, so with all three training reactions
   landing on tree nodes - `Attacher`, `O_in_OH`, `O_in_O2` - **no averaged rate
   rule is created anywhere in this family**. That is the fix for the second
   defect: training entries 1 and 2 are effective two-body coefficients with a
   5 torr third-body density folded in, entry 3 is a genuine two-body radiative
   rate, and their mean is not a rate coefficient of any kind. Adding `O_atom`
   as an L2 node would move that training reaction off the root and silently
   restore the mixed average - do not do it.

If training data for another attacher arrives, add its group to the union and,
if it is a monoradical, as an L2 node; do not widen an existing group to cover
it.

Consequences of the recipe, stated explicitly because they bound the family:

1. LOSE_RADICAL requires at least one unpaired electron on *1. Closed-shell
   attachers (SF6, CO2, N2O, ...) cannot be matched by this recipe at all. That
   is a recipe limitation, not an oversight; it is now doubly enforced, since
   every group in the union also carries u[1,2].
2. GAIN_PAIR must be a legal action on the *generic* atomtype of *1, because the
   product template is built by applying the recipe to the root group itself.
   `ATOMTYPES['F'].increment_lone_pair` is empty (atomtype.py:853), as are H's
   and Cl's, so F could not appear in this tree *even though the F0sc anion
   atomtype exists*. The elements that work at all are C, N, O, P and S - but
   only oxygen has training data here, so only oxygen is in the tree. Widening
   to the halogens needs both an RMG-Py atomtype and training data.

KNOWN LIMITATION - a group cannot require a neutral reactant. RMG groups match
subgraphs, so no group can express "the whole molecule is neutral", and
`allowChargedSpecies` is two-sided (it permits charged reactants *and* products
together, family.py line ~1714) while `generatedSpeciesConstraints` has no
charge key. Blocking anion re-attachment needs a one-sided neutral-reactant
check in RMG-Py, which does not exist. This family no longer generates
O2- + e- => O2(2-), but only incidentally: the radical oxygen of O2- is bonded
to O0sc rather than to another O u1 p2 c0, so it falls outside the union. The
RMG-Py gap is unfixed and the next family that needs a wider group will meet it
again; test/test_plasma_electron_attachment.py pins the current behaviour.

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
    group = "OR{O_atom, O_in_OH, O_in_O2}",
    kinetics = None,
)

entry(
    index = 2,
    label = "O_atom",
    group =
"""
1 *1 O u2 p2 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O_in_OH",
    group =
"""
1 *1 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O_in_O2",
    group =
"""
1 *1 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    kinetics = None,
)

# `O_atom` is intentionally absent from this tree: it is a member of the
# `Attacher` union only, so that atomic O resolves to the root and the
# O + e- => O- training reaction gives the root an exact rule instead of an
# average. See point 2 of longDesc before changing this.
tree(
"""
L1: Attacher
    L2: O_in_OH
    L2: O_in_O2
"""
)
