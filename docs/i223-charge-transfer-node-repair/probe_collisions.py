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
    (ii) the two rates differ by more than 4x THROUGHOUT the window where both
         fits are actually used -- i.e. even at the temperature in that window
         least favourable to splitting.

  The 4x in (ii) is not arbitrary.  This ticket measured the disagreement
  between two independent literature fits of the SAME reaction -- Gupta RP-1232
  R19 vs Ozawa Table III for NO+ + O2 -- at 1.9-3.8x.  Below that, two rates
  merged onto one node disagree by less than the source-to-source scatter for a
  single reaction, so splitting the node buys a distinction the underlying data
  cannot support.  Above it, the merge is discarding real information.

"Where both fits are actually used" is doing real work in (ii), and the probe
reports the full declared range too so you can see the difference.  Every entry
here declares Tmin = 300 K, but the [Ozawa2008] pairs are hypersonic shock-layer
fits with Ea of 238-424 kJ/mol: at 300 K both sides evaluate to ~1e-28 and their
RATIO runs to 1e18 or 1e27, which is an exponential artefact of extrapolating
far below where anyone would use either number.  Quoting those figures as the
strength of the case would be dishonest arithmetic even though it is arithmetic
that favours the conclusion.  The in-range figures are 107x and 218x, both at
10000 K, which is where the two Ozawa pairs agree most closely -- still
decisive, and defensible at the point of maximum doubt.

