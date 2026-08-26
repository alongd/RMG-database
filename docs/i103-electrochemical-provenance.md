# I-103 — The electrochemical provenance of the Cation_R_Recombination Marcus rules

**Report-first. No rate, no λ, no `A`, no `n`, no equation, no family, no thermo, no quarantine
marker was changed.** The only change on this branch is this file; the `git diff` proving it is in
§8.

Evidence labels, used on every claim: **[R]** read from code (file:line), **[D]** read from a
database file (file, entry), **[L]** literature (full citation), **[I]** inference, with its basis
named. **UNKNOWN** marks something that could not be established, always with what would settle it.

---

## 0. The answer

- **The twelve objects rest on five calculations, not twelve.** All seven rate rules are exact
  arithmetic means of the five training entries' λᵢ coefficients — four of them are bit-identical
  copies of a single training entry. The rule-generating code that does this is named and read.
  §3. This is the ruling's own gating question and the answer is **five**, not UNKNOWN.
- **`Cation_Addition_MultipleBond` never held a Marcus entry**, on any branch, at any time. Its
  eight entries have always been `ArrheniusChargeTransfer`/`ArrheniusChargeTransferBM`. The
  ruling's recollection of a seven/five split across two families is a misremembering of the
  rules/training split inside one family. §3.3.
- **The electrochemical context is recovered, and it is a lithium-ion battery SEI model in liquid
  ethylene carbonate against a Li(110) metal electrode, at 298.15 K, with a declared applied
  potential.** It is recorded in `examples/rmg/SEI_pure_EC/input.py` in the reference runtime
  repository — not in this database, and not attached to the entries. §4.4.
- **The driving-force reference is *not* recovered.** Two mutually incompatible Li⁺ references exist
  in this database, 502 kJ/mol apart at 298 K, and **neither one reproduces all five entries as
  physical rates.** §5.
- **The association step is unrecoverable.** Its slots exist (`wr`, `wp`), both are zero on all
  twelve, and **both are dead code in both runtimes** — declared, stored, serialised, never read.
  Whether `K_assoc` was folded into the shared prefactor `A = 1.73e6 m³/(mol·s)`, `n = 2` is
  UNKNOWN, and that prefactor appears nowhere else in either repository. §4.5.
- **The pre-existing `Marcus.get_rate_coefficient` pressure-for-ΔG defect explains none of the
  10⁻²³–10⁻²²⁶ collapse. It explains why nobody saw it.** §6.7.
- **Can the original electrochemical model be reproduced from what the repositories contain? No.**
  §7 names precisely the four things missing and who would have them.
- Contacting the original author — **Matt Johnson `<mjohnson541@gmail.com>`, identified from the
  commit record** — is now the recommendation. It is a gate for the user, not a task, and was not
  attempted. §10.

---

## 1. Contract restatement, and the environment

### 1.1 Intent, in my own words

Diagnose why the `Cation_R_Recombination` Marcus rules evaluate 30–230 orders of magnitude below
anything physical, by recovering — or proving unrecoverable from the repositories — the
electrochemical *reference* and *decomposition* those stored coefficients were written against. The
coefficients themselves are not in question and are not to be touched. Before searching for
provenance, establish how many independent calculations actually underlie the twelve stored
objects, because the ruling's own inventory disagrees with the database and the answer sets the size
of the search. Change no data. Contact no one.

**My restatement and the dispatch text agree.** There is nothing to stop and report.

### 1.2 Verifier

The artifact is this file, committed on branch `i103-electrochem-provenance`, satisfying the eight
numbered items of the dispatch's Verifier. Each is answered in a section named against it in §9.

### 1.3 Environment and pin

| Role | Path | State |
|---|---|---|
| Data under diagnosis | `/home/alon/Code/RMG-database-i103-provenance` | branch `i103-electrochem-provenance`, base `fb3c13c60` |
| Reference runtime | `/home/alon/Code/RMG-Py-plasma` | branch `plasma`, unmodified, not rebuilt, not written to |

```
$ source /home/alon/anaconda3/etc/profile.d/conda.sh && conda activate rmg_env
$ export PYTHONPATH=/home/alon/Code/RMG-Py-plasma:$PYTHONPATH
$ python -c "import rmgpy; print(rmgpy.__file__)"
/home/alon/Code/RMG-Py-plasma/rmgpy/__init__.py
```

