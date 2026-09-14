#!/usr/bin/env python
# encoding: utf-8
"""
I-223 rework: put a NUMBER on every template node that catches two distinct
training reactions, so "split it" or "leave it" stops being a matter of taste.

`probe_rules.py` finds the collisions.  It cannot say which of them matter --
it only annotates them as "a tree-granularity question".  That annotation and
the fact that this ticket split one of them (NO_ion;O_neutral, via O2_neutral)
cannot both stand without a stated criterion.  This probe supplies it.

CRITERION APPLIED HERE (see report.md section 4 for the argument):

  split a merged template when BOTH hold --
    (i)  the two reactants are distinguishable by a group that RMG's existing
         atom types can express, AND the family's recipe can process the
         resulting sample (a node the recipe turns into None is not a repair);
    (ii) the two rates differ, somewhere in their shared validity range, by
         more than 4x.

  The 4x in (ii) is not arbitrary.  This ticket measured the disagreement
  between two independent literature fits of the SAME reaction -- Gupta RP-1232
  R19 vs Ozawa Table III for NO+ + O2 -- at 1.9-3.8x.  Below that, two rates
  merged onto one node disagree by less than the source-to-source scatter for a
  single reaction, so splitting the node buys a distinction the underlying data
  cannot support.  Above it, the merge is discarding real information.

Both halves are reported per pair, so a reader who prefers a different
threshold can re-read the table against it.
"""

import os
import sys
import traceback

import numpy as np

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

THRESHOLD = 4.0

# Every pair of training reactions that share, or shared, one template node.
# Keyed by label so the table survives the index renumbering that deleting a
# training entry causes.
#   (label 1, label 2, what differs, can the tree express it, provenance of the two rates)
#
# The provenance field is not decoration.  Two rates that agree can agree for two very different
# reasons, and only one of them makes a merge safe to keep.  probe_tanarro.py establishes which
# is which here: 18 of the 23 ion-ion neutralization rows in Tanarro Table 1 carry the identical
# 2e-7 (Tg/300)^-0.5 and 16 of those cite one kinetic-scheme review (Kossyi 1992), so agreement
# among them is ONE class estimate quoted twice.  A merge that is lossless for that reason is
# lossless because the source is coarse, and stops being lossless the day a real measurement for
# either pair arrives.  That is a finding with an expiry date, and it is labelled as one below.
PAIRS = [
    ('Hp_r1 + H-_r2 <=> H + H',
     'H2p_r1 + H-_r2 <=> H2 + H',
     'H+ vs H2+ as the cation',
     'expressible as a disconnected 2-atom group, but the recipe returns None '
     'on the resulting sample (probe_h2_recipe.py) -- so no',
     'DIFFERENT sources: Table 1 IN1 cites [21] Konstantinovskii, IN2 cites [71] Scott. '
     'The near-agreement is two sources, not one estimate.'),
    ('H2Op_r1 + O-_r2 <=> H2O + O',
     'H2Op_r1 + OH-_r2 <=> H2O + OH',
     'O- vs OH- as the anion',
     'yes -- an OH_anion group, sibling or child of O_anion',
     'SAME class estimate: Table 1 IN15 and IN22 both cite [56] Kossyi 1992 and both carry the '
     'generic 2e-7 (Tg/300)^-0.5. Identical because the source did not distinguish them.'),
    ('O2p_r1 + O-_r2 <=> O2 + O',
     'O2p_r1 + OH-_r2 <=> O2 + OH',
     'O- vs OH- as the anion',
     'yes -- the same OH_anion group',
     'SAME class estimate, via two citations: Table 1 IN13 cites [73] Gudmundsson, IN20 cites '
     '[56] Kossyi, but both quote the identical generic 2e-7 (Tg/300)^-0.5.'),
    ('O2p_r1 + N_r2 <=> Np + O2',
     'O2p_r1 + N2_r2 <=> N2p + O2',
     'N vs N2 as the neutral',
     'yes -- an N2_neutral group under N_neutral',
     'Both [Ozawa2008] Table III, and pair-specific: different A, n and Ea for each.'),
    ('NOp_r1 + O_r2 <=> NO + Op',
     'NOp_r1 + O2_r2 <=> O2p + NO',
     'O vs O2 as the neutral',
     'yes -- O2_neutral, which this ticket added',
     'Both [Ozawa2008] Table III, and pair-specific: different A, n and Ea for each.'),
]


