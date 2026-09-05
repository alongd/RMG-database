# I-158 — PlasmaAir to full count, and what the rejection actually is

Branch `i158-plasmaair`. Commits `e8afd6c32` (red test), `d7d7ef68a` (the carry),
`a285287ed` / this document (findings).

The carry itself is mechanical and is described in `d7d7ef68a`. This document is for
the findings that outlive it, and for §4, which is written to be implemented from cold
by a worker who has not read any of this.

**Status: the branch is RED on purpose and is blocked on the RMG-Py balance fix in §4.**
`PlasmaAir` carries all 94 entries and loads none of them. That is the intended state:
see §5.

---

## 1. The free electron is a conserved chemical element, and that is the whole rejection

52 of the 94 entries are rejected at load. The category — "the free-electron count
changes across the arrow" — is right, but the *mechanism* is not the one this campaign
assumed, and the difference is weeks of work versus an afternoon.

### 1.1 Two refuted readings

Both were on the table and both are dead by measurement. Recorded because they are the
obvious readings and will be re-formed otherwise:

* *"The electron is double-counted — once as an explicit `e-` species with charge −1,
  and again via `self.electrons` folded in as a scalar."*
* *"`plasma`'s new charge check rejects what `99` accepted."*

### 1.2 What actually happens

`rmgpy/reaction.py::is_balanced` on `plasma` (line 1688) does this, in order:

1. count every atom by element, reactants and products, summing per-atom charge;
2. `for element in element_list: if reactant_elements[element] != product_elements[element]: return False`;
3. fold `self.electrons` into the net charges;
4. `return reactants_net_charge == products_net_charge`.

**`e` is `element_list[0]` — a first-class element, and step 2 on `plasma` does not skip
it.** So a reaction that produces or consumes a free electron has an element census that
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

* **`rxn.electrons` is `0`**, never set. `KineticsLibrary.load` sets it only under
  `if hasattr(entry.data, 'electrons')`, and `Arrhenius`, `ThirdBody`,
  `TwoTemperaturePlasma` and `ElectronCollisionPlasma` carry no such field. **The
  double-count reading is refuted**: there is nothing to double-count, and steps 3–4 are
  unreachable anyway.
* **Charge is conserved**, −1 on both sides. The charge comparison, had it run, would
  have returned `True`.
* The rejection is the element census, and nothing else.

### 1.3 Each branch has half the correct check

This is the finding that matters, and it is the cleanest example this campaign has
produced of the thing the campaign exists to fix.

| | element census | charge check |
|---|---|---|
| `origin/99` (RMG-Py) | **skips `e`** — `if element.symbol == 'e': continue` | **none** — ends `return True` |
| `plasma` (RMG-Py) | counts `e` as an element | **`return reactants_net_charge == products_net_charge`** |

Neither branch has both halves. Simulating each branch's *rule* over all 95 labels in
this library (species parsed with the `plasma` runtime; no RMG-Py file modified):

```
labels examined: 95
  99 (skip e, no charge check)           accepts 95
  plasma (count e, charge check)         accepts 42
  both halves (skip e + charge check)    accepts 94

under BOTH halves, still rejected:
   N2p + N2 => N2 + N + N             charge 1 -> 0
```

So **these 52 entries did load on `99`** — and so did `N2p + N2 => N2 + N + N`, which is
charge-broken (§2). `99` accepts all 95 because it never checks charge at all. `plasma`
accepts 42 because it counts the electron. The union of the two halves is exactly right.

### 1.4 A correction to an earlier claim in this document's history

An earlier revision of this write-up asserted "across 74 RMG-Py checkouts, not one skips
element `e`", and concluded from it that these entries had never loaded on any runtime.
**Both the claim and the conclusion were wrong, and the method was the reason.** The
survey scanned 74 *working trees*; RMG-Py's `origin/99` is checked out in no worktree, so
it was structurally invisible to it. A branch survey — `git show origin/99:rmgpy/reaction.py`
— is the check that would have caught it, and is the one to use when the question is
"what does branch X do", not a glob over checkouts.

The surrounding survey result is still true and still useful: of the 74 *checked-out*
variants, 52 end `return True` and 22 end with the charge comparison, and none of those
74 skips `e`. It simply says nothing about `99`.

