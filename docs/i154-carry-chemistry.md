# I-154 — Carrying the earlier line's plasma chemistry onto the rebuilt foundation

Evidence labels on every claim: **[M]** measured here against the pinned runtime (command and
output reproducible via `docs/i154-carry-chemistry/verify_i154.py`), **[R]** read from code
(file:line), **[D]** read from this database, **[I]** inference with its basis named.

Everything below was measured against
`database.directory = /home/alon/Code/RMG-database-i154-carry-chemistry/input`, with
`rmgpy` resolved from `/home/alon/Code/RMG-Py-i154-carry-chemistry`. Both are printed at the head
of every verifier run, because a suite measured against the wrong database has already cost this
project one meaningless-green result.

---

## 0. What landed, in one table

| Owner | Kind | Carried | Entries | Electron placement |
|---|---|---|---|---|
| `Plasma_Associative_Ionization_Alkali_Alkali` | family | **yes** | 4 training | **(0, 1)** |
| `Plasma_Associative_Ionization_Alkali_Alkaline` | family | **yes** | 1 training | **(0, 1)** |
| `Plasma_Associative_Ionization_Alkaline_Alkaline` | family | **yes** | 3 training | **(0, 1)** |
| `PlasmaAir` | library | **partial** | 42 of 94 | none — every surviving entry conserves the electron |
| `PlasmaAlkali` | library | **partial** | 52 of 66 | none — same |
| `Plasma_Charge_Transfer` | family | held back | (28) | §4.1 |
| `Plasma_Collisional_Ionization` | family | held back | (2) | §4.2 |
| `Plasma_Electron_Impact_Dissociation` | family | held back | (5) | §4.2 |
| `Plasma_Ion_Molecule_Association` | family | held back | (3) | §4.3 |
| `Plasma_Electron_Impact_Ionization` | family | **not carried** | — | superseded, §2 |
| `Plasma_Radiative_Recombination` | family | **not carried** | — | superseded, §2 |

**Landed:** three families with 8 training reactions, two libraries with 94 entries, three electron
placement declarations. [M]

**Held back:** four families, with what each needs written down in §4. Their files are preserved
verbatim under `docs/i154-carry-chemistry/held-back/` so the next ticket starts from the converted
form rather than from branch `99` again.

**The headline finding is §4.** Branch `99`'s plasma families were evidently never run against
RMG's own database consistency suite (`test/database/databaseTest.py`), and four of the seven do
not pass it. Two of those four fail for the same structural reason, and it is a limitation of RMG,
not a mistake by their author: **RMG's family model cannot express a spectator template
participant** — a third body or an incident electron that appears on both sides unchanged. The
suite is green with the three that do pass, measured against a green baseline. [M]

---

## 1. Which earlier branch is authoritative: `99`, not `99_b`

Both branches carry plasma work and they have diverged — merge-base `e883a4c47` (2025-07-09), with
21 commits on `99` and 7 on `99_b` since. [M] `99` is authoritative, on four measurements:

| | `99` | `99_b` |
|---|---|---|
| tip | `ff3299e07`, 2026-04-30 | `cc9d0103f`, 2025-12-16 |
| `PlasmaAir` entries | 95 | 85 |
| `PlasmaAlkali` entries | 66 | 43 |
| plasma families | 9 | 7 |

`99` is later, larger, and a near-superset. Its extra content is real chemistry, not churn: the
`Os` (excited atomic oxygen) channels, electron-impact dissociation of water, and 27 alkali
oxide/hydroxide reactions absent from `99_b`. Where the two overlap they agree — the
`Plasma_Charge_Transfer` training sets are the same 28 reactions under different labels (`99` adds
`_r1`/`_r2` role suffixes), and the three `PlasmaAir` entries that look "lost" from `99_b` are the
same reactions made irreversible on `99`. [M]

**Exactly one thing exists on `99_b` and not on `99`:** the `PlasmaAlkali` entry
`OH + e- <=> OH-`. Its absence from `99` is correct rather than accidental — non-dissociative
electron attachment is owned on this line by the `Plasma_Electron_Attachment` family, whose
training set already carries `OH + e- => OH-` from the same source ([JensenJones1977]). Carrying it
into a library too would have duplicated the channel. [D]

