# PlasmaAir carry — re-measured against the current mainline

Branch: `i158-plasmaair`. Worktree: `/home/alon/Code/RMG-database-i158-plasmaair`.
Engine under test: `/home/alon/Code/RMG-Py-plasma` (branch `plasma`, tip `a3b42f89f`),
which already carries the charge-based balance rule (`rmgpy/reaction.py:1792 is_balanced`,
which judges the free electron by charge, not by a per-element census) and the argon atom
types `Ar0 / Ar+ / Ar++` (`rmgpy/molecule/atomtype.py:436`).

## The merge — the point of the exercise

Before the merge this branch (tip `803d7a2f2`) was cut from `053d48080`, 17 commits behind
and 6 ahead of the mainline `origin/plasma`.

- **Mainline merged:** `origin/plasma` = `c833590ec` ("Merge i210-baseline…"), authored
  2026-09-04.
- **Merge commit:** `212b3238e`, made 2026-09-05. Clean, no conflicts. The mainline does
  **not** touch `input/kinetics/libraries/PlasmaAir/`; it adds new families
  (`Plasma_Electron_Impact_Ionization`, `Plasma_Radiative_Recombination`), the `PlasmaArgon`
  library, docs, and edits to some shared `test/` files, all auto-merged.

**Did anything I measured change across the merge? No.** Every PlasmaAir measurement is
identical before and after:

| measurement | pre-merge (`803d7a2f2`) | post-merge (`212b3238e`) |
|---|---|---|
| `grep -c '^entry('` PlasmaAir/reactions.py | 89 | 89 |
| `test_plasma_air_noble_gas_ionization.py` | 4 passed | 4 passed |

The "world that no longer exists" concern is real for the base but inert for this payload:
the PlasmaAir entries were already carried on this branch (commit `d7d7ef68a`), and the test
runs against `RMG-Py-plasma`, which already had the charge-based rule before the merge. The
merge moved the *base* forward; it did not move any PlasmaAir number.

## Q1 — Does the carried library load, now? Yes.

Under the current engine (charge-based balance, argon atom types) the library loads and every
target reaction both loads and balances. Direct load + `is_balanced()` check against this
worktree's `input/`:

```
Ar + e- => Arp + e- + e-   is_balanced=True   charge L=-1 R=-1   ElectronCollisionPlasma
He + e- => Hep + e- + e-   is_balanced=True   charge L=-1 R=-1   ElectronCollisionPlasma
Hep + e- => He             is_balanced=True   charge L=0  R=0    TwoTemperaturePlasma
Hep2 + e- => Hep           is_balanced=True   charge L=1  R=1    TwoTemperaturePlasma
```

The full `databaseTest.py` (see Verifier 4) also loads the entire database with
`kinetics_families="all"` — including the two new plasma families the merge introduced — and
passes.

## Q2 — Is the number 89 or 94? It is 89, and that is correct under the current mainline.

89 = 94 carried live from branch `99` − 5 that commit `803d7a2f2` (I-176) commented out.
The 5 are every reaction referencing `H3p`:

```
H3p + e- <=> H2 + H
H3p + e- => H + H + H
H3p + H- <=> H2 + H2
H3p + OH- <=> H2 + H2O
H3p + O- <=> OH + H2
```

`H3p` in `PlasmaAir/dictionary.txt` is the disconnected van der Waals graph `[H][H].[H+]`
(an H₂ with a bare `c+1` H⁺, no bond between them). RMG cannot give this species
non-fabricated thermochemistry: group additivity fabricates 0.0, and the connectivity trips
the linearity path. **The condition that holds:** the thermochemistry is *not* available.
I confirmed no thermo library on the merged mainline defines it — a scan of
`input/thermo/libraries/` for `H3+ / H3p` returns only false positives (`[NH3+]`,
`ToluenePlus…`, `[O-][NH3+]`), and the merge added no thermo library for it. The specific
missing species is therefore `H3p` = `[H][H].[H+]`. The 5 entries correctly stay commented.

Branch `99` itself carries these 5 as **live** entries; commenting them is this branch's own
call (I-176), not inherited. That call remains correct under the current mainline, so 89 — not
94 — is the right number.

