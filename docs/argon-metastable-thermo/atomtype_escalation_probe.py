#!/usr/bin/env python
# encoding: utf-8
"""
What would an ``Ar0e`` change actually buy? Measured, so the escalation is a measurement
rather than an argument.

``rmgpy/molecule/atomtype.py`` is in this campaign's gated lane, so nothing here edits it.
What this probe does instead is mutate ``ATOMTYPES['Ar0e'].generic`` IN MEMORY, at runtime,
before the families are loaded, and re-measure reachability under each candidate change.
No file in either repository is touched; the mutation lives for the length of the process.

The candidates are the only two narrowings available, because ``Ar0e`` is declared

    generic=['R', 'R!H', 'R!H!Val7', 'Rx', 'Rx!H', 'Ar']

and the family groups that reach this species are written on exactly two of those.

ONE FALSE START, RECORDED BECAUSE IT IS THE POINT. The first version of this probe mutated
``ATOMTYPES['Ar0e'].generic`` and reported that all four candidates behaved identically --
which would have been a finding, and was instead a broken probe. ``AtomType.generic`` is
not what group matching consults: ``is_specific_case_of`` is ``self is other or self in
other.specific`` (``atomtype.py:209-214``), so the edge that matters is the entry for
``Ar0e`` in ``ATOMTYPES['R'].specific``, not the entry for ``R`` in ``Ar0e.generic``. The
constructor keeps both and only one is read. The tell was that every candidate gave the
same number, including the one that should have removed everything; a probe whose arms all
agree has usually not run. This version mutates BOTH directions and asserts the mutation
took effect before measuring anything.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/atomtype_escalation_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/atomtype_escalation_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/atomtype_escalation_probe.stderr.log >&2)
"""

import logging
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))
DATABASE = os.path.join(REPO, 'input')

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
WITNESSES = [
    ('H', 'multiplicity 2\n1 H u1 p0 c0\n'),
    ('N2', '1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}\n'),
    ('C2H5', 'multiplicity 2\n1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n'
             '2 C u1 p0 c0 {1,S} {6,S} {7,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'
             '5 H u0 p0 c0 {1,S}\n6 H u0 p0 c0 {2,S}\n7 H u0 p0 c0 {2,S}\n'),
    ('HCO', 'multiplicity 2\n1 C u1 p0 c0 {2,D} {3,S}\n2 O u0 p2 c0 {1,D}\n'
            '3 H u0 p0 c0 {1,S}\n'),
    ('HCl', '1 Cl u0 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n'),
    ('CH3', 'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
            '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'),
    ('O2', 'multiplicity 3\n1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}\n'),
]

CANDIDATES = [
    ('as shipped', None),
    ("drop 'R!H'", ['R', 'R!H!Val7', 'Rx', 'Rx!H', 'Ar']),
    ("drop 'R'", ['R!H', 'R!H!Val7', 'Rx', 'Rx!H', 'Ar']),
    ("drop both", ['R!H!Val7', 'Rx', 'Rx!H', 'Ar']),
]

