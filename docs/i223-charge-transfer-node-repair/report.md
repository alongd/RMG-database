# I-223 — Charge-transfer node repair, and the duplicate NO⁺/O₂ rate

Branch `i223-charge-transfer-node-repair`, worktree
`/home/alon/Code/RMG-database-i223-charge-transfer-node-repair`.
Measured from `/home/alon/Code/RMG-Py-i223-ct-node-repair` (built once with
`python utilities.py check-pydas && make build`; 52 `.so` under `rmgpy/`). Nothing was committed
to the code worktree.

**Resolved `database.directory` = `/home/alon/Code/RMG-database-i223-charge-transfer-node-repair/input`**,
printed at the top of every log in `logs/`. Every probe also prints `family loaded from`, because
the family was **never installed under `input/`** — it is loaded straight from
`docs/i154-carry-chemistry/held-back/Plasma_Charge_Transfer/` via `KineticsDatabase.load_families`,
and the "before" runs load a pristine checkout of the family at the branch base `d07add74a` in
`$TMPDIR/i223-before/`, so before and after are measured by identical code against different files.

Every check was run **one at a time** (`probe_checks.py`). This is not optional here:
`kinetics_check_groups_nonidentical` and three of its neighbours do not return `False`, they raise
`ValueError`, which escapes the `with check:` block and aborts the whole family — so a suite run
reports at most one failing node per family and silently never runs the later checks.

> **Status: all twelve family checks pass.** The first round of this ticket left
> `kinetics_check_sample_can_react` red; it was green before the branch, so the branch had traded
> one red check for another. §3 is the account of how that was found and fixed.
>
> **Round 49 changed nothing the branch does.** Every edit in it was to what the branch *says*: a
> tree change described as narrower than it was (§4), a hand-tallied literature count that was wrong
> (§6), two ratios quoted from outside the range where they mean anything (§6), and an overclaim
> about why one merge is harmless (§3). All seven corrections are listed in §9. The code, the
> twelve checks and every rate are unchanged from the previous head; `logs/averaging.stdout.log` is
> the one genuinely new measurement, and it confirms the reparenting it documents is numerically
> inert to 1.000000×.

> **READ §11 AND §12 BEFORE ANYTHING ELSE.** §11 records the finding that inverted this ticket:
> the family's charge-only recipe was a **no-op**, so it generated **zero reactions** while all
> twelve checks stayed green. §12 records the repair, which is a **narrowing**, not a fix — the
> recipe now moves the electron structurally (`GAIN_RADICAL`/`LOSE_PAIR`, no charge action at all),
> the two root templates are narrowed to what that recipe can process without crashing, and the
> family **generates 45 reactions and reproduces all 15 of its remaining training entries
> correctly, none wrongly, with zero crashes**.
>
> **Twelve of the 27 training entries left the family**, and they are preserved with their rates in
> `training/reactions-unrepresentable.py`. §12 says which, why, and what survives of the thirteen
> commits that came before. Sections 1–10 describe the family as it was; where §12 overturns them
> it says so.
>
> *Two corrections to that sentence, both from round 61.* **Eleven** remain, not twelve — entry 18
> came back in §17.1. And "not expressible on a two-label template" was wrong for most of them:
> worked through individually, only **four** of the twelve exceed the two-label template (they need
> a bond-order change, which takes two labels on one molecule). **Seven** fit the template perfectly
> and need a different *recipe*, which is a far smaller obstacle and makes them a sibling family
> rather than a grammar limit. One needed neither, and is back. Also: the header of that file
> claimed every rate in it was primary-source audited; the two `[Ozawa2008]` entries are not, and
> it now says so.

> **§13 THEN OVERTURNED §12's ROOTS.** §12 proved the roots crash-free over the **13 species its
> own training entries name**, and flagged the wider pool as the largest untested surface. It was
> measured: over the **22,344 species the installed thermo libraries name, 17,009 (76%) aborted
> the family**, 630 of its 645 root-A matchers aborted it, **633 of those matchers were not
> cations at all**, and — worst — **N₂⁺, a product the family makes itself in training entries 15
> and 23, aborted it when fed back in as a reactant**. An abort is not a missing reaction; it kills
> the RMG job. The cause was that both roots said `R` while their subtrees name only four elements.
> Narrowing each root to the elements its own children name takes every one of those counts to
> **zero** with the family still generating 45 reactions and reproducing 15 of 15 entries. §13 has
> the numbers, the rejected alternative and the engine finding behind it.

> **§19 REORDERS WHAT IS LEFT.** Every "what remains" list on this ticket has carried *install it
> and run a real reactor* as the next measurement, with the install gate named as the blocker. The
> gate is not the blocker. Of the **25 species** in the 16 training entries, **16 have no thermo in
> any of the 78 installed libraries** — every anion, every molecular cation, and every metal but
> lithium — so **0 of the 16 entries can be simulated today**. The thermo is not missing from the
> world: **14 of those 16 species are written on branch `99`**, uncarried, so what remains is a
> thermo *carry* and a **14-of-16** ceiling on it. But that library **does not load** — 13 of its
> 139 entries, `NO⁺` among them, have no atom type today. And the one `H⁺` the installed database
> holds is a computational-hydrogen-electrode proton, off by ~1530 kJ/mol for gas-phase use, with
> nothing to request in its place.

---

## 1. The two failures, reproduced before any edit

`logs/before.stdout.log`, 24 PASS / 2 FAIL / 1 SKIP:

```
Noble_cation     A              [He]                          0 None             FAIL (no match to root A)
    sample adjlist:
    1 *1 He u0 p1 c0
H2_ion           A              [H][H-]                      -1 None             FAIL (no match to root A)
    sample adjlist:
    multiplicity 2
    1    H u1 p0 c-1 {2,S}
    2 *1 H u0 p0 c0  {1,S}
```

Exactly the two the brief named, with the charges it predicted. Note where the charge went in the
`H2_ion` sample: the labelled `*1` came out **neutral** and the −1 landed on the *unlabelled* atom.

`logs/checks-before.stdout.log`: all eleven other family checks pass; only
`kinetics_check_sample_descends_to_group` fails. **That baseline is the contract the repair has to
meet — no check green there may be red at the end.** It is also the only reason the first round's
regression was catchable at all.

### Why each one failed

Both are `Group.make_sample_molecule` charge-derivation failures, and neither is a typo.

**`Noble_cation`** was `[He,Ne,Ar] ux px c+1`. `pick_wildcards` takes `atomtype[0]`, so the sample
is built on helium; `He` has no charged subtype and its `AtomType` carries an empty `lone_pairs`
list, so `make_sample_atom` falls back to `default_lone_pairs['He'] = 1`, and `update_charge` then
recomputes 2 − 2·1 = 0. The `c+1` in the group is simply overwritten. Root `A` requires
`c[+1,+2,+3,+4]` and rejects it.

**`H2_ion`** was a single-bonded `H⁺`–`H·` pair. That species **does not exist in RMG at all**:

```
H2+ single-bonded    FAIL InvalidAdjacencyListError: Invalid valency for atom H (H0) with
                     1 unpaired electrons, 0 pairs of electrons, 0 charge, and bonds [1.0].
```
(`logs/h2-recipe.stdout.log`)

H2⁺ is held by a one-electron bond, which RMG's integer bond orders cannot express. The family's
**own training dictionary already knows this** — `H2p_r1` is two *unbonded* atoms, `[H+].[H]` — so
the authored node matched nothing at all: `is_subgraph_isomorphic(H2p_r1, H2_ion) = False`, and
H2p_r1 descended only as far as `H_ion` (`logs/candidates.stdout.log` §3–4). The node was dead
before this ticket, not merely un-sampleable.

---

## 2. `Noble_cation`: `[He,Ne,Ar] ux px c+1` → `[Ar+,Ar,He,Ne] ux px c+1`

Measured against every candidate (`logs/noble.stdout.log`, `logs/parent.stdout.log`):

| candidate | sample | matches He⁺ / Ne⁺ / Ar⁺ / Ar₂⁺ / ArH⁺ | proper parent of `Ar_ion` |
|---|---|---|---|
| `[He,Ne,Ar] ux px c+1` (was) | `[He]` **+0** | T T T T T | yes |
| `[Ar,Ne,He] u1 p3 c+1` | `[Ar+]` +1 | F T T F F | — |
| `OR{He_ion, Ne_ion, Ar_ion}` | (skipped) | one each | — |
| **`[Ar+,Ar,He,Ne] ux px c+1`** | **`[ArH+]` +1** | **T T T T T** | **yes** |

The chosen form **does not narrow the node**: its matched set is byte-for-byte the current one.
`Ar+` leads the list because `pick_wildcards` takes the first atomtype, and `Ar+` is the only one of
the three elements that carries `lone_pairs=[3]` and `charge=[1]` of its own, so the sample gets
built at +1. Generic `Ar` stays in the list because the child `Ar_ion` is written on generic `Ar`,
and `Ar+` is *more* specific — an `Ar+`-only parent stops being a proper parent of its own child.
That is not hypothetical: I hit it. My first attempt was `[Ar+,He,Ne]`, and
`kinetics_check_child_parent_relationships` — green in the baseline — went red with *"group
Noble_cation is not a proper parent of its child Ar_ion"*. Adding `Ar` back fixes it and leaves
`Ar_ion` untouched.

The two rejected candidates both narrow the node: `[Ar,Ne,He] u1 p3 c+1` asserts 3 lone pairs, which
is false for He⁺ (0 lone pairs, 1 radical) and drops He⁺, Ar₂⁺ and ArH⁺; the `OR{...}` form — the
idiom this copy already uses for `Anion` — drops Ar₂⁺ and ArH⁺, because a LogicOr can only name
concrete children and there is no atom type for a *bonded* noble-gas cation other than `Ar+`. A node
that passes by being narrowed into something it does not mean is worse than one that fails.

### How fragile the ordering is — the two things the first round left unsaid

The comment in `groups.py` originally said only "`pick_wildcards` takes the first atomtype". Both
halves of what makes that safe are now recorded there, because both were verified in the source and
neither is obvious from the file:

- **`pick_wildcards` has a second stage.** After the first pass it walks each atom again
  (`rmgpy/molecule/group.py:2921-2925`) and, if the chosen atomtype is still *generic*, replaces it
  with the first entry of that atomtype's `.specific` list in `allElements` order. `Ar+` is already
  specific and passes through untouched. A generic `Ar` in first position would not — what it became
  would be decided by `allElements`, not by this file. Leading with a charge-specific atomtype is
  what takes that decision away from RMG.
- **The ordering survives a round trip.** `to_adjacency_list` emits the atomtype list with a plain
  `','.join` and no sort (`rmgpy/molecule/adjlist.py:967`), so re-reading a written-out copy of this
  family preserves `Ar+` in first position. The repair is fragile only against a human re-sorting the
  list by hand, not against RMG's own serialization. That is worth knowing before anyone runs this
  family through a save/load cycle and assumes the worst.

---

## 3. `H2_ion`: deleted, after the first round's repair traded one red check for another

This is the part of the first round that was wrong, and it is worth stating plainly rather than
folding into a summary.

The first round rewrote the node in the unbonded form, `[H+].[H]`. That fixed the sampling — the node
reached root `A` at +1 and matched `H2p_r1` for the first time — and it turned
`kinetics_check_sample_can_react` red:

```
Error in family Plasma_Charge_Transfer when reacting [H+].[H] + [H][H].
apply_recipe returned None, indicating wrong number of products or a charged product.
```
(`logs/checks-h2kept.stderr.log`)

That check was **PASS in `logs/checks-before.stdout.log`**. So the branch closed
`sample_descends_to_group` and opened `sample_can_react`, and the family still had one failing check.
The first round argued the new red was more honest than the old green — the pre-edit pass *is*
vacuous, for the reason below — and left it red on that argument. That was the wrong call: an
argument about which failure is more informative does not license shipping a family that cannot pass
its own suite, and it would have blocked the install gate this ticket exists to clear.

### Why the node cannot be made to work

Measured in `logs/h2-recipe.stdout.log`:

- training entry 2 is **H2⁺ + H⁻ → H₂ + H**. The electron arriving on H2⁺ becomes the *second*
  electron of the H–H bond;
- the recipe is charge-only (`LOSE_CHARGE *1`, `GAIN_CHARGE *2`) — it has no bond-forming action;
- so from an unbonded `[H+].[H]` it can only produce `[H].[H]`, two separate H atoms.
  `_generate_product_structures` calls `product_structure.split()`, gets 3 structures where
  `product_num` is 2, and returns `None`.

This is not a property of how the node is written. It is a property of the recipe: **a charge-only
family can never produce bonded H₂ from H2⁺**, so there is no adjacency list for this node that both
matches `H2p_r1` and reacts. The pre-edit pass was vacuous in the same direction — the old sample
`[H][H-]` is a molecule RMG refuses to build as a species, and `apply_recipe` on it returned
`['[H][H-]', '[H][H]']`, i.e. the charge never moved. A third option, giving H2⁺ a `vdW` bond in both
group and dictionary, turns the check green and was rejected as green-and-wrong: measured, it returns
`['[H+].[H]', '[H][H]']` — an "H₂" that is two unbonded H atoms and a charge that never transferred.

### The fix, and what it costs

Deleting the node turns **all twelve family checks green** (`logs/checks-h2del.stdout.log`, then
`logs/checks-after.stdout.log` at HEAD). Index 102 is left unused rather than renumbering, and the
reasoning above sits in `groups.py` at the node's former position, so the next reader does not
re-derive it and re-add the node.

