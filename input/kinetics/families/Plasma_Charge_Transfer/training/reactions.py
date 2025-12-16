#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Charge_Transfer/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.4.
This family describes reactions of the sort:

A+ + B <=> A + B+  ;  A+ + B- <=> A + B  ;  A++ + B- <=> A+ + B

References:
[Tanarro2015]: M. Jimenez-Redondo, E. Carrasco, V.J. Herrero, I. Tanarro, Chemistry in glow discharges of H2/O2 mixtures. Diagnostics and modeling, Plasma Sources Sci Technol 2015, 24(1), DOI: 10.1088/0963-0252/24/1/015029
[Gupta1990]: R.N. Gupta, J.M. Yos, R.A. Thompson, K.-P. Lee, NASA Reference Publication 1232, 1990, A Review of Reaction Rates and Thermodynamic and Transport Properties for an 11-Species Air Model for Chemical and Thermal Nonequilibrium Calculations to 30000 K
[Aiken2023] T.T. Aiken, PhD Thesis, Detailed Modeling and Sensitivity Analysis of Non-Equilibrium Thermochemistry in Shock-Heated Gases, 2023, University of Colorado.
[Ozawa2008]: T. Ozawa, J. Zhong, D.A. Levin, Development of kinetic-based energy exchange models for noncontinuum, ionized hypersonic flows, Physics of Fluids 2008, 20, 046102, DOI: 10.1063/1.2907198
"""

entry(
    index = 1,
    label = "H+_r1 + H-_r2 <=> H + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.88e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN1
"""
)

entry(
    index = 2,
    label = "H2+_r1 + H-_r2 <=> H2 + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN2
"""
)

entry(
    index = 3,
    label = "O+_r1 + H-_r2 <=> O + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN4
"""
)

entry(
    index = 4,
    label = "O2+_r1 + H-_r2 <=> O2 + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN5
"""
)

entry(
    index = 5,
    label = "H2O+_r1 + H-_r2 <=> H2O + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN7
"""
)

entry(
    index = 6,
    label = "H+_r1 + O-_r2 <=> H + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN9
"""
)

entry(
    index = 7,
    label = "O+_r1 + O-_r2 <=> O + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-1.0, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN12
"""
)

entry(
    index = 8,
    label = "O2+_r1 + O-_r2 <=> O2 + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN13
"""
)

entry(
    index = 9,
    label = "H2O+_r1 + O-_r2 <=> H2O + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN15
"""
)

entry(
    index = 10,
    label = "O2+_r1 + OH-_r2 <=> O2 + OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN20
"""
)

entry(
    index = 11,
    label = "OH+_r1 + OH-_r2 <=> OH + OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN21
"""
)

entry(
    index = 12,
    label = "H2O+_r1 + OH-_r2 <=> H2O + OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN22
"""
)

entry(
    index = 13,
    label = "O2+_r1 + O_r2 <=> O2 + O+",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.92e18, 'cm^3/(mol*s)'), n=-1.11, Ea=(55650, 'cal/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Gupta1990]",
    longDesc = u"""
Table II, R11
"""
)

entry(
    index = 14,
    label = "NO+_r1 + O_r2 <=> NO + O+",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.76e13, 'cm^3/(mol*s)'), n=0.01, Ea=(424.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 15,
    label = "O+_r1 + N2_r2 <=> N2+ + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.1e13, 'cm^3/(mol*s)'), n=0.36, Ea=(189.6, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 16,
    label = "NO+_r1 + N_r2 <=> NO + N+",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.11e15, 'cm^3/(mol*s)'), n=-0.02, Ea=(507.7, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 17,
    label = "NO+_r1 + O2_r2 <=> O2+ + NO",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.8e15, 'cm^3/(mol*s)'), n=0.17, Ea=(65600, 'cal/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Gupta1990]",
    longDesc = u"""
Table II, R19
"""
)

entry(
    index = 18,
    label = "N+_r1 + N2_r2 <=> N2+ + N",
    degeneracy = 1,
    kinetics=Arrhenius(A=(6.99e6, 'cm^3/(mol*s)'), n=1.47, Ea=(26090, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 19,
    label = "Ar+_r1 + N2_r2 <=> Ar + N2+",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.55e13, 'cm^3/(mol*s)'), n=0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 20,
    label = "Ar+_r1 + O_r2 <=> Ar + O+",
    degeneracy = 1,
    kinetics=Arrhenius(A=(3.85e12, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 21,
    label = "NO+_r1 + O2_r2 <=> O2+ + NO",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.4e13, 'cm^3/(mol*s)'), n=0.41, Ea=(271.1, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 22,
    label = "O2+_r1 + N_r2 <=> N+ + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(8.67e13, 'cm^3/(mol*s)'), n=0.14, Ea=(237.8, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 23,
    label = "O2+_r1 + N2_r2 <=> N2+ + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.88e12, 'cm^3/(mol*s)'), n=0.0, Ea=(338.4, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 24,
    label = "Li+_r1 + H-_r2 <=> Li + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.81e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 25,
    label = "Na+_r1 + H-_r2 <=> Na + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.66e16, 'cm^3/(mol*s)'), n=0.2, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 26,
    label = "K+_r1 + H-_r2 <=> K + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(4.43e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 27,
    label = "Mg+_r1 + H-_r2 <=> Mg + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.03e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 28,
    label = "Ca+_r1 + H-_r2 <=> Ca + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.2e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)
