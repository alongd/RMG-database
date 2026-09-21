#!/usr/bin/env python
# encoding: utf-8
"""
Show every new or repaired check RED, then GREEN.

This campaign has found seven checks that could not fail in the direction the defect lay.
Four of them were in this very file's suite, which is why this driver exists: a test that
has never been observed to fail is a claim, not a check.

For each case below it breaks THE THING THE CHECK GUARDS -- a shipped coefficient, a
sentence in the entry, a forbidden group's label, a family's membership of ``default`` --
runs the named tests and records the failure, then restores the file, verifies the restore
by SHA rather than by assumption, and runs the same tests green.

Deliberately NOT done: editing the tests to make them fail. A check shown red by rewriting
its own assertion has demonstrated nothing.

The restore is verified by hashing the file before and after, not by ``git stash`` and not
by ``git checkout``: several of these files are already modified relative to HEAD, so a
git-based restore would revert the work under test, and a worker on this campaign has
already had a stash silently fail to revert.

TWO GUARDS ADDED AFTER THIS SCRIPT FAILED ONCE, AND THE FAILURE IS WORTH READING.
The first run was launched in the background, appeared to die, and was re-launched. It had
not died. Two instances then perturbed and restored the SAME files concurrently, each
"verifying" its restore against a baseline the other had already moved -- so every case
reported red-then-green correctly and an ``ArH`` entry was left in the shipped thermo
library, where it was committed. Per-case SHA verification is not enough when the baseline
itself can be moved underneath you. So:

* a **lock file**, refusing to start while another instance holds it; and
* a **contamination sweep** at the end over every file this script can touch, for the
  marker strings it writes. A restore that silently fails now fails loudly here.

The sweep is the one that would have caught it, and it is cheap. It runs even when a case
raises.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/red_green.py \
        > >(tee -a docs/argon-metastable-thermo/logs/red_green.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/red_green.stderr.log >&2)
"""

import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, os.pardir))
PYTEST = '/home/alon/anaconda3/envs/rmg_env/bin/pytest'
SUITE = 'test/test_argon_metastable_thermo.py'

LIB = 'input/thermo/libraries/PlasmaExcitedNeutralThermo.py'
BIRAD = 'input/kinetics/families/Birad_R_Recombination/groups.py'
RECOMMENDED = 'input/kinetics/families/recommended.py'

