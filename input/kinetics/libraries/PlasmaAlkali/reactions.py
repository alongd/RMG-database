#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaAlkali"
shortDesc = u"PlasmaAlkali"
longDesc = u"""
Plasma kinetics for Alkali and Alkali Earth metals in air plasma environments.

Reference legend:
[Golyatina2021]:  R.I. Golyatina, S.A. Marinov, Analytical Cross Section Approximation for Electron Impact Ionization of Alkali and Other Metals, Inert Gases and Hydrogen Atoms, Atoms 2021, 9(90), DOI: 10.3390/atoms9040090
[VernerFerland1996]: D.A. Verner, G.J. Ferland, Atomic data for astrophysics. I. Radiative recombination rates for H-like, He-like, Li-like and Na-like ions over a broad range of temperature, ApJ 1995, arXiv:astro-ph/9509083v1
[JensenJones1977]: D.E. Jensen and G.A. Jones, "Reaction Rate Coefficients for Flame Calculations", https://apps.dtic.mil/sti/tr/pdf/ADA047018.pdf
[AgerTalcottHoward1986]: J.W. Ager, C.L. Talcott, C.J. Howard, "Gas phase kinetics of the reactions of Na and NaO with O3 and N2O", J. Chem. Phys. 1986, 85, 5584-5592, DOI: 10.1063/1.451573
[AgerHoward1987]: J.W. Ager, C.J. Howard, "Gas phase kinetics of the reactions of NaO with H2, D2, H2O, and D2O", J. Chem. Phys. 1987, 87, 921-925, DOI: 10.1063/1.453726
[GlarborgMarshall2005]: P. Glarborg, P. Marshall, "Mechanism and modeling of the formation of gaseous alkali sulfates", Combust. Flame 2005, 141, 22-39, DOI: 10.1016/j.combustflame.2004.08.014
[GomezMartin2016]: J.C. Gomez Martin, S.M. Daly, J.M.C. Plane, "Kinetic studies of atmospherically relevant reactions of metal oxides", J. Phys. Chem. A 120, 1330-1339 (2016), DOI: 10.1021/acs.jpca.5b00622
[GomezMartin2017]: J.C. Gomez Martin, C. Seaton, M.P. de Miranda, J.M.C. Plane, "The reaction between sodium hydroxide and atomic hydrogen in atmospheric and flame chemistry", J. Phys. Chem. A 2017, 121, 7667-7674, DOI: 10.1021/acs.jpca.7b07808
[HelmerPlane1993]: M. Helmer, J.M.C. Plane, "A study of the reaction NaO2 + O -> NaO + O2: Implications for the chemistry of sodium in the upper atmosphere", J. Geophys. Res. 1993, 98, 23207-23222, DOI: 10.1029/93JD02033
[HusainMarshallPlane1986]: D. Husain, P. Marshall, J.M.C. Plane, "Rate constant for the reaction Na + O2 + N2 -> NaO2 + N2 under mesospheric conditions", J. Photochem. 1986, 32, 1-7, DOI: 10.1016/0047-2670(86)85001-8
[Plane2015]: J.M.C. Plane, W. Feng, E.C.M. Dawkins, "The mesosphere and metals: chemistry and changes", Chem. Rev. 2015, 115, 4497-4541, DOI: 10.1021/cr500501m
[PlaneHusain1986]: J.M.C. Plane, D. Husain, "Determination of the absolute rate constant for the reaction O + NaO -> Na + O2 by time-resolved atomic chemiluminescence at 589 nm", J. Chem. Soc. Faraday Trans. 2 1986, 82, 2047-2052, DOI: 10.1039/F29868202047
[PlaneRajasekhar1988a]: J.M.C. Plane, B. Rajasekhar, "Study of the reaction Li + H2O over the temperature range 850–1000 K by time-resolved laser-induced fluorescence of Li", J. Chem. Soc. Faraday Trans. 2 1988, 84, 273-285, DOI: 10.1039/F29888400273
[PlaneRajasekhar1988b]: J.M.C. Plane, B. Rajasekhar, "A study of the reaction Li + O2 + M (M = N2, He) over the temperature range 267-1100 K by Time-Resolved Lacer-Induced Fluorescence of Li", J. Phys. Chem. 93 1988, 3884-3890, DOI: 10.1021/j100324a041
[Sorvajarvi2015]: T. Sorvajarvi, J. Viljanen, J. Toivonen, P. Marshall, P. Glarborg, "Rate constant and thermochemistry for K + O2 + N2 = KO2 + N2", J. Phys. Chem. A 2015, 119, 3329-3336, DOI: 10.1021/acs.jpca.5b00755
"""

