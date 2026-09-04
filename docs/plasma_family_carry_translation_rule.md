# Carrying a plasma reaction family from branch `99` to the target branch: the translation rule

**Scope.** Six plasma reaction families live on the old branch `99` and are absent from the
current source-of-truth branch (`plasma`, and its cut `i200-collisional`). They must be carried
across **one at a time**, and a verbatim copy is silently wrong because the two branches declare a
family's electron bookkeeping differently. This report is the pathfinder for that carry: it states
the translation rule as a **rule**, backed by measurements, so the next five carries follow it
without re-deriving. The worked subject is `Plasma_Collisional_Ionization`.

All `file:line` references below are in the target code repository
`/home/alon/Code/RMG-Py-plasma` (branch `plasma`); all family paths are in
`/home/alon/Code/RMG-database-i200-collisional` (branch `i200-collisional`). Measurements were
taken with `rmg_env` and, for the standing-suite runs, `PYTHONPATH=/home/alon/Code/RMG-Py-plasma`.

---

## The rule

To translate a family from the `99` convention to the target convention, apply these five edits and
nothing else. Kinetics values, ranks, `shortDesc` and `longDesc` are **carried unchanged** — their
provenance must travel with them.

1. **Strip every `e-` token from the `template(reactants=[...], products=[...])` call.** The
   electron ceases to be a template species. **This is load-bearing, not cosmetic** (see mechanism
   below): a leftover `e-` inflates the template's declared reactant/product count and the family
   fails to load.

2. **Delete the `custom_kinetics = <...>` line.** The loader never reads it.

3. **Rename `product_electrons = <N>` to `electrons = <±N>`**, a **signed net**. The loader reads
   only `electrons`. Sign convention: `electrons` = number of free electrons the *forward* reaction
   **produces** minus the number it **consumes**.
   - Forward reaction produces a free electron (ionisation, associative ionisation): `+N`.
   - Forward reaction consumes a free electron (attachment): `-N`.

4. **In `training/dictionary.txt`:** remove the `e-` group entry (it is no longer a reaction
   species), and rename every charged-species label to a label-safe form — trailing `+` becomes
   `p`, and by symmetry trailing `-` becomes `m` (`NO+` → `NOp`, `Li2+` → `Li2p`). The adjacency
   lists themselves are unchanged.

5. **In `training/reactions.py`:** rewrite each `entry.label` to match the new template — drop the
   `+ e-` term and use the renamed cation labels. Everything else in the entry is unchanged.

`rules.py` (an empty stub on these families) carries verbatim.

### Illustration, verified at a named commit

The rule was derived from the one family that exists on **both** branches and was already migrated:
`Plasma_Associative_Ionization_Alkali_Alkali`. At the current branch tips
(`i200-collisional`@`3c1c57be2`), `git diff 99 i200-collisional -- <that family>` is exactly:

- `groups.py`: `products=["AB+", "e-"]` → `products=["AB+"]`; `custom_kinetics = False` deleted;
  `product_electrons = 1` → `electrons = 1`.
- `training/dictionary.txt`: `e-` group deleted; `Li2+`/`Na2+`/`K2+`/`NaK+` → `Li2p`/`Na2p`/`K2p`/`NaKp`.
- `training/reactions.py`: each label `... <=> Li2+ + e-` → `... <=> Li2p`.

That enumeration is an illustration of the rule above, not a substitute for it: the next family may
carry a `-` label, an electron on the reactant side, or `product_electrons` other than 1, and the
rule covers those where a copied list would not.

---

## What the loader actually reads (evidence for edits 2 and 3)

`KineticsFamily.load` (`family.py:649`) execs `groups.py` into a `local_context` dict that it
pre-seeds — including `local_context['electrons'] = 0` at `family.py:675` — then reads specific keys
back out afterward. The electron count is read at:

```
family.py:696   self.electrons = local_context.get('electrons', 0)
```

There is **no** read of `product_electrons` and **no** read of `custom_kinetics` anywhere in
`family.py`. Assigning them in `groups.py` therefore has no effect: the exec sets them in
`local_context`, and nothing consumes them. A verbatim `99` copy — which sets `product_electrons`
but never `electrons` — leaves `self.electrons` at the seeded default `0`.

**Measured, before/after (`electrons` attribute after `KineticsFamily.load`):**

```
[VERBATIM-99]  electrons = 0     (product_electrons=1 ignored; seeded default 0 stuck)
[TRANSLATED]   electrons = 1     (electrons=1 read at family.py:696)
```

## Why stripping `e-` from the template is load-bearing (evidence for edit 1)

The template's declared product count gates reaction/product-template generation:

```
family.py:1513   product_num = self.product_num or len(template.products)
family.py:1522   (products rejected when the recipe's fragment split != product_num)
```

The recipe for `A_rad + M => A+ + e- + M` touches only `*1`; it makes no bond between the two
reactant fragments, so applying it to `A_rad`·`M` yields exactly **two** product fragments (`A+`,
`M`). If `e-` is left in the template `products`, `len(template.products) == 3` but the split
yields 2, the products are rejected, `generate_product_template` (`family.py:717` → `1082`) receives
an empty list, and load dies with `IndexError: list index out of range`. Removing `e-` makes the
declared count (2) match the split (2). The electron is instead accounted for by the `electrons`
scalar.

