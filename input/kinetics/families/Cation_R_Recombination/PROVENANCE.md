# `Cation_R_Recombination` — what this family is, and what it is not

```
LEGACY SEI ELECTROCHEMISTRY — INCOMPLETE QUANTITATIVE PROVENANCE
```

**Read this before using, citing, refitting, or copying anything in this directory.**

This is a **legacy lithium-ion-battery SEI family**: Marcus-type electron transfer at a lithium
metal electrode, in a liquid carbonate electrolyte, at room temperature, under declared electrode
potentials. It is **not** a plasma family. The name, the `Li+` root group, the `electrons = -1`
declaration and the `LOSE_CHARGE` recipe describe *electrode* electron-transfer bookkeeping; none of
them is evidence of free-electron plasma chemistry.

The label above is deliberate and is **not** "validated". The physical domain has been recovered;
the numbers have not been made reproducible. §5 names the four facts that are still missing, and
they are missing for SEI use too, not only for anyone who wanders in from a plasma model.

---

## 1. The prohibition, stated first

**These rates must not be used in a plasma mechanism.** Specifically, this family must not be
treated as, or substituted for:

- gas-phase electron–ion recombination;
- lithium-plasma recombination;
- a cation source or a cation loss route for an alkali-plasma model;
- kinetics transferable to a two-temperature plasma reactor merely because the reactions carry
  electron metadata.

Evaluated outside the electrochemical domain — no electrode, no reference potential, no applied
bias — the twelve entries return **1e−23 to 1e−226 m³/(mol·s)**, thirty to two hundred and thirty
orders of magnitude below anything physical. The rate law evaluates correctly; what has been lost is
the *semantics of the source model*. The number is not wrong by a factor. It is not the quantity the
data means.

The genuinely available lithium-plasma kinetics are elsewhere in this database and are untouched by
any of this: electron-impact ionisation in `input/kinetics/voronov.yaml` (Z = 3, N = 3/2/1) and
radiative recombination in `input/kinetics/badnell.yaml` (Z = 3, N = 0/1/2). If you came here
looking for Li⁺ + e⁻, those are the files.

`quarantine.py` beside this file carries the machine-readable form of this prohibition:
`state = "QUARANTINED FOR QUANTITATIVE PLASMA USE"`, with `appliesToKineticsClass = "Marcus"` as
the criterion, so the affected set is computed from the data rather than listed.

## 2. The original physical domain, as recovered

The family's only identified consumers are two RMG example inputs in the reference runtime. They
are the surviving statement of the conditions these rates were written for.

| quantity | value | source |
|---|---|---|
| **Family classification** | lithium-ion battery solid-electrolyte-interphase (SEI) electrochemistry | recovered, §6 |
| **Surviving example input** | `examples/rmg/SEI_pure_EC/input.py` (in the RMG-Py runtime, not in this database) | — |
| **Reactor type** | `liquidSurfaceReactor`, surface/volume ratio 1.0e5 m⁻¹ | `SEI_pure_EC/input.py:234-248` |
| **Solvent** | ethylene carbonate — `solvation(solvent='ethylene carbonate')` | `…:250-252` |
| **Electrode** | lithium metal, (110) facet — `catalystProperties(metal='Li110')` | `…:62-64` |
| **Temperature** | 298.15 K | `…:235` |
| **Applied potentials** | `liqPotential = (-1.0,'V')`, `surfPotential = (0.0,'V')` | `…:236-237` |
| **Bulk species held constant** | Li⁺ at 15.0 mol/m³; ethylene carbonate at 15.17 mol/dm³ | `…:238-247` |
| **Family selection** | `kineticsFamilies = ['surface','electrochem', …]` — this family enters via the `electrochem` set | `…:7` |
| **Variant model** | `examples/rmg/SEI_pure_ACN/input.py` — same model in **acetonitrile**, `liqPotential = +0.3 V`, second reactor at 0.0 V | `SEI_pure_ACN/input.py:98-120,133-134` |

The solvent's own constants are in this database: ethylene carbonate, `eps = 95.3`, `n = 1.420`
(`input/solvation/libraries/solvent.py:8678`, added 2023-12-07 in `48709a5ec`). Those two numbers
are precisely and only the inputs an outer-sphere reorganisation term needs — and **every one of the
twelve entries carries `lmbd_o = 0`.**

### 2.1 The reference and sign information that was recovered

This is the part that decides whether the numbers mean anything, and it is only partly recovered.

**Two mutually incompatible Li⁺ references sit in this same database, 502 kJ/mol apart at 298 K.**

