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

# reversible was True until I-223. It is False because RMG generates the reverse direction from a
# template this file cannot author, and that reverse crashes.
#
# generate_reactions runs the reverse whenever `not own_reverse and reversible`
# (family.py:1882-1891), using `reverse_template`. For this family that template is not written
# anywhere -- RMG FABRICATES it by applying the recipe to the root groups, which is where the
# `A-` and `B+` named in template() above come from. So the reverse admits whatever the forward
# roots produce, and nothing in this file can narrow it.
#
# Measured: the reverse applies LOSE_RADICAL to *1, and on O+ (`O u1 p2 c+1`) that gives
# `O u0 p2 c+2` -- an O++ with no atom type -- so generate_reactions raises AtomTypeError and takes
# the job with it. Two of 91 reactant pairs drawn from this family's own training set crash that
# way, and one of them IS training entry 7 (O+ + O- -> O + O), so the family could not even
# reproduce its own entry. With reversible = False: 0 crashes, 45 reactions, 15 of 15 entries
# reproduced. See logs/generate.stdout.log.
#
# What this COSTS, stated plainly: RMG will not construct the reverse of these reactions. That is
# tolerable here only because this family already declares its reverse to be a DIFFERENT family
# (`reverse = "Plasma_Charge_Transfer_Reverse"`, below) -- and that family does not exist in this
# repository, so the reverse chemistry is currently UNREPRESENTED rather than handled elsewhere.
# If the reverse family is ever written, revisit this line first.
reversible = False
allowChargedSpecies = True
electrons = 0

# THERE IS NO CHARGE ACTION IN THIS RECIPE, AND THAT IS DELIBERATE (I-223).
#
# The previous recipe was ['LOSE_CHARGE','*1',1] + ['GAIN_CHARGE','*2',1] and it did NOTHING.
# An atom's charge is DERIVED, not stored: LOSE_CHARGE/GAIN_CHARGE set atom.charge and touch
# nothing else (molecule.py:538-548), and apply_recipe then calls update_charge() on every product
# (family.py:1547), which recomputes charge = valence - bonds - radicals - 2*lone_pairs
# (molecule.py:596-598). None of those three moved, so the charge went straight back and the
# products came out isomorphic to the reactants; _create_reaction discards those
# (family.py:1757-1759) and the family generated ZERO reactions.
#
# So to move an electron you must move it in the STRUCTURE and let update_charge derive the
# charge. Measured over the whole nine-action grammar (probe_grammar.py): GAIN_RADICAL is the only
# single-atom action that moves exactly one electron; GAIN_PAIR/LOSE_PAIR move two; the bond
# actions move one onto each of two atoms and need a second label; the two charge actions move
# none. Hence:
#
#     *1 accepts the electron as an unpaired radical   -> GAIN_RADICAL *1
#     *2 donates one by breaking a lone pair           -> GAIN_RADICAL *2 + LOSE_PAIR *2
#
# This is one of exactly four possible two-label recipes, and it is the one that serves the most
# training entries -- 16 of 27 before the templates were narrowed for crash-safety, 15 after.
# The other three, and the eleven entries that no recipe in the grammar can serve, are in
# report.md section 12. Do not "generalise" this recipe: LOSE_RADICAL on a closed-shell atom
# RAISES ActionError rather than misbehaving, which is why one recipe cannot cover the rest.
recipe(actions=[
    ['GAIN_RADICAL', '*1', 1],
    ['GAIN_RADICAL', '*2', 1],
    ['LOSE_PAIR', '*2', 1],
])

# Forbidden products. THESE MUST CARRY THE RECIPE'S ATOM LABELS OR THEY SILENTLY NEVER FIRE.
# Measured (probe_grammar.py, and report.md section 12): an UNLABELLED forbidden group returns
# True from is_molecule_forbidden when called on a label-free molecule, and False on the same
# molecule at generation time, because the product still carries *1/*2 there. The unlabelled form
# blocks nothing at all; the labelled form blocks correctly. apply_recipe's own docstring hints at
# this ("product atom labels ... to assist in identifying forbidden structures") but nothing
# enforces it, so an unlabelled entry here looks like a guard and is not one.
#
# What they are for: an RMG group constrains ATOMS, not the net charge of a MOLECULE. Root B below
# therefore matches a neutral atom sitting inside a cation -- the nitrogen of NO+, the neutral
# oxygen of O2+ -- and without these the family generates cation + cation "charge transfer",
# 19 of 82 reactions, producing dications like [O+][O+]. With them: 0 of 45.
forbidden(
    label = "like_charge_transfer_star1",
    group =
"""
1 *1 R ux px c[+1,+2,+3,+4] {2,[S,D,T,Q]}
2    R ux px c[+1,+2,+3,+4] {1,[S,D,T,Q]}
""",
    shortDesc = u"""Two bonded cations in a product: the donor was itself a cation.""",
)

