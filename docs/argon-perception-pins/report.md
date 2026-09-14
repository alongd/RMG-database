# I-226 — Re-pinning four assertions against today's engine

**Headline: all four reds were tests doing their job, none was a database regression — and the
brief's framing was right about three of them and wrong in four specific factual details, each
corrected below by measurement.** The most consequential correction is that the *guarantee* the two
buildtime tests protected was **not uniformly lost**: for the dication it is **relocated and still
asserted**, for the dimer it is **partially lost** and now pinned as the smaller thing it is.

> **Revision note (after adversarial review).** This report previously concluded that I-178 had
> lifted the representational blocker on three-body recombination so that *"data alone is now
> exactly what is missing"*. **That conclusion was wrong and is retracted in §4a.** Storage is not
> representability: the channel stores and then fails electron placement, because no owner declares
> the `(2, 1)` shape it needs — and a placement declaration is engine code, not data. I verified the
> correction myself rather than accepting it; the measurements are in
> `logs/probe_threebody_stdout.log`. Two further changes followed: the rate-order caveat I had filed
> as an open question is in fact an **active guard that refuses the entry** (§4b), and the data
> tripwire, which was a text grep that an `m^6` spelling could walk past, is now a semantic check
> (§4d).

Everything below is measured against a freshly built engine, resolved to
`/home/alon/Code/RMG-Py-plasma/rmgpy/molecule/atomtype.cpython-39-x86_64-linux-gnu.so`. Logs are in
`docs/argon-perception-pins/logs/`; the probes that produced them are the three `probe_*.py` scripts
beside this file and are re-runnable.

> **The engine moved during this ticket, and the new pin caught it.** Work began at the briefed tip
> `fced5e836`. Partway through, another session merged `i222-metastable-argon-atomtype`, taking
> `RMG-Py-plasma` to **`311818121`** and rebuilding the `.so` underneath me. The freshly written pin
> on argon's leaf list went red **within the hour**, on the appearance of a fifth leaf `Ar0e`
> (metastable argon; `single=[0]`, `lone_pairs=[3]`, `charge=[0]`). Nothing else moved — `Ar+`,
> `Ar0`, the dimer, the Ar(4+) refusal, the dication and the tripwire were all unaffected, and 220
> of 221 tests stayed green across the jump. The final state is pinned against **`311818121`**,
> because `cross-repo-check` — the stated definition of done — measures the live engine, and a pin
> against a tip that no longer exists is worth nothing. **Verifier item 1's "at `fced5e836`" is
> therefore not literally satisfiable any more**; §7 records both runs. The §1 table below is the
> `311818121` measurement; the four-leaf reading it replaced is in
> `logs/probe_stdout.log`, and the five-leaf one in `logs/probe_at_311818121_stdout.log`.
>
> This is the single most useful thing the ticket produced: it is direct evidence that an exact pin
> on a cross-repository coupling pays for itself, since the interval between writing it and its
> first true positive was under an hour.

---

## 0. The build, and a trap worth recording

The first build **reported success while having done nothing**:

```
$ python setup.py build_ext --inplace -j4 ...; echo "BUILD_EXIT=$?"
Cython (https://cython.org/) is required to build or install RMG Py.
ModuleNotFoundError: No module named 'Cython'
BUILD_EXIT=0
```

`python` resolved to base anaconda, which has no Cython, and `$?` reported the exit status of the
`tee` process-substitution wrapper rather than of `setup.py`. Had I trusted it, every measurement in
this report would have come from the *pre-existing* `.so` — precisely the failure mode the brief
warned about, arriving through a door the brief did not name. The real build needs
`PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH` and `${PIPESTATUS[0]}`, and yields 104 `.so`
files. **`cross-repo-check` is immune to this** — it verifies the `.so` exists and is not older than
its source — which is a point in favour of using it as the definition of done rather than a hand-run
`pytest`.

---

## 1. What argon actually is now (measured)

From `logs/probe_stdout.log`:

