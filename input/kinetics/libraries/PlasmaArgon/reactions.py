#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaArgon"
shortDesc = u"Argon plasma kinetics — electron-impact ionisation and 4s metastable excitation"
longDesc = u"""
Argon plasma chemistry that is citable without fabrication. As of this writing that is
exactly TWO reactions, both electron impact on ground-state argon:

    Ar + e- => Arp + e- + e-     (index 86, ionisation, cross-section table)
    Ar + e- => Ars + e-          (index 87, excitation to the 4s metastable group, I-231)

and nothing else. ``Ars`` is metastable argon Ar(3p5 4s 3P2), whose thermochemistry is in
``PlasmaExcitedNeutralThermo`` (I-221). The provenance, level assignment and Te carrier of
the excitation entry are in its own longDesc; everything from here to the end of this
library description is about index 86 unless it says otherwise. This library exists so that a pure-argon deck need not load the whole
``PlasmaAir`` air library (33 species, 88 reactions) to reach the single argon reaction
the database holds. The air ballast contributed every wall the I-186 first-light run hit
(He2+ thermo, CH / maximumCarbeneRadicals, singlet O2s / allowSingletO2, an anion arriving
as a cation) and none of the argon chemistry; carrying argon in its own file removes that
exposure. See ``/home/alon/Code/RMG-Py-argonrun/docs/i186-ar5torr-firstlight/report.md``.

PROVENANCE
----------
The single entry below is the ACTIVE argon ionisation entry from ``PlasmaAir`` (index 86 on
the i193 base, ~line 1242), carried here verbatim — kinetics, ``shortDesc`` and ``longDesc``
unchanged — so its source travels with it. It is the entry the I-186 first-light run actually
used and exported. Its cross-section table is from:

[Golyatina2021]: R.I. Golyatina, S.A. Marinov, "Analytical Cross Section Approximation for
Electron Impact Ionization of Alkali and Other Metals, Inert Gases and Hydrogen Atoms",
Atoms 2021, 9(90), DOI: 10.3390/atoms9040090

Two datasets exist in ``PlasmaAir`` for this one reaction, and the choice between them is
stated rather than silently resolved. Alongside the active Golyatina2021 entry (51-point
cross-section grid, threshold 15.759 eV) ``PlasmaAir`` carries a COMMENTED-OUT older entry
(~line 1219, ``[LXCat]`` / Phelps, 29-point grid, threshold 15.8 eV) — a coarser, superseded
dataset for the same process. Only the finer, active Golyatina2021 grid is carried here; the
LXCat entry is neither copied nor un-commented.

TWO MODELLING FACTS THIS ENTRY CARRIES
--------------------------------------
* **It is a cross-section TABLE, not a fitted rate.** ``ElectronCollisionPlasma`` integrates
  the tabulated sigma(E) against a MAXWELLIAN electron energy distribution at Te
  (``rmgpy/kinetics/arrhenius.pyx``, ``integrate_rate_coefficient``). The Maxwellian EEDF is
  therefore a deliberate modelling choice of this mechanism, not an accident — a real
  low-pressure discharge EEDF is generally non-Maxwellian, and any rate this entry yields
  inherits that assumption.
* **RMG has no LXCat (or other cross-section) file parser.** A sigma(E) table enters the
  database only by being hand-written into a library entry. That is precisely why this entry
  is copied verbatim rather than re-derived or re-fitted: there is no import path to lean on,
  and re-typing the numbers would be an opportunity to corrupt them.

The rate law ``ElectronCollisionPlasma`` writes the free electron explicitly on both sides
of the label, so this library declares NO electron placement in
``rmgpy.electron_placement`` — exactly as ``PlasmaAir`` does not, and for the same reason.

WHY THIS LIBRARY IS DELIBERATELY SMALL
--------------------------------------
Argon here can be ionised and cannot be un-ionised, and that is the honest state of the
sourced data, not an omission to be filled:

* **Radiative recombination ``Ar+ + e- => Ar + hv`` is NOT here, and does not belong.**
  ``PlasmaRadiativeRecombination`` carries only Li+ -> Li: its Badnell (2006) table
  (``input/kinetics/badnell.yaml``) has no ``Z=18, N=17`` stage — its cation-to-neutral
  stages stop at Z=12, because Ar+ is a Cl-like ion and the systematic radiative-
  recombination programmes have not reached that isoelectronic sequence. A single citable
  Ar+ + e- -> Ar fit does exist (CHIANTI ``ar_2.rrparams``, six-parameter Badnell/Gu form,
  provenance Aldrovandi & Pequignot 1974), but I-120 established it must NOT be entered:
  its validity range in Te cannot be sourced, so it could only ship as a rate usable at any
  Te with no bound. It is also the wrong channel by ~5 orders of magnitude (dissociative
  recombination of Ar2+ dominates) and the runaway it would guard against does not occur at
  the campaign's 1 eV working point. Full measurement: I-120 report,
  ``docs/i120-argon-recombination.md`` on branch ``i120-argon-recombination``.

* **No Ar2+ entry.** Ar2+ has no citable thermochemistry, and its formation is three-body,
  which ``PlasmaReactor`` refuses.

* **No three-body (``ThirdBody``) kinetics.** The reactor refuses them.

* **No stepwise ionisation from the metastable, no quenching, no de-excitation.** Index 87
  produces Ars and nothing in this library consumes it; those channels are separate
  contracts, and the consequence (Ars can only accumulate) is stated in index 87's longDesc.

* **No estimated or analogy-derived rate.** Index 87 is a PUBLISHED rate-coefficient fit, not
  an estimate; an incomplete library that can be named is the deliverable, and a
  complete-looking one built on fabricated numbers is a failure.
"""

