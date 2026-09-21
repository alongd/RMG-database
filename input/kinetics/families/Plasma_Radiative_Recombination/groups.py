#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination/groups"
shortDesc = u"Radiative recombination of a closed-shell atomic cation"
longDesc = u"""
4.2. a.
This RR family describes reactions of the sort:

A+ + e- => A  + hv

*1 is always the reactive atom, N and Z are determined by it.

ONE RECIPE, ONE STAGE. The recipe `GAIN_RADICAL *1 1; LOSE_CHARGE *1 1` realises
exactly one transformation: the captured electron enters an EMPTY orbital on *1,
so *1 gains one unpaired electron and loses one unit of charge while its lone
pairs stay put. That is why the root demands `u0` — it is not an oversight, it is
the recipe's own precondition. The root also demands `c+1`, which is the stage
this family is named for:

    Li+  u0 p0 c+1   +  e-   ->   Li  u1 p0 c0      (the anchor; see rules.py)
    H+   u0 p0 c+1   +  e-   ->   H   u1 p0 c0

The second stage the earlier version of this docstring claimed — `A + e- => A-`,
a net-neutral species capturing an electron to give a mono-anion — is NOT in this
family and must not be added to it. It has its own owner in this database,
`Plasma_Electron_Attachment`, which is named for it and carries the physically
correct recipe for it (`LOSE_RADICAL *1 1; GAIN_PAIR *1 1`: the electron PAIRS
with an existing unpaired electron). This family's recipe cannot do that stage:
applied to a neutral closed-shell centre it builds `X u1 p<unchanged> c-1`, which
RMG cannot type. Measured over every species in this database's thermo libraries,
the pre-I-236 root matched 22915 of 22936 species and its recipe raised
`AtomTypeError` at 134616 of the 230533 centres it labelled — the crash was the
majority outcome, not an argon curiosity.

WHY THE ROOT NAMES ELEMENTS RATHER THAN A WILDCARD. RMG groups match SUBGRAPHS,
so a charge written on *1 constrains that atom and never the molecule around it.
A root of `R u0 px c[+1,...]` — the wildcard with `c0` merely removed — still
matches 617 species, 614 of them NET-NEUTRAL molecules that happen to contain a
formally +1 atom: carbon monoxide's oxygen, every nitro group's nitrogen, every
azide. There is no flag that fixes this. `allowChargedReactants` is the wrong
shape (it forbids charged reactants; this family REQUIRES one, so it stays
undeclared and inherits `allowChargedSpecies = True`), and there is no
`requireChargedReactants`.

What does work is valence arithmetic. For hydrogen and the alkali metals the
formal charge is `1 - 2p - u - bonds`, so `u0 p0 c+1` forces `bonds = 0`: the
group can only ever match a BARE atomic cation, which is exactly the species
radiative recombination consumes. That is not true of carbon, nitrogen or oxygen,
where the same (u, p, c) triple is satisfied by a bonded atom inside a neutral
molecule — which is the whole of the 614. Measured, this root matches 3 species
in the database and raises nothing.

`Na` and `K` match nothing in this database today. They are named because they are
the same chemical class as the anchor — singly charged light closed-shell cations,
the class `rules.py` says its one number is most defensible for — and because the
campaign's alkali chemistry carries `Na+` on a branch that has not landed. Adding
an element here is legitimate only if its `u0 p0 c+1` state is a bare atom AND
`ATOMTYPES[<element>].decrement_charge` is non-empty (`LOSE_CHARGE` raises
`ActionError` otherwise, and the product template is built by applying the recipe
to this very group). `O`, `C`, `Si`, `F` and `Cl` fail the second test today, and
`He`, `Ne` and `Cs` fail it as well.

NOT COVERED, AND NOT COVERABLE HERE: `Ar+ + e- => Ar`, and open-shell atomic
cation recombination generally. `Ar+` is `Ar u1 p3 c+1`; the captured electron has
no empty orbital to enter and must pair, giving `Ar u0 p4 c0`. This recipe instead
builds `Ar u2 p3 c0` — atom type `Ar0e`, the METASTABLE, measurably NOT isomorphic
to ground-state argon. So widening the root's radical count does not make this
family do argon radiative recombination; it makes it generate a different reaction
under this family's name and hand it the ground-state rate rule. The same holds
for `He+` and `Ne+`. Argon radiative recombination is carried in this database by
the sibling reaction library `PlasmaRadiativeRecombination`, entry `[Arp] => [Ar]`,
which needs no family template. A family that generates it would need the pairing
recipe, which is a different family, not a wider root here.

ONE RESIDUAL OVER-MATCH, recorded because no group can exclude it: the entry
`electrocatLiThermo/H3O` is a van der Waals pair, `H2O` beside a bare `[H+]`, and
this root matches its proton fragment. Group matching is subgraph matching, so a
disconnected spectator cannot be seen from *1. The product is the same complex
with the proton reduced; it is an artefact of how that species is declared, not of
this template.

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
the charge stage. That declaration lives in the CODE repository and has since
landed there, so this family resolves its electron placement.

An earlier version of this paragraph said that until the declaration landed the
family would raise `ElectronPlacementError` "the moment it is asked to produce a
reaction". That is not where the gate is, measured on the sibling family
`Plasma_Radiative_Recombination_Pairing` while it was still undeclared
(`docs/i236-radiative-recombination-root/logs/p12-placement-gate.stdout.log`):
`generate_reactions` never consults `FAMILY_ELECTRON_PLACEMENT` and works fine
without an entry. The gate is `resolve_electron_placement`, which the plasma
REACTOR calls at `rmgpy/solver/plasma.pyx:276` during `initialize_model`. An
undeclared family generates reactions and then cannot be simulated.

THE OPEN-SHELL HALF OF THIS PROCESS IS A SEPARATE FAMILY. `Ar+ + e- => Ar` is not
here and cannot be: it needs the pairing recipe, and a family carries one recipe.
It lives in `Plasma_Radiative_Recombination_Pairing`, added by I-236 alongside
this narrowing. The two partition cleanly and neither generates the other's
reaction — measured, `logs/p11-pairing-family.stdout.log`:

    Plasma_Radiative_Recombination          Ar+ -> 0 reactions    Li+ -> 1
    Plasma_Radiative_Recombination_Pairing  Ar+ -> 1 reaction     Li+ -> 0
"""

template(reactants=["A"], products=["A_reduced"], ownReverse=False)

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
1 *1 [H,Li,Na,K] u0 p0 c+1
""",
    kinetics = None,
)

tree(
"""
L1: A
"""
)