| | |
|---|---|
| `ATOMTYPES['Ar'].specific` | `['Ar0', 'Ar0s', 'Ar0e', 'Ar+', 'Ar++']` — **5 leaves** (4 at `fced5e836`) |
| `'Ar' in nonSpecifics` | **False** (`nonSpecifics` is now `['He', 'Ne', 'e']`) |
| generic `Ar` | `single=[]`, `lone_pairs=[]`, `charge=[0, 1, 2]` |
| `Ar0` | `single=[0]`, `lone_pairs=[4]`, `charge=[0]` |
| `Ar0s` | `single=[1]`, `lone_pairs=[3]`, `charge=[0]` |
| `Ar0e` | `single=[0]`, `lone_pairs=[3]`, `charge=[0]` — **new at `311818121`**, metastable argon |
| `Ar+` | `single=[0, 1]`, `lone_pairs=[3]`, `charge=[1]` |
| `Ar++` | `single=[0, 1, 2]`, `lone_pairs=[3]`, `charge=[2]` |

Perception of concrete species:

| adjacency list | result |
|---|---|
| `Ar` ground state `u0 p4 c0` | builds, atom type **`Ar0`** |
| `Ar+` `u1 p3 c+1` | builds, atom type **`Ar+`** (was generic `Ar`) |
| dication `u2 p2 c+2` (as the test spells it) | **`AtomTypeError`** — no leaf |
| dication `u0 p3 c+2` | builds, atom type **`Ar++`** |
| dimer `[Ar][Ar+]` (as the test spells it) | **builds**, atom types **`['Ar0s', 'Ar+']`** |
| nonsense `Ar(4+)` `u4 p0 c+4` | **`AtomTypeError`** — no leaf |

Both of the brief's "two things you will probably find" are confirmed for `Ar+`. **One is wrong**,
see §2.

---

## 2. Four corrections to the brief

The brief invited contradiction; here are the four.

**C1 — The dimer cation does *not* lack an atom type, and does not fail at construction.**
The brief says "the two constructions in `test_argon_cation_buildtime.py` have **no atom type at
all** on today's engine — which is why they raise `AtomTypeError` before ever reaching the
`DatabaseError` those tests were written to assert." That is true of the dication and **false of the
dimer**. The dimer builds cleanly as `Ar0s`–`Ar+` (`logs/probe_exact_stdout.log`, step 1). Its
`AtomTypeError` comes from much later and somewhere else: inside `get_thermo_data` →
`estimate_radical_thermo_via_hbi` → `saturate_radicals`, where HBI adds an H to the neutral argon
and produces an argon with **two** single bonds, which the `Ar0s` narrowing to `single=[1]` no
longer admits. This matters because it changes the answer to item 2 for that test: the species is
not unrepresentable, it is unreachable *through the thermo path*.

**C2 — The dication as spelled is the *physical ground state*, and the engine refuses it.**
`DICATION` is `u2 p2 c+2` — the `3P` ground term of Ar²⁺. The `Ar++` leaf admits `lone_pairs=[3]`
only, i.e. a closed-shell configuration. So the engine today admits a +2 argon that is **not** the
ground state and refuses the one that is. See the referral in §5.

**C3 — The first red is not the one the brief identifies as pre-dating the merge in its assertion
detail.** The brief is right that `test_argon_cation_thermo.py`'s pin was red for ~two weeks. But it
names the failing assertion as `assert ground.atoms[0].atomtype.label == 'Ar'` *"where `ground` is
built from the `Ar+` adjacency list"* — correct — while the reported symptom is
`AssertionError: assert 'Ar+' == 'Ar'`. Both halves check out; no contradiction. Recorded only
because I verified it rather than assuming.

**C4 — There were four reds, not three, and the fourth is a different animal.** Confirmed
independently before it was pointed out: `4 failed, 214 passed` across `test/`
(`logs/full_suite_stdout.log`). The fourth is **not a stale pin** — see §4.

---

## 3. The guarantee question, answered in the brief's terms

The brief asks, for both `AtomTypeError` cases: **equally good, better, or lost?** The two answers
differ, and collapsing them into one would have been the wrong report.

### 3a. The dication — **the guarantee is RELOCATED, and still asserted. Not lost.**

The guarantee was: *a nonsense charge-+2 argon reaches the thermo layer and is refused with a loud
`DatabaseError` naming `Ar++`, rather than handed a fabricated group-additivity number.*

The decisive measurement (`logs/probe_guarantee_stdout.log`) is that a +2 argon the engine **does**
admit still exists, and the thermo layer still refuses it exactly as before:

