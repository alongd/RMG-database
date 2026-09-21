#!/usr/bin/env python
# encoding: utf-8
"""
Can the reachability be CLOSED from the database side, rather than only documented?

The review offered three endings and listed "make the claim true" first. This probe tests
whether the mechanism to do it already exists.

It does, and it is not the quarantine. ``KineticsFamily.__generate_product_structures``
calls ``is_molecule_forbidden`` on the REACTANT structures (``family.py:1669``) and again on
the PRODUCT structures (``:1690``), both during reaction generation -- upstream of species
creation, of thermo, and of the kinetics gate. And ``Birad_R_Recombination`` already uses it:
its groups file carries four ``forbidden(...)`` entries whose own longDesc says

    "This family is intended to handle [O] u2 p2, or [S] u2 p2, or [NH] u2 p1,
     instances with a different number of lone pairs are forbidden"

``Ar u2 p3`` is exactly such an instance. So the question this probe answers is not "can we
suppress the red test" but "does the family already declare a scope that excludes metastable
argon, and does stating that in the mechanism the family already uses actually stop it".

The experiment writes one ``forbidden`` entry into each of the five ordinary families that
reach the species, re-measures, and then RESTORES every file and verifies the restore with
``git diff``. It changes nothing permanently; whether to keep the entries is a separate
decision, taken with this measurement in hand.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/forbidden_group_experiment.py \
        > >(tee -a docs/argon-metastable-thermo/logs/forbidden_group_experiment.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/forbidden_group_experiment.stderr.log >&2)
"""

import logging
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))
DATABASE = os.path.join(REPO, 'input')

FAMILIES = ['Birad_R_Recombination', 'R_Addition_MultipleBond', 'Disproportionation',
            'CO_Disproportionation', 'Cl_Abstraction']

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
    ('C6H5', 'multiplicity 2\n1 C u1 p0 c0 {2,B} {6,B}\n2 C u0 p0 c0 {1,B} {3,B} {7,S}\n'
             '3 C u0 p0 c0 {2,B} {4,B} {8,S}\n4 C u0 p0 c0 {3,B} {5,B} {9,S}\n'
             '5 C u0 p0 c0 {4,B} {6,B} {10,S}\n6 C u0 p0 c0 {1,B} {5,B} {11,S}\n'
             '7 H u0 p0 c0 {2,S}\n8 H u0 p0 c0 {3,S}\n9 H u0 p0 c0 {4,S}\n'
             '10 H u0 p0 c0 {5,S}\n11 H u0 p0 c0 {6,S}\n'),
]

FORBIDDEN_BLOCK = '''

forbidden(
    label = "Ar_metastable_biradical",
    group =
"""
1 Ar u2 p3 c0
""",
    shortDesc = u"""Metastable argon is outside this family's scope and its products have no atom type""",
    longDesc =
u"""
EXPERIMENT ONLY -- written by docs/argon-metastable-thermo/forbidden_group_experiment.py
and removed again by it. Not a shipped change.
""",
)
'''


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def groups_path(family):
    return os.path.join(DATABASE, 'kinetics', 'families', family, 'groups.py')


def git_dirty():
    out = subprocess.run(['git', '-C', REPO, 'diff', '--name-only'],
                         capture_output=True, text=True, check=True)
    return [p for p in out.stdout.split() if p]