entry(
    index = 1,
    label = "Li+ + e- <=> Li",
    kinetics = TwoTemperaturePlasma(A=(1.30e-09, "cm^3/(molecule*s)"), n=-0.95, Ea_g=(0.0, "J/mol"), Ea_e=(0.19,'kJ/mol'),
                                    Tmin = (10, "K"), Tmax = (1000000000, "K")),
    shortDesc = u"[VernerFerland1996]",
    longDesc = u"""
Radiative Recombination to form Li I.
Z=3, N_product=3 (Product has 3 e-).
Fit Parameters: a=1.04e-11, b=0.3880, T0=1.08e+02, T1=1.18e+07

temperatures = ([
    1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
], 'K'),
rate_coefficients = ([
    2.89e-11, 2.32e-11, 1.86e-11, 1.48e-11, 1.18e-11, 9.30e-12, 7.31e-12, 5.71e-12, 4.43e-12, 3.42e-12, 2.63e-12, 2.01e-12, 1.53e-12, 1.16e-12, 8.73e-13, 6.56e-13, 4.91e-13, 3.66e-13, 2.72e-13, 2.01e-13, 1.49e-13, 1.10e-13, 8.03e-14, 5.87e-14, 4.28e-14, 3.10e-14, 2.24e-14, 1.61e-14, 1.15e-14, 8.13e-15, 5.72e-15, 3.99e-15, 2.76e-15, 1.89e-15, 1.28e-15, 8.58e-16, 5.68e-16, 3.72e-16, 2.40e-16, 1.53e-16, 9.66e-17, 6.02e-17, 3.71e-17, 2.27e-17, 1.37e-17, 8.22e-18, 4.90e-18, 2.90e-18, 1.70e-18, 9.96e-19
], 'cm^3/s'),

Also available from:
ThirdBody(arrheniusLow=Arrhenius(A=(2.41e+0,'cm^3/(mol*s)'), n=-1, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
p. 11
"""
)

entry(
    index = 2,
    label = "Na+ + e- <=> Na",
    kinetics = TwoTemperaturePlasma(A=(2.72e-08, "cm^3/(molecule*s)"), n=-1.07, Ea_g=(0.0, "J/mol"), Ea_e=(0.25,'kJ/mol'),
                                    Tmin = (10, "K"), Tmax = (1000000000, "K")),
    shortDesc = u"[VernerFerland1996]",
    longDesc = u"""
Radiative Recombination to form Na I.
Z=11, N_product=11 (Product has 11 e-).
Fit Parameters: a=5.64e-12, b=0.1749, T0=3.08e+02, T1=2.62e+06

temperatures = ([
    1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
], 'K'),
rate_coefficients = ([
    2.72e-11, 2.20e-11, 1.77e-11, 1.41e-11, 1.12e-11, 8.89e-12, 6.98e-12, 5.45e-12, 4.22e-12, 3.24e-12, 2.47e-12, 1.87e-12, 1.41e-12, 1.05e-12, 7.75e-13, 5.70e-13, 4.16e-13, 3.02e-13, 2.17e-13, 1.56e-13, 1.11e-13, 7.85e-14, 5.52e-14, 3.86e-14, 2.68e-14, 1.85e-14, 1.27e-14, 8.62e-15, 5.81e-15, 3.88e-15, 2.57e-15, 1.68e-15, 1.09e-15, 6.98e-16, 4.43e-16, 2.78e-16, 1.73e-16, 1.06e-16, 6.47e-17, 3.91e-17, 2.34e-17, 1.40e-17, 8.25e-18, 4.85e-18, 2.84e-18, 1.65e-18, 9.60e-19, 5.56e-19, 3.21e-19, 1.85e-19
], 'cm^3/s'),

Also available from:
ThirdBody(arrheniusLow=Arrhenius(A=(2.41e+0,'cm^3/(mol*s)'), n=-1, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
p. 11
"""
)

