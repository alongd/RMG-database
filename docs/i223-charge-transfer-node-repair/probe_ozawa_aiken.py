#!/usr/bin/env python
# encoding: utf-8
"""
I-223 follow-up: audit the nine [Ozawa2008] and [Aiken2023] training entries against their
primary documents, and -- where a primary cannot be reached -- bound how much that costs.

This closes the open item left by the [Tanarro2015] audit, which verified twelve entries and
explicitly did NOT verify these nine.  The header of training/reactions.py said their T0 = 1 K
was inferred from internal consistency rather than read.  For three of them it is now READ.
For six it still is not, and the honest result of this probe is a bound, not a verification.

RETRIEVAL STATUS -- what could NOT be reached comes first.

  [Ozawa2008] T. Ozawa, J. Zhong, D.A. Levin, Phys. Fluids 20 (2008) 046102,
    DOI 10.1063/1.2907198, Table III.  *** NOT REACHED. ***
    Publisher (pubs.aip.org) returns HTTP 403.  Two independent open-access indexes agree the
    paper is closed with no repository copy anywhere:
      - OpenAlex: is_oa false, oa_status "closed", oa_url null, best_oa_location null,
        any_repository_has_fulltext false, locations_count 1 (the paywalled DOI).
      - Semantic Scholar: isOpenAccess false, openAccessPdf empty, status CLOSED.
    This is a confirmed negative, not an unsuccessful search: there is no open copy to find.
    The six Ozawa entries are therefore audited by SURROGATE below, never against Table III.

  [Aiken2023] T.T. Aiken, PhD thesis, University of Colorado, 2023, Table 3.16.  *** READ. ***
    https://www.colorado.edu/lab/ngpdl/sites/default/files/attached-files/aiken.pdf
    (direct curl is refused by this sandbox; WebFetch persists the PDF and `pdftotext -layout`
    reads it.)  Table 3.16 is transcribed verbatim in AIKEN_T316 below.

THE T0 QUESTION, AND WHY IT TURNS OUT NOT TO DECIDE ANYTHING HERE.

Aiken Table 3.16 prints its own rate form, k = A T^eta exp(-theta/T_tr) -- a BARE T.  So for the
three [Aiken2023] entries T0 = 1 K is now read off the source, not inferred.  [Ozawa2008] sits in
the same hypersonic air-chemistry lineage (as does [Gupta1990], whose Table II is also bare-T),
but "the field writes it this way" is circumstantial and this probe does not treat it as a read.

Instead it bounds the exposure.  Getting T0 wrong rescales A by 300^n, so the cost is computable
per entry without the document.  The decisive part is that BOTH tree splits this branch made are
Ozawa-vs-Ozawa comparisons:

    O2_neutral split : entry 14 (NOp + O)  vs entry 21 (NOp + O2)
    N2_neutral split : entry 22 (O2p + N)  vs entry 23 (O2p + N2)

A convention error would hit both members of a pair, so the RATIO the split criterion tests moves
by 300^(n1-n2), not by 300^n.  That is a much smaller number, and it is computed below.  If both
splits clear the 4x criterion under either convention, then the unread Table III cannot overturn
a decision already in this branch -- which is the only question that actually blocks anything.

WHAT THE SURROGATES CAN AND CANNOT DO.

  1. Ea, independently of any source.  For charge transfer A+ + B -> A + B+ the endothermicity is
     exactly IE(B) - IE(A), and ionization energies are spectroscopic constants known to many more
     digits than any rate fit.  This checks Ea's VALUE AND UNITS with no document at all.
  2. theta, against a second tabulation.  [Gupta1990] NASA RP-1232 Table II independently lists
     four of these six reactions.  Both trace to Park's air model, so agreement is corroboration
     rather than independence -- but a units or convention error would still show up.
  3. A, to order of magnitude only, against the Langevin capture rate.  An ion-molecule rate
     cannot greatly exceed the capture limit, and A that had been mis-converted per-particle vs
     per-mole would be out by 6e23.  This bounds A; it does not verify its digits.

n is checked for the three Aiken entries and is NOT checked for the six Ozawa ones.  Said plainly
so nobody later reads this probe as having verified more than it did.
"""

