#!/usr/bin/env python
# encoding: utf-8
"""
I-223: why does the repaired H2_ion sample fail `kinetics_check_sample_can_react`?

The recipe is charge-only (LOSE_CHARGE *1, GAIN_CHARGE *2).  H2+ has a
one-electron bond, which RMG's integer bond orders cannot hold, so the family's
own dictionary stores it as two unbonded atoms.  Neutralising the cation of an
unbonded pair therefore cannot make bonded H2 -- it makes two H atoms.  This
probe measures that, and tests every alternative representation of H2+ that does
not require a new atom type.
"""

import os
import sys

from rmgpy import settings
from rmgpy.molecule.group import Group
from rmgpy.molecule.molecule import Molecule

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

VARIANTS = {
    'unbonded  (matches the dictionary)': """
1 *1 H u0 p0 c+1
2    H u1 p0 c0
""",
    'vdW bond  {2,vdW}': """
1 *1 H u0 p0 c+1 {2,vdW}
2    H u1 p0 c0  {1,vdW}
""",
    'single bond (as authored, pre-repair)': """
1 *1 H u0 p0 c+1 {2,S}
2    H u1 p0 c0  {1,S}
""",
}

MOL_VARIANTS = {
    'H2+ unbonded': '1 H u1 p0 c0\n2 H u0 p0 c+1\n',
    'H2+ vdW-bonded': '1 H u1 p0 c0 {2,vdW}\n2 H u0 p0 c+1 {1,vdW}\n',
    'H2+ single-bonded': '1 H u1 p0 c0 {2,S}\n2 H u0 p0 c+1 {1,S}\n',
}


def hdr(t):
    print('')
    print('=' * 78)
    print(t)
    print('=' * 78)


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    # The path this probe actually loads, derived as load_family() derives it. Printing
    # settings['database.directory'] alone names the engine rmgrc's database, which is not where
    # this family comes from -- run.sh tells its reader to check that line, so it has to be the
    # right one. (Round 61.)
    print('family loaded from = {0}'.format(
        os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('I223_FAMILY_ROOT   = {0}'.format(
        os.environ.get('I223_FAMILY_ROOT', '(unset -- the default above)')))
    print('rmgpy database.directory = {0}   <- NOT used by this probe'.format(
        settings['database.directory']))

    family = load_family()

    hdr('0. the training reaction the H2_ion node exists to host')
    dep = family.get_training_depository()
    for e in dep.entries.values():
        if 'H2p' in e.label:
            print('  index {0}: {1}'.format(e.index, e.label))
            for r in e.item.reactants:
                print('    reactant {0}: {1}'.format(
                    r.label, r.molecule[0].to_adjacency_list().rstrip().replace('\n', ' | ')))
            for p in e.item.products:
                print('    product  {0}: {1}'.format(
                    p.label, p.molecule[0].to_adjacency_list().rstrip().replace('\n', ' | ')))

    hdr('1. can each H2+ molecular representation be built and typed?')
    for name, adj in MOL_VARIANTS.items():
        try:
            m = Molecule().from_adjacency_list(adj)
            m.update()
            print('  {0:<20} OK  charge={1:+d} atomtypes={2} n_fragments={3}'.format(
                name, m.get_net_charge(), [a.atomtype.label for a in m.atoms], len(m.split())))
        except Exception as exc:
            print('  {0:<20} FAIL {1}: {2}'.format(name, type(exc).__name__, str(exc).split('\n')[0]))

    hdr('2. apply the recipe to each group variant + the B-root sample')
    b_sample = family.groups.entries['Neutral'].item.make_sample_molecule()
    print('  *2 partner sample: {0}  ({1})'.format(
        b_sample.to_smiles(), b_sample.to_adjacency_list().rstrip().replace('\n', ' | ')))
    print('  recipe: {0}'.format([(a.__class__.__name__ if not isinstance(a, list) else a)
                                  for a in family.forward_recipe.actions]))
    print('')
    for name, adj in VARIANTS.items():
        g = Group().from_adjacency_list(adj)
        try:
            sample = g.make_sample_molecule()
        except Exception as exc:
            print('  {0:<40} sample FAIL {1}'.format(name, type(exc).__name__))
            continue
        print('  {0:<40} sample={1:<12} charge={2:+d}'.format(
            name, sample.to_smiles(), sample.get_net_charge()))
        try:
            products = family.apply_recipe([sample.copy(deep=True), b_sample.copy(deep=True)])
        except Exception as exc:
            print('  {0:<40}   apply_recipe RAISED {1}: {2}'.format(
                name, type(exc).__name__, str(exc).split('\n')[0]))
            continue
        if products is None:
            print('  {0:<40}   apply_recipe -> None (wrong product count, or a charged product)'.format(name))
        else:
            print('  {0:<40}   products -> {1}'.format(
                name, [p.to_smiles() for p in products]))

    hdr('3. what the recipe would have to do, spelled out')
    print('  training reaction 2 is  H2+ + H-  ->  H2 + H.')
    print('  The electron that arrives on H2+ becomes the SECOND electron of the H-H bond.')
    print('  The recipe has only LOSE_CHARGE/GAIN_CHARGE -- no bond-forming action -- so from an')
    print('  unbonded [H+].[H] it can only ever produce [H].[H], i.e. two separate H atoms.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
