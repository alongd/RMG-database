#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 4 -- candidate roots, measured against the whole species inventory.

Each candidate is scored on the two things the ticket cares about -- does it
admit the cations radiative recombination consumes, and does it stop admitting
everything else -- and on the thing that actually decides the design: for every
centre a candidate admits, does the family's recipe
(GAIN_RADICAL *1 1; LOSE_CHARGE *1 1) build a typed molecule?

Centres come from `Molecule.find_subgraph_isomorphisms`, which is the mapping
call `KineticsFamily._match_reactant_to_template` makes, so the centres scored
here are the centres the family would label.

Negative control: `C0` is the root exactly as it stands today. If the harness
were broken so that everything matched or nothing did, C0 would not reproduce
probe 3's 22915/22936, and the run would be void.
"""
import os
from collections import Counter, defaultdict

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))

from rmgpy.data.thermo import ThermoDatabase
from rmgpy.molecule import Molecule, Group
from rmgpy.data.kinetics.family import ReactionRecipe

RECIPE = ReactionRecipe([['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]])

CANDIDATES = [
    ('C0 today',            '1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]'),
    ('C1 drop c0',          '1 *1 R u0 px c[+1,+2,+3,+4,+5,+6,+7,+8]'),
    ('C2 drop c0 and px',   '1 *1 R u0 p0 c+1'),
    ('C3 alkali + H',       '1 *1 [H,Li,Na,K] u0 p0 c+1'),
    ('C4 widen u (brief)',  '1 *1 R ux px c[+1,+2,+3,+4,+5,+6,+7,+8]'),
]

tdb = ThermoDatabase()
lib_dir = os.path.join(DB, 'thermo', 'libraries')
names = sorted(f[:-3] for f in os.listdir(lib_dir) if f.endswith('.py'))
tdb.load_libraries(lib_dir, libraries=names)

seen = {}
for libname, lib in tdb.libraries.items():
    for entry in lib.entries.values():
        item = entry.item
        if not isinstance(item, Molecule):
            continue
        try:
            key = item.to_adjacency_list(remove_h=False)
        except Exception:
            continue
        seen.setdefault(key, (libname, entry.label, item))
total = len(seen)
print('distinct species (by adjacency list): {0}\n'.format(total))

for name, adj in CANDIDATES:
    g = Group().from_adjacency_list(adj)
    matched = []
    typed = 0
    crashed = 0
    crash_kinds = Counter()
    wrong_product = []
    for key, (libname, label, mol) in seen.items():
        try:
            maps = mol.find_subgraph_isomorphisms(g)
        except Exception:
            continue
        if not maps:
            continue
        q = mol.get_net_charge()
        matched.append((libname, label, q))
        centres = set()
        for mapping in maps:
            for mol_atom, grp_atom in mapping.items():
                if grp_atom.label == '*1':
                    centres.add(mol.atoms.index(mol_atom))
        for i in sorted(centres):
            clone = mol.copy(deep=True)
            clone.atoms[i].label = '*1'
            try:
                RECIPE.apply_forward(clone, unique=True)
                clone.update(sort_atoms=False)
                typed += 1
            except Exception as exc:
                crashed += 1
                crash_kinds[type(exc).__name__] += 1

    print('--- {0}   `{1}`'.format(name, adj))
    print('    species matched : {0} of {1}   (q=0: {2}, q>0: {3}, q<0: {4})'.format(
        len(matched), total,
        sum(1 for _, _, q in matched if q == 0),
        sum(1 for _, _, q in matched if q > 0),
        sum(1 for _, _, q in matched if q < 0)))
    print('    centres labelled: {0} typed, {1} raised {2}'.format(
        typed, crashed, dict(crash_kinds)))
    for libname, label, q in sorted(matched)[:12]:
        print('        q={0:+d}  {1}/{2}'.format(q, libname, label))
    if len(matched) > 12:
        print('        ... {0} more'.format(len(matched) - 12))
    print()
