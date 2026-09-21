#!/usr/bin/env python
# encoding: utf-8

"""When a plasma library grows a same-reactant channel, do its tests FAIL or vanish?

That distinction is the whole subject. A failing test argues with you. A test that raises
during *fixture setup* is reported by pytest as an ERROR, in a separate section, and asserts
nothing -- so a library growing one entry can remove twenty checks while the run still prints
a green count for the rest. This campaign has now shipped that defect twice:

* first as ``assert len(reactions) == 1`` inside the fixture (I-234, round 59);
* then as the repair for it, which selected by *reactant* labels -- immune to the library
  growing a reaction about some other species, and still ambiguous the moment it grows a
  second channel of the SAME reactant, which is queued work.

**And the probe that was offered as proof of the repair could not have caught the second
one.** It injected its synthetic twin and then renamed the twin's *reactants*, so the twin
never collided with a reactant-keyed selector; it was structurally incapable of failing in
the direction the defect lay. Round 66 caught that. This rewrite fixes both the selector and
the evidence:

1. it grows each library with a twin sharing the original's **reactants** (products renamed),
   which is the collision shape -- see ``grow_library_plugin.py``;
2. it does not reimplement the selector. It runs **pytest itself**, over the real test files,
   so whatever those files actually do is what gets measured. The previous probe kept its own
   copy of the selection logic, and a copy is free to stay correct while the shipped code is
   not.

Run twice -- once plain, once under the growth plugin -- and compare. The plain run must be
green. The grown run is EXPECTED to have failures: the libraries genuinely no longer hold what
the coverage tests say they hold, and those tests are doing their job by saying so. What it
must not have is **errors**. Errors mean the checks stopped running.

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python probe_fixture_survives_growth.py

Exit 0 when the grown run has zero errors and at least one failure; 1 otherwise.
"""

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, os.pardir))

FILES = [
    'test/test_plasma_argon.py',
    'test/test_plasma_electron_impact_ionization.py',
    'test/test_plasma_radiative_recombination.py',
]

SUMMARY = re.compile(r'(\d+) (passed|failed|error|errors|skipped)')


def run(grown):
    argv = [sys.executable, '-m', 'pytest', '-q', '--no-header', '-p', 'no:cacheprovider']
    if grown:
        argv += ['-p', 'grow_library_plugin']
    argv += FILES
    env = dict(os.environ)
    # The plugin lives beside this probe, not on the default path.
    env['PYTHONPATH'] = HERE + os.pathsep + env.get('PYTHONPATH', '')
    proc = subprocess.run(argv, cwd=ROOT, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout.decode('utf-8', 'replace')
    tail = [line for line in out.splitlines() if 'passed' in line or 'failed' in line
            or 'error' in line]
    counts = {'passed': 0, 'failed': 0, 'error': 0}
    for line in tail[-3:]:
        for number, word in SUMMARY.findall(line):
            key = 'error' if word.startswith('error') else word
            if key in counts:
                counts[key] = int(number)
    return counts, out


def main():
    print('Three plasma test files, run twice.\n')

    shipped, shipped_out = run(grown=False)
    print('AS SHIPPED        passed=%(passed)d failed=%(failed)d errors=%(error)d' % shipped)
    if shipped['failed'] or shipped['error']:
        print('\nThe baseline run is not green; nothing below is interpretable.\n')
        print(shipped_out[-4000:])
        return 1

    grown, grown_out = run(grown=True)
    print('LIBRARIES GROWN   passed=%(passed)d failed=%(failed)d errors=%(error)d' % grown)
    print('                  (one twin per reaction: same reactants, products renamed)\n')

    ok = True
    if grown['error']:
        ok = False
        print('  errors=%d  -> FAIL. A fixture raised during setup, so every test it feeds'
              % grown['error'])
        print('              stopped asserting. These are the checks that silently vanish:')
        for line in grown_out.splitlines():
            if line.startswith('ERROR ') or ' ERROR at setup of ' in line:
                print('                %s' % line.strip())
    else:
        print('  errors=0    -> PASS. Every check still ran against the grown library.')

    if grown['failed']:
        print('  failed=%d   -> PASS. The coverage tests noticed the growth and said so,'
              % grown['failed'])
        print('              which is a test arguing with you rather than disappearing.')
    else:
        ok = False
        print('  failed=0    -> FAIL. Growing a library changed what it holds and NOTHING')
        print('              objected; the coverage claims are not being checked.')

    print('')
    print('PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
