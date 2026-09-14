#!/usr/bin/env python
# encoding: utf-8

"""
Measure the three failing cases using the *exact* constants the tests spell, imported
from the test modules themselves rather than retyped.

The first probe (``probe_argon_perception.py``) used adjacency lists typed from the task
brief's prose and got two of them wrong: the real ``DICATION`` is ``u2 p2 c+2`` (not
``u0 p2 c+2``), and the dimer's failure does not happen at ``from_adjacency_list`` at all.
This probe fixes that by importing ``ARP``/``DICATION``/``DIMER`` from the test module,
and by walking the ``get_thermo_data`` path where the dimer actually dies.
"""

import os
import sys
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, 'test'))

import conftest  # noqa: F401  - pins database.directory, exactly as pytest does

from rmgpy.molecule import Molecule
from rmgpy.molecule.atomtype import ATOMTYPES
from rmgpy.species import Species

import test_argon_cation_buildtime as bt


def banner(title):
    print('\n' + '=' * 78)
    print(title)
    print('=' * 78)


def show(name, adjlist):
    print('\n--- %s ---' % name)
    print('adjlist (verbatim from the test module):')
    print(repr(adjlist))
    try:
        mol = Molecule().from_adjacency_list(adjlist)
    except Exception as exc:
        print('from_adjacency_list RAISED : %s: %s' % (type(exc).__name__, exc))
        traceback.print_exc(file=sys.stdout)
        return None
    print('from_adjacency_list OK     : %r' % mol)
    print('  net charge :', mol.get_net_charge())
    for i, atom in enumerate(mol.atoms):
        print('  atom[%d] element=%-3s atomtype=%-6s radical=%d lone_pairs=%d charge=%+d bonds=%d'
              % (i, atom.element.symbol, atom.atomtype.label, atom.radical_electrons,
                 atom.lone_pairs, atom.charge, len(atom.bonds)))
    return mol


banner('BUILD PROVENANCE')
import rmgpy.molecule.atomtype as atomtype_module
print('atomtype module file :', atomtype_module.__file__)

banner('THE THREE CONSTANTS, AS THE TEST MODULE DEFINES THEM')
print('ARP      =', repr(bt.ARP))
print('DICATION =', repr(bt.DICATION))
print('DIMER    =', repr(bt.DIMER))

banner('STEP 1 - Molecule().from_adjacency_list on each')
mol_arp = show('ARP  (Ar+, u1 p3 c+1)', bt.ARP)
mol_dication = show('DICATION (Ar(2+), u2 p2 c+2)', bt.DICATION)
mol_dimer = show('DIMER (Ar2(+), u0 p3 c+1 -S- u1 p3 c0)', bt.DIMER)

banner('STEP 2 - _species(): Species + generate_resonance_structures')
for name, adjlist in [('ARP', bt.ARP), ('DICATION', bt.DICATION), ('DIMER', bt.DIMER)]:
    print('\n--- _species(%s) ---' % name)
    try:
        sp = bt._species(adjlist, name)
    except Exception as exc:
        print('_species RAISED : %s: %s' % (type(exc).__name__, exc))
        traceback.print_exc(file=sys.stdout)
        continue
    print('_species OK     : %d resonance structure(s)' % len(sp.molecule))
    for j, m in enumerate(sp.molecule):
        print('  structure[%d] %r  atomtypes=%s'
              % (j, m, [a.atomtype.label for a in m.atoms]))

banner('STEP 3 - get_thermo_data on the argon-capable deck (where the tests assert)')
db = bt._db_with(bt.ARGON_CAPABLE_DECK)
for name, adjlist in [('ARP', bt.ARP), ('DICATION', bt.DICATION), ('DIMER', bt.DIMER)]:
    print('\n--- get_thermo_data(_species(%s)) ---' % name)
    try:
        sp = bt._species(adjlist, name)
    except Exception as exc:
        print('  species construction RAISED : %s: %s' % (type(exc).__name__, exc))
        continue
    try:
        data = db.get_thermo_data(sp)
    except Exception as exc:
        print('  get_thermo_data RAISED : %s: %s' % (type(exc).__name__, exc))
        print('  exception module       :', type(exc).__module__)
        print('  exception MRO          :', [c.__name__ for c in type(exc).__mro__])
        traceback.print_exc(file=sys.stdout)
        continue
    print('  get_thermo_data OK  : comment=%r' % data.comment)
    print('  H298 (kJ/mol)       :', data.get_enthalpy(298.15) / 1000.0)

banner('STEP 4 - the reference-deck refusal (the test that still passes)')
ref_db = bt._db_with(bt.REFERENCE_DECK_THERMO_LIBRARIES)
try:
    ref_db.get_thermo_data(bt._species(bt.ARP, 'Ar+'))
    print('  NO EXCEPTION - the reference deck resolved Ar+')
except Exception as exc:
    print('  RAISED : %s: %s' % (type(exc).__name__, exc))

banner('STEP 5 - what the HBI saturation of the dimer actually looks like')
# The dimer test's own docstring says it dies "via HBI saturation". Reproduce that step
# explicitly so the report can name the species whose atom type is missing.
dimer = Molecule().from_adjacency_list(bt.DIMER)
sat = dimer.copy(deep=True)
try:
    sat.saturate_radicals()
    print('  saturated structure : %r' % sat)
    for i, atom in enumerate(sat.atoms):
        print('    atom[%d] element=%-3s atomtype=%-6s radical=%d lone_pairs=%d charge=%+d bonds=%d'
              % (i, atom.element.symbol, atom.atomtype.label, atom.radical_electrons,
                 atom.lone_pairs, atom.charge, len(atom.bonds)))
except Exception as exc:
    print('  saturate_radicals RAISED : %s: %s' % (type(exc).__name__, exc))
    traceback.print_exc(file=sys.stdout)

banner('STEP 6 - which argon adjacency lists DO have an atom type today')
PROBES = [
    ('Ar ground state      u0 p4 c0',  '1 Ar u0 p4 c0\n'),
    ('Ar bonded neutral    u0 p3 c0 + 1 bond (needs a partner)', None),
    ('Ar+  u1 p3 c+1',                 'multiplicity 2\n1 Ar u1 p3 c+1\n'),
    ('Ar+  u0 p3 c+1 (closed shell)',  '1 Ar u0 p3 c+1\n'),
    ('Ar2+ u2 p2 c+2 (3P, the physical ground state)', 'multiplicity 3\n1 Ar u2 p2 c+2\n'),
    ('Ar2+ u0 p3 c+2 (what the Ar++ leaf describes)',  '1 Ar u0 p3 c+2\n'),
]
for name, adjlist in PROBES:
    if adjlist is None:
        continue
    print('\n--- %s ---' % name)
    try:
        m = Molecule().from_adjacency_list(adjlist)
        print('  OK  atomtypes=%s' % [a.atomtype.label for a in m.atoms])
    except Exception as exc:
        print('  RAISED : %s: %s' % (type(exc).__name__, exc))

banner("STEP 7 - the Ar++ leaf's envelope vs the physical 3P ground state")
t = ATOMTYPES['Ar++']
print('Ar++ single=%s lone_pairs=%s charge=%s' % (t.single, t.lone_pairs, t.charge))
print('DICATION as spelled needs lone_pairs=2 (u2 p2 c+2); leaf admits lone_pairs=%s' % t.lone_pairs)

banner('DONE')
