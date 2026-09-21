#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 3 -- the database's own species inventory, against the old root
and against the candidate new root.

Denominator: every species entry in every thermo library in this database.
That is the widest species inventory the database itself states.

For each species the probe records
  * net charge,
  * whether the OLD root `R u0 px c[0,+1..+8]` matches it,
  * whether the CANDIDATE root `R u0 px c[+1..+8]` matches it,
  * for every matched centre, what the family recipe
    (GAIN_RADICAL *1 1; LOSE_CHARGE *1 1) actually builds there -- a typed
    molecule, or an AtomTypeError.

Negative control is built in: the two roots differ only by `c0`, so a bug that
made every match succeed or every match fail would show identical columns, and
the `c0` row would not separate.
"""
import os
import sys
import traceback
from collections import Counter, defaultdict

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))

from rmgpy.data.thermo import ThermoDatabase
from rmgpy.molecule import Molecule, Group
from rmgpy.data.kinetics.family import ReactionRecipe

OLD_ROOT = '1 *1 R u0 px c[0,+1,+2,+3,+4,+5,+6,+7,+8]'
NEW_ROOT = '1 *1 R u0 px c[+1,+2,+3,+4,+5,+6,+7,+8]'
RECIPE = ReactionRecipe([['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]])

old_g = Group().from_adjacency_list(OLD_ROOT)
new_g = Group().from_adjacency_list(NEW_ROOT)

tdb = ThermoDatabase()
lib_dir = os.path.join(DB, 'thermo', 'libraries')
names = sorted(f[:-3] for f in os.listdir(lib_dir) if f.endswith('.py'))
tdb.load_libraries(lib_dir, libraries=names)
print('thermo libraries loaded: {0}'.format(len(tdb.libraries)))

seen = {}
for libname, lib in tdb.libraries.items():
    for entry in lib.entries.values():
        item = entry.item
        if not isinstance(item, Molecule):
            continue
        try:
            key = item.to_adjacency_list(remove_h=False)
        except Exception:
            continue
        if key not in seen:
            seen[key] = (libname, entry.label, item)
print('distinct species (by adjacency list): {0}'.format(len(seen)))

charge_hist = Counter()
old_match = []
new_match = []
matched_centre_outcome = Counter()
crash_examples = defaultdict(list)
excluded_charged_by_u0 = []   # net-charge>0 species with NO u0 centre at all

for key, (libname, label, mol) in seen.items():
    try:
        q = mol.get_net_charge()
    except Exception:
        continue
    charge_hist[q] += 1
    try:
        m_old = mol.is_subgraph_isomorphic(old_g)
        m_new = mol.is_subgraph_isomorphic(new_g)
    except Exception:
        continue
    if m_old:
        old_match.append((libname, label, q))
    if m_new:
        new_match.append((libname, label, q))
    if q > 0 and not m_new:
        excluded_charged_by_u0.append((libname, label, q))

    # what does the recipe build at each matched centre?
    if m_old:
        for i, atom in enumerate(mol.atoms):
            if atom.radical_electrons != 0:
                continue
            if atom.charge < 0 or atom.charge > 8:
                continue
            clone = mol.copy(deep=True)
            clone.atoms[i].label = '*1'
            try:
                RECIPE.apply_forward(clone, unique=True)
                clone.update(sort_atoms=False)
                matched_centre_outcome['TYPED q={0}'.format(atom.charge)] += 1
            except Exception as exc:
                tag = '{0} q={1}'.format(type(exc).__name__, atom.charge)
                matched_centre_outcome[tag] += 1
                if len(crash_examples[tag]) < 3:
                    crash_examples[tag].append('{0}/{1}'.format(libname, label))

print('\n=== net-charge histogram over the whole inventory ===')
for q in sorted(charge_hist):
    print('  q = {0:+d} : {1}'.format(q, charge_hist[q]))
total = sum(charge_hist.values())
charged = sum(v for k, v in charge_hist.items() if k != 0)
cations = sum(v for k, v in charge_hist.items() if k > 0)
print('  total {0} | charged {1} | cations {2}'.format(total, charged, cations))

print('\n=== match sets ===')
print('  OLD root `{0}` matches {1} of {2}'.format(OLD_ROOT, len(old_match), total))
print('     of which q=0  : {0}'.format(sum(1 for _, _, q in old_match if q == 0)))
print('     of which q>0  : {0}'.format(sum(1 for _, _, q in old_match if q > 0)))
print('     of which q<0  : {0}'.format(sum(1 for _, _, q in old_match if q < 0)))
print('  NEW root `{0}` matches {1} of {2}'.format(NEW_ROOT, len(new_match), total))
print('     of which q=0  : {0}'.format(sum(1 for _, _, q in new_match if q == 0)))
print('     of which q>0  : {0}'.format(sum(1 for _, _, q in new_match if q > 0)))
print('     of which q<0  : {0}'.format(sum(1 for _, _, q in new_match if q < 0)))

print('\n=== cations the root excludes because it demands u0 ===')
print('  cations in inventory              : {0}'.format(cations))
print('  cations NOT matched by either root: {0}'.format(len(excluded_charged_by_u0)))
for libname, label, q in sorted(excluded_charged_by_u0)[:40]:
    print('    q={0:+d}  {1}/{2}'.format(q, libname, label))
if len(excluded_charged_by_u0) > 40:
    print('    ... {0} more'.format(len(excluded_charged_by_u0) - 40))

print('\n=== what the recipe builds at every centre the OLD root matches ===')
for tag in sorted(matched_centre_outcome):
    print('  {0:40s} {1}'.format(tag, matched_centre_outcome[tag]))
    for ex in crash_examples.get(tag, []):
        print('      e.g. {0}'.format(ex))

print('\n=== the cations the NEW root keeps ===')
for libname, label, q in sorted((x for x in new_match if x[2] > 0))[:60]:
    print('    q={0:+d}  {1}/{2}'.format(q, libname, label))
print('  ({0} total)'.format(sum(1 for x in new_match if x[2] > 0)))
