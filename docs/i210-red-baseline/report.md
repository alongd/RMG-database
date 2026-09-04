# I-210 red-baseline triage: twelve failing tests at the plasma tip

**Branch:** `i210-baseline` (off `plasma` tip `231617f7e`).
**Engine under test:** `/home/alon/Code/RMG-Py-plasma` (branch `plasma`, tip `b7a032d88`).
**Baseline reproduced:** `12 failed, 171 passed` — the exact twelve named in the brief.

The engine tip moved from `8751394fe` to `b7a032d88` during this work (merges of `i206-placement`
and `i201-wrapper` landed). `i201-wrapper` changed the cythonized `rmgpy/reaction.py`, leaving
`reaction.so` stale; it was rebuilt (`python setup.py build_ext --inplace -j 8`) so results are not
measured against a stale extension. No verdict changed: the same twelve failed at `b7a032d88` before
the rewrites, and all pass after.

Reproduction (the environment is the trap — `RMGpy_RC` is *not* honoured; `test/conftest.py`
pins `database.directory` to this worktree at collection time, which is what actually sets the
engine's database):

```bash
source ~/anaconda3/etc/profile.d/conda.sh && conda activate rmg_env
export PYTHONPATH=/home/alon/Code/RMG-Py-plasma
cd /home/alon/Code/RMG-database-i210-baseline
python -m pytest -o addopts="" -q test/
# 12 failed, 171 passed
python -c "import rmgpy, os; print(os.path.dirname(rmgpy.__file__))"
# /home/alon/Code/RMG-Py-plasma/rmgpy
```

## Verdict count

- **STALE TEST: 12**
- **REAL REGRESSION: 0**
- **UNDETERMINED: 0**

Every one of the twelve fails because a capability moved *deliberately* in RMG-Py, under a
commit that says so in its message. Eight are capability-boundary tests (`... cannot be built`,
`... is unconstrained`) whose boundary the atom-type work erased on purpose; four are attachment
provenance tests that passed only because of a since-fixed electron-propagation bug. No test in
the twelve caught a defect. The chemistry (rates, nodes, products) is correct in every case.

## The table

| test id | group | verdict | evidence |
|---|---|---|---|
| `test_argon_cation_thermo.py::test_the_gate_before_thermochemistry_is_the_atom_type[Na-...]` | atom-type gate | STALE TEST | `Na+` builds (atomtype `Na+`); test expected `KeyError`. Atom type added by `e918cafdd`. |
| `test_argon_cation_thermo.py::test_the_gate_before_thermochemistry_is_the_atom_type[Mg-...]` | atom-type gate | STALE TEST | `Mg+` builds (atomtype `Mg+`); test expected `KeyError`. Atom type added by `e918cafdd`. |
| `test_argon_cation_thermo.py::test_the_gate_before_thermochemistry_is_the_atom_type[K-...]` | atom-type gate | STALE TEST | `K+` builds (atomtype `K+`); test expected `KeyError`. Atom type added by `e918cafdd`. |
| `test_argon_cation_thermo.py::test_the_gate_before_thermochemistry_is_the_atom_type[Ca-...]` | atom-type gate | STALE TEST | `Ca+` builds (atomtype `Ca+`); test expected `KeyError`. Atom type added by `e918cafdd`. |
| `test_argon_cation_thermo.py::test_argon_is_representable_only_because_its_atom_type_is_unconstrained` | atom-type gate | STALE TEST | `ATOMTYPES['Ar'].charge` is now `[0, 1, 2]`; test asserts `not ...charge`. Charge envelope added by `b52045138`. |
| `test_plasma_electron_impact_ionization.py::test_five_covered_elements_cannot_be_built_by_rmg_at_all[Na]` | family "cannot build" | STALE TEST | neutral `Na` (`1 Na u1 p0 c0`) builds (atomtype `Na0`); test expected an exception. Atom type added by `e918cafdd`. |
| `test_plasma_electron_impact_ionization.py::test_five_covered_elements_cannot_be_built_by_rmg_at_all[K]` | family "cannot build" | STALE TEST | neutral `K` builds (atomtype `K0`); test expected an exception. Atom type added by `e918cafdd`. |
| `test_plasma_radiative_recombination.py::test_four_covered_elements_cannot_be_built_by_rmg_at_all[Na]` | family "cannot build" | STALE TEST | neutral `Na` builds (atomtype `Na0`); test expected an exception. Atom type added by `e918cafdd`. |
| `test_plasma_electron_attachment.py::test_trained_species_resolve_to_their_own_rate_through_their_own_node[O2]` | attachment provenance | STALE TEST | numeric rate unchanged & correct (9.6807e10, training rxn 1), node `O_in_O2`; `source`, kinetics class (`Arrhenius` vs `ArrheniusEP`) and comment changed. Caused by electron-propagation fix `bb95576e4`. |
| `test_plasma_electron_attachment.py::test_trained_species_resolve_to_their_own_rate_through_their_own_node[OH]` | attachment provenance | STALE TEST | rate exact & correct (2.9580e10, training rxn 2), node `O_in_OH`; same `source` change. `bb95576e4`. |
| `test_plasma_electron_attachment.py::test_trained_species_resolve_to_their_own_rate_through_their_own_node[O]` | attachment provenance | STALE TEST | rate exact & correct (9.0332e08, training rxn 3), node `O_atom`; same `source` change. `bb95576e4`. |
| `test_plasma_electron_attachment.py::test_o2_rate_comes_from_the_training_set_not_a_library` | attachment provenance | STALE TEST | libraries empty; numeric rate is exactly training rxn 1; `source` object, kinetics class and comment changed. `bb95576e4`. |

## Group 1 + Group 3 — the eight "cannot be built / is unconstrained" tests

**Shape.** Each asserts that a charged or neutral species *cannot be constructed* by
`Molecule().from_adjacency_list(...)`, either via `pytest.raises` or by asserting an atom type
carries no charge envelope. Each now fails with "DID NOT RAISE" / a non-empty charge list,
meaning the species *can* be built.

**Root cause — two deliberate RMG-Py commits on the `plasma` branch.**

### `e918cafdd` — "Give RMG alkali and alkaline-earth atom types" (Alon Grinberg Dana, 2026-08-29)

Deliberate, with a stated reason: *"Na, K, Mg and Ca, with their charged forms ... ported from
branch 99 ... Without these the carried PlasmaAlkali library and four of the plasma families
fail to load with KeyError."* This is a required capability, not a side effect. Measured effect:

```
Na+ -> atomtype Na+ (charge [0, 1])      neutral Na (u1 p0 c0) -> atomtype Na0
Mg+ -> atomtype Mg+ (charge [0, 1, 2])   neutral Mg (u1 p0 c0) -> InvalidAdjacencyListError
K+  -> atomtype K+  (charge [0, 1])      neutral K  (u1 p0 c0) -> atomtype K0
Ca+ -> atomtype Ca+ (charge [0, 1, 2])   neutral Ca (u1 p0 c0) -> InvalidAdjacencyListError
Al  -> KeyError (no atom type)           Be, B -> KeyError (no atom type)
```

This explains exactly which parametrizations flipped:

- **Argon-cation gate** (`test_the_gate_before_thermochemistry_is_the_atom_type`): the *cation*
  cases `Na+/Mg+/K+/Ca+` all now build → four failures. `C`/`F` (`AtomTypeError`) and `Al`
  (`KeyError`) still raise → still pass.
- **Ionization "five covered elements"** builds the *neutral* radical `1 X u1 p0 c0`: only `Na`
  and `K` flip (`Na0`/`K0`); `Mg`/`Ca` still raise `InvalidAdjacencyListError` on that specific
  odd-electron adjacency list and `Al` still `KeyError` — so only `[Na]`, `[K]` fail.
- **Recombination "four covered elements"** builds the neutral radical too: only `Na` flips;
  `Be`, `B`, `Mg` still raise — so only `[Na]` fails.

### `b52045138` — "Narrow the placement declarations, and let noble gases be cations" (Alon Grinberg Dana, 2026-08-29)

Deliberate, stated: *"He, Ne and Ar now declare charge=[0, 1, 2]. They declared no charge
envelope at all, so GroupAtom.make_sample_molecule ... refused every noble-gas cation. Ar+, He+,
He+2 and Ne+ are all real species in the PlasmaAir library this branch carries."* This directly
falsifies the premise of `test_argon_is_representable_only_because_its_atom_type_is_unconstrained`,
which asserts `not ATOMTYPES['Ar'].charge`. `ATOMTYPES['Ar'].charge` is now `[0, 1, 2]`.

Note the corollary the test also documents still holds: a nonsense `Ar(4+)` *still* builds
(`multiplicity 5 / 1 Ar u4 p0 c+4` → net charge 4), because argon is in `nonSpecifics` and
`get_atomtype` returns it without consulting the charge features. So the charge envelope narrows
what group-sample construction will *emit*, not what `from_adjacency_list` will *parse*.

### Attribution method — static source bisect, not a runtime bisect

The attribution to `e918cafdd` and `b52045138` is by the commits' own diffs plus the current
source, verified at the source level across each commit boundary — **not** by a runtime bisect
that checks out the parent and re-runs the assertions. What was verified:

- `e918cafdd~1` (parent): `rmgpy/molecule/atomtype.py` contains **2** `ATOMTYPES['Na'|'Mg'|'K'|'Ca']`
  registrations; the commit itself contains **38**. The added lines are exactly
  `ATOMTYPES['Na'|'Na0'|'Na+'|'K'|'K0'|'K+'|'Mg'|'Mg+'|'Ca'|'Ca+'] = AtomType(...)` — the atom
  types whose absence the eight "cannot be built" assertions encoded.
- `b52045138~1` (`61578919c`): `ATOMTYPES['Ar'] = AtomType('Ar', ..., specific=[])`, no `charge=`
  kwarg (→ unconstrained). The commit changes that line to `..., specific=[], charge=[0, 1, 2]`
  (same for He, Ne). That is the exact line the argon test's premise depended on.

**Why not a runtime bisect.** `atomtype` is a *cimported compiled extension*: `atomtype.pxd`
exists and `atomtype` is built to `atomtype.cpython-39-*.so`. I attempted a cheap runtime bisect
in a throwaway worktree checked out at `e918cafdd~1`, reusing the tip's compiled `.so` (only
`rmgpy/solver/*.pyx` differ across the range, so `molecule.so` is ABI-compatible) — and it returned
**tip** behaviour at the parent checkout (Na+/Mg+/K+/Ca+ built, `Ar.charge == [0,1,2]`), because
the copied `atomtype.so` shadows the parent's `atomtype.py`. A faithful runtime bisect therefore
requires recompiling the `atomtype`/`molecule` extensions at the parent commit — a full Cython
rebuild — which I judged too expensive and disruptive to run against the shared `RMG-Py-plasma`
engine that concurrent sessions use. The static source bisect above is the evidence I stand on; it
is conclusive for *which commit introduced the registrations and the charge envelope*, and the
runtime "now builds / now `[0,1,2]`" side is verified against the current engine tip.

