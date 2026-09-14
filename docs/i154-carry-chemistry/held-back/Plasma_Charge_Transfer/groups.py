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

# reversible is False, and round 61 was right that this costs more than it looks like it costs.
#
# WHAT IT ALSO DOES, which was not understood when it was set. `reversible` does not merely decide
# whether RMG generates the reverse DIRECTION. `_create_reaction` passes it straight into
# `TemplateReaction(reversible=...)`, so it also makes every GENERATED reaction irreversible.
# Training entry 15's own reaction is reversible and comes out of this family irreversible, and its
# reverse kinetics are therefore SUPPRESSED rather than derived from equilibrium. That is a real
# loss of chemistry, not a bookkeeping detail, and "the reverse family does not exist" was never a
# reason for it.
#
# SO WHY IS IT STILL FALSE? Because True still crashes, measured on the narrowed roots with N+
# admitted (logs/generate-r61-reversible.stdout.log): 6 crashes over the 14 training species,
# including TRAINING ENTRY 7 ITSELF (O+ + O-), which the family then cannot reproduce -- 15 of 16
# instead of 16 of 16. The reverse applies LOSE_RADICAL to *1 and on O+ (`O u1 p2 c+1`) that gives
# `O u0 p2 c+2`, an O++ with no atom type. Narrowing the roots did NOT remove this; it was the
# root-B crash surface that the narrowing removed.
#
# A WARNING ABOUT MEASURING THIS. Setting `family.reversible = True` on a LOADED family proves
# nothing. `reverse_template` is built at load time and ONLY if reversible was true then
# (family.py:721-724), so a post-load flip leaves it None, the reverse pass never runs, and you
# measure zero crashes and conclude the opposite of the truth. This comment nearly said exactly
# that. Measure it by editing this line and reloading.
#
# The only real alternative is to write Plasma_Charge_Transfer_Reverse, which is a new family and
# a new ticket. Until then reverse chemistry from this family is UNREPRESENTED -- stated plainly
# here and in report.md section 16 rather than left implicit in one keyword.
#
# The original observation, kept because it is still true of the fabricated template:
#
# generate_reactions runs the reverse whenever `not own_reverse and reversible`
# (family.py:1882-1891), using `reverse_template`. For this family that template is not written
# anywhere -- RMG FABRICATES it by applying the recipe to the root groups, which is where the
# `A-` and `B+` named in template() above come from. So the reverse admits whatever the forward
# roots produce, and nothing in this file can narrow it.
#
# Measured, and re-measured in round 61 on the narrowed roots with N+ admitted: the reverse
# applies LOSE_RADICAL to *1, and on O+ (`O u1 p2 c+1`) that gives `O u0 p2 c+2` -- an O++ with no
# atom type -- so generate_reactions raises AtomTypeError and takes the job with it. 6 of the 105
# reactant pairs drawn from this family's own training species crash that way, and one of them IS
# training entry 7 (O+ + O- -> O + O), so the family cannot reproduce its own entry: 15 of 16
# instead of 16 of 16. With reversible = False: 0 crashes, 50 reactions, 16 of 16 reproduced.
# See logs/generate-r61-reversible.stdout.log against logs/generate-r61-final.stdout.log.
#
# A second thing the fabricated reverse template gets WRONG, recorded because it is invisible: the
# product templates keep the REACTANT-side charge lists. GAIN_RADICAL and LOSE_PAIR change a
# GroupAtom's u and p but never its c, so the generated `A-` is
# `[H,O,metal] u[1,2,3,4] p[0,2] c[+1,+2,+3,+4]` -- still positive, when the acceptor has just
# been neutralised -- and `B+` is `[N,O,H] u[1,2] p[0,1,2,3] c[0,-1,-2,-3,-4]` -- still neutral or
# negative, when the donor has just become a cation. Both are charge-wrong. Anyone reasoning about
# the reverse from `template()` will otherwise trust two groups that are backwards.
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
# training entries -- 16 of 27, both before the templates were narrowed for crash-safety and
# after, once round 61 restored N+ to root A.
# The other three, and the eleven entries this recipe cannot serve -- only FOUR of which exceed
# the two-label template at all -- are in
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
#
# READ THIS BEFORE TRUSTING THEM. THEY ONLY BLOCK **BONDED** POSITIVE CENTRES, AND THAT IS NOT THE
# SAME AS BLOCKING LIKE-CHARGE REACTIONS. Round 61 found the gap and probe_likecharge.py measured
# it. When the two positive centres are not bonded, nothing fires:
#
#     Li+  +  [NH3+]CCO   ->   [Li]  +  [NH3+]CC[OH+]
#
# one reaction, reactant charges (+1, +1), product charges (0, +2), is_balanced() True, every
# guard silent -- and it then inherits the Li_ion;B rate estimated from Li+/H- MUTUAL
# NEUTRALISATION, the opposite physical process. Over a 150-cation set there are 470 such
# reactions (logs/likecharge.stdout.log).
#
# THIS CANNOT BE FIXED HERE. Four candidate root-B narrowings were measured, down to writing N2
# out atom by atom alongside the anion nodes; the count goes 470 -> 200 -> 40 and never reaches 0,
# because the donor ATOM is legitimately neutral or negative while the MOLECULE it sits in is a
# cation, and no subgraph match can see the difference. The engine says so itself, in
# `is_charged_reactant_forbidden`'s docstring (family.py:1726): "A group cannot express this: RMG
# groups match subgraphs, so a `c0` constrains the atom it is written on and never the molecule as
# a whole." The one engine lever that exists, `allowChargedReactants`, is all-or-nothing and would
# bar this family's own ion reactants.
#
# So these two entries are kept for the bonded case they do catch, and the unbonded case is an
# OPEN DEFECT of this family, recorded in report.md section 15 with the engine change that would
# close it. Do not read "0 like-charge" in any earlier log as meaning none exist: those logs were
# measured on a corpus holding four cations in 78 thermo libraries, which was blind to the
# reactant class this family is made of.
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
#
# Both roots name their elements explicitly, and that is load-bearing rather than tidy. They were
# written as `R` -- broader than their own subtrees, which between them name only H, O, metal and
# N -- and `R` is what made this family unusable outside its own training set. A group constrains
# ATOMS, not molecules, so `R ... c[+1,...]` does not mean "a cation": it means "any molecule
# containing a formally positive atom", which is every nitro compound, every N-oxide, every
# nitrile oxide in the database. Measured over the 22,344 species the installed thermo libraries
# name (logs/rootsafety-before.stdout.log):
#
#     root B as `R`  : 17,009 species (76%) made generate_reactions RAISE
#     root A as `R`  :    630 of its 645 matchers raised, and 633 of those matchers were not
#                        cations at all
#     worst of all   : N2+, a PRODUCT of training entries 15 and 23, raised when fed back in --
#                      so the family aborts a job on the iteration after its own reaction fires
#
# The raise is an AtomTypeError from `update_atomtypes`: RMG has no atom type for most ionised
# heavy atoms (Br+, S+, N+ with four bonds), and `generate_reactions` propagates it out to the
# caller, so it ABORTS the run rather than omitting a reaction. That is why these roots are
# narrowed rather than widened, and why the narrowing is by element.
#
# With the element lists below the same sweep measures 0 crashes over all 22,344 species, 0 on the
# family's own products, and the family still reproduces 15 of 15 training entries with 45
# reactions and none wrong (logs/narrow2.stdout.log, logs/rootsafety-after.stdout.log). The
# alternative scored identically -- writing each root as `OR{}` over its children -- and was not
# taken, because a LogicOr root has no sample molecule of its own and the twelve database checks
# descend from these roots.
#
# Both roots stay strictly BROADER than their children, so the family still generalises: root B
# admits an ether oxygen that no child names. What it no longer admits is an element whose cation
# RMG cannot type.

