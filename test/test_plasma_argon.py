#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``PlasmaArgon`` kinetics library (I-193).

``PlasmaArgon`` exists so a pure-argon deck need not load the whole ``PlasmaAir`` air
library (33 species, 88 reactions) to reach the one argon reaction the database holds.
The library was DELIBERATELY one entry: electron-impact ionisation of neutral argon,
``Ar + e- => Arp + e- + e-``, the entry carried verbatim from ``PlasmaAir`` index 86.
I-232 appended three metastable-argon channels; this file still pins the first.

These tests pin the invariants the ticket turns on:

1. **exactly the named entries** - the library is small and stays small. I-232 added the
   four metastable-argon channels (stepwise ionisation, quenching, pooling, and
   metastable-to-resonance mixing; pinned in ``test_plasma_argon_metastable_channels.py``), so
   the count is five. If a later hand adds
   a radiative-recombination row, an Ar2+ row, a three-body row, or any estimated rate, the
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
``PlasmaRadiativeRecombination``'s own longDesc), and the exact entry set is the assertion
that keeps it out.
"""

import os
import types

import pytest

from rmgpy import settings

LIBRARY = 'PlasmaArgon'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

# Pin before anything imports a database-reading module (see test/conftest.py for why).
settings['database.directory'] = THIS_DATABASE

from plasma_library_selection import (  # noqa: E402
    assert_reactions_uniquely_keyed, reaction_for_isolated, reaction_key)
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
    """A fresh ``LibraryReaction`` per test, so mutation cannot leak between them.

    Selected by the channel it is *about* -- reactants and products -- never by position
    and never by reactants alone; ``plasma_library_selection`` carries the full argument
    for that key and the two rounds of defect behind it. The library's smallness is still
    pinned, once, in ``test_library_loads_with_exactly_the_named_entries`` below, where it is a
    claim rather than a precondition, and the key's uniqueness in
    ``test_every_reaction_is_distinguishable_from_every_other``.
    """
    return reaction_for_isolated(library, ['Ar', 'e-'], ['Arp', 'e-', 'e-'])


def test_library_loads_with_exactly_the_named_entries(library):
    """Small library, and it stays small: any unnamed entry fails here.

    The count is the deliberate claim of this file's opening docstring -- an incomplete
    library we can name is the deliverable -- so it is asserted here, where growth produces
    a *failure* someone has to answer, rather than inside a fixture where it would produce
    a setup error nobody sees. The coverage set is pinned alongside it, because a bare count
    is satisfied by any second entry, including a wrong one that replaced this one.
    """
    assert library.label == LIBRARY
    assert len(library.entries) == 5
    assert {reaction_key(r) for r in library.get_library_reactions()} == {
        (('Ar', 'e-'), ('Arp', 'e-', 'e-')),
        (('Ars', 'e-'), ('Arp', 'e-', 'e-')),
        (('Ars', 'e-'), ('Ar', 'e-')),
        (('Ars', 'Ars'), ('Ar', 'Arp', 'e-')),
    }


def test_every_reaction_is_distinguishable_from_every_other(library):
    """No two reactions here share both reactants and products, bar one named pair.

    The exception is ``Ars + e- => Ar + e-``: quenching (89) and metastable-to-resonance
    mixing (91) are kept as two entries by instruction, so a deck can drop 91 on its own. No
    key drawn from the reaction can separate them (``plasma_library_selection`` says why), so
    the exception is pinned exactly: that key, two reactions, both flagged ``duplicate``, and
    no other collision. The rest of the library is checked by the shared assertion.

    This is what makes the ``reaction`` fixture safe. If it ever stops holding, it stops
    holding HERE -- as a failure, in a test whose name says what broke -- instead of
    turning every other test in this file into a setup error that asserts nothing and is
    reported in a section people skim past. The property is cheap and the alternative has
    now cost this campaign two rounds.
    """
    quenching = (('Ars', 'e-'), ('Ar', 'e-'))
    pair = [r for r in library.get_library_reactions() if reaction_key(r) == quenching]
    assert len(pair) == 2 and all(r.duplicate for r in pair)
    assert sorted(r.kinetics.A.value_si / 6.02214076e23 for r in pair) == \
        pytest.approx([4.3e-16, 2.0e-13])
    others = [r for r in library.get_library_reactions() if reaction_key(r) != quenching]
    assert len(others) == 3
    assert_reactions_uniquely_keyed(types.SimpleNamespace(
        label=library.label, get_library_reactions=lambda: others))


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