One caveat on that gap, because it is presented as a durable marker and is not. Both save paths —
`KineticsFamily.save_groups` (`family.py:965`) and `Database.save(reindex=True)` (`base.py:371`) —
go through `Group.get_entries_to_save`, which **renumbers every entry `0..N-1` in tree order**
(`base.py:295-296`). One save through RMG and this file's authored numbering, gaps and all, is gone.
The gap means something to a human and nothing to RMG; it is recorded in the comment so the meaning
survives even when the number does not, and so nobody reads a gap in a machine-written copy of this
family as evidence that something was deleted.

It is not free, and the first round's stated reason for keeping the node — that dropping it would
create a second equal-rank duplicate — was **half right**. Training entry 2 does fall back to
`H_ion;H_anion`, where entry 1 already sits, so the family goes from four colliding template labels
to five. Two measurements say to accept that anyway:

1. **It is not a regression, it is the status quo ante.** `logs/rules-before.stdout.log` shows
   `H_ion;H_anion` holding entries 1 and 2 at the branch base. The first round's node was *preventing*
   a collision that had always been there; deleting it restores the base, it does not introduce
   anything.
2. **The collision is inert**, for a narrower reason than "nothing else lands there". `H_ion` is a
   one-atom group, `H u0 p0 c+1`, with no bond constraint, so the template catches any reaction whose
   `*1` atom is a bare proton. Within *this* training set that is only H⁺ + H⁻, which entry 1
   describes exactly — but a real run carrying a larger H-bearing cation could reach it too, and I
   have not checked whether entry 1's rate is right for such a species. What makes the shadowing
   harmless is not exclusivity; it is that **the two numbers are within 1.11× of each other**
   (`logs/collisions.stdout.log`), so which one wins cannot change an answer.

### Training entry 2 is kept, and annotated

Entry 2 is the only sourced rate in this repo for H2⁺ + H⁻, and it is a reaction that belongs in a
library, not in a charge-only family. It is kept with a `longDesc` saying exactly that.

This is deliberately **not** the treatment entry 17 got, and the difference is the whole point: entry
17 was a *duplicate* — a rival fit for a reaction this family does cover — so deleting it lost nothing
that could not be recovered from the surviving entry. Entry 2 is a *unique* rate for a reaction the
family cannot cover, so deleting it would destroy information with no fallback. The two look like the
same action and are not.

---

## 4. Two more tree changes: `O2_neutral` and `N2_neutral`

These are separate decisions with separate justifications, and the first round ran them together.
Splitting them apart matters because only one of them is coupled to the entry-17 deletion.

### `O2_neutral` (index 213, child of `O_neutral`) — coupled to the deletion

```
1 *2 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
```

This node exists **because deleting entry 17 would otherwise have been inert**. `O_neutral` is
`O ux px c0`, so atomic O and molecular O₂ both landed on it: training 14 (NO⁺ + O) and training 21
(NO⁺ + O₂) both resolved to `NO_ion;O_neutral`, and the tie-break keeps the lower index, so entry 14
shadowed entry 21 regardless of which NO⁺/O₂ fit survived. Choosing Ozawa over Gupta at index 21
changes nothing at the rule level while that is true. `O2_neutral` is the minimum change that makes
the entry-17 decision take effect: training 21 now resolves to `NO_ion;O2_neutral` and the Ozawa rate
is actually reachable.

The deletion is the chemistry call (§5); this node is the plumbing that makes it bite. Neither is a
reason for the other — the deletion would still be right if the tree had already been fine, and this
node would still be needed if a different fit had won.

`O2_neutral` reparents **exactly one** training reaction, index 21, and leaves nothing empty behind
it: `NO_ion;O_neutral` still holds training 14, and `Ar_ion;O_neutral` still holds training 20,
because atomic O continues to descend to `O_neutral` (`logs/averaging.stdout.log`). That is not true
of the second node, below.

### `N2_neutral` (index 214, child of `N_neutral`) — independent, and required by the criterion in §6

```
1 *2 N u0 p1 c0 {2,T}
2    N u0 p1 c0 {1,T}
```

Not coupled to anything above. `N_neutral` is `N ux px c0`, so atomic N and N₂ both landed on it, and
training 22 (O₂⁺ + N) shadowed training 23 (O₂⁺ + N₂). Unlike the O⁻/OH⁻ merges, these two rates are
genuinely different — both `[Ozawa2008]` Table III, but pair-specific, and **at least 107× apart
everywhere both fits are used** (`logs/collisions.stdout.log`; §6 explains why that window and not
the full declared range). The merge was discarding a real, sourced number. §6 states the criterion
that says so; this is the ticket applying it rather than stating it and declining to act on it.

#### It moves four training reactions, not one

A node applies to everything that descends to it, so `N2_neutral` picks up **every** reaction whose
`*2` partner is N₂ — not just the one it was added for. Measured before and after
(`logs/rules-before.stdout.log`, `logs/rules.stdout.log`):

| training | reaction | template at base | template now |
|---|---|---|---|
| 15 | Op_r1 + N2_r2 | `O_atom_ion;N_neutral` | `O_atom_ion;N2_neutral` |
| 18 | Np_r1 + N2_r2 | `N_atom_ion;N_neutral` | `N_atom_ion;N2_neutral` |
| 19 | Arp_r1 + N2_r2 | `Ar_ion;N_neutral` | `Ar_ion;N2_neutral` |
| 23 | O2p_r1 + N2_r2 | `O2_ion;N_neutral` | `O2_ion;N2_neutral` |

Only the last of those was this ticket's target. The other three had no collision at all; they moved
because that is what adding a tree node does. The earlier draft of this report described the change
as if it were surgical, which the logs it cites already contradicted.

**The knock-on, and it is the part worth measuring rather than reasoning about.** Those three
templates held exact rules from training 15, 18 and 19, and now hold nothing exact.
`fill_rules_by_averaging_up` — which a real rate-rules job always runs (`rmgpy/rmg/main.py:610`) and
which `probe_rules.py` deliberately does not — fills each empty parent by averaging its children, and
`N2_neutral` is `N_neutral`'s only child carrying a rule. So each is an average over exactly one
entry. Measured in `logs/averaging.stdout.log`:

| template | at base | now | k(1000 K) | k(5000 K) | k(10000 K) |
|---|---|---|---|---|---|
| `O_atom_ion;N_neutral` | exact, training 15 | averaged over 1 child | 1.000000× | 1.000000× | 1.000000× |
| `N_atom_ion;N_neutral` | exact, training 18 | averaged over 1 child | 1.000000× | 1.000000× | 1.000000× |
| `Ar_ion;N_neutral` | exact, training 19 | averaged over 1 child | 1.000000× | 1.000000× | 1.000000× |

**No rate changes value. What changes is provenance** — the kinetics comment goes from *"rate rule
generated from training reaction 15"* to *"Average of [From training reaction 15 used for
`O_atom_ion;N2_neutral`]"*. Harmless, and not nothing: a reader auditing where a number came from now
has one more hop to make, and the averaging stage — 24 exact rule labels become 89
(`logs/averaging.stdout.log`) — is a behaviour no check reports and no collision count shows.

---

## 5. The duplicate rate

### The brief's premise was wrong, and the primary source says why

`training/reactions.py` carried `NOp_r1 + O2_r2 <=> O2p + NO` twice, both at `rank = 6`:

| index | source | A (cm³/mol·s) | n | Ea | **T0** |
|---|---|---|---|---|---|
| 17 | `[Gupta1990]` Table II R19 | 1.8e15 | 0.17 | 65600 cal/mol | **300 K** |
| 21 | `[Ozawa2008]` Table III | 2.4e13 | 0.41 | 271.1 kJ/mol | **1 K** |

The brief reads the pre-exponentials as differing by ~75×. **They do not share a `T0`**, so that
comparison is not meaningful. Through rmgpy's own `Arrhenius` objects (`logs/kt.stdout.log`), the
ratio runs 1.87 (300 K) to 3.76 (1690 K); index 17 only exceeds 1e6 cm³/mol·s above **1530 K**, and
over that live window the ratio is **3.00–3.76**. A factor of ~3, not 75. Plot in `kT-comparison.png`.

Chasing the provenance settled it. NASA RP-1232 (Gupta, Yos, Thompson & Lee, 1990), Table II, p.45:
**R19 is `O₂ + NO⁺ ⇌ NO + O₂⁺`, `1.8e15 T^0.17 exp(−3.3e4/T)` cm³/mole·sec** — a bare `T`, no
`(T/300)` normalisation. Ea = 65600 cal/mol is exactly θ_d = 3.3e4 K (Ea/R = 33011 K), confirming the
row. **Entry 17 copied Cf verbatim and left `T0 = 300 K`, which makes every k it returns 300^0.17 =
2.64× too low** (`logs/t0.stdout.log`). The 300 came from the twelve `[Tanarro2015]` entries
immediately above it in the file, whose Table 1 *is* written `k = A(T/300)^n`.

### Decision: entry 17 deleted, `[Ozawa2008]` (index 21) kept

Three independent reasons, in order of weight:

1. **Physical.** Dividing `A·Tⁿ` by the Langevin capture rate for NO⁺ + O₂
   (4.51e14 cm³/mol·s, α(O₂) = 1.58 Å³, μ = 15.48 amu) asks how many times the ion–molecule collision
   limit each fit would demand if every super-threshold collision reacted. Gupta's fit demands
   **10–19×** the capture limit over 300–10000 K; Ozawa's stays at **0.55–2.3×**, the ordinary range
   for a polarisable target. For a capture-limited charge transfer, 19× is unphysical.
2. **Thermochemical.** Ozawa's Ea of 271.1 kJ/mol matches the endothermicity
   IE(O₂) − IE(NO) = 12.0697 − 9.2642 eV = 2.8055 eV = **270.7 kJ/mol** almost exactly. Gupta's
   θ_d·R = 274.4 kJ/mol is 3.7 kJ/mol high.
3. **Internal consistency.** Entries 14, 15, 16, 21, 22 and 23 — the whole air-plasma
   charge-exchange block — are `[Ozawa2008]` Table III. Keeping index 21 makes the set one model.

Index 17 is deleted and the index left unused rather than renumbering. The Gupta value, its correct
form, and the reasoning are recorded in the `longDesc` at the top of `training/reactions.py` and in
index 21's own `longDesc`, so nothing is lost from the record.

### How the shadowing actually happens — both paths, not one

The first round named only `KineticsRules.get_rule`. That is the rate-rule path, and it is not the
one a real run hits first for a reaction that is *in* the training depository. Both were verified in
source:

- **Depository first.** `KineticsFamily.get_kinetics` (`rmgpy/data/kinetics/family.py:2667+`) walks
  `self.depositories` **before** it ever calls `get_kinetics_for_template`. With the default
  `kineticsDepositories = 'default'` → `['training']` (`rmgpy/rmg/input.py:154-155`), the training
  depository is in that list, so for the exact reaction NO⁺ + O₂ the depository answers first.
  `_select_best_kinetics` (`family.py:2655-2664`) then sorts on `(rank, index)` and takes `[0]` —
  entry 17 over entry 21, on index alone, at equal rank 6.
- **Rate rules second.** `KineticsRules.get_rule` (`rmgpy/data/kinetics/rules.py:148-154`) sorts on
  `(1000 if not rank else rank, index)` and takes `[0]`, for any *other* reaction that lands on the
  same template.

The two paths agree here — index 17 wins both — which is why the first round's conclusion held
despite naming only one of them. They will not always agree: `_select_best_kinetics` sorts on the
**training entry** index while `get_rule` sorts on the **rule** index, and those diverge as soon as a
training entry is deleted or reordered. The mechanism worth remembering is that **`rank` is the field
that exists to express preference, and at equal rank it discriminates nothing, so an accident of
numbering decides** — in two places, by two different numbers.

### Entry 13 carried the same `T0` bug — fixed

RP-1232 Table II **R11** is `O + O₂⁺ ⇌ O₂ + O⁺`, `2.92e18 T^−1.11 exp(−2.8e4/T)`. Entry 13
(`O2p_r1 + O_r2 <=> O2 + Op`) copied Cf verbatim with `T0 = 300 K` and `n = −1.11`. Because n is
negative and large, that made it **561× too high at every temperature** (`logs/t0.stdout.log`).
`T0` corrected to 1 K; `A = 2.92e18` is Gupta's Cf, untouched. Outside the brief, on your explicit
call.

### No reaction is left at equal rank

`logs/rules.stdout.log` runs `add_rules_from_training` the way a real run does and reports every rule
label holding more than one entry. **No reaction label appears twice**, in training or in the rules.

---

## 6. When is a merged template node a defect? A criterion, and all five collisions measured

The first round found five template labels each catching two training reactions, split one of them,
and annotated the rest as "a tree-granularity question, not a duplicate-entry defect". Those two
things cannot both stand without a rule saying which collisions matter. Here is the rule, and the
measurement for every pair (`probe_collisions.py`, `logs/collisions.stdout.log`).

**Split a merged template when both hold:**

1. the two reactants are distinguishable by a group RMG's existing atom types can express, **and** the
   family's recipe can process the resulting sample — a node the recipe turns into `None` is not a
   repair, it is §3;
2. the two rates differ by more than **4×** *throughout* the window where both fits are actually
   used — that is, even at the temperature in that window least favourable to splitting.

The 4× is not arbitrary. This ticket measured the disagreement between two independent literature fits
of the *same* reaction — Gupta R19 vs Ozawa Table III for NO⁺ + O₂ — at **1.9–3.8×** (§5). Below that,
two rates merged onto one node disagree by less than the source-to-source scatter for a single
reaction, so splitting buys a distinction the underlying data cannot support. Above it, the merge is
discarding real information.

