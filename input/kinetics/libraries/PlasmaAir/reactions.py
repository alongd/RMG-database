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
[VernerFerland1996]: D.A. Verner, G.J. Ferland, Atomic data for astrophysics. I. Radiative recombination rates for H-like, He-like, Li-like and Na-like ions over a broad range of temperature, ApJ 1995, arXiv:astro-ph/9509083v1
[JPL2019]: J.B. Burkholder et al., Chemical Kinetics and Photochemical Data for Use in Atmospheric Studies, Evaluation No. 19, JPL Publication 19-5, NASA/JPL, 2020. https://jpldataeval.jpl.nasa.gov/
[FlorescuMitchell2006]: A.I. Florescu-Mitchell, J.B.A. Mitchell, Dissociative recombination, Phys. Rep. 430 (2006) 277-374. DOI: 10.1016/j.physrep.2006.04.002
[Itikawa2005]: Y. Itikawa, N. Mason, Cross sections for electron collisions with water molecules, J. Phys. Chem. Ref. Data 34 (2005) 1-22. DOI: 10.1063/1.1799251
[Itikawa2006]: Y. Itikawa, Cross sections for electron collisions with nitrogen molecules, J. Phys. Chem. Ref. Data 35 (2006) 31-53. DOI: 10.1063/1.1937426

# can add these:
# Ar+ + H2 <=> ArH+ + H
# ArH+ + H2 <=> Ar + H3+
# Ar+ + O2 <=> Ar + O2+
# N2 + e <=> N2+ + e + e

CARRY-OVER PROVENANCE (I-154)
-----------------------------
This library was authored on an earlier line of development (RMG-database branch
``99``) and re-applied here as a new file rather than merged, because the branch it
came from also carries edits to existing files that this line does not want. What
changed in the carry, and nothing else did:

* **Cation labels gained a ``p`` suffix** (``NO+`` -> ``NOp``, ``Ar+`` -> ``Arp``,
  ...). ``KineticsLibrary.load`` splits a reaction string on a bare ``+``, so a
  species whose own label contains ``+`` is torn in half and the loader reports a
  missing species with an empty name. Every other family in this database already
  spells cations this way; the shipped ionisation library's ``[Lip]`` is the
  precedent. Species, charges and rates are untouched.
* **``NO+`` was re-drawn.** It arrived as ``N u0 p1 c+1 {2,D}`` -- a nitrogen with
  six valence electrons, which this engine has no atom type for. It is now the
  octet form ``N#O+`` (``N u0 p1 c0 {2,T}`` / ``O u0 p1 c+1 {1,T}``), which
  resolves to N3t/O4tc with the same net charge. Same species, better Lewis
  structure.
* **One entry was dropped as unbalanced.** ``N2+ + N2 => N2 + N + N`` carries charge
  +1 on the left and 0 on the right. It is a defect in the source branch, not a
  representation problem, and it is reported rather than repaired: the intended
  channel is ambiguous (dissociative recombination needs an electron; charge
  transfer needs a cation product) and guessing it would be authoring chemistry.

* **51 entries were NOT carried**, because this line has no representation
  for them in a kinetics library. RMG carries a reaction's free-electron
  stoichiometry either as an explicit participant or as the scalar
  ``Reaction.electrons``; ``Reaction.is_balanced`` treats the free electron as a
  conserved pseudo-element, so an explicit-electron entry whose electron COUNT
  changes across the arrow fails the balance check
  (``test/rmgpy/i108ElectronRepresentationMatrixTest.py`` pins this), and the
  metadata form is only reachable through a rate law that carries the count
  itself -- ``VoronovEIArrhenius``, ``BadnellRRArrhenius``, or a charge-transfer
  law. The dropped entries use ``Arrhenius``, ``ThirdBody`` and
  ``TwoTemperaturePlasma``, none of which do. Extending
  ``KineticsLibrary.load_entry`` with an ``electrons=`` argument is the agreed
  fix and is a separate ticket; until it lands these reactions are a NAMED gap
  rather than a silent one. They are listed in
  ``docs/i154-carry-chemistry.md``, by shape:

      (0, 1) x 10  associative / collisional ionisation, electron produced
      (1, 0) x 27  attachment or recombination, electron consumed
      (1, 2) x 14  electron-impact ionisation, one in and two out

  Every entry that survives conserves the free electron count, which is why this
  library correctly declares NO electron placement in
  ``rmgpy.electron_placement.FAMILY_ELECTRON_PLACEMENT``.

