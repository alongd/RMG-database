# I-123, fourth pass — the database half of the pair

The RMG-Py half of this pass, its measurements and its verdict, are in the RMG-Py worktree at
`docs/i123d-audit.md` on branch `i123d-audit`. This note records what happened on **this**
repository, so that the pair is legible from either side.

**The RMG-Py verdict is NOT READY**, on a blocking failure that lives entirely on the RMG-Py side:
RMG's own seed mechanism does not preserve a reaction's owner, the electron-placement declaration
is keyed on that owner, and so a plasma model cannot be restarted from the seed RMG writes for it.
**Nothing in this repository causes it and nothing here can fix it.** See the last section.

## The branch

`i123d-audit-db` is at `d7c8595ce` and is **content-identical to the third pass's
`i123c-audit-db`** — the same tree and the same tip:

```
$ git log --oneline i123c-audit-db..HEAD ; git log --oneline HEAD..i123c-audit-db
(both empty)
```

**Nothing was merged into it this pass, and that is a measurement rather than an omission.** The
repair the fourth pass exists to integrate — the units-pairing fix `i145-units-laundering` and its
`VoronovEIArrhenius` sibling — is an RMG-Py change with **no database half**: no `i145-*` branch
exists in this repository, and no shipped rate value moves because of it. The rate laws in
`PlasmaElectronImpactIonization` and `PlasmaRadiativeRecombination` are declared in
`cm^3/(molecule*s)`, which is the spelling the old and the repaired code handle identically; the
defect only bit a rate law declared in metres, which no entry here is.

```
$ git log --oneline --graph plasma..HEAD
* d7c8595ce Record the database half of the I-123 third audit
* 2d7123b08 Give argon a sourced cation thermochemistry, and audit the gap it came from
*   c7bd96292 Merge i119-recombination: give radiative recombination a library owner
|\
| * aabc3c622 docs: report on the electron loss channels
| * 9ee5042d1 test: pin the recombination path from load to reactor acceptance
| * 9325c2d27 kinetics: give radiative recombination a library owner
* | 1fb224371 Merge i114-ionisation-declaration: give electron-impact ionisation a library owner
|\|
| * fcd87ce6e docs: record that the placement declaration landed
| * 277a0e333 test: pin the ionisation path from load to reactor acceptance
| * 6862c21c5 kinetics: give electron-impact ionisation a library owner
| * bdbbf2864 test: pin database.directory for the suites in this repository
*   ac944618e Merge i104-alkali-plasma: inventory the alkali-plasma cation source and loss network
|\
| * fc7bc101b docs: inventory the alkali-plasma cation source and loss network
*   79320d363 Merge i103-electrochem-provenance: diagnose the Cation_R_Recombination Marcus provenance
|\
| * 069ea3d0b docs: diagnose the Cation_R_Recombination Marcus provenance
* 3b61056c1 Merge i111-sei-reclassification: reclassify Cation_R_Recombination as a legacy SEI family
* 1fcbb80fa docs: report on the SEI reclassification
* aaa97074c test: pin the SEI reclassification and its plasma exclusion
* 03b96a974 kinetics: reclassify Cation_R_Recombination as a legacy SEI family
* 7d4f47d3a kinetics: quarantine the Cation_R_Recombination Marcus data
```

Twenty commits ahead of `plasma`. All **five** merges' second parents equal their branch tips,
read from git rather than asserted — `3b61056c1` is a merge too, though the graph renders it flat
because its first parent is `fb3c13c60` itself:

| merge | second parent | branch tip |
|---|---|---|
| `c7bd96292` | `aabc3c622` | `i119-recombination` `aabc3c622` |
| `1fb224371` | `fcd87ce6e` | `i114-ionisation-declaration` `fcd87ce6e` |
| `ac944618e` | `fc7bc101b` | `i104-alkali-plasma` `fc7bc101b` |
| `79320d363` | `069ea3d0b` | `i103-electrochem-provenance` `069ea3d0b` |
| `3b61056c1` | `1fcbb80fa` | `i111-sei-reclassification` `1fcbb80fa` |

