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
    kinetics=Arrhenius(A=(3.96049e+11, 's^-1'), n=0, Ea=(38.6696, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    rank = 1,
    longDesc =
"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c (APFD SMD solvation scheme) // wb97xd/def2tzvp, no rotors
ts1008

CCCCN(C)CO + H2O <=> C=O + CCCCNC + H2O

Calculated for VdW walls as the reactants and products

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.99182700   -0.55186800    0.16879500
C      -1.07409700   -1.83241500    0.89511900
H      -0.19134900   -1.95919800    1.51492000
H      -1.13931700   -2.64356600    0.17143000
H      -1.96022000   -1.82300100    1.52533200
O      -2.30521100    0.99886000   -1.03786000
H      -1.04051200    0.24831400    0.83901000
C      -2.22155500   -0.32700200   -0.68775800
H      -3.06114600   -0.66282400   -0.06928800
H      -2.12698900   -0.97614500   -1.56131200
C       0.25679400   -0.40513300   -0.62780800
H       0.09706400    0.44393000   -1.29085200
H       0.35581600   -1.30665200   -1.23429000
C       1.48249200   -0.16852900    0.23270000
H       1.67939600   -1.03535100    0.86775700
H       1.29669800    0.68365400    0.89374600
C       2.70962500    0.11055300   -0.62671500
H       2.51874800    0.98792500   -1.25130500
H       2.87013100   -0.72960100   -1.30881000
C       3.96032900    0.33762900    0.20868000
H       4.18987900   -0.54097200    0.81648500
H       4.82595900    0.54310700   -0.42361100
H       3.82971500    1.18611800    0.88476400
O      -1.69612600    1.94701900    1.11491100
H      -2.43079000    1.86699600    1.72719100
H      -2.12307700    1.53580600   -0.08716500
""",
)
