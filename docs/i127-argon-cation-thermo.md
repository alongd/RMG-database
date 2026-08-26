# I-127 — Argon has cation thermochemistry now, and the gap it came from is not a law

**Headline: `Ar⁺` is entered, sourced verbatim from NIST-JANAF table Ar-002 and corroborated
five independent ways — and the audit behind it found that the thermochemistry gap for charged
species is not an oversight list and not an arithmetic law like I-120's `q < Z − 12`, but two
structural gates in series, both owned outside this repository's thermo tree, which between them
predict every one of the 342 charge stages the shipped rate tables can drive.** `Ar₂⁺` was not
entered: the tabulated functions exist and are named below, and they could not be reached from
here.

**Answers, one line each.**

- **`Ar⁺` is in.** `input/thermo/libraries/PlasmaCationThermo.py`, one entry, `ΔfH°(298.15) =
  1520.581 kJ/mol`, `S°(298.15) = 166.404 J/(mol·K)`, `Cp°` on a 13-point grid, valid
  298.15–6000 K, `E0 = 1520.573 kJ/mol`. NIST-JANAF 4th ed., table Ar-002. §4.
- **The database's ion reference-state convention is the ION convention** — the electron priced
  at `H = S = Cp = 0` at all temperatures — established from the three shipped `electron`
  entries and from `Reaction._get_free_energy_of_charge_transfer_reaction`, not assumed. §3.
- **The dispatch's names for the two conventions are swapped** relative to the standard
  literature. The physics is unambiguous; the labels are not, and following the wrong dictionary
  applies the 6.197 kJ/mol correction in the wrong direction. §3.1.
- **The whole path works**: loads, resolves, a finite `Keq` at 300–6000 K, and `PlasmaReactor`
  accepts `Ar + e⁻ => Ar⁺ + 2 e⁻` evaluated at the shipped Voronov argon rate. §5.
- **The previously-uncarryable argon ionisation reaction is carried** — and it was carried in a
  scratch library, because adding a rate to this database is an explicit non-goal. The next
  missing thing is one entry in `PlasmaElectronImpactIonization`, owned by a kinetics ticket. §5.5.
- **The gap is a generation consequence, twice over.** Gate 1 is whether `rmgpy/molecule/
  atomtype.py` admits the element at that charge; gate 2 is whether some application project
  wrote a library entry, because no estimator in this database covers charge. §2.
- **Two defects found and deliberately not fixed.** The shipped `[Lip]` entry disagrees with
  lithium's ionisation energy by **144.86 kJ/mol** — 23× the entire convention gap, so it is not
  a convention choice. And group additivity, asked for a monatomic cation, **does not refuse**:
  it returns a number that puts the cation *below* the neutral for N, Si, Li, H and CH₃⁺. §2.3, §2.4.
- **`Ar₂⁺` is out of reach, not absent from the literature.** Maltsev, Morozov & Osina, *High
  Temperature* **57** (2019) 37–40 tabulate it over 298.15–10 000 K; the paper is closed access
  with no OA copy and ATcT returns HTTP 403 from here. §6.

Evidence labels: **[R]** code (file:line) · **[D]** database (file, entry) · **[M]** measured
(command and output shown) · **[L]** literature, full citation with table or equation ·
**[I]** inference with its basis.

---

## 1. Environment, pin, and what was written where

| Role | Path | State |
|---|---|---|
| Runtime, read-only | `/home/alon/Code/RMG-Py-i123-integration` | branch `i123-integration`, `3559bf431`, **unmodified, not rebuilt** |
| Data under test | `/home/alon/Code/RMG-database-i127-argon-thermo` | branch `i127-argon-thermo`, base `c7bd96292` |
| Interpreter | `/home/alon/anaconda3/envs/rmg_env/bin/python` | 3.9 |

**[M]** Every probe prints its resolution and its pin at the head, and asserts both:

```
python   : /home/alon/anaconda3/envs/rmg_env/bin/python
rmgpy    : /home/alon/Code/RMG-Py-i123-integration/rmgpy/__init__.py
PIN-BEFORE database.directory : /home/alon/Code/RMG-database/input
PIN-AFTER  database.directory : /home/alon/Code/RMG-database-i127-argon-thermo/input
```

`PIN-BEFORE` is the shared checkout. Leaving the pin to discovery would have measured a database
nobody edited — so `common.py` sets it and asserts it, and `test/conftest.py` does the same for
the suite.

**Nothing was built.** No `make`, bare or otherwise. **Nothing was written to any other tree**:
`git status` in the runtime worktree shows no tracked file modified and the same two untracked
YAML files that predate this session. Nothing was written to `/home/alon/Code/RMG-database`,
`/home/alon/Code/RMG-database-plasma`, `/home/alon/Code/RMG-Py`, or any other worker's worktree.

Five probes, both streams persisted, all outside every tracked tree under
`/tmp/claude-1000/-home-alon-Code-RMG-database-i127-argon-thermo/5f0bc24f-.../scratchpad/probes/`:
`probe1` (charged-species inventory and the convention), `probe2` (coverage over all 342 stages),
`probe3` (the whole path, stage by stage), `probe4` (the neutral→+1 row in detail), `probe5` (the
gap's shape and the estimator's error). Being scratch they are not durable; what is quoted here
is the record, and what matters is re-run by `test/test_argon_cation_thermo.py`.

**A probe defect worth recording, because it produced a confident wrong answer before it
produced a right one. [M]** `probe1`'s first draft loaded thermo libraries with
`ThermoLibrary().load(path, ThermoLibrary().local_context, ThermoLibrary().global_context)`.
That raises `AttributeError` on every file — and the draft caught the exception per library and
carried on, reporting **"NET-CHARGED entries found: 0"** and "single-Ar-atom entries anywhere: 0"
from 77 consecutive silent failures. The fix was an assertion that the number of libraries loaded
equals the number of `.py` files on disk, which every probe here now carries. A green that comes
from having measured nothing is the failure mode this campaign has already been damaged by, and
it nearly happened again in the first five minutes.

---

## 2. The coverage audit — *Verifier item 1*

### 2.1 The scope, and the two shipped tables' own arithmetic

**[D]** `input/kinetics/voronov.yaml` holds 13 elements and 134 ionisation stages;
`input/kinetics/badnell.yaml` holds 33 elements and 318 recombination stages. The union of
charge-stage transitions is **342**, and the cation on the `q+1` side of each is what needs
thermochemistry. **[M]** `probe2`, `probe5`:

