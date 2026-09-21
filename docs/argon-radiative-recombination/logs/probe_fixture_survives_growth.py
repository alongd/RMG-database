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

Run three times -- plain, then under each growth shape -- and compare. The plain run must be
green AND non-empty. The grown runs are EXPECTED to have failures: the libraries genuinely no
longer hold what the coverage tests say they hold, and those tests are doing their job by
saying so. What they must not have is **errors**. Errors mean the checks stopped running.

Both growth shapes are exercised, because each previous version of this probe could produce
only the shape that its own fix had already handled:

* ``distinct`` -- same reactants, different products. Defeats a reactant-only selector.
* ``duplicate`` -- same reactants, same products. Defeats *any* key drawn from the reaction,
  and is therefore the case the selector cannot key its way out of; it has to degrade to a
  failure instead. Round 67 caught that this was being argued rather than run.

The runner also refuses to interpret a run that did not finish: pytest's exit code must be
0 or 1, and a run that parsed no outcomes at all is treated as a collection failure rather
than as a clean green.

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

SUMMARY = re.compile(r'(\d+) (passed|failed|error|errors)\b')

# pytest's documented exit codes. Anything else -- a crash, an internal error, a usage
# mistake, a segfault in the engine -- means the numbers scraped from stdout describe a run
# that did not finish, and must not be read as a result.
PYTEST_OK, PYTEST_FAILED = 0, 1
PYTEST_ACCEPTABLE = (PYTEST_OK, PYTEST_FAILED)


class RunError(Exception):
    pass


def run(mode):
    """Run the three test files. ``mode`` is None, 'distinct' or 'duplicate'."""
    argv = [sys.executable, '-m', 'pytest', '-q', '--no-header', '-p', 'no:cacheprovider']
    env = dict(os.environ)
    if mode is not None:
        argv += ['-p', 'grow_library_plugin']
        env['GROW_MODE'] = mode
    argv += FILES
    env['PYTHONPATH'] = HERE + os.pathsep + env.get('PYTHONPATH', '')
    proc = subprocess.run(argv, cwd=ROOT, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout.decode('utf-8', 'replace')

    if proc.returncode not in PYTEST_ACCEPTABLE:
        raise RunError(
            'pytest exited %d for mode=%r, which is not "all passed" or "tests failed". '
            'The counts below describe a run that did not complete and are not a result.'
            '\n\n%s' % (proc.returncode, mode, out[-3000:]))

    counts = {'passed': 0, 'failed': 0, 'error': 0}
    for line in out.splitlines():
        if ' passed' in line or ' failed' in line or 'error' in line:
            for number, word in SUMMARY.findall(line):
                key = 'error' if word.startswith('error') else word
                counts[key] = max(counts[key], int(number))

    # A run reporting nothing is a run that collected nothing. Without this, an import
    # error that stops collection reads as "0 failed, 0 errors" -- a clean green.
    if sum(counts.values()) == 0:
        raise RunError('no test outcomes parsed for mode=%r; collection probably '
                       'failed.\n\n%s' % (mode, out[-3000:]))
    return counts, out


def report(title, counts, expect_failures, note):
    print('%-34s passed=%d failed=%d errors=%d'
          % (title, counts['passed'], counts['failed'], counts['error']))
    print('%-34s %s' % ('', note))
    ok = True
    if counts['error']:
        ok = False
        print('    errors=%d  -> FAIL. A fixture raised during setup: those checks stopped'
              % counts['error'])
        print('                 asserting rather than reporting anything.')
    else:
        print('    errors=0   -> PASS. Every check still ran.')
    if expect_failures:
        if counts['failed']:
            print('    failed=%d   -> PASS. The coverage claims noticed and objected.'
                  % counts['failed'])
        else:
            ok = False
            print('    failed=0   -> FAIL. The library changed and nothing objected.')
    print('')
    return ok


def main():
    print('Three plasma test files. One baseline run, two growth shapes.\n')

    try:
        shipped, _ = run(None)
    except RunError as exc:
        print('BASELINE DID NOT COMPLETE -- nothing below is interpretable.\n%s' % exc)
        return 1

    print('%-34s passed=%d failed=%d errors=%d'
          % ('AS SHIPPED', shipped['passed'], shipped['failed'], shipped['error']))
    if shipped['failed'] or shipped['error']:
        print('\nThe baseline is not green; nothing below is interpretable.')
        return 1
    if shipped['passed'] <= 0:
        print('\nThe baseline passed ZERO tests. A green run of nothing is not a baseline.')
        return 1
    print('%-34s %s\n' % ('', '(the control: this must be green and non-empty)'))

    ok = True
    try:
        distinct, _ = run('distinct')
        ok &= report('GROWN: same reactants, new products', distinct, True,
                     '(the round-66 shape: Ar+ => Ar beside Ar+ => Ar*)')
        duplicate, _ = run('duplicate')
        ok &= report('GROWN: exact duplicate channel', duplicate, True,
                     '(the round-67 shape: no key can separate these; the selector must'
                     ' degrade)')
    except RunError as exc:
        print('A GROWTH RUN DID NOT COMPLETE:\n%s' % exc)
        return 1

    print('PASS' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
