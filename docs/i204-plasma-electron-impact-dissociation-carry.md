# I-204 — carry `Plasma_Electron_Impact_Dissociation` from branch `99`

**Worktree:** `/home/alon/Code/RMG-database-i204-dissociation` (branch `i204-dissociation`, cut from
`plasma`, 0 behind). **Code repo (read-only):** `/home/alon/Code/RMG-Py-plasma` @ `plasma` tip.
**Rule applied:** `RMG-database-i200-collisional/docs/plasma_family_carry_translation_rule.md`.
Last of the four data-carrying families in this consolidation.

## What was carried

Family `Plasma_Electron_Impact_Dissociation` (`AB + e- => A + B + e-`), 5 training entries, carried
by hand (no merge/rebase/cherry-pick of `99`). Files: `groups.py`, `rules.py`,
`training/dictionary.txt`, `training/reactions.py`. Not added to any set in `recommended.py` (matches
the other plasma families on the branch).

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

## Deliverable: the `longDesc` note

The family's `groups.py` `longDesc` now records that this is an electron-impact process, the electron
is a catalyst with net count zero and incident order one, and names `electron_placement.py` as where
that order is declared — so the next reader finds the fact the stoichiometry no longer records.

## Verifier results

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
