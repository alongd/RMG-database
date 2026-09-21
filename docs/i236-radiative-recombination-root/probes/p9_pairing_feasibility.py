#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 9 -- post-mortem on the M3 load failure, and feasibility of a
pairing-recipe family.

M3 (probe 8) swapped the recipe to LOSE_RADICAL + GAIN_PAIR while leaving the
root at `u0`, and the family stopped loading. This probe asks whether that was a
grammar limit or an authoring error, by applying the candidate recipes to
candidate ROOT GROUPS directly -- which is what `generate_product_template` does
at load time -- and by checking the atom-type table entries each action needs.
"""
import os
import traceback

from rmgpy.molecule import Group, Molecule
from rmgpy.molecule.atomtype import ATOMTYPES
from rmgpy.data.kinetics.family import ReactionRecipe

PAIRING_2 = [['LOSE_RADICAL', '*1', 1], ['GAIN_PAIR', '*1', 1]]
PAIRING_3 = [['LOSE_RADICAL', '*1', 1], ['GAIN_PAIR', '*1', 1], ['LOSE_CHARGE', '*1', 1]]
EMPTY_ORBITAL = [['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]]

ROOTS = [
    ('M3 as mutated: u0 root + pairing recipe', '1 *1 [H,Li,Na,K] u0 p0 c+1', PAIRING_2),
    ('u1 root + pairing recipe (2 actions)',    '1 *1 Ar u1 p3 c+1',          PAIRING_2),
    ('u1 root + pairing recipe (3 actions)',    '1 *1 Ar u1 p3 c+1',          PAIRING_3),
    ('u1 root, px lone pairs',                  '1 *1 Ar u1 px c+1',          PAIRING_2),
    ('u1 root, element union with He/Ne',       '1 *1 [Ar,He,Ne] u1 px c+1',  PAIRING_2),
    ('u1 root + empty-orbital recipe',          '1 *1 Ar u1 p3 c+1',          EMPTY_ORBITAL),
]

print('=== applying the recipe to the ROOT GROUP, which is what family.py:1077 does ===')
for name, adj, actions in ROOTS:
    print('\n--- {0}\n    group  {1}\n    recipe {2}'.format(
        name, adj, [a[0] for a in actions]))
    try:
        group = Group().from_adjacency_list(adj)
    except Exception as exc:
        print('    group itself does not parse: {0}: {1}'.format(type(exc).__name__, exc))
        continue
    recipe = ReactionRecipe([list(a) for a in actions])
    try:
        recipe.apply_forward(group, unique=False)
        print('    product template -> {0}'.format(
            ' / '.join(l.strip() for l in group.to_adjacency_list().strip().splitlines())))
    except Exception as exc:
        print('    RAISES {0}: {1}'.format(type(exc).__name__, exc))
        tb = traceback.format_exc().strip().splitlines()
        print('    innermost frame: {0}'.format(tb[-3].strip() if len(tb) > 3 else tb[-1]))

print('\n\n=== and to the SPECIES, which is what apply_recipe does at generation ===')
SPECIES = [
    ('Ar+', 'multiplicity 2\n1 *1 Ar u1 p3 c+1'),
    ('He+', 'multiplicity 2\n1 *1 He u1 p0 c+1'),
    ('Ne+', 'multiplicity 2\n1 *1 Ne u1 p3 c+1'),
    ('Ar  (neutral)', '1 *1 Ar u0 p4 c0'),
    ('Li+', '1 *1 Li u0 p0 c+1'),
]
ground_ar = Molecule().from_adjacency_list('1 Ar u0 p4 c0')
ground_ar.update(sort_atoms=False)

for rname, actions in (('PAIRING (2 actions)', PAIRING_2), ('PAIRING (3 actions)', PAIRING_3)):
    print('\n--- recipe {0}: {1}'.format(rname, [a[0] for a in actions]))
    for label, adj in SPECIES:
        mol = Molecule().from_adjacency_list(adj)
        recipe = ReactionRecipe([list(a) for a in actions])
        try:
            recipe.apply_forward(mol, unique=True)
            mol.update(sort_atoms=False)
            out = ' / '.join(l.strip() for l in mol.to_adjacency_list().strip().splitlines())
            extra = ''
            if label == 'Ar+':
                extra = '   isomorphic to ground-state Ar? {0}'.format(mol.is_isomorphic(ground_ar))
            print('    {0:14s} -> {1}{2}'.format(label, out, extra))
        except Exception as exc:
            print('    {0:14s} -> {1}: {2}'.format(label, type(exc).__name__, exc))

print('\n\n=== atom-type table rows each action needs ===')
for element in ('Ar', 'He', 'Ne', 'H', 'Li'):
    at = ATOMTYPES[element]
    print('  {0:3s} decrement_radical={1!s:12s} increment_lone_pair={2!s:12s} '
          'decrement_charge={3!s}'.format(
              element,
              [a.label for a in at.decrement_radical],
              [a.label for a in at.increment_lone_pair],
              [a.label for a in at.decrement_charge]))
