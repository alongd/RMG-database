# I-157 — carry the alkali ionisation and recombination network to full count

Branch `i157-plasmaalkali`, worktree `/home/alon/Code/RMG-database-i157-plasmaalkali`.
Engine under test: `/home/alon/Code/RMG-Py-plasma` (branch `plasma`, tip `a3b42f89f`),
conda env `rmg_env`, `PYTHONPATH=/home/alon/Code/RMG-Py-plasma`.

The carry adds fourteen entries to `input/kinetics/libraries/PlasmaAlkali/reactions.py`,
taking it 52 → 66. The two sodium entries — the cation's source and sink — load with the
rates and units `origin/99` carries.

**This is a documented variant, not a pure transcription.** Eleven of the fourteen are
byte-identical to `origin/99` apart from a single label line translated into this line's
`p`-suffix cation convention. The other **three — the Li⁺, Na⁺ and Mg²⁺ radiative
recombinations (indices 1, 2, 45)** — additionally deviate in one field: their reaction
arrow was changed from reversible `<=>` to irreversible `=>`, with an accompanying
`reversible = False` attribute. Rates, units, provenance and all numerics are unchanged.
See "The three recombinations are marked irreversible" below for why, and for why the arrow
alone was not enough. No rate parameter, charge, adjacency list or atom type was touched.

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
| radiative recombination `Xp + e- => X` **(marked irreversible)** | 3 | Li⁺ 1, Na⁺ 2, K⁺ 3† |
| radiative recombination `Mgp2 + e- => Mgp` **(marked irreversible)** | 1 | Mg²⁺ 45 |
| hydrated dissociative recombination `XH2Op + e- <=> X + H2O` | 3 | Li 11, Na 12, K 13 |
| CaOH⁺ dissociative recombination | 2 | `CaOHp + e- <=> Ca + OH` 28, `CaOHp + e- <=> CaO + H` 33 |

† K⁺ (index 3) stays **reversible** — it is `ThirdBody`, not Te-dependent, so the reactor
does not refuse it. Only the three `TwoTemperaturePlasma` recombinations (Li⁺, Na⁺, Mg²⁺)
were marked irreversible.

## The sodium pair, side by side with `origin/99`

**Sink — radiative recombination (`origin/99` index 2):** the label spelling changed
(`Na+` → `Nap`) **and** the reversibility (the documented deviation, see below); every
rate parameter and unit is unchanged.

| | `origin/99` | this line |
|---|---|---|
| label | `Na+ + e- <=> Na` | `Nap + e- => Na` **(irreversible)** |
| reversible | `True` (implicit, `<=>`) | **`False`** (`=>`, `reversible = False`) |
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

## The three recombinations are marked irreversible — the defect every load check missed

**The defect.** `PlasmaReactor._validate_reactions` (`rmgpy/solver/plasma.pyx:799-804`)
refuses a **reversible** electron-temperature-dependent reaction at `initialize_model` with
`NonEquilibriumReverseRateError` — Ruling 1: `kf(Tgas, Te) / Keq(Tgas)` combines two
incompatible thermal closures, and it does so *whatever* the instantaneous `Te == Tgas`.
This fires at reactor initialisation, **after** the electron-placement gate and long after
load. So every check run before this — the library loads, all 66 balance, rates evaluate,
the full DB suite and `databaseTest.py` pass — is green while three reactions are
inadmissible to the very reactor they exist for. A one-character negative control isolates
it: the same reaction written `=>` is accepted, written `<=>` is refused.

`PlasmaAlkali` has exactly three reversible Te-dependent entries, and all three are new in
this carry — the `TwoTemperaturePlasma` recombinations at indices 1 (Li⁺), 2 (Na⁺) and 45
(Mg²⁺). The five `ElectronCollisionPlasma` ionisations are already `=>` and pass; the
K⁺/hydrated/CaOH⁺ recombinations are `ThirdBody`/`Arrhenius`, not Te-dependent, and pass.

**The fix (owner ruling): mark those three irreversible.** `<=>` → `=>` on entries 1, 2, 45.
The chemistry, not just loadability: the reverse of `Lip + e- -> Li` **is** lithium
ionisation, and this file already carries it explicitly — `Li + e- => Lip + e- + e-` at
index 38 (Na 39, Mg 41). The reversible recombination therefore double-counted ionisation on
top of the entry that already represents it. Marking it irreversible removes a double-count
as well as the engine refusal, and is physically right for electron-ion recombination here.

**Why the arrow alone was not enough (a second, measured deviation).** Changing only `<=>`
→ `=>` raises `DatabaseError` at load: the loader (`library.py:570`) requires the label
arrow and the entry's `reversible` attribute to agree, and the attribute defaults to `True`.
Reproduced:

