#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Attachment/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Training reactions for non-dissociative electron attachment, A + e- => A-.

The electron is implicit: the family carries `electrons = -1`, so a label written
as "O2 <=> O2-" means "O2 + e- <=> O2-". Charge closes because of that flag, not
because the label is balanced as written.

READ THIS BEFORE ADDING OR TRUSTING A NUMBER HERE
-------------------------------------------------

Two representational constraints bind every rate in this file, and both are
properties of RMG rather than of the chemistry:

1. `KineticsFamily.add_rules_from_training` accepts only `Arrhenius` (and the
   three Surface* kinetics types). `ThirdBody` raises NotImplementedError, and so
   would `ElectronCollisionPlasma`. A family training set therefore *cannot*
   carry a three-body rate coefficient, and cannot carry a cross section.

2. Plain `Arrhenius` has no `uses_electron_temperature` flag - only the four
   plasma kinetics classes set it. **Every rate in this file is therefore
   evaluated at the GAS temperature.** Attachment is electron-driven, so in a
   two-temperature reactor the gas temperature is the wrong independent variable
   outright. This is not a tuning error, it is the wrong axis.

Constraint 1 is what forces the numbers below. The dominant non-dissociative
attachment channel for O2 and OH is three-body,

    A + e- + M  ->  A- + M,

which is how [JensenJones1977] reports it and how the PlasmaAir kinetics library
stores it (as `ThirdBody`, in cm^6/(mol^2*s)). Since the family template is
effectively bimolecular, entries 1 and 2 are **effective two-body rate
coefficients formed as k2 = k3 * [M] at a folded-in reference density**:

    P    = 5 torr  (666.611842 Pa)
    T    = 298.15 K
    [M]  = P / (kB*T) = 1.619403e17 cm^-3 = 2.689082e-7 mol/cm^3

5 torr is the I-007 baseline (argon) and sits inside the 1-10 torr band the
additive sweep covers. **These rates are LINEAR IN DENSITY and are therefore
wrong at any other pressure, by the density ratio.** At 1 atm they would be 152x
larger; across 1-10 torr they are wrong by 5x either way. A family that attaches
electrons 152x too fast under-predicts n_e, which looks like the fix worked and
is a worse failure than the over-prediction it was built to remove.

Entry 3 (O + e- => O-) carries no folded density: it is a genuine two-body
radiative-attachment rate and is pressure-independent.

These are INTERIM values. The right representation is a pressure-dependent form
evaluated at the electron temperature - preferably an `ElectronCollisionPlasma`
cross section, which carries no EEDF assumption at all - and it is blocked on
`add_rules_from_training` accepting more than plain `Arrhenius`. The ranks below
say so.

Reference legend:
[JensenJones1977]: D.E. Jensen and G.A. Jones, "Reaction Rate Coefficients for
    Flame Calculations", RAE Technical Report 77020, 1977, p. 11.
    https://apps.dtic.mil/sti/tr/pdf/ADA047018.pdf
[McElroy2013]: D. McElroy, C. Walsh, A.J. Markwick, M.A. Cordiner, K. Smith,
    T.J. Millar, "The UMIST database for astrochemistry 2012", Astron. Astrophys.
    550 (2013) A36. DOI: 10.1051/0004-6361/201220465
"""

entry(
    index = 1,
    label = "O2 <=> O2-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6807e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 9,
    shortDesc = u"""INTERIM, PRESSURE-BAKED. Effective 2-body k2 = k3*[M] with k3 = 3.6e17 cm^6/(mol^2*s) = 9.9266e-31 cm^6/s [JensenJones1977 p.11], folded at [M] = 1.6194e17 cm^-3 (5 torr, 298.15 K). LINEAR IN DENSITY - wrong at any other pressure by the density ratio (152x at 1 atm). Gas temperature, not electron temperature.""",
    longDesc = u"""
Source is the three-body attachment O2 + e- + M => O2- + M, [JensenJones1977] p. 11,
as stored in the PlasmaAir kinetics library:

    k3 = 3.6e17 cm^6/(mol^2*s) = 9.926604e-31 cm^6/s

Folded to an effective two-body coefficient at the reference density
[M] = 1.619403e17 cm^-3 = 2.689082e-7 mol/cm^3 (5 torr, 298.15 K):

    k2 = k3 * [M] = 1.607517e-13 cm^3/s = 9.6807e10 cm^3/(mol*s)

