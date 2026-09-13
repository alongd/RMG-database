# I-223 — Charge-transfer node repair, and the duplicate NO⁺/O₂ rate

Branch `i223-charge-transfer-node-repair`, worktree
`/home/alon/Code/RMG-database-i223-charge-transfer-node-repair`.
Measured from `/home/alon/Code/RMG-Py-i223-ct-node-repair` (built once with
`python utilities.py check-pydas && make build`; 52 `.so` under `rmgpy/`). Nothing was committed
to the code worktree.

**Resolved `database.directory` = `/home/alon/Code/RMG-database-i223-charge-transfer-node-repair/input`**,
printed at the top of every log in `logs/`. Every probe also prints `family loaded from`, because
the family was **never installed under `input/`** — it is loaded straight from
`docs/i154-carry-chemistry/held-back/Plasma_Charge_Transfer/` via `KineticsDatabase.load_families`,
and the "before" runs load a pristine `git show HEAD:` checkout in `$TMPDIR/i223-before/`, so
before and after are measured by identical code against different files.

Every check was run **one at a time** (`probe_checks.py`). This is not optional here:
`kinetics_check_groups_nonidentical` and three of its neighbours do not return `False`, they raise
`ValueError`, which escapes the `with check:` block and aborts the whole family — so a suite run
reports at most one failing node per family and silently never runs the later checks.

---

## 1. The two failures, reproduced before any edit

`logs/before.stdout.log`, 24 PASS / 2 FAIL / 1 SKIP:

```
Noble_cation     A              [He]                          0 None             FAIL (no match to root A)
    sample adjlist:
    1 *1 He u0 p1 c0
H2_ion           A              [H][H-]                      -1 None             FAIL (no match to root A)
    sample adjlist:
    multiplicity 2
    1    H u1 p0 c-1 {2,S}
    2 *1 H u0 p0 c0  {1,S}
```

Exactly the two the brief named, with the charges it predicted. Note where the charge went in the
`H2_ion` sample: the labelled `*1` came out **neutral** and the −1 landed on the *unlabelled* atom.

`logs/checks-before.stdout.log`: all eleven other family checks pass; only
`kinetics_check_sample_descends_to_group` fails. That baseline matters for §3.

### Why each one failed

Both are `Group.make_sample_molecule` charge-derivation failures, and neither is a typo.

**`Noble_cation`** was `[He,Ne,Ar] ux px c+1`. `pick_wildcards` takes `atomtype[0]`, so the sample
is built on helium; `He` has no charged subtype and its `AtomType` carries an empty `lone_pairs`
list, so `make_sample_atom` falls back to `default_lone_pairs['He'] = 1`, and `update_charge` then
recomputes 2 − 2·1 = 0. The `c+1` in the group is simply overwritten. Root `A` requires
`c[+1,+2,+3,+4]` and rejects it.

**`H2_ion`** was a single-bonded `H⁺`–`H·` pair. That species **does not exist in RMG at all**:

```
H2+ single-bonded    FAIL InvalidAdjacencyListError: Invalid valency for atom H (H0) with
                     1 unpaired electrons, 0 pairs of electrons, 0 charge, and bonds [1.0].
```
(`logs/h2-recipe.stdout.log`)

H2⁺ is held by a one-electron bond, which RMG's integer bond orders cannot express. The family's
**own training dictionary already knows this** — `H2p_r1` is two *unbonded* atoms, `[H+].[H]` — so
the authored node matched nothing at all: `is_subgraph_isomorphic(H2p_r1, H2_ion) = False`, and
H2p_r1 descended only as far as `H_ion` (`logs/candidates.stdout.log` §3–4). The node was dead
before this ticket, not merely un-sampleable.

---

## 2. The repairs

### `Noble_cation`: `[He,Ne,Ar] ux px c+1` → `[Ar+,Ar,He,Ne] ux px c+1`

Measured against every candidate (`logs/noble.stdout.log`, `logs/parent.stdout.log`):