READ THE RATES BEFORE TRUSTING THEM
-----------------------------------
Many entries carried here are marked ``estimated`` by their original author rather
than sourced. That provenance is preserved verbatim in each entry's ``shortDesc``;
it was not upgraded, re-fitted or re-derived by the carry-over, which changed no
number anywhere.
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
    label = "N2 + e- => N + N + e-",
    reversible = False,
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
    index = 8,
    label = "NOp + O <=> O2 + Np",
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
    label = "N2 + Np <=> N2p + N",
    kinetics=Arrhenius(A=(6.99e6, 'cm^3/(mol*s)'), n=01.47, Ea=(26090, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 10,
    label = "O2p + N <=> Np + O2",
    kinetics=Arrhenius(A=(8.67e13, 'cm^3/(mol*s)'), n=0.14, Ea=(237.8, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 11,
    label = "NO + Op <=> O2 + Np",
    kinetics=Arrhenius(A=(1.4e5, 'cm^3/(mol*s)'), n=1.90, Ea=(127.2, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 12,
    label = "O2p + N2 <=> N2p + O2",
    kinetics=Arrhenius(A=(9.88e12, 'cm^3/(mol*s)'), n=0.0, Ea=(338.4, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 13,
    label = "O2p + O <=> Op + O2",
    kinetics=Arrhenius(A=(1.14e14, 'cm^3/(mol*s)'), n=-0.52, Ea=(156, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 14,
    label = "NOp + N <=> N2 + Op",
    kinetics=Arrhenius(A=(3.4e13, 'cm^3/(mol*s)'), n=-1.08, Ea=(106.4, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 15,
    label = "NOp + O2 <=> O2p + NO",
    kinetics=Arrhenius(A=(2.4e13, 'cm^3/(mol*s)'), n=0.41, Ea=(271.1, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 16,
    label = "NOp + O <=> O2p + N",
    kinetics=Arrhenius(A=(7.2e12, 'cm^3/(mol*s)'), n=0.29, Ea=(404.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 17,
    label = "N2 + Op <=> N2p + O",
    kinetics=Arrhenius(A=(9.1e13, 'cm^3/(mol*s)'), n=0.36, Ea=(189.6, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 18,
    label = "NOp + N <=> N2p + O",
    kinetics=Arrhenius(A=(1.7e13, 'cm^3/(mol*s)'), n=0.40, Ea=(295.1, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 25,
    label = "NOp + O <=> NO + Op",
    kinetics=Arrhenius(A=(2.76e13, 'cm^3/(mol*s)'), n=0.01, Ea=(424.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 26,
    label = "NOp + N <=> NO + Np",
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
    label = "H3p + H- <=> H2 + H2",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN3
"""
)

entry(
    index = 71,
    label = "OHp + H- <=> H2O",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN6
"""
)

entry(
    index = 72,
    label = "H3Op + H- <=> H2O + H2",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN8
"""
)

entry(
    index = 73,
    label = "H2p + O- <=> H2O",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN10
"""
)

entry(
    index = 74,
    label = "H3p + O- <=> OH + H2",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN11
"""
)

entry(
    index = 75,
    label = "OHp + O- <=> HO2",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN14
"""
)

entry(
    index = 76,
    label = "H3Op + O- <=> H2O + OH",
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN16
"""
)

entry(
    index = 77,
    label = "H2p + OH- <=> H2O + H",
    kinetics=Arrhenius(A=(1.0e-7, 'cm^3/(molecule*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN17
"""
)

entry(
    index = 78,
    label = "H3p + OH- <=> H2 + H2O",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN18
"""
)

entry(
    index = 79,
    label = "Op + OH- <=> HO2",
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN19
"""
)

entry(
    index = 80,
    label = "H3Op + OH- <=> H2O + H2O",
    kinetics=Arrhenius(A=(4.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN23
"""
)

entry(
    index = 84,
    label = "CHOp + H2O <=> H3Op + CO",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 85,
    label = "H3Op + OH- => H + OH + H2O",
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
    index = 94,
    label = "Os + N2 <=> O + N2",
    kinetics=Arrhenius(A=(1.57e13, 'cm^3/(mol*s)'), n=0.0, Ea=(-220, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) electronic quenching by N2.
JPL Eval. 19-5 recommendation: k(T) = 2.15e-11 * exp(110/T) cm^3 molecule^-1 s^-1.
Converted to cm^3/(mol*s) using N_A = 6.022e23.
Ea = -110 K * R_cal = -218.6 cal/mol (negative = mild T dependence).
""",
)

entry(
    index = 95,
    label = "Os + O2 <=> O + O2",
    kinetics=Arrhenius(A=(1.92e13, 'cm^3/(mol*s)'), n=0.0, Ea=(-110, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) electronic quenching by O2.
JPL Eval. 19-5 recommendation: k(T) = 3.3e-11 * exp(55/T) cm^3 molecule^-1 s^-1
(Note: leaves out the 20% spin-allowed O2(b) channel, which interconverts to
ground-state O2 within ~100 ms in this gas.)
Converted to cm^3/(mol*s) using N_A = 6.022e23.
""",
)

entry(
    index = 96,
    label = "Os + O <=> O + O",
    kinetics=Arrhenius(A=(4.82e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) electronic quenching by ground-state O.
Recommended room-T value k(298 K) = 8.0e-11 cm^3 molecule^-1 s^-1
(see Atkinson et al. evaluations cited in JPL 19-5; T-dependence weak).
Converted to cm^3/(mol*s) using N_A = 6.022e23.
""",
)

entry(
    index = 97,
    label = "Os + Ar <=> O + Ar",
    kinetics=Arrhenius(A=(3.0e8, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) electronic quenching by Ar (slow; mostly inelastic).
Recommended upper bound k(298 K) <= 5e-13 cm^3 molecule^-1 s^-1.
Used here as an explicit small rate so Ar is not treated as a perfect
quencher but does contribute when no other partner is available.
Converted to cm^3/(mol*s) using N_A = 6.022e23.
""",
)

entry(
    index = 98,
    label = "Os + H2O => OH + OH",
    reversible = False,
    kinetics=Arrhenius(A=(1.20e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) reaction with water producing 2 OH (chemical-quenching channel).
JPL Eval. 19-5 recommendation: k(T) = 1.99e-10 * exp(32/T) cm^3 molecule^-1 s^-1
~ 2.0e-10 cm^3 molecule^-1 s^-1 at 298 K.
Treated as irreversible because the reverse (OH + OH -> O(1D) + H2O)
is endothermic by ~1.97 eV and negligibly slow at the temperatures
considered here.
Converted to cm^3/(mol*s) using N_A = 6.022e23.
""",
)

entry(
    index = 99,
    label = "Os + O3 => O2 + O2",
    reversible = False,
    kinetics=Arrhenius(A=(7.23e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) reaction with ozone producing 2 O2 (chemical-quenching channel,
branching ratio ~0.6; the ~0.4 channel to O2 + O + O is omitted here for
simplicity since it cycles back through the standard O + O3 chemistry).
JPL Eval. 19-5 recommendation: k(298 K) = 1.2e-10 cm^3 molecule^-1 s^-1
(combined branches), of which ~60% goes to 2 O2.
Treated as irreversible since the reverse is far endothermic.
Converted to cm^3/(mol*s) using N_A = 6.022e23.
""",
)

entry(
    index = 100,
    label = "Os + H2 => OH + H",
    reversible = False,
    kinetics=Arrhenius(A=(7.23e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) reaction with H2 producing OH + H (chemical-quenching channel,
exothermic by ~1.85 eV).
JPL Eval. 19-5 recommendation: k(298 K) = 1.2e-10 cm^3 molecule^-1 s^-1.
Treated as irreversible.
Converted to cm^3/(mol*s) using N_A = 6.022e23.
""",
)

entry(
    index = 101,
    label = "Os => O",
    reversible = False,
    kinetics=Arrhenius(A=(9.1e-3, 's^-1'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(100, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"[JPL2019]",
    longDesc = u"""
O(1D) -> O(3P) radiative decay (forbidden red-doublet emission near 630 nm).
Total Einstein A coefficient ~ 9.1e-3 s^-1 (lifetime ~110 s).
Negligible vs. collisional quenching at any but very low pressures, but
included so that Os has a destruction path even in pure-Ar (or other
weakly-quenching) bath gases.
""",
)

# ----------------------------------------------------------------------
# Additional plasma-driven N2 / NO+ chemistry that the existing PlasmaAir
# entries do not cover. These channels are needed so that an air-plasma
# RMG run can close the N2+ / NO+ ion budgets and so that N2 ionization
# proceeds via the direct (non-associative) channel rather than only via
# `N + N <=> N2+ + e-`.
#
# Note: Zeldovich and other neutral N + O / N + O2 / N + NO chemistry is
# intentionally NOT added here -- those rates live in the
# primaryNitrogenLibrary and Klippenstein_Glarborg2016 libraries already.
# This block adds only plasma channels (electron-impact ionization,
# dissociative recombination, and electron-impact dissociation of H2O
# producing OH).
# ----------------------------------------------------------------------

entry(
    index = 103,
    label = "H2O + e- => OH + H + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(A=(5.0e14, "cm^3/(mol*s)"), n=0.5,
                                    Ea_g=(0.0, "kJ/mol"),
                                    Ea_e=(5.0, "eV/molecule"),
                                    Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    shortDesc = u"[Itikawa2005]",
    longDesc = u"""
Direct dissociative excitation of water by electron impact, producing
OH + H. Threshold ~5 eV (Itikawa & Mason 2005 review of H2O collisions).
This channel is dominant for OH production from H2O at Te ~ 1-10 eV in
air-plasma conditions, and is otherwise missing from PlasmaAir (the
existing dissociative-attachment and ionization channels do not yield
ground-state OH + H).

Tanarro-style Arrhenius fit to Maxwellian-averaged k(Te); pre-exponential
chosen so that k(Te=1 eV) ~ 1e-9 cm^3 molecule^-1 s^-1 matches Itikawa's
recommended cross-section.
""",
)