#: (name, file, old, new, [tests]) -- `old` must appear exactly once.
CASES = [
    ('a wrong shipped H298 (a6 coefficient moved)', LIB,
     '133267.5845721773, 5.9890428524', '134000.0, 5.9890428524',
     ['test_the_level_energy_in_ev_matches_what_the_plasma_literature_quotes',
      'test_h298_is_the_level_energy_times_hc_na']),

    ('a wrong 1s3 level in the shipped alternatives table', LIB,
     '1s3      3P0   (2P*<1/2>).4s  2[1/2]*  J=0     94553.6652',
     '1s3      3P0   (2P*<1/2>).4s  2[1/2]*  J=0     94552.0000',
     ['test_the_two_metastable_levels_are_separated_by_the_asd_gap']),

    ('a wrong R*ln term in the shipped lumping prose', LIB,
     '(R*ln term 0.0018, <E>/RT term 0.0126)',
     '(R*ln term 0.0028, <E>/RT term 0.0126)',
     ['test_r_ln_q_alone_understates_the_lumping_difference_by_almost_eightfold']),

    ('a wrong crossing temperature in the shipped prose', LIB,
     'It crosses 0.01 at 281 K', 'It crosses 0.01 at 291 K',
     ['test_where_the_lumping_difference_crosses_the_precision_we_quote']),

    ('a wrong shipped Cp (a1 coefficient moved)', LIB,
     'coeffs = [2.5, 0.0, 0.0, 0.0, 0.0,', 'coeffs = [3.0, 0.0, 0.0, 0.0, 0.0,',
     ['test_thermodata_freezes_entropy_whenever_the_last_cp_slope_is_nonpositive',
      'test_cp_is_exactly_five_halves_r_at_every_tabulated_temperature']),

    ('a disclosed anchor number that drifts from the measurement', LIB,
     'dS298(Ar -> Ar(3P2)) =   13.4922 J/(mol*K)',
     'dS298(Ar -> Ar(3P2)) =   13.4000 J/(mol*K)',
     ['test_the_anchor_error_the_engine_delivers_is_the_one_the_library_discloses']),

    ('the superseded anchor pair put back beside the live one', LIB,
     'and goes red if the resolved anchor moves.',
     'and goes red if the resolved anchor moves. (Previously dS = 13.5027, +0.1211.)',
     ['test_the_anchor_error_the_engine_delivers_is_the_one_the_library_discloses']),

    ('the retraction removed from the entry', LIB,
     'is RETRACTED, and what replaces it', 'is revised, and what replaces it',
     ['test_the_library_retracts_the_one_family_claim_and_carries_the_reach_figure']),

    ('a covalent argon given thermo by a library entry', LIB,
     'entry(\n    index = 0,\n    label = "Ar(3P2)",',
     'entry(\n    index = 1,\n    label = "ArH",\n    molecule =\n'
     '"""\nmultiplicity 2\n1 Ar u1 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n""",\n'
     '    thermo = NASA(\n        polynomials = [\n            NASAPolynomial(\n'
     '                coeffs = [3.5, 0.0, 0.0, 0.0, 0.0, 100000.0, 5.0],\n'
     '                Tmin = (200, \'K\'),\n                Tmax = (6000, \'K\'),\n'
     '            ),\n        ],\n        Tmin = (200, \'K\'),\n'
     '        Tmax = (6000, \'K\'),\n        Cp0 = (29.1, \'J/(mol*K)\'),\n'
     '        CpInf = (29.1, \'J/(mol*K)\'),\n    ),\n'
     '    shortDesc = u"RED-GREEN PERTURBATION, NOT REAL DATA",\n'
     '    longDesc = u"""RED-GREEN PERTURBATION""",\n)\n\n'
     'entry(\n    index = 0,\n    label = "Ar(3P2)",',
     ['test_a_covalent_neutral_argon_cannot_be_given_a_number_by_construction',
      'test_the_products_those_families_used_to_build_still_have_no_thermo']),

    ('the containment group left unlabelled, so it matches nothing', BIRAD,
     '1 *2 Ar u2 p3 c0', '1 Ar u2 p3 c0',
     ['test_the_containment_is_written_where_each_family_already_says_it_belongs',
      'test_no_ordinary_family_reaches_the_metastable_any_more',
      'test_the_only_kinetics_files_that_MENTION_the_metastable_are_the_five_containments']),

    ('the containment widened until it eats the chemistry the family is for', BIRAD,
     '1 *2 Ar u2 p3 c0', '1 *2 R!H u2',
     ['test_the_containment_does_not_move_the_chemistry_those_families_exist_for']),

    ('a contained family quietly dropped from the default set', RECOMMENDED,
     "    'CO_Disproportionation',\n    'Birad_R_Recombination',",
     "    'Birad_R_Recombination',",
     ['test_four_of_the_five_ordinary_families_are_in_the_default_recommended_set']),

    ('the one plasma family that reaches it, contained too', BIRAD, None, None,
     ['test_exactly_one_PLASMA_family_reaches_it_which_is_not_the_same_as_one_family']),
]

#: The last case perturbs a file that does not yet exist, so it is written whole.
EII_GROUPS = 'input/kinetics/families/Plasma_Electron_Impact_Ionization/groups.py'
EII_BLOCK = '''

forbidden(
    label = "RED_GREEN_PERTURBATION",
    group =
"""
1 *1 Ar u2 p3 c0
""",
    shortDesc = """RED-GREEN PERTURBATION""",
    longDesc = """RED-GREEN PERTURBATION""",
)
'''


