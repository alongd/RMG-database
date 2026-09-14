#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaCationThermo"
shortDesc = u"Sourced gas-phase thermochemistry for free monatomic cations of plasma interest"
longDesc = u"""
WHY THIS LIBRARY EXISTS
-----------------------
``input/kinetics/voronov.yaml`` can ionise 13 elements and
``input/kinetics/libraries/PlasmaElectronImpactIonization`` carries exactly one of them,
because - in that library's own words - "adding He+, N+, O+, Si+ or Ar+ needs
monatomic-cation thermochemistry that does not exist yet; that is a thermo ticket". Before
this file, the only free monatomic cations with thermochemistry anywhere in this database
were ``[Lip]`` (LithiumPrimaryThermo), ``Li_ion`` (computationalLithiumElectrode) and
``proton`` (electrocatThermo / electrocatLiThermo) - and the last two are electrochemical
reference species whose enthalpy is zero by construction, not gas-phase values. This
library is that thermo ticket, opened for argon.

Everything here is TRANSCRIBED from a published table. No value in this file was fitted,
estimated, interpolated, averaged between sources, or computed from a quantum-chemistry
calculation or a group-additivity scheme.

THE ELECTRON REFERENCE-STATE CONVENTION, WHICH IS THE EASY THING TO GET WRONG
-----------------------------------------------------------------------------
An ion's enthalpy of formation is meaningless without saying how the electron is priced.
Two conventions are in use, and their names are routinely swapped; the authority is

    J. E. Bartmess, "Thermodynamics of the Electron and the Proton",
    J. Phys. Chem. 98 (1994) 6420-6424, doi:10.1021/j100076a029,
    definitions at p. 6420 col. 2 - p. 6421 col. 1.

  * "electron convention" (EC). Delta-f H(e-) = 0 at all T, and the electron is
    "taken as just another chemical species": H(T) - H(0) = 5/2 R T = 6.197 kJ/mol at
    298.15 K, S(298.15) = 20.979 J/(mol*K). Bartmess names JANAF and NIST as EC users.
  * "ion convention" (IC). Delta-f H(e-) = 0 at all T AND H(T) - H(0) = 0 at all T, with
    S(T) = 0 as well. Used by the Gaseous Ion Energetics compilations and the GIANT
    tables. The two differ by 6.197 kJ/mol per electron at 298.15 K.

THIS DATABASE AND THIS RUNTIME USE THE ION CONVENTION. Determined, not assumed:

  * every ``electron`` entry in this database - electrocatThermo, electrocatLiThermo,
    computationalLithiumElectrode - is a NASA polynomial with all seven coefficients
    identically zero, i.e. H = S = Cp = 0 at every T. Those are the only electron
    thermochemistry this database has, and the plasma deck in
    ``RMG-Py .../docs/i123-integration/input.py`` loads ``electrocatThermo`` for exactly
    that entry.
  * ``Reaction._get_free_energy_of_charge_transfer_reaction`` sums free energies over the
    explicit species and adds an electrochemical term only when ``potential != 0``; every
    reactor calls it at ``potential = 0``. So the electron contributes zero free energy.

The value below is therefore the IC value. NIST-JANAF publishes the EC value; the single
line of convention reconciliation is shown in the entry's own longDesc, and it is the only
arithmetic applied to any number in this file.

THE OTHER NOBLE-GAS CATIONS IN THIS LIBRARY
-------------------------------------------
This library was opened for argon and now also carries the two lighter noble-gas cations
``[Hep]`` = He+ (NIST-JANAF He-002) and ``[Nep]`` = Ne+ (NIST-JANAF Ne-002), entered to the
same standard, under the same ion convention, each with its own two-route reconciliation and
an ionisation-energy cross-check to NIST ASD in its longDesc. They are the same class of
free monatomic noble-gas cation as Ar+, and each closes the same eager-thermo wall for its
element: without an entry, ``get_thermo_data`` on a bare He+/Ne+ atom raises a loud
``DatabaseError`` ("Unable to determine thermo parameters for atom He+/Ne+"), because group
additivity has no group for a charged noble-gas atom. The one physics difference worth
naming: He+ is hydrogen-like (2S, no fine structure), so its Cp is a flat 5/2 R at all T,
whereas Ne+ and Ar+ are 2P and carry a Schottky bump (peaking near 500 K for Ne+, 1000 K for
Ar+).

WHAT IS NOT HERE
----------------
The helium DICATION ``[Hep2]`` = He(2+) (monatomic, +2; adjacency ``1 He u0 p0 c+2``) is
absent for the same reason as the argon dication below: NIST-JANAF has no table above He-002
(``https://janaf.nist.gov/tables/He-003.txt`` returns HTTP 404), so there is no tabulated
Cp(T) and S(T) to transcribe, and entering one would mean authoring it. Its 0 K enthalpy of
formation would be the sum of the first two ionisation energies of helium (24.587 + 54.418 =
79.005 eV = 7623 kJ/mol), but a single check value is not a source for the thermal functions.
As with Ar(2+), RMG builds it and then fails loudly (no group-additivity data), so there is
nothing to silently poison -- but there is also nothing to attach an entry to. Not entered.


Two argon cations that are NOT this species are deliberately absent, for two different
reasons. They are easy to confuse because plain ASCII writes both "Ar2+", so this section
spells them apart and uses the unambiguous forms throughout: ``Ar2(+)`` is the argon DIMER
cation (diatomic, net charge +1); ``Ar(2+)`` is the argon DICATION (monatomic, net charge
+2).

``Ar2(+)`` -- the argon dimer cation (diatomic, +1). Tabulated thermodynamic functions for
it do exist - Maltsev, Morozov & Osina, "Thermodynamic Properties of Ar2+ and Ar2 Argon
Dimers", High Temperature 57 (2019) 37-40, doi:10.1134/S0018151X19010176, covering
298.15-10000 K and folded into IVTANTHERMO - but that paper is closed access with no
open-access copy, and ATcT's argon-dimer-cation page returns HTTP 403 from here. Without
the tabulated Cp(T) and S(298) there is no way to enter it that is not authoring, so it is
not entered. See ``docs/i127-argon-cation-thermo.md``.

``Ar(2+)`` and higher stages -- the argon dication (monatomic, +2), ``Ar(3+)``, ... are
absent for a different reason, and it is NOT that RMG cannot build them. RMG constructs the
dication without complaint: the adjacency list ``1 Ar u2 p2 c+2`` (ground-state 3P) parses
and carries net charge +2, because argon's atom type is charge-unconstrained - the same
reason ``Ar(+)`` itself builds. What is missing is sourced thermochemistry: NIST-JANAF has
no table above Ar-002 (Ar+), and a thermo query for the dication does NOT silently
fabricate a group-additivity number - it raises a loud ``DatabaseError`` ("no data ... for
atom Ar++"), because group additivity has no group for a charge-+2 argon atom. So the
dication builds, fails loudly, and has nothing to attach an entry to. (Both this loud
failure and the ``Ar(+)`` values above were re-verified on the i172-balance runtime under
I-179 fork C; see ``docs/i127-argon-cation-thermo.md``.)
"""

