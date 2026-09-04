# I-204 — carry `Plasma_Electron_Impact_Dissociation` from branch `99`

**Worktree:** `/home/alon/Code/RMG-database-i204-dissociation` (branch `i204-dissociation`, cut from
`plasma`, 0 behind). **Code repo (read-only):** `/home/alon/Code/RMG-Py-plasma` @ `plasma` tip.
**Rule applied:** `RMG-database-i200-collisional/docs/plasma_family_carry_translation_rule.md`.
Last of the four data-carrying families in this consolidation.

## Disposition — STAGED OUT of `input/`, deliberately

**This family is NOT in `input/`. Its files live in `docs/plasma_electron_impact_dissociation_staged/`
and must stay there until the electron-placement gap below is closed in the code repository.** This
is the same disposition the other three carries reached, for a sharper reason. The family loads
green, passes the standing kinetics suite, and leaves the 5 torr argon deck untouched — and it
generates a dissociation rate that is **wrong by a factor of the electron density** (§ "Why staged
out"). A family that fails loudly is safe: someone sees the error and stops. A family that is green
*and* wrong is the most dangerous artifact this campaign can produce, because every downstream check
agrees with it — it is one merge away from a mechanism whose dissociation rates are off by n_e with
nothing anywhere to say so, and at 5 torr that factor is enormous. So the report is the deliverable,
not the family. Do not move these files into `input/` until the placement gate (`plasma.pyx:379`) is
lifted and a net-zero placement path exists.

## Why staged out — the dimensional argument (this is the whole finding)

The training coefficients are declared for the two-body process `AB + e- -> A + B + e-`, so their
units are **`cm^3/(mol*s)`** — second order. Example (entry 1):
`A = 1.05e17 cm^3/(mol*s)`, applied as a rate `A·[AB]·[e-]` (units `mol/(cm^3·s)`, correct).

Under the translated representation the generated reaction is unimolecular `AB => A + B`
(`electrons = 0`, no `e-` reactant), so RMG evaluates a **first-order** rate law `A·[AB]`. Feeding a
second-order coefficient (`cm^3/(mol*s)`) into a first-order law leaves the result carrying an extra
`cm^3/mol`, i.e. the computed rate is the true rate **divided by `[e-]`** (in `mol/cm^3`) — off by
**exactly one factor of the electron density n_e**, no more and no less. `TwoTemperaturePlasma`
cannot supply that factor: it is `k(T, Te)`, a function of gas and electron *temperature*, with no
density term. n_e enters only as the incident-electron reaction order, which the `electrons = 0`
stoichiometry has thrown away. At 5 torr, n_e is large, so the error is not a rounding matter — the
dissociation channel is mis-weighted by orders of magnitude, silently.

## What was staged

Family `Plasma_Electron_Impact_Dissociation` (`AB + e- => A + B + e-`), 5 training entries, carried
by hand (no merge/rebase/cherry-pick of `99`) and translated, then staged at
`docs/plasma_electron_impact_dissociation_staged/{groups.py, rules.py, training/dictionary.txt,
training/reactions.py}`. Not added to any set in `recommended.py`. The translation below was verified
with the files temporarily in `input/` (see Verifier results — that green-and-wrong state is the
evidence for staging out); they were then moved to `docs/`.

### The rule, applied to this family

| Edit | Result here |
|---|---|
| 1. Strip `e-` from template | `template(reactants=["AB"], products=["A","B"])` (was `["AB","e-"]`→`["A","B","e-"]`) |
| — remove orphaned `e-` group entry + `L1: e-` tree node | done (e- is no longer a template species) |
| 2. Delete `custom_kinetics` | `custom_kinetics = False` removed |
| 3. `product_electrons` → `electrons` (signed net) | `product_electrons = 1` → **`electrons = 0`** (net catalytic: 1 produced − 1 consumed = 0, per owner ruling 2026-09-03) |
| 4. `dictionary.txt`: remove `e-`, relabel charged | `e-` removed; **no charged species** → no relabel |
| 5. `reactions.py`: drop `+ e-` from labels | `H2 + e- <=> H + H + e-` → `H2 <=> H + H`, ×5 |

`rules.py` (empty stub) carried verbatim. No kinetics value, rank, `shortDesc` or `longDesc` of any
training entry was altered — provenance travels intact.

### Structural walls (both clear)

- **Atom-type perception (Q3a):** all 5 training species load on this branch — H2, H, O2, O, Na2,
  Na, K2, K, NaK. No `NO+`-style wall.
- **Spectator (Q3b):** the recipe (`BREAK_BOND *1-*2`, `GAIN_RADICAL *1`, `GAIN_RADICAL *2`) touches
  both centres; the electron is *removed* from the template under the ruling, not left as a
  spectator. No adjacency-identical group pair is created → cannot trip
  `kinetics_check_groups_nonidentical`. This is the collisional pathfinder's spectator wall
  *not* arising here, confirmed rather than assumed.

## The load-bearing finding — the n_e dependence is lost, and `(1,1)` alone will not restore it

The ruling directed `electrons = 0` with `e-` absent from the template, resting on the premise that
the electron-density dependence would be carried by the kinetics object. **That premise is refuted
empirically**, and the scope-correction's replacement plan (declare `(1,1)` in
`FAMILY_ELECTRON_PLACEMENT`) is the correct *shape* but is **insufficient on its own**.

