# I-193 — Argon gets its own reaction library, and the air library comes off the argon deck

**A new one-entry reaction library `PlasmaArgon` carries the single argon reaction the
database holds. The 5 torr argon deck now loads it instead of the whole `PlasmaAir` air
library.** The argon-only run gets further than first-light did — past every air-ballast
wall — and stops at a *new*, argon-intrinsic wall: RMG cannot generate a reverse rate for
the `ElectronCollisionPlasma` cross-section law during its final model check. That is the
honest edge of the sourced data made visible: argon here can be ionised, and the machinery
that would un-ionise it does not yet exist.

**Runtime** `/home/alon/Code/RMG-Py-argonrun` at `1630944f0` (built, 104 `.so`, not rebuilt).
**Database** `/home/alon/Code/RMG-database-i193-plasmaargon` at base `d9fb68fac`.
**rmgrc** repointed from `/home/alon/Code/RMG-database-i186-firstlight/input` to
`/home/alon/Code/RMG-database-i193-plasmaargon/input`; prior value backed up to this
session's scratchpad (`rmgrc.before-i193.bak`). `rmgrc` is git-ignored by design.

Evidence tags: **[M]** measured (command + output shown) · **[R]** code (file:line) ·
**[D]** database file.

---

## What was built

`input/kinetics/libraries/PlasmaArgon/` — dictionary (`Ar`, `Arp`, `e-`) and one reaction
entry:

```
Ar + e- => Arp + e- + e-      ElectronCollisionPlasma, shortDesc [Golyatina2021]
```

This is the **active** argon ionisation entry from `PlasmaAir` index 86 (~line 1242),
carried **verbatim** — energies grid, sigma grid, `shortDesc`, `longDesc` unchanged. **[M]**
The 51-point energy grid and 51-point cross-section grid are byte-for-byte identical to
`PlasmaAir`'s (`diff` of the exact lines returned no difference).

**Provenance note — two datasets, one chosen.** `PlasmaAir` carries *two* datasets for this
one reaction. The one copied is the active Golyatina2021 entry (51-point cross-section grid,
threshold 15.759 eV). Alongside it, `PlasmaAir` holds a **commented-out** older entry
(~line 1219, `[LXCat]` / Phelps, 29-point grid, threshold 15.8 eV) — a coarser, superseded
dataset for the same process. It was **not** copied or un-commented; only the finer active
grid is here. Both facts are recorded in the new library's `longDesc` and pinned by
`test/test_plasma_argon.py::test_it_is_the_golyatina_grid_not_the_superseded_lxcat_grid`.

**Two modelling facts the entry carries** (now in the `longDesc`):

- It is a **cross-section table**, not a fitted rate. `ElectronCollisionPlasma` integrates
  the tabulated σ(E) against a **Maxwellian** electron energy distribution at Te
  (`rmgpy/kinetics/arrhenius.pyx`, `integrate_rate_coefficient`). The Maxwellian EEDF is a
  deliberate modelling choice, not an accident — a real low-pressure discharge EEDF is
  generally non-Maxwellian.
- RMG has **no LXCat (or any cross-section) file parser**. A σ(E) table enters the database
  only by being hand-written into a library entry — which is exactly why copying verbatim,
  not re-deriving, is the correct move: there is no import path to lean on, and re-typing
  would be an opportunity to corrupt the numbers.

**Why one entry, and why that is the deliverable.** Radiative recombination, dissociative
recombination, Ar₂⁺, and three-body channels are all deliberately absent — none is citable
without fabrication (see Verifier 3 and the non-goals). An incomplete library that can be
named is the deliverable; a complete-looking one would be a failure.

---

## Verifier scorecard

### 1. Before-state reproduced — **PASS**

**[M]** The deck *as it stood* (original, with `PlasmaAir`) run against this database:

```
Moved 1 reactions from edge to core
    The model core has 3 species and 1 reactions
    The model edge has 33 species and 88 reactions
```

then it crashed at exit 1 in the Chemkin writer on the I-190 anion charge-flip
(`e-(1) + O2(12) <=> O(8) + Op(15)` E-imbalance) — reproducing first-light exactly.
**33 edge species, 88 edge reactions**, measured here, not cited.

### 2. Every entry carries its original citation — **PASS**

One entry, copied verbatim from `PlasmaAir` 86, `shortDesc [Golyatina2021]`, with the full
reference (Golyatina & Marinov, *Atoms* 2021, 9(90), DOI 10.3390/atoms9040090) in the
library `longDesc`. No entry exists whose source cannot be named.

### 3. The Ar⁺ recombination question, answered by measurement — **ANSWERED: NO**

**Ar⁺ radiative recombination is NOT in `PlasmaRadiativeRecombination`.**