entry(
    index = 0,
    label = "[Arp]",
    molecule =
"""
multiplicity 2
1 Ar u1 p3 c+1
""",
    thermo = ThermoData(
        # NIST-JANAF Fourth Edition table Ar-002, "Argon, Ion (Ar+)", Ar1+(g), verbatim.
        Tdata = ([298.15, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000,
                  6000], 'K'),
        Cpdata = ([20.984, 20.990, 21.422, 21.915, 22.318, 22.734, 22.773, 22.350, 21.919,
                   21.415, 21.176, 21.050, 20.975], 'J/(mol*K)'),
        H298 = (1520.581, 'kJ/mol'),
        S298 = (166.404, 'J/(mol*K)'),
        Cp0 = (20.7862, 'J/(mol*K)'),
        CpInf = (20.7862, 'J/(mol*K)'),
        Tmin = (298.15, 'K'),
        Tmax = (6000, 'K'),
        E0 = (1520.573, 'kJ/mol'),
    ),
    shortDesc = u"Ar+ (2P) free monatomic cation, NIST-JANAF table Ar-002, ion convention",
    longDesc =
u"""
SOURCE
    M. W. Chase, Jr., NIST-JANAF Thermochemical Tables, Fourth Edition, J. Phys. Chem.
    Ref. Data Monograph 9 (1998), pp. 1-1951; table "Argon, Ion (Ar+)", species
    designation Ar1+(g), table identifier Ar-002. Table revision: CURRENT March 1982
    (1 bar); PREVIOUS March 1977 (1 atm). Enthalpy reference temperature Tr = 298.15 K,
    standard state pressure p0 = 0.1 MPa. Retrieved as
    ``https://janaf.nist.gov/tables/Ar-002.txt``.

VALIDITY RANGE
    The JANAF table runs 0-6000 K and stops there. ``Tmin``/``Tmax`` above are set to
    298.15 K and 6000 K - 298.15 rather than 0 because ``Cpdata`` starts at the reference
    temperature. Nothing here may be used above 6000 K. This is a GAS temperature range;
    it says nothing about the electron temperature, which the ionisation rate law carries
    separately and which has its own range in ``voronov.yaml``.

CONVENTION RECONCILIATION -- THE ONE PIECE OF ARITHMETIC IN THIS FILE
    JANAF tabulates Delta-f H(298.15) = 1526.778 kJ/mol under the ELECTRON convention,
    in which the released electron carries H(298.15) - H(0) = 5/2 R T = 6.197 kJ/mol.
    This database prices the electron at zero enthalpy at all temperatures, which is the
    ION convention, so the value entered is

        1526.778 - 6.197 = 1520.581 kJ/mol.

    Checked a second, independent way from the same table's 0 K row, where the two
    conventions coincide because the electron's integrated heat capacity is zero at 0 K:

        Delta-f H(0)          = 1520.573 kJ/mol            (JANAF Ar-002, T = 0 row)
        + [H(298)-H(0)]_Ar+   = + 6.206 kJ/mol             (JANAF Ar-002, T = 0 row)
        - [H(298)-H(0)]_Ar    = - 6.197 kJ/mol             (JANAF Ar-001, T = 0 row)
        = 1520.582 kJ/mol

    The two routes close to 0.001 kJ/mol. ``E0`` is the 0 K value taken verbatim; it needs
    no conversion for the same reason.

    Cpdata and S298 are transcribed unconverted: they are properties of the ion itself and
    the convention touches only the electron's own thermal functions.

CORROBORATION OF THE TRANSCRIPTION
    Five checks, all closing, none of them a second measurement of the physics:
    1. S(298.15) = 166.404 J/(mol*K) here matches the 166.40 J/(mol*K) that the NIST
       Chemistry WebBook species page for the argon cation (CAS 14791-69-6) reports from
       the same Chase (1998) review - a different NIST renderer, same underlying table.
    2. Delta-f H(0) = 1520.573 kJ/mol against argon's first ionisation energy,
       15.7596119 +/- 0.0000005 eV = 1520.5717 kJ/mol (Kramida, Ralchenko, Reader and
       NIST ASD Team, NIST Atomic Spectra Database ver. 5.12, doi:10.18434/T4W30F,
       accessed 2026-08-26). Agreement 0.0013 kJ/mol.
    3. Delta-f H(298.15) - Delta-f H(0) = 1526.778 - 1520.573 = 6.205 kJ/mol, which is the
       electron's 6.197 kJ/mol plus the 0.009 kJ/mol by which Ar+ exceeds 5/2 R T. That
       identifies the table as EC and not IC by arithmetic rather than by its wording.
    4. Delta-f G(298.15): 1526.778 - 298.15 x (166.404 + 20.979 - 154.845)/1000 =
       1517.078 kJ/mol against the table's own 1517.077 - which also confirms that the
       table carries the electron as a product with S = 20.979 J/(mol*K), i.e. EC.
    5. S(298.15): S(Ar) + R ln(4/1) = 154.845 + 11.526 = 166.371, plus the 0.033
       J/(mol*K) electronic-entropy contribution of the 2P(1/2) level = 166.404.

PHYSICS THE TABLE ENCODES, RECORDED SO THE NON-CONSTANT Cp IS NOT MISTAKEN FOR NOISE
    Ar+ is 2P with a 2P(3/2) ground level and a 2P(1/2) level 1431.6 cm^-1 (2060 K) above
    it. That is why Cp rises from 20.984 J/(mol*K) at 298.15 K to a maximum of
    22.773 J/(mol*K) near 1000 K and falls back toward 5/2 R = 20.786 J/(mol*K) at 6000 K,
    why S(298.15) exceeds neutral argon's by R ln 4 rather than by nothing, and why
    H(298)-H(0) is 6.206 rather than 6.197 kJ/mol. A monatomic-ion entry with a flat
    Cp = 5/2 R would be wrong by up to 10 % over 600-2000 K.

STRUCTURE
    ``1 Ar u1 p3 c+1`` - the gas-phase ground state, 3s2 3p5, one unpaired electron and
    three lone pairs, multiplicity 2. RMG's SMILES round trip corrupts this species
    (``[Ar+]`` reads back as Ar2+, charge doubled), so the adjacency list above is the
    only safe interchange form for it.

NOT THIS SPECIES' REVERSE, AND NOT A RATE
    This entry supplies thermochemistry only. It authorises no channel. Ar+ + e- -> Ar
    radiative recombination has no entry in ``badnell.yaml`` (Z=18 stops at N=11, the
    Na-like ceiling) and was deliberately not added; see ``docs/i120-argon-recombination.md``
    on the branch ``i120-argon-recombination``.
""",
)

