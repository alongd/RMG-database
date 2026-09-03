#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Impact_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.3. a.
This family describes reactions of the sort:

AB + e- => A + B + e-

References:
[Tanarro2015]: M. Jimenez-Redondo, E. Carrasco, V.J. Herrero, I. Tanarro, Chemistry in glow discharges of H2/O2 mixtures. Diagnostics and modeling, Plasma Sources Sci Technol 2015, 24(1), DOI: 10.1088/0963-0252/24/1/015029

todo:
train from a non-arrhenius family...
"""

entry(
    index = 1,
    degeneracy = 1,
    label = "H2 <=> H + H",
    kinetics = TwoTemperaturePlasma(A=(1.05e17, "cm^3/(mol*s)"), n=-1.24, Ea_g=(0.0, "kJ/mol"), Ea_e=(12.59, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, D1
"""
)

entry(
    index = 2,
    degeneracy = 1,
    label = "O2 <=> O + O",
    kinetics = TwoTemperaturePlasma(A=(2.53e15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(5.56, "eV/molecule"),
        Tmin = (1000.0, "K"), Tmax = (100000.0, "K")),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, D2
"""
)

entry(
    index = 3,
    degeneracy = 1,
    label = "Na2 <=> Na + Na",
    kinetics = TwoTemperaturePlasma(A=(3.79e+15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.74, "eV/molecule"),
        Tmin = (300.0, "K"), Tmax = (40000.0, "K")),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
Electron impact dissociation of Na2.
Rate estimated from k(Na2) = 3e-09 cm3/s at Te = 1 eV.
Activation energy set to bond dissociation energy D0 = 0.74 eV.
Arrhenius fit: k = 6.29e-09 * exp(-0.74/Te).
"""
)

entry(
    index = 4,
    degeneracy = 1,
    label = "K2 <=> K + K",
    kinetics = TwoTemperaturePlasma(A=(4.56e+15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.52, "eV/molecule"),
        Tmin = (300.0, "K"), Tmax = (40000.0, "K")),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
Electron impact dissociation of K2.
Rate estimated from k(K2) = 4.5e-09 cm3/s at Te = 1 eV.
Activation energy set to bond dissociation energy D0 = 0.52 eV.
Arrhenius fit: k = 7.57e-09 * exp(-0.52/Te).
"""
)

entry(
    index = 5,
    degeneracy = 1,
    label = "NaK <=> Na + K",
    kinetics = TwoTemperaturePlasma(A=(4.56e+15, "cm^3/(mol*s)"), n=0.0, Ea_g=(0.0, "kJ/mol"), Ea_e=(0.52, "eV/molecule"),
        Tmin = (300.0, "K"), Tmax = (40000.0, "K")),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
Electron impact dissociation of NaK.
Rate estimated from k(NaK) = 3.5e-09 cm3/s at Te = 1 eV.
Activation energy set to bond dissociation energy D0 = 0.63 eV.
Arrhenius fit: k = 6.57e-09 * exp(-0.63/Te).
"""
)
