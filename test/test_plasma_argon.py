#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``PlasmaArgon`` kinetics library (I-193).

``PlasmaArgon`` exists so a pure-argon deck need not load the whole ``PlasmaAir`` air
library (33 species, 88 reactions) to reach the one argon reaction the database holds.
The library is DELIBERATELY one entry: electron-impact ionisation of neutral argon,
``Ar + e- => Arp + e- + e-``, the entry carried verbatim from ``PlasmaAir`` index 86.

These tests pin the invariants the ticket turns on:

1. **exactly one entry** - the library is small and stays small. If a later hand adds a
   radiative-recombination row, an Ar2+ row, a three-body row, or any estimated rate, the
   count changes and this fails. That is the point: an incomplete library we can name is
   the deliverable; a complete-looking one is a failure.
2. **it is the Golyatina2021 cross-section entry, not the superseded LXCat one** -
   ``PlasmaAir`` carries two datasets for this reaction (the active Golyatina2021 51-point
   grid at threshold 15.76 eV, and a commented-out coarser LXCat/Phelps 29-point grid at
   15.8 eV). Only the finer active grid is carried here; this pins the choice.
3. **it loads and balances** - ``ElectronCollisionPlasma`` writes the electron explicitly
   on both sides, and the runtime's E-pseudo-element census (which skips the free electron
   and checks net charge) closes -1 == -1.

The suite is silent on radiative recombination on purpose: that channel does NOT belong
here (see ``docs/i120-argon-recombination.md`` on branch ``i120-argon-recombination`` and
``PlasmaRadiativeRecombination``'s own longDesc), and "exactly one entry" is the assertion
that keeps it out.
"""

import os

import pytest

from rmgpy import settings

LIBRARY = 'PlasmaArgon'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

# Pin before anything imports a database-reading module (see test/conftest.py for why).
settings['database.directory'] = THIS_DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.kinetics.arrhenius import ElectronCollisionPlasma  # noqa: E402


@pytest.fixture(scope='module')
def library():
    """The loaded library. Load failures surface here, not inside a test."""
    assert settings['database.directory'] == THIS_DATABASE, (
        'RMG resolved database.directory to {0!r}, not this worktree ({1!r}).'.format(
            settings['database.directory'], THIS_DATABASE))
    db = KineticsDatabase()
    db.load_libraries(os.path.join(settings['database.directory'], 'kinetics', 'libraries'),
                      libraries=[LIBRARY])
    return db.libraries[LIBRARY]


@pytest.fixture
def reaction(library):
    """A fresh ``LibraryReaction`` per test, so mutation cannot leak between them."""
    reactions = library.get_library_reactions()
    assert len(reactions) == 1
    return reactions[0]


def test_library_loads_with_exactly_one_entry(library):
    """Small library, and it stays small: any second entry fails here."""
    assert library.label == LIBRARY
    assert len(library.entries) == 1


def test_the_one_entry_is_argon_electron_impact_ionisation(reaction):
    """``Ar + e- => Arp + e- + e-``: one argon in, one argon cation out, a net electron."""
    assert [s.label for s in reaction.reactants] == ['Ar', 'e-']
    assert sorted(s.label for s in reaction.products) == ['Arp', 'e-', 'e-']
    # neutral argon in, +1 argon cation out
    ar = next(s for s in reaction.reactants if s.label == 'Ar')
    arp = next(s for s in reaction.products if s.label == 'Arp')
    assert ar.molecule[0].get_net_charge() == 0
    assert arp.molecule[0].get_net_charge() == +1


def test_the_kinetics_are_a_cross_section_table_not_a_fitted_rate(reaction):
    """``ElectronCollisionPlasma`` integrates sigma(E) against a Maxwellian EEDF at Te.

    The rate law being a tabulated cross section (not an Arrhenius/Badnell/Voronov fit) is
    what makes copying verbatim rather than re-deriving the correct move: RMG has no LXCat
    parser, so the table only ever enters by being hand-written.
    """
    assert isinstance(reaction.kinetics, ElectronCollisionPlasma)


def test_it_is_the_golyatina_grid_not_the_superseded_lxcat_grid(reaction):
    """The active Golyatina2021 51-point grid at threshold 15.76 eV, not LXCat's 29 at 15.8.

    ``PlasmaAir`` carries both datasets for this reaction; only the finer, active one is
    here. LXCat's grid has 29 points and starts its non-zero cross section at 15.8 eV;
    Golyatina's has 51 and starts at 15.76 eV. This distinguishes them unambiguously.
    """
    # ElectronCollisionPlasma stores the energy grid in SI molar units (J/mol); one
    # eV/molecule is N_A * e = 96485.33 J/mol.
    ev_per_molecule = 6.02214076e23 * 1.602176634e-19  # J/mol per eV
    energies_eV = reaction.kinetics.energies.value_si / ev_per_molecule
    assert len(energies_eV) == 51
    assert energies_eV[0] == pytest.approx(15.76, abs=1e-2)
    assert energies_eV[-1] == pytest.approx(10000.0, abs=1.0)


def test_the_entry_is_one_way(reaction):
    """Ionisation is authored one-way; nothing is entered as anything's reverse."""
    assert reaction.reversible is False


def test_the_reaction_balances_in_charge(reaction):
    """The explicit electrons balance: net charge -1 on both sides.

    ``ElectronCollisionPlasma`` declares no ``electrons`` field, so ``reaction.electrons``
    stays 0; balance is carried by the census skipping the free electron and comparing net
    charge (the runtime's E-pseudo-element fix).
    """
    assert reaction.is_balanced()
