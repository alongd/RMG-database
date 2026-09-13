#!/usr/bin/env python
# encoding: utf-8
"""
I-223: try candidate repairs for Noble_cation and H2_ion before editing groups.py.

Answers three questions the repair depends on:
  1. Does today's H2_ion node actually match the family's own H2p_r1 training species?
  2. Can RMG build and type He+/Ne+ molecules at all (no atom type may be added)?
  3. Do the candidate replacement groups sample, descend, and still match the real species?
"""

import os
import sys

from rmgpy import settings
from rmgpy.molecule.group import Group
from rmgpy.molecule.molecule import Molecule

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

H2P_R1 = """
1    H u1 p0 c0
2 *1 H u0 p0 c+1
"""

CANDIDATES = {
    'H2_ion (current, bonded)': """
1 *1 H u0 p0 c+1 {2,S}
2    H u1 p0 c0  {1,S}
""",
    'H2_ion (candidate, vdW-disconnected)': """
1 *1 H u0 p0 c+1
2    H u1 p0 c0
""",
    'Noble_cation (current)': """
1 *1 [He,Ne,Ar] ux px c+1
""",
    'Noble_cation (candidate, Ar first + explicit u/p)': """
1 *1 [Ar,Ne,He] u1 p3 c+1
""",
    'He_ion (candidate child)': """
1 *1 He u1 p0 c+1
""",
    'Ne_ion (candidate child)': """
1 *1 Ne u1 p3 c+1
""",
}

SPECIES = {
    'He+': '1 He u1 p0 c+1',
    'Ne+': '1 Ne u1 p3 c+1',
    'Ar+': '1 Ar u1 p3 c+1',
    'H2+ (vdW)': H2P_R1,
}


def show(title):
    print('')
    print('=' * 78)
    print(title)
    print('=' * 78)


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))

    show('1. Can RMG build and type these ions? (no atom type may be added)')
    mols = {}
    for name, adj in SPECIES.items():
        try:
            m = Molecule().from_adjacency_list(adj)
            m.update()
            types = [a.atomtype.label for a in m.atoms]
            mols[name] = m
            print('  {0:<12} OK   charge={1:+d}  atomtypes={2}  smiles={3!r}'.format(
                name, m.get_net_charge(), types, m.to_smiles()))
        except Exception as exc:
            print('  {0:<12} FAIL {1}: {2}'.format(name, type(exc).__name__, exc))

    show('2. Does each candidate group sample to something of the right charge?')
    groups = {}
    for name, adj in CANDIDATES.items():
        g = Group().from_adjacency_list(adj)
        groups[name] = g
        try:
            s = g.make_sample_molecule()
            print('  {0:<42} sample={1:<12} charge={2:+d}'.format(
                name, s.to_smiles(), s.get_net_charge()))
            print('  {0:<42} adjlist: {1}'.format(
                '', s.to_adjacency_list().rstrip().replace('\n', ' | ')))
        except Exception as exc:
            print('  {0:<42} FAIL {1}: {2}'.format(name, type(exc).__name__, exc))

    show('3. Does each candidate group match the real species it is meant to describe?')
    pairs = [
        ('H2_ion (current, bonded)', 'H2+ (vdW)'),
        ('H2_ion (candidate, vdW-disconnected)', 'H2+ (vdW)'),
        ('Noble_cation (current)', 'He+'),
        ('Noble_cation (current)', 'Ne+'),
        ('Noble_cation (current)', 'Ar+'),
        ('Noble_cation (candidate, Ar first + explicit u/p)', 'He+'),
        ('Noble_cation (candidate, Ar first + explicit u/p)', 'Ne+'),
        ('Noble_cation (candidate, Ar first + explicit u/p)', 'Ar+'),
        ('He_ion (candidate child)', 'He+'),
        ('Ne_ion (candidate child)', 'Ne+'),
    ]
    for gname, mname in pairs:
        if mname not in mols:
            print('  {0:<42} vs {1:<12} SKIPPED (species would not build)'.format(gname, mname))
            continue
        m = mols[mname]
        try:
            hit = m.is_subgraph_isomorphic(groups[gname])
        except Exception as exc:
            hit = '{0}: {1}'.format(type(exc).__name__, exc)
        print('  {0:<42} vs {1:<12} subgraph_isomorphic = {2}'.format(gname, mname, hit))

    show('4. Where does the real H2p_r1 species descend today?')
    family = load_family()
    m = Molecule().from_adjacency_list(H2P_R1)
    m.update()
    labeled = m.get_all_labeled_atoms()
    match = family.groups.descend_tree(m, labeled, strict=True, root=family.groups.entries['A'])
    print('  H2p_r1 descends to: {0}'.format(match.label if match else None))
    print('  (H2_ion is the node that is supposed to catch it)')

    show('5. Which training reactions carry a *1 that is a noble-gas cation?')
    dep = family.get_training_depository()
    for e in dep.entries.values():
        for r in e.item.reactants:
            for a in r.molecule[0].atoms:
                if a.symbol in ('He', 'Ne', 'Ar') and a.charge > 0:
                    print('  index {0:>3}  {1}'.format(e.index, e.item))
                    break

    return 0


if __name__ == '__main__':
    sys.exit(main())