| candidate | sample | matches He⁺ / Ne⁺ / Ar⁺ / Ar₂⁺ / ArH⁺ | proper parent of `Ar_ion` |
|---|---|---|---|
| `[He,Ne,Ar] ux px c+1` (was) | `[He]` **+0** | T T T T T | yes |
| `[Ar,Ne,He] u1 p3 c+1` | `[Ar+]` +1 | F T T F F | — |
| `OR{He_ion, Ne_ion, Ar_ion}` | (skipped) | one each | — |
| **`[Ar+,Ar,He,Ne] ux px c+1`** | **`[ArH+]` +1** | **T T T T T** | **yes** |

The chosen form **does not narrow the node**: its matched set is byte-for-byte the current one.
`Ar+` leads the list because `pick_wildcards` takes the first atomtype, and `Ar+` is the only one of
the three elements that carries `lone_pairs=[3]` and `charge=[1]` of its own, so the sample gets
built at +1. Generic `Ar` stays in the list because the child `Ar_ion` is written on generic `Ar`,
and `Ar+` is *more* specific — an `Ar+`-only parent stops being a proper parent of its own child.
That is not hypothetical: I hit it. My first attempt was `[Ar+,He,Ne]`, and
`kinetics_check_child_parent_relationships` — green in the baseline — went red with *"group
Noble_cation is not a proper parent of its child Ar_ion"*. Adding `Ar` back fixes it and leaves
`Ar_ion` untouched.

The two rejected candidates both narrow the node: `[Ar,Ne,He] u1 p3 c+1` asserts 3 lone pairs, which
is false for He⁺ (0 lone pairs, 1 radical) and drops He⁺, Ar₂⁺ and ArH⁺; the `OR{...}` form — the
idiom this copy already uses for `Anion` — drops Ar₂⁺ and ArH⁺, because a LogicOr can only name
concrete children and there is no atom type for a *bonded* noble-gas cation other than `Ar+`. A node
that passes by being narrowed into something it does not mean is worse than one that fails.

### `H2_ion`: bond removed

```
1 *1 H u0 p0 c+1        (was:  1 *1 H u0 p0 c+1 {2,S}  )
2    H u1 p0 c0         (      2    H u1 p0 c0  {1,S}  )
```

Samples `[H+].[H]` at **+1** and — unlike the authored form — actually matches `H2p_r1`. Training
entry 2 now resolves to the template `H2_ion;H_anion` instead of falling back to `H_ion;H_anion`
(`logs/rules.stdout.log`). This preserves the node's meaning exactly: it is the same "the H⁺ centre
of a molecular hydrogen cation" it always claimed to be, now written the way the dictionary writes
it.

### `O2_neutral`: new node (index 213), child of `O_neutral`

```
1 *2 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
```

Added **because of the coupling between two of your decisions**, not as independent scope. Deleting
entry 17 (§4) to make the Ozawa2008 NO⁺/O₂ value the surviving one accomplishes nothing at the rule
level while O₂ and atomic O both descend to `O_neutral` (`O ux px c0`): training 14 (NO⁺ + O) and
training 21 (NO⁺ + O₂) both resolved to `NO_ion;O_neutral`, and `get_rule` keeps the lower index, so
entry 14 shadowed entry 21 regardless. Without this node the entry-17 deletion is inert and the
ticket is internally inconsistent. `O2_neutral` is the minimum that makes that earlier decision take
effect: training 21 now resolves to `NO_ion;O2_neutral` and the Ozawa rate is actually used. It is
written concretely, as the ground-state triplet, to match the dictionary's `O2_r2`; it is the only
training reaction with an O₂ partner, so the blast radius is one reaction.

---

## 3. Every authored node, after (`logs/after.stdout.log`)

`PASS 27  FAIL 0  SKIP 1`. 27 authored group entries + the new `O2_neutral` = 28 authored; the
loaded family reports 30 because `template(products=["A-","B+"])` names two entries `groups.py`
never defines and RMG fabricates them — they are auto-generated product templates, correctly
excluded by the check's own `ignore` list. **The brief's "27 group entries" is right for the file
and wrong for the loaded object.**

