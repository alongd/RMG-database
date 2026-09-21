#!/usr/bin/env python
# encoding: utf-8
"""
Which families reach metastable argon -- the question round 55 asked of SIX families and
this probe asks of ALL of them.

``reachability_probe.py`` loaded the six plasma families and reported that exactly one of
them generates anything from ``Ar u2 p3 c0``. That measurement is correct and is not in
dispute. What it cannot support is the sentence the library then wrote, "exactly one family
reaches it", because the denominator was six and this database ships 142. A measurement over
a hand-picked subset is a measurement of the subset.

So: load every family, react Ar(3P2) unimolecularly and against a spread of ordinary
combustion partners, and report

    families loaded / families that matched / reactions generated / products failing thermo

The last column is the one that decides how bad this is. A family that matches and then
raises ``AtomTypeError`` during thermo generation TERMINATES a mechanism-generation job. A
family that matches and gets a NUMBER is worse, because it reaches a published mechanism
silently. Both are counted separately and neither is assumed.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/all_family_reachability_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/all_family_reachability_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/all_family_reachability_probe.stderr.log >&2)
"""

import os
import sys
import traceback

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402
from rmgpy.data.thermo import ThermoDatabase               # noqa: E402
from rmgpy.molecule import Molecule                        # noqa: E402
from rmgpy.species import Species                          # noqa: E402

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'

#: Ordinary combustion partners. These are not exotic: every one of them is a bath-gas or
#: radical-pool member that an argon-diluted deck has in its core model on the first
#: iteration. The point is precisely that they are ordinary.
PARTNERS = [
    ('H',      'multiplicity 2\n1 H u1 p0 c0\n'),
    ('OH',     'multiplicity 2\n1 O u1 p2 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n'),
    ('CH3',    'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
               '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'),
    ('O2',     'multiplicity 3\n1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}\n'),
    ('N2',     '1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}\n'),
    ('H2',     '1 H u0 p0 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n'),
    ('O',      'multiplicity 3\n1 O u2 p2 c0\n'),
    ('N',      'multiplicity 4\n1 N u3 p1 c0\n'),
    ('CH4',    '1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n2 H u0 p0 c0 {1,S}\n'
               '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n5 H u0 p0 c0 {1,S}\n'),
    ('H2O',    '1 O u0 p2 c0 {2,S} {3,S}\n2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n'),
    ('CO',     '1 C u0 p1 c-1 {2,T}\n2 O u0 p1 c+1 {1,T}\n'),
    ('HO2',    'multiplicity 2\n1 O u0 p2 c0 {2,S} {3,S}\n2 O u1 p2 c0 {1,S}\n'
               '3 H u0 p0 c0 {1,S}\n'),
    ('C2H4',   '1 C u0 p0 c0 {2,D} {3,S} {4,S}\n2 C u0 p0 c0 {1,D} {5,S} {6,S}\n'
               '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n5 H u0 p0 c0 {2,S}\n'
               '6 H u0 p0 c0 {2,S}\n'),
    ('Ar',     '1 Ar u0 p4 c0\n'),
    ('Ar(3P2)', AR_META),
]


def species(adj, label):
    return Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def adj1(spc):
    return spc.molecule[0].to_adjacency_list().strip().replace('\n', ' | ')


banner("0. DENOMINATOR")
family_dir = os.path.join(DATABASE, 'kinetics', 'families')
on_disk = sorted(d for d in os.listdir(family_dir)
                 if os.path.isdir(os.path.join(family_dir, d)))
print("  family directories on disk: %d" % len(on_disk))

kdb = KineticsDatabase()
kdb.load_families(family_dir, families='all', depositories=['training'])
loaded = sorted(kdb.families)
print("  families LOADED by load_families(families='all'): %d" % len(loaded))
missing = sorted(set(on_disk) - set(loaded))
if missing:
    print("  on disk but NOT loaded (%d): %s" % (len(missing), missing))

banner("1. UNIMOLECULAR: generate_reactions_from_families([Ar(3P2)])")
meta = species(AR_META, 'Ar(3P2)')
uni = kdb.generate_reactions_from_families([meta], products=None, resonance=True)
print("  reactions: %d" % len(uni))
for rxn in uni:
    print("    %-46s %s" % (rxn.family, rxn))

banner("2. BIMOLECULAR: generate_reactions_from_families([Ar(3P2), X]) for ordinary X")
hits = {}          # family -> list of (partner, rxn)
for label, adj in PARTNERS:
    partner = species(adj, label)
    try:
        rxns = kdb.generate_reactions_from_families(
            [meta, partner], products=None, resonance=True)
    except Exception as exc:                                        # noqa: BLE001
        print("\n  partner %-9s GENERATION RAISED %s: %s" % (label, type(exc).__name__, exc))
        traceback.print_exc()
        continue
    print("\n  partner %-9s -> %d reaction(s)" % (label, len(rxns)))
    for rxn in rxns:
        hits.setdefault(rxn.family, []).append((label, rxn))
        print("      %-40s %s" % (rxn.family, rxn))
        print("          products: %s" % [adj1(s) for s in rxn.products])

banner("3. REACH FIGURE")
matched = sorted(set(list(hits) + [r.family for r in uni]))
print("  families loaded                : %d" % len(loaded))
print("  families that MATCHED Ar(3P2)  : %d  %s" % (len(matched), matched))
print("  reactions generated            : %d"
      % (len(uni) + sum(len(v) for v in hits.values())))

banner("4. DOES THERMO SURVIVE THE PRODUCTS? (crash vs silent number)")
tdb = ThermoDatabase()
tdb.load(os.path.join(DATABASE, 'thermo'))
print("  thermo libraries loaded: %d" % len(tdb.libraries))

crashed = []
numbered = []
seen = set()
all_pairs = [(r.family, '-', r) for r in uni]
for family, pairs in sorted(hits.items()):
    all_pairs.extend((family, label, rxn) for label, rxn in pairs)
for family, label, rxn in all_pairs:
    for prod in rxn.products:
        key = adj1(prod)
        if key in seen:
            continue
        seen.add(key)
        fresh = Species(molecule=[prod.molecule[0].copy(deep=True)])
        try:
            data = tdb.get_thermo_data(fresh)
        except Exception as exc:                                    # noqa: BLE001
            crashed.append((family, label, key, type(exc).__name__, str(exc)[:160]))
            print("\n  CRASH  %-40s %-9s %s" % (family, label, key))
            print("         %s: %s" % (type(exc).__name__, str(exc)[:200]))
        else:
            numbered.append((family, label, key, data))
            print("\n  NUMBER %-40s %-9s %s" % (family, label, key))
            print("         H298 = %.4f kJ/mol   S298 = %.4f J/(mol*K)   source = %s"
                  % (data.get_enthalpy(298.15) / 1000.0,
                     data.get_entropy(298.15),
                     (data.comment or '').strip().replace('\n', ' / ')[:140]))

banner("5. SUMMARY")
print("  families loaded                          : %d" % len(loaded))
print("  families matching Ar(3P2)                : %d" % len(matched))
print("  distinct products examined               : %d" % len(seen))
print("  products whose thermo CRASHED            : %d" % len(crashed))
print("  products that got a NUMBER               : %d" % len(numbered))
for row in numbered:
    print("      NUMBER: %s via %s + %s" % (row[2], row[0], row[1]))
for row in crashed:
    print("      CRASH : %s via %s + %s  (%s)" % (row[2], row[0], row[1], row[3]))

sys.stdout.flush()