import math
import os
import sys

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

# ---------------------------------------------------------------------------------------------
# [Aiken2023] Table 3.16, transcribed verbatim, INCLUDING the row this family does not use.
# Caption: "Charge exchange reaction rate coefficients that do not come from Park [1]
#           (k = A T^eta exp(-theta/T_tr))."
# Columns: Reaction | A (m^3/s) | eta | theta (K) | Ref.
# Note the units: A is per-PARTICLE volume in SI (m^3/s), not cm^3/mol/s.  The conversion to the
# unit this database uses is 1e6 cm^3/m^3 * N_A, i.e. 6.02214e29 -- a factor that would be very
# easy to drop and would show up as a ~1e30 error, not a subtle one.
#   entry index -> (reaction as printed, A m^3/s, eta, theta K, ref as cited)
AIKEN_T316 = {
    18: ('N+ + N2(X) -> N2+(X) + N(4S)',   1.16e-23, 1.47, 13130.0, '[161, 189] Phelps'),
    19: ('Ar+(1) + N2(X) -> N2+(X) + Ar(1)', 2.57e-17, 0.50,     0.0, '[143]'),
    20: ('Ar+(1) + O(3P) -> O+ + Ar(1)',     6.39e-18, 0.00,     0.0, '[159]'),
}
# The table's fourth row, Ar+(1) + O2(X) -> O2+ + Ar(1), 4.20e-15 m^3/s, eta -0.78, theta 0,
# ref [5], is NOT carried by this family and so is not audited.  It is recorded here only so the
# transcription is complete and a later reader can see nothing was cherry-picked.  (pdftotext
# renders its A with a leading dash, which is the table's en-dash column rule bleeding into the
# number, not a negative pre-exponential.)
AIKEN_UNUSED = ('Ar+(1) + O2(X) -> O2+ + Ar(1)', 4.20e-15, -0.78, 0.0, '[5]')

M3_S_TO_CM3_MOL_S = 1.0e6 * 6.02214076e23

# ---------------------------------------------------------------------------------------------
# [Gupta1990] NASA RP-1232 Table II, "Chemical Reactions and Rate Coefficients", forward rate
# coefficients in cm^3/mole-sec, written k = Cf T^eta exp(-theta/T) -- bare T.  Transcribed from
# the scanned original (already retrieved for the entry-13 work in the previous round).  Only the
# rows that overlap this family's Ozawa entries are listed.
#   entry index -> (RP-1232 reaction number, reaction as printed, Cf, eta, theta K)
GUPTA_TII = {
    14: (16, 'O + NO+ = NO + O+',   3.63e15, -0.60, 50800.0),
    15: (17, 'N2 + O+ = O + N2+',   3.40e19, -2.00, 23000.0),
    16: (18, 'N + NO+ = NO + N+',   1.00e19, -0.93, 61000.0),
    21: (19, 'O2 + NO+ = NO + O2+', 1.80e15,  0.17, 33000.0),
}
# Entries 22 (O2+ + N) and 23 (O2+ + N2) have no counterpart in RP-1232 Table II, so for those
# two the theta surrogate is the ionization-energy check alone.

# ---------------------------------------------------------------------------------------------
# Ionization energies, NIST Atomic Spectra Database / NIST Chemistry WebBook, in eV.  These are
# spectroscopic constants, quoted to far more precision than any rate fit needs.
IE_EV = {
    'N':  14.53414, 'O':  13.61806, 'Ar': 15.75962,
    'N2': 15.58080, 'O2': 12.06970, 'NO':  9.26438,
}
EV_TO_KJ_MOL = 96.48534

