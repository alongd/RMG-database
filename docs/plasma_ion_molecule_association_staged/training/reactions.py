#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Ion_Molecule_Association/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.6.
This family describes reactions of the sort:

A+ + B (+M) <=> AB+ (+M)
"""

entry(
    index = 1,
    label = "Lip + H <=> LiHp",
    degeneracy = 1,
    kinetics=Arrhenius(A=(6.02e4, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 2,
    label = "Nap + H <=> NaHp",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.02e8, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 3,
    label = "Mgp + H <=> MgHp",
    degeneracy = 1,
    kinetics=Arrhenius(A=(6.02e5, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)
