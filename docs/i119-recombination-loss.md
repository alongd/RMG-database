# I-119 — Giving the lithium plasma an electron loss channel

**Headline, and it is the boundary rather than the build: the mechanism now has an electron sink,
and it is not the dominant one — nor could any sink of its kind be.** Radiative recombination
`Li⁺ + e⁻ → Li + hν` is implemented, resolving and accepted by the reactor. It is the *only* one of
the five channels this ticket inventoried that is implementable today. It is **~1000× weaker than
the ionisation source at Te = 1 eV** (§3.2), and — the structural half, which does not depend on any
number — it is **second order in the electron density while the source is first order** (§8), so it
cannot set an electron density at all. It can only set an ionisation *fraction*, and the fraction it
sets is 99.9 % ionised.

**Answer, in one line each.**

- **Implemented: one channel.** `input/kinetics/libraries/PlasmaRadiativeRecombination`, one entry,
  `[Lip] => [Li]`, `electrons = -1`, irreversible, kinetics `BadnellRRArrhenius(Z=3, N=2)` read from
  the shipped table. Loads, balances, resolves through electron placement, and is accepted by
  `PlasmaReactor` at the Badnell rate to 12 significant figures — each shown separately in §5.
- **The Li⁺ stage is present**, measured, not assumed: `badnell.yaml` `Z: 3, N: 2`,
  `A = 8.7e-12 cm³/(molecule·s)`. §4.
- **Coverage narrows 318 → 12 → 6 → 1**, and the one is Li⁺ — the same shape of arithmetic the
  ionisation table gave, arriving at the same single species for the same reason. §4.
- **Three-body recombination — the dominant volume sink — is blocked twice over**, and the second
  blocker is new: it has no shipped fit (confirmed), *and* it **cannot be stored at all**, because
  the only Te-aware third-order rate law carries no electron count and the loader therefore refuses
  it as unbalanced. Measured in §10. Data alone would not unblock it.
- **Wall loss beats volume ionisation by 19× at 5 torr and 1877× at 0.05 torr** and the reactor has
  no place for it. Not implemented, per the ticket. §3.6.
- **Can the mechanism reach a steady electron density? Formally yes, physically no.** There is a
  stable fixed point, and it sits at 99.9 % ionisation of the lithium — roughly four orders above a
  real glow discharge — because every volume recombination channel is higher order in `n_e` than the
  source is, and only a *first*-order loss (wall) can balance a first-order source at low `n_e`.
  §8.
- **Argon can be ionised here and can never be recombined.** The two shipped tables are asymmetric
  and the asymmetry lands on this campaign's own benchmark bath gas. §4.3.

**The premise this ticket was handed was half right, and the half that failed is the interesting
one.** The dispatch's expectation was that Badnell "plausibly has both data and representation".
The data are there. The representation was not: a new library cannot resolve until a key is added to
a registry that lives in RMG-Py, not in this repository (§6.1). That is a cross-repository
dependency, and it is why §12 records what a green suite here does *not* prove.

Evidence labels: **[R]** code (file:line) · **[D]** database (file, entry) · **[M]** measured
(command and output shown) · **[L]** literature · **[I]** inference with its basis.

---

## 1. Environment and pin

| Role | Path | State |
|---|---|---|
| Reference runtime, read-only | `/home/alon/Code/RMG-Py-i116-ionisation-registry` | branch `i116-ionisation-registry`, `18abb2789`, **unmodified and not rebuilt** |
| Runtime this ticket wrote | `/home/alon/Code/RMG-Py-i119-rr-registry` | branch `i119-rr-registry`, `92e2d4234`, forked from `18abb2789`, built here |
| Data under test | `/home/alon/Code/RMG-database-i119-recombination` | branch `i119-recombination`, base `fcd87ce6e` |
| Interpreter | `/home/alon/anaconda3/envs/rmg_env/bin/python` | 3.9.23 |

Everything up to and including §5 was measured against the **reference** runtime with the
declaration injected at runtime, which is why §6.1's refusal is shown against the registry exactly
as `18abb2789` ships it. §7 and §11 were then re-measured against **both**, which is what makes the
negative control a diff rather than an assertion.

**[M]** Import resolution, printed before any other work and again after it:

```
$ PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH \
  PYTHONPATH=/home/alon/Code/RMG-Py-i116-ionisation-registry \
  python -c "import sys, rmgpy; print(sys.executable); print(rmgpy.__file__)"
/home/alon/anaconda3/envs/rmg_env/bin/python
/home/alon/Code/RMG-Py-i116-ionisation-registry/rmgpy/__init__.py
```

It must not resolve to `/home/alon/Code/RMG-Py`, which is branch `polymer` and is what `rmg_env`
gives by default — importable, working, and wrong.

**On building.** The reference checkout was **not** built and not written to: every compiled
extension there is already newer than every source (`arrhenius.pyx`, `reaction.py` and `plasma.pyx`
last written `23:29:24`; their `.so` files built `23:33`–`23:36`) **[M]**. The **new** worktree was
built with `make build`, never bare `make` — bare `make` runs `pip install -e .` and repoints the
shared conda environment under every other worker on this machine **[R]** (`Makefile:17,24-30`). It
produced 104 extensions, exactly matching the reference's 104.

**[M] A trap worth recording, because `make build` alone is not sufficient in a *fresh* worktree.**
The first build failed:

```
Cython.Compiler.Errors.InternalError: Internal compiler error: 'settings.pxi' not found
make: *** [Makefile:39: build] Error 1
```

`rmgpy/solver/settings.pxi` is **generated and gitignored** (`.gitignore:66`), written by
`utilities.py:check_pydas()`, and `make build` does not depend on it — only `make check` and the
install path do **[R]** (`Makefile:17-23`). A worktree created from a branch therefore has no
`settings.pxi` at all, and `base.pyx:45` does `include "settings.pxi"`. The fix that does **not**
touch the shared environment is to run the generator alone first:

```bash
python utilities.py check-pydas   # writes rmgpy/solver/settings.pxi; no pip, no sentinel
make build
```

**And a second trap that nearly hid the first.** The failed build was launched as
`( ... make build ... ); echo "EXIT=$?"`, which reported `EXIT=0` — the exit status of the `echo`,
not of `make`. The failure was caught only because the artefact count was checked afterwards
(`find . -name '*.so' | wc -l` returned 0). **Verify a build by its artefacts, not by a reported
exit code.**

**`database.directory` is pinned to this worktree**, never the shared plasma checkout. The `rmgrc`
that ships on the runtime branch points at `../RMG-database-plasma/input` **[R]**, so leaving the
pin to discovery would have measured a database nobody edited. Every probe prints `PIN-BEFORE` and
`PIN-AFTER`, and both read `/home/alon/Code/RMG-database-i119-recombination/input` in all five. The
suite pins the same way, in `test/conftest.py` and again at the head of the new test module.

Five probes, stdout and stderr both persisted, all outside every tracked tree, under
`/tmp/claude-1000/-home-alon-Code-RMG-database-i119-recombination/b33b06d4-.../scratchpad/`:
`probe1` (table coverage and buildability), `probe2` (the four stages), `probe3` (what blocks
three-body), `probe4` (rate ranking, steady state, wall loss, Langevin), `probe5` (table asymmetry,
Li₂⁺). Being scratch they are not durable; the output quoted here is the durable record.

---

## 2. The conditions I assumed, and what depends on them

### 2.1 The gap is real and it is not mine to close

No ratified M7 condition set exists in this project. I did not invent one. What I did instead was
adopt, unchanged, the set that `docs/i104-alkali-plasma-cation-source-inventory.md` §0.2 proposed
from the campaign's own anchors, so that this report and that one are comparable line by line and
neither introduces a second unratified standard.

