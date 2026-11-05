#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaNitrogenExcited"
shortDesc = "Reduced room-temperature N2(A), N2(a-prime), N2(a), N2(w) molecular losses"
longDesc = """
Irreversible heavy-particle and radiative channels at 298-300 K for Ar-rich
N2 mixtures. Room-temperature measurements are transferred to the existing
electronic manifolds with explicit conventions. The A+N2 coefficient is an
upper bound, not a central value. No measured 300-600 K temperature law is
claimed. C->B->A radiation belongs to PlasmaArgonExcited. Atomic nitrogen
is required and supplied separately; see README.md for gaps and the
neutral-wall declaration. No electron channels or ThirdBody entries.
"""

entry(
    index = 1,
    label = "N2A + N2 => N2 + N2",
    reversible = False,
    kinetics = Arrhenius(A=(1.8066425369999999, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "A_V0_QUENCH_BOUND",
    longDesc = """
Herron, J. Phys. Chem. Ref. Data 28, 1453 (1999), Table 7 and p.1476,
doi:10.1063/1.556043. Evaluated upper limit k <= 3e-24 m^3/(particle*s)
for A(v=0) + N2, based on Levron-Phelps. This is NOT a central value.
A_V0_QUENCH_BOUND: use the upper limit as the nominal reduced-model loss;
uncertainty is not a symmetric error bar. Sensitivity is zero to this bound.
Ground vibrational products are lumped to N2. Transfer v=0 to the electronic
manifold; constant extension to 298 K. No measured 300-600 K temperature law
or guaranteed 600 K upper bound is claimed.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 2,
    label = "N2A + N2A => N2C + N2",
    reversible = False,
    kinetics = Arrhenius(A=(90332126.85, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "POOL_V0_TO_MANIFOLD",
    longDesc = """
Piper, J. Chem. Phys. 88, 231 (1988), doi:10.1063/1.454649.
A(v=0)+A(v=0) C-formation event coefficient (1.5 +/- 0.4)e-16
m^3/(particle*s); quoted uncertainty belongs to this branch.
POOL_V0_TO_MANIFOLD: apply the v=0 pair to lumped A; ground vibrational
products are lumped to N2. Event rate k*n_A^2 (no extra half); gross A
loss is 2*k*n_A^2. The companion C->B->A cascade returns one A, so net
post-cascade A loss is k*n_A^2. HIR, dissociation and other unlisted
products are not covered. A(v=1)+A(v=1) C yield is below 5e-17;
this constant is not a vibrational average or a measured temperature law.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 3,
    label = "N2A + N2A => N2B + N2",
    reversible = False,
    kinetics = Arrhenius(A=(46370491.78299999, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "POOL_V0_TO_MANIFOLD",
    longDesc = """
Piper, J. Chem. Phys. 88, 6911 (1988), doi:10.1063/1.454388.
A(v=0)+A(v=0) B-formation event coefficient 7.7e-17 m^3/(particle*s).
No aggregate numerical uncertainty is established here; pairs containing
v=1 produce roughly three times more B.
POOL_V0_TO_MANIFOLD: apply the v=0 pair to lumped A; ground vibrational
products are lumped to N2. Event rate k*n_A^2; gross A loss 2*k*n_A^2,
net post-B->A-cascade loss k*n_A^2. This is one product branch, not total
pooling. HIR, dissociation and other unlisted products are not covered.
Constant room-temperature extension, not a measured 300-600 K law.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 4,
    label = "N2a + N2 => N2ap + N2",
    reversible = False,
    duplicate = True,
    kinetics = Arrhenius(A=(13248711.938, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_V0_COUPLING",
    longDesc = """
Marinelli et al., J. Chem. Phys. 90, 2167 (1989), Table I,
doi:10.1063/1.456012. Total a(v=0) removal (2.2 +/- 0.2)e-17
m^3/(particle*s); quoted uncertainty is experimental removal uncertainty.
SINGLET_V0_COUPLING: assign removal to the inferred principal a->a-prime
coupling channel, and transfer v=0 to the electronic manifold. Ground
vibrational products are lumped to N2. Constant near room temperature;
no measured 300-600 K law. Reverse coupling is a separate irreversible
entry, not inferred from shifted-ground-state RMG thermo.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 5,
    label = "N2a + Ar => N2ap + Ar",
    reversible = False,
    duplicate = True,
    kinetics = Arrhenius(A=(7828784.327, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_TOTAL_TO_AP",
    longDesc = """
Marinelli et al., J. Chem. Phys. 90, 2167 (1989), Table I,
doi:10.1063/1.456012. Total a(v=0) removal (1.3 +/- 0.1)e-17
m^3/(particle*s); quoted uncertainty is for total removal, not branching.
SINGLET_TOTAL_TO_AP: assign all measured loss to a-prime, transferring v=0
to the electronic manifold. Sensitivity f in [0,1] feeds a-prime, (1-f)
feeds ground N2, holding total removal fixed; scale the paired reverse
coupling by f as well. No branching measurement or 300-600 K law is claimed.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 6,
    label = "N2ap + N2 => N2a + N2",
    reversible = False,
    duplicate = True,
    kinetics = Arrhenius(A=(26497423.876, "m^3/(mol*s)"), n=0, Ea=(14498.7561103735, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_SPECTROSCOPIC_REVERSE",
    longDesc = """
Downward normalization: Marinelli et al. (1989), Table I,
doi:10.1063/1.456012, k_down=(2.2 +/- 0.2)e-17 m^3/(particle*s).
SINGLET_SPECTROSCOPIC_REVERSE: k_up/k_down=2*exp(-1743.797574924/T),
using the 1212 cm^-1 separation and Pi degeneracy from Piper (1987),
Eq. (5), doi:10.1063/1.453223. Transfer this Ar spectroscopic relation
to N2. Derived coupling, not a reverse-rate measurement or a relation
from RMG thermo. The normalization uncertainty excludes the unquantified
vibrational-manifold, product-assignment and collider transfers.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 7,
    label = "N2ap + Ar => N2a + Ar",
    reversible = False,
    duplicate = True,
    kinetics = Arrhenius(A=(15657568.654, "m^3/(mol*s)"), n=0, Ea=(14498.7561103735, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_SPECTROSCOPIC_REVERSE",
    longDesc = """
Downward normalization: Marinelli et al. (1989), Table I,
doi:10.1063/1.456012, k_down=(1.3 +/- 0.1)e-17 m^3/(particle*s).
SINGLET_SPECTROSCOPIC_REVERSE: k_up/k_down=2*exp(-1743.797574924/T),
using the 1212 cm^-1 separation and Pi degeneracy from Piper (1987),
Eq. (5), doi:10.1063/1.453223. Derived coupling, not a reverse-rate
measurement or a relation from RMG thermo. Normalization uncertainty
excludes unquantified branching and manifold transfers. Under the
SINGLET_TOTAL_TO_AP sensitivity, multiply this reverse rate by f too.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 8,
    label = "N2ap + N2 => N2B + N2",
    reversible = False,
    kinetics = Arrhenius(A=(114420.69400999999, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "AP_N2_TO_B",
    longDesc = """
Piper, J. Chem. Phys. 87, 1625 (1987), Table I,
doi:10.1063/1.453223. Measured total removal (1.9 +/- 0.5)e-19
m^3/(particle*s); this uncertainty does not measure the B yield.
AP_N2_TO_B: assign all loss to B, following Guerra et al. (2019),
reaction N6, doi:10.1088/1361-6595/ab252c. Unit B yield is a product
convention, not a branching measurement. B->A radiation is in the
companion argon library. Ground vibrational products are lumped to N2;
constant room-temperature extension, not a measured 300-600 K law.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)

entry(
    index = 9,
    label = "N2a => N2",
    reversible = False,
    kinetics = Arrhenius(A=(18000.0, "s^-1"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_RADIATIVE_LUMP",
    longDesc = """
Guerra et al., Plasma Sources Sci. Technol. 28, 073001 (2019),
reaction N26, doi:10.1088/1361-6595/ab252c, 1.8e4 s^-1.
SINGLET_RADIATIVE_LUMP: tabulated electronic-state radiative loss;
ground vibrational products are lumped to N2. No numerical uncertainty
is supplied in the selected table. Photon energy is not gas heating.
This is a terminal singlet loss, distinct from a->a-prime radiation.
""",
)

entry(
    index = 10,
    label = "N2a => N2ap",
    reversible = False,
    kinetics = Arrhenius(A=(191.0, "s^-1"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_RADIATIVE_LUMP",
    longDesc = """
Guerra et al., Plasma Sources Sci. Technol. 28, 073001 (2019),
reaction N27, doi:10.1088/1361-6595/ab252c, 191 s^-1.
SINGLET_RADIATIVE_LUMP: tabulated electronic-state radiative exchange,
not terminal singlet loss. No numerical uncertainty is supplied in the
selected table. Photon energy is not gas heating.
""",
)

entry(
    index = 11,
    label = "N2A => N2",
    reversible = False,
    kinetics = Arrhenius(A=(0.5263157894736842, "s^-1"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "A_V0_RADIATIVE_LUMP",
    longDesc = """
Lofthus and Krupenie, J. Phys. Chem. Ref. Data 6, 113 (1977),
Table 82, doi:10.1063/1.555546: A(v=0) lifetime 1.9 s.
A_V0_RADIATIVE_LUMP: transfer the v=0 lifetime to the electronic manifold,
rate 1/1.9 s^-1. No numerical uncertainty is supplied in that row;
this is not a vibrational average. Ground vibrational products are
lumped to N2. Photon energy is not gas heating.
""",
)


entry(
    index = 12,
    label = "N2w => N2a",
    reversible = False,
    kinetics = Arrhenius(A=(650.0, "s^-1"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "SINGLET_RADIATIVE_LUMP",
    longDesc = """
Guerra et al., Plasma Sources Sci. Technol. 28, 073001 (2019),
Table 5, reaction N28, doi:10.1088/1361-6595/ab252c, 650 s^-1.
The selected review attributes the transition to Fraser, Rawlins and Miller
(1988), J. Chem. Phys. 88, 538-544. Use the review's electronic-manifold
coefficient; no vibrationally resolved lifetime measurement is claimed here.
SINGLET_RADIATIVE_LUMP: w(1Delta_u)->a(1Pi_g) radiative transfer,
not terminal singlet loss; no numerical uncertainty is supplied in the
selected table. Photon energy is not gas heating. Preserve the distinct
existing N2w and N2a species, with one a produced per w removed.
""",
)

entry(
    index = 13,
    label = "N2w + N2 => N2a + N2",
    reversible = False,
    kinetics = Arrhenius(A=(6022141.79, "m^3/(mol*s)"), n=0, Ea=(0.0, "J/mol"),
                         Tmin=(298, "K"), Tmax=(300, "K")),
    shortDesc = "W_N2_TO_A",
    longDesc = """
Guerra et al., Plasma Sources Sci. Technol. 28, 073001 (2019),
Table 5, reaction N4, doi:10.1088/1361-6595/ab252c, 1e-17 m^3/(particle*s).
The selected review attributes this channel to Sa and Loureiro (1997),
J. Phys. D: Appl. Phys. 30, 2320-2330. This is the review's adopted
model coefficient, not a newly established collider-resolved measurement.
W_N2_TO_A: transfer the tabulated electronic-state coefficient to the
existing w(1Delta_u) and a(1Pi_g) manifolds with unit a yield; this is
singlet exchange, not terminal singlet loss. Ground vibrational collider
states are lumped to N2. No numerical uncertainty is supplied in the
selected table, and no measured 300-600 K temperature law is claimed.
Do not transfer this coefficient to Ar without a separate evaluated source.
A_molar = k_particle * N_A; N_A=6.02214179e23 mol^-1.
""",
)