# Root A is a LogicOr over its own children, NOT a flat group, and that is what lets N+ in.
#
# An earlier round of this ticket wrote here that N+ was impossible without a new atom type,
# reasoning that a group's `u` and `p` lists are a cross product so any root admitting `N u2 p1`
# also admits `O u1 p1` (H2O+) and `O u0 p1` (NO+), which crash. The premise is right and the
# conclusion does not follow: a flat group is not the only thing a root can be.
# `_match_reactant_to_template` (family.py:1817-1829) has an explicit LogicNode branch, so an
# `OR{}` over per-element children separates `N u2 p1` from `O u1 p1` exactly, with no new atom
# type. Measured over all 27 entries and the 22,344-species corpus (probe_nitrogen.py,
# logs/nitrogen.stdout.log):
#
#     flat  [H,O,N,metal] ux p[0,1,2]   16 of 27 reproduced, but 638 root-A crashes and 1 feedback
#                                       crash -- the cross-product argument, confirmed
#     OR{H_cation, O_cation, Metal_cation, N_atom_ion}
#                                       16 of 27, 0 crashes of any kind, 0 wrong, 0 like-charge
#
# So the flat root really cannot do it and the OR root can, at no measured cost. Training entry 18
# (N+ + N2) came back out of reactions-unrepresentable.py on the strength of that measurement.
#
# The cost of an OR root, which is real: it has no sample molecule of its own, so `probe_nodes.py`
# reports it as SKIP rather than PASS and the twelve checks descend from its children instead.
# That is why root B below is still a flat group -- it does not need the separation.
entry(
    index = 0,
    label = "A",
    group = "OR{H_cation, O_cation, Metal_cation, N_atom_ion}",
    kinetics = None,
)

