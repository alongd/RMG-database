# PlasmaAtomicNitrogen

Resolved N(4S), N(2D), and N(2P) channels for argon/nitrogen plasmas.
Load PlasmaAtomicNitrogenThermo before general thermo libraries, together
with the molecular PlasmaNitrogen, PlasmaNitrogenExcited and
PlasmaArgonExcited libraries. Preserve the latter's B/C pooling and cascade.
Dissociative pooling belongs only to the optional
PlasmaNitrogenDissociativePooling library.

## Heavy-particle rates and radiation

Particle units are m3/s for binary collisions, m6/s for ternary events,
and s-1 for spontaneous emission. Every reaction is irreversible.
Explicit collider entries remove two N atoms per recombination event;
there is no ThirdBody or extra aggregate recombination reaction.

| Process | Rate | Evaluation / convention |
|---|---:|---|
| A+N -> N2+N(2P) | 4.4e-17 | Herron 1999, factor 1.5; unit dominant P product, vibrational N2 lumped |
| N(2D)+N2 -> N+N2 | 1.7e-20 | Herron Table 2, factor 1.5; conflicting temperature slopes not adopted |
| N(2P)+N2 -> N+N2 | 5e-23 | Herron Table 5, factor 5; do not use Guerra's older 6e-20 |
| N(2P)+N -> products | 6e-19 total | Herron Table 5, factor 3; unresolved products, declared 3:1 S:D model split from Guerra N10:N11 |
| N+N+N2 -> N2(B)+N2 | 8.27e-46 exp(500/T) | Guerra N22, no quoted numerical uncertainty |
| N+N+Ar -> N2(B/X)+Ar | 3.8051969e-45 total at 298 K | Campbell-Thrush total; half B, half X as a declared interpretation of about half via B |

Herron: doi:10.1063/1.556043. Guerra: doi:10.1088/1361-6595/ab252c.
Campbell-Thrush: doi:10.1098/rspa.1967.0014. The Ar total is
(1.38 +/- 0.11)e15 cm6 mol-2 s-1 converted with RMG N_A.
The room-temperature constants are held constant to 600 K by an explicit,
unvalidated extension. Arrhenius validity fields delimit this adopted
model envelope; they do not claim measurements throughout it. Product
branching uncertainty is separate from the evaluated total-rate errors.
For P+N, a product sensitivity should retain total 6e-19 and vary the S:D
allocation; the baseline 3:1 ratio is not a new evaluated branching yield.

NIST ASD (doi:10.18434/T4W30F), N I TP reference T7370, supplies the
forbidden radiative probabilities. Sum M1 and E2 and all lower-J branches,
then average over upper-J populations in proportion to 2J+1. This gives:

- N(2D) => N: 1.26726e-05 s-1. J=3/2 A(M1,E2)=(1.60e-5,4.34e-6); J=5/2=(9.71e-7,6.59e-6) s-1. ASD accuracy B (<=10%).

- N(2P) => N: 0.0052 s-1. J=3/2 A=6.5e-3; J=1/2 A=2.6e-3 s-1. ASD accuracy D (<=50%).

- N(2P) => N(2D): 0.0881633333333 s-1. J=3/2 sum A=1.02e-3+6e-2+1.81e-3+2.56e-2; J=1/2 sum A=3.45e-2+1.13e-3+5.2e-2 s-1. ASD accuracy C (<=25%).

These are optically thin losses; photons are not gas or electron heating.
State manifolds are explicit, but J levels are not. The same statistical
fine-structure convention sets enthalpy centroids and entropy in the thermo
library (degeneracies S=4, D=10, P=6). Ground N uses the existing multiplicity-4
adjacency. The doublets have electronicstate 2D/2P and remain distinct.

## Neutral walls

Merge these declarations with the molecular and argon declarations.
A cylinder chamberGeometry with R=5 cm, L=30 cm is required for N recombination;
a bare diffusion length cannot determine its surface resistance.

```python
wallNeutralDiffusion = {
    'N': {'kind': 'homonuclearRecombination', 'product': 'N2',
          'diffusivity': (7.05616e20, '1/(m*s)'), 'recombinationProbability': 5e-5},
    'N(2D)': {'product': 'N', 'diffusivity': (7.05616e20, '1/(m*s)')},
    'N(2P)': {'product': 'N', 'diffusivity': (7.05616e20, '1/(m*s)')},
}
```
Ground-atom recombination uses Guerra Eq.33:
tau = Lambda^2/D + 2(V/S)(2-gamma)/(gamma*vbar).
V/S = R*L/[2(R+L)] comes from the declared cylinder.
Half a ground N2 returns per N atom; the material enthalpy decrease is
reported separately as wall_recombination_energy_flux, deposited at the wall.
The excited atoms use ordinary one-to-one same-skeleton deactivation to N.

Gamma=5e-5 is the declared Pyrex/silica central policy, bracketed from
1e-5 to 1e-3. Pure-N2 Pyrex measurements are roughly 2e-5 to 8e-5;
material history and Ar admixture are not covered by that interval.
Surface evidence: doi:10.1088/0022-3727/40/18/017 and Guerra 2019.
Both gamma and D*n are held constant by convention over 300-600 K.
The transferred Chapman-Enskog N-in-Ar estimate uses N sigma=3.298 Angstrom,
epsilon/k=71.4 K; Ar sigma=3.33 Angstrom, epsilon=1134.93 J/mol.
It is neither a measured mixture diffusivity nor a temperature law.
The same Ar-bath D*n is transferred to the two excited atomic manifolds
and to mixtures with x_N2 up to 0.2.

## Explicit source gaps and electron channels