**[D]** That library's `dictionary.txt` holds only `[Lip]`/`[Li]`; its single entry is
`[Lip] => [Li]` (`BadnellRRArrhenius(Z=3, N=2)`). **[M]** Grepping the library for any argon
species returns only prose — its own `longDesc` states it outright: *"Argon has no
radiative-recombination fit here at all … `badnell.yaml` carries no `Z = 18, N = 17` stage —
the table's cation-to-neutral stages stop at Z = 12."* Ar⁺ is a Cl-like ion (17 electrons),
which the systematic Badnell (2006) radiative-recombination programme never reached.

**Prior art, read and disambiguated.** Branch `i120-argon-recombination` (`5f52259f6`) carries
a 697-line study of exactly this question. **[M]** `git merge-base --is-ancestor HEAD plasma`
→ **NO** (never merged), and its own headline is "the argon rate … was deliberately not
entered." It found a citable Ar⁺ + e⁻ → Ar fit (CHIANTI `ar_2.rrparams`, six-parameter
Badnell/Gu form) but established it must **not** be entered: its validity range in Te cannot
be sourced, so it could only ship as a rate usable at any Te with no bound. It is also the
wrong channel by ~5 orders of magnitude and the runaway it guards against does not occur at
the 1 eV working point. So `PlasmaArgon` correctly contains **no** recombination: the answer
changed nothing about what the library must hold.

### 4. The deck runs — reported exactly (a failing run is a valid result) — **REPORTED**

The edited deck (`PlasmaArgon`, no `PlasmaAir`, `generatedSpeciesConstraints` deleted):

- **True exit code: 1.** Captured from the python process (`EXIT=$?` immediately after the
  interpreter = 1). The task wrapper reported "[exited with code 0]" — that is bash's exit
  after a trailing `echo`, which masks python's status; the real value is 1, from an uncaught
  exception.
