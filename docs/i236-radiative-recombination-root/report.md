# I-236 — Narrowing the root of `Plasma_Radiative_Recombination`

Worktree `/home/alon/Code/RMG-database-i236-radiative-root`, branch
`i236-radiative-recombination-root`, base `96f2afa4a`.
Engine for every measurement: `/home/alon/Code/RMG-Py-plasma` (branch `plasma`, tip `311818121`),
on `PYTHONPATH`. **RMG-Py was not modified.**

Every probe prints its resolved database as its first line. The "after" runs resolve to
`/home/alon/Code/RMG-database-i236-radiative-root/input`; the baseline runs resolve to
`docs/superpowers/base_input`, a hard-linked copy of `input/` whose only difference is a pristine
`Plasma_Radiative_Recombination/groups.py`, verified byte-identical to `HEAD` by `diff` before any
measurement. `git stash` was not used anywhere. Probes: `probes/`. Logs: `logs/`.

---

## Where this ended up, after a correction

`Ar+ + e- => Ar` **is generated, by this branch, with ground-state argon as the product**, asserted
by isomorphism against both the ground state and the metastable:

```
Plasma_Radiative_Recombination_Pairing
  <Molecule "[Ar+]"> => <Molecule "[Ar]">   electrons=-1
    product: 1 Ar u0 p4 c0
    isomorphic to GROUND-STATE Ar : True
    isomorphic to METASTABLE Ar   : False
    net charge: +0
```

It took a second family, because the two halves of radiative recombination need two *recipes* and a
family carries one. That is the correct decomposition, not a workaround.

**An earlier draft of this report stopped after the narrowing and called the argon half a known
limitation. That was wrong, and the section below headed "the brief's prescription is wrong"
remains true only about the prescription — widening the sibling family's root — and not about the
conclusion I drew from it.** I had also inferred a grammar limit from one failed load without
reporting the exception; the post-mortem is in "M3 was an authoring error", and it inverted the
conclusion. Both corrections came from measurements that are in this document.

**A third claim of mine was overturned in review, and it was one I had stated without measuring.**
On the review round, the manager pointed out that `electrocatLiThermo/H3O` is not a bare atomic
cation, which made "the root can only ever match a bare atomic cation" an over-reach; probing that
also showed the sentence beside it — "the generated product is the same complex with the proton
reduced" — is simply false. The family generates **nothing** from that entry, because the recipe's
two product fragments meet a one-product template. Both statements are corrected where they stood,
here and in `groups.py`, with the measurement in `logs/p14-composite-cation.stdout.log`. The pattern
is the same one as the other two: an assertion about what the code would do, written from reading
rather than running, in a document whose every neighbouring number was measured.

## Which database every measurement used

There is **no `rmgrc` in this worktree root**, and none in `~/.rmg`. The only `rmgrc` on this
machine that could have been picked up is `/home/alon/Code/RMG-Py-plasma/rmgrc`, which pins
`database.directory = ../RMG-database-plasma/input` — the shared checkout — and RMG reads it only
when that is the current working directory, which it never was here.

Pinning was done three ways, all of them at this worktree:

| what | how it was pinned |
|---|---|
| every probe | `settings['database.directory'] = os.environ['I236_DB']` in-process, printed as the first line of every log |
| `pytest test/` | `test/conftest.py`, which pins to this repository's `input/` before any test module imports |
| `databaseTest.py` | a one-line `-p pin_db` plugin on `PYTHONPATH` |

Audited across every probe log: 7 runs resolved to
`/home/alon/Code/RMG-database-i236-radiative-root/input` and 1 to
`/home/alon/Code/RMG-database-i236-radiative-root/docs/superpowers/base_input`, the byte-verified
baseline copy inside this worktree. **No log mentions `RMG-database-plasma`. No measurement in this
branch was taken against the shared database.**

The `databasetest-run1-raced-my-own-edit` log is a different thing and is explained in full under
"The engine's database suite, pinned here": the suite was pinned correctly, all six tests passed,
and its pollution guard fired because I edited `rules.py` *inside this worktree* while it ran.

---

## The brief's prescription is wrong, and so was my first conclusion from that

Both defects reproduce exactly as reported. But the brief's Defect 1 says the root's `u0` is what
keeps `Ar+` out and implies that widening the radical count would make the family do
`Ar+ + e- => Ar`. **It would not.** `u0` is not an oversight; it is the recipe's own precondition,
and widening it makes the family generate a *different reaction* under this family's name.

`logs/p2-recipe-reach.stdout.log`, applying the family's own recipe
(`GAIN_RADICAL *1 1; LOSE_CHARGE *1 1`) to each centre:

