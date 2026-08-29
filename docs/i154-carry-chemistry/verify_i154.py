#!/usr/bin/env python3
"""I-154 verifier: the carried plasma chemistry loads, and every electron-bearing
owner declares its placement.

Run:

    cd /home/alon/Code/RMG-Py-i154-carry-chemistry
    export PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH
    export PYTHONPATH=/home/alon/Code/RMG-Py-i154-carry-chemistry:$PYTHONPATH
    python /home/alon/Code/RMG-database-i154-carry-chemistry/docs/i154-carry-chemistry/verify_i154.py

Exits 0 only if every check below passes.  The resolved database directory is
printed first, because a suite measured against the wrong database is the failure
mode this project has already paid for once.

The four checks:

1. LOADS       — every carried family and library loads, with the entry counts
                 this ticket landed.
2. PLACEMENT   — every carried owner whose reactions change the free-electron
                 count is declared in ``FAMILY_ELECTRON_PLACEMENT``, and its
                 declared ``(reactant_count, product_count)`` matches the shape
                 read off its own entries.  Owners that carry no free electron
                 must NOT be declared.
3. REFUSAL     — an undeclared owner is still refused by name with
                 ``ElectronPlacementError``.  No permissive fallback was added.
4. DATABASE    — the kinetics database loads with and without the plasma
                 families, and both carried libraries load through it.
"""
import os
import re
import sys

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.kinetics.family import KineticsFamily, TemplateReaction
from rmgpy.data.kinetics.library import KineticsLibrary
from rmgpy.electron_placement import FAMILY_ELECTRON_PLACEMENT, resolve_electron_placement
from rmgpy.exceptions import ElectronPlacementError
from rmgpy.kinetics import Arrhenius
from rmgpy.molecule import Molecule
from rmgpy.species import Species

DB = settings['database.directory']
KIN = os.path.join(DB, 'kinetics')

#: label -> (net electrons declared in groups.py, expected training entry count)
CARRIED_FAMILIES = {
    'Plasma_Associative_Ionization_Alkali_Alkali':     (1, 4),
    'Plasma_Associative_Ionization_Alkali_Alkaline':   (1, 1),
    'Plasma_Associative_Ionization_Alkaline_Alkaline': (1, 3),
}

#: Held back from the database, with the reason each one is not carried.  They
#: live under ``docs/i154-carry-chemistry/held-back/`` and are described in
#: ``docs/i154-carry-chemistry.md`` section 4.  Asserted ABSENT here so that
#: landing one of them has to be a deliberate edit to this file.
HELD_BACK_FAMILIES = {
    'Plasma_Charge_Transfer':
        'group tree defects: wildcard lone pairs on charged generic roots, a '
        'one-electron-bond H2+, and a noble-gas branch whose members need '
        'different lone-pair counts',
    'Plasma_Collisional_Ionization':
        'its LogicOr third-body collider is a SPECTATOR template participant, '
        'so the engine generates six product groups identical to the reactant '
        'leaves and kinetics_check_groups_nonidentical refuses them',
    'Plasma_Electron_Impact_Dissociation':
        'the incident electron is a SPECTATOR template participant, and the two '
        'consistency checks contradict each other for that shape',
    'Plasma_Ion_Molecule_Association':
        'the recipe forms a ZERO-order bond and the training products are '
        'unbonded atom pairs, so apply_recipe returns None',
}

#: label -> expected entry count
CARRIED_LIBRARIES = {'PlasmaAir': 42, 'PlasmaAlkali': 52}

#: The owners this ticket declares, and the shape each must declare.
EXPECTED_PLACEMENT = {
    'Plasma_Associative_Ionization_Alkali_Alkali':     (0, 1),
    'Plasma_Associative_Ionization_Alkali_Alkaline':   (0, 1),
    'Plasma_Associative_Ionization_Alkaline_Alkaline': (0, 1),
}

#: Carried owners that must stay UNdeclared, with the reason each one is exempt.
MUST_NOT_DECLARE = {
    'PlasmaAir': 'every surviving entry conserves the free electron count',
    'PlasmaAlkali': 'every surviving entry conserves the free electron count',
    'Plasma_Charge_Transfer': 'held back, and carries no free electron anyway',
    'Plasma_Collisional_Ionization': 'held back from the database',
    'Plasma_Electron_Impact_Dissociation': 'held back from the database',
    'Plasma_Ion_Molecule_Association': 'held back, and carries no free electron anyway',
}

