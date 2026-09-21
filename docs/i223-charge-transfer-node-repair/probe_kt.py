#!/usr/bin/env python
# encoding: utf-8
"""
I-223: compare the two duplicate literature rates for NOp_r1 + O2_r2 <=> O2p + NO.

Both entries sit at rank 6, so `KineticsRules.get_rule` breaks the tie on index
alone and index 17 (Gupta) silently wins.  This measures how far apart the two
fits actually are over 300-10000 K.

NOTE the two entries do NOT share a T0: index 17 is T0 = 300 K, index 21 is
T0 = 1 K.  Comparing their A factors directly is therefore meaningless -- the
"75x" apparent gap is mostly the T0 convention.  Everything below is evaluated
through rmgpy's own Arrhenius objects, which honour T0.
"""

import os
import sys

import numpy as np

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

LABEL = 'NOp_r1 + O2_r2 <=> O2p + NO'
TEMPERATURES = [300, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()

    dups = [e for e in dep.entries.values() if e.label == LABEL]
    print('entries labelled {0!r}: {1}'.format(LABEL, [e.index for e in dups]))
    print('')
    for e in dups:
        k = e.data
        print('  index {0:>3}  rank {1}  {2:<14} A={3:.4g} {4}  n={5}  Ea={6:.4g} kJ/mol  T0={7} K'.format(
            e.index, e.rank, e.short_desc,
            k.A.value, k.A.units, k.n.value_si,
            k.Ea.value_si / 1000.0, k.T0.value_si))
        print('           longDesc: {0}'.format(e.long_desc.strip()))
    print('')

    if len(dups) != 2:
        print('expected exactly 2 duplicates, found {0} -- aborting'.format(len(dups)))
        return 1

    dups.sort(key=lambda e: e.index)
    lo, hi = dups

    print('Ea as stated: {0:.5g} kJ/mol (index {1}) vs {2:.5g} kJ/mol (index {3})'.format(
        lo.data.Ea.value_si / 1000, lo.index, hi.data.Ea.value_si / 1000, hi.index))
    print('Ea/R        : {0:.6g} K        vs {1:.6g} K'.format(
        lo.data.Ea.value_si / 8.314462618, hi.data.Ea.value_si / 8.314462618))
    print('')

    print('k(T) in cm^3/(mol*s)   [rmgpy returns SI m^3/(mol*s); x1e6 to cm^3]')
    print('')
    print('{0:>7}  {1:>14}  {2:>14}  {3:>10}'.format(
        'T / K', 'index {0}'.format(lo.index), 'index {0}'.format(hi.index),
        '{0}/{1}'.format(lo.index, hi.index)))
    print('-' * 52)
    for T in TEMPERATURES:
        k1 = lo.data.get_rate_coefficient(T) * 1e6
        k2 = hi.data.get_rate_coefficient(T) * 1e6
        print('{0:>7}  {1:>14.4e}  {2:>14.4e}  {3:>10.3f}'.format(T, k1, k2, k1 / k2))

    Ts = np.linspace(300, 10000, 971)
    r = np.array([lo.data.get_rate_coefficient(float(T)) / hi.data.get_rate_coefficient(float(T))
                  for T in Ts])
    print('')
    print('ratio index{0}/index{1} over 300-10000 K: min {2:.3f} (at {3:.0f} K), '
          'max {4:.3f} (at {5:.0f} K)'.format(
              lo.index, hi.index, r.min(), Ts[r.argmin()], r.max(), Ts[r.argmax()]))

    # the window where this reaction is not utterly frozen out
    ks = np.array([lo.data.get_rate_coefficient(float(T)) * 1e6 for T in Ts])
    live = Ts[ks > 1e6]
    if len(live):
        print('index {0} exceeds 1e6 cm^3/(mol*s) above {1:.0f} K'.format(lo.index, live[0]))
        m = (Ts >= live[0])
        print('over that window the ratio runs {0:.3f} to {1:.3f}'.format(r[m].min(), r[m].max()))

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 7), sharex=True,
                                       gridspec_kw={'height_ratios': [3, 1]})
        x = 1000.0 / Ts
        for e, style in ((lo, '-'), (hi, '--')):
            y = [e.data.get_rate_coefficient(float(T)) * 1e6 for T in Ts]
            ax1.semilogy(x, y, style, label='index {0}  {1}'.format(e.index, e.short_desc))
        ax1.set_ylabel('k / cm$^3$ mol$^{-1}$ s$^{-1}$')
        ax1.set_title('NO$^+$ + O$_2$ $\\rightleftharpoons$ O$_2^+$ + NO, 300-10000 K')
        ax1.legend()
        ax1.grid(alpha=0.3)
        ax2.plot(x, r)
        ax2.axhline(1.0, color='k', lw=0.6)
        ax2.set_ylabel('k$_{%d}$ / k$_{%d}$' % (lo.index, hi.index))
        ax2.set_xlabel('1000 K / T')
        ax2.grid(alpha=0.3)
        fig.tight_layout()
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kT-comparison.png')
        fig.savefig(out, dpi=140)
        print('')
        print('plot written to {0}'.format(out))
    except Exception as exc:
        print('')
        print('plot skipped: {0}: {1}'.format(type(exc).__name__, exc))

    return 0


if __name__ == '__main__':
    sys.exit(main())
