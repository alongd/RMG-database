#!/usr/bin/env python
# encoding: utf-8

"""
Build-time resolution tests for the argon cation, added under I-179 fork C.

The report is ``docs/i127-argon-cation-thermo.md`` (I-127) plus the I-179 fork-C
verification. ``test_argon_cation_thermo.py`` already proves the *values* transcribe
NIST-JANAF Ar-002 and that a **direct** ``get_thermo_data`` query over *all* libraries
returns the entry. This file closes the gap that direct query leaves open and that I-179
was asked to nail down: **does the library actually win over group additivity at
model-build time, when only the deck's own ``thermoLibraries`` are loaded** - not when
every library in the tree happens to be present?

``get_thermo_data`` is the exact method RMG's model builder calls, so the only thing that
separates "direct query" from "build time" is *which* libraries are loaded, in what order.
At build time that set is the input file's ``thermoLibraries`` list and nothing else. The
canonical plasma deck is ``RMG-Py/docs/i123-integration/input.py`` (named in this library's
own ``longDesc``); its list is transcribed below. It does **not** include
``PlasmaCationThermo`` - so as that deck stands, ``Ar+`` misses every loaded library and
is refused at the thermochemistry wall. That is a critical-path finding, not a bug in the
entry: the entry is correct, and an argon-capable deck must add the library to its
``thermoLibraries``. Both halves are pinned here so neither can regress silently:

  * with the library in the loaded set, the library wins and the value is the entered one;
  * with the current reference deck's set, ``Ar+`` is refused with a LOUD ``DatabaseError``
    rather than handed a silently fabricated group-additivity number.

The last two tests put on the record which of the two species both written "Ar2+" raises
the loud failure: the dication ``Ar(2+)`` (monatomic, +2) and the dimer ``Ar2(+)``
(diatomic, +1) each build and each raise ``DatabaseError`` - neither is silently
fabricated. "Loud failure, not silent fabrication" is the distinction this campaign cares
about.

Run with the runtime pinned::

    cd /home/alon/Code/RMG-database-i179-argon-thermo
    PYTHONPATH=/home/alon/Code/RMG-Py-i172-balance \\
        python -m pytest test/test_argon_cation_buildtime.py -q

``test/conftest.py`` pins ``database.directory`` to this worktree before collection.
"""

import os

import pytest

from rmgpy import settings
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.exceptions import DatabaseError
from rmgpy.molecule import Molecule
from rmgpy.species import Species

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))
LIBRARY_DIR = os.path.join(THIS_DATABASE, 'thermo', 'libraries')
GROUP_DIR = os.path.join(THIS_DATABASE, 'thermo', 'groups')

LIBRARY = 'PlasmaCationThermo'
ENTERED_H298 = 1520.581  # kJ/mol, ion convention

#: The plasma deck's ``thermoLibraries``, transcribed verbatim from
#: ``RMG-Py/docs/i123-integration/input.py`` (the deck named in PlasmaCationThermo's
#: longDesc). Note what is NOT in it: ``PlasmaCationThermo``. That omission is the finding.
REFERENCE_DECK_THERMO_LIBRARIES = [
    'LithiumPrimaryThermo',
    'LithiumAdditionalThermo',
    'primaryThermoLibrary',
    'electrocatThermo',
]
#: What an argon-capable deck must load: the reference deck plus this library.
ARGON_CAPABLE_DECK = REFERENCE_DECK_THERMO_LIBRARIES + [LIBRARY]

ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'                  # Ar+  monatomic +1, the entry
DICATION = 'multiplicity 3\n1 Ar u2 p2 c+2\n'             # Ar(2+) monatomic +2, ground 3P
DIMER = ('multiplicity 2\n'                               # Ar2(+) diatomic +1
         '1 Ar u0 p3 c+1 {2,S}\n'
         '2 Ar u1 p3 c0 {1,S}\n')


def _species(adjacency_list, label=''):
    """A species built as RMG builds one at model time: with resonance structures."""
    s = Species(label=label, molecule=[Molecule().from_adjacency_list(adjacency_list)])
    s.generate_resonance_structures()
    return s


def _db_with(libraries):
    """A ThermoDatabase loaded with exactly ``libraries`` (ordered) and the groups, i.e.
    the state RMG is in at build time for a deck whose ``thermoLibraries`` is that list."""
    db = ThermoDatabase()
    db.load_groups(GROUP_DIR)
    db.load_libraries(LIBRARY_DIR, libraries=libraries)
    db.library_order = list(libraries)
    return db


@pytest.fixture(scope='module')
def pinned():
    assert settings['database.directory'] == THIS_DATABASE, (
        f"database.directory is {settings['database.directory']!r}, not this worktree")
    return THIS_DATABASE


@pytest.fixture(scope='module')
def argon_capable_db(pinned):
    return _db_with(ARGON_CAPABLE_DECK)


@pytest.fixture(scope='module')
def reference_deck_db(pinned):
    return _db_with(REFERENCE_DECK_THERMO_LIBRARIES)


def test_the_reference_deck_does_not_load_this_library():
    """The premise of the finding, pinned so it is visible if the deck ever changes:
    the canonical plasma deck's thermoLibraries omits PlasmaCationThermo."""
    assert LIBRARY not in REFERENCE_DECK_THERMO_LIBRARIES


def test_at_build_time_with_the_library_loaded_it_wins_over_group_additivity(argon_capable_db):
    """With PlasmaCationThermo among the loaded libraries, get_thermo_data - the method
    RMG's model builder calls - returns the library entry, not a group-additivity estimate."""
    data = argon_capable_db.get_thermo_data(_species(ARP, 'Ar+'))
    assert LIBRARY in data.comment, f"resolved from {data.comment!r}, not the library"
    # get_thermo_data round-trips through Wilhoit, which moves H298 by ~3 J/mol; the entered
    # value is asserted verbatim in test_argon_cation_thermo.py.
    got = data.get_enthalpy(298.15) / 1000.0
    assert abs(got - ENTERED_H298) < 0.01, f"H298 {got} kJ/mol, expected ~{ENTERED_H298}"


def test_at_build_time_with_the_reference_deck_argon_is_refused_loudly(reference_deck_db):
    """With the current reference deck's libraries (no PlasmaCationThermo), Ar+ misses
    every library AND group additivity fails loudly for the noble-gas cation: a
    DatabaseError, never a silently fabricated number. This is why an argon-capable deck
    must add the library."""
    with pytest.raises(DatabaseError):
        reference_deck_db.get_thermo_data(_species(ARP, 'Ar+'))


def test_the_dication_builds_and_raises_the_loud_databaseerror(argon_capable_db):
    """The dication Ar(2+) (monatomic, +2) is the "Ar2+" reading that builds yet raises the
    loud DatabaseError - group additivity has no group for a charge-+2 argon atom."""
    species = _species(DICATION, 'Ar2+')
    assert species.molecule[0].get_net_charge() == 2
    with pytest.raises(DatabaseError) as exc:
        argon_capable_db.get_thermo_data(species)
    assert 'Ar++' in str(exc.value)


def test_the_dimer_cation_builds_and_raises_the_loud_databaseerror(argon_capable_db):
    """The dimer Ar2(+) (diatomic, +1) also builds and also raises a loud DatabaseError,
    via HBI saturation rather than a bare atom type - still loud, still not fabricated."""
    species = _species(DIMER, 'Ar2+dimer')
    assert species.molecule[0].get_net_charge() == 1
    with pytest.raises(DatabaseError):
        argon_capable_db.get_thermo_data(species)
