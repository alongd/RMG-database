#!/usr/bin/env python
# encoding: utf-8
"""
Load probe for I-221: does ``Ar u2 p3 c0`` perceive, and where does its thermochemistry
come from?

Run twice -- once before the new library exists (the BASELINE, which is what a reader of
this database gets today) and once after -- so "the entry is matched" is a measurement
rather than an assertion:

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/load_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/load_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/load_probe.stderr.log >&2)
"""

import os
import sys
import traceback

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
THIS_DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = THIS_DATABASE

from rmgpy.data.thermo import ThermoDatabase          # noqa: E402
from rmgpy.molecule import Molecule                    # noqa: E402
from rmgpy.molecule.atomtype import ATOMTYPES          # noqa: E402
from rmgpy.species import Species                      # noqa: E402

LIBRARY_DIR = os.path.join(THIS_DATABASE, 'thermo', 'libraries')
GROUP_DIR = os.path.join(THIS_DATABASE, 'thermo', 'groups')

T0 = 298.15
NEW_LIBRARY = 'PlasmaExcitedNeutralThermo'

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'


def banner(text):
    print("\n" + text)
    print("-" * len(text))


def species(adjacency_list, label=''):
    return Species(label=label,
                   molecule=[Molecule().from_adjacency_list(adjacency_list)])


print("database.directory = %s" % settings['database.directory'])
print("rmgpy from          = %s" % os.path.dirname(sys.modules['rmgpy'].__file__))

banner("1. PERCEPTION -- what atom type does each argon adjacency list take?")
for label, adj in (("ground state", AR), ("metastable", AR_META), ("cation", ARP)):
    m = Molecule().from_adjacency_list(adj)
    a = m.atoms[0]
    print("  %-13s %-24s -> atomtype %-6s  u%d p%d c%+d  multiplicity %d  net charge %+d"
          % (label, adj.strip().splitlines()[-1], a.atomtype.label, a.radical_electrons,
             a.lone_pairs, a.charge, m.multiplicity, m.get_net_charge()))
print("  ATOMTYPES['Ar'].specific = %s" % ATOMTYPES['Ar'].specific)
print("  ATOMTYPES['Ar0e'].generic = %s" % ATOMTYPES['Ar0e'].generic)

banner("2. THE METASTABLE IS A DISTINCT SPECIES FROM BOTH OF THE OTHER TWO")
meta = Molecule().from_adjacency_list(AR_META)
for label, adj in (("ground state", AR), ("cation", ARP)):
    other = Molecule().from_adjacency_list(adj)
    print("  isomorphic to %-13s : %s" % (label, meta.is_isomorphic(other)))

banner("3. LIBRARIES ON DISK")
on_disk = sorted(f[:-3] for f in os.listdir(LIBRARY_DIR) if f.endswith('.py'))
print("  %d library files; %s is %s"
      % (len(on_disk), NEW_LIBRARY, "PRESENT" if NEW_LIBRARY in on_disk else "ABSENT"))

db = ThermoDatabase()
db.load_libraries(LIBRARY_DIR)
db.load_groups(GROUP_DIR)
print("  %d libraries loaded" % len(db.libraries))
if NEW_LIBRARY in db.libraries:
    print("  %s entries: %s" % (NEW_LIBRARY, list(db.libraries[NEW_LIBRARY].entries)))

banner("4. THERMOCHEMISTRY THROUGH THE FULL DATABASE (libraries + group additivity)")
for label, adj in (("Ar (ground)", AR), ("Ar* metastable", AR_META), ("Ar+ cation", ARP)):
    try:
        data = db.get_thermo_data(species(adj, label))
    except Exception as exc:                                  # noqa: BLE001
        print("  %-15s RAISED %s: %s" % (label, type(exc).__name__, exc))
        traceback.print_exc()
        continue
    print("  %-15s H298 = %12.3f kJ/mol   S298 = %10.3f J/(mol*K)   Cp(298) = %8.3f"
          % (label, data.get_enthalpy(T0) / 1000.0, data.get_entropy(T0),
             data.get_heat_capacity(T0)))
    print("  %-15s Cp(1000) = %8.3f   Cp(6000) = %8.3f" % ("",
          data.get_heat_capacity(1000.0), data.get_heat_capacity(6000.0)))
    print("  %-15s source: %s" % ("", (data.comment or "<no comment>").strip()))

banner("5. WITH EVERY LIBRARY UNLOADED -- what the ESTIMATOR alone would answer")
bare = ThermoDatabase()
bare.load_libraries(LIBRARY_DIR)
bare.unload_libraries()
bare.load_groups(GROUP_DIR)
assert not bare.libraries
for label, adj in (("Ar* metastable", AR_META),):
    try:
        data = bare.get_thermo_data(species(adj, label))
    except Exception as exc:                                  # noqa: BLE001
        print("  %-15s REFUSED by the estimator: %s: %s"
              % (label, type(exc).__name__, str(exc).strip().splitlines()[0]))
    else:
        print("  %-15s ESTIMATOR ANSWERED H298 = %.3f kJ/mol  S298 = %.3f  -- comment: %s"
              % (label, data.get_enthalpy(T0) / 1000.0, data.get_entropy(T0),
                 (data.comment or "<none>").strip()))

banner("6. REFERENCE STATES AS THIS DATABASE HOLDS THEM")
ar_entry = db.libraries['primaryThermoLibrary'].entries['Ar']
print("  primaryThermoLibrary['Ar'] is a %s" % type(ar_entry.data).__name__)
print("    S298 straight off the entry     = %.3f J/(mol*K)" % ar_entry.data.get_entropy(T0))
print("    H298 straight off the entry     = %.3f kJ/mol"
      % (ar_entry.data.get_enthalpy(T0) / 1000.0))
print("    Cp298 straight off the entry    = %.3f J/(mol*K)"
      % ar_entry.data.get_heat_capacity(T0))
print("    NIST-JANAF Ar-001 S298          = 154.845 J/(mol*K)   <- what the entry cites")
print("    gap (JANAF - in-database entry) = %.3f J/(mol*K)"
      % (154.845 - ar_entry.data.get_entropy(T0)))