SCRIPT = r'''
import json, logging, os, sys
from rmgpy import settings
settings['database.directory'] = %(db)r
logging.getLogger().setLevel(logging.CRITICAL)
from rmgpy.molecule.atomtype import ATOMTYPES
ar0e = ATOMTYPES['Ar0e']
generic = %(generic)r
if generic is not None:
    dropped = [g for g in ['R', 'R!H', 'R!H!Val7', 'Rx', 'Rx!H', 'Ar'] if g not in generic]
    for g in dropped:
        # BOTH directions. `generic` is bookkeeping; `specific` is what
        # is_specific_case_of reads (atomtype.py:209-214), and mutating only the
        # first is a no-op that looks like a measurement.
        ATOMTYPES[g].specific = [t for t in ATOMTYPES[g].specific if t is not ar0e]
    ar0e.generic = [ATOMTYPES[g] for g in generic]
    # the mutation must have taken effect, or everything below measures nothing
    for g in dropped:
        assert not ar0e.is_specific_case_of(ATOMTYPES[g]), \
            'mutation did not take: Ar0e is still a specific case of %%s' %% g
    for g in generic:
        assert ar0e.is_specific_case_of(ATOMTYPES[g]), g
else:
    assert ar0e.is_specific_case_of(ATOMTYPES['R'])
    assert ar0e.is_specific_case_of(ATOMTYPES['R!H'])
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule import Molecule
from rmgpy.species import Species
kdb = KineticsDatabase()
kdb.load_families(os.path.join(%(db)r, 'kinetics', 'families'), families='all',
                  depositories=['training'])
# lift the five containments so this measures the ATOM TYPE, not the forbidden groups
for fam in ['Birad_R_Recombination', 'R_Addition_MultipleBond', 'Disproportionation',
            'CO_Disproportionation', 'Cl_Abstraction']:
    f = kdb.families[fam]
    if f.forbidden and 'Ar_metastable_biradical' in f.forbidden.entries:
        f.forbidden.entries.pop('Ar_metastable_biradical')
meta = Species(label='m', molecule=[Molecule().from_adjacency_list(%(meta)r)])
hits = {}
for label, adj in %(witnesses)r:
    spc = Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])
    for rxn in kdb.generate_reactions_from_families([meta, spc], products=None,
                                                    resonance=True):
        hits.setdefault(rxn.family, []).append(label)
for rxn in kdb.generate_reactions_from_families([meta], products=None, resonance=True):
    hits.setdefault(rxn.family, []).append('(unimolecular)')
# a control: ordinary radical chemistry must not move
ch3 = Species(label='CH3', molecule=[Molecule().from_adjacency_list(
    'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
    '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n')])
h = Species(label='H', molecule=[Molecule().from_adjacency_list(
    'multiplicity 2\n1 H u1 p0 c0\n')])
control = sorted({r.family for r in kdb.generate_reactions_from_families(
    [ch3, h], products=None, resonance=True)})
# and: does ground-state argon or Ar+ move?
arp = Species(label='Arp', molecule=[Molecule().from_adjacency_list(
    'multiplicity 2\n1 Ar u1 p3 c+1\n')])
arp_hits = sorted({r.family for r in kdb.generate_reactions_from_families(
    [arp], products=None, resonance=True)})
print('RESULT' + json.dumps({'hits': {k: sorted(set(v)) for k, v in hits.items()},
                             'control': control, 'arp': arp_hits}))
'''


def banner(text):
    print("\n" + text)
    print("=" * len(text))


logging.getLogger().setLevel(logging.CRITICAL)

banner("WHAT THE GROUPS ACTUALLY SAY")
print("  Plasma_Electron_Impact_Ionization  A_rad             1 *1 R    u[1,2,3,4] px c[...]")
print("  Disproportionation                 Root, atom *1     1 *1 R    u[1,2,3,4]")
print("  CO_Disproportionation              Root, atom *1     1 *1 R    u[1,2,3,4]")
print("  Cl_Abstraction                     Root, atom *3     1 *3 R    u[1,2,3,4]")
print("  Birad_R_Recombination              Birad             1 *2 R!H  u2")
print("  R_Addition_MultipleBond            Y_1centerbirad    1 *3 R!H  u2")
print()
print("  Note the first four: the family this species is SUPPOSED to react in and three of")
print("  the five it must not are written on the SAME generic with the SAME u range.")

env = dict(os.environ)
env['PYTHONPATH'] = '/home/alon/Code/RMG-Py-plasma'
env.setdefault('MPLCONFIGDIR', os.environ.get('TMPDIR', '/tmp'))

table = []
for name, generic in CANDIDATES:
    banner("CANDIDATE: %s   (generic = %s)" % (name, generic or 'unchanged'))
    code = SCRIPT % dict(db=DATABASE, generic=generic, meta=AR_META, witnesses=WITNESSES)
    proc = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True,
                          env=env, cwd=REPO)
    line = [ln for ln in proc.stdout.splitlines() if ln.startswith('RESULT')]
    if not line:
        print("  FAILED: %s" % proc.stderr[-800:])
        continue
    import json
    data = json.loads(line[0][len('RESULT'):])
    hits = data['hits']
    ordinary = sorted(set(hits) - {'Plasma_Electron_Impact_Ionization'})
    eii = 'Plasma_Electron_Impact_Ionization' in hits
    print("  ordinary families reaching Ar(3P2) : %d  %s" % (len(ordinary), ordinary))
    print("  intended ionisation channel        : %s" % ('SURVIVES' if eii else 'LOST'))
    print("  control CH3 + H                    : %s" % data['control'])
    print("  Ar+ unimolecular                   : %s" % data['arp'])
    table.append((name, len(ordinary), ordinary, eii, data['control']))

banner("SUMMARY -- WHAT AN Ar0e NARROWING WOULD BUY")
print("  %-14s %-9s %-10s %s" % ('candidate', 'ordinary', 'EII', 'families left'))
for name, n, ordinary, eii, _control in table:
    print("  %-14s %-9d %-10s %s" % (name, n, 'kept' if eii else 'LOST', ordinary))
sys.stdout.flush()