**Which temperatures count, and why it is not the declared range.** Every entry here declares
`Tmin = 300 K`, but the two `[Ozawa2008]` pairs are hypersonic shock-layer fits with Ea of
238–424 kJ/mol. At 300 K both sides of each pair evaluate to ~1e-28 cm³/mol·s and their *ratio* runs
to 6e18 and 3.6e27 — an exponential artefact of extrapolating far below where anyone would use either
number. An earlier draft of this report quoted those figures as the strength of the case. They are
arithmetic that favours the conclusion and they are not evidence, so the verdicts are decided on
5000–10000 K, where both fits are live, and on the **weakest** disagreement in that window rather
than the strongest.

| template pair | in-window (decides) | declared-range (artefact) | expressible | verdict | why the verdict holds |
|---|---|---|---|---|---|
| 1 / 2 · H⁺+H⁻ vs H2⁺+H⁻ | 1.11× | 1.11× | **no** | leave merged | recipe cannot process an H2⁺ node (§3) |
| 9 / 12 · H₂O⁺+O⁻ vs H₂O⁺+OH⁻ | 1.00× | 1.00× | yes | leave merged | **coarse source — expires, see below** |
| 8 / 10 · O₂⁺+O⁻ vs O₂⁺+OH⁻ | 1.00× | 1.00× | yes | leave merged | **coarse source — expires, see below** |
| 22 / 23 · O₂⁺+N vs O₂⁺+N₂ | **107×** | 6.4e18× | yes | **split** | rates genuinely differ → `N2_neutral`, §4 |
| 14 / 21 · NO⁺+O vs NO⁺+O₂ | **218×** | 3.6e27× | yes | **split** | rates genuinely differ → `O2_neutral`, §4 |

The in-window figures are the minimum over 5000–10000 K, both reached at 10000 K. The Tanarro pairs
have `Ea = 0` and equal `n`, so their ratio is exactly `A₁/A₂` at every temperature and there is no
window to argue about.

Zero merged pairs are left that the criterion condemns. Both splits it demands are in the branch.

**How much does the 4× matter?** Not at all, within a wide margin, and that is checkable rather than
asserted. The largest in-window ratio among the merges is **1.11×**; the smallest among the splits is
**107×**. **Any threshold strictly between those gives the same five verdicts — a factor-of-96
window**, and 4× sits inside it with two orders of magnitude of room on either side. The probe
computes and prints that interval on every run (`logs/collisions.stdout.log`), so if a future entry
narrows it, the criterion stops looking robust in the same place it is stated. A threshold that only
worked at one value would be a fudge; this one is not load-bearing.

### The two "lossless" merges are lossless because the *source* is coarse — and that expires

Entries 8, 9, 10 and 12 return **bit-identical** rates, so splitting `O_anion` would change nothing
any rate depends on. Four independent measurements do not land on the same three digits, so I read the
primary document rather than concluding the tree was right.