| Quantity | Assumed | Basis |
|---|---|---|
| Composition | Ar or N₂ bath + trace Li (10⁻⁴–10⁻² mole fraction), neutral at t = 0 | The campaign's benchmark bath (I-004/I-007); Li's 5.392 eV ionisation energy is 6–10 eV below any plausible bath gas, so trace Li dominates the ion balance |
| Pressure | 0.05–5 torr, centred on 5 torr | I-004 (5 torr, room temperature) and I-007 (0.05–1.0 torr sweep) |
| `Tgas` | 300–1000 K | I-004's "room temperature"; the lithium NASA polynomials here are valid to 3000 K, so there is headroom |
| `Te` | 0.5–2 eV, centred on 1 eV | The campaign's adjudicated three-body working point, and the standard low-pressure glow range |
| EEDF | **Maxwellian — not a free choice** | `BadnellRRArrhenius` and `VoronovEIArrhenius` are Maxwellian-averaged fits by construction **[L]**; the runtime has no non-Maxwellian EEDF path and no Boltzmann solver |
| E/N | Not represented at all | `PlasmaReactor` takes `T`, `P`, `Te` and nothing else **[R]** |
| `n_e` | 10¹⁰–10¹⁴ cm⁻³, centred on 10¹² | Standard glow range; the reactor requires an explicit positive value and supplies no default |
| Residence time | **UNKNOWN**; assumed integration horizon 10⁻⁵–10⁻¹ s | `PlasmaReactor` is a batch reactor with no flow term **[R]**, so "residence time" can only mean the integration horizon. **What would settle it:** a ratified M7 reactor specification |
| Geometry | Cylinder R = 1 cm, L = 10 cm, for the wall-loss estimate only | Nothing in the project specifies one; no implemented channel depends on it |

### 2.2 Which conclusions survive the choice and which do not

| Finding | Robust or sensitive |
|---|---|
| Radiative recombination is the **only** implementable electron sink today | **Robust.** A property of the shipped data and the runtime, independent of conditions |
| Three-body recombination cannot be **stored**, regardless of data | **Robust.** A property of the code (§10) |
| **A volume recombination channel cannot set an electron density, only an ionisation fraction** — source first order in `n_e`, sinks second and third | **Robust.** Structural, holds at every Te, pressure, bath and density (§8) |
| Radiative recombination is not the dominant volume sink | **Robust in ranking, sensitive in size.** Three-body beats it by 2.2× at n_e = 10¹⁰ and 8.7× at 10¹⁴, Te = 1 eV (§3.3) |
| The source outruns the implementable sink by ~10³ | **SENSITIVE to Te, strongly.** 993× at 1 eV; 1.8× at 0.5 eV; the ranking **inverts** below ~0.45 eV, where the 5.4 eV threshold shuts ionisation off (§3.2) |
| The fixed point sits at 99.9 % ionisation | **SENSITIVE, same way.** 0.9990 at 1 eV, 0.6397 at 0.5 eV, 0.00067 at 0.3 eV (§8) |
| Wall loss outruns volume ionisation | **SENSITIVE in size, robust in direction across the assumed pressure range.** 19× at 5 torr, 1877× at 0.05 torr; the ranking inverts only near 1 atm (§3.6) |
| Li⁺ is the terminal ion of any mixed feed | **Robust.** Driven by a 6.7–10.4 eV ionisation-energy gap (§3.7) |
| Badnell's Li⁺ fit is used inside its stated range | **Robust.** Tmin/Tmax = 10 K / 10⁷ K, wider than any condition considered |

The single most load-bearing ratification is **`Te`**. Everything about the *size* of the mismatch
between source and sink moves by four orders across 0.3–2 eV. Nothing about its *structure* moves at
all.

---

## 3. The loss-channel inventory

Every channel is written **one-way**. Field key, per the dispatch: **eq** elementary equation ·
**mol** molecularity · **T** the temperature that drives it · **net e** net electron stoichiometry ·
**prov** provenance · **impl** implementable today, with the reason.

### 3.1 Summary

| # | Channel | mol | driven by | net e | Implementable today? |
|---|---|---|---|---|---|
| 1 | Radiative recombination `Li⁺ + e⁻ => Li + hν` | 2 → 1 | Te | −1 | **YES — implemented here** |
| 2 | Three-body e–e–ion recombination `Li⁺ + 2e⁻ => Li + e⁻` | 3 → 2 | Te | −1 | **No** — no shipped fit **and** not storable (§10) |
| 3 | Neutral-stabilised three-body `Li⁺ + e⁻ + M => Li + M` | 3 → 2 | Te, Tgas | −1 | **No** — no Li-specific coefficient exists; also §10 |
| 4 | Dissociative recombination `Li₂⁺ + e⁻ => Li + Li*` | 2 → 2 | Te | −1 | **No** — the reactant cannot be built (§3.5) |
| 5 | Wall / surface loss `Li⁺ + e⁻ --(wall)--> Li` | not a volume rate law | Tgas, P, Te, geometry | −1 per event | **No** — a reactor capability this reactor lacks (§3.6) |
| 6 | Charge transfer `X⁺ + Li => X + Li⁺` | 2 → 2 | Tgas (weakly) | **0** | **Not a loss channel at all** (§3.7) |

