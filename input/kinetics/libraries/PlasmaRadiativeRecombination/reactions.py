#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaRadiativeRecombination"
shortDesc = u"Radiative recombination of atomic cations, from the Badnell (2006) fits"
longDesc = u"""
Radiative recombination of a monatomic cation with a free electron, one recombination
stage:

    A+ + e-  =>  A + hv

carried in RMG's database representation as ``A+ => A`` with ``electrons = -1``. Unlike
electron-impact ionization, this channel has no spectator electron: the incident electron
is captured and does not come out again, so the single electron is both the whole incident
order and the whole net change. That is the degenerate case where a one-sided declaration
would have sufficed, and it is why this library's placement declaration reads
``(reactant_count, product_count) = (1, 0)`` - the same numbers attachment declares, for
the same structural reason and different chemistry.

The photon is not represented. RMG has no photon species, and ``hv`` carries neither
charge nor mass, so no balance check misses it. What IS lost by omitting it is the energy
sink: this reaction removes 5.392 eV per event from the electron population and the model
has nowhere to put it. `PlasmaReactor` prescribes ``Te`` rather than solving an electron
energy equation, so that omission costs nothing here - but it would matter to any reactor
that closed the electron energy balance, and it is recorded rather than assumed away.

WHAT THIS CHANNEL IS, AND WHAT IT IS NOT
----------------------------------------
**It is not the inverse of electron-impact ionization.** A binding project ruling forbids
treating the reverse of a process as the same elementary channel run backwards, and this
is the case that makes the rule concrete. The physical inverse of
``Li + e- => Li+ + 2 e-`` is **three-body (collisional) electron-ion recombination**,
``Li+ + 2 e- => Li + e-`` - same participants, run the other way, third order, with the
second electron carrying off the binding energy. Radiative recombination is a *different
forward channel*: second order, with a photon carrying the energy instead. Its own inverse
is photoionization ``Li + hv => Li+ + e-``, which needs a radiation field the reactor does
not have. All three are distinct processes with distinct rates.

**It is therefore not the dominant electron sink.** At every electron density this campaign
has named, three-body recombination outruns radiative recombination - by ~2x at
n_e = 1e10 cm^-3 and by ~9x at 1e14 cm^-3, at Te = 1 eV. Three-body recombination has no
shipped fit anywhere in this database (``input/kinetics/`` holds ``voronov.yaml`` and
``badnell.yaml`` and nothing else), so it is not entered here and no rate for it is
authored. The measurements, and what would be needed to close that gap, are in
``docs/i119-recombination-loss.md``.

WHY A LIBRARY AND NOT A FAMILY
------------------------------
The same argument that made ionization a library, and it transfers without weakening;
the long form is ``docs/i114-ionisation-owner.md``. The Badnell fit is indexed by
``(Z, N)`` - a nuclear charge and an electron count, an *atomic identity*, not a molecular
group - and its five parameters (A, B, T0, T1, and the optional C, T2) describe one ion's
recombination cross-section summed over final states. There is no group-additivity trend to
interpolate along, so an averaged "estimate" between two elements' fits would be a
fabricated number rather than an uncertain one. RMG could not build such a tree in any case:
``family.average_kinetics`` guards on a closed allowlist of
``[Arrhenius, SurfaceChargeTransfer, ArrheniusChargeTransfer, Marcus]`` and
``BadnellRRArrhenius`` is not on it, exactly as ``VoronovEIArrhenius`` is not.

COVERAGE, AND WHY IT IS ONE ENTRY
---------------------------------
``input/kinetics/badnell.yaml`` holds 33 nuclear charges spanning Z = 1-54 and 318 ``(Z, N)``
stages. Only ``N = Z - 1`` - a singly charged cation capturing an electron to give the
neutral - is a stage this database can represent at all; the other 306 are multiply charged
ions, which is a separate representational problem. That leaves **12**: Z = 1-12
(H+, He+, Li+, Be+, B+, C+, N+, O+, F+, Ne+, Na+, Mg+).

Of those 12, RMG can construct both endpoints in their gas-phase ground states for **6**:
H, He, Li, N, O, Ne. (Be, B, Na and Mg have no RMG atom types - ``KeyError``; C+ as
``C u1 p1 c+1`` and F+ as ``F u2 p2 c+1`` fail ``AtomTypeError``.) Of those 6, exactly
**one** has thermochemistry for the reactant cation in this database as a free monatomic
ion: Li+ (``[Lip]``, ``LithiumPrimaryThermo`` index 65, ``computationalLithiumElectrode``).
H+ exists as ``proton`` in ``electrocatThermo`` / ``electrocatLiThermo``, but that is an
electrocatalysis reference species carrying the computational-hydrogen-electrode convention,
not a gas-phase proton.

So coverage narrows 318 -> 12 -> 6 -> 1, and the one is Li+. Two consequences worth naming:

* The bound is thermochemistry, not this table and not this owner. Adding He+, N+, O+ or Ne+
  needs monatomic-cation thermochemistry that does not exist here; that is a thermo ticket,
  and until it lands those reactions could not enter a model whichever owner was chosen.
* **Argon has no radiative-recombination fit here at all.** Ar is this campaign's benchmark
  bath gas and its electron-impact ionization *is* in ``voronov.yaml``, but ``badnell.yaml``
  carries no ``Z = 18, N = 17`` stage - the table's cation-to-neutral stages stop at Z = 12.
  An Ar-bath model can ionize argon and cannot radiatively recombine it.

WHAT HAPPENS TO A SPECIES THIS LIBRARY DOES NOT COVER
-----------------------------------------------------
Nothing, and visibly. A library has no template, so an uncovered cation is never offered a
recombination reaction: no match, no tree descent, no averaged rule, no estimate. The
absence shows up as a missing channel, which a mechanism reader can see, rather than as a
wrong number, which they cannot.

USING IT
--------
Add ``'PlasmaRadiativeRecombination'`` to ``kineticsLibraries`` in the input file, supply the
electron species, and supply ``[Lip]``. The reactor-facing form ``Li+ + e- => Li`` is produced
by ``rmgpy.electron_placement.resolve_electron_placement`` from the ``(1, 0)`` declaration;
the entry below is the canonical database form and must not be written with an explicit
electron participant, which the resolver refuses as double representation.
"""