```
distinct (Z, q) cations either shipped table drives : 342
  Z <= 20, i.e. an element RMG has any atom type for : 198
  Z >  20, no RMG atom type at any charge            : 144   Z = [21..30, 36, 42, 54]
```

**[M]** Before this branch, thermochemistry existed for **2 of 342**; after it, **3 of 342**.

### 2.2 The table

**[M]** `probe4`, `probe5`. The neutral → +1 stage, which is the only one a gas-phase mechanism
can currently use. `M⁺ ground` is whether RMG can construct the ion in its **gas-phase ground
state** — not whether some adjacency list with that charge happens to parse, which is a weaker
and misleading question (§2.5). `GAV` columns come from a database with every library unloaded,
so any number there is group additivity and HBI. `IE₁` is NIST ASD ver. 5.12 **[L]**.

| Z | el | driven by | M⁺ ground state | library thermo | GAV(M⁺) | GAV(M) | GAV rise | IE₁ | GAV error |
|---|----|-----------|-----------------|----------------|--------:|-------:|---------:|----:|----------:|
| 1 | H | ionise+recomb | **YES** `H+` | `proton` — *electrochemical* | 0.0 | 205.0 | −205.0 | 1312.0 | **−1517.1** |
| 2 | He | ionise+recomb | **YES** unconstrained | — none — | refused | refused | — | 2372.3 | — |
| 3 | Li | ionise+recomb | **YES** `Li+` | `[Lip]` — *§2.3* | −85.0 | 120.0 | −205.0 | 520.2 | **−725.2** |
| 4 | Be | recombine | NO `KeyError` | — none — | — | — | — | 899.5 | — |
| 5 | B | recombine | NO `KeyError` | — none — | — | — | — | 800.6 | — |
| 6 | C | ionise+recomb | NO `AtomTypeError` | — none — | — | — | — | 1086.5 | — |
| 7 | N | ionise+recomb | **YES** `N3sc` | — none — | 386.1 | 624.1 | −237.9 | 1402.3 | **−1640.3** |
| 8 | O | ionise+recomb | **YES** `O4sc` | — none — | 570.3 | 249.1 | +321.2 | 1313.9 | **−992.7** |
| 9 | F | recombine | NO `AtomTypeError` | — none — | — | — | — | 1681.0 | — |
| 10 | Ne | recombine | **YES** unconstrained | — none — | refused | refused | — | 2080.7 | — |
| 11 | Na | ionise+recomb | NO `KeyError` | — none — | — | — | — | 495.8 | — |
| 12 | Mg | ionise+recomb | NO `KeyError` | — none — | — | — | — | 737.7 | — |
| 13 | Al | ionise | NO `KeyError` | — none — | — | — | — | 577.5 | — |
| 14 | Si | ionise | **YES** `Sis` | — none — | 613.7 | 869.9 | −256.2 | 786.5 | **−1042.7** |
| 18 | **Ar** | ionise | **YES** unconstrained | **`PlasmaCationThermo`** | refused | refused | — | 1520.6 | — |
| 19 | K | ionise | NO `KeyError` | — none — | — | — | — | 418.8 | — |
| 20 | Ca | ionise | NO `KeyError` | — none — | — | — | — | 589.8 | — |

Enthalpies in kJ/mol. `GAV error` is `GAV rise − IE₁`: how far group additivity's answer falls
short of the *minimum* the ionisation energy requires.

**[M]** Above the neutral stage:

```
ground-state-representable cations, all (Z,q) : 18 / 342
  at q = +1 : 8 of 17   ['H','He','Li','N','O','Ne','Si','Ar']
  at q >= 2 : 10        [He2+, Ne2+..4+, Si2+..4+, Ar2+..4+]
```

and **[M]** no entry anywhere in the 78 thermo libraries carries net charge above +1
(`test_no_element_in_either_shipped_table_has_thermochemistry_above_charge_one`). So ten
representable multiply charged cations exist with no thermochemistry, and there representability
is *not* the binding constraint — data is.

### 2.3 Verdict: a generation consequence, and the shape is two gates in series

> **It is not a list of oversights and it is not an arithmetic law in `(Z, q)`.** I-120's
> `q < Z − 12` was a law because it was a predicate on the Badnell snapshot's isoelectronic
> ceiling — arithmetic, and predictive for anything added later. There is no such predicate
> here. The gap is decided by two gates, neither of which is about ionisation, charge stage, or
> nuclear charge, and neither of which lives in this repository's thermo tree.

**Gate 1 — representation. Owner: `rmgpy/molecule/atomtype.py`, i.e. RMG-Py.** Whether an atom
type admits the element at that charge. **[M]** `probe5` splits it three ways, and the split is
the whole story:

| kind | elements | behaviour |
|---|---|---|
| **no charged atom type at all** | Be, B, Na, Mg, Al, K, Ca | `KeyError` — cannot be built at any charge |
| **charged atom types exist, but not for the free atom's valence** | C, F, P, Cl | `AtomTypeError` |
| **charge-constrained atom type, declared `[1]`** | H (`H+`), Li (`Li+`), N (`N3sc`), O (`O4sc`) | builds at +1 and only +1 |
| **charge-*un*constrained atom type** | He, Ne, Si, Ar | builds at **any** charge, meaningful or not |
| **no atom type for the element at all** | Sc…Xe, 144 of the 342 stages | nothing to build |

**[I]** The pattern in the third row is a record of which unrelated projects needed a charged
atom, not of any plasma requirement: `N3sc`/`O4sc`/`S4sc` came in for organic zwitterions
(nitro groups, sulfoxides), `Li+` for battery electrolytes, `H+` for electrocatalysis. Basis:
the charged atom-type inventory printed by `probe5`, whose 54 entries are C/N/O/S/P/halogen
zwitterion types plus `H+`, `H-`, `Li+`, `e`.

**Gate 2 — data. Owner: whoever writes a library entry.** Given a representable cation, only a
hand-written library entry can supply its thermochemistry, because **no estimator covers charge**
(§2.4). So coverage is exactly the set of library entries, and library entries arrive one at a
time from application projects.

**Two clean arithmetic sub-laws are worth keeping**, since they are the predictive part:

- **For `Z > 20` — 144 of 342 stages, 42 % — coverage is exactly zero and cannot be otherwise**,
  because RMG has no atom type for those elements at any charge. Nothing added to either rate
  table changes this without an RMG-Py change.
- **Coverage is zero for every `q ≥ 2`**, for every element, and will stay zero until someone
  sources a multiply charged monatomic cation — which nobody has, here or in I-119/I-120.

### 2.4 Group additivity does not refuse a cation. It answers, and the answer's sign is wrong

