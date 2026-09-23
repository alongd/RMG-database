#!/usr/bin/env python
# encoding: utf-8
"""
What a running mechanism actually sees, as opposed to what the entries say.

``get_thermo_data`` does not hand back a library's ``ThermoData`` untouched -- values pass
through a Wilhoit/NASA round trip. This probe measures the size of that artefact for the three
argon species and for the ground-state entries the new metastable entry is anchored on, so the
``longDesc``'s disclosure carries measured numbers rather than the entries' face values.
"""

import os

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
settings['database.directory'] = os.path.abspath(
    os.path.join(HERE, os.pardir, os.pardir, 'input'))

from rmgpy.data.thermo import ThermoDatabase          # noqa: E402
from rmgpy.molecule import Molecule                    # noqa: E402
from rmgpy.species import Species                      # noqa: E402

T0 = 298.15
LIB = os.path.join(settings['database.directory'], 'thermo', 'libraries')
GRP = os.path.join(settings['database.directory'], 'thermo', 'groups')

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'

db = ThermoDatabase()
db.load_libraries(LIB)
db.load_groups(GRP)


def resolved(adj, label):
    return db.get_thermo_data(Species(label=label,
                                      molecule=[Molecule().from_adjacency_list(adj)]))


print("\nENTRY FACE VALUES (what is written in the files)")
print("-" * 48)
face = {}
for lib, key in (('PlasmaExcitedNeutralThermo', 'Ar(3P2)'),
                 ('BurkeH2O2', 'Ar'),
                 ('primaryThermoLibrary', 'Ar')):
    d = db.libraries[lib].entries[key].data
    face[(lib, key)] = (d.get_enthalpy(T0) / 1000.0, d.get_entropy(T0))
    print("  %-28s %-9s H298 = %11.4f kJ/mol   S298 = %10.4f J/(mol*K)"
          % (lib, key, face[(lib, key)][0], face[(lib, key)][1]))

print("\nWHAT get_thermo_data RESOLVES TO (what a mechanism sees)")
print("-" * 56)
res = {}
for label, adj in (('Ar', AR), ('Ar(3P2)', AR_META)):
    d = resolved(adj, label)
    res[label] = (d.get_enthalpy(T0) / 1000.0, d.get_entropy(T0))
    print("  %-9s H298 = %11.4f kJ/mol   S298 = %10.4f J/(mol*K)   <- %s"
          % (label, res[label][0], res[label][1], (d.comment or '').strip()))

print("\nTHE ROUND-TRIP ARTEFACT, ENTRY -> RESOLVED")
print("-" * 42)
print("  Ar (BurkeH2O2 wins)   dS = %+.4f J/(mol*K)"
      % (res['Ar'][1] - face[('BurkeH2O2', 'Ar')][1]))
print("  Ar(3P2)               dS = %+.4f J/(mol*K)"
      % (res['Ar(3P2)'][1] - face[('PlasmaExcitedNeutralThermo', 'Ar(3P2)')][1]))
print("  Ar(3P2)               dH = %+.4f kJ/mol"
      % (res['Ar(3P2)'][0] - face[('PlasmaExcitedNeutralThermo', 'Ar(3P2)')][0]))

print("\nTHE EXCITATION STEP AS A MECHANISM WOULD COMPUTE IT:  Ar -> Ar(3P2)")
print("-" * 68)
print("  dH298 resolved  = %10.4f kJ/mol      exact (level energy) = 1114.2468"
      % (res['Ar(3P2)'][0] - res['Ar'][0]))
print("  dS298 resolved  = %10.4f J/(mol*K)   exact (R ln 5)       =   13.3816"
      % (res['Ar(3P2)'][1] - res['Ar'][1]))
print("  dS error        = %+10.4f J/(mol*K)  -> %+.4f kJ/mol in dG at 298.15 K"
      % (res['Ar(3P2)'][1] - res['Ar'][1] - 13.38161,
         -T0 * (res['Ar(3P2)'][1] - res['Ar'][1] - 13.38161) / 1000.0))
print("  (JANAF Ar-001 S298 = 154.845; primaryThermoLibrary's NASA Ar = %.4f;"
      % face[('primaryThermoLibrary', 'Ar')][1])
print("   BurkeH2O2's Ar, which is the one that WINS the lookup   = %.4f)"
      % face[('BurkeH2O2', 'Ar')][1])