### 3.2 Channel 1 — Radiative recombination of Li⁺ ✅ *implemented*

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ => Li + hν` — canonical database form `[Lip] => [Li]`, `electrons = -1` |
| **mol** | 2 → 1 (the photon is not a species) |
| **T** | **Te**, and only Te. Tgas: no. P: no. E/N: no. EEDF: Maxwellian, structurally |
| **net e** | **−1**; incident-electron order **1**; overall order **2** |
| **prov** | Badnell, N. R., "Radiative recombination data for modeling dynamic finite-density plasmas", *ApJS* **167** (2006) 334–342, doi:10.1086/508465 **[L]**; shipped as `input/kinetics/badnell.yaml`, `Z: 3, N: 2` **[D]** |
| **states** | Total RR only, summed over all final n, l. The radiative cascade is not resolved and the photon is not represented |
| **applic** | Fully inside range: Tmin/Tmax = 10 K / 10⁷ K, wider than any condition considered |
| **unc** | Badnell's fits reproduce his own calculations to ≲5 %; RR theory for a two-electron target is good to ~10–20 % **[L]**+**[I]**. Small next to every other uncertainty here |
| **impl** | **Yes.** Data shipped, rate law carries a signed `electrons`, one placement declaration needed. §5 |
| **Physical inverse** | **Photoionisation** `Li + hν => Li⁺ + e⁻` — a photon partner and a radiation-field driving quantity. `PlasmaReactor` has no radiation field **[R]**, so this inverse cannot be represented at all and RR must stand as a strictly one-way sink. Defensible for an optically thin cold plasma, and **stated rather than assumed** |

**[M]** Measured against the pin, next to the ionisation channel at the same Te — which is the
comparison the dispatch asks for, and the reason this ticket's headline is a boundary:

| Te / eV | α_RR / cm³ s⁻¹ | α_ion / cm³ s⁻¹ | α_ion / α_RR |
|---|---|---|---|
| 0.30 | 5.6323e−13 | 3.7555e−16 | **0.00067** |
| 0.50 | 3.7699e−13 | 6.6935e−13 | 1.78 |
| 0.80 | 2.5887e−13 | 4.9538e−11 | 191 |
| 1.00 | 2.1611e−13 | 2.1471e−10 | **993.5** |
| 1.50 | 1.5512e−13 | 1.5903e−09 | 1.03e+4 |
| 2.00 | 1.2227e−13 | 4.4733e−09 | 3.66e+4 |

Radiative recombination is nearly flat in Te (a weak Te^−0.6 decline); ionisation moves six orders
across the same span, because of the 5.4 eV threshold. **The crossover is near Te ≈ 0.45 eV.** Above
it the source dominates by up to four orders; below it the plasma simply decays. Every one of these
α_RR values reproduces `docs/i104-alkali-plasma-cation-source-inventory.md` §4.2 exactly, which is
an independent corroboration rather than a citation.

### 3.3 Channel 2 — Three-body electron–ion recombination ❌ *the dominant volume sink, and unreachable*

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ + e⁻ => Li + e⁻` |
| **mol** | 3 → 2 (exactly at `PlasmaReactor`'s three-participant ceiling) |
| **T** | **Te, strongly** — ≈ Te^−4.5. n_e enters through the reaction *order*, not the coefficient, which is why the third body must be written explicitly and never as `ThirdBody`/`Lindemann`/`Troe`; the reactor refuses pressure-dependent kinetics outright **[R]** |
| **net e** | **−1**; incident-electron order **2**; overall order **3**. Its placement declaration would be `(2, 1)` |
| **prov** | **Not in this repository** **[M]**: `input/kinetics/` holds exactly `voronov.yaml` and `badnell.yaml`, and a case-insensitive grep of `input/` for `stevefelt\|mansbach\|collisional.radiative\|TwoTemperaturePlasma` returns nothing. The literature formula is Stevefelt, J., Boulmer, J. & Delpech, J.-F., "Collisional–radiative recombination in cold plasmas", *Phys. Rev. A* **12** (1975) 1246–1251, doi:10.1103/PhysRevA.12.1246 **[L]**, resting on Mansbach, P. & Keck, J., *Phys. Rev.* **181** (1969) 275, doi:10.1103/PhysRev.181.275 **[L]** |
| **states** | **Unresolved, and it matters.** Capture is into high Rydberg levels which then cascade; writing `=> Li` compresses a ladder into one step. Faithful representation needs Li Rydberg manifolds, which RMG cannot express |
| **applic** | Stevefelt's formula was derived for **Te < 4000 K** **[L]**; the working point Te = 1 eV is 11 605 K, ~3× above it. Standard practice extrapolates it, but that is an assumption |
| **impl** | **No, for two independent reasons, either sufficient.** (a) No shipped fit. (b) **It cannot be stored even with one** — §10 |
| **Physical inverse** | **Electron-impact ionisation** (`PlasmaElectronImpactIonization` on this base). This is the genuine microscopic inverse — same participants, reversed — and **the only true forward/inverse pair in this inventory** |

**[M]** How much is being left out. Stevefelt's coefficient
`α_cr = 1.55e-10·Te^-0.63 + 6.0e-9·Te^-2.18·n_e^0.37 + 3.8e-9·Te^-4.5·n_e` (Te in K, n_e in cm⁻³,
cm³/s), evaluated against the Badnell fit that ships:

| n_e / cm⁻³ | α_cr/α_RR at 0.5 eV | at 1.0 eV | at 2.0 eV |
|---|---|---|---|
| 10¹⁰ | 2.25 | 2.16 | 2.33 |
| 10¹² | 4.60 | 3.03 | 2.66 |
| 10¹⁴ | 28.5 | 8.66 | 4.58 |

**Three-body recombination beats radiative recombination everywhere in the assumed range.** Omitting
it understates the volume electron sink by between 2× and 29×.

**Warning against double counting, carried forward because it now binds a shipped entry.** Stevefelt's
*first* term, `1.55e-10·Te^-0.63`, **is** the radiative contribution. Anyone who later stores the full
Stevefelt coefficient alongside the `PlasmaRadiativeRecombination` entry added here counts radiative
recombination twice. Use Stevefelt's collisional terms only, or Stevefelt alone — never both in full.

**[M]** A decomposition worth recording, because it changes what "store the three-body rate" even
means. At Te = 1 eV:

| n_e / cm⁻³ | t₁ (radiative) | t₂ (∝ n_e^0.37) | t₃ (∝ n_e) | α_RR (Badnell) |
|---|---|---|---|---|
| 10¹⁰ | 4.262e−13 | 4.143e−14 | 1.945e−17 | 2.161e−13 |
| 10¹² | 4.262e−13 | 2.276e−13 | 1.945e−15 | 2.161e−13 |
| 10¹⁴ | 4.262e−13 | 1.251e−12 | 1.945e−13 | 2.161e−13 |

**[I]** Only t₃ is linear in n_e, so **only t₃ maps onto an elementary third-order reaction**. t₂'s
`n_e^0.37` is a collisional–radiative *effective* coefficient with the cascade folded in; it has no
elementary reaction to be the rate law of. Basis: the definition of reaction order. So "storing
three-body recombination" can only ever mean storing

`k_3b(Te) = 3.8e-9·Te_K^-4.5 = 1.945e-27·Te_eV^-4.5 cm⁶/s`

— and at n_e = 10¹² that term is **1.9e−15 cm³/s against α_RR = 2.2e−13**, i.e. two orders *below*
the channel that ships. The dominant part of collisional–radiative recombination is not an
elementary reaction at all. That is a finding about the milestone: even a perfect three-body entry
would not carry the sink the ratio table above promises.

**[D]** The campaign's own adjudicated coefficient, `8.75e-27·Te_eV^-4.5 cm⁶/s` (`plasma-pm2`
`INSIGHTS.md`, I-013), is **4.50×** the Stevefelt t₃ value re-expressed in eV — same class, same
exponent, ordinary inter-treatment spread. The adjudicated value is corroborated, not contradicted.
It is nonetheless **not entered here**: it is an adjudication in a PM repository, not a sourced,
shipped fit in this database, and the ticket forbids authoring a rate. Even if it were entered, §10
shows it could not load.

### 3.4 Channel 3 — Neutral-stabilised three-body recombination ❌

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ + M => Li + M`, M = Ar or N₂ · **mol** 3 → 2 · **net e** −1 · **T** Te and Tgas |
| **prov** | **UNKNOWN for Li⁺ specifically.** No measured or computed `Li⁺ + e⁻ + Ar` coefficient was found. **What would settle it:** a flowing-afterglow measurement, or a Li-specific collisional–radiative model including neutral collisions |
| **impl** | **No.** No data, and §10's representation blocker applies identically |
| **Physical inverse** | **Thermal ionisation by neutral collision**, `Li + M => Li⁺ + e⁻ + M`. **[I]** At Tgas ≤ 1000 K this needs 5.392 eV from a thermal collision; the Boltzmann factor `exp(−5.392 eV/kT)` ≈ 10⁻²⁷. Negligible, and **omitted explicitly rather than reconstructed from the forward via `Keq`** |

**Dismissed, with the reason recorded.** **[I]** A neutral third body is far less effective than an
electron at carrying off the binding energy of a high Rydberg state, and standard practice is that
the electron-stabilised term dominates below ~1 atm — so §3.3 covers the same sink better, and with
at least a sourced formula behind it. That is an inference from the physics of energy transfer, not
a measurement.

### 3.5 Channel 4 — Dissociative recombination ❌ *unrepresentable at the molecule layer*

| Field | Value |
|---|---|
| **eq** | `Li₂⁺ + e⁻ => Li + Li*` · **mol** 2 → 2 · **net e** −1 · **T** Te, typically ≈ Te^−0.5 |
| **prov** | **UNKNOWN.** No Li₂⁺ dissociative-recombination cross section or rate coefficient was found. **[L]**+**[I]** Li₂⁺ is a hard case theoretically — like H₂⁺ it lacks a favourable low-lying doubly excited dissociative state crossing the ion's ground vibrational level, so the indirect Rydberg mechanism dominates and MQDT machinery is needed. **What would settle it:** an MQDT calculation or a storage-ring measurement |
| **states** | Would be strongly state-resolved (Li(2s)+Li(2p) vs Li(2s)+Li(2s)) — resolution RMG cannot express |
| **impl** | **No, on two independent grounds, either sufficient** |
| **Physical inverse** | **Associative ionisation** `Li + Li* => Li₂⁺ + e⁻` — a different process with a different rate, not "DR backwards" |

**[M]** Ground 1: `Li₂⁺` cannot be built in this runtime. Re-measured here rather than cited:

```
Li2  (neutral) OK  q=+0  [Li][Li]
Li2+ (cation)  FAIL AtomTypeError: Unable to determine atom type for atom Li+, which has
               1 single bonds, 0 double bonds ... and +1 charge.
Li2+ (alt)     FAIL AtomTypeError: (same)
```

`ATOMTYPES` defines `Li`, `Li+` and `Li0`, and none of them accepts a **bonded** Li⁺ **[R]**. Neutral
Li₂ builds fine, which is what makes this a representational limit and not a chemistry one. Ground 2:
no rate data exists to store even if it did.

***Note for a mixed feed.*** If M7 is Li in **air** rather than Li in Ar, dissociative recombination
of N₂⁺ and O₂⁺ becomes the dominant electron sink, and for *those* ions the data are abundant and
the ions are buildable. That is air chemistry and belongs to the M6/air track — but it is the single
most promising route to a dominant, implementable sink, and it is named here so it is not lost.

### 3.6 Channel 5 — Wall and surface loss ⚠️ *dominant, and structurally unrepresentable*

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ --(wall)--> Li`, transport-limited by ambipolar diffusion |
| **mol** | **Not defined** — it is a boundary condition, not a volume rate law. Its dependence on `n_e` is **first order** |
| **T** | Tgas and P (through the neutral density and hence ion mobility), Te (through `D_a ≈ D_i(1 + Te/Ti)`), and **reactor geometry**, which no other channel here depends on |
| **net e** | −1 per event |
| **prov** | Standard ambipolar-diffusion theory; the mobility input is `μ₀(Li⁺ in N₂) ≈ 4 cm²/(V·s)` at STP, an order-of-magnitude value. **UNKNOWN:** a measured reduced mobility for Li⁺ in the actual bath. **What would settle it:** an ion-mobility measurement or a Mason–Schamp calculation |
| **impl** | **No. Neither family nor library — it is a reactor feature, and this reactor does not have one.** `PlasmaReactor` is a homogeneous isobaric batch reactor with no surface, no geometry and no diffusion term **[R]**. **Not implemented, and deliberately not approximated by a volume reaction** |
| **Physical inverse** | **Wall desorption / sputtering of Li** — a surface *source* with entirely different physics. Not represented; **[I]** at these energies not expected to matter |