`99` also SPLITS associative ionisation into three metal-specific families where `99_b` had one
generic `Plasma_Associative_Ionization`. That split is carried, because a single tree over
`alkali + alkali`, `alkali + alkaline` and `alkaline + alkaline` would put three different recipes
under one root.

---

## 2. What was deliberately NOT carried, and why

`99` has families named `Plasma_Electron_Impact_Ionization` and `Plasma_Radiative_Recombination`.
This line already owns both chemistries — as the **libraries** `PlasmaElectronImpactIonization` and
`PlasmaRadiativeRecombination`. Those libraries are not an accident of naming: each carries a long,
argued rationale for why a family was rejected *on measurement*, recorded in
`docs/i114-ionisation-owner.md` and `docs/i119-recombination-loss.md`. The short form [R]:

* RMG's rate-rule averaging cannot combine two `VoronovEIArrhenius` or two `BadnellRRArrhenius`
  fits at all — `family.average_kinetics` guards on a closed allowlist of
  `[Arrhenius, SurfaceChargeTransfer, ArrheniusChargeTransfer, Marcus]` — so such a family is
  capped at one training entry per node and buys no generativity.
* The fits are per-species, indexed by `(Z, N)`, with no group-additivity trend to interpolate
  along. A family would match exactly the species it has data for, which is the set of entries a
  library would hold anyway.

Carrying the `99` families would have created a second owner for a chemistry this line has already
adjudicated, and the two owners would disagree. They are dropped, and this paragraph is the record
of the ruling.

---

## 3. The four load-time blockers, measured

The ticket's premise — that this chemistry was carryable and only lacked a placement declaration —
was **refuted on first contact**. Loading the `99` content unchanged against this engine: 0 of 2
libraries and 0 of 9 families load. [M] Four independent causes, none of them the declaration:

### 3.1 Charge tokens above +4 (`InvalidAdjacencyListError`)

Five family group trees use `c[0,+1,...,+8]`; this engine's `adjlist.py` parser stopped at `+4`.
**Fixed** by carrying branch `99`'s own eight-line addition to that parser — purely additive, it
extends the recognised token set and changes nothing about existing behaviour.

### 3.2 No alkali or alkaline-earth atom types (`KeyError: 'Na'`)

`Na`, `K`, `Mg`, `Ca` and the generic `metal`/`alkali`/`alkaline` nodes exist only on RMG-Py `99`.
**Fixed**, on the user's instruction, but *not* by taking that branch's files: see §6.

### 3.3 `NO+` drawn without an octet (`AtomTypeError`)

`99` writes `NO+` as `N u0 p1 c+1 {2,D}` — a nitrogen with six valence electrons. This engine has
no atom type for it, and it is the worse Lewis structure: NO⁺ is isoelectronic with N₂. Re-drawn as
`N#O+` (`N u0 p1 c0 {2,T}` / `O u0 p1 c+1 {1,T}`), which resolves to `N3t`/`O4tc` with net charge
+1. [M] Same species, same charge, no rate touched. In what landed this is one file, the `PlasmaAir`
dictionary; the same correction was also needed in the `Plasma_Charge_Transfer` and
`Plasma_Collisional_Ionization` training dictionaries, which are held back (§4).

### 3.4 The structural one: a library cannot hold an electron-count-changing reaction

This is the finding that shapes the whole delivery, and it is worth stating precisely.

`99` carries the electron as an **explicit participant** (`N + O <=> NO+ + e-`). On this line
`Reaction.is_balanced()` treats the free electron as a conserved pseudo-element `E`, so any
explicit-electron shape whose electron **count changes** across the arrow fails the per-element
comparison before charge is even looked at. That is not incidental — it is pinned as
`EXPECTED['EI/explicit'] = (False, False, True)` in
`test/rmgpy/i108ElectronRepresentationMatrixTest.py`. [R]

The canonical alternative is the metadata scalar `Reaction.electrons`. But `KineticsLibrary.load`
sets it from exactly one place — `entry.data.electrons`, the rate law's own field — and
`load_entry` takes no electron argument [R]. Measured, of the rate laws in play: [M]

| rate law | carries `electrons`? |
|---|---|
| `Arrhenius`, `ThirdBody`, `Lindemann`, `Troe` | no |
| `TwoTemperaturePlasma`, `ElectronCollisionPlasma` | **no** |
| `BadnellRRArrhenius`, `VoronovEIArrhenius`, `ArrheniusChargeTransfer` | yes |