## Q3 — Does the argon ionisation network work? Yes.

All four payload reactions are live, load with the rate parameters they carry, and balance
under the charge rule (the `is_balanced` table above). Details from `PlasmaAir/reactions.py`:

- **idx 86** `Ar + e- => Arp + e- + e-` — `ElectronCollisionPlasma`, Golyatina2021 cross
  section, threshold 15.759 eV. (An older LXCat version at 15.8 eV sits **commented**
  directly above it, deliberately superseded — this is one of branch `99`'s 10 commented
  entries, carried as-is.)
- **idx 87** `He + e- => Hep + e- + e-` — `ElectronCollisionPlasma`, Golyatina2021,
  threshold 24.587 eV.
- **idx 92** `Hep + e- => He` — `TwoTemperaturePlasma` (He⁺ recombination).
- **idx 93** `Hep2 + e- => Hep` — `TwoTemperaturePlasma` (He²⁺ → He⁺).

Note the brief cites the argon threshold as 15.8 eV; the *live* carried value is Golyatina's
15.759 eV. The 15.8 eV number is the superseded LXCat entry, which is commented out.

## The label convention (`p`, not bare `+`)

Every live label uses the `p` suffix for cations; a scan of all live labels finds **no** bare
`+` used as anything but a ` + ` separator. The convention is intact — no defect to report.

## Commented entries and why (full enumeration)

Total entry blocks are conserved across the carry: branch `99` = 94 live + 10 commented = 104;
this branch = 89 live + 15 commented = 104. Exactly 5 moved live → commented.

**Branch 99's 10 commented, carried as-is (labels shown with the `p` convention applied):**

| label | reason (inherited from branch 99) |
|---|---|
| `Ar + e- => Arp + e- + e-` | superseded LXCat version of the live Golyatina idx-86 reaction |
| `H2 + e- => Hp + H + e- + e-` | dissociative ionisation, held on branch 99 |
| `H2O + e- => Hp + OH + e- + e-` | dissociative ionisation, held on branch 99 |
| `H2O + e- => Op + H2 + e- + e-` | dissociative ionisation, held on branch 99 |
| `H2O + e- => OHp + H + e- + e-` | dissociative ionisation, held on branch 99 |
| `Kr + e- => Krp + e- + e-` | krypton — outside the Ar/N/O scope |
| `Xe + e- => Xep + e- + e-` | xenon — outside the Ar/N/O scope |
| `NO <=> N + O` | third-body dissociation, held on branch 99 |
| `O2 <=> O + O` | third-body dissociation, held on branch 99 |
| `O2 + e- => Op + O + e- + e-` | dissociative ionisation, held on branch 99 |

**This branch's 5 additional commented (I-176):** the `H3p` reactions listed under Q2 —
no non-fabricated thermochemistry for `[H][H].[H+]`.

## Verifiers

1. **RED-first — the non-event, recorded as evidence about method.** The payload test
   `test/test_plasma_air_noble_gas_ionization.py` (4 tests, incl. `Ar + e- => Arp + e- + e-`
   with the branch-99 cross section) **passed both pre-merge and post-merge**; it **never had a
   red state, and I declined to manufacture one.** This sentence is load-bearing: it says how the
   green was obtained. There is no red because the entries were already carried on this branch
   (commit `d7d7ef68a`) and the engine (`RMG-Py-plasma`) already judged balance by charge before
   the merge, so nothing the merge did could turn this test red. Fabricating a red — e.g. by
   pointing the test at an older engine — would have been theatre, not evidence, so it was not
   done. (Run: `PYTHONPATH=/home/alon/Code/RMG-Py-plasma python -m pytest
   test/test_plasma_air_noble_gas_ionization.py` → `4 passed`.)
2. **Entry count:** the justified number is **89** (94 carried − 5 H3p with no thermo, Q2).
   `grep -c '^entry(' input/kinetics/libraries/PlasmaAir/reactions.py` → `89`.
