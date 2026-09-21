#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 14 -- is the narrowed root's third match a BARE atomic cation?

The report claims `[H,Li,Na,K] u0 p0 c+1` "can only ever match a bare atomic
cation", by the valence arithmetic `charge = 1 - 2p - u - bonds`. The arithmetic
constrains ONE ATOM. It says nothing about the rest of the species, because group
matching is subgraph matching. This probe asks whether any of the three matched
species is something other than a lone atom, and if so what the families do with
it.

Three questions, in order:

  1. what the shipped `electrocatLiThermo/H3O` entry actually is, atom by atom,
     with bond counts and connected-component counts taken from the molecule
     rather than from its label;
  2. whether each family's root matches it, and at which atom;
  3. how many reactions each family generates from it.

Positive controls are built into question 3 and run in the SAME loop: `[Lip]`
must give 1 reaction from `Plasma_Radiative_Recombination` and `Ar+` must give 1
from the pairing family. A harness that returned 0 for everything -- a mis-built
family, a bad adjacency list, a swallowed exception -- would show 0 on those rows
too, and the H3O row would prove nothing. If the controls read 1 and the H3O row
reads 0, the 0 is a property of the species and not of the probe.

Question 4 asks the recipe directly at the matched centre, because a reaction
count alone cannot separate "the root never matched" from "the root matched and
generation declined afterwards" -- and it is exactly that distinction the
corrected sentence in the report has to state.
"""
import os
import sys
import traceback

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))
print()

from rmgpy.data.thermo import ThermoDatabase
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule import Molecule

FAMILIES = ['Plasma_Radiative_Recombination',
            'Plasma_Radiative_Recombination_Pairing']

# ---------------------------------------------------------------- the species
tdb = ThermoDatabase()
tdb.load_libraries(os.path.join(DB, 'thermo', 'libraries'),
                   libraries=['electrocatLiThermo', 'LithiumPrimaryThermo'])

targets = {}
for libname, lib in tdb.libraries.items():
    for entry in lib.entries.values():
        if not isinstance(entry.item, Molecule):
            continue
        if entry.label in ('H3O', 'proton', '[Lip]'):
            targets['{0}/{1}'.format(libname, entry.label)] = entry.item

print('=' * 72)
print('1. WHAT THE SHIPPED ENTRIES ARE, ATOM BY ATOM')
print('=' * 72)
for name in sorted(targets):
    mol = targets[name]
    print('--- {0}'.format(name))
    print('    adjacency list as shipped:')
    for line in mol.to_adjacency_list().strip().splitlines():
        print('        {0}'.format(line))
    frags = mol.split()
    print('    net charge          : {0:+d}'.format(mol.get_net_charge()))
    print('    atoms               : {0}'.format(len(mol.atoms)))
    print('    connected fragments : {0}'.format(len(frags)))
    for i, atom in enumerate(mol.atoms, start=1):
        print('    atom {0}: {1:<2} u{2} p{3} c{4:+d}  bonds={5}'.format(
            i, atom.element.symbol, atom.radical_electrons, atom.lone_pairs,
            atom.charge, len(atom.bonds)))
    print('    WHOLE SPECIES IS ONE UNBONDED ATOM: {0}'.format(len(mol.atoms) == 1))
    print()

# ---------------------------------------------------------------- the families
kdb = KineticsDatabase()
kdb.load_families(os.path.join(DB, 'kinetics', 'families'), families=FAMILIES)

print('=' * 72)
print('2. WHICH ATOM EACH ROOT MATCHES')
print('=' * 72)
for fam_label in FAMILIES:
    fam = kdb.families[fam_label]
    root = fam.groups.top[0]
    print('--- {0}'.format(fam_label))
    print('    root {0!r}: {1}'.format(
        root.label, root.item.to_adjacency_list().strip().replace('\n', ' / ')))
    for name in sorted(targets):
        mol = targets[name]
        hits = []
        matched = mol.is_subgraph_isomorphic(root.item.copy(deep=True))
        mappings = mol.find_subgraph_isomorphisms(root.item.copy(deep=True))
        for mapping in mappings:
            for mol_atom in mapping.keys():
                idx = mol.atoms.index(mol_atom) + 1
                hits.append('atom {0} ({1} u{2} p{3} c{4:+d} bonds={5})'.format(
                    idx, mol_atom.element.symbol, mol_atom.radical_electrons,
                    mol_atom.lone_pairs, mol_atom.charge, len(mol_atom.bonds)))
        print('    {0:<36} match={1!s:<6} {2}'.format(
            name, matched, '; '.join(hits) if hits else '-'))
    print()

# ------------------------------------------------------------- what they build
print('=' * 72)
print('3. WHAT EACH FAMILY GENERATES  (controls in the same loop)')
print('=' * 72)
CASES = [
    ('electrocatLiThermo/H3O', targets['electrocatLiThermo/H3O'], 'THE QUESTION'),
    ('electrocatLiThermo/proton', targets['electrocatLiThermo/proton'], 'control'),
    ('LithiumPrimaryThermo/[Lip]', targets['LithiumPrimaryThermo/[Lip]'],
     'POSITIVE CONTROL for Plasma_Radiative_Recombination'),
    ('Ar+ (built here)', Molecule().from_adjacency_list('multiplicity 2\n1 Ar u1 p3 c+1'),
     'POSITIVE CONTROL for the pairing family'),
]
for fam_label in FAMILIES:
    fam = kdb.families[fam_label]
    print('--- {0}'.format(fam_label))
    for name, mol, role in CASES:
        try:
            rxns = fam.generate_reactions([mol.copy(deep=True)])
        except Exception:
            print('    {0:<30} RAISES  [{1}]'.format(name, role))
            traceback.print_exc(file=sys.stdout)
            continue
        print('    {0:<30} {1} reaction(s)   [{2}]'.format(name, len(rxns), role))
        for r in rxns:
            print('        {0}   electrons={1}'.format(r, getattr(r, 'electrons', None)))
            for p in r.products:
                print('        product: {0}'.format(' / '.join(
                    l.strip() for l in p.to_adjacency_list().strip().splitlines())))
    print()

# --------------------------------------------- recipe applied to the centre
print('=' * 72)
print('4. DOES THE RECIPE ITSELF BUILD ANYTHING AT THE MATCHED H3O CENTRE?')
print('   (separates "root never matched" from "matched, generation declined")')
print('=' * 72)
for fam_label in FAMILIES:
    fam = kdb.families[fam_label]
    root = fam.groups.top[0]
    base = targets['electrocatLiThermo/H3O']
    mappings = base.find_subgraph_isomorphisms(root.item.copy(deep=True))
    print('--- {0}: {1} mapping(s) of the root onto the species'.format(
        fam_label, len(mappings)))
    if not mappings:
        print('    nothing to apply the recipe to')
        print()
        continue
    work = base.copy(deep=True)
    maps = work.find_subgraph_isomorphisms(root.item.copy(deep=True))
    for mol_atom, grp_atom in maps[0].items():
        mol_atom.label = grp_atom.label
    try:
        products = fam.apply_recipe([work])
    except Exception:
        print('    apply_recipe RAISES:')
        traceback.print_exc(file=sys.stdout)
        print()
        continue
    if products is None:
        print('    apply_recipe returned None -- the recipe declined this centre')
        print()
        continue
    for p in products:
        print('    product: {0}'.format(' / '.join(
            l.strip() for l in p.to_adjacency_list().strip().splitlines())))
        print('    product net charge {0:+d}'.format(p.get_net_charge()))
    print()

# ------------------------------------------------ WHICH branch declined, exactly
print('=' * 72)
print('5. THE EXACT REASON apply_recipe DECLINES, NOT INFERRED')
print('   family.py:1516 splits the product structure; family.py:1521-1532 returns')
print('   None when the fragment count differs from the template product count.')
print('=' * 72)
from rmgpy.data.kinetics.family import ReactionRecipe
for fam_label in FAMILIES:
    fam = kdb.families[fam_label]
    root = fam.groups.top[0]
    print('--- {0}'.format(fam_label))
    # family.py:1512 -- `self.product_num or len(template.products)`. Reading
    # `fam.product_num` alone gives None here and would score every row DECLINED.
    product_num = fam.product_num or len(fam.forward_template.products)
    print('    template products      : {0}  (family.product_num = {1}, effective = {2})'.format(
        [p.label for p in fam.forward_template.products], fam.product_num, product_num))
    for name in ('electrocatLiThermo/H3O', 'electrocatLiThermo/proton'):
        base = targets.get(name)
        if base is None:
            continue
        work = base.copy(deep=True)
        maps = work.find_subgraph_isomorphisms(root.item.copy(deep=True))
        if not maps:
            print('    {0:<28} root does not match -- not reached'.format(name))
            continue
        for mol_atom, grp_atom in maps[0].items():
            mol_atom.label = grp_atom.label
        recipe = ReactionRecipe(fam.forward_recipe.actions)
        try:
            recipe.apply_forward(work, unique=True)
        except Exception as exc:
            print('    {0:<28} recipe raises {1}: {2}'.format(
                name, type(exc).__name__, exc))
            continue
        work.update(sort_atoms=not fam.save_order)
        frags = work.split()
        print('    {0:<28} recipe builds {1} fragment(s): {2}'.format(
            name, len(frags), ', '.join(f.to_smiles() for f in frags)))
        print('    {0:<28} template wants {1}  ->  {2}'.format(
            '', product_num,
            'ACCEPTED' if len(frags) == product_num
            else 'DECLINED at family.py:1532 (product count != template count)'))
    print()