So **a kinetics library on this line can only hold an electron-count-changing reaction if its rate
law carries the count itself.** That is why the two shipped plasma libraries hold exactly one entry
each, and it is a property of the loader, not of those libraries.

Consequence: 51 `PlasmaAir` entries and 14 `PlasmaAlkali` entries have no representation here at
all. They are listed in full in §7. The agreed fix — extending `KineticsLibrary.load_entry` with an
`electrons=` argument — is deliberately **not** done in this ticket; it is new engine work with its
own design question (a library spans several electron shapes, and the placement registry holds one
declaration per owner).

The **families** are unaffected by this one: a family declares `electrons` in its `groups.py` and
hands the count down to its training depository [R]. Every one of the 46 training reactions loads.
Loading, however, turned out not to be the last gate — see §4.

---

## 4. What the consistency suite refused, and why four families are held back

Loading is necessary, not sufficient. `test/database/databaseTest.py` is this database's own
consistency suite, and it checks things a load never does: that every group descends to its root,
that no two nodes match the same structures, that a sample molecule built from each node can
actually react, that parent/child relations are real. **Baseline measured first: the suite is green
on this branch without any carried family (6 passed).** [M] So everything below is the carry's
doing, and nothing is a pre-existing failure being blamed on it.

All seven families load. Four fail the suite.

### 4.1 `Plasma_Charge_Transfer` — its group tree, on four counts

Held back after four separate defects, each found by the suite and each needing a chemistry
decision rather than a transcription:

* `NO_ion` was drawn as the non-octet `N(+)=O` (the same defect as §3.3, here in a *group*). The
  octet form puts the charge on oxygen, which also moves the `*1` label the recipe discharges — so
  the node has to move from the `N_cation` branch to the `O_cation` branch. Chemically right,
  but it is a redesign of the tree, not a transcription.
* `Anion` (`1 *2 R ux px c-1`) and `O_anion` (`1 *2 O ux px c-1`) leave lone pairs WILD. The sample
  builder resolves the wildcard to the minimum and then bonds the atom up to satisfy the charge,
  producing "H⁻ with two single bonds" and "O⁻ with three" — not atoms. [M]
* `H2_ion` samples to a molecule whose charge lands on the wrong atom, because H₂⁺ has a
  **one-electron bond** and RMG has no way to write one. Its formal-charge stand-in is overridden
  by RMG's own charge recomputation.
* `Noble_cation` (`[He,Ne,Ar] ux px c+1`) samples NEUTRAL: He⁺ needs `u1 p0`, Ar⁺ needs `u1 p3`, and
  one group cannot pin lone pairs across both.

I fixed the first three far enough to see the fourth, then stopped: past that point I was
redesigning someone else's family tree without a chemist, which is what this ticket is told not to
do. The partial repairs are in the held-back copy.

### 4.2 `Plasma_Collisional_Ionization` and `Plasma_Electron_Impact_Dissociation` — spectators

**This is the generalisable finding.** Both families make a SPECTATOR a template participant: a
third-body collider `M` in one, the incident electron in the other. Both pass through the recipe
unchanged. RMG's family model cannot express that, and its own two consistency checks prove it by
contradicting each other:

* `kinetics_check_groups_nonidentical` refuses two nodes that match the same structures. A
  spectator's product-template group is by construction identical to its reactant group. For
  `Plasma_Collisional_Ionization`, whose `M` is a `LogicOr` over six colliders, the engine
  auto-generates six product groups `M1`…`M6`, each identical to a reactant leaf. [M]
* `kinetics_check_reactant_and_product_template` refuses a product label equal to a reactant label
  in a non-reversible family, and says "Please rename product label".

For `Plasma_Electron_Impact_Dissociation` those two are jointly unsatisfiable, and I measured it
rather than reasoned it: renaming the product-side electron to `e-_p` satisfies the second check and
immediately trips the first, on the pair `('e-', 'e-_p')`. [M] There is no spelling that satisfies
both, because the requirement is contradictory for a participant that must appear on both sides
with the same structure and a different name.

Landing either family needs a decision that is RMG-Py's, not the database's: either the family model
grows a spectator/third-body participant kind, or these two are re-expressed without one (the
collider folded into rate rules; the electron carried as a count, which §4.4 shows it cannot be).

