# PlasmaNitrogenExcited

Thirteen irreversible molecular loss/coupling entries for the existing `N2A`
(A 3Sigma_u+), `N2ap` (a-prime 1Sigma_u-), `N2a` (a 1Pi_g),
and `N2w` (w 1Delta_u) labels.
Use with `PlasmaNitrogen` and `PlasmaArgonExcited`; the latter owns
C→B→A radiation. No existing species identity or rate is changed.
No electron-impact owner is missing for B/C in the pinned nitrogen map:
class-A rows 14, 15, 17 and 21 already have owners. No electron entries,
ThirdBody representation, or ground-state vibrational kinetics are added here.

## Scope and sources

The constants are room-temperature measurements/evaluations, declared valid
at 298–300 K. Application at 600 K is an unvalidated constant-rate extension
(except the explicitly temperature-dependent spectroscopic reverse factor),
not a measured temperature law. Each entry records the uncertainty and the
state, product or collider transfer. Rates below use particle units, m3/s
for binary collisions and s−1 for radiation. Stored bimolecular Arrhenius
prefactors use molar units and N_A=6.02214179e23 mol−1, matching RMG.

| Process | Selected rate | Source | Convention / uncertainty |
|---|---:|---|---|
| A + N2 → 2 N2 | 3e-24 | [Herron 1999](https://doi.org/10.1063/1.556043), Table 7, p.1476 | `A_V0_QUENCH_BOUND`: evaluated **upper limit**, not a central value; v=0 transferred to manifold |
| A + A → C + N2 | 1.5e-16 | [Piper 1988 I](https://doi.org/10.1063/1.454649) | `POOL_V0_TO_MANIFOLD`; ±0.4e-16 for v=0 pair |
| A + A → B + N2 | 7.7e-17 | [Piper 1988 II](https://doi.org/10.1063/1.454388) | Same convention; no aggregate uncertainty transcribed; v=1-containing pairs yield about 3× more B |
| a + N2 → a′ + N2 | 2.2e-17 | [Marinelli 1989](https://doi.org/10.1063/1.456012), Table I | `SINGLET_V0_COUPLING`; ±0.2e-17 on total removal, principal-fate assignment |
| a + Ar → a′ + Ar | 1.3e-17 | Marinelli, Table I | `SINGLET_TOTAL_TO_AP`; ±0.1e-17 on total removal, unit a′ yield assumed |
| a′ + N2 → a + N2 | 2.2e-17 × 2 exp(−1743.797574924/T) | Marinelli normalization; [Piper 1987](https://doi.org/10.1063/1.453223), Eq. (5) | `SINGLET_SPECTROSCOPIC_REVERSE`, Ar spectroscopic ratio transferred to N2 |
| a′ + Ar → a + Ar | 1.3e-17 × 2 exp(−1743.797574924/T) | Same normalization/ratio sources | Same convention; reverse is derived, not measured |
| a′ + N2 → B + N2 | 1.9e-19 | Piper 1987, Table I | `AP_N2_TO_B`; ±0.5e-19 total loss; B yield follows [Guerra 2019](https://doi.org/10.1088/1361-6595/ab252c) N6 as a product convention |
| a → N2 | 18000 | Guerra 2019, N26 | `SINGLET_RADIATIVE_LUMP`; no numerical uncertainty in selected table |
| a → a′ | 191 | Guerra 2019, N27 | Same convention; exchange, not terminal singlet loss |
| A → N2 | 1/1.9 | [Lofthus–Krupenie 1977](https://doi.org/10.1063/1.555546), Table 82 | `A_V0_RADIATIVE_LUMP`; v=0 lifetime, no uncertainty in selected row |
| w → a | 650 | Guerra 2019, Table 5, N28 | `SINGLET_RADIATIVE_LUMP`; adopted manifold rate, no numerical uncertainty supplied |
| w + N2 → a + N2 | 1e-17 | Guerra 2019, Table 5, N4 | `W_N2_TO_A`; adopted model coefficient, unit a yield, no numerical uncertainty supplied |

Each pooling branch has event rate r=k n_A², gross A removal 2r, and
post-C/B-cascade net A removal r because one A returns. Do not add a total
pooling coefficient on top of these branches. HIR and other unlisted products
are **not covered**. The reverse singlet factor uses 1212 cm−1 and Pi degeneracy
2; deriving it from RMG's shifted ground-state entropy would implement a
different model. Opposite irreversible singlet entries are marked duplicate
for library duplicate bookkeeping; both physical directions remain explicit.

For the Ar singlet branching sensitivity, let f range from 0 to 1: keep total
a removal 1.3e-17 fixed, route f to a′ and 1−f to N2, and scale the Ar reverse
coupling by f. Thus direct terminal a loss changes from 0 to k_Ar n_Ar while
gross a loss is unchanged; exchange alone must not be counted as terminal
singlet loss. All vibrational ground products are lumped to `N2`; radiation
is not a gas-heating closure.

The w radiation and N2-collider coefficients are taken from Guerra's reviewed
model, which attributes them to Fraser et al. (1988) and Sá–Loureiro (1997),
respectively. Both transfer w to a; neither is a terminal singlet loss.
They are adopted electronic-manifold rates, not newly verified state-specific
measurements. The radiation closes w even when its N2 collider is scarce.
`W_AR_COUPLING_SOURCE_GAP`: no evaluated w+Ar→a+Ar coefficient was verified
in the reviewed sources. Omit that channel; do not copy the w+N2 coefficient,
infer a zero upper bound, or substitute data for the distinct triplet W state.

## Neutral walls

Copy this declaration into the plasma reactor, merging with the companion
Ar declarations. Geometry belongs to the reactor, not the kinetic library.

```python
wallNeutralDiffusion = {
    'N2A': {'product': 'N2', 'diffusivity': (4.957867365474875e20, '1/(m*s)')},
    'N2ap': {'product': 'N2', 'diffusivity': (4.957867365474875e20, '1/(m*s)')},
    'N2a': {'product': 'N2', 'diffusivity': (4.957867365474875e20, '1/(m*s)')},
    'N2w': {'product': 'N2', 'diffusivity': (4.957867365474875e20, '1/(m*s)')},
}
```

[Piper 1982](https://doi.org/10.1063/1.444158), p.2375, gives
D(A(v=0) in Ar)=153±10 cm2/s at 1 Torr, 298 K (adopting Levron–Phelps).
This gives the declared constant Dn=4.957867365474875e20 m−1 s−1.
`N2_COMMON_AR_BATH_DIFFUSION` transfers A transport to a-prime, a and w, and
pure-Ar transport to x_N2≤0.2. The ±6.5% measurement error does not bound
these transfers or temperature extrapolation. Do not apply the flow-reactor
0.62 correction to the spatially uniform model. The existing operator returns
one ground N2 per lost excited molecule, with frequency Dn/(n Lambda²).

The planning table used Lambda=20.3 mm. The real-job cylinder R=5 cm,
L=30 cm instead gives Lambda=[(2.405/R)²+(pi/L)²]^(-1/2) in the engine
(the first Bessel zero is rounded to 2.405).
Compare using the actual geometry; do not silently equate these lengths.

A+N2 zero-to-bound sensitivity: at 300 K and the most restrictive planning
point (10 Torr, x_N2=0.2), removing the bound subtracts 0.19313 s−1 versus
3.7377 s−1 wall loss (5.17% of wall); all other planning points have a smaller
ratio. This is about twentyfold below wall, not a guarantee of unchanged n_A.

## Explicit source gaps

`A_AR_QUENCH_SOURCE_GAP`: omit A+Ar terminal quenching; no verified evaluated
coefficient was selected. Ar is generally reported as an inefficient A
quencher, but that statement is not a numerical upper bound. At 300 K,
10 Torr, x_N2=0.01, Lambda=20.3 mm, k equal to wall loss is
1.173e-23 m3/s (scale with actual wall frequency divided by n_Ar).
The required real-job sensitivity injects k=1e-23 only in the test network,
never in this library, and reports the change in n_A at all three compositions.

No independent terminal a′+Ar coefficient is selected; the explicit coupled
kinetics already accounts for its indirect decay. a′→X radiation is zero
nominal (omitted). Piper's conditional lifetime bound is not a measured
radiative rate: with the chosen a→X rate, its conditional bound corresponds
to about 63 s−1, not the inverse of the older 23 ms lifetime quoted with an
80 microsecond a lifetime.

## Atomic nitrogen: required, supplied separately

Atomic nitrogen cannot be omitted from the intended physical model. Its N(4S)
species, atom-conserving wall recombination (N→1/2 N2), A+N quenching and
dissociative-pooling sensitivity are supplied by a separate change.

The earlier fixed-row diagnostic at x_N2=0.01, 25 Td, Tg=298.15 K, 5 Torr,
R=5 cm and L=30 cm, with maintained n_e=1e17 m^-3, gave steady
n_A=4.80105e19 m^-3. With k_D=2e-16 m3/s, S_N=2 k_D n_A²=9.22004e23
m^-3 s^-1. For gamma_N=1e-4, lambda_N=0.728935 s^-1 and the net
post-cascade A loss frequency=10906.3 s^-1, the posterior ratio
4.4e-17 n_N/(A loss frequency)=5102.91, far above 0.05. At gamma_N=1e-2
the ratio is 401.177. The linear posterior n_N exceeds the nitrogen inventory;
it diagnoses failure of a small-perturbation omission, not a physical N density.
The k_D value is a high-pressure model transfer from
[Jans 2021](https://doi.org/10.1088/1361-6595/abcc7c), not an evaluated
low-pressure dissociation rate. Lambda_N uses Guerra Eq. (33) with
Chapman–Enskog N-in-Ar diffusion; it is not an implemented atomic-wall model.

**Forcing caveat:** fixed n_e at 25 Td is not consistent with the proposed
0.5 W discharge. This replay drives A production of order 1e24 m^-3 s^-1,
whereas the earlier power-ceiling estimate was at most 2e20 m^-3 s^-1.
The resulting n_A therefore overstates the intended deck by orders of
magnitude. These are stress-test numbers, not a power-coupled discharge
prediction; they do not establish an omission bound. The atomic-N requirement
is retained rather than attempting to certify omission with this forcing.

## Worker verification

`test/test_plasma_nitrogen_excited.py` checks all thirteen entries, exact species
identities, rates/units, sources/conventions, balance, companion coexistence,
same-state pooling stoichiometry, and the four nonzero wall residuals.
A separate decay test checks the combined w radiation/collisional frequency
and one-to-one transfer to a.
Before the companion branch is merged, set `PLASMA_ARGON_EXCITED_ROOT` to that
checkout. The real-job test reuses its pinned pure-Ar 60 Td EEDF fixture,
admits all new channels, and runs to 1 ns at x_N2=0.01, 0.05, 0.2 with Chemkin
and native profiles enabled. This is an admission/integration check, not a
production EEDF or discharge-sustainment validation. The steady molecular
jobs and per-state loss tables are separate evidence requirements.
The maintained-density forcing subclass stays outside this repository. Accepted
integration data can be used while the engine's post-integration reverse-rate
collision audit is fixed separately; they do not imply clean RMG.execute
completion. The native power-balance binding ambiguity also remains an engine
issue, separate from this molecular library.
