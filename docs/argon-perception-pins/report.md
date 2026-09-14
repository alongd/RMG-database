# I-226 — Re-pinning four assertions against today's engine

**Headline: all four reds were tests doing their job, none was a database regression — and the
brief's framing was right about three of them and wrong in four specific factual details, each
corrected below by measurement.** The most consequential correction is that the *guarantee* the two
buildtime tests protected was **not uniformly lost**: for the dication it is **relocated and still
asserted**, for the dimer it is **partially lost** and now pinned as the smaller thing it is.

Everything below is measured against a freshly built engine at `fced5e836`, resolved to
`/home/alon/Code/RMG-Py-plasma/rmgpy/molecule/atomtype.cpython-39-x86_64-linux-gnu.so`. Logs are in
`docs/argon-perception-pins/logs/`; the probes that produced them are the three `probe_*.py` scripts
beside this file and are re-runnable.

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
| `ATOMTYPES['Ar'].specific` | `['Ar0', 'Ar0s', 'Ar+', 'Ar++']` — **4 leaves** |
| `'Ar' in nonSpecifics` | **False** (`nonSpecifics` is now `['He', 'Ne', 'e']`) |
| generic `Ar` | `single=[]`, `lone_pairs=[]`, `charge=[0, 1, 2]` |
| `Ar0` | `single=[0]`, `lone_pairs=[4]`, `charge=[0]` |
| `Ar0s` | `single=[1]`, `lone_pairs=[3]`, `charge=[0]` |
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

**The representational blocker is gone.** This inverts two claims in
`docs/i119-recombination-loss.md`: its headline *"blocked twice over"* is now half stale, and its
*"Data alone would not unblock it"* is **backwards** — data alone is now exactly what is missing.

The re-pin splits the old single test into three, because the old one could only say "nothing can be
stored" and there are now three separable facts:

1. `..._can_now_be_stored_and_the_remaining_blocker_is_data` — the inversion itself;
2. `..._with_the_wrong_electron_count_is_still_refused` (parametrized over "absent" and "+1") — the
   balance check became *reachable*, not *permissive*, which is what stops the lifted block from
   becoming a quiet way to ship an unbalanced reaction;
3. `test_this_repository_still_ships_no_three_body_coefficient` — **the new tripwire**, pointing the
   same way the old one did. It fires if anybody adds a three-body entry to
   `PlasmaRadiativeRecombination` (verified read-only: that library ships exactly one `entry(`, no
   `TwoTemperaturePlasma`, no `cm^6`), and sends them back to `i119`.

**What I deliberately did not claim.** That a stored three-body entry would be *correct*.
`TwoTemperaturePlasma` is a `k(T, Te)` law; three-body recombination is second order in the electron
density, and whether the reactor multiplies through by `n_e` the right number of times is an engine
question I did **not** measure — no reactor was run. Storing it is necessary, not sufficient. This
is flagged in the test docstring and in §5.

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

**R3 — `TwoTemperaturePlasma.electrons` is a `ScalarQuantity`, not an `int`, and compares unequal to
the integer it displays.** `repr()` shows `-1`; `law.electrons == -1` is **`False`**; there is no
`__int__`. This cost me one red test until I found that this repository already has the convention
(`kinetics.electrons.value == pytest.approx(-1)` for the rate law, plain `int` on
`Reaction.electrons`). It is a live trap for the next person, though **not** a defect — the balance
check reads it correctly, and my wrong-sign measurements prove the semantics work. Recorded so it is
not rediscovered.

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
| 1 | the two argon files green, counts against their own totals | **70 passed** (was `3 failed, 67 passed` — same 70 collected) |
| 2 | every rewritten assertion justified by a printed measurement | yes — §1, §3a, §4; logs named per assertion |
| 3 | each docstring records what changed and why the old pin was right | yes — all four rewritten docstrings carry a "what this was written for, and why it was right" section |
| 4 | guarantee question answered in the stated terms | yes — §3a **relocated, not lost**; §3b **partially lost** |
| 5 | whole `test/` run, every red listed | yes — §2 C4; the 4 reds named; now **221 passed, 0 failed** |
| 6 | `databaseTest.py` still `6 passed` | **6 passed** both against `RMG-database-plasma` and, re-run pinned, against this worktree (§6) |
| 7 | nothing under `input/`, nothing in `rmgpy/`, `git status` clean | see the close-out check |
| 8 | `stdout.log`/`stderr.log` for every measurement | yes — `docs/argon-perception-pins/logs/` |

Definition of done, per the tool:

```
$ bin/cross-repo-check --db <this worktree> --py /home/alon/Code/RMG-Py-plasma
  database : ... @ d1694dacd (i226-argon-perception-pins)
  engine   : ... @ fced5e836 (plasma)
  built    : 52 extension(s); atomtype -> .../atomtype.cpython-39-x86_64-linux-gnu.so
  pytest   : 221 passed, 568 warnings in 25.86s
  CLEAN -- every collected test in the database checkout passes against this engine.
  exit 0
```

221 = the previous 218 collected, plus 3 from splitting the tripwire into four tests.

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