def sha(path):
    with open(path, 'rb') as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def run_tests(tests):
    args = [PYTEST, '-q', '--no-header', '-p', 'no:cacheprovider']
    args += ['%s::%s' % (SUITE, t) for t in tests]
    env = dict(os.environ)
    env['PYTHONPATH'] = '/home/alon/Code/RMG-Py-plasma'
    env.setdefault('MPLCONFIGDIR', tempfile.gettempdir())
    proc = subprocess.run(args, cwd=REPO, capture_output=True, text=True, env=env)
    tail = [ln for ln in proc.stdout.splitlines()
            if ln.startswith('FAILED') or ln.startswith('ERROR')
            or ' passed' in ln or ' failed' in ln or ' error' in ln]
    return proc.returncode, tail


def banner(text):
    print("\n" + "=" * 78)
    print(text)
    print("=" * 78)


#: Strings this script writes into repository files. None may survive it.
MARKERS = ['RED-GREEN PERTURBATION', 'RED_GREEN_PERTURBATION', 'label = "ArH"',
           '134000.0, 5.9890428524', 'coeffs = [3.0, 0.0', '94552.0000',
           'R*ln term 0.0028', 'It crosses 0.01 at 291 K', '13.4000 J/(mol*K)',
           'Previously dS = 13.5027', 'is revised, and what replaces it']
TOUCHABLE = sorted({LIB, BIRAD, RECOMMENDED, EII_GROUPS})

#: Cases 10 and 11 do not ADD a marker, they REPLACE one - unlabelling the containment
#: group, and widening it to R!H. There is nothing distinctive to grep for afterwards, so
#: these are positive checks instead: the labelled group must be there, exactly once.
#: (An earlier version tried to catch them with the markers `1 Ar u2 p3 c0` and
#: `1 *2 R!H u2`, which are the entry's own molecule and the family's own Birad group -
#: the sweep correctly refused to start and the markers were the thing that was wrong.)
MUST_CONTAIN = {
    'input/kinetics/families/Birad_R_Recombination/groups.py': '1 *2 Ar u2 p3 c0',
    'input/kinetics/families/R_Addition_MultipleBond/groups.py': '1 *3 Ar u2 p3 c0',
    'input/kinetics/families/Disproportionation/groups.py': '1 *1 Ar u2 p3 c0',
    'input/kinetics/families/CO_Disproportionation/groups.py': '1 *1 Ar u2 p3 c0',
    'input/kinetics/families/Cl_Abstraction/groups.py': '1 *3 Ar u2 p3 c0',
    'input/thermo/libraries/PlasmaExcitedNeutralThermo.py': 'label = "Ar(3P2)"',
}

LOCK = os.path.join(REPO, 'docs', 'argon-metastable-thermo', '.red_green.lock')