```
--- closed-shell +2 argon, u0 p3 c+2 ---
  BUILD OK        : Molecule(smiles="[Ar+2]") atomtypes=['Ar++'] net_charge=2
  THERMO RAISED   : DatabaseError: Unable to determine thermo parameters for atom
                    {'*': <Atom 'Ar++'>} in molecule <Molecule "[Ar+2]">: no data for
                    node R or any of its ancestors in database group.
    -> 'Ar++' in message : True
```

So the property is intact; only the adjacency list that reaches it changed. The re-pinned test now
asserts **both** halves — that the `3P` spelling dies at `AtomTypeError`, and that the closed-shell
spelling still earns the loud `DatabaseError`. Had I only swapped the expected exception type, this
guarantee would have been silently dropped while the test went green: the exact "green and wrong"
outcome this campaign keeps catching.

### 3b. The dimer — **the guarantee is PARTIALLY LOST. Say so plainly.**

The campaign-level property — *loud failure, never silent fabrication* — **holds**: the run aborts
and no number is invented. If that is the whole question, the new exception is **equally good**.

But the test guaranteed something more specific, and that part is gone. The old `DatabaseError`
demonstrated a fact about the **thermo database**: that it has no group for this species and says
so. Today the thermo database is **never consulted** — the molecule machinery fails first, inside
HBI saturation. The test can no longer witness the database's refusal; it can only witness that the
dimer is unreachable. **That is a smaller guarantee than the one it replaced**, and I have pinned it
as such (`pytest.raises(AtomTypeError)`, asserting on `'2 single bonds'` and `'+0 charge'`) rather
than dressing it up as equivalent.

One could argue the earlier failure is *better* because it fails faster. I do not think that holds
here: it fails faster at the cost of no longer testing the layer the test was written to test, and
the new failure's message points at an atom-type hole rather than at the missing thermo group — a
worse diagnostic for anyone who lands on it.

---

## 4. The fourth red — a tripwire that fired exactly as designed

`test_plasma_radiative_recombination.py::test_three_body_recombination_still_cannot_be_stored_at_all`
is **not** a stale pin, and must not be treated as one. Its own docstring said:

> *"This is a tripwire, not a wish: if RMG-Py gives `TwoTemperaturePlasma` an `electrons` field,
> this test fails, and whoever made that change is pointed at `docs/i119-recombination-loss.md` to
> finish the job with a sourced coefficient."*

The engine tip `fced5e836` is the merge **"give TwoTemperaturePlasma a signed-net electron count"**.
The tripwire fired for precisely its stated reason. Per the standing doctrine — *when a tripwire
refuses your construct, ask whether it caught a real defect or is a false positive, not how to get
past it* — this one **caught a real change**, and the correct response is to honour the "come back
here", which is what the re-pin does.

Measured (`logs/probe_guarantee_stdout.log`):

| | |
|---|---|
| `TwoTemperaturePlasma` has `electrons` | **yes**, default `0` |
| in `_NET_ELECTRON_KINETICS_CLASSES` | **yes** (`BadnellRRArrhenius`, `VoronovEIArrhenius`, `TwoTemperaturePlasma`) |
| three-body entry, `electrons=-1` | **STORES** — `kinetics.electrons.value == -1`, `reaction.electrons == -1` |
| three-body entry, no `electrons` | refused, `"was not balanced"` |
| three-body entry, `electrons=1` | refused, `"was not balanced"` |

### 4a. RETRACTED: "the representational blocker is gone, data alone is what is missing"

**An earlier revision of this report said exactly that. It is wrong, and this section replaces it.**
Adversarial review caught it, I verified the correction myself rather than taking it on trust, and
the measurement backs the reviewer on every point (`logs/probe_threebody_stdout.log`).

**Storage is not representability.** Being able to *persist* an entry says nothing about whether the
engine can *resolve* it into something a reactor can evaluate. Three-body recombination still cannot
be resolved, for a reason that is not data:

| step | result |
|---|---|
| `FAMILY_ELECTRON_PLACEMENT` size | **9 entries** |
| any declaration `(2, 1)` — the shape three-body needs | **None.** `[o for o, d in ... if d == (2, 1)] == []` |
| stored under an owner absent from the map | `ElectronPlacementError`: *"Family 'PlasmaThreeBodyRecombination' has no electron-placement declaration ... refusing to infer electron placement from the net electron count."* |
| forced under `PlasmaRadiativeRecombination`, declared `(1, 0)` | net matches (−1 = −1), but refused: *"built a view with 2 reactant(s), but its kinetics TwoTemperaturePlasma has a rate coefficient of order 3 ... the rate wrong by a factor of the electron density while the reaction looks well formed."* |