| node | root | sample | charge | descends to | verdict |
|---|---|---|---|---|---|
| A | A | `[H+]` | +1 | H_ion | PASS |
| B | B | `[H][H]` | 0 | Neutral | PASS |
| H_cation | A | `[H+]` | +1 | H_ion | PASS |
| O_cation | A | `[OH+]` | +1 | OH_ion | PASS |
| N_cation | A | `[NH2+]` | +1 | N_cation | PASS |
| **Noble_cation** | A | `[ArH+]` | **+1** | Noble_cation | **PASS** |
| Metal_cation | A | `[Li+]` | +1 | Li_ion | PASS |
| H_ion | A | `[H+]` | +1 | H_ion | PASS |
| **H2_ion** | A | `[H+].[H]` | **+1** | H2_ion | **PASS** |
| O_atom_ion | A | `[O+]` | +1 | O_atom_ion | PASS |
| OH_ion | A | `[OH+]` | +1 | OH_ion | PASS |
| H2O_ion | A | `[OH2+]` | +1 | H2O_ion | PASS |
| O2_ion | A | `[O][O+]` | +1 | O2_ion | PASS |
| N_atom_ion | A | `[N+]` | +1 | N_atom_ion | PASS |
| NO_ion | A | `N#[O+]` | +1 | NO_ion | PASS |
| Ar_ion | A | `[Ar+]` | +1 | Ar_ion | PASS |
| Li_ion / Na_ion / K_ion | A | `[Li+]` / `[Na+]` / `[K+]` | +1 | itself | PASS |
| Mg_ion / Ca_ion | A | `[Mg+]` / `[Ca+]` | +1 | itself | PASS |
| Anion | — | (LogicOr) | — | — | SKIP — not a `Group`, so `make_sample_molecule` never runs on it; its children are checked instead |
| Neutral | B | `[H][H]` | 0 | Neutral | PASS |
| H_anion | B | `[H-]` | −1 | H_anion | PASS |
| O_anion | B | `[OH-]` | −1 | O_anion | PASS |
| O_neutral | B | `O` | 0 | O_neutral | PASS |
| N_neutral | B | `N` | 0 | N_neutral | PASS |
| **O2_neutral** | B | `[O][O]` | 0 | O2_neutral | **PASS** |

### Full per-check status (`logs/checks-after.stdout.log`)

| check | before | after |
|---|---|---|
| correct_number_of_nodes_in_rules | PASS | PASS |
| nodes_in_rules_found_in_groups | PASS | PASS |
| groups_found_in_tree | PASS | PASS |
| **groups_nonidentical** | PASS | PASS |
| child_parent_relationships | PASS | PASS |
| siblings_for_parents | PASS | PASS |
| cd_atom_type | PASS | PASS |
| reactant_and_product_template | PASS | PASS |
| num_reactant_and_product | PASS | PASS |
| family_electrons_reach_training_reactions | PASS | PASS |
| **sample_descends_to_group** | **RAISED ValueError** | **PASS** |
| **sample_can_react** | PASS (vacuously — see below) | **RAISED ValueError** |

### `sample_can_react` — the one red check, and why it is progress

One error, on one pair (`logs/checks-after.stderr.log`):

```
Error in family Plasma_Charge_Transfer when reacting [H+].[H] + [H][H].
apply_recipe returned None, indicating wrong number of products or a charged product.
```

`Noble_cation`'s `[ArH+]` reacts fine. The cause is structural, measured in
`logs/h2-recipe.stdout.log`:

- training entry 2 is **H2⁺ + H⁻ → H₂ + H**. The electron arriving on H2⁺ becomes the *second*
  electron of the H–H bond;
- the recipe is charge-only (`LOSE_CHARGE *1`, `GAIN_CHARGE *2`) — it has no bond-forming action;
- so from an unbonded `[H+].[H]` it can only produce `[H].[H]`, two separate H atoms.
  `_generate_product_structures` calls `product_structure.split()`, gets 3 where `product_num` is 2,
  and returns `None`.