The probe also prints the INTERVAL of thresholds that would produce the same
five verdicts, which is the honest way to show a threshold is not load-bearing:
if that interval is wide, the exact value of 4x does not matter.
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
#   (label 1, label 2, what differs, can the tree express it, provenance of the two rates,
#    (T_lo, T_hi) window in which the verdict is decided, why that window)
#
# The provenance field is not decoration.  Two rates that agree can agree for two very different
# reasons, and only one of them makes a merge safe to keep.  probe_tanarro.py establishes which
# is which here, and counts it from the transcribed table rather than asserting it: 17 of the 23
# ion-ion neutralization rows in Tanarro Table 1 carry the identical 2e-7 (Tg/300)^-0.5 and 14 of
# those cite one kinetic-scheme review (Kossyi 1992), so agreement among them is ONE class
# estimate quoted twice.  A merge that is lossless for that reason is lossless because the source
# is coarse, and stops being lossless the day a real measurement for either pair arrives.  That is
# a finding with an expiry date, and it is labelled as one below.
# (An earlier version of this comment said 18 and 16.  Both were wrong -- IN8 is 2.3e-7, not the
# generic value.  The conclusion is unchanged; the count is now computed, not tallied by hand.)
PAIRS = [
    ('Hp_r1 + H-_r2 <=> H + H',
     'H2p_r1 + H-_r2 <=> H2 + H',
     'H+ vs H2+ as the cation',
     'expressible as a disconnected 2-atom group, but the recipe returns None '
     'on the resulting sample (probe_h2_recipe.py) -- so no',
     'DIFFERENT sources: Table 1 IN1 cites [21] Konstantinovskii, IN2 cites [71] Scott. '
     'The near-agreement is two sources, not one estimate.',
     (300.0, 10000.0),
     'Ea = 0 and n is -0.5 on both sides, so the ratio is exactly A1/A2 at every T. '
     'No window to argue about.'),
    ('H2Op_r1 + O-_r2 <=> H2O + O',
     'H2Op_r1 + OH-_r2 <=> H2O + OH',
     'O- vs OH- as the anion',
     'yes -- an OH_anion group, sibling or child of O_anion',
     'SAME class estimate: Table 1 IN15 and IN22 both cite [56] Kossyi 1992 and both carry the '
     'generic 2e-7 (Tg/300)^-0.5. Identical because the source did not distinguish them.',
     (300.0, 10000.0),
     'Identical parameters, so the ratio is 1 at every T.'),
    ('O2p_r1 + O-_r2 <=> O2 + O',
     'O2p_r1 + OH-_r2 <=> O2 + OH',
     'O- vs OH- as the anion',
     'yes -- the same OH_anion group',
     'SAME class estimate, via two citations: Table 1 IN13 cites [73] Gudmundsson, IN20 cites '
     '[56] Kossyi, but both quote the identical generic 2e-7 (Tg/300)^-0.5.',
     (300.0, 10000.0),
     'Identical parameters, so the ratio is 1 at every T.'),
    ('O2p_r1 + N_r2 <=> Np + O2',
     'O2p_r1 + N2_r2 <=> N2p + O2',
     'N vs N2 as the neutral',
     'yes -- an N2_neutral group under N_neutral',
     'Both [Ozawa2008] Table III, and pair-specific: different A, n and Ea for each.',
     (5000.0, 10000.0),
     'Ozawa fits hypersonic shock layers; both carry large Ea (238 and 338 kJ/mol), so at 300 K '
     'both k are ~1e-28 and their ratio is an exponential artefact of extrapolating far below '
     'where either fit is used. Decided on the high-T end, where both are live.'),
    ('NOp_r1 + O_r2 <=> NO + Op',
     'NOp_r1 + O2_r2 <=> O2p + NO',
     'O vs O2 as the neutral',
     'yes -- O2_neutral, which this ticket added',
     'Both [Ozawa2008] Table III, and pair-specific: different A, n and Ea for each.',
     (5000.0, 10000.0),
     'Same reasoning: Ea of 424 and 271 kJ/mol, so the 300 K ratio is extrapolation. Decided on '
     'the high-T end.'),
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
    for lbl1, lbl2, what, expressible, provenance, window, window_why in PAIRS:
        e1, e2 = by_label[lbl1][0], by_label[lbl2][0]
        t1 = ';'.join(g.label for g in family.get_reaction_template(e1.item))
        t2 = ';'.join(g.label for g in family.get_reaction_template(e2.item))
        k1, k2 = e1.data, e2.data
        lo, hi, fell_back = shared_range(k1, k2)
        w_lo, w_hi = window

        print('=' * 92)
        print('{0}   [{1}]'.format(lbl1, t1))
        print('{0}   [{1}]'.format(lbl2, t2))
        print('  differ in        : {0}'.format(what))
        print('  tree can express : {0}'.format(expressible))
        print('  rate provenance  : {0}'.format(provenance))
        print('  declared T range : {0:g} - {1:g} K{2}'.format(
            lo, hi, '   (windows disjoint; fell back to the family range)' if fell_back else ''))
        print('  DECIDED on       : {0:g} - {1:g} K'.format(w_lo, w_hi))
        print('  because          : {0}'.format(window_why))
        print('  status now       : {0}'.format(
            'MERGED onto one node' if t1 == t2 else 'SPLIT across two nodes'))
        print('')
        print('  {0:>8}  {1:>13}  {2:>13}  {3:>10}'.format('T / K', 'k1', 'k2', 'k1/k2'))
        grid = np.unique(np.concatenate([
            np.array([lo, hi]),
            np.linspace(lo, hi, 9),
        ]))
        declared_worst = 0.0
        declared_T = lo
        in_window = []           # (spread, T) for every grid point inside the deciding window
        for T in grid:
            T = float(T)
            v1 = k1.get_rate_coefficient(T) * 1e6
            v2 = k2.get_rate_coefficient(T) * 1e6
            ratio = v1 / v2
            spread = max(ratio, 1.0 / ratio)
            if spread > declared_worst:
                declared_worst, declared_T = spread, T
            inside = w_lo <= T <= w_hi
            if inside:
                in_window.append((spread, T))
            print('  {0:>8.0f}  {1:>13.4e}  {2:>13.4e}  {3:>10.4g}{4}'.format(
                T, v1, v2, ratio, '   <- deciding window' if inside else ''))

        # The DECISION statistic is the WEAKEST disagreement anywhere in the deciding window, not
        # the strongest. "These rates differ by at least Nx everywhere both fits are used" is a
        # claim that survives someone checking it at the temperature least favourable to me; "they
        # differ by up to Nx somewhere" is not. Both are printed.
        decided_min, decided_min_T = min(in_window)
        decided_max, decided_max_T = max(in_window)
        expressible_ok = not expressible.rstrip().endswith('no')
        meets = decided_min > THRESHOLD
        verdict = 'SPLIT' if (expressible_ok and meets) else 'LEAVE MERGED'
        class_estimate = provenance.startswith('SAME class estimate')
        print('')
        print('  worst over the DECLARED range : {0:.4g}x at {1:.0f} K'.format(
            declared_worst, declared_T))
        print('  in the deciding window, they differ by between {0:.4g}x (at {1:.0f} K) and '
              '{2:.4g}x (at {3:.0f} K)'.format(
                  decided_min, decided_min_T, decided_max, decided_max_T))
        print('  DECIDED on the weakest of those : {0:.4g}x   -> > {1}x? {2}'.format(
            decided_min, THRESHOLD, 'yes' if meets else 'no'))
        if declared_worst / max(decided_min, 1e-300) > 10:
            print('  (the declared-range figure is {0:.3g}x larger. It is an extrapolation'.format(
                declared_worst / decided_min))
            print('   artefact and is NOT the number this verdict rests on.)')
        print('  VERDICT: {0}'.format(verdict))
        if verdict == 'LEAVE MERGED' and class_estimate:
            print('    EXPIRES: lossless because the SOURCE is coarse, not because the tree is')
            print('    right. Both sides quote one class estimate. The first real measurement for')
            print('    either pair makes this merge start discarding data, as the N/N2 merge does.')
        print('')
        verdicts.append((lbl1, lbl2, t1 == t2, decided_min, decided_min_T, expressible_ok,
                         verdict, class_estimate, declared_worst))

    print('=' * 92)
    print('summary')
    print('=' * 92)
    hdr = '{0:<40} {1:<7} {2:>11} {3:>11} {4:<6} {5:<13} {6}'.format(
        'template pair', 'status', 'in-range', 'declared', 'expr.', 'verdict', 'holds because')
    print(hdr)
    print('-' * len(hdr))
    for lbl1, lbl2, merged, worst, worst_T, ok, verdict, class_est, declared in verdicts:
        name = '{0} / {1}'.format(lbl1.split(' <=>')[0], lbl2.split(' <=>')[0])
        if verdict == 'SPLIT':
            why = 'rates differ'
        elif class_est:
            why = 'coarse source -- EXPIRES'
        elif not ok:
            why = 'recipe cannot process the node'
        else:
            why = 'rates agree, sources differ'
        print('{0:<40} {1:<7} {2:>10.4g}x {3:>10.4g}x {4:<6} {5:<13} {6}'.format(
            name[:40], 'merged' if merged else 'split', worst, declared,
            'yes' if ok else 'no', verdict, why))
    print('')
    print('')
    print('"in-range" is the figure the verdict rests on; "declared" is the worst over the full')
    print('300-10000 K window each entry declares, and for the Ozawa pairs that is extrapolation.')
    print('')

    # How much does the 4x actually matter? Report the interval of thresholds giving these same
    # five verdicts. A threshold that only works at one value is a fudge; a wide interval is not.
    splits = [v[3] for v in verdicts if v[6] == 'SPLIT']
    # Include every LEAVE MERGED pair in the floor, even the one held merged by criterion (i)
    # rather than by the threshold. Excluding it would quietly widen the interval and overstate
    # how insensitive the result is.
    merges = [v[3] for v in verdicts if v[6] == 'LEAVE MERGED']
    floor = max(merges) if merges else 1.0
    ceiling = min(splits) if splits else float('inf')
    print('sensitivity of the verdicts to the threshold')
    print('  largest in-window ratio among LEAVE MERGED (all of them) : {0:.4g}x'.format(floor))
    print('  smallest in-window ratio among SPLIT                     : {0:.4g}x'.format(ceiling))
    if ceiling > floor:
        print('  => ANY threshold strictly between {0:.4g}x and {1:.4g}x gives these same five'.format(
            floor, ceiling))
        print('     verdicts -- a factor-of-{0:.0f} window. The chosen {1}x sits inside it, and'.format(
            ceiling / floor, THRESHOLD))
        print('     the conclusions do not depend on where in that window it sits.')
        if not (floor < THRESHOLD < ceiling):
            print('  !! but the chosen threshold is NOT inside that interval -- check it.')
    else:
        print('  => NO threshold separates these verdicts; the criterion is not doing the work.')
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
