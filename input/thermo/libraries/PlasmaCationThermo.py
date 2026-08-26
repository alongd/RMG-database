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

WHAT IS NOT HERE
----------------
``Ar2+``. Tabulated thermodynamic functions for it do exist - Maltsev, Morozov & Osina,
"Thermodynamic Properties of Ar2+ and Ar2 Argon Dimers", High Temperature 57 (2019) 37-40,
doi:10.1134/S0018151X19010176, covering 298.15-10000 K and folded into IVTANTHERMO - but
that paper is closed access with no open-access copy, and ATcT's argon-dimer-cation page
returns HTTP 403 from here. Without the tabulated Cp(T) and S(298) there is no way to
enter it that is not authoring, so it is not entered. See
``docs/i127-argon-cation-thermo.md``.

Higher argon charge stages (Ar2+ the dication, Ar3+, ...) are absent for a different
reason: ``voronov.yaml`` can drive them, but RMG cannot construct a doubly charged
monatomic cation, so there is nothing for a thermochemistry entry to attach to.
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