entry(
    index = 1,
    label = "[Hep]",
    molecule =
"""
multiplicity 2
1 He u1 p0 c+1
""",
    thermo = ThermoData(
        # NIST-JANAF Fourth Edition table He-002, "Helium, Ion (He+)", He1+(g), verbatim.
        # He+ is hydrogen-like (2S, one 1s electron, no low-lying electronic levels), so
        # Cp is a flat 5/2 R = 20.786 J/(mol*K) at every tabulated temperature.
        Tdata = ([298.15, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000,
                  6000], 'K'),
        Cpdata = ([20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786,
                   20.786, 20.786, 20.786, 20.786, 20.786], 'J/(mol*K)'),
        H298 = (2372.325, 'kJ/mol'),
        S298 = (131.913, 'J/(mol*K)'),
        Cp0 = (20.7862, 'J/(mol*K)'),
        CpInf = (20.7862, 'J/(mol*K)'),
        Tmin = (298.15, 'K'),
        Tmax = (6000, 'K'),
        E0 = (2372.324, 'kJ/mol'),
    ),
    shortDesc = u"He+ (2S) free monatomic cation, NIST-JANAF table He-002, ion convention",
    longDesc =
u"""
SOURCE
    M. W. Chase, Jr., NIST-JANAF Thermochemical Tables, Fourth Edition, J. Phys. Chem.
    Ref. Data Monograph 9 (1998), pp. 1-1951; table "Helium, Ion (He+)", species
    designation He1+(g), table identifier He-002. Enthalpy reference temperature
    Tr = 298.15 K, standard state pressure p0 = 0.1 MPa. Retrieved as
    ``https://janaf.nist.gov/tables/He-002.txt``.

VALIDITY RANGE
    The JANAF table runs 0-6000 K and stops there. ``Tmin``/``Tmax`` are 298.15 K and
    6000 K - 298.15 rather than 0 because ``Cpdata`` starts at the reference temperature.
    Nothing here may be used above 6000 K. This is a GAS temperature range; it says
    nothing about the electron temperature, which the ionisation rate law carries
    separately.

CONVENTION RECONCILIATION -- THE ONE PIECE OF ARITHMETIC IN THIS ENTRY
    JANAF tabulates Delta-f H(298.15) = 2378.522 kJ/mol under the ELECTRON convention,
    in which the released electron carries H(298.15) - H(0) = 5/2 R T = 6.197 kJ/mol.
    This database prices the electron at zero enthalpy at all temperatures, which is the
    ION convention (see the library longDesc), so the value entered is

        2378.522 - 6.197 = 2372.325 kJ/mol.

    Checked a second, independent way from the same table's 0 K row, where the two
    conventions coincide because the electron's integrated heat capacity is zero at 0 K:

        Delta-f H(0)          = 2372.324 kJ/mol            (JANAF He-002, T = 0 row)
        + [H(298)-H(0)]_He+   = + 6.197 kJ/mol             (JANAF He-002, T = 0 row)
        - [H(298)-H(0)]_He    = - 6.197 kJ/mol             (JANAF He-001, T = 0 row)
        = 2372.324 kJ/mol

    The two routes close to 0.001 kJ/mol. ``E0`` is the 0 K value taken verbatim; it
    needs no conversion for the same reason. Cpdata and S298 are transcribed unconverted:
    they are properties of the ion itself and the convention touches only the electron.

CORROBORATION OF THE TRANSCRIPTION
    1. Delta-f H(0) = 2372.324 kJ/mol against helium's first ionisation energy,
       24.58738880 eV = 2372.323 kJ/mol (Kramida, Ralchenko, Reader and the NIST ASD
       Team, NIST Atomic Spectra Database ver. 5.12, doi:10.18434/T4W30F, 1 eV =
       96.48533212 kJ/mol CODATA). Agreement 0.001 kJ/mol.
    2. S(298.15) = 131.913 J/(mol*K) = S(He, 126.152) + R ln 2 = 126.152 + 5.763 =
       131.915 J/(mol*K). The R ln 2 is the 2S(1/2) ground-level degeneracy of the
       one-electron ion; there is no fine-structure term because He+ has an S ground
       term with no orbital angular momentum.

PHYSICS THE TABLE ENCODES
    He+ is a one-electron (hydrogen-like) ion in a 2S(1/2) ground state. An S term has
    no low-lying fine-structure partner, so unlike Ar+/Ne+ there is no Schottky bump:
    Cp is a flat 5/2 R = 20.786 J/(mol*K) across the whole table, and the entropy exceeds
    neutral helium's by exactly R ln 2 rather than R ln 4. A flat monatomic Cp is the
    correct physics here, not an approximation.

STRUCTURE
    ``1 He u1 p0 c+1`` -- one unpaired electron, no lone pairs, multiplicity 2. The
    species is genuinely He+, a bare helium cation with no hydrogen. ``to_smiles()`` writes
    it correctly as ``[He+]`` (no phantom hydrogen), but the monatomic-ion SMILES round
    trip reads that string back with net charge +2, the same ``from_smiles`` corruption the
    ``[Arp]`` entry above documents, so the adjacency list is the only safe interchange
    form. Do not be misled by ``[HeH+]`` (helium hydride) appearing in group-additivity
    error messages for this species: that is group additivity's own radical-saturation
    reference -- ``saturate_radicals`` caps the open valence with an H to look up an HBI
    base -- not the species and not a SMILES bug. That the diagnostic prints the saturated
    intermediate rather than the species asked about is a genuinely misleading behaviour,
    but it is a runtime-repo diagnostic matter, not a property of this entry.
""",
)

