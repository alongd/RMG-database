# Round 118 — the verification stopped one commit too early, and the derivation failed open

Branch `i221-argon-metastable-thermo`, base `a3ed93580`. Paired engine **`9b89a937c`**,
checked out and built at `/home/alon/Code/RMG-Py-mgr-i221-deck-probe-234349`.

Both HIGH are closed, all four MEDIUM are closed, both LOW are corrected. Two things the
brief did not name were found while measuring the two it did, and one of them is in this
round's own new probe.

Nothing in the thermodynamics or in the containment set was touched: both were confirmed
correct by the owner against NIST ASD and JANAF and by two independent measurements of the
template space, and this round hardens the *checks that carry them* rather than the
numbers.

---

## 1. What was measured, and with what

| run | result | log |
|---|---|---|
| three gated files at `a3ed93580`, paired engine | **80 passed** | `logs/round118-three-files-at-a3ed93580.log` |
| three gated files at this tip | **81 passed** | `logs/round118-three-files-after.log` |
| whole `test/` tree at this tip | **325 passed**, 0 failed | `logs/round118-full-suite.log` |
| `test_eii_quarantine.py` under the **advertised** pin | **2 failed, 16 passed** | `logs/round118-stale-pin-red.log` |
| undetermined-slot probe (2×2, base vs tip) | defect reproduced, repair holds | `logs/round118-undetermined-slot-probe.log` |
| witness probe, committed version at `a3ed93580` | **exit 0**, one family mislabelled SILENT | `logs/round118-witness-probe-red-at-a3ed93580.log` |
| witness probe at this tip | exit 0, the raise attributed, SILENT now 0 | `logs/round118-witness-probe-after.log` |
| tip re-verification | **exit 0** | `logs/round118-tip-reverification.log` |

Every run captured both streams. The counts: 58 + 18 = 76 tests in the two files the brief
measured, which is its "75 passed" plus this round's one new test; 5 more in
`test_argon_cation_buildtime.py`.

---

## 2. HIGH 1 — the verification re-established at the tip

`9c2e8fe27` is not an ancestor of the tip. Its rebased twin `025536186` is, and eleven
commits sit after it. **A verification stated in a commit message is attached to a commit,
and a rebase detaches it silently** — so the re-verification is written as a program:
`docs/argon-metastable-thermo/tip_reverification.py` reads the artifacts out of the working
tree, names the check covering each, proves that check still exists, and measures the
containment live. Run it at any commit and it answers for that commit. It exits 0 here.

| artifact | blob at tip | what it does | what checks it | what would catch it being wrong |
|---|---|---|---|---|
| eleven family `groups.py` barriers | see probe output | one `Ar_metastable_biradical` forbidden group each, at the template position the shipped matcher maps `Ar u2 p3 c0` onto | `test_every_family_whose_template_admits_the_metastable_is_forbidden`, `test_the_containment_does_not_move_the_chemistry_those_families_exist_for`, and now `test_a_template_slot_that_cannot_be_evaluated_refuses_the_derivation` | a barrier at the wrong position or missing from a matching family fails the **derived**-vs-contained comparison, not an enumeration of known families; a barrier that is too broad moves the family's own chemistry and fails the controls |
| `Plasma_Electron_Impact_Ionization/quarantine.py` | `5669cf4b962f` | declares the family quarantined for quantitative use, with the kinetics class the refusal keys on and the engine capability it requires | `test_this_runtime_ENFORCES_the_declared_engine_requirement`, `test_this_runtime_ENFORCES_the_pin_as_more_than_an_attribute_lookup` | both require a real exception out of the real admission path, so a manifest that parses and gates nothing fails; measured red under an engine that ignores the requirement fields (2 failed) |
| `PlasmaExcitedNeutralThermo.py` | `5246abc7bc21` | the one entry: Ar 4s `3P2`, `H298` from the ASD level energy, `S298 = ` JANAF `+ R ln 5`, `Cp = 5/2 R` | `test_h298_is_the_level_energy_times_hc_na`, `test_s298_is_the_ground_state_plus_the_exact_degeneracy_term`, `test_the_e0_gap_is_the_thermal_enthalpy_and_not_the_298_convention`, `test_the_entry_is_the_1s5_level_and_says_so`, `test_the_resonant_levels_are_excluded_on_lifetime_not_on_taste` | each number is re-derived from the identity that produced it, so a changed digit fails arithmetic rather than a remembered constant; the state identity is pinned separately, because an entry that drifted into meaning a different argon level would still load and still match |
| `test_argon_metastable_thermo.py` | `8298b096bbf7` | the executable half of `report.md` | its own red states and anti-vacuity controls | round 118 found the two that had neither — see HIGH 2 and MEDIUM 2 |
| `test_eii_quarantine.py` | `f60088106fab` | pins the quarantine gate behaviourally | as above | the pin it advertised named a runtime it fails on — MEDIUM 4 |
| `test_argon_cation_buildtime.py` | `f15639e2183a` | build-time refusals for the cation library | `test_at_build_time_with_the_reference_deck_argon_is_refused_loudly` | — |

