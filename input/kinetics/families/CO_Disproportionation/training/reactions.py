#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "C2H + CH3O <=> C2H2 + CH2O",
    kinetics=Arrhenius(A=(3.61e+13,'cm^3/(mol*s)','*|/',5), n=0, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    rank = 4,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

