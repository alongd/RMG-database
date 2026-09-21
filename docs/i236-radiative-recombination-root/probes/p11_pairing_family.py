#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 11 -- does the pairing family load, and does it generate
`Ar+ + e- => Ar` with ground-state argon as the product?

Both arms of the electron-placement question are measured here: first with the
registry as RMG-Py actually ships it (this family absent), then with the one
entry this family needs injected in-process. The second arm is what shows the
DATABASE half is complete; the first is what shows exactly which one-line code
change is still owed.
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
from rmgpy import electron_placement

FAMILY = 'Plasma_Radiative_Recombination_Pairing'
SIBLING = 'Plasma_Radiative_Recombination'

print('\nFAMILY_ELECTRON_PLACEMENT contains {0!r}: {1}'.format(
    FAMILY, FAMILY in electron_placement.FAMILY_ELECTRON_PLACEMENT))

kdb = KineticsDatabase()
kdb.load_families(os.path.join(DB, 'kinetics', 'families'),
                  families=[FAMILY, SIBLING], depositories=['training'])
fam = kdb.families[FAMILY]
print('family loaded: {0} | electrons = {1} | reversible = {2}'.format(
    fam.label, fam.electrons, fam.reversible))
print('recipe            : {0}'.format([list(a) for a in fam.forward_recipe.actions]))
print('tree entries      : {0}'.format(sorted(fam.groups.entries)))
print('reactant template : {0}  {1}'.format(
    [e.label for e in fam.forward_template.reactants],
    fam.groups.entries['Ar_cation'].item.to_adjacency_list().strip()))
print('PRODUCT template  : {0}  {1}'.format(
    [e.label for e in fam.forward_template.products],
    fam.forward_template.products[0].item.to_adjacency_list().strip()))
print('rate rules        : {0}'.format(
    {lbl: str(e.data) for lbl, e in fam.rules.entries.items()
     for e in e} if False else
    {lbl: repr(entries[0].data) for lbl, entries in fam.rules.entries.items()}))

GROUND_AR = Molecule().from_adjacency_list('1 Ar u0 p4 c0')
GROUND_AR.update(sort_atoms=False)
METASTABLE = Molecule().from_adjacency_list('multiplicity 3\n1 Ar u2 p3 c0')
METASTABLE.update(sort_atoms=False)

CASES = [
    ('Ar+', 'multiplicity 2\n1 Ar u1 p3 c+1'),
    ('Ar  (neutral)', '1 Ar u0 p4 c0'),
    ('Ar(3P2)', 'multiplicity 3\n1 Ar u2 p3 c0'),
    ('Li+', '1 Li u0 p0 c+1'),
    ('He+', 'multiplicity 2\n1 He u1 p0 c+1'),
    ('CH4', '1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n2 H u0 p0 c0 {1,S}\n'
            '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n5 H u0 p0 c0 {1,S}'),
]


def run(tag):
    print('\n' + '=' * 70)
    print(tag)
    print('=' * 70)
    for label, adj in CASES:
        mol = Molecule().from_adjacency_list(adj)
        print('--- {0}'.format(label))
        try:
            rxns = fam.generate_reactions([mol])
        except Exception:
            print('    RAISES:')
            for line in traceback.format_exc().strip().splitlines()[-4:]:
                print('      {0}'.format(line))
            continue
        print('    {0} reaction(s)'.format(len(rxns)))
        for r in rxns:
            print('      {0}   electrons={1}'.format(r, r.electrons))
            for p in r.products:
                pm = p if isinstance(p, Molecule) else p.molecule[0]
                print('        product: {0}'.format(
                    ' / '.join(l.strip() for l in pm.to_adjacency_list().strip().splitlines())))
                print('        isomorphic to GROUND-STATE Ar : {0}'.format(pm.is_isomorphic(GROUND_AR)))
                print('        isomorphic to METASTABLE Ar   : {0}'.format(pm.is_isomorphic(METASTABLE)))
                print('        net charge: {0:+d}'.format(pm.get_net_charge()))


run('ARM 1 -- registry as RMG-Py ships it (this family NOT declared)')

electron_placement.FAMILY_ELECTRON_PLACEMENT[FAMILY] = (1, 0)
print('\n\ninjected FAMILY_ELECTRON_PLACEMENT[{0!r}] = (1, 0)'.format(FAMILY))
run('ARM 2 -- with the one-line RMG-Py registry entry this family needs')

print('\n\n=== does the sibling family still refuse Ar+, and this one refuse Li+? ===')
sib = kdb.families[SIBLING]
for fname, f in (('Plasma_Radiative_Recombination', sib), (FAMILY, fam)):
    for label, adj in (('Ar+', 'multiplicity 2\n1 Ar u1 p3 c+1'), ('Li+', '1 Li u0 p0 c+1')):
        try:
            n = len(f.generate_reactions([Molecule().from_adjacency_list(adj)]))
        except Exception as exc:
            n = '{0}'.format(type(exc).__name__)
        print('  {0:42s} {1:4s} -> {2}'.format(fname, label, n))
