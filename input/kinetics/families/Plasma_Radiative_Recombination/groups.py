#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination/groups"
shortDesc = u""
longDesc = u"""
4.2. a.
This RR family describes reactions of the sort:

A+ + e- => A  + hv
A  + e- => A- + hv

*1 is always the reactive atom, N and Z are determined by it.

The template below covers the second stage, `A + e- => A-` (a net-neutral species
captures an electron to give the mono-anion): the reactant group `A` is a closed-
shell centre `R u0 c[0,+1,...]`, the recipe adds a radical and lowers the charge by
one, so a c0 reactant gives a c-1 product and a c+1 reactant (e.g. Li+) gives a c0
neutral. Linked, in the sibling library, to the `BadnellRRArrhenius` kinetics object.

Carried from branch `99` and translated to this branch's electron-bookkeeping
convention (see `docs/plasma_family_carry_translation_rule.md`): the free electron
is not a template species here. It is stripped from the `template(...)` call and
replaced by the signed scalar `electrons = -1` — the *net* number of free electrons
the forward reaction produces (0 produced minus 1 consumed = -1). Note this is NOT
a verbatim carry of `99`'s `product_electrons = 0`: the signed net is -1, and 0
would leave the product side unbalanced at -1 and the reaction silently dropped.
`electrons = -1` closes the 0 -> -1 charge gap in `family.py` charge balance, the
same mechanism `Plasma_Electron_Attachment` uses.

NOT the reactor-facing electron order. `electrons = -1` is the NET count, not the
incident order. The reactor-facing electron placement is resolved by
`rmgpy.electron_placement.resolve_electron_placement` from a
`(reactant_count, product_count)` declaration keyed on the family label in
`FAMILY_ELECTRON_PLACEMENT`. This family requires the entry

    'Plasma_Radiative_Recombination': (1, 0)

— incident order 1 (one electron captured), product count 0 (no free electron out),
net -1 — which is IDENTICAL to the pair the sibling library `PlasmaRadiativeRecombination`
already declares: the electron is captured and does not come out again, whatever
the charge stage. That declaration lives in the CODE repository and is out of scope
for this database-only ticket; a companion ticket adds it. Until it lands, this
family raises `ElectronPlacementError` naming this family the moment it is asked to
produce a reaction (confirmed empirically, see the carry report).
"""

template(reactants=["A"], products=["A-"], ownReverse=False)

reverse = "photoionization"

reversible = False
allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['GAIN_RADICAL', '*1', 1],
    ['LOSE_CHARGE', '*1', 1],
])

entry(
    index = 0,
    label = "A",
    group =
"""
1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]
""",
    kinetics = None,
)

tree(
"""
L1: A
"""
)