### 1.5 The label tearing is a separate, `plasma`-side mechanism

The earlier revision also let a second mechanism ride on the first. Stated properly, and
independently:

* `origin/99`'s loader splits a reaction string on `' + '` (spaced):
  `for reactant in reactants.split(' + ')`. A species label containing `+` survives.
  **`Ar+` is not torn on `99`.**
* `plasma`'s loader splits on a bare `'+'`:
  `for reactant in reactants.split('+')` (`rmgpy/data/kinetics/library.py:599`). A
  species whose own label contains `+` is torn in half.

That bare-`+` split is why this branch spells cations `Arp`, and it is a fact about
`plasma`'s loader only. It is **not** a reason `99`'s entries failed — they did not fail
on `99`. The two mechanisms are unrelated and neither supports the other.

### 1.6 The partition on `plasma` is exact

Measured by loading each of the 94 entries alone into a throwaway one-entry library (one
rejection aborts a whole library, so a single load shows only the first failure):

* **42 accepted — every one has zero net electron change.** No exceptions.
* **52 rejected — 51 have nonzero net electron change**; the 52nd is
  `N2p + N2 => N2 + N + N`, which has zero electron change and fails the *charge*
  comparison instead.
* Every rejection is a balance error. **None is an unknown atom type**, so the carry's
  atom-type premise held and its falsifier did not fire.

Shapes of the 51: `(0,1) × 10` associative/collisional ionisation, `(1,0) × 27`
attachment or recombination, `(1,2) × 14` electron-impact ionisation.

### 1.7 Where this leaves the "agreed fix"

I-154 (and this library's header until this ticket) named an `electrons=` argument on
`KineticsLibrary.load_entry` as the way forward — routing the count through the scalar
metadata path. On this evidence **that is not required for these entries**: they carry
their electrons explicitly as species, charge already balances, and the only thing
rejecting them is a census that counts a free electron as if it were an argon atom.

---

## 2. `N2p + N2 => N2 + N + N` is defective at source

Charge +1 on the left, 0 on the right, no free electron on either side. It is the only
one of the 52 rejections that §4's change would **not** repair, and the only entry in the
library rejected by the charge comparison rather than the element census.

It is carried verbatim and left failing. The intended channel is ambiguous —
dissociative recombination needs an electron, charge transfer needs a cation product —
and choosing between them would be authoring chemistry, not carrying it.

It is also the first hard evidence that `plasma`'s charge check earns its keep: `99`
loaded this entry silently (§1.3), and any model built on `99`'s PlasmaAir has been
carrying a charge-non-conserving reaction.

---

## 3. `databaseTest.py` has been measuring the wrong tree

**This is bigger than this ticket and should be treated as such.**

### 3.1 Mechanism

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

That path is resolved against RMG's cwd, and the suite is normally run from the RMG-Py
worktree root — so it resolves to `/home/alon/Code/RMG-database-plasma/input`, **the
shared checkout**, regardless of which database worktree holds the change under test.

### 3.2 What a green unpinned run actually measured

Run exactly as the I-158 contract writes it — `python -m pytest test/database/databaseTest.py`
from `RMG-Py-plasma` — against this ticket's 94-entry file:

```
6 passed in 486.68s (0:08:06)
```

**That green measured `/home/alon/Code/RMG-database-plasma/input` — the shared checkout,
at 42 entries, without this change.** It never opened the file under test. Pinned
correctly, the same suite gives six setup ERRORs.

The retroactive consequence, on the record: **any `databaseTest` green recorded by a
session that did not explicitly pin is evidence about the shared checkout, not about that
session's work.** This is a database campaign whose worktrees are exactly where the
changes live, so the two are almost never the same tree. Past "databaseTest green"
entries in this campaign's ledger should be re-read with that in mind, or re-run pinned.

The trap is documented one layer down and still bit: `RMG-Py-plasma/rmgrc` itself warns
that a tracked copy "has produced meaningless-green test runs (a whole suite measured
against the wrong, or a since-moved, database)", and this repository's `test/conftest.py`
pins `database.directory` for exactly this reason. But `conftest.py` covers only the
suites *in this repository*; `databaseTest.py` lives in RMG-Py and is covered by neither.

