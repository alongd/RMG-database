#!/usr/bin/env python
# encoding: utf-8

"""
Measure how today's engine perceives argon.

Every re-pinned assertion in ``test/test_argon_cation_thermo.py`` and
``test/test_argon_cation_buildtime.py`` is justified by a line this script printed, not
by reading ``rmgpy/molecule/atomtype.py``. The resolved ``.so`` path is printed first so
the record shows which build each measurement came from.
"""

import traceback

import rmgpy.molecule.atomtype as atomtype_module
from rmgpy.molecule.atomtype import ATOMTYPES
from rmgpy.molecule import Molecule


def banner(title):
    print('\n' + '=' * 78)
    print(title)
    print('=' * 78)


banner('BUILD PROVENANCE')
print('atomtype module file :', atomtype_module.__file__)
import rmgpy.molecule.molecule as molecule_module
print('molecule module file :', molecule_module.__file__)
import rmgpy
print('rmgpy package dir    :', rmgpy.__path__[0])

banner("ATOMTYPES['Ar'] AND ITS LEAVES")
ar = ATOMTYPES['Ar']
print('Ar.label      :', ar.label)
print('Ar.generic    :', [t.label for t in ar.generic])
print('Ar.specific   :', [t.label for t in ar.specific])
print('len(specific) :', len(ar.specific))

for label in ['Ar'] + [t.label for t in ar.specific]:
    t = ATOMTYPES[label]
    print('\nleaf %-6s single=%-10s all_double=%-8s lone_pairs=%-8s charge=%s'
          % (t.label, t.single, t.all_double, t.lone_pairs, t.charge))
    print('       %-6s generic=%s specific=%s'
          % ('', [g.label for g in t.generic], [s.label for s in t.specific]))

banner("IS 'Ar' STILL IN nonSpecifics?")
try:
    from rmgpy.molecule.atomtype import allElements, nonSpecifics
    print('nonSpecifics :', nonSpecifics)
    print("'Ar' in nonSpecifics :", 'Ar' in nonSpecifics)
    print('allElements  :', allElements)
except ImportError:
    print('nonSpecifics not importable from rmgpy.molecule.atomtype')
    traceback.print_exc()

banner('PERCEPTION OF CONCRETE ADJACENCY LISTS')

CASES = [
    ('ground-state argon (u0 p4 c0)', """
1 Ar u0 p4 c0
"""),
    ('Ar+ cation (u1 p3 c+1)', """
1 Ar u1 p3 c+1
"""),
    ('dication, exactly as test_argon_cation_buildtime spells it', """
1 Ar u0 p2 c+2
"""),
    ('dimer cation, exactly as test_argon_cation_buildtime spells it', """
1 Ar u0 p3 c+1 {2,S}
2 Ar u1 p3 c0  {1,S}
"""),
]

for name, adjlist in CASES:
    print('\n--- %s ---' % name)
    print('adjlist:%s' % adjlist)
    try:
        mol = Molecule().from_adjacency_list(adjlist)
    except Exception as exc:
        print('RAISED   : %s: %s' % (type(exc).__name__, exc))
        traceback.print_exc()
        continue
    print('OK       : %r' % mol)
    print('charge   :', mol.get_net_charge())
    for i, atom in enumerate(mol.atoms):
        print('  atom[%d] element=%-3s atomtype=%-6s radical=%d lone_pairs=%d charge=%+d'
              % (i, atom.element.symbol, atom.atomtype.label,
                 atom.radical_electrons, atom.lone_pairs, atom.charge))

banner('DOES A LEAF ADMIT THE TWO NONSENSE CONSTRUCTIONS?')
print('dication requirement    : single=0, lone_pairs=2, charge=+2')
print('dimer-cation atom 1 req : single=1, lone_pairs=3, charge=+1')
print('dimer-cation atom 2 req : single=1, lone_pairs=3, charge=0')
for label in ['Ar'] + [t.label for t in ar.specific]:
    t = ATOMTYPES[label]
    print('  %-6s single=%-10s lone_pairs=%-8s charge=%s'
          % (t.label, t.single, t.lone_pairs, t.charge))

banner('DONE')
