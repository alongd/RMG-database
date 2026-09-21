#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination_Pairing/groups"
shortDesc = u"Radiative recombination of an OPEN-SHELL atomic cation (shell-closing capture)"
longDesc = u"""
Radiative recombination in which the captured electron PAIRS with an electron
already present, closing the shell:

    A+(*1) + e-  =>  A(*1) + hv        where A+ is open-shell and A is closed-shell

    Ar+  Ar u1 p3 c+1   +  e-   ->   Ar  u0 p4 c0        (3s2 3p5 -> 3s2 3p6)

WHY THIS IS A SECOND FAMILY AND NOT A WIDER ROOT ON THE FIRST ONE
------------------------------------------------------------------
`Plasma_Radiative_Recombination` and this family are the same physical process
split by the only thing that distinguishes them mechanically: whether the
captured electron finds an EMPTY orbital or has to PAIR. Those are two different
recipes, and a family carries exactly one, so they are two families.

    empty-orbital capture   GAIN_RADICAL + LOSE_CHARGE    u0 c+1 -> u1 c0
                            Li+ -> Li,  Na+ -> Na,  H+ -> H
                            `Plasma_Radiative_Recombination`

    pairing capture         LOSE_RADICAL + GAIN_PAIR       u1 c+1 -> u0 c0
                            + LOSE_CHARGE                  Ar+ -> Ar
                            THIS FAMILY

The split is not a workaround for a matching problem. Widening the sibling
family's root to `u1` instead would make ITS recipe build `Ar u2 p3 c0` — atom
type `Ar0e`, the argon METASTABLE — and hand it a ground-state rate rule.
Measured: `docs/i236-radiative-recombination-root/logs/p2-recipe-reach.stdout.log`.

WHY THE RECIPE HAS THREE ACTIONS AND NOT TWO
---------------------------------------------
`LOSE_RADICAL + GAIN_PAIR` alone is enough on a MOLECULE — the pair of actions
moves one electron onto *1 and `Atom.apply_action` carries the charge with it, so
`Ar u1 p3 c+1` becomes `Ar u0 p4 c0` with no charge action at all. It is NOT
enough on a GROUP: `GroupAtom.apply_action` leaves a group's declared charge
alone, so the product TEMPLATE comes out as `Ar u0 p4 c+1` — a template that
claims this family makes a cation. `LOSE_CHARGE` is what fixes the template.

The cost of the third action is a transient: on a molecule the recipe passes
through `c-1` before `Molecule.update()` recomputes the charge back to `c0`
(measured, `logs/p9-pairing-feasibility.stdout.log` and the charge-bookkeeping
probe beside it). `KineticsFamily.apply_recipe` calls `update()` before any charge
balance is checked (`family.py:1561`), so the transient never reaches the balance
— but it is real, it is invisible in the generated product, and it is written down
here so nobody has to rediscover it.

WHY THE ROOT IS ONE ELEMENT
----------------------------
`Ar` is the only element this family can carry today, and the limit is in RMG-Py's
atom-type table, not in the chemistry. `GAIN_PAIR` requires a non-empty
`increment_lone_pair` row on every atom type in the group, and measured against
this branch:

    Ar   decrement_radical=['Ar']   increment_lone_pair=['Ar']   decrement_charge=['Ar']
    He   decrement_radical=['He']   increment_lone_pair=[]       decrement_charge=[]
    Ne   decrement_radical=['Ne']   increment_lone_pair=[]       decrement_charge=[]

so `He+` and `Ne+` — both of which have thermochemistry in `PlasmaCationThermo`
and both of which recombine by exactly this mechanism — cannot appear in this
tree. A root of `[Ar,He,Ne] u1 px c+1` raises at load:

    ActionError: Unable to update GroupAtom due to GAIN_PAIR action:
    Unknown atom type produced from set "[AtomType "Ar", AtomType "He", AtomType "Ne"]"

That is an RMG-Py atom-type gap of the same shape as the empty `increment_charge`
row for oxygen that forced a wildcard top on
`Plasma_Associative_Ionization_Alkaline_Alkaline` (I-224). Filling it is RMG-Py
work and is owned elsewhere; when it lands, add `He` and `Ne` here and nowhere
else. Do NOT widen the root to a generic `R` or to `px` to get around it: the
sibling family's I-236 narrowing measured what a wildcard root costs — 22915 of
22936 species matched and `AtomTypeError` at 134616 centres.

`Ar u1 p3 c+1` is also, by valence arithmetic, only ever a BARE argon cation:
argon's formal charge is `8 - 2p - u - bonds`, so `u1 p3 c+1` forces `bonds = 0`.
The group cannot reach inside a molecule, which is the property the sibling
family had to be narrowed to obtain.

ELECTRON BOOKKEEPING
--------------------
The free electron is not a template species. `electrons = -1` is the signed NET
number of free electrons the forward reaction produces: 0 produced minus 1
consumed. Same convention as `Plasma_Electron_Attachment` and the sibling
`Plasma_Radiative_Recombination`, and same value.

REQUIRES AN RMG-Py REGISTRY ENTRY THAT DOES NOT EXIST YET — BUT NOT WHERE THE
SIBLING FAMILY'S DOCSTRING SAYS. The reactor-facing electron placement is
resolved from `FAMILY_ELECTRON_PLACEMENT` in `rmgpy/electron_placement.py`, keyed
on the family label. This family needs

    'Plasma_Radiative_Recombination_Pairing': (1, 0)

— incident order 1, product count 0, net -1, identical to the pair the sibling
family and the `PlasmaRadiativeRecombination` library both declare. That file is
in the CODE repository and was out of scope for the database ticket that added
this family, so the entry is NOT there yet.

What that costs is precisely one thing, and it is NOT reaction generation.
Measured (`logs/p11-pairing-family.stdout.log`, `logs/p12-placement-gate.stdout.log`):

* `generate_reactions` works with the registry exactly as RMG-Py ships it. This
  family produces `Ar+ + e- => Ar` with ground-state argon, `electrons = -1`, with
  no registry entry at all. The claim in `Plasma_Radiative_Recombination/groups.py`
  that an undeclared family "raises the moment it is asked to produce a reaction"
  does not hold here; generation never consults the registry.
* `resolve_electron_placement` is the gate, and the plasma REACTOR is what calls
  it — `rmgpy/solver/plasma.pyx:276`, during `initialize_model`. Without the entry
  it raises at `electron_placement.py:462`:

      ElectronPlacementError: Family 'Plasma_Radiative_Recombination_Pairing' has
      no electron-placement declaration (reaction [Ar+] => [Ar], electrons=-1);
      refusing to infer electron placement from the net electron count.

  With the entry, and with a rate attached, it certifies the view
  `[Ar+] + e- => [Ar]`.

So the family is complete and correct on the database side, and cannot be
SIMULATED until that one line lands in RMG-Py. Generation, database checks and
the tests in `test/test_plasma_radiative_recombination_pairing.py` all pass
without it.
"""

template(reactants=["Ar_cation"], products=["Ar_neutral"], ownReverse=False)

reverse = "photoionization_from_closed_shell"

reversible = False
allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['LOSE_RADICAL', '*1', 1],
    ['GAIN_PAIR', '*1', 1],
    ['LOSE_CHARGE', '*1', 1],
])

entry(
    index = 0,
    label = "Ar_cation",
    group =
"""
1 *1 Ar u1 p3 c+1
""",
    kinetics = None,
)

tree(
"""
L1: Ar_cation
"""
)