### 3.3 The pin that makes it honest

Without editing RMG-Py's `rmgrc` (git-ignored, per-checkout, must not be edited in
place), use a pytest plugin loaded with `-p`, which runs before collection and therefore
before `setup_class` reads the setting:

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
can tell a real green from a meaningless one without re-deriving any of this. **Any
session recording a `databaseTest` result should paste that line beside it.**

---

## 4. SPECIFICATION — the RMG-Py balance fix

Written to be implemented from cold. **Not implemented here: no RMG-Py file was modified
by I-158, and this section is a specification, not a patch.** Everything below is
arithmetic over the database plus quotation of existing source.

### 4.1 The change

One file, one function: `rmgpy/reaction.py`, `Reaction.is_balanced`, on branch `plasma`.

Add the free-electron skip to the element-comparison loop, leaving the charge comparison
exactly as it is. `plasma` currently reads:

```python
        for element in element_list:
            if reactant_elements[element] != product_elements[element]:
                return False
```

`origin/99` already carries the skip this needs, verbatim:

```python
        for element in element_list:
            if element.symbol == 'e':
                continue
            if reactant_elements[element] != product_elements[element]:
                return False
```

**Take `99`'s loop and keep `plasma`'s ending.** The result is neither branch's behaviour
and is the union of their correct halves:

```python
        for element in element_list:
            if element.symbol == 'e':
                continue                      # from origin/99: the free electron is
                                              # tracked by charge, not by element count
            if reactant_elements[element] != product_elements[element]:
                return False

        if self.electrons < 0:
            reactants_net_charge += self.electrons
        elif self.electrons > 0:
            products_net_charge -= self.electrons

        return reactants_net_charge == products_net_charge   # kept from plasma
```

**Why this is correct rather than merely permissive.** Removing the electron from the
element census does not remove it from the check — it moves it to the charge comparison,
which already accounts for it correctly: every `e-` species contributes charge −1 through
the per-atom sum, and the scalar `self.electrons` is folded in immediately above. An
entry that gains or loses electrons without a matching charge change still fails. What
stops failing is the case where the electron bookkeeping is *right* and was being
double-judged: once as charge (correctly) and once as a conserved element (incorrectly).

`plasma`'s charge comparison is the precondition that makes this safe. Applying `99`'s
skip to a runtime that ends `return True` would give `99`'s behaviour — 95 of 95
accepted, including a charge-broken entry. **Do not port the skip without the charge
check.**

### 4.2 Expected effect, measured

Recomputing both halves by hand for every label in `PlasmaAir` (script:
`counterfactual.py`, reproduced in §4.5):

```
entries examined                 : 95
would PASS with 'e' skipped      : 94
would still FAIL                 : 1
  STILL FAILS  N2p + N2 => N2 + N + N   elements_match=True  charge 1 -> 0
currently rejected but would pass: 52
currently accepted but would fail: 0
```

* **52 entries currently rejected would load** — the whole I-158 carry, including
  `Ar + e- => Arp + e- + e-`, the argon cation supply the 5 torr deck needs.
* **Zero regressions** within this library: nothing currently accepted would start
  failing.
* **`N2p + N2 => N2 + N + N` still fails, correctly** — it is charge-broken at source
  (§2), and it is the test that proves the change did not simply switch the check off.

### 4.3 Scope of the zero-regression claim — read this before trusting it

The "zero regressions" number above is **scoped to `PlasmaAir`'s 95 labels only**. It is
arithmetic over one library, not a test run, and it is not evidence about the rest of the
database or about RMG-Py's own suites. An implementer must widen it. What that means
concretely:

* The change can only *widen* acceptance — it removes one `return False` path and adds
  none — so no reaction that currently balances can stop balancing. The risk is therefore
  entirely in the other direction: reactions that *should* be rejected and would now slip
  through. The only guard against that is the charge comparison, which is why §4.1
  insists it stays.
* The class of newly-accepted reactions is exactly: element census matches apart from
  `e`, **and** charge conserves. A reaction with a genuine electron-accounting error that
  nonetheless conserves charge would newly pass — the implementer should decide whether
  such a thing is constructible and, if so, pin it.