**Downstream (brief §4).** The capability turning on is load-bearing, not cosmetic: per
`e918cafdd`'s own message, the carried `PlasmaAlkali` library and four plasma families now *load*
where they previously raised `KeyError`; per `b52045138`, `GroupAtom.make_sample_molecule` now
emits noble-gas and alkali cations it previously refused. That is precisely why the brief says
"the fact that these elements are now constructible is itself worth pinning, because it can
regress" — the rewritten tests below pin it.

## Group 2 — the four attachment provenance tests

**Shape (different in kind).** These are *not* capability-boundary tests. All four fail at the
single assertion `assert source == 'rate rules'`, where `family.get_kinetics(..., estimator='rate
rules', return_all_kinetics=False)` now returns the **training depository object** as `source`.

**This is not a wrong rate.** Probed directly against the plasma engine:

```
O2:  template ['O_in_O2'], A*1e6 = 9.6807e10  == training reaction 1  (exact, rel 1e-9)
     comment: "Matched reaction 1 O2 <=> O2- in Plasma_Electron_Attachment/training
               This reaction matched rate rule [O_in_O2] ..."
     libraries == {}  (no library is even loaded)
```

The numeric rate is exactly training reaction 1's value, the node is `O_in_O2`, no library is
involved, and no averaging occurs. The test's stated intent — *"the rate comes from the training
set, not a library"* — is **fully satisfied**.

