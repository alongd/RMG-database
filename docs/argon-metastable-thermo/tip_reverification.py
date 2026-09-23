#!/usr/bin/env python
# encoding: utf-8
"""Round 118 HIGH 1: re-establish the verification at the TIP, re-runnably.

This branch was recorded VERIFIED at ``9c2e8fe27``. It was then rebased, so that commit is
not an ancestor of the tip; its byte-identical twin is ``025536186``, and everything after
that is branch-owned and had never been checked against the tree being merged.

A verification stated in a commit message is attached to a commit. A rebase, a squash or a
cherry-pick detaches it, and nothing notices -- which is exactly what happened here. So the
re-verification is written as a program instead: it reads the artifacts out of the WORKING
TREE, names the check that covers each one, proves that check still exists and still has
the shape it is credited with, and measures the containment live. Run it at any commit and
it answers for that commit.

For each artifact it reports:

    identity     path and the git blob sha of the bytes actually examined
    does         what the artifact is for
    checked by   the named tests/probes, each verified to EXIST (a renamed or deleted test
                 fails this probe rather than silently leaving the artifact uncovered)
    would catch  what a wrong version of this artifact would trip

EXIT CODE IS THE CHECK: 0 only if every artifact is present, every named check resolves,
all eleven containment barriers are attached with their mapped labels, and the two negative
controls hold. Anything this probe cannot establish is printed as CANNOT VERIFY and is
fatal -- an unverifiable artifact must not read the same as a verified one, which is the
whole lesson of the round it was written in.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-mgr-i221-deck-probe-234349 \\
        python docs/argon-metastable-thermo/tip_reverification.py \\
        > >(tee docs/argon-metastable-thermo/logs/tip_reverification.stdout.log) \\
        2> >(tee docs/argon-metastable-thermo/logs/tip_reverification.stderr.log >&2)
"""

import importlib.util
import os
import subprocess
import sys

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))
DATABASE = os.path.join(REPO, 'input')
settings['database.directory'] = DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402
from rmgpy.molecule import Molecule                         # noqa: E402

#: The commit the recorded verification actually reaches. Everything this probe covers was
#: added after it.
VERIFIED_THROUGH = '025536186'

CONTAINMENT = 'Ar_metastable_biradical'
EII = 'Plasma_Electron_Impact_Ionization'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
AR_GROUND = '1 Ar u0 p4 c0\n'
METHYL = 'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n' \
         '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'

#: family -> the label of the group atom the shipped matcher maps metastable argon onto.
#: This is a RECORD of the derivation in `template_space_derivation.py`, not a hand-made
#: list; `template_space_derivation.py` is what says the set is complete, and the test in
#: `test_argon_metastable_thermo.py` is what keeps the two in step.
BARRIERS = {'Birad_R_Recombination': '*2', 'Cation_NO_Substitution': '*2',
            'Li_NO_Substitution': '*2', 'Br_Abstraction': '*3', 'Cl_Abstraction': '*3',
            'F_Abstraction': '*3', 'R_Addition_MultipleBond': '*3',
            'CO_Disproportionation': '*1', 'Disproportionation': '*1',
            'Disproportionation-Y': '*1', 'Surface_Adsorption_Double': '*1'}

THERMO_TESTS = 'test/test_argon_metastable_thermo.py'
EII_TESTS = 'test/test_eii_quarantine.py'
BUILD_TESTS = 'test/test_argon_cation_buildtime.py'

