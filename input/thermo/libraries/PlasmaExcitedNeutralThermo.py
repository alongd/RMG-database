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

4. **No kinetics is authorised by anything here.** These are thermochemical values. Not one
   reaction, family, training entry or rate accompanies them. In particular, metastable argon
   having thermochemistry does NOT mean this database can produce it: no channel populates it and
   no channel destroys it. Until kinetics exists, a mechanism containing this species would hold
   an inert, unreachable island.
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
        E0 = (1114.247, 'kJ/mol'),
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
        ``E0`` carries the SAME number, and that is an identity rather than an oversight:
            dfH(298.15) = dfH(0) + [H(298)-H(0)]_Ar(3P2) - [H(298)-H(0)]_Ar
        with dfH(0) = the level energy (ground-state argon's dfH(0) being zero), and both
        bracketed increments equal to 5/2*R*T = 6.197 kJ/mol -- Ar(3P2) because a single level
        has no internal structure, Ar because JANAF Ar-001's T = 0 row gives exactly -6.197.
        They cancel, so dfH(298.15) = dfH(0) = 1114.247 kJ/mol. For Ar+ the same two increments
        do NOT cancel (6.206 against 6.197), which is why that entry's H298 and E0 differ by
        0.008 kJ/mol and this one's do not.

    Cross-check, not a second measurement: 93143.7600 cm^-1 = 11.54835 eV, against the 11.548 eV
    that the plasma literature routinely quotes for the argon 4s metastable.

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
    argue mildly FOR lumping being harmless. The lump is rejected because it would be a FITTED
    number under a charter that forbids fitted numbers. A degeneracy-weighted lump assumes the
    two metastables are Boltzmann-distributed with respect to one another at the GAS temperature.
    In a low-pressure discharge they are not: their populations are set by electron-impact
    excitation and by their own very different quenching, and the 1s5/1s3 ratio is an OUTPUT of
    the plasma kinetics, not a function of T. Writing the Boltzmann lump would be quietly
    asserting an equilibrium the model exists to test. A single named level asserts nothing: it
    is a transcribed energy, an exact degeneracy and an exact translational Cp.

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

VALIDITY RANGE
    ``Tmin``/``Tmax`` are 298.15 K and 6000 K, matching ``PlasmaCationThermo`` and JANAF Ar-001's
    own ceiling. The functions themselves have no upper bound -- 5/2 R and R*ln 5 do not expire --
    but the IDENTIFICATION of "metastable argon" with the 1s5 level alone weakens as temperature
    rises, because the 4p manifold sits only ~10000 cm^-1 higher and begins to populate. Those are
    different species, not this one, so nothing here becomes wrong; it becomes incomplete. This is
    a GAS temperature range and says nothing about the electron temperature.

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

NOT A CHANNEL, AND NOT IN ANY DECK
    This entry supplies thermochemistry only and authorises no reaction. Argon metastables are
    produced by electron-impact excitation and destroyed by stepwise ionisation, two- and
    three-body quenching, and wall loss; NONE of those has an entry anywhere in this database,
    and none was added with this file. ``input/kinetics/libraries/PlasmaAir`` advertises
    "metastable quenching" in its own longDesc but its dictionary carries only ``Ar`` and
    ``Arp`` -- no metastable species and no metastable reaction. The simulation inputs in this
    campaign declare argon as ground state plus cation only and were not edited. After this file,
    metastable argon CAN exist; it still appears nowhere.
""",
)