entry(
    index = 86,
    label = "Ar + e- => Arp + e- + e-",
    reversible = False,
    kinetics = ElectronCollisionPlasma(
        energies = ([
            15.76, 15.86, 16.26, 16.76, 17.76, 20.76, 25.76, 35.76, 45.76, 55.76, 65.76, 75.76, 85.76, 95.76, 105.76, 155.76, 205.76, 255.76, 305.76, 355.76, 405.76, 455.76, 505.76, 555.76, 605.76, 655.76, 705.76, 755.76, 805.76, 855.76, 905.76, 955.76, 1005.76, 1505.76, 2005.76, 2505.76, 3005.76, 3505.76, 4005.76, 4505.76, 5005.76, 5505.76, 6005.76, 6505.76, 7005.76, 7505.76, 8005.76, 8505.76, 9005.76, 9505.76, 10000.00
        ], 'eV/molecule'),
        sigma = ([
            0.00e+00, 1.16e-22, 5.74e-22, 1.13e-21, 2.21e-21, 5.12e-21, 9.10e-21, 1.47e-20, 1.81e-20, 2.03e-20, 2.16e-20, 2.23e-20, 2.27e-20, 2.29e-20, 2.28e-20, 2.15e-20, 1.96e-20, 1.79e-20, 1.64e-20, 1.51e-20, 1.40e-20, 1.30e-20, 1.22e-20, 1.15e-20, 1.08e-20, 1.03e-20, 9.74e-21, 9.28e-21, 8.87e-21, 8.49e-21, 8.14e-21, 7.83e-21, 7.53e-21, 5.53e-21, 4.40e-21, 3.68e-21, 3.17e-21, 2.79e-21, 2.50e-21, 2.27e-21, 2.08e-21, 1.92e-21, 1.78e-21, 1.67e-21, 1.57e-21, 1.48e-21, 1.40e-21, 1.33e-21, 1.27e-21, 1.21e-21, 1.16e-21
        ], 'm^2'),
    ),
    shortDesc = u"[Golyatina2021]",
    longDesc = u"""
Ar Ionization. Threshold 15.759 eV.
"""
)