**Measured live, not asserted from a table:** 140 families loaded, all eleven barriers
present and mapped onto the expected label (`*2` ×3, `*3` ×4, `*1` ×4), the metastable
caught by **11 of 11** (the anti-vacuity half), ground-state argon by **0 of 11**, a methyl
radical by **0 of 11**.

**What I could not re-verify.** The eleven `groups.py` diffs are re-verified *by behaviour*
— the barrier is present, correctly positioned, catches the metastable and nothing else —
not by reading each diff hunk against the family's own chemistry by hand. A barrier that is
correctly positioned and still wrong about some third species would pass everything here.
The controls cover each family's own reactions, which is the strongest available check
short of a full generation sweep per family.

---

## 3. HIGH 2 — the containment derivation failed open, and now refuses

`matching_slots()` caught every matcher exception into `MATCHER_ERRORS` and continued. Its
own `main()` was fatal on a non-empty list; the **test** was not, and the test is what runs
in CI.

Measured, 2×2, in `docs/argon-metastable-thermo/undetermined_slot_probe.py`:

| derivation | injected raise in `H_Abstraction` | verdict |
|---|---|---|
| committed at `a3ed93580` | no | complete (correct) |
| committed at `a3ed93580` | **yes** | **complete — 11 families derived, 2 matcher errors recorded and not asserted on** |
| working tree | no | complete (the repair costs nothing) |
| working tree | **yes** | **REFUSED** |

The injection goes into a family that is **not** in `CONTAINED_FAMILIES`, because the
defect is that an *omitted* family leaves the comparison true. Injecting into a contained
one would shorten the derived set and fail the comparison for the wrong reason — which
would look like the check working.

The repair is in the function, not at the call site: `matching_slots()` now **raises
`UndeterminedSlot` by default**, and a caller that wants a survey opts in with
`on_error='record'`. The one such caller, the derivation's `main()`, was already fatal on
the collection. A check that can only fail if its caller remembers to perform a second
check is a check that fails open.

### The census the brief asked for

**Sites in the three test files that record an error without asserting on it: two before
this round, zero after.** Both were `except Exception: pass` around
`add_rules_from_training` (MEDIUM 3). The complete enumeration of every exception handler
in the three files:

| site | shape | asserted on? |
|---|---|---|
| `test_argon_metastable_thermo.py:1918` (was ~1829) | `except Exception: pass` around `add_rules_from_training` | **no → removed this round** |
| `test_eii_quarantine.py:97` (was ~90) | same | **no → removed this round** |
| `test_argon_metastable_thermo.py:1599` | `except Exception: continue` in the `u`-sweep | **yes** — a refusal *is* the datum, and `assert built` is the positive control that stops the test reporting its own bug as a fact about the database. Named here because it is a swallow: an unrelated failure inside `from_adjacency_list` would read as "this `u` does not build". The positive control bounds it; it is not closed. |
| `test_argon_metastable_thermo.py:64`, `test_argon_cation_buildtime.py:67` | `except ImportError` widening `NO_NUMBER` to two exception classes | **yes** — deliberate cross-engine tolerance, and the tuple is what the assertions use |

Outside the three files but load-bearing for them: `MATCHER_ERRORS` in
`template_space_derivation.py` (closed this round) and `GENERATION_FAILURES` in
`template_witness_probe.py` (closed this round, MEDIUM 1).

---

## 4. MEDIUM

**1. The witness probe turned a generation failure into `SILENT` and exited 0.**
Reproduced on the committed version: `Surface_Adsorption_Double`, containment detached,
raises **`AtomTypeError`** — *not* `UntypeableStructureError` as the brief has it; the
adjacency list that reaches `update_atomtypes` carries `multiplicity -187` and no atom type
owns a double-bonded argon. The probe printed one line, returned `[]`, counted zero
reactions, listed the family `SILENT (template admits, no partner derived)` and exited 0.

