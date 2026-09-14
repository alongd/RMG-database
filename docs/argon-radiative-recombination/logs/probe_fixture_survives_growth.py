#!/usr/bin/env python
"""Does the corrected fixture survive the library growing? Measure, do not assume.

The reason I first gave for NOT fixing the two sibling files was that the change is
unverifiable while each library has exactly one entry. That reason is wrong: the entry
count is a property of the loaded object, and a loaded object can be grown in memory.

This probe loads each library for real, injects a synthetic second entry, and runs BOTH
selection strategies against it:

  old: reactions = library.get_library_reactions(); assert len(reactions) == 1; reactions[0]
  new: [r for r in ... if [s.label for s in r.reactants] == TARGET]; assert len(...) == 1

The claim under test is that the old one raises (which, inside a pytest fixture, is a setup
ERROR that silently removes every test it feeds) and the new one still returns the entry the
file is about. Nothing is written to the database; the growth happens in memory only.
"""
import copy
import os
import sys

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase

# Same pin ``test/conftest.py`` applies: without it ``database.directory`` resolves to the
# shared checkout, not this worktree, and the probe would measure someone else's database.
THIS_DATABASE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, 'input'))
settings['database.directory'] = THIS_DATABASE
print('database.directory = %s\n' % settings['database.directory'])

CASES = [
    ('PlasmaArgon', ['Ar', 'e-']),
    ('PlasmaElectronImpactIonization', ['[Li]']),
    ('PlasmaRadiativeRecombination', ['[Arp]']),  # already two-entry: control
]


def load(label):
    db = KineticsDatabase()
    db.load_libraries(os.path.join(settings['database.directory'], 'kinetics', 'libraries'),
                      libraries=[label])
    return db.libraries[label]


def select_old(library):
    reactions = library.get_library_reactions()
    assert len(reactions) == 1
    return reactions[0]


def select_new(library, target):
    matches = [r for r in library.get_library_reactions()
               if [s.label for s in r.reactants] == target]
    assert len(matches) == 1
    return matches[0]


def grow(library):
    """Inject a synthetic second entry, so the loaded library has one more than it ships."""
    key = max(library.entries) if library.entries else 0
    twin = copy.deepcopy(next(iter(library.entries.values())))
    twin.index = 9999
    twin.label = 'synthetic-probe-entry'
    for species in twin.item.reactants:
        species.label = species.label + '_probe'
    library.entries['synthetic-probe-entry'] = twin
    return key


failures = []
for label, target in CASES:
    library = load(label)
    shipped = len(library.entries)
    grow(library)
    grown = len(library.entries)

    try:
        select_old(library)
        old = 'returned a reaction'
    except AssertionError:
        old = 'AssertionError -> pytest SETUP ERROR, every test on this fixture silently skipped'

    try:
        got = select_new(library, target)
        new = 'returned %s' % ' + '.join(s.label for s in got.reactants)
        ok = [s.label for s in got.reactants] == target
    except AssertionError as exc:
        new = 'AssertionError: %s' % exc
        ok = False

    print('%-32s shipped=%d grown=%d' % (label, shipped, grown))
    print('    old (by position): %s' % old)
    print('    new (by identity): %s' % new)
    print('    -> %s' % ('PASS' if ok else 'FAIL'))
    print('')
    if not ok:
        failures.append(label)

if failures:
    print('FAILED for: %s' % ', '.join(failures))
    sys.exit(1)
print('All three libraries: identity selection survives growth, positional selection does not.')
