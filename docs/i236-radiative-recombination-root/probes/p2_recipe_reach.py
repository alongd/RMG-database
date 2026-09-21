#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 2 -- what the family's recipe can and cannot produce.

The brief says the root's `u0` is what keeps Ar+ out, implying that widening the
radical count would let the family do `Ar+ + e- => Ar`.  This probe asks the
engine instead of reasoning about it:

  A. Is the product the recipe would build from Ar+ -- GAIN_RADICAL then
     LOSE_CHARGE, i.e. `Ar u2 p3 c0` -- ground-state argon, or something else?
  B. Which single-centre electron-capture transformations does each of the two
     recipes in this database actually realise?
"""
import os

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))

from rmgpy.molecule import Molecule
from rmgpy.data.kinetics.family import ReactionRecipe


RECIPES = {
    'RR  (GAIN_RADICAL + LOSE_CHARGE)': [['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]],
    'ATT (LOSE_RADICAL  + GAIN_PAIR)':  [['LOSE_RADICAL', '*1', 1], ['GAIN_PAIR', '*1', 1]],
}

CENTRES = [
    ('Li+',        '1 *1 Li u0 p0 c+1'),
    ('Na+',        '1 *1 Na u0 p0 c+1'),
    ('H+',         '1 *1 H  u0 p0 c+1'),
    ('Ar+',        '1 *1 Ar u1 p3 c+1'),
    ('He+',        '1 *1 He u1 p0 c+1'),
    ('Ar  (neut)', '1 *1 Ar u0 p4 c0'),
    ('O   (neut)', '1 *1 O  u2 p2 c0'),
]

for rname, actions in RECIPES.items():
    print('\n=== recipe {0} ==='.format(rname))
    recipe = ReactionRecipe([list(a) for a in actions])
    for label, adj in CENTRES:
        try:
            mol = Molecule().from_adjacency_list(adj)
        except Exception as exc:
            print('  {0:12s} reactant NOT CONSTRUCTIBLE: {1}'.format(label, exc))
            continue
        clone = mol.copy(deep=True)
        try:
            recipe.apply_forward(clone, unique=True)
            clone.update(sort_atoms=False)
            out = ' / '.join(l.strip() for l in
                             clone.to_adjacency_list().strip().splitlines())
            print('  {0:12s} -> {1}'.format(label, out))
        except Exception as exc:
            print('  {0:12s} -> {1}: {2}'.format(label, type(exc).__name__, exc))

print('\n=== is `Ar u2 p3 c0` ground-state argon? ===')
ground = Molecule().from_adjacency_list('1 Ar u0 p4 c0')
for adj in ('1 Ar u2 p3 c0',):
    try:
        m = Molecule().from_adjacency_list(adj)
        m.update(sort_atoms=False)
        print('  {0!r} constructible; atomtype={1}; isomorphic to ground Ar? {2}'.format(
            adj, m.atoms[0].atomtype.label, m.is_isomorphic(ground)))
    except Exception as exc:
        print('  {0!r} -> {1}: {2}'.format(adj, type(exc).__name__, exc))
