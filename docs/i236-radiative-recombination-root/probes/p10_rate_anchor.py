#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 10 -- the rate anchor for the pairing family's root rule.

Evaluates the sibling library's sourced argon entry, PlasmaRadiativeRecombination
index 1 ([Arp] => [Ar]), at the campaign's working points, using the engine's own
two-temperature call rather than arithmetic done here. Note that the plain
`get_rate_coefficient(T)` interface evaluates k(T, Te=T) and is NOT what this
rule is anchored on; `get_rate_coefficient_two_temp(T, Te)` is.
"""
from rmgpy.kinetics import TwoTemperaturePlasma

k = TwoTemperaturePlasma(A=(3.77e-13, 'cm^3/(molecule*s)'), n=-0.651,
                         Ea_g=(0.0, 'kJ/mol'), Ea_e=(0.0, 'kJ/mol'), T0=(1e4, 'K'),
                         electrons=-1, Tmin=(1e4, 'K'), Tmax=(1e8, 'K'))
print('library entry:', k)
print('A in SI          : %.6e m^3/(mol*s)' % k.A.value_si)
print('Tgas fixed at 300 K throughout (Ea_g = Ea_e = 0, so k does not depend on it)')
print()
for eV in (1.0, 2.0, 3.0):
    Te = eV * 11604.518
    print('Te = %.1f eV = %9.2f K   k(T=300, Te) = %.6e m^3/(mol*s)'
          % (eV, Te, k.get_rate_coefficient_two_temp(300.0, Te)))
print()
print('note Tmin = 1e4 K: 1 eV = 11604.5 K is inside it, 3 eV is well inside;')
print('rmgpy has no production caller for is_temperature_valid, so the bound is')
print('documentation, not enforcement.')