**Two branches in this repository are deliberately outside the union**, and neither is an ancestor
of anything here: `i129-lithium-cation-enthalpy` (`75e0cb6f0`) and `i120-argon-recombination`
(`5f52259f6`).

## The baseline

This repository has **no** local/remote divergence, unlike RMG-Py, and the position is unchanged
from the third pass:

```
$ git rev-list --count origin/plasma..plasma ; git rev-list --count plasma..origin/plasma
0
0
```

Both are `fb3c13c60`. Every database number in the RMG-Py report is taken against that.

## The suites

`python -m pytest test` from this repository root, paired with the matching RMG-Py tree, each
worktree pinned at its own `database.directory`:

| tree | failed | passed |
|---|---|---|
| this branch `d7c8595ce` + the RMG-Py union | **4** | **173** |
| local `plasma` `fb3c13c60` + RMG-Py `plasma` | **4** | **41** |

`4 failed, 173 passed, 284 warnings in 22.96s` and `4 failed, 41 passed in 1.04s`. The same four
failures on both, all in `test/test_plasma_electron_attachment.py`:
`test_trained_species_resolve_to_their_own_rate_through_their_own_node[O2|OH|O]` and
`test_o2_rate_comes_from_the_training_set_not_a_library`. Pre-existing on the shared branch,
identical on both bases, untouched by this union. Reproduces the third pass exactly.

Run as-is the **baseline** suite does not fail but errors at fixture setup, resolving
`database.directory` to the sibling `RMG-database` — the polymer-branch database. The baseline has
no `test/conftest.py`; this branch does, because `bdbbf2864` is one of the merges under audit. The
baseline figure above was taken with an equivalent `rmgrc` written at that detached worktree's root,
as passes 1 and 3 also had to. **That pin is a union improvement**, and it is the difference between
a suite that measures its own tree and one that silently measures another's.

## What this branch still carries wrong

The lithium cation's enthalpy, measured on this tree rather than inherited:

```
LithiumPrimaryThermo :: entry '[Lip]' index=65
    H298      = 532.936 kJ/mol
    E0        = 526.738 kJ/mol
    shortDesc = []          <- empty: no provenance recorded
```

against a reference `dfH(Li+,g) = dfH(Li,g) + IE(Li) = 159.3 + 520.2 = 679.5 kJ/mol` — a gap of
**146.6 kJ/mol (1.52 eV)** low. The branch that diagnosed it, `i129-lithium-cation-enthalpy`
(`75e0cb6f0`), is **not** merged here, so the union carries the old value unchanged from the third
pass. Non-blocking only because both reactions in the shipped deck are irreversible, so no `Keq` is
formed from it; it would matter to any reversible cation chemistry and to any equilibrium
composition.

The lithium and cation thermo libraries this database offers, measured: `LithiumPrimaryThermo`,
`LithiumAdditionalThermo`, `PlasmaCationThermo`.

## What the RMG-Py blocker means for this repository

Nothing to change here, but worth recording so the next pass does not go looking for it on this
side.

The electron-placement declaration lives in RMG-Py (`rmgpy/electron_placement.py`) and is keyed on
the **owner label** — which, for the two channels this repository supplies, is the kinetics
library's own name. **This repository's contribution is correct and was re-measured this pass**:
`PlasmaElectronImpactIonization` and `PlasmaRadiativeRecombination` are exactly the two labels the
registry declares, one entry each, and both were driven through loading, charge balancing, placement
resolution and reactor acceptance, then through a generated model and a written Chemkin file.

The blocker is that a **serialisation** on the RMG-Py side — the seed mechanism RMG writes for every
run — renames the library to `seed`/`restart` and so drops the key. A database-side change could not
prevent that, and the plausible fix (record the originating owner on the entry, and decide what a
registry keyed one-placement-per-owner means for a library that holds many) is entirely an RMG-Py
decision. It is the same structural obstruction as the strict-`xfail` landmine that stops one
library carrying both charge channels — which is why the campaign's workaround here, **two libraries
rather than one**, remains the right shape for this repository.

## Gates

Nothing was merged into `plasma` in this repository, nothing was pushed, and no pull request was
opened.