- **`MODEL GENERATION COMPLETED` — did NOT appear.** **[M]** 0 occurrences in both
  `stdout.log` and `RMG.log`. **[R]** RMG logs that line only *after* `self.check_model()`
  (`rmgpy/rmg/main.py:1415`→:1418); the crash is *inside* `check_model()`, so the line is
  never reached. Model *generation* did finish ("At time 1.0000e-03 s, reached target
  termination time") and Chemkin files were written — but the run did not complete.
- **Final counts:** core **6 species, 1 reaction**; edge **2 species, 2 reactions**.
- **The fatal, uncaught error** (`stderr.log`, propagated to `rmg.py` top level):

  ```
  rmgpy.exceptions.ReactionError: Unexpected kinetics type
  <class 'rmgpy.kinetics.arrhenius.ElectronCollisionPlasma'>; should be one of
  ('KineticsData', 'Arrhenius', 'SurfaceArrhenius', 'SurfaceChargeTransfer',
   'MultiArrhenius', 'PDepArrhenius', 'MultiPDepArrhenius', 'Chebyshev', 'ThirdBody',
   'Lindemann', 'Troe', 'StickingCoefficient', 'ArrheniusChargeTransfer')
  ```

  raised in `Reaction.check_collision_limit_violation` → `generate_reverse_rate_coefficient`,
  called from `check_model()`. The final model check tries to build a *reverse* rate for the
  argon ionisation and `ElectronCollisionPlasma` has no reverse-rate support. This is a NEW
  wall — argon-intrinsic, reached only because the air-ballast walls are gone. **Not chased
  into a fix.**
- **A second, non-fatal failure** was recorded first: Cantera `ck2yaml` cannot parse the
  exported `Ar(2)+e-(1)=>Arp(3)+e-(1)+e-(1)` TDEP line ("could not convert string to float:
  'e-(1)'"). **[R]** It is caught at `main.py:1409` (logged, appended to `export_failures`),
  so it did not stop the run — `check_model()` did.

- **`chemkin/chem.inp` (core), verbatim:**

  ```
  SPECIES
      He   Ne   N2   e-(1)   Ar(2)   Arp(3)
  END

  REACTIONS    KCAL/MOLE   MOLES
  Ar(2)+e-(1)=>Arp(3)+e-(1)+e-(1)          2.981e+13 0.597     361.244
      TDEP/e-(1)/   ! ElectronCollisionPlasma exported as a modified-Arrhenius fit of
                    ! k(Te) over 1.16e+04-1.16e+05 K; the original functional form is not
                    ! representable in Chemkin
  END
  ```

### 5. The edge is argon-only — **two readings, per the owner's ruling**

Full model inventory:

| where | species | reactions | provenance |
|---|---|---|---|
| core | `e-(1)`, `Ar(2)`, `Arp(3)` | `Ar + e- => Arp + e- + e-` | deck input species + **PlasmaArgon** |
| core | `He`, `Ne`, `N2` (non-reactive) | — | **RMG `main.py:724`**, unconditional bath gases |
| edge | `[Li](4)`, `[Lip](5)` | `Li + e- => Lip + e- + e-`; `Lip + e- => Li` | **PlasmaElectronImpactIonization**, **PlasmaRadiativeRecombination** |

- **Literal reading** ("no nitrogen/oxygen/hydrogen/carbon species anywhere") — **FAIL**:
  `N2` is present. But the premise behind that wording — that any N₂ would come from
  `PlasmaAir` — is false.
- **Revised reading** (owner's ruling: no species and no reaction traceable to the
  `PlasmaAir` *library* reaches core or edge; RMG's unconditional non-reactive bath gases
  Ar/He/Ne/N2 are exempt) — **PASS**: there is **no O/H/C-bearing species, no charged air
  species, and no reaction of `PlasmaAir` provenance** anywhere in the model. Every one of
  `PlasmaAir`'s 33 air species (O, O₂, OH, NO, CO, CH, H₂O, O₃, …) is gone. `He`/`Ne`/`N2`
  are RMG core behaviour (`main.py:724`); `[Li]`/`[Lip]` come from the two lithium libraries
  the deck was told to keep, not from air.

### 6. `databaseTest` passes, baseline and after — **PASS**

`python -m pytest test/database/databaseTest.py` against this runtime, both clean:

- **Baseline** (PlasmaArgon absent, library moved aside for the whole run):
  **`6 passed in 528.40s`, exit 0**.
- **After** (PlasmaArgon present): **`6 passed in 755.45s`, exit 0**. `test_kinetics` — which
  iterates every reaction library and checks adjacency lists, rate units and rate
  reasonableness — passed with `PlasmaArgon` loaded.

(An earlier baseline attempt reported exit 1 despite `6 passed`: the database-pollution guard
detected the `PlasmaArgon` files I restored *mid-run* for a parallel deck run. A test-harness
artifact of my file-move, not a validation failure; re-run clean, it is exit 0.)

`test/test_plasma_argon.py` (new, 6 tests) pins the library invariants: **`6 passed`**.

---

## The deck change

`/home/alon/Code/RMG-Py-argonrun/docs/i186-ar5torr-firstlight/input.py`
(`+10 / −33`, uncommitted — the runtime branch is held for the owner's merge):

- `reactionLibraries`: `PlasmaAir` removed, `PlasmaArgon` added;
  `PlasmaElectronImpactIonization` and `PlasmaRadiativeRecombination` kept (as instructed).
- The whole `generatedSpeciesConstraints(...)` block deleted (its `allowed=[...]` and
  `allowSingletO2=True` existed only to tolerate the air library), restoring RMG's default
  constraints in full.

This edit is **not committed** — the runtime worktree sits on a held integration branch. It
is preserved in this session's scratchpad (`run-after/input.py`).

---

## Findings

1. **The argon-only run's wall moved from the air library to argon itself.** First-light
   (with `PlasmaAir`) died in the Chemkin writer on an air anion (I-190). This run gets past
   generation and Chemkin export and dies in `check_model()` →
   `check_collision_limit_violation` → `generate_reverse_rate_coefficient`, which has no
   branch for `ElectronCollisionPlasma`. **The reverse-rate/collision-limit check does not
   support the plasma cross-section rate law.** Owner: RMG-Py. Reported, not fixed.

2. **RMG injects N₂ (and He, Ne) into every model, unconditionally.** `rmgpy/rmg/main.py:724`
   adds Ar, He, Ne, N₂ as non-reactive bath gases "since RMG-Java does." Harmless for
   kinetics — they carry no reactions and enter at zero concentration — but for a mechanism
   we intend to *publish*, an inert nitrogen diluent nobody asked for in a pure-argon plasma
   is not nothing. Worth an owner's eye whatever else happens.

3. **Keeping the two lithium libraries puts Li/Li⁺ on the edge.** `PlasmaElectronImpactIonization`
   and `PlasmaRadiativeRecombination` (kept per the deck instruction) add `[Li]`/`[Lip]` and
   their two reactions to the edge. Inert here (the deck's `initialMoleFractions` name only
   Ar/Arp/e-), and not air chemistry, so they do not fail the revised Verifier 5 — but if a
   future argon deck wants a strictly argon+e⁻ edge, those two libraries are the remaining
   non-argon source.

4. **Cantera export cannot represent the exported plasma rate.** `generateCanteraYAML2=True`
   drives a `ck2yaml` pass that fails to parse the `TDEP/e-(1)/` argon line. Caught and
   non-fatal here, but the Cantera path has no representation for the electron-temperature
   rate law — the same limitation the Chemkin comment already annotates.

5. **`PlasmaAir` carries two datasets for the one argon ionisation reaction.** Active
   Golyatina2021 (51-point σ(E), 15.759 eV) and commented-out LXCat/Phelps (29-point,
   15.8 eV). Only the finer active one is in `PlasmaArgon`; recorded so the choice is on the
   record rather than silently resolved.

## Remaining work / not reached

- The argon reverse-rate wall (finding 1) is an RMG-Py matter; not opened here.
- No physical conclusion is drawn from the run — it exercises the machinery, it does not
  model an argon plasma.
- The deck edit is uncommitted by design (held runtime branch); the owner decides its home.
