"""Show ``test_a_bond_free_neutral_argon_at_p3_is_u2_or_it_does_not_exist`` RED, then GREEN.

Every other check in this ticket is shown red by perturbing a file in this repository --
a shipped coefficient, a sentence, a forbidden group's label. This one cannot be: what it
guards is ENGINE behaviour, the adjacency-list valency check that refuses u0, u1, u3 and
u4 for a bond-free neutral argon at p3. Breaking that means editing ``rmgpy/``, which this
campaign's rules forbid and which the owner's ruling makes pointless anyway.

So the perturbation is applied IN MEMORY, in this process only, and no file is touched.
``ConsistencyChecker.check_partial_charge`` is replaced with a no-op, which is exactly the
counterfactual the test claims to catch: *an engine that admits a second (u, p, c) at this
atom type*. Under it all five ``u`` values construct and perceive as ``Ar0e``, and the
test's ``list(built) == [2]`` must fail. Restoring the attribute restores the behaviour --
verified here by identity, not assumed, and there is no file state to sweep.

The order is deliberate: GREEN, then RED, then GREEN again. A test that is red before the
perturbation is red for some other reason and proves nothing about the perturbation.

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma:. \\
      /home/alon/anaconda3/envs/rmg_env/bin/python docs/argon-metastable-thermo/u_determined_red_green.py
"""
import importlib.util
import os
import sys

os.environ.setdefault('MPLCONFIGDIR', os.environ.get('TMPDIR', '/tmp'))

from rmgpy.molecule.adjlist import ConsistencyChecker

# Loaded by path, not by `from test... import`: this repository's `test/` has no
# __init__.py, so it is only a namespace-package candidate and Python's own stdlib `test`
# package wins the name no matter where the repository sits on sys.path.
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir))
_suite_path = os.path.join(REPO, 'test', 'test_argon_metastable_thermo.py')
_spec = importlib.util.spec_from_file_location('i221_suite', _suite_path)
_suite = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_suite)
check = _suite.test_a_bond_free_neutral_argon_at_p3_is_u2_or_it_does_not_exist
print('loaded the shipped test from %s' % _suite_path, flush=True)


def run(label):
    try:
        check()
    except AssertionError as exc:
        print('  %-28s RED    AssertionError: %s' % (label, str(exc).splitlines()[0]),
              flush=True)
        return 'red'
    print('  %-28s GREEN' % label, flush=True)
    return 'green'


print('=== the check that guards engine behaviour, shown red without touching rmgpy/ ===',
      flush=True)

original = ConsistencyChecker.check_partial_charge
before = run('unperturbed')

ConsistencyChecker.check_partial_charge = staticmethod(lambda atom: None)
try:
    during = run('valency check disabled')
finally:
    ConsistencyChecker.check_partial_charge = original

assert ConsistencyChecker.check_partial_charge is original, 'the restore did not take'
after = run('restored')

ok = (before, during, after) == ('green', 'red', 'green')
print('\nRESULT: green -> red -> green = %s' % ok, flush=True)
print('No file was modified; the restore is verified by object identity.', flush=True)
sys.exit(0 if ok else 1)
