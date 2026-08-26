#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for ``PlasmaCationThermo``, the argon-cation thermochemistry entry, and for
the charged-species thermochemistry coverage this ticket measured around it.

The report is ``docs/i127-argon-cation-thermo.md``. This file is the executable half of
it: every number quoted there that can be re-derived is re-derived here, so a later
change that moves one fails a test rather than silently contradicting a document.

Four groups, in descending order of how much they would cost to be wrong about:

1. **The reference-state convention.** ``Ar+`` is entered under the ion convention -
   the electron priced at zero enthalpy at all temperatures - because that is what this
   database and this runtime do. NIST-JANAF publishes the electron-convention value and
   the two differ by 6.197 kJ/mol. A value entered under the wrong one is wrong by an
   amount no other test here would catch, so the determination and the conversion are
   both pinned, by two independent arithmetic routes that close to 0.002 kJ/mol.

2. **The sourced values themselves**, against the source and against argon's ionisation
   energy from an unrelated database.

3. **The whole path** - load, resolve, a finite equilibrium constant, reactor
   acceptance, and the argon ionisation reaction carried end to end. Each separately,
   because each can fail on its own.

4. **The coverage gap's shape**, and the two defects found while measuring it: the
   shipped ``[Lip]`` entry disagrees with lithium's ionisation energy by 145 kJ/mol, and
   group additivity answers for monatomic cations with numbers that put the cation
   *below* the neutral. Both are pinned as they are, not fixed - fixing either is
   another ticket's work - so that if either is ever corrected, the test fails and points
   whoever did it at the report.

Run with the runtime pinned::

    cd /home/alon/Code/RMG-database-i127-argon-thermo
    PYTHONPATH=/home/alon/Code/RMG-Py-i123-integration \\
        python -m pytest test/test_argon_cation_thermo.py -q

