#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Collisional_Ionization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.1. a.
This family describes reactions of the sort:

A  + M => A+ + e- + M

References:
[Gupta1990]: R.N. Gupta, J.M. Yos, R.A. Thompson, K.-P. Lee, NASA Reference Publication 1232, 1990, A Review of Reaction Rates and Thermodynamic and Transport Properties for an 11-Species Air Model for Chemical and Thermal Nonequilibrium Calculations to 30000 K
"""

entry(
    index = 1,
    label = "NO + O2 <=> NOp + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.2e15, 'cm^3/(mol*s)'), n=-0.35, Ea=(215000, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Guptap1990]",
    longDesc = u"""
Table II R15
"""
)

entry(
    index = 2,
    label = "NO + N2 <=> NOp + N2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.2e15, 'cm^3/(mol*s)'), n=-0.35, Ea=(215000, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Guptap1990]",
    longDesc = u"""
Table II R15
(same rate as above)
"""
)
