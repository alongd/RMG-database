#!/usr/bin/env python
# encoding: utf-8

name = "Fixture_Wrong_Products/training"
shortDesc = u"Test fixture training set. One entry. The rate is a placeholder, not a measurement."
longDesc = u"""
NOT CHEMISTRY. Test data for check_family_generates.py -- see ../../README.md.

One entry, whose DECLARED products this family cannot make:

    declared:   O+ + N2 -> NO+ + N
    generated:  O+ + N2 -> N2+ + O

Forward, it is generated from its own reactants, so the "does this family generate anything"
assertion has something to find. Backward, its product N2+ is the species that a root written as
`R` cannot survive, so the "does this family survive its own product" assertion has something to
find too -- in the sibling fixture that carries that defect.

The rate below is A = 1.0e-12 cm^3/(molecule*s), n = 0, Ea = 0. It is a placeholder. Do not cite
it, copy it into a real family, or treat it as having any provenance. The real reaction's audited
rate lives in the Plasma_Charge_Transfer training set and is not reproduced here, deliberately,
so that this directory cannot be mistaken for a source of chemistry.
"""

entry(
    index = 1,
    label = "Op_r1 + N2_r2 <=> NOp + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.0e-12, 'cm^3/(molecule*s)'), n=0, Ea=(0.0, 'kJ/mol'),
                         T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[fixture]",
    longDesc = u"""
Placeholder rate. See the longDesc at the top of this file.
""",
)