def sweep():
    """Every marker this script writes, hunted in every file it can touch.

    Per-case SHA verification checks a restore against a baseline. This checks the RESULT,
    which is the thing that actually matters and the thing that was wrong the one time
    this script failed."""
    found = []
    for rel in TOUCHABLE:
        path = os.path.join(REPO, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as handle:
            text = handle.read()
        for marker in MARKERS:
            if marker in text:
                found.append((rel, marker))
    # ... and the positive checks, for the cases that replace rather than add.
    for rel, required in sorted(MUST_CONTAIN.items()):
        with open(os.path.join(REPO, rel), encoding='utf-8') as handle:
            text = handle.read()
        if text.count(required) != 1:
            found.append((rel, 'MISSING or DUPLICATED: %r (%d)'
                          % (required, text.count(required))))
    with open(os.path.join(REPO, RECOMMENDED), encoding='utf-8') as handle:
        if "'CO_Disproportionation'," not in handle.read():
            found.append((RECOMMENDED, "MISSING 'CO_Disproportionation'"))
    return found


try:
    fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
except FileExistsError:
    with open(LOCK) as handle:
        holder = handle.read().strip()
    sys.exit("refusing to start: %s exists (pid %s). Two instances perturbing the same "
             "files is exactly how this script failed once. Remove the lock only after "
             "confirming no other run is alive." % (LOCK, holder))

pre = sweep()
if pre:
    os.unlink(LOCK)
    sys.exit("refusing to start: the tree already contains perturbation markers, so a "
             "baseline taken now would bake them in: %s" % pre)

results = []
for name, rel, old, new, tests in CASES:
    path = os.path.join(REPO, rel)
    banner("CASE: %s\n  file : %s\n  tests: %s" % (name, rel, ', '.join(tests)))

    fd, backup = tempfile.mkstemp(prefix='redgreen-')
    os.close(fd)
    shutil.copy2(path, backup)
    before = sha(path)

    try:
        if old is None:
            # the final case appends a forbidden group to the EII family instead
            target = os.path.join(REPO, EII_GROUPS)
            fd2, backup2 = tempfile.mkstemp(prefix='redgreen-eii-')
            os.close(fd2)
            shutil.copy2(target, backup2)
            before2 = sha(target)
            with open(target, 'a', encoding='utf-8') as handle:
                handle.write(EII_BLOCK)
            print("  perturbed: appended a forbidden group to %s" % EII_GROUPS)
        else:
            with open(path, encoding='utf-8') as handle:
                text = handle.read()
            count = text.count(old)
            assert count == 1, ('%s: anchor appears %d times, not once' % (name, count))
            with open(path, 'w', encoding='utf-8') as handle:
                handle.write(text.replace(old, new))
            print("  perturbed: %r -> %r" % (old[:70], new[:70]))

        code, tail = run_tests(tests)
        print("  RED   exit=%d" % code)
        for line in tail:
            print("        %s" % line)
        red_ok = code != 0
    finally:
        if old is None:
            shutil.copy2(backup2, target)
            os.unlink(backup2)
            assert sha(target) == before2, 'RESTORE FAILED for %s' % EII_GROUPS
            print("  restored %s, sha verified" % EII_GROUPS)
        shutil.copy2(backup, path)
        os.unlink(backup)
        assert sha(path) == before, 'RESTORE FAILED for %s' % rel
        print("  restored %s, sha verified" % rel)

    code, tail = run_tests(tests)
    print("  GREEN exit=%d" % code)
    for line in tail:
        print("        %s" % line)
    green_ok = code == 0

    results.append((name, red_ok, green_ok))
    print("  VERDICT: red=%s green=%s" % ('YES' if red_ok else 'NO -- CANNOT FAIL',
                                          'YES' if green_ok else 'NO'))

banner("CONTAMINATION SWEEP")
os.unlink(LOCK)
leftovers = sweep()
if leftovers:
    print("  LEFTOVER PERTURBATIONS -- DO NOT COMMIT:")
    for rel, marker in leftovers:
        print("      %s  <- %r" % (rel, marker))
else:
    print("  clean: none of %d markers survives in any of the %d files this script touches"
          % (len(MARKERS), len(TOUCHABLE)))

banner("SUMMARY")
bad = len(leftovers)
for name, red_ok, green_ok in results:
    flag = 'ok  ' if (red_ok and green_ok) else 'BAD '
    if not (red_ok and green_ok):
        bad += 1
    print("  %s red=%-3s green=%-3s  %s" % (flag, 'yes' if red_ok else 'NO',
                                            'yes' if green_ok else 'NO', name))
print("\n  cases: %d, failed to demonstrate: %d, leftover perturbations: %d"
      % (len(results), bad - len(leftovers), len(leftovers)))

dirty = subprocess.run(['git', '-C', REPO, 'status', '--porcelain'],
                       capture_output=True, text=True).stdout
print("\n  git status --porcelain after the run:")
for line in dirty.splitlines():
    print("      %s" % line)
sys.exit(1 if bad else 0)
