#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaAtomicNitrogen"
shortDesc = "Resolved N(4S), N(2D), N(2P) chemistry for Ar/N2 plasmas"
longDesc = """Irreversible atomic nitrogen channels with evaluated source rates and explicit product/state/temperature conventions. See README.md; optional dissociative pooling is separate."""

entry(
    index = 1,
    label = 'N2A + N => N2 + N(2P)',
    reversible = False,
    kinetics = Arrhenius(A=(26497423.876, 'm^3/(mol*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'A_N_DOMINANT_P',
    longDesc = """Herron (1999), doi:10.1063/1.556043. Table 7, pp.1473-1475. Evaluated removal at 298 K; uncertainty factor 1.5. Convention: all A+N events produce the suggested dominant N(2P) product; unit yield is not measured. Vibrational N2 products are lumped to ground N2. Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 2,
    label = 'N(2D) + N2 => N + N2',
    reversible = False,
    kinetics = Arrhenius(A=(10237.641043, 'm^3/(mol*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'D_N2_QUENCH',
    longDesc = """Herron (1999), doi:10.1063/1.556043. Table 2, p.1459. Evaluated 1.7e-14 cm3 molecule-1 s-1, uncertainty factor 1.5 at 298 K. Convention: physical quenching to N(4S). Conflicting reported temperature slopes are not adopted. Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 3,
    label = 'N(2P) + N2 => N + N2',
    reversible = False,
    kinetics = Arrhenius(A=(30.11070895, 'm^3/(mol*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'P_N2_QUENCH',
    longDesc = """Herron (1999), doi:10.1063/1.556043. Table 5, p.1464. Evaluated 5e-17 cm3 molecule-1 s-1, uncertainty factor 5 at 298 K. Convention: quenching returns N(4S); no transfer of Guerra N13 (6e-20 m3/s). Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 4,
    label = 'N(2P) + N => N + N',
    reversible = False,
    kinetics = Arrhenius(A=(270996.38055, 'm^3/(mol*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'P_N_BRANCH_CONVENTION',
    longDesc = """Herron (1999), doi:10.1063/1.556043. Table 5: TOTAL removal 6e-19 m3/s with uncertainty factor 3. Products were not resolved in that evaluation. Convention: use the 3:1 ground:D product ratio of Guerra (2019), doi:10.1088/1361-6595/ab252c, N10:N11, renormalized to the Herron evaluated total. This entry is 0.75 of that total; the ratio is a model transfer, not an evaluated yield. Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 5,
    label = 'N(2P) + N => N(2D) + N',
    reversible = False,
    kinetics = Arrhenius(A=(90332.12685, 'm^3/(mol*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'P_N_BRANCH_CONVENTION',
    longDesc = """Herron (1999), doi:10.1063/1.556043. Table 5: TOTAL removal 6e-19 m3/s with uncertainty factor 3. Convention: 0.25 of that total returns N(2D), using the 3:1 product ratio in Guerra (2019), doi:10.1088/1361-6595/ab252c, N10:N11. Product branching is unresolved in Herron and this ratio is a model transfer, not an evaluated yield. Do not add another total removal channel. Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 6,
    label = 'N + N + N2 => N2B + N2',
    reversible = False,
    kinetics = Arrhenius(A=(299.9214056804086, 'm^6/(mol^2*s)'), n=0,
                         Ea=(-4157.236, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'N_RECOMB_N2_B',
    longDesc = """Guerra (2019), doi:10.1088/1361-6595/ab252c, Table 5 N22. Selected expression k=8.27e-46 exp(500/T) m6/s; no numerical uncertainty given in that row. Convention: explicit N2 collider and N2(B) product, with its cascade owned by PlasmaArgonExcited. Do not replace the exponent with a different evaluation or add a ThirdBody. Event rate k*n_N^2*n_N2 removes two N atoms. The 300-600 K use is an adopted model law, not a new validation of the underlying room-temperature measurements.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 7,
    label = 'N + N + Ar => N2B + Ar',
    reversible = False,
    kinetics = Arrhenius(A=(690.0, 'm^6/(mol^2*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'N_RECOMB_AR_HALF_B_X',
    longDesc = """Campbell and Thrush (1967), doi:10.1098/rspa.1967.0014. Total Ar-collider coefficient (1.38 +/- 0.11)e15 cm6 mol-2 s-1 at 298 K. Convention: split the total equally between N2(B) and N2(X), reflecting the source statement about half via B. Branch uncertainty is not quantified; +/-0.11 applies to the total. Each entry is k/2; no additional total or ThirdBody. Event rate consumes two N atoms. Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 8,
    label = 'N + N + Ar => N2 + Ar',
    reversible = False,
    kinetics = Arrhenius(A=(690.0, 'm^6/(mol^2*s)'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'N_RECOMB_AR_HALF_B_X',
    longDesc = """Campbell and Thrush (1967), doi:10.1098/rspa.1967.0014. Total Ar-collider coefficient (1.38 +/- 0.11)e15 cm6 mol-2 s-1 at 298 K. Convention: split the total equally between N2(B) and N2(X), reflecting the source statement about half via B. Branch uncertainty is not quantified; +/-0.11 applies to the total. Each entry is k/2; no additional total or ThirdBody. Event rate consumes two N atoms. Constant 298 K coefficient extended to 300-600 K by convention, not a measured temperature law.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 9,
    label = 'N(2D) => N',
    reversible = False,
    kinetics = Arrhenius(A=(1.26726e-05, 's^-1'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'D_TO_S_RADIATION',
    longDesc = """NIST Atomic Spectra Database, doi:10.18434/T4W30F, N I forbidden transitions, TP reference T7370, retrieved 2026-11-05. J=3/2 A(M1,E2)=(1.60e-5,4.34e-6); J=5/2=(9.71e-7,6.59e-6) s-1. ASD accuracy B (<=10%). Convention: sum M1/E2 and lower-J branches, average over upper fine-structure levels with statistical weights 2J+1 (D:4,6; P:2,4). The fine-structure populations are not solved. Uncertainty includes the quoted ASD accuracy and an unquantified manifold-population transfer. Photons leave; no gas/electron heating credit.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 10,
    label = 'N(2P) => N',
    reversible = False,
    kinetics = Arrhenius(A=(0.0052, 's^-1'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'P_TO_S_RADIATION',
    longDesc = """NIST Atomic Spectra Database, doi:10.18434/T4W30F, N I forbidden transitions, TP reference T7370, retrieved 2026-11-05. J=3/2 A=6.5e-3; J=1/2 A=2.6e-3 s-1. ASD accuracy D (<=50%). Convention: sum M1/E2 and lower-J branches, average over upper fine-structure levels with statistical weights 2J+1 (D:4,6; P:2,4). The fine-structure populations are not solved. Uncertainty includes the quoted ASD accuracy and an unquantified manifold-population transfer. Photons leave; no gas/electron heating credit.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 11,
    label = 'N(2P) => N(2D)',
    reversible = False,
    kinetics = Arrhenius(A=(0.08816333333333333, 's^-1'), n=0,
                         Ea=(0, "J/mol"), Tmin=(298,"K"), Tmax=(600,"K")),
    shortDesc = 'P_TO_D_RADIATION',
    longDesc = """NIST Atomic Spectra Database, doi:10.18434/T4W30F, N I forbidden transitions, TP reference T7370, retrieved 2026-11-05. J=3/2 sum A=1.02e-3+6e-2+1.81e-3+2.56e-2; J=1/2 sum A=3.45e-2+1.13e-3+5.2e-2 s-1. ASD accuracy C (<=25%). Convention: sum M1/E2 and lower-J branches, average over upper fine-structure levels with statistical weights 2J+1 (D:4,6; P:2,4). The fine-structure populations are not solved. Uncertainty includes the quoted ASD accuracy and an unquantified manifold-population transfer. Photons leave; no gas/electron heating credit.
Particle-to-molar conversion uses N_A=6.02214179e23 mol^-1 to power (reactant order - 1).""",
)

entry(
    index = 12,
    label = 'e- + N => e- + N(2D)',
    reversible = False,
    kinetics = EEDFChannel(
        process='e + N(4S) <-> e + N(2D), Excitation',
        collision_set="IST-Lisbon-N-Wang2014",
        side='ine',
    ),
    shortDesc = "Resolved atomic nitrogen electron excitation or superelastic owner",
    longDesc = 'Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714. IST-Lisbon atomic-N data with logarithmic extension to 1 keV; source threshold 2.39071 eV, upper/lower degeneracy 2.5. Convention: resolved term populations with source thresholds retained; the reverse rate follows source detailed balance. This is an ordinary Boltzmann collision owner with full electron energy accounting from the table. Do not also declare a separate electron energy term or a thermal reverse. Uncertainty: no numerical cross-section uncertainty adopted; no new validation of the extrapolation. Input cross sections and the collision map must be fingerprinted by the table-generation specification.',
)

entry(
    index = 13,
    label = 'e- + N(2D) => e- + N',
    reversible = False,
    kinetics = EEDFChannel(
        process='e + N(4S) <-> e + N(2D), Excitation',
        collision_set="IST-Lisbon-N-Wang2014",
        side='sup',
    ),
    shortDesc = "Resolved atomic nitrogen electron excitation or superelastic owner",
    longDesc = 'Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714. IST-Lisbon atomic-N data with logarithmic extension to 1 keV; source threshold 2.39071 eV, upper/lower degeneracy 2.5. Convention: resolved term populations with source thresholds retained; the reverse rate follows source detailed balance. This is an ordinary Boltzmann collision owner with full electron energy accounting from the table. Do not also declare a separate electron energy term or a thermal reverse. Uncertainty: no numerical cross-section uncertainty adopted; no new validation of the extrapolation. Input cross sections and the collision map must be fingerprinted by the table-generation specification.',
)

entry(
    index = 14,
    label = 'e- + N => e- + N(2P)',
    reversible = False,
    kinetics = EEDFChannel(
        process='e + N(4S) <-> e + N(2P), Excitation',
        collision_set="IST-Lisbon-N-Wang2014",
        side='ine',
    ),
    shortDesc = "Resolved atomic nitrogen electron excitation or superelastic owner",
    longDesc = 'Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714. IST-Lisbon atomic-N data with logarithmic extension to 1 keV; source threshold 3.5676 eV, upper/lower degeneracy 1.5. Convention: resolved term populations with source thresholds retained; the reverse rate follows source detailed balance. This is an ordinary Boltzmann collision owner with full electron energy accounting from the table. Do not also declare a separate electron energy term or a thermal reverse. Uncertainty: no numerical cross-section uncertainty adopted; no new validation of the extrapolation. Input cross sections and the collision map must be fingerprinted by the table-generation specification.',
)

entry(
    index = 15,
    label = 'e- + N(2P) => e- + N',
    reversible = False,
    kinetics = EEDFChannel(
        process='e + N(4S) <-> e + N(2P), Excitation',
        collision_set="IST-Lisbon-N-Wang2014",
        side='sup',
    ),
    shortDesc = "Resolved atomic nitrogen electron excitation or superelastic owner",
    longDesc = 'Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714. IST-Lisbon atomic-N data with logarithmic extension to 1 keV; source threshold 3.5676 eV, upper/lower degeneracy 1.5. Convention: resolved term populations with source thresholds retained; the reverse rate follows source detailed balance. This is an ordinary Boltzmann collision owner with full electron energy accounting from the table. Do not also declare a separate electron energy term or a thermal reverse. Uncertainty: no numerical cross-section uncertainty adopted; no new validation of the extrapolation. Input cross sections and the collision map must be fingerprinted by the table-generation specification.',
)

entry(
    index = 16,
    label = 'e- + N(2D) => e- + N(2P)',
    reversible = False,
    kinetics = EEDFChannel(
        process='e + N(2D) <-> e + N(2P), Excitation',
        collision_set="IST-Lisbon-N-Wang2014",
        side='ine',
    ),
    shortDesc = "Resolved atomic nitrogen electron excitation or superelastic owner",
    longDesc = 'Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714. IST-Lisbon atomic-N data with logarithmic extension to 1 keV; source threshold 1.177 eV, upper/lower degeneracy 0.6. Convention: resolved term populations with source thresholds retained; the reverse rate follows source detailed balance. This is an ordinary Boltzmann collision owner with full electron energy accounting from the table. Do not also declare a separate electron energy term or a thermal reverse. Uncertainty: no numerical cross-section uncertainty adopted; no new validation of the extrapolation. Input cross sections and the collision map must be fingerprinted by the table-generation specification.',
)

entry(
    index = 17,
    label = 'e- + N(2P) => e- + N(2D)',
    reversible = False,
    kinetics = EEDFChannel(
        process='e + N(2D) <-> e + N(2P), Excitation',
        collision_set="IST-Lisbon-N-Wang2014",
        side='sup',
    ),
    shortDesc = "Resolved atomic nitrogen electron excitation or superelastic owner",
    longDesc = 'Wang, Zatsarinny and Bartschat (2014), doi:10.1103/PhysRevA.89.062714. IST-Lisbon atomic-N data with logarithmic extension to 1 keV; source threshold 1.177 eV, upper/lower degeneracy 0.6. Convention: resolved term populations with source thresholds retained; the reverse rate follows source detailed balance. This is an ordinary Boltzmann collision owner with full electron energy accounting from the table. Do not also declare a separate electron energy term or a thermal reverse. Uncertainty: no numerical cross-section uncertainty adopted; no new validation of the extrapolation. Input cross sections and the collision map must be fingerprinted by the table-generation specification.',
)