forbidden(
    label = "like_charge_transfer_star2",
    group =
"""
1 *2 R ux px c[+1,+2,+3,+4] {2,[S,D,T,Q]}
2    R ux px c[+1,+2,+3,+4] {1,[S,D,T,Q]}
""",
    shortDesc = u"""As above, with the label on the donor atom.""",
)

forbidden(
    label = "excited_O2_cation",
    group =
"""
1 *2 O u2 p1 c+1 {2,[S,D,T,Q]}
2    R ux px cx  {1,[S,D,T,Q]}
""",
    shortDesc = u"""O2+ in the state this recipe would otherwise make it in.""",
    longDesc = u"""
O2 donating from a lone pair gives `O u2 p1 c+1`, but O2+ ground state is `O u0 p2 c+1` bonded to
`O u1 p2 c0` -- the electron O2 actually loses is an unpaired one, which is LOSE_RADICAL, a
different recipe. Without this entry the family generates the reverse of training entry 13
(O+ + O2 -> O + O2+) with a wrong-state O2+: green, and wrong. Measured: it is the only such case
left once the roots are narrowed, and blocking it takes the wrongly-served training entries from
1 to 0 at a cost of 18 of 63 generated reactions.
""",
)

# Root Definitions

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 R ux p[0,2] c[+1,+2,+3,+4]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "B",
    group =
"""
1 *2 R u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]
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
1 *1 O ux p2 c+1
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Metal_cation",
    group =
"""
1 *1 metal ux p0 c+1
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
    index = 114,
    label = "O2_ion",
    group =
"""
1 *1 O u0 p2 c+1 {2,S}
2    O u1 p2 c0  {1,S}
""",
    kinetics = None,
)

# Nitrogen cations, noble-gas cations, NO+ and H2O+ are NO LONGER IN THIS TREE (I-223).
# They were removed together with the nodes N_cation (12), N_atom_ion (121), NO_ion (122),
# Noble_cation (13), Ar_ion (131) and H2O_ion (113), because the narrowed root A below is
# `p[0,2]` and every one of them sits at `p1` or `p3`:
#
#   N+   `N u2 p1 c+1`   Ar+  `Ar u1 p3 c+1`   NO+  `O u0 p1 c+1`   H2O+ `O u1 p1 c+1`
#
# Root A cannot admit them, because the recipe above breaks on them -- GAIN_RADICAL turns H2O+
# into `O u2 p1` with two single bonds and NO+ into `O u1 p1` with a triple bond, and NEITHER HAS
# AN ATOM TYPE, so generate_reactions raises AtomTypeError and takes the RMG job with it. Ar+
# does have a typeable product but the wrong one: `Ar u2 p3`, not ground-state `Ar u0 p4`.
#
# N+ is the painful one. It needs `p1`, it would work perfectly well with this recipe, and it is
# excluded only because a group's `u` and `p` lists are a CROSS PRODUCT, not a disjunction: any
# root admitting `N u2 p1` also admits `O u1 p1` (H2O+) and `O u0 p1` (NO+), which crash. The
# vocabulary that would separate them is a charge-specific atom type per element, and the engine
# defines exactly six -- Li+ Na+ K+ Mg+ Ca+ Ar+ -- none for N, O or H. Adding one is an engine
# change and out of scope. Training entry 18 (N+ + N2) is the cost, and it is recorded with the
# other eleven in training/reactions-unrepresentable.py.

# Metal cations
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
1 *2 O u[0,1] p3 c-1
""",
    kinetics = None,
)

# Neutrals
entry(
    index = 212,
    label = "N_neutral",
    group =
"""
1 *2 N u[0,1] p1 c0
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
        L3: O2_ion
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
    L2: N_neutral
        L3: N2_neutral
"""
)