#: artifact -> (what it does, [(file, callable name)], what would catch it being wrong)
ARTIFACTS = [
    ('the eleven family groups.py barriers',
     ['input/kinetics/families/%s/groups.py' % label for label in sorted(BARRIERS)],
     'Each adds one forbidden group, `Ar_metastable_biradical`, at the template position '
     'the shipped matcher maps Ar(3P2) onto, so the family refuses to generate with it.',
     [(THERMO_TESTS, 'test_every_family_whose_template_admits_the_metastable_is_forbidden'),
      (THERMO_TESTS, 'test_the_containment_does_not_move_the_chemistry_those_families_exist_for'),
      (THERMO_TESTS, 'test_a_template_slot_that_cannot_be_evaluated_refuses_the_derivation')],
     'A barrier at the wrong template position, or missing from a family whose template '
     'admits the species, fails the derivation test: it compares the DERIVED set against '
     'the contained set rather than enumerating known families. A barrier that is too '
     'broad fails the chemistry controls, which generate each family\'s own reactions.'),

    ('the EII quarantine manifest',
     ['input/kinetics/families/%s/quarantine.py' % EII],
     'Declares Plasma_Electron_Impact_Ionization quarantined for quantitative use, with '
     'the kinetics class the refusal keys on and the engine capability it requires.',
     [(EII_TESTS, 'test_this_runtime_ENFORCES_the_declared_engine_requirement'),
      (EII_TESTS, 'test_this_runtime_ENFORCES_the_pin_as_more_than_an_attribute_lookup')],
     'The tests require a real exception out of the real admission path, so a manifest '
     'that parses but gates nothing fails them. A manifest naming a capability the '
     'runtime lacks fails the enforcement pair rather than passing quietly.'),

    ('the metastable thermo entry',
     ['input/thermo/libraries/PlasmaExcitedNeutralThermo.py'],
     'One library entry: argon 4s 3P2 (Paschen 1s5), H298 from the NIST ASD level energy, '
     'S298 = JANAF ground-state entropy + R ln 5, Cp = 5/2 R.',
     [(THERMO_TESTS, 'test_h298_is_the_level_energy_times_hc_na'),
      (THERMO_TESTS, 'test_s298_is_the_ground_state_plus_the_exact_degeneracy_term'),
      (THERMO_TESTS, 'test_the_e0_gap_is_the_thermal_enthalpy_and_not_the_298_convention'),
      (THERMO_TESTS, 'test_the_entry_is_the_1s5_level_and_says_so'),
      (THERMO_TESTS, 'test_the_resonant_levels_are_excluded_on_lifetime_not_on_taste')],
     'Every number is re-derived from the identity that produced it, so a changed digit '
     'fails arithmetic rather than a remembered constant. The state identity is pinned '
     'separately, so an entry that drifted into meaning a different argon level -- which '
     'would still load and still match -- fails too.'),

    ('the three test files themselves',
     [THERMO_TESTS, EII_TESTS, BUILD_TESTS],
     'The executable half of docs/argon-metastable-thermo/report.md: every re-derivable '
     'number in the report is re-derived here.',
     [(THERMO_TESTS, 'test_an_arkane_structure_only_declaration_reports_ready_with_a_zero_partition_function'),
      (THERMO_TESTS, 'test_a_template_slot_that_cannot_be_evaluated_refuses_the_derivation'),
      (BUILD_TESTS, 'test_at_build_time_with_the_reference_deck_argon_is_refused_loudly')],
     'What checks a test is its red state and its anti-vacuity control. Round 118 found '
     'two tests that had neither: the Q=0 test built the conformer it then asserted on '
     '(it now goes through arkane.input, so Arkane produces the zero), and the '
     'completeness test could pass over a family its matcher could not evaluate (it now '
     'refuses). Both are named here because they are the two whose coverage was a claim '
     'rather than a measurement.'),
]


def blob(path):
    try:
        return subprocess.check_output(
            ['git', '-C', REPO, 'rev-parse', 'HEAD:%s' % path],
            stderr=subprocess.DEVNULL).decode().strip()[:12]
    except subprocess.CalledProcessError:
        return None


def added_after_verification(path):
    """True if `path` was touched after the commit the recorded verification reaches."""
    out = subprocess.check_output(
        ['git', '-C', REPO, 'log', '--oneline', '%s..HEAD' % VERIFIED_THROUGH, '--', path]
    ).decode().strip()
    return bool(out), len(out.splitlines())


