#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 7 -- what `kinetics_check_sample_can_react` actually exercises.

That check passes for this family both before and after the narrowing, while the
recipe raises `AtomTypeError` at 134616 real centres before it. This probe asks
which molecule the check feeds the recipe, for the old root and the new one.
"""
from rmgpy.molecule import Group
from rmgpy.data.kinetics.family import ReactionRecipe

RECIPE = ReactionRecipe([['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]])

ROOTS = [
    ('old', '1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]'),
    ('new', '1 *1 [H,Li,Na,K] u0 p0 c+1'),
]

for name, adj in ROOTS:
    g = Group().from_adjacency_list(adj)
    sample = g.make_sample_molecule()
    line = ' / '.join(l.strip() for l in sample.to_adjacency_list().strip().splitlines())
    print('{0} root {1!r}'.format(name, adj))
    print('    make_sample_molecule() -> {0}'.format(line))
    print('    sample matches its own group: {0}'.format(
        sample.is_subgraph_isomorphic(g)))
    clone = sample.copy(deep=True)
    for a in clone.atoms:
        if a.label == '*1':
            break
    try:
        RECIPE.apply_forward(clone, unique=True)
        clone.update(sort_atoms=False)
        out = ' / '.join(l.strip() for l in clone.to_adjacency_list().strip().splitlines())
        print('    recipe on the sample   -> {0}'.format(out))
    except Exception as exc:
        print('    recipe on the sample   -> {0}: {1}'.format(type(exc).__name__, exc))
    print()
