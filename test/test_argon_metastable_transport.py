#!/usr/bin/env python
# encoding: utf-8
"""
Unit tests for the metastable-argon ``Ar(3P2)`` entry in ``PrimaryTransportLibrary`` (I-268).

Without a library hit, ``TransportDatabase.get_transport_properties`` falls back to group
additivity, which saturates the ``u2`` biradical to ``ArH2``; no atom type exists for it, so
the Chemkin export (``render_transport_file``) aborts. The entry exists to stop the lookup
before group estimation runs. These tests pin that it does, that it is the same species as
the thermo entry, and - as the negative control - that removing it brings the failure back.

Run with the runtime pinned::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python -m pytest \\
        test/test_argon_metastable_transport.py -q

``test/conftest.py`` pins ``database.directory`` to this worktree before collection.
"""

import os

import pytest

from rmgpy.data.thermo import ThermoDatabase
from rmgpy.data.transport import TransportDatabase
from rmgpy.exceptions import AtomTypeError
from rmgpy.molecule import Molecule
from rmgpy.species import Species

try:
    from rmgpy.exceptions import SaturatedStructureError
except ImportError:                     # an engine older than the round-80 saturation fix
    SaturatedStructureError = None

NO_NUMBER = ((AtomTypeError, SaturatedStructureError) if SaturatedStructureError is not None
             else (AtomTypeError,))

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))
TRANSPORT_DIR = os.path.join(THIS_DATABASE, 'transport')
LIBRARY = 'PrimaryTransportLibrary'
LABEL = 'Ar(3P2)'

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'


def _species(adjacency_list):
    return Species(molecule=[Molecule().from_adjacency_list(adjacency_list)])


def _transport_database(libraries=None):
    database = TransportDatabase()
    database.load(TRANSPORT_DIR, libraries=libraries)
    return database


@pytest.fixture(scope='module')
def all_libraries():
    """Every transport library, which is what a deck that names none loads."""
    return _transport_database()


def test_metastable_resolves_to_the_library_entry(all_libraries):
    transport, _, entry = all_libraries.get_transport_properties(_species(AR_META))
    assert transport.comment == LIBRARY
    assert entry.label == LABEL
    assert transport.shapeIndex == 0
    assert transport.epsilon.value_si == pytest.approx(1134.93)            # 136.5 K * R
    assert transport.sigma.value_si == pytest.approx(3.33e-10)
    assert transport.dipoleMoment.value_si == 0
    assert transport.polarizability.value_si == pytest.approx(1.64e-30)
    assert transport.rotrelaxcollnum == 0


def test_metastable_resolves_when_only_this_library_is_loaded():
    transport, _, entry = _transport_database([LIBRARY]).get_transport_properties(
        _species(AR_META))
    assert transport.comment == LIBRARY
    assert entry.label == LABEL


def test_without_the_entry_the_lookup_still_fails():
    """Negative control: every other library loaded, and the group estimate refuses."""
    others = [os.path.splitext(f)[0] for f in os.listdir(os.path.join(TRANSPORT_DIR, 'libraries'))
              if f.endswith('.py') and f != LIBRARY + '.py']
    with pytest.raises(NO_NUMBER):
        _transport_database(others).get_transport_properties(_species(AR_META))


def test_entry_is_the_thermo_library_species():
    thermo_database = ThermoDatabase()
    thermo_database.load_libraries(os.path.join(THIS_DATABASE, 'thermo', 'libraries'),
                                   ['PlasmaExcitedNeutralThermo'])
    thermo = thermo_database.libraries['PlasmaExcitedNeutralThermo']
    transport = _transport_database([LIBRARY]).libraries[LIBRARY]
    assert transport.entries[LABEL].item.is_isomorphic(thermo.entries[LABEL].item)


def test_ground_state_argon_does_not_match_the_metastable(all_libraries):
    transport, _, entry = all_libraries.get_transport_properties(_species(AR))
    assert entry.label != LABEL
    assert transport.comment != LIBRARY