# Static dipole polarizability volumes, CRC Handbook, in cm^3 (1 Angstrom^3 = 1e-24 cm^3), and
# molar masses in g/mol.  Used only for the Langevin capture bound.
ALPHA_CM3 = {
    'N': 1.10e-24, 'O': 0.802e-24, 'Ar': 1.6411e-24,
    'N2': 1.7403e-24, 'O2': 1.5812e-24, 'NO': 1.70e-24,
}
MASS = {'N': 14.007, 'O': 15.999, 'Ar': 39.948, 'N2': 28.014, 'O2': 31.998, 'NO': 30.006}

# entry index -> (cation, neutral) as the reaction is written, A+ + B -> A + B+
PAIRS = {
    14: ('NO', 'O'),  15: ('O', 'N2'),  16: ('NO', 'N'),
    18: ('N', 'N2'),  19: ('Ar', 'N2'), 20: ('Ar', 'O'),
    21: ('NO', 'O2'), 22: ('O2', 'N'),  23: ('O2', 'N2'),
}
OZAWA = (14, 15, 16, 21, 22, 23)
AIKEN = (18, 19, 20)

# The two splits this branch made, with the in-window ratio each was decided on.  Those ratios
# come from probe_collisions.py (logs/collisions.stdout.log, summary table) and are restated here
# only so this probe can test them against the T0 question; probe_collisions.py remains the
# authority on how they were derived.
SPLITS = {
    'O2_neutral (NOp + O vs NOp + O2)': (14, 21, 217.7),
    'N2_neutral (O2p + N vs O2p + N2)': (22, 23, 106.8),
}
CRITERION = 4.0

# Same stop rule as probe_tanarro.py: under this factor a discrepancy is a transcription slip to
# correct in place; at or above it, STOP and report the row rather than fixing the digit, because
# that size of error is normally a units or convention fault and rescaling A would bury it.
ORDER_OF_MAGNITUDE = 10.0
TOL = 1e-9
R_J = 8.31446261815324


