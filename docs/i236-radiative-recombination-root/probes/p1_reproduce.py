#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 1 -- reproduce both defects of the Plasma_Radiative_Recombination root.

Loads the family alone and asks it to generate reactions for Ar+ (what radiative
recombination actually consumes) and for neutral Ar (what the root also matches).
Prints the resolved database directory first, so a run against the wrong tree is
visible rather than silent.
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
from rmgpy.species import Species

FAMILY = 'Plasma_Radiative_Recombination'

kdb = KineticsDatabase()
kdb.load_families(os.path.join(DB, 'kinetics', 'families'), families=[FAMILY])
fam = kdb.families[FAMILY]
print('family loaded: {0} | electrons = {1}'.format(fam.label, fam.electrons))
print('groups tree entries: {0} -> {1}'.format(
    len(fam.groups.entries), sorted(fam.groups.entries.keys())))
print('root group adjlist: {0!r}'.format(
    str(fam.groups.entries['A'].item).strip()))
print('recipe: {0}'.format([[a.action, a.label if hasattr(a, "label") else a] for a in []] or
                           fam.forward_recipe.actions))
print('template: reactants={0} products={1}'.format(
    [e.label for e in fam.forward_template.reactants],
    [e.label for e in fam.forward_template.products]))
print()

CASES = [
    ('Ar+  (what RR consumes)', '1 Ar u1 p3 c+1'),
    ('Ar   (neutral)',          '1 Ar u0 p4 c0'),
]

for name, adj in CASES:
    print('--- {0} : {1}'.format(name, adj))
    spc = Species().from_adjacency_list(adj)
    spc.generate_resonance_structures()
    try:
        rxns = fam.generate_reactions([spc.molecule[0]])
        print('    {0} reaction(s)'.format(len(rxns)))
        for r in rxns:
            print('      {0}'.format(r))
            for p in r.products:
                print('        product adjlist: {0!r}'.format(
                    str(p.to_adjacency_list()).strip()))
    except Exception:
        print('    RAISES:')
        traceback.print_exc(file=sys.stdout)
    print()

# Does the root group match, independent of whether the recipe survives?
from rmgpy.data.kinetics.common import ensure_species
root = fam.groups.entries['A'].item
for name, adj in CASES:
    mol = Molecule().from_adjacency_list(adj)
    print('root group matches {0:26s}: {1}'.format(
        name, mol.is_subgraph_isomorphic(root)))
