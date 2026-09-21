#!/usr/bin/env python
# encoding: utf-8
"""
I-223: the two [Gupta1990] training entries carry T0 = 300 K, but Gupta's
Table II is written as  k = Cf * T^eta * exp(-theta_d / T)  -- a bare T, i.e.
T0 = 1 K.  RMG evaluates A*(T/T0)^n, so an entry that copies Cf verbatim and
leaves T0 at 300 K is wrong by a factor of 300^n.

Source (OCR of NASA RP-1232, Table II, p.45):
    R11   O + O2+  <=> O2 + O+    2.92e18 T^-1.11 exp(-2.8e4/T)
    R19   O2 + NO+ <=> NO + O2+   1.8e15  T^ 0.17 exp(-3.3e4/T)
Both in cm^3/(mole-sec).  Neither carries a (T/300) normalisation.

The 12 [Tanarro2015] entries above them in the file DO use the (T/300) form,
which is the low-temperature plasma convention -- that is where the 300 came
from.  Entries 13 and 17 sit immediately after that block.
"""

import os
import sys

import numpy as np

from rmgpy import settings
from rmgpy.kinetics import Arrhenius

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

# Gupta Table II, as printed
GUPTA = {
    13: dict(label='O2p_r1 + O_r2 <=> O2 + Op', row='R11', Cf=2.92e18, eta=-1.11, theta=2.8e4),
    17: dict(label='NOp_r1 + O2_r2 <=> O2p + NO', row='R19', Cf=1.8e15, eta=0.17, theta=3.3e4),
}

TEMPERATURES = [300, 1000, 2000, 4000, 6000, 10000]
R = 8.314462618


