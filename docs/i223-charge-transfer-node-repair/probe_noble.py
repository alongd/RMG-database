#!/usr/bin/env python
# encoding: utf-8
"""
I-223: decide the Noble_cation repair.

The node must (a) still match every noble-gas cation the current wildcard form
matches, and (b) produce a sample molecule that descends back to root A.  This
compares the current form against two candidate repairs on both counts.
"""

import os
import sys

from rmgpy import settings
from rmgpy.molecule.group import Group
from rmgpy.molecule.molecule import Molecule

CURRENT = '1 *1 [He,Ne,Ar] ux px c+1'

CANDIDATES = {
    'current            [He,Ne,Ar] ux px c+1': CURRENT,
    'cand-A  charge-specific  [Ar+,He,Ne] ux px c+1': '1 *1 [Ar+,He,Ne] ux px c+1',
    'cand-B  narrowed         [Ar,Ne,He] u1 p3 c+1': '1 *1 [Ar,Ne,He] u1 p3 c+1',
    'cand-C  He_ion child     He u1 p0 c+1': '1 *1 He u1 p0 c+1',
    'cand-C  Ne_ion child     Ne u1 p3 c+1': '1 *1 Ne u1 p3 c+1',
    'cand-C  Ar_ion child     Ar u1 p3 c+1 (existing)': '1 *1 Ar u1 p3 c+1',
}

SPECIES = {
    'He+       [He+]': '1 *1 He u1 p0 c+1',
    'Ne+       [Ne+]': '1 *1 Ne u1 p3 c+1',
    'Ar+       [Ar+]': '1 *1 Ar u1 p3 c+1',
    'Ar2+  (Ar0s-Ar+)': """
1 *1 Ar u0 p3 c+1 {2,S}
2    Ar u1 p3 c0  {1,S}
""",
    'ArH+  (argonium)': """
1 *1 Ar u0 p3 c+1 {2,S}
2    H  u0 p0 c0  {1,S}
""",
}


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('')

    mols = {}
    print('--- species build/typing ---')
    for name, adj in SPECIES.items():
        try:
            m = Molecule().from_adjacency_list(adj)
            m.update()
            mols[name] = m
            print('  {0:<18} charge={1:+d} atomtypes={2}'.format(
                name, m.get_net_charge(), [a.atomtype.label for a in m.atoms]))
        except Exception as exc:
            print('  {0:<18} FAIL {1}: {2}'.format(name, type(exc).__name__, exc))

    print('')
    print('--- sampling ---')
    groups = {}
    for name, adj in CANDIDATES.items():
        g = Group().from_adjacency_list(adj)
        groups[name] = g
        try:
            s = g.make_sample_molecule()
            print('  {0:<46} sample={1:<12} charge={2:+d}'.format(
                name, s.to_smiles(), s.get_net_charge()))
        except Exception as exc:
            print('  {0:<46} FAIL {1}: {2}'.format(name, type(exc).__name__, exc))

    print('')
    print('--- matching (does the node still catch the species it means?) ---')
    width = max(len(n) for n in CANDIDATES)
    print('  {0:<{1}} {2}'.format('node', width, '  '.join('{0:<18}'.format(s) for s in SPECIES)))
    for name, g in groups.items():
        cells = []
        for sname in SPECIES:
            if sname not in mols:
                cells.append('{0:<18}'.format('n/a'))
                continue
            try:
                hit = mols[sname].is_subgraph_isomorphic(g)
            except Exception as exc:
                hit = type(exc).__name__
            cells.append('{0:<18}'.format(str(hit)))
        print('  {0:<{1}} {2}'.format(name, width, '  '.join(cells)))

    return 0


if __name__ == '__main__':
    sys.exit(main())