**[M]** The size of what is being dropped, for a cylinder R = 1 cm, L = 10 cm at Te = 1 eV, against
τ_ion at n_e = 10¹² cm⁻³:

| P / torr | D_a / cm² s⁻¹ | τ_wall / s | τ_ion / s | Which wins |
|---|---|---|---|---|
| 0.05 | 6.850e+4 | 2.481e−6 | 4.658e−3 | **wall, by 1877×** |
| 1.0 | 3.425e+3 | 4.963e−5 | 4.658e−3 | **wall, by 94×** |
| 5.0 | 6.850e+2 | 2.481e−4 | 4.658e−3 | **wall, by 19×** |
| 760 | 4.507e+0 | 3.772e−2 | 4.658e−3 | volume, by 8× |

**Across the whole assumed pressure range the dominant electron sink is the one the reactor cannot
represent**, and it gets worse as pressure falls. The 5 torr row reproduces
`docs/i104-alkali-plasma-cation-source-inventory.md` §4.9 exactly. A mechanism that omits it
over-predicts steady-state electron density, one-sidedly. §8 shows *why* no volume channel can
substitute.

### 3.7 Channel 6 — Charge transfer to abundant neutrals ✅ *representable, and not a loss channel*

| Field | Value |
|---|---|
| **eq** | `X⁺ + Li => X + Li⁺`, X = N₂, O₂, Ar, H₂O, NO · **mol** 2 → 2 · **T** Tgas, weakly |
| **net e** | **0 — no electron participates, and none is created or destroyed** |
| **prov** | **No direct measurement of `N₂⁺ + Li`, `O₂⁺ + Li` or `Ar⁺ + Li` was found.** The venue would be Anicich's compilation of gas-phase ion–molecule rate constants or the UMIST/KIDA databases; neither was reached. The defensible fallback is the Langevin capture rate, computed here from Li's static dipole polarizability α = 24.33 Å³ **[M]**: `N₂⁺ + Li` 4.898e−9, `O₂⁺ + Li` 4.837e−9, `Ar⁺ + Li` 4.750e−9, `He⁺ + Li` 7.252e−9 cm³/s |
| **unc** | Factor ~2–3, **one-sided**: Langevin is an upper bound, assuming every capture collision transfers charge **[L]**+**[I]** |
| **impl** | Representable — charge-conserving, no electron, `is_balanced = True` — but **not implemented here**, because it is not a loss channel and the ticket is the sink half. It is also not authorable from shipped data: the Langevin numbers are computed, not cited |
| **Physical inverse** | **Endothermic charge transfer** `Li⁺ + X => Li + X⁺`, endothermic by IE(X) − IE(Li) = 6.68 eV (O₂) to 10.37 eV (Ar). **[I]** At Tgas ≤ 1000 K the Boltzmann factor is below 10⁻³³. **Omitted as a named, explicitly negligible channel — never reconstructed from the forward through `Keq(Tgas)`** |

**Explicitly dismissed as a loss channel, and it is the campaign's terminal-species risk instead.**
Charge transfer *moves* an existing charge; it destroys none. With IE(Li) = 5.392 eV against
IE(N₂) = 15.581, IE(Ar) = 15.760, IE(O₂) = 12.070, IE(H₂O) = 12.621 **[L]** (NIST ASD and Chemistry
WebBook), every bath-gas ion converts to Li⁺ on essentially every capture collision — **[I]** a
~1.3e−7 s conversion time at 5 torr with 1 % Li, four orders faster than any recombination channel
above. **Li⁺ becomes the terminal ion**, which makes the Li⁺ loss channels load-bearing rather than
decorative. That is the argument *for* this ticket, and §8 is the reason it is only half satisfied.

---

## 4. The Li⁺ stage, and the coverage arithmetic

### 4.1 The stage is present — measured, not assumed

The dispatch asked for this to be checked rather than trusted, on the precedent that of 134 Voronov
stages only a handful were usable. **[M]**, parsing `input/kinetics/badnell.yaml` directly:

```
source: Badnell, N.R. (2006) ApJS 167, 334, Radiative Recombination Data for Modeling
        Dynamic Finite-Density Plasmas
notes : Z is the nuclear charge, N is the number of electrons prior to recombination.
blocks: 33   total (Z,N) stages: 318
Z values: [1..30, 36, 42, 54]

Li block: {'Z': 3, 'entries': [
    {'N': 0, 'A': 2.867e-10, ...},
    {'N': 1, 'A': 9.349e-11, ...},
    {'N': 2, 'A': 8.7e-12, 'B': 0.364, 'T0': 1.470e2, 'T1': 7.153e6,
             'C': 0.1508, 'T2': 7.154e5}]}
```

**Present.** `N` counts electrons *prior to* recombination per the table's own `notes`, so `N = 2`
is the two-electron ion Li⁺ capturing to three-electron neutral Li. That off-by-one is the plausible
mistake and it is pinned by an assertion on the A-factor, not merely on the index.

### 4.2 318 → 12 → 6 → 1

**[M]** Only `N = Z − 1` — a singly charged cation capturing to the neutral — is a stage this
database can represent at all. The other 306 are multiply charged ions, a separate representational
problem this ticket does not open.

```
cation -> neutral stages (N = Z-1) present for Z = [1..12]  -> 12 of 33 blocks
```

**[M]** Of those 12, how many can RMG build on *both* sides in their gas-phase ground states:

```
sym  cation (reactant)                neutral (product)
H    OK q=+1 [H+]                     OK q=+0 [H]
He   OK q=+1 [He+]                    OK q=+0 [He]
Li   OK q=+1 [Li+]                    OK q=+0 [Li]
Be   FAIL KeyError: 'Be'              FAIL KeyError: 'Be'
B    FAIL KeyError: 'B'               FAIL KeyError: 'B'
C    FAIL AtomTypeError (C u1 p1 c+1) OK q=+0 [C]
N    OK q=+1 [N+]                     OK q=+0 [N]
O    OK q=+1 [O+]                     OK q=+0 [O]
F    FAIL AtomTypeError (F u2 p2 c+1) OK q=+0 [F]
Ne   OK q=+1 [Ne+]                    OK q=+0 [Ne]
Na   FAIL KeyError: 'Na'              FAIL KeyError: 'Na'
Mg   FAIL KeyError: 'Mg'              FAIL KeyError: 'Mg'

Both endpoints buildable: 6 -> ['H', 'He', 'Li', 'N', 'O', 'Ne']
```

**[D]** Of those 6, how many have thermochemistry for the *reactant cation* as a free monatomic ion
in this database? Grepping every `thermo/libraries/*.py` for a single-line adjacency list carrying
`c+1` returns exactly two species — the same two the ionisation ticket found:

| species | file |
|---|---|
| `1 Li u0 p0 c+1` (`[Lip]`) | `LithiumPrimaryThermo.py`, `computationalLithiumElectrode.py` |
| `1 H u0 p0 c+1` (`proton`) | `electrocatThermo.py`, `electrocatLiThermo.py` |

Every other `c+1` hit is a *bonded* atom inside a polyatomic species (NO⁺, NH₄⁺, …). **[I]** The
`proton` entry is an electrocatalysis reference species carrying the computational-hydrogen-electrode
convention; putting it in a gas-phase plasma would import an unrelated reference state. Basis: the
libraries it lives in and their contents.

**So coverage narrows 318 → 12 → 6 → 1, and the one is Li⁺.** He⁺, N⁺, O⁺ and Ne⁺ have no monatomic
thermochemistry here; until that lands, no owner of any kind could put those reactions in a model.
**The bound is thermochemistry, not this table and not the library-versus-family choice.**

### 4.3 The two shipped tables are asymmetric, and it lands on the bath gas

**[M]** A finding this ticket adds, from comparing the two tables' usable stages directly:

