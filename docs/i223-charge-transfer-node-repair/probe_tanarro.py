#!/usr/bin/env python
# encoding: utf-8
"""
I-223 rework: audit all twelve [Tanarro2015] training entries against Table 1 of the
primary document, row by row -- reaction, A, temperature exponent, T0 and Ea.

Primary source, read directly (not from a secondary compilation):
    M. Jimenez-Redondo, E. Carrasco, V.J. Herrero, I. Tanarro,
    "Chemistry in glow discharges of H2/O2 mixtures. Diagnostics and modelling",
    Plasma Sources Sci. Technol. 24 (2015) 015029, DOI 10.1088/0963-0252/24/1/015029.
    Open author manuscript: https://europepmc.org/articles/PMC4685741?pdf=render
    Table 1, section "Ion-ion neutralization", rows IN1-IN23.
    Rates are printed as  k = A (Tg/300)^n  cm^3/s, with Tg in K -- hence T0 = 300 K, which is
    what these entries carry and is correct (contrast [Gupta1990], which is bare-T; see the
    header note in training/reactions.py).

WHY THIS PROBE EXISTS, beyond checking digits.

Of the 23 ion-ion neutralization rows in that table, 18 carry the SAME expression,
2e-7 (Tg/300)^-0.5, and 16 of those cite the same single reference [56] -- Kossyi, Kostinsky,
Matveyev & Silakov, Plasma Sources Sci. Technol. 1 (1992) 207, a kinetic-scheme review rather
than a measurement of any particular pair.  The rows that differ are exactly the ones with a
pair-specific source: IN1 1.8e-7 [21], IN4 2.3e-7 [60], IN12 exponent -1 [57], IN17 1e-7 with no
T dependence, IN23 4e-7 [21].

So where several of these entries agree exactly, that is ONE class estimate quoted several
times, not several determinations that happen to agree.  The paper gives its own reason for not
refining them: "Other mechanisms such as electron impact neutralization and ion-ion
recombination are also considered, but their importance is orders of magnitude lower", and "The
relevance of the negative ion processes in the global chemistry of the discharge is low".

This matters to probe_collisions.py.  Two template merges in this family are lossless only
because the numbers on both sides are the same class estimate.  That is a property of the
SOURCE, not evidence that the tree is right, and it expires the day anyone supplies a real
measurement for one of those pairs.
"""

import os
import sys
import traceback

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

# Table 1, ion-ion neutralization block, transcribed from the rows this family uses.
# (row, reaction as printed, A / cm^3 s^-1, exponent on (Tg/300), reference as cited by Table 1)
TABLE1 = {
    1:  ('IN1',  'H+ + H- -> 2H',            1.8e-7, -0.5, '[21] Konstantinovskii 2005'),
    2:  ('IN2',  'H2+ + H- -> H + H2',       2.0e-7, -0.5, '[71] Scott 1996'),
    3:  ('IN4',  'O+ + H- -> H + O',         2.3e-7, -0.5, '[60] Millar 1997 (UMIST)'),
    4:  ('IN5',  'O2+ + H- -> H + O2',       2.0e-7, -0.5, '[56] Kossyi 1992'),
    5:  ('IN7',  'H2O+ + H- -> H + H2O',     2.0e-7, -0.5, '[56] Kossyi 1992'),
    6:  ('IN9',  'H+ + O- -> H + O',         2.0e-7, -0.5, '[56] Kossyi 1992'),
    7:  ('IN12', 'O+ + O- -> 2O',            2.0e-7, -1.0, '[57] Stafford 2004'),
    8:  ('IN13', 'O2+ + O- -> O2 + O',       2.0e-7, -0.5, '[73] Gudmundsson 2007'),
    9:  ('IN15', 'H2O+ + O- -> O + H2O',     2.0e-7, -0.5, '[56] Kossyi 1992'),
    10: ('IN20', 'O2+ + OH- -> OH + O2',     2.0e-7, -0.5, '[56] Kossyi 1992'),
    11: ('IN21', 'OH+ + OH- -> 2OH',         2.0e-7, -0.5, '[56] Kossyi 1992'),
    12: ('IN22', 'H2O+ + OH- -> H2O + OH',   2.0e-7, -0.5, '[56] Kossyi 1992'),
}

# How many of the 23 rows in that block share the generic value, and how many cite Kossyi for it.
GENERIC_ROWS_IN_TABLE = 18
GENERIC_ROWS_CITING_KOSSYI = 16
TOTAL_IN_ROWS = 23

TOL = 1e-9