3. **Normalised label set — the corrected predicate, which holds exactly.** The brief asked for
   a strict superset of branch 99's live labels. That predicate is wrong for this carry, and the
   correct one is provable and holds:

   > **The current live label set = branch 99's live label set, MINUS the 5 deliberately-
   > commented H3p reactions, WITH entry 24 relabelled for its owner-approved charge fix.**

   That equality is exact — no other label is added, dropped, or altered. This is not a failed
   check; it is the right check, and it passes. (The strict-superset framing would only have been
   correct for a carry that commented nothing and corrected nothing; this one deliberately does
   both, so the predicate is corrected here in the artifact rather than worked around.)

   Normalisation used: split each label on the arrow (`=>` / `<=>`, preserving reversibility),
   split each side on ` + `, replace `+`→`p` within each species token (so `Ar+`→`Arp`,
   `He+2`→`Hep2`), and sort species within each side to absorb product-ordering differences. The
   two accounted-for differences:
   - the **5 H3p** reactions (commented per Q2); and
   - **entry 24**: branch 99's `N2+ + N2 => N2 + N + N` (charge +1 → 0, *unbalanced*) was
     corrected on this branch to `N2p + N2 => N + Np + N2` (charge +1 → +1, balanced) —
     commit `49bc0114b`, on the owner's ruling. The label changed because a product species
     changed (`N` → `Np`); it is the same reaction, corrected, not a lost label.
   Every one of branch 99's other 89 live labels is present verbatim (modulo the `p` convention).
4. **`databaseTest.py` — full provenance, so this reproduces in three months.** This campaign has
   already measured the *wrong* database once by getting exactly this resolution wrong, so the
   recipe is recorded in full, not by reference to an ephemeral path.

   - **Where the test lives:** the canonical `databaseTest.py` was **removed from RMG-database in
     commit `190ebafc7`** and now lives in **RMG-Py**. There is no `test/database/databaseTest.py`
     in this repo; the one run is
     `/home/alon/Code/RMG-Py-plasma/test/database/databaseTest.py`.
   - **The resolution trap:** the test reads `settings['database.directory']`, which RMG resolves
     from the first `rmgrc` it finds — **CWD first**, then `~/.rmg/rmgrc`, then `rmgpy/rmgrc`. The
     `rmgrc` sitting in `RMG-Py-plasma/`'s own directory points at the shared
     `/home/alon/Code/RMG-database-plasma/input`. Running with that as CWD would silently measure
     the **shared** database, not this worktree.
   - **How this run avoided it:** pytest was invoked from a dedicated rundir
     (`<scratch>/dbtest_run`) that contained a single-line `rmgrc`:

     ```
     database.directory = /home/alon/Code/RMG-database-i158-plasmaair/input
     ```

     To reproduce, `mkdir` any empty dir, drop that one-line `rmgrc` in it, and run pytest **from
     that dir** so its CWD `rmgrc` wins.
   - **Verified before the run:** from that rundir,
     `python -c "from rmgpy import settings; print(settings['database.directory'], settings.sources['database.directory'])"`
     printed `/home/alon/Code/RMG-database-i158-plasmaair/input  from rmgrc` — i.e. **this**
     checkout, `source = from rmgrc`, not the shared path.
   - **Result:** `PYTHONPATH=/home/alon/Code/RMG-Py-plasma python -m pytest
     /home/alon/Code/RMG-Py-plasma/test/database/databaseTest.py` → **6 passed** in 726 s
     (12:06), exit 0. Engine: `RMG-Py-plasma`@`a3b42f89f`; conda env `rmg_env`, Python 3.9.

## What I could not determine

- **Whether `H3p` could be rescued with real thermo, not whether the mainline supplies it.**
  I established that no thermo library on the merged mainline defines `[H][H].[H+]` and that GA
  fabricates it — so under the mainline *as it stands* the entries stay commented. I did **not**
  establish whether a citable H₃⁺ thermochemistry exists in the literature that could be entered
  as a library value to bring the 5 entries back; that is an open sourcing question, not a
  measurement of this branch.
- **Runtime behaviour beyond load + balance.** I verified the argon network loads, carries its
  rate parameters, and passes `is_balanced()` and the full `databaseTest.py`. I did **not** run
  an RMG job that actually integrates the 5-torr argon bath and exercises these rates in a
  mechanism — "works" here means loads, balances, and passes the database suite, not
  "produces a converged simulation."