``test/conftest.py`` pins ``database.directory`` to this worktree before collection; the
fixtures below assert that pin rather than trusting it.
"""

import math
import os
import shutil
import tempfile

import pytest

from rmgpy import settings
from rmgpy import electron_placement
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.molecule import Molecule
from rmgpy.reaction import Reaction
from rmgpy.species import Species

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,
                                             'input'))
LIBRARY_DIR = os.path.join(THIS_DATABASE, 'thermo', 'libraries')
GROUP_DIR = os.path.join(THIS_DATABASE, 'thermo', 'groups')
KINETICS_LIBRARY_DIR = os.path.join(THIS_DATABASE, 'kinetics', 'libraries')

LIBRARY = 'PlasmaCationThermo'
IONISATION = 'PlasmaElectronImpactIonization'

R = 8.31446261815324
T0 = 298.15
#: kJ/mol per eV, CODATA.
EV = 96.48533212331

# --- the source, quoted so a test can check the file against it -------------------
#: NIST-JANAF Fourth Edition, table Ar-002 "Argon, Ion (Ar+)", T = 298.15 row.
#: Electron convention, in which the released electron carries 5/2 R T.
JANAF_ARP_H298_ELECTRON_CONVENTION = 1526.778      # kJ/mol
JANAF_ARP_S298 = 166.404                           # J/(mol*K)
JANAF_ARP_CP298 = 20.984                           # J/(mol*K)
JANAF_ARP_GF298 = 1517.077                         # kJ/mol
#: NIST-JANAF Ar-002, T = 0 row: delta-f H(0), and -(H - H(Tr)) = H(298.15) - H(0).
JANAF_ARP_H0 = 1520.573                            # kJ/mol
JANAF_ARP_DH_298_0 = 6.206                         # kJ/mol
#: NIST-JANAF Ar-001 "Argon (Ar)", the element reference state.
JANAF_AR_S298 = 154.845                            # J/(mol*K)
JANAF_AR_DH_298_0 = 6.197                          # kJ/mol
#: JANAF's electron, i.e. what the electron convention prices it at.
JANAF_ELECTRON_S298 = 20.979                       # J/(mol*K)

#: NIST Atomic Spectra Database ver. 5.12, doi:10.18434/T4W30F.
IE_AR_EV = 15.7596119
IE_LI_EV = 5.391714996

#: What is actually in the file.
ENTERED_H298 = 1520.581                            # kJ/mol, ion convention
ENTERED_E0 = 1520.573                              # kJ/mol, convention-free at 0 K

AR = '1 Ar u0 p4 c0\n'
ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'
LI = 'multiplicity 2\n1 Li u1 p0 c0\n'
LIP = '1 Li u0 p0 c+1\n'
ELECTRON = '1 e u0 p0 c-1\n'


def _species(adjacency_list, label=''):
    return Species(label=label,
                   molecule=[Molecule().from_adjacency_list(adjacency_list)])


@pytest.fixture(scope='module')
def pinned():
    """Assert the pin rather than trusting it. A run against another checkout would
    otherwise produce a green that means nothing, which has happened on this campaign."""
    assert settings['database.directory'] == THIS_DATABASE, (
        f"database.directory is {settings['database.directory']!r}, not this worktree")
    return THIS_DATABASE


@pytest.fixture(scope='module')
def thermo_db(pinned):
    db = ThermoDatabase()
    db.load_libraries(LIBRARY_DIR)
    db.load_groups(GROUP_DIR)
    return db


@pytest.fixture(scope='module')
def estimator_only(pinned):
    """The same database with every library unloaded, so any answer it gives is group
    additivity and HBI rather than a lookup."""
    db = ThermoDatabase()
    db.load_libraries(LIBRARY_DIR)
    db.unload_libraries()
    db.load_groups(GROUP_DIR)
    assert not db.libraries
    return db


@pytest.fixture(scope='module')
def entry(thermo_db):
    return thermo_db.libraries[LIBRARY].entries['[Arp]']


# =====================================================================================
# 1. The reference-state convention
# =====================================================================================

def test_every_electron_entry_in_this_database_prices_the_electron_at_zero(thermo_db):
    """The determination behind the whole entry, stated as a test.

    Three libraries carry an ``electron`` species. All three give it a NASA polynomial
    whose coefficients are identically zero, so H = S = Cp = 0 at every temperature.
    That is the ion convention (Bartmess 1994), and it is what fixes which of the two
    published Ar+ enthalpies may be entered here. If a library ever gives the electron
    real thermal functions, this fails and the Ar+ entry has to be revisited with it.
    """
    found = {}
    for name, library in thermo_db.libraries.items():
        for label, e in library.entries.items():
            if e.item is not None and e.item.is_electron():
                found[name] = e
    assert set(found) == {'electrocatThermo', 'electrocatLiThermo',
                          'computationalLithiumElectrode'}, sorted(found)
    for name, e in found.items():
        # 298-3000 K is the span those NASA polynomials declare; outside it they raise
        # rather than answer, which is itself a statement that they are placeholders.
        for T in (298.15, 500.0, 1000.0, 3000.0):
            assert e.data.get_enthalpy(T) == 0.0, (name, T)
            assert e.data.get_entropy(T) == 0.0, (name, T)
            assert e.data.get_heat_capacity(T) == 0.0, (name, T)


def test_the_runtime_adds_no_electron_term_to_a_charge_transfer_free_energy(thermo_db):
    """The second half of the determination, and the half that lives in RMG-Py.

    ``Reaction._get_free_energy_of_charge_transfer_reaction`` adds an electrochemical
    term only when ``potential != 0``, and every reactor calls it at zero. So an
    ionisation's dG is the same whether the electron is carried as metadata or as an
    explicit species - which is the ion convention expressed in code.
    """
    ar, arp = _species(AR, 'Ar'), _species(ARP, 'Ar+')
    electron = _species(ELECTRON, 'e-')
    for s in (ar, arp, electron):
        s.thermo = thermo_db.get_thermo_data(s)

    implicit = Reaction(reactants=[ar], products=[arp], electrons=+1, reversible=False)
    explicit = Reaction(reactants=[ar, electron],
                        products=[arp, electron, electron],
                        electrons=0, reversible=False)
    assert implicit.get_free_energy_of_reaction(T0) == pytest.approx(
        explicit.get_free_energy_of_reaction(T0), abs=1e-6)


def test_the_entered_enthalpy_is_the_ion_convention_value_by_two_routes(entry):
    """The one piece of arithmetic applied to any sourced number in this branch.

    Route 1 converts JANAF's 298.15 K electron-convention value by the electron's
    5/2 R T. Route 2 rebuilds it from JANAF's 0 K row, where the two conventions
    coincide. They close to 0.002 kJ/mol, which is what makes the conversion a
    transcription rather than a choice.
    """
    thermal_electron = 2.5 * R * T0 / 1000.0
    assert thermal_electron == pytest.approx(6.197, abs=0.001)

    route_1 = JANAF_ARP_H298_ELECTRON_CONVENTION - thermal_electron
    route_2 = JANAF_ARP_H0 + JANAF_ARP_DH_298_0 - JANAF_AR_DH_298_0
    assert route_1 == pytest.approx(route_2, abs=0.002)

    entered = entry.data.H298.value_si / 1000.0
    assert entered == pytest.approx(ENTERED_H298, abs=1e-6)
    assert entered == pytest.approx(route_1, abs=0.002)
    assert entered == pytest.approx(route_2, abs=0.002)

    # and it is NOT the electron-convention value, which is the mistake being avoided
    assert abs(entered - JANAF_ARP_H298_ELECTRON_CONVENTION) == pytest.approx(
        thermal_electron, abs=0.002)


def test_the_source_table_is_electron_convention_by_its_own_arithmetic():
    """Established from the table's numbers rather than from anybody's wording, because
    the two conventions' NAMES are inverted between sources and the arithmetic is not.

    The discriminator has to be the ENTHALPY. JANAF's own 298.15 K and 0 K
    enthalpies of formation differ by 6.205 kJ/mol, which is the electron's
    5/2 R T = 6.197 plus the 0.009 by which Ar+'s own enthalpy increment exceeds a bare
    monatomic gas's. Under the ion convention the same difference would be 0.009 alone.
    6.205 against 0.009 is not a close call.
    """
    difference = JANAF_ARP_H298_ELECTRON_CONVENTION - JANAF_ARP_H0
    assert difference == pytest.approx(6.205, abs=0.001)

    thermal_electron = 2.5 * R * T0 / 1000.0
    ion_own_increment = JANAF_ARP_DH_298_0 - JANAF_AR_DH_298_0
    assert ion_own_increment == pytest.approx(0.009, abs=0.001)
    # electron convention predicts the observed difference; ion convention does not
    assert difference == pytest.approx(thermal_electron + ion_own_increment, abs=0.002)
    assert abs(difference - ion_own_increment) > 6.0


def test_the_two_conventions_free_energies_coincide_near_room_temperature():
    """Why the free energy is NOT the discriminator, pinned so nobody tries to use it.

    Bartmess (J. Phys. Chem. 98 (1994) 6420, p. 6421) records Sharpe and Richardson's
    observation that at 297 K the electron's T*S numerically equals its H - H(0), so the
    two conventions give the same delta-G for an ionisation. That is a coincidence, not
    an identity, and it is also the reason the ion-convention value entered here gives
    an almost exactly right free energy of ionisation at room temperature: measured, RMG
    returns 1517.077 kJ/mol for Ar => Ar+ at 300 K against JANAF's own delta-f G(300) of
    1517.017 - 0.060 kJ/mol apart. The agreement decays away from 298 K, and that
    residue belongs to the electron's zero thermochemistry, not to this entry.
    """
    electron_convention = JANAF_ARP_H298_ELECTRON_CONVENTION - T0 * (
        JANAF_ARP_S298 + JANAF_ELECTRON_S298 - JANAF_AR_S298) / 1000.0
    ion_convention = ENTERED_H298 - T0 * (JANAF_ARP_S298 - JANAF_AR_S298) / 1000.0
    assert electron_convention == pytest.approx(JANAF_ARP_GF298, abs=0.002)
    assert ion_convention == pytest.approx(electron_convention, abs=0.1)


# =====================================================================================
# 2. The sourced values
# =====================================================================================

def test_the_entry_transcribes_the_janaf_table(entry):
    data = entry.data
    assert type(data).__name__ == 'ThermoData'
    assert data.S298.value_si == pytest.approx(JANAF_ARP_S298, abs=1e-6)
    assert data.get_heat_capacity(T0) == pytest.approx(JANAF_ARP_CP298, abs=1e-6)
    assert data.E0.value_si / 1000.0 == pytest.approx(ENTERED_E0, abs=1e-6)
    # the table stops at 6000 K and so does the entry
    assert data.Tmin.value_si == pytest.approx(T0, abs=1e-6)
    assert data.Tmax.value_si == pytest.approx(6000.0, abs=1e-6)


@pytest.mark.parametrize('T,janaf_s,janaf_dh', [
    (300.0, 166.533, 0.039),
    (500.0, 177.461, 4.325),
    (1000.0, 193.065, 15.606),
    (2000.0, 208.596, 37.960),
    (6000.0, 232.040, 122.994),
])
def test_the_entry_reproduces_the_janaf_columns_across_the_whole_range(entry, T,
                                                                      janaf_s,
                                                                      janaf_dh):
    """The 298.15 K point being right does not make the Cp grid right. This walks the
    table: entropy to 0.03 J/(mol*K) and the enthalpy increment to 0.04 kJ/mol at every
    decade from 300 K to the table's 6000 K ceiling. If the Cpdata grid is ever thinned
    or a value mistyped, this is what catches it."""
    assert entry.data.get_entropy(T) == pytest.approx(janaf_s, abs=0.03)
    increment = (entry.data.get_enthalpy(T) - entry.data.get_enthalpy(T0)) / 1000.0
    assert increment == pytest.approx(janaf_dh, abs=0.04)


def test_e0_reproduces_argons_ionisation_energy_from_an_unrelated_database(entry):
    """Corroboration, not a second measurement: JANAF's 0 K enthalpy of formation for
    Ar+ is argon's first ionisation energy, and NIST ASD measures that spectroscopically
    to eight figures. Agreement to 0.002 kJ/mol says the transcription is right."""
    assert entry.data.E0.value_si / 1000.0 == pytest.approx(IE_AR_EV * EV, abs=0.005)


def test_the_heat_capacity_is_not_five_halves_R_and_that_is_the_physics(entry):
    """Ar+ is 2P with a 2P(1/2) level 1431.6 cm^-1 above the 2P(3/2) ground level, so Cp
    carries a Schottky bump peaking near 1000 K. An entry with a flat monatomic Cp would
    be wrong by ~10% over 600-2000 K; this pins that the bump is present and where."""
    monatomic = 2.5 * R
    assert entry.data.get_heat_capacity(T0) > monatomic
    peak_T = max((300.0, 400.0, 600.0, 800.0, 1000.0, 1500.0, 2000.0, 4000.0, 6000.0),
                 key=entry.data.get_heat_capacity)
    assert peak_T == 1000.0
    assert entry.data.get_heat_capacity(1000.0) / monatomic == pytest.approx(1.096,
                                                                            abs=0.002)
    assert entry.data.get_heat_capacity(6000.0) == pytest.approx(monatomic, abs=0.2)


def test_the_entropy_is_the_neutrals_plus_the_electronic_degeneracy(entry):
    """S(Ar+) - S(Ar) is R ln 4 from the 2P(3/2) ground level's degeneracy, plus a small
    contribution from the 2P(1/2) level. Both are in the transcribed number; this is a
    check on the transcription that needs nothing but the two JANAF entropies."""
    difference = JANAF_ARP_S298 - JANAF_AR_S298
    assert difference == pytest.approx(R * math.log(4.0), abs=0.05)
    assert entry.data.S298.value_si - JANAF_AR_S298 == pytest.approx(difference,
                                                                    abs=1e-6)


def test_the_structure_is_the_gas_phase_ground_state(entry):
    molecule = entry.item
    assert len(molecule.atoms) == 1
    atom = molecule.atoms[0]
    assert atom.element.symbol == 'Ar'
    assert molecule.get_net_charge() == 1
    assert atom.radical_electrons == 1        # 3s2 3p5
    assert atom.lone_pairs == 3
    assert molecule.multiplicity == 2


def test_the_smiles_round_trip_still_corrupts_this_species(entry):
    """Recorded by ``docs/i120-argon-recombination.md`` and re-pinned here because this
    entry is the first thing in the database that would be silently mismatched by it:
    ``Ar+`` exports to ``[Ar+]``, which reads back as Ar2+. Adjacency lists are the only
    safe interchange form. If RMG-Py ever fixes this, the test fails and the warning in
    the library's longDesc can be retired."""
    smiles = entry.item.to_smiles()
    assert Molecule().from_smiles(smiles).get_net_charge() == 2