| reference | what it is | G(298 K) | G(1000 K) |
|---|---|---|---|
| `input/thermo/libraries/LithiumPrimaryThermo.py` entry 65 `[Lip]` | bare gas-phase monatomic Li⁺ (`E0 = 526.738 kJ/mol`, `Cp0 = CpInf = 5R/2`) | **+493.332 kJ/mol** | +389.471 kJ/mol |
| `input/thermo/libraries/computationalLithiumElectrode.py` entry 3 `Li_ion` | the computational-lithium-electrode convention: `Li⁺ + e⁻ ≡ Li(s)` at 0 V vs Li/Li⁺ (`H298 = 0`, `S298 = 29.12 J/(mol·K)`, Cp of Li(s)); its companion `electron` entry is an identically zero NASA polynomial | **−8.678 kJ/mol** | −42.854 kJ/mol |

`computationalLithiumElectrode.py` states its own sign convention in its header (lines 5–14):

```
This library uses the computational lithum electrode model where
Li+ + e- = Li(s) @ -3.04 V vs SHE
If using this library, the potential in your input file
will be referenced to the Li/Li+ electrode (not SHE)
For example, if you set your reactor potential to O V,
that would be -3.04 V vs SHEs
```

**Neither SEI example loads that library.** Both load `LithiumPrimaryThermo` — the gas-phase
reference — so which convention is in force is decided by an input file living in a *different*
repository, and nothing in this database flags the conflict.

**Do not resolve this by choosing.** Substituting the electrode reference recovers 34 to 214 orders
of magnitude, and **restores only two of the five training entries** (the two carbon-centred
radicals reach their own barrierless ceiling `A·T^n`; the three heteroatom-centred ones stay 6–17
orders below it). Picking a reference because it improves the numbers is calibration to expectation,
not recovery. Likewise: do not fit a potential offset, per-entry or global, and specifically not
4.44 V.

### 2.2 Where a reference potential *would* live — and why it does not

The structural finding, and the reason this is not a translation bug someone can repair:

- In ReactionMechanismSimulator.jl, the electrode-interface path adds
  `dGrxns .+= electronchanges .* (phi .- referencepotentials) .* F`, where
  `referencepotentials` is `hasproperty(reaction.kinetics, :V0) ? reaction.kinetics.V0 : 0.0`
  (`src/Interface.jl:97-107`).
- **`V0` is a field of `Arrheniusq`, not of `Marcus`** (`src/Calculators/Rate.jl:35` vs `:42-50`).
  So for a Marcus reaction the reference potential silently defaults to `0.0`, and ΔG is shifted by
  the **full absolute** `n_e·φ·F` with no reference subtracted.

> The electrochemical driving-force reference was not lost in translation into this database. **It
> was never representable in the `Marcus` type at all** — not in the Julia original, not in the
> RMG-Py port, not in the `.rms` serialisation between them.

The `ArrheniusChargeTransferBM` rule that the Marcus set *replaced* (§4) did carry `V0`, `alpha` and
`electrons`.

## 3. The original rate law, in its original Julia

Marcus kinetics entered ReactionMechanismSimulator.jl in `f1c175b58`, *"add Marcus kinetics type and
allow dGrxn dependence of kinetics"*, **Matt Johnson, 2024-02-03** — five weeks before the training
entries in this directory landed. The source tree is reachable from this repository's remote on
branch `official/fix/py311_ci` (tip `cf83540e3`), `src/Calculators/Rate.jl:42-58`:

```julia
@with_kw struct Marcus{N<:Number,K<:Number,Q,B,P<:AbstractRateUncertainty} <: AbstractRate
    A::N ; n::K ; lmbd_i_coefs::Q ; lmbd_o::K ; wr::K = 0.0 ; wp::K = 0.0 ; beta::B ; unc::P
end
@inline function (arr::Marcus)(;T,P=0.0,C=0.0,phi=0.0,dGrxn=0.0,d=0.0)
    lmbd = arr.lmbd_o + evalpoly(T,arr.lmbd_i_coefs)
    arr.A*T^arr.n*exp(-lmbd/4.0*(1.0+dGrxn/lmbd)^2/(R*T)-arr.beta*d)
end
```

The RMG-Py port is `rmgpy/kinetics/arrhenius.pyx`; its barrier is

```python
cpdef double get_gibbs_activation_energy(self, double T, double dGrxn) except -1:
    lmbd_i = self.get_lmbd_i(T)
    return (lmbd_i+self.lmbd_o.value_si)/4.0*(1.0+dGrxn/(lmbd_i+self.lmbd_o.value_si))**2
```