This is the finding that makes "library entry or nothing" the only honest policy, and it is the
one a future ticket is most likely to trip over.

**[M]** `probe5`, libraries unloaded. Asked for a monatomic cation, the estimator saturates the
ion into a **neutral-valence group descriptor** and returns a number:

```
el      GAV(M+)      GAV(M)    GAV rise        IE1        error  what M+ was matched to
H           0.0       205.0      -205.0     1312.0      -1517.1
Li        -85.0       120.0      -205.0      520.2       -725.2  group(Li)
N         386.1       624.1      -237.9     1402.3      -1640.3  group(N3s-CsCsCs) + radical(NJ2_C)
O         570.3       249.1      +321.2     1313.9       -992.7  group(O2s-CsCs) + radical(CJ3)
Si        613.7       869.9      -256.2      786.5      -1042.7  group(CsJ2_singlet-CsH) + radical(Cs_P)
He  DatabaseError DatabaseError          --     2372.3          n/a
Ne  DatabaseError DatabaseError          --     2080.7          n/a
Ar  DatabaseError DatabaseError          --     1520.6          n/a
```

`N⁺` is matched to `group(N3s-CsCsCs)` — a **trisubstituted amine nitrogen**. `O⁺` to
`group(O2s-CsCs)`, an ether oxygen. **[M]** And the polyatomic control:

```
GAV(CH3+) =       2.1 kJ/mol  via group(Cs-CsCsCsCs)
GAV(CH3)  =     145.6 kJ/mol  via group(Cs-HHHH) + radical(CH3)
rise      =    -143.5 kJ/mol   IE(CH3) = 949.2 kJ/mol   error = -1092.8 kJ/mol, sign wrong
```

The methyl cation is estimated as a **neopentane-like carbon**, 143.5 kJ/mol *below* the methyl
radical, where the ionisation energy of CH₃ (9.8380 eV, NIST WebBook evaluated value **[L]**)
requires it to be 949.2 kJ/mol above. **In five of the six cases the estimator gets the sign of
ionisation wrong.** Only `O⁺` has the right sign, and it is still 993 kJ/mol low.

> **[I] A cation that reaches group additivity in this database gets a number, silently, that is
> wrong by roughly an ionisation energy.** The three noble gases are the only place it fails
> loudly, and only because no thermo group covers them. Basis: the eight measurements above,
> against ionisation energies from an independent database. Pinned by
> `test_group_additivity_answers_for_monatomic_cations_and_the_answer_is_wrong` and
> `test_the_other_noble_gas_cations_are_still_refused`.

**Not fixed here.** Making the estimator refuse charged species is an RMG-database groups change
with reach far beyond argon, and it is nobody's non-goal to *do* — but it is not this ticket's.
Recorded as the highest-value follow-on in §8.

### 2.5 The defect in the shipped `[Lip]` entry, recorded not corrected

The dispatch says to establish the convention from existing charged species. The obvious
instrument is the one gas-phase-style cation/neutral pair of the same element, and it fails.

**[M]** `probe1`:

```
H(298,[Lip]) - H(298,[Li]) =  375.3635 kJ/mol      E0 route: 375.3630
IE(Li), NIST ASD           =  520.2214 kJ/mol      (5.391714996 eV)
DISCREPANCY                = -144.8579 kJ/mol      = -1.5013 eV
ratio |discrepancy| / convention gap = 23.4x
```

**[I] A 145 kJ/mol gap cannot be a convention choice**: the entire difference between the two
conventions is 6.197 kJ/mol, and this is 23.4× that. So `[Lip]` cannot be used to read the
convention off, and it is a defect on its own terms. Basis: the two conventions' definitional
difference (§3.1) against the measured gap.

**[M] And the entropy of the same pair is exactly right**, which is what makes the enthalpy a
defect rather than a different reference state: `S(298,[Li]) − S(298,[Lip]) = 5.7632 J/(mol·K)`,
which is `R ln 2` to 0.002 — the electronic degeneracy of Li(²S) against Li⁺(¹S), handled
correctly. Only the enthalpy is wrong.

**Not fixed.** Modifying existing thermochemistry is an explicit non-goal. Pinned as-is by
`test_the_shipped_lithium_cation_disagrees_with_lithiums_ionisation_energy`, which fails if it is
ever corrected and points whoever did it here. **[I]** The cause was not diagnosed; the entry is
an ARC calculation at `ccsd(t)-f12/cc-pvdz-f12` and a 1.5 eV error in lithium's ionisation energy
at that level is not a basis-set artefact, so something upstream of the number is wrong. Basis:
the level of theory recorded in `LithiumPrimaryThermo`'s own header **[D]** against the size of
the discrepancy. **This matters beyond lithium**: `[Lip]` is the cation in the only working
plasma charge network this campaign has, so every equilibrium that network computes is off by
145 kJ/mol.

### 2.6 A representability caveat that belongs on the record

**[M]** `probe5`: argon's atom type declares **no charge constraint at all**.

```
Ar+  -> atomtype Ar   declared charges NONE (unconstrained)   from  1 Ar u1 p3 c+1
```

So `1 Ar u4 p0 c+4` parses just as readily as the ground state. **[I] Argon's cation is
representable by permissiveness rather than by design** — which is also the mechanism behind
I-120's SMILES defect, where `[Ar+]` reads back as Ar²⁺ with nothing to object. The consequence
for this entry: it matches the ground-state adjacency list and *only* that, so a mechanism that
constructs `Ar⁺` some other way will miss it rather than mismatch it. Basis: the atom type's
empty `charge` list and the isomorphism check in
`test_argon_is_representable_only_because_its_atom_type_is_unconstrained`.

