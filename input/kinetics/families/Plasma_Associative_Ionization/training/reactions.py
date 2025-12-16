#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.5.
This family describes reactions of the sort:

A + B <=> AB+ + e-

Reference:
[Aiken2025] T.T. Aiken, I.D. Boyd, I.V. Adamovich, Phys. Plasmas 2025, 32, 103512. DOI: 10.1063/5.0294530
"""

entry(
    index = 1,
    label = "O_A + O_B <=> O2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(1.82e10, 'cm^3/(mol*s)'), n=0.6797, Ea=(160336, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[Aiken2025]",
    longDesc = u"""
Table VIII
Associative ionization
"""
)

entry(
    index = 2,
    label = "Li_A + Li_B <=> Li2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 3,
    label = "Na_A + Na_B <=> Na2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(1.08e13, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 4,
    label = "Na_A + K_B <=> NaK+ + e-",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.03e13, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 5,
    label = "K_A + K_B <=> K2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(3.01e12, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 6,
    label = "Mg_A + Mg_B <=> Mg2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(6.02e13, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 7,
    label = "Ca_A + Ca_B <=> Ca2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(1.87e13, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"estimated",
    longDesc = u"""
"""
)
