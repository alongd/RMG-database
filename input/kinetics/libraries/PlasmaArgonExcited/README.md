# Room-temperature Ar(4s) heavy-particle losses

Load `PlasmaArgonExcited` with `PlasmaArgon`, `PlasmaArgonDimer`, and
`PlasmaNitrogen`. Use the existing `PlasmaExcitedNeutralThermo`,
`primaryThermoLibrary`, `PlasmaThermo`, and `electrocatThermo` thermochemistry.
The dictionary preserves their electronic-state identities. No new thermo is
needed. Do **not** load `PlasmaArgonLegacy` alongside this library.

This is a **declared reduced network**, intended for an isothermal 298–300 K,
5 Torr Ar/N2 calculation with x(N2)=0.01–0.2. It is not a complete plasma
mechanism. The constants do not establish a temperature law or validity beyond
that domain. The 298 K application is a constant-rate extension from 300 K.

There are 27 irreversible Arrhenius entries: eight N2-transfer branches,
seven Ar collision channels, ten unordered pooling pairs, and two N2 radiative
channels. No electron reactants, ThirdBody, explicit neutral excimer, or
trapped-resonance decay entries are introduced. Explicit repeated Ar reactants
supply the bath-density powers in the two ternary entries.

## Per-state inventory and ownership

`Ars` is 1s5 (3P2); the other dictionary labels are `Ar(1s4)` (3P1),
`Ar(1s3)` (3P0), and `Ar(1s2)` (1P1). “Reserved” below means map ownership,
not a claim that a loaded reaction exists. The baseline map still marks
excited-target reaction owners absent. Electron implementation is separate.

| Process | 1s5 | 1s4 | 1s3 | 1s2 |
|---|---|---|---|---|
| Electron 4s mixing | reserved 125–127 | reserved 97,98,125 | reserved 44,97,126 | reserved 44,98,127 |
| Electron de-excitation to ground | inverse of map 2 missing | inverse of 3 missing | inverse of 4 missing | inverse of 5 missing |
| Stepwise ionization | reserved 154 | reserved 155 | reserved 156 | reserved 157 |
| Electron excitation to 2p / higher | reserved 128–137 / 138–153 | reserved 99–108 / 109–124 | reserved 45–54 / 55–70 | reserved 71–80 / 81–96 |
| Direct ground quench by Ar | added A5 | omitted, unsourced | omitted, unsourced | omitted, unsourced |
| Ar ternary / excimer loss | added A6, eliminated triplet | added A7, eliminated singlet | omitted from reduced network | omitted, unsourced |
| N2 total loss and C/B products | Q5, entries 1–2 | Q4, entries 3–4 | Q3, entries 5–6 | Q2, entries 7–8 |
| N2 dissociation | omitted, no adopted branch | omitted, joint bound below | omitted, no adopted branch | omitted, joint bound below |
| Pooling with all four states | added matrix | added matrix | added matrix | added matrix |
| Ar-induced mixing | A4 to 1s4 | A3 to 1s5 | A2 to 1s4 | A1 to 1s3 |
| Neutral wall diffusion | existing operator, declaration below | same | same | same |
| Quenching by N | conditional N1, out of scope | unsourced, out of scope | conditional N1, out of scope | unsourced, out of scope |
| Trapped resonance emission | not applicable | separate operator work | not applicable | separate operator work |

The EEDF map is `input/eedf/argon_channel_map.yaml`. All six unordered
4s-mixing pairs are reserved there; each needs two directional owners.
Ground excitation rows 2–5 have `superelastic_in_set: false`; their missing
reverse cannot be supplied by a heavy-particle reaction. Stepwise ionization
uses the map's existing TRINITI transfer convention. Higher electron excitations
can cascade back into 4s: their gross depletion is not necessarily net loss.
No electron rate is invented here at the nominal n_e=1e17 m^-3.

N1 remains conditional on atomic N being generated. Piper, Clyne and Monkhouse,
Chem. Phys. 51, 107–112 (1980), measured three upper-N excitation channels
from mixed Ar(3P2,0)+N at 296 K, with sum 1.74e-16 m^3/s. That is neither
four state-resolved total losses nor a justification for low-N(2D/2P) products.
The first-run deck's absence of N is a manager integration check. N2(A) losses
and the singlets N2(a′), N2(a) are also separate work.

