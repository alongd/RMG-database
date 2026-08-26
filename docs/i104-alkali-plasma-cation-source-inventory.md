# I-104 — The alkali-plasma cation source and loss network

**Report-first. No rate, family, group, tree node, training entry, library entry or thermo file was
edited.** The only change on this branch is this file; the `git diff` proving it is in §9.

Evidence labels on every claim: **[R]** read from code (file:line), **[D]** read from this
database (file, entry), **[L]** literature (full citation), **[I]** inference, with its basis
named. **UNKNOWN** marks a field that could not be established, always with what would settle it.

---

## 0. The condition set, and why the answer is *no*

### 0.1 The gap is real, and slightly narrower than the dispatch states

The dispatch says the intended M7 composition, pressure, `Tgas`, `Te`, EEDF assumption and
residence-time range "are not recorded anywhere in this project." I checked before building on it.

**Confirmed for M7.** `STRATEGY.md:53` defines M7 as "alkali mechanism" and names no condition.
`contracts/I-099_cation-marcus-quarantine.md` §7 instructs the reader to "start from the intended
M7 composition, pressure, `Tgas`, `Te`, EEDF assumption and residence-time range" without supplying
one. `LEDGER.md:6068`, the I-104 entry itself, repeats the list as an input it does not provide.
**No ratified M7 condition set exists** [D].

**But the campaign is not silent, and that matters.** Three anchors exist and were used to build the
assumption below rather than inventing one:

| Anchor | Value | Source |
|---|---|---|
| Benchmark pressure and gas temperature | **5 torr, room temperature** | `LEDGER.md:1508`, I-004 Ar cold-validation intent [D] |
| Benchmark pressure sweep | **0.05 – 1.0 torr** partial pressure | `LEDGER.md:1542`, I-007 [D] |
| Working electron temperature | **Te = 1 eV** | `INSIGHTS.md:939-957`, the adjudicated three-body coefficient [D] |

That is a low-pressure, cold-gas, ~1 eV glow-discharge working point. It is what this campaign has
actually been computing against.

### 0.2 The condition set I assumed

**Everything below is scoped to this set. It is a proposal, not a ratification — adopting it is the
user's call.**

| Quantity | Assumed | Justification |
|---|---|---|
| Composition | Ar or N₂ bath + **trace Li (10⁻⁴ – 10⁻² mole fraction)**, neutral at t = 0 | The campaign's benchmark bath is Ar (I-004/I-007) [D]. Trace Li because Li's ionisation energy, 5.392 eV, is 6–10 eV below every plausible bath gas, so even trace Li dominates the ion balance (§4.7) |
| Pressure | **0.05 – 5 torr**, centred on 5 torr | I-004 and I-007 directly [D] |
| `Tgas` | **300 – 1000 K** | I-004's "room temperature"; extended to 1000 K because the lithium NASA polynomials in this database are valid to 3000 K [D] `LithiumPrimaryThermo.py`, so there is headroom, and a glow discharge is not isothermal with its walls |
| `Te` | **0.5 – 2 eV**, centred on 1 eV | `INSIGHTS.md:939` [D]; also the standard low-pressure glow range |
| EEDF | **Maxwellian** — and this is *not* a free choice | `ElectronCollisionPlasma.integrate_rate_coefficient` integrates σ(E) against a Maxwellian and nothing else [R] `arrhenius.pyx:648-694`; `VoronovEIArrhenius` and `BadnellRRArrhenius` are Maxwellian-averaged fits by construction [L]. The runtime has **no** non-Maxwellian EEDF path |
| E/N | **not represented at all** | `PlasmaReactor` takes `T`, `P`, `Te` and nothing else [R] `plasma.pyx:110`. There is no field, no E/N, no Boltzmann solver. Any channel whose rate is naturally keyed on E/N must be re-expressed in `Te` before it can be stored |
| `n_e` (initial) | **10¹⁰ – 10¹⁴ cm⁻³**, centred on 10¹² | Standard glow range; the reactor requires a strictly positive explicit value and supplies no default [R] `plasma.pyx:400-408` |
| Residence time | **UNKNOWN.** Assumed integration horizon 10⁻⁵ – 10⁻¹ s | Nothing in the project names one. `PlasmaReactor` is a **batch** reactor with no flow term [R] `plasma.pyx:30-44`, so "residence time" can only mean the integration horizon. **What would settle it:** a ratified M7 reactor specification |

### 0.3 Sensitivity — which findings survive any plausible condition set

| Finding | Robust or sensitive |
|---|---|
| Electron-impact ionisation of atomic Li is the **only** cation source from a neutral alkali feed that has both usable data and a representable shape | **Robust.** True at every Te, pressure and bath in the range, and for any alkali |
| Li is a **charge sink**: every bath-gas molecular ion transfers its charge to Li at ~the Langevin rate | **Robust.** Driven by a 6.7–10.4 eV ionisation-energy gap; no plausible condition closes it |
| Neither ionisation nor recombination can currently be **stored and reach the reactor** (§3) | **Robust.** A property of the code, wholly independent of conditions |
| Three-body (collisional-radiative) recombination beats radiative recombination | **Robust in ranking, sensitive in size.** 2.2× at n_e = 10¹⁰, 110× at 10¹⁴ (§4.3) |
| **Wall loss outruns volume ionisation** | **SENSITIVE — and this is the one to ratify first.** At 5 torr, R = 1 cm: τ_wall ≈ 2.5×10⁻⁴ s vs τ_ion ≈ 4.7×10⁻³ s, a 20× margin. At 1 atm: τ_wall ≈ 3.8×10⁻² s and the ranking inverts (§4.9) |
| Voronov's Li fit is used **below its stated lower bound** at Te < 1 eV | **Sensitive.** Disappears if `Te` is ratified at ≥ 1 eV; binding if the ratified range reaches 0.5 eV |
| Stevefelt's CRR formula is used **above its stated upper bound** | **Sensitive**, same way, in the opposite direction (§4.3) |

### 0.4 The answer, in six lines

- **Can a defensible cation source be assembled from the literature at the assumed conditions?
  No — but not for the reason the ticket anticipated.**
- The **data are already here**: `input/kinetics/voronov.yaml` carries Voronov's Li electron-impact
  ionisation fit and `input/kinetics/badnell.yaml` carries Badnell's Li⁺ radiative-recombination
  fit, both sourced, both loading, both evaluating correctly against the pin (§2, §4).
- What is missing is a **representation**. `Reaction.is_balanced()` counts the free-electron
  pseudo-species as a conserved chemical element, so **every** reaction that changes the electron
  count is refused by the kinetics-library loader; the metadata alternative is refused by the
  reactor. Measured both ways in §3. It is a pincer with no gap.
- The gap is **one function** — `rmgpy/reaction.py:1669-1731` in `RMG-Py-plasma`, not a database
  change and not in this ticket's scope. With it fixed, §3.4 shows the reactor already **accepts**
  the explicit form carrying real Voronov and Badnell kinetics.
- Two Li channels are additionally blocked at the molecule layer: **`Li₂⁺` cannot be built at all**
  (no atom type for a bonded Li⁺), which removes dissociative recombination and associative
  ionisation independently of any data (§4.5, §4.6).
- **Wall loss is the largest single electron sink at the campaign's own anchor conditions and the
  reactor cannot represent it.** Ratifying the conditions is what decides whether that is
  acceptable (§4.9).

Eleven durable findings, six of them defects, are in §10.

---

## 1. Environment and pin

| Role | Path | State |
|---|---|---|
| Runtime (imports) | `/home/alon/Code/RMG-Py-plasma` | branch `plasma`, unmodified, **not rebuilt** |
| Data under inventory | `/home/alon/Code/RMG-database-i104-alkali` | branch `i104-alkali-plasma`, base `fb3c13c60` |

```
$ conda activate rmg_env
$ export PYTHONPATH=/home/alon/Code/RMG-Py-plasma:$PYTHONPATH
$ python -c "import rmgpy; print(rmgpy.__file__)"
/home/alon/Code/RMG-Py-plasma/rmgpy/__init__.py
```

Every probe printed `PIN rmgpy:` first and `PIN-AFTER rmgpy:` last; both read
`/home/alon/Code/RMG-Py-plasma/rmgpy` in all four. `/home/alon/Code/RMG-Py` (branch `polymer`) was
never on the path. Nothing was built — no bare `make`, no `make build`.