```
Voronov neutral->+1  Z: [1, 2, 3, 6, 7, 8, 11, 12, 13, 14, 18, 19, 20]
Badnell +1->neutral  Z: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ionisable but NOT recombinable Z: [13, 14, 18, 19, 20]     # Al, Si, Ar, K, Ca
recombinable but NOT ionisable Z: [4, 5, 9, 10]            # Be, B, F, Ne
both                          Z: [1, 2, 3, 6, 7, 8, 11, 12]

Ar is Z=18. Badnell Z=18 N values: [0..11] -> N=17 present? False
Voronov  Z=18 N values: [1..18]            -> N=18 present? True
```

**Argon — this campaign's benchmark bath gas — can be ionised from shipped data and can never be
radiatively recombined from it.** Badnell's cation-to-neutral stages stop at Z = 12; Ar's block
covers only Ar XIII and above. An Ar-bath mechanism built from these two libraries would create
argon ions it has no channel to remove. This is a data hole that reads as a modelling choice, and it
is pinned by `test_argon_can_be_ionised_here_but_cannot_be_radiatively_recombined`.

---

## 5. The whole path, step by step

**[M]** Run against the pinned worktrees. Each of the four steps is also a test in
`test/test_plasma_radiative_recombination.py`.

### Step 1 — LOAD

```
INFO:root:Loading kinetics library PlasmaRadiativeRecombination from
  /home/alon/Code/RMG-database-i119-recombination/input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py...
library loaded  : PlasmaRadiativeRecombination  entries: 1
entry.label     : [Lip] => [Li]
reaction class  : LibraryReaction | library = PlasmaRadiativeRecombination
                                  | family  = PlasmaRadiativeRecombination
reactants       : [('[Lip]', 1)]
products        : [('[Li]', 0)]
rxn.electrons   : -1
rxn.reversible  : False
kinetics        : BadnellRRArrhenius | A = 8.7e-12 cm^3/(molecule*s) | B = 0.364
                  | T0 = 147 K | T1 = 7.153e+06 K | C = 0.1508 | T2 = 715400 K
kinetics.electrons        : -1
uses_electron_temperature : True
uses_electron_density     : True
Tmin/Tmax       : 10 K / 1e+07 K
explicit electron participants: 0
```

The kinetics are **not authored here**: the entry is `BadnellRRArrhenius(Z=3, N=2)`, which reads
`settings['database.directory']/kinetics/badnell.yaml` at load **[R]** (`arrhenius.pyx:887`), so the
shipped table stays the single source of the numbers. `electrons = -1` arrives on the reaction
because `KineticsLibrary.load` copies it off the rate law **[R]** (`library.py:583`) — the step that
three-body recombination cannot take (§10).

### Step 2 — BALANCE

```
rxn.is_balanced() : True
net charge L/R    : +1 / +0   (electrons=-1 closes it)
```

Atoms balance trivially. The charge does not, and `Reaction.is_balanced` closes it by folding in the
metadata electron — which only works because step 1's propagation happened.

### Step 3 — RESOLVE ELECTRON PLACEMENT

The refusal is shown **first**, against the registry exactly as the runtime ships it:

```
registry as SHIPPED by the runtime: {'Plasma_Electron_Attachment': (1, 0),
                                     'Cation_R_Recombination': (1, 0),
                                     'PlasmaElectronImpactIonization': (1, 2)}
undeclared      : ElectronPlacementError: Family 'PlasmaRadiativeRecombination' has no
                  electron-placement declaration (reaction [Lip] => [Li], electrons=-1);
                  refusing to infer electron placement from the net electron count

registry WITH the declaration: {..., 'PlasmaRadiativeRecombination': (1, 0)}
rxn.family      : 'PlasmaRadiativeRecombination'
VIEW            : [Lip] + e => [Li]
view reactants  : ['[Lip]', 'e']
view products   : ['[Li]']
view.electrons  : 0 | view.reversible: False
view.comment    : Electron-placement view (family 'PlasmaRadiativeRecombination',
                  rate-order cross-check: agrees (order 2)) of: [Lip] => [Li]
E balance L/R   : 0 / 0
CANONICAL UNCHANGED: True | electrons=-1 reactants=['[Lip]'] products=['[Li]']
```

Three things to read off it.

- **The refusal comes first, and nothing is inherited.** This matters more here than it did for
  ionisation: `electrons = -1` is *attachment-shaped*, and `Plasma_Electron_Attachment` already
  declares `(1, 0)` — the very value this library needs. An undeclared owner whose shape another
  owner has declared still resolves to nothing. There is no path from "undeclared" to "resolved by
  analogy".
- **The E pseudo-element balances at 0/0, not 1/1.** A captured electron is a bound electron, and
  the cation's deficit is exactly what it fills. That is the structural proof the declared *sides*
  were the right sides.
- **The rate-order cross-check agrees at order 2**, which is the proof that the declared *incident
  order* matches the `cm³/(molecule·s)` Badnell coefficient. The canonical database reaction is
  byte-identical afterwards.

### Step 4 — ACCEPTED BY THE PLASMA REACTOR

```
core species    : ['[Lip]', '[Li]', 'e']
ACCEPTED. reactor.electron_index = 2
kf (m^3/mol/s)  = [130142.84590741]
k_Badnell(Te=11604.5 K) = 130142.8459074114
```

`PlasmaReactor.initialize_model` was handed the **canonical** reaction and resolved placement
itself, so this is the path a real model takes. Acceptance alone would not be enough — a view
evaluated at the wrong reaction order does not raise — so `kf` is compared against
`BadnellRRArrhenius.get_rate_coefficient_electron_temp(1 eV)` and matches to 12 significant figures.

---

## 6. The declaration

### 6.1 Where it lives, and why that is a finding

`FAMILY_ELECTRON_PLACEMENT` is a module-level dict in RMG-Py **[R]**
(`rmgpy/electron_placement.py:149`), described in its own comment as "a closed, hand-maintained
list". A database repository cannot ship an entry in it. The one-line addition this library needs is

```python
'PlasmaRadiativeRecombination': (1, 0),
```

`LibraryReaction.__init__` sets `self.family = library` **[R]** (`library.py:100`), which is what
makes a library label a valid key at all.

**This is the half of the dispatch's premise that failed.** The brief expected Badnell to have "both
data and representation" because the rate law now carries a signed `electrons` field. It does — but
carrying an electron count gets a reaction through the *loader*, not through the *resolver*, and
those are two different gates in two different repositories.

**It has been committed**, on a branch of its own rather than into the read-only reference:
`i119-rr-registry` at `92e2d4234`, in `/home/alon/Code/RMG-Py-i119-rr-registry`, forked from
`i116-ionisation-registry@18abb2789`. The change is the registry key plus the comment beside it, and
the two pre-existing tests that assert the registry's exact contents
(`i108ElectronRepresentationMatrixTest.py`, `i113IonisationPlacementTest.py`) updated for a fourth
owner. **No resolver logic moved** — the two-sided schema I-113 built already expresses this shape.
`i116IonisationRegistryTest.py` needed no change: it keys everything off its own `LIBRARY` constant
rather than the whole table.

**[M]** Against that runtime, with the declaration shipped rather than injected:

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-i119-rr-registry python -c "..."
REGISTRY:
   Plasma_Electron_Attachment       (1, 0)
   Cation_R_Recombination           (1, 0)
   PlasmaRadiativeRecombination     (1, 0)
   PlasmaElectronImpactIonization   (1, 2)