entry(
    index = 2,
    label = "[Nep]",
    molecule =
"""
multiplicity 2
1 Ne u1 p3 c+1
""",
    thermo = ThermoData(
        # NIST-JANAF Fourth Edition table Ne-002, "Neon, Ion (Ne+)", Ne1+(g), verbatim.
        # Ne+ is 2P with a 2P(3/2) ground level and a 2P(1/2) level ~780 cm^-1 above it,
        # so Cp carries a Schottky bump peaking near 500 K, like Ar+ but at lower T.
        Tdata = ([298.15, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 4000, 5000,
                  6000], 'K'),
        Cpdata = ([22.119, 22.133, 22.650, 22.788, 22.718, 22.382, 22.048, 21.507,
                   21.239, 21.008, 20.916, 20.872, 20.846], 'J/(mol*K)'),
        H298 = (2080.769, 'kJ/mol'),
        S298 = (158.307, 'J/(mol*K)'),
        Cp0 = (20.7862, 'J/(mol*K)'),
        CpInf = (20.7862, 'J/(mol*K)'),
        Tmin = (298.15, 'K'),
        Tmax = (6000, 'K'),
        E0 = (2080.662, 'kJ/mol'),
    ),
    shortDesc = u"Ne+ (2P) free monatomic cation, NIST-JANAF table Ne-002, ion convention",
    longDesc =
u"""
SOURCE
    M. W. Chase, Jr., NIST-JANAF Thermochemical Tables, Fourth Edition, J. Phys. Chem.
    Ref. Data Monograph 9 (1998), pp. 1-1951; table "Neon, Ion (Ne+)", species
    designation Ne1+(g), table identifier Ne-002. Enthalpy reference temperature
    Tr = 298.15 K, standard state pressure p0 = 0.1 MPa. Retrieved as
    ``https://janaf.nist.gov/tables/Ne-002.txt``.

VALIDITY RANGE
    The JANAF table runs 0-6000 K and stops there. ``Tmin``/``Tmax`` are 298.15 K and
    6000 K - 298.15 rather than 0 because ``Cpdata`` starts at the reference temperature.
    Nothing here may be used above 6000 K. This is a GAS temperature range; it says
    nothing about the electron temperature, which the ionisation rate law carries
    separately.

CONVENTION RECONCILIATION -- THE ONE PIECE OF ARITHMETIC IN THIS ENTRY
    JANAF tabulates Delta-f H(298.15) = 2086.966 kJ/mol under the ELECTRON convention,
    in which the released electron carries H(298.15) - H(0) = 5/2 R T = 6.197 kJ/mol.
    This database prices the electron at zero enthalpy at all temperatures, which is the
    ION convention (see the library longDesc), so the value entered is

        2086.966 - 6.197 = 2080.769 kJ/mol.

    Checked a second, independent way from the same table's 0 K row, where the two
    conventions coincide because the electron's integrated heat capacity is zero at 0 K:

        Delta-f H(0)          = 2080.662 kJ/mol            (JANAF Ne-002, T = 0 row)
        + [H(298)-H(0)]_Ne+   = + 6.304 kJ/mol             (JANAF Ne-002, T = 0 row)
        - [H(298)-H(0)]_Ne    = - 6.197 kJ/mol             (JANAF Ne-001, T = 0 row)
        = 2080.769 kJ/mol

    The two routes close to 0.001 kJ/mol. ``E0`` is the 0 K value taken verbatim; it
    needs no conversion for the same reason. Cpdata and S298 are transcribed unconverted:
    they are properties of the ion itself and the convention touches only the electron.
    (The Ne+ increment [H(298)-H(0)] = 6.304 exceeds a bare monatomic gas's 6.197 by the
    0.107 kJ/mol its 2P fine structure contributes, exactly as for Ar+.)

CORROBORATION OF THE TRANSCRIPTION
    1. Delta-f H(0) = 2080.662 kJ/mol against neon's first ionisation energy,
       21.564540 eV = 2080.662 kJ/mol (Kramida, Ralchenko, Reader and the NIST ASD Team,
       NIST Atomic Spectra Database ver. 5.12, doi:10.18434/T4W30F, 1 eV =
       96.48533212 kJ/mol CODATA). Agreement < 0.001 kJ/mol.
    2. S(298.15) = 158.307 J/(mol*K) = S(Ne, 146.327) + R ln 4 + fine structure =
       146.327 + 11.526 + 0.454 = 158.307 J/(mol*K). The R ln 4 is the 2P(3/2)
       ground-level degeneracy; the 0.454 is the 2P(1/2) electronic contribution, the
       same structure as Ar+.

PHYSICS THE TABLE ENCODES
    Ne+ is 2P with a 2P(3/2) ground level and a 2P(1/2) level ~780.4 cm^-1 above it (a
    smaller splitting than Ar+'s 1431.6 cm^-1). That is why Cp rises from 22.119 at
    298.15 K to a maximum of 22.788 J/(mol*K) near 500 K -- a lower peak temperature than
    Ar+'s ~1000 K because the level spacing is smaller -- and falls back toward 5/2 R =
    20.786 J/(mol*K) at 6000 K. A monatomic-ion entry with a flat Cp = 5/2 R would be
    wrong by up to ~10 % over 400-1500 K.

STRUCTURE
    ``1 Ne u1 p3 c+1`` -- 2s2 2p5, one unpaired electron and three lone pairs,
    multiplicity 2. The species is genuinely Ne+, a bare neon cation with no hydrogen.
    ``to_smiles()`` writes it correctly as ``[Ne+]`` (no phantom hydrogen), but the
    monatomic-ion SMILES round trip reads that string back with net charge +2, the same
    ``from_smiles`` corruption the ``[Arp]`` entry documents, so the adjacency list is the
    only safe interchange form. The ``[NeH+]`` that appears in group-additivity error
    messages is GA's own ``saturate_radicals`` reference (an H capping the open valence to
    find an HBI base), not the species and not a SMILES bug -- a misleading diagnostic,
    someone else's runtime-repo ticket, not a property of this entry.
""",
)
