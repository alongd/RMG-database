#!/usr/bin/env python
# encoding: utf-8
"""Round 118 HIGH 2: the completeness check passes over a family nobody evaluated.

``test_every_family_whose_template_admits_the_metastable_is_forbidden`` is the only thing
standing behind "the contained set is the WHOLE set". It derives the set by asking the
shipped matcher which families' template slots admit ``Ar u2 p3 c0``, and compares that
derived set against ``CONTAINED_FAMILIES``.

``matching_slots()`` used to catch every matcher exception into ``MATCHER_ERRORS`` and
carry on. A family whose relevant slot raises is therefore absent from the derived set --
and if it is absent from ``CONTAINED_FAMILIES`` too, which is exactly the case of a family
added tomorrow, the comparison stays true. The check passes, and it has said nothing at
all about the family it could not evaluate.

This probe measures that, both ways, against both revisions of the derivation module:

    revision x injection -> does the completeness comparison still say "complete"?

    committed at BASE_REV, no injection : complete   (correct, and the state that ships)
    committed at BASE_REV, injected     : complete   <-- THE DEFECT
    working tree,          no injection : complete   (the repair costs nothing)
    working tree,          injected     : REFUSED    <-- the repair

The injection is a matcher that raises, standing in for a new group node, an exotic atom
type, or a malformed template -- anything that makes ``_match_reactant_to_template`` throw.
It is applied to ``H_Abstraction``: a family that is NOT in ``CONTAINED_FAMILIES``, because
the defect is that an *omitted* family leaves the comparison true. Injecting into a
contained family would shorten the derived set and fail the comparison for the wrong
reason, which would look like the check working.

EXIT CODE IS THE CHECK: 0 only if the base reproduces the defect AND the working tree
refuses. A probe that cannot come out wrong is not evidence, so both arms are required.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-mgr-i221-deck-probe-234349 \\
        python docs/argon-metastable-thermo/undetermined_slot_probe.py \\
        > >(tee docs/argon-metastable-thermo/logs/undetermined_slot_probe.stdout.log) \\
        2> >(tee docs/argon-metastable-thermo/logs/undetermined_slot_probe.stderr.log >&2)
"""

import importlib.util
import os
import subprocess
import sys
import tempfile

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))
DATABASE = os.path.join(REPO, 'input')
settings['database.directory'] = DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402

#: The commit this branch's verification was recorded against, rebased. Its derivation
#: module is the "before" arm: the file as it ships, not a reconstruction of it.
BASE_REV = 'a3ed93580'
MODULE_PATH = 'docs/argon-metastable-thermo/template_space_derivation.py'

#: Not in CONTAINED_FAMILIES, and loaded by every run of the suite.
VICTIM = 'H_Abstraction'

#: Kept in step with test_argon_metastable_thermo.py by the assertion in `main()`, which
#: reads the real one out of the test module rather than trusting this copy.
CONTAINED_FAMILIES = {'Birad_R_Recombination', 'R_Addition_MultipleBond',
                      'Disproportionation', 'CO_Disproportionation', 'Cl_Abstraction',
                      'Br_Abstraction', 'F_Abstraction', 'Disproportionation-Y',
                      'Surface_Adsorption_Double', 'Cation_NO_Substitution',
                      'Li_NO_Substitution'}
EII = 'Plasma_Electron_Impact_Ionization'


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def committed_module(revision):
    """The derivation module as `revision` committed it, loaded by path."""
    blob = subprocess.check_output(['git', '-C', REPO, 'show',
                                    '%s:%s' % (revision, MODULE_PATH)])
    handle = tempfile.NamedTemporaryFile('wb', suffix='_derivation_%s.py' % revision,
                                         delete=False)
    handle.write(blob)
    handle.close()
    return load_module(handle.name, 'derivation_%s' % revision), handle.name


def raising_matcher(*_args, **_kwargs):
    raise RuntimeError('injected: this template slot cannot be evaluated')


