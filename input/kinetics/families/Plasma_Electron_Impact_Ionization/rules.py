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
        A = (1.292979e+08, 'm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (20000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""ESTIMATE — one-point generalization of the sourced Voronov lithium electron-impact ionisation rate. NOT a fitted rule, NOT a prediction. Order-of-magnitude placeholder handed to every species this family matches. See longDesc for source and bounds.""",
    longDesc = u"""
ESTIMATED RATE RULE — one-point cross-family generalization. Read all of this.

PROVENANCE
----------
The A-factor is the rate coefficient of the sourced reaction

    [Li] => [Lip]    (Li(2S) + e- => Li+ + 2 e-, `PlasmaElectronImpactIonization/reactions.py`)

a `VoronovEIArrhenius(Z=3, N=3)` fit loaded by (Z, N) from
`input/kinetics/voronov.yaml`, evaluated ONCE at the campaign's 1 eV working point:

    k(Te = 1 eV = 11604.5 K) = 1.292979e+08 m^3/(mol*s)

and frozen as a temperature-independent Arrhenius (n=0, Ea=0). Its cited source is

    [Voronov1997]: G.S. Voronov, "A Practical Fit Formula for Ionization Rate
    Coefficients of Atoms and Ions by Electron Impact: Z = 1-28", Atomic Data and
    Nuclear Data Tables 65 (1997) 1-35 (Table I, Z=3, N=3: the Li I -> Li II
    stage, ionisation threshold dE = 5.4 eV).

The value here was obtained by
`VoronovEIArrhenius(Z=3,N=3).get_rate_coefficient(11604.5)` against the pinned
runtime — reproducible, not transcribed.

ANCHOR CHANGED, 2026-09-04, on the owner's ruling. This rule was ORIGINALLY
anchored on argon electron-impact ionisation ([Golyatina2021], `PlasmaArgon`
entry 86, an `ElectronCollisionPlasma` cross-section table, k(1 eV) = 1.254444e3
m^3/(mol*s)). It was re-anchored onto Voronov lithium because an order-of-
magnitude placeholder should rest on chemistry the family can actually be asked
about: this family CANNOT generate argon at all (closed-shell Ar has u0, outside
the template's u[1,2,3,4]; `generate_reactions([Ar])` returns 0 reactions),
whereas it does generate `Li + e- => Li+`. Lithium is equally sourced and equally
citable, so the swap costs nothing in provenance and makes the validity statement
below defensible. The old argon number is preserved in the carry report, not
silently dropped.

WHAT THIS IS
------------
A ONE-POINT GENERALIZATION: one sourced reaction's rate coefficient, taken at a
single electron temperature, promoted to the top node of a family whose template
`A_rad` matches any radical (u[1,2,3,4]) with any charge. It exists so the family
returns a defensible order-of-magnitude number instead of nothing. It is a
PLACEHOLDER, not a prediction.

WHAT THIS IS NOT — the range of validity, and it is the deliverable
-------------------------------------------------------------------
* It is a light-alkali ionisation rate at 1 eV, applied flat to every radical the
  template matches. It is defensible as an ORDER-OF-MAGNITUDE estimate for
  LOW-THRESHOLD light atoms — the alkalis and hydrogen (ionisation thresholds
  ~4-14 eV) that dominate the campaign's chemistry — NEAR the 1 eV working point.
  It is NOT defensible for high-threshold species: a noble gas (Ar 15.76 eV,
  He 24.6 eV) ionises orders of magnitude more slowly at 1 eV than lithium
  (5.4 eV) does, so on those this rule OVER-predicts badly — the mirror image of
  the error the original argon anchor made on light atoms. The two sourced
  endpoints at 1 eV bracket the family's true spread: Li 1.29e8 vs Ar 1.25e3
  m^3/(mol*s), five orders apart on threshold alone. Read this number as "roughly
  a light atom near 1 eV", never as a species rate.
* It is not electron-temperature-aware. Plain Arrhenius has no
  `uses_electron_temperature` flag, so the family evaluates it at the GAS
  temperature — the wrong independent variable for an electron-driven process,
  exactly as documented for the interim entries in `Plasma_Electron_Attachment`.
  The true Voronov rate climbs steeply with Te across a discharge; this single
  1 eV point does not carry that.
* It is not the sibling library, and cannot shadow it. Where the sourced library
  `PlasmaElectronImpactIonization` (Voronov) covers a species — Li, the very datum
  this estimate is anchored on — the library wins by RMG's library-over-family
  precedence and this flat estimate is SUPPRESSED at model construction; the model
  keeps the sourced Te-dependent fit, not this 1 eV point. Confirmed empirically
  (see the carry report's precedence section).

rank 10: a poor rank (smaller is better; auto-fits use 11), marking this as the
least-reliable kind of number a rule can carry — a hand-placed placeholder.
Superseded the moment a real per-species electron-temperature-dependent form can
be carried by this family.
""",
)