**The pre-edit pass was vacuous.** The old sample `[H][H-]` is a molecule RMG refuses to build as a
species, and `apply_recipe` on it returned `['[H][H-]', '[H][H]']` — the charge never moved at all.
The check passed on a pair that meant nothing. A third option (give H2⁺ a `vdW` bond in both group
and dictionary) would turn the check green and was rejected for the same reason: measured, it
returns `['[H+].[H]', '[H][H]']`, i.e. it "produces" an H₂ that is two unbonded H atoms and a
charge that never transferred. Green and wrong.

Dropping `H2_ion` instead would have pushed training entry 2 onto `H_ion;H_anion` — the *same*
template as training entry 1 — creating a second equal-rank duplicate, which is the defect this
ticket exists to remove.

So the red check is a real limitation now stated out loud: **this family's recipe cannot represent
the H2⁺ mutual-neutralisation channel**, because RMG cannot represent H2⁺'s bond. If that channel is
wanted, it needs a library entry, not this family.

---

## 4. The duplicate rate

### The brief's premise was wrong, and the primary source says why

`training/reactions.py` carried `NOp_r1 + O2_r2 <=> O2p + NO` twice, both at `rank = 6`:

| index | source | A (cm³/mol·s) | n | Ea | **T0** |
|---|---|---|---|---|---|
| 17 | `[Gupta1990]` Table II R19 | 1.8e15 | 0.17 | 65600 cal/mol | **300 K** |
| 21 | `[Ozawa2008]` Table III | 2.4e13 | 0.41 | 271.1 kJ/mol | **1 K** |

The brief reads the pre-exponentials as differing by ~75×. **They do not share a `T0`**, so that
comparison is not meaningful. Through rmgpy's own `Arrhenius` objects (`logs/kt.stdout.log`):

| T / K | index 17 | index 21 | 17/21 |
|---|---|---|---|
| 300 | 2.93e−33 | 1.56e−33 | 1.87 |
| 1000 | 1.02e+01 | 2.82e+00 | 3.61 |
| 2000 | 1.69e+08 | 4.50e+07 | 3.75 |
| 4000 | 7.28e+11 | 2.07e+11 | 3.51 |
| 6000 | 1.22e+13 | 3.71e+12 | 3.30 |
| 10000 | 1.20e+14 | 4.02e+13 | 3.00 |

Ratio min 1.87 (300 K), max 3.76 (1690 K); index 17 only exceeds 1e6 cm³/mol·s above **1530 K**, and
over that live window the ratio runs **3.00–3.76**. So: a factor of ~3, not 75. Plot in
`kT-comparison.png`.

Chasing the provenance settled it. I pulled NASA RP-1232 (Gupta, Yos, Thompson & Lee, 1990) and OCRd
Table II, p.45. **R19 is `O₂ + NO⁺ ⇌ NO + O₂⁺`, `1.8e15 T^0.17 exp(−3.3e4/T)` cm³/mole·sec** — a
bare `T`, no `(T/300)` normalisation. Ea = 65600 cal/mol is exactly θ_d = 3.3e4 K (Ea/R = 33011 K),
confirming the row. **Entry 17 copied Cf verbatim and left `T0 = 300 K`, which makes every k it
returns 300^0.17 = 2.64× too low** (`logs/t0.stdout.log`). The 300 came from the twelve
`[Tanarro2015]` entries immediately above it in the file, whose Table 1 *is* written `k = A(T/300)^n`
— for them T0 = 300 K is correct.

### Decision: entry 17 deleted, `[Ozawa2008]` (index 21) kept

Three independent reasons, in order of weight:

1. **Physical.** Dividing `A·Tⁿ` by the Langevin capture rate for NO⁺ + O₂
   (4.51e14 cm³/mol·s, α(O₂) = 1.58 Å³, μ = 15.48 amu) asks how many times the ion–molecule collision
   limit each fit would demand if every super-threshold collision reacted:

   | T / K | Gupta (T0 corrected) | Ozawa idx 21 | G/O | G prefac/k_L | O prefac/k_L |
   |---|---|---|---|---|---|
   | 300 | 8.02e−33 | 1.56e−33 | 5.13 | 10.5 | 0.55 |
   | 2000 | 4.47e+08 | 4.50e+07 | 9.94 | 14.6 | 1.20 |
   | 6000 | 3.23e+13 | 3.71e+12 | 8.71 | 17.5 | 1.89 |
   | 10000 | 3.18e+14 | 4.02e+13 | 7.91 | **19.1** | **2.33** |

   Gupta's fit demands 10–19× the capture limit; Ozawa's stays at 0.55–2.3×, which is the ordinary
   range for a polarisable target. For a capture-limited charge transfer, 19× is unphysical.