```
Reaction string reversibility (True) and entry attribute `reversible` (False)
must agree if reaction is irreversible.
```

So marking a library entry irreversible is inherently a two-field edit — arrow **and**
`reversible = False` — which is exactly how this file's own `ElectronCollisionPlasma`
ionisations already spell it. Both are two spellings of one change (mark irreversible); no
independent second change was made. The owner's "change only the arrow" is under-specified
against the loader, and this is the deviation I took to satisfy the intent. It is flagged
here explicitly.

**Verifier — reactor admissibility, not loading.**
`test/test_plasma_alkali_reversible_te_admissibility.py` builds a charge-neutral
`PlasmaReactor` for each of the three and, at `initialize_model`:

- **accepts** the carried irreversible form (runs to completion, no reverse-rate refusal);
- **negative control** — the same reaction forced `reversible=True` still raises
  `NonEquilibriumReverseRateError` (message carries `TwoTemperaturePlasma` and
  `irreversible`). A check that cannot fail is not a check.

```
6 passed  (3 accept + 3 negative control, for Li⁺/Na⁺/Mg²⁺)
```

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

The red state was observed against the original carry, when the sink label was still `<=>`
(the failure message above shows it). After the owner ruling the sink is `Nap + e- => Na`
(irreversible); the test was updated to that label and to assert `reversible is False`, and
still passes (3 passed). The RED-first requirement was met at the original carry; the
reversibility rework is the separately documented deviation, verified by the reactor
admissibility suite above.

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

Result, arrow-**sensitive**: three `origin/99` live labels are not covered here, and they
are exactly the documented deviation — the Li⁺/Na⁺/Mg²⁺ recombinations, `<=>` in
`origin/99`, `=>` here:

```
99-only: (('Li^+', 'e-'), '<=>', ('Li',))
99-only: (('Na^+', 'e-'), '<=>', ('Na',))
99-only: (('Mg^2+', 'e-'), '<=>', ('Mg^+',))
```

Arrow-**insensitive** (topology only, ignoring reversibility): **zero** `origin/99` labels
uncovered. So every `origin/99` reaction's species topology is present here; the only live
difference is the reversibility of those three, which is the intended variant. The strict
superset does **not** hold; the topology superset does, plus three known arrow flips.

**Is the check sound?** It is discriminating, not vacuous: a dropped entry surfaces as
uncovered topology, a spurious one as extra, and a reversibility change surfaces as an
arrow-sensitive delta — which is precisely how the three deviations showed up rather than
hiding. Reporting both the arrow-sensitive and arrow-insensitive results is what keeps a
reversibility edit from passing silently. Its limit, unchanged: it says nothing about
whether **kinetics/units** were carried faithfully — that is covered for the sodium pair by
verifier 1 and for all fourteen by the byte-level block comparison below.

Independent of labels, every carried block was compared byte-for-byte against `origin/99`
with its label line removed: **11 of 14 are identical; 3 differ** — indices 1, 2, 45, each
by the single added `reversible = False,` line. So for all fourteen the kinetics objects,
numeric tables, units and `shortDesc`/`longDesc` provenance are identical to source; the
only non-label deviation anywhere is that one attribute on those three.

## Working directory and resolved database for the suite run

- Working directory: `/home/alon/Code/RMG-database-i157-plasmaalkali` (worktree root).
- Resolved `database.directory` (printed before each run):
  `/home/alon/Code/RMG-database-i157-plasmaalkali/input` — this checkout, via the absolute
  path in the worktree-root `rmgrc`. The measurement trap (RMG reads `rmgrc` from cwd
  first, and `RMG-Py-plasma/rmgrc` points at the shared `../RMG-database-plasma/input`)
  is avoided by running from the worktree root.

**DB repo suite** (`python -m pytest -o addopts="" -q test/`, conftest-pinned): includes
the sodium test, the new reactor-admissibility test (6 cases), and the seven plasma test
files.

```
1 failed, 195 passed in 24.89s
```

The `195 passed` is `189` from before the reversibility rework plus the 6 new
reactor-admissibility cases; the failure count did not move.

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
6 passed in 309.06s (0:05:09)   # re-run after the reversibility rework; was 6 passed before it too
```

This is the comprehensive full-database load (all families + libraries, `PlasmaAlkali` at
66 entries) and it is **green**, pinned to this checkout, both before and after the three
entries were marked irreversible. The brief's literally-named verifier passes; the one red
in the DB-repo suite above is the argon atom-type test, which `databaseTest.py` does not
include.

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