**This corrects a premise.** It is natural to assume `electrons = 0` is what breaks the verbatim
load. It is not: forcing `electrons = 0` on an *otherwise-translated* family (with `e-` already
stripped) loads past `generate_product_template` unchanged. The groups-load crash is driven by the
leftover `e-` in the template; the `electrons` value drives downstream charge balance
(`family.py:1574-1583`) and the `Reaction.electrons` metadata that lands on the plasma electron
balance, not the template geometry.

## Sign convention, cross-checked (evidence for edit 3)

`family.py:1574-1583` uses `self.electrons` for charge balance: a positive value is treated as
electrons appearing on the product side, a negative value as electrons on the reactant side. Two
families already on the target branch pin the two signs:

- `Plasma_Electron_Attachment` (`A + e- => A-`, electron consumed): `electrons = -1`.
- `Plasma_Associative_Ionization_Alkali_Alkali` (`A + B => AB+ + e-`, electron produced):
  `electrons = 1`.

For `Plasma_Collisional_Ionization`'s `A_rad + M => A+ + e- + M`, one electron is produced, so
**`electrons = +1`**. Charge-balance check: reactants net 0; products `A+`(+1) with the electron in
the scalar; `family.py:1581` does `product_net_charge -= electrons` → `+1 - 1 = 0` = reactants.
Balances. `electrons = 0` would leave products at `+1 ≠ 0` and the reaction would be silently
dropped (`family.py:1585-1589`, debug-log only); `electrons = -1` would unbalance the reactant side
and also drop it.

---

## `Plasma_Collisional_Ionization` — carry outcome

Applying the rule to all four files (diff vs. verbatim `99` shows *only* the rule's edits, no
kinetics touched). The translated family loads through `groups` and reports `electrons = 1` and
template `['A_rad','M'] -> ['A+','M']`.

### The blocker the rule does not cover: the `NO+` training species

The rule is **necessary but not sufficient** for this family. Its two training entries use the
species `NO+` (nitrosonium), whose adjacency on `99` is:

```
NO+
1 N u0 p1 c+1 {2,D}      # +1 on N, double bond
2 O u0 p2 c0  {1,D}
```

On the target branch this fails atom-type perception:
`AtomTypeError: Unable to determine atom type for atom N+, which has ... 1 double bonds (1 to O) ...
1 lone pairs, and +1 charge`. It is also chemically wrong: nitrosonium is `[N≡O]+` with the formal
charge on **oxygen**. The only adjacency that both is correct and loads on this branch is the
charge-on-O triple-bond form (the motif this database already uses for the isoelectronic CO):

```
NOp
1 N u0 p1 c0  {2,T}
2 O u0 p1 c+1 {1,T}      # N#[O+]
```

Adopting that adjacency is a **species-identity change** (a gated action) and would be "refitting" a
training entry (a Non-goal). Per the user's decision, the two training entries are therefore
**held** — preserved as comments in `training/reactions.py`, with the correct `NOp` adjacency
recorded there — and `training/dictionary.txt` is empty. The family loads with an empty training
set (`electrons = 1`, `n_training = 0`); re-enabling the entries is a one-step follow-up once the
`NO+` representation is approved.

**Lesson for the next five carries:** the five-line rule handles electron bookkeeping, but a
family's training species must independently survive the target branch's atom-type perception. Probe
each training species with `Molecule().from_adjacency_list(...)` before assuming the carry loads.

### The standing suite goes red — and why that is the *check's* coverage gap, not a family defect

Once the translation lets the family load through `groups` (the verbatim `99` copy never did),
`generate_product_template` runs and the standing kinetics-family suite
(`RMG-Py-plasma/test/database/databaseTest.py::TestDatabase::test_kinetics`) goes from green to red:

```
baseline DB (RMG-database-plasma/input) : 1 passed  in 438.19s
worktree DB (this family added)         : 1 failed  in 368.90s   (kinetics_check_groups_nonidentical)
```

The error is `Group N2 ... identical to group M1` … `Group He ... identical to group M6`. Two
readings are possible — a real defect in the family, or a false positive in the check — and the
evidence supports the **false positive / coverage gap** reading:

- **What the check does (read-only, `databaseTest.py:663-682`).** It iterates *every* group entry
  pairwise — `for nodeName, nodeGroup in family.entries.items(): for nodeNameOther, nodeGroupOther
  in entries_copy.items(): family.match_node_to_node(...)` — and raises if any two entries are
  adjacency-identical. It is **group-by-group over all entries**, including the ones
  `generate_product_template` auto-creates (`A+`, and `M1..M6`, the product-side expansion of the
  `M = OR{N2,N,O2,O,Ar,He}` union). It does not know or care that some of those entries are a
  spectator's product image.