| reactant | recipe builds | is that the RR product? |
|---|---|---|
| `Li+` `Li u0 p0 c+1` | `Li u1 p0 c0` | **yes** — neutral Li |
| `H+` `H u0 p0 c+1` | `H u1 p0 c0` | **yes** — H atom |
| `Ar+` `Ar u1 p3 c+1` | `Ar u2 p3 c0`, atom type **`Ar0e`** | **no** — `isomorphic to ground Ar? False` |
| `He+` `He u1 p0 c+1` | `He u2 p0 c0` | no |
| `Ar` (neutral) | `AtomTypeError` | — |
| `O` (neutral) | `AtomTypeError` | — |

The recipe realises exactly one transformation: **the captured electron enters an empty orbital**,
so `*1` gains one unpaired electron and loses one unit of charge with its lone pairs unchanged.
That is correct for a closed-shell cation, and it is why the root demands `u0`. `Ar+` has no empty
orbital — its captured electron must *pair*, `u1 p3 -> u0 p4` — and this recipe cannot do that.
A widened root would generate `Ar+ + e- => Ar(3P2)`, the metastable, and hand it the ground-state
rate rule in `rules.py`. That is strictly worse than matching nothing, because it is green.

So widening the sibling family's root is not the fix. **What I then got wrong was to conclude that
the reaction therefore could not be generated at all.** It can — by the family with the other
recipe, which is what `Plasma_Radiative_Recombination_Pairing` is. Verifier item 4 is satisfied; it
is satisfied by a second family rather than by this one.

The sibling library already records the direction of this, from I-234
(`input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py:363-371`): *"The family's
`GAIN_RADICAL` recipe is also the wrong direction for argon, whose recombination takes u1 -> u0."*
This ticket measures it, names the resulting species (`Ar0e`), and pins it in a test.

---

## Both defects, reproduced before anything changed

`logs/p1-baseline.stdout.log`, family loaded alone through `KineticsDatabase.load_families`:

```
family loaded: Plasma_Radiative_Recombination | electrons = -1
--- Ar+  (what RR consumes) : 1 Ar u1 p3 c+1
    0 reaction(s)
--- Ar   (neutral) : 1 Ar u0 p4 c0
    RAISES: rmgpy.exceptions.AtomTypeError: Unable to determine atom type for atom Ar.-,
    which has 0 single bonds, ..., 4 lone pairs, and -1 charge.
root group matches Ar+  (what RR consumes)   : False
root group matches Ar   (neutral)            : True
```

and on stderr, the failed product exactly as the brief quotes it:

```
ERROR:root:Could not update atomtypes for this molecule:
multiplicity -187
1 *1 Ar u1 p4 c-1
```

---

## Defect 1, measured: how wide is the exclusion?

**Denominator.** Every species entry in every thermo library in this database: 78 libraries,
**22,936** distinct species by adjacency list (`logs/p3-inventory-baseline.stdout.log`).

The charged part of that inventory is tiny, and worth stating because it is the denominator the
brief asks for:

| net charge | species |
|---|---|
| −1 | 1 (`electrocatLiThermo/electron`) |
| 0 | 22,929 |
| +1 | 6 |

**Of the 6 cations, the root excludes 3 for the `u0` reason: `PlasmaCationThermo/[Arp]`,
`[Hep]`, `[Nep]`** — every noble-gas cation in the database, and nothing else. The three it keeps
are `LithiumPrimaryThermo/[Lip]`, `electrocatLiThermo/proton` and `electrocatLiThermo/H3O`.

So the brief's "and by the same argument on any noble gas, and on any closed-shell species whose
cation is a doublet — which is most of them" is **true as a statement about chemistry and false as
a statement about this database**: the database carries six cations, and the exclusion costs three
of them. The generalisation is right about the world and overstates the local stake, and the local
stake is what a narrowing can be measured against.

---

## Defect 2, measured: it does not merely match neutral `Ar`

The root matched **22,915 of 22,936** species — 99.9% of the database. Of the 230,533 centres it
labelled across them, applying the recipe gave a typed molecule at 95,917 and raised
`AtomTypeError` at **134,616**. The crash is the majority outcome, not an argon curiosity. Neutral
`Ar`, `HF`, `F2`, `CH4` and 22,908 others all entered.

---

## The five candidate roots, measured side by side

`logs/p4-candidates.stdout.log`. `C0` is the root as it stood, and reproducing probe 3's
22,915/22,936 is the run's negative control — a harness that matched everything or nothing would
not land on that number. "centres" counts the mappings
`Molecule.find_subgraph_isomorphisms` returns, which is the call
`KineticsFamily._match_reactant_to_template` makes.

| candidate | group | species matched | of which net-neutral | of which cations | centres typed | centres raised |
|---|---|---|---|---|---|---|
| **C0** as it stood | `R u0 px c[0,+1,…]` | 22,915 | 22,912 | 3 | 95,917 | **134,616** |
| **C1** drop `c0` | `R u0 px c[+1,…]` | 617 | **614** | 3 | 5 | **670** |
| **C2** drop `c0` and `px` | `R u0 p0 c+1` | 607 | **604** | 3 | 3 | **662** |
| **C3** *(landed)* | `[H,Li,Na,K] u0 p0 c+1` | **3** | **0** | 3 | 3 | **0** |
| **C4** the brief's widening | `R ux px c[+1,…]` | 697 | 691 | **6** | 8 | **747** |

