# I-157 — carry the alkali ionisation and recombination network to full count

Branch `i157-plasmaalkali`, worktree `/home/alon/Code/RMG-database-i157-plasmaalkali`.
Engine under test: `/home/alon/Code/RMG-Py-plasma` (branch `plasma`, tip `a3b42f89f`),
conda env `rmg_env`, `PYTHONPATH=/home/alon/Code/RMG-Py-plasma`.

The carry adds fourteen entries to `input/kinetics/libraries/PlasmaAlkali/reactions.py`,
taking it 52 → 66. Each is byte-identical to `origin/99` apart from a single label line
translated into this line's `p`-suffix cation convention; the diff is 245 insertions,
0 deletions. The two sodium entries — the cation's source and sink — load with the rates
and units `origin/99` carries.

## The count I am claiming, and why

**66.** All fourteen missing live entries carry and load cleanly; none needs to stay
commented out. The premise that these could not be represented in a kinetics library on
this line — asserted by the here-file's own `CARRY-OVER PROVENANCE (I-154)` note and by
the sibling `PlasmaAir`'s "intended RED" status — was **falsified by measurement** (see
"Contradictions" below). `grep -c '^entry(' … reactions.py` → 66.

The fourteen, with the `origin/99` indices they retain:

| shape | count | entries (origin/99 index) |
|---|---|---|
| electron-impact ionisation `X + e- => Xp + e- + e-` | 5 | Li 38, Na 39, K 40, Mg 41, Si 42 |
| radiative recombination `Xp + e- <=> X` | 3 | Li⁺ 1, Na⁺ 2, K⁺ 3 |
| radiative recombination `Mgp2 + e- <=> Mgp` | 1 | Mg²⁺ 45 |
| hydrated dissociative recombination `XH2Op + e- <=> X + H2O` | 3 | Li 11, Na 12, K 13 |
| CaOH⁺ dissociative recombination | 2 | `CaOHp + e- <=> Ca + OH` 28, `CaOHp + e- <=> CaO + H` 33 |

## The sodium pair, side by side with `origin/99`

Carried verbatim; only the label spelling changed (`Na+` → `Nap`).

**Sink — radiative recombination (`origin/99` index 2):**

| | `origin/99` | this line |
|---|---|---|
| label | `Na+ + e- <=> Na` | `Nap + e- <=> Na` |
| kinetics | `TwoTemperaturePlasma` | `TwoTemperaturePlasma` |
| A | `2.72e-08 cm^3/(molecule*s)` | `2.72e-08 cm^3/(molecule*s)` |
| n | `-1.07` | `-1.07` |
| Ea_g | `0.0 J/mol` | `0.0 J/mol` |
| Ea_e | `0.25 kJ/mol` | `0.25 kJ/mol` |
| Tmin/Tmax | `10 / 1e9 K` | `10 / 1e9 K` |
| provenance | `[VernerFerland1996]` | `[VernerFerland1996]` |

