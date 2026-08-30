# I-158 — PlasmaAir to full count, and what the rejection actually is

Branch `i158-plasmaair`. Commits `e8afd6c32` (red test), `d7d7ef68a` (the carry),
plus this document.

The carry itself is mechanical and is described in `d7d7ef68a`. This document is for
the two findings that outlive it.

---

## 1. The free electron is a conserved chemical element, and that is the whole rejection

52 of the 94 entries are rejected at load. The category — "the free-electron count
changes across the arrow" — is right, but the *mechanism* is not the one this campaign
has been assuming, and the difference is weeks of work versus an afternoon.

### What was assumed

Two plausible readings were on the table, and **both are refuted by measurement**:

* *"`plasma`'s new charge check rejects what branch `99` accepted."*
* *"The electron is double-counted — once as an explicit `e-` species with charge −1,
  and again via `self.electrons` folded in as a scalar."*

### What actually happens

`rmgpy/reaction.py::is_balanced` on `plasma` (line 1688) does this, in order:

1. count every atom by element, reactants and products, summing per-atom charge;
2. `for element in element_list: if reactant_elements[element] != product_elements[element]: return False`;
3. fold `self.electrons` into the net charges;
4. `return reactants_net_charge == products_net_charge`.

**`e` is `element_list[0]` — a first-class element, and step 2 does not skip it.**
There is no skip of element `e` anywhere in `is_balanced`, on any branch (see §1.3).
So a reaction that produces or consumes a free electron has an element census that
differs in `e`, and step 2 returns `False` **before steps 3 and 4 ever run**.

Instrumented, for the entry this ticket exists for:

```
=== Ar + e- => Arp + e- + e-
    rxn.electrons                : 0
    reactant element census      : {'Ar': 1, 'e': 1}
    product  element census      : {'Ar': 1, 'e': 2}
    elements DIFFERING           : ['e']
    reactants_net_charge         : -1
    products_net_charge          : -1
    charge conserved by hand?    : True
    per-species charge           : [('Ar', 0), ('e-', -1)] -> [('Arp', 1), ('e-', -1), ('e-', -1)]
    is_balanced()                : False
```

Three things to read off that:

* **`rxn.electrons` is `0`.** It is never set for these entries. `KineticsLibrary.load`
  sets it only under `if hasattr(entry.data, 'electrons')`, and `Arrhenius`,
  `ThirdBody`, `TwoTemperaturePlasma` and `ElectronCollisionPlasma` carry no such
  field. **The double-count hypothesis is refuted**: there is nothing to double-count,
  because the scalar is never populated and steps 3–4 are never reached.
* **Charge is conserved**: −1 on both sides. The charge comparison, had it run, would
  have returned `True`.
* The rejection is the element census, and nothing else.

### 1.3 It is not campaign-introduced

The same reaction, built by hand, on three runtimes:

```
RMG-Py-plasma        rxn.electrons = 0   is_balanced() = False
RMG-Py-archive-base  rxn.electrons = 0   is_balanced() = False
RMG-Py-declare       rxn.electrons = 0   is_balanced() = False
```

The latter two are pre-campaign, *permissive* variants that end `return True`
unconditionally and never compare charge at all. They reject it anyway — in the same
element loop, which is byte-identical between the variants.

Surveyed across **74** RMG-Py checkouts on this machine, `is_balanced` varies on exactly
one axis, and it is not the one that matters here:

| variant | count | element loop | ends |
|---|---|---|---|
| permissive (pre-campaign) | 52 | counts `e`, `return False` | `return True` |
| campaign-era | 22 | counts `e`, `return False` | `return reactants_net_charge == products_net_charge` |

**Not one of the 74 skips element `e`.** So `plasma`'s stricter ending is not the cause
of these rejections, and relaxing it would not fix them.

The corollary is the uncomfortable one: **these 52 entries have never loaded on any
runtime in this tree, including branch `99`'s own.** On `99` they would fail even
earlier — `KineticsLibrary.load` splits a reaction string on a bare `+`, so `99`'s
`Ar+` spelling tears the species in half before the balance check is reached. The
framing "`99` had these working and we lost them" is false; they were never live.

### 1.4 The partition is exact

Independently measured by loading each of the 94 entries alone into a throwaway
one-entry library (one rejection aborts a whole library, so a single load shows only
the first failure):

* **42 accepted — every one has zero net electron change.** No exceptions.
* **52 rejected — 51 have nonzero net electron change**; the 52nd is `N2p + N2 => N2 + N + N`,
  which has zero electron change and fails the *charge* comparison instead (see §2).
* Every rejection is a balance error. **None is an unknown atom type**, so the carry's
  atom-type premise held and its falsifier did not fire.

Shapes of the 51: `(0,1) × 10` associative/collisional ionisation, `(1,0) × 27`
attachment or recombination, `(1,2) × 14` electron-impact ionisation.

