#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "C2H5NO2 <=> CH3CH2ONO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+10, 's^-1'), n=1, Ea=(60660, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""From kinetic library NOx2018""",
)