## N2 transfer: primary totals, declared product split

Velazco, Kolts and Setser, *J. Chem. Phys.* **69**, 4357–4373 (1978),
[doi:10.1063/1.436447](https://doi.org/10.1063/1.436447), Tables I and II:

| State | Total k (m^3 per particle per s) | Source and uncertainty |
|---|---:|---|
| 1s5 | 3.6e-17 | Table I, 3P2, footnote g: three determinations differ by <10% |
| 1s4 | 0.8e-17 | Table II, 3P1, literature comparison, Ref. 20; no uncertainty supplied |
| 1s3 | 1.6e-17 | Table I, 3P0, attributed to Piper et al. (1973), Ref. 2a |
| 1s2 | 5.4e-17 | Table II, 1P1, literature comparison, Ref. 20; no uncertainty supplied |

Table I's metastable relative uncertainty is ±10%, excluding experiment-specific
errors; the paper estimates ±20% absolute reliability. Do not transfer that
uncertainty to the resonance comparison values. The original table units are
10^-11 cm^3/s; these are **total** removal coefficients at 300 K.

**AR4S_N2_PRODUCT_SPLIT:** use fC=fB=0.5 for each state. Kolts, Brashears
and Setser, *J. Chem. Phys.* **67**, 2931–2933 (1977), as reported by
[Klages et al. (2020)](https://doi.org/10.1002/ppap.202000070), measured
C/B=1.0±0.2 for a roughly 7:1 mixture of 1s5 and 1s3. Applying it separately
to all four states is an approved transfer convention, **not four measurements**.
Sadeghi, Cheaib and Setser, JCP **90**, 219 (1989),
[doi:10.1063/1.456691](https://doi.org/10.1063/1.456691), concerns halogen
reactants; no primary per-state N2 branching was established from that lead.
The approved mixture fallback is therefore used.

The measured mixture ratio maps to fC=0.444–0.545. The honest transfer
sensitivity is the full fC in [0,1], independently for each state, with
fB=1-fC: direct C production spans zero to the full transfer rate, direct B
production spans the complement, while each Ar total remains unchanged.
After complete radiative relaxation both branches reach N2(A); their transient
C/B populations and photons differ. Keep each pair sum equal to the total.
The nominal entries use identical halves, with no extra total-loss entry.

Reject the resonance C-production numbers quoted by Isola et al. (2014),
[doi:10.1088/0963-0252/23/1/015014](https://doi.org/10.1088/0963-0252/23/1/015014):
its 1s4 partial rate 3.6e-17 exceeds the adopted total 0.8e-17 by 4.5 times.
No retrieved primary measurement supersedes the total set. Klages' joint bound
for resonance-induced dissociation is k(1s2)+k(1s4)<2e-19 m^3/s, not a
rate or separate bound to add twice. Dissociation is omitted; zero is not proven.

## Reduced Ar collision network and excimer elimination

**REDUCED_AR4S_HEAVY_NETWORK:** [Stankov et al. (2022), Table 3](https://doi.org/10.1088/1361-6595/ac9332),
*Plasma Sources Sci. Technol.* **31**, 125002. Particle rate coefficients:

| ID / entry | Process (Ar bath shown once for binary) | k | Table row / original citation |
|---|---|---:|---|
| A1 / 9 | 1s2 + Ar → 1s3 + Ar | 4.76e-20 m^3/s | 350 / Firestone, Oka & Takao 1979 |
| A2 / 10 | 1s3 + Ar → 1s4 + Ar | 5.30e-21 m^3/s | 351 / Kolts & Setser 1978 |
| A3 / 11 | 1s4 + Ar → 1s5 + Ar | 1.50e-20 m^3/s | 352 / Millet et al. 1982 |
| A4 / 12 | 1s5 + Ar → 1s4 + Ar | 2.50e-21 m^3/s | 354 / Millet et al. 1982 |
| A5 / 13 | 1s5 + Ar → 2 Ar | 1.50e-20 m^3/s | 355 / Millet et al. 1982 |
| A6 / 14 | 1s5 + 2 Ar → 3 Ar | 1.30e-44 m^6/s | 356 / Millet et al. 1982 |
| A7 / 15 | 1s4 + 2 Ar → 3 Ar | 1.50e-45 m^6/s | 353 / Millet et al. 1982 |

A6/A7 eliminate the triplet/singlet neutral excimer and its radiative decay:
only the net isothermal removal is modeled. This is not a gas-heating model,
a time-resolved excimer population, or a measured direct three-body ground
transition. No statistical error or temperature law is supplied in Table 3.

A3/A4 are separate, irreversible, independently supplied directional rates,
marked as duplicates only to satisfy RMG's reverse-stoichiometry duplicate
check. They are not a detailed-balance pair. At 298 K their up/down ratio
0.1667 differs from the electronic Boltzmann ratio (~0.0323).

The reduction omits direct ground quench of 1s4/1s3/1s2, ternary loss of
1s3 and 1s2, and all unsourced Ar-mixing directions beyond A1–A4. An older
1s3 ternary measurement exists but is not imported into this source set.
The known-channel ranking below supports the reduction at the proposed
composition. It does **not** bound unknown omitted coefficients: a blanket
claim that N2 beats every unsourced omitted channel by fivefold is unsupported.
Legacy constants are alternatives from a lumped metastable model, not extra
channels to load alongside this network.

## Pooling

Entries 16–25 implement Table 3 rows 278–287, exactly once per unordered pair.
The symmetric matrix in units of 1e-15 m^3/s, order (1s5,1s4,1s3,1s2), is:

| | 1s5 | 1s4 | 1s3 | 1s2 |
|---|---:|---:|---:|---:|
| 1s5 | 1.2 | 2.1 | 4.2 | 4.2 |
| 1s4 | 2.1 | 2.1 | 2.1 | 2.1 |
| 1s3 | 4.2 | 2.1 | 1.2 | 2.1 |
| 1s2 | 4.2 | 2.1 | 2.1 | 2.1 |

Stankov cites Blagoev & Popov, *Phys. Lett. A* **70**, 416–418 (1979),
except 1s3 self-pooling, attributed to Kolokolov et al., *Phys. Scr.* **50**,
371–402 (1994). The original investigators explicitly define the event
convention in [Kolokolov & Blagoev, Phys. Usp. 36, 152–170 (1993),
Eq. (2.1), section 4.1](https://doi.org/10.1070/PU1993v036n03ABEH002138):
electron production is k*n_i*n_j; identical-state atom removal is 2*k*n_i^2.
RMG applies this stoichiometric factor; **do not halve k**.

That account reports 1s5 self-pooling (1.2±0.2)e-15 m^3/s (random error)
and explains that all ten constants could not be independently inferred.
The adopted matrix is the evaluated Stankov model, not ten equally precise
measurements. Earlier electron-production data combine Penning and associative
ionization; the atomic-ion-only product `Arp + Ar + e-` follows Stankov's
reduction. Table 3 supplies no uncertainty for each matrix cell.

## Radiative product closure and thermochemistry

Entries 26–27 are N2C → N2B at 2.74e7 s^-1 and N2B → N2A at 2e5 s^-1.
These are the published vibrationally lumped electronic-state coefficients N23
and N25 in [Guerra et al., PSST 28, 073001 (2019), Table 5](https://doi.org/10.1088/1361-6595/ab252c).
N23 cites [Lofthus & Krupenie, JPCRD 6, 113–307 (1977)](https://doi.org/10.1063/1.555546):
Table 82 gives C(v=0) lifetime (3.66±0.05)e-8 s. Its measurement uncertainty
is not an error bar for arbitrary vibrational populations. Lofthus–Krupenie
also lists B lifetimes from 8.0 microseconds at v=0 to 4.1 microseconds at
v=12, rather than a unique electronic-manifold average. N25 in Guerra cites
Piper, JCP 91, 864–873 (1989); use that published lumped rate rather than
inventing vibrational weights. The approved **lumping uncertainty** is this
v-dependent lifetime range, 4.1–8.0 microseconds, or a rate range of
1.25e5–2.44e5 s^-1 around the nominal 5 microseconds / 2e5 s^-1.
It describes sensitivity to the unresolved vibrational population, not a
statistical confidence interval. Guerra supplies no statistical uncertainty
for N25.

This closure neglects explicit vibrational redistribution and photon trapping
in those molecular bands. It prevents C/B from becoming permanent reservoirs;
it does not complete N2(A) chemistry. PlasmaNitrogen has no duplicate radiative
entries. All new reactions are explicitly irreversible: the shifted electronic
thermo and eliminated radiation do not support thermal detailed balance.

## Wall declaration

The existing neutral-diffusion operator consumes the following dictionary as
the `wallNeutralDiffusion` argument of `plasmaReactor`. The deck must also
supply its actual diffusion length or chamber geometry and declare ion transport
separately for a mixed bath. The test explicitly flags its scalar ion mobility
as a single-bath diagnostic and subtracts the operator-off residual; it does not
validate ion transport. The test reads this
snippet and checks the residual, with nonzero populations of every 4s state.

```python
wallNeutralDiffusion = {
    'Ars': {'product': 'Ar', 'diffusivity': (1.7e20, '1/(m*s)')},
    'Ar(1s4)': {'product': 'Ar', 'diffusivity': (1.7e20, '1/(m*s)')},
    'Ar(1s3)': {'product': 'Ar', 'diffusivity': (1.7e20, '1/(m*s)')},
    'Ar(1s2)': {'product': 'Ar', 'diffusivity': (1.7e20, '1/(m*s)')},
}
```

**COMMON_AR_BATH_DIFFUSION:** [Donkó et al., J. Phys. D 57, 375209 (2024)](https://doi.org/10.1088/1361-6463/ad4e42)
uses D*n_gas=1.7e20 m^-1 s^-1 for excited Ar. Applying it to all four states,
and unchanged up to x(N2)=0.2, is a declared common-Ar-bath approximation;
it is not four measured mixture coefficients. No temperature exponent or
numerical uncertainty is supplied. Do not substitute Lennard-Jones transport.

At 5 Torr, 298 K, D=1.04924e-3 m^2/s. For the illustrative diffusion length
20.3 mm, all four wall frequencies are 2.54615 s^-1. Frequencies scale
linearly with D*n and as inverse diffusion length squared. Even doubling this
coefficient leaves this illustrative wall sink far below the known chemical
sinks (at least thousands per second); geometry still belongs to the deck.

## Magnitudes and validation boundary

At 5 Torr, 298 K, n=1.6202181e23 m^-3. Binary bath frequencies are k*n_bath;
ternary frequencies are k*n_Ar^2. Values in s^-1:

| Channel | x(N2)=0.01 | x(N2)=0.2 |
|---|---:|---:|
| Q5 | 58327.9 | 1166557.0 |
| Q4 | 12961.7 | 259234.9 |
| Q3 | 25923.5 | 518469.8 |
| Q2 | 87491.8 | 1749835.5 |
| A1 | 7635.12 | 6169.79 |
| A2 | 850.128 | 686.972 |
| A3 | 2406.02 | 1944.26 |
| A4 | 401.004 | 324.044 |
| A5 | 2406.02 | 1944.26 |
| A6 | 334.473 | 218.409 |
| A7 | 38.593 | 25.201 |

N2 dominates the retained Ar-bath channels; Q4/A3=5.39 already at 1%.
Pooling requires excited-state densities, not the gas density: with all four
n_i=1e16 m^-3, total pooling losses per state are (129,105,108,126) s^-1.
They can overtake other sinks if excited populations grow; these are examples,
not predicted discharge populations. The wall example is smaller still.

Rate tests use RMG's particle/mole convention N_A=6.02214179e23 mol^-1,
matching `rmgpy.constants.Na` in the target engine. Molar coefficients scale
as N_A^(reaction_order-1). Tests separately evaluate 298 and 300 K,
both mixture points, all matrix cells, event stoichiometry, dictionary/thermo
loading, atom and charge conservation, coexistence, and the actual wall residual.
The short real model-generation test is a heavy-particle admission exercise;
its electron and ion products are marked nonreactive to keep electron kinetics
outside that check. It is not an EEDF discharge or steady-state validation.
