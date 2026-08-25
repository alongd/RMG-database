#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaElectronImpactIonization"
shortDesc = u"Electron-impact ionization of neutral atoms, from the Voronov (1997) fits"
longDesc = u"""
Electron-impact ionization of a ground-state neutral atom, one ionization stage:

    A + e-  =>  A+ + 2 e-

carried in RMG's database representation as ``A => A+`` with ``electrons = +1``. The
incident electron is a spectator - it comes out again - so it is not part of the net
count; only the liberated surplus is. The incident electron is restored, on both sides,
by ``rmgpy.electron_placement.resolve_electron_placement`` from this library's
``(reactant_count, product_count) = (1, 2)`` placement declaration, which is what makes
the reactor-facing reaction second order and therefore dimensionally consistent with the
``cm^3/(molecule*s)`` Voronov A-factor.

WHY A LIBRARY AND NOT A FAMILY
------------------------------
This is a database decision and it was argued, not assumed. The full argument, with the
measurements behind it, is ``docs/i114-ionisation-owner.md``. In short:

1. **A family here could not generalise even in principle.** A safe ionization family
   would have to follow the ``Plasma_Electron_Attachment`` pattern - a ``LogicOr`` root
   whose members are exactly the trained groups - because the Voronov fit is per-species
   (each stage has its own A, P, X, K and its own ionization threshold dE), with no
   group-additivity trend to interpolate along. Such a family matches exactly the species
   it has data for and nothing else, which is precisely the set of entries you would
   otherwise write here. Its generativity is zero, and generativity is the only thing a
   family buys.

2. **RMG cannot build a rate-rule tree out of Voronov fits at all.** Every trained family
   runs ``fill_rules_by_averaging_up``, and both averaging implementations crash on this
   rate law: ``KineticsRules._get_average_kinetics`` raises
   ``AttributeError: 'VoronovEIArrhenius' object has no attribute 'n'``, and
   ``family.average_kinetics`` raises ``UnboundLocalError`` from its own type guard
   (``VoronovEIArrhenius`` is not in its allowlist ``[Arrhenius, SurfaceChargeTransfer,
   ArrheniusChargeTransfer, Marcus]``). A Voronov-trained family is therefore limited to
   one training entry per node forever - a library wearing template machinery.

3. **Forward and reverse must be separate one-way processes.** A binding ruling forbids
   treating the reverse of a process as the same channel run backwards, and the physical
   inverse of electron-impact ionization is three-body (collisional) recombination
   ``A+ + 2 e- => A + e-``, not ionization backwards. A library entry is one-way by
   construction: this entry is ``=>``, ``reversible = False``. Radiative recombination
   ``A+ + e- => A + hv`` (Badnell 2006, ``input/kinetics/badnell.yaml``) is a *different*
   forward channel, not this one's inverse, and is deliberately not entered here.
   ``PlasmaReactor`` independently refuses any reversible electron-temperature-dependent
   reaction, so a reversible entry could not have run anyway.

WHAT HAPPENS TO A SPECIES THIS LIBRARY DOES NOT COVER
-----------------------------------------------------
**Nothing at all, silently and correctly.** A library has no template: an uncovered species
is simply never given an ionization reaction. There is no match, no estimate, and no
fabricated rate. That is the whole point of choosing a library here - the failure mode this
project keeps hitting is a template that matches more than its data supports, and a library
cannot exhibit it. If a mechanism needs ionization for a species not listed above, the
absence shows up as a missing channel, which is visible, rather than as a wrong number,
which is not.

COVERAGE, AND WHY IT IS ONE ENTRY
---------------------------------
``input/kinetics/voronov.yaml`` holds 13 elements and 134 ``(Z, N)`` ionization stages, of
which 13 are the neutral -> +1 stage (one per element). Of those 13, RMG can construct both
endpoints in their gas-phase ground states for 7: H, He, Li, N, O, Si, Ar. (Na, Mg, Al, K
and Ca have no RMG atom types - ``KeyError``; C+ as ``C u1 p1 c+1`` fails
``AtomTypeError``.) Of those 7, exactly one has thermochemistry for the product cation in
this database as a free monatomic ion: Li+ (``[Lip]``, ``LithiumPrimaryThermo``,
``computationalLithiumElectrode``). H+ exists as ``proton`` in ``electrocatThermo`` /
``electrocatLiThermo``, but that is an electrocatalysis reference species, not a gas-phase
proton, and using it here would import an unrelated reference state.

So one entry is not timidity, it is the coverage. Adding He+, N+, O+, Si+ or Ar+ needs
monatomic-cation thermochemistry that does not exist yet; that is a thermo ticket, and until
it lands those reactions could not be put into a model regardless of which owner was chosen.

USING IT
--------
Add ``'PlasmaElectronImpactIonization'`` to ``kineticsLibraries`` in the input file, supply
the electron species, and supply ``[Li]``. The reactor-facing form is produced by the
placement resolver; the entry below is the canonical database form and must not be written
with an explicit electron participant (the resolver refuses double representation).
"""

entry(
    index = 0,
    label = "[Li] => [Lip]",
    degeneracy = 1,
    reversible = False,
    kinetics = VoronovEIArrhenius(Z=3, N=3),
    shortDesc = u"Li(2S) + e- => Li+ + 2 e-",
    longDesc = u"""
Voronov (1997) Table I, Z=3, N=3: the Li I -> Li II stage, dE = 5.4 eV.
Loaded from ``input/kinetics/voronov.yaml`` by ``(Z, N)`` rather than transcribed, so the
shipped table stays the single source of the numbers and no rate is authored here.

``VoronovEIArrhenius`` supplies ``electrons = +1`` itself; ``KineticsLibrary.load``
propagates that onto the reaction, which is what lets ``Reaction.is_balanced`` close the
0 -> +1 charge gap. Valid over Te = 1 eV to 20 keV (11 604.5 K to 2.3209e8 K) per the
table's own Tmin/Tmax; k is vanishingly small below the 5.4 eV threshold
(k(Te = 300 K) = 6.9e-82 m^3/(mol*s)) and reaches 5.0e7 m^3/(mol*s) at Te = 10 000 K.

Physical inverse, named and NOT implemented here: three-body (collisional) recombination
Li+ + 2 e- => Li + e-. Radiative recombination Li+ + e- => Li + hv (Badnell 2006) is a
separate forward channel, not this reaction's inverse.
""",
    reference = None,
    referenceType = "",
)