So the blocker count did **not** go two → one. It went **(no storage, no data) → (no placement
declaration, no data)**. A placement declaration is a line in `rmgpy/electron_placement.py`, not a
number from a paper — so "data alone" was wrong **in kind**, not merely in degree.

The engine states this itself, in the comment directly above `FAMILY_ELECTRON_PLACEMENT`, inside the
very table my test asserts membership in. Three-body recombination *"would declare `(2, 1)`. That
declaration is absent, but the reason narrowed with I-178 ... the storage blocker is lifted; what
remains absent is this placement declaration and a sourced third-order coefficient, neither of which
I-178 adds."* I had asserted membership in that dict without reading the paragraph above it.

**The honest statement**, which now appears in the test docstring, the module docstring and here:
I-178 lifted the **storage** blocker and **narrowed** the remaining ones; the channel is **still not
representable end to end**; what is missing is a **`(2, 1)` placement declaration in RMG-Py** *plus*
a **sourced third-order coefficient**.

### 4b. The rate-order caveat was real, and I undersold it

My first report framed "does the reactor multiply through by `n_e` correctly?" as an unmeasured
engine question. **It is not an open question — it is an active guard that refuses the entry**, at
`electron_placement.py:704-720`, and its own message names the failure mode: *"the rate wrong by a
factor of the electron density while the reaction looks well formed."*

This matters more than a caveat, because the `(1, 0)` declaration's **net is identical** to what a
three-body entry needs (−1). Net-charge balance alone therefore cannot distinguish them; only the
incident order can, and the order check is what catches it. An attempt to smuggle three-body
recombination in under the existing declaration does not silently produce a wrong rate — it is
refused. That is now pinned, not merely noted.

### 4c. What the five tests cover

The old single test became five, because it could only say "nothing can be stored":

1. `..._can_now_be_stored_and_the_remaining_blocker_is_data` — storage works; `(2, 1)` is absent;
2. `..._with_the_wrong_electron_count_is_still_refused` (parametrized over "absent" and "+1") — the
   balance check became *reachable*, not *permissive*;
3. `..._has_no_placement_declaration_and_cannot_resolve` — **new**; the named placement failure;
4. `..._trips_the_rate_order_guard` — **new**; the order refusal, quoting its own message;
5. `test_this_repository_still_ships_no_three_body_coefficient` — the data tripwire, rebuilt (§4d).

### 4d. The tripwire was a text grep, and could be walked past

Review flagged that the first version read `reactions.py` as characters — `entry(` count of one, no
`TwoTemperaturePlasma`, no `cm^6`. That is defeated by a coefficient in `m^6`, by a different
kinetics class, and most likely of all by **editing the existing entry to third order without adding
a second `entry(`**.

It now loads the library and asks the engine for the order implied by the coefficient's units.
Measured (`logs/probe_threebody_stdout.log` §D): `get_plasma_rate_order` returns `3` for all four
third-order spellings — `cm^6`/`m^6`, per mole and per molecule — and `2` for second-order ones. An
unrecognised unit returns `None`, which the test also refuses, since an order the engine cannot
determine must not pass silently.

A mutation test confirms the fix is not cosmetic (`logs/tripwire_mutation_stdout.log`):

| mutation (edit the existing entry, no new `entry(`) | new tripwire | old grep |
|---|---|---|
| `cm^6/(molecule^2*s)` | **FAIL (order 3)** | FAIL |
| `m^6/(molecule^2*s)` | **FAIL (order 3)** | **pass — walked past** |
| `m^6/(mol^2*s)` | **FAIL (order 3)** | **pass — walked past** |
| unmutated (shipped `BadnellRRArrhenius`, order 2) | pass | pass |

---

## 5. Referrals to RMG-Py — findings, not edits

Nothing in `rmgpy/` was touched. Three items belong to the engine owner.

**R1 — `Ar++` admits the wrong electronic configuration.** The leaf is `lone_pairs=[3]`,
`charge=[2]`, i.e. closed-shell. The physical ground state of Ar²⁺ is `3P` = `u2 p2 c+2`, 2 lone
pairs, which now has **no atom type at all**. The engine admits a +2 argon that is not the ground
state and refuses the one that is. If plasma chemistry ever needs Ar²⁺ as a real species rather than
as a nonsense-input probe, this blocks it.

