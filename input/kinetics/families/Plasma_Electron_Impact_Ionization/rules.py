#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Impact_Ionization/rules"
shortDesc = u""
longDesc = u"""
One estimated rate rule, on the root node `A_rad`.

WHY A RULE AND NOT A TRAINING REACTION. The ruling asks for a single defensible
number so a family that is asked to estimate returns something rather than
nothing. The honest form of "a single sourced reaction's kinetics promoted to a
top-node rule for a whole family" is a hand-written rule on the root, not a
training reaction: a family training reaction needs a concrete species carrying
the number, and the only sourced number available here is argon's — argon cannot
be a training species in this family (closed-shell Ar has u0, and the template
demands u[1,2,3,4], so it does not match the family at all), and any other
concrete species substituted in would either misrepresent argon's datum as that
species' own or duplicate a value the sibling library already carries exactly
(Li). A root rule keeps the estimate textually and structurally distinct from the
sourced library data it was derived from, which is the property this ticket most
needs to preserve. This is `add_rules_from_training`-free: the training set is
empty, so `fill_rules_by_averaging_up` has nothing to average (single-node tree)
and this rule stands as written.

THE NUMBER, ITS SOURCE, AND ITS BOUNDS are in the entry's own longDesc below.
Read it before trusting or reusing the value.
"""

entry(
    index = 1,
    label = "A_rad",
    kinetics = Arrhenius(
        A = (1.254444e+03, 'm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (20000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""ESTIMATE — one-point generalization of argon electron-impact ionisation. NOT a fitted rule, NOT a prediction. Order-of-magnitude placeholder handed to every species this family matches. See longDesc for source and bounds.""",
    longDesc = u"""
ESTIMATED RATE RULE — one-point cross-family generalization. Read all of this.

PROVENANCE
----------
The A-factor is the rate coefficient of the single sourced reaction in the
`PlasmaArgon` reaction library on this branch,

    Ar + e-  =>  Ar+ + e- + e-    (entry index 86, `PlasmaArgon/reactions.py`)

evaluated ONCE, at the campaign's 1 eV working point:

    k(Te = 1 eV = 11604.5 K) = 1.254444e+03 m^3/(mol*s)

and frozen as a temperature-independent Arrhenius (n=0, Ea=0). The `PlasmaArgon`
entry is an `ElectronCollisionPlasma` cross-section table, not a fitted rate; its
own cited source is

    [Golyatina2021]: R.I. Golyatina, S.A. Marinov, "Analytical Cross Section
    Approximation for Electron Impact Ionization of Alkali and Other Metals,
    Inert Gases and Hydrogen Atoms", Atoms 2021, 9(90), DOI: 10.3390/atoms9040090

(51-point sigma(E) grid, threshold 15.759 eV). The value here was obtained by
`ElectronCollisionPlasma.get_rate_coefficient(11604.5)` against the pinned
runtime — reproducible, not transcribed.

WHAT THIS IS
------------
A ONE-POINT GENERALIZATION: one sourced reaction's rate coefficient, taken at a
single electron temperature, promoted to the top node of a family whose template
`A_rad` matches any radical (u[1,2,3,4]) with any charge. It exists so the family
returns a defensible order-of-magnitude number instead of nothing. It is a
PLACEHOLDER, not a prediction.

WHAT THIS IS NOT
----------------
* It is not a rate for the species it is handed to. It is argon's rate, at 1 eV,
  applied flat. Argon's ionisation threshold is 15.76 eV, which makes its rate at
  Te = 1 eV anomalously small — about FIVE ORDERS OF MAGNITUDE below the real
  electron-impact ionisation rate of a low-threshold light atom at the same Te
  (e.g. Li: Voronov Z=3,N=3 gives k(1 eV) = 1.29e8 m^3/(mol*s), vs 1.25e3 here).
  So this estimate is defensible only as an order-of-magnitude floor for
  high-threshold, noble-gas-like ionisation near 1 eV; it badly under-predicts
  alkali and hydrogen ionisation and must not be read as quantitative for them.
* It is not electron-temperature-aware. Plain Arrhenius has no
  `uses_electron_temperature` flag, so the family evaluates it at the GAS
  temperature — the wrong independent variable for an electron-driven process,
  exactly as documented for the interim entries in `Plasma_Electron_Attachment`.
* It is not the sibling library. Where the sourced library `PlasmaElectronImpactIonization`
  (Voronov) covers a species — Li — the library wins by RMG's library-over-family
  precedence; this estimate cannot displace it. And argon itself, the number's
  own source, cannot be produced by this family (u0 does not match u[1,2,3,4]), so
  the estimate can never overwrite the sourced argon datum in `PlasmaArgon`.

rank 10: a poor rank (smaller is better; auto-fits use 11), marking this as the
least-reliable kind of number a rule can carry — a hand-placed placeholder.
Superseded the moment a real per-species electron-temperature-dependent form can
be carried by this family.
""",
)
