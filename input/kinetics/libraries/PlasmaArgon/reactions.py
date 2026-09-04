#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaArgon"
shortDesc = u"Argon plasma kinetics — electron-impact ionisation only"
longDesc = u"""
Argon plasma chemistry that is citable without fabrication. As of this writing that is
exactly ONE reaction: electron-impact ionisation of neutral argon,

    Ar + e- => Arp + e- + e-

and nothing else. This library exists so that a pure-argon deck need not load the whole
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

WHY THIS LIBRARY IS DELIBERATELY ONE ENTRY
------------------------------------------
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

* **No estimated, fitted or analogy-derived rate.** An incomplete library that can be named
  is the deliverable; a complete-looking one built on fabricated numbers is a failure.
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