exact-table assertion: OK
```

**The new entry is the first to duplicate an existing *value* while declaring different chemistry.**
`Plasma_Electron_Attachment`, `Cation_R_Recombination` and now `PlasmaRadiativeRecombination` all
read `(1, 0)` for three unrelated processes. That duplication is the argument for the table being a
list of **owners** rather than a list of **shapes** — and §5's refusal is the proof it behaves that
way, since an undeclared owner is refused by name even when another owner has already declared its
exact numbers.

### 6.2 It validates against the reaction's own electron count

```
declared net = 0 - 1 = -1 ; reaction.electrons = -1 ; agree: True
```

**[M]** And five wrong declarations are each refused — it takes two distinct guards to catch them:

| declaration | net implied | refused by |
|---|---|---|
| `(2, 1)` | −1 (**correct net**) | the view-shape guard: "built a view with 3 reactant(s)" — third order against a second-order coefficient |
| `(0, 1)` | +1 | the net-count guard: "ionization-shaped … family declares …" |
| `(1, 2)` | +1 | net-count guard (this is the *ionisation* declaration) |
| `(2, 0)` | −2 | net-count guard |
| `(1, 1)` | 0 | net-count guard |

`(2, 1)` is the one that matters most and the one only the second guard sees: its net is right, and
it is **precisely the declaration three-body recombination would carry**. A copy-paste between the
two entries is the plausible mistake, and it is caught.

---

## 7. Negative control — nothing that worked before has moved

Done three ways, each stronger than the last.

**(a) In the suite**, each pre-existing shape is resolved **twice** — once with this library's
declaration absent from the registry and once with it present — and the two views compared
participant by participant. The ionisation library is **loaded from disk** rather than
reconstructed, so this also catches an accidental edit to the entry on this base.

**(b) Across the two runtimes [M].** The same three owners resolved against the reference runtime
(no new key) and against `i119-rr-registry` (key shipped), output diffed:

| owner | view | `electrons` | k at Te = 1 eV | canonical after |
|---|---|---|---|---|
| `Plasma_Electron_Attachment` | `O2 + e => O2-` | 0 | 1.0000000000e+04 | `electrons=-1  ['O2'] => ['O2-']` |
| `Cation_R_Recombination` | `Lip + CH3 + e => CH3Li` | 0 | 1.0000000000e+04 | `electrons=-1  ['Lip','CH3'] => ['CH3Li']` |
| `PlasmaElectronImpactIonization` | `[Li] + e => [Lip] + e + e` | 0 | 1.2929913339e+08 | `electrons=+1  ['[Li]'] => ['[Lip]']` |

```
$ diff without.log with.log
IDENTICAL: every pre-existing owner resolves byte-for-byte the same with and without
the new declaration.
```

Not "equivalent" — byte-for-byte, participants, net count, rate coefficient and unmutated canonical
reaction alike.

**(c) The upstream suites, un-skipped [M].** The three RMG-Py suites that assert the registry's
contents were run against the new runtime. Run as they normally are they report `64 passed, 35
skipped` — *identical to the reference runtime*, the skips being 35 tests that need a database
carrying the ionisation library and get `RMG-database-plasma` instead. Pinning `database.directory`
at this worktree, which does carry it, turns them all on:

```
$ python -m pytest test/rmgpy/i108ElectronRepresentationMatrixTest.py \
      test/rmgpy/i113IonisationPlacementTest.py \
      test/rmgpy/i116IonisationRegistryTest.py -q -p pin_db
99 passed in 9.15s
```

Those 35 drive the **real** ionisation library through the resolver — including its wrong-declaration
refusals and its reactor acceptance — against the runtime this ticket modified. Nothing about the
forward half moved.

`Cation_R_Recombination` was **not modified, copied, or used as a model.** It is a quarantined legacy
battery-SEI family under a binding ruling and it is not plasma recombination; it appears here only as
a control, which is what the ruling permits. Worth stating plainly given this ticket's subject matter
shares its name.

---

## 8. Can this mechanism reach a steady electron density?

**Formally yes. Physically no. And the reason is structural, not numerical.**

In a closed, quasineutral batch of total lithium `n_tot` (`n_e = n_Li⁺`, `n_Li = n_tot − n_e`), the
mechanism as it now stands is

```
dn_e/dt = k_ion·n_Li·n_e  −  k_RR·n_Li⁺·n_e  =  n_e·(k_ion·n_Li − k_RR·n_e)
```

There **is** a stable fixed point, at `n_Li⁺/n_Li = k_ion/k_RR`. **[I]** But notice what it is a
fixed point *of*: both terms are bilinear in `n_e`, so `n_e` cancels and the balance fixes only the
**ionisation fraction**, not the density. Basis: the algebra above.

**[M]** Where it lands:

| Te / eV | r = k_ion/k_RR | x = ionised fraction at the fixed point |
|---|---|---|
| 0.30 | 6.668e−4 | 0.00067 |
| 0.50 | 1.776 | 0.6397 |
| 0.80 | 191.4 | 0.9948 |
| 1.00 | 993.5 | **0.99899** |
| 1.50 | 1.025e+4 | 0.99990 |
| 2.00 | 3.659e+4 | 0.99997 |

At the campaign's working point the mechanism runs to **99.9 % ionisation of all the lithium**. A
real low-pressure glow sits at fractional ionisation of order 10⁻⁶–10⁻⁴, so this over-predicts by
roughly four orders of magnitude.

**[M]** Adding three-body recombination barely helps, which is the point. With
`k_3b = 1.945e-27·Te_eV^-4.5 cm⁶/s` and `n_tot = 10¹⁴ cm⁻³` at Te = 1 eV:

```
RR only (what ships)   x = 0.998994   n_e = 9.9899e+13 cm^-3
RR + three-body        x = 0.998093   n_e = 9.9809e+13 cm^-3
```

**The missing sink is missing in the order that matters.** Count the dependence on `n_e`:

| process | dependence on n_e | can it balance the source at low n_e? |
|---|---|---|
| ionisation source, `k_ion·n_Li·n_e` | **first order** | — |
| radiative recombination, `k_RR·n_e²` | second order | **no** — falls away faster than the source as n_e → 0 |
| three-body recombination, `k_3b·n_e³` | third order | **no** — worse still |
| **wall loss**, `n_e/τ_wall` | **first order** | **yes** — the only one that can |

**[I]** A first-order source can only be balanced at low electron density by a first-order loss.
Every volume recombination channel is higher order, by the physics of what recombination *is*: it
needs at least two charged partners to meet. So no volume channel — implemented, missing, or yet to
be found — can set the electron density of a low-pressure discharge. That is what wall loss does,
and it is precisely the channel `PlasmaReactor` cannot represent. Basis: the order table above and
the standard low-pressure discharge balance.

**What is missing, named:**

1. **A wall-loss term in `PlasmaReactor`**, or an explicit ruling that M7 models are volume-only and
   their electron densities are upper bounds. This is the one that decides whether the mechanism is
   physical. **Owner: runtime / user.**
2. **A ratified condition set**, principally `Te`. Everything about the *size* of the mismatch moves
   by four orders across the assumed range. **Owner: user.**
3. **An `electrons` field on `TwoTemperaturePlasma`** (§10) plus a sourced three-body coefficient,
   which together would add ~2–29× of volume sink and would not change the answer above.
   **Owner: runtime, then data programme.**

Stating this as the dispatch invites: **the sink half of M7 is done to the limit of what is
implementable, and the mechanism still cannot be trusted for a steady-state electron density.** That
is a finding about the milestone, not a failure of this ticket.

---

## 9. Forward channels paired with their actual physical inverses

The ruling restated as a table. Only **one** row is a true inverse pair; every other pairs with a
process of different molecularity, partner, or driving quantity. **None of the inverses is
implemented, and no rate here is reconstructed from `kf/Keq`.**

| # | Forward | Its actual physical inverse, named | Same elementary channel? | Inverse available? |
|---|---|---|---|---|
| 1 | **Radiative recombination** `Li⁺ + e⁻ => Li + hν` *(implemented)* | **Photoionisation** `Li + hν => Li⁺ + e⁻` | No — photon partner, radiation-field driven | **No.** The reactor has no radiation field |
| 2 | **Electron-impact ionisation** `Li + e⁻ => Li⁺ + 2e⁻` *(on this base)* | **Three-body e–e–ion recombination** `Li⁺ + 2e⁻ => Li + e⁻` | **Yes — the only genuine pair here** | **No.** No shipped fit and not storable (§10) |
| 3 | Three-body e–e–ion recombination | **Electron-impact ionisation** | **Yes** | Yes — it is the shipped forward half |
| 4 | Neutral-stabilised three-body recombination | **Thermal ionisation by neutral collision** `Li + M => Li⁺ + e⁻ + M` | No — heavy-particle collision, Tgas-driven | Negligible (Boltzmann ~10⁻²⁷ at 1000 K); omitted explicitly |
| 5 | Dissociative recombination of Li₂⁺ | **Associative ionisation** `Li + Li* => Li₂⁺ + e⁻` | No — bond breaking vs bound-state formation | No; both unrepresentable |
| 6 | Wall loss by ambipolar diffusion | **Wall desorption / sputtering of Li** | No — a surface source | Not represented |
| 7 | Exothermic charge transfer `X⁺ + Li => X + Li⁺` | **Endothermic charge transfer** `Li⁺ + X => Li + X⁺` | No — 6.7–10.4 eV endothermic | Negligible; omitted explicitly, never via `Keq` |

**The generalisation the ruling protects, stated for this ticket:** the inverse of ionisation is a
recombination process *chosen by conditions*, not a fixed partner. Row 1 is the trap this ticket was
warned about and the reason the implemented channel is deliberately **not** entered as anything's
reverse: radiative recombination is a second-order forward process with a photon, and pairing it
with ionisation would have been wrong twice — wrong partner and wrong order.

**[R]** The reactor enforces the same rule independently: `plasma.pyx` refuses any reversible
electron-temperature-dependent reaction (`NonEquilibriumReverseRateError`) and any reversible
electron-containing reaction, so a reversible entry could not have run regardless. The entry here is
`=>` in the label *and* `reversible = False` in the body; the loader raises if the two disagree
**[R]** (`library.py:518-527`).

---

## 10. Why three-body recombination cannot be stored, independently of the data

This is the finding this ticket adds that was not in the prior art, and it changes what "get the
data" would buy.

**[M]** Which Te-aware rate laws carry a net electron count:

```
TwoTemperaturePlasma   electrons=ABSENT uses_electron_temperature=True  uses_electron_density=ABSENT
BadnellRRArrhenius     electrons=-1     uses_electron_temperature=True  uses_electron_density=True
VoronovEIArrhenius     electrons=1      uses_electron_temperature=True  uses_electron_density=True
_NET_ELECTRON_KINETICS_CLASSES = ('BadnellRRArrhenius', 'VoronovEIArrhenius')
```

`TwoTemperaturePlasma` is the **only** shipped rate law that can express a Te-dependent third-order
coefficient — it is the Kossyi form `A·Te^n·exp(…)` **[R]** (`arrhenius.pyx:320-362`) and it is what
`8.75e-27·Te^-4.5` would be written as. It has no `electrons` attribute.

**[R]** `KineticsLibrary.load` copies an electron count onto the reaction **only if the rate law
declares one** (`library.py:567`, `if hasattr(entry.data, 'electrons')`), and `load_entry` takes no
`electrons` argument (`library.py:602-619`). Its own comment says so: *"Unlike the depository there
is no fallback for kinetics that declare no count of their own: a depository falls back on the
electron count declared by the family that owns it, and a library has no owning family to ask."*

**[M]** So a three-body entry arrives at the balance check claiming zero electrons against a
+1 → 0 charge change, and is rejected before any question about the *number* arises:

```
$ # scratch library, TwoTemperaturePlasma(A=(8.75e-27,'cm^6/(molecule^2*s)'), n=-4.5, ...)
DatabaseError: Reaction [Lip] => [Li] in kinetics library ThreeBodyTrial was not balanced!
Please reformulate.
```

**The consequence.** The representation pincer that `docs/i104-alkali-plasma-cation-source-inventory.md`
§3 identified has been **half** dissolved, not dissolved: it is gone for the two rate laws that were
given an `electrons` field, and it stands unchanged for every other rate law — including the only
one that could carry three-body recombination. **[I]** Obtaining a sourced three-body coefficient
tomorrow would therefore unblock nothing; the runtime change has to come first. Basis: the measured
`DatabaseError` above plus the two code sites.

`test_three_body_recombination_still_cannot_be_stored_at_all` pins this as a **tripwire**: if RMG-Py
ever gives `TwoTemperaturePlasma` an `electrons` field, that test fails, and whoever made the change
is pointed back here to finish the job with a sourced coefficient rather than leaving the channel
half-enabled.

**What would be needed, in order:**

1. An `electrons` field on `TwoTemperaturePlasma` (or a new Te-aware third-order rate law that has
   one), plus its addition to `_NET_ELECTRON_KINETICS_CLASSES`. **Owner: RMG-Py.**
2. A placement declaration `'PlasmaThreeBodyRecombination': (2, 1)` — the schema already supports it;
   the widened two-sided declaration was built for exactly this. **Owner: RMG-Py.**
3. A **sourced, shipped** three-body coefficient. The campaign's adjudicated
   `8.75e-27·Te_eV^-4.5 cm⁶/s` is corroborated to within 4.5× by Stevefelt's collisional term
   (§3.3), but it is an adjudication in a PM repository, not a table in this database.
   **Owner: data programme.** Note §3.3's decomposition first: only the term linear in `n_e` is an
   elementary rate law, and it is *two orders below* the radiative channel at n_e = 10¹².

---

## 11. What changed, and the suites

**Two branches, two commits each half, no merge, no push, no PR.**

### RMG-database — `i119-recombination`, base `fcd87ce6e`

| commit | |
|---|---|
| `9325c2d27` | kinetics: give radiative recombination a library owner |
| `9ee5042d1` | test: pin the recombination path from load to reactor acceptance |
| *(this file)* | docs: report on the electron loss channels |

**[M]** `git diff --stat fcd87ce6e`:

```
 docs/i119-recombination-loss.md                                       | 1039 ++++++++++++++++++
 input/kinetics/libraries/PlasmaRadiativeRecombination/dictionary.txt  |   7 +
 input/kinetics/libraries/PlasmaRadiativeRecombination/reactions.py    | 138 +++
 test/test_plasma_radiative_recombination.py                           | 743 ++++++++++++++++