**Three stored parameters reach no arithmetic.**

- `wr` and `wp` — the precursor/successor-complex work terms, i.e. exactly where a Marcus
  association step is supposed to live — are constructed, stored, exposed as properties, serialised
  into `.rms` files and passed into the Julia constructor, and are read by **no** arithmetic in
  either implementation.
- `beta` is absent from the RMG-Py rate law entirely; in RMS it multiplies a tunnelling distance `d`
  that is a *domain* field defaulting to `0.0` which RMG never populates. Every stored
  `beta = 1.2e10 m⁻¹` is inert.

**The author's own electrochemical reference case for this rate law** was added 16 minutes after the
type, in `8c308fdbd` *"add a Marcus reaction to the ORR.rms mechanism for testing"*
(`src/testing/ORR.rms`) — oxygen reduction, adsorbed species:

```yaml
- kinetics: {A: 6.0e12, lmbd_o: 100000.0,
             lmbd_i_coefs: [2.63844404e+03 9.64948798e+00 7.41268237e-03 -6.10277107e-06],
             beta: 1.2e10, n: 1.0, d: 0.0, type: Marcus}
  products: [HOOA] ; reactants: [O2A, H+] ; electronchange: -1 ; reversible: false
```

It is nothing like the entries here: `lmbd_o = 100 kJ/mol` against 0, `n = 1.0` against 2,
`reversible: false` against this family's `reversible = True`. The only shared parameter is
`beta = 1.2e10 m⁻¹` (1.2 Å⁻¹, the conventional electron-tunnelling decay constant).

## 4. History and author attribution

The family's entire history is five commits, by one author. **This is repository provenance. It is
not a contact list, and it authorises no enquiry.**

