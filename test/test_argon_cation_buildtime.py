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
(diatomic, +1). "Loud failure, not silent fabrication" is the distinction this campaign
cares about, and it still holds for both - but **not by the same mechanism it once did**,
and the two tests' names and docstrings were rewritten under I-226 to say so:

  * the dication's ``3P`` spelling no longer perceives at all and dies at
    ``AtomTypeError``; the loud ``DatabaseError`` guarantee was *relocated* onto the
    closed-shell spelling the ``Ar++`` leaf admits, where it is still asserted;
  * the dimer still builds, but is refused during HBI saturation by ``AtomTypeError``
    before the thermo database is consulted at all - still loud, but a *narrower*
    guarantee than the original ``DatabaseError``, which proved the database itself
    refused it.

Both changes trace to RMG-Py moving argon out of ``nonSpecifics`` into the leaves
``Ar0``/``Ar0s``/``Ar+``/``Ar++`` and then narrowing ``Ar0s`` to ``single=[1]``. The
measurements behind every re-pinned assertion are in
``docs/argon-perception-pins/logs/`` and the findings in
``docs/argon-perception-pins/report.md``.

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
from rmgpy.exceptions import AtomTypeError, DatabaseError
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
#: The +2 argon the engine's ``Ar++`` leaf actually admits: closed-shell, 3 lone pairs.
#: ``DICATION`` above (the physical ``3P`` ground state, 2 lone pairs) no longer perceives
#: at all - see ``test_the_dication_no_longer_builds_...`` and the report's referral.
DICATION_CLOSED_SHELL = '1 Ar u0 p3 c+2\n'                # Ar(2+) monatomic +2, closed shell
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


def test_the_dication_no_longer_builds_but_the_loud_refusal_survives_on_the_spelling_that_does(
        argon_capable_db):
    """The dication's guarantee was RELOCATED, not lost - and this test now pins both ends.

    **What this test was written for, and why it was right.** The dication Ar(2+)
    (monatomic, +2) was the "Ar2+" reading that *builds* yet raises a loud ``DatabaseError``
    from the thermo layer: group additivity has no group for a charge-+2 argon atom, so the
    species is refused rather than handed a fabricated number. When it was written, argon was
    a ``nonSpecifics`` catch-all, so ``DICATION`` - spelled ``u2 p2 c+2``, the physical
    ``3P`` ground state - perceived as the generic ``Ar`` and built without complaint. The
    assertion chain (builds -> net charge 2 -> DatabaseError mentioning ``Ar++``) was an
    accurate description of the engine of the day.

    **What changed.** Argon left ``nonSpecifics`` and grew the leaves
    ``Ar0``/``Ar0s``/``Ar+``/``Ar++``. The ``Ar++`` leaf admits ``lone_pairs=[3]`` only -
    i.e. the closed-shell configuration - so the ``3P`` spelling ``u2 p2 c+2`` (2 lone pairs)
    matches **no** leaf and now raises ``AtomTypeError`` inside ``from_adjacency_list``,
    before ``get_thermo_data`` is ever called. The "builds" half of this test's premise is
    gone.

    **Why the guarantee is not lost.** A +2 argon that the engine *does* admit still exists:
    ``u0 p3 c+2`` perceives as ``Ar++``, builds, and is still refused by the thermo layer
    with the same loud ``DatabaseError`` naming ``Ar++``
    (``docs/argon-perception-pins/logs/probe_guarantee_stdout.log``). So the property this
    test protects - **loud failure, never silent fabrication, for a charge-+2 argon** - is
    intact; only the adjacency list that reaches it has changed. Both halves are pinned here
    so neither can regress silently.

    **Referral, not a fix.** That the engine's ``Ar++`` leaf refuses the *physical ground
    state* of Ar(2+) while admitting a closed-shell configuration is a finding about the
    atom-type work, owned in RMG-Py. It is written up in
    ``docs/argon-perception-pins/report.md`` and deliberately not patched here."""
    # Half one: the 3P spelling no longer builds at all - it dies at perception.
    with pytest.raises(AtomTypeError) as build_exc:
        _species(DICATION, 'Ar2+')
    assert '+2 charge' in str(build_exc.value)
    assert '2 lone pairs' in str(build_exc.value)

    # Half two: the spelling the Ar++ leaf DOES admit still reaches the thermo layer,
    # and is still refused loudly rather than fabricated. This is the original guarantee.
    species = _species(DICATION_CLOSED_SHELL, 'Ar2+')
    assert species.molecule[0].get_net_charge() == 2
    assert species.molecule[0].atoms[0].atomtype.label == 'Ar++'
    with pytest.raises(DatabaseError) as exc:
        argon_capable_db.get_thermo_data(species)
    assert 'Ar++' in str(exc.value)


def test_the_dimer_cation_still_builds_but_is_now_refused_one_layer_earlier(argon_capable_db):
    """The dimer still fails loudly, but from a different layer - and that IS a partial loss.

    **What this test was written for, and why it was right.** The dimer Ar2(+) (diatomic,
    +1) built, then raised a loud ``DatabaseError`` from ``get_thermo_data`` - reached "via
    HBI saturation rather than a bare atom type", as the original docstring correctly said.
    RMG saturates the radical to look up a closed-shell parent, the saturated argon has no
    thermo group, and the database refuses it. Still loud, still not fabricated.

    **What changed.** Nothing about *building* it: measurement confirms the dimer still
    parses, as ``Ar0s`` bonded to ``Ar+`` (``[Ar][Ar+]``). What changed is one step deeper.
    HBI saturation adds an H to the neutral argon, producing an argon with **two** single
    bonds, 3 lone pairs and charge 0 - and the merge that narrowed ``Ar0s`` to ``single=[1]``
    left no leaf that admits it. So ``saturate_radicals`` now raises ``AtomTypeError`` from
    inside ``estimate_radical_thermo_via_hbi``, at the same call site where the
    ``DatabaseError`` used to come from
    (``docs/argon-perception-pins/logs/probe_exact_stdout.log``, steps 3 and 5).

    **The guarantee question, answered.** The campaign's property - *loud failure, not
    silent fabrication* - **holds**: the run still aborts, and no number is invented. But the
    guarantee is **narrower than it was**, and the honest word is partially lost. The old
    assertion demonstrated something about the **thermo database**: that it has no group for
    this species and says so. Today the thermo database is never consulted, because the
    molecule machinery fails first. This test can no longer witness the database's refusal of
    the dimer; it can only witness that the dimer is unreachable. That is a smaller
    guarantee, and it is pinned as such rather than dressed up as equivalent.

    **Referral, not a fix.** Whether ``Ar0s`` narrowed to ``single=[1]`` *should* admit the
    HBI-saturated two-bond argon is an RMG-Py question - HBI saturation can manufacture
    valences the narrowing never considered. See ``docs/argon-perception-pins/report.md``."""
    # Building it is unchanged - this half of the original premise still holds.
    species = _species(DIMER, 'Ar2+dimer')
    assert species.molecule[0].get_net_charge() == 1
    assert [a.atomtype.label for a in species.molecule[0].atoms] == ['Ar0s', 'Ar+']

    # It is still refused loudly, but now by perception during HBI saturation rather than
    # by the thermo database. Pinned as AtomTypeError precisely because it is NOT the same
    # guarantee: DatabaseError would mean the database was reached and said no.
    with pytest.raises(AtomTypeError) as exc:
        argon_capable_db.get_thermo_data(species)
    assert '2 single bonds' in str(exc.value)
    assert '+0 charge' in str(exc.value)
