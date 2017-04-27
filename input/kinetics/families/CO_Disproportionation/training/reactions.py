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
    label = "HCO + H <=> CO + H2",
    kinetics=Arrhenius(A=(9.03e+13,'cm^3/(mol*s)','*|/',2), n=0, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    rank = 1,
    shortDesc = u"""Review and estimation based on experimental results""",
    longDesc = 
u"""
p. 519
R. Atkinson, D.L. Baulch, R.A. Cox, R.F. Hampson, J.A. Kerr, J. Troe,
Evaluated Kinetic Data for Combustion Modelling
Journal of Physical and Chemical Reference Data, 1992, 21, 411,
doi: 10.1063/1.555918
""",
)