```

Only additions. **No rate, family, group, tree node, training entry, `rules.py`, `dictionary.txt`,
thermo file, `voronov.yaml` or `badnell.yaml` was modified**, and neither was the
`PlasmaElectronImpactIonization` library on this base, which this ticket consumes read-only as the
forward half.

### RMG-Py — `i119-rr-registry`, forked from `i116-ionisation-registry@18abb2789`

| commit | |
|---|---|
| `92e2d4234` | Let a kinetics library own radiative recombination |

**[M]** `git diff --stat 18abb2789`:

```
 rmgpy/electron_placement.py                        | 39 +++++++++++++++++++---
 test/rmgpy/i108ElectronRepresentationMatrixTest.py | 20 ++++++++----
 test/rmgpy/i113IonisationPlacementTest.py          | 20 ++++++++++----
```

One registry key and the comment beside it; two pre-existing exact-table tests updated for a fourth
owner. **No resolver logic**: `resolve_electron_placement`, `_place_declared_electrons`,
`_NET_ELECTRON_KINETICS_CLASSES` and the guard order are untouched, and `Reaction.is_balanced`,
`rmgpy/electron_balance.py` and `rmgpy/chemkin.pyx` were not opened.

**Nothing was written to any shared checkout** — not `/home/alon/Code/RMG-Py`, not
`/home/alon/Code/RMG-Py-plasma`, not `/home/alon/Code/RMG-database-plasma`, and not
`/home/alon/Code/RMG-Py-i116-ionisation-registry`, which was on `PYTHONPATH` for reading only and was
never built. `/home/alon/Code/RMG-Py-i119-rr-registry` is this ticket's own worktree, created for it.

### Suites

**[M]** Against the **new** runtime, with the declaration shipped rather than injected:

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-i119-rr-registry python -m pytest test/ -q      # RMG-database
4 failed, 107 passed

$ ... python -m pytest test/test_plasma_radiative_recombination.py -q
36 passed
```

**[M]** Against the **reference** runtime, where the test fixture injects the declaration instead —
the same counts, which is the property that lets the two halves merge separately:

```
$ PYTHONPATH=/home/alon/Code/RMG-Py-i116-ionisation-registry python -m pytest test/ -q
4 failed, 107 passed
```

**[M]** RMG-Py side, `database.directory` pinned at this worktree so nothing skips:

```
$ python -m pytest test/rmgpy/i108ElectronRepresentationMatrixTest.py \
      test/rmgpy/i113IonisationPlacementTest.py \
      test/rmgpy/i116IonisationRegistryTest.py -q -p pin_db
99 passed in 9.15s
```

**The four failures are pre-existing and are not this ticket's.** All four are in
`test/test_plasma_electron_attachment.py`, all four concern whether a trained rate resolves through
`'rate rules'` or through the training depository, and they are red **identically against two
different runtimes** (`RMG-Py-i116-ionisation-registry` and `RMG-Py-plasma`) — so they are not a
runtime-pin artefact either. `git status --porcelain` shows **no tracked file modified** on this
branch, so nothing that suite reads has changed; and it fails the same way when run alone, before
any file of this ticket's is imported. Recorded as a durable finding, not fixed: it is the
attachment family's suite and out of scope here.

