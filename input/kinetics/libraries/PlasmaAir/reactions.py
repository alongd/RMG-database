#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaAir"
shortDesc = u"PlasmaAir"
longDesc = u"""
Plasma kinetics for air considering Ar / N / O chemistry

Foundational kinetic library for Argon-Nitrogen-Oxygen plasma discharges.
Includes electron-impact ionization/excitation for Argon, charge transfer reactions,
metastable quenching, and key nitrogen-oxygen neutral chemistry.

Rate coefficients have been converted to molar units [cm^3/(mol*s)] from particle units.
Electron temperature dependent rates use the flag Te=True.

Reference legend:
[Park1993]: C. Park, "Review of chemical-kinetic problems of future NASA missions. I - Earth entries", Journal of Thermophysics and Heat Transfer 1993, 7, 385-398. DOI: 10.2514/3.431, https://arc.aiaa.org/doi/epdf/10.2514/3.431
[JensenJones1977]: D.E. Jensen and G.A. Jones, "Reaction Rate Coefficients for Flame Calculations", https://apps.dtic.mil/sti/tr/pdf/ADA047018.pdf
[Gupta1990]: R.N. Gupta, J.M. Yos, R.A. Thompson, K.-P. Lee, NASA Reference Publication 1232, 1990, A Review of Reaction Rates and Thermodynamic and Transport Properties for an 11-Species Air Model for Chemical and Thermal Nonequilibrium Calculations to 30000 K
[Aiken2025] T.T. Aiken, I.D. Boyd, I.V. Adamovich, Phys. Plasmas 2025, 32, 103512. DOI: 10.1063/5.0294530
[Aiken2023] T.T. Aiken, PhD Thesis, Detailed Modeling and Sensitivity Analysis of Non-Equilibrium Thermochemistry in Shock-Heated Gases, 2023, University of Colorado.
[LXCat]: LXCat / Phelps Database (Retrieved April 3, 2025)
[Ozawa2008]: T. Ozawa, J. Zhong, D.A. Levin, Development of kinetic-based energy exchange models for noncontinuum, ionized hypersonic flows, Physics of Fluids 2008, 20, 046102, DOI: 10.1063/1.2907198
[Tanarro2015]: M. Jimenez-Redondo, E. Carrasco, V.J. Herrero, I. Tanarro, Chemistry in glow discharges of H2/O2 mixtures. Diagnostics and modeling, Plasma Sources Sci Technol 2015, 24(1), DOI: 10.1088/0963-0252/24/1/015029
[Golyatina2021]:  R.I. Golyatina, S.A. Marinov, Analytical Cross Section Approximation for Electron Impact Ionization of Alkali and Other Metals, Inert Gases and Hydrogen Atoms, Atoms 2021, 9(90), DOI: 10.3390/atoms9040090
[Verner1995]: D.A. Verner, G.J. Ferland, Atomic data for astrophysics. I. Radiative recombination rates for H-like, He-like, Li-like and Na-like ions over a broad range of temperature, ApJ 1995, arXiv:astro-ph/9509083v1

# can add these:
# Ar+ + H2 <=> ArH+ + H
# ArH+ + H2 <=> Ar + H3+
# Ar+ + O2 <=> Ar + O2+
# N2 + e <=> N2+ + e + e
"""

entry(
    index = 1,
    label = "N2 <=> N + N",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(7.00e+21,'cm^3/(mol*s)'), n=-1.60, Ea=(225000,'cal/mol'), T0=(1,'K')),
                         efficiencies={'[N]': 4.3, '[O]': 4.3, 'N#N': 1.0, '[O][O]': 1.0,
                                       '[N]=O': 1.0, '[N+]': 4.3, '[O+]': 4.3, '[N+]#N': 1.0,
                                       '[O+][O]': 1.0, '[N+]=O': 1.0}),
    shortDesc = u"[Park1993]",
    longDesc = u"""
Table 2
"""
)

