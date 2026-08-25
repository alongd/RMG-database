# I-111 — Reclassifying `Cation_R_Recombination` as a legacy SEI family

**One line.** `Cation_R_Recombination` is a lithium-ion-battery SEI family that this project has
been reading as plasma chemistry; this ticket makes the repository say so permanently, keeps the
family out of every plasma configuration, leaves it working inside the electrochemical one, changes
no science, and pins all of it with tests.

The label, verbatim, and it is not "validated":

```
LEGACY SEI ELECTROCHEMISTRY — INCOMPLETE QUANTITATIVE PROVENANCE
```

The evidence base is `docs/i103-electrochemical-provenance.md` on branch
`i103-electrochem-provenance` (commit `069ea3d0b9a56ebfb9db936defc4d2294bf6b0db`, blob
`483733f7535407b87446d9e5d18e76779efcf875`, SHA-256 of the file as committed
`d6d2e6511c2549d24e369eb13e51b6dae0ef3c6ff53fd19c1e25184c7bc132c2`). Nothing here re-derives it;
the recovered facts are restated beside the family, where a reader will be standing.

---

## 1. Environment and pins

| Role | Path | Pin |
|---|---|---|
| Data under test (the only thing written) | `/home/alon/Code/RMG-database-i111-sei` | branch `i111-sei-reclassification`, base `fb3c13c60` |
| Runtime, primary | `/home/alon/Code/RMG-Py-plasma` | branch `plasma`, `a61dc1303`, unmodified, not rebuilt |
| Runtime, second (carries the I-102 quarantine gate) | `/home/alon/Code/RMG-Py-i102-quarantine` | branch `i102-quarantine`, unmodified, not rebuilt |

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-plasma python -c "import rmgpy; print(rmgpy.__file__)"
/home/alon/Code/RMG-Py-plasma/rmgpy/__init__.py
```

`database.directory` was pinned to **this** worktree for every run, never to the shared
`RMG-database-plasma`. RMG's `rmgrc` resolution ends in a bare `return` and falls back silently, so
the pin was made in-process by a one-line pytest plugin and printed:

```
pinned to: /home/alon/Code/RMG-database-i111-sei/input
```

Nothing was built. `make` was not run in any form. No file was written to `/home/alon/Code/RMG-Py`,
`/home/alon/Code/RMG-Py-plasma`, `/home/alon/Code/RMG-Py-i102-quarantine`,
`/home/alon/Code/RMG-database-plasma`, or any other worker's worktree; both runtimes were read only
and both have unmodified tracked trees.

## 2. Which mechanism: extend I-102, not a second gate

**Chosen: extend.** I-102 landed a quarantine marker in the database
(`input/kinetics/families/Cation_R_Recombination/quarantine.py`, on branch `i102-quarantine-db`) and
a loader plus a hard-fail gate in RMG-Py (`rmgpy/data/kinetics/quarantine.py`, invoked at three
model boundaries in `rmgpy/rmg/model.py`). That marker is the right shape for this ticket's
plasma-domain limitation and it already covers exactly these entries by a criterion computed from
the data.

`i102-quarantine-db` was `fb3c13c60` + 1 commit — a direct descendant of this ticket's base — so the
marker was **cherry-picked onto this branch unchanged** (`7d4f47d3a`) and then extended in place.
There is one marker, not two. A second gate on the same twelve entries would have been worse than
either alone: two refusal paths, two states, and no way for a reader to tell which one is in force.

**The two limitations are separate, and the marker now carries both.**

| limitation | field | what enforces it |
|---|---|---|
| **2a — plasma-domain exclusion** | `state = "QUARANTINED FOR QUANTITATIVE PLASMA USE"` (I-102) | the RMG-Py gate where the runtime carries it; declared configuration where it does not (§4) |
| **2b — incomplete provenance** | `classification = "LEGACY SEI ELECTROCHEMISTRY — INCOMPLETE QUANTITATIVE PROVENANCE"` (this ticket) | documentation and tests; it is a statement about the data, not a gate, and it holds **inside** the SEI domain too |

A consumer that supplies an electrode and a reference lifts 2a and still does not get validated
data. That is why the second label exists rather than being folded into the first.

## 3. Every place changed, named

Four files in this repository. Nothing anywhere else.

| file | what changed | why here |
|---|---|---|
| `input/kinetics/families/Cation_R_Recombination/quarantine.py` | cherry-picked from I-102, then extended with `classification`, `domain`, `isPlasmaFamily = False`, `familySets`, `provenance`, and a `longDesc` note on where the gate does and does not exist | the machine-readable record, beside the data |
| `input/kinetics/families/Cation_R_Recombination/PROVENANCE.md` | **new** — the full recovered context (§5 below lists what it must contain) | documentation where a reader inspecting the family will be standing |
| `input/kinetics/families/Cation_R_Recombination/groups.py` | `shortDesc` and `longDesc` filled — both were empty strings | RMG loads and renders these; it is the family's own self-description |
| `input/kinetics/families/recommended.py` | comment above `'Cation_R_Recombination'` inside the `electrochem` set | where a reader choosing a family set looks |
| `test/test_cation_r_recombination_sei.py` | **new** — 18 tests | §6 |
| `docs/i111-sei-reclassification.md` | **new** — this file | the report |

**The inventory correction, stated precisely.** The dispatch asks that if the family is counted among
the plasma families, that count be corrected. **In this repository it is not, and that was checked
rather than assumed.** `input/kinetics/families/recommended.py` defines eight curated sets —
`default`, `ch_pyrolysis`, `liquid_peroxide`, `surface`, `halogens`, `surface_development`,
`electrochem`, `surface_CO2` — and the word "plasma" does not appear in the file at all. The family
is a member of exactly one set, `electrochem`, which is already correct; it is in the union of no
other. So there was no plasma count here to decrement. What was missing was the *statement* — the
sets carried the right answer and said nothing about why — and that is what §3's four files add.

**Where the miscount actually lives is outside this repository**, and §7 records it rather than
fixing it out of scope.

## 4. The plasma-domain exclusion, and the structural limitation it rests on

**This database has no formal plasma domain-selection mechanism.** There is no `plasma` family set;
even `Plasma_Electron_Attachment`, the one genuinely plasma family here, belongs to no set. The
dispatch anticipates exactly this and rules: enforce what can be enforced, **document the structural
limitation, and do not expand it into a general domain-typing redesign.** Adding a `plasma = {...}`
set would be that redesign — it would require deciding, as a chemistry matter, which of 135 families
a plasma model should load, which this ticket does not own. It was not done.

What enforces the exclusion, therefore, is a pair, and which half is load-bearing depends on the
runtime:

1. **Declared configuration, always.** The family is in `electrochem` and in no other curated set.
   Any deck that selects families by set — which is how the SEI examples and the `default`-based
   decks do it — cannot reach it from a plasma configuration.
2. **Explicit failure, where the gate exists.** Under a runtime carrying
   `rmgpy/data/kinetics/quarantine.py`, all twelve objects are `Marcus`, the manifest's criterion is
   `Marcus`, and every one of them refuses at kinetics estimation, core admission and edge
   admission. Measured, against this worktree's manifest:

   ```
   QUARANTINED FOR QUANTITATIVE PLASMA USE: refusing to admit a quarantined rate at admission to the model core.
     family:             Cation_R_Recombination
     provenance:         Cation_R_Recombination/training entry 2 "CH3 + Li <=> CH3Li"; rank 3; template [Root_2R->C]; …
     reaction:           [Li+] + [CH3] <=> [Li][CH3]
     kinetics class:     Marcus
     reason:             electrochemical reference/domain unavailable
     quarantine record:  /home/alon/Code/RMG-database-i111-sei/input/kinetics/families/Cation_R_Recombination/quarantine.py
   This reaction is not being dropped, averaged, zeroed, reversed, made irreversible, or given a
   substitute rate …
   ```

**The limitation, stated plainly rather than papered over.** The gate is **not present in every
plasma runtime.** `/home/alon/Code/RMG-Py-plasma` (branch `plasma`) — the runtime this ticket was
pinned to, and the one the plasma line of work uses — has no
`rmgpy/data/kinetics/quarantine.py` and no `QuarantinedKineticsError`. Under it the manifest is an
inert data file and no refusal fires. Two residual holes follow, and neither is closable from this
repository:

- **A plasma deck that names the family individually** — rather than selecting a set — bypasses the
  declared-configuration exclusion, and under a gateless runtime bypasses everything. One such deck
  exists (§7).
- **Merging the I-102 loader into the plasma runtime** is what closes this properly. That is an
  RMG-Py change on a branch this ticket does not own, and the dispatch requires such a change to be
  raised before it is made. It is raised here and not made.

The manifest itself now records the absence, so it cannot be silent: a reader who finds the file and
assumes a gate is reading a file that tells them otherwise. `test_a_plasma_consumer_cannot_silently_receive_a_marcus_rate`
asserts on both branches — refusal where the gate exists, declared configuration plus the documented
absence where it does not — and skips in neither, because a skip here is indistinguishable from a
pass.

## 5. What is documented beside the family

`input/kinetics/families/Cation_R_Recombination/PROVENANCE.md`, in the family directory, records
every item the dispatch requires, and `test_the_recovered_physical_domain_is_documented_beside_the_family`
asserts each one is present rather than trusting that it was written:

original physical domain (lithium-ion battery SEI electrochemistry) · the surviving
`examples/rmg/SEI_pure_EC/input.py` path · reactor type (`liquidSurfaceReactor`, S/V = 1.0e5 m⁻¹) ·
solvent (ethylene carbonate, ε = 95.3, n = 1.420; ACN in the variant model) · temperature
(298.15 K) · the Li(110) metal electrode · declared potentials (`liqPotential = −1.0 V`,
`surfPotential = 0.0 V`; +0.3 V / 0.0 V in the ACN model) · the recovered sign/reference information
(the two incompatible Li⁺ references 502 kJ/mol apart, the computational-lithium-electrode
convention quoted from its own header, and the finding that `V0` is not a field of `Marcus` in either
implementation so the reference silently defaults to 0.0) · the original Julia rate law verbatim,
its commit, and the author's own ORR reference case for it · source references recovered
(doi:10.1021/acsomega.7b01425 for the four-point method; the RMS commits; the electrode-convention
header) · historical commits and author attribution · **the twelve-to-five genealogy** · the four
unresolved facts · the explicit prohibition on plasma use · and the path and hashes for the complete
evidence.

**The twelve-to-five genealogy** is recorded and, in the test suite, *recomputed*: seven rate rules
plus five training entries is twelve objects; each rule's `lmbd_i_coefs` is reproduced as the
arithmetic mean of the training entries it was fitted from — bit-exact for the four single-source
rules, within six-significant-figure rounding for the three multi-source ones. The seven rules
introduce no information the five calculations do not already contain, and `A = 1.73e6` / `n = 2` are
identical across all twelve and so carry none at all.

## 6. Verification

### 6.1 The five checks the dispatch requires

| # | requirement | test | result |
|---|---|---|---|
| 1 | the alkali-plasma configuration does not load or generate from this family | `test_the_alkali_plasma_configuration_neither_loads_nor_generates_this_family`, `test_the_family_belongs_to_no_plasma_facing_curated_set` | PASS — the family is absent from the loaded set, and Li⁺ + •CH₃ and Li⁺ + •NH₂ generate **0** reactions from it |
| 2 | no plasma mechanism silently receives one of its Marcus rates | `test_a_plasma_consumer_cannot_silently_receive_a_marcus_rate`, `test_the_quarantine_criterion_covers_all_twelve_objects` | PASS on both runtimes — explicit `QuarantinedKineticsError` where the gate exists; declared configuration + documented absence where it does not. Criterion coverage **12 of 12** |
| 3 | the exclusion does not remove the Voronov and Badnell lithium-plasma kinetics | `test_the_independent_lithium_plasma_kinetics_survive[voronov/badnell]`, `test_the_lithium_plasma_data_files_are_untouched_by_this_ticket` | PASS — `voronov.yaml` Z = 3 with N ∈ {1,2,3}, `badnell.yaml` Z = 3 with N ∈ {0,1,2}, both files byte-identical to base `fb3c13c60` |
| 4 | the historical SEI example still identifies the family under its electrochemical configuration | `test_the_sei_example_still_selects_this_family_through_electrochem`, `test_the_family_still_generates_its_sei_reaction` | PASS — the example reaches the family through the `electrochem` set (not by name), and the family still generates `[Li+] + [CH3] <=> [Li][CH3]` with `Marcus` kinetics from training entry `CH3 + Li <=> CH3Li` |
| 5 | the relevant RMG-Py and full RMG-database suites pass against pinned worktrees | §6.3 | PASS, with one pre-existing failure set named and shown to pre-date this ticket |

### 6.2 This ticket's suite, on both runtimes

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-plasma python -m pytest test/test_cation_r_recombination_sei.py -q
18 passed in 1.19s

$ PYTHONPATH=/home/alon/Code/RMG-Py-i102-quarantine python -m pytest test/test_cation_r_recombination_sei.py -q
18 passed in 1.26s
```

