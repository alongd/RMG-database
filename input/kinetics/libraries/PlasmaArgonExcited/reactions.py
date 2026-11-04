#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaArgonExcited"
shortDesc = "Reduced room-temperature heavy-particle losses of the four Ar(4s) states"
longDesc = """
Ars = 1s5 (3P2); Ar(1s4) = 3P1; Ar(1s3) = 3P0; Ar(1s2) = 1P1.
For isothermal 298-300 K, Ar/N2 at 5 Torr and x_N2=0.01-0.2.
The 298 K use is an explicitly constant-rate extension of room-temperature data,
not a measured temperature law. All entries are irreversible: the electronic
state thermo does not justify thermal detailed balance for this reduced model.
AR4S_N2_PRODUCT_SPLIT transfers a mixed-metastable C/B measurement to each state.
See README.md for source tables, uncertainties, omissions and deck declarations.
Do not combine this library with PlasmaArgonLegacy.
"""

entry(
    index = 1,
    label = "Ars + N2 => Ar + N2C",
    reversible = False,
    kinetics = Arrhenius(A=(10839855.222, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table I (3P2), footnote g, doi:10.1063/1.436447. Total = 3.6e-17 m^3/(particle*s), 300 K.
Metastable relative uncertainty +/-10%; absolute reliability +/-20%.
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 2,
    label = "Ars + N2 => Ar + N2B",
    reversible = False,
    kinetics = Arrhenius(A=(10839855.222, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table I (3P2), footnote g, doi:10.1063/1.436447. Total = 3.6e-17 m^3/(particle*s), 300 K.
Metastable relative uncertainty +/-10%; absolute reliability +/-20%.
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 3,
    label = "Ar(1s4) + N2 => Ar + N2C",
    reversible = False,
    kinetics = Arrhenius(A=(2408856.716, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table II (3P1), Ref. 20, doi:10.1063/1.436447. Total = 8e-18 m^3/(particle*s), 300 K.
Resonance-state uncertainty is not supplied in the comparison table; the metastable +/-20% is not assigned to it.
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 4,
    label = "Ar(1s4) + N2 => Ar + N2B",
    reversible = False,
    kinetics = Arrhenius(A=(2408856.716, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table II (3P1), Ref. 20, doi:10.1063/1.436447. Total = 8e-18 m^3/(particle*s), 300 K.
Resonance-state uncertainty is not supplied in the comparison table; the metastable +/-20% is not assigned to it.
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 5,
    label = "Ar(1s3) + N2 => Ar + N2C",
    reversible = False,
    kinetics = Arrhenius(A=(4817713.432, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table I (3P0), Ref. 2a, doi:10.1063/1.436447. Total = 1.6e-17 m^3/(particle*s), 300 K.
Table I metastable relative uncertainty +/-10%; absolute reliability +/-20%; 3P0 value attributed to Piper et al. (1973).
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 6,
    label = "Ar(1s3) + N2 => Ar + N2B",
    reversible = False,
    kinetics = Arrhenius(A=(4817713.432, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table I (3P0), Ref. 2a, doi:10.1063/1.436447. Total = 1.6e-17 m^3/(particle*s), 300 K.
Table I metastable relative uncertainty +/-10%; absolute reliability +/-20%; 3P0 value attributed to Piper et al. (1973).
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 7,
    label = "Ar(1s2) + N2 => Ar + N2C",
    reversible = False,
    kinetics = Arrhenius(A=(16259782.833, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table II (1P1), Ref. 20, doi:10.1063/1.436447. Total = 5.4e-17 m^3/(particle*s), 300 K.
Resonance-state uncertainty is not supplied in the comparison table; the metastable +/-20% is not assigned to it.
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 8,
    label = "Ar(1s2) + N2 => Ar + N2B",
    reversible = False,
    kinetics = Arrhenius(A=(16259782.833, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Velazco 1978 total; declared AR4S_N2_PRODUCT_SPLIT (one-half)",
    longDesc = """
Velazco, Kolts and Setser, J. Chem. Phys. 69, 4357-4373 (1978),
Table II (1P1), Ref. 20, doi:10.1063/1.436447. Total = 5.4e-17 m^3/(particle*s), 300 K.
Resonance-state uncertainty is not supplied in the comparison table; the metastable +/-20% is not assigned to it.
AR4S_N2_PRODUCT_SPLIT: nominal fC=fB=0.5, transferred to this state from
mixed-metastable C/B=1.0 +/-0.2, Kolts, Brashears and Setser (1977),
J. Chem. Phys. 67, 2931-2933, as reported by Klages et al. (2020). This is not a per-state
branching measurement. Sensitivity fC in [0,1], fB=1-fC leaves total Ar loss
unchanged. No dissociation branch. Rate is constant only near room temperature.
A_molar = k_particle * 0.5 * N_A; N_A=6.02214179e23 mol^-1 (RMG particle/mole convention).
""",
)

entry(
    index = 9,
    label = "Ar(1s2) + Ar => Ar(1s3) + Ar",
    reversible = False,
    kinetics = Arrhenius(A=(28665.3949204, 'm^3/(mol*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 350; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 350, citing Firestone, Oka and Takao (1979).
Particle rate = 4.76e-20 m^3/(particle*s); multiply by N_A
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
""",
)

entry(
    index = 10,
    label = "Ar(1s3) + Ar => Ar(1s4) + Ar",
    reversible = False,
    kinetics = Arrhenius(A=(3191.7351487, 'm^3/(mol*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 351; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 351, citing Kolts and Setser (1978).
Particle rate = 5.3e-21 m^3/(particle*s); multiply by N_A
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
""",
)

entry(
    index = 11,
    label = "Ar(1s4) + Ar => Ars + Ar",
    reversible = False,
    duplicate = True,
    kinetics = Arrhenius(A=(9033.212685, 'm^3/(mol*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 352; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 352, citing Millet et al. (1982).
Particle rate = 1.5e-20 m^3/(particle*s); multiply by N_A
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
""",
)

entry(
    index = 12,
    label = "Ars + Ar => Ar(1s4) + Ar",
    reversible = False,
    duplicate = True,
    kinetics = Arrhenius(A=(1505.5354475, 'm^3/(mol*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 354; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 354, citing Millet et al. (1982).
Particle rate = 2.5e-21 m^3/(particle*s); multiply by N_A
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
""",
)

entry(
    index = 13,
    label = "Ars + Ar => Ar + Ar",
    reversible = False,
    kinetics = Arrhenius(A=(9033.212685, 'm^3/(mol*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 355; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 355, citing Millet et al. (1982).
Particle rate = 1.5e-20 m^3/(particle*s); multiply by N_A
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
""",
)

entry(
    index = 14,
    label = "Ars + Ar + Ar => Ar + Ar + Ar",
    reversible = False,
    kinetics = Arrhenius(A=(4714.604926052372, 'm^6/(mol^2*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 356; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 356, citing Millet et al. (1982).
Particle rate = 1.3e-44 m^6/(particle^2*s); multiply by N_A squared
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
Eliminated excimer: formation followed by photon loss is collapsed to ground Ar.
No explicit excimer population, reverse recombination or gas-heating model.
""",
)

entry(
    index = 15,
    label = "Ar(1s4) + Ar + Ar => Ar + Ar + Ar",
    reversible = False,
    kinetics = Arrhenius(A=(543.9928760829661, 'm^6/(mol^2*s)'),
                         n=0, Ea=(0, 'J/mol'), Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 353; reduced directional Ar network",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 353, citing Millet et al. (1982).
Particle rate = 1.5e-45 m^6/(particle^2*s); multiply by N_A squared
for molar units, N_A=6.02214179e23 mol^-1 (RMG convention).
REDUCED_AR4S_HEAVY_NETWORK: directional irreversible coefficient, not a
thermodynamic reverse. The compilation supplies no numerical uncertainty
or fitted temperature law for this row. Restricted here to 298-300 K;
the two-Kelvin extension to the 298 K deck is a declared approximation.
Eliminated excimer: formation followed by photon loss is collapsed to ground Ar.
No explicit excimer population, reverse recombination or gas-heating model.
""",
)

entry(
    index = 16,
    label = "Ars + Ars => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(722657014.8, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 278; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 278, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=1.2e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 17,
    label = "Ars + Ar(1s4) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(1264649775.8999999, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 279; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 279, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=2.1e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 18,
    label = "Ars + Ar(1s3) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(2529299551.7999997, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 280; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 280, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=4.2e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 19,
    label = "Ars + Ar(1s2) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(2529299551.7999997, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 281; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 281, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=4.2e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 20,
    label = "Ar(1s4) + Ar(1s4) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(1264649775.8999999, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 282; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 282, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=2.1e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 21,
    label = "Ar(1s4) + Ar(1s3) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(1264649775.8999999, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 283; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 283, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=2.1e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 22,
    label = "Ar(1s4) + Ar(1s2) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(1264649775.8999999, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 284; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 284, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=2.1e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 23,
    label = "Ar(1s3) + Ar(1s3) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(722657014.8, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 285; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 285, citing
Kolokolov, Kudrjavtsev and Blagoev, Phys. Scr. 50, 371-402 (1994).
REDUCED_AR4S_HEAVY_NETWORK: k=1.2e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 24,
    label = "Ar(1s3) + Ar(1s2) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(1264649775.8999999, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 286; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 286, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=2.1e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 25,
    label = "Ar(1s2) + Ar(1s2) => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(A=(1264649775.8999999, 'm^3/(mol*s)'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Stankov 2022 Table 3 row 287; pooling event coefficient",
    longDesc = """
Stankov et al., Plasma Sources Sci. Technol. 31, 125002 (2022),
doi:10.1088/1361-6595/ac9332, Table 3 row 287, citing
Blagoev and Popov, Phys. Lett. A 70, 416-418 (1979).
REDUCED_AR4S_HEAVY_NETWORK: k=2.1e-15 m^3/(particle*s); molar A=k*N_A,
N_A=6.02214179e23 mol^-1 (RMG convention). This is an event/electron-production
coefficient: r=k*n_i*n_j; for identical partners the atom loss is 2*r.
The convention is explicit in Kolokolov and Blagoev, Phys. Usp. 36, 152-170
(1993), sec. 4.1 and Eq. (2.1), doi:10.1070/PU1993v036n03ABEH002138.
No additional factor of 1/2 is applied. One entry per unordered pair.
The adopted atomic-ion product follows Stankov; the older measurements can
include associative ionization and do not establish ten independent precise
state-resolved measurements. Table 3 gives no numerical uncertainty for this
row. Restricted to 298-300 K; no temperature law inferred.
""",
)

entry(
    index = 26,
    label = "N2C => N2B",
    reversible = False,
    kinetics = Arrhenius(A=(2.74e7, 's^-1'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Guerra 2019 N23, based on Lofthus-Krupenie 1977: lumped C-B emission",
    longDesc = """
Guerra et al., Plasma Sources Sci. Technol. 28, 073001 (2019),
doi:10.1088/1361-6595/ab252c, Table 5 N23, citing Lofthus and Krupenie,
J. Phys. Chem. Ref. Data 6, 113-307 (1977), doi:10.1063/1.555546.
Lofthus-Krupenie Table 82 gives C(v=0) lifetime (3.66 +/-0.05)e-8 s,
a weighted average of measurements. Use the evaluated kinetic model's
vibrationally lumped electronic C->B rate 2.74e7 s^-1 (not a resolved v model).
The v=0 uncertainty is not an uncertainty for transfer to every vibrational
population. Photon escapes; no thermal reverse, no gas-heating claim.
""",
)

entry(
    index = 27,
    label = "N2B => N2A",
    reversible = False,
    kinetics = Arrhenius(A=(2e5, 's^-1'), n=0, Ea=(0, 'J/mol'),
                         Tmin=(298, 'K'), Tmax=(300, 'K')),
    shortDesc = "Guerra 2019 N25: vibrationally lumped B-A emission",
    longDesc = """
Guerra et al., Plasma Sources Sci. Technol. 28, 073001 (2019),
doi:10.1088/1361-6595/ab252c, Table 5 N25, citing Piper,
J. Chem. Phys. 91, 864-873 (1989). Adopt the published vibrationally lumped
B->A rate 2e5 s^-1, not an invented mean of individual vibrational lifetimes.
For comparison, Lofthus and Krupenie, J. Phys. Chem. Ref. Data 6, 113-307
(1977), doi:10.1063/1.555546, Table 82 reports B-state lifetimes varying with v
(about 8 to 4 microseconds); it does not give a unique lumped B lifetime.
Guerra supplies no numerical uncertainty for the lumped N25 coefficient.
Photon escapes; explicitly irreversible. N2(A) loss is outside this library.
""",
)