def completeness(derivation, db, inject):
    """Run the completeness comparison the way the test runs it.

    Returns ``('complete', ...)``, ``('incomplete', ...)`` or ``('refused', ...)`` -- the
    third being the only answer that distinguishes "did not match" from "nobody knows"."""
    meta = derivation.molecule(derivation.AR_META)
    if hasattr(derivation, 'MATCHER_ERRORS'):
        derivation.MATCHER_ERRORS[:] = []

    original = db.families[VICTIM]._match_reactant_to_template
    if inject:
        db.families[VICTIM]._match_reactant_to_template = raising_matcher
    try:
        admits = {}
        for label, family in db.families.items():
            try:
                slots = {d: derivation.matching_slots(family, meta, d)
                         for d in ('forward', 'reverse')}
            except Exception as exc:                        # noqa: BLE001
                if type(exc).__name__ == 'UndeterminedSlot':
                    return 'refused', str(exc).split('.')[0]
                raise
            if slots['forward'] or slots['reverse']:
                admits[label] = slots
    finally:
        db.families[VICTIM]._match_reactant_to_template = original

    derived = sorted(set(admits) - {EII})
    recorded = list(getattr(derivation, 'MATCHER_ERRORS', []))
    if derived == sorted(CONTAINED_FAMILIES):
        return 'complete', '%d families derived; %d matcher error(s) recorded and not ' \
                           'asserted on' % (len(derived), len(recorded))
    return 'incomplete', 'derived %d, contained %d' % (len(derived),
                                                       len(CONTAINED_FAMILIES))


def main():
    print('loading every family from %s' % DATABASE, flush=True)
    db = KineticsDatabase()
    db.load_families(os.path.join(DATABASE, 'kinetics', 'families'), families='all')
    print('families loaded: %d' % len(db.families), flush=True)

    # The contained set is read from the test module rather than trusted from the copy
    # above, so this probe cannot quietly drift away from the thing it is about.
    test_module = load_module(os.path.join(REPO, 'test', 'test_argon_metastable_thermo.py'),
                              'i221_thermo_tests_for_probe')
    assert set(test_module.CONTAINED_FAMILIES) == CONTAINED_FAMILIES, (
        'this probe and the test disagree about the contained set: %s'
        % sorted(set(test_module.CONTAINED_FAMILIES) ^ CONTAINED_FAMILIES))
    assert VICTIM not in CONTAINED_FAMILIES, VICTIM
    assert VICTIM in db.families, VICTIM

    base, temp_path = committed_module(BASE_REV)
    tip = load_module(os.path.join(REPO, MODULE_PATH), 'derivation_worktree')

    rows = []
    for name, derivation in (('committed at %s' % BASE_REV, base), ('working tree', tip)):
        for inject in (False, True):
            verdict, detail = completeness(derivation, db, inject)
            rows.append((name, inject, verdict, detail))
            print('\n%-24s injected=%-5s -> %s\n    %s'
                  % (name, inject, verdict.upper(), detail), flush=True)
    os.unlink(temp_path)

    by_key = {(name, inject): verdict for name, inject, verdict, _d in rows}
    base_name, tip_name = 'committed at %s' % BASE_REV, 'working tree'

    defect_reproduced = by_key[(base_name, True)] == 'complete'
    repair_holds = by_key[(tip_name, True)] == 'refused'
    no_cost = by_key[(tip_name, False)] == 'complete'
    control = by_key[(base_name, False)] == 'complete'

    print('\n=== RESULT ===', flush=True)
    print('  control  -- the committed check is correct when nothing is injected : %s'
          % control, flush=True)
    print('  DEFECT   -- the committed check still says "complete" with a family it '
          'could not evaluate : %s' % defect_reproduced, flush=True)
    print('  repair   -- the working tree REFUSES instead of omitting                : %s'
          % repair_holds, flush=True)
    print('  no cost  -- the working tree is unchanged when nothing is injected      : %s'
          % no_cost, flush=True)
    ok = control and defect_reproduced and repair_holds and no_cost
    print('\nEXIT %d' % (0 if ok else 1), flush=True)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