### 6.3 The suites

**RMG-Py, the relevant modules** — `test/rmgpy/data/` in full (the database-facing suite, which is
what a database change can break) plus `reactionMarcusTest.py`, `electronPlacementTest.py` and
`solver/reverseReconstructionGuardTest.py`, the modules that name this family:

```
runtime /home/alon/Code/RMG-Py-plasma            (a61dc1303)   426 passed, 7 skipped in 15.48s
runtime /home/alon/Code/RMG-Py-i102-quarantine                 450 passed, 7 skipped in 15.72s
```

both against `database.directory = /home/alon/Code/RMG-database-i111-sei/input`. The second run is
the one that matters most for the marker: it is the runtime where the quarantine is **live**, and
450 tests pass with it loaded. (`solver/reverseReconstructionGuardTest.py` does not exist on the
i102 branch, so that run is 3 modules to the first run's 4 — hence 450 items against 426.)

**RMG-database, the full `test/` directory:**

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-plasma python -m pytest test/ -q
4 failed, 59 passed in 1.37s
```

The four failures are **pre-existing and unrelated**, and that was established rather than asserted.
They are all in `test/test_plasma_electron_attachment.py`
(`test_trained_species_resolve_to_their_own_rate_through_their_own_node[O2|OH|O]` and
`test_o2_rate_comes_from_the_training_set_not_a_library`), a module that touches only
`Plasma_Electron_Attachment` — a family this ticket does not go near. Running that module against a
clean export of the ticket's base commit reproduces exactly the same four:

```
$ git archive fb3c13c60 | tar -x -C <scratch>/basetree
$ cd <scratch>/basetree && pytest test/test_plasma_electron_attachment.py -q   # pinned to basetree
4 failed, 41 passed in 1.15s
```

**One observation about that module, recorded not fixed.** Run on its own against this worktree it
does not fail — it **errors out entirely, 45 errors**, because its fixture asserts
`settings['database.directory']` equals its own worktree and there is no `rmgrc` at this repository
root to make that true. In a combined `pytest test/` run it passes that guard only because this
ticket's module sets the pin at import time and sorts first alphabetically. That is a real fragility
in the existing module's pinning, it pre-dates this ticket, and changing it is not this ticket's
scope.

### 6.4 No scientific value changed

The diff, in full:

```
$ git diff --stat fb3c13c60
 .../families/Cation_R_Recombination/groups.py      | 32 +++++++-
 .../families/Cation_R_Recombination/quarantine.py  | 94 ++++++++++++++++++++++
 input/kinetics/families/recommended.py             |  7 ++
 3 files changed, 131 insertions(+), 2 deletions(-)
```

(plus three untracked additions: `PROVENANCE.md`, the test module, and this report.)

Every science-bearing path, explicitly:

```
$ git diff --stat fb3c13c60 -- \
    input/kinetics/families/Cation_R_Recombination/rules.py \
    input/kinetics/families/Cation_R_Recombination/training/ \
    input/thermo/ input/solvation/ \
    input/kinetics/voronov.yaml input/kinetics/badnell.yaml input/kinetics/libraries/
(no output)
```

No `rules.py`, no `training/reactions.py`, no `training/dictionary.txt`, no thermo, no solvation, no
kinetics library, no other family anywhere:

```
$ git diff --name-only fb3c13c60 -- input/kinetics/families/
input/kinetics/families/Cation_R_Recombination/groups.py
input/kinetics/families/Cation_R_Recombination/quarantine.py
input/kinetics/families/recommended.py
```

The only two lines **removed** anywhere in the ticket are in `groups.py`, and they are the empty
description it had:

```
$ git diff fb3c13c60 -- .../Cation_R_Recombination/groups.py | grep '^-' | grep -v '^---'
-shortDesc = ""
-
```

Everything else in that file is an addition. `template`, `reverse`, `reversible`, `reactantNum`,
`productNum`, `autoGenerated`, `allowChargedSpecies`, `electrons`, the `recipe`, all seven `Group`
entries and the `tree` are untouched.

And because a file diff only proves what was edited, not what is loaded, the suite carries a
**behavioural** pin: `test_no_scientific_value_changed` reloads the family and recomputes a SHA-256
over a canonical rendering of all twelve objects — kinetics class, `A`, `n`, all four `lmbd_i`
coefficients, `beta`, `wr`, `wp`, `lmbd_o`, `rank` — plus each training entry's reaction equation as
stored and the family's recipe, electron count, reversibility and template arity:

```
0a77f301dc81b60c13b64caa9d009e08c08121712b1cd677d48b905e21aa0a34
```

identical under both runtimes. Reformatting the files cannot move it; changing a number, an
orientation, a kinetics class or the recipe must.

**Specifically not done**, each of which was available and each of which would have been calibration
rather than recovery: no choice made between the two Li⁺ references; no association contribution
inferred from the shared prefactor; no potential offset fitted, per-entry or global, and specifically
not 4.44 V; no λ refitted; no entry deleted, averaged, zeroed, reversed or made irreversible; no
family renamed.

## 7. What I could not reach

- **The alkali-plasma deck that names the family individually.**
  `/home/alon/Code/RMG-Py-plasma/docs/m7-preflight/input.py:34` lists `'Cation_R_Recombination'` in
  the `kineticsFamilies` of a two-temperature `plasmaReactor` job, and its own header says it loads
  the six lithium cation families so that Li⁺ is produced "via the auto-derived reverse template of
  `Cation_R_Recombination`". **That is the plasma configuration this reclassification refutes, and it
  is the one place the family really is counted as plasma chemistry.** It is in a shared checkout
  this ticket forbids writing to, and it is an RMG-Py workflow config, which the dispatch requires be
  raised before changing. Raised, not changed. Two further consumers in the same runtime name the
  family for legitimate reasons and are not affected by the reclassification:
  `rmgpy/electron_placement.py:108` (an electron-placement declaration) and six test modules.
- **Merging the I-102 quarantine loader into the plasma runtime.** This is what would turn §4's
  declared-configuration exclusion into an explicit failure under the runtime the plasma work
  actually uses. RMG-Py change, different branch, not owned here.
- **A formal plasma domain-selection mechanism.** Deliberately not built (§4). The consequence is
  that "exclude from every plasma configuration" is enforced by a set membership and a marker rather
  than by a domain type the loader understands. If a plasma set is ever wanted, `recommended.py` is
  where it goes and this family must not be in it.
- **The four unresolved provenance facts** are still unresolved and this ticket did not attempt them
  — the Li⁺ reference the λᵢ set was computed against, whether implicit solvation was used and in
  which solvent, the derivation of `A = 1.73e6` / `n = 2`, and the association/electron-transfer
  decomposition. They are recorded in `PROVENANCE.md` §7 as open, which is why the label says
  INCOMPLETE QUANTITATIVE PROVENANCE.
- **The pre-existing `test_plasma_electron_attachment.py` failures and its pinning fragility**
  (§6.3) are named and left alone.
- **No RMG model was run.** No `rmg.py` job, no reactor, no convergence. The exclusion is
  demonstrated at family loading, reaction generation, kinetics estimation and the quarantine
  boundary — not by running a plasma mechanism to completion.

## 8. Compliance statements

**No outreach was drafted, filed, or suggested.** No email, no draft, no reminder, no TODO, no
follow-up issue, and nothing anywhere in this branch that waits on a reply from anyone. Matt Johnson
is named in `PROVENANCE.md` §4 solely as the repository's own commit-record attribution, and that
section says in terms that it is provenance and authorises no enquiry.

**Nothing was deleted, repaired, refitted, or reinterpreted.** The rates, the reorganisation
energies, the training reactions and their level of theory are exactly as they were.

**The alkali milestone is not unblocked by this.** Removing an invalid surrogate eliminates a wrong
answer; it does not supply a right one, and it says nothing about whether the replacement plasma
network is complete. A different ticket owns that question.

**Branch state:** committed on `i111-sei-reclassification`. Not merged, not pushed, no PR.