Two things decide the design here.

**Removing `c0` is not enough — not close.** C1 still admits **614 net-neutral molecules**, because
RMG groups match *subgraphs*: a charge written on `*1` constrains that atom and never the molecule
around it. Carbon monoxide's oxygen is `O u0 p1 c+1`; every nitro group's nitrogen is
`N u0 p0 c+1`; every organic azide has one too. There is no flag that fixes this.
`allowChargedReactants` is the wrong shape — it *forbids* charged reactants, and this family
*requires* one — and there is no `requireChargedReactants`.

**C4, the brief's fix, is the worst of the five.** It does admit all six cations, `Ar+` included —
so the brief's mechanism is real — but it adds 691 neutral molecules and raises at 747 centres, and
the argon reaction it would generate produces `Ar0e`, not argon.

**What makes C3 work is valence arithmetic, not charge.** For hydrogen and the alkali metals the
formal charge is `1 − 2p − u − bonds`, so `u0 p0 c+1` forces `bonds = 0`: the group can only ever
match a **bare, unbonded cation atom**, which is exactly what radiative recombination consumes. The
same `(u, p, c)` triple on C, N, O or a halogen is satisfied by a *bonded* atom inside a neutral
molecule — which is the whole of the 614.

**The arithmetic constrains one atom, and that is all it constrains.** An earlier draft of this
section concluded that the root "can only ever match a bare atomic cation", meaning a species that
is a lone atom. That over-reaches, and one of the three matches shows how: `electrocatLiThermo/H3O`
is a two-fragment species, and the root matches its unbonded proton, not the species. The correct
statement is that the root matches a bare cation **fragment**, which may sit inside a multi-fragment
species. What that costs is measured in the section below: nothing.

---

## The ending I chose, and why

**One recipe per family, therefore one family per recipe — three electron-capture recipes, three
families.** The brief offered three endings and the answer is a superset of its Ending 2:

| recipe | reaction | family |
|---|---|---|
| `GAIN_RADICAL + LOSE_CHARGE` | closed-shell cation → radical neutral, `Li+ -> Li` | `Plasma_Radiative_Recombination` — **narrowed here** |
| `LOSE_RADICAL + GAIN_PAIR + LOSE_CHARGE` | open-shell cation → closed-shell neutral, `Ar+ -> Ar` | `Plasma_Radiative_Recombination_Pairing` — **added here** |
| `LOSE_RADICAL + GAIN_PAIR` | neutral → mono-anion, `A + e- => A-` | `Plasma_Electron_Attachment` — **already existed** |

The argument is the recipe throughout. A family has exactly one, and the first implements "capture
into an empty orbital": correct for closed-shell cations, and *structurally incapable* of the
`A + e- => A-` stage its old docstring claimed — applied to a neutral closed-shell centre it builds
`X u1 p<unchanged> c-1`, which is the 134,616 `AtomTypeError`s. That stage was never homeless:
`Plasma_Electron_Attachment` is named for it, carries the pairing recipe, and already restricts its
tree to the three shapes it has data for.

Ending 1 as the brief framed it — split the root into two *branches* — cannot work, because two
stages need two recipes and a branch cannot carry one. Ending 3 — one group admitting `Ar+` and
excluding `Ar` — cannot work either: even if `Ar+` matched, this recipe's product would be the
metastable. But the thing Ending 1 was reaching for is right, and it is delivered as a second
family rather than a second branch.

Where this differs from the I-224 precedent, which is otherwise the same shape: I-224 could name
its chemistry with an existing atom type (`alkaline` is exactly Mg and Ca). There is no atom type
for "bare closed-shell atomic cation", so the root names elements and leans on valence arithmetic
to pin the bond count — the same device `Plasma_Electron_Attachment`'s `O_atom` group uses and
documents. I did **not** follow the attachment family into a `LogicOr` union with L2 children: its
union exists to express three *different shapes*, and to keep generated reactions off an averaged
root rule. Here every member is the same shape, differing only by element, which a single
element-union group states directly; and this family has one hand-written root rule and an empty
training set, so there is nothing for `fill_rules_by_averaging_up` to fabricate and no averaging
hazard to route around.

### What landed

```
 groups.py  entry A   1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]
                  ->  1 *1 [H,Li,Na,K] u0 p0 c+1

 groups.py  template(reactants=["A"], products=["A-"], ...)
                  ->  template(reactants=["A"], products=["A_reduced"], ...)

 groups.py  longDesc  rewritten: the `A + e- => A-` stage removed and referred to its owner;
                      the recipe's reach, the subgraph-matching trap, the rule for adding an
                      element, and the argon split all stated.
 rules.py   longDesc  two now-false sentences about the template's reach corrected. The rate
                      value, rank, units and provenance are untouched.

 NEW  input/kinetics/families/Plasma_Radiative_Recombination_Pairing/
                      groups.py, rules.py, training/{reactions.py,dictionary.txt}
                      the open-shell half; see its own section below.

 input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py
                      one prose paragraph: it quoted the old root verbatim. Corrected on the
                      owner's explicit instruction, after the brief's non-goal was scoped to
                      the library's entries and data. No entry, rate, source, species, index
                      or `electrons` value touched.
```