entry(
    index = 3,
    label = "K+ + e- <=> K",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(2.41e+0,'cm^6/(mol^2*s)'), n=-1, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 4,
    label = "Li+ + OH- <=> Li + OH",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=-0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 5,
    label = "Na+ + OH- <=> Na + OH",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=-0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 6,
    label = "K+ + OH- <=> K + OH",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=-0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 8,
    label = "LiH2O+ <=> Li+ + H2O",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.2e+17,'cm^3/(mol*s)'), n=0.0, Ea=(45700,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 9,
    label = "NaH2O+ <=> Na+ + H2O",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.8e+17,'cm^3/(mol*s)'), n=0.0, Ea=(29800,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 10,
    label = "KH2O+ <=> K+ + H2O",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(6.0e+16,'cm^3/(mol*s)'), n=0.0, Ea=(19900,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 11,
    label = "LiH2O+ + e- <=> Li + H2O",
    kinetics=Arrhenius(A=(6.0e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 12,
    label = "NaH2O+ + e- <=> Na + H2O",
    kinetics=Arrhenius(A=(6.0e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 13,
    label = "KH2O+ + e- <=> K + H2O",
    kinetics=Arrhenius(A=(6.0e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 14,
    label = "LiH2O+ + OH- => Li + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 15,
    label = "NaH2O+ + OH- => Na + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 16,
    label = "KH2O+ + OH- => K + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 17,
    label = "Li + O2 <=> LiO2",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(5.24e+20,'cm^6/(mol^2*s)'), n=-1.02, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[PlaneRajasekhar1988b]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Primary measurement covers 267-1100 K and is recommended for use over 300-6000 K.
Replaces the prior [JensenJones1977] value (3.6e+17 cm^6/mol^2/s, n=-1, Ea=0), which was ~1.2e+3 too low.
""",
)

entry(
    index = 18,
    label = "Na + O2 <=> NaO2",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.16e+21,'cm^6/(mol^2*s)'), n=-1.22, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[HusainMarshallPlane1986]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Primary measurement covers 415-1016 K and is recommended for use over 300-6000 K.
Replaces the prior [JensenJones1977] value (3.6e+17 cm^6/mol^2/s, n=-1, Ea=0), which was ~5e+2 to 6e+2 too low.
""",
)

entry(
    index = 19,
    label = "K + O2 <=> KO2",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.99e+22,'cm^6/(mol^2*s)'), n=-1.55, Ea=(20,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[Sorvajarvi2015]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Primary direct CPFAAS measurement covers 748-1323 K (the highest-T anchor for the entire alkali + O2 + M family);
recommended for use over 300-6000 K.
Replaces the prior [JensenJones1977] value (3.6e+17 cm^6/mol^2/s, n=-1, Ea=0), which was ~5e+2 to 1e+3 too low.
""",
)

entry(
    index = 20,
    label = "LiO2 + H2 <=> LiOH + OH",
    kinetics=Arrhenius(A=(1.8e12, 'cm^3/(mol*s)'), n=0.0, Ea=(19900.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 21,
    label = "NaO2 + H2 <=> NaOH + OH",
    kinetics=Arrhenius(A=(1.8e12, 'cm^3/(mol*s)'), n=0.0, Ea=(19900.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 22,
    label = "KO2 + H2 <=> KOH + OH",
    kinetics=Arrhenius(A=(1.8e12, 'cm^3/(mol*s)'), n=0.0, Ea=(19900.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 23,
    label = "LiO2 + OH <=> LiOH + O2",
    kinetics=Arrhenius(A=(1.2e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 24,
    label = "NaO2 + OH <=> NaOH + O2",
    kinetics=Arrhenius(A=(1.2e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 25,
    label = "KO2 + OH <=> KOH + O2",
    kinetics=Arrhenius(A=(1.2e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 26,
    label = "Na + HO2 <=> NaO2 + H",
    kinetics=Arrhenius(A=(6.0e12, 'cm^3/(mol*s)'), n=0.0, Ea=(1990.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 27,
    label = "K + HO2 <=> KO2 + H",
    kinetics=Arrhenius(A=(6.0e12, 'cm^3/(mol*s)'), n=0.0, Ea=(1990.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 28,
    label = "CaOH+ + e- <=> Ca + OH",
    kinetics=Arrhenius(A=(3.0e23, 'cm^3/(mol*s)'), n=-2.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 29,
    label = "CaOH + H <=> CaO + H2",
    kinetics=Arrhenius(A=(2.4e13, 'cm^3/(mol*s)'), n=0.0, Ea=(7300.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 30,
    label = "CaOH + H <=> Ca + H2O",
    kinetics=Arrhenius(A=(2.4e12, 'cm^3/(mol*s)'), n=0.0, Ea=(1200.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 31,
    label = "CaOH2 + H <=> CaOH + H2O",
    kinetics=Arrhenius(A=(1.8e13, 'cm^3/(mol*s)'), n=0.0, Ea=(1200.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 32,
    label = "CaO + H2O <=> CaOH2",
    kinetics=Arrhenius(A=(3.6e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 33,
    label = "CaOH+ + e- <=> CaO + H",
    kinetics=Arrhenius(A=(3.0e23, 'cm^3/(mol*s)'), n=-2.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 34,
    label = "CaOH+ + H <=> Ca+ + H2O",
    kinetics=Arrhenius(A=(6.0e13, 'cm^3/(mol*s)'), n=-2.0, Ea=(2000.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 35,
    label = "H3O+ + Li => Li+ + H2O + H",
    reversible = False,
    kinetics=Arrhenius(A=(1.0e19, 'cm^3/(mol*s)'), n=-1.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 36,
    label = "H3O+ + Na => Na+ + H2O + H",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e22, 'cm^3/(mol*s)'), n=-2.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 37,
    label = "H3O+ + K => K+ + H2O + H",
    reversible = False,
    kinetics=Arrhenius(A=(2.7e22, 'cm^3/(mol*s)'), n=-2.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 38,
    label = "Li + e- => Li+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            5.39, 5.49, 5.89, 6.39, 7.39, 10.39, 15.39, 25.39, 35.39, 45.39, 55.39, 65.39, 75.39, 85.39, 95.39, 105.39, 155.39, 205.39, 255.39, 305.39, 355.39, 405.39, 455.39, 505.39, 555.39, 605.39, 655.39, 705.39, 755.39, 805.39, 855.39, 905.39, 955.39, 1005.39, 1505.39, 2005.39, 2505.39, 3005.39, 3505.39, 4005.39, 4505.39, 5005.39, 5505.39, 6005.39, 6505.39, 7005.39, 7505.39, 8005.39, 8505.39, 9005.39, 9505.39, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 5.33e-22, 2.56e-21, 4.88e-21, 8.87e-21, 1.72e-20, 2.41e-20, 2.81e-20, 2.81e-20, 2.70e-20, 2.56e-20, 2.43e-20, 2.31e-20, 2.20e-20, 2.09e-20, 2.00e-20, 1.65e-20, 1.42e-20, 1.25e-20, 1.13e-20, 1.03e-20, 9.51e-21, 8.85e-21, 8.30e-21, 7.82e-21, 7.41e-21, 7.05e-21, 6.72e-21, 6.44e-21, 6.18e-21, 5.94e-21, 5.73e-21, 5.53e-21, 5.35e-21, 4.12e-21, 3.41e-21, 2.95e-21, 2.61e-21, 2.36e-21, 2.16e-21, 2.00e-21, 1.86e-21, 1.75e-21, 1.65e-21, 1.56e-21, 1.49e-21, 1.42e-21, 1.36e-21, 1.31e-21, 1.26e-21, 1.21e-21, 1.17e-21
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Li Ionization. Threshold 5.392 eV.
"""
)

entry(
    index = 39,
    label = "Na + e- => Na+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            5.14, 5.24, 5.64, 6.14, 7.14, 10.14, 15.14, 25.14, 35.14, 45.14, 55.14, 65.14, 75.14, 85.14, 95.14, 105.14, 155.14, 205.14, 255.14, 305.14, 355.14, 405.14, 455.14, 505.14, 555.14, 605.14, 655.14, 705.14, 755.14, 805.14, 855.14, 905.14, 955.14, 1005.14, 1505.14, 2005.14, 2505.14, 3005.14, 3505.14, 4005.14, 4505.14, 5005.14, 5505.14, 6005.14, 6505.14, 7005.14, 7505.14, 8005.14, 8505.14, 9005.14, 9505.14, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 8.28e-22, 3.94e-21, 7.42e-21, 1.32e-20, 2.43e-20, 3.18e-20, 3.35e-20, 3.12e-20, 2.84e-20, 2.59e-20, 2.36e-20, 2.17e-20, 2.01e-20, 1.87e-20, 1.75e-20, 1.32e-20, 1.07e-20, 8.95e-21, 7.74e-21, 6.82e-21, 6.11e-21, 5.54e-21, 5.07e-21, 4.67e-21, 4.34e-21, 4.05e-21, 3.80e-21, 3.58e-21, 3.39e-21, 3.22e-21, 3.06e-21, 2.92e-21, 2.79e-21, 1.96e-21, 1.52e-21, 1.25e-21, 1.06e-21, 9.23e-22, 8.19e-22, 7.37e-22, 6.71e-22, 6.16e-22, 5.70e-22, 5.31e-22, 4.96e-22, 4.67e-22, 4.40e-22, 4.17e-22, 3.96e-22, 3.78e-22, 3.61e-22
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Na Ionization. Threshold 5.139 eV.
"""
)

entry(
    index = 40,
    label = "K + e- => K+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            4.34, 4.44, 4.84, 5.34, 6.34, 9.34, 14.34, 24.34, 34.34, 44.34, 54.34, 64.34, 74.34, 84.34, 94.34, 104.34, 154.34, 204.34, 254.34, 304.34, 354.34, 404.34, 454.34, 504.34, 554.34, 604.34, 654.34, 704.34, 754.34, 804.34, 854.34, 904.34, 954.34, 1004.34, 1504.34, 2004.34, 2504.34, 3004.34, 3504.34, 4004.34, 4504.34, 5004.34, 5504.34, 6004.34, 6504.34, 7004.34, 7504.34, 8004.34, 8504.34, 9004.34, 9504.34, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 9.19e-22, 4.43e-21, 8.45e-21, 1.55e-20, 3.05e-20, 4.38e-20, 5.29e-20, 5.41e-20, 5.31e-20, 5.14e-20, 4.94e-20, 4.75e-20, 4.57e-20, 4.41e-20, 4.25e-20, 3.64e-20, 3.21e-20, 2.90e-20, 2.65e-20, 2.46e-20, 2.30e-20, 2.16e-20, 2.05e-20, 1.95e-20, 1.86e-20, 1.78e-20, 1.72e-20, 1.65e-20, 1.60e-20, 1.55e-20, 1.50e-20, 1.45e-20, 1.41e-20, 1.13e-20, 9.65e-21, 8.52e-21, 7.69e-21, 7.05e-21, 6.54e-21, 6.12e-21, 5.77e-21, 5.47e-21, 5.20e-21, 4.97e-21, 4.77e-21, 4.59e-21, 4.42e-21, 4.27e-21, 4.14e-21, 4.01e-21, 3.90e-21
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
K Ionization. Threshold 4.339 eV.
"""
)

entry(
    index = 41,
    label = "Mg + e- => Mg+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            7.65, 7.75, 8.15, 8.65, 9.65, 12.65, 17.65, 27.65, 37.65, 47.65, 57.65, 67.65, 77.65, 87.65, 97.65, 107.65, 157.65, 207.65, 257.65, 307.65, 357.65, 407.65, 457.65, 507.65, 557.65, 607.65, 657.65, 707.65, 757.65, 807.65, 857.65, 907.65, 957.65, 1007.65, 1507.65, 2007.65, 2507.65, 3007.65, 3507.65, 4007.65, 4507.65, 5007.65, 5507.65, 6007.65, 6507.65, 7007.65, 7507.65, 8007.65, 8507.65, 9007.65, 9507.65, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 6.48e-22, 3.11e-21, 5.92e-21, 1.08e-20, 2.08e-20, 2.90e-20, 3.30e-20, 3.21e-20, 3.01e-20, 2.80e-20, 2.60e-20, 2.42e-20, 2.27e-20, 2.13e-20, 2.00e-20, 1.56e-20, 1.28e-20, 1.08e-20, 9.45e-21, 8.40e-21, 7.56e-21, 6.89e-21, 6.33e-21, 5.86e-21, 5.46e-21, 5.12e-21, 4.82e-21, 4.55e-21, 4.31e-21, 4.10e-21, 3.91e-21, 3.74e-21, 3.58e-21, 2.55e-21, 1.99e-21, 1.65e-21, 1.41e-21, 1.23e-21, 1.10e-21, 9.94e-22, 9.07e-22, 8.36e-22, 7.75e-22, 7.23e-22, 6.78e-22, 6.39e-22, 6.04e-22, 5.74e-22, 5.46e-22, 5.21e-22, 4.99e-22
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Mg Ionization. Threshold 7.646 eV.
"""
)

entry(
    index = 42,
    label = "Si + e- => Si+ + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            8.16, 8.26, 8.66, 9.16, 10.16, 13.16, 18.16, 28.16, 38.16, 48.16, 58.16, 68.16, 78.16, 88.16, 98.16, 108.16, 158.16, 208.16, 258.16, 308.16, 358.16, 408.16, 458.16, 508.16, 558.16, 608.16, 658.16, 708.16, 758.16, 808.16, 858.16, 908.16, 958.16, 1008.16, 1508.16, 2008.16, 2508.16, 3008.16, 3508.16, 4008.16, 4508.16, 5008.16, 5508.16, 6008.16, 6508.16, 7008.16, 7508.16, 8008.16, 8508.16, 9008.16, 9508.16, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 6.30e-22, 3.07e-21, 5.94e-21, 1.12e-20, 2.35e-20, 3.65e-20, 4.83e-20, 5.23e-20, 5.31e-20, 5.26e-20, 5.15e-20, 5.02e-20, 4.88e-20, 4.74e-20, 4.60e-20, 4.00e-20, 3.56e-20, 3.22e-20, 2.95e-20, 2.73e-20, 2.55e-20, 2.40e-20, 2.27e-20, 2.15e-20, 2.05e-20, 1.97e-20, 1.89e-20, 1.82e-20, 1.75e-20, 1.69e-20, 1.64e-20, 1.59e-20, 1.54e-20, 1.22e-20, 1.03e-20, 9.03e-21, 8.10e-21, 7.39e-21, 6.82e-21, 6.35e-21, 5.96e-21, 5.63e-21, 5.34e-21, 5.09e-21, 4.87e-21, 4.67e-21, 4.49e-21, 4.33e-21, 4.18e-21, 4.05e-21, 3.92e-21
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Si Ionization. Threshold 8.157 eV.
"""
)

# entry(
#     index = 43,
#     label = "Li+2 + e- <=> Li+",
#     kinetics = TwoTemperaturePlasma(A=(5.08e-09, "cm^3/(molecule*s)"), n=-0.89, Ea_g=(0.0, "J/mol"), Ea_e=(0.18,'kJ/mol'),
#                                     Tmin = (10, "K"), Tmax = (1000000000, "K")),
#     shortDesc = u"[VernerFerland1996]",
#     longDesc = u"""
# Radiative Recombination to form Li II.
# Z=3, N_product=2 (Product has 2 e-).
# Fit Parameters: a=1.11e-10, b=0.6926, T0=2.44e+01, T1=8.32e+06
#
# temperatures = ([
#     1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
# ], 'K'),
# rate_coefficients = ([
#     1.49e-10, 1.20e-10, 9.71e-11, 7.81e-11, 6.26e-11, 5.01e-11, 4.00e-11, 3.18e-11, 2.52e-11, 2.00e-11, 1.58e-11, 1.24e-11, 9.78e-12, 7.68e-12, 6.02e-12, 4.71e-12, 3.68e-12, 2.86e-12, 2.23e-12, 1.73e-12, 1.34e-12, 1.03e-12, 7.93e-13, 6.07e-13, 4.63e-13, 3.51e-13, 2.65e-13, 1.98e-13, 1.47e-13, 1.09e-13, 7.92e-14, 5.72e-14, 4.08e-14, 2.87e-14, 2.00e-14, 1.37e-14, 9.22e-15, 6.13e-15, 4.02e-15, 2.59e-15, 1.65e-15, 1.04e-15, 6.43e-16, 3.95e-16, 2.40e-16, 1.44e-16, 8.60e-17, 5.10e-17, 3.00e-17, 1.76e-17
# ], 'cm^3/s'),
# """
# )
#
# entry(
#     index = 44,
#     label = "Li+3 + e- <=> Li+2",
#     kinetics = TwoTemperaturePlasma(A=(1.32e-08, "cm^3/(molecule*s)"), n=-0.86, Ea_g=(0.0, "J/mol"), Ea_e=(0.19,'kJ/mol'),
#                                     Tmin = (10, "K"), Tmax = (1000000000, "K")),
#     shortDesc = u"[VernerFerland1996]",
#     longDesc = u"""
# Radiative Recombination to form Li III.
# Z=3, N_product=1 (Product has 1 e-).
# Fit Parameters: a=3.04e-10, b=0.7539, T0=1.87e+01, T1=6.21e+06
#
# temperatures = ([
#     1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
# ], 'K'),
# rate_coefficients = ([
#     3.62e-10, 2.94e-10, 2.38e-10, 1.92e-10, 1.55e-10, 1.25e-10, 9.99e-11, 8.00e-11, 6.39e-11, 5.10e-11, 4.06e-11, 3.23e-11, 2.56e-11, 2.03e-11, 1.60e-11, 1.26e-11, 9.96e-12, 7.83e-12, 6.14e-12, 4.81e-12, 3.75e-12, 2.92e-12, 2.26e-12, 1.74e-12, 1.34e-12, 1.02e-12, 7.73e-13, 5.81e-13, 4.33e-13, 3.19e-13, 2.33e-13, 1.68e-13, 1.20e-13, 8.40e-14, 5.81e-14, 3.96e-14, 2.66e-14, 1.75e-14, 1.14e-14, 7.32e-15, 4.63e-15, 2.89e-15, 1.78e-15, 1.09e-15, 6.56e-16, 3.93e-16, 2.34e-16, 1.38e-16, 8.09e-17, 4.73e-17
# ], 'cm^3/s'),
# """
# )

entry(
    index = 45,
    label = "Mg+2 + e- <=> Mg+",
    kinetics = TwoTemperaturePlasma(A=(8.69e-09, "cm^3/(molecule*s)"), n=-0.99, Ea_g=(0.0, "J/mol"), Ea_e=(0.23,'kJ/mol'),
                                    Tmin = (10, "K"), Tmax = (1000000000, "K")),
    shortDesc = u"[VernerFerland1996]",
    longDesc = u"""
Radiative Recombination to form Mg II.
Z=12, N_product=11 (Product has 11 e-).
Fit Parameters: a=1.92e-11, b=0.3028, T0=4.85e+02, T1=5.89e+06

temperatures = ([
    1.00e+01, 1.46e+01, 2.12e+01, 3.09e+01, 4.50e+01, 6.55e+01, 9.54e+01, 1.39e+02, 2.02e+02, 2.95e+02, 4.29e+02, 6.25e+02, 9.10e+02, 1.33e+03, 1.93e+03, 2.81e+03, 4.09e+03, 5.96e+03, 8.69e+03, 1.26e+04, 1.84e+04, 2.68e+04, 3.91e+04, 5.69e+04, 8.29e+04, 1.21e+05, 1.76e+05, 2.56e+05, 3.73e+05, 5.43e+05, 7.91e+05, 1.15e+06, 1.68e+06, 2.44e+06, 3.56e+06, 5.18e+06, 7.54e+06, 1.10e+07, 1.60e+07, 2.33e+07, 3.39e+07, 4.94e+07, 7.20e+07, 1.05e+08, 1.53e+08, 2.22e+08, 3.24e+08, 4.71e+08, 6.87e+08, 1.00e+09
], 'K'),
rate_coefficients = ([
    1.22e-10, 9.89e-11, 8.02e-11, 6.48e-11, 5.22e-11, 4.18e-11, 3.33e-11, 2.64e-11, 2.08e-11, 1.63e-11, 1.27e-11, 9.83e-12, 7.56e-12, 5.77e-12, 4.37e-12, 3.30e-12, 2.47e-12, 1.84e-12, 1.36e-12, 1.00e-12, 7.35e-13, 5.36e-13, 3.89e-13, 2.80e-13, 2.01e-13, 1.43e-13, 1.01e-13, 7.13e-14, 4.97e-14, 3.44e-14, 2.36e-14, 1.61e-14, 1.08e-14, 7.18e-15, 4.72e-15, 3.07e-15, 1.97e-15, 1.25e-15, 7.88e-16, 4.89e-16, 3.01e-16, 1.83e-16, 1.11e-16, 6.62e-17, 3.93e-17, 2.32e-17, 1.36e-17, 7.98e-18, 4.64e-18, 2.69e-18
], 'cm^3/s'),
"""
)

entry(
    index = 46,
    label = "Na + O3 <=> NaO + O2",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(231.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerTalcottHoward1986]",
    longDesc = u"""
Direct laboratory measurement of Na + O3.
Modified-Arrhenius form k = 1.1e-9 * exp(-116/T) cm^3 molecule^-1 s^-1 from the Plane mesospheric
recommendation, anchored to the [AgerTalcottHoward1986] data; converted using N_A = 6.022e23
(231 cal/mol = 116 K * R_cal). Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 47,
    label = "Li + O3 <=> LiO + O2",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(231.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerTalcottHoward1986]",
    longDesc = u"""
Assumed same rate as Na + O3 <=> NaO + O2 by analogy. No primary Li + O3 kinetics measurement
survived source triage. Confidence: ANALOGY.
""",
)

entry(
    index = 48,
    label = "K + O3 <=> KO + O2",
    kinetics=Arrhenius(A=(1.08e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[Plane2015]",
    longDesc = u"""
K-specific value taken from the [Plane2015] meteoric K scheme rather than copied from Na.
Confidence: EXTRAPOLATED_FLAT.
""",
)

entry(
    index = 49,
    label = "Na + O <=> NaO",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.10e+21,'cm^6/(mol^2*s)'), n=-1.50, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[GlarborgMarshall2005]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
No primary Na + O + M measurement is available; this rate is the alkali/alkaline-earth analogy form
adopted in the Glarborg-Marshall combustion modeling work. Note: NaO+ + e- (excited-state cation
chemistry of Griffin et al. 2001) was explicitly rejected as a source - that paper concerns the
NaO(A2Sigma+) + O system, not ground-state Na + O association. Confidence: ANALOGY.
""",
)

entry(
    index = 50,
    label = "Li + O <=> LiO",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.10e+21,'cm^6/(mol^2*s)'), n=-1.50, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[GlarborgMarshall2005]",
    longDesc = u"""
Assumed same rate as Na + O + M by analogy. No primary Li + O + M data. Confidence: ANALOGY.
""",
)

entry(
    index = 51,
    label = "K + O <=> KO",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.10e+21,'cm^6/(mol^2*s)'), n=-1.50, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[GlarborgMarshall2005]",
    longDesc = u"""
Assumed same rate as Na + O + M by analogy. No primary K + O + M data. Confidence: ANALOGY.
""",
)

entry(
    index = 52,
    label = "NaO + O <=> Na + O2",
    kinetics=Arrhenius(A=(9.37e12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneHusain1986]",
    longDesc = u"""
Ground-state NaO(X) + O direct measurement. Do not substitute the NaO(A2Sigma+) + O kinetics
of Griffin et al. 2001 here. Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 53,
    label = "LiO + O <=> Li + O2",
    kinetics=Arrhenius(A=(9.37e12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneHusain1986]",
    longDesc = u"""
Assumed same rate as NaO + O <=> Na + O2 by analogy. No primary LiO + O data. Confidence: ANALOGY.
""",
)

entry(
    index = 54,
    label = "KO + O <=> K + O2",
    kinetics=Arrhenius(A=(9.37e12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneHusain1986]",
    longDesc = u"""
Assumed same rate as NaO + O <=> Na + O2 by analogy. No primary KO + O data. Confidence: ANALOGY.
""",
)

entry(
    index = 55,
    label = "NaO + H2 <=> NaOH + H",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(2186.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerHoward1987]",
    longDesc = u"""
Modified-Arrhenius fit (Plane2015 review evaluation) to the [AgerHoward1987] room-T anchor
[k(308-471 K) = (2.6 +/- 0.7)e-11 cm^3 molecule^-1 s^-1]. An unresolved low-T discrepancy versus
[GomezMartin2016] remains. Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 56,
    label = "LiO + H2 <=> LiOH + H",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(2186.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerHoward1987]",
    longDesc = u"""
Assumed same rate as NaO + H2 <=> NaOH + H by analogy. No primary LiO + H2 data. Confidence: ANALOGY.
""",
)

entry(
    index = 57,
    label = "KO + H2 <=> KOH + H",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(2186.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerHoward1987]",
    longDesc = u"""
Assumed same rate as NaO + H2 <=> NaOH + H by analogy. No primary KO + H2 data. Confidence: ANALOGY.
""",
)

entry(
    index = 58,
    label = "NaO + H2O <=> NaOH + OH",
    kinetics=Arrhenius(A=(3.05e14, 'cm^3/(mol*s)'), n=0.0, Ea=(477.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[GomezMartin2016]",
    longDesc = u"""
[GomezMartin2016] direct measurement with explicit T-dependence; preferred over the older flat
[AgerHoward1987] surrogate. Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 59,
    label = "LiO + H2O <=> LiOH + OH",
    kinetics=Arrhenius(A=(3.05e14, 'cm^3/(mol*s)'), n=0.0, Ea=(477.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[GomezMartin2016]",
    longDesc = u"""
Assumed same rate as NaO + H2O <=> NaOH + OH by analogy. No primary LiO + H2O data. Confidence: ANALOGY.
""",
)

entry(
    index = 60,
    label = "KO + H2O <=> KOH + OH",
    kinetics=Arrhenius(A=(1.32e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[Plane2015]",
    longDesc = u"""
K-specific direct value retained from the [Plane2015] meteoric K scheme. Confidence: EXTRAPOLATED_FLAT.
""",
)

entry(
    index = 61,
    label = "NaOH + H <=> Na + H2O",
    kinetics=Arrhenius(A=(2.29e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[GomezMartin2017]",
    longDesc = u"""
Direct measurement at 230-298 K with essentially no temperature dependence; validated against
flame chemistry. Confidence: MEASURED_HIGH_T (the cleanest entry in the alkali metal-oxide block).
""",
)

entry(
    index = 62,
    label = "LiOH + H <=> Li + H2O",
    kinetics=Arrhenius(A=(9.60e13, 'cm^3/(mol*s)'), n=0.0, Ea=(24400.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneRajasekhar1988a]",
    longDesc = u"""
Derived from the measured reverse reaction Li + H2O and Li/LiOH thermochemistry; the high barrier
(~24 kcal/mol) reflects LiOH stability and is required by detailed balance. Do NOT copy the Na rate
here. Confidence: EXTRAPOLATED_T_DEPENDENT.
""",
)

entry(
    index = 63,
    label = "KOH + H <=> K + H2O",
    kinetics=Arrhenius(A=(3.00e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[Plane2015]",
    longDesc = u"""
High-T flame-inferred K-specific value from the [Plane2015] meteoric K scheme. Confidence: MEASURED_HIGH_T.
""",
)

entry(
    index = 64,
    label = "NaO2 + O <=> NaO + O2",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.0, Ea=(1868.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[HelmerPlane1993]",
    longDesc = u"""
Modified-Arrhenius fit (Plane2015 review evaluation) anchored to the 295 K direct flow-tube
measurement of [HelmerPlane1993] [k = (2.2 +/- 1.0)e-11 cm^3 molecule^-1 s^-1]. Confidence:
EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 65,
    label = "LiO2 + O <=> LiO + O2",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.0, Ea=(1868.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[HelmerPlane1993]",
    longDesc = u"""
Assumed same rate as NaO2 + O <=> NaO + O2 by analogy. No primary LiO2 + O data. Confidence: ANALOGY.
""",
)

entry(
    index = 66,
    label = "KO2 + O <=> KO + O2",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.0, Ea=(1868.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[HelmerPlane1993]",
    longDesc = u"""
Assumed same rate as NaO2 + O <=> NaO + O2 by analogy. No primary KO2 + O data. Confidence: ANALOGY.
""",
)

