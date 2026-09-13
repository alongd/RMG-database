#!/usr/bin/env python
# encoding: utf-8
"""
I-223: the Noble_cation repair must also stay a proper parent of Ar_ion.

Listing the charge-specific `Ar+` atomtype first is what makes the sample come
out at +1, but `Ar+` is *more* specific than Ar_ion's `Ar`, so the parent-child
check then fails.  This compares the ways out.
"""

import os
import sys

from rmgpy import settings
from rmgpy.data.base import Database, Entry
from rmgpy.molecule.group import Group
from rmgpy.molecule.molecule import Molecule

PARENTS = {
    'current      [He,Ne,Ar] ux px c+1': '1 *1 [He,Ne,Ar] ux px c+1',
    'P1           [Ar+,He,Ne] ux px c+1': '1 *1 [Ar+,He,Ne] ux px c+1',
    'P2           [Ar+,Ar,He,Ne] ux px c+1': '1 *1 [Ar+,Ar,He,Ne] ux px c+1',
}

CHILDREN = {
    'C1  Ar_ion as authored   Ar u1 p3 c+1': '1 *1 Ar u1 p3 c+1',
    'C2  Ar_ion charge-typed  Ar+ u1 p3 c+1': '1 *1 Ar+ u1 p3 c+1',
}

SPECIES = {
    'He+': '1 *1 He u1 p0 c+1',
    'Ne+': '1 *1 Ne u1 p3 c+1',
    'Ar+': '1 *1 Ar u1 p3 c+1',
    'Ar2+': '1 *1 Ar u0 p3 c+1 {2,S}\n2 Ar u1 p3 c0 {1,S}\n',
    'ArH+': '1 *1 Ar u0 p3 c+1 {2,S}\n2 H u0 p0 c0 {1,S}\n',
}


def main():
    print('cwd                = {0}'.format(os.getcwd()))
    print('database.directory = {0}'.format(settings['database.directory']))
    print('')

    db = Database()
    mols = {}
    for n, a in SPECIES.items():
        m = Molecule().from_adjacency_list(a)
        m.update()
        mols[n] = m

    print('--- parent samples, and parent/child validity ---')
    for pname, padj in PARENTS.items():
        p = Group().from_adjacency_list(padj)
        pe = Entry(label='parent', item=p)
        try:
            s = p.make_sample_molecule()
            sample = '{0} ({1:+d})'.format(s.to_smiles(), s.get_net_charge())
        except Exception as exc:
            sample = 'FAIL ' + type(exc).__name__
        print('  {0:<42} sample = {1}'.format(pname, sample))
        for cname, cadj in CHILDREN.items():
            ce = Entry(label='child', item=Group().from_adjacency_list(cadj))
            ok = db.match_node_to_child(pe, ce)
            print('      proper parent of {0:<40} {1}'.format(cname, ok))

    print('')
    print('--- child sampling and matching ---')
    for cname, cadj in CHILDREN.items():
        c = Group().from_adjacency_list(cadj)
        try:
            s = c.make_sample_molecule()
            sample = '{0} ({1:+d})'.format(s.to_smiles(), s.get_net_charge())
        except Exception as exc:
            sample = 'FAIL ' + type(exc).__name__
        hits = [n for n in SPECIES if mols[n].is_subgraph_isomorphic(c)]
        print('  {0:<42} sample = {1:<12} matches {2}'.format(cname, sample, hits))

    print('')
    print('--- parent matching (the set must not shrink) ---')
    for pname, padj in PARENTS.items():
        p = Group().from_adjacency_list(padj)
        hits = [n for n in SPECIES if mols[n].is_subgraph_isomorphic(p)]
        print('  {0:<42} matches {1}'.format(pname, hits))

    return 0


if __name__ == '__main__':
    sys.exit(main())
