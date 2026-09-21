#!/usr/bin/env python
# encoding: utf-8
"""
I-223: candidate roots, scored on the crash surface probe_rootsafety.py opened up.

probe_rootsafety.py measured the committed roots against every species the installed thermo
libraries name and found the family is NOT crash-safe: 17,009 of 22,344 species abort it through
root B, 630 of 645 root-A matchers abort it through root A, and one of the family's OWN products
(N2+, made by training entries 15 and 23) aborts it when fed back in. This probe is the repair
search: it scores candidate root pairs on that surface and on the family's own training set at the
same time, because a root that is crash-free by virtue of matching nothing is not a repair.

Scored per candidate pair, over the SAME pool probe_rootsafety.py used:

  crash-pool   species (of 22,344) that abort the family as the *2 partner
  crash-A      root-A matchers that abort it as the *1 reactant
  crash-back   the family's own training products that abort it when fed back in  -- must be 0
  right/wrong  training entries reproduced with their declared / with different products
  rxns         reactions generated over the training reactant pool
  like         generated reactions with two reactants of the same charge sign

The candidates are narrowings, never widenings. Every widening measured in this ticket traded one
crash for another or for silently wrong products, and a crash aborts a whole RMG job.

  A0/B0   the committed roots, as the control.
  A1/B1   the root narrowed to the union of the ELEMENTS its own children name. The committed
          roots are broader than their own subtrees -- root A says `R` while its three children
          are H, O and metal -- and that gap is the entire root-A crash surface.
  A2/B2   the root written as a LogicOr over its children, so the template matches the authored
          chemistry and nothing else. `Anion` in this family is already written this way.
"""

import argparse
import collections
import itertools
import logging
import os
import sys
import time
import traceback

from rmgpy.molecule.group import Group
from rmgpy.data.base import make_logic_node

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_rootsafety import (load_pool, matches, run, hdr,  # noqa: E402
                              SAFE_CATION, SAFE_NEUTRAL)

CAND_A = collections.OrderedDict([
    ('A0 committed  R ux p[0,2] c+',
     '1 *1 R ux p[0,2] c[+1,+2,+3,+4]'),
    ('A1 elements   [H,O,metal]',
     '1 *1 [H,O,metal] ux p[0,2] c[+1,+2,+3,+4]'),
    ('A2 OR{children}',
     'OR{H_cation, O_cation, Metal_cation}'),
])

CAND_B = collections.OrderedDict([
    ('B0 committed  R u[0,1] p[1-4] c0-',
     '1 *2 R u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]'),
    ('B1 elements   [H,O,N]',
     '1 *2 [H,O,N] u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]'),
    ('B2 OR{children}',
     'OR{Anion, N_neutral}'),
])


def build(family, spec):
    if spec.startswith('OR{') or spec.startswith('AND{'):
        return make_logic_node(spec)
    return Group().from_adjacency_list(spec)


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


