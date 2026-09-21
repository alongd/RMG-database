#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 13 -- show every test of the pairing family red.

Same discipline as probe 8: break exactly one thing the suite guards, run it,
restore, assert byte-identity. The interesting mutation is N3 -- it swaps in the
SIBLING family's recipe, which still generates a reaction from Ar+, just the
wrong one (the metastable Ar0e). A test that only counted reactions would stay
green through it.
"""
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FAM = os.path.join(ROOT, 'input', 'kinetics', 'families',
                   'Plasma_Radiative_Recombination_Pairing')
GROUPS = os.path.join(FAM, 'groups.py')
RULES = os.path.join(FAM, 'rules.py')
SUITE = os.path.join(ROOT, 'test', 'test_plasma_radiative_recombination_pairing.py')

MUTATIONS = [
    ('N1-drop-LOSE_CHARGE-from-recipe', GROUPS,
     "    ['LOSE_RADICAL', '*1', 1],\n    ['GAIN_PAIR', '*1', 1],\n    ['LOSE_CHARGE', '*1', 1],",
     "    ['LOSE_RADICAL', '*1', 1],\n    ['GAIN_PAIR', '*1', 1],"),
    ('N2-root-widened-to-He-and-Ne', GROUPS,
     '\n1 *1 Ar u1 p3 c+1\n',
     '\n1 *1 [Ar,He,Ne] u1 px c+1\n'),
    ('N3-recipe-swapped-to-the-siblings', GROUPS,
     "    ['LOSE_RADICAL', '*1', 1],\n    ['GAIN_PAIR', '*1', 1],\n    ['LOSE_CHARGE', '*1', 1],",
     "    ['GAIN_RADICAL', '*1', 1],\n    ['LOSE_CHARGE', '*1', 1],"),
    ('N4-root-radical-count-wrong', GROUPS,
     '\n1 *1 Ar u1 p3 c+1\n',
     '\n1 *1 Ar u2 p3 c+1\n'),
    ('N5-rate-anchor-changed', RULES,
     "A = (1.007892e+05, 'm^3/(mol*s)')",
     "A = (1.000000e+05, 'm^3/(mol*s)')"),
]

originals = {}
for path in (GROUPS, RULES):
    with open(path, 'rb') as handle:
        originals[path] = handle.read()

env = dict(os.environ)
env['PYTHONPATH'] = '/home/alon/Code/RMG-Py-plasma'

left_green = []
only = sys.argv[1:] or None
for name, path, old, new in MUTATIONS:
    if only and name not in only:
        continue
    text = originals[path].decode('utf-8')
    assert text.count(old) == 1, '{0}: anchor not unique ({1} hits)'.format(name, text.count(old))
    with open(path, 'w') as handle:
        handle.write(text.replace(old, new))
    print('\n' + '=' * 78)
    print('{0}   [{1}]\n   {2!r}\n-> {3!r}'.format(name, os.path.basename(path), old, new))
    print('=' * 78)
    sys.stdout.flush()
    proc = subprocess.run(
        ['/home/alon/anaconda3/envs/rmg_env/bin/python', '-m', 'pytest', SUITE, '-q',
         '--no-header', '-p', 'no:cacheprovider'],
        cwd=ROOT, env=env, capture_output=True, text=True)
    print(proc.stdout[-7000:])
    if proc.stderr.strip():
        print('--- stderr ---\n{0}'.format(proc.stderr[-2000:]))
    print('EXIT {0}'.format(proc.returncode))
    if proc.returncode == 0:
        left_green.append(name)

    with open(path, 'wb') as handle:
        handle.write(originals[path])
    with open(path, 'rb') as handle:
        assert handle.read() == originals[path], '{0}: restore did not round-trip'.format(name)
    print('restored, byte-identical')

print('\n' + '=' * 78)
if left_green:
    print('MUTATIONS THAT LEFT THE SUITE GREEN: {0}'.format(left_green))
    sys.exit(1)
print('every mutation turned the suite red')