entry(
    index = 87,
    label = "Ar + e- => Ars + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(
        A = (5.0e-15, 'm^3/(molecule*s)'),
        n = 0.74,
        Ea_g = (11.56, 'eV/molecule'),
        Ea_e = (11.56, 'eV/molecule'),
        T0 = (11604.51812, 'K'),
    ),
    shortDesc = u"[Ashida1995 via Rehman2016] Ar(4s) metastable group (3P2 + 3P0) -> Ars",
    longDesc = u"""
Electron-impact excitation of ground-state argon to the 4s METASTABLE group (I-231).

SOURCE. [Ashida1995] S. Ashida, C. Lee, M.A. Lieberman, J. Vac. Sci. Technol. A 13(5),
2498-2507 (1995), as tabulated in [Rehman2016] T. Rehman et al., J. Phys.: Conf. Ser. 682,
012035 (2016), DOI: 10.1088/1742-6596/682/1/012035 (CC-BY), Table 1 ("rate coefficient for
argon system as taken from [11]", [11] = Ashida1995). The row, verbatim:

    Ar + e -> Ar(4s)m + e        5.00 . 10-15 Te0.74 exp(-11.56/Te)

with Te in eV (the table's footnote). The table states no units; m^3/s is inferred from the
magnitudes of its other rows. Ashida1995 itself was not read for this entry.

LEVELS. The channel is the 4s METASTABLE group: 1s5 = 3P2 (11.548 eV) and 1s3 = 3P0
(11.723 eV), lumped by the source and mapped here, entire, to ``Ars`` = Ar(3P2); 3P0 is folded
into it. The resonance levels 1s4 = 3P1 and 1s2 = 1P1 are NOT included: Table 1 carries them
as a separate row of identical form, ``Ar + e -> Ar(4s)r + e``, which is not entered.

RANGE. Rehman2016 states no validity range for the fit. The only working point that source
uses is Te = 3 eV (heavy particles 600 K, 5 mTorr). The campaign evaluates it at Te = 0.85 to
0.90 eV, which is an EXTRAPOLATION below that point. The fit's stated range in Ashida1995 is
an open item.

ELECTRON TEMPERATURE, AND HOW THE ENGINE READS IT. ``TwoTemperaturePlasma`` evaluates

    k(T, Te) = A (Te/T0)^n exp(-Ea_g/(R T)) exp(Ea_e (Te - T)/(R T Te))

With Ea_g = Ea_e = E the two gas-temperature terms cancel identically,
exp(-E/RT + E/RT - E/(R Te)) = exp(-E/(R Te)), so the rate depends on Te ONLY; T0 = 1 eV =
11604.51812 K turns (Te/T0)^n into Te[eV]^0.74. The class sets
``uses_electron_temperature``, so ``PlasmaReactor`` evaluates it through
``get_rate_coefficient_two_temp(T, Te)``. Its plain ``get_rate_coefficient(T)`` is
k(T, Te=T), which at a gas temperature of ~300 K is ~1e-190 of the Te value: a consumer that
bypasses the plasma reactor gets the wrong-temperature answer, which is why this must not be
an ``Arrhenius``. Irreversible because ``PlasmaReactor`` refuses reversible Te-dependent
kinetics; there is therefore NO superelastic de-excitation Ars + e- => Ar + e-.

Hand check at Te = 0.900 eV: 0.9^0.74 = 0.92500, exp(-11.56/0.9) = 2.6407e-6,
k = 5.0e-15 * 0.92500 * 2.6407e-6 = 1.2213e-20 m^3/s = 7.355e3 m^3/(mol*s).

NOT IN THIS LIBRARY. Nothing consumes Ars here: no stepwise ionisation (separate contract),
no quenching, no diffusion to the wall. In a model built from this library alone Ars can
only accumulate.
""",
)
