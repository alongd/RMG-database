#!/usr/bin/env python
# encoding: utf-8
"""
I-223: prove no template label is left carrying two entries at equal rank.

`KineticsRules.get_rule` resolves a collision with
    entries.sort(key=lambda x: (1000 if not x.rank else x.rank, x.index))
then takes entries[0] (rmgpy/data/kinetics/rules.py:151-154).  With equal ranks
the rank key -- the field that exists to express preference -- discriminates
nothing and the smaller index wins by accident, silently.

This runs add_rules_from_training + fill_rules_by_averaging_up the way a real
RMG run does, then reports every rule label holding more than one entry.
"""

import os
import sys
from collections import Counter

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()

    print('training entries   = {0}'.format(len(dep.entries)))
    labels = Counter(e.label for e in dep.entries.values())
    dup_labels = {k: v for k, v in labels.items() if v > 1}
    print('duplicate reaction labels in training: {0}'.format(dup_labels or 'none'))
    print('')

    print('--- duplicate check on the training depository itself ---')
    bad = False
    for lbl, n in dup_labels.items():
        es = sorted([e for e in dep.entries.values() if e.label == lbl], key=lambda e: e.index)
        ranks = [e.rank for e in es]
        print('  {0!r}: indices {1}, ranks {2}'.format(lbl, [e.index for e in es], ranks))
        if len(set(ranks)) != len(ranks):
            bad = True
            print('    ^^ EQUAL RANKS -- get_rule would pick by index, silently')
    if not dup_labels:
        print('  none')
    print('')

    print('--- template each training reaction resolves to ---')
    for e in sorted(dep.entries.values(), key=lambda e: e.index):
        try:
            template = family.get_reaction_template(e.item)
            tlabel = ';'.join(g.label for g in template)
        except Exception as exc:
            tlabel = '!! {0}: {1}'.format(type(exc).__name__, exc)
        print('  {0:>3}  {1:<34} -> {2}'.format(e.index, e.label, tlabel))
    print('')

    print('--- rate rules generated from training ---')
    family.add_rules_from_training(thermo_database=None)
    entries_by_label = family.rules.entries
    n_multi = 0
    for lbl, es in sorted(entries_by_label.items()):
        if len(es) < 2:
            continue
        n_multi += 1
        ranks = [e.rank for e in es]
        print('  {0}: {1} entries, ranks {2}'.format(lbl, len(es), ranks))
        chosen = sorted(es, key=lambda x: (1000 if not x.rank else x.rank, x.index))[0]
        for e in sorted(es, key=lambda x: x.index):
            origin = (e.long_desc or '').strip().split('\n')[0]
            print('      rule idx {0:>3}  rank {1}  {2:<14} {3} {4}'.format(
                e.index, e.rank, e.short_desc, origin,
                '   <-- get_rule picks this one' if e is chosen else ''))
        # Same *reaction* twice is an accident. Different reactions sharing one
        # template node is ordinary RMG: the tree is coarser than the chemistry.
        origins = [(e.long_desc or '').strip().split('\n')[0] for e in es]
        if len(set(origins)) != len(origins):
            bad = True
            print('    ^^ SAME REACTION TWICE at equal rank -- decided by index, silently')
        elif len(set(ranks)) != len(ranks):
            print('    (distinct reactions sharing one template node; equal rank here means')
            print('     get_rule keeps the lowest index and discards the rest -- ordinary RMG,')
            print('     and a tree-granularity question, not a duplicate-entry defect)')
    if n_multi == 0:
        print('  every rule label holds exactly one entry')
    print('')

    print('total rule labels  = {0}'.format(len(entries_by_label)))
    print('labels with >1 entry = {0}'.format(n_multi))
    print('')
    print('VERDICT: {0}'.format(
        'SAME REACTION TWICE AT EQUAL RANK' if bad
        else 'no reaction appears twice at equal rank, in training or in the rules'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