def test_no_argon_dimer_cation_was_entered(thermo_db):
    """Ar2+ was looked for and not entered: the tabulated functions exist (Maltsev,
    Morozov & Osina, High Temperature 57 (2019) 37-40) but the paper is closed access
    and ATcT returns HTTP 403, so entering one would mean authoring it. If a defensible
    source is ever reached, this test is the place that says so."""
    for library in thermo_db.libraries.values():
        for e in library.entries.values():
            if e.item is None:
                continue
            symbols = [a.element.symbol for a in e.item.atoms]
            if symbols.count('Ar') > 1:
                pytest.fail(f'unexpected multi-argon entry {e.label!r}')


# =====================================================================================
# 3. The whole path
# =====================================================================================

def test_the_library_loads_alongside_every_other_thermo_library(thermo_db):
    on_disk = [f for f in os.listdir(LIBRARY_DIR) if f.endswith('.py')]
    assert len(thermo_db.libraries) == len(on_disk)
    assert LIBRARY in thermo_db.libraries
    assert list(thermo_db.libraries[LIBRARY].entries) == ['[Arp]']


def test_the_species_resolves_to_this_library(thermo_db):
    data = thermo_db.get_thermo_data(_species(ARP, 'Ar+'))
    assert LIBRARY in data.comment
    # get_thermo_data round-trips through Wilhoit, which moves H298 by ~3 J/mol for
    # every species it returns; 0.01 kJ/mol is that artefact, not a data tolerance.
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(ENTERED_H298, abs=0.01)