failures = []


def check(condition, message):
    if condition:
        print('    ok   {0}'.format(message))
    else:
        print('    FAIL {0}'.format(message))
        failures.append(message)


def entry_shape(label):
    """(reactant electrons, product electrons) read off a reaction label."""
    lhs, _, rhs = re.split(r'(<=>|=>)', label, maxsplit=1)
    side = lambda s: [t.strip() for t in re.split(r'\s\+\s', s.strip()) if t.strip()]
    return side(lhs).count('e-'), side(rhs).count('e-')


print('=' * 78)
print('I-154 verifier')
print('=' * 78)
print('database.directory = {0}'.format(DB))
print('rmgpy              = {0}'.format(__import__('rmgpy').__file__))
print()

kdb = KineticsDatabase()
lc, gc = kdb.local_context, kdb.global_context

# ---------------------------------------------------------------- 1. LOADS
print('1. LOADS')
families = {}
for label, (electrons, n_training) in sorted(CARRIED_FAMILIES.items()):
    fam = KineticsFamily(label=label)
    try:
        fam.load(os.path.join(KIN, 'families', label), dict(lc), dict(gc),
                 depository_labels=None)
    except Exception as exc:
        check(False, '{0}: {1}: {2}'.format(label, type(exc).__name__, exc))
        continue
    families[label] = fam
    got = sum(len(d.entries) for d in fam.depositories if d.label.endswith('/training'))
    check(fam.electrons == electrons and got == n_training,
          '{0:<48} electrons={1} training={2}'.format(label, fam.electrons, got))

for label, n_entries in sorted(CARRIED_LIBRARIES.items()):
    lib = KineticsLibrary(label=label)
    try:
        lib.load(os.path.join(KIN, 'libraries', label, 'reactions.py'), dict(lc), dict(gc))
    except Exception as exc:
        check(False, '{0}: {1}: {2}'.format(label, type(exc).__name__, exc))
        continue
    check(len(lib.entries) == n_entries,
          '{0:<48} {1} entries'.format(label, len(lib.entries)))

# ------------------------------------------------------------ 2. PLACEMENT
print()
print('2. PLACEMENT')
for label, expected in sorted(EXPECTED_PLACEMENT.items()):
    declared = FAMILY_ELECTRON_PLACEMENT.get(label)
    check(declared == expected, '{0:<48} declares {1}'.format(label, declared))
    if label not in families:
        continue
    # The declaration must match what the family's own entries do: the net change
    # equals product_count - reactant_count, and no training label may carry an
    # explicit electron (that would be double representation).
    net = expected[1] - expected[0]
    check(families[label].electrons == net,
          '{0:<48} groups.py electrons={1} matches declared net {2}'.format(
              label, families[label].electrons, net))
    path = os.path.join(KIN, 'families', label, 'training', 'reactions.py')
    labels = re.findall(r'^\s*label = "([^"]+)"', open(path).read(), re.M)
    check(all(entry_shape(l) == (0, 0) for l in labels),
          '{0:<48} no training label carries an explicit electron'.format(label))

for label, why in sorted(MUST_NOT_DECLARE.items()):
    check(label not in FAMILY_ELECTRON_PLACEMENT,
          '{0:<48} undeclared - {1}'.format(label, why))

# Every surviving library entry must conserve the electron count, which is what
# makes the two libraries' absence from the registry correct rather than lucky.
for label in sorted(CARRIED_LIBRARIES):
    path = os.path.join(KIN, 'libraries', label, 'reactions.py')
    labels = re.findall(r'^\s*label = "([^"]+)"', open(path).read(), re.M)
    bad = [l for l in labels if entry_shape(l)[0] != entry_shape(l)[1]]
    check(not bad, '{0:<48} all {1} entries conserve the electron count'.format(
        label, len(labels)))