Every probe printed `PIN rmgpy:` first and `PIN-AFTER rmgpy:` last; all four read inside
`RMG-Py-plasma`. `/home/alon/Code/RMG-Py` (branch `polymer`) was never on the path. Nothing was
built; `make` was never run in any form. The four probes, with `stdout.log` and `stderr.log`
persisted, live outside every tracked tree under
`/tmp/claude-1000/-home-alon-Code-RMG-database-i103-provenance/8592de58-.../scratchpad/`:
`probe1` (Li⁺ thermochemistry across libraries), `probe2`/`probe2b` (ΔG and k under both
references), `probe3` (solvation of Li⁺ in ethylene carbonate), `probe4` (the five evaluated under
the source model's own declared conditions). Being scratch they are not durable; the numbers quoted
here are the record.

**Search space for every `git` claim below.** All `git log --all` / `git grep` commands ran against
355 fetched refs (`git for-each-ref refs/remotes | wc -l` → 355), including the full
`ReactionMechanismGenerator/RMG-database` remote fetched to 2026-08-21. A claim of the form "never,
on any branch" therefore means *never on any of those 355 refs* — it cannot speak for a branch that
was never pushed, or one deleted before this clone's first fetch. That limit is real and is carried
into §11.

---

## 2. The framing this report works to

Restated from the governing ruling, because the withdrawn version is still in circulation:

> The stored Marcus kinetics are **not self-contained**. Their four-point reorganisation-energy
> coefficients survive, but the electrochemical driving-force reference, association-step
> decomposition, and electrode semantics needed to evaluate them are **not represented durably** in
> the current database/runtime path.

> **The evidence does not yet show that λ is wrong.**

Nothing in this report refits, rescales, reinterprets or proposes a value for λ. Where §5 varies a
quantity to test a hypothesis, the quantity varied is the *reference against which ΔG is computed*,
never λ, and the variation is a diagnostic evaluation, not a fit. Every λ number quoted is read from
the database or produced by executing `Marcus.get_lmbd_i` on the stored coefficients unchanged. No
potential offset is adopted, per-entry or global, and specifically not 4.44 V.

---

## 3. Phase 1 — the inventory reconciled

**This section is the gate. It is complete before §4 begins.**

### 3.1 The count in the database

```
$ grep -c "^entry(" input/kinetics/families/Cation_R_Recombination/rules.py              -> 7
$ grep -c "^entry(" input/kinetics/families/Cation_R_Recombination/training/reactions.py -> 5
$ grep -o "kinetics = [A-Za-z]*(" input/kinetics/families/Cation_Addition_MultipleBond/rules.py \
      input/kinetics/families/Cation_Addition_MultipleBond/training/reactions.py | sort | uniq -c
      5 .../Cation_Addition_MultipleBond/rules.py:kinetics = ArrheniusChargeTransferBM(
      3 .../Cation_Addition_MultipleBond/training/reactions.py:kinetics = ArrheniusChargeTransfer(
```

**7 rules + 5 training entries, all `Marcus`, all in `Cation_R_Recombination`. Zero Marcus entries
in `Cation_Addition_MultipleBond`, which holds 8 entries of two different charge-transfer classes**
[D]. The dispatch's table is confirmed exactly; the ruling's is not.

### 3.2 The genealogy — the seven rules are derived, not independent

This is the highest-value question in the ticket, and it closes on three independent lines.

**(a) The entries say so.** Every rule's own `comment` and `shortDesc` reads
`"Marcus rule fitted to N training reactions at node <label>"` [D] `rules.py:12,14,24,26,36,38,…`.
The N values are 5, 2, 3, 1, 1, 1, 1.

**(b) The code that wrote them is named and read.** `average_kinetics` at [R]
`rmgpy/data/kinetics/family.py:4842-4892` sums `lmbd_i_coefs` element-wise over the training
kinetics and divides by the count — an **arithmetic** mean — while averaging `A` in log space (a
geometric mean) and averaging `beta`, `wr`, `wp` arithmetically. The comment string is written at
[R] `family.py:3637-3639`:

```python
if isinstance(kinetics, Marcus):
    st = "Marcus rule fitted to {0} training reactions at node {1}".format(len(rxnlists[i][0]), entry.label)
```

**(c) The numbers confirm it exactly.** Executing that arithmetic on the five stored training
`lmbd_i_coefs` and comparing with the seven stored rule `lmbd_i_coefs`, the maximum relative
deviation across all four coefficients of each rule:

| rule node [D] `rules.py` | N | training sources | max relative deviation |
|---|---|---|---|
| `Root` | 5 | NH2 + C2H5 + CH3 + CH3NH + SH | 8.31e-07 |
| `Root_2R->C` | 2 | C2H5 + CH3 | 9.04e-06 |
| `Root_N-2R->C` | 3 | NH2 + CH3NH + SH | 2.26e-06 |
| `Root_2R->C_Ext-2C-R` | 1 | C2H5 | **0.00e+00** |
| `Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R` | 1 | CH3NH | **0.00e+00** |
| `Root_N-2R->C_2BrClFHILiNOPSSi->S` | 1 | SH | **0.00e+00** |
| `Root_N-2R->C_N-2BrClFHILiNOPSSi->S` | 1 | NH2 | **0.00e+00** |

The residuals on the three multi-source nodes are 10⁻⁶–10⁻⁵, exactly the rounding of six
significant figures in the stored decimals; the four single-source nodes are **bit-exact**. The
actual numbers, verbatim [D]:

```
training/reactions.py                                        rules.py
  NH2    [21824.5, -0.0341626, -0.0013254,   4.92966e-07]  == Root_N-2R->C_N-2BrClFHILiNOPSSi->S
  C2H5   [51072.9,  0.770449,   0.00461441, -2.38037e-06]  == Root_2R->C_Ext-2C-R
  CH3    [51902.4, -1.10249,   -0.00813508,  3.26585e-06]  (no leaf rule of its own)
  CH3NH  [22140,   -3.52755,   -0.00528491,  2.76922e-06]  == Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R
  SH     [20364.7,  0.177444,  -0.000702861,-3.39533e-08]  == Root_N-2R->C_2BrClFHILiNOPSSi->S

  Root         [33460.9, -0.743262, -0.00216677, 8.22742e-07]  = mean of all five
  Root_2R->C   [51487.7, -0.166019, -0.00176034, 4.42738e-07]  = mean of C2H5, CH3
  Root_N-2R->C [21443.1, -1.12809,  -0.00243772, 1.07608e-06]  = mean of NH2, CH3NH, SH
```

Worked, for the first coefficient of `Root_2R->C`: (51902.4 + 51072.9)/2 = **51487.65**, stored
51487.7. For `Root`: (21824.5 + 51072.9 + 51902.4 + 22140 + 20364.7)/5 = **33460.9**, stored 33460.9.

**`A` and `n` carry no information at all.** All twelve entries share
`A = 1.73e+06 m^3/(mol*s)` and `n = 2`, identically [D]. A geometric mean of a constant is that
constant, so the rules' `A` is uninformative about their provenance — it is the *training* set's
single shared prefactor propagated seven times.

A fourth fingerprint corroborates the code path: the rules write `wr=(0,'kJ/mol')`,
`wp=(0,'kJ/mol')` while the training entries write `wr=(0,'J/mol')`, `wp=(0,'J/mol')` [D]. That unit
change is exactly `average_kinetics`' `wr=(wr * 0.001, "kJ/mol")` at [R] `family.py:4889-4890`.
Numerically both are zero; as evidence the rules were machine-produced by that function, it is
decisive.

**Conclusion: the seven rules introduce zero information the five training entries do not already
contain.** Four are copies; three are means.

### 3.3 Did `Cation_Addition_MultipleBond` ever hold Marcus entries?

**No. Never, on any of the 355 fetched refs.** The commands, with their real output:

```
$ git log --all -S "Marcus" --oneline -- input/kinetics/families/Cation_Addition_MultipleBond/
(no output)

$ git log --all -S "lmbd_i_coefs" --oneline --name-only -- input/kinetics/families/
b23abeb0c train Cation_R_Recombination
input/kinetics/families/Cation_R_Recombination/rules.py
4c3faffdf add training reactions for Cation_R_Recombination
input/kinetics/families/Cation_R_Recombination/training/reactions.py
a2259aa9c train Cation_R_Recombination                       (official/lithium_reorder)
input/kinetics/families/Cation_R_Recombination/rules.py
355eb2581 add training reactions for Cation_R_Recombination  (official/lithium_reorder)
input/kinetics/families/Cation_R_Recombination/training/reactions.py
14b9d90cd train Cation_R_Recombination                       (official/lithium)
input/kinetics/families/Cation_R_Recombination/rules.py
bd15dd825 add training reactions for Cation_R_Recombination  (official/lithium)
input/kinetics/families/Cation_R_Recombination/training/reactions.py

$ git log --all --follow --format='%h %ad %s' --date=short \
      -- input/kinetics/families/Cation_Addition_MultipleBond/training/reactions.py
acdec68c9 2026-08-17 kinetics: store the electron coefficient as -1 on charged entries
863c05aab 2022-01-11 bulk tree generation
1c363bde2 2021-12-14 Cation_Addition_MultipleBond family
2f220fc89 2022-01-11 bulk tree generation commit
baa39c6db 2021-12-14 Cation_Addition_MultipleBond training reactions
cc7ef729b 2022-01-11 bulk tree generation commit
7f87ff14b 2021-12-14 Cation_Addition_MultipleBond training reactions
```

The `-S "lmbd_i_coefs"` search is the stronger of the two: `lmbd_i_coefs` is the one field no
non-Marcus kinetics class has, so any commit that ever added or removed a Marcus entry anywhere
under `input/kinetics/families/` must appear in it. Six commits appear, all six in
`Cation_R_Recombination`, and the three pairs are the same two commits cherry-picked onto
`official/lithium`, `official/lithium_reorder` and the mainline — identical author, identical
timestamps to the second: `Matt Johnson <mjohnson541@gmail.com>`, 2024-03-09 18:21:21 and 18:21:39
−0800.

`Cation_Addition_MultipleBond`'s own history is four tree-generation events and one 2026
electron-coefficient repair. **It has never carried a Marcus entry, so the ruling's §2 attribution
of seven calculations to it has no referent in the data.** The ruling's "seven
`Cation_Addition_MultipleBond` + five `Cation_R_Recombination`" is, on this evidence, a
misremembering of "seven rules + five training entries in `Cation_R_Recombination`" [I], resting on
the exact numerical coincidence of the 7/5 split and on the total absence of any competing Marcus
set anywhere in the searched history.

### 3.4 Are the five training entries distinct chemistry?

**Yes — five distinct radicals, one shared cation, one reaction type.** From
`training/dictionary.txt` and `training/reactions.py` [D]:

| # | label as stored | actual reaction (the label writes the `c+1` cation as neutral and omits e⁻) | λᵢ 298 K | λᵢ 1000 K |
|---|---|---|---|---|
| 0 | `NH2 + Li <=> NH2Li` | Li⁺ + •NH₂ + e⁻ → LiNH₂ | 21.71 | 20.96 |
| 1 | `C2H5 + Li <=> C2H5Li` | Li⁺ + •C₂H₅ + e⁻ → LiC₂H₅ | 51.65 | 54.08 |
| 2 | `CH3 + Li <=> CH3Li` | Li⁺ + •CH₃ + e⁻ → LiCH₃ | 50.94 | 45.93 |
| 3 | `CH3NH + Li <=> CH3NHLi` | Li⁺ + CH₃N•H + e⁻ → CH₃N(H)Li | 20.69 | 16.10 |
| 4 | `SH + Li <=> SHLi` | Li⁺ + •SH + e⁻ → LiSH | 20.35 | 19.81 |

λᵢ in kJ/mol, by executing `Marcus.get_lmbd_i(T)` on each entry's own unmodified coefficients
[R]+[D]. The five coefficient vectors are pairwise distinct in all four components, so this is
**not one calculation re-entered with substituent relabelling** — that would show shared or
trivially scaled coefficients. The spread is structured: the two carbon-centred radicals sit at
46–54 kJ/mol, the three heteroatom-centred ones at 16–22 kJ/mol, a clean 2.4× separation that the
rate-rule tree then rediscovers as its `2R->C` / `N-2R->C` split.

All five share, identically: `A = 1.73e+06 m^3/(mol*s)`, `n = 2`, `beta = 1.2e+10 m^-1`,
`wr = wp = lmbd_o = 0`, `rank = 3`, and the single-line provenance note
`"Calculated using a geometric mean with the four point method at
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp"` [D].

### 3.5 The answer Phase 1 exists to produce

> **How many independent quantum-chemical calculations do these twelve objects actually rest on?**
>
> **Five — and each of the five supplies λᵢ only.**

Five independent four-point λᵢ determinations, one per radical. The seven rules add none. And even
the five are narrower than "five calculations" suggests: the four-point method computes the
*inner-sphere reorganisation energy* from four single-point energies at two geometries [L] the
method as reassessed in "Reassessment of the Four-Point Approach to the Electron-Transfer
Marcus–Hush Theory", *ACS Omega* **2** (2017) 7846, doi:10.1021/acsomega.7b01425. It yields **no**
ΔG, **no** prefactor, **no** outer-sphere term, **no** temperature range and **no** uncertainty.
Every one of those is supplied from elsewhere, or set to zero.

**Consequence, stated as the ruling asks it to be:** any search for calculation directories should
be sized at **five**, and should expect λᵢ jobs — geometry optimisations and single points on R•,
its charged counterpart and RLi at `wb97x-d3/def2-tzvp` with `ccsd(t)-f12/cc-pvdz-f12` energies —
not twelve rate calculations. A search that goes looking for twelve, or for reaction rates, will
come back empty for the wrong reason.

---

## 4. Phase 2 — the provenance search

Six items, each with what was found, where, and — where nothing was found — the search space named.

### 4.1 Commit history, authors and dates

**Found, completely.** The family's entire history is five commits, by one author.

| commit | date | author | what it did |
|---|---|---|---|
| `dd4852f68` | 2021-12-14 | Matt Johnson `<mjohnson541@gmail.com>` | `Cation_R_Recombination initial family` — created `groups.py`, `rules.py` |
| `cc7ef729b`, `2f220fc89`, `863c05aab` | 2022-01-11 | Matt Johnson | bulk tree generation (touched siblings, not this family's rules) |
| `4c3faffdf` | **2024-03-09 18:21:21 −0800** | Matt Johnson | `add training reactions for Cation_R_Recombination` — the five Marcus training entries and `training/dictionary.txt`, both created from nothing |
| `b23abeb0c` | **2024-03-09 18:21:39 −0800** | Matt Johnson | `train Cation_R_Recombination` — regenerated `groups.py` (+87 lines of tree) and replaced `rules.py` wholesale with the seven Marcus rules |

Two facts fall out of this that no other source records.

**(a) Eighteen seconds.** `4c3faffdf` and `b23abeb0c` are 18 s apart. That is a script run, not two
human edits, and it independently corroborates §3.2: the rules were machine-generated from the
training set the instant it landed.

**(b) The Marcus set *replaced* a charge-transfer set.** Before `b23abeb0c`, `rules.py` held
**exactly one** entry, and it was not Marcus [D] `git show b23abeb0c^:…/rules.py`:

```python
kinetics = ArrheniusChargeTransferBM(A=(7.25239e+06,'m^3/(mol*s)'), n=0.211611,
    w0=(159759,'J/mol'), E0=(7480.68,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'),
    uncertainty=RateUncertainty(mu=-0.0396322771044, var=5.01691061618, Tref=1000.0,
    N=145, correlation='Root',),
    comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 4.58987665919"""),
rank = 0,
```

So on 2024-03-09 the family was **converted** from a Blowers–Masel charge-transfer parameterisation
— which carries `V0`, `alpha` and `electrons`, i.e. explicit electrode semantics — to a Marcus
parameterisation, which carries none of them. That conversion is the moment the electrode semantics
left the entries, and it is recorded nowhere but in this diff. §6.1 returns to it.

`training/reactions.py` before `4c3faffdf` was the bare template header — **no prior training data
was overwritten** [D] `git show bd15dd825^:…/training/reactions.py`.

### 4.2 References, citations, DOIs or comments naming the source model

**Nothing, and the negative result is informative.**

```
$ grep -rn "doi\|DOI\|http\|reference\|Reference" input/kinetics/families/Cation_R_Recombination/
(no output)
```

The only provenance text anywhere in the family is the five identical `longDesc` lines quoted in
§3.4. No DOI, no URL, no author, no report, no calculation identifier, no date, no software name.

**What makes this informative** is the contrast with the sibling families created in the same
lithium campaign by the same author. `1,2_Elimination_LiR`, `1,2_Intra_Elimination_LiR`,
`Li_Addition_MultipleBond` and the lithium additions to `H_Abstraction` all carry the *full*
ARC/Arkane stamp on each training entry [D] — optimised TS geometry in Cartesian coordinates,
external symmetry and optical isomer counts, 1-D rotor scan results with invalidation reasons, and
a longer level-of-theory line:

```
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvpused COSMO TZPD-Fine with energy files
    fit to dGsolv298 for library solvents:
    ["water","butanol","dimethylformamide",…,"diethyl carbonate","dimethyl carbonate",]
    MAE error: 3473.2666466033193 J/mol
```

[D] `input/kinetics/families/1,2_Elimination_LiR/training/reactions.py:230`,
`…/Li_Addition_MultipleBond/training/reactions.py:37`, and three more.

The `Cation_R_Recombination` note is the **first clause of that same string with everything after it
removed** — same level of theory, but no COSMO clause, no solvent fit, no MAE, no geometry, no
rotors. Two readings, and the evidence does not separate them:

- **[I-a]** The Marcus λᵢ jobs came from a different, hand-run workflow than the automated ARC
  pipeline that stamped the siblings, and simply never had that record to write.
- **[I-b]** They came from the same pipeline but were transcribed by hand into the training file
  with only the level-of-theory fragment carried across.

Either way the operative fact is the same, and it is one of the ticket's answers: **whether the λᵢ
determinations included an implicit-solvation model is not recorded for these five, while it is
recorded for their siblings.** That is a lost decomposition detail of exactly the kind the ruling
describes, and §6.5 weighs it as a failure-mode candidate.

### 4.3 Calculation directories, input/output files, supporting data

**None. Not one file, anywhere reachable.**

Search space, named in full:

1. This database, all 355 fetched refs, for the level-of-theory string:
   `git log --all -S "ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp"` → 10 commits, **all of them
   `training/reactions.py` edits in one family or another**. No commit ever added a calculation
   directory, a log file, an Arkane input, a `.yml` job file, or a geometry file to this repository.
2. This database's working tree: `find`/`grep` for `*arkane*`, `*calc*`, `*.out`, `*.log`, `*.yml`
   under any `Cation*` path → nothing.
3. `/home/alon/Code/RMG-Py-plasma`, whole tree, for the same level-of-theory string → two hits, both
   irrelevant: a test fixture database and an Arkane documentation example.
4. The `official/lithium` and `official/lithium_reorder` branches — where the campaign lived — for
   any non-`input/` content: `git ls-tree -r --name-only official/lithium | grep -v '^input/'` → CI
   configuration, conda recipes, `README.rst`, and family diagram PNGs. **No scripts, no notebooks,
   no data directories.**
5. The shared prefactor: `git log --all -S "1.73e+06"` → only the six Marcus commits of §3.3.
   `git grep "1.73e"` across the working tree → unrelated `H_Abstraction` and `Birad_recombination`
   entries. **`A = 1.73e6 m³/(mol·s)` with `n = 2` appears nowhere else in either repository.**

RMG-database is a data repository and has never hosted quantum-chemistry job trees; that these are
absent is expected. The finding is not that they are missing from an odd place — it is that **no
pointer to where they live was ever recorded either.**

### 4.4 Solvent, electrode, reference electrode, applied potential

**Found — and this is the substantive recovery of the ticket.** It is not in this database and not
attached to the entries; it is in the reference runtime repository, as a worked example input.

`Cation_R_Recombination` is a member of the `electrochem` family group [D]
`input/kinetics/families/recommended.py:177`, inside the set at lines 165–182 alongside
`Surface_Proton_Electron_Reduction_*`, `1,2_Elimination_LiR` and the other Cation families. Two RMG
input files in the reference runtime enable that whole group and are therefore the family's only
identified consumers [R] `/home/alon/Code/RMG-Py-plasma/examples/rmg/SEI_pure_EC/input.py:7`,
`…/SEI_pure_ACN/input.py:7`. SEI = solid electrolyte interphase; these are lithium-ion battery
models.

Read off `examples/rmg/SEI_pure_EC/input.py` verbatim [R]:

| quantity the ruling asks for | value | line |
|---|---|---|
| **Solvent** | ethylene carbonate — `solvation(solvent='ethylene carbonate')` | 250-252 |
| **Electrode** | lithium metal, (110) facet — `catalystProperties(metal = 'Li110')` | 62-64 |
| **Applied potential** | `liqPotential=(-1.0,'V')`, `surfPotential=(0.0,'V')` | 236-237 |
| **Temperature** | 298.15 K | 235 |
| **Reactor** | `liquidSurfaceReactor`, surface/volume ratio 1.0e5 m⁻¹ | 234-248 |
| **Thermo libraries** | `['electrocatLiThermo','primaryThermoLibrary','LithiumPrimaryThermo','LithiumAdditionalThermo','thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo']` | 3 |
| **Bulk species** | Li⁺ at 15.0 mol/m³ and ethylene carbonate at 15.17 mol/dm³, both held constant | 238-247 |

`SEI_pure_ACN/input.py` is the same model in **acetonitrile**, with `liqPotential` at `+0.3 V` and a
second reactor at `0.0 V` [R] lines 98-120, 133-134.

The solvent's own physical constants are in this database [D]
`input/solvation/libraries/solvent.py:8678` — ethylene carbonate, `eps = 95.3`, `n = 1.420` — added
by the same author in `48709a5ec` (2023-12-07) *"add dielectric constant and index of refractions
from literature from carbonate compounds"*. Those two numbers are precisely and only the inputs an
outer-sphere reorganisation term needs. **`lmbd_o = 0` on all twelve entries** [D].

**Reference electrode: a candidate exists, and it is not the one the example loads.**
`input/thermo/libraries/computationalLithiumElectrode.py` states its convention in its own header
[D] lines 5-14:

```
This library uses the computational lithum electrode model where
Li+ + e- = Li(s) @ -3.04 V vs SHE
If using this library, the potential in your input file
will be referenced to the Li/Li+ electrode (not SHE)
For example, if you set your reactor potential to O V,
that would be -3.04 V vs SHEs
```

and it implements it: entry 3 `Li_ion` (`1 Li u0 p0 c+1`) is given `H298 = 0 kcal/mol`,
`S298 = 29.12 J/(mol·K)` and the Cp of **Li(s)** [D], while entry 2 `electron` is an identically
zero NASA polynomial [D]. That is the computational-electrode convention — the lithium analogue of
the computational hydrogen electrode.

**But neither SEI input loads that library** [R] `SEI_pure_EC/input.py:3`,
`SEI_pure_ACN/input.py:3` — both load `LithiumPrimaryThermo`, whose `[Lip]` entry 65 is a bare
gas-phase Li⁺: monatomic NASA coefficients (a₁ = 2.5), `Cp0 = CpInf = 20.7862 J/(mol·K)` = 5R/2,
`E0 = 526.738 kJ/mol`, geometry a single Li atom [D] `LithiumPrimaryThermo.py:3095-3120`.

**Two mutually incompatible Li⁺ references therefore sit in the same database**, and which one is
in force is decided by an input file that lives in a different repository. Measured [probe1, probe2]:

```
T =  298 K   G(LithiumPrimaryThermo [Lip])           =  493.332 kJ/mol
             G(computationalLithiumElectrode Li_ion) =   -8.678 kJ/mol   gap = 502.010 kJ/mol
T = 1000 K   G(LithiumPrimaryThermo [Lip])           =  389.471 kJ/mol
             G(computationalLithiumElectrode Li_ion) =  -42.854 kJ/mol   gap = 432.325 kJ/mol
```

**A 502 kJ/mol reference ambiguity, sitting directly inside ΔG of all twelve entries.** §5 tests it.

### 4.5 The association step — is `K_assoc` recorded?

**No, and its slots are dead code in both runtimes.**

The ruling states the overall rate was `k_overall = K_assoc · k_ET`. In the Marcus formulation the
precursor- and successor-complex work is carried by `wr` and `wp`. Both exist as fields. Neither is
ever read.

**RMG-Py** [R] `rmgpy/kinetics/arrhenius.pyx:3617-3624`:

```python
cpdef double get_gibbs_activation_energy(self, double T, double dGrxn) except -1:
    lmbd_i = self.get_lmbd_i(T)
    return (lmbd_i+self.lmbd_o.value_si)/4.0*(1.0+dGrxn/(lmbd_i+self.lmbd_o.value_si))**2
```

`wr` and `wp` are constructed, stored, exposed as properties, and included in `__repr__` and
`__reduce__` — and appear in no arithmetic anywhere in the class.

**ReactionMechanismSimulator** [R] `official/fix/py311_ci:src/Calculators/Rate.jl:42-58`:

```julia
@with_kw struct Marcus{...} <: AbstractRate
    A::N ; n::K ; lmbd_i_coefs::Q ; lmbd_o::K ; wr::K = 0.0 ; wp::K = 0.0 ; beta::B ; unc::P
end
@inline function (arr::Marcus)(;T,P=0.0,C=0.0,phi=0.0,dGrxn=0.0,d=0.0)
    lmbd = arr.lmbd_o + evalpoly(T,arr.lmbd_i_coefs)
    arr.A*T^arr.n*exp(-lmbd/4.0*(1.0+dGrxn/lmbd)^2/(R*T)-arr.beta*d)
end
```

Same picture: `wr`/`wp` are struct fields the rate functor never touches. And they are faithfully
carried across the boundary between the two — `rmgpy/yaml_rms.py:172-180` serialises `wr` and `wp`
into the `.rms` file, and `rmgpy/rmg/reactionmechanismsimulator_reactors.py:660-663` passes them
into the Julia constructor — so the pipeline preserves, end to end, two numbers that nothing
consumes.

**Is `K_assoc` folded into `A`? UNKNOWN.** The shared `A = 1.73e6 m³/(mol·s)` with `n = 2` is a
bimolecular prefactor with a `T²` temperature dependence that is neither the `T^0.5` of collision
theory nor the `T¹` of an Eyring frequency factor. `A·T²` = 1.54e11 m³/(mol·s) at 298 K, roughly
four orders of magnitude *above* the diffusion limit in a liquid, so it is not a diffusion-limited
encounter frequency either. Whether the `T²` and the magnitude arise from an association equilibrium
absorbed into the prefactor, or from something else, cannot be determined: the value appears
**nowhere else in either repository** (§4.3 item 5), it carries no comment, and the only other
Marcus entry this author ever wrote uses different values (`A = 6.0e12`, `n = 1.0`; §4.6b).
**What would settle it:** the derivation or the script that produced `1.73e6, n = 2` — see §7.

**Recorded irrecoverably, or merely unrecorded?** Unrecorded, and worse: if `K_assoc` *was* folded
into `A`, the fold is not merely undocumented but **unreversible from the stored data**, because `A`
is a single number shared by all five entries while `K_assoc` for an ion-pair encounter would differ
per radical. A shared prefactor cannot carry a per-radical association constant. [I], resting on the
five entries having identical `A` [D] and distinct radicals [D].

### 4.6 Can the original model be identified precisely enough to be reproduced?

**Identified: yes — to the level of the rate law, the solver, the solvent, the electrode and the
reactor conditions. Reproduced: no.** §7 separates these.

What *is* identified precisely, and was not before this ticket:

**(a) The rate law and its original implementation.** Marcus kinetics entered
ReactionMechanismSimulator.jl in commit `f1c175b58`, *"add Marcus kinetics type and allow dGrxn
dependence of kinetics"*, **Matt Johnson, 2024-02-03** — five weeks before the training entries
landed. The source is reachable from this repository: a branch of the RMG-database remote,
`official/fix/py311_ci`, carries the RMS source tree (`src/Calculators/Rate.jl`, `src/Domain.jl`,
`src/Interface.jl`, `src/testing/ORR.rms`). The full rate law, verbatim, is quoted in §4.5.

**(b) The author's own reference case for it**, added 16 minutes later in `8c308fdbd`, *"add a
Marcus reaction to the ORR.rms mechanism for testing"* [D] `src/testing/ORR.rms`:

```yaml
- kinetics: {A: 6.0e12, lmbd_o: 100000.0,
             lmbd_i_coefs: [2.63844404e+03 9.64948798e+00 7.41268237e-03 -6.10277107e-06],
             beta: 1.2e10, n: 1.0, d: 0.0, type: Marcus}
  products: [HOOA] ; reactants: [O2A, H+] ; electronchange: -1 ; reversible: false
```

ORR is the oxygen reduction reaction; the `A` suffix marks adsorbed species. **This is the
electrochemical calibration case for the Marcus type, and it is nothing like the Li entries**:
`lmbd_o = 100 kJ/mol` where the Li entries carry `lmbd_o = 0`; `n = 1.0` where they carry `n = 2`;
`reversible: false` where the Li family declares `reversible = True` [D]
`Cation_R_Recombination/groups.py:13`. The only parameter the two share is `beta = 1.2e10 m⁻¹`
(= 1.2 Å⁻¹, the conventional electron-tunnelling decay constant).

**(c) The driving-force plumbing — including where a reference potential *would* live.** In RMS the
electrode-interface path is [R] `official/fix/py311_ci:src/Interface.jl:97-107`:

```julia
dGrxns = -M*Gpart
electronchanges = [hasproperty(reaction, :electronchange) ? reaction.electronchange : 0.0 for ...]
referencepotentials = [hasproperty(reaction.kinetics, :V0) ? reaction.kinetics.V0 : 0.0 for ...]
...
dGrxns .+= electronchanges.*(phi.-referencepotentials).*F
kfs = getkf.(reactions,nothing,T,0.0,0.0,Ref([]),A,phi,dGrxns,0.0)
```

**`V0` is a field of `Arrheniusq`, not of `Marcus`** [R] `src/Calculators/Rate.jl:35` vs `:42-50`.
So `hasproperty(Marcus, :V0)` is `false`, the reference potential silently defaults to `0.0`, and
`dGrxn` for a Marcus reaction is shifted by the **full absolute** `n_e·φ·F` with no reference
subtracted. This is the central structural finding of the ticket:

> **The electrochemical driving-force reference is not "lost in translation" from the source model
> to this database. It was never representable in the Marcus type at all** — not in the Julia
> original, not in the RMG-Py port, not in the `.rms` serialisation between them. The
> `ArrheniusChargeTransferBM` rule that the Marcus set *replaced* in `b23abeb0c` (§4.1b) did carry
> `V0`.

[R], four files, both languages.

**(d) Two further parameters that cannot reach the rate from a database entry.**

- **`beta` is inert through the RMG path.** The `exp(−β·d)` tunnelling term needs a distance `d`.
  In RMS, `d` is a *domain* field with default `0.0` [R] `src/Domain.jl:485,512`, populated only
  from an `initialconds` key `"d"` [R] `src/Domain.jl:519-520`. RMG never writes that key: neither
  `rmgpy/rmg/input.py:966-1047` — where `liquidSurfaceReactor` accepts `surfPotential` and
  `liqPotential` and nothing else of this kind — nor
  `reactionmechanismsimulator_reactors.py:544-546` supplies one. So `d = 0`, `exp(−β·d) = 1`,
  always. In the RMG-Py port the term is **absent from the rate law entirely** [R]
  `arrhenius.pyx:3594-3609`; `beta` is stored and never read.
- **`lmbd_o` is dropped by the rule-fitting code.** `average_kinetics` sums and averages
  `lmbd_i_coefs`, `beta`, `wr` and `wp`, but **never touches `lmbd_o`**, and the `Marcus(...)` it
  constructs at [R] `family.py:4884-4892` does not pass `lmbd_o` at all — so a fitted rule takes the
  constructor default of `(0, 'J/mol')` regardless of what its training entries carried. Here every
  training `lmbd_o` is already 0, so nothing was lost. **The defect is latent, not active**, and
  §9.4 records it.

---

## 5. The reference ambiguity, measured

§4.4 established that two Li⁺ references sit in this database 502 kJ/mol apart. This section
measures what each does to the twelve. **Nothing here refits λ.** λ is read from the stored
coefficients unchanged in every column; the only things varied are which stored Li⁺ thermochemistry
ΔG is computed against and — in §5.3 — whether the solvation correction the source model declares is
applied.

### 5.1 The current path reproduced

A control first. Evaluating the five as the runtime does today
(`Reaction.get_rate_coefficient` → `get_free_energy_of_reaction` at potential 0 →
`Marcus.get_rate_coefficient` [R] `reaction.py:1111-1142`) reproduces
`docs/i092-reverse-direction-census.md` §4 to four significant figures for the three entries whose
thermochemistry both probes resolved identically — NH₂ 1.032e-179, C₂H₅ 1.044e-23, CH₃ 7.129e-40 at
1000 K. The probe is calibrated against the prior census.

### 5.2 The two references, side by side

k in m³/(mol·s), λ in kJ/mol from the stored coefficients, ΔG in kJ/mol. `[LPT]` = Li⁺ from
`LithiumPrimaryThermo` — what the runtime uses today, and what the SEI example loads; `[CLE]` = Li⁺
from `computationalLithiumElectrode`. Every neutral species' thermochemistry is identical between
the two columns.

**T = 1000 K**

| entry | λ | ΔG [LPT] | k [LPT] | ΔG [CLE] | k [CLE] | orders recovered |
|---|---|---|---|---|---|---|
| NH₂ | 20.96 | −574.9 | 1.03e−179 | −142.6 | 1.04e+03 | 182 |
| C₂H₅ | 54.08 | −436.0 | 1.04e−23 | −3.7 | **4.21e+11** | 34 |
| CH₃ | 45.93 | −471.1 | 7.13e−40 | −38.7 | **1.67e+12** | 51 |
| CH₃NH | 16.10 | −537.9 | 2.38e−209 | −105.5 | 5.58e+05 | 214 |
| SH | 19.81 | −610.7 | 1.14e−218 | −178.3 | 4.66e−05 | 213 |

**T = 298 K**

| entry | λ | ΔG [LPT] | k [LPT] | ΔG [CLE] | k [CLE] |
|---|---|---|---|---|---|
| NH₂ | 21.71 | −648.8 | 0 (underflow) | −146.8 | 3.86e−21 |
| C₂H₅ | 51.65 | −510.1 | 6.96e−168 | −8.1 | **3.80e+09** |
| CH₃ | 50.94 | −543.9 | 1.26e−198 | −41.9 | **1.31e+11** |
| CH₃NH | 20.69 | −608.5 | 0 (underflow) | −106.5 | 3.99e−05 |
| SH | 20.35 | −676.1 | 0 (underflow) | −174.1 | 1.91e−40 |

Read this carefully, because it is the ticket's central measurement and it cuts both ways.

- **The reference substitution recovers 34 to 214 orders of magnitude.** That is the dominant term
  in the collapse by an enormous margin. No other candidate in §6 is within a hundred orders of it.
- **For the two carbon-centred radicals it recovers the rate completely.** `A·T^n` = 1.73e12 at
  1000 K is the entries' own barrierless ceiling; C₂H₅ reaches 4.21e11 and CH₃ reaches 1.67e12 —
  the reaction becomes the barrierless radical–cation recombination it physically is.
- **For the three heteroatom-centred radicals it does not.** They land at 1.0e3, 5.6e5 and 4.7e−5,
  still 6 to 17 orders below that ceiling, because ΔG is still 5–9 λ past the inverted-region apex.

**Conclusion: the driving-force reference is the dominant missing term, and substituting the one
candidate reference this database records does not by itself restore all five entries.** Stated
plainly: it is not the whole story, and the residual is real. §6 does not manufacture a culprit for
that residual.

### 5.3 The other candidate: the solvation correction the source model declares

The SEI model runs in liquid ethylene carbonate with `solvation(...)` enabled (§4.4), so every
species' free energy gets a solvation correction the gas-phase evaluation omits. Measured against
this database's own solvation data [probe3, probe4]:

```
ΔGsolv(Li⁺, ethylene carbonate, 298 K) = -378.75 kJ/mol      ΔHsolv = -544.6 kJ/mol
ΔGsolv(•CH₃, ethylene carbonate, 298 K) =   +0.20 kJ/mol
```

Same sign and same order of magnitude as the 502 kJ/mol reference gap — an independent candidate for
the same missing term. Applied to all three species of each reaction at the source model's own
298.15 K:

| entry | ΔG gas | ΔG with EC solvation | k gas | k with EC solvation |
|---|---|---|---|---|
| NH₂ | −648.9 | −340.1 | 0 | 4.37e−194 |
| C₂H₅ | −507.4 | −212.8 | 1.12e−165 | 1.44e−11 |
| CH₃ | −544.3 | −250.7 | 7.11e−199 | 7.75e−24 |
| CH₃NH | −608.5 | −297.9 | 0 | 3.61e−152 |
| SH | −676.1 | −406.4 | 0 | 3.42e−310 |

**It recovers 130–160 orders of magnitude and still leaves every entry unusable.** And the number
itself is not trustworthy: RMG's solvation is an Abraham/Mintz LSER fitted on **neutral** solutes,
and the group-additivity descriptors it returns for Li⁺ (`L = 56.24`, `S = 11.05`, `B = 9.02`,
`E = 7.74`) are far outside the range any of those parameters take for a real neutral solute
[probe3]. The products inherit the same spurious lithium contribution
(ΔGsolv(RLi) = −80 to −117 kJ/mol) [probe4]. **This table is a magnitude check, not a
reproduction**, and it is reported as such.

---

## 6. The failure modes, decided

The ruling's candidate explanations, each marked supported / ruled out / open, with its evidence.
Where the evidence does not separate two candidates, that is said rather than resolved.

### 6.1 A missing or zeroed driving-force reference — **SUPPORTED, and dominant**

The strongest-evidenced candidate, on four independent lines:

1. **Structural.** The Marcus type has no `V0` field in either language, so the RMS interface path
   that subtracts a reference potential —
   `dGrxns .+= electronchanges.*(phi.-referencepotentials).*F` [R] `Interface.jl:105` — silently
   uses `0.0` for every Marcus reaction [R] `Interface.jl:99`. There is no slot for a reference to
   be stored in.
2. **Historical.** The rule the Marcus set replaced was `ArrheniusChargeTransferBM`, which carries
   `V0`, `alpha` and `electrons` [D] §4.1b. The 2024-03-09 conversion removed the only field the
   family had ever had for an electrode reference.
3. **Numerical.** Substituting the one alternative reference this database records moves the rates
   by 34 to 214 orders of magnitude and restores two of five to their barrierless ceiling (§5.2).
   Nothing else in this list moves them by more than ~10.
4. **Documentary.** Two incompatible Li⁺ references coexist in this database, 502 kJ/mol apart, and
   one of them announces in its own header that it redefines the potential origin [D] §4.4.

**But it is not sufficient on its own.** Three of five entries remain 6–17 orders below their
ceiling under the recovered reference (§5.2). So this failure mode is supported as the dominant
term and **not** as the sole one.

### 6.2 The association equilibrium `K_assoc` lost or double-counted — **OPEN, and undecidable from the repositories**

The slots exist, are zero on all twelve, and are dead code in both runtimes (§4.5). Whether
`K_assoc` was folded into `A = 1.73e6, n = 2` cannot be determined, and if it was, it cannot be
unfolded: one shared prefactor cannot carry five per-radical association constants (§4.5). No
evidence supports it; no evidence rules it out. **What would settle it:** the derivation of the
prefactor. §7 item 3.

### 6.3 An electrode potential term evaluated at a value the source never used — **PARTLY RULED OUT, and the residual is a different defect**

Ruled out as an explanation of the collapse: the applied potential reaches Marcus kinetics only
through ΔG, and the source model's own declared values are `liqPotential = −1.0 V`,
`surfPotential = 0.0 V` [R] `SEI_pure_EC/input.py:236-237`. One volt is 96.5 kJ/mol per electron —
**four to six times too small** to close a 432–502 kJ/mol gap, and of the wrong sign to help. The
collapse is not a potential-value error.

*Not* ruled out, and recorded here because it surfaced while establishing the above: the RMS
interface constructor takes its `phi` from the **surface** domain, not the liquid one —
`if isa(domain2.phase, IdealSurface); phi = domain2.phi` [R] `Interface.jl:100-104` — and RMG
constructs it without passing `phi` at all [R] `reactionmechanismsimulator_reactors.py:549-559`, so
the interface reactions see `surfPotential` (0.0 V) and the `liqPotential` (−1.0 V) the user wrote
never reaches them. That is a live defect in the reference runtime, worth a ticket of its own, and
it is **not** the cause of this collapse — see the arithmetic above.

### 6.4 A unit or sign convention lost in translation — **RULED OUT for the collapse**

Checked directly. The RMS and RMG-Py rate laws are algebraically identical on the terms both
implement:

```
RMS   : A*T^n * exp( -λ/4*(1+ΔG/λ)^2 / (R*T) - β*d ),   λ = lmbd_o + Σ cᵢTⁱ
RMG-Py: A*T^n * exp( -ΔG‡/(R*T) ),   ΔG‡ = (λᵢ+λₒ)/4*(1+ΔG/(λᵢ+λₒ))^2
```

[R] `Rate.jl:51-58` vs `arrhenius.pyx:3594-3624`. Same parabola, same sign on ΔG, same units —
J/mol throughout, with `lmbd_i_coefs` dimensionless-typed and read as J/mol by `get_lmbd_i`. Units
on the stored entries are internally consistent: `A` in `m^3/(mol*s)`, `beta` in `m^-1` (training) /
`1/m` (rules), the same unit under two spellings. The `wr`/`wp` J/mol→kJ/mol change between training
and rules is the averaging code's doing (§3.2) and is numerically inert at zero.

Two real translation losses exist and neither collapses a rate: **`β·d` was dropped from the Python
port** — which *raises* k, since `exp(−β·d) ≤ 1`, and is inert anyway at `d = 0` — and **`lmbd_o` is
dropped by the rule fitter**, which is latent since all training `lmbd_o` are 0. Both are recorded
in §9.

### 6.5 A solvent-phase λ applied where the solvent term is meaningless — **OPEN, with a specific unrecorded fact at its centre**

The entries carry `lmbd_o = 0` — no outer-sphere term at all [D]. The author's own ORR reference
case carries `lmbd_o = 100 kJ/mol` [D] §4.6b. The solvent's ε and n are in this database [D] §4.4.
And the sibling lithium training entries record a COSMO implicit-solvation model in their
level-of-theory note while these five record only the first clause of that string, with the COSMO
part absent (§4.2).

So the open question is sharp and answerable — **were the five λᵢ determinations run in implicit
solvent or in vacuum?** — and it is not answerable from the repositories. Both readings are
consistent with `lmbd_o = 0`: an inner-sphere λᵢ computed in COSMO already carries some solvent
response, and one computed in vacuum carries none. **This report does not propose a value for λ or
λₒ and takes no position on which reading is right.** It records that the fact is unrecorded, and
names what would settle it (§7 item 2).

The 2.26 V spread across the five `V_peak` values that `docs/i092-reverse-direction-census.md` §10
left unexplained is the same question seen from another angle: a single constant convention offset
would give a single constant, and the spread implies at least one per-entry term is missing. §5.2's
residual — two of five restored, three not — is a third view of the same thing.

### 6.6 The kinetics evaluated at a temperature or in a phase the source never covered — **SUPPORTED as a real error, but secondary**

**Phase: supported.** The source model is a `liquidSurfaceReactor` in liquid ethylene carbonate at a
Li(110) interface [R] §4.4. The evaluations producing 10⁻²³–10⁻²²⁶ are gas-phase, at
`potential = 0`, with no solvation, in `SimpleReactor` and direct-call paths. That is a phase the
source model never covered, and §5.3 measures the resulting error at 130–160 orders of magnitude. It
is real, and it is mechanistically subsumed by §6.1: the way "wrong phase" hurts here is precisely
that the ion's reference/solvation term goes missing.

**Temperature: supported, smaller.** The entries carry no `Tmin`/`Tmax` [D] and the source model
runs at a single temperature, 298.15 K [R]. Evaluating them at 1000 K, as the prior census and this
report both do, is extrapolation past any validated range — the λᵢ cubics are being evaluated where
nothing constrains them. This is a caveat on the numbers, not a cause of the collapse: the collapse
is present at 298 K too, and worse (§5.2).

### 6.7 The `Marcus.get_rate_coefficient` pressure-for-ΔG defect — **explains none of the collapse**

The dispatch asks explicitly which part of the collapse this recently-fixed defect explains. The
answer is **none of it — and it is why the collapse went unseen for two and a half years.**

Before `ce58b97f6` [R] `/home/alon/Code/RMG-Py-plasma`, `Reaction.get_rate_coefficient` ended in a
bare `self.kinetics.get_rate_coefficient(T, P)`, so `Marcus` received the **pressure** in the
`dGrxn` slot. Two regimes, both measured [probe2b]:

| pre-fix regime | what Marcus saw | k(1000 K) for the five |
|---|---|---|
| No pressure supplied (`P = 0`) — the common case | `dGrxn = 0`, exactly thermoneutral | 9.2e11, 3.4e11, 4.3e11, 1.1e12, 9.5e11 |
| Reactor at 1 bar (`P = 1e5`) | `dGrxn = +1e5 J/mol` | 1.3e3, 3.2e6, 1.5e6, 2.0e1, 5.9e2 |

The `P = 0` row is the important one. **It returns 3e11–1e12 m³/(mol·s) — barrierless,
collision-limited, and entirely plausible.** The stored thermochemistry never entered the
calculation at all, so the reference error had no way to show. The 10⁻²³–10⁻²²⁶ figures are
**post-fix** numbers; they appeared only once `ce58b97f6` began resolving ΔG from real species
thermochemistry.

So the correct causal statement is:

> The pressure-for-ΔG defect is not a cause of the collapse. It is the reason the collapse was
> invisible: it substituted a physically plausible thermoneutral rate for the real one, silently,
> with no exception and no warning, for every Marcus reaction in the database.

A second-order note for anyone re-reading historical results: any rate quoted from this family
before `ce58b97f6` — including `docs/i041-cation-reachability.md` §4.3's `k(300) = 9.452e8` — is a
thermoneutral-barrier number, not a rate the stored thermochemistry supports. That is already
recorded as finding 1 of `docs/i092-reverse-direction-census.md` §9.

### 6.8 The summary the ruling asks for

| candidate | verdict | one-line evidence |
|---|---|---|
| Missing / zeroed driving-force reference | **SUPPORTED, dominant** | 34–214 orders recovered; no `V0` slot on `Marcus` in either language; two Li⁺ references 502 kJ/mol apart |
| Wrong phase / no solvation | **SUPPORTED, secondary; mechanistically the same term** | source model is liquid EC; 130–160 orders recovered, still unusable |
| Evaluation outside any validated T range | **SUPPORTED, minor** | no `Tmin`/`Tmax`; source model is single-T at 298.15 K |
| `K_assoc` lost or double-counted | **OPEN** | `wr`/`wp` zero and dead; prefactor origin unknown and unfoldable |
| Solvent-phase λ where λₒ is meaningless | **OPEN** | COSMO clause present on siblings, absent here; `lmbd_o = 0` vs ORR's 1e5 |
| Electrode potential at a value the source never used | **RULED OUT for the collapse** | 1 V = 96.5 kJ/mol, 4–6× too small and wrong sign |
| Unit or sign convention lost in translation | **RULED OUT for the collapse** | rate laws algebraically identical; the two real losses both raise k or are inert |
| The pressure-for-ΔG defect | **RULED OUT as cause; it is the concealment** | pre-fix at P = 0 returned 3e11–1e12, plausible and wrong |

**The evidence does not distinguish between the two OPEN candidates**, and it does not need to in
order to answer §7: both are unrecorded facts about the same five calculations, and one and the same
act recovers both.

---

## 7. Can the original electrochemical model be reproduced from what the repositories contain?

# No.

Not "not yet", and not "with effort". Four facts are required to reproduce it and **none of the four
is recorded anywhere in either repository**, on any of the 355 fetched refs.

| # | What is missing | Why it is required | Who or what would have it |
|---|---|---|---|
| 1 | **The Li⁺ thermochemistry the λᵢ set was computed alongside**, and hence the electron reference in force | ΔG enters the barrier quadratically; the two candidate references in this database differ by 502 kJ/mol and neither restores all five entries (§5) | The author's calculation record, or the job that produced the five λᵢ values. Not in this repository (§4.3) |
| 2 | **Whether the five λᵢ determinations used implicit solvation (COSMO), and in which solvent** | Decides whether `lmbd_o = 0` means "no solvent term needed, it is already inside λᵢ" or "the solvent term was omitted" (§6.5) | The same calculation record. The sibling families' entries prove the author's pipeline *did* record this when it ran (§4.2) |
| 3 | **The derivation of `A = 1.73e6 m³/(mol·s)`, `n = 2`** | It is the entire prefactor of all twelve entries, appears nowhere else in either repository, and is the only place `K_assoc` could have been folded (§4.5) | The author, or the script that wrote `training/reactions.py` on 2024-03-09 |
| 4 | **The association-step decomposition `k_overall = K_assoc · k_ET`** | `wr`/`wp` are zero and unread; a single shared prefactor cannot carry five per-radical association constants, so even if it was folded in it cannot be unfolded (§4.5) | The author. This one may be irrecoverable even from him, if the fold was implicit |

Items 1–3 are single facts that a single person could supply from memory or from a directory on a
disk. Item 4 may not exist in recoverable form at all.

**What *was* recovered, and should be recorded so the next ticket does not re-derive it:** the
solvent (ethylene carbonate, ε = 95.3, n = 1.420), the co-solvent variant (acetonitrile), the
electrode (Li(110) metal), the applied potentials (−1.0 V liquid / 0.0 V surface, and +0.3 V / 0.0 V
in the ACN model), the temperature (298.15 K), the reactor type (`liquidSurfaceReactor`), the solver
(ReactionMechanismSimulator.jl), the exact rate law in its original Julia, the author's own
electrochemical reference case for that rate law (ORR), the identity of the author, and the fact
that `Cation_R_Recombination` is a **lithium-ion battery SEI family**, not a plasma family.

That is a large recovery. It is not reproduction, and this report does not present it as one.

---

## 8. Read-only compliance

```
$ git status --porcelain
?? docs/i103-electrochemical-provenance.md

$ git diff --stat
(no output)

$ git diff --stat -- input/
(no output)
```

**No rate, no λ, no `A`, no `n`, no equation, no family, no group, no tree, no training entry, no
thermo file, no `reactions.py`, no `rules.py`, and no quarantine marker was changed** — in this
repository or in any other. No quarantine metadata was added, removed or altered: at the time of
writing `input/kinetics/families/Cation_R_Recombination/` contains `groups.py`, `rules.py` and
`training/` only, and the marker landing on `i102-quarantine-db` (`a739cdeee`,
*"kinetics: quarantine the Cation_R_Recombination Marcus data"*) has not merged here. It was read to
confirm it does not conflict with this report; it was not touched.

Nothing was written to `/home/alon/Code/RMG-Py`, `/home/alon/Code/RMG-Py-plasma`,
`/home/alon/Code/RMG-database-plasma`, or any other worktree. `RMG-Py-plasma` was read only — its
`git status` is unchanged and no build was run. The sole addition anywhere is this report; the
commit carrying it touches one file. (The ticket's contract note lives at
`docs/contracts/i103-electrochem-provenance.md` and is deliberately untracked — `docs/contracts/`
is in `.gitignore:28` — so it does not appear above and is not part of the commit.)

**One thing found that could invite an edit, recorded rather than acted on**, per the ruling's
prohibition on any production edit before the original is reproduced:

- **Would change:** nothing in this database. The `V0`-shaped hole is in the `Marcus` class in
  `RMG-Py-plasma` and in RMS, not in these entries. **Predicted effect of adding `V0` to `Marcus`:**
  it would give the reference a place to live, which is a precondition for ever storing one.
  **Predicted problem:** it is a schema change to a kinetics class in the upstream runtime, with no
  value to put in the new field until item 1 of §7 is answered — and an empty slot invites someone
  to fill it with a guess. A runtime decision, not a provenance decision.

---

## 9. Durable findings

Eight. The first five are defects in the pinned runtime; the rest are provenance facts not
previously recorded anywhere.

1. **The `Marcus` kinetics class has no reference-potential field in either implementation, and the
   RMS electrode-interface path silently substitutes `0.0` for it.** [R] `Rate.jl:42-50` (no `V0` in
   the struct) against `:35` (`V0` on `Arrheniusq`); [R] `Interface.jl:99,105`
   (`hasproperty(reaction.kinetics, :V0) ? … : 0.0`, then
   `dGrxns .+= electronchanges.*(phi.-referencepotentials).*F`). Any Marcus reaction at an electrode
   is evaluated against the absolute potential with no reference subtracted, with no diagnostic.
   This is the structural root of the ticket.

2. **`wr` and `wp` are dead parameters in both runtimes.** Declared, stored, exposed as properties,
   serialised into `.rms` files [R] `yaml_rms.py:172-180`, passed into the Julia constructor [R]
   `reactionmechanismsimulator_reactors.py:660-663` — and read by no arithmetic anywhere [R]
   `arrhenius.pyx:3617-3624`, `Rate.jl:51-58`. The entire association/work-term decomposition of
   Marcus theory is unimplemented while appearing to be supported.

3. **`beta` is dead through the RMG path.** The `exp(−β·d)` tunnelling term is absent from the
   RMG-Py rate law entirely [R] `arrhenius.pyx:3594-3609`; in RMS it survives, but `d` is a domain
   field defaulting to `0.0` [R] `Domain.jl:485,512,519-520` that RMG never populates [R]
   `rmg/input.py:966-1047`, `reactionmechanismsimulator_reactors.py:544-546`. Every stored
   `beta = 1.2e10 m^-1` is inert.

4. **`average_kinetics` silently drops `lmbd_o` when fitting a Marcus rate rule.** It accumulates
   `lmbd_i_coefs`, `beta`, `wr` and `wp`, never `lmbd_o`, and constructs `Marcus(...)` without
   passing it [R] `family.py:4846-4892`. A rule fitted from training entries with a non-zero
   outer-sphere reorganisation energy would silently get `lmbd_o = 0`. **Latent here** — all five
   training entries carry `lmbd_o = 0` — but it will fire the first time anyone trains a Marcus
   family in solvent.

5. **A `Marcus` class default is off by twenty orders of magnitude.** The constructor signature is
   `beta=(1.2e-10,"1/m")` [R] `arrhenius.pyx:3505`, while every stored entry and the RMS reference
   case use `1.2e+10 m^-1` (= 1.2 Å⁻¹, the conventional tunnelling decay constant). Inert today
   because finding 3 makes `beta` unreachable and because every entry specifies it explicitly. It
   would bite the moment either changes.

6. **Two mutually incompatible Li⁺ references coexist in this database, 502 kJ/mol apart at 298 K.**
   `LithiumPrimaryThermo.py` entry 65 `[Lip]` is a gas-phase monatomic cation
   (`E0 = 526.738 kJ/mol`, `Cp0 = CpInf = 5R/2`); `computationalLithiumElectrode.py` entry 3
   `Li_ion` defines `Li⁺ + e⁻ ≡ Li(s)` at 0 V vs Li/Li⁺ (`H298 = 0`, `S298 = 29.12`) and says so in
   its own header [D]. Which is in force is decided by an input file in a *different repository*,
   and the two SEI examples load the former. Nothing in this database flags the conflict.

7. **`Cation_R_Recombination` was converted from `ArrheniusChargeTransferBM` to `Marcus` on
   2024-03-09, and that conversion is when the electrode semantics left the entries.** The single
   prior rule carried `V0`, `alpha` and `electrons`; the seven Marcus rules that replaced it carry
   none of them [D] `git show b23abeb0c^:…/rules.py`. Recorded nowhere but in the diff.

8. **The family's provenance note is a truncation of its siblings'.** Every other lithium family
   trained in the same campaign carries the full ARC/Arkane record — TS geometry, symmetry, rotor
   scans, `used COSMO TZPD-Fine`, the solvent fit list and its MAE. These five carry the
   level-of-theory clause and nothing after it [D]. Whichever way that happened (§4.2), the
   operative loss is the same: **whether these λᵢ were computed in implicit solvent is not recorded
   here, and is recorded for every sibling.**

---

## 10. The gate: contacting the original author

**Step 7 of the ruling's search — contacting the original authors — was not attempted, and is not
mine to initiate.** It is stated here as a recommendation to the user, and nothing more.

§7 establishes that the provenance is **not recoverable from the repositories alone**, and names
four specific facts that are missing. Three of the four are single facts a single person could
supply. This report therefore recommends:

> **This now requires contacting the original author.**
>
> **Who:** Matt Johnson, `<mjohnson541@gmail.com>` — identified from the commit record as sole
> author of all five commits that created this family, of the RMS `Marcus` type five weeks earlier,
> and of the two SEI example models that consume the family. The identification is from
> `git log --format='%an <%ae>'` on `dd4852f68`, `4c3faffdf`, `b23abeb0c`, `f1c175b58`, `8c308fdbd`
> [D], not from any external source.
>
> **What to ask, in priority order** — §7's table restated as questions:
> 1. Which Li⁺ thermochemistry were the five λᵢ values computed alongside — the gas-phase
>    `LithiumPrimaryThermo` `[Lip]`, the `computationalLithiumElectrode` Li/Li⁺ convention, or a
>    third thing not in the database?
> 2. Were the five four-point λᵢ jobs run with COSMO implicit solvation, as their sibling lithium
>    families were, or in vacuum?
> 3. Where does `A = 1.73e6 m³/(mol·s)`, `n = 2` come from, and does it contain an association
>    equilibrium?
> 4. Do the five calculation directories still exist?
>
> **Why this rather than more work in the repositories:** §4.3 names five exhaustive search spaces
> that came back empty, and §5 shows that the two candidate references recoverable from the data
> restore two of five entries between them. There is no further repository-side evidence to find.

Nothing in this report should be read as authorising contact. It is the user's call and the user's
action.

---

## 11. What this report could not reach

Named rather than papered over, because each bounds what §5–§7 can claim.

- **Deleted or never-pushed branches.** Every `git` claim covers the 355 refs fetched into this
  clone (`official` to 2026-08-21, plus `origin` and local branches). A branch deleted before this
  clone's first fetch, or one that never left the author's machine, is outside every search in §3.3
  and §4.3. **This is the single largest limit on the "never, on any branch" claims** and it cannot
  be closed from here — only by someone with repository administration access, or with the author's
  local clone.
- **No reactor was run, and no RMS simulation was executed.** The RMS behaviour in §4.6 and §6.3 is
  read from Julia source on branch `official/fix/py311_ci` and reasoned from the entries' declared
  properties. Julia was not installed, `SEI_pure_EC` was not run, and the
  `liqPotential`/`surfPotential` defect in §6.3 was **not** demonstrated by execution. It is a
  source-reading claim and is labelled as such.
- **The RMS source read is a branch snapshot, not the upstream repository.** `official/fix/py311_ci`
  is a branch of the *RMG-database* remote that happens to carry the ReactionMechanismSimulator.jl
  tree, tip `cf83540e3` (Jackson Burns, 2025-05-23). Whether it matches the RMS release the SEI
  models were run against is UNKNOWN; the upstream RMS repository was not consulted, and no network
  access was used at any point in this ticket.
- **The Li⁺ solvation number is an out-of-range extrapolation, and §5.3 is a magnitude check, not a
  reproduction.** RMG's Abraham/Mintz LSER is fitted on neutral solutes; the descriptors returned
  for Li⁺ are far outside any physical neutral range (§5.3). A real ΔGsolv(Li⁺, EC) would need an
  ion-solvation model RMG does not have.
- **The literature search was confined to what is re-checkable from the repositories.** The
  four-point-method citation in §3.5 is carried over from `docs/i092-reverse-direction-census.md`
  §2.1 and re-verified against the entries' own wording. No publication behind
  `LithiumPrimaryThermo` or behind the SEI models was consulted — `docs/i092-reverse-direction-census.md`
  §10 already flags that gap, and nothing here closes it.
- **The 145-sample `RateUncertainty` on the superseded BM rule (§4.1b) was not traced.** Its
  `correlation='Root'` and `N=145` point at a global charge-transfer tree fit whose training set was
  not identified. It is superseded data and does not bear on the Marcus entries, but it is the one
  thread in §4.1 left unpulled.
- **Only `Cation_R_Recombination` was diagnosed.** The other members of the `electrochem` family
  group [D] `recommended.py:165-182` carry `ArrheniusChargeTransfer`/`ArrheniusChargeTransferBM`
  kinetics and were not examined. Findings 1–5 are `Marcus`-specific and do not transfer; findings
  6–8 plausibly do, since they concern the shared lithium campaign rather than the rate law.