### 4.3 `Plasma_Ion_Molecule_Association` — the product is not a molecule

`apply_recipe` returns `None` for every sample, and the reason is in the data, not the engine: the
recipe forms a **zero-order** bond (`['FORM_BOND', '*1', 0, '*2']`) and the training "products" are
written as two unbonded atoms — `LiHp` is `1 Li u0 p0 c+1` and `2 H u1 p0 c0`, with no bond line at
all. [D] So the "association product" never associates: the structure splits into two fragments and
the recipe reports the wrong product count.

That is a straightforward authored defect, and repairing it means deciding what LiH⁺ is — bond
order, where the charge sits, whether `*2` should lose a radical at all. A chemistry decision, so it
is reported rather than guessed.

### 4.4 A limit of the placement registry, found here

`Plasma_Electron_Impact_Dissociation` is `AB + e- -> A + B + e-`: an incident electron that is
CONSERVED. Its natural declaration would be `(1, 1)` — and **that declaration could never be
honoured**, because `PlasmaReactor._resolve_electron_placements` is gated on `electrons != 0` [R]
and a conserving shape has a zero net count. The registry is unreachable for electron-conserving
chemistry. Such a family has to carry its electron as an explicit template participant, which is
exactly what makes it fall foul of §4.2. Both halves of that trap are now recorded in
`rmgpy/electron_placement.py`.

---

## 5. The electron placement of every carried owner, derived

The registry is `rmgpy.electron_placement.FAMILY_ELECTRON_PLACEMENT`, keyed by owner label, valued
`(reactant_count, product_count)` — incident order and net production, which are two different
numbers.

**Four owners declared, all `(0, 1)`** — and they are the first entries in that table with an empty
reactant side:

```
Plasma_Associative_Ionization_Alkali_Alkali        Li + Li  ->  Li2+ + e-
Plasma_Associative_Ionization_Alkali_Alkaline      Na + Mg  ->  NaMg+ + e-
Plasma_Associative_Ionization_Alkaline_Alkaline    O  + O   ->  O2+  + e-
Plasma_Collisional_Ionization                      NO + O2  ->  NO+  + e- + O2
```

No electron is incident, so the electron contributes **nothing to the reaction order** — the rate
is second order in the heavy particles, which is what the `cm^3/(mol*s)` coefficients are written
for — while the net change is **+1**. This is the mirror image of attachment's degenerate case:
there one number did both jobs because the electron was purely incident; here the two numbers
differ because it is purely produced. `(0, 1)` passes the resolver's shape check because it still
places an electron somewhere; only `(0, 0)` is malformed. [R]

Verified end to end: a `Plasma_Collisional_Ionization`-shaped reaction pushed through
`resolve_electron_placement` comes back with zero reactant electrons, one product electron, and
`electrons = 0` on the view, with the canonical reaction unmutated. [M]

**Three owners deliberately undeclared**, each for a measured reason:

* `Plasma_Charge_Transfer` (`A+ + B- -> A + B`) and `Plasma_Ion_Molecule_Association`
  (`Li+ + H -> LiH+`) — no free electron participates at all. Both declare `electrons = 0`, so the
  resolver is never reached, and a declaration would be a claim about a shape that does not exist.
* `Plasma_Electron_Impact_Dissociation` (`AB + e- -> A + B + e-`) — this one **does** carry an
  incident electron, and still declares nothing, because on `99` the electron is a genuine template
  reactant: a real group in its `groups.py`, tagged `*3`, with the electron in its training
  dictionary [D]. Its reactions therefore arrive already in reactor form with `electrons = 0`, and
  `PlasmaReactor._resolve_electron_placements` passes them through by identity. There is nothing to
  place.

  **Worth naming as a limit of the registry:** a `(1, 1)` declaration could not be honoured even if
  written. The resolver is gated on `electrons != 0` [R] and an electron-*conserving* shape has a
  zero net count, so it never reaches the table. The explicit-participant representation is not a
  workaround for that — it is the representation that shape already has.

Both libraries are also undeclared, and correctly so: every entry that survived the §3.4 filter
conserves the electron count. The verifier asserts that, so the absence stays correct rather than
lucky. [M]

---

## 6. What was changed in existing files, and why