| commit | date | author | what it did |
|---|---|---|---|
| `dd4852f68` | 2021-12-14 | Matt Johnson `<mjohnson541@gmail.com>` | `Cation_R_Recombination initial family` — created `groups.py`, `rules.py` |
| `cc7ef729b`, `2f220fc89`, `863c05aab` | 2022-01-11 | Matt Johnson | bulk tree generation (touched siblings, not this family's rules) |
| `4c3faffdf` | **2024-03-09 18:21:21 −0800** | Matt Johnson | `add training reactions for Cation_R_Recombination` — the five Marcus training entries and `training/dictionary.txt`, both created from nothing |
| `b23abeb0c` | **2024-03-09 18:21:39 −0800** | Matt Johnson | `train Cation_R_Recombination` — regenerated `groups.py` and replaced `rules.py` wholesale with the seven Marcus rules |

Two facts fall out of this that no other source records.

**(a) Eighteen seconds.** The two 2024-03-09 commits are 18 s apart — a script run, not two human
edits. The rules were machine-generated from the training set the instant it landed.

**(b) The Marcus set *replaced* a charge-transfer set.** Before `b23abeb0c`, `rules.py` held exactly
one entry and it was not Marcus:

```python
kinetics = ArrheniusChargeTransferBM(A=(7.25239e+06,'m^3/(mol*s)'), n=0.211611,
    w0=(159759,'J/mol'), E0=(7480.68,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), …)
```

That parameterisation carries `V0`, `alpha` and `electrons` — explicit electrode semantics. **The
conversion on 2024-03-09 is the moment the electrode semantics left the entries, and it is recorded
nowhere but in that diff.**

## 5. The twelve database objects rest on five calculations

`rules.py` holds **7** entries; `training/reactions.py` holds **5**. All twelve are `Marcus`. That
is the twelve. Underneath them there are **five** independent quantum-chemical determinations, one
per radical, and **each supplies λᵢ only.**

**The seven rules are derived from the five training entries, not independent of them.** Each rule's
own `comment` says so (`"Marcus rule fitted to N training reactions at node <label>"`), the code
that wrote them is `average_kinetics` in `rmgpy/data/kinetics/family.py`, and the arithmetic
reproduces the stored numbers:

| rule node (`rules.py`) | N | training sources | max relative deviation |
|---|---|---|---|
| `Root` | 5 | NH2 + C2H5 + CH3 + CH3NH + SH | 8.31e−07 |
| `Root_2R->C` | 2 | C2H5 + CH3 | 9.04e−06 |
| `Root_N-2R->C` | 3 | NH2 + CH3NH + SH | 2.26e−06 |
| `Root_2R->C_Ext-2C-R` | 1 | C2H5 | **0.00e+00** |
| `Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R` | 1 | CH3NH | **0.00e+00** |
| `Root_N-2R->C_2BrClFHILiNOPSSi->S` | 1 | SH | **0.00e+00** |
| `Root_N-2R->C_N-2BrClFHILiNOPSSi->S` | 1 | NH2 | **0.00e+00** |

Four rules are bit-exact copies of a single training entry; three are arithmetic means. The
residuals on the multi-source nodes are 1e−6–1e−5, exactly six-significant-figure rounding. Worked:
`Root_2R->C` first coefficient = (51902.4 + 51072.9)/2 = 51487.65, stored 51487.7; `Root` =
(21824.5 + 51072.9 + 51902.4 + 22140 + 20364.7)/5 = 33460.9, stored 33460.9.

A fourth fingerprint corroborates the code path: the rules write `wr=(0,'kJ/mol')` while the
training entries write `wr=(0,'J/mol')` — exactly `average_kinetics`' `wr=(wr*0.001,"kJ/mol")`.

**The five calculations**, which *are* distinct chemistry — five radicals, one cation, one reaction
type (the stored labels write the `c+1` cation as if neutral and omit e⁻; `training/dictionary.txt`
is authoritative):

| # | label as stored | actual reaction | λᵢ(298 K) | λᵢ(1000 K) |
|---|---|---|---|---|
| 0 | `NH2 + Li <=> NH2Li` | Li⁺ + •NH₂ + e⁻ → LiNH₂ | 21.71 | 20.96 |
| 1 | `C2H5 + Li <=> C2H5Li` | Li⁺ + •C₂H₅ + e⁻ → LiC₂H₅ | 51.65 | 54.08 |
| 2 | `CH3 + Li <=> CH3Li` | Li⁺ + •CH₃ + e⁻ → LiCH₃ | 50.94 | 45.93 |
| 3 | `CH3NH + Li <=> CH3NHLi` | Li⁺ + CH₃N•H + e⁻ → CH₃N(H)Li | 20.69 | 16.10 |
| 4 | `SH + Li <=> SHLi` | Li⁺ + •SH + e⁻ → LiSH | 20.35 | 19.81 |

λᵢ in kJ/mol. The five coefficient vectors are pairwise distinct in all four components, so this is
not one calculation re-entered with substituent relabelling. All five share, identically:
`A = 1.73e+06 m³/(mol·s)`, `n = 2`, `beta = 1.2e10 m⁻¹`, `wr = wp = lmbd_o = 0`, `rank = 3`, and one
line of provenance: *"Calculated using a geometric mean with the four point method at
ccsd(t)-f12/cc-pvdz-f12//wb97x-d3/def2-tzvp"*.

**`A` and `n` carry no genealogical information.** All twelve share them identically, and a
geometric mean of a constant is that constant.

**Sizing consequence.** Any search for the underlying calculation record should be sized at **five**
λᵢ jobs — geometry optimisations and single points on R•, its charged counterpart and RLi at
`wb97x-d3/def2-tzvp` with `ccsd(t)-f12/cc-pvdz-f12` energies — not twelve rate calculations. The
four-point method yields **no** ΔG, **no** prefactor, **no** outer-sphere term, **no** temperature
range and **no** uncertainty; every one of those was supplied from elsewhere or set to zero.

## 6. Source references recovered

- **The four-point method** — "Reassessment of the Four-Point Approach to the Electron-Transfer
  Marcus–Hush Theory", *ACS Omega* **2** (2017) 7846, doi:10.1021/acsomega.7b01425. This is the
  method the entries' own `longDesc` names.
- **The rate law and its reference case** — ReactionMechanismSimulator.jl, commits `f1c175b58` and
  `8c308fdbd` (§3), reachable on branch `official/fix/py311_ci` of this repository's remote.
- **The computational-lithium-electrode convention** — stated in
  `input/thermo/libraries/computationalLithiumElectrode.py:5-14` (§2.1).

**No DOI, URL, author, report, calculation identifier, date or software name appears anywhere in
this family directory.** `grep -rn "doi\|DOI\|http\|reference" .` over this directory returns
nothing. That negative result is informative: every sibling family from the same 2021–2024 lithium
campaign (`1,2_Elimination_LiR`, `1,2_Intra_Elimination_LiR`, `Li_Addition_MultipleBond`, the
lithium additions to `H_Abstraction`) carries the **full** ARC/Arkane stamp on each training entry —
optimised TS geometry, symmetry and optical-isomer counts, 1-D rotor scans with invalidation
reasons, and a longer level-of-theory line ending `used COSMO TZPD-Fine … MAE error: 3473.27 J/mol`.
**This family's note is the first clause of that same string with everything after it removed.**

## 7. The four facts that are still missing

The domain is recovered. The rates are **not** reproducible. Four facts are required and none is
recorded anywhere in either repository, on any of the 355 fetched refs.

| # | what is missing | why it is required |
|---|---|---|
| 1 | **The Li⁺ thermochemistry the λᵢ set was computed against**, and hence the electron reference in force | ΔG enters the barrier quadratically; the two candidate references in this database differ by 502 kJ/mol and neither restores all five entries (§2.1) |
| 2 | **Whether the five λᵢ determinations used implicit solvation, and in which solvent** | Decides whether `lmbd_o = 0` means "no solvent term needed, it is already inside λᵢ" or "the solvent term was omitted". Recorded for every sibling family; absent here (§6) |
| 3 | **The derivation of `A = 1.73e6 m³/(mol·s)`, `n = 2`** | It is the entire prefactor of all twelve entries, appears nowhere else in either repository, and is the only place an association equilibrium could have been folded |
| 4 | **The association/electron-transfer decomposition `k_overall = K_assoc · k_ET`**, including whether `K_assoc` was folded into the stored rate | `wr`/`wp` are zero and unread (§3). Worse: a single shared prefactor cannot carry five per-radical association constants, so even if `K_assoc` was folded in, it **cannot be unfolded** from the stored data |

On item 3, what is known: `A·T²` = 1.54e11 m³/(mol·s) at 298 K — neither the `T^0.5` of collision
theory nor the `T¹` of an Eyring frequency factor, and roughly four orders of magnitude *above* the
liquid-phase diffusion limit. Whether that arises from an absorbed association equilibrium or from
something else cannot be determined from the repositories.

**Because of these four, the label at the top of this file says INCOMPLETE QUANTITATIVE PROVENANCE
and not "validated" — and that holds for SEI use, not only for anyone arriving from a plasma model.**

## 8. Do not

- **Do not choose between the two Li⁺ references** (§2.1). They differ by 502 kJ/mol and neither
  restores all five entries; picking one is calibration to expectation.
- **Do not infer the association contribution from the shared prefactor** (§7, item 4).
- **Do not fit a potential offset**, per-entry or global, and specifically not 4.44 V.
- **Do not refit λ.** A separate binding ruling forbids it outright.
- **Do not delete or prune anything in this directory.** The rates, the reorganisation energies, the
  training reactions and their level of theory are the provenance evidence any recovery track needs,
  and they remain valid for an electrode/electrolyte model that supplies the missing reference.
- **Do not rename the family identifier.** A rename needs a complete reference audit; it has at
  least seven consumers in the RMG-Py runtime alone (electron-placement declarations, six test
  modules, two example inputs).

## 9. The complete evidence, and where it lives

This file is a summary written to sit beside the data. The full investigation, with every command
and its real output, is committed in this repository:

| document | branch | commit | blob |
|---|---|---|---|
| `docs/i103-electrochemical-provenance.md` — the provenance investigation this file summarises | `i103-electrochem-provenance` | `069ea3d0b9a56ebfb9db936defc4d2294bf6b0db` | `483733f7535407b87446d9e5d18e76779efcf875` |
| `docs/i111-sei-reclassification.md` — the reclassification and its structural limitations | this branch | see `git log` | — |
| `docs/i092-reverse-direction-census.md` — the twelve reverse directions | `i092-reverse-census` | `d97ea12d0` | `0b040793c0426099b5e35565d7a61334ee1c4b85` |
| `docs/i104-alkali-plasma-cation-source-inventory.md` — what the alkali-plasma cation network actually needs, and why it is not this family | `i104-alkali-plasma` | `fc7bc101bfe9a44d869d10bce3b037fd7e6bdb05` | `552f0bddb2cfc1dce9e291513b388c4f1e7b47ef` |
| `docs/i041-cation-reachability.md` — reachability of the eleven charged-cation families | this branch | `fb3c13c60` | `f2d6aa115ffdf8c5307f4a6811188a845a465b21` |

SHA-256 of `docs/i103-electrochemical-provenance.md` as committed:
`d6d2e6511c2549d24e369eb13e51b6dae0ef3c6ff53fd19c1e25184c7bc132c2`.

Retrieve it with:

```bash
git show i103-electrochem-provenance:docs/i103-electrochemical-provenance.md
```

The reclassification is pinned by `test/test_cation_r_recombination_sei.py`.
