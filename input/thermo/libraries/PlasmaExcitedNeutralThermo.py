#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaExcitedNeutralThermo"
shortDesc = u"Sourced gas-phase thermochemistry for electronically excited NEUTRAL species of plasma interest"
longDesc = u"""
WHY THIS LIBRARY EXISTS
-----------------------
A low-pressure argon discharge keeps most of its non-ionising excited-state energy in the 4s
metastable levels, and they are the principal route into stepwise ionisation. Until this file,
this database represented argon with exactly two species - ground state ``Ar`` and the cation
``Ar+`` - and had no third. The atom type that makes a third one perceivable, ``Ar0e``, landed in
RMG-Py (``rmgpy/molecule/atomtype.py``, and see ``docs/i222-metastable-argon-atomtype/`` in that
repository); what was still missing was thermochemistry, and a species with no thermochemistry
cannot exist in RMG at all. Measured on the engine before this file existed: a ``Species`` built
from ``Ar u2 p3 c0`` perceives cleanly as ``Ar0e``, and then ``get_thermo_data`` raises

    AtomTypeError: Unable to determine atom type for atom Ar, which has 2 single bonds, ...,
                   3 lone pairs, and +0 charge.

from inside ``estimate_radical_thermo_via_hbi`` -- group additivity saturates the two radicals
with hydrogens, producing an ``ArH2`` that has no atom type. So metastable argon fails LOUDLY
rather than being silently fabricated, which is the good failure mode; but it is still a failure,
and this library is what removes it. See ``docs/argon-metastable-thermo/`` for the probe output.

WHY A NEW LIBRARY AND NOT AN EXISTING ONE
-----------------------------------------
``PlasmaCationThermo`` is the obvious neighbour and is the wrong home: it is named for cations,
its charter says "free monatomic CATIONS of plasma interest", and its whole electron
reference-state discussion exists because its species carry charge. Nothing here carries charge,
so that discussion would be dead weight around a neutral, and the library name would lie.
``primaryThermoLibrary`` already carries one electronically excited species (``O2(S)``, index 3)
and would technically hold this one too, but it is the database's general-purpose combustion
default: an entry placed there is loaded by every RMG job whether or not it is running a plasma,
and a metastable that quietly appears in a combustion mechanism is exactly the surprise this
campaign spends its effort avoiding. A separate, explicitly-named library is opted into.

The scope is therefore: gas-phase thermochemistry of ELECTRONICALLY EXCITED, ELECTRICALLY NEUTRAL
species that matter in plasmas, each pinned to one named spectroscopic level. Excited ions belong
in ``PlasmaCationThermo``; ground-state neutrals belong in the ordinary libraries.

WHAT THIS FILE FORBIDS
----------------------
Everything here is TRANSCRIBED from a published table or derived from transcribed values by an
exact identity written out in the entry's own ``longDesc``. No value in this file was fitted,
estimated, interpolated, averaged between sources, or computed from a quantum-chemistry
calculation or a group-additivity scheme. An entry that cannot be written that way does not go
in; it goes in a report as an open question.

WHAT THE READER MUST NOT ASSUME
-------------------------------
1. **An adjacency list is not a state.** ``Ar u2 p3 c0`` carries no orbital information at all.
   Argon has three distinct triplet 4s levels that all answer to it, and they are not one
   reservoir. Every entry in this library therefore NAMES the level it represents, in its
   ``shortDesc``, in its label, and in its ``longDesc``, with the alternatives' numbers shown so
   the choice can be overruled from one read. An entry here that did not name its level would not
   be a sourced value; it would be an ambiguity with a number attached.

2. **RMG cannot tell these states apart, and will not stop you conflating them.** There is exactly
   one neutral bond-free ``p3`` argon adjacency list, so a second argon 4s level cannot be added
   to this database as a second species without a structural distinction RMG does not have. If
   some later ticket needs both metastables resolved, that is an engine problem, not a data
   problem, and it must be raised as one.

3. **A species here is constructible, not present.** Nothing in this library puts anything into
   any reactor. The simulation input files in this campaign declare argon as ground state plus
   cation only; this file does not change that and is not meant to. No deck was edited.

4. **No kinetics is added here, but kinetics is UNLOCKED here, and the two are different.** Not
   one reaction, family, training entry or rate ships in this file. But a thermo entry is what
   makes a species real enough for a family to generate on, and measured, one does: loading this
   library lets ``Plasma_Electron_Impact_Ionization`` produce ``Ar(3P2) => Ar+`` on a rank-10
   placeholder rate generalised from lithium. Read "THIS IS NOT AN INERT ISLAND" in the entry's
   longDesc before loading this library for anything but thermochemistry. An earlier draft of
   this file claimed the species was unreachable; that claim was false and the grep that produced
   it could not have established it.
"""

