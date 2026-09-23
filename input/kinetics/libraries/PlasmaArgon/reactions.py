#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaArgon"
shortDesc = u"Argon plasma kinetics — electron-impact ionisation, 4s metastable excitation and its loss channels"
longDesc = u"""
Argon plasma chemistry that is citable without fabrication: electron impact on ground-state
argon,

    Ar + e- => Arp + e- + e-     (index 86, ionisation, cross-section table)
    Ar + e- => Ars + e-          (index 87, excitation to the 4s metastable group, I-231)

and the loss channels of the metastable it makes (indices 88-93, I-232; listed at the end
of this description). ``Ars`` is metastable argon Ar(3p5 4s 3P2), whose thermochemistry is in
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

* **No Ar2+ entry.** Ar2+ has no citable thermochemistry.

* **No ``ThirdBody`` kinetics.** The reactor refuses them. A three-body collision with an
  explicit third partner written into the label (index 93, ``Ars + Ar + Ar``) is a plain
  termolecular ``Arrhenius`` and is admitted: ``PlasmaReactor`` takes one to three
  participants per side.

* **No estimated or analogy-derived rate.** Every entry is a PUBLISHED rate coefficient or
  fit, not an estimate; an incomplete library that can be named is the deliverable, and a
  complete-looking one built on fabricated numbers is a failure.

METASTABLE-ARGON CHANNELS (I-232) -- WHAT THE TEXT ABOVE NO LONGER SAYS
------------------------------------------------------------------------
Six channels of metastable argon ``Ars`` are appended, each a published Maxwellian or
constant fit (not an estimate):

* 88  ``Ars + e- => Arp + e- + e-``   stepwise ionisation, Te-dependent;
* 89  ``Ars + e- => Ar + e-``         superelastic quenching, Te-dependent, one-way;
* 90  ``Ars + Ars => Arp + Ar + e-``  pooling, gas-temperature constant;
* 91  ``Ars + e- => Ar + e-``         metastable-to-resonance mixing, taken as an effective
                                      loss to the ground state, constant; the MAXIMUM-loss
                                      limit of that channel (see its longDesc);
* 92  ``Ars + Ar => Ar + Ar``         two-body quenching by ground-state argon, constant;
* 93  ``Ars + Ar + Ar => Ar + Ar + Ar``  three-body quenching (via the Ar2 excimer), constant.

88, 89 and 91 are Ashida, Lee & Lieberman (1995), read from the tabulation in Rehman et al.
(2016), Table 1. 90, 92 and 93 are Lymberopoulos & Economou (1993), Table I, which also
lists 91's coefficient. Index 87 (I-231) produces ``Ars``; 88-93 are its sinks. There is
still no diffusion loss of ``Ars`` to the wall.
91 is a separate entry from 89 on purpose, so that a deck can drop it on its own; it is
also the largest electron loss of ``Ars`` by a factor of about 500 at 1 eV. At 5 torr and
298 K, 92 and 93 remove ``Ars`` at about 490 and 2900 per second whatever the electron
density, so at low electron density they are the dominant loss.
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
    duplicate = True,
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

LOSS OF Ars (amended by I-232). Entries 88-93 consume Ars: stepwise ionisation, electron
quenching, pooling, metastable-to-resonance mixing, and two- and three-body quenching by
ground-state argon. Only the diffusion loss to the wall is absent. ``duplicate = True`` is required here because 89
and 91 (``Ars + e- => Ar + e-``) are this reaction reversed, and the library's load-time
duplicate check matches in either direction.
""",
)