- **Why the identity is correct by construction.** The recipe (`LOSE_RADICAL *1`, `GAIN_CHARGE *1`)
  acts *only* on `A_rad` (`*1`); it never touches `M` (`*2`). A third body is, by definition, a
  species that leaves the reaction unchanged, so its product group is *necessarily* identical to its
  reactant group. `M1..M6 == N2..He` is not a duplication bug in the family — it is what a spectator
  is. The redundant *concrete* clones are produced by `generate_product_template` (RMG-Py, out of
  scope here); the family's `groups.py` is a faithful representation of "`A_rad` ionises, `M` is any
  of these six third bodies, unchanged."

- **The check has simply never seen a spectator.** Baseline is green, so no family currently on the
  branch carries two adjacency-identical group entries — i.e. none exercises a true unmodified
  spectator. Other families whose template lists a species on both sides (`H_Abstraction`,
  `Surface_Abstraction`, `SubstitutionS`, …) are *not* spectators: their recipe modifies those
  species, so their product groups differ from their reactant groups and no identical pair arises.
  `Plasma_Collisional_Ionization` is the **first** family to present the check with a genuine third
  body, so the failure is a coverage gap the check has not been written for, not a defect it caught.

Verdict: **coverage gap in `kinetics_check_groups_nonidentical`, not a defect in the carried
family.** The honest fix is code-side (teach the check, or `generate_product_template`, about
spectators) and out of this database-only ticket's scope. Because that fix cannot be made here, and
because leaving the standing suite red is a regression the ticket forbids, the family is **not added
to `input/`**; its translated files are preserved under
`docs/plasma_collisional_ionization_staged/` for the follow-up.

### This blocker is specific to this one family

Of the six families being carried from `99`, **only `Plasma_Collisional_Ionization` has a molecular
spectator** in its template. The other five list only the electron `e-` on both sides —
`Plasma_Electron_Impact_Ionization` (`A_rad + e- => A+ + e- + e-`),
`Plasma_Electron_Impact_Dissociation` (`AB + e- => A + B + e-`),
`Plasma_Radiative_Recombination`, `Plasma_Charge_Transfer`, `Plasma_Ion_Molecule_Association` — and
edit 1 of the rule **strips `e-` from the template** (it becomes the `electrons` scalar), so no
spectator group is ever created and none of them can trip this check. The translation rule therefore
still unblocks the other carries unchanged; this report's two blockers (`NO+`, spectator) are
`Plasma_Collisional_Ionization`'s alone.

### The 5 torr argon deck is unaffected

The canonical deck (`RMG-Py-plasma/docs/i194-ar5torr-plasma-lineage/input.py`, run with
`RMG-Py-plasma/rmg.py` at tip `bb0a5d8e7`, clean run directory, `PYTHON_EXIT` captured from the
interpreter) produces the **same passing outcome** on both databases, confirming the carry does not
touch it:

```
baseline DB (RMG-database-plasma/input)          : PYTHON_EXIT=0, one MODEL GENERATION COMPLETED, final core 3 species / 1 reaction
worktree DB (RMG-database-i200-collisional/input) : PYTHON_EXIT=0, one MODEL GENERATION COMPLETED, final core 3 species / 1 reaction
```

The one core reaction is the argon ionisation `Ar + e- => Arp + e- + e-`, promoted from edge to core
(`Adding species Arp(3) to model core` / `Moved 1 reactions from edge to core`). It is carried by the
standalone `PlasmaArgon` reaction library, which the deck requests alongside
`PlasmaElectronImpactIonization` and `PlasmaRadiativeRecombination`. "Unaffected" is shown by baseline
== worktree, both green.

**Correction — a harness error in an earlier pass, recorded so it is not repeated.** The first
measurement of this section used the wrong deck: `RMG-Py-i164-ar5torr/docs/i164-ar5torr/input.py`,
from an older worktree whose `reactionLibraries` predates the `PlasmaArgon` split (I-193) and lists
only `PlasmaElectronImpactIonization` + `PlasmaRadiativeRecombination`. Since I-193 the argon reaction
lives in `PlasmaArgon` and in neither of those, so that stale deck loaded **no** argon chemistry, the
model stayed reaction-free, and the `CoreError` guard at `main.py:1878` correctly fired (3 species /
0 reactions, `PYTHON_EXIT=1`) on *both* databases. That guard is real and correctly on the branch;
the wrong conclusion was that it fires **at head** — it does not. The cause was the deck copy (wrong
worktree, missing `PlasmaArgon`), not the plasma tip and not this carry.

### Registration

Were the family added, it would go in **no** set in `input/kinetics/families/recommended.py`,
matching the four plasma families already on the branch (which appear in no set). A run would get it
only by naming it explicitly.

### Outcome

The pathfinder **translation rule is derived, verified, and complete** — it unblocks the five
remaining carries. `Plasma_Collisional_Ionization` itself is **held out of `input/`** pending two
decisions that are outside this ticket's scope: (1) the `NO+` species representation (a gated
species-identity change), and (2) the spectator coverage gap in `kinetics_check_groups_nonidentical`
(a code-side fix). Its translated files are staged under `docs/plasma_collisional_ionization_staged/`
so re-landing, once both are resolved, is a move plus one training-entry re-enable.