What changed is more than the provenance string, and the report should not undersell it: the
kinetics *object and its class* changed too. The exact-match (depository) path returns a
`copy.deepcopy` of the raw training `Arrhenius`; the old rate-rules path ran that same training
data through `add_rules_from_training`, whose `to_arrhenius_ep` converts a plain `Arrhenius` into an
`ArrheniusEP`. So the two paths yield different kinetics classes (`Arrhenius` vs `ArrheniusEP`),
different `source` objects, and different comment strings. Confirmed against the current engine:

```
exact-match path (electrons=-1): class=Arrhenius   source=<training depository>  A_si=96807  (deepcopy of the raw entry)
rate-rules path  (electrons=0) : class=ArrheniusEP source='rate rules'            A_si=96807
numeric k1/k0 ratio at 300/1000/2000 K: [1.0, 1.0, 1.0]
```

They are numerically equal here for a specific and sufficient reason, not because the object is the
same: these training entries have `n=0`, `Ea=0`, `T0=1 K` and degeneracy 1, so the `ArrheniusEP`
(`alpha=0`, `E0=0`) reduces to exactly the same `k(T)` as the deepcopied `Arrhenius`. So the honest
statement is: **the numeric rate is unchanged, and here is why it is unchanged — the kinetics
object, its class, and the provenance string all changed.** The rewritten tests assert equality with
`pytest.approx(rel=1e-9)` on the rate and drop any class/exact-string dependence, which is
consistent with this wording and not with a "byte-identical" claim.