### 4.4 Suites to run, and the red-first test to write

**Write this test first and confirm it RED before changing `is_balanced`.** This project
has repeatedly had green tests that proved nothing because they asserted against the
wrong object; red-first is what makes the green mean something.

The test, in RMG-Py, e.g. `test/rmgpy/reactionTest.py` or a new
`test/rmgpy/i158ElectronCensusTest.py` — it needs no database, only three species:

```python
def test_electron_producing_reaction_balances_by_charge_not_element_count():
    """Ar + e- => Ar+ + 2 e- conserves charge (-1 = -1) and must balance,
    even though its free-electron COUNT changes 1 -> 2."""
    Ar  = Species(label='Ar',  molecule=[Molecule().from_adjacency_list('1 Ar u0 p4 c0')])
    Arp = Species(label='Ar+', molecule=[Molecule().from_adjacency_list('1 Ar u1 p3 c+1')])
    e   = Species(label='e-',  molecule=[Molecule().from_adjacency_list('1 e  u1 p0 c-1')])
    assert Reaction(reactants=[Ar, e], products=[Arp, e, e]).is_balanced()

def test_charge_non_conserving_reaction_still_fails():
    """The skip must not switch the check off: N2+ + N2 => N2 + N + N is
    charge +1 -> 0 and must STILL be rejected."""
    ...
    assert not Reaction(reactants=[N2p, N2], products=[N2, N, N]).is_balanced()
```

The first assertion is red today (element census `{Ar:1, e:1}` vs `{Ar:1, e:2}`); the
second is green today and must **stay** green — it is the negative control, and a change
that turns it red has switched the check off rather than fixed it.

Suites to run after, all of which touch `is_balanced` or electron balance:

```
test/rmgpy/reactionTest.py
test/rmgpy/i108ElectronRepresentationMatrixTest.py
test/rmgpy/electronPlacementTest.py
test/rmgpy/i134DuplicateElectronsTest.py
test/rmgpy/reactionChargeTransferTest.py
test/rmgpy/data/kinetics/electronPropagationTest.py
test/rmgpy/data/kinetics/libraryElectronPropagationTest.py
test/rmgpy/data/kinetics/plasmaLocalContextTest.py
test/rmgpy/i116IonisationRegistryTest.py
```

`test/rmgpy/i108ElectronRepresentationMatrixTest.py` is the one to read before writing
any code: it pins the current treatment of the free electron as a conserved
pseudo-element, so it is the suite most likely to encode the behaviour being changed. If
it goes red, that is a decision to surface, not a test to edit — it may be pinning the
defect.

And, pinned per §3.3 so the result means something:

```
test/database/databaseTest.py        # with -p rmg_pin at the i158 worktree
```

### 4.5 Reproducing the measurements

The scripts behind §1 and §4.2 are small and worth re-running rather than trusting:

* per-entry accept/reject census — load each entry alone into a throwaway one-entry
  library, since one rejection aborts a whole library;
* the instrumented single-reaction dump in §1.2 — rebuild the reaction from the library's
  own `dictionary.txt` and print the element census, both net charges, `rxn.electrons`,
  and the per-species charge sums;
* the branch-rule simulation in §1.3 — compute both halves by hand under each branch's
  rule; note this needs only the `plasma` runtime to *parse species*, and does not
  require checking out or building `99`.

Definition of done for the successor ticket: with the fix in place, `PlasmaAir` loads 93
of its 94 entries, the four noble-gas assertions in
`test/test_plasma_air_noble_gas_ionization.py` (this repository) go green, and
`N2p + N2 => N2 + N + N` is the sole remaining rejection.

---

## 5. Why this branch is left red

The 52 entries are **not** commented out, deliberately. Commenting them would produce a
library that loads cleanly and quietly lacks argon ionisation — and the next person to
run a 5 torr argon deck against it would get a green model with no argon chemistry in it.
That silent success is the exact failure mode this campaign exists to eliminate, and it is
strictly worse than a loud red.

The branch therefore carries the whole truth and does not load, which is the correct input
to §4. It is blocked on the RMG-Py balance fix and is not proposed for merge; merges are
the owner's gate.
