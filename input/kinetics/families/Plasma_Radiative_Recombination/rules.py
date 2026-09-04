#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination/rules"
shortDesc = u""
longDesc = u"""
One estimated rate rule, on the root node `A`.

WHY A RULE AND NOT A TRAINING REACTION. Same reasoning as the sibling EII family
(see `Plasma_Electron_Impact_Ionization/rules.py`): the ruling asks for a single
defensible number promoted to a top-node rule for the whole family, and the honest
form of that is a hand-written root rule, not a training reaction. The only sourced
number available is the Badnell Li+ radiative-recombination fit; putting it on a
concrete training species (Li+) would produce a value duplicating — and confusable
with — what the sibling library `PlasmaRadiativeRecombination` already carries
exactly. A root rule keeps the estimate structurally distinct from the sourced
library data it was derived from. The training set is empty, so
`fill_rules_by_averaging_up` has nothing to average (single-node tree) and this
rule stands as written.

THE NUMBER, ITS SOURCE, AND ITS BOUNDS are in the entry's own longDesc below.
"""

entry(
    index = 1,
    label = "A",
    kinetics = Arrhenius(
        A = (1.301428e+05, 'm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (20000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""ESTIMATE — one-point generalization of Li+ radiative recombination (Badnell 2006). NOT a fitted rule, NOT a prediction. Order-of-magnitude placeholder handed to every species this family matches. See longDesc for source and bounds.""",
    longDesc = u"""
ESTIMATED RATE RULE — one-point cross-family generalization. Read all of this.

PROVENANCE
----------
The A-factor is the rate coefficient of the single sourced reaction in the
`PlasmaRadiativeRecombination` reaction library on this branch,

    Li+ + e-  =>  Li + hv    (entry index 0, `PlasmaRadiativeRecombination/reactions.py`)

evaluated ONCE, at the campaign's 1 eV working point:

    k(Te = 1 eV = 11604.5 K) = 1.301428e+05 m^3/(mol*s)

and frozen as a temperature-independent Arrhenius (n=0, Ea=0). The library entry is
a `BadnellRRArrhenius(Z=3, N=2)` fit loaded from `input/kinetics/badnell.yaml`; its
own cited source is

    [Badnell2006]: N.R. Badnell, "Radiative Recombination Data for Modeling of
    Cosmic Plasmas" — the (Z, N)-indexed radiative-recombination fits shipped in
    `input/kinetics/badnell.yaml` (Z=3, N=2: the Li II -> Li I stage;
    A = 8.7e-12 cm^3/(molecule*s), B = 0.364, T0 = 147.0 K, T1 = 7.153e6 K,
    C = 0.1508, T2 = 7.154e5 K).

The value here was obtained by `BadnellRRArrhenius(Z=3,N=2).get_rate_coefficient(11604.5)`
against the pinned runtime — reproducible, not transcribed. It reproduces the
`1.301e5` that the library's own longDesc quotes at 1.0 eV.

WHAT THIS IS
------------
A ONE-POINT GENERALIZATION: one sourced reaction's rate coefficient, taken at a
single electron temperature, promoted to the top node of a family whose template
`A` matches any closed-shell centre (u0, any of c[0,+1,...]). It exists so the
family returns a defensible order-of-magnitude number instead of nothing. It is a
PLACEHOLDER, not a prediction.

WHAT THIS IS NOT
----------------
* It is not a rate for the species it is handed to, and it crosses a charge stage.
  The number is the Li+(+1) -> Li(0) CATION-to-neutral radiative-recombination
  rate; this family's template stage is A(0) -> A-(-1), neutral-to-anion (it also
  admits cation reactants, so Li+ -> Li itself is in range). Radiative-
  recombination/attachment rate coefficients vary by orders of magnitude with the
  ion's charge, nuclear charge and electron affinity — none of which the local
  connectivity RMG matches on can see — so this single value is an order-of-
  magnitude anchor, not a per-species rate. It is most defensible for singly
  charged light cations near 1 eV (where it was sourced) and least defensible for
  neutral-to-anion attachment, where the physics (and the true rate) differ.
* It is not electron-temperature-aware. Plain Arrhenius has no
  `uses_electron_temperature` flag, so the family evaluates it at the GAS
  temperature — the wrong independent variable for an electron-driven process,
  exactly as documented for the interim entries in `Plasma_Electron_Attachment`.
* It is not the sibling library. Where `PlasmaRadiativeRecombination` covers a
  species — Li+ — the library wins by RMG's library-over-family precedence and
  this estimate cannot displace it.

rank 10: a poor rank (smaller is better; auto-fits use 11), marking this as the
least-reliable kind of number a rule can carry — a hand-placed placeholder.
Superseded the moment a real per-species electron-temperature-dependent form can
be carried by this family.
""",
)