def test_without_this_library_the_species_is_refused(estimator_only):
    """What the state of the world was before this branch, measured rather than
    remembered: no estimator in this database covers a monatomic argon cation."""
    with pytest.raises(Exception):
        estimator_only.get_thermo_data(_species(ARP, 'Ar+'))


@pytest.mark.parametrize('T', [300.0, 500.0, 1000.0, 2000.0, 6000.0])
def test_an_equilibrium_constant_involving_the_cation_is_finite(thermo_db, T):
    ar, arp = _species(AR, 'Ar'), _species(ARP, 'Ar+')
    for s in (ar, arp):
        s.thermo = thermo_db.get_thermo_data(s)
    reaction = Reaction(reactants=[ar], products=[arp], electrons=+1, reversible=False)
    assert reaction.is_balanced()
    Kc = reaction.get_equilibrium_constant(T)
    assert math.isfinite(Kc) and Kc > 0.0
    dG = reaction.get_free_energy_of_reaction(T) / 1000.0
    assert 1200.0 < dG < 1600.0          # of order the ionisation energy, as it must be


def test_the_runtime_refuses_to_reverse_that_equilibrium(thermo_db):
    """The Keq above is finite and it is NOT licence to build a reverse rate from it.
    The electron is priced at zero in that sum, so Keq describes a different reaction
    than the one being reversed, and RMG-Py says so by name. Pinned so a green
    'the equilibrium constant computes' is never read as more than it is."""
    ar, arp = _species(AR, 'Ar'), _species(ARP, 'Ar+')
    for s in (ar, arp):
        s.thermo = thermo_db.get_thermo_data(s)
    reaction = Reaction(reactants=[ar], products=[arp], electrons=+1, reversible=True)
    refusal = reaction.get_reverse_from_equilibrium_refusal()
    assert refusal is not None
    assert 'omits the electron entirely' in refusal


