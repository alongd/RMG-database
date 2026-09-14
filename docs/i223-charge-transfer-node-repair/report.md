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

**Source verification still undone.** `[Gupta1990]` (RP-1232 Table II) and `[Tanarro2015]` (Table 1,
all twelve entries, §6) are now verified against their primary documents. **`[Ozawa2008]` Table III
and `[Aiken2023]` Table 3.16 are not** — nine entries, including both sides of the N/N₂ split this
ticket just made on the strength of their numbers. Their `T0 = 1 K` is inferred from internal
consistency (θ values line up with bare-T fits), not read. The audit rule in §6 is written down so
whoever takes those two can apply the same one.

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
  because §3 went looking. Other training entries have not been audited that way.
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
| `t0` | base | the `[Gupta1990]` `T0` argument |
| `t0-head` | HEAD | the precondition message, demonstrated |
