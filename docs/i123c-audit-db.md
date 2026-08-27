# I-123, third pass — the database half of the pair

The RMG-Py half of this pass, its measurements and its verdict, are in the RMG-Py worktree at
`docs/i123c-audit.md` on branch `i123c-audit`. This note records what happened on **this**
repository, so that the pair is legible from either side.

## The branch

`i123c-audit-db` is content-identical to the second pass's `i123b-reaudit-db`, at `2d7123b08`.

**Nothing was merged into it this pass, and that is a measurement rather than an omission.** The
two repairs the third pass exists to integrate — the reaction-identity repair and the Chemkin
reader repair — are RMG-Py changes with **no database half**: no `i134-*` or `i135-*` branch exists
in this repository.

```
$ git log --oneline --graph plasma..HEAD
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

All five merges' second parents equal their branch tips, verified from git rather than asserted.

## The baseline

This repository has **no** local/remote divergence, unlike RMG-Py:

```
$ git rev-list --count refs/remotes/origin/plasma..plasma ; git rev-list --count plasma..refs/remotes/origin/plasma
0
0
```

Both are `fb3c13c60`. Every database number in the RMG-Py report is taken against that.

## The suites

`python -m pytest test`, paired with the matching RMG-Py tree:

| tree | failed | passed |
|---|---|---|
| this branch `2d7123b08` + the RMG-Py union | **4** | **173** |
| local `plasma` `fb3c13c60` + RMG-Py `plasma` | **4** | **41** |

The same four failures on both, all in `test/test_plasma_electron_attachment.py` and all one
assertion — `assert <KineticsDepository "Plasma_Electron_Attachment/training"> == 'rate rules'`.
Pre-existing on the shared branch, identical on both bases, untouched by this union.

Run as-is the **baseline** suite does not fail but errors at fixture setup 45 times, resolving
`database.directory` to `/home/alon/Code/RMG-database/input` — the polymer-branch database. The
baseline has no `test/conftest.py`; this branch does, because `bdbbf2864` is one of the merges
under audit. The baseline figure above was taken with an equivalent `rmgrc` written at the
repository root. **That pin is a union improvement**, and it is the difference between a suite that
measures its own tree and one that silently measures another's.

## What this branch still carries wrong

The lithium cation's enthalpy, measured on this tree rather than inherited:

```
LithiumPrimaryThermo :: entry '[Lip]' index=65
    H298 = 532.936 kJ/mol
    E0   = 526.738 kJ/mol
```

against a reference `dfH(Li+,g) = dfH(Li,g) + IE(Li) = 159.3 + 520.2 = 679.5 kJ/mol` — a gap of
**+146.6 kJ/mol (+1.52 eV)**. The branch that diagnosed it, `i129-lithium-cation-enthalpy`
(`75e0cb6f0`), is **not** merged here, so the union carries the old value. Non-blocking only
because both reactions in the shipped deck are irreversible, so no `Keq` is formed from it.

## Gates

Nothing was merged into `plasma` in this repository, nothing was pushed, and no pull request was
opened.
