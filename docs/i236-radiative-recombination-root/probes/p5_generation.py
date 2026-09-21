#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 5 -- what the narrowed family generates, by product structure.

Runs the shipped path, `KineticsFamily.generate_reactions`, and reports the
product as an adjacency list and as an isomorphism test against the species the
reaction is supposed to make. A count alone would pass on an empty list; the
isomorphism test is what cannot.
"""
import os
import sys
import traceback

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))

from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule import Molecule

FAMILY = 'Plasma_Radiative_Recombination'
kdb = KineticsDatabase()
kdb.load_families(os.path.join(DB, 'kinetics', 'families'), families=[FAMILY])
fam = kdb.families[FAMILY]
print('family loaded: {0} | electrons = {1} | tree entries = {2}'.format(
    fam.label, fam.electrons, sorted(fam.groups.entries)))
print('root group:\n{0}'.format(fam.groups.entries['A'].item.to_adjacency_list().strip()))
print()

CASES = [
    ('Li+', '1 Li u0 p0 c+1', '1 Li u1 p0 c0'),
    ('H+',  '1 H  u0 p0 c+1', '1 H  u1 p0 c0'),
    ('Na+', '1 Na u0 p0 c+1', '1 Na u1 p0 c0'),
    ('Ar+', 'multiplicity 2\n1 Ar u1 p3 c+1', '1 Ar u0 p4 c0'),
    ('Ar',  '1 Ar u0 p4 c0',  None),
    ('He+', 'multiplicity 2\n1 He u1 p0 c+1', '1 He u0 p1 c0'),
    ('CO',  '1 C u0 p1 c-1 {2,T}\n2 O u0 p1 c+1 {1,T}', None),
    ('CH4', '1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n2 H u0 p0 c0 {1,S}\n'
            '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n5 H u0 p0 c0 {1,S}', None),
]

for label, adj, expect in CASES:
    mol = Molecule().from_adjacency_list(adj)
    print('--- {0}'.format(label))
    try:
        rxns = fam.generate_reactions([mol])
    except Exception:
        print('    RAISES:')
        traceback.print_exc(file=sys.stdout)
        print()
        continue
    print('    {0} reaction(s)'.format(len(rxns)))
    for r in rxns:
        print('      {0}   electrons={1}'.format(r, getattr(r, 'electrons', None)))
        for p in r.products:
            padj = ' / '.join(l.strip() for l in
                              p.to_adjacency_list().strip().splitlines())
            print('        product: {0}'.format(padj))
            if expect is not None:
                want = Molecule().from_adjacency_list(expect)
                want.update(sort_atoms=False)
                print('        isomorphic to expected {0!r}: {1}'.format(
                    expect.replace('\n', ' / '), p.is_isomorphic(want)))
    print()