def score(family, pool, keys, train_r, train_p, declared, limit_pool):
    """Score the family AS CURRENTLY TEMPLATED. Returns a dict."""
    res = {}

    # crash-back: the family's own products, fed back in as reactants
    back = []
    for pk in train_p:
        for rk in train_r:
            _, exc = run(family, pool[pk][0], pool[rk][0])
            if exc is not None:
                back.append(pk)
                break
    res['crash_back'] = back

    # crash-pool: every pool species as the *2 partner of a known-safe cation
    a_keys, crash_pool = [], 0
    for k in keys:
        if matches(family, pool[k][0], 0):
            a_keys.append(k)
        _, exc = run(family, pool[k][0], pool[SAFE_CATION][0])
        if exc is not None:
            crash_pool += 1
    res['crash_pool'] = crash_pool
    res['n_a'] = len(a_keys)

    # crash-A: every root-A matcher as the *1 reactant against a known-safe neutral
    crash_a = 0
    for k in a_keys:
        _, exc = run(family, pool[k][0], pool[SAFE_NEUTRAL][0])
        if exc is not None:
            crash_a += 1
    res['crash_a'] = crash_a

    # the training set itself
    right, wrong, rxns, like, crash_tr = set(), set(), 0, 0, 0
    for k1, k2 in itertools.combinations_with_replacement(sorted(train_r), 2):
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
            for idx, dr, dp in declared:
                if same(rm, dr):
                    (right if same(pm, dp) else wrong).add(idx)
                elif same(rm, dp):
                    (right if same(pm, dr) else wrong).add(idx)
    res.update(right=len(right), wrong=len(wrong), rxns=rxns, like=like, crash_tr=crash_tr)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0, help='cap the pool (timing runs only)')
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
        print('POOL CAPPED to {0} -- timing run, not a verdict.'.format(len(keys)))
    print('pool = {0} species ({1} thermo, +{2} unrepresentable) in {3:.0f}s'.format(
        len(pool), n_thermo, n_unrep, time.time() - t0))
    print('training reactants = {0}   training products = {1}'.format(len(train_r), len(train_p)))

    dep = family.get_training_depository()
    entries = sorted(dep.entries.values(), key=lambda e: e.index)
    declared = [(e.index,
                 [s.molecule[0] for s in e.item.reactants],
                 [s.molecule[0] for s in e.item.products]) for e in entries]
    n_entries = len(entries)

    hdr('CANDIDATE ROOT PAIRS, scored on the crash surface and on the training set')
    print('pool = {0} species. "crash-pool" and "crash-A" are counts of SPECIES, not pairs.'.format(
        len(keys)))
    print('A repair has crash-back = 0 first; then crash-pool and crash-A as low as possible;')
    print('then right = {0} of {0} and wrong = 0. A candidate that trades reproduction for'.format(
        n_entries))
    print('crash-safety is not a repair.')
    print('')
    row = '{0:<24} {1:<24} {2:>10} {3:>8} {4:>7} {5:>7} {6:>6} {7:>6} {8:>5}'
    header = row.format('root A', 'root B', 'crash-pool', 'crash-A', 'c-back',
                        'matchA', 'right', 'wrong', 'rxns')
    print(header)
    print('-' * len(header))

    orig_a = family.forward_template.reactants[0].item
    orig_b = family.forward_template.reactants[1].item
    results = {}
    for (an, aspec), (bn, bspec) in itertools.product(CAND_A.items(), CAND_B.items()):
        try:
            family.forward_template.reactants[0].item = build(family, aspec)
            family.forward_template.reactants[1].item = build(family, bspec)
        except Exception as exc:
            print(row.format(an[:24], bn[:24], 'BUILD FAILED: {0}'.format(type(exc).__name__),
                             '', '', '', '', '', ''))
            continue
        try:
            r = score(family, pool, keys, train_r, train_p, declared, args.limit)
        except Exception as exc:
            print(row.format(an[:24], bn[:24], 'SCORE FAILED', type(exc).__name__,
                             '', '', '', '', ''))
            continue
        results[(an, bn)] = r
        print(row.format(an[:24], bn[:24], r['crash_pool'], r['crash_a'],
                         len(r['crash_back']), r['n_a'],
                         '{0}/{1}'.format(r['right'], n_entries), r['wrong'], r['rxns']))
    family.forward_template.reactants[0].item = orig_a
    family.forward_template.reactants[1].item = orig_b

    hdr('WHICH CANDIDATES ARE CRASH-FREE AND STILL REPRODUCE EVERYTHING')
    clean = [(k, r) for k, r in results.items()
             if r['crash_pool'] == 0 and r['crash_a'] == 0 and not r['crash_back']
             and r['crash_tr'] == 0 and r['right'] == n_entries and r['wrong'] == 0]
    if clean:
        for (an, bn), r in clean:
            print('  {0:<24} + {1:<24}   {2} reactions, {3} like-charge'.format(
                an, bn, r['rxns'], r['like']))
    else:
        print('  NONE. No candidate root pair is both crash-free over the pool and faithful to')
        print('  the training set. Ranked by crash count, then by reproduction:')
        for (an, bn), r in sorted(results.items(),
                                  key=lambda kv: (kv[1]['crash_pool'] + kv[1]['crash_a']
                                                  + len(kv[1]['crash_back']),
                                                  -kv[1]['right'])):
            print('  {0:<24} + {1:<24} crash {2}+{3}+{4}, right {5}/{6}, wrong {7}'.format(
                an, bn, r['crash_pool'], r['crash_a'], len(r['crash_back']),
                r['right'], n_entries, r['wrong']))
    print('')
    print('What this probe could NOT reach: the same holes probe_rootsafety.py lists -- species')
    print('RMG generates rather than reads, real cations at scale, and everything downstream of')
    print('generation. It also does not run the twelve database checks; a root that scores well')
    print('here still has to sample, descend and pass them.')
    return 0 if clean else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