# A discrepancy below this factor is a transcription slip: correct the digit in place, recording
# the row and the corrected value.  At or above it, STOP and report the row without touching it.
# An order of magnitude is not a typo -- it is usually a units or convention mismatch, and
# rescaling A to make k(T) look right would leave the convention error in the file, invisible.
# Entry 13 of this very family is the precedent: it read as a wrong number and was actually a
# wrong T0 (bare-T Gupta fit carrying the Tanarro (T/300) convention), worth 561x.
ORDER_OF_MAGNITUDE = 10.0


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()
    by_index = {e.index: e for e in dep.entries.values()}

    missing = sorted(i for i in TABLE1 if i not in by_index)
    if missing:
        print('PRECONDITION NOT MET: training entries {0} are not in the depository.'.format(missing))
        print('This probe audits the twelve [Tanarro2015] entries, indices 1-12.')
        return 2

    row = '{0:<4} {1:<6} {2:<30} {3:>10} {4:>10} {5:>6} {6:>6} {7:>6} {8}'
    header = row.format('idx', 'row', 'reaction (as in Table 1)', 'A source', 'A entered',
                        'n src', 'n ent', 'T0', 'verdict')
    print(header)
    print('-' * len(header))

    bad = 0
    for idx in sorted(TABLE1):
        tag, rxn, A_src, n_src, ref = TABLE1[idx]
        e = by_index[idx]
        k = e.data
        # entries are written in cm^3/(molecule*s), the same unit Table 1 prints
        A_ent = k.A.value
        n_ent = k.n.value_si
        T0 = k.T0.value_si
        Ea = k.Ea.value_si

        problems = []
        severe = False
        if abs(A_ent - A_src) / A_src > 1e-6:
            factor = A_ent / A_src
            spread = max(factor, 1.0 / factor)
            problems.append('A off by {0:.4g}x'.format(factor))
            if spread >= ORDER_OF_MAGNITUDE:
                severe = True
        if abs(n_ent - n_src) > TOL:
            problems.append('n is {0} not {1}'.format(n_ent, n_src))
            severe = True   # an exponent is never a typo-sized error over 300-10000 K
        if abs(T0 - 300.0) > TOL:
            problems.append('T0 is {0:g} K, Table 1 is (Tg/300)'.format(T0))
            severe = True   # a T0 mismatch is a convention error, the entry-13 failure mode
        if abs(Ea) > TOL:
            problems.append('Ea is {0:g} J/mol, Table 1 row has none'.format(Ea))
            severe = True
        if 'cm^3/(molecule*s)' not in str(k.A.units):
            problems.append('units are {0}, Table 1 is cm^3/s per molecule'.format(k.A.units))
            severe = True

        if not problems:
            verdict = 'OK'
        elif severe:
            verdict = 'STOP -- REPORT, DO NOT FIX: ' + '; '.join(problems)
            bad += 1
        else:
            verdict = 'correct in place: ' + '; '.join(problems)
            bad += 1
        print(row.format(idx, tag, rxn, '{0:.3g}'.format(A_src), '{0:.3g}'.format(A_ent),
                         n_src, n_ent, '{0:g}'.format(T0), verdict))

    print('')
    print('cited source per row (from Table 1, not from this file):')
    for idx in sorted(TABLE1):
        print('  entry {0:>2}  {1:<6} {2}'.format(idx, TABLE1[idx][0], TABLE1[idx][4]))

    print('')
    print('provenance of the repeated value')
    print('  {0} of the {1} ion-ion neutralization rows in Table 1 carry 2e-7 (Tg/300)^-0.5;'.format(
        GENERIC_ROWS_IN_TABLE, TOTAL_IN_ROWS))
    print('  {0} of those cite one reference, Kossyi 1992, a kinetic-scheme review.'.format(
        GENERIC_ROWS_CITING_KOSSYI))
    print('  Rows with a pair-specific source carry pair-specific numbers (IN1, IN4, IN12,')
    print('  IN17, IN23).  Agreement among the rest is one estimate quoted many times.')
    print('  => where two of these entries are merged onto one template node, the merge is')
    print('     lossless because the SOURCE is coarse, not because the tree is right.')

    print('')
    print('rule applied to each mismatch')
    print('  below {0:g}x  -> transcription slip; correct the digit in place, record the row.'.format(
        ORDER_OF_MAGNITUDE))
    print('  at or above, or any n / T0 / Ea / units mismatch -> STOP, report, leave it alone:')
    print('    that size of error is a units or convention problem, and rescaling A to make k(T)')
    print('    look right would bury it.  Entry 13 of this family was exactly that case (561x).')

    print('')
    print('{0} of {1} [Tanarro2015] entries disagree with Table 1'.format(bad, len(TABLE1)))
    return 1 if bad else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