The user directed that the alkali/alkaline-earth atom types be brought over. A literal
`git checkout 99 -- rmgpy/molecule/*.py` would not have been a port but a **revert**: 26 commits on
this line touch those four files since the merge base, and the checkout would have deleted this
line's `F0sc`/`F1sc`/`Cl0sc`/`Br0sc` charged-halogen atom types (`99eca41be`, `07d88306d`) and
desynchronised `molecule.py` from a `molecule.pxd` that differs by 207 lines, which does not
compile. [M] Delivered instead as a targeted merge — every atom type and element-table row `99`
adds is present, and this line's 26 commits are intact.

| File | Change | Why |
|---|---|---|
| `rmgpy/molecule/adjlist.py` | +8 lines: recognise charge tokens `+5`…`+8` | §3.1. Branch `99`'s own edit, purely additive |
| `rmgpy/molecule/element.py` | 4 dict rows extended for Na/K/Mg/Ca (`valences`, `valence_electrons`, `lone_pairs`, `electronegativity`) | §3.2. Additive |
| `rmgpy/molecule/atomtype.py` | new `metal`/`alkali`/`alkaline` generics; new `Na`,`K`,`Mg`,`Ca` types and their charged/neutral forms with `set_actions`; Li joined to `metal`/`alkali`; `allElements` extended | §3.2 |
| `rmgpy/molecule/atomtype.py` | **`Ca` (atomic carbon) renamed to `Catom`** | see below |
| `rmgpy/molecule/group.py` | `default_lone_pairs` extended with Li/Na/K/Mg/Ca | see below |
| `rmgpy/electron_placement.py` | four `(0, 1)` declarations, and the reasoning for the three deliberate absences | §4 |

**The `Ca` rename is the one to look at.** On this line `Ca` was the atom type for *atomic carbon*;
in the carried chemistry `Ca` means *calcium*. Keeping both would have made every `Ca` group in the
carried families silently match atomic carbon — a wrong match, which is worse than a failure.
Branch `99` solved it the same way. Measured blast radius before doing it: `Ca` appears as an
atom-type token in **zero** database adjacency lists, **zero** RMG-Py test files, and 11 places in
`atomtype.py` itself, all of them the carbon one. [M] The two other `'Ca'` hits in RMG-Py are the
chemical *element* calcium, which is a different namespace.

**`allElements` and `default_lone_pairs` are the non-obvious part**, and they were found by a
crash, not by reading. Adding the atom types alone made `test_make_sample_molecule` **segfault** —
not raise, segfault — for every new element. [M] `GroupAtom.make_sample_atom` resolves an atom
type's element by scanning `allElements`; an atom type absent from that list leaves `element` as
`None`, and the compiled Cython dereferences it. Registering the four elements there, and giving
them lone-pair defaults, fixes it: `test/rmgpy/molecule` goes from a core dump to **775 passed, 14
skipped**. [M]

Recorded because it generalises: **adding an atom type to `ATOMTYPES` is not enough — it must also
be registered in `allElements`, or the failure is a segfault in a test that never names your type.**

**Deliberately NOT carried from `99`'s `element.py`:** that branch flips
`chemkin_name = chemkin_name or self.symbol` to `... or self.name`, which renames every species in
every Chemkin file this engine writes. Unrelated to atom types, and a regression.

**`recommended.py` is untouched.** `Plasma_Electron_Attachment` is not in any recommended set
either [D], so the convention on this line is that plasma families are requested individually in an
input file. Adding them to `default` would put plasma chemistry into every ordinary combustion run.

---

## 7. Reservations — read these before trusting a number

The carry changed no rate coefficient anywhere. These are problems the carried chemistry *arrived*
with, reported rather than repaired.

