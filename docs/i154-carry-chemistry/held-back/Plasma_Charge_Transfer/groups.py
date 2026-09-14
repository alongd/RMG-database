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
allowChargedSpecies = True
electrons = 0

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

# The charge-specific `Ar+` is listed first on purpose, and generic `Ar` is kept after it.
#
# `pick_wildcards` takes the *first* atomtype when it builds the sample molecule
# (rmgpy/molecule/group.py:2857). Neither `He` nor `Ne` has a charged subtype or any `lone_pairs`
# of its own, so a He-first sample falls back to neutral-helium defaults and comes out as `[He]` at
# charge 0 -- which the root `A` (c[+1,+2,+3,+4]) then rejects. `Ar+` carries lone_pairs=[3] and
# charge=[1], so putting it first builds the sample at +1 ([ArH+]).
#
# "Takes the first atomtype" is only half the mechanism. `pick_wildcards` has a second stage at
# group.py:2921-2925: after the first pass it walks each atom again and, if the chosen atomtype is
# still *generic*, replaces it with the first entry of that atomtype's `.specific` list in
# `allElements` order. `Ar+` is already specific, so it passes through that stage untouched; a
# generic `Ar` in first position would not, and what it became would be decided by `allElements`
# rather than by this file.
#
# The ordering survives a save/load round trip. `to_adjacency_list` emits the list with a plain
# ','.join and no sort (rmgpy/molecule/adjlist.py:967), so re-reading a written-out copy of this
# family preserves `Ar+` in first position. The repair is therefore fragile only against a human
# re-sorting the list by hand, not against RMG's own serialization.
#
# Generic `Ar` must stay in the list as well: the child `Ar_ion` is written on the generic `Ar`
# atomtype, and `Ar+` is *more* specific than `Ar`, so an `Ar+`-only parent stops being a proper
# parent of its own child (kinetics_check_child_parent_relationships).
#
# The matched set is unchanged by all of this -- He+, Ne+, Ar+, Ar2+ and ArH+ all still match,
# measured in docs/i223-charge-transfer-node-repair/logs/parent.stdout.log.
entry(
    index = 13,
    label = "Noble_cation",
    group =
"""
1 *1 [Ar+,Ar,He,Ne] ux px c+1
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

# There is no H2_ion node here, and index 102 is deliberately left unused. I-223 removed it.
#
# "Left unused" holds only for as long as nobody writes this family back out through RMG. Both
# save paths -- KineticsFamily.save_groups (family.py:965) and Database.save(reindex=True)
# (base.py:371) -- go through Group.get_entries_to_save, which renumbers EVERY entry 0..N-1 in tree
# order (base.py:295-296). One save and this file's authored scheme (0, 1, 10, 11, ... 213, 214)
# and every gap in it, including this one, is gone. The gaps carry meaning for a human reader and
# none for RMG, so do not rely on them surviving, and do not read a gap in a machine-written copy
# of this family as evidence that something was deleted.
#
# As authored it was `H u0 p0 c+1` single-bonded to `H u0 p0 c0`, which is not H2+: the one-electron
# bond H2+ actually has cannot be written with integer bond orders, so a single bond hands both
# bonding electrons to the pair and the node sampled as `[H][H-]` at charge -1, failing to descend
# to root A. It also matched nothing -- the family's own dictionary writes H2p_r1 as two *unbonded*
# atoms, `[H+].[H]`, and is_subgraph_isomorphic against the bonded node is False, so training
# reaction 2 descended only as far as H_ion (logs/candidates.stdout.log). The node was dead.
#
# Rewriting it in the unbonded form did make it sample at +1 and match H2p_r1 -- and turned
# kinetics_check_sample_can_react red, because the recipe cannot process the result. LOSE_CHARGE on
# *1 of `[H+].[H]` gives `[H].[H]`, which _generate_product_structures splits into two structures;
# with the partner's product that is three against a product_num of two, so apply_recipe returns
# None (logs/h2-recipe.stdout.log, logs/checks-h2kept.*.log). The family's recipe only moves charge
# and has no bond-forming action, so it can never make H2 out of H2+ -- this chemistry is not a
# member of a charge-only family regardless of how the node is written.
#
# Deleting the node instead turns all twelve family checks green (logs/checks-h2del.stdout.log).
# The cost is that training reaction 2 falls back to the template H_ion;H_anion and is shadowed by
# reaction 1 there -- which is exactly where it sat before this branch (logs/rules-before.stdout.log)
# and costs nothing measurable: the two Tanarro rates differ by 1.064x, and reaction 2 describes a
# reaction this family provably cannot generate, so its rule could only ever have been applied to
# H+ + H-, which reaction 1 already describes (logs/collisions.stdout.log).

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
1    N u0 p1 c0  {2,T}
2 *1 O u0 p1 c+1 {1,T}
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
    group = "OR{H_anion, O_anion}",
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
1 *2 H u0 p1 c-1
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "O_anion",
    group =
"""
1 *2 O ux p3 c-1
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

# Added by I-223. `O_neutral` is `O ux px c0`, so atomic O and molecular O2 both landed on
# it, and the two training reactions that use them -- index 14 (NOp_r1 + O_r2) and index 21
# (NOp_r1 + O2_r2) -- both resolved to the template `NO_ion;O_neutral`. KineticsRules.get_rule
# then kept the lower index and the O2 rate was never used, which is the same silent-shadowing
# defect as the duplicate entry this ticket deleted, one level up. Written concretely, as the
# ground-state triplet, to match the training dictionary's O2_r2.
#
# O_anion still catches both O- and OH- (colliding training 8/10 and 9/12). That merge is left in
# place, and the reason is measured rather than deferred -- but it is provisional, which is the
# part worth reading. Those four entries carry the *identical* rate, so the two templates hold the
# same number and splitting them would change nothing today (logs/collisions.stdout.log). They are
# identical because Tanarro's Table 1 gives 17 of its 23 ion-ion neutralization rows one generic
# value, 14 of them citing a single kinetic-scheme review (logs/tanarro.stdout.log) -- the SOURCE
# does not distinguish these pairs, which is not the same as the tree being at the right
# granularity. The first pair-specific measurement for O- or OH- makes this merge start silently
# discarding data exactly as the N/N2 merge did. So the question of whether OH_anion is a sibling
# or a child of O_anion stays open; it has no rate consequence yet, not no rate consequence ever.
entry(
    index = 213,
    label = "O2_neutral",
    group =
"""
1 *2 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    kinetics = None,
)

# Added by I-223 for the same reason as O2_neutral, and on the same criterion. `N_neutral` is
# `N ux px c0`, so atomic N and molecular N2 both landed on it: training 22 (O2p_r1 + N_r2) and
# training 23 (O2p_r1 + N2_r2) both resolved to `O2_ion;N_neutral`, and get_rule kept the lower
# index, discarding the N2 rate. Unlike the O-/OH- merge these two rates are genuinely different
# -- both [Ozawa2008] Table III, but at least 107x apart everywhere both fits are used (5000-10000
# K; logs/collisions.stdout.log) -- so the merge was destroying real information.
# Written concretely, as the triply-bonded ground state, to match the training dictionary's N2_r2.
#
# THIS NODE MOVES FOUR TRAINING REACTIONS, NOT ONE. Every reaction whose *2 partner is N2 now
# descends here, so besides training 23 it reparents 15 (Op_r1 + N2_r2), 18 (Np_r1 + N2_r2) and
# 19 (Arp_r1 + N2_r2). Measured before and after in logs/rules-before.stdout.log and
# logs/rules.stdout.log. Those three had no collision and were not the reason for the node; they
# move because a tree node applies to everything that descends to it, which is the point of a tree
# and is worth saying out loud rather than letting a reader infer the change was surgical.
#
# The knock-on: O_atom_ion;N_neutral, N_atom_ion;N_neutral and Ar_ion;N_neutral held exact rules
# from training 15, 18 and 19 before, and now hold nothing exact. fill_rules_by_averaging_up --
# which a real rate-rules job always runs, rmgpy/rmg/main.py:610 -- fills each of them by
# averaging over N_neutral's children, of which N2_neutral is the only one carrying a rule. So an
# average over exactly one entry. Measured in logs/averaging.stdout.log: the value those three
# templates return is unchanged to 1.000000x at 1000, 5000 and 10000 K. What changed is the
# PROVENANCE -- "rate rule from training reaction 15" becomes "Average of [training reaction 15
# used for O_atom_ion;N2_neutral]" in the kinetics comment. No number moves; a label does.
# Contrast O2_neutral above, which reparented only training 21 and left nothing empty behind it.
entry(
    index = 214,
    label = "N2_neutral",
    group =
"""
1 *2 N u0 p1 c0 {2,T}
2    N u0 p1 c0 {1,T}
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
    L2: O_cation
        L3: O_atom_ion
        L3: OH_ion
        L3: H2O_ion
        L3: O2_ion
        L3: NO_ion
    L2: N_cation
        L3: N_atom_ion
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
            L4: O2_neutral
        L3: N_neutral
            L4: N2_neutral
"""
)