entry(
    index = 2,
    label = "N2 + e- <=> N + N + e-",
    kinetics = TwoTemperaturePlasma(A=(3.00e24, "cm^3/(mol*s)"), n=-1.60, Ea_g=(0.0, "kJ/mol"), Ea_e=(941.3, "kJ/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

# entry(
#     index = 3,
#     label = "O2 <=> O + O",
#     kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.00e+21,'cm^3/(mol*s)'), n=-1.50, Ea=(118000,'cal/mol'), T0=(1,'K')),
#                          efficiencies={'[N]': 50, '[O]': 5.0, 'N#N': 1.0, '[O][O]': 1.0,
#                                        '[N]=O': 1.0, '[N+]': 5.0, '[O+]': 5.0, '[N+]#N': 1.0,
#                                        '[O+][O]': 1.0, '[N+]=O': 1.0}),
#     shortDesc = u"[Park1993]",
#     longDesc = u"""
# Table 2
# """
# )

# entry(
#     index = 4,
#     label = "NO <=> N + O",
#     kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(5.00e+15,'cm^3/(mol*s)'), n=-0.0, Ea=(150000,'cal/mol'), T0=(1,'K')),
#                          efficiencies={'[N]': 22, '[O]': 22, 'N#N': 1.0, '[O][O]': 1.0,
#                                        '[N]=O': 22, '[N+]': 22, '[O+]': 22, '[N+]#N': 1.0,
#                                        '[O+][O]': 1.0, '[N+]=O': 1.0}),
#     shortDesc = u"[Park1993]",
#     longDesc = u"""
# Table 2
# """
# )

entry(
    index = 5,
    label = "N + O <=> NO+ + e-",
    kinetics=Arrhenius(A=(5.55e9, 'cm^3/(mol*s)'), n=0.7617, Ea=(66000, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Aiken2025]",
    longDesc = u"""
Table VIII
Associative ionization
"""
)

entry(
    index = 6,
    label = "O + O <=> O2+ + e-",
    kinetics=Arrhenius(A=(1.82e10, 'cm^3/(mol*s)'), n=0.6797, Ea=(160336, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Aiken2025]",
    longDesc = u"""
Table VIII
Associative ionization

Also available in reverse:
    label = "O2+ + e- <=> O + O",
    kinetics = TwoTemperaturePlasma(A=(2.95e16, "cm^3/(mol*s)"), n=-0.7, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
Table 1, N4
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 7,
    label = "N + N <=> N2+ + e-",
    kinetics=Arrhenius(A=(3.485e11, 'cm^3/(mol*s)'), n=0.5067, Ea=(141511, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Aiken2025]",
    longDesc = u"""
Table VIII
Associative ionization
"""
)

entry(
    index = 8,
    label = "NO+ + O <=> O2 + N+",
    kinetics=Arrhenius(A=(1.0e12, 'cm^3/(mol*s)'), n=0.50, Ea=(153400, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Park1993]",
    longDesc = u"""
Table 2
Charge exchange

Also available from:
Arrhenius(A=(1.00e12, 'cm^3/(mol*s)'), n=0.50, Ea=(642.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
Table III
"""
)

entry(
    index = 9,
    label = "N2 + N+ <=> N2+ + N",
    kinetics=Arrhenius(A=(6.99e6, 'cm^3/(mol*s)'), n=01.47, Ea=(26090, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 10,
    label = "O2+ + N <=> N+ + O2",
    kinetics=Arrhenius(A=(8.67e13, 'cm^3/(mol*s)'), n=0.14, Ea=(237.8, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 11,
    label = "NO + O+ <=> O2 + N+",
    kinetics=Arrhenius(A=(1.4e5, 'cm^3/(mol*s)'), n=1.90, Ea=(127.2, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 12,
    label = "O2+ + N2 <=> N2+ + O2",
    kinetics=Arrhenius(A=(9.88e12, 'cm^3/(mol*s)'), n=0.0, Ea=(338.4, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 13,
    label = "O2+ + O <=> O+ + O2",
    kinetics=Arrhenius(A=(1.14e14, 'cm^3/(mol*s)'), n=-0.52, Ea=(156, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 14,
    label = "NO+ + N <=> N2 + O+",
    kinetics=Arrhenius(A=(3.4e13, 'cm^3/(mol*s)'), n=-1.08, Ea=(106.4, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 15,
    label = "NO+ + O2 <=> O2+ + NO",
    kinetics=Arrhenius(A=(2.4e13, 'cm^3/(mol*s)'), n=0.41, Ea=(271.1, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 16,
    label = "NO+ + O <=> O2+ + N",
    kinetics=Arrhenius(A=(7.2e12, 'cm^3/(mol*s)'), n=0.29, Ea=(404.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 17,
    label = "N2 + O+ <=> N2+ + O",
    kinetics=Arrhenius(A=(9.1e13, 'cm^3/(mol*s)'), n=0.36, Ea=(189.6, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 18,
    label = "NO+ + N <=> N2+ + O",
    kinetics=Arrhenius(A=(1.7e13, 'cm^3/(mol*s)'), n=0.40, Ea=(295.1, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 19,
    label = "O + e- => O+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(6.2e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(14.3, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I1
Electron Impact Ionization

Also available from:
    kinetics = TwoTemperaturePlasma(A=(3.9e33, "cm^3/(mol*s)"), n=-3.78, Ea_g=(0.0, "J/mol"), Ea_e=(315000, "cal/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Park1993]",
Table 2
Electron-impact ionization
"""
)

entry(
    index = 20,
    label = "N + e- => N+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(2.5e34, "cm^3/(mol*s)"), n=-3.82, Ea_g=(0.0, "J/mol"), Ea_e=(335050, "cal/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Park1993]",
    longDesc = u"""
Table 2
Electron-impact ionization
"""
)

entry(
    index = 21,
    label = "O+ + e- <=> O",
    kinetics = TwoTemperaturePlasma(A=(1.07e11, "cm^3/(mol*s)"), n=-0.52, Ea_g=(0.0, "J/mol"), Ea_e=(0.0, "cal/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Park1993]",
    longDesc = u"""
Table 2
Radiative recombination
"""
)

entry(
    index = 22,
    label = "N+ + e- <=> N",
    kinetics = TwoTemperaturePlasma(A=(1.52e11, "cm^3/(mol*s)"), n=-0.48, Ea_g=(0.0, "J/mol"), Ea_e=(0.0, "cal/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Park1993]",
    longDesc = u"""
Table 2
Radiative recombination
"""
)

entry(
    index = 23,
    label = "O2 + N2 <=> NO + NO+ + e-",
    kinetics=Arrhenius(A=(1.38e20, 'cm^3/(mol*s)'), n=-1.84, Ea=(280200.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Gupta1990]",
    longDesc = u"""
Table II, R14
"""
)

entry(
    index = 24,
    label = "N2+ + N2 <=> N2 + N + N",
    kinetics=Arrhenius(A=(6.99e21, 'cm^3/(mol*s)'), n=-1.60, Ea=(941.3, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 25,
    label = "NO+ + O <=> NO + O+",
    kinetics=Arrhenius(A=(2.76e13, 'cm^3/(mol*s)'), n=0.01, Ea=(424.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 26,
    label = "NO+ + N <=> NO + N+",
    kinetics=Arrhenius(A=(1.11e15, 'cm^3/(mol*s)'), n=-0.02, Ea=(507.7, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

# entry(
#     index = 27,
#     label = "O2 + e- => O+ + O + e- + e-",
#     reversible = False,
#     kinetics = TwoTemperaturePlasma(A=(2.9e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(22.5, "eV/molecule"),
#                                     Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
#     shortDesc = u"[Tanarro2015]",
#     longDesc = u"""
# Table 1, I2
# Electron Impact Ionization
# RMG does not accept reactions with more than 3 products in its solver
# """
# )

entry(
    index = 28,
    label = "O2 + e- => O2+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(4.26e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(13.1, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I3
Electron Impact Ionization
"""
)

entry(
    index = 29,
    label = "H + e- => H+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(3.91e15, "cm^3/(mol*s)"), n=0.49, Ea_g=(0.0, "J/mol"), Ea_e=(12.89, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I4
Electron Impact Ionization
"""
)

# entry(
#     index = 30,
#     label = "H2 + e- => H+ + H + e- + e-",
#     reversible = False,
#     kinetics = TwoTemperaturePlasma(A=(1.81e16, "cm^3/(mol*s)"), n=0.44, Ea_g=(0.0, "J/mol"), Ea_e=(37.72, "eV/molecule"),
#                                     Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
#     shortDesc = u"[Tanarro2015]",
#     longDesc = u"""
# Table 1, I5
# Electron Impact Ionization
# RMG does not accept reactions with more than 3 products in its solver
# """
# )

entry(
    index = 31,
    label = "H2 + e- => H2+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.88e16, "cm^3/(mol*s)"), n=0.17, Ea_g=(0.0, "J/mol"), Ea_e=(20.07, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I6
Electron Impact Ionization
"""
)

entry(
    index = 32,
    label = "OH + e- => OH+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(8.91e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(12.6, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I7
Electron Impact Ionization
"""
)

entry(
    index = 33,
    label = "H2O + e- => H2O+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(5.94e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(13.3, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I8
Electron Impact Ionization
"""
)

# entry(
#     index = 34,
#     label = "H2O + e- => OH+ + H + e- + e-",
#     reversible = False,
#     kinetics = TwoTemperaturePlasma(A=(1.73e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(17.7, "eV/molecule"),
#                                     Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
#     shortDesc = u"[Tanarro2015]",
#     longDesc = u"""
# Table 1, I9
# Electron Impact Ionization
# RMG does not accept reactions with more than 3 products in its solver
# """
# )

# entry(
#     index = 35,
#     label = "H2O + e- => H+ + OH + e- + e-",
#     reversible = False,
#     kinetics = TwoTemperaturePlasma(A=(1.07e17, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(20.0, "eV/molecule"),
#                                     Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
#     shortDesc = u"[Tanarro2015]",
#     longDesc = u"""
# Table 1, I10
# Electron Impact Ionization
# RMG does not accept reactions with more than 3 products in its solver
# """
# )

# entry(
#     index = 36,
#     label = "H2O + e- => O+ + H2 + e- + e-",
#     reversible = False,
#     kinetics = TwoTemperaturePlasma(A=(1.82e14, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "J/mol"), Ea_e=(23.5, "eV/molecule"),
#                                     Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
#     shortDesc = u"[Tanarro2015]",
#     longDesc = u"""
# Table 1, I11
# Electron Impact Ionization
# RMG does not accept reactions with more than 3 products in its solver
# """
# )

entry(
    index = 37,
    label = "O2s + e- => O2+ + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(5.42e14, "cm^3/(mol*s)"), n=2.0, Ea_g=(0.0, "J/mol"), Ea_e=(11.6, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, I11
Electron Impact Ionization
"""
)

entry(
    index = 38,
    label = "H2O + e- => Os + H2 + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.2e15, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(7.0, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, D6
"""
)

entry(
    index = 39,
    label = "O2s + e- => O + O + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(2.5e15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(4.6, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, D7
"""
)

entry(
    index = 40,
    label = "O2 + e- => O + Os + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(2.53e15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(5.56, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, D3
"""
)

entry(
    index = 41,
    label = "H2+ + e- <=> H + H",
    kinetics = TwoTemperaturePlasma(A=(3.53e10, "cm^3/(mol*s)"), n=4.00, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.60, "kJ/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N1
Fitted Arrhenius to "K_N1" polynom rate between Te=6000-25000 K
"""
)

entry(
    index = 42,
    label = "H3+ + e- => H + H + H",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.07e08, "cm^3/(mol*s)"), n=6.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.54, "kJ/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N2
Fitted Arrhenius to "0.5*K_N2" polynom rate between Te=6000-25000 K
"""
)

entry(
    index = 43,
    label = "H3+ + e- <=> H2 + H",
    kinetics = TwoTemperaturePlasma(A=(1.07e08, "cm^3/(mol*s)"), n=6.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.54, "kJ/mol"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N2
Fitted Arrhenius to "0.5*K_N2" polynom rate between Te=6000-25000 K
"""
)

entry(
    index = 44,
    label = "O2+ + e- <=> O + Os",
    kinetics = TwoTemperaturePlasma(A=(6.38e16, "cm^3/(mol*s)"), n=-0.7, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N5
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 45,
    label = "O2+ + e- <=> Os + Os",
    kinetics = TwoTemperaturePlasma(A=(4.55e16, "cm^3/(mol*s)"), n=-0.7, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N6
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 46,
    label = "OH+ + e- <=> O + H",
    kinetics = TwoTemperaturePlasma(A=(2.26e16, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N7
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 47,
    label = "H2O+ + e- <=> OH + H",
    kinetics = TwoTemperaturePlasma(A=(5.18e16, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N8
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 48,
    label = "H2O+ + e- <=> O + H2",
    kinetics = TwoTemperaturePlasma(A=(2.35e16, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N9
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 49,
    label = "H2O+ + e- => O + H + H",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.84e17, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N10
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 50,
    label = "H3O+ + e- => OH + H + H",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.72e17, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N11
Fitted Arrhenius to between Te=6000-25000 K

Also available from:
TwoTemperaturePlasma(A=(3.6e20, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "J/mol"), Ea_e=(-1.0, "cal/mol"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[JensenJones1977]",
p. 14
"""
)

entry(
    index = 51,
    label = "H3O+ + e- => O + H2 + H",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(3.37e15, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N12
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 52,
    label = "H3O+ + e- <=> OH + H2",
    kinetics = TwoTemperaturePlasma(A=(3.62e16, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N13
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 53,
    label = "H3O+ + e- <=> H2O + H",
    kinetics = TwoTemperaturePlasma(A=(6.50e16, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N14
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 54,
    label = "HO2+ + e- <=> O2 + H",
    kinetics = TwoTemperaturePlasma(A=(1.81e17, "cm^3/(mol*s)"), n=-0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.0, "kJ/mol"), T0=(300, "K"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, N15
Fitted Arrhenius to between Te=6000-25000 K
"""
)

entry(
    index = 55,
    label = "O2 + e- <=> O- + O",
    kinetics = TwoTemperaturePlasma(A=(6.44e14, "cm^3/(mol*s)"), n=-1.391, Ea_g=(0.0, "kJ/mol"), Ea_e=(6.26, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, A1

Also available in reverse:
Arrhenius(A=(1.38e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
Table 1, Dt11
"""
)

entry(
    index = 56,
    label = "H2O + e- <=> OH + H-",
    kinetics = TwoTemperaturePlasma(A=(2.13e15, "cm^3/(mol*s)"), n=-1.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(6.66, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, A2
"""
)

entry(
    index = 57,
    label = "H2 + e- <=> H- + H",
    kinetics = TwoTemperaturePlasma(A=(3.37e11, "cm^3/(mol*s)"), n=0.5, Ea_g=(0.0, "kJ/mol"), Ea_e=(5.5, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, A3
Also available in reverse:
Arrhenius(A=(7.83e14, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
Table 1, Dt2
"""
)

entry(
    index = 58,
    label = "O2s + e- <=> O- + O",
    kinetics = TwoTemperaturePlasma(A=(1.37e14, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(2.29, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, A4
"""
)

entry(
    index = 59,
    label = "H2O + e- <=> H2 + O-",
    kinetics = TwoTemperaturePlasma(A=(4.26e14, "cm^3/(mol*s)"), n=-1.3, Ea_g=(0.0, "kJ/mol"), Ea_e=(8.61, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, A5
Also available in reverse:
Arrhenius(A=(3.61e14, 'cm^3/(mol*s)'), n=-0.24, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
Table 1, Dt10
"""
)

entry(
    index = 60,
    label = "H2O + e- <=> OH- + H",
    kinetics = TwoTemperaturePlasma(A=(7.47e13, "cm^3/(mol*s)"), n=-1.3, Ea_g=(0.0, "kJ/mol"), Ea_e=(7.32, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, A6
Also available in reverse:
Arrhenius(A=(1.08e15, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
Table 1, Dt5
"""
)

entry(
    index = 61,
    label = "H- + e- => H + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.40e16, "cm^3/(mol*s)"), n=2.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.13, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt1
"""
)

entry(
    index = 62,
    label = "H- + O <=> OH + e-",
    kinetics=Arrhenius(A=(6.02e14, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt3
"""
)

entry(
    index = 63,
    label = "H- + O2 <=> HO2 + e-",
    kinetics=Arrhenius(A=(7.23e14, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt4
"""
)

entry(
    index = 64,
    label = "OH- + O <=> HO2 + e-",
    kinetics=Arrhenius(A=(1.20e14, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt6
"""
)

entry(
    index = 65,
    label = "OH- + e- => OH + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(5.82e18, "cm^3/(mol*s)"), n=-1.9, Ea_g=(0.0, "kJ/mol"), Ea_e=(12.1, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt7
"""
)

entry(
    index = 66,
    label = "O- + O2s <=> O3 + e-",
    kinetics=Arrhenius(A=(1.14e14, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt8
"""
)

entry(
    index = 67,
    label = "O- + H <=> OH + e-",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.00, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, Dt9
"""
)

entry(
    index = 68,
    label = "O2 + e- <=> O2s + e-",
    kinetics = TwoTemperaturePlasma(A=(1.02e15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(3.1, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, X1
"""
)

entry(
    index = 69,
    label = "O + e- <=> Os + e-",
    kinetics = TwoTemperaturePlasma(A=(2.71e15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(2.29, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, X2
"""
)

entry(
    index = 70,
    label = "H3+ + H- <=> H2 + H2",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN3
"""
)

entry(
    index = 71,
    label = "OH+ + H- <=> H2O",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN6
"""
)

entry(
    index = 72,
    label = "H3O+ + H- <=> H2O + H2",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN8
"""
)

entry(
    index = 73,
    label = "H2+ + O- <=> H2O",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN10
"""
)

entry(
    index = 74,
    label = "H3+ + O- <=> OH + H2",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN11
"""
)

entry(
    index = 75,
    label = "OH+ + O- <=> HO2",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN14
"""
)

entry(
    index = 76,
    label = "H3O+ + O- <=> H2O + OH",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN16
"""
)

entry(
    index = 77,
    label = "H2+ + OH- <=> H2O + H",
    kinetics=Arrhenius(A=(1.0e-7, 'cm^3/(molecule*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN17
"""
)

entry(
    index = 78,
    label = "H3+ + OH- <=> H2 + H2O",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN18
"""
)

entry(
    index = 79,
    label = "O+ + OH- <=> HO2",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN19
"""
)

entry(
    index = 80,
    label = "H3O+ + OH- <=> H2O + H2O",
    kinetics=Arrhenius(A=(4.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN23
"""
)

entry(
    index = 81,
    label = "OH + e- <=> OH-",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.1e+17,'cm^6/(mol^2*s)'), n=0.0, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 82,
    label = "O2 + e- <=> O2-",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(3.6e+17,'cm^6/(mol^2*s)'), n=0.0, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 83,
    label = "CH + O <=> CHO+ + e-",
    kinetics=Arrhenius(A=(3.0e15, 'cm^3/(mol*s)'), n=-1.0, Ea=(3400.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 84,
    label = "CHO+ + H2O <=> H3O+ + CO",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 85,
    label = "H3O+ + OH- => H + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(4.8e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

# entry(
#     index = 86,
#     label = "Ar + e- => Ar+ + e- + e-",
#     reversible = False,
#     kinetics = ElectronCollisionPlasma(
#         energies = ([
#             15.8, 16.0, 17.0, 18.0, 20.0, 22.0, 23.75, 25.0, 26.5, 30.0,
#             32.5, 35.0, 37.5, 40.0, 50.0, 55.0, 100.0, 150.0, 200.0, 300.0,
#             500.0, 700.0, 1000.0, 1500.0, 2000.0, 3000.0, 5000.0, 7000.0, 10000.0
#         ], 'eV/molecule'),
#         sigma = ([
#             0.0, 2.02e-22, 1.34e-21, 2.94e-21, 6.3e-21, 9.3e-21, 1.15e-20,
#             1.3e-20, 1.45e-20, 1.8e-20, 1.99e-20, 2.17e-20, 2.31e-20, 2.39e-20,
#             2.53e-20, 2.6e-20, 2.85e-20, 2.52e-20, 2.39e-20, 2.0e-20, 1.45e-20,
#             1.15e-20, 8.6e-21, 6.4e-21, 5.2e-21, 3.6e-21, 2.4e-21, 1.8e-21, 1.35e-21
#         ], 'm^2'),
#     ),
#     shortDesc = u"[LXCat]",
#     longDesc = u"""
# Ar -> Ar+ Ionization. Threshold 15.8 eV.
# """
# )

entry(
    index = 86,
    label = "Ar + e- => Ar+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            15.76, 15.86, 16.26, 16.76, 17.76, 20.76, 25.76, 35.76, 45.76, 55.76, 65.76, 75.76, 85.76, 95.76, 105.76, 155.76, 205.76, 255.76, 305.76, 355.76, 405.76, 455.76, 505.76, 555.76, 605.76, 655.76, 705.76, 755.76, 805.76, 855.76, 905.76, 955.76, 1005.76, 1505.76, 2005.76, 2505.76, 3005.76, 3505.76, 4005.76, 4505.76, 5005.76, 5505.76, 6005.76, 6505.76, 7005.76, 7505.76, 8005.76, 8505.76, 9005.76, 9505.76, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 1.16e-22, 5.74e-22, 1.13e-21, 2.21e-21, 5.12e-21, 9.10e-21, 1.47e-20, 1.81e-20, 2.03e-20, 2.16e-20, 2.23e-20, 2.27e-20, 2.29e-20, 2.28e-20, 2.15e-20, 1.96e-20, 1.79e-20, 1.64e-20, 1.51e-20, 1.40e-20, 1.30e-20, 1.22e-20, 1.15e-20, 1.08e-20, 1.03e-20, 9.74e-21, 9.28e-21, 8.87e-21, 8.49e-21, 8.14e-21, 7.83e-21, 7.53e-21, 5.53e-21, 4.40e-21, 3.68e-21, 3.17e-21, 2.79e-21, 2.50e-21, 2.27e-21, 2.08e-21, 1.92e-21, 1.78e-21, 1.67e-21, 1.57e-21, 1.48e-21, 1.40e-21, 1.33e-21, 1.27e-21, 1.21e-21, 1.16e-21
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Ar Ionization. Threshold 15.759 eV.
"""
)

entry(
    index = 87,
    label = "He + e- => He+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            24.59, 24.69, 25.09, 25.59, 26.59, 29.59, 34.59, 44.59, 54.59, 64.59, 74.59, 84.59, 94.59, 104.59, 154.59, 204.59, 254.59, 304.59, 354.59, 404.59, 454.59, 504.59, 554.59, 604.59, 654.59, 704.59, 754.59, 804.59, 854.59, 904.59, 954.59, 1004.59, 1504.59, 2004.59, 2504.59, 3004.59, 3504.59, 4004.59, 4504.59, 5004.59, 5504.59, 6004.59, 6504.59, 7004.59, 7504.59, 8004.59, 8504.59, 9004.59, 9504.59, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 9.15e-24, 4.54e-23, 9.01e-23, 1.77e-22, 4.21e-22, 7.77e-22, 1.33e-21, 1.74e-21, 2.03e-21, 2.24e-21, 2.40e-21, 2.51e-21, 2.59e-21, 2.69e-21, 2.60e-21, 2.45e-21, 2.30e-21, 2.15e-21, 2.02e-21, 1.89e-21, 1.79e-21, 1.69e-21, 1.60e-21, 1.52e-21, 1.45e-21, 1.38e-21, 1.32e-21, 1.27e-21, 1.22e-21, 1.17e-21, 1.13e-21, 8.29e-22, 6.58e-22, 5.47e-22, 4.69e-22, 4.12e-22, 3.67e-22, 3.31e-22, 3.02e-22, 2.78e-22, 2.58e-22, 2.40e-22, 2.25e-22, 2.12e-22, 2.00e-22, 1.90e-22, 1.80e-22, 1.72e-22, 1.64e-22
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
He Ionization. Threshold 24.587 eV.
"""
)

entry(
    index = 88,
    label = "Ne + e- => Ne+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            21.56, 21.66, 22.06, 22.56, 23.56, 26.56, 31.56, 41.56, 51.56, 61.56, 71.56, 81.56, 91.56, 101.56, 151.56, 201.56, 251.56, 301.56, 351.56, 401.56, 451.56, 501.56, 551.56, 601.56, 651.56, 701.56, 751.56, 801.56, 851.56, 901.56, 951.56, 1001.56, 1501.56, 2001.56, 2501.56, 3001.56, 3501.56, 4001.56, 4501.56, 5001.56, 5501.56, 6001.56, 6501.56, 7001.56, 7501.56, 8001.56, 8501.56, 9001.56, 9501.56, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 1.34e-23, 6.66e-23, 1.33e-22, 2.62e-22, 6.34e-22, 1.20e-21, 2.17e-21, 2.95e-21, 3.59e-21, 4.11e-21, 4.53e-21, 4.87e-21, 5.14e-21, 5.88e-21, 6.04e-21, 5.95e-21, 5.75e-21, 5.51e-21, 5.27e-21, 5.02e-21, 4.79e-21, 4.57e-21, 4.37e-21, 4.17e-21, 4.00e-21, 3.83e-21, 3.68e-21, 3.54e-21, 3.41e-21, 3.28e-21, 3.17e-21, 2.34e-21, 1.85e-21, 1.52e-21, 1.30e-21, 1.13e-21, 1.00e-21, 8.97e-22, 8.13e-22, 7.44e-22, 6.85e-22, 6.35e-22, 5.92e-22, 5.54e-22, 5.21e-22, 4.92e-22, 4.65e-22, 4.42e-22, 4.20e-22
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Ne Ionization. Threshold 21.564 eV.
"""
)

# entry(
#     index = 89,
#     label = "Kr + e- => Kr+ + e- + e-",
#     reversible = False,
#     kinetics = ElectronCollisionPlasma(
#         energies = ([
#             14.00, 14.10, 14.50, 15.00, 16.00, 19.00, 24.00, 34.00, 44.00, 54.00, 64.00, 74.00, 84.00, 94.00, 104.00, 154.00, 204.00, 254.00, 304.00, 354.00, 404.00, 454.00, 504.00, 554.00, 604.00, 654.00, 704.00, 754.00, 804.00, 854.00, 904.00, 954.00, 1004.00, 1504.00, 2004.00, 2504.00, 3004.00, 3504.00, 4004.00, 4504.00, 5004.00, 5504.00, 6004.00, 6504.00, 7004.00, 7504.00, 8004.00, 8504.00, 9004.00, 9504.00, 10000.00
#         ], 'eV/molecule'),
#         sigma = ([
#             0.00e+00, 1.63e-22, 8.06e-22, 1.59e-21, 3.10e-21, 7.16e-21, 1.27e-20, 2.03e-20, 2.50e-20, 2.79e-20, 2.96e-20, 3.06e-20, 3.11e-20, 3.13e-20, 3.13e-20, 2.95e-20, 2.71e-20, 2.48e-20, 2.28e-20, 2.11e-20, 1.97e-20, 1.84e-20, 1.73e-20, 1.63e-20, 1.55e-20, 1.47e-20, 1.40e-20, 1.34e-20, 1.28e-20, 1.23e-20, 1.18e-20, 1.14e-20, 1.10e-20, 8.24e-21, 6.67e-21, 5.64e-21, 4.91e-21, 4.36e-21, 3.94e-21, 3.59e-21, 3.31e-21, 3.07e-21, 2.87e-21, 2.70e-21, 2.54e-21, 2.41e-21, 2.29e-21, 2.18e-21, 2.09e-21, 2.00e-21, 1.92e-21
#         ], 'm^2'),
#     ),
#     shortDesc = u"[Golyatina2021]",
#     longDesc = u"""
# Kr Ionization. Threshold 13.996 eV.
# """
# )
#
# entry(
#     index = 90,
#     label = "Xe + e- => Xe+ + e- + e-",
#     reversible = False,
#     kinetics = ElectronCollisionPlasma(
#         energies = ([
#             12.13, 12.23, 12.63, 13.13, 14.13, 17.13, 22.13, 32.13, 42.13, 52.13, 62.13, 72.13, 82.13, 92.13, 102.13, 152.13, 202.13, 252.13, 302.13, 352.13, 402.13, 452.13, 502.13, 552.13, 602.13, 652.13, 702.13, 752.13, 802.13, 852.13, 902.13, 952.13, 1002.13, 1502.13, 2002.13, 2502.13, 3002.13, 3502.13, 4002.13, 4502.13, 5002.13, 5502.13, 6002.13, 6502.13, 7002.13, 7502.13, 8002.13, 8502.13, 9002.13, 9502.13, 10000.00
#         ], 'eV/molecule'),
#         sigma = ([
#             0.00e+00, 2.36e-22, 1.16e-21, 2.30e-21, 4.46e-21, 1.02e-20, 1.79e-20, 2.83e-20, 3.44e-20, 3.80e-20, 4.01e-20, 4.12e-20, 4.17e-20, 4.18e-20, 4.16e-20, 3.89e-20, 3.56e-20, 3.26e-20, 3.00e-20, 2.78e-20, 2.59e-20, 2.42e-20, 2.28e-20, 2.16e-20, 2.05e-20, 1.95e-20, 1.86e-20, 1.78e-20, 1.71e-20, 1.64e-20, 1.58e-20, 1.53e-20, 1.48e-20, 1.12e-20, 9.13e-21, 7.78e-21, 6.81e-21, 6.09e-21, 5.52e-21, 5.06e-21, 4.68e-21, 4.36e-21, 4.09e-21, 3.85e-21, 3.64e-21, 3.46e-21, 3.30e-21, 3.15e-21, 3.02e-21, 2.90e-21, 2.79e-21
#         ], 'm^2'),
#     ),
#     shortDesc = u"[Golyatina2021]",
#     longDesc = u"""
# Xe Ionization. Threshold 12.127 eV.
# """
# )

entry(
    index = 91,
    label = "H+ + e- => H",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(2.97e-09, "cm^3/(molecule*s)"), n=-1.0, Ea_g=(0.0, "J/mol"), Ea_e=(0.26,'kJ/mol'),
                                    Tmin = (10, "K"), Tmax = (1000000000, "K")),
    shortDesc = u"[Verner1995]",
    longDesc = u"""
Radiative Recombination: H I
Fit Parameters: a=7.98e-11, b=0.7480, T0=3.15e+00, T1=7.04e+05
Formula: Verner & Ferland (1996) Eq. 4.

temperatures = ([
    1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
], 'K'),
rate_coefficients = ([
    3.44e-11, 2.76e-11, 2.21e-11, 1.76e-11, 1.40e-11, 1.12e-11, 8.86e-12, 7.02e-12, 5.55e-12, 4.38e-12, 3.45e-12, 2.72e-12, 2.13e-12, 1.67e-12, 1.30e-12, 1.01e-12, 7.83e-13, 6.04e-13, 4.64e-13, 3.54e-13, 2.68e-13, 2.02e-13, 1.51e-13, 1.11e-13, 8.13e-14, 5.88e-14, 4.19e-14, 2.95e-14, 2.04e-14, 1.40e-14, 9.39e-15, 6.22e-15, 4.06e-15, 2.61e-15, 1.65e-15, 1.03e-15, 6.39e-16, 3.91e-16, 2.36e-16, 1.42e-16, 8.44e-17, 4.99e-17, 2.93e-17, 1.71e-17, 9.98e-18, 5.79e-18, 3.35e-18, 1.93e-18, 1.11e-18, 6.38e-19
], 'cm^3/s'),
"""
)

entry(
    index = 92,
    label = "He+ + e- => He",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(1.21e-09, "cm^3/(molecule*s)"), n=-0.87, Ea_g=(0.0, "J/mol"), Ea_e=(0.19,'kJ/mol'),
                                    Tmin = (10, "K"), Tmax = (1000000000, "K")),
    shortDesc = u"[VernerFerland1996]",
    longDesc = u"""
Radiative Recombination to form He I.
Z=2, N_product=2 (Product has 2 e-).
Fit Parameters: a=9.36e-10, b=0.7892, T0=4.27e-02, T1=4.68e+06

temperatures = ([
    1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
], 'K'),
rate_coefficients = ([
    3.38e-11, 2.70e-11, 2.15e-11, 1.72e-11, 1.37e-11, 1.09e-11, 8.67e-12, 6.90e-12, 5.48e-12, 4.36e-12, 3.46e-12, 2.75e-12, 2.18e-12, 1.73e-12, 1.37e-12, 1.08e-12, 8.55e-13, 6.74e-13, 5.30e-13, 4.16e-13, 3.25e-13, 2.53e-13, 1.97e-13, 1.52e-13, 1.17e-13, 8.90e-14, 6.74e-14, 5.06e-14, 3.76e-14, 2.77e-14, 2.01e-14, 1.44e-14, 1.02e-14, 7.11e-15, 4.88e-15, 3.30e-15, 2.19e-15, 1.44e-15, 9.26e-16, 5.89e-16, 3.69e-16, 2.29e-16, 1.40e-16, 8.49e-17, 5.10e-17, 3.04e-17, 1.80e-17, 1.06e-17, 6.19e-18, 3.61e-18
], 'cm^3/s'),
"""
)

entry(
    index = 93,
    label = "He+2 + e- => He+",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(7.68e-09, "cm^3/(molecule*s)"), n=-0.91, Ea_g=(0.0, "J/mol"), Ea_e=(0.22,'kJ/mol'),
                                    Tmin = (10, "K"), Tmax = (1000000000, "K")),
    shortDesc = u"[VernerFerland1996]",
    longDesc = u"""
Radiative Recombination to form He II.
Z=2, N_product=1 (Product has 1 e-).
Fit Parameters: a=1.89e-10, b=0.7624, T0=9.37e+00, T1=2.77e+06

temperatures = ([
    1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
], 'K'),
rate_coefficients = ([
    1.54e-10, 1.25e-10, 1.01e-10, 8.10e-11, 6.50e-11, 5.21e-11, 4.17e-11, 3.33e-11, 2.66e-11, 2.11e-11, 1.68e-11, 1.33e-11, 1.05e-11, 8.34e-12, 6.58e-12, 5.18e-12, 4.07e-12, 3.18e-12, 2.49e-12, 1.94e-12, 1.50e-12, 1.16e-12, 8.90e-13, 6.79e-13, 5.15e-13, 3.87e-13, 2.88e-13, 2.13e-13, 1.55e-13, 1.12e-13, 7.95e-14, 5.58e-14, 3.85e-14, 2.62e-14, 1.76e-14, 1.16e-14, 7.52e-15, 4.82e-15, 3.04e-15, 1.90e-15, 1.17e-15, 7.11e-16, 4.29e-16, 2.57e-16, 1.53e-16, 9.00e-17, 5.28e-17, 3.08e-17, 1.79e-17, 1.04e-17
], 'cm^3/s'),
"""
)
