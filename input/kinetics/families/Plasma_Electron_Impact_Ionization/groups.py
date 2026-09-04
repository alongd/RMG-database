#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Impact_Ionization/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions of the sort:

A  + e- => A+ + e- + e-

*1 is always the reactive atom, N and Z are determined by it.

Carried from branch `99` and translated to this branch's electron-bookkeeping
convention (see `docs/plasma_family_carry_translation_rule.md`): the free
electron is not a template species here. The reactant electron and the two
product electrons are stripped from the `template(...)` call and replaced by the
signed scalar `electrons = +1` — the *net* number of free electrons the forward
reaction produces (2 produced minus 1 consumed). That scalar is what closes the
0 -> +1 charge gap in `family.py` charge balance without leaving an unconsumed
electron fragment on the product side.

NOT the reactor-facing electron order. `electrons = +1` is the NET count, not the
incident order. The incident order (which the rate coefficient's dimensionality
must match) and the net are independent, and the reactor-facing electron
placement is resolved by `rmgpy.electron_placement.resolve_electron_placement`
from a `(reactant_count, product_count)` declaration keyed on the family label in
`FAMILY_ELECTRON_PLACEMENT`. This family requires the entry

    'Plasma_Electron_Impact_Ionization': (1, 2)

— incident order 1 (one electron in), product count 2 (two electrons out), net
+1 — which is IDENTICAL to the pair the sibling library `PlasmaElectronImpactIonization`
already declares, for the same reason: same forward electron bookkeeping. That
declaration lives in the CODE repository and is out of scope for this
database-only ticket; a companion ticket adds it. Until it lands, this family
raises `ElectronPlacementError` naming this family the moment it is asked to
produce a reaction (confirmed empirically, see the carry report).
"""

template(reactants=["A_rad"], products=["A+"], ownReverse=False)

reverse = "electron_impact_attachment"

reversible = False
allowChargedSpecies = True
electrons = 1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 1],
    ['GAIN_CHARGE', '*1', 1],
])

entry(
    index = 0,
    label = "A_rad",
    group =
"""
1 *1 R u[1,2,3,4] px c[0,+1,+2,+3,+4,+5,+6,+7,+8]
""",
    kinetics = None,
)

tree(
"""
L1: A_rad
"""
)