1. **Seven of the eight training rates that landed are not sourced — read this one first.**
   Across all seven families examined, 18 of 46 training reactions carry a `shortDesc` of
   `estimated` or `[estimated]` rather than a citation. [M] The three families that LANDED are the
   worst of them:

   | family | entries | `estimated` |
   |---|---|---|
   | `Plasma_Associative_Ionization_Alkali_Alkali` | 4 | **4** |
   | `Plasma_Associative_Ionization_Alkali_Alkaline` | 1 | **1** |
   | `Plasma_Associative_Ionization_Alkaline_Alkaline` | 3 | **2** |
   | *(held back)* `Plasma_Charge_Transfer` | 28 | 5 |
   | *(held back)* `Plasma_Collisional_Ionization` | 2 | 0 |
   | *(held back)* `Plasma_Electron_Impact_Dissociation` | 5 | 3 |
   | *(held back)* `Plasma_Ion_Molecule_Association` | 3 | **3** |

   Only one landed training rate is sourced: `O + O <=> O2+` from [Aiken2025]. The other seven are
   the author's own estimates. These are FAMILIES, so an estimated rate does not stay on its own
   reaction — `fill_rules_by_averaging_up` propagates it to every species the tree matches. **They
   should be sourced or removed before any of these three families is used in a model.** The carry
   preserved the provenance verbatim and upgraded nothing, which is why this is visible at all.

2. **One entry was dropped as unbalanced.** `PlasmaAir`'s `N2+ + N2 => N2 + N + N` carries charge
   +1 on the left and 0 on the right [M]. It is a defect on the source branch, and it is reported
   rather than repaired because the intended channel is genuinely ambiguous — dissociative
   recombination would need an electron, charge transfer would need a cation product. Guessing
   would be authoring chemistry.

3. **`Plasma_Associative_Ionization_Alkali_Alkaline` was narrowed to its trained scope.** Its `B`
   root admitted `[Ca,Mg,O,N] u[2,3]`, but the recipe applies `GAIN_CHARGE` to `*2` and this
   engine's generic `O` carries `increment_charge=[]`, so the union cannot be charged and the
   family does not load [M]. The O/N branch also has **no training data at all** — the only
   training reaction is `Na + Mg` — so `fill_rules_by_averaging_up` would have handed an
   alkali-metal rate to every O and N atom in a mechanism. Narrowed to `[Ca,Mg] u2`, and the three
   untrained `nonmetal_B`/`O_B`/`N_B` nodes dropped with it. This is the same doctrine
   `Plasma_Electron_Attachment` already states: the tree matches only what the training set
   supports.

4. **`Plasma_Associative_Ionization_Alkali_Alkaline` now has one training reaction and a tree that
   can match more than that one.** Its `A` root still admits `[Li,Na,K,H]`. One `Na + Mg` datum
   averaged up to Li, K and H is thin. Not changed here — narrowing it further is a judgement about
   the chemistry, not about the carry.

5. **`TwoTemperaturePlasma` training entries evaluate against the electron temperature; plain
   `Arrhenius` ones do not.** `Plasma_Electron_Impact_Dissociation` uses the former, correctly. The
   four `(0, 1)` families use plain `Arrhenius`, so their rates are evaluated at the **gas**
   temperature. For associative ionisation, which is heavy-particle driven, that is right. For
   `Plasma_Collisional_Ionization` it is also right — it is explicitly the heavy-particle channel,
   with the electron-impact case delegated elsewhere. Recorded so the distinction is not
   re-litigated.

6. **Nothing here has been run in a reactor.** This ticket verifies loading, placement, refusal and
   database consistency. Whether these families generate sensible reactions, and whether the rates
   behave in `PlasmaReactor`, is not measured — that is the next ticket.

---

## 8. The library entries that could not be carried

Every one of these exists on branch `99` and is blocked by §3.4 alone — the species all parse, the
rates are all present. They return as soon as `KineticsLibrary.load_entry` accepts an `electrons=`
argument.

#### PlasmaAir — 51 entries not carried