entry(
    index = 0,
    label = "[Lip] => [Li]",
    degeneracy = 1,
    reversible = False,
    kinetics = BadnellRRArrhenius(Z=3, N=2),
    shortDesc = u"Li+ + e- => Li + hv",
    longDesc = u"""
Badnell (2006), Z=3, N=2: the Li II -> Li I radiative recombination stage. ``N`` is the
electron count *prior to* recombination, so N=2 is the two-electron ion Li+, per the
table's own ``notes`` field. Loaded from ``input/kinetics/badnell.yaml`` by ``(Z, N)``
rather than transcribed, so the shipped table stays the single source of the numbers and
no rate is authored here: A = 8.7e-12 cm^3/(molecule*s), B = 0.364, T0 = 147.0 K,
T1 = 7.153e6 K, C = 0.1508, T2 = 7.154e5 K.

``BadnellRRArrhenius`` supplies ``electrons = -1`` itself; ``KineticsLibrary.load``
propagates that onto the reaction, which is what lets ``Reaction.is_balanced`` close the
+1 -> 0 charge gap. Valid over Te = 10 K to 1e7 K per the class's own defaults - wider than
any condition an alkali plasma model is likely to reach, so unlike the Voronov ionization
entry this fit is never used outside its stated range.

Rate, measured against the pinned runtime (m^3/(mol*s), and cm^3/s per particle):

    Te = 0.3 eV (3481 K)   k = 3.392e5   alpha = 5.632e-13
    Te = 0.5 eV (5802 K)   k = 2.270e5   alpha = 3.770e-13
    Te = 1.0 eV (11605 K)  k = 1.301e5   alpha = 2.161e-13
    Te = 2.0 eV (23209 K)  k = 7.363e4   alpha = 1.223e-13

Physical inverse, named and NOT implemented here: **photoionization** Li + hv => Li+ + e-,
which is driven by a radiation field ``PlasmaReactor`` does not have. This reaction is NOT
the inverse of electron-impact ionization; that is three-body recombination
Li+ + 2 e- => Li + e-, a third-order channel with no shipped fit in this database.
""",
    reference = None,
    referenceType = "",
)