def measure(tag):
    """Reload the database from scratch and report what reaches the metastable."""
    from rmgpy.data.kinetics.database import KineticsDatabase
    from rmgpy.molecule import Molecule
    from rmgpy.species import Species

    kdb = KineticsDatabase()
    kdb.load_families(os.path.join(DATABASE, 'kinetics', 'families'),
                      families='all', depositories=['training'])
    meta = Species(label='Ar(3P2)',
                   molecule=[Molecule().from_adjacency_list(AR_META)])
    hits = {}
    for label, adj in WITNESSES:
        spc = Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])
        for rxn in kdb.generate_reactions_from_families([meta, spc], products=None,
                                                        resonance=True):
            hits.setdefault(rxn.family, set()).add(label)
    uni = kdb.generate_reactions_from_families([meta], products=None, resonance=True)
    for rxn in uni:
        hits.setdefault(rxn.family, set()).add('(unimolecular)')

    print("\n  [%s] families loaded: %d" % (tag, len(kdb.families)))
    for fam, labels in sorted(hits.items()):
        print("      %-34s via %s" % (fam, sorted(labels)))
    ordinary = sorted(set(hits) - {'Plasma_Electron_Impact_Ionization'})
    print("      ordinary families still reaching Ar(3P2): %d %s"
          % (len(ordinary), ordinary))
    print("      the intended ionisation channel survives: %s"
          % ('Plasma_Electron_Impact_Ionization' in hits))

    # ... and does ordinary chemistry still work? a control that must not move.
    ch3 = Species(label='CH3', molecule=[Molecule().from_adjacency_list(
        'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
        '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n')])
    h = Species(label='H', molecule=[Molecule().from_adjacency_list(
        'multiplicity 2\n1 H u1 p0 c0\n')])
    o = Species(label='O', molecule=[Molecule().from_adjacency_list(
        'multiplicity 3\n1 O u2 p2 c0\n')])
    controls = {}
    for name, pair in (('CH3+H', [ch3, h]), ('O+CH3', [o, ch3])):
        rxns = kdb.generate_reactions_from_families(pair, products=None, resonance=True)
        controls[name] = sorted({r.family for r in rxns})
        print("      CONTROL %-7s -> %d reactions, families %s"
              % (name, len(rxns), controls[name]))
    return ordinary, controls


logging.getLogger().setLevel(logging.CRITICAL)

banner("0. CLEAN TREE?")
dirty = git_dirty()
print("  tracked files already modified before the experiment: %d" % len(dirty))
for path in dirty:
    print("      %s" % path)
targets = {groups_path(f) for f in FAMILIES}
clash = [p for p in dirty if os.path.join(REPO, p) in targets]
assert not clash, 'refusing to run: %s already modified' % clash

banner("1. BEFORE")
before_ordinary, before_controls = measure('before')

banner("2. WRITE ONE forbidden() ENTRY PER FAMILY")
backups = {}
try:
    for family in FAMILIES:
        path = groups_path(family)
        fd, tmp = tempfile.mkstemp(prefix='groups-backup-')
        os.close(fd)
        shutil.copy2(path, tmp)
        backups[path] = tmp
        with open(path, 'a', encoding='utf-8') as handle:
            handle.write(FORBIDDEN_BLOCK)
        print("  appended to %s" % os.path.relpath(path, REPO))

    banner("3. AFTER")
    after_ordinary, after_controls = measure('after')
finally:
    banner("4. RESTORE, AND VERIFY THE RESTORE")
    for path, tmp in backups.items():
        shutil.copy2(tmp, path)
        os.unlink(tmp)
    still_dirty = git_dirty()
    new_dirt = [p for p in still_dirty if os.path.join(REPO, p) in targets]
    print("  family groups.py files still showing a diff: %d %s"
          % (len(new_dirt), new_dirt))
    assert not new_dirt, 'RESTORE FAILED -- do not trust the comparison above'
    print("  restore verified by git diff (not by assumption)")

banner("5. VERDICT")
print("  ordinary families reaching Ar(3P2) before : %d %s"
      % (len(before_ordinary), before_ordinary))
print("  ordinary families reaching Ar(3P2) after  : %d %s"
      % (len(after_ordinary), after_ordinary))
print("  controls unchanged                        : %s"
      % (before_controls == after_controls))
for name in sorted(before_controls):
    if before_controls[name] != after_controls[name]:
        print("      CONTROL MOVED %s: %s -> %s"
              % (name, before_controls[name], after_controls[name]))
sys.stdout.flush()