2. **Thermochemical.** Ozawa's Ea of 271.1 kJ/mol matches the endothermicity
   IE(O₂) − IE(NO) = 12.0697 − 9.2642 eV = 2.8055 eV = **270.7 kJ/mol** almost exactly. Gupta's
   θ_d·R = 274.4 kJ/mol is 3.7 kJ/mol high.
3. **Internal consistency.** Entries 14, 15, 16, 21, 22 and 23 — the whole air-plasma
   charge-exchange block — are `[Ozawa2008]` Table III. Keeping index 21 makes the set one model.

Index 17 is deleted and the index left unused rather than renumbering. The Gupta value, its correct
form, and the reasoning are recorded in the `longDesc` at the top of `training/reactions.py` and in
index 21's own `longDesc`, so nothing is lost from the record.

### Entry 13 carried the same `T0` bug — fixed

RP-1232 Table II **R11** is `O + O₂⁺ ⇌ O₂ + O⁺`, `2.92e18 T^−1.11 exp(−2.8e4/T)`. Entry 13
(`O2p_r1 + O_r2 <=> O2 + Op`) copied Cf verbatim with `T0 = 300 K` and `n = −1.11`. Because n is
negative and large, that made it **561× too high at every temperature** (`logs/t0.stdout.log`):

| T / K | as entered | source form | ratio |
|---|---|---|---|
| 300 | 8.42e−23 | 1.52e−25 | 0.00180 |
| 4000 | 1.50e+14 | 2.67e+11 | 0.00178 |
| 10000 | 3.62e+15 | 6.45e+12 | 0.00178 |

`T0` corrected to 1 K; `A = 2.92e18` is Gupta's Cf, untouched. This was outside the brief and is
here on your explicit call.

### No reaction is left at equal rank

`logs/rules.stdout.log` runs `add_rules_from_training` the way a real run does and reports every rule
label holding more than one entry. **No reaction label appears twice**, in training or in the rules.

---

## 5. Clean `git status`

```
$ git status --porcelain -- input/ docs/i202-charge-transfer-carry/
[no output]

$ git diff --stat
 .../held-back/Plasma_Charge_Transfer/groups.py     | 48 +++++++++++++++++++--
 .../Plasma_Charge_Transfer/training/reactions.py   | 50 +++++++++++++++-------
 2 files changed, 80 insertions(+), 18 deletions(-)
```

Nothing under `input/` changed. The 24-entry copy under `docs/i202-charge-transfer-carry/` is
untouched. `test/conftest.py` untouched. The RMG-Py worktree has no commits and no tracked-file
changes (build artifacts only). No atom type was added or changed. `autoGenerated` and
`own_reverse` were not set. Nothing pushed, nothing merged.

---

## 6. What this could not reach

**Left open deliberately, needing your decision.** Three more template nodes are coarser than their
chemistry, in the same way `O_neutral` was, and I stopped at the one that unblocked the entry-17
decision (`logs/rules.stdout.log`):

| template | colliding training reactions | what is merged |
|---|---|---|
| `O2_ion;O_anion` | 8 (O₂⁺ + O⁻), 10 (O₂⁺ + OH⁻) | O⁻ and OH⁻ both match `O_anion` = `O ux p3 c-1` |
| `H2O_ion;O_anion` | 9 (H₂O⁺ + O⁻), 12 (H₂O⁺ + OH⁻) | same |
| `O2_ion;N_neutral` | 22 (O₂⁺ + N), 23 (O₂⁺ + N₂) | N and N₂ both match `N_neutral` = `N ux px c0` |

