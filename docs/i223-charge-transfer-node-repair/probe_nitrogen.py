#!/usr/bin/env python
# encoding: utf-8
"""
I-223: can root A admit N+ after all? Re-deriving a claim of impossibility.

THE CLAIM UNDER TEST, quoted from groups.py as committed at 995efc1c7:

    "N+ ... is excluded only because a group's `u` and `p` lists are a CROSS PRODUCT, not a
     disjunction: any root admitting `N u2 p1` also admits `O u1 p1` (H2O+) and `O u0 p1` (NO+),
     which crash. The vocabulary that would separate them is a charge-specific atom type per
     element, and the engine defines exactly six."

The first sentence is true of a FLAT group and the conclusion does not follow from it, because a
flat group is not the only thing a root can be. `_match_reactant_to_template` (family.py:1817-1829)
has an explicit LogicNode branch, which this ticket already measured in section 13.3 -- so a root
written as `OR{}` over per-element children separates `N u2 p1` from `O u1 p1` exactly, with no new
atom type. Round 61 reports it does, reproducing 16 of 27 entries including entry 18. This probe
re-derives that from scratch before anything is built on it.

WHAT IT MEASURES, for each candidate root A, against all 27 entries -- the 15 active ones AND the
12 in reactions-unrepresentable.py, because the whole question is whether entry 18 comes back:

  right / wrong   entries reproduced with declared / with different products
  crash-pool      species of the 22,344-species corpus that abort the family as the *2 partner
  crash-A         root-A matchers that abort it as the *1 reactant
  crash-back      the family's own products, fed back in as reactants
  like            generated reactions whose two reactants carry the same charge sign

A candidate is only better than the committed root if it reproduces MORE and crashes NO more.
"""

import argparse
import itertools
import logging
import os
import sys
import time
import traceback

from rmgpy.data.base import Entry, make_logic_node
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.kinetics.depository import KineticsDepository
from rmgpy.molecule.group import Group

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_rootsafety import load_pool, matches, run, hdr, UNREP, SAFE_CATION, SAFE_NEUTRAL  # noqa

# The new node. N+ is `N u2 p1 c+1`: nitrogen has 5 valence electrons, c+1 leaves 4, and u2 p1 is
# exactly 4. GAIN_RADICAL takes it to `N u3 p1 c0`, which is ground-state atomic nitrogen -- the
# declared product of entry 18. The engine types both ends; N+ is N3sc.
N_ATOM_ION = '1 *1 N u2 p1 c+1'

CANDIDATES = [
    ('committed  [H,O,metal] ux p[0,2]', 'group',
     '1 *1 [H,O,metal] ux p[0,2] c[+1,+2,+3,+4]'),
    ('flat+N     [H,O,N,metal] ux p[0,1,2]', 'group',
     '1 *1 [H,O,N,metal] ux p[0,1,2] c[+1,+2,+3,+4]'),
    ('OR{children}', 'logic',
     'OR{H_cation, O_cation, Metal_cation}'),
    ('OR{children, N_atom_ion}', 'logic',
     'OR{H_cation, O_cation, Metal_cation, N_atom_ion}'),
]


def same(a, b):
    if len(a) != len(b):
        return False
    rem = list(b)
    for x in a:
        for i, y in enumerate(rem):
            try:
                if x.is_isomorphic(y):
                    rem.pop(i)
                    break
            except Exception:
                continue
        else:
            return False
    return True


def as_mols(objs):
    return [(o.molecule[0] if hasattr(o, 'molecule') else o) for o in objs]


def all_declared(family):
    """Every entry this family has ever carried: the 15 active and the 12 set aside."""
    out = []
    for e in family.get_training_depository().entries.values():
        out.append((e.index, 'active',
                    [s.molecule[0] for s in e.item.reactants],
                    [s.molecule[0] for s in e.item.products]))
    if os.path.exists(UNREP):
        dep = KineticsDepository(label='unrepresentable')
        dep.load(UNREP, KineticsDatabase().local_context, None)
        for e in dep.entries.values():
            out.append((e.index, 'set-aside',
                        [s.molecule[0] for s in e.item.reactants],
                        [s.molecule[0] for s in e.item.products]))
    return sorted(out, key=lambda t: t[0])