The tree is unchanged (`L1: A`), as are `electrons = -1`, the `(1, 0)` placement declaration,
`allowChargedSpecies = True`, the recipe, `reversible`, `reverse`, and the (empty) training set.

`Na` and `K` match nothing in this database today. They are in because they are the anchor's own
chemical class — singly charged light closed-shell cations, which `rules.py` says is where its one
number is most defensible — and because the campaign's alkali chemistry carries `Na+` on a branch
that has not landed. The rule for adding an element is now written in `groups.py` and enforced by a
test: its `u0 p0 c+1` state must be a bare atom, **and** `ATOMTYPES[element].decrement_charge` must
be non-empty or `LOSE_CHARGE` raises `ActionError` when the product template is built. `O`, `C`,
`Si`, `F`, `Cl`, `He`, `Ne` and `Cs` fail the second test today.

---

## Before and after, both directions

Against the 22,936-species inventory:

| quantity | before | after |
|---|---|---|
| species matching the root | 22,915 | **3** |
| — net-neutral | 22,912 | **0** |
| — cations | 3 | 3 |
| centres where the recipe raises `AtomTypeError` | 134,616 | **0** |
| cations in the inventory the root refuses | 3 of 6 | 3 of 6 (**unchanged**) |
| `generate_reactions([Ar])` | **raises `AtomTypeError`** | 0 reactions |
| `generate_reactions([Ar+])` | 0 reactions | 0 reactions (**unchanged**) |
| 12 family checks in `databaseTest.py`, one at a time | **12 of 12** | **12 of 12** |
| 2 depository checks | 2 of 2 | 2 of 2 |

**Which species entered, and which left.** The new root is a strict subset of the old one — `R`
admits every element, `px` every lone-pair count, and `c+1` is in the old charge list — so
**nothing entered**: 0 species. **22,912 left, and every one of them is net-neutral.** The three
cations that matched before still match: `LithiumPrimaryThermo/[Lip]`,
`electrocatLiThermo/proton`, `electrocatLiThermo/H3O`. The list of what left is 22,912 long and is
not reproduced; what characterises it exactly is "every species in the database except those
three".

**No cation gained or lost coverage.** That is the honest summary of the cation side: the narrowing
removes junk, and fixes nothing about argon. Argon radiative recombination is carried by the
sibling library entry `[Arp] => [Ar]` (index 1, landed I-234), which needs no family template, so
nothing in the campaign is blocked by the family's inability.

**What the family generates after the change** (`logs/p5-generation-after.stdout.log`, through the
shipped `generate_reactions` path, product asserted by isomorphism):

```
Li+  ->  1 reaction:  [Li+] => [Li]     product multiplicity 2 / 1 Li u1 p0 c0   isomorphic: True
H+   ->  1 reaction:  [H+]  => [H]      product multiplicity 2 / 1 H  u1 p0 c0   isomorphic: True
Na+  ->  1 reaction:  [Na+] => [Na]     product multiplicity 2 / 1 Na u1 p0 c0   isomorphic: True
Ar+  ->  0 reactions      Ar  -> 0 reactions      He+ -> 0 reactions
CO   ->  0 reactions      CH4 -> 0 reactions
```

---

## One residual over-match, recorded because no group can exclude it

`electrocatLiThermo/H3O` is **not** the hydronium ion. It is a van der Waals pair — water beside a
detached bare `[H+]`. As shipped, printed back from the loaded entry rather than retyped
(`logs/p14-composite-cation.stdout.log`):

```
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c+1          <- 2 connected fragments; atom 4 has bonds=0
```

The root matches atom 4, and nothing at the group level can stop it: group matching is subgraph
matching, so a disconnected spectator is invisible from `*1`. This is the species that makes the
"bare atomic cation" phrasing above wrong — the match is a bare cation *fragment* inside a
composite, and the family's three matches are therefore **two lone-atom species and one composite**,
not three lone atoms.

**What it costs, measured:** nothing. Both families return **0 reactions** from this entry.

```
                                          Plasma_Radiative_Recombination   ..._Pairing
electrocatLiThermo/H3O   [the question]          0 reaction(s)              0 reaction(s)
electrocatLiThermo/proton      [control]         1 reaction(s)              0 reaction(s)
LithiumPrimaryThermo/[Lip]    [pos. ctrl]        1 reaction(s)              0 reaction(s)
Ar+                           [pos. ctrl]        0 reaction(s)              1 reaction(s)
```