In each, `get_rule` keeps the lower index and the other training reaction's rate is never used —
silently, with nothing logged. That is the same shadowing that motivated `O2_neutral`, and the four
colliding pairs above are the evidence a follow-up should start from. The blocking sub-question is a
tree-design call that needs the owner, not a worker: **should `OH_anion` be a sibling of `O_anion` or
a child of it?** That choice decides what an unlisted anion falls back to, and it is not derivable
from the training set.

**Unprovable until the family is installed under `input/`:**

- `add_rules_from_training` was run here in isolation with `thermo_database=None`. Per the campaign's
  own record, a family carrying `TwoTemperaturePlasma` kinetics crashes a real RMG run at
  `main.py:590` inside `add_rules_from_training` while the DB suite stays green — this family's
  training entries are plain `Arrhenius`, so that specific trap does not apply, but I have not run
  RMG end to end and cannot say the family survives one.
- `get_reaction_template` matches on **reactant-side labelled atoms only and never inspects
  `reaction.products`**. Every green here — the descent table, the template assignments, the rule
  generation — is therefore evidence about the *reactant* side of each entry. It is not evidence that
  the recipe produces the stated products. The one place I did test the product side,
  `sample_can_react`, is exactly where the H2⁺ defect surfaced.
- Reactor admissibility is untested. I-157 established that loading ≠ admissible: reversible
  Te-dependent recombinations are refused at `initialize_model`. Nothing here was put through a
  reactor.
- `is_molecule_forbidden` was exercised only against this family's own (empty) forbidden groups, not
  against the global `input/forbiddenStructures.py`, because the family was never loaded through
  `RMGDatabase`.
- `probe_checks.py` injects a `SimpleNamespace` in place of a real `RMGDatabase` so that one family
  can be checked in isolation. That is deliberate — `RMGDatabase.__init__` does `global database;
  database = self` with no reset, and two in one process has been measured shifting a thermo value by
  0.36 kJ/mol — but it means the library-level and cross-family checks in `test_kinetics` were not
  run at all.

**Source verification I did not do.** Only `[Gupta1990]` was checked against the primary document
(NASA RP-1232 Table II, OCRd from the Caltech mirror). `[Tanarro2015]`, `[Ozawa2008]` and
`[Aiken2023]` were not fetched; their `T0` conventions are inferred from internal consistency
(Tanarro's `(T/300)` form is standard for low-temperature plasma tables; Ozawa and Aiken already
carry `T0 = 1 K` and their θ values line up with bare-T fits). A full `T0` audit of all 27 entries
against their four primary sources remains undone — it is the natural companion to the entry-13 fix
and would be a materially larger job than it looks.

**OCR caveat.** RP-1232 is a scanned document. The exponent in R19 rendered as `10lG`, which I read
as 10¹⁵ on the strength of n = 0.17 and θ_d = 3.3e4 matching the database entry exactly, and of the
same OCR rendering 10¹⁸ as `10 1S` in R11. If that digit is wrong, the *relative* argument in §4
changes but the `T0` finding does not — the bare-`T` form of the table is unambiguous in the scan.

---

## Files

| path | what |
|---|---|
| `probe_nodes.py` | per-node sample + descend, one node at a time |
| `probe_checks.py` | every family-level `test_kinetics` check, one at a time |
| `probe_candidates.py` | can RMG build He⁺/Ne⁺/H2⁺; does the old node match anything |
| `probe_noble.py` | the four `Noble_cation` candidates, sampling and matched set |
| `probe_parent.py` | parent/child validity of each `Noble_cation` candidate |
| `probe_h2_recipe.py` | why the repaired `H2_ion` sample cannot react |
| `probe_kt.py` | k(T) over 300–10000 K for the two duplicate fits |
| `probe_t0.py` | the `T0` error in both `[Gupta1990]` entries, and the Langevin comparison |
| `probe_rules.py` | template each training reaction resolves to; equal-rank collisions |
| `run.sh` | runner — pins cwd and `PYTHONPATH`, persists **both** streams per probe |
| `logs/*.{stdout,stderr}.log` | one pair per measurement |
| `kT-comparison.png` | k(T) and ratio for the duplicate |