### 1.5 What the fix looks like, measured

Recomputing both halves of the check by hand for all entries, with element `e` excluded
from the element census and charge conservation left to carry the electron bookkeeping:

```
entries examined                 : 95
would PASS with 'e' skipped      : 94
would still FAIL                 : 1
  STILL FAILS  N2p + N2 => N2 + N + N   elements_match=True  charge 1 -> 0
currently rejected but would pass: 52
currently accepted but would fail: 0
```

Zero regressions, and the one entry that still fails is the one that *should* fail.

This is an afternoon, not weeks — and note *why* it is safe: the campaign's charge
comparison already computes the correct answer for every one of these reactions. It
simply never gets reached. The stricter ending is what makes the small fix viable,
rather than being the thing in the way.

It also relocates the agreed fix. The I-154 note (and this library's header until this
ticket) named an `electrons=` argument on `KineticsLibrary.load_entry` as the way
forward — routing the count through the scalar metadata path. That is a larger change,
and on this evidence it is not required for these entries: they carry their electrons
explicitly as species, charge already balances, and the only thing rejecting them is a
census that counts a free electron as if it were an argon atom.

**Scope note.** Nothing in RMG-Py was modified. §1.5 is arithmetic over the database,
not a patch, and the fix itself remains someone else's contract.

---

## 2. `N2p + N2 => N2 + N + N` is defective at source

Charge +1 on the left, 0 on the right, no free electron on either side. It is the only
one of the 52 rejections that §1.5's change would **not** repair, and the only entry in
the library rejected by the charge comparison rather than the element census.

It is carried verbatim and left failing. The intended channel is ambiguous —
dissociative recombination needs an electron, charge transfer needs a cation product —
and choosing between them would be authoring chemistry, not carrying it.

This is the first hard evidence that the campaign's charge check earns its keep: it is a
real data defect on branch `99`, and the permissive variant would have loaded it
silently.

---

## 3. `databaseTest.py` has been measuring the wrong tree

**This is bigger than this ticket and should be treated as such.**

### Mechanism

`test/database/databaseTest.py` resolves its database in `setup_class`:

```python
database_directory = settings["database.directory"]
cls.database.load(database_directory, kinetics_families="all")
```

`settings["database.directory"]` comes from an `rmgrc`, which RMG looks for in the
current working directory, then `~/.rmg`, then beside the `rmgpy` package. There is no
`~/.rmg/rmgrc` on this machine. Every plasma RMG-Py worktree ships an `rmgrc` containing:

```
database.directory = ../RMG-database-plasma/input
```

That path is relative to RMG's cwd, and the suite is normally run from the RMG-Py
worktree root — so it resolves to `/home/alon/Code/RMG-database-plasma/input`, **the
shared checkout**, no matter which database worktree the change under test lives in.

### What that costs

Run as the I-158 contract writes it — `python -m pytest test/database/databaseTest.py`
from `RMG-Py-plasma` — this ticket's 94-entry file reports:

```
6 passed in 486.68s (0:08:06)
```

Eight minutes of green that never opened the file under test. Pinned correctly, the
same suite gives six setup ERRORs. **A `databaseTest` green recorded by any session that
did not explicitly pin is evidence about the shared checkout, not about that session's
work** — and this is a database campaign whose worktrees are precisely where the changes
live. Any past "databaseTest green" in this campaign's ledger should be re-read with
that in mind, or re-run.

The trap is well documented one layer down and still bit: `RMG-Py-plasma/rmgrc` itself
warns that a tracked copy "has produced meaningless-green test runs (a whole suite
measured against the wrong, or a since-moved, database)", and this repository's
`test/conftest.py` pins `database.directory` for exactly this reason. But
`conftest.py` only covers the suites *in this repository*; `databaseTest.py` lives in
RMG-Py and is covered by neither.

### The pin that makes it honest

Without editing RMG-Py's `rmgrc` (which is git-ignored, per-checkout, and must not be
edited in place), use a pytest plugin loaded with `-p`, which runs before collection and
therefore before `setup_class` reads the setting:

```python
# rmg_pin.py, anywhere on PYTHONPATH
from rmgpy import settings
settings["database.directory"] = "/abs/path/to/YOUR-RMG-database-worktree/input"
print("rmg_pin: database.directory =", settings["database.directory"])
```

```bash
cd /home/alon/Code/RMG-Py-plasma
PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH \
PYTHONPATH=/path/containing/rmg_pin \
  python -m pytest test/database/databaseTest.py -p rmg_pin -q
```

The `print` is the point: it puts the resolved path in the run log, so a future reader
can tell a real green from a meaningless one without re-deriving any of this. Any
session recording a `databaseTest` result should paste that line beside it.