**1. The kinetics object carries electron TEMPERATURE, not electron DENSITY.**
`TwoTemperaturePlasma` is `k(T, Te)` (`RMG-Py-plasma/rmgpy/kinetics/arrhenius.pyx:320-341`): gas
temperature `T` and electron *temperature* `Te` (via `Ea_e`). It has no electron-*density* (n_e)
term. With `electrons = 0` and no explicit `e-` reactant, the generated reaction is the unimolecular
`AB => A + B` — first order, no n_e factor:

```
generated: <Molecule "[H][H]"> => <Molecule "[H]"> + <Molecule "[H]">   electrons=0, no e- reactant
kinetics  : TwoTemperaturePlasma(A=(1.05e17,'cm^3/(mol*s)'), n=-1.24, Ea_g=0, Ea_e=(12.59,'eV/molecule'))
```

The n_e dependence is the incident-electron *reaction order*, which lives only in placement, never
in the kinetics object. So it is genuinely **lost** in this representation. (The coefficient's units
`cm^3/(mol*s)` are second-order, but the reaction is now first order — the missing `[e-]` factor is
exactly the "off by a factor of electron density" corruption `electron_placement.py` warns of at
lines 67-70.)

**2. A `(1,1)` declaration cannot be honoured for this shape — the resolver is gated out.**
`PlasmaReactor._resolve_electron_placements` (`RMG-Py-plasma/rmgpy/solver/plasma.pyx:379`) selects
reactions for the resolver with `if getattr(rxn, 'electrons', 0):`. With `electrons = 0` the reaction
is passed through unchanged (`plasma.pyx:383`) and `resolve_electron_placement` — the *only*
production call site is `plasma.pyx:381` — is **never called**. So a `(1,1)` entry in
`FAMILY_ELECTRON_PLACEMENT` would never be consulted for this family.

Directly calling the resolver (the path the gate skips) *does* raise, naming the family:

```
ElectronPlacementError: Family 'Plasma_Electron_Impact_Dissociation' has no electron-placement
declaration (reaction <Molecule "[H][H]"> => <Molecule "[H]"> + <Molecule "[H]">, electrons=0);
refusing to infer electron placement from the net electron count.
```

— which **confirms** the scope-correction's ElectronPlacementError expectation *for the direct call*,
but **refutes** that it ever fires in a run: the gate makes it unreachable for an `electrons=0`
reaction. This is exactly what `electron_placement.py`'s own docstring records **by name** for this
family (lines 199-209): *"A `(1, 1)` declaration therefore could not be honoured even if someone
wrote it: the resolver would never consult the table for that shape."*

### Companion-ticket specification (as requested)

- **Label:** `'Plasma_Electron_Impact_Dissociation'`
- **Pair:** `(1, 1)` — `reactant_count = 1`: one incident electron, which is the whole point (makes
  the rate second order, the `cm^3/(mol*s)` coefficient dimensionally meaningful, and the n_e
  dependence real); `product_count = 1`: one liberated; **net = 0** (catalyst).
- **The pair is necessary but not sufficient.** The companion ticket must *also* change the
  `electrons != 0` gate at `plasma.pyx:379` (and give the resolver/reactor a net-zero,
  both-sides-nonzero placement path) — otherwise the `(1,1)` entry is dead code for this shape. The
  gate is the real blocker, not the mapping entry. This is a code-repo change and is out of scope
  here (code repo kept read-only).

## The code's recorded reason for holding this family back is wrong

`electron_placement.py`'s docstring names this family twice and both times attributes its absence to
a **spectator** problem:

> "…``Plasma_Collisional_Ionization`` and ``Plasma_Electron_Impact_Dissociation`` both make a
> SPECTATOR a template participant, which RMG's family model cannot express…" (lines 186-189)
>
> "Such a family has to carry its electron as an explicit template participant instead, which is what
> that one does — and which is separately why it is held back from the database (RMG's family model
> cannot express a spectator participant…)" (lines 205-208)

