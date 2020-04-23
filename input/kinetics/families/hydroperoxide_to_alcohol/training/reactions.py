#!/usr/bin/env python
# encoding: utf-8

name = "hydroperoxide_to_alcohol/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 0,
    label = "CH3OOH + H2O <=> CH3OH + H2O2",
    degeneracy = 1.0,
    rank = 5,
    kinetics = Arrhenius(A=(1e5,'cm^3/(mol*s)'), n=0, Ea=(10,'kcal/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
estimated to have a lifetime of about 30 min
(divided by 18 cm^3/mol, the rate is 5.8E-4 1/s)
""",
)

entry(
    index = 1,
    label = "H2O + cyanoisopropylOOH <=> H2O2 + cyanoisopropylOH",
    degeneracy = 1.0,
    rank = 5,
    kinetics = Arrhenius(A=(1e5,'cm^3/(mol*s)'), n=0, Ea=(10,'kcal/mol'),
                         T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    longDesc =
"""
estimated to have a lifetime of about 30 min
(divided by 18 cm^3/mol, the rate is 5.8E-4 1/s)
""",
)