@pytest.fixture(scope='module')
def argon_ionisation(pinned):
    """The reaction this ticket unblocks, built in a SCRATCH copy of the shipped
    ionisation library under a temporary directory.

    Adding an argon rate to this database is an explicit non-goal of the ticket, and it
    is a different owner's call besides. What is demonstrated here is that the
    thermochemistry wall - the reason that library's own header gives for carrying one
    entry - is gone. The scratch library keeps the shipped library's NAME because
    ``FAMILY_ELECTRON_PLACEMENT`` is keyed on the label; nothing is written into the
    repository.
    """
    tmp = tempfile.mkdtemp(prefix='i127-scratch-kinetics-')
    try:
        libraries = os.path.join(tmp, 'libraries')
        os.makedirs(libraries)
        shutil.copytree(os.path.join(KINETICS_LIBRARY_DIR, IONISATION),
                        os.path.join(libraries, IONISATION))
        with open(os.path.join(libraries, IONISATION, 'dictionary.txt'), 'a') as fh:
            fh.write('\n[Ar]\n' + AR + '\n[Arp]\n' + ARP)
        with open(os.path.join(libraries, IONISATION, 'reactions.py'), 'a') as fh:
            fh.write('\nentry(\n'
                     '    index = 900,\n'
                     '    label = "[Ar] => [Arp]",\n'
                     '    degeneracy = 1,\n'
                     '    reversible = False,\n'
                     '    kinetics = VoronovEIArrhenius(Z=18, N=18),\n'
                     '    shortDesc = u"scratch only",\n'
                     ')\n')
        db = KineticsDatabase()
        db.load_libraries(libraries, libraries=[IONISATION])
        reactions = db.libraries[IONISATION].get_library_reactions()
        argon = [r for r in reactions
                 if any(a.element.symbol == 'Ar'
                        for a in r.reactants[0].molecule[0].atoms)]
        assert len(argon) == 1
        yield argon[0]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_the_argon_ionisation_reaction_loads_and_balances(argon_ionisation):
    assert type(argon_ionisation.kinetics).__name__ == 'VoronovEIArrhenius'
    assert argon_ionisation.electrons == +1
    assert argon_ionisation.is_balanced()