Four probes, stdout and stderr persisted, all outside every tracked tree, under
`/tmp/claude-1000/-home-alon-Code-RMG-database-i104-alkali/930af96a-.../scratchpad/`: `probe1`
(rate magnitudes, Langevin, Saha, diffusion), `probe2` (library round-trip), `probe3` (balance and
atom types), `probe4` (family resolver and reactor validation). Being scratch they are not durable;
the output quoted here is the durable record.

---

## 2. What this repository and runtime already contain

This is the part of the answer that was not expected, so it is stated before the inventory.

### 2.1 Two sourced atomic-data tables, already committed

| File | Source string, as stored | Li content |
|---|---|---|
| `input/kinetics/voronov.yaml` | `Voronov, G.S. (1997) Atom. Data Nucl. Data Tables 65, 1, Electron-impact ionization rate coefficient fits, Z=1–28` [D] | `Z: 3, element: Li` with three stages; `N: 3` is **neutral Li**: `dE: 5.4` eV, `P: 0`, `A: 1.39e-7` cm³/(molecule·s), `X: 0.438`, `K: 0.41`, `Tmin: 1` eV, `Tmax: 20e3` eV [D] |
| `input/kinetics/badnell.yaml` | `Badnell, N.R. (2006) ApJS 167, 334, Radiative Recombination Data for Modeling Dynamic Finite-Density Plasmas` [D]; `notes: Z is the nuclear charge, N is the number of electrons prior to recombination` [D] | `Z: 3` with `N: 0,1,2`; **`N: 2` is Li⁺ + e⁻ → Li**: `A: 8.7e-12` cm³/(molecule·s), `B: 0.364`, `T0: 147.0` K, `T1: 7.153e6` K, `C: 0.1508`, `T2: 7.154e5` K [D] |

Full citations: Voronov, G. S., "A practical fit formula for ionization rate coefficients of atoms
and ions by electron impact: Z = 1–28", *At. Data Nucl. Data Tables* **65** (1997) 1–35,
doi:10.1006/adnd.1997.0732 [L]. Badnell, N. R., "Radiative recombination data for modeling dynamic
finite-density plasmas", *Astrophys. J. Suppl. Ser.* **167** (2006) 334–342, doi:10.1086/508465 [L].

Both load and evaluate against the pin. Measured, `probe1`:

```
Voronov Li(N=3): VoronovEIArrhenius(A=(8.37078e+16,'cm^3/(mol*s)'), P=0, X=0.438, K=0.41,
                 dE=(5.4,'eV'), Tmin=(11604.5,'K'), Tmax=(2.3209e+08,'K'))
Badnell Li+(N=2): BadnellRRArrhenius(A=(8.7e-12,'cm^3/(molecule*s)'), B=0.364, T0=(147,'K'),
                 T1=(7.153e+06,'K'), C=0.1508, T2=(715400,'K'), Tmin=(10,'K'), Tmax=(1e+07,'K'))
```

### 2.2 The four electron-temperature-aware kinetics classes

All in `rmgpy/kinetics/arrhenius.pyx`, all setting `uses_electron_temperature = True` [R]:

| Class | Line | Rate law | Channel it fits |
|---|---|---|---|
| `TwoTemperaturePlasma` | 320 | `A·Te^n·exp(−Ea_g/RT)·exp(Ea_e(Te−T)/(R·T·Te))`, Kossyi form [R] `arrhenius.pyx:326-334` | Three-body recombination; any two-temperature channel |
| `ElectronCollisionPlasma` | 570 | `⟨σv⟩(Te)` by trapezoidal integration of tabulated σ(E) over a Maxwellian [R] `arrhenius.pyx:648-694` | Any channel with a published cross section |
| `BadnellRRArrhenius` | 816 | Badnell RR fit; sets `uses_electron_density = True` as well [R] `arrhenius.pyx:857-858` | Radiative recombination |
| `VoronovEIArrhenius` | 1411 | Voronov fit; also sets `uses_electron_density = True` [R] `arrhenius.pyx:1458-1459` | Electron-impact ionisation |

All four are in the kinetics-library loading namespace [R] `data/kinetics/database.py:101-104`, so a
library `entry()` can name them directly. Verified by loading a synthetic library, `probe2`.

### 2.3 The reactor, and what it will and will not accept

`PlasmaReactor` is a **homogeneous, isobaric, batch, two-temperature** reactor with the electron
carried explicitly in the state vector, EOS `PV = R(N_heavy·T_gas + N_e·T_e)` [R] `plasma.pyx:28-44`.

Requirements that bind this inventory, each from named code:

| # | Requirement | Enforcement |
|---|---|---|
| 1 | Scalar `T`, `P`, `Te` only; no ranged conditions | [R] `plasma.pyx:113-117` |
| 2 | `Te` explicit, finite, strictly positive; **no fallback from Te to Tgas** | [R] `plasma.pyx:118-136` |
| 3 | Exactly one electron pseudo-species in the core, with a strictly positive initial amount | [R] `plasma.pyx:356-406` |
| 4 | Between 1 and 3 reactants and 1 and 3 products | [R] `plasma.pyx:431-435` |
| 5 | **No pressure-dependent kinetics** — so a three-body process must be written with the third body explicit, never as `ThirdBody`/`Lindemann`/`Troe` | [R] `plasma.pyx:449-453` |
| 6 | **`rxn.electrons != 0` is rejected outright** — metadata "cannot distinguish incident-electron order from net electron production" | [R] `plasma.pyx:461-469` |
| 7 | `uses_electron_density` kinetics must carry an explicit electron **among the reactants** | [R] `plasma.pyx:479-486` |
| 8 | `uses_electron_temperature` kinetics must expose `get_rate_coefficient_two_temp` or `get_rate_coefficient_electron_temp` | [R] `plasma.pyx:487-500` |
| 9 | A Te-dependent reaction **must be irreversible** — `kf(Tgas,Te)/Keq(Tgas)` mixes two thermal closures and `Keq(Te)` misprices heavy-species thermochemistry. `Te == Tgas` does not bypass it | [R] `plasma.pyx:502-511` |
| 10 | Any reversible electron-containing reaction is refused even without Te-dependence: `Keq(Tgas)` "would price the electron's thermochemistry at the gas temperature" | [R] `plasma.pyx:536-542` |
| 11 | No constant species — freezing the electron "would silently break charge conservation" | [R] `plasma.pyx:136-140` |

Requirements 9 and 10 are the reactor's own enforcement of the ruling this ticket's constraint 2
cites. They are why every channel below is written **one-way**.

### 2.4 The species side

- Neutral Li exists: `[Li]`, `multiplicity 2 / 1 Li u1 p0 c0`, NASA valid 10–3000 K [D]
  `LithiumPrimaryThermo.py:21-33`.
- Li⁺ exists as `1 Li u0 p0 c+1`, labelled `[Lip]` in kinetics dictionaries [D]
  `LithiumPrimaryChargedKinetics/dictionary.txt:1`; the `[Lip]` spelling is forced, because the
  library label parser splits on `'+'` [R] `library.py:553,559` and a label containing `Li+` breaks
  (measured, `probe2`).
- The electron builds from `1 e u0 p0 c-1`; element `e` has atomic number −1 [R]
  `molecule/element.py:178` and is in `element_list` (measured, `probe3`).
- **Do not adopt the existing `electron` thermo entry.** All three copies —
  `electrocatThermo.py:39`, `electrocatLiThermo.py:39`, `computationalLithiumElectrode.py:39` — are
  all-zero NASA polynomials, i.e. H = S = Cp = 0 at every T [D]. That is the computational-hydrogen-
  electrode convention, correct there and wrong for a free gas-phase electron. Requirement 9/10
  keeps it out of every *rate*, but it enters any equilibrium check the authors will want to run.
  (Recorded already in the reverse-direction census; repeated because it binds here too.)
- **`Li₂⁺` does not exist and cannot be built** — see §4.5.

---

## 3. The representation pincer — the central finding

This section is the reason the answer in §0.4 is *no*. Every claim in it was measured.

### 3.1 `is_balanced()` treats the free electron as a conserved element

`Reaction.is_balanced()` accumulates a per-element count over both sides, including element `e`
carried by the electron pseudo-species, and returns `False` on any mismatch [R]
`reaction.py:1684-1723`. Measured over every plasma reaction shape (`probe3`):