---

## 12. What this ticket could not reach

Stated plainly, since a green suite is easy to over-read.

- **The placement declaration is not in this repository and cannot be.** It is committed, on
  `i119-rr-registry` (§11) — but that is a *second branch in a second repository*, and the two have
  to merge together or the channel is inert. The test module injects the declaration when the
  runtime does not carry it, so the database suite is green against **both** runtimes; that is
  deliberate, and the corollary is that **a green database suite is not by itself evidence that the
  RMG-Py entry exists.** Same caveat, verbatim, as `docs/i114-ionisation-owner.md` §8. Three RMG-Py
  branches now have to land in order — `i113-placement-widening` → `i116-ionisation-registry` →
  `i119-rr-registry` — before either library resolves in a shared checkout **[M]**
  (`git merge-base --is-ancestor`, each confirmed).
- **A merge conflict is waiting upstream, and it is not this ticket's to resolve. [M]**
  `i114-ionisation-declaration` (`4a5bcba03`) and `i116-ionisation-registry` (`18abb2789`) are
  **parallel** branches — their merge-base is `dde602778`, i113's tip, and neither is an ancestor of
  the other — and **both add the identical key** `'PlasmaElectronImpactIonization': (1, 2)`, both
  editing `rmgpy/electron_placement.py`, `i108ElectronRepresentationMatrixTest.py` and
  `i113IonisationPlacementTest.py`. Whoever integrates the campaign has to land one and rebase or
  drop the other; landing both as-is conflicts. My branch is stacked on `i116`, so it inherits
  whichever way that goes, and a rebase onto a different base would need
  `git rebase --onto`. Flagged rather than acted on: rewriting a branch two other tickets are based
  on is not a call this ticket gets to make.
- **No RMG model was run.** No `rmg.py` job, no enlargement, no integration. `PlasmaReactor` accepted
  the reaction and evaluated it at the right rate; §8's steady state is *analysis of the rate
  equations*, not an integrated trajectory. Whether the network solves, and whether an ionisation or
  recombination channel survives flux filtering and pruning into a converged mechanism, is a
  different question this did not ask.
- **Thermochemistry was stubbed for the reactor demonstration.** A constant-Cp NASA polynomial was
  used for Li, Li⁺ and e⁻. Nothing in the acceptance path depends on the values — the reaction is
  irreversible so no Keq is formed — but this is not a statement that the real thermochemistry works
  in a plasma reactor. The all-zero `electron` thermo entries in `electrocatThermo.py`,
  `electrocatLiThermo.py` and `computationalLithiumElectrode.py` remain a trap for anyone who runs
  an equilibrium check **[D]**.
- **Only the +1 → neutral stage was considered.** The 306 multiply charged stages in the table were
  not represented, tested, or costed.
- **The wall-loss estimate rests on an order-of-magnitude mobility and an invented geometry.**
  `μ₀(Li⁺ in N₂) ≈ 4 cm²/(V·s)` is not a measured value for this system, and R = 1 cm / L = 10 cm is
  a stand-in for a reactor nobody has specified. The 19× and 1877× margins are therefore
  factor-of-a-few numbers, not precise ones. What they establish robustly is the *ranking* and the
  *order* argument in §8, neither of which depends on the coefficient.
- **No literature search reached a three-body coefficient validated above Te = 4000 K for Li⁺**,
  which is what Stevefelt's stated range demands and the working point exceeds by ~3×.
- **No Li₂⁺ dissociative-recombination data was found**, and the search was not exhaustive — an MQDT
  treatment may exist in the early-universe-chemistry literature. Moot while the ion is
  unbuildable, but it would stop being moot if that were fixed.
- **Dere 2007's Li normalisation was still not read**, so the factor-≈2.2 uncertainty on the
  *ionisation* A-factor that `docs/i104-alkali-plasma-cation-source-inventory.md` §4.1 flagged
  stands unresolved. It propagates directly into §8's `r = k_ion/k_RR` and hence into the fixed
  point — though not enough to change the conclusion, since a factor of 2 against a factor of 1000
  moves 0.99899 to 0.99799.
- **Only lithium.** He⁺, N⁺, O⁺ and Ne⁺ are buildable and in the table; none has monatomic
  thermochemistry here. The channel-by-channel inventory was not repeated for them, though every
  structural finding in §8 and §10 transfers unchanged — they are about the electron, not about
  lithium.
- **The four pre-existing attachment-suite failures were diagnosed as pre-existing, not diagnosed as
  to cause.** Establishing that they predate this branch and survive a runtime swap is as far as
  this ticket went.

---

## 13. Durable findings

Eleven, in descending order of consequence. Findings 9–11 are about the machinery rather than the
chemistry, and each cost a real detour here.

1. **No volume recombination channel can set an electron density.** The source is first order in
   `n_e` and every recombination channel is second order or higher, so at low `n_e` the source
   always wins; only a first-order loss — wall/transport — can balance it. This is structural, holds
   at every condition, and means the reactor's missing wall-loss term is not a refinement but the
   thing that sets the answer. §8.
2. **Radiative recombination is implemented, and it is ~1000× weaker than the source at Te = 1 eV.**
   The two-channel mechanism's fixed point is 99.9 % ionisation of the lithium, roughly four orders
   above a real glow discharge. §3.2, §8.
3. **Three-body recombination cannot be *stored*, not merely un-sourced.**
   `TwoTemperaturePlasma` carries no `electrons` field, so a three-body library entry fails the
   loader's balance check before any question of data arises. Obtaining the coefficient would unblock
   nothing without a runtime change first. Measured. §10.
4. **The i104 representation pincer is half dissolved, not dissolved.** It is gone for the two rate
   laws given an `electrons` field (Voronov, Badnell) and stands unchanged for every other — which
   is every channel not yet implemented. §10.
5. **The two shipped atomic tables are asymmetric, and the asymmetry lands on the benchmark bath
   gas.** Ar can be ionised from `voronov.yaml` and cannot be radiatively recombined from
   `badnell.yaml` at all; five elements (Al, Si, Ar, K, Ca) are ionisable-but-not-recombinable. §4.3.
6. **Radiative-recombination coverage narrows 318 → 12 → 6 → 1, and the bound is thermochemistry.**
   The same arithmetic and the same single species as the ionisation table, for the same reason: only
   Li⁺ has free-monatomic-cation thermochemistry in this database. §4.2.
7. **Only the term linear in `n_e` of a collisional–radiative coefficient is an elementary rate law.**
   Stevefelt's dominant collisional term goes as `n_e^0.37` and has no elementary reaction to be the
   rate law of; the part that *is* storable is two orders below the radiative channel at
   n_e = 10¹². So even a perfect three-body entry would carry less sink than the α_cr/α_RR ratio
   suggests. §3.3.
8. **Four attachment-suite tests are pre-existing red**, identically against three runtimes now
   (`RMG-Py-plasma`, `i116-ionisation-registry`, `i119-rr-registry`), with no tracked file modified
   on this branch. They concern rate-rule versus training-depository attribution and are unrelated
   to this ticket. §11.
9. **`make build` alone cannot build a fresh RMG-Py worktree.** `rmgpy/solver/settings.pxi` is
   generated and gitignored, and only the `check` / install paths write it — so a worktree created
   from a branch dies on `InternalError: 'settings.pxi' not found`. `python utilities.py check-pydas`
   generates it alone, without the `pip install -e .` that bare `make` would run and that would
   repoint the shared conda environment. The standing advice "`make build`, never bare `make`" is
   necessary and, on a new worktree, not sufficient. §1.
10. **Verify a build by its artefacts, not by a reported exit code.** A `( ... make ... ); echo $?`
    wrapper reported success for the failed build above, because `$?` had by then become the
    `echo`'s. The failure surfaced only from `find . -name '*.so' | wc -l` returning 0 against the
    reference's 104. §1.
11. **`i114-ionisation-declaration` and `i116-ionisation-registry` are parallel branches that add the
    same registry key**, from a shared merge-base at i113's tip, touching the same three files. They
    cannot both land as-is. Not this ticket's to fix, and its own branch is stacked on `i116`. §12.

Also worth keeping: **using Stevefelt's full coefficient alongside the entry added here
double-counts radiative recombination**, because Stevefelt's first term *is* the radiative
contribution — and that warning now binds a shipped entry rather than a hypothetical one. §3.3.