def shared_range(k1, k2):
    """Intersection of the two Arrhenius validity windows, with a fallback."""
    los, his = [], []
    for k in (k1, k2):
        los.append(k.Tmin.value_si if k.Tmin is not None else None)
        his.append(k.Tmax.value_si if k.Tmax is not None else None)
    lo = max([t for t in los if t] or [300.0])
    hi = min([t for t in his if t] or [10000.0])
    if hi <= lo:  # disjoint windows: fall back to the family's stated range
        return 300.0, 10000.0, True
    return lo, hi, False


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()
    by_label = {}
    for e in dep.entries.values():
        by_label.setdefault(e.label, []).append(e)

    missing = [lbl for pair in PAIRS for lbl in pair[:2] if lbl not in by_label]
    if missing:
        print('PRECONDITION NOT MET: these training reactions are not in the depository:')
        for lbl in missing:
            print('    {0}'.format(lbl))
        print('This probe expects the full training set of the Plasma_Charge_Transfer copy at')
        print('docs/i154-carry-chemistry/held-back/ (or a checkout named by I223_FAMILY_ROOT).')
        return 2

    print('threshold for "the rates disagree enough to be worth a node" = {0}x'.format(THRESHOLD))
    print('(= the measured Gupta-vs-Ozawa scatter for ONE reaction, 1.9-3.8x)')
    print('')

    verdicts = []
    for lbl1, lbl2, what, expressible, provenance in PAIRS:
        e1, e2 = by_label[lbl1][0], by_label[lbl2][0]
        t1 = ';'.join(g.label for g in family.get_reaction_template(e1.item))
        t2 = ';'.join(g.label for g in family.get_reaction_template(e2.item))
        k1, k2 = e1.data, e2.data
        lo, hi, fell_back = shared_range(k1, k2)

        print('=' * 92)
        print('{0}   [{1}]'.format(lbl1, t1))
        print('{0}   [{1}]'.format(lbl2, t2))
        print('  differ in        : {0}'.format(what))
        print('  tree can express : {0}'.format(expressible))
        print('  rate provenance  : {0}'.format(provenance))
        print('  shared T range   : {0:g} - {1:g} K{2}'.format(
            lo, hi, '   (windows disjoint; fell back to the family range)' if fell_back else ''))
        print('  status now       : {0}'.format(
            'MERGED onto one node' if t1 == t2 else 'SPLIT across two nodes'))
        print('')
        print('  {0:>8}  {1:>13}  {2:>13}  {3:>10}'.format('T / K', 'k1', 'k2', 'k1/k2'))
        grid = np.unique(np.concatenate([
            np.array([lo, hi]),
            np.linspace(lo, hi, 9),
        ]))
        worst = 0.0
        worst_T = lo
        for T in grid:
            v1 = k1.get_rate_coefficient(float(T)) * 1e6
            v2 = k2.get_rate_coefficient(float(T)) * 1e6
            ratio = v1 / v2
            spread = max(ratio, 1.0 / ratio)
            if spread > worst:
                worst, worst_T = spread, float(T)
            print('  {0:>8.0f}  {1:>13.4e}  {2:>13.4e}  {3:>10.4g}'.format(float(T), v1, v2, ratio))
        expressible_ok = not expressible.rstrip().endswith('no')
        meets = worst > THRESHOLD
        verdict = 'SPLIT' if (expressible_ok and meets) else 'LEAVE MERGED'
        class_estimate = provenance.startswith('SAME class estimate')
        print('')
        print('  worst disagreement: {0:.4g}x at {1:.0f} K   -> {2} > {3}x? {4}'.format(
            worst, worst_T, 'ratio', THRESHOLD, 'yes' if meets else 'no'))
        print('  VERDICT: {0}'.format(verdict))
        if verdict == 'LEAVE MERGED' and class_estimate:
            print('    EXPIRES: lossless because the SOURCE is coarse, not because the tree is')
            print('    right. Both sides quote one class estimate. The first real measurement for')
            print('    either pair makes this merge start discarding data, as the N/N2 merge does.')
        print('')
        verdicts.append((lbl1, lbl2, t1 == t2, worst, worst_T, expressible_ok, verdict,
                         class_estimate))

    print('=' * 92)
    print('summary')
    print('=' * 92)
    hdr = '{0:<46} {1:<9} {2:>12} {3:<11} {4:<13} {5}'.format(
        'template pair', 'status', 'worst ratio', 'expressible', 'verdict', 'holds because')
    print(hdr)
    print('-' * len(hdr))
    for lbl1, lbl2, merged, worst, worst_T, ok, verdict, class_est in verdicts:
        name = '{0} / {1}'.format(lbl1.split(' <=>')[0], lbl2.split(' <=>')[0])
        if verdict == 'SPLIT':
            why = 'rates differ'
        elif class_est:
            why = 'coarse source -- EXPIRES'
        elif not ok:
            why = 'recipe cannot process the node'
        else:
            why = 'rates agree, sources differ'
        print('{0:<46} {1:<9} {2:>11.4g}x {3:<11} {4:<13} {5}'.format(
            name[:46], 'merged' if merged else 'split', worst, 'yes' if ok else 'no',
            verdict, why))
    print('')
    unresolved = [v for v in verdicts if v[2] and v[6] == 'SPLIT']
    print('still merged but the criterion says SPLIT: {0}'.format(len(unresolved)))
    for v in unresolved:
        print('    {0}  /  {1}'.format(v[0], v[1]))
    expiring = [v for v in verdicts if v[2] and v[7]]
    print('')
    print('merged on a coarse source, and therefore provisional: {0}'.format(len(expiring)))
    for v in expiring:
        print('    {0}  /  {1}'.format(v[0], v[1]))
    print('  These are the O-/OH- merges. They cost nothing TODAY because Tanarro Table 1 gives')
    print('  both sides the same class estimate (probe_tanarro.py), not because O_anion is the')
    print('  right granularity. Keep the OH_anion sibling-vs-child question open.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