def score(family, pool, keys, declared, train_p, train_r):
    right, wrong, rxns, like, crash_tr = {}, {}, 0, 0, 0
    # Every unordered pair of reactants named by ANY of the 27 entries.
    rk = sorted({k for _, _, dr, _ in declared for m in dr
                 for k in ['{0}|{1:+d}'.format(m.to_smiles(), m.get_net_charge())]
                 if k in pool})
    for k1, k2 in itertools.combinations_with_replacement(rk, 2):
        try:
            out = family.generate_reactions(
                [pool[k1][0].copy(deep=True), pool[k2][0].copy(deep=True)])
        except Exception:
            crash_tr += 1
            continue
        for rx in out:
            rm, pm = as_mols(rx.reactants), as_mols(rx.products)
            rxns += 1
            qs = [m.get_net_charge() for m in rm]
            if all(q > 0 for q in qs) or all(q < 0 for q in qs):
                like += 1
            for idx, kind, dr, dp in declared:
                if same(rm, dr):
                    (right if same(pm, dp) else wrong)[idx] = kind
                elif same(rm, dp):
                    (right if same(pm, dr) else wrong)[idx] = kind

    a_keys, crash_pool = [], 0
    for k in keys:
        if matches(family, pool[k][0], 0):
            a_keys.append(k)
        _, exc = run(family, pool[k][0], pool[SAFE_CATION][0])
        if exc is not None:
            crash_pool += 1
    crash_a = sum(1 for k in a_keys
                  if run(family, pool[k][0], pool[SAFE_NEUTRAL][0])[1] is not None)
    back = [pk for pk in train_p
            if any(run(family, pool[pk][0], pool[r][0])[1] is not None for r in train_r)]
    return dict(right=right, wrong=wrong, rxns=rxns, like=like, crash_tr=crash_tr,
                crash_pool=crash_pool, crash_a=crash_a, back=back, n_a=len(a_keys))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0, help='cap the corpus (timing runs only)')
    args = ap.parse_args()
    logging.getLogger().setLevel(logging.CRITICAL)

    t0 = time.time()
    family, pool, n_thermo, n_unrep, train_r, train_p = load_pool()
    keys = sorted(pool)
    if args.limit:
        import random
        held = [k for k in keys if pool[k][1].startswith(('training', 'unrepresentable'))]
        rest = [k for k in keys if k not in held]
        random.Random(223).shuffle(rest)
        keys = sorted(set(held) | set(rest[:max(0, args.limit - len(held))]))
        print('CORPUS CAPPED to {0} -- timing run, not a verdict.'.format(len(keys)))
    print('corpus = {0} species in {1:.0f}s'.format(len(pool), time.time() - t0))

    declared = all_declared(family)
    n_active = sum(1 for d in declared if d[1] == 'active')
    print('declared entries = {0}  ({1} active + {2} set aside)'.format(
        len(declared), n_active, len(declared) - n_active))

    # N+ itself, before any candidate: does the engine type it, and does the recipe work on it?
    hdr('PART 0 -- N+ on its own terms, before any root is changed')
    npm = None
    for idx, kind, dr, dp in declared:
        if idx == 18:
            npm = [m.copy(deep=True) for m in dr]
            print('entry 18 = {0} -> {1}'.format(
                ' + '.join(m.to_smiles() for m in dr), ' + '.join(m.to_smiles() for m in dp)))
    if npm:
        for m in npm:
            m.clear_labeled_atoms()
            for a in m.atoms:
                if a.charge:
                    print('  charged atom in {0}: {1} u{2} p{3} c{4:+d}   atomtype = {5}'.format(
                        m.to_smiles(), a.element.symbol, a.radical_electrons,
                        a.lone_pairs, a.charge, a.atomtype.label))
    print('')
    print('The committed comment says N+ "would work perfectly well with this recipe". If the')
    print('atomtype above resolves, the only thing excluding it is the shape of root A.')

    hdr('CANDIDATE ROOTS FOR A, scored over all {0} entries and the {1}-species corpus'.format(
        len(declared), len(keys)))
    orig = family.forward_template.reactants[0].item
    row = '{0:<38} {1:>7} {2:>7} {3:>6} {4:>10} {5:>8} {6:>7} {7:>5} {8:>5}'
    header = row.format('root A', 'right', 'wrong', 'e18', 'crash-pool', 'crash-A',
                        'c-back', 'like', 'rxns')
    print(header)
    print('-' * len(header))
    results = {}
    for name, kind, spec in CANDIDATES:
        # The new node has to exist in groups.entries before an OR can name it.
        if 'N_atom_ion' in spec and 'N_atom_ion' not in family.groups.entries:
            family.groups.entries['N_atom_ion'] = Entry(
                index=121, label='N_atom_ion',
                item=Group().from_adjacency_list(N_ATOM_ION),
                parent=family.groups.entries['A'], children=[])
        try:
            family.forward_template.reactants[0].item = (
                make_logic_node(spec) if kind == 'logic' else Group().from_adjacency_list(spec))
            r = score(family, pool, keys, declared, train_p, train_r)
        except Exception as exc:
            print(row.format(name[:38], 'BUILD/SCORE FAILED', type(exc).__name__,
                             '', '', '', '', '', ''))
            continue
        results[name] = r
        print(row.format(name[:38], len(r['right']), len(r['wrong']),
                         'YES' if 18 in r['right'] else ('WRONG' if 18 in r['wrong'] else 'no'),
                         r['crash_pool'], r['crash_a'], len(r['back']), r['like'], r['rxns']))
    family.forward_template.reactants[0].item = orig

    hdr('WHICH ENTRIES EACH CANDIDATE REPRODUCES')
    for name, r in results.items():
        act = sorted(i for i, k in r['right'].items() if k == 'active')
        aside = sorted(i for i, k in r['right'].items() if k == 'set-aside')
        print('  {0}'.format(name))
        print('     active reproduced    : {0:>2}  {1}'.format(len(act), act))
        print('     set-aside recovered  : {0:>2}  {1}'.format(len(aside), aside))
        if r['wrong']:
            print('     WRONG products       : {0}'.format(sorted(r['wrong'])))

    hdr('VERDICT')
    base = results.get('committed  [H,O,metal] ux p[0,2]')
    best = results.get('OR{children, N_atom_ion}')
    if base is None or best is None:
        print('Could not score both the committed root and the OR+N candidate; nothing concluded.')
        return 2
    gained = sorted(set(best['right']) - set(base['right']))
    worse = (best['crash_pool'] > base['crash_pool'] or best['crash_a'] > base['crash_a']
             or len(best['back']) > len(base['back']) or len(best['wrong']) > len(base['wrong'])
             or best['like'] > base['like'])
    print('committed root reproduces {0}; OR+N_atom_ion reproduces {1}.'.format(
        len(base['right']), len(best['right'])))
    print('entries gained: {0}'.format(gained))
    print('crash counts   committed {0}/{1}/{2}   OR+N {3}/{4}/{5}  (pool / root-A / feedback)'.format(
        base['crash_pool'], base['crash_a'], len(base['back']),
        best['crash_pool'], best['crash_a'], len(best['back'])))
    print('')
    if gained and not worse:
        print('CONFIRMED: the impossibility claim in groups.py is WRONG. Admitting N+ costs')
        print('nothing measurable and recovers {0}.'.format(gained))
        return 0
    if not gained:
        print('NOT CONFIRMED: the OR+N candidate reproduces nothing the committed root does not.')
        return 1
    print('PARTIAL: entries are gained but something got worse. See the table.')
    return 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