Reference state, spelled out because it is baked in and invisible in the number:
    P = 5 torr, T = 298.15 K, [M] = 1.619403e17 cm^-3.
k2 scales linearly with [M]. At 1 atm it would be 1.4715e13 cm^3/(mol*s), 152x
larger; anywhere in the 1-10 torr sweep it is wrong by up to 5x either way.

Temperature: GAS temperature. The source is a flame-chemistry compilation with no
electron-temperature dependence, and plain Arrhenius cannot express one. For a
two-temperature reactor this is the wrong independent variable, not merely an
imprecise one.
EEDF: none assumed - this is not a cross-section-derived rate, so no electron
energy distribution is implied. It also therefore carries no Te dependence at all,
which is the main thing wrong with it for a non-thermal discharge.

Rank 9: interim. Superseded as soon as a real pressure-dependent, electron-
temperature-aware form can be carried by a family training set.
""",
)

entry(
    index = 2,
    label = "OH <=> OH-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9580e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 9,
    shortDesc = u"""INTERIM, PRESSURE-BAKED. Effective 2-body k2 = k3*[M] with k3 = 1.1e17 cm^6/(mol^2*s) = 3.0331e-31 cm^6/s [JensenJones1977 p.11], folded at [M] = 1.6194e17 cm^-3 (5 torr, 298.15 K). LINEAR IN DENSITY - wrong at any other pressure by the density ratio (152x at 1 atm). Gas temperature, not electron temperature.""",
    longDesc = u"""
Source is the three-body attachment OH + e- + M => OH- + M, [JensenJones1977] p. 11,
as stored in the PlasmaAir kinetics library:

    k3 = 1.1e17 cm^6/(mol^2*s) = 3.033129e-31 cm^6/s

Folded to an effective two-body coefficient at the reference density
[M] = 1.619403e17 cm^-3 = 2.689082e-7 mol/cm^3 (5 torr, 298.15 K):

    k2 = k3 * [M] = 4.911858e-14 cm^3/s = 2.9580e10 cm^3/(mol*s)

Reference state, spelled out because it is baked in and invisible in the number:
    P = 5 torr, T = 298.15 K, [M] = 1.619403e17 cm^-3.
k2 scales linearly with [M]. At 1 atm it would be 4.4960e12 cm^3/(mol*s), 152x
larger.

Temperature: GAS temperature, for the same reason as entry 1, and wrong on the
same axis.
EEDF: none assumed; not a cross-section-derived rate.

Rank 9: interim, on the same grounds as entry 1.
""",
)

entry(
    index = 3,
    label = "O <=> O-",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.0332e+08, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 7,
    shortDesc = u"""Radiative attachment O + e- => O- + hv, k = 1.5e-15 cm^3/s [McElroy2013]. Genuinely 2-body: NO folded-in density, pressure-independent. Gas temperature, not electron temperature.""",
    longDesc = u"""
There is no O + e- => O- entry in PlasmaAir; the O- in that library is produced by
dissociative attachment to O2 / H2O, which is a different family. The value here is
the genuine two-body radiative attachment channel

    O + e-  =>  O- + hv,    k = 1.5e-15 cm^3/s

as tabulated in the UMIST astrochemistry database [McElroy2013] (alpha = 1.5e-15,
beta = 0, gamma = 0; temperature-independent over 10-41000 K). In molar units:

    k = 1.5e-15 * 6.02214076e23 = 9.0332e8 cm^3/(mol*s)

Reference state: NONE. This is a true two-body rate coefficient with no third body
and no folded-in density, so unlike entries 1 and 2 it is valid at any pressure.

Temperature: GAS temperature. The source rate is temperature-independent, so the
distinction is moot for this entry read alone; it is not moot for how this entry
averages with its siblings up the tree.
EEDF: none assumed - a radiative-attachment rate coefficient, not a cross-section
integral.

CAVEAT, deliberate and load-bearing: this rate is ~2 orders of magnitude below
entries 1 and 2 partly because radiative attachment really is slow, and partly
because entries 1 and 2 have a 5 torr third-body density folded into them while
this one has none. Do not read the ratio as chemistry, and note that the ratio
itself changes with the reference pressure chosen for entries 1 and 2.

Rank 7: better provenance than the pressure-baked entries (no folded density,
direct two-body literature value), but still a gas-temperature Arrhenius standing
in for an electron-driven process.
""",
)