```
  EI  explicit   [Li] + e => [Lip] + e + e     electrons=+0  is_balanced=False
  EI  half       [Li] => [Lip] + e             electrons=+0  is_balanced=False
  EI  metadata   [Li] => [Lip]  (electrons=+1) electrons=+1  is_balanced=True
  EI  metadata0  [Li] => [Lip]  (electrons=0)  electrons=+0  is_balanced=True
  RR  explicit   [Lip] + e => [Li]             electrons=+0  is_balanced=False
  RR  metadata   [Lip] => [Li]  (electrons=-1) electrons=-1  is_balanced=True
  3b  e-e-ion    [Lip] + e + e => [Li] + e     electrons=+0  is_balanced=False
  3b  neutral M  [Lip] + e + Ar => [Li] + Ar   electrons=+0  is_balanced=False
  CT  ion-atom   [Lip] + Ar => [Li] + Ar       electrons=+0  is_balanced=True
```

Every electron-*changing* reaction written with an explicit electron is refused. Only the
charge-conserving heavy-particle shapes and the metadata forms pass.

### 3.2 …so the kinetics-library loader cannot store one

`KineticsLibrary.load` calls `rxn.is_balanced()` and raises on failure [R] `library.py:566-568`.
Measured directly, loading a synthetic library through `KineticsDatabase.load_libraries` (`probe2`):

```
rmgpy.exceptions.DatabaseError: Reaction [Li] + e => [Lip] + e + e in kinetics library
TestPlasma was not balanced! Please reformulate.
```

And there is no metadata escape on the library route: `KineticsLibrary.load_entry` has **no
`electrons` keyword** [R] `library.py:584-601`. A library entry can carry the electron only as an
explicit species — the one form `is_balanced()` refuses.

### 3.3 …and the metadata form cannot reach the reactor

Three independent refusals, all measured (`probe4`):

```
resolve_electron_placement -> ElectronPlacementError: Family 'Plasma_Electron_Impact_Ionization'
  has no electron-placement declaration (reaction [Li] => [Li+], electrons=1); refusing to infer
  electron placement from the net electron count.

(declared family, ionisation shape) -> ElectronPlacementError: Reaction [Li] => [Li+] carries
  electrons=1, which is ionization-shaped (net electron production); family
  'Plasma_Electron_Attachment' declares single-electron consumption (net -1). No placement view
  is defined for this shape in this increment.

metadata EI -> PlasmaStateError: reaction [Li] => [Li+] carries a metadata-only electron count
  (electrons=1); this representation cannot distinguish incident-electron order from net electron
  production, so it is unsupported here.
```

`FAMILY_ELECTRON_PLACEMENT` holds exactly two entries, both `('reactants', 1)` [R]
`electron_placement.py:106-109`, and its own docstring states the limit plainly: *"Ionization- and
excitation-type families (net electron production, or none) must gain their own declarations and
their own validation before they can resolve"* [R] `electron_placement.py:103-105`.

Note also that families never produce an explicit electron at all: `_create_reaction` builds every
`TemplateReaction` with `electrons=self.electrons` metadata [R] `family.py:1751-1772`.

### 3.4 The shape the reactor actually wants is the one that cannot be stored

The same explicit reactions, carrying real Voronov and Badnell kinetics, put through
`PlasmaReactor._validate_reactions` at 5 torr / 300 K / Te = 1 eV (`probe4`):

```
  explicit EI ACCEPTED by PlasmaReactor; is_balanced = False
  explicit RR ACCEPTED by PlasmaReactor; is_balanced = False
```

**The reactor accepts exactly what the database refuses to store.** That is the whole gap, and it
is one function wide.

### 3.5 A defect found on the way: the charge check is dead code

`is_balanced()` accumulates `reactants_net_charge` and `products_net_charge`, adjusts them by
`self.electrons`, and then `return True` **without ever comparing them** [R]
`reaction.py:1682-1731`. Measured (`probe3`):

```
  [Li] => [Lip] with electrons=0 : is_balanced = True   <- reactant charge 0, product charge +1
```

So the check refuses correct chemistry (§3.1) and passes a flat charge violation. Both halves are
the same bug: element counting stands where charge balancing belongs.

---

## 4. The channel inventory

Every channel is written **one-way**, per requirements 9 and 10 of §2.3 and the ruling this ticket
cites. "Physical inverse" names the process that actually runs the other way — never "the forward
backwards".

Field key, per the dispatch: **eq** elementary equation · **e-order** incident-electron kinetic
order · **net e** net electron stoichiometry · **mol** molecularity · **deps** Te / Tgas / P / E-N /
EEDF · **prov** rate or cross-section provenance · **states** product-state resolution · **applic**
applicability to §0.2 · **unc** uncertainty · **route** family-generable or exact library reaction.

### 4.1 Channel 1 — Electron-impact ionisation of neutral Li  ✅ *the cation source*

