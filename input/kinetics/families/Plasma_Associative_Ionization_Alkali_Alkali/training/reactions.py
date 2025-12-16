#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkali_Alkali/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.5.
This family describes reactions of the sort:

A + B <=> AB+ + e-
"""

entry(
    index = 1,
    label = "Li_A + Li_B <=> Li2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 2,
    label = "Na_A + Na_B <=> Na2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(1.08e13, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 3,
    label = "K_A + Na_B <=> NaK+ + e-",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.03e13, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 4,
    label = "K_A + K_B <=> K2+ + e-",
    degeneracy = 2,
    kinetics=Arrhenius(A=(3.01e12, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)