entry(
    index = 88,
    label = "Ars + e- => Arp + e- + e-",
    reversible = False,
    kinetics = TwoTemperaturePlasma(
        A = (6.8e-15, 'm^3/(molecule*s)'),
        n = 0.67,
        Ea_g = (4.20, 'eV/molecule'),
        Ea_e = (4.20, 'eV/molecule'),
        T0 = (11604.51812, 'K'),
    ),
    shortDesc = u"[Ashida1995 via Rehman2016 Table 1] Maxwellian fit, stepwise ionisation from the 4s metastable",
    longDesc = u"""
Stepwise ionisation of metastable argon, k = 6.8e-15 Te^0.67 exp(-4.20/Te) m^3/s, Te in eV.

SOURCE. S. Ashida, C. Lee & M.A. Lieberman, J. Vac. Sci. Technol. A 13(5), 2498-2507
(1995), read from its tabulation in F. Rehman et al., J. Phys.: Conf. Ser. 682, 012035
(2016), Table 1 ("Table showing the rate coefficient for argon system as taken from [11]",
[11] = Ashida 1995). Row: "Ar(4s)m + e -> Ar+ + 2e, 6.80 . 10^-15 Te^0.67 exp(-4.20/Te)",
Te in eV. The 1995 paper itself was not re-read.

LEVEL. Rehman's model "contains 5 levels: the ground level (Ar), 4s metastable
(Ar(4s)m), 4s resonance (Ar(4s)r), 4p (Ar(4p)) and ion level (Ar+)". The number therefore
covers the metastable GROUP, Ar(4s 3P2) + Ar(4s 3P0), which ``Ars`` represents here; the
thermochemistry of ``Ars`` is that of 3P2 alone (``PlasmaExcitedNeutralThermo``). The 4.20 eV
threshold agrees with IE - E(3P2) = 15.7596117 - 11.54835442 = 4.21126 eV to 0.3%. Cost: the
3P0 member (0.17 eV higher, g = 1 against 5) is folded into the 3P2 species.

ELECTRON TEMPERATURE. ``TwoTemperaturePlasma`` with Ea_g = Ea_e = E reduces exactly to
A (Te/T0)^n exp(-E/(R Te)), independent of the gas temperature; T0 = 11604.51812 K = 1 eV
makes (Te/T0) the temperature in eV. ``PlasmaReactor`` evaluates it through
``get_rate_coefficient_two_temp(T, Te)``. Plain ``get_rate_coefficient(T)`` evaluates it at
Te = T and is wrong for this entry.

HAND CHECK at Te = 0.900 eV (10442.07 K): 0.9^0.67 = 0.931842, exp(-4.20/0.9) =
9.40356e-3, k = 6.8e-15 x 0.931842 x 9.40356e-3 = 5.95859e-17 m^3/s = 3.58835e7 m^3/(mol s).

Irreversible: its reverse is three-body recombination, and the reactor refuses reversible
Te-dependent reactions.
""",
)

entry(
    index = 89,
    label = "Ars + e- => Ar + e-",
    duplicate = True,
    reversible = False,
    kinetics = TwoTemperaturePlasma(
        A = (4.3e-16, 'm^3/(molecule*s)'),
        n = 0.74,
        Ea_g = (0, 'eV/molecule'),
        Ea_e = (0, 'eV/molecule'),
        T0 = (11604.51812, 'K'),
    ),
    shortDesc = u"[Ashida1995 via Rehman2016 Table 1] Maxwellian fit, superelastic quenching of the 4s metastable",
    longDesc = u"""
Superelastic electron quenching of metastable argon to the ground state,
k = 4.3e-16 Te^0.74 m^3/s, Te in eV.

SOURCE and LEVEL as for index 88. Row: "Ar(4s)m + e -> Ar + e, 4.30 . 10^-16 Te^0.74".

ONE-WAY BY CONSTRUCTION. This is the reverse of excitation ``Ar + e- => Ars + e-``
(index 87, I-231). Both directions are entered as
independent irreversible fits because the reactor refuses reversible Te-dependent reactions,
so detailed balance between them is NOT enforced by the engine. Checked by hand against
the I-231 fit 5.0e-15 Te^0.74 exp(-11.56/Te): k_q/k_exc = 0.086 exp(11.56/Te), while
detailed balance at Te requires (g0/g*) exp(dE/Te). With the lumped 4s weight g* = 12 the
prefactor 1/12 = 0.0833 agrees to 3%; with the 3P2 weight g* = 5 of the thermo entry
(prefactor 0.2) the pair is inconsistent by a factor 2.3. The factor is the cost of the
level assignment. (The metastable-group weight g* = 5 + 1 = 6 gives prefactor 0.167, off by
1.9.) The source enters BOTH 4s groups with the same excitation fit, so 0.086 ~ 1/12 is the
balance of the whole 4s manifold; the pair is not balanced for either group on its own.

HAND CHECK at Te = 0.900 eV: 0.9^0.74 = 0.924995, k = 4.3e-16 x 0.924995 =
3.97748e-16 m^3/s = 2.39529e8 m^3/(mol s).

``duplicate = True`` IS REQUIRED, AND SO IS ITS PARTNER'S. ``KineticsLibrary.check_for_duplicates``
compares with ``is_isomorphic`` in EITHER direction, so this entry and the excitation entry 87
are reported as duplicates of each other ("Unexpected duplicate reaction Ar + e- => Ars + e-
... Reaction index 89 matches index 87", measured on RMG-Py-plasma@74b683639 with I-231's
entry inserted) and the library refuses to load unless BOTH carry the flag. The flag does not
merge them: ``convert_duplicates_to_multi`` compares same-direction only, and the exporters
recompute Chemkin DUPLICATE marks from the whole deck. It is a false positive of the load
check for two one-way reactions, recorded here rather than worked around.
""",
)