The positive controls run in the same loop on purpose: a harness that returned 0 for everything —
a mis-built family, a swallowed exception — would show 0 on those rows too, and the H3O row would
prove nothing.

**Why it is 0, named rather than inferred.** It is not that the root fails to match; it matches, and
the recipe builds at the centre. `find_subgraph_isomorphisms` returns exactly 1 mapping, and the
recipe applied there yields `H2O` plus an `H` atom — **two fragments against a one-product
template**. `apply_recipe` splits the product structure at `family.py:1516`, compares the count
against the template's, and returns `None` at `family.py:1532`; no reaction is emitted. The same
code path accepts `proton`, whose product is one fragment. This is the distinction a reaction count
alone cannot make, which is why the probe asks the recipe directly as well.

**No guard was added**, deliberately: a guard for a case that does not fire is a check that cannot
fail, which is the failure class this campaign keeps finding. This is an artefact of how that
species is declared in an electrochemistry library, not of this template — the same
disconnected-species hazard the campaign has already hit on the thermo side. It is recorded in
`groups.py` and here, rather than worked around.

---

## Finding: `kinetics_check_sample_can_react` could not fail here

This is the eighth unfailable check this campaign has found, and it is worth its own section
because it is the check whose *name* promises to catch exactly this defect — "Recipe applies to
group entry".

`logs/p7-sample.stdout.log`:

| root | `make_sample_molecule()` | recipe on the sample |
|---|---|---|
| old `R u0 px c[0,+1,…]` | `1 *1 H u0 p0 c0 {2,S}` / `2 H u0 p0 c0 {1,S}` — **H₂** | `H u1 p0 c-1` bonded to H — **types fine** |
| new `[H,Li,Na,K] u0 p0 c+1` | `1 *1 H u0 p0 c+1` — **H⁺** | `H u1 p0 c0` — H atom |

The old root's fabricated sample is molecular hydrogen with `*1` on one of its atoms, and the
recipe drives that to a bonded hydride radical, which RMG *can* type. So the check passed — while
the same recipe raised `AtomTypeError` at 134,616 real centres in the database the check had just
loaded. **General form:** `kinetics_check_sample_can_react` exercises one fabricated molecule per
group, chosen by `make_sample_molecule` to be as small as possible; for a wildcard group that
molecule is hydrogen, and hydrogen is the element least likely to expose a lone-pair or charge
defect. The check cannot fail in the direction a too-wide root fails. That is a referral to
RMG-Py, not a change here; this ticket's own tests do the job instead, by asserting against real
species from the database's own inventory.

Consistent with that: **all twelve family checks passed on the broken tree and on the fixed one**,
12/12 both sides (`logs/p6-checks-baseline.stdout.log`, `logs/p6-checks-after.stdout.log`). The
suite is not evidence for this change in either direction.

---

## Tests, and every one of them shown red

New file `test/test_plasma_radiative_recombination_family.py`, 17 tests (the pre-existing
`test_plasma_radiative_recombination.py` covers the *library* and is untouched). Two rules the
assertions follow, both aimed at the traps the brief names:

* **Assert the product by structure.** Every positive test isomorphism-checks the product molecule
  against the species the reaction must make; a count would pass against a family that never
  loaded.
* **Prove the family loaded, by a value, in the same test as every negative assertion.**
  `_family_is_really_loaded` checks `electrons == -1` and the root's label, and every
  "does not match" test additionally asserts the `Li+` positive control *in that test*, so a family
  that vanished cannot masquerade as a family that correctly refused.

Four mutations, each breaking exactly one thing the suite guards, each restored and verified
byte-identical afterwards (`probes/p8_red_runs.py`, `logs/p8-red-runs.stdout.log`):

| mutation | result |
|---|---|
| **M1** root reverted to the pre-I-236 `R u0 px c[0,+1,…]` | **7 failed**, 10 passed — including `[Ar]`, `[CO]`, `[CH4]`, `[HF]`, `[CH3NO2]` |
| **M2** root widened by one element, `[H,Li,Na,K,N]` | **3 failed**, 14 passed — the element-list guard and `[CH3NO2]` |
| **M3** recipe swapped to `LOSE_RADICAL + GAIN_PAIR` | **17 errors** — the family does not load at all (below) |
| **M4** `electrons = -1` → `electrons = 0` | **14 failed**, 3 passed |

Green afterwards: `17 passed` (`logs/green-run.stdout.log`), and the worktree's whole suite
`266 passed in 45.46 s` (`logs/worktree-suite-after.stdout.log`).

## The engine's database suite, pinned here — final run, both families present

```
6 passed in 517.43s (0:08:37)     EXIT 0        logs/databasetest-final.stdout.log
```

No pollution banner (nothing under `input/` was edited while it ran). Worktree suite after
everything, including the new family's 16 tests: `282 passed in 28.56s`
(`logs/worktree-suite-final.stdout.log`). The run below is the earlier one, kept because its
first attempt is a lesson.

## The engine's database suite, pinned here