**R2 — the `Ar0s` narrowing to `single=[1]` is invisible to HBI saturation.** HBI manufactures
valences the narrowing never considered: saturating the Ar₂⁺ radical produces a neutral argon with
**two** single bonds, which no leaf admits, so `saturate_radicals` raises instead of returning a
saturated structure. Any radical argon species reached through the HBI path will hit this. Note the
asymmetry — `Ar++` *does* allow `single=[0, 1, 2]`, so two bonds are admissible at +2 but not at 0.
Whether that is intended is the engine's call.

**R0 — the `(2, 1)` placement declaration for three-body recombination is absent.** This is the
blocker that replaced the storage one, and it is engine work: a line in `FAMILY_ELECTRON_PLACEMENT`.
Until it lands, no three-body entry can resolve no matter how good its coefficient is. The engine's
own comment already names it as outstanding; nothing in this branch changes that, and nothing in
this branch should.

**R3 — `TwoTemperaturePlasma.electrons` is a `ScalarQuantity`, not an `int`, and compares unequal to
the integer it displays.** `repr()` shows `-1`; `law.electrons == -1` is **`False`**; there is no
`__int__`. This cost me one red test until I found that this repository already has the convention
(`kinetics.electrons.value == pytest.approx(-1)` for the rate law, plain `int` on
`Reaction.electrons`). It is a live trap for the next person, though **not** a defect — the balance
check reads it correctly, and my wrong-sign measurements prove the semantics work. Review adds the
mechanism: `Reaction.electrons` is copied as a plain value at `library.py:612`, which is why the two
compare differently. Recorded so it is not rediscovered.

---

## 5b. What `docs/i119-recombination-loss.md` should say — recommendation, not an edit

It is **not** edited from this branch. Two of its lines are now inaccurate in detail, and one that I
previously called wrong is in fact correct:

| line | status | recommended wording |
|---|---|---|
| *"blocked twice over"* | **still true in count**; the second blocker changed identity | keep the count; replace the second blocker *"it **cannot be stored at all**"* with *"it has **no `(2, 1)` electron-placement declaration**, so it stores but cannot resolve"* |
| *"the only Te-aware third-order rate law carries no electron count and the loader therefore refuses it as unbalanced"* | **stale since I-178** | *"I-178 gave `TwoTemperaturePlasma` a signed-net `electrons` field, so such an entry now loads; it then fails electron placement, and — forced under the `(1, 0)` radiative declaration — is refused by the rate-order guard"* |
| *"Data alone would not unblock it"* | **correct; I was wrong to call it backwards** | leave exactly as it stands |

Its §8 argument (every volume recombination channel is higher order in `n_e` than the source) is
untouched by any of this and needs no change.

---

## 5c. Known fragility in the dimer re-pin

Accepted by review as-is, recorded here so whoever moves the code finds it. The dimer test now pins
`pytest.raises(AtomTypeError)` on a failure raised inside `estimate_radical_thermo_via_hbi` →
`saturate_radicals`. That ties the test to an **implementation detail of the HBI path**, which is
more fragile than the `DatabaseError` it replaced: any rework of how RMG saturates radicals, or of
where thermo estimation gives up, will move or remove this exception and turn the test red without
anything about argon having changed.

If that happens, the question to ask is the one this ticket asked: *is the dimer still refused
loudly and not fabricated?* If yes, re-pin to wherever the refusal now lives. The test asserts on
`'2 single bonds'` and `'+0 charge'` precisely so the next reader can tell whether they are looking
at the same underlying refusal in a new place, or at a genuinely different outcome.

---

## 6. A cross-checkout hazard found while satisfying the Verifier

`test/database/databaseTest.py` lives in the **engine**, and resolves its database from an `rmgrc`
in the current working directory. Run the obvious way — from `/home/alon/Code/RMG-Py-plasma` — it
therefore measured **`/home/alon/Code/RMG-database-plasma`**, the shared primary checkout, and *not*
this worktree. A "6 passed" from that run says nothing about the database I changed. This is exactly
the hazard `test/conftest.py` in this repository was written to prevent for the local suites, and it
is unguarded for `databaseTest.py`.