A first version of `probe5` asked "does *any* `(u, p)` split with this charge parse?" and
answered YES for Ar⁴⁺, Ne⁴⁺ and Si⁴⁺. That is a finding about the question, not about argon, and
it is why every representability number above uses one deterministic ground-state rule
(`s²pⁿ` filling under Hund's rule) and nothing else.

---

## 3. The ion reference-state convention — *Verifier item 2*

**Determined, not assumed: this database and this runtime use the ION convention — the electron
priced at `H = S = Cp = 0` at every temperature.** Two independent pieces of evidence, one in the
data and one in the code.

### 3.1 First, the naming, because it is inverted in the dispatch

**[L]** John E. Bartmess, "Thermodynamics of the Electron and the Proton", *J. Phys. Chem.* **98**
(1994) 6420–6424, doi:10.1021/j100076a029. Definitions on p. 6420 col. 2 – p. 6421 col. 1,
quoted from the paper:

- **"electron convention" (EC)** — *"used in compilations such as the JANAF Tables and the
  NIST…"*; `ΔfH(e⁻) = 0` at all T and the electron is *"taken as just another chemical species"*,
  `H_T − H_0 = 5/2 R T` = 6.197 kJ/mol at 298.15 K, `S°(298.15) = 20.979 J/(mol·K)`.
- **"ion convention" (IC)** — *"used in the 'Gaseous Ion Energetics' compilation and the GIANT
  Tables, as well as in most papers published on the subject of gas-phase ion thermochemistry.
  This similarly sets ΔfH(e⁻) as equal to zero at all temperatures, but H_T − H_0 is also defined
  as equal to zero at all temperatures"*, with `S_T = 0` too.

> **The dispatch's labels are the other way round.** It reads *"whether the electron is treated as
> having zero enthalpy at all temperatures (the 'electron convention') or is given its own thermal
> enthalpy (the 'ion convention')"*. Under Bartmess the zero-enthalpy one is the **ion**
> convention and the thermal one is the **electron** convention. The physics in the dispatch is
> exactly right and the 6.2 kJ/mol figure is exactly right; only the two names are swapped. This
> is worth a sentence rather than a shrug, because a reader who applies the dispatch's dictionary
> to a JANAF number moves it 6.197 kJ/mol in the wrong direction — a 12.4 kJ/mol error, invisible
> to every test in this repository. Everything below names both and defines by physics.

### 3.2 The determination, from the data

**[M]** `probe1` swept all 78 thermo libraries and 25 218 molecule-carrying entries. Nine
net-charged entries exist, five distinct species:

```
library                            label              q nat  adjlist
electrocatLiThermo                 electron          -1   1  1 e u0 p0 c-1
electrocatLiThermo                 proton            +1   1  1 H u0 p0 c+1
electrocatLiThermo                 H3O               +1   4  ... 4 H u0 p0 c+1
LithiumPrimaryThermo               [Lip]             +1   1  1 Li u0 p0 c+1
electrocatThermo                   electron          -1   1  1 e u0 p0 c-1
electrocatThermo                   proton            +1   1  1 H u0 p0 c+1
electrocatThermo                   H3O               +1   4  ... 4 H u0 p0 c+1
computationalLithiumElectrode      electron          -1   1  1 e u0 p0 c-1
computationalLithiumElectrode      Li_ion            +1   1  1 Li u0 p0 c+1
```

**[D]** **All three `electron` entries are NASA polynomials with every coefficient identically
zero**, so `H = S = Cp = 0` at every temperature in their declared 298–3000 K span. That is the
IC electron exactly. Pinned by
`test_every_electron_entry_in_this_database_prices_the_electron_at_zero`.

**[D]** The other charged entries fix no gas-phase convention at all: `proton` has
`H298 = 0` with the comment *"1/2 free energy of H2(g)"* — a computational hydrogen electrode —
and `Li_ion` has `H298 = 0` with *"Li+ + e- = Li(s) @ -3.04 V vs SHE"*. Both are electrochemical
reference species. And `[Lip]`, the only gas-phase-style one, is 145 kJ/mol off any convention
(§2.5).

### 3.3 The determination, from the code

**[R]** `rmgpy/reaction.py:822-844`, `_get_free_energy_of_charge_transfer_reaction` sums free
energies over the explicit reactant and product lists and then

```python
if potential != 0.:
    dGrxn -=  self.electrons * constants.F * potential
```

Every reactor calls it at `potential = 0`. **[M]** So the electron contributes exactly zero, and
`dG` for `Ar → Ar⁺` is bit-identical whether the electron is carried as `Reaction.electrons`
metadata or as an explicit species with the shipped zero thermo:

```
dG(298.15) electron implicit = 1517.0987 kJ/mol
dG(298.15) electron explicit = 1517.0987 kJ/mol   difference 0.000e+00
```

Pinned by `test_the_runtime_adds_no_electron_term_to_a_charge_transfer_free_energy`.

**[R]** And the runtime is explicit that this is a limitation rather than a model:
`Reaction.get_reverse_from_equilibrium_refusal` refuses to build a reverse rate from such a `Keq`
because *"get_equilibrium_constant sums free energies over the explicit species and omits the
electron entirely"* (`rmgpy/reaction.py:619-622`).

> **Conclusion: the value entered for any cation here must be the IC value.** It is also the
> *composable* choice, which is the argument that settles it independently of the convention
> question: if an explicit electron with real thermal functions is ever added, `1520.581 +
> H_e(T)` reproduces JANAF exactly, whereas an EC value would double-count the electron. §4.2.

---

## 4. `Ar⁺`: the sourced values — *Verifier item 3*

### 4.1 The source

**[L]** M. W. Chase, Jr., **NIST-JANAF Thermochemical Tables, Fourth Edition**, *J. Phys. Chem.
Ref. Data* Monograph 9 (1998), pp. 1–1951; table **"Argon, Ion (Ar⁺)"**, species designation
`Ar1+(g)`, table identifier **Ar-002**. Revision: CURRENT March 1982 (1 bar), PREVIOUS March 1977
(1 atm). `Tr = 298.15 K`, `p° = 0.1 MPa`. Retrieved as `https://janaf.nist.gov/tables/Ar-002.txt`.

**[M]** The rows transcribed, verbatim:

| T / K | Cp° | S° | H−H°(Tr) | ΔfH° (EC) | ΔfG° (EC) |
|---|---|---|---|---|---|
| 0 | 0 | 0 | −6.206 | **1520.573** | — |
| **298.15** | **20.984** | **166.404** | 0 | **1526.778** | 1517.077 |
| 300 | 20.990 | 166.533 | 0.039 | 1526.817 | 1517.017 |
| 400 | 21.422 | 172.627 | 2.158 | 1528.936 | 1513.432 |
| 500 | 21.915 | 177.461 | 4.325 | 1531.104 | 1509.306 |
| 600 | 22.318 | 181.494 | 6.538 | 1533.316 | 1504.740 |
| 800 | 22.734 | 187.983 | 11.051 | 1537.830 | 1494.536 |
| 1000 | 22.773 | 193.065 | 15.606 | 1542.385 | 1483.186 |
| 1500 | 22.350 | 202.228 | 26.898 | 1553.677 | 1451.134 |
| 2000 | 21.919 | 208.596 | 37.960 | 1564.739 | 1415.279 |
| 3000 | 21.415 | 217.375 | 59.595 | 1586.374 | 1335.847 |
| 4000 | 21.176 | 223.499 | 80.877 | 1607.656 | 1249.124 |
| 5000 | 21.050 | 228.210 | 101.984 | 1628.763 | 1157.046 |
| 6000 | 20.975 | 232.040 | 122.994 | 1649.772 | 1060.728 |

Cp° and S° in J/(mol·K); enthalpies in kJ/mol.

**VALIDITY RANGE, and it is a hard stop: 0–6000 K, and the table ends there.** `Tmin`/`Tmax` on
the entry are 298.15 and 6000 K — 298.15 rather than 0 because the `Cpdata` grid starts at the
reference temperature. Nothing here may be used above 6000 K, and nothing here was extrapolated.
**[I]** This is a *gas* temperature range and says nothing about the electron temperature, which
the Voronov rate law carries separately with its own 1 eV–20 keV range **[D]**. Basis: `Tgas` and
`Te` are independent state variables in `PlasmaReactor` **[R]**.

### 4.2 The convention reconciliation — the only arithmetic applied to any sourced number

JANAF is EC (proved in §4.3). This database is IC (§3). So:

```
route 1   1526.778 - 6.197                 = 1520.5806 kJ/mol
route 2   1520.573 + 6.206 - 6.197         = 1520.5820 kJ/mol
entered                                    = 1520.5810 kJ/mol
```

Route 1 subtracts the electron's `5/2 R T(298.15) = 6.1974 kJ/mol`. Route 2 rebuilds the same
number from the 0 K row, where the conventions coincide because the electron's integrated heat
capacity is zero at 0 K, adding Ar⁺'s own enthalpy increment and removing neutral argon's. **The
two routes close to 0.0014 kJ/mol**, which is what makes this a transcription rather than a
choice. `E0 = 1520.573` is the 0 K value taken verbatim; it needs no conversion for the same
reason. `Cpdata` and `S298` are transcribed unconverted — the convention touches only the
electron's own thermal functions, not the ion's.

Pinned by `test_the_entered_enthalpy_is_the_ion_convention_value_by_two_routes`, which also
asserts the entered value is **not** the EC value.

### 4.3 That the source is EC, established from its numbers rather than its wording

**[M]** The discriminator has to be the enthalpy, and it is decisive:

```
JANAF dfH(298.15) - dfH(0) = 1526.778 - 1520.573 = 6.205 kJ/mol
electron's 5/2 R T(298.15)                       = 6.197
Ar+'s own increment over a bare monatomic gas    = 6.206 - 6.197 = 0.009
EC predicts 6.197 + 0.009 = 6.206;  IC predicts 0.009 alone
```

6.205 against 0.009 is not a close call. Pinned by
`test_the_source_table_is_electron_convention_by_its_own_arithmetic`.

**[M] The free energy is NOT a discriminator, and that is worth knowing.** Bartmess (p. 6421)
records Sharpe and Richardson's observation that at **297 K** the electron's `T·S` happens to
equal its `H − H₀`, so the two conventions give the same `ΔG` for an ionisation **[L]**. Measured
here: the EC route reproduces JANAF's `ΔfG°(298.15) = 1517.077` to 0.002 kJ/mol *with* the
electron at `S = 20.979`, and the IC route — this entry, electron omitted — lands 0.058 kJ/mol
away. Anyone using `ΔfG` to tell the conventions apart at room temperature will conclude they
are identical. Pinned by `test_the_two_conventions_free_energies_coincide_near_room_temperature`.

**The payoff of choosing IC, measured. [M]** RMG's `dG` for `Ar => Ar⁺` against JANAF's own
`ΔfG°(T)` column, which is the physically correct free energy of ionisation:

| T / K | RMG `dG` | JANAF `ΔfG°` | difference |
|---|---|---|---|
| 300 | 1517.077 | 1517.017 | **+0.060** |
| 500 | 1514.715 | 1509.306 | +5.409 |
| 1000 | 1508.419 | 1483.186 | +25.233 |
| 2000 | 1482.625 | 1415.279 | +67.346 |
| 6000 | 1262.739 | 1060.728 | +202.011 |

**[I]** At room temperature the entered value gives an essentially exact free energy of
ionisation. The growing residue above it is the electron's own omitted free energy — the
electron's entropy is what RMG cannot carry — plus a smaller contribution from the neutral-argon
library's NASA fit drifting from JANAF. **That residue belongs to the electron's zero
thermochemistry, not to this entry**: entering the EC value instead would make every row worse by
a further 6.197 kJ/mol. Basis: the two conventions' definitions against the measured column, and
the fact that RMG's own `S(Ar⁺)` and `H−H298(Ar⁺)` reproduce the JANAF columns to
0.03 J/(mol·K) and 0.04 kJ/mol across the whole range (§4.4), so the deviation cannot be in the
cation. It is also exactly why the runtime refuses to reverse these reactions (§3.3).

### 4.4 Corroboration — five checks, all closing

**[M]**

1. **`S°(298.15) = 166.404`** matches the **166.40 J/(mol·K)** the NIST Chemistry WebBook species
   page for the argon cation (CAS 14791-69-6) reports from the same Chase (1998) review **[L]** —
   a different NIST renderer over the same table, so this checks the retrieval, not the physics.
2. **`ΔfH°(0) = 1520.573`** against argon's first ionisation energy, **15.7596119 ± 0.0000005 eV
   = 1520.5714 kJ/mol** (Kramida, Ralchenko, Reader & NIST ASD Team, **NIST Atomic Spectra
   Database ver. 5.12**, doi:10.18434/T4W30F, accessed 2026-08-26) **[L]**. Agreement
   **0.0016 kJ/mol**, from a completely independent database.
3. **The EC/IC identification** above, `6.205 = 6.197 + 0.009`.
4. **`ΔfG°(298.15)`** reproduced to 0.001 kJ/mol from `ΔfH°`, `S°(Ar⁺)`, `S°(e⁻) = 20.979` and
   `S°(Ar) = 154.845` — which also confirms the table carries the electron as a product.
5. **`S°(298.15)`**: `S°(Ar) + R ln 4 = 154.845 + 11.526 = 166.371`, plus the 0.033 J/(mol·K)
   electronic contribution of the ²P₁ᐟ₂ level = **166.404**.

**[M] And the transcription checked across the whole range, not just at 298.15 K** — the loaded
entry against JANAF's own columns:

| T / K | RMG `S°` | JANAF `S°` | RMG `H−H298` | JANAF `H−H298` |
|---|---|---|---|---|
| 300 | 166.544 | 166.533 | 0.039 | 0.039 |
| 500 | 177.475 | 177.461 | 4.326 | 4.325 |
| 1000 | 193.061 | 193.065 | 15.594 | 15.606 |
| 2000 | 208.585 | 208.596 | 37.942 | 37.960 |
| 6000 | 232.048 | 232.040 | 123.030 | 122.994 |

Pinned by `test_the_entry_reproduces_the_janaf_columns_across_the_whole_range`.

### 4.5 The physics the table encodes, so the non-constant Cp is not mistaken for noise

**[L]** Ar⁺ is ²P, with a ²P₃ᐟ₂ ground level and a ²P₁ᐟ₂ level 1431.6 cm⁻¹ (2060 K) above it.
**[I]** That single fact explains three things in the numbers at once, which is a further check on
them: `Cp°` rises from 20.984 J/(mol·K) at 298.15 K to a maximum of 22.773 near 1000 K — 9.6 %
above `5/2 R` — and relaxes back to 20.975 at 6000 K; `S°(298.15)` exceeds neutral argon's by
`R ln 4` plus 0.033; and `H(298)−H(0)` is 6.206 rather than 6.197. **A monatomic-cation entry
written with a flat `Cp = 5/2 R` would be wrong by up to 10 % over 600–2000 K.** Basis: a
two-level Schottky term at that splitting. Pinned by
`test_the_heat_capacity_is_not_five_halves_R_and_that_is_the_physics`.

### 4.6 Uncertainty

**[L]+[I]** `ΔfH°` rests on argon's ionisation energy, which is spectroscopic and known to eight
figures — this is the rare thermochemical value whose enthalpy carries essentially no
uncertainty. `S°` and `Cp°` come from the electronic partition function over known NIST ASD
levels plus Sackur–Tetrode translation, so their uncertainty is also negligible on any scale a
mechanism cares about. **The real uncertainty in using this entry is not in the numbers, it is in
the electron's representation** (§4.3): the free energy of ionisation RMG computes from it is
exact at 300 K and 25 kJ/mol high at 1000 K, and no better value for Ar⁺ would improve that.
Basis: the source's own provenance against the measured `ΔfG` column.

---

## 5. The whole path, stage by stage — *Verifier items 5 and 6*

**[M]** `probe3`, all stages, and every one of them separately.

### 5.1 It loads

```
[PASS] every thermo library still loads -- 78 libraries
[PASS] PlasmaCationThermo is among them
    entries: ['[Arp]']
    model      : ThermoData
    H298       : 1520.5810 kJ/mol
    S298       : 166.4040 J/(mol*K)
    E0         : 1520.5730 kJ/mol
    Tmin/Tmax  : 298.15 / 6000.0 K
    Cp(298.15) : 20.9840 J/(mol*K)
    Cp(1000)   : 22.7730 J/(mol*K)
```

### 5.2 The species resolves — and did not before

```
[PASS] resolution reached the new library -- Thermo library: PlasmaCationThermo
    H298    : 1520.5841 kJ/mol      S298 : 166.4146 J/(mol*K)
    without the library: DatabaseError: Unable to determine thermo parameters for
    atom {'*': <Atom 'Ar+'>} in molecule <Molecule "[ArH+]">
[PASS] WITHOUT the library Ar+ is refused
```

The before/after is measured, not remembered: the same database with `PlasmaCationThermo`
unloaded refuses, and the failure route is visible — HBI saturates `Ar⁺` into `[ArH+]` looking
for a group. **[M]** `get_thermo_data` round-trips a `ThermoData` through Wilhoit, which moves
`H298` by ~3 J/mol for every species it returns, the new entry included; the 1520.5841 above is
that artefact, not a data difference.

### 5.3 An equilibrium constant computes and is finite

```
T=  300.0 K   dGrxn=  1517.0771 kJ/mol   Kc=7.22552e-265   finite=True
T=  500.0 K   dGrxn=  1514.7153 kJ/mol   Kc=5.78171e-159   finite=True
T= 1000.0 K   dGrxn=  1508.4187 kJ/mol   Kc= 1.62151e-79   finite=True
T= 2000.0 K   dGrxn=  1482.6249 kJ/mol   Kc= 1.89938e-39   finite=True
T= 6000.0 K   dGrxn=  1262.7388 kJ/mol   Kc= 1.01650e-11   finite=True
```

**And what that green does not mean.** The same runtime refuses to build a reverse rate from it:

```
reverse-from-Keq refusal: it transfers charge (electrons=1) carried only as reaction
metadata, so get_equilibrium_constant sums free energies over the explicit species and
omits the electron entirely, and its kinetics None declares no electrode-potential
reference that would supply one
```

Pinned by `test_the_runtime_refuses_to_reverse_that_equilibrium`, so nobody reads "the
equilibrium constant computes" as licence to reverse an ionisation.

### 5.4 The plasma reactor accepts it

```
[PASS] the plasma reactor accepted the argon reaction
    reactor.kf   = 1.085417e+07
    Voronov k(Te=23209.0 K) = 1.085417e+07
    electron_index = 2
```

`Te = 23209 K` is 2 eV, inside the shipped Voronov argon fit's stated 1 eV–20 keV range **[D]**.
The reactor's `kf` is the Voronov argon rate to 1 part in 10⁹, so the reaction is being evaluated
at its own rate law and not at a fallback.

### 5.5 The previously-uncarryable argon ionisation reaction — *Verifier item 6*

**It is carried.** **[M]**

```
scratch library reactions: ['[Li] => [Lip]', '[Ar] => [Arp]']
[Ar] => [Arp]   electrons=1  kinetics=VoronovEIArrhenius  family=PlasmaElectronImpactIonization
[PASS] it declares a net electron gain
[PASS] it balances
[PASS] its owner is a placement-registry key -- PlasmaElectronImpactIonization -> (1, 2)
    resolved view: [Ar] + e- => [Arp] + e- + e-   electrons (reactants, products) = (1, 2)
[PASS] it resolves to Ar + e- => Ar+ + 2 e-
```

**It was carried in a scratch library outside every tracked tree, and that is deliberate.**
Adding a rate to this database is an explicit non-goal, and the argon ionisation entry belongs to
whoever owns `PlasmaElectronImpactIonization`. What this demonstrates is that the *reason* that
library gives for carrying one entry is gone. **[D]** Its own header:

> *"Of those 7, exactly one has thermochemistry for the product cation in this database as a free
> monatomic ion: Li+ … Adding He+, N+, O+, Si+ or Ar+ needs monatomic-cation thermochemistry that
> does not exist yet; that is a thermo ticket, and until it lands those reactions could not be put
> into a model regardless of which owner was chosen."*

**[M]** That header's coverage arithmetic is independently reproduced by `probe5`: of the 13
elements `voronov.yaml` ionises at the neutral stage, RMG can construct both endpoints for
exactly **7 — H, He, Li, N, O, Si, Ar** — which is the same seven, from a different method.

**The next missing thing, named.** For argon there is now exactly one: a two-line entry
`[Ar] => [Arp]` with `VoronovEIArrhenius(Z=18, N=18)` in
`input/kinetics/libraries/PlasmaElectronImpactIonization/reactions.py`, plus its two
`dictionary.txt` species. Everything downstream of it is measured working above. **Owner: a
kinetics ticket.** For the other four constructible endpoints — He⁺, N⁺, O⁺, Si⁺ — the missing
thing is still thermochemistry, one sourced entry each, and §2.4 says why an estimate will not
do.

---

## 6. `Ar₂⁺` — *Verifier item 4: out of reach, and here is exactly where it stops*

**Not entered. The tabulated functions exist, are identified, and could not be reached from
here.**

**[L]** M. A. Maltsev, I. V. Morozov & E. L. Osina, **"Thermodynamic Properties of Ar₂⁺ and Ar₂
Argon Dimers"**, *High Temperature* **57** (1) (2019) 37–40, doi:10.1134/S0018151X19010176.
Rovibronic partition functions and thermodynamic functions — heat capacity, entropy, reduced
Gibbs energy — computed over **298.15–10 000 K** from interatomic interaction potentials, with
several interaction models compared; the results were added to the **IVTANTHERMO** database. Its
spectroscopic input traces to Signorell & Merkt, *J. Chem. Phys.* **109** (1998) 9762 and Rupper
& Merkt, *J. Chem. Phys.* **117** (2002) 4264.

**[M]** Where it stops:

| Route | Result |
|---|---|
| Springer `link.springer.com/article/10.1134/S0018151X19010176` | 303 redirect to an IdP authorisation endpoint; paywalled |
| OpenAlex `W2964635563` | `is_oa: false`, `oa_status: "closed"`, no best-OA location, no PDF, no repository full text |
| ATcT argon-dimer-cation species page (v1.124 and v1.130, species 2778) | **HTTP 403** |
| NIST WebBook, formula `Ar2` | the neutral dimer only, and it carries *no* gas-phase thermochemistry — only ion energetics and diatomic constants |
| NIST-JANAF | no Ar₂⁺ table; the argon tables are Ar-001 (neutral) and Ar-002 (Ar⁺) |
| IVTANTHERMO | not reachable from here |

**[I] Why "add nothing" and not "derive it".** `D₀(Ar₂⁺)` is well measured (≈1.2–1.3 eV) and
`ΔfH°(Ar₂⁺) = ΔfH°(Ar⁺) + ΔfH°(Ar) − D₀` is one line of arithmetic. That line is **authoring**
under this ticket's rules — it is a computation from a bond energy and an analogy to another
charge stage, both explicitly forbidden — and it would still leave `S°` and `Cp(T)` unsourced,
which cannot be had at all without the vibrational and electronic structure the Maltsev paper
integrates. A `ThermoData` entry needs all three. So: nothing entered. Basis: the entry shape
`ThermoData` requires against what the reachable sources supply.

**What would unblock it:** the Maltsev *High Temperature* 57 (2019) 37–40 tables, via a library
request or an institutional Springer subscription. With them the entry is a transcription, the
same shape as §4. Pinned by `test_no_argon_dimer_cation_was_entered`, which fails if a
multi-argon entry ever appears without this section being updated.

**[I] And what it would be worth.** I-120 measured Ar₂⁺ dissociative recombination at ~2.9 × 10⁵
times faster than Ar⁺ radiative recombination at Te = 1 eV, making it the argon electron sink
that matters. So Ar₂⁺ thermochemistry is the *second* thing that channel needs. The first is an
RMG-Py change — `TwoTemperaturePlasma` gaining an `electrons` field — without which a power-law
rate for it cannot be stored at all. Basis: `docs/i120-argon-recombination.md` §3 and §4.1,
consumed read-only.

---

## 7. Negative control, the diff, and the suites — *Verifier items 7 and 8*

### 7.1 Negative control

**[M]** The two lithium suites, whole, against the pinned runtime:

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-i123-integration python -m pytest \
      test/test_plasma_radiative_recombination.py \
      test/test_plasma_electron_impact_ionization.py -q
66 passed in 1.37s
```

66, the same count `docs/i120-argon-recombination.md` §7.3 recorded.

**[M]** Both lithium species and neutral argon re-derived inside this ticket's own module, at the
values recorded before it, so a silent edit surfaces here too:

```
Li   H298=   157.5723 S298= 138.6620  <- Thermo library: LithiumPrimaryThermo
Li+  H298=   532.9358 S298= 132.8988  <- Thermo library: LithiumPrimaryThermo
Ar   H298=     0.0031 S298= 154.7348  <- Thermo library: BurkeH2O2
```

Neutral argon still resolves to `BurkeH2O2`, not to the new library, and its `H298` is zero to
3.1 J/mol — the Wilhoit round-trip artefact §5.2 describes, present identically before this
branch.

**[M]** The full database suite, with and without the new library file, measured by moving it out
and back rather than by memory:

```
base (library moved aside) :  4 failed, 125 passed
this branch                :  4 failed, 173 passed        (125 + 48 new, same 4 failures)
```

**The four failures are inherited and not diagnosed.** All four are in
`test/test_plasma_electron_attachment.py`, all four concern whether a trained rate resolves
through `'rate rules'` or through the training depository, and `docs/i119-recombination-loss.md`
§11 and `docs/i120-argon-recombination.md` §7.4 both record them red on earlier base commits
against three different runtimes. This branch modifies no tracked file that suite reads. Out of
scope per the non-goals.

### 7.2 The diff — *Verifier item 8*

**[M]** `git status --porcelain` before committing, in the only worktree this ticket wrote to:

```
?? input/thermo/libraries/PlasmaCationThermo.py
?? test/test_argon_cation_thermo.py
```

Three files, all new, all additive (`docs/i127-argon-cation-thermo.md` is this report; it and the
two above are the commit). `docs/contracts/` is gitignored working scratch.

**No `voronov.yaml`, no `badnell.yaml`, no kinetics library, no family, no group, no tree node, no
training entry, no `rules.py`, no `dictionary.txt`, and no existing thermo file was modified.**
The lithium libraries and both plasma kinetics libraries were read and not touched.
`Cation_R_Recombination`, the quarantined battery-SEI family, was not opened.
`Reaction.is_balanced` and `rmgpy/electron_balance.py` are untouched — this branch cannot touch
them, they are in the other repository, and that repository has no diff.

**[M]** In the runtime worktree `/home/alon/Code/RMG-Py-i123-integration`, `git diff` is empty and
`git status --porcelain` shows the two untracked YAML files that predate this session. **One
branch, one commit, no RMG-Py change.**

---

## 8. Durable findings

Eight, in descending order of consequence.

1. **Group additivity does not refuse a charged species — it saturates the ion into a
   neutral-valence group descriptor and returns a number that is wrong by roughly an ionisation
   energy, with the sign of ionisation wrong in five of six measured cases.** `CH₃⁺` is estimated
   143.5 kJ/mol *below* `CH₃`, where `IE(CH₃)` requires 949.2 kJ/mol above. This is the most
   consequential thing in this ticket: it means every charged species this database can generate
   either has a hand-written library entry or has a silently wrong number, and it is not
   argon-specific. **Highest-value follow-on: make the thermo estimator refuse net charge rather
   than answer.** Owner: RMG-database groups, or an RMG-Py guard. §2.4.
2. **The thermochemistry gap is a generation consequence, not a law and not a list** — two gates
   in series, both owned outside this repository's thermo tree. Gate 1 is whether
   `rmgpy/molecule/atomtype.py` admits the element at that charge (three-way split, §2.3); gate 2
   is whether an application project wrote a library entry, since no estimator covers charge.
   Two clean sub-laws survive: coverage is identically zero for `Z > 20` (144 of 342 stages, and
   no rate-table addition changes it without RMG-Py), and identically zero for every `q ≥ 2`. §2.
3. **The database's ion reference-state convention is the ION convention** — electron at
   `H = S = Cp = 0` at all T — determined from three identically-zero `electron` entries and from
   `_get_free_energy_of_charge_transfer_reaction` adding no term at `potential = 0`. Not
   assumed, and not readable from any cation in the database. §3.
4. **The dispatch's names for the two conventions are swapped relative to Bartmess (1994)**, the
   standard reference. The physics and the 6.2 kJ/mol are right; the labels are inverted, and a
   reader who follows them moves a JANAF number the wrong way by 6.197 kJ/mol. §3.1.
5. **`Ar⁺` thermochemistry is entered, sourced, and corroborated five ways** — NIST-JANAF Ar-002,
   `ΔfH°(298.15) = 1520.581 kJ/mol` (ion convention, converted from JANAF's 1526.778 by two
   routes closing to 0.0014), `S° = 166.404`, `Cp°` on a 13-point grid reproducing the JANAF
   columns to 0.03 J/(mol·K) and 0.04 kJ/mol from 300 to 6000 K. Valid 298.15–6000 K. §4.
6. **The shipped `[Lip]` entry disagrees with lithium's ionisation energy by 144.86 kJ/mol** —
   23× the entire convention gap, so not a convention choice — while its *entropy* is exactly
   right (`R ln 2` below neutral lithium). `[Lip]` is the cation in the only working plasma charge
   network this campaign has, so every equilibrium that network computes carries this error.
   Recorded, pinned, not fixed. §2.5.
7. **The argon ionisation reaction is now carryable end to end**, and the only thing left for it
   is one entry in `PlasmaElectronImpactIonization` — whose own header named this thermo ticket as
   its blocker, and whose 7-element coverage arithmetic this ticket independently reproduced. §5.5.
8. **`Ar₂⁺` has published tabulated thermodynamic functions and they are unreachable from here**
   — Maltsev, Morozov & Osina, *High Temperature* **57** (2019) 37–40, 298.15–10 000 K,
   IVTANTHERMO; Springer paywalled, ATcT 403. Deriving it from `D₀` would be authoring and would
   still leave `S°` and `Cp(T)` unsourced. It is also the *second* blocker on the argon channel
   that actually dominates; the first is an RMG-Py change I-120 already identified. §6.

Also worth keeping: **argon's cation is representable only because argon's atom type declares no
charge constraint**, so `Ar⁴⁺` parses as readily as `Ar⁺` and nothing objects — the same
permissiveness behind I-120's `[Ar+]` → Ar²⁺ SMILES defect, re-pinned here. §2.6.

---

## 9. What this ticket could not reach — *Verifier item 9*

- **The Maltsev *High Temperature* 57 (2019) tables for `Ar₂⁺`**, which is the whole reason
  nothing was entered for it. Springer paywalled, no OA copy, ATcT 403. §6.
- **ATcT at all.** Every `atct.anl.gov` species page returns HTTP 403 from here, so the one
  independent modern compilation that could corroborate `ΔfH°(Ar⁺)` was unavailable. The
  corroboration in §4.4 is therefore NIST-internal plus NIST ASD, not a second compilation.
- **The JANAF Ar-002 table's own uncertainty statement.** The `.txt` download carries data
  columns and no uncertainty column, and the Monograph 9 front matter was not retrieved. §4.6's
  uncertainty discussion is an inference from the source's provenance, not a quoted figure.
- **A directly published ion-convention value for `Ar⁺`.** Lias *et al.*, "Gas-Phase Ion and
  Neutral Thermochemistry" would carry one and would remove the need for the §4.2 conversion
  entirely; its `Ar⁺` row was not retrieved. The conversion is documented and self-checking, but
  it is a conversion.
- **The cause of the `[Lip]` 145 kJ/mol discrepancy.** Measured and pinned; not diagnosed. §2.5.
- **He⁺, N⁺, O⁺ and Si⁺ were counted, not sourced.** They are constructible, they have no
  thermochemistry, and no literature search was run for any of them. **[I]** All four are in
  NIST-JANAF as monatomic ions, so the outlook is good and the work is transcription — but that
  is an expectation, not a retrieval.
- **The 11 elements that cannot be built at all** (Be, B, C, F, Na, Mg, Al, P, Cl, K, Ca) were
  characterised by the exception they raise, not by what an atom type for them would have to look
  like. That design question was not opened.
- **No RMG model was run.** No `rmg.py` job, no enlargement, no integration. Every claim here is
  arithmetic on shipped objects, a loader result, or a `PlasmaReactor.initialize_model` call — not
  an integrated trajectory. In particular, the argon ionisation reaction has been shown *carried*,
  not shown to *produce Ar⁺ in a converged model*.
- **The estimator's behaviour on charged *polyatomics* was probed with one species** (`CH₃⁺`).
  The finding generalises by mechanism, not by measurement.
- **Whether making the estimator refuse charge breaks existing mechanisms.** Finding 1 recommends
  it; the blast radius across the zwitterion-carrying libraries was not measured.
- **The four inherited attachment failures were confirmed inherited, not diagnosed.**