def test_the_argon_ionisation_reaction_resolves_its_electrons(argon_ionisation):
    registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
    assert registry.get(argon_ionisation.family) == (1, 2)
    electron = _species(ELECTRON, 'e-')
    view = electron_placement.resolve_electron_placement(
        argon_ionisation,
        list(argon_ionisation.reactants) + list(argon_ionisation.products) + [electron])
    assert sum(1 for s in view.reactants if s.is_electron()) == 1
    assert sum(1 for s in view.products if s.is_electron()) == 2
    assert len(argon_ionisation.reactants) == 1       # canonical form not mutated


def test_the_plasma_reactor_accepts_the_argon_ionisation_reaction(thermo_db,
                                                                  argon_ionisation):
    from rmgpy.solver.plasma import PlasmaReactor

    ar = argon_ionisation.reactants[0]
    arp = argon_ionisation.products[0]
    electron = _species(ELECTRON, 'e-')
    for s in (ar, arp, electron):
        s.thermo = thermo_db.get_thermo_data(s)
    assert LIBRARY in arp.thermo.comment

    Te = 23209.0            # 2 eV, inside the Voronov argon fit's 1 eV - 20 keV range
    reactor = PlasmaReactor(T=(1000, 'K'), P=(1, 'bar'), Te=(Te, 'K'),
                            initial_mole_fractions={ar: 1.0, arp: 1e-12,
                                                    electron: 1e-12},
                            termination=[])
    reactor.initialize_model(core_species=[ar, arp, electron],
                             core_reactions=[argon_ionisation],
                             edge_species=[], edge_reactions=[])
    assert len(reactor.kf) == 1
    expected = argon_ionisation.kinetics.get_rate_coefficient_electron_temp(Te)
    assert reactor.kf[0] == pytest.approx(expected, rel=1e-9)
    assert reactor.kf[0] > 0.0


# =====================================================================================
# 4. Coverage, and the two defects found while measuring it
# =====================================================================================

def test_the_only_gas_phase_cations_in_this_database_are_these_three(thermo_db):
    """The coverage audit's headline, as a set rather than a count. Four distinct
    charged species exist in the whole database; two of them - ``proton`` and
    ``Li_ion`` - are electrochemical reference species with H298 = 0 by construction and
    are not gas-phase thermochemistry at all."""
    cations = {}
    for name, library in thermo_db.libraries.items():
        for label, e in library.entries.items():
            if e.item is None or e.item.get_net_charge() <= 0:
                continue
            cations.setdefault(label, set()).add(name)
    assert set(cations) == {'proton', 'H3O', 'Li_ion', '[Lip]', '[Arp]'}, sorted(cations)
    assert cations['[Arp]'] == {LIBRARY}

    # the two electrochemical ones are zero by construction, not by measurement
    for label, expected_libraries in (('proton', {'electrocatThermo',
                                                  'electrocatLiThermo'}),
                                      ('Li_ion', {'computationalLithiumElectrode'})):
        assert cations[label] == expected_libraries
        for name in expected_libraries:
            data = thermo_db.libraries[name].entries[label].data
            assert abs(data.get_enthalpy(T0)) < 10.0      # J/mol