| Field | Value |
|---|---|
| **eq** | `Li + e⁻ => Li⁺ + e⁻ + e⁻` |
| **e-order** | **1** — one incident electron among the reactants |
| **net e** | **+1** |
| **mol** | 2 reactants → 3 products (at the reactor's 3-participant ceiling, req. 4) |
| **deps** | **Te: yes.** Tgas: **no**. P: **no**. E/N: **no**. EEDF: **Maxwellian, structurally** — the Voronov form is a Maxwellian average and the runtime offers no alternative |
| **prov** | Voronov 1997, doi:10.1006/adnd.1997.0732 [L], **already in this repository** as `voronov.yaml` `Z:3, N:3` [D]. Voronov's own Li input is McFarland, R. H. & Kinney, J. D., "Absolute cross sections of lithium and other alkali metal atoms for ionization by electrons", *Phys. Rev.* **137** (1965) A1058, doi:10.1103/PhysRev.137.A1058 [L], and Jalin, R., Hagemann, R. & Botter, R., "Absolute electron impact ionization cross sections of Li in the energy range from 100 to 2000 eV", *J. Chem. Phys.* **59** (1973) 952, doi:10.1063/1.1680119 [L]. Lotz, W., "Electron-impact ionization cross-sections and ionization rate coefficients for atoms and ions", *Astrophys. J. Suppl.* **14** (1967) 207, doi:10.1086/190154 [L] normalised Brink's relative data to McFarland & Kinney |
| **states** | **None.** Ground-state Li(2²S) → ground-state Li⁺(¹S). No excited state, no stepwise route via Li(2p), no inner-shell channel resolved. This is a real accuracy limit at the low end of the assumed Te range — see **unc** |
| **applic** | **Partly outside range at the low end.** The stored fit declares `Tmin = 1 eV` (11604.5 K, measured) [D]. The assumed Te range reaches **0.5 eV**, i.e. **below** it. Above 1 eV the fit is inside its range everywhere the assumption goes |
| **unc** | Three layers, the second material. (a) *Fit vs its own input:* Voronov quotes ≲10 % [L]. (b) **Its input is disputed by a factor ≈2.2.** Dere, K. P., "Ionization rate coefficients for the elements hydrogen through zinc", *Astron. Astrophys.* **466** (2007) 771–792, doi:10.1051/0004-6361:20066728 [L] reportedly divided the McFarland & Kinney measurements by ≈2.2 to reconcile them with high-energy data before refitting — so the underlying Li absolute scale is uncertain at the factor-2 level, not the 10 % level. *Honest limit on this claim:* the factor comes from a secondary summary of Dere 2007; the paper's Li section was not read directly (the publisher returned HTTP 403), so treat "≈2.2" as indicative. **UNKNOWN:** which normalisation Voronov's Li entry follows. **What would settle it:** reading Voronov 1997 §Li and Dere 2007 §Li directly (§11). (c) *Missing physics:* stepwise ionisation via Li(2p) has a 3.54 eV second step against the 5.39 eV direct threshold, so at Te ≤ 1 eV the true ionisation rate **exceeds** ground-state-only Voronov, by an amount this inventory did not quantify |
| **route** | **Exact library reaction.** Two independent reasons. *Chemistry:* the rate is set by one atom's ionisation threshold and full cross-section shape — there is no group-additivity trend to interpolate along, which is precisely the argument `Plasma_Electron_Attachment/groups.py:29-35` already makes for attachment [D]. *Code:* no family route exists at all, `resolve_electron_placement` refusing ionisation shapes by name [R] (§3.3) |
| **Physical inverse** | **Three-body electron–electron–ion recombination** (§4.3), `Li⁺ + e⁻ + e⁻ => Li + e⁻`. This is the genuine microscopic inverse — same participants, reversed. It is **not** radiative recombination, which is the inverse of photoionisation instead (§4.2) |

Measured k(Te), `probe1`, converted to cm³/s:

| Te / eV | k_EI(Li) / cm³ s⁻¹ | τ_ion at n_e = 10¹² cm⁻³ |
|---|---|---|
| 0.30 | 3.756×10⁻¹⁶ | 2.66×10³ s |
| 0.50 | 6.694×10⁻¹³ | 1.49 s |
| 0.80 | 4.954×10⁻¹¹ | 2.02×10⁻² s |
| 1.00 | 2.147×10⁻¹⁰ | 4.66×10⁻³ s |
| 1.50 | 1.590×10⁻⁹ | 6.29×10⁻⁴ s |
| 2.00 | 4.473×10⁻⁹ | 2.24×10⁻⁴ s |

The six orders of magnitude between 0.3 and 1.0 eV are why §0.3 flags the `Te` ratification as
load-bearing: at 0.5 eV nothing ionises on any plausible horizon; at 1.5 eV ionisation is
sub-millisecond.

### 4.2 Channel 2 — Radiative recombination of Li⁺  ✅

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ => Li` (+ hν, not a species) |
| **e-order** | **1** |
| **net e** | **−1** |
| **mol** | 2 → 1 |
| **deps** | **Te: yes.** Tgas: no. P: no. E/N: no. EEDF: Maxwellian, structurally |
| **prov** | Badnell 2006, doi:10.1086/508465 [L], **already in this repository** as `badnell.yaml` `Z:3, N:2` [D] |
| **states** | **Total RR only** — summed over all final n, l. Not level-resolved, and the emitted photon is not represented. Writing the product as ground-state Li is an approximation that ignores the radiative cascade |
| **applic** | **Fully inside range.** Stored `Tmin = 10 K`, `Tmax = 10⁷ K` (measured) — wider than any condition considered |
| **unc** | Badnell's fits reproduce his own calculations to ≲5 %; RR theory for a two-electron target is itself good to ~10–20 % [L]+[I]. Small compared with every other uncertainty here |
| **route** | **Exact library reaction**, same two reasons as §4.1 |
| **Physical inverse** | **Photoionisation**, `Li + hν => Li⁺ + e⁻`. Different collision partner (a photon, not an electron), different driving quantity (radiation field, not Te), different molecularity. **The reactor has no radiation field** [R] `plasma.pyx:110`, so this inverse **cannot be represented at all** and RR must stand as a strictly one-way sink. That is physically defensible for an optically thin cold plasma and must be *stated*, not assumed |

Measured α_RR(Te), `probe1`: 5.63×10⁻¹³ cm³/s at 0.3 eV, 2.16×10⁻¹³ at 1.0 eV, 1.22×10⁻¹³ at
2.0 eV — a weak Te^(−0.6)-ish decline, three orders below the ionisation rate at 1 eV.

### 4.3 Channel 3 — Three-body electron–electron–ion recombination  ⚠️ *data outside its range*

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ + e⁻ => Li + e⁻` |
| **e-order** | **2** — two incident electrons; the second is the stabilising third body |
| **net e** | **−1** |
| **mol** | 3 → 2 (exactly at the reactor's ceiling, req. 4) |
| **deps** | **Te: strongly**, ≈ Te^(−4.5). n_e: through the reaction order, not the coefficient — which is the correct way to write it and why the third body must be explicit. Tgas: no. P: only through n_e. E/N: no. EEDF: Maxwellian |
| **prov** | Stevefelt, J., Boulmer, J. & Delpech, J.-F., "Collisional-radiative recombination in cold plasmas", *Phys. Rev. A* **12** (1975) 1246–1251, doi:10.1103/PhysRevA.12.1246 [L], resting on Mansbach, P. & Keck, J., "Monte Carlo trajectory calculations of atomic excitation and ionization by thermal electrons", *Phys. Rev.* **181** (1969) 275, doi:10.1103/PhysRev.181.275 [L]. **Not in this repository.** The Stevefelt coefficient is `α_cr = 1.55e-10·Te^-0.63 + 6.0e-9·Te^-2.18·n_e^0.37 + 3.8e-9·Te^-4.5·n_e` cm³/s, Te in K, n_e in cm⁻³ |
| **states** | **Unresolved, and this matters.** CRR captures into high Rydberg levels which then cascade collisionally and radiatively to the ground state. There is no single product state; writing `=> Li` compresses a ladder into one step. Faithful representation would need Li Rydberg manifolds, which RMG cannot express |
| **applic** | **Above its stated range.** Stevefelt *et al.* derived the formula for **Te < 4000 K** [L]; the assumed working point Te = 1 eV is **11 605 K**, ~3× above it. The functional form is standard practice well beyond that range, but the extrapolation is an assumption, not a validation. **UNKNOWN:** a CRR coefficient validated at 1–2 eV for Li⁺. **What would settle it:** a Li-specific collisional-radiative model, or an afterglow measurement in a Li plasma |
| **unc** | Factor ~2, and independently cross-checked here. Re-expressing Stevefelt's collisional term in eV gives **1.95×10⁻²⁷ cm⁶/s at Te = 1 eV**, against the campaign's own adjudicated value `8.75e-27·Te_eV^-4.5` = **8.75×10⁻²⁷** [D] `INSIGHTS.md:939-957` — a factor 4.5. Same class, same scaling exponent, ordinary spread between published CRR treatments. The campaign's value is **not** contradicted |
| **route** | **Exact library reaction.** Additionally: it must be written with the second electron explicit, **never** as `ThirdBody`/`Lindemann`/`Troe`, because `PlasmaReactor` refuses pressure-dependent kinetics outright [R] `plasma.pyx:449-453` |
| **Physical inverse** | **Electron-impact ionisation** (§4.1). Genuine inverse pair — and the *only* genuine forward/inverse pair in this inventory |

**Warning against double counting.** Stevefelt's *first* term, `1.55e-10·Te^-0.63`, **is** the
radiative-recombination contribution. Storing the full Stevefelt coefficient alongside the Badnell
RR entry of §4.2 counts radiative recombination twice. Use Stevefelt's collisional terms only, or
Stevefelt alone — not both in full [L]+[I].

Measured ranking against §4.2, `probe1`, at 5 torr / 300 K:

| n_e / cm⁻³ | α_CRR/α_RR at Te = 0.5 eV | at 1.0 eV | at 2.0 eV |
|---|---|---|---|
| 10¹⁰ | 2.25 | 2.16 | 2.33 |
| 10¹² | 4.60 | 3.03 | 2.66 |
| 10¹⁴ | 28.5 | 8.66 | 4.58 |

**Three-body recombination beats radiative recombination everywhere in the assumed range** — by
2.2× at the low-density end and 110× at 10¹⁴ cm⁻³ / 0.3 eV. Omitting it would understate the
electron sink by at least a factor of 2 and at most two orders of magnitude.

### 4.4 Channel 4 — Neutral-stabilised three-body recombination

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ + M => Li + M`, M = Ar or N₂ |
| **e-order** | **1** |
| **net e** | **−1** |
| **mol** | 3 → 2 |
| **deps** | Te: yes. Tgas: yes (through M's thermal motion). P: through [M]. E/N: no. EEDF: Maxwellian |
| **prov** | **UNKNOWN for Li⁺ specifically.** No measured or computed `Li⁺ + e⁻ + Ar` coefficient was found. **What would settle it:** a flowing-afterglow measurement, or a Li-specific CRR model including neutral collisions |
| **states** | Unresolved, as §4.3 |
| **applic** | Expected **negligible against §4.3 in the assumed range** [I]: a neutral third body is far less effective than an electron at removing the binding energy of a high Rydberg state, and standard practice is that the electron-stabilised term dominates below ~1 atm. That inference is the basis for the recommendation, and it is an inference, not a measurement |
| **unc** | **UNKNOWN** — no value to attach one to |
| **route** | Exact library reaction, third body explicit (req. 5), **if it is included at all** |
| **Physical inverse** | **Collisional (heavy-particle) ionisation**, `Li + M => Li⁺ + e⁻ + M` — thermal ionisation by a neutral. At Tgas ≤ 1000 K this needs 5.392 eV from a thermal collision; the Boltzmann factor is `exp(−5.392 eV/kT)` ≈ 10⁻²⁷ at 1000 K [I]. **Negligible, and it must be omitted explicitly rather than reconstructed from the forward via `Keq`** |

**Recommendation: dismiss, with the reason recorded.** Not because it is unphysical but because
there is no Li-specific number to store, and §4.3 covers the same sink with sourced data.

### 4.5 Channel 5 — Dissociative recombination of molecular ions  ❌ *unrepresentable*

| Field | Value |
|---|---|
| **eq** | `Li₂⁺ + e⁻ => Li + Li*` |
| **e-order** | 1 · **net e** −1 · **mol** 2 → 2 |
| **deps** | Te: yes, typically ≈ Te^(−0.5). Tgas: no. P: no. EEDF: Maxwellian |
| **prov** | **UNKNOWN.** No Li₂⁺ dissociative-recombination cross section or rate coefficient was found in this session. Li₂⁺ is a hard case theoretically — like H₂⁺ it has no favourable low-lying doubly excited dissociative state crossing the ion's ground vibrational level, so the indirect Rydberg mechanism dominates and the standard MQDT machinery is needed [L]+[I]. **What would settle it:** an MQDT calculation for Li₂⁺, or a storage-ring measurement. Neither was found |
| **states** | Would be strongly state-resolved (Li(2s) + Li(2p) vs Li(2s) + Li(2s)) — resolution RMG cannot express |
| **applic** | Moot |
| **unc** | **UNKNOWN** |
| **route** | Moot |
| **Physical inverse** | **Associative ionisation** (§4.6), `Li + Li* => Li₂⁺ + e⁻` — a different process with a different rate, not "DR backwards" |

**Dismissed, on two independent grounds, either of which alone is sufficient.**

1. **`Li₂⁺` cannot be built in this runtime.** `ATOMTYPES` defines exactly `Li`, `Li+`, `Li0` and
   none of them accepts a bonded Li⁺ (measured, `probe3`):
   ```
   Li atom types defined: ['Li', 'Li+', 'Li0']
   Li2+ REFUSED: AtomTypeError Unable to determine atom type for atom Li+, which has 1 single
   bonds, 0 double bonds ... and +1 charge.
   ```
   [R] `molecule/atomtype.py:989`. Neutral `Li₂` builds fine; the **cation** does not.
2. No rate data exists to store even if it did.

*Note for the mixed feed.* If M7 ends up as Li in **air** rather than Li in Ar, dissociative
recombination of N₂⁺ and O₂⁺ becomes the dominant electron sink, and for those ions the data are
abundant. That is air chemistry and belongs to the M6/air-ionisation track, not to the alkali cation
source. Named here so it is not lost.

### 4.6 Channel 6 — Associative ionisation  ❌ *unrepresentable*

| Field | Value |
|---|---|
| **eq** | `Li(2p) + Li(2p) => Li₂⁺ + e⁻` (the ground-state pair `Li + Li => Li₂⁺ + e⁻` is endothermic; IE(Li₂) = 5.11 eV) |
| **e-order** | **0** — no incident electron. This is the property that makes AI interesting: it is a cation source that does **not** require a pre-existing electron population |
| **net e** | **+1** · **mol** 2 → 2 |
| **deps** | Te: **no** — driven by the excited-state population, hence by Tgas and by whatever pumps Li(2p). P: through the excited-state density. EEDF: only indirectly, through electron-impact excitation of Li(2p) |
| **prov** | Klyucharev, A. N., "Chemi-ionization processes", *Physics-Uspekhi* **36** (1993) 486–512, doi:10.1070/PU1993v036n06ABEH002162 [L]; Klyucharev, A. N. *et al.*, "Rate coefficients for the chemi-ionization processes in sodium- and other alkali-metal geocosmical plasmas", *New Astron. Rev.* **51** (2007) 547–562, doi:10.1016/j.newar.2007.05.001 [L]. The best-characterised alkali AI benchmark is sodium: Boulmer, J., Bonanno, R. & Weiner, J., "Crossed-beam measurements of absolute rate coefficients in associative ionisation collisions between Na*(np) and Na(3s)", *J. Phys. B* **16** (1983) 3015–3024, doi:10.1088/0022-3700/16/16/021 [L]. **UNKNOWN for Li at the specific states relevant here** |
| **states** | **Entirely state-resolved** — the rate depends on the principal quantum number of the excited partner, which is the whole subject of the Klyucharev literature |
| **applic** | Would need a Li(2p) population, which at Tgas ≤ 1000 K comes only from electron-impact excitation — i.e. it is not an *independent* source, it is downstream of the electron population it would create |
| **unc** | **UNKNOWN** |
| **route** | Moot |
| **Physical inverse** | **Dissociative recombination of Li₂⁺** (§4.5) |

**Dismissed on three grounds.** (1) `Li₂⁺` is unrepresentable (§4.5). (2) **RMG has no
electronic-state resolution** — `Li(2p)` is not a distinct species from `Li(2s)` in an adjacency
list, so the reactant cannot be written. (3) It is not a bootstrap source: it needs excited Li,
which needs electrons.

### 4.7 Channel 7 — Charge transfer with abundant neutrals or ions  ✅ *representable today, but not a source*

| Field | Value |
|---|---|
| **eq** | `X⁺ + Li => X + Li⁺`, X = N₂, O₂, Ar, H₂O, NO |
| **e-order** | **0** — no electron participates |
| **net e** | **0** |
| **mol** | 2 → 2 |
| **deps** | Te: **no**. Tgas: weakly (Langevin capture is T-independent; the efficiency factor is not). P: no. E/N: no (at thermal energies). EEDF: no |
| **prov** | **No direct measurement of `N₂⁺ + Li` or `O₂⁺ + Li` was found.** The venue for one is Anicich's compilation of gas-phase ion–molecule rate constants, or the UMIST/KIDA astrochemical databases; neither was reachable in this session (§11). The defensible fallback is the **Langevin capture rate**, computed here from the static dipole polarizability of Li, α = 24.33 Å³ (`probe1`): |
| | `N₂⁺ + Li` → 4.88×10⁻⁹ cm³/s = 2.94×10⁹ m³/(mol·s) · `O₂⁺ + Li` → 4.82×10⁻⁹ · `Ar⁺ + Li` → 4.73×10⁻⁹ · `He⁺ + Li` → 7.24×10⁻⁹ |
| **states** | Unresolved. The product X may be vibrationally or electronically excited; near-resonant channels are favoured, which is exactly what the Langevin estimate averages over |
| **applic** | Valid across the whole assumed range — capture rates are essentially condition-independent at thermal energies |
| **unc** | **Factor ~2–3, one-sided.** Langevin is an **upper bound**: it assumes every capture collision transfers charge. Strongly exothermic transfers with poor Franck–Condon overlap can run an order of magnitude below it [L]+[I] |
| **route** | **Library, as an exact reaction.** It is technically family-shaped — charge-conserving, no electron, `is_balanced = True` (measured, §3.1) — but the efficiency factor is a property of one specific ion pair's energy resonance, not of a group. A family would interpolate a quantity that does not interpolate. Same argument as §4.1, chemistry half only |
| **Physical inverse** | **Endothermic charge transfer**, `Li⁺ + X => Li + X⁺`, endothermic by IE(X) − IE(Li) = **6.68 eV (O₂) to 10.37 eV (Ar)**. At Tgas ≤ 1000 K the Boltzmann factor is below 10⁻³³ [I]. **It must be omitted as a named, explicitly negligible channel** — not reconstructed from the forward through `Keq(Tgas)`, which the ruling and `plasma.pyx:536-542` both forbid |

**This is not a cation source, and it is the campaign's terminal-species risk.** Charge transfer
*moves* an existing charge; it creates none. Its real consequence is the opposite: with

```
IE(Li) = 5.392 eV   vs   IE(N₂) = 15.581   IE(Ar) = 15.760   IE(O₂) = 12.070   IE(H₂O) = 12.621
```
[L] NIST Atomic Spectra Database and NIST Chemistry WebBook, every bath-gas ion converts to Li⁺ on
essentially every capture collision. At 5 torr with 1 % Li (n_Li = 1.6×10¹⁵ cm⁻³) the conversion
time is `1/(k·n_Li)` ≈ **1.3×10⁻⁷ s** [I], four orders faster than any recombination channel above.

**Li⁺ therefore becomes the terminal ion of the mechanism** — precisely the "artificial terminal
species" the restated M7 gate exists to prevent. The consequence for implementation: the Li⁺ loss
channels (§4.2, §4.3) are not optional garnish, they are the only thing standing between the model
and a mechanism where all charge accumulates on lithium and never leaves.

### 4.8 Channel 8 — Ion–molecule association followed by stabilisation  ❌ *unrepresentable*

| Field | Value |
|---|---|
| **eq** | `Li⁺ + N₂ + M => Li⁺·N₂ + M` |
| **e-order** | **0** · **net e** **0** · **mol** 3 → 2 (exactly at the ceiling, req. 4) |
| **deps** | Te: no. Tgas: yes. P: strongly, through [M]. E/N: no. EEDF: no |
| **prov** | Binding energies are computational: Li⁺·N₂ **11.1 kcal/mol** and Li⁺·(N₂)₂ **21.2 kcal/mol** at MP2/CCSD, bonding purely electrostatic and dominated by the ion–quadrupole term [L] (Dawoud, Y. & Alomari, R., *Struct. Chem.* **30** (2019) 53–60, doi:10.1007/s11224-018-1147-8). The experimental compilation is Keesee, R. G. & Castleman, A. W., Jr., "Thermochemical data on gas-phase ion–molecule association and clustering reactions", *J. Phys. Chem. Ref. Data* **15** (1986) 1011, doi:10.1063/1.555757 [L]. **UNKNOWN:** the association *rate coefficient*, as opposed to the equilibrium thermochemistry. **What would settle it:** a high-pressure mass-spectrometric or flow-tube kinetics measurement |
| **states** | The nascent complex is vibrationally hot; stabilisation efficiency is the whole physics and is unresolved |
| **applic** | **Marginal at the assumed pressures.** A 0.48 eV bond against kT = 0.026–0.086 eV survives thermally, but three-body association is a high-pressure process and 0.05–5 torr is the low-pressure limit [I] |
| **unc** | **UNKNOWN** — no rate to attach one to |
| **route** | Library, third body explicit (req. 5) — **if the representation problem is fixed** |
| **Physical inverse** | **Collision-induced dissociation of the cluster**, `Li⁺·N₂ + M => Li⁺ + N₂ + M`. Different molecularity from the association's stabilisation step and a different energy-transfer problem; its own one-way entry |

**Dismissed.** `Li⁺·N₂` needs a bonded Li⁺ atom, which raises the same `AtomTypeError` as `Li₂⁺`
(§4.5) [R] `atomtype.py:989`. And even if it built, the channel changes neither the electron count
nor the cation count — it relocates a cation, it does not create or destroy one. It matters for M7
only if Li⁺ clustering shifts the *effective* recombination rate, which is a second-order effect on
a network that does not yet have a first-order one.

### 4.9 Channel 9 — Wall and surface losses  ⚠️ *dominant, and structurally unrepresentable*

| Field | Value |
|---|---|
| **eq** | `Li⁺ + e⁻ --(wall)--> Li`, transport-limited by ambipolar diffusion |
| **e-order** | Not a volume rate law at all — a boundary condition |
| **net e** | −1 per event · **mol** not defined for a surface process |
| **deps** | Tgas, P (through the neutral density and hence the ion mobility), Te (through `D_a ≈ D_i(1 + Te/Ti)`), and **reactor geometry**, which no other channel here depends on |
| **prov** | Standard ambipolar-diffusion theory; the ion mobility input is `μ₀(Li⁺ in N₂) ≈ 4 cm²/(V·s)` at STP, an order-of-magnitude value. **UNKNOWN:** a measured reduced mobility for Li⁺ in the actual bath gas. **What would settle it:** an ion-mobility measurement or a Mason–Schamp calculation with the Li⁺–bath potential |
| **states** | Wall neutralisation returns Li in an unspecified state; sticking vs recycling is itself unknown |
| **applic** | See below — dominant at the low-pressure anchor |
| **unc** | Factor ~3 on the coefficient, plus complete uncertainty on the geometry, which nobody has specified |
| **route** | **Neither family nor library. It is a reactor feature, and this reactor does not have it** |
| **Physical inverse** | **Wall desorption / sputtering of Li**, a surface-source process with entirely different physics. Not represented, and at these energies not expected to matter [I] |

**Dismissed as unrepresentable — but flagged as the headline sensitivity.** `PlasmaReactor` is a
homogeneous isobaric batch reactor with no surface, no geometry and no diffusion term [R]
`plasma.pyx:28-44`. There is no place to put this.

The size of what is being dropped, computed for a cylinder R = 1 cm, L = 10 cm at Te = 1 eV
(`probe1`):

| Pressure | D_a / cm² s⁻¹ | τ_wall | τ_ion at n_e = 10¹² cm⁻³, Te = 1 eV | Which wins |
|---|---|---|---|---|
| **5 torr** | 6.85×10² | **2.5×10⁻⁴ s** | 4.7×10⁻³ s | **wall, by 19×** |
| 760 torr | 4.51 | 3.8×10⁻² s | 4.7×10⁻³ s | volume, by 8× |

**At the campaign's own anchor conditions the dominant electron sink is the one the reactor cannot
represent.** A mechanism that omits it will over-predict the steady-state electron density —
the error is one-sided and, at 5 torr, roughly an order of magnitude. This is not a reason to stop;
it is a reason the condition set has to be ratified before the inventory is finalised, exactly as
the dispatch anticipated. At or near atmospheric pressure the problem largely goes away.

### 4.10 Channel 10 — Penning / chemi-ionisation by metastables  ⚠️ *not in the brief, and worth naming*

Not on the dispatch's list, but it is a genuine cation source from a neutral feed that needs no
pre-existing free electron, so omitting it silently would be a gap.

| Field | Value |
|---|---|
| **eq** | `Ar*(³P₂, 11.548 eV) + Li => Ar + Li⁺ + e⁻`, and `He*(2³S, 19.82 eV) + Li => He + Li⁺ + e⁻` |
| **e-order** | **0** · **net e** **+1** · **mol** 2 → 3 |
| **deps** | Tgas; the metastable density, which is itself electron-driven. Not directly Te |
| **prov** | Energetically allowed by a wide margin — every rare-gas metastable lies ≥ 6 eV above IE(Li) = 5.392 eV [L]. For He* + Li the system is well characterised: doi:10.1021/acs.jpca.3c00431 (*J. Phys. Chem. A* 2023, symmetry dependence of the continuum coupling in chemi-ionisation of Li(2²S₁/₂) by He(2³S₁, 2³P_J)) [L] and arXiv:1901.02482 (metastable-He beam × Li MOT) [L]. Afterglow rate coefficients for Penning ionisation of the heavier alkalis by He(2³S₁) are of order 10⁻⁹ cm³ s⁻¹ [L]. **UNKNOWN for `Ar* + Li` specifically**, which is the pair the campaign's Ar bath would need. **What would settle it:** a flowing-afterglow or merged-beam measurement of Ar*(³P₂) + Li |
| **states** | **Fully state-resolved** — the reactant is a specific metastable level, and the AI branch (`He* + Li => HeLi⁺ + e⁻`) competes with the PI branch |
| **applic** | Would be a real source in an Ar glow, where metastable densities of 10¹⁰–10¹² cm⁻³ are ordinary |
| **unc** | **UNKNOWN** for the Ar pair |
| **route** | Library, if ever representable |
| **Physical inverse** | **Three-body recombination into a metastable channel**, i.e. `Ar + Li⁺ + e⁻ => Ar* + Li` — a distinct process from either §4.3 or §4.4, and unmeasured |

**Dismissed, on the same ground as §4.6: RMG has no electronic-state resolution.** `Ar*` is not a
distinct species from `Ar` in an adjacency list, so the reactant cannot be written. Recorded because
if M7's reactor ever gains excited-state species, this becomes a first-class alkali cation source
that needs no electron to bootstrap it — which is exactly the property §4.1 lacks.

---

## 5. Forward channels paired with their actual physical inverses

The ruling's point restated as a table: only **one** row is a true inverse pair. Everything else
pairs with a process of different molecularity, partner or driving quantity.

| # | Forward | Its actual physical inverse, named | Same elementary channel? | Inverse available? |
|---|---|---|---|---|
| 1 | Electron-impact ionisation, `Li + e⁻ => Li⁺ + 2e⁻` | **Three-body electron–electron–ion recombination** (§4.3) | **Yes** — the only genuine pair here | Yes, §4.3, outside its stated Te range |
| 2 | Radiative recombination, `Li⁺ + e⁻ => Li` | **Photoionisation**, `Li + hν => Li⁺ + e⁻` | No — photon partner, radiation-field driven | **No.** The reactor has no radiation field |
| 3 | Three-body e–e–ion recombination | **Electron-impact ionisation** (§4.1) | **Yes** | Yes, §4.1 |
| 4 | Neutral-stabilised three-body recombination | **Thermal ionisation by neutral collision**, `Li + M => Li⁺ + e⁻ + M` | No — heavy-particle collision, Tgas-driven, not Te-driven | Negligible (Boltzmann ~10⁻²⁷ at 1000 K); omit explicitly |
| 5 | Dissociative recombination of Li₂⁺ | **Associative ionisation** (§4.6) | No — bound-state formation vs bond breaking | No; both unrepresentable |
| 6 | Associative ionisation | **Dissociative recombination of Li₂⁺** (§4.5) | No | No; both unrepresentable |
| 7 | Exothermic charge transfer, `X⁺ + Li => X + Li⁺` | **Endothermic charge transfer**, `Li⁺ + X => Li + X⁺` | No — 6.7–10.4 eV endothermic, a different channel | Negligible; omit explicitly, never via `Keq` |
| 8 | Ion–molecule association | **Collision-induced dissociation of the cluster** | No — different molecularity and energy-transfer problem | Unrepresentable |
| 9 | Wall loss by ambipolar diffusion | **Wall desorption / sputtering** | No — a surface source | Not represented |
| 10 | Penning / chemi-ionisation | **Three-body recombination into a metastable channel** | No | Unmeasured |

The generalisation the ruling is protecting: **the inverse of ionisation is a recombination process
chosen by conditions, not a fixed partner.** At 10¹⁴ cm⁻³ it is three-body; at 10¹⁰ cm⁻³ it is
within 2× of radiative; in a molecular bath it is dissociative recombination of a molecular ion
that lithium is not even part of.

---

## 6. Family versus library, per channel

| # | Channel | Route | Reason |
|---|---|---|---|
| 1 | Electron-impact ionisation of Li | **Library, exact** | *Chemistry:* the rate is one atom's threshold and cross-section shape; no group-additivity trend exists, exactly as `Plasma_Electron_Attachment/groups.py:29-35` argues for attachment [D]. *Code:* `resolve_electron_placement` refuses ionisation shapes by name [R] `electron_placement.py:103-105, 212-225` — **no family route exists** |
| 2 | Radiative recombination | **Library, exact** | Same, both halves. Additionally the Badnell fit is indexed by (Z, N), an atomic identity, not a molecular group |
| 3 | Three-body e–e–ion recombination | **Library, exact**, third body explicit | Same. Plus req. 5: `PlasmaReactor` refuses pressure-dependent kinetics [R] `plasma.pyx:449-453`, so no `ThirdBody` form |
| 4 | Neutral-stabilised three-body | **Library, exact** — if included | Same; currently no data (§4.4) |
| 5 | Dissociative recombination | **Neither** | Reactant unrepresentable (§4.5) |
| 6 | Associative ionisation | **Neither** | Reactant and product unrepresentable (§4.6) |
| 7 | Charge transfer | **Library, exact** | Technically family-shaped and `is_balanced = True` (measured), but the efficiency factor is an ion-pair energy-resonance property. A family would interpolate a quantity that does not interpolate — the same argument that governs attachment |
| 8 | Ion–molecule association | **Library, exact** — if ever representable | Cluster ion unrepresentable (§4.8) |
| 9 | Wall loss | **Neither** | A reactor feature, not a reaction (§4.9) |
| 10 | Penning ionisation | **Library, exact** — if ever representable | Needs metastable species (§4.10) |

**The general rule this yields:** in a plasma mechanism, **no electron-driven channel should be
family-generated**, on the chemistry alone — the rate tracks an ionisation threshold and a
cross-section shape, neither of which is a function of local connectivity. That RMG's electron
resolver also refuses these shapes is a second, independent lock on the same door. The one
existing plasma family in this database reached the same conclusion for attachment and enforced it
structurally, matching exactly the three shapes it has data for [D]
`Plasma_Electron_Attachment/groups.py:29-56`.

---

## 7. The explicit answer

> **Can a defensible cation source be assembled from what exists in the literature at the assumed
> conditions?**

**No.** But the boundary is not where the ticket expected it, and that is the useful part.

**The literature is not the blocker.** For the one channel that matters — electron-impact
ionisation of atomic Li — the data are sourced, published, *already committed to this repository*,
and evaluate correctly against the pin (§2.1, §4.1). Its dominant inverse, three-body recombination,
has a standard formula with a known factor-2 spread that this report cross-checked against the
campaign's own adjudicated value and found consistent (§4.3). Radiative recombination is in the
repository too. Charge transfer has a defensible Langevin estimate. **That is a workable network.**

**The blocker is representation, and it is precisely locatable.**

| # | What is missing | Where | Owner |
|---|---|---|---|
| **1** | **`Reaction.is_balanced()` counts the free-electron pseudo-species as a conserved chemical element, so every electron-changing reaction is refused by the kinetics-library loader** — while the metadata alternative is refused by the reactor and by the family resolver. No representation survives both ends (§3) | `rmgpy/reaction.py:1669-1731` in `RMG-Py-plasma` | **Runtime.** One function. Not a database change, and not this ticket |
| **2** | A **ratified M7 condition set** — composition, P, Tgas, Te, EEDF, residence time. §0.2 proposes one from the campaign's own anchors; adopting it is the user's call | `plasma-pm2` STRATEGY / contract | **User** |
| **3** | A **three-body recombination coefficient valid above Te = 4000 K** for Li⁺. Stevefelt is used ~3× beyond its stated range at the working point (§4.3) | literature or calculation | Data programme |
| **4** | The **Voronov Li normalisation**: whether it follows McFarland & Kinney as published or the ≈2.2-divided rescaling (§4.1) | Voronov 1997 §Li | Data programme |
| **5** | **`Li₂⁺` atom-type support**, if molecular-ion channels are ever wanted (§4.5) | `rmgpy/molecule/atomtype.py` | Runtime, low priority |
| **6** | **A wall-loss term, or an explicit statement that the model is volume-only.** At 5 torr this is the largest electron sink and the reactor has no place for it (§4.9) | `PlasmaReactor` or a scoping decision | **User / runtime** |
| **7** | **Excited-state species** (`Li(2p)`, `Ar*`, `He*`), if stepwise ionisation or Penning ionisation is ever wanted (§4.6, §4.10) | RMG core | Runtime, out of scope |

**What the M7 implementation ticket looks like once item 1 is fixed.** Four library entries, all
irreversible, all with the electron explicit, all against species this database already has:

```
[Li]  + e            =>  [Lip] + e + e     VoronovEIArrhenius(Z=3, N=3)
[Lip] + e            =>  [Li]              BadnellRRArrhenius(Z=3, N=2)
[Lip] + e + e        =>  [Li] + e          TwoTemperaturePlasma(...)   # Stevefelt collisional terms
[Xp]  + [Li]         =>  [X]  + [Lip]      Arrhenius(...)              # Langevin, per bath ion
```

Written with `=>` in the label *and* `reversible=False` in the entry — the loader raises if the two
disagree [R] `library.py:517-527` — and with `[Lip]`, never `Li+`, because the label parser splits
on `'+'` [R] `library.py:553`. Rows 1–3 were put through `PlasmaReactor._validate_reactions` in
this exact form and **all were accepted** (§3.4). Only `is_balanced()` stands between here and
there.

**Stated plainly, as the dispatch invites:** the alkali cation source exists, is sourced, and is
already sitting in this repository. It cannot be written down. That is a better problem than the one
the ticket was opened to investigate, and it is a one-function problem in a repository nobody has
been told not to fix.

---

## 8. Two hard constraints — compliance

**Constraint 1 — no Marcus electrode-transfer rate as a surrogate for a free-electron collision.**
Not one channel above uses a `Marcus` rate, and none uses the `Cation_R_Recombination` family, its
rules, its training reactions, or its λ set. The temptation the ticket names was live and is
recorded rather than acted on: those entries carry a ready-made `Li⁺ + R• (+ e⁻)` shape that looks
like recombination. It is not. `Marcus` consumes `T_gas` in all three places it uses a temperature
and has **no `uses_electron_temperature` attribute at all** — so `PlasmaReactor`'s
`getattr(kin, 'uses_electron_temperature', False)` returns `False` and would route a plasma
reaction down the thermal branch with no diagnostic [R] `plasma.pyx:487, 583`. Every electron-driven
channel above is assigned a Te-aware class from §2.2 instead.

**Constraint 2 — forward and reverse explicit, as separate one-way processes.** §5 pairs every
forward channel with its actual physical inverse, named as a process, and §4 writes every channel
one-way. No `kf/Keq(Tgas)` appears anywhere, no `Keq(Te)` substitute is proposed, and no channel's
inverse is assumed to be "the forward backwards" — §5 shows nine of the ten pairs are *not*. The
reactor enforces the same rule independently at `plasma.pyx:502-511` and `536-542` [R].

---

## 9. Read-only compliance

```
$ git status --porcelain
?? docs/i104-alkali-plasma-cation-source-inventory.md

$ git diff --stat fb3c13c60 -- input/
(no output)

$ git diff --stat
(no output — no tracked file is modified)
```

**No rate, family, group, tree node, training entry, `rules.py`, `reactions.py`, `dictionary.txt`,
thermo file, `voronov.yaml` or `badnell.yaml` was changed**, in this repository or any other.
Nothing was written to `/home/alon/Code/RMG-Py`, `/home/alon/Code/RMG-Py-plasma`,
`/home/alon/Code/RMG-database-plasma`, `/home/alon/Code/plasma-pm2`, or any other worktree.
`/home/alon/Code/RMG-Py-plasma` was on `PYTHONPATH` for reading only and was never built. The
synthetic library used in `probe2` was written to the scratchpad, outside every tracked tree. Live
output of these commands is reproduced in the report-back accompanying this document.

Things that could invite an edit, recorded rather than acted on:

- **Would change:** `Reaction.is_balanced()` to balance charge rather than count the electron
  pseudo-element. **Predicted effect:** unblocks the entire inventory at a stroke (§7 item 1).
  **Predicted problem:** it is in the shared runtime, not this database, and it touches every
  reaction RMG builds. A runtime ticket with its own regression scope.
- **Would change:** add a `Li₂⁺`-capable atom type. **Predicted effect:** unblocks §4.5 and §4.6
  representationally. **Predicted problem:** no data to put in them, so it would unblock nothing
  useful yet.

---

## 10. Durable findings

Eleven, in descending order of consequence. The first six are defects in the pinned runtime.

1. **No representation exists in which an electron-changing reaction can be both stored and
   evaluated.** `is_balanced()` refuses the explicit form (so the library loader refuses it);
   `PlasmaReactor` and `resolve_electron_placement` refuse the metadata form. Measured both ways,
   §3. This blocks the entire alkali plasma programme, not just this ticket.
2. **`Reaction.is_balanced()` counts the free-electron pseudo-species as a conserved chemical
   element** [R] `reaction.py:1684-1723`. `[Li] + e => [Lip] + e + e` returns `False`. Electrons are
   created and destroyed by ionisation; they are not conserved like carbon.
3. **The charge comparison inside `is_balanced()` is dead code.** `reactants_net_charge` and
   `products_net_charge` are accumulated, adjusted by `self.electrons`, and never compared [R]
   `reaction.py:1682-1731`. `[Li] => [Lip]` with `electrons=0` passes — charge 0 → +1. Findings 2
   and 3 are the same bug seen from both sides.
4. **`PlasmaReactor` accepts exactly the reaction form the database cannot store.** Explicit-electron
   EI and RR carrying real Voronov and Badnell kinetics both passed `_validate_reactions` while
   `is_balanced()` reported `False` for both (§3.4). The two ends of the pipeline disagree about the
   canonical representation.
5. **`Li₂⁺` cannot be constructed.** `ATOMTYPES` has `Li`, `Li+`, `Li0` and none accepts a bonded
   `Li+`; the adjacency list raises `AtomTypeError` [R] `atomtype.py:989`. Neutral `Li₂` builds
   fine. Every molecular-lithium-ion channel is blocked at the molecule layer.
6. **A kinetics-library label cannot contain a species named `Li+`.** The parser splits reactant and
   product strings on `'+'` [R] `library.py:553,559`, so `Li+` produces an empty token and a
   `DatabaseError` (measured). This database's `[Lip]` convention [D]
   `LithiumPrimaryChargedKinetics/dictionary.txt:1` is a workaround for a parser limitation, and any
   future plasma library must follow it.
7. **The alkali cation source data are already in this repository, unnoticed.**
   `input/kinetics/voronov.yaml` carries Voronov's Li electron-impact ionisation fit and
   `input/kinetics/badnell.yaml` carries Badnell's Li⁺ radiative-recombination fit, both with source
   strings, both loading, both evaluating [D]. The ticket was opened on the premise that the source
   had to be found in the literature; most of it was already committed.
8. **Lithium is a charge sink in any mixed feed.** IE(Li) = 5.392 eV lies 6.7–10.4 eV below every
   plausible bath gas, so every bath-gas ion transfers charge to Li at ~the Langevin rate
   (4.7–4.9×10⁻⁹ cm³/s, computed) — a ~10⁻⁷ s conversion time at 5 torr with 1 % Li. **Li⁺ becomes
   the terminal ion**, which is the exact failure the restated M7 gate names. Its loss channels are
   load-bearing, not decorative.
9. **At the campaign's own anchor conditions the dominant electron sink is one the reactor cannot
   represent.** τ_wall ≈ 2.5×10⁻⁴ s at 5 torr against τ_ion ≈ 4.7×10⁻³ s — a 19× margin — and
   `PlasmaReactor` is a homogeneous batch reactor with no surface or geometry [R] `plasma.pyx:28-44`.
   The omission biases the electron density upward, one-sidedly. At 1 atm the ranking inverts.
10. **The EEDF is not a modelling choice in this runtime, it is a structural assumption.**
    `ElectronCollisionPlasma` integrates against a Maxwellian and nothing else [R]
    `arrhenius.pyx:648-694`; Voronov and Badnell are Maxwellian averages by construction; there is no
    E/N, no field and no Boltzmann solver anywhere. Any channel naturally keyed on E/N must be
    re-expressed in Te before it can be stored, and the dispatch's "EEDF assumption" is already made.
11. **The campaign's adjudicated three-body coefficient is corroborated.** `8.75e-27·Te_eV^-4.5`
    [D] `INSIGHTS.md:939-957` versus Stevefelt's collisional term re-expressed in eV,
    `1.95e-27·Te_eV^-4.5` — a factor 4.5, same class, same exponent, ordinary inter-treatment spread.
    The value adjudicated in I-013 stands.

Also worth keeping: **using Stevefelt's full coefficient alongside the Badnell RR entry double-counts
radiative recombination**, because Stevefelt's first term *is* the radiative contribution (§4.3).

---

## 11. What this inventory could not reach

Named rather than papered over, because each is a real limit on §7:

- **The ratified M7 condition set does not exist**, so every condition-dependent finding here is
  conditional on §0.2, which is a proposal. §0.3 separates what survives any plausible set from what
  does not; ratification is the user's call and is the first thing that should happen next.
- **The residence time is genuinely unknown**, not merely unrecorded. `PlasmaReactor` is a batch
  reactor with no flow term [R], so the question may not even be well-posed until the M7 reactor
  specification exists.
- **Voronov 1997 itself was not read.** The Li entry's underlying normalisation — McFarland & Kinney
  as published, or the ≈2.2-divided rescaling that a later compilation adopted — is the single
  largest quantified uncertainty on the one channel that matters, and it is a factor of 2 on the
  cation source term. Settling it needs the paper.
- **No direct measurement of `N₂⁺ + Li`, `O₂⁺ + Li` or `Ar⁺ + Li` charge transfer was found.**
  The searches did not reach Anicich's compilation of gas-phase ion–molecule rate constants or the
  UMIST/KIDA databases, which is where such a value would live. The Langevin numbers in §4.7 are
  computed here, not cited, and are upper bounds.
- **No `Ar*(³P₂) + Li` Penning rate was found**, which is the pair an Ar-bath model would need
  (§4.10). The He* + Li system is well characterised and the Ar* one apparently is not.
- **No Li₂⁺ dissociative-recombination data was found**, and the search was not exhaustive — an MQDT
  treatment may exist in the early-universe-chemistry literature. It is moot while the ion is
  unrepresentable (§4.5), but it would stop being moot if finding 5 were fixed.
- **No reactor was run.** The `PlasmaReactor` acceptances in §3.4 come from calling
  `_validate_reactions` directly, not from integrating a mechanism. Nothing here demonstrates that
  the network *solves*, only that its reactions would be admitted.
- **Stepwise ionisation via Li(2p) was not quantified.** It is named as a known accuracy limit on
  §4.1 at Te ≤ 1 eV and its size was not estimated; doing so needs a collisional-radiative model of
  Li, which is a task in itself.
- **The Li thermo above 3000 K was not examined.** The NASA polynomials stop there [D]. Within the
  assumed Tgas range that is ample, but a hotter ratified condition set would run past them.
- **Only lithium was inventoried.** The dispatch says "other alkali species if relevant"; Na, K and
  Cs were not examined. Their data availability was checked, though, and is favourable:
  `voronov.yaml` carries `H, He, Li, C, N, O, Na, Mg, Al, Si, Ar, K, Ca` [D], so **Na and K
  electron-impact ionisation fits are already in this repository too**; Cs (Z = 55) is not, being
  outside Voronov's Z ≤ 28 range. `badnell.yaml` spans Z = 1–54 [D]. What was *not* done is the
  channel-by-channel inventory for those elements. Every structural finding in §3 and §10 transfers
  unchanged — they are about the electron, not about lithium.
