#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkali_Alkaline/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.5.
This family describes reactions of the sort:

A + B <=> AB+ + e-
"""

entry(
    index = 1,
    label = "Na_A + Mg_B <=> NaMg+ + e-",
    degeneracy = 1,
    kinetics=Arrhenius(A=(5.0e13, 'cm^3/(mol*s)'), n=0.6797, Ea=(160336, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"[estimated]",
    longDesc = u"""
Estimated using the geometric mean of Na+Na (index 3) and Mg+Mg (index 6) rates, 
multiplied by a factor of 2 to account for heteronuclear collision statistics.
k_cross ~ 2 * sqrt(k_NaNa * k_MgMg)
"""
)
