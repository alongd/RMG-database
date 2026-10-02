#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaThermo"
thermoConvention = "ion"
shortDesc = u"Sourced gas-phase thermochemistry for ions of plasma interest"
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

The monatomic entries here are TRANSCRIBED from published tables. The Ar2+ and O3- entries are
derived from primary-read spectroscopic constants and stated partition-function
calculations; each longDesc gives its complete derivation. Except for the one explicitly
identified interpolated vibrational level in that Ar2+ derivation and the documented
298 K reference extensions of the oxygen Cp grids, no value in this file
is estimated, interpolated, averaged between sources, or computed from a quantum-chemistry
calculation or a group-additivity scheme.

DERIVATION ADMISSION RULE
--------------------------
This library admits (1) directly transcribed ion thermochemistry from a published
table and (2) an entry derived from primary-read spectroscopic constants when the entry
states every constant's source, DOI, page/table location and provenance grade, and marks
every calculated number as derived. The derived entries in this file are ``[Ar2p]`` and ``[O3m]``.

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

THIS DATABASE AND THIS RUNTIME USE THE ION CONVENTION. Determined, not assumed. Every
entry in this library, including the derived ``[Ar2p]`` entry, uses that convention:

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
arithmetic applied to the transcribed JANAF entries in this file. The derived ``[Ar2p]``
entry is calculated by the documented derivation below.

REFERENCE STATE CONVENTION
--------------------------
Every entry is a gas-phase species at the 1 bar standard state (the 0.1 MPa standard
state used by the JANAF tables). Formation enthalpies use the listed element reference
states at 0 K. The JANAF entries are TRANSCRIBED under this gas/1-bar/ION
convention after their electron-convention enthalpies are reconciled in their own
longDescs. ``[Ar2p]`` and ``[O3m]`` are DERIVED under the same gas/1-bar/ION
convention from their primary-read spectroscopic constants. There is deliberately one electron convention
per runtime: no entry in this library uses the electron convention.

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


OXYGEN IONS
-----------
The entries [Op], [O2p], [O2m] transcribe NIST-JANAF Fourth Edition
O-002, O-030, O-031 (SRD13 content 1998, doi:10.18434/T42S31; grade P).
[Om] transcribes the published McBride NASA7 coefficient table in
Goos/Burcat/Ruscic BURCAT.THR (species last added 3 January 2023),
with independent JANAF O-003 checks. All signed EC -> IC conversions
use the fixed 298.15 K enthalpy reference; anions ADD 6197.392574 J/mol.
Species Cp and S are unchanged. The ThermoData entries shift their
anchors to literal 298 K with the first source Cp segment, keeping the
whole source grid through 6000 K. [Om]'s first source polynomial has an
explicit 0.15 K analytical extension to 298 K for that same reference.
No new polynomial fitting or cross-source averaging is performed here.
RMG's production processing converts ThermoData via Wilhoit into NASA
with forced 100-5000 K bounds. This does not extend the source coverage;
[O3m] is delivered only through 1000 K. Published library NASA7 [Om]
retains its full 298-6000 K interval. Production H/S/Cp errors at both
reference temperatures and the imposed ranges are documented and tested.
O+ is the quartet 4S ground state, not PlasmaAir's doublet Op graph.
The [O3m] entry derives its thermal functions from primary-read measured
spectroscopic constants and transcribes ATcT Hf(0); its complete calculation,
assumptions and limitations are in its longDesc and docs/plasma-o2-charged-data.md.

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


Two argon cation species are easy to confuse because plain ASCII writes both "Ar2+", so
this section spells them apart and uses the unambiguous forms throughout: ``Ar2(+)`` is
the argon DIMER cation (diatomic, net charge +1); ``Ar(2+)`` is the argon DICATION
(monatomic, net charge +2).

``Ar2(+)`` -- the argon dimer cation (diatomic, +1) -- is entered below as the ``[Ar2p]``
DERIVED entry. Its primary-read constants, partition-function calculation, and ruled
database values are documented in that entry. Tabulated thermodynamic functions for the
same species do exist - Maltsev, Morozov & Osina, "Thermodynamic Properties of Ar2+ and
Ar2 Argon Dimers", High Temperature 57 (2019) 37-40, doi:10.1134/S0018151X19010176,
covering 298.15-10000 K and folded into IVTANTHERMO - but that paper is closed access
with no open-access copy, and ATcT's argon-dimer-cation page returns HTTP 403 from here.
That not-yet-read tabulation would supersede the derived entry once it is defensibly
read and transcribed. See ``docs/i127-argon-cation-thermo.md``.

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
    shortDesc = u"Ar+ (2P) free monatomic cation, NIST-JANAF table Ar-002, gas-phase 1 bar, ion convention",
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
    shortDesc = u"He+ (2S) free monatomic cation, NIST-JANAF table He-002, gas-phase 1 bar, ion convention",
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
    shortDesc = u"Ne+ (2P) free monatomic cation, NIST-JANAF table Ne-002, gas-phase 1 bar, ion convention",
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