No evaluated N(2D)+N, N(2D)+Ar, or N(2P)+Ar loss coefficient was verified
in the selected evaluation. These channels are omitted, not assigned zero
as an experimental upper bound. P+N product branching remains a model
convention even though its total removal is evaluated.
No O/NO chemistry or additional atomic ion chemistry is included.

The local IST-Lisbon N set provides N->D/P electron excitation from
Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714.
These are required sourced owners, not a missing-cross-section assumption.
Their six ordinary owners are entries 12–17. The frozen map in
`input/eedf/atomic_nitrogen_channel_map.json` pins both local source downloads
and their six-block solver realization, with an explicit ordinary inverse
owner for each excitation. Atomic midpoint qualification has passed on the
completed reduced tables. Full production-table qualification remains required.
Entries 18–19 supply rate-only dissociation, described below; their event curves
are not identical to sing-sup and do not define a constant branch split.
Physical discharge validation remains pending.

## Verification

test/test_plasma_atomic_nitrogen.py checks independent source rate values,
balance, state identity, manifold thermo, molecular-library coexistence,
and actual wall residual conservation. Physical 0.5 W densities, A-loss
shares, pooling on/off, and gamma brackets require the engine dependency
to land and a correctly regenerated production EEDF table. No fixed-density
probe or conditional reduced balance is a physical power-consistent result.

## Resolved atomic electron collisions

Entries 12–17 own the three Wang–Zatsarinny–Bartschat excitation/superelastic pairs, including N(2D) ↔ N(2P), as ordinary ine/sup EEDF channels. Their electron energy loss/gain belongs to the table. The source thresholds 2.39071, 3.5676 and 1.177 eV are retained; they differ slightly from the NIST term-centroid thermo spacings. DOI:10.1103/PhysRevA.89.062714; local IST-Lisbon extension to 1 keV. The table must also include all three atomic elastic channels.

The bounded atomic-target screen rejects the omitted-target approximation: at total-gas fractions N(4S)=5e-4 and N(2D)=N(2P)=2e-4, mobility and field power change by up to 2.932%. The production spec therefore needs three realized total-neutral-gas fraction axes, initially zero and those bounds. Atoms displace Ar. Interpolation is multilinear on these axes, including after an explicitly approved single midpoint insertion. Runtime refuses any fraction above its named top node.

Atomic ionization remains excluded from this chemistry. Its electron cross sections exist in the source files, but the corresponding N+ chemistry and owner are outside this library's current scope. A one-way quadrature on the 18 atom-present screened EEDFs (298.15 K, 5 Torr; 4/17/25 Td; x_N2=.01/.05/.2; Ar4s/ground=0 or1e-5) gives:

| State | k range (m3/s) | ion production per electron at its bound (s^-1) |
|---|---:|---:|
| N(4S) | 9.91e-28 .. 4.29e-19 | 8.02e-8 .. 34.7 |
| N(2D) | 2.72e-24 .. 4.69e-17 | 8.82e-5 .. 1.52e3 |
| N(2P) | 8.26e-23 .. 1.33e-16 | 2.67e-3 .. 4.31e3 |

The summed threshold-only power estimate is 2.36e-7% .. 0.0586% of field power. This is an order-of-magnitude diagnostic using source thresholds 14.54, 12.149 and 10.972 eV and the existing screened EEDFs; it omits ionization feedback and N+ chemistry. It is not a self-consistent discharge result, a rigorous omission bound, or an assumed electron density. The local source files identify the same Wang et al. DOI above.

N2 dissociation retains the separately approved rate-only role: chemical rates from the two extra cross sections, no new Boltzmann collision or electron energy sink, with explicit complete-N2-loss coverage. The table records that role structurally; compiled checks and the independent acceptance probe must pass before production use.


The spec-only command `python -m rmgpy.tools.eedf.atomic --base-spec BASE
--database DATABASE --sources LOCAL_DOWNLOAD_DIRECTORY --output NEW_DIRECTORY`
retains the Ar/N2 collision map, including its Ar(4s) population policy, and
adds the three atomic elastic blocks and three ordinary owner pairs. It
verifies the frozen source hashes and loaded library identities before
writing `atomic-spec.json`. The conversion report records source/library
pins and the production-grid node count. Numerical cross-section downloads
remain local; the repository contains their pins and process identities.

## Rate-only N2 dissociation

Entries 18 and 19 integrate the separate SS (2 N) and SD (N + N(2D)) curves
from the pinned IST-Lisbon `N2_LXCat_extra.txt` over the same solved EEDF.
The source sha256 is `f2d2433c76c6e6667dc843069a53c0d7a7f78a5e8e183300ae967b1f7c63230a`.
Cosby 1993 (doi:10.1063/1.464385) and Zipf–McLaughlin 1978
(doi:10.1016/0032-0633(78)90066-1) are the source chain reported by Guerra 2019
(doi:10.1088/1361-6595/ab252c). The local header says “Check notes”; the branch
numbers were not independently reconstructed from those publications.

This is a declared complete-N2-energy-inventory approximation. Existing losses,
including sing-sup, cover the energy; the event curves and thresholds differ
from sing-sup, so they are not equivalent. The SS/SD thresholds are 10/12 eV
versus sing-sup at 13 eV. At 14/18/20 eV the SS fractions are respectively
0.578815, 0.222931 and 0.00711826. A constant branching yield is inappropriate.
No extra Boltzmann collision or electron energy term is added. Source fingerprints
are separate from the energy-operator fingerprint, with complete coverage and
unique chemical owners enforced in the table metadata. Runtime refuses a
rate-only owner declared as an electron-energy entry. Quantitative branch
uncertainty is not adopted. Physical N production and pooling sensitivity still
require the power-consistent discharge calculation.