`A.units` is preserved as the per-molecule spelling `cm^3/(molecule*s)`; its SI value is
`1.638e10 m^3/(mol*s)` (the numeral × Avogadro's number), which is exactly the
`molecule` → `mol` conversion the test pins.

**Source — electron-impact ionisation (`origin/99` index 39):**

| | `origin/99` | this line |
|---|---|---|
| label | `Na + e- => Na+ + e- + e-` | `Na + e- => Nap + e- + e-` |
| kinetics | `ElectronCollisionPlasma` | `ElectronCollisionPlasma` |
| energies | 52-pt grid, `eV/molecule`, threshold `5.14` | identical |
| sigma | 52-pt cross section, `m^2`, σ₀ = `0.0` | identical |
| reversible | `False` | `False` |
| provenance | `[Golyatina2021]` (threshold 5.139 eV) | `[Golyatina2021]` |

## RED → GREEN, verifier 1

`test/test_plasma_alkali_sodium_pair.py` loads `PlasmaAlkali` from the pinned worktree
and asserts the pair's kinetics classes, rate parameters, **and units**. It observed a
genuine red state before the carry:

```
before carry (52 entries):  2 failed, 1 passed
   FAILED … the sodium cation's sink 'Nap + e- <=> Na' is not carried
   FAILED … the sodium cation's source 'Na + e- => Nap + e- + e-' is not carried
after  carry (66 entries):  3 passed
```

The third test (`… differ_by_avogadro …`) passes in both states by design: it checks that
`cm^3/(molecule*s)` and `cm^3/(mol*s)` both parse and differ by Avogadro's number — a
property of the unit machinery, independent of the carry. The two load-and-assert tests
are the RED-first ones.

## Label normalisation for the superset check (verifier 3), and its soundness

I did **not** use a global `+`→`p` substitution: that conflates the reaction separator
` + ` with a charge `+` and is lossy. Instead I tokenised each label on its arrow
(`<=>` / `=>`) and on ` + `, canonicalised each species token's charge spelling to a
neutral form (here `Xp2`/`origin/99` `X+2` → `X^2+`; `Xp`/`X+` → `X^+`; anions ending in
`-` untouched), and compared each side as a **sorted** multiset so reactant ordering can't
create a spurious mismatch. Commented (`#`) entries are excluded on both sides.

Result: the live-label sets are **equal**, not merely a superset — 66 = 66, with zero
`origin/99` labels uncovered and zero extra here. The superset holds.

**Is the check sound?** It is discriminating, not vacuous: a dropped entry would surface
as `MISSING`, a mis-spelled or spurious one as `EXTRA`; the run reported neither. Its
limit, stated plainly: it proves each `origin/99` reaction has a same-topology counterpart
here, but says nothing about whether the **kinetics/units** were carried faithfully for the
twelve non-sodium entries. That gap is covered for the sodium pair by verifier 1, and for
all fourteen by the byte-level block comparison (below); a label superset alone would pass
on a file whose rates had been silently altered, so it is necessary but not sufficient and
should not be read as the whole guarantee.

Independent of labels, every carried block was compared byte-for-byte against `origin/99`
with its label line removed: **0 of 14 differ**. So kinetics objects, numeric tables,
units and `shortDesc`/`longDesc` provenance are identical to source.

## Working directory and resolved database for the suite run

- Working directory: `/home/alon/Code/RMG-database-i157-plasmaalkali` (worktree root).
- Resolved `database.directory` (printed before each run):
  `/home/alon/Code/RMG-database-i157-plasmaalkali/input` — this checkout, via the absolute
  path in the worktree-root `rmgrc`. The measurement trap (RMG reads `rmgrc` from cwd
  first, and `RMG-Py-plasma/rmgrc` points at the shared `../RMG-database-plasma/input`)
  is avoided by running from the worktree root.

**DB repo suite** (`python -m pytest -o addopts="" -q test/`, conftest-pinned): includes
the new sodium test and the seven plasma test files.

```
1 failed, 189 passed in 24.12s
```

The single failure is
`test_argon_cation_thermo.py::test_argon_atom_type_now_declares_a_charge_envelope_but_still_parses_any_charge`
— `assert ground.atoms[0].atomtype.label == 'Ar'` returning `'Ar+'`. It is **pre-existing
and unrelated to this carry**: it constructs a ground-state argon molecule and inspects its
atom type; it never loads `PlasmaAlkali`. Proven by restoring the pre-carry 52-entry
`reactions.py` and re-running it — it fails identically. The cause is the RMG-Py engine tip
moving from `b7a032d88` (which I-210 pinned this expectation against) to `a3b42f89f`, where
argon's atom-type resolution changed. It is owned in RMG-Py / the argon-thermo work and is
gated (atom-type definitions are not mine to touch), so I left it and report it.

**RMG-Py `databaseTest.py`** (the file the brief names), run from the worktree root pinned
to this input:

```
cwd = /home/alon/Code/RMG-database-i157-plasmaalkali
database.directory = /home/alon/Code/RMG-database-i157-plasmaalkali/input
6 passed in 302.38s (0:05:02)
```

This is the comprehensive full-database load (all families + libraries, `PlasmaAlkali` at
66 entries) and it is **green**, pinned to this checkout. The brief's literally-named
verifier passes; the one red in the DB-repo suite above is the argon atom-type test, which
`databaseTest.py` does not include.

## Contradictions with the brief (measurement wins)

1. **The brief's prose enumerates 13, but 14 is right.** The listed categories
   (5 EII + 3 radiative + 3 hydrated + 2 CaOH⁺) sum to 13; the count gap is 14. The
   fourteenth live entry is `Mgp2 + e- <=> Mgp` (Mg²⁺ radiative recombination,
   `origin/99` index 45, `TwoTemperaturePlasma`, `[VernerFerland1996]`), which the prose
   omits. `origin/99` also holds `Li+2`/`Li+3` recombinations but they are **commented
   out** there (`# entry(`), so they are not among the live fourteen and I did not carry
   them. Carrying the live Mg²⁺ entry is what makes the count reconcile to 66.

2. **The sodium source is not a `cm^3/(mol*s)` rate.** The brief frames the pair's units
   as "`cm^3/(molecule*s)` and `cm^3/(mol*s)`". Only the sink (recombination) is a molar/
   per-molecule Arrhenius-family coefficient; the source (ionisation) is an
   `ElectronCollisionPlasma` **cross section** in `m^2` over `eV/molecule`, with no
   `cm^3/(mol*s)` anywhere. The test asserts each entry's actual carried units rather than
   forcing the brief's framing, and separately demonstrates the Avogadro relationship on
   the recombination's `cm^3/(molecule*s)` against a `cm^3/(mol*s)` literal.

3. **The here-file's `I-154` note is stale.** It says these fourteen "were NOT carried,
   because this line has no representation for them in a kinetics library," pending an
   `electrons=` argument on `load_entry`. On the current `plasma` tip that fix is
   superseded: `is_balanced` (docstring at `rmgpy/reaction.py`) "exempts the free electron
   from the per-element comparison and … judges [it] by charge instead," so
   `Ar + e- => Ar+ + e- + e-` balances by charge (−1 = −1). All fourteen load with
   `electrons=0` and their explicit `e-` species; no rate law needed to carry an electron
   count. I added a note at the carry site recording that this supersedes the I-154 prose
   above it. I did **not** edit the I-154 note itself or `PlasmaAir` (off-limits), but the
   same staleness applies to `PlasmaAir`'s "intended RED", which is worth a separate look
   by its owner.

## The K⁺ recombination — it loads, and its magnitude looks anomalous

Two questions were raised about the K⁺ recombination entry (`origin/99` index 3). Both are
answered by measurement below. First, what it is:

```
label = "Kp + e- <=> K",
kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.41e+0,'cm^6/(mol^2*s)'), n=-1, Ea=(0,'cal/mol'), T0=(1,'K')),
                     efficiencies={}),
shortDesc = u"[JensenJones1977]",
```

**Not a units-vs-order mismatch.** The kinetics object is a `ThirdBody` wrapper, so the
reaction is `K+ + e- (+M) <=> K (+M)` and its `arrheniusLow` legitimately carries the
third-order unit `cm^6/(mol^2*s)` — the low-pressure limit absorbs the third-body
concentration. A two-body *label* under a three-body *coefficient* is the ordinary
`ThirdBody` convention, not a defect. (An earlier draft of this report mis-read this as a
units mismatch by reading the units without the wrapper; that framing is withdrawn.)

**Does it load? Yes — checked specifically.** Loaded from this worktree, the entry resolves
with `electrons = 0`, `is_balanced() == True`, kinetics class `ThirdBody`. The concern that
`ThirdBody` is absent from `rmgpy.electron_placement._NET_ELECTRON_KINETICS_CLASSES`
(`('BadnellRRArrhenius', 'VoronovEIArrhenius')`) does not bite at load: that tuple gates the
electron-**placement** path (`resolve_electron_placement`), which is called only from the
PlasmaReactor solver (`rmgpy/solver/plasma.pyx:410`) to expand a *scalar* `Reaction.electrons`
into explicit `e-` species. This entry carries its electron as an **explicit `e-` species in
the label**, so `Reaction.electrons` stays `0`, there is nothing to place, and the placement
gate is never reached. Acceptance at load is decided by `is_balanced`, which exempts the free
electron from the element census and checks charge (`+1 − 1 = 0 = 0`) — and passes. All
fourteen carried entries load this way (`electrons = 0`, `is_balanced True`); this one was the
sharpest case and it loads.

  *Caveat, downstream and not exercised here:* were this reaction ever driven through the
  PlasmaReactor solver with its electron carried as a scalar needing placement, `ThirdBody`
  would not be recognised by `_declares_net_electron_count`. That path is not reached by the
  explicit-electron library form, by databaseTest, or by anything this carry touches, but it
  is where a future consumer could trip.

**The magnitude looks anomalous — stated, not changed.** With `A = 2.41 cm^6/(mol^2*s)`,
`n = -1`, `Ea = 0`, the low-pressure coefficient is `k = 2.41 / T`, so
`k(1000 K) = 2.41e-3 cm^6/(mol^2*s)` (`= 2.41e-15` in SI m⁶/(mol²·s)). That is many orders of
magnitude below the usual range for a three-body recombination coefficient. **This value
looks anomalous and was carried unchanged** — it is a byte-faithful carry from
Jensen & Jones 1977 p. 11, and re-sourcing or re-fitting a rate is an owner gate. I state the
number and the concern; I do not conclude it is wrong.

## The intended engine pin, and what reddened under it

The intended pin is confirmed as `a3b42f89f` — the current tip of RMG-Py `plasma`, carrying
the merged atom-type and kinetics-class work. Measured against exactly that pin, one test
reddens under engine drift alone:
`test_argon_cation_thermo.py::test_argon_atom_type_now_declares_a_charge_envelope_but_still_parses_any_charge`
fails at `assert ground.atoms[0].atomtype.label == 'Ar'`, which now returns `'Ar+'`. What
moved: that test was written by I-210 to pin the engine at `b7a032d88`, where a ground-state
argon adjacency list resolved to atom type `Ar`; at `a3b42f89f` it resolves to `Ar+`, so the
specific-atom-type resolution for argon has changed between those tips. The test never loads
`PlasmaAlkali` (proven — it fails identically with the pre-carry 52-entry file restored), so
this is unrelated to the carry and is not mine to fix (atom-type definitions are gated). It
is a live signal that the argon atom-type test suite is now stale against its own declared
engine pin and its owner should re-triage it.

## What I could not determine

- **Whether the twelve non-sodium carried entries are chemically correct**, only that they
  are byte-identical to `origin/99` and load/balance. This is a carry, not a re-derivation.
  The K⁺ magnitude flagged above (anomalously small three-body coefficient) is the one
  concrete concern I surfaced; there may be others in the carried numerics I did not audit,
  since fidelity-to-source, not correctness, was the mandate.
- **I did not rebuild any RMG-Py extension.** The resident `reaction.so` already carries the
  electron-exempting `is_balanced` (the sodium pair balances through it), so it is current
  for the behaviour this carry depends on; I did not verify every other compiled extension is
  in sync with the `a3b42f89f` source, only the one this work rests on.