**Root cause — `bb95576e4` "Count electrons toward molecularity, and give families a route to
their training reactions" (Alon Grinberg Dana, 2026-08-16), a deliberate bug fix.**

`get_kinetics` (family.py:2666) searches `self.depositories` *before* the rate-rules estimator,
and with `return_all_kinetics=False` an exact depository match short-circuits and returns
`source=<depository>` (family.py:2695). That short-circuit is unchanged since 2018 (`81ede25d74`).
The variable is whether the training entry *matches* the generated reaction:

- The generated attachment reaction carries `electrons=-1` (the family's declaration).
- Before `bb95576e4`, training reactions loaded with `electrons=0` — the exact bug that commit
  names and fixes (*"a family's declaration died at the load boundary and every training reaction
  reported electrons=0"*).
- `Reaction.is_isomorphic` **compares the electron count**. So before the fix, training entry
  (`electrons=0`) ≠ generated reaction (`electrons=-1`): the depository search *missed*, and
  `get_kinetics` fell through to the rate-rules estimator → `source='rate rules'`, comment
  `"From training reaction 1 used for O_in_O2\nExact match found for rate rule [O_in_O2]"`.

Proven by forcing the training entry's electron count both ways against the current engine:

```
training entry electrons = -1 (current)  -> is_isomorphic True  -> source = training depository
training entry electrons =  0 (pre-fix)  -> is_isomorphic False -> source = 'rate rules'
                                            comment "From training reaction 1 used for O_in_O2 ..."
```

So these four tests were **green only because of the electron-propagation bug**. The fix restored
the correct behaviour — an exact training reaction is matched as an exact training reaction — and
the tests, which pin the buggy fall-through path and its comment strings, went red while the
numeric rate stayed exactly right. Same class as the other eight in the sense that a deliberate
RMG-Py change moved the ground under a test; different in kind in that the mechanism is
electron-count isomorphism in `get_kinetics`, not atom-type construction, and the moved
capability is a *correctness fix* rather than an added element.

**Not a regression.** The `"Matched reaction N ... in <family>/training"` provenance is the
standard RMG comment for an exact training-reaction match and is more direct, not less trustworthy,
than the rate-rule citation it replaced. The numeric rate, node, product charge and formula are all
unchanged and correct; the kinetics class and provenance changed, as detailed above, and the
rewritten tests assert the new class-agnostic truth (own node, own numeric rate, from the training
depository, no library, no average).

## What I could not determine

Nothing in the twelve is undetermined. Every failure has a named causal commit on the `plasma`
branch and a stated, deliberate reason. The one thing I did **not** attempt — out of scope and
out of bounds (RMG-Py is closed to me) — is to judge whether `Ar` gaining a `[0, 1, 2]` charge
envelope while a nonsense `Ar(4+)` still parses is a fully coherent design; the two coexist by the
`nonSpecifics` route the commit message describes. That coherence question is open and **owned in
RMG-Py**, where the noble-gas charge specifics (Ar0/Ar+/Ar++) live, not in this database triage.
The rewritten argon test pins the *observed current behaviour* so it cannot regress silently, and
its docstring says explicitly that pinning is not blessing — deliberately, so the rewrite cannot be
read as ratifying a parser gap as a spec.

## Disposition of the tests

All twelve verdicts are STALE with a named commit, so per the campaign rule (a test whose name has
become false is rewritten to assert the new truth, never deleted or skipped) each is rewritten to
pin the new, correct behaviour. No test was deleted or skipped; every parametrization is retained
(elements that still cannot be built keep their `pytest.raises` assertion, elements that now build
gain a constructibility assertion). Final count after the rewrite is recorded below.

## Final count

Measured against the current engine tip `b7a032d88` (with `reaction.so` rebuilt), run from the
repo root:

```
before rewrites (pre-rewrite tests @ b7a032d88):  12 failed, 171 passed   # same twelve as at 8751394fe
after  rewrites (this branch      @ b7a032d88):  183 passed, 0 skipped, 0 xfailed
```

The before-line was measured in a throwaway database worktree at the pre-rewrite tip `231617f7e`
against the same `b7a032d88` engine, confirming the two intervening merges changed no verdict.

Nothing was deleted or skipped (0 skips, 0 xfails). The total test count is unchanged at 183 —
every parametrization was retained, moved to whichever assertion is now true:

| location | before | after | net |
|---|---|---|---|
| argon-cation gate | 7 params (C,F,Na,Mg,Al,K,Ca) | gate 3 (C,F,Al) + new alkali 4 (Na,Mg,K,Ca) | 0 |
| argon unconstrained | 1 | 1 (renamed, asserts `charge==[0,1,2]`) | 0 |
| ionization "covered elements" | 5 (Na,Mg,Al,K,Ca) | 3 (Mg,Al,Ca) + new 2 (Na,K) | 0 |
| recombination "covered elements" | 4 (Be,B,Na,Mg) | 3 (Be,B,Mg) + new 1 (Na) | 0 |
| attachment provenance | 4 | 4 (rewritten in place) | 0 |

So the 12 formerly-failing cases now pass by asserting the new, correct behaviour, and the 171
previously-passing tests are untouched.

Committed on branch `i210-baseline`; commit sha recorded in the handoff / commit message.