entry(
    index = 3,
    label = "[Ar2p]",
    molecule =
"""
multiplicity 2
1 Ar u0 p3 c+1 {2,S}
2 Ar u1 p3 c0 {1,S}
""",
    thermo = ThermoData(
        # Derived from the primary-read Signorell & Merkt constants below.  The
        # tabulation is the database's source form; RMG processes it downstream.
        Tdata = ([298.15, 300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata = ([36.204, 36.220, 36.833, 37.173, 37.398, 37.712, 37.969, 38.604],
                  'J/(mol*K)'),
        H298 = (1391.112, 'kJ/mol'),
        S298 = (237.472, 'J/(mol*K)'),
        Cp0 = (29.1006, 'J/(mol*K)'),
        CpInf = (37.4151, 'J/(mol*K)'),
        Tmin = (298.15, 'K'),
        Tmax = (1500, 'K'),
    ),
    shortDesc = u"Ar2+ (A 2Sigma+1/2u) dimer cation, derived primary-read constants, gas-phase 1 bar, ion convention",
    longDesc =
u"""
PROVENANCE AND GRADE
    This is a DERIVED entry, admitted under the library header's primary-read
    spectroscopic-constant rule. It is not a transcription of Maltsev, Morozov & Osina
    (2019). The primary-read constants are split between the two papers: D0 and r_e
    below are from Signorell & Merkt (SM98), J. Chem. Phys. 109 (1998) 9762-9771,
    doi:10.1063/1.477646, abstract/p. 9766 and Table II; omega_e and omega_e x_e are
    from Signorell, Wuest & Merkt (SWM97), J. Chem. Phys. 107 (1997) 10819-10822,
    doi:10.1063/1.474199, Table I p. 10821. Maltsev, Morozov & Osina (2019) remains
    the not-yet-read tabulation that would supersede this derived entry when checked.

    D0(Ar2+, A) = 10603.7 +/- 6 cm^-1: SM98 abstract and p. 9766, derived from the
    measured potential curve; grade PRIMARY-READ. The potential's De was held at the
    1997 value, so this is a refinement, not an independent measurement.
    omega_e = 307.0 +/- 0.4 cm^-1 and omega_e x_e = 2.05 +/- 0.05 cm^-1:
    Signorell, Wuest & Merkt, J. Chem. Phys. 107 (1997) 10819-10822,
    doi:10.1063/1.474199, Table I p. 10821; grade PRIMARY-READ. SM98 confirms these
    low-v constants on p. 9766; grade PRIMARY-READ.
    r_e = 2.32 +/- 0.09 A: SM98, p. 9766, Table II; grade PRIMARY-READ (measured).
    sigma = 2: SM98 p. 9766 states that the spin statistical weights of odd N and even
    N+ levels are zero, so half the rotational levels are absent; grade PRIMARY-READ.
    g_el = 2: the observed A 2Sigma+1/2u ground state in SM98, abstract and p. 9766;
    grade PRIMARY-READ.
    Ar+ Delta-f H(0) = 1520.573 kJ/mol: Chase, NIST-JANAF Fourth Edition (1998),
    table Ar-002, T = 0 row, pp. 1-1951, retrieved from
    https://janaf.nist.gov/tables/Ar-002.txt; grade TRANSCRIBED. The database's ion
    convention is the convention used here, as stated in the library header.

DERIVATION (all results in this block are DERIVED)
    The partition function contains translation for m(Ar2+) = 79.896 amu, a rigid rotor
    with sigma = 2 and r_e = 2.32 A, the electronic degeneracy g_el = 2, and exactly 53
    vibrational levels. The level set used by ``docs/ar2p-thermo/thermo_check.py`` is:

      * v = 0, 1, 2, 4: Morse substitutions derived from the low-v constants
        omega_e = 307.0 and omega_e x_e = 2.05 cm^-1, read from Signorell, Wuest &
        Merkt (SWM97), J. Chem. Phys. 107 (1997) 10819-10822, abstract and Table I
        p. 10821. SM98 p. 9766 confirms that the low-v levels are the Morse-fit part.
      * v = 3, 5-10, and 12-52: the 48 calculated line positions in Signorell & Merkt
        (SM98), J. Chem. Phys. 109 (1998) 9762-9771, Table I p. 9765, shifted as
        G(v)-G(0) = nu_calc - (116591.1 - 2.0) cm^-1.
      * v = 11: one explicitly INTERPOLATED level, the arithmetic mean of the v = 10
        and v = 12 shifted SM98 levels because Table I does not list v = 11.

    No v = 53, 54, or 55 level is included. A pure 56-level Morse alternative would
    instead give S(298.15) = 237.477626 J/(mol*K) and Cp(1500) = 38.566234 J/(mol*K),
    versus the shipped hybrid values S(298.15) = 237.472407 J/(mol*K) and Cp(1500) =
    38.603586 J/(mol*K).

    The older SWM97 Morse cutoff 10601.2 cm^-1 is retained only as the derived
    implementation cutoff for those Morse substitutions; it is the SWM97 D0 value
    (abstract/Table I p. 10821). The formation-energy calculation uses the refined SM98
    D0(Ar2+, A) = 10603.7 +/- 6 cm^-1, extracted from the potential curve (SM98 abstract
    and p. 9766). Thus the two constants are not interchangeable source values.

    In the SM98 shift, 116591.1 cm^-1 is the measured Ar2 ionization energy (SM98
    abstract and Eq. (5), p. 9766), while the 2.0 cm^-1 subtraction is the delta defined
    with the Table I level construction on p. 9766. Both are primary-read constants;
    the subtraction is the source-defined level-origin arithmetic.

    The anharmonic fallback levels use

        G(v) = omega_e(v+1/2) - omega_e x_e(v+1/2)^2 - G(0),

    retaining levels below the SWM97 Morse cutoff only for the four stated substitutions.
    The calculation was independently reproduced
    by the versioned calculation in ``docs/ar2p-thermo/thermo_check.py``; its output is
    recorded in ``docs/ar2p-thermo/thermo_check.log``. It gives
    H-H(0) = 9.781223 kJ/mol, S(298.15) = 237.472407 J/(mol*K), and the Cp values
    tabulated above at 298.15, 300, 400, 500, 600, 800, 1000 and 1500 K.

    The 79.896 amu model mass is 2 x 39.948 u, using the NIST/CIAAW natural-abundance
    standard atomic weight of argon; it is not 2 x the Ar-40 isotope mass minus an
    electron. The CODATA 2018 values of h, kB, c, N_A and m_u are documented in
    docs/ar2p-thermo/thermo_check.py. The conversion 0.01196265656387 kJ/mol per
    cm^-1 is DERIVED as N_A h c / 1000 because that script uses c in cm/s and the
    wavenumber in cm^-1. Thus:

    Delta-f H(0) = 1520.573 - (10603.7 cm^-1)(0.01196265656 kJ/mol per cm^-1)
                  = 1393.724579 kJ/mol (DERIVED).
    H(298.15) = Delta-f H(0) + [H(298.15)-H(0)]_Ar2+
                - 2(5/2 R T) = 1391.111017 kJ/mol (DERIVED),
    while the ruled database value is H298 = 1391.112 kJ/mol. The difference is
    0.000983 kJ/mol, i.e. 0.983 J/mol, rounded at the ruled 1 J/mol precision. The factor
    of two is the two explicit atoms in the ion-convention formation reaction. Delta-f H(0) is recorded
    here rather than as ``E0``: the scope's processing probe showed that a raw E0 field
    is on a different scale from this entry's H298 and is discarded by RMG processing.

    The tabulated values are the database ThermoData form over 298.15-1500 K. Cp0 = 3.5R
    and CpInf = 4.5R are derived limiting values (R = 8.314462618 J/(mol*K)); the
    computed Cp at 1500 K is allowed to exceed CpInf because the latter is only the
    high-temperature rigid-rotor/harmonic-oscillator limit for this finite model.

REFERENCE-STATE AND VALIDITY
    This entry uses the ion convention: the database electron has H = S = Cp = 0 at
    every temperature. It is valid only over 298.15-1500 K. No value above 1500 K is
    supported by the spectroscopic-level model or this tabulation.

KEQ CHECK (DERIVED)
    For Ar+ + Ar + Ar <=> Ar2+ + Ar, the calculated standard-state thermochemical
    factor relative to the earlier scope model is 0.896582 at 298.15 K and 0.895841 at
    1000 K. The corresponding Delta-Phi values are -0.907653 and -0.914524 J/(mol*K),
    with Phi = S - [H-H(0)]/T. These are the factors used in the run report; the
    reaction itself is outside this thermo-only ticket.

    Maltsev et al., High Temperature 57 (2019) 37-40, doi:10.1134/S0018151X19010176,
    Table 4 p. 39, is retained only as a secondary cross-check. Its entropy differs by
    approximately R ln 2, consistent with the missing symmetry factor inferred from
    SM98, and its Cp discrepancy was not reproduced. It is not used for this entry.
""",
)

entry(
    index = 4,
    label = "[Op]",
    molecule = """
multiplicity 4
1 O u3 p1 c+1
""",
    thermo = ThermoData(
        Tdata = ([298.0, 298.15, 300.0, 350.0, 400.0, 450.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0], 'K'),
        Cpdata = ([20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.786, 20.787, 20.787, 20.788, 20.789, 20.79, 20.792, 20.795, 20.799, 20.804, 20.81, 20.818, 20.827, 20.839, 20.853, 20.87, 20.89, 20.912, 20.938, 20.968, 21.001, 21.038, 21.079, 21.125, 21.174, 21.229, 21.287, 21.351, 21.418, 21.491, 21.568, 21.649, 21.735, 21.826, 21.921, 22.02, 22.123, 22.231], 'J/(mol*K)'),
        H298 = (1562.585489526, 'kJ/mol'),
        S298 = (154.948539881, 'J/(mol*K)'),
        Cp0 = (20.786156545383, 'J/(mol*K)'),
        CpInf = (20.786156545383, 'J/(mol*K)'),
        E0 = (1560.733, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = u"O+(4S), JANAF O-002, gas/1 bar/ion convention; grade P",
    longDesc = u"""
SOURCE AND GRADE
    M. W. Chase Jr., NIST-JANAF Thermochemical Tables, Fourth Edition (1998),
    SRD 13, content version 1998, doi:10.18434/T42S31, table O-002,
    O+(g), rows 0, 298.15-6000 K; grade P (full table read).
    https://janaf.nist.gov/tables/O-002.txt ; accessed 2026-10-02.

CONVENTION AND DERIVATION
    Gas, standard pressure 0.1 MPa (1 bar), ground state 4S.
    The source uses the electron convention. This entry uses the gas-phase
    ion convention (H=S=Cp=0 for the explicit electron), not an electrochemical
    zero-formation-enthalpy convention. Signed charge q = +1.
    Hf_IC(298.15) = 1568.786 - (+1)*(5/2)*R*298.15/1000
                 = 1562.588607426 kJ/mol; R = 8.31446261815324 J/(mol*K).
    Hf(0) = 1560.733 kJ/mol needs no electron correction at zero temperature.
    Species Cp and S are transcribed without an electron entropy subtraction.

    RMG ThermoData anchors H298 and S298 at 298 K, not 298.15 K.
    With the line Cp(T)=a*T+b through the first two tabulated points,
    a=0 J/(mol*K**2), b=20.786 J/(mol*K), the
    derived shifts from 298 to 298.15 K are integral(Cp dT)=0.003117900
    kJ/mol and integral(Cp/T dT)=0.010460119 J/(mol*K).
    Thus H298=1562.585489526 kJ/mol and S298=154.948539881 J/(mol*K).
    These are coordinate/convention conversions of the table, not a fitted
    thermal model. All original Cp points are verbatim source rows; the added 298 K
    point is a DERIVED reference-coordinate extension of the first segment. Cp0=2.5R and CpInf=2.5R are the
    classical translation/rotation and fully excited vibration limits used by RMG.
    These limits exclude dissociation and further electronic states; Cp0 is
    the RMG classical limit, not a quantum T -> 0 rotational limit.
    The 298 K point has DERIVED Cp=20.786000000 J/(mol*K), from the
    first segment extended by 0.15 K. Tmin=298 K includes that reference
    point; the original tabulated range is 298.15-6000 K. The source grid remains available through 6000 K. RMG process_thermo_data
    converts ThermoData via Wilhoit to NASA over its hardcoded 100-5000 K
    interval. That imposed interval does not extend the source validity.
    Equal atomic Cp0/CpInf make the runtime's Wilhoit conversion use
    constant Cp=2.5R, losing the JANAF high-T electronic contribution.
    At 5000 K the delivered source Cp=21.351 J/(mol*K), while production
    NASA gives 20.786156545 J/(mol*K), a -2.646 percent error. This known
    loss is tested and documented; the retained source grid is not claimed
    to be reproduced by the transformed model over its whole range.
    See docs/plasma-o2-charged-data.md for measured conversion errors.

CHECK AT ANOTHER TABULATED TEMPERATURE
    At 400 K the source gives Cp=20.786 J/(mol*K),
    S=161.067 J/(mol*K), H(400)-H(298.15)=
    2.117 kJ/mol. Compare RMG's enthalpy against
    1562.588607426+2.117 kJ/mol, not directly against
    the source's temperature-dependent formation-enthalpy column: the latter
    also changes the elemental reference and the electron EC contribution.
    The tests quantify RMG's piecewise-linear Cp integration error.

STRUCTURE
    O+(4S) is represented by the adjacency list above.
    O+ has three unpaired electrons; the existing doublet PlasmaAir Op is not this ground state.
""",
)

entry(
    index = 5,
    label = "[O2p]",
    molecule = """
multiplicity 2
1 O u0 p2 c+1 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([298.0, 298.15, 300.0, 350.0, 400.0, 450.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0], 'K'),
        Cpdata = ([29.194675676, 29.195, 29.199, 29.342, 29.573, 29.882, 30.25, 31.078, 31.916, 32.687, 33.364, 33.945, 34.44, 34.859, 35.216, 35.521, 35.784, 36.011, 36.21, 36.384, 36.538, 36.675, 36.798, 36.908, 37.009, 37.101, 37.185, 37.263, 37.336, 37.403, 37.466, 37.526, 37.583, 37.637, 37.689, 37.74, 37.79, 37.838, 37.887, 37.936, 37.985, 38.035, 38.088, 38.142, 38.199, 38.258, 38.322, 38.389, 38.462, 38.539, 38.622, 38.711, 38.807, 38.91, 39.02, 39.138, 39.265, 39.4, 39.545, 39.699, 39.863, 40.036], 'J/(mol*K)'),
        H298 = (1164.686228200, 'kJ/mol'),
        S298 = (206.200308309, 'J/(mol*K)'),
        Cp0 = (29.100619163536, 'J/(mol*K)'),
        CpInf = (37.415081781690, 'J/(mol*K)'),
        E0 = (1164.700, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = u"O2+(2Pi_g), JANAF O-030, gas/1 bar/ion convention; grade P",
    longDesc = u"""
SOURCE AND GRADE
    M. W. Chase Jr., NIST-JANAF Thermochemical Tables, Fourth Edition (1998),
    SRD 13, content version 1998, doi:10.18434/T42S31, table O-030,
    O2+(g), rows 0, 298.15-6000 K; grade P (full table read).
    https://janaf.nist.gov/tables/O-030.txt ; accessed 2026-10-02.

CONVENTION AND DERIVATION
    Gas, standard pressure 0.1 MPa (1 bar), ground state 2Pi_g.
    The source uses the electron convention. This entry uses the gas-phase
    ion convention (H=S=Cp=0 for the explicit electron), not an electrochemical
    zero-formation-enthalpy convention. Signed charge q = +1.
    Hf_IC(298.15) = 1170.888 - (+1)*(5/2)*R*298.15/1000
                 = 1164.690607426 kJ/mol; R = 8.31446261815324 J/(mol*K).
    Hf(0) = 1164.700 kJ/mol needs no electron correction at zero temperature.
    Species Cp and S are transcribed without an electron entropy subtraction.

    RMG ThermoData anchors H298 and S298 at 298 K, not 298.15 K.
    With the line Cp(T)=a*T+b through the first two tabulated points,
    a=0.00216216216216 J/(mol*K**2), b=28.5503513514 J/(mol*K), the
    derived shifts from 298 to 298.15 K are integral(Cp dT)=0.004379226
    kJ/mol and integral(Cp/T dT)=0.014691691 J/(mol*K).
    Thus H298=1164.686228200 kJ/mol and S298=206.200308309 J/(mol*K).
    These are coordinate/convention conversions of the table, not a fitted
    thermal model. All original Cp points are verbatim source rows; the added 298 K
    point is a DERIVED reference-coordinate extension of the first segment. Cp0=3.5R and CpInf=4.5R are the
    classical translation/rotation and fully excited vibration limits used by RMG.
    These limits exclude dissociation and further electronic states; Cp0 is
    the RMG classical limit, not a quantum T -> 0 rotational limit.
    The 298 K point has DERIVED Cp=29.194675676 J/(mol*K), from the
    first segment extended by 0.15 K. Tmin=298 K includes that reference
    point; the original tabulated range is 298.15-6000 K. The source grid remains available through 6000 K. RMG process_thermo_data
    converts ThermoData via Wilhoit to NASA over its hardcoded 100-5000 K
    interval. That imposed interval does not extend the source validity.
    See docs/plasma-o2-charged-data.md for measured conversion errors.

CHECK AT ANOTHER TABULATED TEMPERATURE
    At 400 K the source gives Cp=29.573 J/(mol*K),
    S=214.839 J/(mol*K), H(400)-H(298.15)=
    2.990 kJ/mol. Compare RMG's enthalpy against
    1164.690607426+2.990 kJ/mol, not directly against
    the source's temperature-dependent formation-enthalpy column: the latter
    also changes the elemental reference and the electron EC contribution.
    The tests quantify RMG's piecewise-linear Cp integration error.

STRUCTURE
    O2+(2Pi_g) is represented by the adjacency list above.
    The molecular-ion graph follows the existing PlasmaAir charge and radical encoding.
""",
)

entry(
    index = 6,
    label = "[Om]",
    molecule = """
multiplicity 2
1 O u1 p3 c-1
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.90805921, -1.69804907e-3, 2.98069955e-6,
                          -2.43835127e-9, 7.61229311e-13, 12181.145858937089, 2.80339097],
                Tmin = (298, 'K'), Tmax = (1000, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.54474869, -4.66695513e-5, 1.84912357e-8,
                          -3.18159223e-12, 1.98962956e-16, 12249.583058937089, 4.52131015],
                Tmin = (1000, 'K'), Tmax = (6000, 'K'),
            ),
        ],
        Cp0 = (20.786156545383, 'J/(mol*K)'),
        CpInf = (20.786156545383, 'J/(mol*K)'),
        E0 = (105.814, 'kJ/mol'),
        Tmin = (298, 'K'), Tmax = (6000, 'K'),
    ),
    shortDesc = u"O-(2P), published McBride NASA7, JANAF cross-check, gas/1 bar/ion convention; grade P",
    longDesc = u"""
SOURCE AND GRADE
    Published NASA7 coefficients: Goos, Burcat and Ruscic, Extended Third
    Millennium Thermodynamic Database, BURCAT.THR, species last added
    3 January 2023; record O- g 1/97, CAS 14337-01-0. Grade P for the
    published polynomial table (record and explanatory header read).
    https://respecth.elte.hu/burcat/BURCAT.THR.txt ; accessed 2026-10-02.
    Database citation: Burcat and Ruscic, ANL-05/20 / TAE 960 (2005).
    The record attributes coefficients to Bonnie McBride and electronic
    levels to Gurvich 1989. It notes the JANAF fine-structure splitting
    discrepancy (text 177.08 versus calculation 181 cm^-1). Original
    Gurvich full text was not independently read; P applies to the published
    coefficient table, not to an invented original measurement attribution.
    No polynomial is fitted here. Raw coefficients are pinned in
    test/plasma_oxygen_om_nasa_reference.json.

CONVENTION AND DERIVATION
    Gas, 1 bar, ground-state O-(2P), ion convention. The published model
    has electron-convention Hf(298.15)=101.846 kJ/mol. For q=-1 the signed
    conversion ADDS (5/2)*R_SI*298.15=6197.392574 J/mol to H at every T
    relative to the fixed 298.15 K reference; Cp and S stay unchanged.
    NASA7 H/R contains its integration constant a6. Each source a6,
    11435.7717 and 11504.2089 K, therefore increases by
    6197.392574/R_runtime = 745.374158937089 K; R_runtime=8.314472.
    This is an enthalpy-reference conversion, not a new fit or averaging.
    Cp0=CpInf=5R_SI/2 are the atomic classical limits. Source E0=105.814
    kJ/mol is transcribed from JANAF O-003, 0 K row, independently of
    RMG's downstream Wilhoit-extrapolated conformer E0.

INDEPENDENT JANAF CHECK AND PRODUCTION PATH
    Chase, NIST-JANAF Fourth Edition (1998), SRD13 content 1998,
    doi:10.18434/T42S31, table O-003, grade P (full table read):
    https://janaf.nist.gov/tables/O-003.txt . H_IC(298.15)=108.043392574
    kJ/mol, S=157.790, Cp=21.692 J/(mol*K); at 400 K H increment=2.191
    kJ/mol, S=164.114 and Cp=21.364 J/(mol*K). The source polynomial
    differs slightly from the rounded JANAF rows: both comparisons are
    tested and reported, with no adjustment of Cp or entropy coefficients.
    A ThermoData atomic entry with equal Cp0/CpInf loses fine-structure
    Cp in this runtime's Wilhoit conversion. The published NASA7 entry
    instead survives process_thermo_data unchanged when selected from a
    thermo library and can be exported to Chemkin/Cantera.

RANGE AND STATE
    Published range 298.15-6000 K, split at 1000 K; all of the upper range
    is retained. The first polynomial is analytically extended to 298 K
    solely for RMG's literal reference temperature. This 0.15 K extension
    is derived, not an additional source row. It yields Cp=21.685924482,
    H=108.039866792 kJ/mol, S=157.785382796 J/(mol*K).
    The doublet adjacency list matches PlasmaAir O-. Further electronic
    states or ion thermochemistry below 298 K are not supplied.
""",
)