def load_test_module(relative):
    path = os.path.join(REPO, relative)
    spec = importlib.util.spec_from_file_location(
        'reverify_' + os.path.basename(relative)[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def molecule(adjlist):
    mol = Molecule().from_adjacency_list(adjlist)
    mol.update_atomtypes()
    return mol


def main():
    problems = []

    print('re-verifying the working tree at %s' % (blob('.') or 'HEAD'), flush=True)
    print('the recorded verification reaches %s; everything below is after it\n'
          % VERIFIED_THROUGH, flush=True)

    modules = {}
    for relative in (THERMO_TESTS, EII_TESTS, BUILD_TESTS):
        try:
            modules[relative] = load_test_module(relative)
        except Exception as exc:                            # noqa: BLE001
            problems.append('CANNOT VERIFY: %s did not import: %s: %s'
                            % (relative, type(exc).__name__, exc))

    for title, paths, does, checks, would_catch in ARTIFACTS:
        print('=== %s' % title, flush=True)
        print('    does        : %s' % does, flush=True)
        for path in paths:
            sha = blob(path)
            touched, commits = added_after_verification(path)
            if sha is None:
                problems.append('CANNOT VERIFY: %s is not in the tree' % path)
                print('    MISSING     : %s' % path, flush=True)
                continue
            print('    identity    : %-68s blob %s  (%d commit%s after %s)'
                  % (path, sha, commits, '' if commits == 1 else 's', VERIFIED_THROUGH),
                  flush=True)
            if not touched:
                problems.append(
                    '%s was NOT touched after %s; this probe claims to cover the '
                    'post-verification artifacts and this one is not among them'
                    % (path, VERIFIED_THROUGH))
        for relative, name in checks:
            module = modules.get(relative)
            if module is None:
                continue
            if not hasattr(module, name):
                problems.append('CANNOT VERIFY: %s::%s does not exist, so the artifact '
                                'above is credited to a check that is not there'
                                % (relative, name))
                print('    checked by  : %s::%s   <-- MISSING' % (relative, name),
                      flush=True)
            else:
                print('    checked by  : %s::%s' % (relative, name), flush=True)
        print('    would catch : %s\n' % would_catch, flush=True)

    # ---- the containment, measured rather than asserted from the table ----------------
    print('=== the eleven barriers, measured in the loaded database', flush=True)
    db = KineticsDatabase()
    db.load_families(os.path.join(DATABASE, 'kinetics', 'families'), families='all')
    print('    families loaded: %d' % len(db.families), flush=True)

    meta, ground, methyl = molecule(AR_META), molecule(AR_GROUND), molecule(METHYL)
    for label in sorted(BARRIERS):
        family = db.families.get(label)
        if family is None:
            problems.append('CANNOT VERIFY: family %s is not loaded' % label)
            continue
        forbidden = family.forbidden
        if forbidden is None or CONTAINMENT not in forbidden.entries:
            problems.append('%s does not carry %s' % (label, CONTAINMENT))
            print('    %-30s NO BARRIER' % label, flush=True)
            continue
        group = forbidden.entries[CONTAINMENT].item
        labels = sorted({atom.label for atom in getattr(group, 'atoms', []) if atom.label})
        expected = BARRIERS[label]
        ok = expected in labels
        if not ok:
            problems.append('%s maps the barrier onto %s, expected %s'
                            % (label, labels, expected))
        print('    %-30s barrier present, labels %-12s expected %s  %s'
              % (label, labels or '-', expected, 'ok' if ok else '<-- WRONG'), flush=True)

    # ---- the two negative controls ---------------------------------------------------
    print('\n=== negative controls (the containment must not be about argon, or about '
          'radicals)', flush=True)
    # Anti-vacuity first: the metastable itself MUST be caught, or "ground-state argon is
    # caught in 0 of 11" is a statement about a comparison that cannot come out positive.
    positive = [label for label in sorted(BARRIERS)
                if db.families.get(label) is not None
                and db.families[label].forbidden is not None
                and CONTAINMENT in db.families[label].forbidden.entries
                and meta.is_subgraph_isomorphic(
                    db.families[label].forbidden.entries[CONTAINMENT].item)]
    print('    %-20s forbidden in %d of %d families  %s'
          % ('THE METASTABLE', len(positive), len(BARRIERS),
             'ok' if len(positive) == len(BARRIERS) else '<-- the controls below are '
             'vacuous: the comparison cannot come out positive'), flush=True)
    if len(positive) != len(BARRIERS):
        problems.append('the metastable is caught by only %d of %d barriers, so the '
                        'negative controls prove nothing' % (len(positive), len(BARRIERS)))
    for name, mol in (('ground-state argon', ground), ('methyl radical', methyl)):
        forbidding = []
        for label in sorted(BARRIERS):
            family = db.families.get(label)
            forbidden = family.forbidden if family is not None else None
            if forbidden is None or CONTAINMENT not in forbidden.entries:
                continue
            try:
                # `mol.is_subgraph_isomorphic(group)` is the direction the forbidden check
                # itself uses; `group.is_isomorphic(mol)` raises TypeError on a Molecule,
                # which the CANNOT VERIFY guard below caught on this probe's first run --
                # the control had been reporting "forbidden in 0 of 11" without evaluating
                # anything at all.
                if mol.is_subgraph_isomorphic(forbidden.entries[CONTAINMENT].item):
                    forbidding.append(label)
            except Exception:                               # noqa: BLE001
                # A control that cannot be evaluated is not a control that passed.
                problems.append('CANNOT VERIFY: the %s control could not be evaluated '
                                'against %s' % (name, label))
        print('    %-20s forbidden in %d of %d families  %s'
              % (name, len(forbidding), len(BARRIERS),
                 'ok' if not forbidding else '<-- %s' % forbidding), flush=True)
        if forbidding:
            problems.append('%s is caught by the containment in %s' % (name, forbidding))

    print('\n=== RESULT ===', flush=True)
    if problems:
        for problem in problems:
            print('  %s' % problem, flush=True)
    else:
        print('  every post-%s artifact is present, every named check resolves, all '
              '%d barriers are attached at their mapped labels, and both negative '
              'controls hold' % (VERIFIED_THROUGH, len(BARRIERS)), flush=True)
    print('\nEXIT %d' % (1 if problems else 0), flush=True)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