entry(
    index = 90,
    label = "Ars + Ars => Arp + Ar + e-",
    reversible = False,
    kinetics = Arrhenius(
        A = (6.2e-16, 'm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"[Lymberopoulos1993 Table I, R6] metastable pooling, gas-temperature constant",
    longDesc = u"""
Metastable pooling (Penning ionisation between two metastables), k = 6.2e-16 m^3/s,
temperature independent. A heavy-particle collision: it belongs to the gas temperature, so
it is a plain ``Arrhenius`` and does not carry ``uses_electron_temperature``.

SOURCE. D.P. Lymberopoulos & D.J. Economou, J. Appl. Phys. 73(8), 3668-3679 (1993), Table I
("Important collision processes in argon discharge"), row 6, verbatim:

    6   Metastable pooling   Ar*+Ar*->Ar+ +Ar+e   ...   k_mp=6.2x10^-10   48-50

in cm^3/s (the table footnote: "Units are cm3/s except for k3q which is in cm6/s"). The
paper's own references 48-50 were not read. Rehman et al. (2016) Table 1, the source of
88/89/91, carries no pooling row. LEVEL as for index 88: the paper's ``Ar*`` is "a composite
(3P0 and 3P2) metastable level". Energetics: 2 x 11.548 = 23.10 eV > 15.76 eV, exothermic.

Irreversible: the reverse is three-body, which ``PlasmaReactor`` refuses.

HAND CHECK: 6.2e-16 m^3/s x 6.02214076e23 = 3.73373e8 m^3/(mol s).
""",
)

entry(
    index = 91,
    label = "Ars + e- => Ar + e-",
    duplicate = True,
    reversible = False,
    kinetics = TwoTemperaturePlasma(
        A = (2.0e-13, 'm^3/(molecule*s)'),
        n = 0,
        Ea_g = (0, 'eV/molecule'),
        Ea_e = (0, 'eV/molecule'),
        T0 = (11604.51812, 'K'),
    ),
    shortDesc = u"[Ashida1995 via Rehman2016 Table 1] metastable-to-resonance mixing, effective loss to ground; MAXIMUM-loss limit",
    longDesc = u"""
Electron-induced mixing of the 4s metastable group into the 4s resonance group, entered as
an EFFECTIVE loss of ``Ars`` to the ground state: k = 2.0e-13 m^3/s, independent of Te.

THIS IS THE MAXIMUM-LOSS LIMIT OF THE CHANNEL, NOT ITS PHYSICAL VALUE. The physical loss lies
between a deck with this entry and a deck without it.

SOURCE as for index 88. Rows: "Ar(4s)m + e -> Ar(4s)r + e, 2.00 . 10^-13" and
"Ar(4s)r -> Ar + hv, 3.00 . 10^7" (s^-1). The same coefficient is row 5 of Lymberopoulos &
Economou (1993) Table I: "5  Quenching to resonant  Ar*+e->Ar^r+e  ...  k_r=2x10^-7  48-50"
(cm^3/s), where the resonant states "decay by emission of radiation".

WHY THE PRODUCT IS Ar, AND WHY THAT IS AN UPPER BOUND. The database has no resonance-level
species, so the two-step path Ar(4s)m + e -> Ar(4s)r + e, Ar(4s)r -> Ar + hv is collapsed
into one step. The collapse assumes two things: the resonance level decays at the
UNTRAPPED 3.0e7 s^-1 of the same table, and none of it mixes back into the metastable group
before it decays. Every resonance atom made is then lost, which is the most this channel can
remove. At 5 torr the resonance line is heavily radiation-trapped: the effective decay is
orders of magnitude slower than 3.0e7 s^-1, so a large part of the resonance population is
mixed back to ``Ars`` by electrons first, and the real net loss is smaller. Trapping is not
modelled here. Report a deck's result with 91 on and with 91 off; the physical answer lies
between the two.

A SEPARATE ENTRY FROM 89 ON PURPOSE, so that a deck can remove it without touching the
quenching fit. It is the larger channel by far: at Te = 0.900 eV, 2.0e-13 / 3.97748e-16 = 503.

CARRIER. ``TwoTemperaturePlasma`` with n = 0 and Ea_g = Ea_e = 0 is the constant A at every
(T, Te). It is an electron-impact rate, so it carries ``uses_electron_temperature`` like 88/89.
It is deliberately NOT a plain ``Arrhenius``. ``TwoTemperaturePlasma`` is not an ``Arrhenius``
subclass, so ``convert_duplicates_to_multi`` leaves 89 and 91 as two entries and does not fold
them into one ``MultiArrhenius``. That fold would evaluate 89's Te law at the gas temperature.

``duplicate = True`` is required: 91 is a same-direction duplicate of 89, and the
reverse-direction partner of the excitation entry 87.

HAND CHECK: 2.0e-13 m^3/s x 6.02214076e23 = 1.204428e11 m^3/(mol s), at any Te.
""",
)

entry(
    index = 92,
    label = "Ars + Ar => Ar + Ar",
    reversible = False,
    kinetics = Arrhenius(
        A = (3e-15, 'cm^3/(molecule*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"[Lymberopoulos1993 Table I, R7] two-body quenching of the metastable by ground-state argon",
    longDesc = u"""
Two-body quenching of metastable argon by a ground-state atom, k = 3e-15 cm^3/s,
temperature independent. A heavy-particle collision, so a plain gas-temperature
``Arrhenius`` without ``uses_electron_temperature``, like index 90.

SOURCE. D.P. Lymberopoulos & D.J. Economou, J. Appl. Phys. 73(8), 3668-3679 (1993), Table I,
row 7, verbatim:

    7   Two-body quenching   Ar*+Ar->2Ar   ...   k_2q=3x10^-15   48-50

in cm^3/s (table footnote). The paper's text: "the only quenching reactions considered are
two- and three-body collisions with ground state argon atoms". Its references 48-50 were not
read. LEVEL as for index 90.

SIZE. At 5 torr and 298.15 K, n_Ar = 1.6195e17 cm^-3 and k n_Ar = 486 s^-1, independent of the
electron density.

Irreversible: the reverse, excitation by a thermal ground-state atom, is negligible at the gas
temperature, and the pair would otherwise need the ``Ars`` thermochemistry to be balanced.

HAND CHECK: 3e-15 cm^3/s = 3e-21 m^3/s; x 6.02214076e23 = 1.806642e3 m^3/(mol s).
""",
)

entry(
    index = 93,
    label = "Ars + Ar + Ar => Ar + Ar + Ar",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.1e-31, 'cm^6/(molecule^2*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"[Lymberopoulos1993 Table I, R8] three-body quenching of the metastable via the Ar2 excimer",
    longDesc = u"""
Three-body quenching of metastable argon by two ground-state atoms, k = 1.1e-31 cm^6/s,
temperature independent, gas-temperature ``Arrhenius``.

SOURCE. D.P. Lymberopoulos & D.J. Economou, J. Appl. Phys. 73(8), 3668-3679 (1993), Table I,
row 8, verbatim:

    8   Three-body quenching   Ar*+2Ar->Ar2+Ar   ...   k_3q=1.1x10^-31   48-50

with the table footnote "Units are cm3/s except for k3q which is in cm6/s". References 48-50
were not read. LEVEL as for index 90.

THE PRODUCT. The real product is the Ar2* excimer (the table writes Ar2), not two ground-state
atoms. The excimer is bound only in its excited state and radiates promptly in the vacuum-
ultraviolet continuum, dissociating to 2 Ar + hv. The database has no Ar2 excimer species, so
the step is collapsed to ``Ar + Ar + Ar``. The collapse loses the emitted photon and nothing
the reactor tracks.

THE THIRD PARTNER IS EXPLICIT. This is a termolecular ``Arrhenius`` with both argon atoms in
the label, NOT a ``ThirdBody`` rate. ``PlasmaReactor`` refuses ``ThirdBody`` kinetics but
admits one to three participants per side and multiplies all three concentrations. Only argon
is a collider here; in a mixture, other gases would also quench and are not represented.

SIZE. At 5 torr and 298.15 K, k n_Ar^2 = 1.1e-31 x (1.6195e17)^2 = 2885 s^-1, independent of
the electron density. That is the largest single loss of ``Ars`` at low electron density.

Irreversible: the reverse is not a channel anyone holds.

HAND CHECK: 1.1e-31 cm^6/s = 1.1e-43 m^6/s; x (6.02214076e23)^2 = 3.98928e4 m^6/(mol^2 s).
""",
)