entry(
    index = 7,
    label = "[O2m]",
    molecule = """
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([298.0, 298.15, 300.0, 350.0, 400.0, 450.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0], 'K'),
        Cpdata = ([30.450810811, 30.453, 30.48, 31.224, 31.962, 32.648, 33.262, 34.271, 35.032, 35.609, 36.055, 36.407, 36.691, 36.926, 37.123, 37.293, 37.441, 37.572, 37.69, 37.798, 37.897, 37.989, 38.075, 38.157, 38.234, 38.308, 38.38, 38.448, 38.515, 38.58, 38.644, 38.706, 38.767, 38.826, 38.885, 38.943, 39.001, 39.057, 39.113, 39.169, 39.224, 39.279, 39.333, 39.387, 39.44, 39.494, 39.547, 39.599, 39.652, 39.704, 39.756, 39.808, 39.86, 39.912, 39.963, 40.015, 40.066, 40.117, 40.168, 40.219, 40.27, 40.321], 'J/(mol*K)'),
        H298 = (-42.400175212, 'kJ/mol'),
        S298 = (209.575675716, 'J/(mol*K)'),
        Cp0 = (29.100619163536, 'J/(mol*K)'),
        CpInf = (37.415081781690, 'J/(mol*K)'),
        E0 = (-42.464, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = u"O2-(2Pi_g), JANAF O-031, gas/1 bar/ion convention; grade P",
    longDesc = u"""
SOURCE AND GRADE
    M. W. Chase Jr., NIST-JANAF Thermochemical Tables, Fourth Edition (1998),
    SRD 13, content version 1998, doi:10.18434/T42S31, table O-031,
    O2-(g), rows 0, 298.15-6000 K; grade P (full table read).
    https://janaf.nist.gov/tables/O-031.txt ; accessed 2026-10-02.

CONVENTION AND DERIVATION
    Gas, standard pressure 0.1 MPa (1 bar), ground state 2Pi_g.
    The source uses the electron convention. This entry uses the gas-phase
    ion convention (H=S=Cp=0 for the explicit electron), not an electrochemical
    zero-formation-enthalpy convention. Signed charge q = -1.
    Hf_IC(298.15) = -48.593 - (-1)*(5/2)*R*298.15/1000
                 = -42.395607426 kJ/mol; R = 8.31446261815324 J/(mol*K).
    Hf(0) = -42.464 kJ/mol needs no electron correction at zero temperature.
    Species Cp and S are transcribed without an electron entropy subtraction.

    RMG ThermoData anchors H298 and S298 at 298 K, not 298.15 K.
    With the line Cp(T)=a*T+b through the first two tabulated points,
    a=0.0145945945946 J/(mol*K**2), b=26.1016216216 J/(mol*K), the
    derived shifts from 298 to 298.15 K are integral(Cp dT)=0.004567786
    kJ/mol and integral(Cp/T dT)=0.015324284 J/(mol*K).
    Thus H298=-42.400175212 kJ/mol and S298=209.575675716 J/(mol*K).
    These are coordinate/convention conversions of the table, not a fitted
    thermal model. All original Cp points are verbatim source rows; the added 298 K
    point is a DERIVED reference-coordinate extension of the first segment. Cp0=3.5R and CpInf=4.5R are the
    classical translation/rotation and fully excited vibration limits used by RMG.
    These limits exclude dissociation and further electronic states; Cp0 is
    the RMG classical limit, not a quantum T -> 0 rotational limit.
    The 298 K point has DERIVED Cp=30.450810811 J/(mol*K), from the
    first segment extended by 0.15 K. Tmin=298 K includes that reference
    point; the original tabulated range is 298.15-6000 K. The source grid remains available through 6000 K. RMG process_thermo_data
    converts ThermoData via Wilhoit to NASA over its hardcoded 100-5000 K
    interval. That imposed interval does not extend the source validity.
    See docs/plasma-o2-charged-data.md for measured conversion errors.

CHECK AT ANOTHER TABULATED TEMPERATURE
    At 400 K the source gives Cp=31.962 J/(mol*K),
    S=218.752 J/(mol*K), H(400)-H(298.15)=
    3.179 kJ/mol. Compare RMG's enthalpy against
    -42.395607426+3.179 kJ/mol, not directly against
    the source's temperature-dependent formation-enthalpy column: the latter
    also changes the elemental reference and the electron EC contribution.
    The tests quantify RMG's piecewise-linear Cp integration error.

STRUCTURE
    O2-(2Pi_g) is represented by the adjacency list above.
    The molecular-ion graph follows the existing PlasmaAir charge and radical encoding.
""",
)

entry(
    index = 8,
    label = "[O3m]",
    molecule = """
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([298.0, 298.15, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0, 650.0, 700.0, 750.0, 800.0, 850.0, 900.0, 950.0, 1000.0], 'K'),
        Cpdata = ([41.923817394, 41.931351573, 42.024273114, 44.382529297, 46.40991189, 48.109263675, 49.518487162, 50.684175236, 51.650384399, 52.454881647, 53.128631606, 53.696497001, 54.178265602, 54.589651312, 54.943152418, 55.24874693, 55.514440662], 'J/(mol*K)'),
        H298 = (-60.827614921, 'kJ/mol'),
        S298 = (247.946770625, 'J/(mol*K)'),
        Cp0 = (33.257850472613, 'J/(mol*K)'),
        CpInf = (58.201238327073, 'J/(mol*K)'),
        E0 = (-58.47, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"O3-: ATcT Hf(0), derived primary-read spectroscopy, gas/1 bar/ion convention; grade P",
    longDesc = u"""
DERIVED ENTRY -- ADMITTED PRIMARY-READ CONSTANTS, NOT NEUTRAL THERMO PLUS EA
    O3- is X 2B1, with the doublet bent, two equivalent terminal oxygens.
    Only Hf(0) is a transcription. Cp(T), S(T) and the thermal H increment
    are DERIVED in a rigid-rotor/harmonic-oscillator (RRHO) ideal-gas model.
    This is neither a fitted polynomial nor a quantum-chemistry calculation.

SOURCES, LOCATIONS AND GRADES
    ATcT Thermochemical Network version 1.156, Ozonide, species_number=298,
    selected enthalpy table: Hf(0) = -58.47 +/- 0.21 kJ/mol; relative molar
    mass = 47.99875 +/- 0.00090 g/mol. Grade P (complete database page read).
    https://atct.anl.gov/Thermochemical%20Data/version%201.156/species/?species_number=298
    Accessed 2026-10-02. ATcT's 298.15 K value (-60.83 kJ/mol) is not
    substituted for the independent RRHO-derived thermal increment.
    At 0 K the EC and IC electron enthalpy correction is identically zero.

    Arnold, Xu, Kim and Neumark, J. Chem. Phys. 101 (1994) 912-922,
    doi:10.1063/1.467745. Grade P (full paper read from the authors public
    publication archive https://bromine.cchem.berkeley.edu/grppub/pes20.pdf).
    Section IV A, p. 917: r = 1.36 +/- 0.02 A, angle = 111.8 +/- 2.0 deg.
    The text and conclusion give 111.8 deg; Table V rounds differently
    (111.7). The text value is used, with no averaging of these versions.
    Section IV A p. 917 and experimental present-work row of Table V p. 918:
    harmonic wave numbers 975 +/- 50, 550 +/- 50, 880 +/- 50 cm^-1.
    These are spectroscopic constants obtained by the authors from their
    experimental spectra (Franck-Condon analysis/sequence bands), not the
    ab initio rows in Table V. The Table V footnote states that the 880
    value uses sequence bands of an unpublished vibrationally hot spectrum;
    the constant is nonetheless explicitly published in this primary paper.
    We do not refit the spectrum. The paper's measured EA = 2.103 +/- 0.004
    eV (p. 916-917) corroborates ATcT's listed provenance, not a second
    enthalpy to average. Neither matrix frequencies nor calculated geometry
    are substituted.

    JANAF Fourth Edition, SRD 13 content version 1998,
    doi:10.18434/T42S31, table O-029 (O2 reference), 0 K row:
    H(O2,298.15)-H(O2,0) = 8.683 kJ/mol; grade P.
    https://janaf.nist.gov/tables/O-029.txt
    SI defining constants: h=6.62607015e-34 J*s, kB=1.380649e-23 J/K,
    c=299792458 m/s, NA=6.02214076e23 /mol, R=NA*kB.
    These exact SI constants are from BIPM SI Brochure 9th edition (2019),
    official SI defining-constants table (primary standard, grade P),
    https://www.bipm.org/en/measurement-units/si-defining-constants.

COMPLETE DERIVATION, GAS AT 1 BAR, ION CONVENTION
    Use three equal oxygen mass shares m/3 with total m=0.04799875/NA kg.
    Coordinates are (0,0,0), (+r*sin(angle/2),r*cos(angle/2),0),
    (-r*sin(angle/2),r*cos(angle/2),0), shifted to their centre of mass.
    The principal moments from sum(m_i*(r_i^2*identity-r_i*r_i^T)) are
    [1.0297005166650976e-46, 6.7389082932463416e-46, 7.768608809911439e-46] kg*m^2.
    Rotational theta_j = h^2/(8*pi^2*kB*I_j) = [3.9113629096563263, 0.5976535417426835, 0.5184367635810628] K.
    Vibrational theta_i = h*c*100*wave_number_i/kB = [1402.8074555663352, 791.3272826271635, 1266.1236522034615] K.
    Symmetry number sigma=2 from equivalent terminal atoms, electronic
    degeneracy g=2 from the doublet ground state.

    q_trans = (2*pi*m*kB*T/h^2)^(3/2)*kB*T/(1e5 Pa)
    q_rot = sqrt(pi)*T^(3/2)/(sigma*sqrt(theta_A*theta_B*theta_C))
    x_i = theta_i/T
    S/R = ln(q_trans)+5/2 + ln(q_rot)+3/2 + ln(g)
          + sum(x_i/(exp(x_i)-1)-ln(1-exp(-x_i)))
    [H(T)-H(0)]/R = 4*T + sum(theta_i/(exp(x_i)-1))
    Cp/R = 4 + sum(x_i^2*exp(-x_i)/(1-exp(-x_i))^2)

    Hf_IC(298.15) = -58.47 + 10.673174217 - (3/2)*8.683
                 = -60.821325783 kJ/mol.
    The source Hf(0) is convention independent; the derived increment has
    no free-electron thermal term. Equivalently Hf_EC = Hf_IC - (5/2)*R*T
    for this charge -1 ion, so EC -> IC ADDS that electron increment.
    S is the species entropy, without an electron entropy subtraction.
    Derived S(298.15)=247.967869804 J/(mol*K), Cp(298.15)=41.931351573 J/(mol*K).
    ThermoData's 298 K anchors subtract integral(Cp dT)=0.006289138 kJ/mol
    and integral(Cp/T dT)=0.021099179 J/(mol*K) using the first Cp segment.
    The 298 K reference Cp=41.923817394 J/(mol*K) is DERIVED by
    extending the first Cp segment by 0.15 K; all other Cp grid points
    are derived with the stated RRHO formula. Tmin includes that anchor. Downstream
    piecewise-linear integration is checked independently at 400 K.

LIMITATIONS AND RANGE
    Only the ground electronic state and rigid-rotor/harmonic-oscillator
    thermal functions are included. Unknown anion anharmonicities are not
    invented. The spectroscopic uncertainties and this RRHO approximation
    limit accuracy; this does not claim JANAF-grade tabulated thermal data.
    The declared 298-1000 K interval is the calculation's delivery range,
    not an experimentally established interval. Cp0=4R and CpInf=7R are
    the classical translation/nonlinear-rotation and three excited vibration
    limits required by RMG's Wilhoit model, not quantum T -> 0 limits.
    They do not admit source data above 1000 K. process_thermo_data imposes
    NASA metadata 100-5000 K; use this ion only in the delivered 298-1000 K
    interval. Conversion errors at 298.15/400 K are tested and reported. A complete primary-read
    ion thermal table would supersede the derived thermal functions.
""",
)