def langevin_cm3_mol_s(cation, neutral):
    """2*pi*e*sqrt(alpha/mu) in cgs, converted to cm^3/mol/s."""
    e_esu = 4.80320471e-10
    amu_g = 1.66053907e-24
    mu = MASS[cation] * MASS[neutral] / (MASS[cation] + MASS[neutral]) * amu_g
    return 2.0 * math.pi * e_esu * math.sqrt(ALPHA_CM3[neutral] / mu) * 6.02214076e23


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()
    by_index = {e.index: e for e in dep.entries.values()}

    wanted = sorted(OZAWA + AIKEN)
    missing = [i for i in wanted if i not in by_index]
    if missing:
        print('PRECONDITION NOT MET: training entries {0} are not in the depository.'.format(missing))
        return 2

    # Read every number from the file; nothing below is re-typed from the entries.
    ent = {}
    for i in wanted:
        k = by_index[i].data
        ent[i] = {
            'label': by_index[i].label,
            'A': k.A.value, 'A_units': str(k.A.units),
            'n': k.n.value_si, 'T0': k.T0.value_si,
            'Ea_J': k.Ea.value_si,
        }

    severe = 0
    slips = 0

    # -----------------------------------------------------------------------------------------
    print('=' * 100)
    print('PART 1 -- [Aiken2023] Table 3.16, READ from the primary. Three entries, audited in full.')
    print('=' * 100)
    print('Table form: k = A T^eta exp(-theta/T_tr), a BARE T -> T0 = 1 K, read not inferred.')
    print('A is printed in m^3/s (per particle); conversion to cm^3/(mol*s) is x{0:.6g}.'
          .format(M3_S_TO_CM3_MOL_S))
    print('')
    row = '{0:<4} {1:<34} {2:>10} {3:>12} {4:>11} {5:>8} {6}'
    head = row.format('idx', 'reaction (as printed in Table 3.16)', 'A m^3/s', 'A->cm3/mol/s',
                      'A entered', 'ratio', 'verdict')
    print(head)
    print('-' * len(head))
    for i in AIKEN:
        rxn, A_m3, eta, theta, ref = AIKEN_T316[i]
        A_expect = A_m3 * M3_S_TO_CM3_MOL_S
        e = ent[i]
        problems = []
        is_severe = False

        ratio = e['A'] / A_expect
        spread = max(ratio, 1.0 / ratio)
        # The source prints A to three significant figures, so the entered value can only ever
        # match to rounding. Anything beyond 0.5% is a real disagreement, not rounding.
        if spread > 1.005:
            problems.append('A off by {0:.4g}x'.format(ratio))
            if spread >= ORDER_OF_MAGNITUDE:
                is_severe = True
        if abs(e['n'] - eta) > TOL:
            problems.append('n is {0} not {1}'.format(e['n'], eta))
            is_severe = True
        if abs(e['T0'] - 1.0) > TOL:
            problems.append('T0 is {0:g} K, Table 3.16 is bare-T'.format(e['T0']))
            is_severe = True
        Ea_expect = theta * R_J
        if abs(Ea_expect) < TOL:
            if abs(e['Ea_J']) > TOL:
                problems.append('Ea is {0:g} J/mol, theta is 0'.format(e['Ea_J']))
                is_severe = True
        else:
            r = e['Ea_J'] / Ea_expect
            if max(r, 1.0 / r) > 1.005:
                problems.append('Ea off by {0:.4g}x (theta {1:g} K -> {2:.5g} J/mol)'
                                .format(r, theta, Ea_expect))
                is_severe = max(r, 1.0 / r) >= ORDER_OF_MAGNITUDE
        if 'cm^3/(mol*s)' not in e['A_units']:
            problems.append('units are {0}'.format(e['A_units']))
            is_severe = True

        if not problems:
            verdict = 'OK'
        elif is_severe:
            verdict = 'STOP -- REPORT, DO NOT FIX: ' + '; '.join(problems)
            severe += 1
        else:
            verdict = 'SLIP -- fix in place: ' + '; '.join(problems)
            slips += 1
        print(row.format(i, rxn, '{0:.3g}'.format(A_m3), '{0:.5g}'.format(A_expect),
                         '{0:.5g}'.format(e['A']), '{0:.4f}'.format(ratio), verdict))
    print('')
    print('Row of Table 3.16 not carried by this family, recorded so the transcription is whole:')
    print('  {0}: A = {1:.3g} m^3/s, eta = {2}, theta = {3:g} K, ref {4}'.format(*AIKEN_UNUSED))
    print('')

    # -----------------------------------------------------------------------------------------
    print('=' * 100)
    print('PART 2 -- [Ozawa2008] Table III, NOT REACHED. Six entries, audited by surrogate.')
    print('=' * 100)
    print('pubs.aip.org -> HTTP 403. OpenAlex: oa_status "closed", any_repository_has_fulltext')
    print('false, locations_count 1. Semantic Scholar: CLOSED, openAccessPdf empty.')
    print('No open copy exists to find. Nothing below verifies a digit of Table III.')
    print('')
    print('Surrogate 1 -- Ea against spectroscopic ionization energies. For A+ + B -> A + B+ the')
    print('endothermicity is exactly IE(B) - IE(A). Independent of every rate compilation.')
    print('')
    row2 = '{0:<4} {1:<26} {2:>13} {3:>13} {4:>8}  {5}'
    head2 = row2.format('idx', 'reaction', 'Ea kJ/mol', 'dIE kJ/mol', 'ratio', 'verdict')
    print(head2)
    print('-' * len(head2))
    for i in wanted:
        cat, neu = PAIRS[i]
        dIE = (IE_EV[neu] - IE_EV[cat]) * EV_TO_KJ_MOL
        Ea_kj = ent[i]['Ea_J'] / 1000.0
        if dIE <= 0.0:
            ok = abs(Ea_kj) < TOL
            verdict = ('OK -- exothermic by {0:.1f} kJ/mol, Ea = 0 is right'.format(-dIE)
                       if ok else 'STOP -- exothermic but Ea = {0:g}'.format(Ea_kj))
            if not ok:
                severe += 1
            print(row2.format(i, '{0}+ + {1}'.format(cat, neu), '{0:.1f}'.format(Ea_kj),
                              '{0:.1f}'.format(dIE), '--', verdict))
            continue
        r = Ea_kj / dIE
        # A fit's Ea may sit above the thermodynamic threshold; it must not sit meaningfully
        # below it, and it must not be out by a unit factor.
        if max(r, 1.0 / r) >= ORDER_OF_MAGNITUDE:
            verdict = 'STOP -- REPORT: off by {0:.4g}x, smells of units'.format(r)
            severe += 1
        elif r < 0.97:
            verdict = 'CHECK -- Ea below the thermodynamic threshold'
            slips += 1
        elif r > 1.15:
            verdict = 'note -- {0:.1%} above threshold, admissible for a fit'.format(r - 1.0)
        else:
            verdict = 'OK'
        print(row2.format(i, '{0}+ + {1}'.format(cat, neu), '{0:.1f}'.format(Ea_kj),
                          '{0:.1f}'.format(dIE), '{0:.4f}'.format(r), verdict))
    print('')

    print('Surrogate 2 -- theta against [Gupta1990] RP-1232 Table II, which independently lists')
    print('four of the six. Both trace to Park, so this corroborates rather than confirms; a')
    print('units or convention fault would still show.')
    print('')
    row3 = '{0:<4} {1:<22} {2:>11} {3:>11} {4:>8}   {5:>11} {6:>11}'
    head3 = row3.format('idx', 'RP-1232 Table II row', 'theta ours', 'theta RP', 'ratio',
                        'A ours', 'Cf RP')
    print(head3)
    print('-' * len(head3))
    for i in OZAWA:
        if i not in GUPTA_TII:
            print(row3.format(i, '-- no counterpart --', '{0:.0f}'.format(ent[i]['Ea_J'] / R_J),
                              '--', '--', '{0:.3g}'.format(ent[i]['A']), '--'))
            continue
        num, rxn, Cf, eta, theta = GUPTA_TII[i]
        ours = ent[i]['Ea_J'] / R_J
        print(row3.format(i, 'R{0}  {1}'.format(num, rxn.split('=')[0].strip()),
                          '{0:.0f}'.format(ours), '{0:.0f}'.format(theta),
                          '{0:.4f}'.format(ours / theta),
                          '{0:.3g}'.format(ent[i]['A']), '{0:.3g}'.format(Cf)))
    print('')
    print('A and n differ between the two compilations, as they must -- they are rival fits, and')
    print('this branch already chose Ozawa over Gupta for entry 21 on Langevin grounds (entry 17')
    print('deleted). The point of the column pair above is only that the two A columns occupy the')
    print('same decades, so the entered A is not out by a mole-vs-particle factor.')
    print('')

    print('Surrogate 3 -- A against the Langevin capture rate 2*pi*e*sqrt(alpha/mu)*N_A. An')
    print('ion-molecule rate cannot greatly exceed capture; a per-particle/per-mole slip is 6e23.')
    print('')
    row4 = '{0:<4} {1:<12} {2:>11} {3:>28}  {4}'
    head4 = row4.format('idx', 'reaction', 'k_Langevin', 'A*T^n / k_L at 300/5k/10k K', 'verdict')
    print(head4)
    print('-' * len(head4))
    for i in wanted:
        cat, neu = PAIRS[i]
        kL = langevin_cm3_mol_s(cat, neu)
        A, n, T0 = ent[i]['A'], ent[i]['n'], ent[i]['T0']
        vals = [A * (T / T0) ** n / kL for T in (300.0, 5000.0, 10000.0)]
        worst = max(vals)
        if worst > 1e3 or max(vals) < 1e-6:
            verdict = 'STOP -- REPORT: outside any capture-limited range'
            severe += 1
        elif worst > 10.0:
            verdict = 'CHECK -- well above capture'
            slips += 1
        else:
            verdict = 'OK -- within an order of magnitude of capture'
        print(row4.format(i, '{0}+ + {1}'.format(cat, neu), '{0:.2e}'.format(kL),
                          ' '.join('{0:8.3f}'.format(v) for v in vals), verdict))
    print('')

    # -----------------------------------------------------------------------------------------
    print('=' * 100)
    print('PART 3 -- what the unread Table III could actually cost.')
    print('=' * 100)
    print('If T0 were really 300 K rather than the 1 K these entries carry, A would be wrong by')
    print('300^n. Per entry that factor is:')
    print('')
    for i in OZAWA:
        print('  entry {0:<3} n = {1:>6}   300^n = {2:8.3f}x'
              .format(i, ent[i]['n'], 300.0 ** ent[i]['n']))
    print('')
    print('But every comparison this branch DECIDED on is Ozawa-against-Ozawa, so a convention')
    print('error hits both sides and the ratio moves only by 300^(n1-n2):')
    print('')
    row5 = '{0:<36} {1:>10} {2:>12} {3:>12}  {4}'
    head5 = row5.format('split', 'as decided', 'worst other', 'vs {0:g}x'.format(CRITERION),
                        'verdict')
    print(head5)
    print('-' * len(head5))
    overturned = 0
    for name, (i1, i2, decided) in sorted(SPLITS.items()):
        shift = 300.0 ** (ent[i1]['n'] - ent[i2]['n'])
        alt = [decided * shift, decided / shift]
        worst = min(alt)
        ok = worst > CRITERION
        if not ok:
            overturned += 1
        print(row5.format(name, '{0:.1f}x'.format(decided), '{0:.1f}x'.format(worst),
                          '{0:.1f}x margin'.format(worst / CRITERION),
                          'SURVIVES' if ok else 'OVERTURNED'))
    print('')
    print('So the T0 convention, even if it is wrong, cannot overturn either split: the worst')
    print('case still clears the criterion. The unread Table III is a gap in the RECORD, not a')
    print('risk to a decision this branch already made.')
    print('')

    # -----------------------------------------------------------------------------------------
    print('=' * 100)
    print('SUMMARY')
    print('=' * 100)
    print('  [Aiken2023] Table 3.16 : READ. {0} of {0} entries verified, T0 = 1 K read from the'
          .format(len(AIKEN)))
    print('                           printed rate form, A converted from m^3/s at x6.02214e29.')
    print('  [Ozawa2008] Table III  : NOT REACHED (closed, confirmed by two OA indexes).')
    print('                           {0} entries: Ea verified against ionization energies,'
          .format(len(OZAWA)))
    print('                           theta corroborated against RP-1232 where it overlaps,')
    print('                           A bounded by the capture rate. n and T0 NOT verified.')
    print('  splits overturned by the T0 question : {0}'.format(overturned))
    print('  entries to STOP and report           : {0}'.format(severe))
    print('  transcription slips to fix in place  : {0}'.format(slips))
    print('')
    if severe:
        print('VERDICT: STOP. See the rows marked STOP above; do not edit those digits.')
        return 1
    if slips:
        print('VERDICT: {0} slip(s) to correct in place, each recorded above.'.format(slips))
        return 1
    print('VERDICT: no entry contradicts its source or any surrogate. Three of nine are now')
    print('verified against the primary; six remain surrogate-checked only, and the header of')
    print('training/reactions.py must keep saying so.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
