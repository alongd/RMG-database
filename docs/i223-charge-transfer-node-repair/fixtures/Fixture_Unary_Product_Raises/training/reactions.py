#!/usr/bin/env python
# encoding: utf-8

name = "Fixture_Unary_Product_Raises/training"
shortDesc = u"Test fixture training set. One entry. The rate is a placeholder, not a measurement."
longDesc = u"""
NOT CHEMISTRY. Test data for check_family_generates.py -- see ../../README.md.

One UNIMOLECULAR entry:

    H2O -> H2O+

It is here so that the product-side assertion is tested on a family whose arity is one. Handing
two molecules to a unary family matches nothing and returns an empty list, so a check that assumes
two reactants never applies the recipe and never sees that H2O+ raises when it comes back alone.

The rate below is A = 1.0e-12 s^-1, n = 0, Ea = 0. It is a placeholder, it is not balanced in
charge on purpose -- an ionisation without its electron -- and nothing here should be read as
chemistry or copied into a real family.
"""

entry(
    index = 1,
    label = "H2O_r1 <=> H2Op",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.0e-12, 's^-1'), n=0, Ea=(0.0, 'kJ/mol'),
                         T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[fixture]",
    longDesc = u"""
Placeholder rate. See the longDesc at the top of this file.
""",
)
