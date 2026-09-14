#!/usr/bin/env python
# encoding: utf-8
"""
Which library wins the ground-state argon lookup, and what decides it.

An entry whose ``S298`` is constructed as "ground state plus R ln g" is only as good as the
ground state the RUNTIME resolves. This probe measures what decides that, because the answer
is not "the best source" and is not curated at all on the load-everything path.
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

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'

db = ThermoDatabase()
db.load_libraries(LIB)


def banner(text):
    print("\n" + text)
    print("-" * len(text))


banner("1. EVERY LIBRARY THAT CARRIES GROUND-STATE ARGON, IN LOAD ORDER")
ground = Molecule().from_adjacency_list(AR)
meta = Molecule().from_adjacency_list(AR_META)
carriers, meta_carriers = [], []
for position, name in enumerate(db.library_order):
    for label, e in db.libraries[name].entries.items():
        if e.item is None or not hasattr(e.item, 'is_isomorphic'):
            continue
        try:
            if e.item.is_isomorphic(ground):
                carriers.append((position, name, label, e.data.get_entropy(T0)))
            elif e.item.is_isomorphic(meta):
                meta_carriers.append((position, name, label, e.data.get_entropy(T0)))
        except Exception:                                    # noqa: BLE001
            pass

print("%5s  %-30s %-10s %12s %10s"
      % ("order", "library", "label", "S298 (API)", "vs JANAF"))
for position, name, label, s in carriers:
    print("%5d  %-30s %-10s %12.4f %+10.4f"
          % (position, name, label, s, s - 154.845))
print("\n  -> the FIRST of these in load order wins; get_thermo_data_from_libraries")
print("     returns on the first match (rmgpy/data/thermo.py:1923-1927).")

print("\n  and for the metastable, for contrast:")
for position, name, label, s in meta_carriers:
    print("%5d  %-30s %-10s %12.4f" % (position, name, label, s))
print("  -> exactly one carrier, so this entry cannot be shadowed. That is uniqueness,")
print("     not precedence: it would be shadowed too if a second library ever carried it.")

banner("2. WHAT SETS load_library ORDER WHEN NOTHING IS DECLARED")
on_disk_walk = []
for root, _dirs, files in os.walk(LIB):
    for f in files:
        if f.endswith('.py'):
            on_disk_walk.append(f[:-3])
print("  db.library_order == os.walk order : %s" % (db.library_order == on_disk_walk))
print("  db.library_order == sorted order  : %s" % (db.library_order == sorted(on_disk_walk)))
print("  first 8 in load order: %s" % db.library_order[:8])
print("\n  load_libraries(path) with libraries=None appends in os.walk order")
print("  (rmgpy/data/thermo.py:944-954) -- i.e. filesystem order, uncurated and")
print("  machine-dependent. A deck that declares thermoLibraries gets THAT list instead,")
print("  so precedence is curated in a real run and arbitrary everywhere else:")
print("  databaseTest.py, these probes, and any script calling load_libraries(path).")

banner("3. THE CONSEQUENCE FOR AN 'ANCHORED' ENTRY")
winner = carriers[0]
print("  Ar(3P2) S298 was built as  JANAF Ar-001 154.8450 + R ln 5 = 168.2266")
print("  the runtime's ground state is %s at %.4f J/(mol*K)" % (winner[1], winner[3]))
print("  so the resolved excitation entropy is high by %+.4f J/(mol*K)"
      % (154.845 - winner[3]))
print("\n  had a different carrier won, the same anchoring would be off by:")
for _position, name, _label, s in carriers:
    print("    %-30s %+.4f J/(mol*K)" % (name, 154.845 - s))