That run also tripped the suite's own pollution guard, reporting three files modified under
`RMG-database-plasma`. **No damage**: `git diff` in that checkout is empty — the files were rewritten
byte-identically and only their mtimes moved. (The two untracked `Seed/`, `Seed_edge/` directories
there are dated 2026-08-27 and are not mine.) Nothing was reverted because nothing changed.

Item 6 was therefore re-run **pinned to this worktree** via an `rmgrc` in a scratch cwd, which is
the run that actually answers the Verifier. Both results are in §7.

---

## 7. Verifier

| # | Item | Result |
|---|---|---|
| 1 | the two argon files green, counts against their own totals | **70 passed** (was `3 failed, 67 passed` — same 70 collected). Pinned against `311818121`, not `fced5e836`; see the note at the top |
| 2 | every rewritten assertion justified by a printed measurement | yes — §1, §3a, §4; logs named per assertion |
| 3 | each docstring records what changed and why the old pin was right | yes — all four rewritten docstrings carry a "what this was written for, and why it was right" section |
| 4 | guarantee question answered in the stated terms | yes — §3a **relocated, not lost**; §3b **partially lost** |
| 5 | whole `test/` run, every red listed | yes — §2 C4; the 4 reds named; now **223 passed, 0 failed** |
| 6 | `databaseTest.py` still `6 passed` | **6 passed** both against `RMG-database-plasma` and, re-run pinned, against this worktree (§6) |
| 7 | nothing under `input/`, nothing in `rmgpy/`, `git status` clean | see the close-out check |
| 8 | `stdout.log`/`stderr.log` for every measurement | yes — `docs/argon-perception-pins/logs/` |

Definition of done, per the tool:

```
$ bin/cross-repo-check --db <this worktree> --py /home/alon/Code/RMG-Py-plasma
  database : ... @ <rework tip> (i226-argon-perception-pins)
  engine   : ... @ 311818121 (plasma)
  built    : 52 extension(s); atomtype -> .../atomtype.cpython-39-x86_64-linux-gnu.so
  built    : atomtype .so is 12 min old and not older than its source
  pytest   : 223 passed, 568 warnings in 27.63s
  CLEAN -- every collected test in the database checkout passes against this engine.
  exit 0
```

223 = the original 218 collected, plus 5 from splitting the single tripwire into six items (storage,
two wrong-sign cases, the missing placement declaration, the rate-order guard, and the data
tripwire).

Three `cross-repo-check` runs are in `logs/`, and the middle one is the interesting one:

1. at `fced5e836`, after the re-pins — `221 passed`, exit 0;
2. at `311818121`, before the `Ar0e` re-pin — `1 failed, 220 passed`, exit 1, naming
   `test_argon_atom_type_resolves_to_a_specific_leaf_and_no_longer_parses_any_charge`. This is the
   new pin catching a real engine change, unprompted, within the hour;
3. at `311818121`, after it — `221 passed`, exit 0;
4. at `311818121`, after the post-review rework — **`223 passed`, exit 0**. This is the final state.

---

## 8. One loose end the next person should know about

Renaming the three argon tests leaves two **dangling references** in
`docs/i157-plasmaalkali/report.md` (lines 213 and 318), which cite
`test_argon_atom_type_now_declares_a_charge_envelope_but_still_parses_any_charge`. I did **not**
edit that report: it is a historical record of a run that happened, and the name it cites was correct
then. The mapping is:

| old name | new name |
|---|---|
| `test_argon_atom_type_now_declares_a_charge_envelope_but_still_parses_any_charge` | `test_argon_atom_type_resolves_to_a_specific_leaf_and_no_longer_parses_any_charge` |
| `test_the_dication_builds_and_raises_the_loud_databaseerror` | `test_the_dication_no_longer_builds_but_the_loud_refusal_survives_on_the_spelling_that_does` |
| `test_the_dimer_cation_builds_and_raises_the_loud_databaseerror` | `test_the_dimer_cation_still_builds_but_is_now_refused_one_layer_earlier` |
| `test_three_body_recombination_still_cannot_be_stored_at_all` | `test_three_body_recombination_can_now_be_stored_and_the_remaining_blocker_is_data` (+2 siblings) |

The names were changed because each old name asserts, in words, something now measurably false —
a test whose name lies is worse than one that is merely red.