`[Tanarro2015]` Table 1, open author manuscript at
[europepmc.org/articles/PMC4685741](https://europepmc.org/articles/PMC4685741), section "Ion-ion
neutralization", rows IN1–IN23:

- **17 of the 23 rows carry the identical `2×10⁻⁷ (Tg/300)^−0.5`**, and **14 of those cite one
  reference** — [56] Kossyi, Kostinsky, Matveyev & Silakov, *Plasma Sources Sci. Technol.* **1** (1992)
  207, a kinetic-scheme review, not a measurement of any particular ion pair. (The other three cite
  [71], [72] and [73], each quoting the same generic value.)
- **Six rows differ**: IN1 `1.8e-7` [21], IN4 `2.3e-7` [60], IN8 `2.3e-7` [60], IN12 exponent −1 [57],
  IN17 `1e-7` with no T dependence [56], IN23 `4e-7` [21]. Five of the six carry a pair-specific
  source — the table carries pair-specific values wherever the authors had them. IN17 is the
  exception that cites [56] and differs anyway, so *"cites Kossyi"* and *"carries the generic value"*
  are separate predicates and are counted separately.

> An earlier draft of this report said 18 and 16. Both were wrong: **IN8 is `2.3e-7`**, not the
> generic value, and I had miscounted it. The conclusion is unaffected — 14 of 23 rows still trace to
> one review, and the four entries this bears on (8, 9, 10, 12 → rows IN13, IN15, IN20, IN22) all sit
> in the generic 17 either way. The counts are now **recomputed from the transcribed block on every
> run** of `probe_tanarro.py` rather than tallied by hand in prose, and the probe cross-checks its
> 12-row audit table against its 23-row block and refuses to run if they disagree. A number in a
> comment is not checkable; this one is.
- The authors say why they did not refine the rest: *"Other mechanisms such as electron impact
  neutralization and ion-ion recombination are also considered, but their importance is orders of
  magnitude lower"*, and *"The relevance of the negative ion processes in the global chemistry of the
  discharge is low"*.

So the answer is the second kind: **one class estimate applied to a family of reactions, not four
determinations that agree.** Specifically, entries 9 and 12 both quote [56] directly; entries 8 and 10
reach the same number by two citations ([73] Gudmundsson and [56] Kossyi) that are themselves quoting
it.

That changes what the follow-up should say. Those merges cost nothing **today**, because the source
does not distinguish the pairs — not because `O_anion` is at the right granularity. **The first
pair-specific measurement for O⁻ or OH⁻ makes this merge start silently discarding data, exactly as
the N/N₂ merge did until §4.** The finding has an expiry date and is labelled as one in
`logs/collisions.stdout.log`, in the `groups.py` comment, and in §8 below. The `OH_anion`
sibling-vs-child question stays open on that basis.

### `[Tanarro2015]` audited in full: eleven rows exact, one slip corrected

With Table 1 open, all twelve Tanarro entries were audited row by row — reaction, A, exponent, T0, Ea,
units (`probe_tanarro.py`, `logs/tanarro.stdout.log`). Eleven match exactly. One correction:

| entry | row | as entered | Table 1 | factor | action |
|---|---|---|---|---|---|
| 1 | IN1 · H⁺ + H⁻ → 2H | `A = 1.88e-7` | `1.8e-7` | 1.044× | corrected in place |

Finding a wrong digit in the first row checked is evidence the block was never verified against its
source, which is why the audit went to all twelve rather than stopping at one.

**The rule the audit applied, and it is the load-bearing part.** A discrepancy under **10×** is a
transcription slip: correct the digit in place, recording the row so each correction is independently
checkable. A discrepancy of an order of magnitude or more — or *any* mismatch in exponent, T0, Ea or
units — is **stopped and reported, not fixed**, because an error that size is usually a units or
convention mismatch rather than a typo, and rescaling A to make k(T) look right leaves the real defect
in the file and much harder to find. Entry 13 of this family is the precedent: it read as a wrong
number and was a wrong `T0` convention worth 561×. No row in this audit hit the stop threshold.

**Consequence of the entry-1 correction on §6's own conclusions: none.** The entry-1 vs entry-2 ratio
moves from 1.06× to **1.11×**, still far below the 4× threshold, so the `H_ion;H_anion` verdict is
unchanged and the lossless finding is unaffected. Stated here so no reader has to re-derive it.

### `[Aiken2023]` verified, `[Ozawa2008]` unreachable — and what that costs

`probe_ozawa_aiken.py` / `logs/ozawa-aiken.stdout.log`. This closes the item §8 previously carried as
"nine entries unverified". It closes it unevenly, and the uneven part is the point.

**`[Aiken2023]` Table 3.16 — read, three of three verified.** The thesis is open
(`colorado.edu/lab/ngpdl/.../aiken.pdf`; direct `curl` is refused by this sandbox, `WebFetch` +
`pdftotext -layout` works). The table prints its own rate form, `k = A T^η exp(−θ/T_tr)` — **bare T,
so `T0 = 1 K` is now read rather than inferred.** Its `A` column is in **m³/s per particle**, so the
conversion into this database's `cm³/(mol·s)` is ×6.02214e29:

| entry | reaction (as printed) | `A` Table 3.16 | → cm³/(mol·s) | `A` entered | ratio |
|---|---|---|---|---|---|
| 18 | N⁺ + N₂(X) → N₂⁺(X) + N(⁴S) | 1.16e−23 m³/s | 6.9857e6 | 6.99e6 | 1.0006 |
| 19 | Ar⁺(1) + N₂(X) → N₂⁺(X) + Ar(1) | 2.57e−17 m³/s | 1.5477e13 | 1.55e13 | 1.0015 |
| 20 | Ar⁺(1) + O(³P) → O⁺ + Ar(1) | 6.39e−18 m³/s | 3.8481e12 | 3.85e12 | 1.0005 |

All three agree to three-significant-figure rounding, with `η` and `θ` exact. No slips, nothing to fix.

**`[Ozawa2008]` Table III — not reached, and this is a confirmed negative rather than a failed
search.** `pubs.aip.org` returns HTTP 403; OpenAlex reports `is_oa: false`, `oa_status: "closed"`,
`best_oa_location: null`, `any_repository_has_fulltext: false`, `locations_count: 1`; Semantic Scholar
independently reports `CLOSED` with an empty `openAccessPdf`. **There is no open copy to find.** The
six entries are therefore checked by surrogate, and the surrogates bound rather than verify:

| surrogate | what it tests | result |
|---|---|---|
| `Ea` vs IE(B) − IE(A) | value **and** units of `Ea`, independent of every compilation | all six within **1%** |
| `θ` vs RP-1232 Table II | corroboration against a second tabulation (4 of 6 overlap) | within **1.2%** (R16/R17/R18/R19) |
| `A` vs Langevin capture | order of magnitude; a mole-vs-particle slip is 6e23 | all nine **0.02–4.3×** capture |

**`n` and `T0` are not verified for these six.** Both compilations being Park-derived means RP-1232
corroborates rather than independently confirms, and the surrogates should not be read as more.

**What the gap can cost, which is the part that decides whether it blocks.** A wrong `T0` rescales `A`
by `300^n` — up to 10.4× for entry 21. But **both splits this branch made are Ozawa-against-Ozawa**
(14 vs 21; 22 vs 23), so a convention error hits both sides of each comparison and the ratio the §6
criterion tests moves only by `300^(n₁−n₂)`:

| split | as decided | under the other convention | vs the 4× criterion |
|---|---|---|---|
| `N2_neutral` (O₂⁺ + N vs O₂⁺ + N₂) | 106.8× | 48.1× | 12.0× margin — **survives** |
| `O2_neutral` (NO⁺ + O vs NO⁺ + O₂) | 217.7× | 22.2× | 5.6× margin — **survives** |

So the unread table is **a gap in the record, not a risk to a decision already in the branch**. The
handoff flagged this as the one remaining item that could invalidate the N/N₂ split; measured, it
cannot. Entry 23 is immune outright (`n = 0.0`, so `300^n = 1.000`).

---

## 7. Every authored node, and every check, after

`logs/after.stdout.log`: **PASS 27  FAIL 0  SKIP 1**. 26 surviving authored group entries + `O2_neutral`
+ `N2_neutral` = 28 authored (`H2_ion` deleted); the loaded family reports 30 because
`template(products=["A-","B+"])` names two entries `groups.py` never defines and RMG fabricates them —
auto-generated product templates, correctly excluded by the check's own `ignore` list. **The brief's
"27 group entries" is right for the file and wrong for the loaded object.**

| node | root | sample | charge | descends to | verdict |
|---|---|---|---|---|---|
| A | A | `[H+]` | +1 | H_ion | PASS |
| B | B | `[H][H]` | 0 | Neutral | PASS |
| H_cation | A | `[H+]` | +1 | H_ion | PASS |
| O_cation | A | `[OH+]` | +1 | OH_ion | PASS |
| N_cation | A | `[NH2+]` | +1 | N_cation | PASS |
| **Noble_cation** | A | `[ArH+]` | **+1** | Noble_cation | **PASS** |
| Metal_cation | A | `[Li+]` | +1 | Li_ion | PASS |
| H_ion | A | `[H+]` | +1 | H_ion | PASS |
| O_atom_ion | A | `[O+]` | +1 | O_atom_ion | PASS |
| OH_ion | A | `[OH+]` | +1 | OH_ion | PASS |
| H2O_ion | A | `[OH2+]` | +1 | H2O_ion | PASS |
| O2_ion | A | `[O][O+]` | +1 | O2_ion | PASS |
| N_atom_ion | A | `[N+]` | +1 | N_atom_ion | PASS |
| NO_ion | A | `N#[O+]` | +1 | NO_ion | PASS |
| Ar_ion | A | `[Ar+]` | +1 | Ar_ion | PASS |
| Li_ion / Na_ion / K_ion | A | `[Li+]` / `[Na+]` / `[K+]` | +1 | itself | PASS |
| Mg_ion / Ca_ion | A | `[Mg+]` / `[Ca+]` | +1 | itself | PASS |
| Anion | — | (LogicOr) | — | — | SKIP — not a `Group`, so `make_sample_molecule` never runs on it; its children are checked instead |
| Neutral | B | `[H][H]` | 0 | Neutral | PASS |
| H_anion | B | `[H-]` | −1 | H_anion | PASS |
| O_anion | B | `[OH-]` | −1 | O_anion | PASS |
| O_neutral | B | `O` | 0 | O_neutral | PASS |
| N_neutral | B | `N` | 0 | N_neutral | PASS |
| **O2_neutral** | B | `[O][O]` | 0 | O2_neutral | **PASS** |
| **N2_neutral** | B | `N#N` | 0 | N2_neutral | **PASS** |

### Full per-check status

| check | before (`checks-before`) | first round (`checks-h2kept`) | now (`checks-after`) |
|---|---|---|---|
| correct_number_of_nodes_in_rules | PASS | PASS | PASS |
| nodes_in_rules_found_in_groups | PASS | PASS | PASS |
| groups_found_in_tree | PASS | PASS | PASS |
| groups_nonidentical | PASS | PASS | PASS |
| child_parent_relationships | PASS | PASS | PASS |
| siblings_for_parents | PASS | PASS | PASS |
| cd_atom_type | PASS | PASS | PASS |
| reactant_and_product_template | PASS | PASS | PASS |
| num_reactant_and_product | PASS | PASS | PASS |
| family_electrons_reach_training_reactions | PASS | PASS | PASS |
| **sample_descends_to_group** | **RAISED** | PASS | **PASS** |
| **sample_can_react** | PASS (vacuously) | **RAISED** | **PASS** |

**No check that was green before this branch is red now**, and both originally-failing conditions are
closed. `logs/checks-h2del.stdout.log` is the isolated measurement that the deletion, and not
something else in the branch, is what turns the twelfth check green.

---

## 8. What this could not reach

**Open, and needing your decision.** One tree-design question, now with its cost quantified and its
expiry stated:

- **Should `OH_anion` be a sibling of `O_anion` or a child of it?** `O_anion` = `O ux p3 c-1` catches
  both O⁻ and OH⁻, merging training 8/10 and 9/12. Per §6 this costs **nothing today** and the reason
  is a property of `[Tanarro2015]`, not of the tree: the source gives both sides one class estimate.
  It stops being free the moment a pair-specific rate for O⁻ or OH⁻ enters the file. The choice
  decides what an unlisted anion falls back to and is not derivable from the training set.

**Source verification: three of four sources done, the fourth is unreachable.** `[Gupta1990]`
(RP-1232 Table II), `[Tanarro2015]` (Table 1, all twelve entries, §6) and now `[Aiken2023]`
(Table 3.16, all three entries) are verified against their primary documents. **`[Ozawa2008]`
Table III is not, and cannot be** — see §6 for the audit and the bound on what that costs. The
short version: the paper is closed with no open copy anywhere, so its six entries are checked by
surrogate only, and the two splits that rest on them survive the worst case of the unread
convention by 5.6× and 12×.

**Unprovable until the family is installed under `input/`:**

- `add_rules_from_training` was run here in isolation with `thermo_database=None`. Per the campaign's
  own record, a family carrying `TwoTemperaturePlasma` kinetics crashes a real RMG run at
  `main.py:590` inside `add_rules_from_training` while the DB suite stays green — this family's
  training entries are plain `Arrhenius`, so that specific trap does not apply, but I have not run
  RMG end to end and cannot say the family survives one.
- `get_reaction_template` matches on **reactant-side labelled atoms only and never inspects
  `reaction.products`**. Every green here — the descent table, the template assignments, the rule
  generation — is therefore evidence about the *reactant* side of each entry. It is not evidence that
  the recipe produces the stated products. The one place the product side is tested,
  `sample_can_react`, is exactly where the H2⁺ defect surfaced — and note that it surfaced only for a
  node whose *sample* the recipe rejected. Entry 2 remains in the training set as a reaction whose
  products this family cannot make, and **no check in the suite catches that**; it is caught here only
  because §3 went looking. **This item is now closed, and badly: the other 26 entries have since been
  audited and they are all in the same state, for a reason that is not per-entry. See §11.**
- Reactor admissibility is untested. I-157 established that loading ≠ admissible: reversible
  Te-dependent recombinations are refused at `initialize_model`. Nothing here was put through a
  reactor.
- `is_molecule_forbidden` was exercised only against this family's own (empty) forbidden groups, not
  against the global `input/forbiddenStructures.py`, because the family was never loaded through
  `RMGDatabase`.
- `probe_checks.py` injects a `SimpleNamespace` in place of a real `RMGDatabase` so that one family
  can be checked in isolation. That is deliberate — `RMGDatabase.__init__` does `global database;
  database = self` with no reset, and two in one process has been measured shifting a thermo value by
  0.36 kJ/mol — but it means the library-level and cross-family checks in `test_kinetics` were not
  run at all.

**OCR caveat.** RP-1232 is a scanned document. The exponent in R19 rendered as `10lG`, which I read
as 10¹⁵ on the strength of n = 0.17 and θ_d = 3.3e4 matching the database entry exactly, and of the
same OCR rendering 10¹⁸ as `10 1S` in R11. If that digit is wrong, the *relative* argument in §5
changes but the `T0` finding does not — the bare-`T` form of the table is unambiguous in the scan.
`[Tanarro2015]`, by contrast, was read from a text-layer PDF, not OCR.

---

## 9. Deviations from the brief, each on an explicit decision of yours

| deviation | why it is outside the brief | your call |
|---|---|---|
| `H2_ion` **deleted**, not repaired | the brief said make it sample and descend | rework directive's lean, confirmed by measurement: deletion is the only state where all twelve checks pass |
| `sample_can_react` no longer red | the first round shipped it red on my argument | reversed — a more informative failure is still a failure |
| entry 13's `T0` corrected | a different reaction from the duplicate | yours, first round |
| `O2_neutral` added | tree change, outside "repair these two nodes" | yours, first round — it is what makes the entry-17 deletion take effect |
| `N2_neutral` added | second tree change, outside the brief entirely | yours, this round — the criterion in §6 condemns the merge at 107× |
| training entry 2 annotated, not deleted | training-data edit outside the brief | yours, this round — unique rate, no fallback, unlike entry 17 |
| training entry 1 `A` corrected 1.88e-7 → 1.8e-7 | training-data edit outside the brief | yours, this round |
| all twelve `[Tanarro2015]` entries audited | source verification outside the brief | yours, round 47 |

### Corrections this round (49) made to the branch's own record

None of these changed what the branch does; all of them changed what it says. Listed separately from
the deviations above because they are my errors, not decisions.

| corrected | was | is |
|---|---|---|
| §4 · what `N2_neutral` moves | described as splitting training 22/23 | it also reparents 15, 18 and 19, and demotes three templates from exact to averaged — §4, measured in `logs/averaging.stdout.log` |
| §6 · Tanarro provenance count | 18 generic rows, 16 citing Kossyi | **17 and 14**; IN8 is `2.3e-7`. Now computed by the probe, not tallied in prose |
| §6 · the ratios quoted for the splits | 6.4e18× and 3.6e27× | **107× and 218×**; the large figures are 300 K extrapolation of shock-layer fits and are labelled as artefacts |
| §6 · threshold justification | 4× asserted from the scatter measurement | the same, plus the **interval (1.11×, 107×)** over which the verdicts are unchanged, computed per run |
| §3 · why the `H_ion;H_anion` merge is harmless | "can only ever be applied to H⁺ + H⁻" | `H_ion` is an unconstrained one-atom group; it is harmless because the two rates are within 1.11×, not because nothing else matches |
| `probe_rules.py` docstring | claimed it ran `fill_rules_by_averaging_up` | it does not, and says so; the averaging stage is measured in `probe_averaging.py` |
| `groups.py` · "index 102 left unused" | presented as durable | any save through RMG renumbers every entry `0..N-1` (`base.py:295-296`); the gap is for humans only |

---

## 10. Clean `git status`

```
$ git status --porcelain -- input/ docs/i202-charge-transfer-carry/ test/conftest.py
[no output]

$ git diff --stat d07add74a -- docs/i154-carry-chemistry/
 .../held-back/Plasma_Charge_Transfer/groups.py     | 110 ++++++++++++++++++---
 .../Plasma_Charge_Transfer/training/reactions.py   |  99 ++++++++++++++++---
 2 files changed, 181 insertions(+), 28 deletions(-)
```

Nothing under `input/` changed. The 24-entry copy under `docs/i202-charge-transfer-carry/` is
untouched. `test/conftest.py` untouched. The RMG-Py worktree is at `535c679cf` with no commits and no
tracked-file changes (build artifacts only). No atom type was added or changed. `autoGenerated` and
`own_reverse` were not set. **Nothing pushed, nothing merged, and the family is still not installed
under `input/`.**

---

## 11. STOP — the recipe is inert, and the family generates no reactions

This is the audit §8 listed as open work ("the other training entries have not been audited that
way"). It was expected to find a handful of entries like entry 2. It found that the question is not
per-entry.

**Evidence: `probe_producibility.py`, `logs/producibility.stdout.log`, exit status 1.**

### What happens

The recipe is `[['LOSE_CHARGE', '*1', 1], ['GAIN_CHARGE', '*2', 1]]`, and that is the whole of it.

1. `Atom.decrement_charge` / `increment_charge` set `atom.charge` **and touch nothing else**
   (`molecule.py:538-548`).
2. `apply_recipe` then calls `struct.update_charge()` on every product structure
   (`family.py:1547`).
3. `Atom.update_charge` **re-derives** the charge from the structure
   (`molecule.py:596-598`):

   ```
   charge = valence_electrons − bond_order − radical_electrons − 2 × lone_pairs
   ```

The recipe changed none of the three quantities on the right, so step 3 puts the charge back exactly
where step 1 found it. The products come out isomorphic to the reactants, and `_create_reaction`
discards a reaction whose products are the same species as its reactants (`family.py:1757-1759`).

### Measured three ways, independently

| measurement | result |
|---|---|
| `apply_recipe` on Li⁺+H⁻, O⁺+O, Ar⁺+N₂ | 3 of 3 return the **reactants verbatim**, charge unmoved |
| `generate_reactions` on the same three pairs | **0 reactions** each |
| all 27 training entries through `apply_recipe` | 26 `INERT` (reactants returned), 1 `NO OUTPUT` (entry 2, product count 3 ≠ 2). **`PRODUCIBLE`: 0** |

### This is the family's defect, not RMG's

`probe_producibility.py` parses every recipe under `input/kinetics/families/` on each run rather than
quoting a tally:

- **20** mainline families use `LOSE_CHARGE` or `GAIN_CHARGE`.
- **20 of 20** pair it with a structural action — a radical change, a lone-pair change, or a bond
  change — i.e. with something that moves the electron count the charge is derived from.
- **0** use charge actions alone.

`Plasma_Radiative_Recombination`, the closest analogue, spells out the convention:
`[['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]]`. The arriving electron has to be put
*somewhere* in the structure; declaring the charge is bookkeeping on top of that, not a substitute
for it.

### Why twelve green checks say nothing about this

`kinetics_check_sample_can_react` is the only check that runs the recipe. It requires that
`apply_recipe` not raise, not return `None`, and that resonance generation on the output not throw.
Its own comment is `# Just check none of this throws errors` (`databaseTest.py:1668`). It never
compares the products to the reactants, so **a no-op recipe passes it by construction**.

Of the other eleven, ten are tree-shape, label or unit checks that never open the training
depository at all. The eleventh, `kinetics_check_family_electrons_reach_training_reactions`, does —
and this family declares `electrons = 0`, so the check returns `True` on its first line
(`databaseTest.py:842-843`) without reading an entry. **No check in the suite ever compares a
training entry's declared products to what the recipe makes.**

Re-run after this finding: **ALL 12 STILL PASS** (`logs/checks-recheck.stdout.log`). That is the
finding, not a reassurance.

### What a repair would need — measured, not chosen

For each entry, `probe_producibility.py` computes the change between each reactant species and the
product species of the same formula, in the four quantities `update_charge` balances, and reads off
the action set that change implies. The answer is that **one recipe cannot serve this training set**:

| side | distinct action sets | breakdown |
|---|---|---|
| cation `*1` | **4** | `GAIN_RADICAL+LOSE_CHARGE` (18 entries) · `LOSE_RADICAL+GAIN_PAIR+LOSE_CHARGE` (5: H₂O⁺, Ar⁺) · `CHANGE_BOND(−1)+GAIN_RADICAL+GAIN_PAIR+LOSE_CHARGE` (3: NO⁺) · `CHANGE_BOND(+1)+LOSE_RADICAL+LOSE_CHARGE` (1: entry 2) |
| partner `*2` | **2** | `GAIN_RADICAL+LOSE_PAIR+GAIN_CHARGE` (21) · `LOSE_RADICAL+GAIN_CHARGE` (6) |

Two structural obstacles, beyond the count:

- **Ar⁺ → Ar needs the opposite radical action to O⁺ → O.** Ar⁺ is `Ar u1 p3 c+1` and neutral Ar is
  `Ar u0 p4 c0`: the electron pairs up. O⁺ is `O u1 p2 c+1` and neutral O is `O u2 p2 c0`: the
  electron stays unpaired. `GAIN_RADICAL` is right for one and wrong for the other, and no single
  action covers both.
- **Entries 2, 14, 16, 21 need a bond-order change** (NO⁺ `N#[O+]` → NO `[N]=O`, and entry 2's H₂).
  `CHANGE_BOND` takes **two** labelled atoms. The template has `*1` and `*2` and they are on
  different molecules, so the present template cannot express it at all — this is a template change,
  not just a recipe change.

### I stopped here rather than fixing it

Three reasons, in order:

1. **The stop rule.** A convention/structure mismatch gets reported, not patched — patching it
   buries the defect. This is that case, one level up from entry 13's `T0`.
2. **The contract's gate**: "If a node turns out to need a chemistry decision I cannot source, bring
   the decision to the owner rather than guessing it." Choosing between one recipe with more actions,
   several narrower families, and "these reactions are not a family" is that decision.
3. **It is outside the brief**, which was two group nodes and a duplicate rate.

Nothing else in this report is retracted. The nodes are repaired, the rates are audited against
their primaries, the splits hold. All of it describes a family that cannot presently react.

### What §11 could not reach

- **The reverse family.** `groups.py` sets `reverse = "Plasma_Charge_Transfer_Reverse"` with
  `own_reverse = False`, so the reverse is a separate object that does not exist in this repository.
  Whether it carries the same defect is unmeasured.
- **Whether this family has ever been run.** Generating zero reactions is consistent with never
  having been exercised in a real job, but this probe cannot establish that, and the campaign's
  other copies were not checked for it here.
- **Whether the same defect sits in the other plasma families.** The census above counts recipes, not
  behaviour, and it covers `input/` — the held-back copies under `docs/` were not swept.

---

## Files

| path | what |
|---|---|
| `probe_nodes.py` | per-node sample + descend, one node at a time |
| `probe_checks.py` | every family-level `test_kinetics` check, one at a time |
| `probe_candidates.py` | can RMG build He⁺/Ne⁺/H2⁺; does the old node match anything |
| `probe_noble.py` | the four `Noble_cation` candidates, sampling and matched set |
| `probe_parent.py` | parent/child validity of each `Noble_cation` candidate |
| `probe_h2_recipe.py` | why an H2⁺ node cannot react, in any adjacency list |
| `probe_kt.py` | k(T) over 300–10000 K for the two duplicate fits |
| `probe_t0.py` | the `T0` error in both `[Gupta1990]` entries, and the Langevin comparison |
| `probe_rules.py` | template each training reaction resolves to; equal-rank collisions |
| `probe_collisions.py` | **the split criterion, applied to all five collisions with rate ratios and source provenance** |
| `probe_tanarro.py` | all twelve `[Tanarro2015]` entries audited against Table 1, with the stop rule; provenance counts computed from the full 23-row block |
| `probe_averaging.py` | **what the new nodes reparent, and what `fill_rules_by_averaging_up` then does about it** |
| `probe_ozawa_aiken.py` | **`[Aiken2023]` Table 3.16 audited against the primary; `[Ozawa2008]` Table III recorded unreachable and bounded by three surrogates** |
| `probe_producibility.py` | **§11 — all 27 training entries run through the recipe; the inert-recipe finding, the mainline recipe census, and the per-entry action sets a repair would need** |
| `probe_grammar.py` | **§12 — the nine-action grammar measured, and all four possible recipes against all 27 entries** |
| `probe_narrow.py` | **§12 — twelve candidate root pairs, scored on crashes, reactions and wrongly-served entries** |
| `probe_generate.py` | **§12 — what the family on disk generates: the 0 → 45 measurement** |
| `check_family_generates.py` | **§12 — the check that would have caught the inert recipe; runs over every installed family** |
| `probe_rootsafety.py` | **§13 — the roots driven over all 22,344 species the installed thermo libraries name, plus the family's own products fed back in as reactants** |
| `probe_narrow2.py` | **§13 — nine candidate root pairs scored on that crash surface and on the training set at once** |
| `fixtures/` | **§13.6, §17 — five minimal one-entry families, self-contained, giving the check a failing case for each assertion and a passing case for all; `--selftest` runs them** |
| `probe_nitrogen.py` | **§14 — four candidate root-A forms scored over all 27 entries and the corpus; re-derives the N⁺ impossibility claim and refutes it** |
| `probe_likecharge.py` | **§15 — synthesises a cation set by protonation, because the corpus holds four cations in 78 libraries, and measures the like-charge reactions no guard blocks** |
| `probe_thermo_coverage.py` | **§19 — every species of the training set matched by isomorphism against all 78 thermo libraries; the 0-of-16 simulatable result, and PART 2 against the uncarried branch-99 source library** |
| `run.sh` | runner — pins cwd and `PYTHONPATH`, persists **both** streams per probe |
| `logs/*.{stdout,stderr}.log` | one pair per measurement |
| `kT-comparison.png` | k(T) and ratio for the duplicate |

Every probe honours `I223_FAMILY_ROOT`, so any of them can be pointed at a pre-edit checkout and the
before/after comparison is made by identical code. `probe_t0.py` additionally prints a precondition
message naming that variable when run against a HEAD where entry 17 no longer exists, instead of
dying on a `KeyError` — it is an argument about the pre-edit file and says so.

### Log index

| log | family read | shows |
|---|---|---|
| `before` / `checks-before` | base `d07add74a` | the two node failures; eleven checks green, `sample_descends_to_group` red |
| `checks-h2kept` | first round's HEAD | `sample_can_react` red — the regression |
| `checks-h2del` / `nodes-h2del` / `rules-h2del` | deletion variant, in isolation | all twelve green; the `H_ion;H_anion` collision returning |
| `after` / `checks-after` / `rules` / `collisions` / `tanarro` / `candidates` / `parent` | HEAD | the final state |
| `rules-before` | base | `H_ion;H_anion` already collided before this branch; the N-template assignments before `N2_neutral` |
| `averaging` / `averaging-before` | HEAD / base | the reparenting of training 15/18/19, and the exact-to-averaged demotion with its 1.000000× numeric check |
| `ozawa-aiken` | HEAD | `[Aiken2023]` three of three verified; `[Ozawa2008]` unreachable, surrogates, and the `300^(n₁−n₂)` bound showing neither split can be overturned |
| `producibility` | HEAD | **0 of 27 training entries producible; the recipe returns its reactants; `generate_reactions` → 0; 20 of 20 mainline charge recipes pair the action with a structural one** |
| `checks-recheck` | HEAD | all twelve still pass **after** the producibility finding — the suite cannot see it |
| `grammar` | HEAD | the action grammar measured; the 16/4/2/1/4 partition of the training set |
| `narrow` | HEAD | twelve candidate root pairs; only four are crash-free |
| `generate` | HEAD | **45 reactions, 0 crashes, 15 of 15 entries reproduced, 0 wrong** |
| `checks-narrowed` / `nodes-narrowed` | HEAD | all twelve pass and all 18 nodes descend after the narrowing |
| `check-generates` | HEAD | 103 installed families audited, none inert |
| `check-generates-control` | i202 staged copy | the same check on the UNREPAIRED copy: INERT, exit 1 |
| `rootsafety-before` | HEAD before §13 | **17,009 of 22,344 species abort the family; 630 of 645 root-A matchers abort it; 633 of those matchers are not cations; N₂⁺ — its own product — aborts it** |
| `narrow2` | HEAD before §13 | nine candidate root pairs; both roots must narrow; two designs score identically at 0 crashes |
| `rootsafety-after` | HEAD | **0 crashes on all 22,344, 0 on root A, 0 on feedback; 11 root-A matchers, all cations** |
| `nodes-rootsafety` / `generate-rootsafety` / `checks-rootsafety` / `check-generates-rootsafety` | HEAD | 18 nodes descend, 45 reactions and 15 of 15 reproduced, twelve checks green, 103 families still non-inert — the full verifier set re-run after the §13 narrowing |
| `check-generates-feedback` | HEAD | the product-side assertion over 103 installed families + this one: **0 own-product raises** |
| `check-generates-control-feedback` | throwaway pre-§13 copy | the same check **FAILS**, naming entries 15 and 23 and the product `N#[N+]` |
| `check-selftest` | `fixtures/` | all three fixtures produce their expected verdict — `ok`, `inert`, `feedback` — so both assertions are proven to fire *and* to stay quiet |
| `nitrogen` | HEAD before r61 | **N⁺ is admissible after all: `OR{…, N_atom_ion}` gives 16 of 27 with 0 crashes; the flat widening gives 16 with 638** |
| `likecharge` | HEAD before r61 | **470 like-charge reactions over a 150-cation set; no root-B narrowing reaches 0** |
| `generate-r61-reversible` | `reversible = True` | **6 crashes including training entry 7; 15 of 16** — why §16 keeps it False |
| `nodes-r61` / `checks-r61` / `generate-r61-final` / `rootsafety-r61` / `check-generates-r61` / `check-selftest-r61` | HEAD | 18 PASS 2 SKIP; twelve checks; 50 reactions and 16 of 16; 0 crashes over 22,344; 103 families ok under the strengthened assertions; five fixtures |
| `thermo-coverage` | HEAD + `99:…/plasma.py` | **9 of 25 species have library thermo; 0 of 16 training entries are simulatable; the only H⁺ is a CHE-convention proton; branch 99 holds 14 of the 16 missing but 13 of its 139 entries have no atom type** |
| `t0` | base | the `[Gupta1990]` `T0` argument |
| `t0-head` | HEAD | the precondition message, demonstrated |

---

## 12. OUTCOME 2 — the grammar can express charge transfer, but not for this whole family

§11 stopped at "the recipe is inert, and repairing it is a redesign". This section is that
redesign, measured. The question it had to answer first:

> Can a single recipe in RMG's action grammar express "one electron moves from `*2` to `*1`" for
> every structure the family's templates admit — and if not, what is the narrowest set of
> templates for which it can?

**The answer is outcome 2 of the three the brief named, explicitly: no single recipe serves all 27
training entries; one serves 16 of them; and after narrowing the templates so it cannot crash, 15.**

### 12.1 The two prior numbers, re-measured on `RMG-Py-plasma@311818121`

Both reproduced as my own measurements before anything was built on them
(`logs/grammar.stdout.log`, PART 0):

| claim | measured here |
|---|---|
| the shipped recipe is inert | `apply_recipe` returned the reactants unchanged for **3 of 3** demonstration pairs |
| the family generates nothing | `generate_reactions` returned **0** for all three |
| no mainline family has a bare charge recipe | **20** families use a charge action, **20 of 20** pair it with a structural one, **0** are charge-only |

The census is parsed from `input/kinetics/families/*/groups.py` on every run rather than quoted, so
it cannot drift from the repo.

### 12.2 The grammar, read from the engine and then measured

`valid_actions` (`family.py:809-812`) is exactly nine. What each does to the **derived** charge was
measured by applying it to a probe molecule and reading `update_charge` back — not asserted:

| action | labels needed | Δcharge on `*1` | electrons moved |
|---|---|---|---|
| `GAIN_RADICAL` / `LOSE_RADICAL` | 1 | −1 / +1 | **one** |
| `GAIN_PAIR` / `LOSE_PAIR` | 1 | −2 / +2 | two |
| `CHANGE_BOND(+1)` / `FORM_BOND` / `BREAK_BOND` | **2** | −1 / −1 / +1 | one, onto *each* of two atoms |
| `GAIN_CHARGE` / `LOSE_CHARGE` | 1 | **0** | **none** |

The last row is the whole of §11 in one line: the two charge actions are the only ones in the
grammar with no effect on the quantity the charge is derived from.

So exactly four two-label recipes can move one electron from `*2` to `*1`:

| | accept on `*1` | donate from `*2` |
|---|---|---|
| **A1** | `GAIN_RADICAL` — electron stays unpaired | |
| **A2** | `LOSE_RADICAL + GAIN_PAIR` — electron pairs up | |
| **B1** | | `LOSE_RADICAL` — an unpaired electron leaves |
| **B2** | | `GAIN_RADICAL + LOSE_PAIR` — a pair is broken |

### 12.3 All four, against all 27 entries

Every combination was run against every entry (`logs/grammar.stdout.log`, PART 2). The partition is
**exact — no entry is served by more than one**:

| recipe | entries served | which |
|---|---|---|
| **A1 \| B2** | **16** | 1, 3, 4, 6, 7, 8, 10, 11, 15, 18, 23, 24, 25, 26, 27, 28 |
| A2 \| B2 | 4 | 5, 9, 12, 19 (H₂O⁺, Ar⁺) |
| A1 \| B1 | 2 | 13, 22 (O(³P), N(⁴S) as donor) |
| A2 \| B1 | 1 | 20 |
| **none** | **4** | 2, 14, 16, 21 (H₂⁺ and all three NO⁺ entries) |

**This is not a matter of convention.** The wrong choice does not produce a different molecule — it
`raises`. `LOSE_RADICAL` on a closed-shell atom is an `ActionError` because radical counts cannot go
negative. H⁺ (`u0`) cannot use A2; N₂ (`u0` on `*2`) cannot use B1.

Two chemically real facts sit underneath, and neither is expressible as a uniform action:

- **Ar⁺ → Ar pairs the electron up; O⁺ → O does not.** Ar⁺ `u1 p3` → Ar `u0 p4`, but O⁺ `u1 p2` →
  O `u2 p2`. Same `u`, opposite action. Whether the arriving electron pairs depends on the
  acceptor's ground state.
- **NO⁺ → NO changes a bond order** (`N#[O+]` → `[N]=O`). `CHANGE_BOND` takes **two** labelled
  atoms; this template has one per reactant, on different molecules. No two-label recipe can do it.

I checked whether RMG's resonance machinery quietly identifies these states — it does not. Ar `u2p3`
vs `u0p4`, O `u0p3` vs `u2p2`, O⁺ `u3p1` vs `u1p2`: each generates only itself, and
`Species.is_isomorphic` is `False` after `generate_resonance_structures` in every case. A bonus from
that check: the A1 product of H₂O⁺ (`O u2 p1`, two single bonds) **has no atom type at all**, which
is why those entries raise rather than mismatch.

### 12.4 Narrowing the templates — a crash-safety requirement before a chemistry preference

The shipped roots are `*1 R ux px c[+1..+4]` and `*2 R ux px c[0..-4]`, and with a *working* recipe
they are dangerous, because **an RMG group constrains atoms, not molecules**:

- `*2 R ux px c[0,...]` matches any neutral atom — **including the hydrogen inside OH⁺**. The family
  then tries to take an electron from it, `LOSE_PAIR` finds none, and `ActionError` propagates out
  of `generate_reactions`.
- `GAIN_RADICAL` on H₂O⁺ or NO⁺ produces untypeable oxygen → `AtomTypeError`, likewise out.

**Those are crashes, not over-generation: they abort the whole RMG job.** Twelve candidate root
pairs were measured (`logs/narrow.stdout.log`); only four reach zero crashes. The chosen pair:

```
A: 1 *1 R ux p[0,2]         c[+1,+2,+3,+4]
B: 1 *2 R u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]
```

**N⁺ is the painful casualty.** `N u2 p1 c+1` works perfectly with this recipe and is excluded only
because a group's `u` and `p` lists are a **cross product, not a disjunction**: any root admitting
`N u2 p1` also admits `O u1 p1` (H₂O⁺) and `O u0 p1` (NO⁺), which crash. The vocabulary that would
separate them is a charge-specific atom type per element, and the engine defines exactly six —
`Li+ Na+ K+ Mg+ Ca+ Ar+`, none for N, O or H. **Adding one is an engine change and out of scope, so
this is reported rather than done.** It is the single cheapest thing that would widen this family.

### 12.5 Two traps found while doing it, both worth more than this ticket

**A family forbidden group without atom labels is inert.** Group templates cannot require a *molecule*
to be neutral, so root B matches the neutral N of NO⁺ and the neutral O of O₂⁺, and the family
generated cation + cation "charge transfer" — **19 of 82 reactions**, producing dications like
`[O+][O+]`. Forbidden groups are the right tool, and the obvious form of them does nothing:

| forbidden group | `is_molecule_forbidden` on the bare molecule | blocks generation? |
|---|---|---|
| unlabelled | `True` | **No** |
| same group, `*2` on one atom | `True` | **Yes** |

At generation time the product still carries `*1`/`*2`, and an unlabelled group fails to match it.
`apply_recipe`'s docstring hints at this ("product atom labels … to assist in identifying forbidden
structures") but nothing enforces it, so **an unlabelled entry looks like a guard and is not one**.
With the labelled forms: 0 like-charge reactions of 45.

**`reversible = True` on a non-own-reverse family generates a reverse you cannot author.**
`generate_reactions` runs the reverse whenever `not own_reverse and reversible`
(`family.py:1882-1891`), using `reverse_template` — which for this family **RMG fabricates** by
applying the recipe to the roots. Nothing in `groups.py` can narrow it. Measured: the reverse applies
`LOSE_RADICAL` to `*1`, and on O⁺ that gives `O u0 p2 c+2` — an O²⁺ with no atom type — so
`generate_reactions` raised on 2 of 91 pairs, **one of which was training entry 7 itself**. Setting
`reversible = False` is the only database-side lever and is what the family now carries. The cost is
stated at the declaration: RMG will not construct the reverse of these reactions, and the
`Plasma_Charge_Transfer_Reverse` family that is supposed to hold that chemistry **does not exist in
this repository**, so the reverse is currently unrepresented rather than handled elsewhere.

### 12.6 Before and after

Measured against the family **as it stands on disk**, not an in-memory mock
(`probe_generate.py`, `logs/generate.stdout.log`):

| | before | after |
|---|---:|---:|
| reactions generated over its own training species | **0** | **45** |
| crashes (`generate_reactions` raised) | 0 of 231 | **0 of 91** |
| training entries reproduced with declared products | **0 of 27** | **15 of 15** |
| training entries reproduced *wrongly* | 0 | **0** |
| like-charge (cation+cation) reactions | 0 | **0** |
| twelve family checks | all pass | **all pass** (`logs/checks-narrowed.stdout.log`) |

"0 crashes before" is not a virtue — an inert recipe cannot crash. 25 of the 45 reactions are
outside the training set; that is a family generalising and is not an error.

### 12.7 The check that would have caught this

`check_family_generates.py` — family-agnostic, with a real exit code. It hands each training entry's
own reactants to `generate_reactions` and fails a family that generates **nothing** for every entry.

Controls both ways, which is the point:

- **Negative control**: run against the unrepaired 24-entry copy at
  `docs/i202-charge-transfer-carry/staged-family/` (still charge-only, untouched by this ticket) →
  `0 generates, 24 nothing`, **INERT, exit 1**.
- **Positive**: all **103** installed families plus this one → all generate, `INERT: 0`, exit 0.
  No other family in the repository has this defect.

**Where it belongs, and why it is not there.** Beside the other twelve, in
`test/database/databaseTest.py`, as `kinetics_check_family_generates_its_training_reactions`. That
file is in the **RMG-Py repository**, which this ticket may not modify — so **the place where it
would run automatically does not yet exist for this repo**. This file is the runnable stand-in; it
has to be invoked rather than collected. Landing it upstream is a separate change to a separate repo.

One weakness I found in my own check and fixed: a family that fails to *load* was being reported as
"skipped", which would let the check pass on a family it never saw — the same shape of hole it
exists to close. It now fails on that.

### 12.8 What this means for the thirteen commits already on the branch

None of the rate work is retracted. What changes is how much of the family it applies to.

| # | commit | survives? |
|---|---|---|
| 1 | `f41e544f3` repair `Noble_cation` and `H2_ion` | **half**. The `H2_ion` finding survives. `Noble_cation` is now **deleted** — Ar⁺ is `p3`, outside the narrowed root. The repair was correct and its subject left the family. |
| 2 | `527dd5a73` correct both `[Gupta1990]` entries vs RP-1232 | **as record**. Entry 17 was already deleted; entry 13 has moved to `reactions-unrepresentable.py` carrying its corrected `T0`. The 561× finding stands and is why the stop rule exists. |
| 3 | `f4caa64fc` add `O2_neutral` so the NO⁺/O₂ rate is reachable | **undone**. `O2_neutral` is removed and entry 21 has left. The node existed to make one entry reachable; that entry is not representable. |
| 4 | `9ddfd0fb5` probes, logs, report | superseded in part by §11–§12; the probes still run. |
| 5 | `7942025ed` delete `H2_ion`, split `N2_neutral` | **mostly**. The `H2_ion` deletion stands. `N2_neutral` stands and is still load-bearing — entries 15 and 23 use it. |
| 6 | `0ca642c53` audit `[Tanarro2015]` vs Table 1 | **fully**. All twelve audits stand; 8 of those entries remain in the family, 4 moved out with their corrected rates. |
| 7 | `eaec8710a` rework after spar 47 | stands as record. |
| 8 | `006e72456` what `N2_neutral` actually moves | **partly stale**. Its reparenting analysis references `O_neutral`, which is now removed. The 1.000000× averaging measurement still holds for `N2_neutral`. |
| 9 | `30c7c221f` measure what the new nodes reparent | same: `N2_neutral` half stands, `O2_neutral` half is moot. |
| 10 | `88ff98e83` `[Aiken2023]` verified, `[Ozawa2008]` unreachable | **as record only.** All **3 of 3** Aiken entries (18, 19, 20) and **4 of 6** Ozawa entries (14, 16, 21, 22) have left the family. The verification was correct; it now describes chemistry in the unrepresentable file. |
| 11 | `bfa54579b` bound what the unreadable Ozawa table can cost | **moot.** It defended two splits — `N2_neutral` (22 vs 23) and `O2_neutral` (14 vs 21). Entry 22 has left, `O2_neutral` is removed, 14 and 21 have left. **Both splits it was protecting are gone**, so the bound protects nothing that remains. The reasoning — same-source cancellation, `300^(n₁−n₂)` — is still correct and still the right method; it has no live subject here. |
| 12 | `37e52073a` say that the recipe does nothing | **superseded** by the repair, kept as the record of the defect. |
| 13 | `847eb57b2` audit every training entry, and stop | **discharged.** The stop is resolved by §12. |

The short version: **the node repairs and the tree splits were the most affected, and the source
audits the least.** Rates were never the problem. Of the two tree splits this branch was proudest
of, one (`O2_neutral`) is removed outright and the other (`N2_neutral`) survives and is still used.

### 12.9 What §12 could not reach

- **Species outside the training set.** The pool is the 13 species the surviving entries name. A
  root pair that is crash-free over those is **not proven** crash-free over every molecule a real
  mechanism contains, and the crashes here were severe. This is the largest untested surface.
- **A real RMG run.** Nothing was put through `main.py`, a reactor, or `add_rules_from_training`
  with a real thermo database.
- **The four "no recipe" entries as their own families.** Groups 1 and 2 of
  `reactions-unrepresentable.py` each have a known, written-out recipe and would each make a
  coherent family. That is a new ticket; none was created.
- **A LogicOr top.** It might express the exact acceptable set where a flat group cannot, but tops
  are consumed as `Group`s by `_match_reactant_to_template`, so it is a separate experiment and was
  not attempted. **§13 measured this and it is wrong**: `_match_reactant_to_template`
  (family.py:1817-1829) has an explicit `LogicNode` branch that iterates `get_possible_structures`,
  and an `OR{}` top matches correctly. It was scored in §13.3 and rejected on other grounds.
- **The reverse family.** `Plasma_Charge_Transfer_Reverse` does not exist here, and `reversible` is
  now `False` partly because of that.

---

## 13. The roots were not crash-safe, and the family aborted on its own product

§12.9 named "species outside the training set" as the largest untested surface. It was measured
this round, and it inverted: **the family as committed could not be installed.** The measurement
is `probe_rootsafety.py` over the 22,344 distinct species named by all 78 installed thermo
libraries — 1,700× the 13-species pool §12 used.

### 13.1 What the sweep found

| measured over 22,344 species | committed roots | narrowed roots |
|---|---|---|
| species that abort the family as the `*2` partner | **17,009 (76%)** | **0** |
| root-A matchers | 645 | 11 |
| …of which are **not cations at all** | **633** | **0** |
| root-A matchers that abort the family as the `*1` reactant | **630** | **0** |
| the family's own training **products**, fed back in, that abort it | **1 (N₂⁺)** | **0** |
| training entries reproduced correctly / wrongly | 15 / 0 | 15 / 0 |
| reactions over the training pool | 45 | 45 |

Every failure is an `AtomTypeError` raised by `update_atomtypes` inside `apply_recipe`, and
`generate_reactions` propagates it to the caller. It **aborts the run**; it does not omit a
reaction. Logs: `logs/rootsafety-before.stdout.log`, `logs/rootsafety-after.stdout.log`.

### 13.2 The three findings, in order of severity

**(a) The family aborted on a species it makes itself.** Training entries 15 (`O⁺ + N₂`) and 23
(`O₂⁺ + N₂`) both produce **N₂⁺**. N₂⁺ is `N u1 p0 c+1 {2,T} | N u0 p1 c0 {1,T}` — its charged N
matched root A, and `GAIN_RADICAL *1` turned it into `N u2 p0 c0` holding a triple bond, which has
no atom type. So an RMG job would fire entry 15, put N₂⁺ into the core, and abort on the **next**
iteration.

`probe_generate.py` could not see this, because it drives training **reactants** only. A product
is a future reactant by construction, and that is now a separate stage (`PART 1c`) rather than an
assumption. This is the single most transferable thing in §13: **a family that is safe on its
reactants is not thereby safe, and the gap is exactly one RMG iteration wide.**

**(b) "A cation" is not a thing a group can say.** A group constrains **atoms**, not molecules, so
`R ux p[0,2] c[+1,+2,+3,+4]` does not mean "a cation" — it means "a molecule containing a formally
positive atom". **633 of the 645 root-A matchers were neutral molecules**: nitro compounds
(`[O-][N+](=O)CCC[N+](=O)[O-]`, BurcatNS), N-oxides, nitrile oxides, azides. Nitroalkanes are
ordinary combustion species. This is the same "atoms, not molecules" trap recorded in §12.5, biting
on the other root, and it is worth stating as a rule: **a charge in a group is a statement about
one atom, and every root written to mean a molecular charge is wrong by construction.**

**(c) The roots were broader than their own subtrees.** Root A said `R`; its three children name
`H`, `O` and `metal`. Root B said `R`; its children name `H`, `O` and `N`. Generation matches the
**root**, not the children, so that gap was the whole crash surface — everything with a bromine, a
sulfur, a phosphorus. Nothing in the twelve checks compares a root to the union of its children.

### 13.3 The repair, chosen by measurement

`probe_narrow2.py` scored nine candidate root pairs on the crash surface **and** on the training
set simultaneously, because a root that is crash-free by matching nothing is not a repair
(`logs/narrow2.stdout.log`). Narrowings only — every widening measured in this ticket traded one
crash for another or for silently wrong products.

| root A | root B | crash-pool | crash-A | crash-back | right | rxns |
|---|---|---|---|---|---|---|
| `R` (committed) | `R` (committed) | 17,009 | 630 | 1 | 15/15 | 45 |
| `R` | `[H,O,N]` | 0 | 630 | 1 | 15/15 | 45 |
| `[H,O,metal]` | `R` | 17,009 | 0 | 0 | 15/15 | 45 |
| **`[H,O,metal]`** | **`[H,O,N]`** | **0** | **0** | **0** | **15/15** | **45** |
| `OR{children}` | `OR{children}` | 0 | 0 | 0 | 15/15 | 45 |

Both roots had to change: narrowing either one alone leaves the other's crashes intact. The two
crash-free designs score **identically** on every column, so the choice was made on other grounds:

- **Element lists were taken.** A `Group` root has a sample molecule, and
  `kinetics_check_sample_descends_to_group` needs one. The tree's existing `Anion` LogicOr already
  shows up in `probe_nodes.py` as `SKIP (not a Group)` — acceptable for an interior node, not for a
  top that two checks descend from.
- **`OR{children}` was rejected**, not untried. It works — contrary to §12.9 — and would make the
  root exactly equal to the union of its children, which is arguably the more honest statement. It
  is the better design the day RMG's checks handle a LogicOr top.

Both narrowed roots stay strictly **broader** than their children, so the family still generalises:
root B admits an ether oxygen no child names. What it no longer admits is an element whose ion RMG
cannot type.

### 13.4 Why this is the database's defect and not RMG's — and where it is RMG's

The database's part is unambiguous: a root that claims `R` while its subtree covers four elements is
a database error, and it is fixed here.

The engine's part is the one that cannot be fixed here, and it is the same finding §12 already
carries: **RMG has no atom types for most ionised heavy atoms.** `Br u1 p2 c+1` with one bond, `S⁺`,
four-bonded `N⁺` — none is typeable, so no charge-transfer family in RMG can generalise past H, O,
N and the six charge-specific metal types (`Li+ Na+ K+ Mg+ Ca+ Ar+`). The narrowing above is not a
chemistry judgement that bromine does not accept charge; it is the database declining to ask the
engine a question the engine cannot answer. Per the standing gate, that stays a line in this report.

### 13.5 A count worth flagging, which is not a crash

With the narrowed roots, **12,283 of 22,344 species still react** with a single test cation (Li⁺),
producing 19,100 reactions in that one sweep. That is legitimate family generalisation, not a
defect — but the rate rules behind it were measured for atomic and diatomic ions, and the tree will
hand a nitroalkane the same number. It over-generates within its element set. Nothing was changed
for it; it is recorded because a reviewer sizing the family's cost in a real job needs the number.

### 13.6 The check that would have caught it

`check_family_generates.py` gained a second assertion: **for each training entry, drive the entry's
own PRODUCTS back in as reactants, and fail the family if any raises.** It is four lines of the same
loop the check already runs, and it is the only thing in this repository that looks at the product
side at all.

It fails rather than merely reporting, unlike the existing `raises` column. A zero has a benign
reading — a forbidden product, a species the roots exclude on purpose. A raise on a species the
family *makes itself* has none: it means a job that uses the family kills itself using it.

Controlled both ways, as the §12.7 check was:

| run | result |
|---|---|
| 103 installed families + the repaired family | all ok, **0 own-product raises**, exit 0 |
| the pre-§13 roots, on a throwaway copy | **FAIL**, naming entries 15 and 23 and the product `N#[N+]`, exit 1 |

Logs: `check-generates-feedback`, `check-generates-control-feedback`.

**The controls are now permanent, and self-contained.** Both defects this ticket found live in a
family that has since been repaired, so the real family can only ever demonstrate the *passing*
case — a check whose failing case is unreachable is one nobody can re-verify. `fixtures/` holds
three minimal one-entry families, `Fixture_Healthy`, `Fixture_Inert_Recipe` and
`Fixture_Own_Product_Raises`, which between them exercise both assertions in both directions and
depend on nothing outside their own directory. `python check_family_generates.py --selftest` runs
all three and asserts each produces its expected verdict; it exits 0 today
(`logs/check-selftest.stdout.log`).

**Building them turned up a fourth finding.** `Fixture_Inert_Recipe` could not keep the narrowed
roots: a charge action forces the root's atom types to be charge-resolvable, because
`generate_product_template` applies the recipe to the root **groups** at load time (`family.py:717`
→ `1077`) and `GroupAtom._lose_charge` raises `ActionError: Unknown atom type produced from set
[H, O, metal]`. **A charge-only recipe and an element-named root cannot coexist — the family will
not load at all.** So §11's inert recipe and §13's broad roots are not independent defects: the
broad `R` root is precisely what let the inert recipe hide, and had the roots named their elements
from the start, the inert recipe would have failed loudly at load time instead of passing twelve
checks for three review rounds.

Same caveat as §12.7 on where it belongs — RMG-Py's `test/database/databaseTest.py`, which this
ticket may not modify, so it must be invoked rather than collected. **A separate RMG-Py ticket is
being filed by the owner to land it**, on its own branch in a fresh worktree; nothing here is
copied into RMG-Py. The top of `check_family_generates.py` carries the block that ticket needs:
what the two assertions are, that they should become two methods rather than one, what they proved
over the 103 installed families, and where the fixtures go. It does not reach products of
products — only the first generation is fed back.

### 13.7 What §13 could not reach

- **Species RMG *generates* rather than reads from a library.** The pool is every species the
  installed thermo libraries can name. A running job invents more, and they are not covered.
- **Real cations at scale.** The whole installed database holds **four** cations across 78
  libraries, one of which is this campaign's own `[Ar+]`. Root A's genuine exposure is those plus
  the family's own training and unrepresentable sets — 11 species after narrowing. Root B was
  exercised over all 22,344; root A was not.
- **A real RMG run.** Still nothing through `main.py`, a reactor, or `add_rules_from_training` with
  a real thermo database. Reactor admissibility remains untested (the I-157 precedent: loading is
  not admissibility).
- **Rate correctness**, which is the source audits of §5–§6 and is untouched by a root change.

---

# Round 61

Six HIGH and three MEDIUM, against `995efc1c7`. One of them reverses a claim of impossibility this
report made, one is a defect in the delivered family, one is a defect in the check, and one is a
correction to a claim I over-generalised. **What survives unchanged, so it is not re-defended
below: 17,009 → 0, 630 → 0, the node descents, the twelve checks, and the generated reactions. All
reproduce. They establish the stated corpus results and they do not establish general safety** —
§13.7 said so and §15 now shows exactly where the gap bites.

## 14. N⁺ was not impossible. It is back, and the argument that excluded it was half right

§13 and `groups.py` said root A could not admit N⁺ (`N u2 p1 c+1`) without also admitting H₂O⁺
(`O u1 p1 c+1`) and NO⁺ (`O u0 p1 c+1`), which crash, and concluded that only a new charge-specific
atom type could separate them. Re-derived from scratch (`probe_nitrogen.py`,
`logs/nitrogen.stdout.log`), over all 27 entries and the 22,344-species corpus:

| root A | reproduced | entry 18 | crash-pool | crash-A | crash-back |
|---|---|---|---|---|---|
| `[H,O,metal] ux p[0,2]` (committed) | 15 of 27 | no | 0 | 0 | 0 |
| **flat** `[H,O,N,metal] ux p[0,1,2]` | 16 of 27 | yes | 0 | **638** | **1** |
| `OR{H_cation, O_cation, Metal_cation}` | 15 of 27 | no | 0 | 0 | 0 |
| **`OR{…, N_atom_ion}`** | **16 of 27** | **yes** | **0** | **0** | **0** |

**The premise was right and the conclusion did not follow.** A group's `u` and `p` lists really are
a cross product, and the flat widening really does cost 638 crashes — that half of the argument is
now measured rather than asserted. What it missed is that a root need not be a flat group. §13.3
had already established that `_match_reactant_to_template` handles a `LogicNode` top, and had
rejected `OR{}` roots for a different reason (no sample molecule); nothing connected that to the
nitrogen question one section earlier.

So root A is now `OR{H_cation, O_cation, Metal_cation, N_atom_ion}` with `N_atom_ion` = `N u2 p1 c+1`
exactly. The engine already types N⁺ as `N3sc`; no atom type was added. **Training entry 18
(N⁺ + N₂ → N₂⁺ + N, [Aiken2023] Table 3.16) is back in `training/reactions.py`**, its rate and
provenance untouched — only the family's ability to make the reaction changed. The set-aside file
is down to eleven.

The cost of an `OR` root, paid and recorded: it has no sample molecule, so `probe_nodes.py` now
reports 18 PASS / 0 FAIL / **2** SKIP, root A having joined `Anion`. The twelve checks descend from
its children and all twelve still pass.

H₂O⁺, NO⁺ and Ar⁺ stay out, and none of them for the reason that was written here. All three type
fine. The recipe does not fit them — see §14.1.

### 14.1 Argon: the disposition holds, and here is the measurement a future reader will want

Removing argon from this recipe is correct, and the reason is not the one a reader will guess.
**Widening root A to admit Ar⁺ does not crash — it produces the wrong product.** `GAIN_RADICAL` on
`Ar u1 p3 c+1` gives `Ar u2 p3 c0`, which is a perfectly typeable molecule and is not ground-state
argon (`Ar u0 p4 c0`). A wider root here buys silently wrong chemistry, which is worse than a
crash, because a crash stops the job.

Ground-state argon needs the electron **paired** on arrival: `LOSE_RADICAL + GAIN_PAIR` on the
acceptor. And the two argon entries do not even share a donor recipe with each other — 19
(Ar⁺ + N₂) needs pair donation, 22 (Ar⁺ + O) needs radical donation. **So a single fixed-recipe
noble-gas family cannot cover both**, and no widening of *this* family reaches argon at all.

What this does **not** do is discharge the campaign's argon charge-transfer requirement. That
requirement is real and it belongs to milestone two. Deleting `Noble_cation` was right *within this
recipe's boundary* and it left the chemistry unrepresented, which is the honest statement of the
position. **Do not widen this family for argon.**

## 15. The like-charge guards do not block like-charge reactions, and nothing here can

**This is an open defect in the delivered family.** The two `forbidden` entries block two **bonded**
positive centres. When the positive centres are not bonded, nothing fires:

    Li⁺  +  [NH3+]CCO   →   [Li]  +  [NH3+]CC[OH+]

one reaction, reactant charges (+1, +1), product charges (0, +2), `is_balanced()` **True**, every
guard silent. It then inherits the `Li_ion;B` rate estimated from Li⁺/H⁻ **mutual neutralisation** —
the opposite physical process. Reproduced exactly as round 61 reported it.

**Why every earlier measurement here said zero.** The corpus is the installed thermo libraries,
which hold **four cations across 78 files**. It was nearly blind to the one reactant class this
family is made of, so "0 like-charge" in `generate`, `rootsafety` and `narrow2` is a statement about
the corpus, not about the family. `probe_likecharge.py` fixes that by protonating corpus species at
their lone-pair N and O sites to synthesise a realistic organic-cation set, and driving
cation × cation — the pair type no earlier run here ever formed.

Measured over a 150-cation set (`logs/likecharge.stdout.log`), with root A held at the §14 form:

| root B | like-charge reactions | entries reproduced | wrong | crashes |
|---|---|---|---|---|
| `[H,O,N] u[0,1] p[1,2,3,4] c[0,-1,…]` (committed) | **470** | 16 of 27 | 0 | 0 |
| `[H,O,N] … p[1,3,4]` (no neutral-O donor) | 200 | 16 of 27 | 0 | 0 |
| `OR{Anion, N_neutral}` | 200 | 16 of 27 | 0 | 0 |
| `OR{Anion, N2_only}` — N₂ written out atom by atom | **40** | 16 of 27 | 0 | 0 |

**Nothing reaches zero, and the residual is structural.** Even with N₂ spelled out in full beside
the anion nodes, 40 survive — through molecules like `[O-][N+](=[NH2+])C`, where the donor atom is a
legitimate `O_anion` while the molecule it sits in is a cation. **A group constrains one atom; the
thing that must be forbidden is a property of the pair of molecules.** The engine states this
itself, in `is_charged_reactant_forbidden`'s docstring (`family.py:1726`):

> A group cannot express this: RMG groups match subgraphs, so a `c0` constrains the atom it is
> written on and never the molecule as a whole.

**So I could not carry out this instruction as written, and that is the finding.** The one engine
lever that exists, `allowChargedReactants`, is all-or-nothing and would bar this family's own ion
reactants. What is needed is a family-level declaration that the reactant pair must carry opposite
charge signs — an `rmgpy/` change, which per the standing gate is a line in this report and not
something I made.

**No partial mitigation was taken.** `OR{Anion, N2_only}` cuts 470 → 40 at no measured cost and was
still declined: an unfixable hole made 12× smaller is harder to find and invites false confidence,
and the narrowing would quietly reduce the family to a lookup table over four donors. The guards
are kept for the bonded case they do catch, the gap is written at the guards themselves in
`groups.py`, and `probe_likecharge.py` is committed so the number is reproducible.

## 16. `reversible = False` costs reverse chemistry, and `True` costs training entry 7

Round 61 is right that `reversible` does more than make the reverse direction unavailable.
`_create_reaction` passes it straight into `TemplateReaction(reversible=...)`, so **every generated
reaction is irreversible**: entry 15's own training reaction is reversible and comes out of this
family irreversible, its reverse kinetics suppressed rather than derived from equilibrium. Naming a
reverse family that does not exist was never a reason for that.

I tried to restore `True`, and it fails on measurement:

| | crashes over the 105 training pairs | reactions | reproduced |
|---|---|---|---|
| `reversible = True` | **6**, including **training entry 7 itself** (O⁺ + O⁻) | 47 | 15 of 16 |
| `reversible = False` | 0 | 50 | **16 of 16** |

The reverse applies `LOSE_RADICAL` to `*1`, and on O⁺ (`O u1 p2 c+1`) that gives `O u0 p2 c+2` — an
O²⁺ with no atom type. **The root narrowing did not remove this**; it removed the root-B crash
surface, which is a different thing. Logs: `generate-r61-reversible` against `generate-r61-final`.

So the answer is round 61's second option, stated plainly: **reverse chemistry from this family is
unrepresented.** It is acceptable only in the sense that this family is held back and not installed;
it is not acceptable in a family that ships. Closing it means writing
`Plasma_Charge_Transfer_Reverse`, which is a new family and a new ticket.

**A methodology error worth more than the result.** My first measurement of this said `reversible =
True` was free — 0 crashes, 45 reactions. It was an artifact. `reverse_template` is built at load
time and **only if `reversible` was true then** (`family.py:721-724`), so setting
`family.reversible = True` on an already-loaded family leaves it `None`, the reverse pass never
runs, and you measure the opposite of the truth. I nearly shipped that. It is now a warning
comment at the keyword itself.

Round 61's related observation is confirmed and recorded in `groups.py`: the fabricated product
templates keep the **reactant-side charge lists**, because `GAIN_RADICAL` and `LOSE_PAIR` change a
`GroupAtom`'s `u` and `p` but never its `c`. `A-` comes out `c[+1,+2,+3,+4]` — still positive, after
the acceptor has been neutralised — and `B+` comes out `c[0,-1,…]`. Both backwards.

## 17. The check asserted less than its own verdict claimed

Two holes, both inside the first generation, and a third I introduced while fixing them.

**17.1 "Generates" meant "returned a non-empty list."** The verdict line said *generates at least
one of its own training reactions*; the code asserted only that `generate_reactions` returned
something. Those are different claims. `audit()` now compares each generated reaction against the
entry's **declared products** and reports three numbers — `reproduces`, `other`, `nothing` — and a
family that generates but reproduces nothing now **fails** with its own verdict rather than passing
as `ok`.

**17.2 The product side drove the wrong species, and never tested a unary family.** It fed the
**declared** products, not the ones the family actually makes — the sharper test, because a family
that makes the wrong product will meet *that* product next iteration and the declared one never. It
also always supplied **two** reactants: handing two molecules to a unary family matches nothing and
returns `[]` without ever applying the recipe, so such a family was reported `ok` while its real
product raised the moment it came back alone. Arity now comes from
`len(family.forward_template.reactants)`, and both generated and declared products are driven.

**17.3 The fix's own false positive, caught before it was believed.** With 17.1 in place the sweep
failed three installed families — `1,4_Cyclic_birad_scission`, `Li_Abstraction`,
`Surface_Dissociation_Beta_vdW` — as generating the wrong products. They are not defective. A
reaction found in the **reverse** direction is stored family-forward, so the molecules handed in
come back as `rx.products`; what the check had extracted was each family's own input handed
straight back. Both sides are now compared. **Three families accused by a new assertion, on its
first run, is the shape of a bug in the assertion** — this is the second time in this ticket that
rule has paid.

**Fixtures.** `fixtures/` is up from three to five: `Fixture_Wrong_Products` (generates a reaction
from every entry, never the declared one) and `Fixture_Unary_Product_Raises` (unary; H₂O → H₂O⁺
reproduces, and H₂O⁺ fed back **alone** raises `AtomTypeError` while H₂O⁺ **with a partner** is
silent — the hole, exactly). The unary one needs `electrons = 1` to load at all, because the
depository balance check folds the family electron count into net charge
(`depository.py:236-243`). `--selftest` covers all five and exits 0.

**Controls after all of it:** 103 families audited, 103 `ok`, 0 inert, 0 wrong, 0 unloadable,
**0 own-product raises**; `Plasma_Charge_Transfer` at 16 reproduced, 0 other, 0 nothing, 0 raises.

### 17.4 The claim about charge actions and element-named roots was too wide

I wrote that "a charge-only recipe and an element-named root cannot coexist." The measurement
behind it stands — narrowing `Fixture_Inert_Recipe`'s root A to `[H,O]` refuses to load with
`ActionError: Unknown atom type produced from set [H, O]` — but the generalisation does not. The
real condition is about **transitions, not element lists**:

> a charge action requires every atom type the root admits to have a charge transition available
> from it

A charge-only family whose roots name the six types that *do* carry one — `Li+ Na+ K+ Mg+ Ca+ Ar+`
— loads fine and stays just as inert. Corrected in `fixtures/Fixture_Inert_Recipe/groups.py` and
`fixtures/README.md`. What survives is narrower and still worth having: **in this family** the broad
`R` root is what let the inert recipe hide, and an element-named root A would have surfaced it
loudly at load time.

### 17.5 Every probe now prints the path it actually loaded

`check_family_generates.py` opened by printing `settings['database.directory']` while resolving its
targets from `__file__` — so the committed sweep log named `/home/alon/Code/RMG-database-plasma/input`,
a database that does not contain `Plasma_Charge_Transfer` at all, while correctly auditing this
tree. `run.sh` tells its reader to check exactly that line. The result was right and the only line
the reader was told to check was wrong.

It now prints the paths it read, with the `rmgpy` setting shown beneath and labelled as unused.
`probe_generate.py` and `probe_h2_recipe.py` had the same shape — a hardcoded family path while
loading honoured `I223_FAMILY_ROOT` — and both now derive the printed path the way `load_family()`
derives it, and print `I223_FAMILY_ROOT` beside it. **`probe_h2_recipe.py` was not re-run**: it
references the `Neutral` group node, which §12 deleted, so it no longer runs against this family at
all. Its fix is for the record.

## 18. State after round 61

| | before r61 | after |
|---|---|---|
| training entries active / set aside | 15 / 12 | **16 / 11** |
| entries reproduced, with declared products | 15 of 15 | **16 of 16** |
| reactions generated over the training pool | 45 | **50** |
| crashes: corpus / root-A / own-product | 0 / 0 / 0 | 0 / 0 / 0 |
| root-A matchers in the corpus, of which non-cations | 11 / 0 | 12 / 0 |
| node descents | 18 PASS, 1 SKIP | 18 PASS, **2 SKIP** (root A is now a LogicOr) |
| twelve database checks | pass | pass |
| 103-family sweep | ok, weaker assertion | **ok, against declared products and generated products** |
| like-charge reactions | reported 0 | **470 measured, open defect, §15** |
| reverse chemistry | lost, under-documented | **lost, documented, §16** |
| training entries a reactor could simulate | assumed to await the install gate | **0 of 16, §19 — the gate was never the blocker** |

**Disposition, 2026-09-15.** On the measurement above the owner closed I-223's family work here: the
16-entry family stands as it is, the sibling-family split of the seven set-aside entries is **not**
done on this branch, and the branch-99 thermo carry becomes **its own ticket** (§19.3). The reason
for stopping rather than splitting is that nothing further on this branch can be judged by anything
stronger than the corpus probes that already pass — the ceiling is thermo, not family shape.

**What is still not established.** General safety — everything above is a corpus result. A real RMG
run through `main.py` with a reactor, which **§19 now shows is not merely un-run but unassemblable
today**, for want of thermo rather than for want of the install gate. Reactor admissibility (I-157:
loading is not admissibility).
Rate correctness beyond the §5–§6 audits, and the two `[Ozawa2008]` rates that could not be checked
at all. Products of products. And the like-charge defect of §15, which is open by measurement, not
by omission.

---

## 19. The reactor run is not blocked by the install gate. It is blocked by thermo, and by more than the gate would cost

The step every version of this ticket's "what remains" list has carried — *install it and run a real
reactor* — rests on a premise nobody had measured: that a reactor can be assembled from the species
this family touches. It cannot. Not one of its sixteen training reactions can be simulated by this
database today.

`probe_thermo_coverage.py` takes each of the 25 distinct species in the 16 active training entries —
from the entry's own `Molecule` object, never from a label and never from a SMILES string, because
RMG's SMILES round trip corrupts monatomic ions of both signs — and asks
`ThermoDatabase.get_thermo_data_from_libraries` whether any of the **78** installed libraries matches
it by isomorphism. Log: `logs/thermo-coverage.stdout.log`.

| | |
|---|---|
| distinct species in the training set | 25 |
| with library thermo | **9** |
| without | **16** |
| training entries with every species covered | **0 of 16** |

Covered: `H`, `O`, `O2`, `OH`, `N2` (all from `BurkeH2O2`), `N` (`primaryNS`), `Li` and `Li+`
(`LithiumPrimaryThermo`), and `H+` — on which see §19.1, because that one is worse than a miss.

Missing: **every anion** (`H⁻`, `O⁻`, `OH⁻`), every molecular cation (`O⁺`, `O2⁺`, `OH⁺`, `N⁺`,
`N2⁺`), and every metal except lithium (`Na⁺/Na`, `K⁺/K`, `Mg⁺/Mg`, `Ca⁺/Ca`). Across the whole
campaign the database holds free-cation thermo for exactly three species — `Ar⁺`, `He⁺`, `Ne⁺`, all
noble gases, from I-127/I-179/I-186 — and this family consumes none of them.

**This reorders the remaining work.** Installing the family under `input/` would produce a family
that loads, passes its checks, and still cannot appear in any reactor, because RMG needs thermo for
every species it puts in the core and an ion's thermo must come from a library (group additivity
fabricates 0.0 for a disconnected ion and is not defined for a free monatomic one — the I-157/I-127
rule). The gate is not what stands between this family and a run.

**The cheapest first reaction is entry 24**, `Li⁺ + H⁻ → Li + H`: three of its four species are
covered, so **one sourced `H⁻` entry makes it the first charge-transfer reaction this database can
simulate**. Entry 18, `N⁺ + N2 → N2⁺ + N`, needs two (`N⁺`, `N2⁺`); entries 15 and 23 need three.
Sourcing thermo is outside what this ticket owns, so this is a scope statement for whoever picks it
up, not work done here.

### 19.1 The only H⁺ in the database is a computational-hydrogen-electrode proton

`H⁺` does match — in `electrocatLiThermo`, an electrocatalysis library, with `H298 = 0` and the
comment `1/2 free energy of H2(g)`. That is the CHE reference convention: the proton is *defined*
to be half a hydrogen molecule because it is always paired with an electrode electron. A gas-phase
proton's ΔfH₂₉₈ is about **+1530 kJ/mol**. A deck that requests that library and lets it serve
`H⁺` to training entries 1 and 6 is wrong by roughly that much, silently, with no check anywhere
that would say so — the same green-and-wrong shape as I-204.

It only bites a deck that names `electrocatLiThermo` in its `thermoLibraries`, since a run loads
only the libraries it asks for. But the corollary is the point: **there is no gas-phase H⁺ entry to
ask for instead** — not in the installed database. There is one on branch `99`; see §19.2. For the
plasma campaign this is a missing-library finding with a convention trap attached, and it belongs
with the I-127 cation-convention rule rather than in this family.

### 19.2 The thermo exists. It is on branch `99`, uncarried, and it does not load wholesale

`99:input/thermo/libraries/plasma.py` is a **139-entry** library of charged and metallic species
that no carry ticket has brought into the target database. PART 2 of the probe matches the sixteen
missing species against it, and the answer changes what kind of item this is:

| | |
|---|---|
| missing species branch 99 **holds** | **14 of 16** |
| missing species it lacks too | 2 — neutral **Ca** and **Mg** (their *cations* `Ca⁺`, `Mg⁺` are both there) |
| training entries a full carry would make simulatable | **14 of 16** — all but 27 and 28, the Mg and Ca entries |

So the remaining work is a **thermo carry**, not original sourcing: `H⁻`, `O⁻`, `OH⁻`, `O⁺`, `O2⁺`,
`OH⁺`, `N⁺`, `N2⁺`, `Na⁺/Na`, `K⁺/K`, `Ca⁺`, `Mg⁺` are all written and waiting. Branch 99 also
carries a **correct gas-phase proton** (NASA `a₆ = 184021.49 K`, i.e. ΔfH₂₉₈ ≈ 1530 kJ/mol), which
is the entry §19.1 says the database has no way to ask for.

Two things a carry ticket has to know before it starts, both measured here rather than assumed:

**1. The library does not load.** RMG's `ThermoDatabase.load_libraries` executes a library file
whole, so one bad adjacency list takes the file with it. **13 of the 139 entries build no molecule
against today's engine** — `O+2`, `O+3`, `O+4`, `O+5`, `N2-`, `N2H+`, `C+`, `CH+`, `CH-(S)`, `K-`,
`Li-`, `Na-`, and **`NO+`** — each an `AtomTypeError` for an ionised heavy atom RMG has no atom type
for. That is the same engine limit §13 and §14 ran into from the group side, seen from the thermo
side. The probe therefore parses the file entry by entry; a carry must split, not copy.

`NO+` in that list is worth naming twice: it is the species behind the family's duplicate-rate
work (§5) and several set-aside entries. **It has thermo written, and cannot be loaded today.**

**2. One entry in it carries a units error, in a comment.** The `H+` entry's `longDesc` offers an
"alternative source" `ThermoData` with `H298 = (1530.047,'kcal/mol')`. The gas-phase proton is
1530.0 **kJ**/mol — 365.7 kcal/mol. The active NASA polynomial beside it is correct, so nothing is
wrong today, but the commented block is wrong by 4.184× and is exactly the kind of thing a carry
copies. This is on branch 99 and is not mine to change; it is recorded so the carry sees it.

### 19.3 For the thermo-carry ticket, picking this up cold

The owner's disposition (2026-09-15) is that this is **its own RMG-database ticket**, not part of
I-223 and not folded into whichever ticket installs the family. Everything it needs:

    git show 99:input/thermo/libraries/plasma.py > <somewhere>/libraries/plasma.py
    I223_THERMO99=<somewhere>/libraries ./run.sh thermo-coverage probe_thermo_coverage.py

Full output: `logs/thermo-coverage.stdout.log`. The probe is family-agnostic — point it at any
family and it answers the same question for that one.

**The 14 to carry**, as `<needed species> ← <branch-99 entry label>`:

    H-_r2  ← H-      O-_r2  ← O-      OH-_r2 ← OH-     Op_r1  ← O+
    O2p_r1 ← O2+     OHp_r1 ← OH+     Np_r1  ← N+      N2p    ← N2+
    Nap_r1 ← Na+     Na     ← Na      Kp_r1  ← K+      K      ← K
    Mgp_r1 ← Mg+     Cap_r1 ← Ca+

Neutral **Mg** and **Ca** are in no library anywhere and need real sourcing; they are the only
reason the ceiling is 14 of 16 rather than 16 of 16.

Three constraints on the work, each measured above rather than assumed:

1. **Split, do not copy** — 13 of the 139 entries have no atom type today (§19.2). A file-level copy
   makes the whole library unloadable, which is its state on branch 99 right now.
2. **Per-entry convention check** — every carried ion needs the JANAF-electron-convention vs
   ion-convention subtraction and the ionisation-energy cross-check that the I-127/I-186 tickets
   established. Availability is not validity, and `[Lip]` in `LithiumPrimaryThermo` is already a
   pinned ~20 kJ/mol defect that check catches.
3. **`NO⁺` is an RMG-Py dependency, not a database one.** It has thermo written and no atom type, so
   it cannot be carried until the engine gains one — the same wall §13 and §14 hit from the group
   side.