def langevin(alpha_A3, m1_amu, m2_amu):
    """Langevin capture rate, cm^3/(mol*s).  alpha in angstrom^3."""
    e = 4.80320425e-10          # statcoulomb
    alpha = alpha_A3 * 1e-24    # cm^3
    mu = m1_amu * m2_amu / (m1_amu + m2_amu) * 1.66053907e-24  # g
    k_cm3_per_s = 2 * np.pi * e * np.sqrt(alpha / mu)
    return k_cm3_per_s * 6.02214076e23


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('')

    family = load_family()
    dep = family.get_training_depository()
    by_index = {e.index: e for e in dep.entries.values()}

    # This probe is an argument ABOUT the pre-edit file: it needs both [Gupta1990] entries as they
    # were originally transcribed, including index 17, which the edit it justifies then deletes.
    # Run against this branch's HEAD it would otherwise die on a bare KeyError, so say what it wants.
    missing = sorted(i for i in GUPTA if i not in by_index)
    if missing:
        print('PRECONDITION NOT MET')
        print('  training entries present : {0}'.format(sorted(by_index)))
        print('  missing                  : {0}'.format(missing))
        print('')
        print('  This probe reads the two [Gupta1990] entries as originally transcribed, index 13')
        print('  and index 17.  Index 17 is the duplicate NO+/O2 rate that I-223 deleted and index')
        print("  13's T0 was corrected in the same commit, so neither is in this branch's HEAD in")
        print('  its original form.  Point the probe at a pre-edit checkout of the family:')
        print('')
        print('      git worktree add <dir> {0}   # or any commit at or before the base'.format(
            'd07add74a'))
        print('      I223_FAMILY_ROOT=<dir>/docs/i154-carry-chemistry/held-back \\')
        print('          ./run.sh t0 probe_t0.py')
        print('')
        print('  The saved evidence for the original run is logs/t0.stdout.log.')
        return 2

    for idx, g in GUPTA.items():
        e = by_index[idx]
        k = e.data
        print('=' * 78)
        print('entry {0}  {1}   [Gupta1990] Table II {2}'.format(idx, g['label'], g['row']))
        print('  source form     : k = {0:.3g} * T^{1} * exp(-{2:.0f}/T)   cm^3/(mol*s)'.format(
            g['Cf'], g['eta'], g['theta']))
        print('  as entered      : A = {0:.4g} {1}, n = {2}, Ea = {3:.6g} {4}, T0 = {5:g} K'.format(
            k.A.value, k.A.units, k.n.value_si, k.Ea.value, k.Ea.units, k.T0.value_si))
        print('  Ea/R as entered : {0:.6g} K   (source theta_d = {1:.0f} K)'.format(
            k.Ea.value_si / R, g['theta']))
        print('  A == Cf?        : {0}'.format(abs(k.A.value - g['Cf']) / g['Cf'] < 1e-6))
        print('  => the entry copies Cf verbatim but declares T0 = {0:g} K, so every k it returns'.format(
            k.T0.value_si))
        print('     is off by 300^{0} = {1:.4g}x  ({2})'.format(
            g['eta'], 300.0 ** g['eta'],
            'too LOW' if g['eta'] > 0 else 'too HIGH'))

        fixed = Arrhenius(A=(g['Cf'], 'cm^3/(mol*s)'), n=g['eta'],
                          Ea=(g['theta'] * R, 'J/mol'), T0=(1, 'K'),
                          Tmin=(300, 'K'), Tmax=(10000, 'K'))
        print('')
        print('  {0:>7}  {1:>13}  {2:>13}  {3:>9}'.format(
            'T / K', 'as entered', 'source form', 'ratio'))
        for T in TEMPERATURES:
            k1 = k.get_rate_coefficient(T) * 1e6
            k2 = fixed.get_rate_coefficient(T) * 1e6
            print('  {0:>7}  {1:>13.4e}  {2:>13.4e}  {3:>9.4g}'.format(T, k1, k2, k2 / k1))
        print('')

    print('=' * 78)
    print('the duplicate, both evaluated in their OWN source convention')
    print('=' * 78)
    gupta = Arrhenius(A=(GUPTA[17]['Cf'], 'cm^3/(mol*s)'), n=GUPTA[17]['eta'],
                      Ea=(GUPTA[17]['theta'] * R, 'J/mol'), T0=(1, 'K'),
                      Tmin=(300, 'K'), Tmax=(10000, 'K'))
    ozawa = by_index[21].data

    k_l = langevin(1.58, 30.006, 31.999)   # alpha(O2)=1.58 A^3; NO+ vs O2
    print('Langevin capture rate for NO+ + O2 : {0:.3e} cm^3/(mol*s)'.format(k_l))
    print('(the reaction is endothermic by IE(O2) - IE(NO) = 12.0697 - 9.2642 eV')
    print(' = 2.8055 eV = 270.7 kJ/mol; Ozawa Ea = 271.1, Gupta theta_d*R = 274.4)')
    print('')
    print('{0:>7}  {1:>13}  {2:>13}  {3:>8}  {4:>14}  {5:>14}'.format(
        'T / K', 'Gupta (T0=1)', 'Ozawa idx21', 'G/O', 'G prefac/kL', 'O prefac/kL'))
    print('-' * 82)
    for T in TEMPERATURES + [8000]:
        kg = gupta.get_rate_coefficient(T) * 1e6
        ko = ozawa.get_rate_coefficient(T) * 1e6
        pg = GUPTA[17]['Cf'] * T ** GUPTA[17]['eta']
        po = ozawa.A.value * T ** ozawa.n.value_si
        print('{0:>7}  {1:>13.4e}  {2:>13.4e}  {3:>8.3f}  {4:>14.2f}  {5:>14.2f}'.format(
            T, kg, ko, kg / ko, pg / k_l, po / k_l))
    print('')
    print('"prefac/kL" is A*T^n divided by the Langevin capture rate: how many times the')
    print('ion-molecule collision limit the fit would demand if every super-threshold')
    print('collision reacted. A value far above ~1 is unphysical for a capture-limited')
    print('charge transfer.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