entry(
    index = 0,
    label = "Ar(3P2)",
    molecule =
"""
multiplicity 3
1 Ar u2 p3 c0
""",
    thermo = ThermoData(
        # Free monatomic species pinned to ONE electronic level, so Cp is translation only:
        # Cp(T) = 5/2 R = 20.786 J/(mol*K) at every temperature, exactly. This is the same
        # number NIST-JANAF Ar-001 tabulates for ground-state argon at every one of these
        # temperatures, and it is exact rather than transcribed-and-rounded.
        Tdata = ([298.15, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000,
                  6000], 'K'),
        Cpdata = ([20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786,
                   20.786, 20.786, 20.786, 20.786, 20.786], 'J/(mol*K)'),
        H298 = (1114.247, 'kJ/mol'),
        S298 = (168.227, 'J/(mol*K)'),
        Cp0 = (20.7862, 'J/(mol*K)'),
        CpInf = (20.7862, 'J/(mol*K)'),
        Tmin = (298.15, 'K'),
        Tmax = (6000, 'K'),
        # E0 is deliberately NOT stated. See "E0 IS DERIVED, NOT STATED" in the longDesc:
        # RMG's E0 is not the excitation energy, the two are 5/2*R*298 apart, and stating
        # one gives the file two sources of truth that measurably disagree.
    ),
    shortDesc = u"Ar(4s 3P2), the 1s5 metastable ONLY, NIST ASD level 93143.7600 cm^-1, g = 5",
    longDesc =
u"""
WHICH STATE THIS IS, STATED BEFORE ANYTHING ELSE
    This entry is the single level

        Ar I  3s2.3p5.(2P*<3/2>).4s   2[3/2]*   J = 2   g = 5   E = 93143.7600 cm^-1

    -- Paschen 1s5, LS-label 3P2, the lower and by far the more populous of argon's two 4s
    metastables. It is NOT a lump over the 4s manifold, NOT the 3P0 metastable, and NOT either
    of the two resonant levels. What the alternatives would have cost is tabulated below.

SOURCE
    A. Kramida, Yu. Ralchenko, J. Reader and the NIST ASD Team (2024), NIST Atomic Spectra
    Database (version 5.12), doi:10.18434/T4W30F, National Institute of Standards and
    Technology, Gaithersburg MD. Table: "Ar I" energy levels, retrieved 2026-09-14 from
    ``https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=Ar+I&units=0&format=1``
    (units cm^-1, levels referred to the 3s2.3p6 1S0 ground state at 0.0000 cm^-1). The same
    retrieval gives the ionisation limit, Ar II (3p5 2P*<3/2>), at 127109.842 +/- 0.004 cm^-1.

    Ground-state reference values: NIST-JANAF Thermochemical Tables, Fourth Edition (M. W.
    Chase, Jr., J. Phys. Chem. Ref. Data Monograph 9, 1998), table "Argon (Ar)", identifier
    Ar-001, ``https://janaf.nist.gov/tables/Ar-001.txt``: S(298.15) = 154.845 J/(mol*K),
    Cp = 20.786 J/(mol*K) at every tabulated T, [H(298.15)-H(0)] = 6.197 kJ/mol, dfH = 0
    throughout (argon is an element in its standard state). The database's own ground-state
    argon is ``input/thermo/libraries/primaryThermoLibrary.py``, entry index 15, label ``Ar``
    -- a NASA polynomial with coeffs [2.5, 0, 0, 0, 0, -745.375, 4.37967] on both intervals,
    which evaluates to S(298.15) = 154.846 J/(mol*K) and Cp = 20.786 J/(mol*K), agreeing with
    JANAF Ar-001 to 0.001 J/(mol*K). (Measured, not asserted.)

THE THREE NUMBERS, ONE LINE OF ARITHMETIC EACH
    Cp(T) = 5/2 R = 20.786 J/(mol*K), exact at every T. A free monatomic species pinned to one
        electronic level has translational degrees of freedom and nothing else; there is no
        rotation, no vibration, and -- this is the part specific to a single level -- no
        internal electronic structure to contribute a Schottky term. Contrast the ``[Arp]``
        entry of ``PlasmaCationThermo``, whose Cp peaks at 22.773 J/(mol*K) near 1000 K
        precisely because Ar+ is a 2P term carrying a 2P(1/2) partner 1431.6 cm^-1 up.

    S298 = S298(Ar, JANAF Ar-001) + R*ln(g*/g0) = 154.845 + 8.314462618*ln(5/1)
         = 154.845 + 13.382 = 168.227 J/(mol*K).
        The degeneracy term is EXACT, not an approximation: the translational, pressure and
        mass contributions are identical between Ar(3P2) and Ar (same atom, same mass, same
        standard state), so the whole difference is the electronic term R*ln(g), with g = 2J+1
        = 5 for J = 2 against g = 1 for the 1S0 ground state.

    H298 = E(1s5) * h*c*N_A = 93143.7600 cm^-1 * 11.9626565957 J/(mol*cm^-1)
         = 1114.2468 kJ/mol -> 1114.247 kJ/mol.
        This is a FORMATION enthalpy and the thermal correction cancels inside it:
            dfH(298.15) = dfH(0) + [H(298)-H(0)]_Ar(3P2) - [H(298)-H(0)]_Ar
        with dfH(0) = the level energy (ground-state argon's dfH(0) being zero), and both
        bracketed increments equal to 5/2*R*T -- Ar(3P2) because a single level has no
        internal structure, Ar because JANAF Ar-001's T = 0 row gives exactly -6.197.
        They cancel, so the THERMOCHEMICAL dfH(0) of this species is also 1114.247. Read
        the next section before concluding that this number belongs in the ``E0`` field.

    Cross-check, not a second measurement: 93143.7600 cm^-1 = 11.54835 eV, against the 11.548 eV
    that the plasma literature routinely quotes for the argon 4s metastable.

E0 IS DERIVED, NOT STATED -- AND WHY THE OBVIOUS VALUE IS THE WRONG ONE
    The ``E0`` field is absent from the entry above. That is deliberate, it was got wrong first,
    and the trap is a collision of names worth writing out because it is what makes the wrong
    answer look exact.

    The spectroscopic term value 93143.76 cm^-1 genuinely IS a 0 K quantity, and the
    thermochemical dfH(0) of this species genuinely IS 1114.247 kJ/mol by the cancellation just
    above. So writing ``E0 = (1114.247, 'kJ/mol')`` feels like transcription. It is not, because
    RMG's ``E0`` is a different quantity that happens to be numerically close.

    RMG's ``E0`` is the species' enthalpy at 0 K obtained by integrating THE SPECIES' OWN Cp down
    from the reference temperature -- with no element correction, because RMG's convention drops
    it (it cancels in any balanced reaction, which is all RMG uses E0 for). Measured on this very
    entry (``docs/argon-metastable-thermo/logs/round55_probe.stdout.log``):

        entry.data.E0 as it was stated      1114.2470 kJ/mol
        data.to_wilhoit(B=1000).E0          1108.0527 kJ/mol
        difference                            +6.1943 kJ/mol  = 5/2 * R * 298

    Note the 298, not 298.15: ``ThermoData.to_wilhoit`` calls ``get_enthalpy(298)``
    (``rmgpy/thermo/thermodata.pyx:366-389``), the same 298 K field convention documented under
    "WHERE THIS RECIPE BREAKS" below. 5/2*R*298.15 would be 6.1974.

    Two further facts settle it:

    * ``to_wilhoit`` reads ``Tdata``/``Cpdata``/``H298``/``S298`` and NEVER consults ``self.E0``,
      and ``thermoengine.process_thermo_data`` then sets ``spc.conformer.E0 = wilhoit.E0``
      (``rmgpy/thermo/thermoengine.py:75-78``). So a stated ``E0`` is INERT on the path the
      runtime actually uses and visible only to code that reads the field directly. Measured
      end to end: after ``process_thermo_data``, both ``NASA.E0`` and ``spc.conformer.E0`` are
      1108.0527.
    * Stating it therefore gives one species two zero-point energies that disagree by 6.19
      kJ/mol depending on which API reaches it. Deriving it gives one.

    The alternative -- state ``E0 = 1108.053`` to match -- was considered and rejected: it is a
    number with no source, obtained by subtracting a thermal correction from a transcribed value
    purely to satisfy a field, and it would drift silently the moment ``Tdata``, ``Cpdata`` or
    ``H298`` changed. Leaving the field empty makes the derivation the single source of truth and
    costs nothing, because the derivation is exactly what the runtime does anyway.

    The same collision exists, unfixed, in ``PlasmaCationThermo``: measured, ``[Arp]`` states
    E0 = 1520.5730 while ``to_wilhoit`` derives 1514.3867, a gap of 6.1863 kJ/mol. That library
    is out of this ticket's scope and is reported, not edited.

WHY THIS FORM AND NOT NASA
    ``ThermoData``, matching ``PlasmaCationThermo``, not the ``NASA`` form that ground-state
    argon uses in ``primaryThermoLibrary``. ``ThermoData`` states Cp on a temperature grid and
    H298/S298 at the reference temperature -- which is exactly the shape of what is known here:
    three transcribed-or-derived constants and a Cp that is constant. Emitting a NASA polynomial
    would mean choosing coefficients, i.e. fitting, for a function that has a closed form; the
    charter of this file forbids that even when the fit would be exact. Anything downstream that
    wants a polynomial can convert, and the conversion is then visibly downstream of the data.

THE ALTERNATIVES, SO THIS CHOICE CAN BE OVERRULED FROM ONE READ
    All four 3p5.4s levels, NIST ASD ver. 5.12, with what an entry built on each would carry:

      Paschen  LS    config / term / J                E (cm^-1)   g   H298      S298
      1s5      3P2   (2P*<3/2>).4s  2[3/2]*  J=2     93143.7600   5   1114.247  168.227  <- THIS
      1s4      3P1   (2P*<3/2>).4s  2[3/2]*  J=1     93750.5978   3   1121.506  163.979
      1s3      3P0   (2P*<1/2>).4s  2[1/2]*  J=0     94553.6652   1   1131.113  154.845
      1s2      1P1   (2P*<1/2>).4s  2[1/2]*  J=1     95399.8276   3   1141.235  163.979
      {1s5+1s3} degeneracy-weighted lump at 298.15 K     -    5.0011  1114.251  168.241

    (H298 in kJ/mol, S298 in J/(mol*K); every row computed by the two identities above.)

QUESTION 1 -- WHICH LEVELS BELONG IN THE ENTRY AT ALL: THE 1s4 / 1s2 EXCLUSION
    1s2 (1P1) is not an option this entry declines; it is UNREPRESENTABLE. Argon has eight
    valence electrons; with ``p3`` (six of them paired in lone pairs), no bonds and no charge,
    the remaining two must be unpaired, so ``Ar u2 p3 c0`` is the only neutral bond-free p3
    adjacency list and it is necessarily a TRIPLET (multiplicity 3). A singlet 4s level has no
    adjacency list in RMG at all.

    1s4 (3P1) IS representable by the same adjacency list and is excluded on physics. It is a
    RESONANT level: J = 1 to J = 0 is electric-dipole allowed, and NIST ASD gives the 106.6660 nm
    line at A = 1.320e+08 s^-1, a natural lifetime of 7.6 ns. (1s2 radiates at 104.8220 nm with
    A = 5.32e+08 s^-1, 1.9 ns.) Against that:

        1s5 (3P2)   tau = 38 (+8/-5) s   MEASURED, H. Katori and F. Shimizu, Phys. Rev. Lett.
                                         70 (1993) 3545-3548, doi:10.1103/PhysRevLett.70.3545
        1s5 (3P2)   tau = 55.9 s         computed, N. E. Small-Warren and L.-Y. Chow Chiu,
                                         Phys. Rev. A 11 (1975) 1777, doi:10.1103/PhysRevA.11.1777
        1s3 (3P0)   tau = 44.9 s         computed, same paper

    Nine to ten orders of magnitude. 1s5 and 1s3 are reservoirs on any chemical timescale; 1s4
    and 1s2 are not reservoirs at all, they are radiative transients. Note the caveat that goes
    with that: in a real discharge the 106.7 and 104.8 nm photons are RADIATION-TRAPPED, and the
    effective lifetimes of 1s4/1s2 rise by orders of magnitude at high argon density. Trapping is
    a transport property of the vessel, not of the atom -- it depends on pressure, geometry and
    line shape -- so it can never be a property of a thermochemistry entry. If some later work
    needs a radiation-trapped resonant level, it needs its own species and its own justification,
    and it cannot reuse this adjacency list, because this one is taken.

QUESTION 2 -- HOW THE ADMITTED LEVELS ARE WEIGHTED: WHY 1s5 ALONE AND NOT {1s5 + 1s3}
    This is a separate question from Question 1 and is answered separately.

    The arithmetic first, measured (``docs/argon-metastable-thermo/check_levels.py``):
    dE(1s3 - 1s5) = 1409.9052 cm^-1 = 0.174806 eV = 16.8662 kJ/mol, against RT = 2.478957 kJ/mol
    at 298.15 K, so exp(-dE/RT) = 1.1096e-03 and the degeneracy-weighted partition sum is
    5 + 1*0.0011096 = 5.001110 against 5 for 1s5 alone.

    The entropy difference this implies is NOT R*ln(5.0011/5) = 0.00185 J/(mol*K). That is only
    the first of two terms: the electronic entropy of a manifold is
    S_el = R*ln(Q) + R*<E>/(RT), and the second term dominates here because the level is high
    and thinly populated. The true difference is

        298.15 K :  0.0144 J/(mol*K)      (R*ln term 0.0018, <E>/RT term 0.0126)
        6000   K :  1.4594 J/(mol*K)      (R*ln term 1.1086, <E>/RT term 0.3509)

    so a reader who uses R*ln(Q) alone is low by 7.8x at the reference temperature. Against the
    0.001 J/(mol*K) precision at which S298 is written here, the lumping choice therefore is NOT
    numerically moot at 298.15 K -- it is 14 last-digits, and it falls below one last-digit only
    under about 207 K. It crosses 0.01 at 281 K, 0.1 at 449 K and 1.0 at 1561 K. The lumped
    entry's H298 would differ by +0.0037 kJ/mol and it would carry a Schottky Cp rising to
    0.854 J/(mol*K) near 1000 K instead of a flat 5/2 R.

    None of that is why the lump is rejected, and it is worth being clear that the magnitudes
    argue mildly FOR lumping being harmless at 298.15 K.

    The lump is NOT rejected for being a fitted number, and an earlier draft of this file said so
    and was wrong. A degeneracy-weighted Boltzmann state sum is ANALYTICAL, not fitted: it has a
    closed form, no adjustable parameter, and nothing in this file's charter forbids it. It is
    rejected for a different and narrower reason -- it is CONDITIONAL, and its condition does not
    hold where this species is used. The lump is exact given that the two metastables are
    equilibrated with each other at the gas temperature. In a low-pressure discharge they are
    not: their populations are set by electron-impact excitation and by their own very different
    quenching, so the 1s5/1s3 ratio is an OUTPUT of the plasma kinetics rather than a function of
    T. Writing the lump would silently carry an antecedent the model exists to test. A single
    named level carries no antecedent at all: a transcribed energy, an exact degeneracy, an exact
    translational Cp.

    That distinction matters practically, not just verbally. "Fitted" would mean the lump may
    never be used here. "Conditional" means it may be used exactly when its condition holds --
    a thermal or near-LTE argon plasma, an afterglow late enough to have equilibrated, any
    situation where the 4s manifold is collisionally mixed. The table below is what such a reader
    needs, and the answer visibly depends on their temperature.

WHAT LUMPING WOULD COST, IF SOMEONE'S CONDITIONS JUSTIFY IT
    Shifts RELATIVE to this entry (1s5 alone), computed by the two-term expression above over
    NIST ASD level energies and degeneracies. "2-level" = {1s5, 1s3}, the two metastables;
    "4-level" = the whole 3p5.4s manifold, the two metastables plus the two resonant levels.
    Measured, ``docs/argon-metastable-thermo/round55_probe.py``:

        T (K)  |  dS 2-lvl   dH 2-lvl  |  dS 4-lvl   dH 4-lvl  |  n(4s)/n(1s5)
        -------+------------------------+------------------------+--------------
         298.15|    0.0144     0.0037  |    1.0345     0.2296  |     1.032
         500   |    0.1450     0.0582  |    2.3801     0.7598  |     1.109
        1000   |    0.6482     0.4323  |    4.4082     2.2251  |     1.300
        2000   |    1.1525     1.1406  |    6.0872     4.5819  |     1.579
        3000   |    1.3244     1.5571  |    6.6580     5.9647  |     1.754
        4000   |    1.3988     1.8131  |    6.9032     6.8078  |     1.869
        5000   |    1.4372     1.9838  |    7.0284     7.3649  |     1.951
        6000   |    1.4594     2.1053  |    7.1004     7.7578  |     2.011

    dS in J/(mol*K), dH in kJ/mol. The last column is the equilibrium population of the WHOLE 4s
    manifold relative to 1s5 alone, sum(g exp(-E/RT)) / 5 -- so 2.011 at 6000 K means the manifold
    holds twice what 1s5 does, i.e. the other three levels together have caught up with it.

    Read it this way. At the reference temperature this entry IS the 4s manifold to within
    1 J/(mol*K) and 0.23 kJ/mol, and the two-metastable question is worth 0.0144 J/(mol*K). The
    gap opens exactly where a discharge lives: by 2000 K the four-level lump differs by 6.1
    J/(mol*K) and 4.6 kJ/mol, which is no longer a rounding question. So this entry is the right
    object for a species-resolved kinetic model -- the case it was written for, where 1s5 is
    tracked separately because it has its own production and loss -- and is NOT the right object
    for a reader who wants one lumped "Ar*" pseudo-species at several thousand kelvin. That reader
    should build the manifold sum for their own conditions using the level table above, and should
    be aware that the two resonant levels they would then be lumping in are radiatively coupled to
    the ground state (see Question 1), so whether they belong in a reservoir at all depends on the
    vessel's radiation trapping and not on this table.

    The physical case for 1s5 in particular, had the two been equally defensible: it is the lower
    level, it carries g = 5 against g = 1, and it therefore holds roughly 5/6 of the metastable
    population even under the equilibrium assumption that is being declined.

WHERE THIS RECIPE BREAKS IF IT IS REUSED CARELESSLY
    The recipe here -- "H298 from the level energy, S298 from the ground state plus R*ln(g),
    Cp from the ground state" -- is the one ``primaryThermoLibrary``'s ``O2(S)`` entry (index 3)
    uses, and it stands on much firmer ground for argon than it did for O2, because for a free
    monatomic species the borrowed Cp is not borrowed at all: 5/2 R is exact, at every T. The
    ``O2(S)`` entry genuinely approximates, taking singlet oxygen's Cp and S from the triplet,
    which is right for translation and rotation and wrong in detail for vibration. Three ways
    this can go wrong for somebody else:

    1. **Any polyatomic.** The moment the excited species has vibrations, the excited state's
       frequencies differ from the ground state's and the borrowed Cp becomes an approximation
       that must be labelled as one. Do not copy the "Cp is exact" sentence out of this entry.
    2. **Any level that is not a single level.** If the structure you are entering answers to a
       whole term or manifold rather than one J, the Cp acquires a Schottky contribution and the
       entropy acquires the R*<E>/RT term shown above. The flat Cp here is a consequence of
       "one level", not of "monatomic".
    3. **Any charged species.** Then the electron reference-state convention matters, and the
       number must be reconciled the way ``PlasmaCationThermo``'s entries are. It does not arise
       here because this species is neutral: no electron is created or destroyed relative to
       ground-state argon, so no convention enters and none of that arithmetic applies.

    A fourth, specific to this database rather than to the recipe: the ground-state Ar that a
    running mechanism actually resolves to is NOT the JANAF-anchored value used above, and is not
    ``primaryThermoLibrary``'s either. Measured with the full library set loaded,
    ``get_thermo_data`` on ``Ar u0 p4 c0`` returns S(298.15) = 154.7348 J/(mol*K) from
    ``BurkeH2O2``, which wins the lookup; that entry is a 4-figure combustion value, 36.98
    cal/(mol*K), sitting 0.110 J/(mol*K) below JANAF's 154.845. So a mechanism that differences
    this entry against its own ground-state argon sees, measured end to end,

        dH298(Ar -> Ar(3P2)) = 1114.2470 kJ/mol      against 1114.2468 exact   (agrees)
        dS298(Ar -> Ar(3P2)) =   13.5027 J/(mol*K)   against   13.3816 exact   (+0.1211)

    i.e. the enthalpy of excitation comes out right to 0.0002 kJ/mol while the entropy carries
    +0.121 J/(mol*K), worth -0.036 kJ/mol in dG at 298.15 K. Anchoring this entry on BurkeH2O2
    instead would make that difference exact and this entry's own absolute S298 wrong by the same
    amount; the sourced table wins, and the artefact is disclosed here rather than hidden.
    Re-anchoring BurkeH2O2 is a different ticket and was deliberately not attempted.

    A fifth, database-wide rather than specific to argon, recorded because it is invisible until
    measured: RMG's ``ThermoData.H298`` and ``ThermoData.S298`` fields are referenced to **298 K,
    not 298.15 K** (``rmgpy/thermo/thermodata.pyx``, properties ``H298``/``S298`` and the
    ``assert Tdata[0] >= 298`` corrections beneath them). Every JANAF-sourced entry in this
    database -- these, and ``PlasmaCationThermo``'s -- writes the 298.15 K value into that field,
    so ``get_entropy(298.15)`` returns the written value plus Cp*ln(298.15/298) = +0.0105
    J/(mol*K) here, and ``get_enthalpy(298.15)`` returns it plus Cp*0.15 = +0.0031 kJ/mol. That
    is why this entry's S298 reads 168.227 in the file and 168.2375 through the API. The offset is
    the same for any species with the same Cp, so it cancels exactly in the Ar -> Ar(3P2)
    difference above. It is NOT corrected for here: writing 168.216 to make the API return 168.227
    would break the identity this entry is built on and would differ from every sibling entry.

VALIDITY RANGE -- AND THE RANGE YOU WILL ACTUALLY GET, WHICH IS NOT THE SAME
    ``Tmin``/``Tmax`` are 298.15 K and 6000 K, matching ``PlasmaCationThermo`` and JANAF Ar-001's
    own ceiling. That is a statement about the DATA: 5/2 R and R*ln 5 do not expire, and the
    tabulated Cp is exact at every point on the grid.

    **Standard RMG processing will not give you 6000 K.** Measured
    (``docs/argon-metastable-thermo/logs/reachability_probe.stdout.log``):

        process_thermo_data(spc, <this entry>, NASA)  ->  NASA, Tmin = 100.0 K, Tmax = 5000.0 K
        NASA at  298.15 K:  Cp = 20.7862  S = 168.2375  H = 1114.2501
        NASA at 5000.00 K:  Cp = 20.7862  S = 226.8462  H = 1211.9837
        NASA at 6000.00 K:  RAISED ValueError: No valid NASA polynomial at temperature 6000 K.

    The cause is one branch in ``rmgpy/thermo/thermoengine.py:86-99``: a library entry that is
    ALREADY a ``NASA`` is kept verbatim, and anything else is refit with a hard-coded
    ``to_nasa(Tmin=100.0, Tmax=5000.0, Tint=1000.0)``. This entry is a ``ThermoData`` -- chosen on
    charter grounds, see "WHY THIS FORM AND NOT NASA" -- so it is refit, and the declared ceiling
    is discarded on the way. That is an engine limit, not a defect in these numbers, but this file
    is what advertises 6000 K so this file has to say it.

    Two consequences worth having explicitly:

    * The charter-driven form choice has a behavioural price that was not visible when it was
      made. Emitting NASA would preserve 6000 K; it would also mean fitting coefficients, which
      the charter forbids. The form choice stands -- a truthful 5000 K beats a fitted 6000 K --
      but the price is now on the record rather than discovered later by someone whose reactor
      stopped at 5000 K.
    * Ground-state argon loses its range the same way, for a different reason. Its
      ``primaryThermoLibrary`` entry IS a NASA valid to 6000 K and would be kept verbatim -- but
      that entry does not win the lookup; ``BurkeH2O2``'s ``ThermoData`` does (see "WHERE THIS
      RECIPE BREAKS", point four), and gets refit to 5000 K like this one. Measured.

    **Above the tabulated grid, the raw functions go wrong silently.** ``ThermoData`` extrapolates
    Cp and H but FREEZES S at its last tabulated point:

        T (K)      Cp        S (this entry)   S (exact)     H (this entry)   H (exact)
        6000    20.7860        230.6353       230.6358        1232.7688      1232.7697
        8000    20.7860        230.6353       236.6156        1274.3408      1274.3420
       10000    20.7860        230.6353       241.2539        1315.9128      1315.9143

    So at and below 6000 K the entry is right; above it, enthalpy keeps climbing correctly while
    entropy stops, and any free energy built from the pair is wrong and gets worse with T.
    ``is_temperature_valid`` returns ``False`` at 8000 K and correctly ``True`` at 6000 -- the
    guard exists and is accurate; nothing in the accessor path calls it. Reported as an RMG-Py
    referral, not worked around here: a data file cannot make an accessor raise.

    Finally, and separately from all of the above: the IDENTIFICATION of "metastable argon" with
    the 1s5 level alone weakens as temperature rises, because the rest of the 4s manifold catches
    up (see the lumping table -- by 6000 K it holds twice what 1s5 does) and the 4p manifold sits
    only ~10000 cm^-1 higher and begins to populate. Those are different species, not this one, so
    nothing here becomes wrong; it becomes incomplete. All of this is a GAS temperature range and
    says nothing about the electron temperature.

HOW MANY ELECTRONIC STATES DOES THIS SPECIES HAVE? RMG GIVES THREE DIFFERENT ANSWERS
    Measured on one and the same ``Species`` built from the adjacency list below:

        this entry's S298, via R*ln(g) with g = 2J+1 = 5           g = 5
        conformer after thermoengine.process_thermo_data           spin_multiplicity = 1
        conformer after Species.generate_statmech()                spin_multiplicity = 3
        the molecule itself                                        multiplicity = 3

    The three disagree because they are counting different things. ``g = 5`` is the TOTAL
    electronic degeneracy 2J+1 of the ``3P2`` level, which is what thermochemistry needs. RMG's
    ``spin_multiplicity`` is 2S+1 and knows only about unpaired electrons, so it says 3 and has
    no way to express the orbital part; a freshly constructed ``Conformer`` says 1 because nothing
    has told it otherwise. The spread is R*ln(5/3) = 4.2472 J/(mol*K) against statmech and
    R*ln 5 = 13.3816 against the untouched conformer.

    **Is it fixable from the database side? No.** An RMG adjacency list carries u, p and c; it has
    no J, and there is no library field that sets a conformer's electronic degeneracy. The entry's
    S298 is correct as a thermochemical quantity, and any code path that rebuilds a partition
    function from the conformer instead of reading S298 -- pressure-dependent networks are the
    obvious one -- will disagree with it by the amounts above. The repair is an engine concept
    (electronic degeneracy decoupled from spin multiplicity), not a data change, and is reported
    as such. Until then: **use this entry's S298; do not let statmech regenerate it.**

STRUCTURE
    ``1 Ar u2 p3 c0``, multiplicity 3: three lone pairs, two unpaired electrons, no bonds, net
    charge 0. Measured on the engine, this perceives as atom type ``Ar0e`` and is isomorphic to
    neither ground-state argon nor Ar+. Two warnings that go with it:

    * ``Ar0e`` in a GROUP adjacency list does not mean "metastable". Atom-type perception ignores
      ``u`` entirely, so ``1 Ar0e ux p3 c0`` matches u1 argon as readily as the u2 metastable. A
      group that means this species must write ``u2`` explicitly. (RMG-Py's own atomtype.py says
      so at length; repeated here because a kinetics author reading this entry is exactly the
      person who will get it wrong.)
    * The SMILES round trip is not safe for monatomic species in this database -- documented for
      ``[Arp]``/``[Hep]``/``[Nep]`` in ``PlasmaCationThermo``, where ``from_smiles`` returns a
      doubled charge. The adjacency list above is the only interchange form to use.

THIS IS NOT AN INERT ISLAND. READ THIS BEFORE LOADING THE LIBRARY
    An earlier draft of this file said metastable argon was unreachable -- that no channel could
    produce or destroy it, so loading this library added an isolated number and nothing else.
    **That was false, and the way it was established was invalid.** The claim rested on grepping
    the kinetics files for the literal string ``Ar u2 p3 c0``. Families do not match literals,
    they match GROUPS, so a literal search can never establish that no family matches a species.
    Absence of a string is not absence of a channel. The only way to settle it is to generate
    reactions and look at what comes back, which is now done
    (``docs/argon-metastable-thermo/reachability_probe.py``).

    MEASURED. Of the six plasma families in this database, five generate nothing from this
    species and one does:

        Plasma_Electron_Impact_Ionization  ->  [Ar] => [Ar+]
            template A_rad, degeneracy 1.0, electrons +1, irreversible
            products: multiplicity 2 | 1 Ar u1 p3 c+1
        Plasma_Electron_Attachment                       ->  0
        Plasma_Radiative_Recombination                   ->  0
        Plasma_Associative_Ionization_Alkali_Alkali      ->  0
        Plasma_Associative_Ionization_Alkali_Alkaline    ->  0
        Plasma_Associative_Ionization_Alkaline_Alkaline  ->  0

    So loading this library alongside that family activates a STEPWISE IONISATION channel for
    argon: Ar(3P2) + e- -> Ar+ + 2 e-, which is exactly the process that makes metastables matter
    in a discharge. That is chemistry appearing, not a number sitting still.

    WHAT RATE THAT CHANNEL GETS, AND WHERE IT COMES FROM. The family has one rate rule, on node
    ``A_rad``, rank 10, A = 1.292979e+08 m^3/(mol*s). Its own shortDesc calls it an ESTIMATE and
    its longDesc is explicit and honest about what it is: a ONE-POINT GENERALIZATION of the
    sourced Voronov electron-impact ionisation rate for LITHIUM, evaluated once at Te = 1 eV and
    frozen as a temperature-independent Arrhenius, handed flat to every radical the template
    matches. It is a placeholder, not a prediction, and it says so. Adding this library therefore
    does not merely add a sourced number to the database -- it gives argon a stepwise-ionisation
    rate derived from lithium.

    AND IT FALSIFIES THAT RULE'S OWN STATED PREMISE. The ``A_rad`` longDesc argues its choice of
    anchor partly like this:

        "this family CANNOT generate argon at all (closed-shell Ar has u0, outside the
         template's u[1,2,3,4]; generate_reactions([Ar]) returns 0 reactions)"

    That was true when it was written, because ground-state argon was the only argon in the
    database. It is FALSE as of this file: Ar(3P2) has u2, squarely inside ``u[1,2,3,4]``, and the
    family generates it. The rule's validity paragraph then warns that the estimate "is NOT
    defensible for high-threshold species: a noble gas (Ar 15.76 eV, He 24.6 eV) ionises orders of
    magnitude more slowly at 1 eV than lithium (5.4 eV) does, so on those this rule OVER-predicts
    badly", and brackets the spread as Li 1.29e8 against Ar 1.25e3 m^3/(mol*s), five orders apart.

    ONE ARITHMETIC CORRECTION IN THE RULE'S FAVOUR, WHICH IS THE INTERESTING PART. That warning
    is about GROUND-STATE argon. It does not transfer to this species, because ionising an already
    excited atom costs only what is left:

        Ar II limit                    127109.842 cm^-1
        minus the 1s5 level             93143.7600 cm^-1
        = threshold from Ar(3P2)        33966.082 cm^-1 = 4.2113 eV

    4.21 eV is BELOW lithium's 5.4 eV. By the rule's own criterion -- "defensible as an
    order-of-magnitude estimate for LOW-THRESHOLD light atoms near the 1 eV working point" --
    Ar(3P2) is a better fit for that placeholder than the ground-state argon the rule was
    re-anchored away from. The five-orders-of-magnitude over-prediction the rule warns about is a
    ground-state hazard, not a metastable one. That is lucky rather than designed, and it is not a
    reason to leave the rule's premise sentence standing: the sentence is now factually wrong, and
    the next species someone adds may not be lucky.

    NONE OF THAT IS TOUCHED HERE. Changing the family, its template, its rules or that longDesc is
    a different ticket and a different piece of chemistry, and it needs the owner before anyone
    starts. This file's obligation is to say what a user gets, and the above is what a user gets.
    ``test/test_argon_metastable_thermo.py`` pins the reaction count, the template and the rule's
    rank, so the day any of them moves, something fails loudly instead of drifting.

STILL NOT IN ANY DECK, AND STILL WITHOUT PRODUCTION OR LOSS CHEMISTRY
    Everything above is about what a family GENERATES on demand. Nothing in this library puts
    anything into a reactor. Separately, the channels that would make this species physical are
    still absent: metastables are PRODUCED by electron-impact excitation and destroyed by two- and
    three-body quenching and wall loss, and none of those has an entry anywhere in this database.
    So the picture after this file is a species with one generated loss channel carrying a
    lithium-derived placeholder rate, no production channel at all, and no appearance in any deck
    -- which is worse than an island in one specific way: an island is visibly incomplete, whereas
    a species with loss and no production will quietly go to zero.
    ``input/kinetics/libraries/PlasmaAir`` advertises "metastable quenching" in its own longDesc
    but its dictionary carries only ``Ar`` and ``Arp`` -- no metastable species and no metastable
    reaction. The simulation inputs in this campaign declare argon as ground state plus cation
    only and were not edited.
""",
)
