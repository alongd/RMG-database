#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination_Pairing/rules"
shortDesc = u""
longDesc = u"""
One estimated rate rule, on the root node `Ar_cation`, which is the only node in
the tree.

WHY A RULE AND NOT A TRAINING REACTION: the same reasoning as the sibling
families `Plasma_Radiative_Recombination` and `Plasma_Electron_Impact_Ionization`
— a hand-written root rule keeps the estimate structurally distinct from the
sourced library data it was derived from, and the training set cannot carry a
`TwoTemperaturePlasma` at all. See `training/reactions.py`.

THE NUMBER, ITS SOURCE AND ITS BOUNDS are in the entry's own longDesc below.
"""

entry(
    index = 1,
    label = "Ar_cation",
    kinetics = Arrhenius(
        A = (1.007892e+05, 'm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (20000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""ESTIMATE — the sourced argon radiative-recombination rate frozen at one electron temperature. NOT a fitted rule, NOT a prediction. The Te dependence it was derived from is DISCARDED by this form; see longDesc.""",
    longDesc = u"""
ESTIMATED RATE RULE — one sourced rate, frozen at one working point. Read all of
this before using the number.

PROVENANCE
----------
The A-factor is the rate coefficient of the single sourced argon reaction in the
`PlasmaRadiativeRecombination` reaction library on this branch,

    Ar+ + e-  =>  Ar + hv    (entry index 1, `[Arp] => [Ar]`)

whose own source is

    [ShullVanSteenberg1982]: J. M. Shull and M. Van Steenberg, "The Ionization
    Equilibrium of Astrophysically Abundant Elements", Astrophys. J. Suppl. Ser.
    48 (1982) 95-107, equation (4) with Table 2 row AR1:
    A_rad = 3.77e-13 cm^3/s, X_rad = 6.51e-01, referenced to T0 = 1e4 K.

evaluated ONCE, at the argon deck's electron temperature:

    k(Te = 3 eV = 34813.55 K) = 1.007892e+05 m^3/(mol*s)

obtained from `TwoTemperaturePlasma.get_rate_coefficient_two_temp(300.0, 34813.55)`
against the pinned runtime — reproducible, not transcribed. The same call gives
2.060725e+05 at 1 eV and 1.312350e+05 at 2 eV, so the whole 1-3 eV span is inside
a factor of 2.2 of this value; the choice of working point is not what dominates
the error here.

WHAT THIS IS NOT
----------------
* It is not electron-temperature-aware, and that is a real loss, not a formality.
  The source IS a Te power law (Te^-0.651) and this form throws it away: plain
  `Arrhenius` has no `uses_electron_temperature` flag, so the family evaluates it
  at the GAS temperature — the wrong independent variable for an electron-driven
  process. This is the same defect documented for the interim entries in
  `Plasma_Electron_Attachment` and for the sibling family's root rule. Where the
  library covers the species — argon, i.e. every species this family matches today
  — the library WINS by RMG's library-over-family precedence and carries the
  correct `TwoTemperaturePlasma` form, so this rule is what a future, wider tree
  would fall back on rather than what the argon deck actually uses.
* It is not a per-species rate. Radiative-recombination coefficients scale with
  the ion's charge and nuclear charge, neither of which the local connectivity RMG
  matches on can see. Today the tree is argon alone, so the rule and the species
  coincide exactly; the moment `He` and `Ne` become representable (see
  `groups.py`) this becomes an argon number handed to helium and neon, and it
  should be replaced by per-node rules at that point rather than averaged.
* `Tmin`/`Tmax` above are documentation. `is_temperature_valid` has no production
  caller anywhere in RMG-Py, so nothing refuses this rule outside 300-20000 K.

rank 10: a poor rank (smaller is better; auto-fits use 11), marking this as a
hand-placed placeholder. Superseded the moment this family can carry a
`TwoTemperaturePlasma` rule directly.
""",
)
