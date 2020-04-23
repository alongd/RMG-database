#!/usr/bin/env python
# encoding: utf-8

name = "hemiaminal_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 0,
    label = "CCCCN(C)CO <=> CH2O + CCCCNC",
    degeneracy = 1.0,
    kinetics=Arrhenius(A=(1.67323e+13, 's^-1'), n=-0.439556, Ea=(34.4251, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    rank = 5,
    longDesc =
"""
CBS-QB3 SMD water, no rotors

Calculated for VdW walls as the reactants and products

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -1.00758300   -0.56286700    0.15639900
C      -1.11899400   -1.85519900    0.87755000
H      -0.23022100   -2.01446700    1.48429300
H      -1.22016500   -2.66269400    0.15162000
H      -1.99602500   -1.82452900    1.52258600
O      -2.28474300    1.06326800   -1.01408300
H      -1.05716400    0.25503100    0.83659900
C      -2.24323400   -0.28475300   -0.70488000
H      -3.08929400   -0.61766600   -0.09142200
H      -2.16787500   -0.90740600   -1.60014600
C       0.25700500   -0.42716300   -0.64107800
H       0.08362200    0.39006300   -1.34119600
H       0.38157200   -1.35223600   -1.20864600
C       1.47531900   -0.12417500    0.22474300
H       1.64882200   -0.93482900    0.93926600
H       1.28045000    0.78336100    0.80697300
C       2.73322800    0.07286800   -0.62894200
H       2.55781800    0.88166800   -1.34737100
H       2.91458600   -0.83265500   -1.21926700
C       3.97071400    0.39227700    0.21128300
H       4.18963200   -0.41663400    0.91548900
H       4.85250800    0.53191700   -0.42031500
H       3.82723300    1.30912400    0.79169700
O      -1.61284000    1.83322700    1.19963100
H      -2.35924000    1.68611300    1.79201300
H      -2.07469700    1.54601400   -0.03872700
""",
)
