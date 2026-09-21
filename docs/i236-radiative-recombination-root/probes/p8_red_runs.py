#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 8 -- show every new test red.

For each mutation: break exactly one thing the suite guards, run the suite,
record the outcome, restore the file, and assert byte-identity with what was
there before. A `git stash`-style round trip is deliberately not used -- the
restore is verified by comparing bytes.
"""
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
GROUPS = os.path.join(ROOT, 'input', 'kinetics', 'families',
                      'Plasma_Radiative_Recombination', 'groups.py')
SUITE = os.path.join(ROOT, 'test', 'test_plasma_radiative_recombination_family.py')

MUTATIONS = [
    ('M1-root-reverted-to-pre-I236',
     '1 *1 [H,Li,Na,K] u0 p0 c+1',
     '1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]'),
    ('M2-root-widened-by-one-element',
     '1 *1 [H,Li,Na,K] u0 p0 c+1',
     '1 *1 [H,Li,Na,K,N] u0 p0 c+1'),
    ('M3-recipe-swapped-to-pairing',
     "    ['GAIN_RADICAL', '*1', 1],\n    ['LOSE_CHARGE', '*1', 1],",
     "    ['LOSE_RADICAL', '*1', 1],\n    ['GAIN_PAIR', '*1', 1],"),
    ('M4-electrons-zeroed',
     '\nelectrons = -1\n',
     '\nelectrons = 0\n'),
]

with open(GROUPS, 'rb') as handle:
    original = handle.read()

env = dict(os.environ)
env['PYTHONPATH'] = '/home/alon/Code/RMG-Py-plasma'

failed_to_break = []
only = sys.argv[1:] or None
for name, old, new in MUTATIONS:
    if only and name not in only:
        continue
    text = original.decode('utf-8')
    assert text.count(old) == 1, '{0}: anchor not unique ({1} hits)'.format(name, text.count(old))
    with open(GROUPS, 'w') as handle:
        handle.write(text.replace(old, new))
    print('\n' + '=' * 78)
    print('{0}\n   {1!r}\n-> {2!r}'.format(name, old, new))
    print('=' * 78)
    sys.stdout.flush()
    proc = subprocess.run(
        ['/home/alon/anaconda3/envs/rmg_env/bin/python', '-m', 'pytest', SUITE, '-q',
         '--no-header', '-p', 'no:cacheprovider'],
        cwd=ROOT, env=env, capture_output=True, text=True)
    print(proc.stdout[-6000:])
    if proc.stderr.strip():
        print('--- stderr ---')
        print(proc.stderr[-3000:])
    print('EXIT {0}'.format(proc.returncode))
    if proc.returncode == 0:
        failed_to_break.append(name)

    with open(GROUPS, 'wb') as handle:
        handle.write(original)
    with open(GROUPS, 'rb') as handle:
        assert handle.read() == original, '{0}: restore did not round-trip'.format(name)
    print('restored, byte-identical')

print('\n' + '=' * 78)
if failed_to_break:
    print('MUTATIONS THAT LEFT THE SUITE GREEN: {0}'.format(failed_to_break))
    sys.exit(1)
print('every mutation turned the suite red')