def test_no_element_in_either_shipped_table_has_thermochemistry_above_charge_one(
        thermo_db):
    """The one clean arithmetic statement in the coverage audit. Both rate tables drive
    342 charge-stage transitions; thermochemistry exists for the +1 cation of two
    elements and for nothing at all above +1."""
    for library in thermo_db.libraries.values():
        for e in library.entries.values():
            if e.item is not None:
                assert e.item.get_net_charge() <= 1, e.label


def test_the_shipped_lithium_cation_disagrees_with_lithiums_ionisation_energy(
        thermo_db):
    """A defect found, pinned, and deliberately NOT fixed - modifying existing
    thermochemistry is a non-goal of this ticket.

    ``[Lip]`` minus ``[Li]`` in LithiumPrimaryThermo is 375.36 kJ/mol where lithium's
    ionisation energy is 520.22. The gap is 144.86 kJ/mol, which is 23x the entire
    6.197 kJ/mol difference between the two electron conventions - so it cannot be a
    convention choice, and that entry cannot be used to read this database's convention
    off. If it is ever corrected, this test fails and points at the report.
    """
    library = thermo_db.libraries['LithiumPrimaryThermo']
    neutral = library.entries['[Li]'].data
    cation = library.entries['[Lip]'].data

    rise = (cation.get_enthalpy(T0) - neutral.get_enthalpy(T0)) / 1000.0
    assert rise == pytest.approx(375.363, abs=0.01)

    expected = IE_LI_EV * EV
    assert expected == pytest.approx(520.221, abs=0.01)
    discrepancy = rise - expected
    assert discrepancy == pytest.approx(-144.858, abs=0.01)
    assert abs(discrepancy) > 20 * (2.5 * R * T0 / 1000.0)

    # the ENTROPY of the same pair is right, which is what makes the enthalpy a defect
    # rather than a different reference state: S(Li+) is S(Li) minus R ln 2 exactly.
    s_gap = neutral.get_entropy(T0) - cation.get_entropy(T0)
    assert s_gap == pytest.approx(R * math.log(2.0), abs=0.002)


@pytest.mark.parametrize('symbol,cation,neutral,ie_ev', [
    ('N', 'multiplicity 3\n1 N u2 p1 c+1\n', 'multiplicity 4\n1 N u3 p1 c0\n', 14.53413),
    ('O', 'multiplicity 4\n1 O u3 p1 c+1\n', 'multiplicity 3\n1 O u2 p2 c0\n', 13.618055),
    ('Si', 'multiplicity 2\n1 Si u1 p1 c+1\n', 'multiplicity 3\n1 Si u2 p1 c0\n', 8.15168),
])
def test_group_additivity_answers_for_monatomic_cations_and_the_answer_is_wrong(
        estimator_only, symbol, cation, neutral, ie_ev):
    """The second defect, and the reason a library entry is the only honest way to give
    a cation thermochemistry here.

    Asked for a monatomic cation, group additivity does not refuse. It saturates the ion
    into a neutral-valence group descriptor - N+ is matched to ``group(N3s-CsCsCs)``, a
    trisubstituted amine - and returns a number. The number must exceed the neutral's by
    at least the element's ionisation energy. It does not; for N and Si it is *lower*
    than the neutral, so even the sign of ionisation is wrong.

    This is why the gap is a generation consequence rather than a list: nothing in this
    database can produce a charged species' thermochemistry except a library entry
    somebody wrote by hand.
    """
    got = estimator_only.get_thermo_data(_species(cation)).get_enthalpy(T0) / 1000.0
    base = estimator_only.get_thermo_data(_species(neutral)).get_enthalpy(T0) / 1000.0
    rise = got - base
    ionisation_energy = ie_ev * EV
    assert rise < ionisation_energy - 500.0, (
        f'{symbol}+ estimated {rise:+.1f} kJ/mol above {symbol}, '
        f'IE is {ionisation_energy:.1f} kJ/mol')


