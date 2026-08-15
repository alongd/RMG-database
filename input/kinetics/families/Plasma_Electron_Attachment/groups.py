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

Three consequences are structural, and all three are load-bearing:

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

2. **Every member of that union is also a child of the root**, and the invariant
   is exactly that: `set(root.item.components) == {c.label for c in
   root.children}`. It is what keeps generated reactions off the root's own
   rate rule.

   `fill_rules_by_averaging_up` does put an averaged rule on `Attacher`, and
   that average is a bad number - training entries 1 and 2 are effective
   two-body coefficients with a 5 torr third-body density folded in, entry 3 is
   a genuine two-body radiative rate, and their mean is not a rate coefficient
   of any kind. It is tolerable only because no generated reaction can be given
   it. `Database.descend_tree` returns the *root* when a structure matches the
   root but none of its children; with the union and the child set identical,
   any structure the union admits necessarily matches the child that admitted
   it, so descent never stops at `Attacher`.

   Say that precisely, because the looser claim is false: this rule is **not**
   unreachable in general. Ask the rate-rule API for it by name and you get it -
   `get_kinetics_for_template(retrieve_template(['Attacher']), degeneracy=1)`
   returns `A = 13727.2 m^3/(mol*s)`, the mixed average, via family.py:2608/2625.
   That route is open on every family root in the database and is not this
   family's to close. What this family guarantees is the narrower thing that
   matters for a mechanism: nothing RMG *generates* resolves to `Attacher`.

   This is the second attempt at that property. The first kept `O_atom` out of
   the tree entirely, so atomic O resolved to the root and gave it an exact rule,
   and no averaged rule existed anywhere. That worked chemically and was illegal
   structurally: RMG's own database consistency check
   (`test/database/databaseTest.py::kinetics_check_groups_found_in_tree`) walks
   every non-top, non-product group up its parent chain, and a parentless group
   makes it dereference `None`. Do not solve an averaging problem by leaving a
   group out of the tree.

3. Every trained group carries the `multiplicity` of the state its rate was
   measured in, because RMG group matching compares connectivity, radical count,
   lone pairs and charge, and nothing else - two adjacent `O u1 p2 c0` atoms are
   ground-state triplet O2 and singlet-delta O2(a1Dg) alike. Without
   `multiplicity [3]` on `O_in_O2`, O2(a1Dg) - one of the dominant excited
   species in an oxygen discharge, with its own attachment behaviour - collects
   the ground-state triplet rate to four significant figures. `Group.multiplicity`
   is a matched constraint (`rmgpy/molecule/group.py`, enforced in
   `Molecule.is_subgraph_isomorphic`), it constrains the multiplicity of the
   *whole* matched molecule, and it needs no engine change.

   `O_in_OH` [2] and `O_atom` [3] are stated for the same reason but are, today,
   unfalsifiable rather than load-bearing, and that is deliberate. Charge is
   derived, so `O u1 p2 c0` fixes the bond count at one and `O u2 p2 c0` at zero:
   `O_in_OH` can only ever match the whole two-atom molecule OH, and `O_atom`
   only lone atomic O. A single unpaired electron admits only a doublet, and an
   atom bearing two unpaired electrons in a multiplicity-1 molecule is rejected
   outright by RMG's adjacency-list checker (`ConsistencyChecker.check_hund_rule`),
   so no other multiplicity is representable for either. Constraining them
   therefore loses no legitimate match, and records that these are ground-state
   rates for the day a wider group or an excited-state representation arrives.

   KNOWN LIMITATION, upstream of this family and not fixable in it: RMG erases
   the spin state before the group ever sees it.
   `resonance.generate_resonance_structures` opens with `mol.update()`
   (rmgpy/molecule/resonance.py:197), and `Molecule.update_multiplicity`
   recomputes `multiplicity = radical_count + 1` unconditionally
   (rmgpy/molecule/molecule.py:1595), so a species declared `multiplicity 1`
   with two unpaired electrons comes back relabelled `multiplicity 3` - and is
   then isomorphic to ground-state O2, so RMG would not carry it as a distinct
   species at all. The group constraint is still correct and still refuses a
   singlet that reaches it as a singlet; what it cannot do is survive an engine
   that rewrites the reactant first. Pinned by
   test_known_limitation_resonance_generation_erases_declared_multiplicity.

If training data for another attacher arrives, add its group to the union **and**
as an L2 node - both, always, or generation starts resolving to the root
average - and give
the group the multiplicity of the state its rate was measured in. Do not widen an
existing group to cover it.

Consequences of the recipe, stated explicitly because they bound the family:

1. LOSE_RADICAL requires at least one unpaired electron on *1. Closed-shell
   attachers (SF6, CO2, N2O, ...) cannot be matched by this recipe at all. That
   is a recipe limitation, not an oversight; it is now doubly enforced, since
   every group in the union also carries u[1,2].
2. GAIN_PAIR must be a legal action on the *generic* atomtype of *1, because the
   product template is built by applying the recipe to the root group itself.
   Against the RMG-Py this family targets, `increment_lone_pair` is wired for
   H, C, N, O, P, S, F, Cl and Br; the one element it is still empty for is
   **iodine**, which therefore could not appear in this tree even if data
   arrived. Everything else - the halogens included - is absent from this family
   for one reason only: **there is no training data for it here**, not because
   RMG cannot represent it. (This file previously claimed F, H and Cl had no
   `increment_lone_pair` action; the charged-atomtype work has since closed that
   gap, and widening to the halogens is now a training-data ticket.) Only oxygen
   has training data, so only oxygen is in the tree.

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
multiplicity [3]
1 *1 O u2 p2 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O_in_OH",
    group =
"""
multiplicity [2]
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
multiplicity [3]
1 *1 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    kinetics = None,
)

# Every member of the `Attacher` union is an L2 node here, and must stay that
# way: that identity is what keeps generated reactions off the root's averaged
# rule, since `descend_tree` only stops at the root when no child matches.
# Adding a union member without its L2 node hands the mixed pressure-baked/
# radiative average to whatever the new member admits. (The rate-rule API can
# still fetch that average by name - see point 2 of longDesc.)
tree(
"""
L1: Attacher
    L2: O_atom
    L2: O_in_OH
    L2: O_in_O2
"""
)