# The declaration must actually resolve.  Build a reaction in the shape
# Plasma_Associative_Ionization_Alkaline_Alkaline produces -- O + O -> O2+ + e- --
# and push it through the resolver.
electron = Species(label='e-', molecule=[Molecule().from_adjacency_list('1 e u1 p0 c-1')])
o_atom = Species(label='O', molecule=[Molecule().from_adjacency_list('1 O u2 p2 c0')])
o_atom2 = Species(label='O_b', molecule=[Molecule().from_adjacency_list('1 O u2 p2 c0')])
o2p = Species(label='O2+', molecule=[Molecule().from_adjacency_list(
    '1 O u0 p2 c+1 {2,S}\n2 O u1 p2 c0 {1,S}')])

# A plain Reaction is a cdef class with no ``family`` slot; the resolver reads
# ``Reaction.family``, so the probe has to be the class that actually carries it.
rxn = TemplateReaction(reactants=[o_atom, o_atom2], products=[o2p], electrons=1,
                       reversible=False, family='Plasma_Associative_Ionization_Alkaline_Alkaline',
                       kinetics=Arrhenius(A=(2.2e15, 'cm^3/(mol*s)'), n=-0.35,
                                          Ea=(215000, 'cal/mol'), T0=(1, 'K')))
try:
    view = resolve_electron_placement(rxn, [o_atom, o_atom2, o2p, electron])
except Exception as exc:
    check(False, 'resolver on an associative-ionisation-shaped reaction: '
                 '{0}: {1}'.format(type(exc).__name__, exc))
else:
    n_r = sum(1 for s in view.reactants if s.is_electron())
    n_p = sum(1 for s in view.products if s.is_electron())
    check((n_r, n_p) == (0, 1) and view.electrons == 0,
          'resolver places (0, 1) and zeroes the metadata count')
    check(rxn.electrons == 1 and len(rxn.reactants) == 2 and len(rxn.products) == 1,
          'the canonical reaction is not mutated by the resolver')

# -------------------------------------------------------------- 3. REFUSAL
print()
print('3. REFUSAL')
undeclared = TemplateReaction(reactants=[o_atom, o_atom2], products=[o2p], electrons=1,
                              reversible=False, family='Plasma_Not_A_Real_Family',
                              kinetics=rxn.kinetics)
try:
    resolve_electron_placement(undeclared, [o_atom, o_atom2, o2p, electron])
except ElectronPlacementError as exc:
    check('Plasma_Not_A_Real_Family' in str(exc),
          'undeclared owner refused by name')
except Exception as exc:
    check(False, 'undeclared owner raised {0}, not ElectronPlacementError'.format(
        type(exc).__name__))
else:
    check(False, 'undeclared owner was NOT refused - a fallback has appeared')

# ------------------------------------------------------------- 4. DATABASE
print()
print('4. DATABASE')
plasma_families = sorted(CARRIED_FAMILIES) + ['Plasma_Electron_Attachment']

for label, why in sorted(HELD_BACK_FAMILIES.items()):
    check(not os.path.isdir(os.path.join(KIN, 'families', label)),
          '{0:<48} absent from the database - {1}'.format(label, why))

kdb_without = KineticsDatabase()
kdb_without.load(KIN, families=['default'], libraries=[], depositories=[])
n_without = len(kdb_without.families)

kdb_with = KineticsDatabase()
kdb_with.load(KIN, families=['default'] + plasma_families, libraries=[], depositories=[])
n_with = len(kdb_with.families)

check(n_without > 0,
      'database loads WITHOUT the plasma families ({0} families)'.format(n_without))
check(n_with >= n_without,
      'database loads WITH the plasma families ({0} families, +{1})'.format(
          n_with, n_with - n_without))
missing = [f for f in plasma_families if f not in kdb_with.families]
check(not missing, 'every requested plasma family is present when asked for')

kdb_libs = KineticsDatabase()
kdb_libs.load(KIN, families=[], libraries=sorted(CARRIED_LIBRARIES), depositories=[])
check(sorted(kdb_libs.libraries) == sorted(CARRIED_LIBRARIES),
      'both carried libraries load through the database loader')

print()
print('=' * 78)
if failures:
    print('FAILED: {0} check(s)'.format(len(failures)))
    for f in failures:
        print('  - {0}'.format(f))
    sys.exit(1)
print('All checks passed.')
sys.exit(0)
