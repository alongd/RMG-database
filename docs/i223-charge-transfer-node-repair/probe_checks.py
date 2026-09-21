#!/usr/bin/env python
# encoding: utf-8
"""
I-223: run every family-level check of test_kinetics against the 28-entry
Plasma_Charge_Transfer copy, ONE AT A TIME.

The suite cannot do this: `kinetics_check_groups_nonidentical` does not return
False, it raises ValueError, which escapes its `with check:` block and aborts
the whole test function for the family -- so a suite run reports at most one
failing node per family and silently never runs the later checks.

The family is loaded from its docs/ path.  It is NOT installed under input/.
"""

import os
import sys
import traceback
import types

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

RMGPY_TEST = os.path.join(os.environ.get('RMGPY_ROOT', '/home/alon/Code/RMG-Py-i223-ct-node-repair'))
sys.path.insert(0, os.path.join(RMGPY_TEST, 'test', 'database'))
from databaseTest import TestDatabase  # noqa: E402

# checks test_kinetics runs per family, in its own order
CHECKS = [
    'kinetics_check_correct_number_of_nodes_in_rules',
    'kinetics_check_nodes_in_rules_found_in_groups',
    'kinetics_check_groups_found_in_tree',
    'kinetics_check_groups_nonidentical',
    'kinetics_check_child_parent_relationships',
    'kinetics_check_siblings_for_parents',
    'kinetics_check_cd_atom_type',
    'kinetics_check_reactant_and_product_template',
    'kinetics_check_num_reactant_and_product',
    'kinetics_check_family_electrons_reach_training_reactions',
    'kinetics_check_sample_descends_to_group',
    'kinetics_check_sample_can_react',
]


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()

    tester = TestDatabase()
    tester.database = types.SimpleNamespace(
        kinetics=types.SimpleNamespace(families={FAMILY: family}, libraries={}),
    )

    print('auto_generated     = {0}'.format(family.auto_generated))
    print('own_reverse        = {0}'.format(family.own_reverse))
    print('n groups.top       = {0}, n template reactants = {1}'.format(
        len(family.groups.top), len(family.forward_template.reactants)))
    print('')

    failures = []
    for name in CHECKS:
        if name == 'kinetics_check_unimolecular_groups' and \
                len(family.forward_template.reactants) >= len(family.groups.top):
            print('{0:<55} SKIP (not unimolecular-group shaped)'.format(name))
            continue
        try:
            result = getattr(tester, name)(FAMILY)
        except Exception as exc:
            failures.append(name)
            print('{0:<55} RAISED {1}'.format(name, type(exc).__name__))
            print('    {0}'.format(str(exc).replace('\n', '\n    ')))
            continue
        if result:
            print('{0:<55} PASS'.format(name))
        else:
            failures.append(name)
            print('{0:<55} FAIL (returned {1!r})'.format(name, result))

    print('')
    if failures:
        print('FAILED CHECKS: {0}'.format(', '.join(failures)))
    else:
        print('ALL {0} FAMILY CHECKS PASS'.format(len(CHECKS)))
    return 1 if failures else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