`pytest -p pin_db /home/alon/Code/RMG-Py-plasma/test/database/databaseTest.py -q`, with a one-line
plugin setting `database.directory` to this worktree (the engine's own `rmgrc` points at the shared
checkout, so an unpinned run measures someone else's tree):

```
6 passed in 488.38s (0:08:08)     EXIT 0
```

`test_kinetics`, `test_thermo`, `test_solvation`, `test_statmech`, `test_transport`,
`test_metal_libraries`. `logs/databasetest-after.stdout.log`.

**A first run of this suite exited 1, and the reason was mine, not the database's.**
`logs/databasetest-run1-raced-my-own-edit.stdout.log`: all 6 tests PASSED, and then the suite's
own pollution guard fired —

```
DATABASE POLLUTION: the test suite modified the RMG-database checkout at ...
  modified .../Plasma_Radiative_Recombination/rules.py
```

— because I edited `rules.py` while the suite was running in the background. The guard compares the
tree before and after and cannot tell a test's write from mine. `git diff` on `rules.py` shows only
my own prose edit, with no reindexing or reformatting of the kind `Database.save` would leave, so
nothing was perturbed; the suite was re-run with nothing else touching the tree and is the `EXIT 0`
above. Both logs are kept. The lesson is the obvious one: do not edit under
`settings['database.directory']` while that suite is running.

---

## M3 was an authoring error, and reporting it as anything else was the mistake

M3 swapped the recipe to the pairing form and the family stopped loading. The exact failure:

```
rmgpy/data/kinetics/family.py:717   self.forward_template.products = self.generate_product_template(...)
rmgpy/data/kinetics/family.py:1077  product_structure = self.apply_recipe(reactant_structure, forward=True, unique=False)
rmgpy/data/kinetics/family.py:1403  self.forward_recipe.apply_forward(reactant_structure, unique)
rmgpy/data/kinetics/family.py:498   atom.apply_action(['LOSE_RADICAL', label, 1])
rmgpy/molecule/group.py:484 -> group.py:355
rmgpy.exceptions.ActionError: Unable to update GroupAtom due to LOSE_RADICAL action:
Invalid radical electron set "[0]".
```

Read it: `LOSE_RADICAL` was applied to a group declaring `u0`. M3 changed the recipe and **left the
root at `u0`** — it asked a group with no unpaired electron to lose one. That is a mutation I
authored badly, and it says nothing whatsoever about whether the recipe grammar can express
pairing capture.

`logs/p9-pairing-feasibility.stdout.log` applies each candidate recipe to each candidate *root
group*, which is exactly the call `generate_product_template` makes at load:

| root group | recipe | product template |
|---|---|---|
| `[H,Li,Na,K] u0 p0 c+1` | `LOSE_RADICAL + GAIN_PAIR` | **ActionError** — M3, reproduced |
| `Ar u1 p3 c+1` | `LOSE_RADICAL + GAIN_PAIR` | `Ar u0 p4 c+1` — loads, but the template says *cation* |
| `Ar u1 p3 c+1` | `LOSE_RADICAL + GAIN_PAIR + LOSE_CHARGE` | **`Ar u0 p4 c0`** — loads, and correct |
| `Ar u1 px c+1` | `LOSE_RADICAL + GAIN_PAIR` | `Ar u0 p[1,2,3,4] c+1` — loads |
| `[Ar,He,Ne] u1 px c+1` | `LOSE_RADICAL + GAIN_PAIR` | **ActionError**, and this one *is* a real limit — below |
| `Ar u1 p3 c+1` | `GAIN_RADICAL + LOSE_CHARGE` | `Ar u2 p3 c0` — the metastable |

**The recipe grammar expresses pairing capture without difficulty.** Root and recipe do have to
move together, which is the one true thing I took from M3.

### The third action, and why two is not enough

`LOSE_RADICAL + GAIN_PAIR` is sufficient on a **molecule**: `Atom.apply_action` carries the charge,
so `Ar u1 p3 c+1` → `Ar u0 p4 c0` with no charge action at all. It is *not* sufficient on a
**group**, because `GroupAtom.apply_action` leaves a declared charge alone — hence the `c+1` product
template in the table above, a template asserting that this family makes a cation.

Adding `LOSE_CHARGE` fixes the template and introduces a transient on the molecule side, measured:

```
3-action  AFTER RECIPE, BEFORE update()   u=0 p=4 c=-1  net=-1
3-action  AFTER update()                  u=0 p=4 c=+0  net=+0
```

`Molecule.update()` recomputes the charge back to 0, and `KineticsFamily.apply_recipe` calls
`update()` (`family.py:1561`) before any charge balance is checked — so the transient never reaches
the balance and the generated product is identical either way. It is written into the family's
`groups.py` because it is exactly the "recipe path fails open" hazard the attachment suite warns
about: a wrong intermediate that a later call silently repairs.

**The three-action recipe is therefore correct, and it is the recipe the family ships.**

---

## The second family: `Plasma_Radiative_Recombination_Pairing`

Added under `input/kinetics/families/Plasma_Radiative_Recombination_Pairing/`.

```
recipe   LOSE_RADICAL *1 1 ; GAIN_PAIR *1 1 ; LOSE_CHARGE *1 1
root     Ar_cation     1 *1 Ar u1 p3 c+1
product  Ar_neutral    1 *1 Ar u0 p4 c0        (generated by the recipe, verified at load)
tree     L1: Ar_cation
rules    one root rule, rank 10, A = 1.007892e+05 m^3/(mol*s), n = 0, Ea = 0
training empty, deliberately
electrons = -1 ; reversible = False ; allowChargedSpecies = True
```

**The split is a partition, and that was checked with both families loaded together** — which is how
a real run sees them, and the condition under which a bad split would generate the same reaction
twice (`logs/p11-pairing-family.stdout.log`):

```
Plasma_Radiative_Recombination             Ar+  -> 0 reactions
Plasma_Radiative_Recombination             Li+  -> 1 reaction
Plasma_Radiative_Recombination_Pairing     Ar+  -> 1 reaction
Plasma_Radiative_Recombination_Pairing     Li+  -> 0 reactions
```

Refused by the new family, each for a stated reason: neutral `Ar`, `Ar(3P2)`, `Li+`, `H+`, `He+`,
`Ne+`, `CH4`, `CO`. The root needs no narrowing of the kind the sibling did: argon's formal charge
is `8 - 2p - u - bonds`, so `u1 p3 c+1` already forces zero bonds and the group cannot reach inside
a molecule.

### The root is one element, and the limit is RMG-Py's atom-type table

`He+` and `Ne+` recombine by exactly this mechanism, both have thermochemistry in
`PlasmaCationThermo`, and neither can be in this tree:

```
Ar   decrement_radical=['Ar']   increment_lone_pair=['Ar']   decrement_charge=['Ar']
He   decrement_radical=['He']   increment_lone_pair=[]       decrement_charge=[]
Ne   decrement_radical=['Ne']   increment_lone_pair=[]       decrement_charge=[]
```

`GAIN_PAIR` needs a non-empty `increment_lone_pair` row on every atom type in the group, so a root
of `[Ar,He,Ne] u1 px c+1` raises at load:

```
ActionError: Unable to update GroupAtom due to GAIN_PAIR action:
Unknown atom type produced from set "[AtomType "Ar", AtomType "He", AtomType "Ne"]"
```

This is the same shape as I-224's finding that `ATOMTYPES['O']` has an empty `increment_charge` row.
It is an RMG-Py gap, it is named in `groups.py`, and it is pinned by a test that fails the day the
table is filled in — so the widening is prompted rather than forgotten.

### The rate rule

One root rule, the same construction the sibling family and the EII family use: the sourced library
number frozen at one working point, marked an estimate, rank 10.

```
source   PlasmaRadiativeRecombination index 1, [Arp] => [Ar]
         Shull & Van Steenberg 1982, ApJS 48, 95, Table 2 row AR1
         A_rad = 3.77e-13 cm^3/s, X_rad = 0.651, T0 = 1e4 K
k(Te)    1 eV  2.060725e+05      2 eV  1.312350e+05      3 eV  1.007892e+05   m^3/(mol*s)
frozen   3 eV = 34813.55 K, the argon deck's electron temperature   -> 1.007892e+05
```

Obtained from `TwoTemperaturePlasma.get_rate_coefficient_two_temp(300.0, 34813.55)` against the
pinned runtime, not transcribed (`logs/p10-rate-anchor.stdout.log`). The whole 1–3 eV span is
within a factor of 2.2, so the working point is not what dominates the error.

**What this form throws away is real**: the source *is* a Te power law and plain `Arrhenius` has no
`uses_electron_temperature` flag, so the family would evaluate it at the gas temperature. It
matters less than it looks only because the library covers every species this family matches today
and wins by library-over-family precedence, carrying the correct `TwoTemperaturePlasma`. That is
written into `rules.py` rather than left for someone to find.

### Where the missing RMG-Py registry entry actually bites — a claim of mine that failed

I wrote into the new family's `groups.py`, copying the sibling's wording, that an undeclared family
"raises `ElectronPlacementError` the moment it is asked to produce a reaction". **Measured, that is
false**, and the correction is now in both families' docstrings.

`logs/p11-pairing-family.stdout.log` runs generation twice, once with
`FAMILY_ELECTRON_PLACEMENT` exactly as RMG-Py ships it (this family absent) and once with the entry
injected in-process. **Both arms generate `Ar+ + e- => Ar` identically.** Generation never consults
the registry.

`logs/p12-placement-gate.stdout.log` finds the real gate — `resolve_electron_placement`, which the
plasma **reactor** calls at `rmgpy/solver/plasma.pyx:276` during `initialize_model`:

| | result |
|---|---|
| without the entry | `ElectronPlacementError` at `electron_placement.py:462`: *"Family 'Plasma_Radiative_Recombination_Pairing' has no electron-placement declaration … refusing to infer electron placement from the net electron count"* |
| with the entry, no rate on the reaction | refused at line 567 — a placement view cannot be certified for an unknown rate form |
| with the entry and the family's rule attached | **resolves**: `[Ar+] + e- => [Ar]`, electron placed on the reactant side |

So the database half is complete: the family loads, generates the right reaction, and passes every
check. **It cannot be *simulated* until one line lands in RMG-Py**, which is out of scope here:

```python
# rmgpy/electron_placement.py, FAMILY_ELECTRON_PLACEMENT
'Plasma_Radiative_Recombination_Pairing': (1, 0),
```

That is pinned by `test_known_limitation_the_family_generates_but_cannot_yet_be_simulated`, which
asserts the raise *and* asserts as its positive control that the sibling family IS declared — so a
broken import cannot make the test pass. It fails, deliberately, the day the entry lands.

### Tests for the new family, each shown red

`test/test_plasma_radiative_recombination_pairing.py`, 16 tests, `16 passed`. Five mutations
(`probes/p13_red_runs_pairing.py`, `logs/p13-red-runs-pairing.stdout.log`), each restored and
verified byte-identical:

| mutation | result |
|---|---|
| **N1** drop `LOSE_CHARGE` (recipe back to two actions) | 2 failed — the product template turns `c+1` |
| **N2** root widened to `[Ar,He,Ne] u1 px c+1` | 16 errors — family does not load, the He/Ne limit |
| **N3** recipe swapped to the sibling's | 3 failed — *still generates a reaction from Ar+*, and the product assertion catches it |
| **N4** root radical count `u1` → `u2` | 12 failed |
| **N5** rate anchor changed 1.007892e5 → 1.0e5 | 1 failed |

**N3 is the one that matters.** With the sibling's recipe the family still returns exactly one
reaction from `Ar+`, so any count-based test stays green. What fails is the structure assertion:

```
AssertionError: product is 'multiplicity 3\n1 Ar u2 p3 c0', expected ground-state argon
```

That is the metastable, caught by name.

The 12 family checks in `databaseTest.py`, run one at a time for the new family:
**12 of 12 pass**, plus 2 of 2 depository checks (`logs/p6-checks-pairing.stdout.log`). As with the
narrowing, that is not evidence — the same 12 passed on the broken sibling — which is why the
mutation table above exists.

---

## What this could not reach, and what it left stale

* **A real RMG run.** Every generation measurement is a direct `generate_reactions` /
  `generate_reactions_from_families` call on hand-built molecules. No job was launched, so nothing
  here shows what a live model does with the narrowed family — only what the family returns.
* **`add_rules_from_training`.** Not exercised. The training set is empty and `rules.py` carries one
  hand-written root rule, so the I-224 failure mode (an unreachable training entry crashing
  `main.py:590` while the suite stays green) has no trigger here — but that is an argument from the
  file's contents, not a measurement of the call.
* **Whether the retained chemistry is right.** This ticket measured *reach*, not chemistry. Whether
  `1.301428e+05 m³/(mol·s)` is defensible for `H+ + e- => H` is untouched; `rules.py` itself calls
  it an order-of-magnitude placeholder.
* **Rate selection.** `estimate_kinetics` was not called; no reaction generated above was asked for
  its rate.
* **Species outside the thermo libraries.** The 22,936-species denominator is every thermo library
  entry. Species that appear only in kinetics libraries or only as intermediates a model builds are
  not in it. The conclusion is not sensitive to this — the failure mode was matching *everything* —
  but the denominator is what it is.
* **The pairing family cannot be simulated yet**, and that is one line in RMG-Py, not a database
  gap. See the placement-gate section: generation, checks and tests are all green without it.
* **`He+` and `Ne+` radiative recombination is still not generable by anything** — the right family
  now exists and the atom-type table refuses to let them in. Both have thermochemistry in this
  database, so this is a live gap, not a theoretical one, and it is RMG-Py's to close.
* **`Plasma_Electron_Attachment` was read, not measured.** It is named as the owner of the
  `A + e- => A-` stage on the strength of its docstring, recipe and tree; no reaction was generated
  from it here, and no check was run to confirm that the species this family stopped matching would
  be correctly refused *there*. They would mostly be refused — its tree is three oxygen shapes —
  which is the point, but it was not measured.
* **The new family's rate rule was not compared against the library at the reactor.** The claim that
  library-over-family precedence makes the rule's missing Te dependence harmless for argon is
  precedence as documented, not precedence as observed in a run.
* **Two claims in this report were wrong when first written**, and both are corrected above rather
  than quietly edited: that `Ar+ + e- => Ar` could not be generated at all, and that an undeclared
  family raises `ElectronPlacementError` at generation time. Both were inferences; the measurements
  that overturned them were cheap and should have come first.
