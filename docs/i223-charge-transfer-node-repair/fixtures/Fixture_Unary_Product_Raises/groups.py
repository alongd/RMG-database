#!/usr/bin/env python
# encoding: utf-8

name = "Fixture_Unary_Product_Raises/groups"
shortDesc = u"Test fixture: a UNARY family whose product raises only when fed back ALONE."
longDesc = u"""
NOT CHEMISTRY. This is test data for check_family_generates.py. The rate is a placeholder.

THE DEFECT THIS FIXTURE CARRIES: it is a defect in the CHECK, not in a family, and it is the
reason this fixture is unary while the other four are bimolecular.

One reactant, one label, recipe GAIN_RADICAL *1 + LOSE_PAIR *1 -- ionisation of a lone pair:

    H2O  ->  H2O+       `O u0 p2 c0`  ->  `O u1 p1 c+1`, which the engine types as O4sc

Feed that product back in ALONE and the same recipe gives `O u2 p0 c+2` on two single bonds, which
has no atom type, so generate_reactions raises AtomTypeError -- the family cannot survive its own
product, exactly like Fixture_Own_Product_Raises.

WHAT MAKES IT A DIFFERENT TEST. Round 61 found that the check always supplied TWO reactants to the
product-side assertion. Handing two molecules to a unary family matches nothing and returns an
empty list without ever applying the recipe, so the check reported this family `ok` while its real
product raised the moment it came back alone. The arity of the family has to come from
`len(family.forward_template.reactants)`, not from an assumption.

Measured, on this fixture:

    H2O alone            ->  [OH2+]              the declared reaction, reproduced
    H2O+ alone           ->  AtomTypeError       the defect
    H2O+ with a partner  ->  nothing, no raise   the check hole, exactly

`electrons = 1` is required rather than decorative. The depository balance check runs at load time
and folds the family's electron count into the net charge (depository.py:236-243), so without it
this ionisation is refused as unbalanced and the fixture will not load at all.

The check should report this fixture as FAIL -- 1 of its own products RAISE when fed back in --
and exit 1. Before the round-61 fix it reported `ok`.
"""

template(reactants=["A"], products=["A+"], ownReverse=False)

reverse = "Fixture_Unary_Product_Raises_Reverse"
reversible = False

allowChargedSpecies = True
electrons = 1

recipe(actions=[
    ['GAIN_RADICAL', '*1', 1],
    ['LOSE_PAIR', '*1', 1],
])

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 O u[0,1] p[1,2] c[0,+1]
""",
    kinetics = None,
)

tree(
"""
L1: A
"""
)