That reason does not survive measurement of the representation this ticket produces:

- The recipe is `BREAK_BOND *1-*2`, `GAIN_RADICAL *1`, `GAIN_RADICAL *2` — it acts on **both** heavy
  centres. There is no unchanged heavy species, so no heavy spectator exists. The only conserved
  participant is the electron itself.
- Under the ruling the electron is **removed** from the template (`reactants=["AB"]`,
  `products=["A","B"]`), so nothing is asked to carry a spectator participant at all. The family then
  loads green, passes `test_kinetics`, and generates reactions (Verifier 1 & 4). The "family model
  cannot express it" claim is therefore false for this representation — I loaded it.

So the docstring's spectator reason describes only the *old* `99` shape (electron kept in the
template), and is stale for the shape the ruling defines. **The real reason this family must stay out
of `input/` is not the spectator — it is the placement gate and the n_e loss above.** This matters
because the next person to reopen this will start from that docstring: they will go hunting for a way
to express a spectator participant, when the actual blocker is the `electrons != 0` gate at
`plasma.pyx:379`. A wrong reason in the code's own record is a finding in its own right; correcting
it belongs in the companion (code-repo) ticket alongside the gate change.

## Deliverable: the `longDesc` note

The staged `groups.py` `longDesc` records that this is an electron-impact process, the electron is a
catalyst with net count zero and incident order one, and names `electron_placement.py` as where that
order is declared — so the next reader finds the fact the stoichiometry no longer records.

## Verifier results

The four verifier runs below were performed with the family temporarily in `input/`. That is
deliberate: Verifier 4's AFTER run is the *green-and-wrong* state that justifies staging out — the
family passed the standing suite while generating an n_e-wrong rate. The files were moved to
`docs/plasma_electron_impact_dissociation_staged/` immediately afterward; `input/` no longer contains
the family.

### 1. Family loads and is what we think it is (worktree DB)
```
template  : reactants ['AB'] -> products ['A','B']
electrons : 0
n_training: 5   (all TwoTemperaturePlasma)
  [1] H2 <=> H + H     Ea_e=12.59 eV   rank 6
  [2] O2 <=> O + O     Ea_e=5.56  eV   rank 6
  [3] Na2 <=> Na + Na  Ea_e=0.74  eV   rank 9
  [4] K2 <=> K + K     Ea_e=0.52  eV   rank 9
  [5] NaK <=> Na + K   Ea_e=0.52  eV   rank 9
```

### 3. Before/after electron bookkeeping (mirrors `family.py:675`/`696`)
```
[VERBATIM-99] product_electrons=1  ->  electrons (as loader reads) = 0
[TRANSLATED]  product_electrons=<absent>  ->  electrons (as loader reads) = 0
```
`99` declares its count under the other branch's key `product_electrons` (never read → default 0);
the translated copy declares `electrons=0` (read → 0). Both 0, but accidental-default in `99` vs
intentional-by-ruling in mine. (This family differs from the collisional pathfinder case, 99→0 vs
translated→1, because the catalytic net here is 0 on both.)

### 4. Standing DB test — `test/database/databaseTest.py::TestDatabase::test_kinetics`
One suite per process (separate `pytest` invocations, separate CWDs/rmgrc).
```
BASELINE  (RMG-database-plasma/input)           : 1 passed, 5 deselected in 545.64s   EXIT=0
AFTER     (RMG-database-i204-dissociation/input) : 1 passed, 5 deselected in 407.79s   EXIT=0
```
No worse than baseline — the family adds a clean green node; the spectator wall the pathfinder hit
does not arise here (no adjacency-identical group pair created).

### 5. 5 torr argon deck — `RMG-Py-plasma/docs/i194-ar5torr-plasma-lineage/input.py`
Deck requests `kineticsFamilies=['Plasma_Electron_Attachment']` only — not this family — so
*unchanged* is the prediction, and it holds. Run with `RMG-Py-plasma/rmg.py`, clean run dir, rmgrc →
worktree DB, `PYTHON_EXIT` captured from the interpreter itself:
```
ARGON_PYTHON_EXIT=0
MODEL GENERATION COMPLETED  (count = 1)
The final model core has 3 species and 1 reactions
```

## Non-goals honoured
No merge/rebase/cherry-pick of `99`; no `recommended.py` change; no other family touched; code repo
read-only; no kinetics value altered; electron convention unchanged (ruled). Committing not gated;
push/merge gated and not done.
