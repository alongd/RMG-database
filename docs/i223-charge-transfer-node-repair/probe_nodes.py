#!/usr/bin/env python
# encoding: utf-8
"""
I-223: per-node sample/descend probe for the 28-entry Plasma_Charge_Transfer copy.

Loads the family straight from its docs/ path (NOT from input/) and, for every
authored Group node, makes a sample molecule and descends the tree from the
node's own root.  Each node is reported independently so that one failure does
not hide the next -- the suite's own check aborts on the first AtomTypeError.
"""

import os
import sys
import traceback

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule.group import Group

FAMILY = 'Plasma_Charge_Transfer'
# I223_FAMILY_ROOT lets the same probes run against a pristine pre-edit checkout of the family,
# so "before" and "after" are measured by identical code.
FAMILY_ROOT = os.environ.get('I223_FAMILY_ROOT') or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..',
    'i154-carry-chemistry', 'held-back',
)


def load_family():
    kdb = KineticsDatabase()
    kdb.recommended_families = {}
    kdb.load_families(os.path.normpath(FAMILY_ROOT), families=[FAMILY], depositories=['training'])
    return kdb.families[FAMILY]


def main():
    print('cwd                 = {0}'.format(os.getcwd()))
    print('database.directory  = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()

    print('training entries    = {0}'.format(len(family.get_training_depository().entries)))
    print('group entries       = {0}'.format(len(family.groups.entries)))
    print('')

    ignore = []
    if not family.own_reverse:
        for product in family.forward_template.products:
            ignore.append(product)
            ignore.extend(product.children)
    print('ignored (products)  = {0}'.format([e.label for e in ignore]))
    print('')

    row = '{0:<16} {1:<14} {2:<24} {3:>6} {4:<16} {5}'
    header = row.format('node', 'root', 'sample molecule', 'charge', 'descends to', 'verdict')
    print(header)
    print('-' * len(header))

    n_fail = n_pass = n_skip = 0
    for name, entry in family.groups.entries.items():
        if entry in ignore:
            continue
        if not isinstance(entry.item, Group):
            print(row.format(name, '-', '(LogicNode)', '-', '-', 'SKIP (not a Group)'))
            n_skip += 1
            continue

        ancestors = family.ancestors(entry)
        root = ancestors[-1] if ancestors else entry

        try:
            sample = entry.item.make_sample_molecule()
        except Exception as exc:
            n_fail += 1
            print(row.format(name, root.label, '!! ' + type(exc).__name__, '-', '-', 'FAIL (sample)'))
            print('    {0}'.format(str(exc).replace('\n', '\n    ')))
            continue

        try:
            smiles = sample.to_smiles()
        except Exception as exc:
            smiles = '<no smiles: {0}>'.format(type(exc).__name__)
        charge = sample.get_net_charge()

        atoms = sample.get_all_labeled_atoms()
        try:
            match = family.groups.descend_tree(sample, atoms, strict=True, root=root)
        except Exception as exc:
            n_fail += 1
            print(row.format(name, root.label, smiles, charge,
                             '!! ' + type(exc).__name__, 'FAIL (descend)'))
            print('    {0}'.format(str(exc).replace('\n', '\n    ')))
            continue

        if match is None:
            n_fail += 1
            print(row.format(name, root.label, smiles, charge, 'None',
                             'FAIL (no match to root {0})'.format(root.label)))
            print('    sample adjlist:\n    {0}'.format(
                sample.to_adjacency_list().rstrip().replace('\n', '\n    ')))
            continue

        # the node itself, or one of its descendants, must be where we land
        chain = [match] + family.groups.ancestors(match)
        if entry in chain:
            n_pass += 1
            verdict = 'PASS'
        else:
            n_fail += 1
            verdict = 'FAIL (landed off-branch)'
        print(row.format(name, root.label, smiles, charge, match.label, verdict))

    print('')
    print('PASS {0}   FAIL {1}   SKIP {2}'.format(n_pass, n_fail, n_skip))
    return 1 if n_fail else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