Closed, **with one deviation from the brief, stated plainly**: the brief asks that a
generation failure cannot be reported as `SILENT` with exit 0. It is no longer reported as
`SILENT` — failures now have their own bucket, tagged by arm (`detached` / `attached` /
`control`). But making *any* raise fatal would have made this probe exit non-zero on every
run of this branch forever, because this particular raise is **expected and is itself the
containment's justification** — it is not that the family generates something unwanted, it
is that the species cannot be represented at all. A check that always fails detects nothing.
So the raise is **declared** in `EXPECTED_WITHOUT_CONTAINMENT`, by family and exception
type, with its reason; any undeclared raise, any raise in the attached or control arms, and
any declaration that stops firing (a stale declaration) are all fatal. The swallow became a
named expectation rather than an anonymous one.

**2. The `Q = 0` test manufactured its conclusion.** It built
`Conformer(..., spin_multiplicity=0)` itself and then asserted `Q == 0` — arithmetic about a
conformer the test wrote, green whichever way Arkane behaves. It now goes through
`arkane.input.species(structure=..., E0=...)` with **no** `spinMultiplicity`, so Arkane's own
default (`arkane/input.py:157`) produces the zero, and a contrast case with
`spinMultiplicity=5` returns `Q = 5` so the zero is attributable to the multiplicity rather
than to anything else about the species.

**3. `except Exception: pass` around `add_rules_from_training`, in both fixtures.** Removed.
Measured first, so the removal is not a guess: under the paired engine the call **does not
raise** and the EII training depository holds **zero entries** — the guard was protecting
nothing, and it would have hidden exactly the failure it was most likely to see, a training
reaction added later that does not load.

**4. The advertised pin named a runtime the tests fail on.** Reproduced: under
`RMG-Py-i222-metastable-argon-atomtype`, `test_eii_quarantine.py` gives **2 failed, 16
passed**, both failures being the engine-requirement enforcement pair. All three gated files
now name the paired engine `9b89a937c`, and so do the two probes' run lines — **three** stale
paths, not two: `test_argon_cation_buildtime.py:52` named `RMG-Py-i172-balance` and the brief
did not count it.

---

## 5. LOW

- `test_eii_quarantine.py:7` said 23.7 orders. Corrected to **20.93**, with the arithmetic
  (`log10(3.109200e7 / 3.664598e-14) = 20.9286`), the test that pins it, and *why* the old
  figure existed: it came from dividing by `PUBLISHED_EII_3EV = 2.0583e10`, a constant round
  59 could find no provenance for and round 77 withdrew from the assertion — the docstring
  kept quoting the number it had produced.
- `test_argon_metastable_thermo.py:20` said `E0 == H298`. Corrected to the real
  relationship: the entry states `H298 = 1114.2470` kJ/mol and states no `E0`; the derived
  `E0 = 1108.0496` sits `2.5RT = 6.1974` kJ/mol below it. Stated, not deleted, and pointed
  at the test that already measured it.

---

## 6. Found while measuring, not in the brief

- **My own re-verification probe's negative control could not be evaluated.**
  `Group.is_isomorphic(Molecule)` raises `TypeError`; the control was printing
  "ground-state argon forbidden in 0 of 11 — ok" while evaluating nothing. Its own
  `CANNOT VERIFY` guard caught it on the first run, which is the only reason this is a
  footnote rather than a finding in the next round. Fixed to
  `mol.is_subgraph_isomorphic(group)`, the direction the forbidden check itself uses, and
  an anti-vacuity line was added: the metastable must be caught by **11 of 11** or the two
  negative controls prove nothing.
- **A third stale runtime path** — see MEDIUM 4.

---

## 7. Named, not fixed

- `test_argon_metastable_thermo.py:1599`'s `except Exception: continue` — bounded by a
  positive control, not closed. See the census table.
- The throwaway worktree used for the red arm
  (`/home/alon/Code/RMG-database-r118-red`) had its checkout removed cleanly, but
  `git worktree prune` cannot unlink `.git/worktrees/RMG-database-r118-red`: **Device or
  resource busy** in this sandbox. The same error occurs on a pre-existing
  `RMG-database-i234-idcheck-tmp` entry, so it is an environment condition rather than
  something this round created. The entry is listed `prunable` and its working directory is
  gone; it needs one `git worktree prune` outside the sandbox.
- `report.md` still describes the verification as attached to a commit. Updating it is the
  last act before a merge, not before.