entry(
    index = 1,
    label = "B",
    group =
"""
1 *2 [H,O,N] u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]
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

entry(
    index = 15,
    label = "N_atom_ion",
    group =
"""
1 *1 N u2 p1 c+1
""",
    kinetics = None,
    shortDesc = u"""Atomic N+, written out so that root A can admit it without admitting H2O+.""",
    longDesc = u"""
N+ is `N u2 p1 c+1`: nitrogen has five valence electrons, c+1 leaves four, and u2 p1 is exactly
four. The engine types it as N3sc, and GAIN_RADICAL takes it to `N u3 p1 c0`, which is
ground-state atomic nitrogen -- the declared product of training entry 18.

This node exists as a SEPARATE child rather than as a widening of the p list on root A. Widening
p to [0,1,2] admits `O u1 p1` (H2O+) and `O u0 p1` (NO+) at the same time, because a group's u
and p lists are a cross product; those two have no atom type after GAIN_RADICAL and raise. The
measurement is in logs/nitrogen.stdout.log: the flat widening costs 638 root-A crashes, this node
costs none.
""",
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
# N+ WAS RECORDED HERE AS IMPOSSIBLE, AND THAT WAS WRONG. This comment used to say that any root
# admitting `N u2 p1` also admits `O u1 p1` (H2O+) and `O u0 p1` (NO+), and concluded that only a
# new charge-specific atom type could separate them. The premise holds -- measured, a flat
# `[H,O,N,metal] ux p[0,1,2]` costs 638 root-A crashes -- but the conclusion does not, because a
# root need not be a flat group. Root A is now `OR{H_cation, O_cation, Metal_cation, N_atom_ion}`
# and `N_atom_ion` is `N u2 p1 c+1` exactly, which admits N+ and nothing else. 16 of 27 entries
# reproduce, with zero crashes of any kind (probe_nitrogen.py, logs/nitrogen.stdout.log).
# Training entry 18 (N+ + N2) is back in training/reactions.py.
#
# H2O+, NO+ and Ar+ remain out, each for its own measured reason, and none of them is "no atom
# type for the ion": all three type fine. The recipe simply does not fit them -- GAIN_RADICAL
# makes H2O+ into `O u2 p1` and NO+ into `O u1 p1`, neither of which types, and makes Ar+ into
# `Ar u2 p3` rather than ground-state `Ar u0 p4`, which is a WRONG product rather than a crash.
# Each would need a different recipe, not a wider root. See report.md section 14 for argon.

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
    L2: N_atom_ion

L1: B
    L2: Anion
        L3: H_anion
        L3: O_anion
    L2: N_neutral
        L3: N2_neutral
"""
)