@pytest.mark.parametrize('symbol,adjacency_list', [
    ('He', 'multiplicity 2\n1 He u1 p0 c+1\n'),
    ('Ne', 'multiplicity 2\n1 Ne u1 p3 c+1\n'),
])
def test_the_other_noble_gas_cations_are_still_refused(estimator_only, symbol,
                                                       adjacency_list):
    """The noble gases are the one place group additivity fails loudly instead of
    quietly, because no thermo group covers them. Ar+ was in this set until this branch;
    He+ and Ne+ still are, and each needs its own sourced entry."""
    with pytest.raises(Exception):
        estimator_only.get_thermo_data(_species(adjacency_list))


@pytest.mark.parametrize('symbol,adjacency_list,error', [
    ('C', 'multiplicity 2\n1 C u1 p1 c+1\n', 'AtomTypeError'),
    ('F', 'multiplicity 3\n1 F u2 p2 c+1\n', 'AtomTypeError'),
    ('Na', '1 Na u0 p0 c+1\n', 'KeyError'),
    ('Mg', 'multiplicity 2\n1 Mg u1 p0 c+1\n', 'KeyError'),
    ('Al', '1 Al u0 p1 c+1\n', 'KeyError'),
    ('K', '1 K u0 p0 c+1\n', 'KeyError'),
    ('Ca', 'multiplicity 2\n1 Ca u1 p0 c+1\n', 'KeyError'),
])
def test_the_gate_before_thermochemistry_is_the_atom_type(symbol, adjacency_list, error):
    """Six of the thirteen elements ``voronov.yaml`` can ionise - C, Na, Mg, Al, K, Ca -
    cannot have thermochemistry at all, for a reason that has nothing to do with data
    and two more (F, Cl) join them on the recombination side: RMG has no
    atom type that admits the element at charge +1, so the cation cannot be constructed
    for an entry to attach to. That gate lives in ``rmgpy/molecule/atomtype.py``, i.e.
    in RMG-Py, and is what makes this gap a generation consequence."""
    with pytest.raises(Exception) as excinfo:
        Molecule().from_adjacency_list(adjacency_list)
    assert type(excinfo.value).__name__ == error


def test_argon_is_representable_only_because_its_atom_type_is_unconstrained():
    """And the corollary, which is uncomfortable and belongs on the record: argon's atom
    type declares no charge constraint at all, so RMG accepts Ar at any charge including
    arrangements no free ion has. Ar+ builds for the same reason Ar(4+) does. The entry
    added by this branch is the ground state and matches only the ground state."""
    from rmgpy.molecule.atomtype import ATOMTYPES

    ground = Molecule().from_adjacency_list(ARP)
    assert not ATOMTYPES['Ar'].charge
    assert ground.atoms[0].atomtype.label == 'Ar'

    # a nonsense argon cation parses just as readily, and is NOT this entry's species
    nonsense = Molecule().from_adjacency_list('multiplicity 5\n1 Ar u4 p0 c+4\n')
    assert nonsense.get_net_charge() == 4
    assert not ground.is_isomorphic(nonsense)


# =====================================================================================
# Negative control
# =====================================================================================

@pytest.mark.parametrize('label,adjacency_list,h298,s298,library', [
    ('Li', LI, 157.5723, 138.6620, 'LithiumPrimaryThermo'),
    ('Li+', LIP, 532.9358, 132.8988, 'LithiumPrimaryThermo'),
])
def test_the_lithium_channel_species_are_untouched(thermo_db, label, adjacency_list,
                                                   h298, s298, library):
    data = thermo_db.get_thermo_data(_species(adjacency_list, label))
    assert library in data.comment
    assert data.get_enthalpy(T0) / 1000.0 == pytest.approx(h298, abs=0.01)
    assert data.get_entropy(T0) == pytest.approx(s298, abs=0.02)


def test_neutral_argon_is_untouched(thermo_db):
    data = thermo_db.get_thermo_data(_species(AR, 'Ar'))
    assert LIBRARY not in data.comment
    assert abs(data.get_enthalpy(T0)) < 10.0          # J/mol; argon is a reference state
    assert data.get_entropy(T0) == pytest.approx(154.735, abs=0.2)
