#!/usr/bin/env python
# encoding: utf-8
"""
I-223 round-49 rework: measure what `N2_neutral` did BEYOND the 22/23 collision it was added for.

Adding a node does two things a report can easily conflate:

  1. it splits the collision it was added to split -- training 22/23, which is what section 4 of
     the report claimed and all it claimed;
  2. it REPARENTS every other training reaction whose partner descends to the new node, moving
     each to a different exact template. Three of those moves (training 15, 18, 19) had no
     collision at all and were not this ticket's stated target.

And a third, one level further out: the templates those three vacated are now EMPTY exact
templates. `fill_rules_by_averaging_up` -- which a real rate-rules job always runs
(`rmgpy/rmg/main.py:610` -> `rmgpy/data/kinetics/rules.py:172`) -- fills an empty parent by
averaging its children. `N_neutral`'s children now include `N2_neutral`, so anything descending to
`X;N_neutral` still sees the N2 number, but as an average carrying a comment rather than as an
exact rule.

This probe runs BOTH stages the way a real job does -- add_rules_from_training AND
fill_rules_by_averaging_up -- and reports, per template, whether the rule sitting there is exact
or averaged and where its value came from. Point it at a pre-edit checkout with I223_FAMILY_ROOT
to see the same table before the node existed.

(`probe_rules.py` deliberately stops after add_rules_from_training: its question is which labels
hold two entries at equal rank, and averaging would add derived entries that muddy that count.
Its docstring used to claim it ran both. It does not, and now says so.)
"""

import os
import sys
import traceback

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

# The templates this ticket's two new nodes touch, plus the ones they vacate.
WATCH = [
    'O2_ion;N_neutral',
    'O2_ion;N2_neutral',
    'O_atom_ion;N_neutral',
    'O_atom_ion;N2_neutral',
    'N_atom_ion;N_neutral',
    'N_atom_ion;N2_neutral',
    'Ar_ion;N_neutral',
    'Ar_ion;N2_neutral',
    'NO_ion;O_neutral',
    'NO_ion;O2_neutral',
    'Ar_ion;O_neutral',
    'Ar_ion;O2_neutral',
]


def describe(entry):
    """Exact rule from training, or a value averaged up from children?"""
    texts = [(entry.long_desc or '').strip(), (entry.short_desc or '').strip()]
    data_comment = getattr(getattr(entry, 'data', None), 'comment', '') or ''
    texts.append(data_comment.strip())
    blob = '\n'.join(t for t in texts if t)
    first = next((t.split('\n')[0] for t in texts if t), '')
    if 'Average of' in blob or 'Averaged' in blob:
        # the averaged comment names its children; keep the informative part
        for line in blob.split('\n'):
            if 'Average of' in line:
                return 'AVERAGED', line.strip()[:110]
        return 'AVERAGED', first[:110]
    if 'training reaction' in blob:
        return 'exact', first[:110]
    return 'derived', (first or '(no comment recorded)')[:110]


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()

    print('--- which template each N2-carrying training reaction resolves to ---')
    for e in sorted(dep.entries.values(), key=lambda e: e.index):
        if '_N2_r2' in e.label or 'N2_r2' in e.label or '+ N_r2' in e.label:
            template = ';'.join(g.label for g in family.get_reaction_template(e.item))
            print('  {0:>3}  {1:<34} -> {2}'.format(e.index, e.label, template))
    print('')

    print('--- stage 1: add_rules_from_training (exact rules only) ---')
    family.add_rules_from_training(thermo_database=None)
    after_training = {lbl: len(es) for lbl, es in family.rules.entries.items()}
    print('  rule labels holding at least one exact rule: {0}'.format(len(after_training)))
    for lbl in WATCH:
        print('    {0:<28} {1}'.format(
            lbl, '{0} exact rule(s)'.format(after_training[lbl]) if lbl in after_training
            else 'EMPTY -- nothing exact here'))
    print('')

    print('--- stage 2: fill_rules_by_averaging_up (what a real job also runs) ---')
    # verbose=True so the averaged entries record which children they averaged; the family is
    # small enough that the comment blowup the docstring warns about does not matter here.
    family.fill_rules_by_averaging_up(verbose=True)
    after_fill = family.rules.entries
    print('  rule labels after filling: {0}  (+{1})'.format(
        len(after_fill), len(after_fill) - len(after_training)))
    print('')

    row = '{0:<28} {1:<10} {2:<9} {3}'
    header = row.format('template', 'stage 1', 'kind', 'source of the value now sitting there')
    print(header)
    print('-' * len(header))
    for lbl in WATCH:
        was = '{0} exact'.format(after_training[lbl]) if lbl in after_training else 'empty'
        es = after_fill.get(lbl)
        if not es:
            print(row.format(lbl, was, '-', 'still nothing -- nothing descends here'))
            continue
        for e in es:
            kind, origin = describe(e)
            print(row.format(lbl, was, kind, origin or '(no description)'))
    print('')

    # An "average" over a single child should BE that child's value. Check it, rather than
    # assuming it: the difference between "provenance label changed" and "number changed" is the
    # whole question of whether the reparenting is harmless.
    print('--- does the averaged parent return the same k as its one child? ---')
    pairs = [('O_atom_ion;N_neutral', 'O_atom_ion;N2_neutral'),
             ('N_atom_ion;N_neutral', 'N_atom_ion;N2_neutral'),
             ('Ar_ion;N_neutral', 'Ar_ion;N2_neutral')]
    print('  {0:<24} {1:>12} {2:>13} {3:>13} {4:>9}'.format(
        'template', 'T / K', 'averaged k', 'child k', 'ratio'))
    worst = 1.0
    for parent_lbl, child_lbl in pairs:
        pe = after_fill.get(parent_lbl)
        ce = after_fill.get(child_lbl)
        if not pe or not ce:
            print('  {0:<24} missing one side'.format(parent_lbl))
            continue
        for T in (1000.0, 5000.0, 10000.0):
            kp = pe[0].data.get_rate_coefficient(T) * 1e6
            kc = ce[0].data.get_rate_coefficient(T) * 1e6
            ratio = kp / kc if kc else float('nan')
            worst = max(worst, ratio, 1.0 / ratio if ratio else 1.0)
            print('  {0:<24} {1:>12.0f} {2:>13.4e} {3:>13.4e} {4:>9.6g}'.format(
                parent_lbl, T, kp, kc, ratio))
    print('')
    print('  worst deviation of averaged parent from its single child: {0:.6g}x'.format(worst))
    print('  (an average over one entry is that entry; if this is 1, the reparenting changed')
    print('   the PROVENANCE LABEL of these three templates and not the number they return)')
    print('')

    filled = [lbl for lbl in WATCH
              if lbl not in after_training and lbl in after_fill]
    print('templates that hold NO exact rule and are served by averaging: {0}'.format(len(filled)))
    for lbl in filled:
        print('    {0}'.format(lbl))
    print('')
    print('Reading: a template in that list is not broken. It means a reaction descending there')
    print('gets a value averaged over the node\'s children rather than a rate somebody sourced')
    print('for it, and the comment on the resulting kinetics says so. Worth stating in the report')
    print('because it is a behaviour change that no check reports and no collision count shows.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