| reaction as written on `99` | shape (e- in, e- out) |
|---|---|
| `N + O <=> NOp + e-` | (0, 1) |
| `O + O <=> O2p + e-` | (0, 1) |
| `N + N <=> N2p + e-` | (0, 1) |
| `O + e- => Op + e- + e-` | (1, 2) |
| `N + e- => Np + e- + e-` | (1, 2) |
| `Op + e- <=> O` | (1, 0) |
| `Np + e- <=> N` | (1, 0) |
| `O2 + N2 => NO + NOp + e-` | (0, 1) |
| `O2 + e- => O2p + e- + e-` | (1, 2) |
| `H + e- => Hp + e- + e-` | (1, 2) |
| `H2 + e- => H2p + e- + e-` | (1, 2) |
| `OH + e- => OHp + e- + e-` | (1, 2) |
| `H2O + e- => H2Op + e- + e-` | (1, 2) |
| `O2s + e- => O2p + e- + e-` | (1, 2) |
| `H2p + e- <=> H + H` | (1, 0) |
| `H3p + e- => H + H + H` | (1, 0) |
| `H3p + e- <=> H2 + H` | (1, 0) |
| `O2p + e- <=> O + Os` | (1, 0) |
| `O2p + e- <=> Os + Os` | (1, 0) |
| `OHp + e- <=> O + H` | (1, 0) |
| `H2Op + e- <=> OH + H` | (1, 0) |
| `H2Op + e- <=> O + H2` | (1, 0) |
| `H2Op + e- => O + H + H` | (1, 0) |
| `H3Op + e- => OH + H + H` | (1, 0) |
| `H3Op + e- => O + H2 + H` | (1, 0) |
| `H3Op + e- <=> OH + H2` | (1, 0) |
| `H3Op + e- <=> H2O + H` | (1, 0) |
| `HO2p + e- <=> O2 + H` | (1, 0) |
| `O2 + e- <=> O- + O` | (1, 0) |
| `H2O + e- <=> OH + H-` | (1, 0) |
| `H2 + e- <=> H- + H` | (1, 0) |
| `O2s + e- <=> O- + O` | (1, 0) |
| `H2O + e- <=> H2 + O-` | (1, 0) |
| `H2O + e- <=> OH- + H` | (1, 0) |
| `H- + e- => H + e- + e-` | (1, 2) |
| `H- + O <=> OH + e-` | (0, 1) |
| `H- + O2 <=> HO2 + e-` | (0, 1) |
| `OH- + O <=> HO2 + e-` | (0, 1) |
| `OH- + e- => OH + e- + e-` | (1, 2) |
| `O- + O2s <=> O3 + e-` | (0, 1) |
| `O- + H <=> OH + e-` | (0, 1) |
| `OH + e- <=> OH-` | (1, 0) |
| `O2 + e- <=> O2-` | (1, 0) |
| `CH + O <=> CHOp + e-` | (0, 1) |
| `Ar + e- => Arp + e- + e-` | (1, 2) |
| `He + e- => Hep + e- + e-` | (1, 2) |
| `Ne + e- => Nep + e- + e-` | (1, 2) |
| `Hp + e- => H` | (1, 0) |
| `Hep + e- => He` | (1, 0) |
| `Hep2 + e- => Hep` | (1, 0) |
| `N2 + e- => N2p + e- + e-` | (1, 2) |

#### PlasmaAlkali — 14 entries not carried

| reaction as written on `99` | shape (e- in, e- out) |
|---|---|
| `Lip + e- <=> Li` | (1, 0) |
| `Nap + e- <=> Na` | (1, 0) |
| `Kp + e- <=> K` | (1, 0) |
| `LiH2Op + e- <=> Li + H2O` | (1, 0) |
| `NaH2Op + e- <=> Na + H2O` | (1, 0) |
| `KH2Op + e- <=> K + H2O` | (1, 0) |
| `CaOHp + e- <=> Ca + OH` | (1, 0) |
| `CaOHp + e- <=> CaO + H` | (1, 0) |
| `Li + e- => Lip + e- + e-` | (1, 2) |
| `Na + e- => Nap + e- + e-` | (1, 2) |
| `K + e- => Kp + e- + e-` | (1, 2) |
| `Mg + e- => Mgp + e- + e-` | (1, 2) |
| `Si + e- => Sip + e- + e-` | (1, 2) |
| `Mgp2 + e- <=> Mgp` | (1, 0) |


---

## 9. Reproducing this

```bash
cd /home/alon/Code/RMG-Py-i154-carry-chemistry
export PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH
export PYTHONPATH=/home/alon/Code/RMG-Py-i154-carry-chemistry:$PYTHONPATH
python /home/alon/Code/RMG-database-i154-carry-chemistry/docs/i154-carry-chemistry/verify_i154.py
python -m pytest test/rmgpy/molecule -q --no-header
```

The verifier prints the resolved `database.directory` and `rmgpy` path first, then checks: every
carried owner LOADS with the entry counts above; every electron-bearing owner declares PLACEMENT
matching the shape read off its own entries, and every electron-free owner declares none; an
undeclared owner is still REFUSED by name with `ElectronPlacementError`; and the kinetics DATABASE
loads with and without the plasma families.
