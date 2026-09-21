#!/usr/bin/env python
# encoding: utf-8
"""
I-223: like-charge reactions the forbidden groups do not catch, and what would catch them.

THE DEFECT, reproduced. The family's two like-charge guards forbid two BONDED positive centres in
a product. Round 61 found that two cations still react when the positive centres are not bonded:

    Li+  +  [NH3+]CCO   ->   [Li]  +  [NH3+]CC[OH+]

one reaction, reactant charges (+1, +1), product charges (0, +2), `is_balanced()` True, every guard
silent. It then inherits the Li_ion;B rate estimated from Li+/H- MUTUAL NEUTRALISATION, which is
the opposite physical process.

WHY THE CORPUS MISSED IT, which is the more important half. probe_rootsafety.py drove 22,344
species, but the installed thermo libraries hold only FOUR cations in 78 libraries. The corpus was
blind to exactly the reactant class this family is made of. This probe fixes that: it PROTONATES
corpus species at their lone-pair N and O sites to synthesise a realistic organic-cation set, and
drives cation x cation pairs, which is the pair type no earlier measurement here ever formed.

WHAT IT THEN ASKS. Given that `is_charged_reactant_forbidden`'s own docstring in the engine says
"A group cannot express this: RMG groups match subgraphs, so a `c0` constrains the atom it is
written on and never the molecule as a whole" -- can any DATABASE-side change reach zero
like-charge reactions without losing training entries? Candidate root B narrowings are scored on:

  like        generated reactions whose two reactants carry the same charge sign  -- must be 0
  right/wrong entries of all 27 reproduced with declared / with different products
  crash-*     the crash counts probe_rootsafety.py measures, which must not regress

A candidate that reaches like = 0 by no longer reproducing the training set is not a fix.
"""

import argparse
import itertools
import logging
import os
import random
import sys
import time
import traceback

from rmgpy.data.base import Entry, make_logic_node
from rmgpy.molecule import Molecule, Atom, Bond
from rmgpy.molecule.group import Group

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_rootsafety import (load_pool, matches, run, hdr,  # noqa: E402
                              SAFE_CATION, SAFE_NEUTRAL)
from probe_nitrogen import all_declared, same, as_mols, N_ATOM_ION  # noqa: E402

# Root A is held fixed at the OR form that probe_nitrogen.py established, so that this probe
# varies one thing. Entry 18 is in the declared set either way.
ROOT_A = 'OR{H_cation, O_cation, Metal_cation, N_atom_ion}'

CAND_B = [
    ('B0 committed [H,O,N] p[1,2,3,4]', 'group',
     '1 *2 [H,O,N] u[0,1] p[1,2,3,4] c[0,-1,-2,-3,-4]'),
    ('B1 no neutral-O donor p[1,3,4]', 'group',
     '1 *2 [H,O,N] u[0,1] p[1,3,4] c[0,-1,-2,-3,-4]'),
    ('B2 OR{Anion, N_neutral}', 'logic',
     'OR{Anion, N_neutral}'),
    ('B3 OR{Anion, N2_only}', 'logic',
     'OR{Anion, N2_only}'),
]

# N2 written out in full: both nitrogens neutral, p1, joined by a triple bond. Nothing else in a
# neutral molecule looks like this -- an organic azide's terminal N#N carries c+1 on one end.
N2_ONLY = """
1 *2 N u0 p1 c0 {2,T}
2    N u0 p1 c0 {1,T}
"""


def protonate(mol):
    """Return a +1 cation made by adding H+ to a neutral lone-pair N or O, or None."""
    for i, atom in enumerate(mol.atoms):
        if atom.charge != 0 or atom.lone_pairs < 1:
            continue
        if atom.element.symbol not in ('N', 'O'):
            continue
        c = mol.copy(deep=True)
        target = c.atoms[i]
        h = Atom(element='H', radical_electrons=0, charge=0, lone_pairs=0)
        c.add_atom(h)
        c.add_bond(Bond(target, h, order=1))
        target.lone_pairs -= 1
        try:
            c.update()
        except Exception:
            continue
        if c.get_net_charge() == 1:
            return c
    return None


def build_cations(pool, keys, want, seed):
    """The synthetic cation set: real cations first, then protonated corpus species."""
    cats = {}
    for k in keys:
        if pool[k][0].get_net_charge() > 0:
            cats[k] = (pool[k][0], 'real: ' + pool[k][1])
    # The exact molecule round 61 used, so the regression case is named and permanent.
    try:
        m = Molecule().from_smiles('[NH3+]CCO')
        cats['[NH3+]CCO|+1'] = (m, 'round 61 counterexample')
    except Exception:
        pass
    rng = random.Random(seed)
    order = list(keys)
    rng.shuffle(order)
    for k in order:
        if len(cats) >= want:
            break
        if pool[k][0].get_net_charge() != 0:
            continue
        c = protonate(pool[k][0])
        if c is None:
            continue
        try:
            key = '{0}|{1:+d}'.format(c.to_smiles(), c.get_net_charge())
        except Exception:
            continue
        if key not in cats:
            cats[key] = (c, 'protonated ' + k)
    return cats


def score(family, pool, cats, keys, declared, train_p, train_r):
    """like-charge count over cation x cation, plus reproduction and the crash counts."""
    like, like_examples = 0, []
    ckeys = sorted(cats)
    for k1, k2 in itertools.combinations_with_replacement(ckeys, 2):
        try:
            out = family.generate_reactions(
                [cats[k1][0].copy(deep=True), cats[k2][0].copy(deep=True)])
        except Exception:
            continue
        for rx in out:
            rm, pm = as_mols(rx.reactants), as_mols(rx.products)
            qs = [m.get_net_charge() for m in rm]
            if all(q > 0 for q in qs) or all(q < 0 for q in qs):
                like += 1
                if len(like_examples) < 6:
                    like_examples.append('{0} -> {1}   charges {2} -> {3}'.format(
                        ' + '.join(m.to_smiles() for m in rm),
                        ' + '.join(m.to_smiles() for m in pm),
                        qs, [m.get_net_charge() for m in pm]))

    right, wrong, rxns = {}, {}, 0
    rk = sorted({k for _, _, dr, _ in declared for m in dr
                 for k in ['{0}|{1:+d}'.format(m.to_smiles(), m.get_net_charge())]
                 if k in pool})
    for k1, k2 in itertools.combinations_with_replacement(rk, 2):
        try:
            out = family.generate_reactions(
                [pool[k1][0].copy(deep=True), pool[k2][0].copy(deep=True)])
        except Exception:
            continue
        for rx in out:
            rm, pm = as_mols(rx.reactants), as_mols(rx.products)
            rxns += 1
            for idx, kind, dr, dp in declared:
                if same(rm, dr):
                    (right if same(pm, dp) else wrong)[idx] = kind
                elif same(rm, dp):
                    (right if same(pm, dr) else wrong)[idx] = kind

    crash_pool = sum(1 for k in keys
                     if run(family, pool[k][0], pool[SAFE_CATION][0])[1] is not None)
    a_keys = [k for k in keys if matches(family, pool[k][0], 0)]
    crash_a = sum(1 for k in a_keys
                  if run(family, pool[k][0], pool[SAFE_NEUTRAL][0])[1] is not None)
    back = [pk for pk in train_p
            if any(run(family, pool[pk][0], pool[r][0])[1] is not None for r in train_r)]
    return dict(like=like, ex=like_examples, right=right, wrong=wrong, rxns=rxns,
                crash_pool=crash_pool, crash_a=crash_a, back=back)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--cations', type=int, default=120,
                    help='size of the synthetic cation set (pairs go as the square)')
    ap.add_argument('--seed', type=int, default=223)
    args = ap.parse_args()
    logging.getLogger().setLevel(logging.CRITICAL)

    t0 = time.time()
    family, pool, n_thermo, n_unrep, train_r, train_p = load_pool()
    keys = sorted(pool)
    if args.limit:
        held = [k for k in keys if pool[k][1].startswith(('training', 'unrepresentable'))]
        rest = [k for k in keys if k not in held]
        random.Random(args.seed).shuffle(rest)
        keys = sorted(set(held) | set(rest[:max(0, args.limit - len(held))]))
        print('CORPUS CAPPED to {0} -- timing run, not a verdict.'.format(len(keys)))
    print('corpus = {0} species in {1:.0f}s'.format(len(pool), time.time() - t0))

    if 'N_atom_ion' not in family.groups.entries:
        family.groups.entries['N_atom_ion'] = Entry(
            index=121, label='N_atom_ion', item=Group().from_adjacency_list(N_ATOM_ION),
            parent=family.groups.entries['A'], children=[])
    if 'N2_only' not in family.groups.entries:
        family.groups.entries['N2_only'] = Entry(
            index=214, label='N2_only', item=Group().from_adjacency_list(N2_ONLY),
            parent=family.groups.entries['B'], children=[])

    declared = all_declared(family)

    hdr('PART 1 -- the synthetic cation set, because the corpus has almost none')
    cats = build_cations(pool, keys, args.cations, args.seed)
    real = [k for k, v in cats.items() if v[1].startswith('real')]
    print('installed thermo libraries hold {0} cations in 78 files. This probe adds protonated'.format(
        len(real)))
    print('corpus species to reach {0}, giving {1} unordered cation pairs.'.format(
        len(cats), len(cats) * (len(cats) + 1) // 2))
    print('')
    for k in sorted(cats)[:12]:
        print('   {0:<40} {1}'.format(k[:40], cats[k][1]))
    print('   ... {0} more'.format(max(0, len(cats) - 12)))

    hdr('PART 2 -- the defect, on the committed guards')
    orig_a = family.forward_template.reactants[0].item
    orig_b = family.forward_template.reactants[1].item
    forb = sorted(family.forbidden.entries) if family.forbidden else []
    print('forbidden groups loaded : {0}'.format(forb))
    print('root A held at          : {0}'.format(ROOT_A))
    print('')
    row = '{0:<34} {1:>6} {2:>7} {3:>7} {4:>10} {5:>8} {6:>7} {7:>5}'
    header = row.format('root B', 'like', 'right', 'wrong', 'crash-pool', 'crash-A', 'c-back',
                        'rxns')
    print(header)
    print('-' * len(header))
    results = {}
    for name, kind, spec in CAND_B:
        try:
            family.forward_template.reactants[0].item = make_logic_node(ROOT_A)
            family.forward_template.reactants[1].item = (
                make_logic_node(spec) if kind == 'logic' else Group().from_adjacency_list(spec))
            r = score(family, pool, cats, keys, declared, train_p, train_r)
        except Exception as exc:
            print(row.format(name[:34], 'FAILED', type(exc).__name__, '', '', '', '', ''))
            continue
        results[name] = r
        print(row.format(name[:34], r['like'], len(r['right']), len(r['wrong']),
                         r['crash_pool'], r['crash_a'], len(r['back']), r['rxns']))
    family.forward_template.reactants[0].item = orig_a
    family.forward_template.reactants[1].item = orig_b

    hdr('PART 3 -- what the like-charge reactions actually look like')
    for name, r in results.items():
        if not r['ex']:
            continue
        print('  {0}  ({1} like-charge reactions)'.format(name, r['like']))
        for e in r['ex']:
            print('     {0}'.format(e))
        print('')

    hdr('PART 4 -- which entries survive each candidate')
    for name, r in results.items():
        act = sorted(i for i, k in r['right'].items() if k == 'active')
        aside = sorted(i for i, k in r['right'].items() if k == 'set-aside')
        print('  {0:<34} active {1:>2} {2}'.format(name, len(act), act))
        print('  {0:<34} aside  {1:>2} {3}{2}'.format(
            '', len(aside), aside, ''))

    hdr('VERDICT')
    clean = [(n, r) for n, r in results.items()
             if r['like'] == 0 and not r['wrong'] and r['crash_pool'] == 0
             and r['crash_a'] == 0 and not r['back']]
    if clean:
        best = max(clean, key=lambda kv: len(kv[1]['right']))
        print('Candidates reaching like = 0 with no crash and no wrong product:')
        for n, r in clean:
            print('   {0:<34} reproduces {1} of {2}'.format(n, len(r['right']), len(declared)))
        print('')
        print('Most faithful of those: {0}, reproducing {1} of {2}.'.format(
            best[0], len(best[1]['right']), len(declared)))
        base = results.get('B0 committed [H,O,N] p[1,2,3,4]')
        if base and len(best[1]['right']) < len(base['right']):
            print('It costs {0} entries against the committed root B. That is a trade, not a fix.'
                  .format(len(base['right']) - len(best[1]['right'])))
            return 1
        return 0
    print('NO candidate root B reaches zero like-charge reactions without other damage.')
    print('Ranked by like-charge count, then by entries reproduced:')
    for n, r in sorted(results.items(), key=lambda kv: (kv[1]['like'], -len(kv[1]['right']))):
        print('   {0:<34} like {1:>5}  right {2:>2}  wrong {3}  crash {4}/{5}/{6}'.format(
            n, r['like'], len(r['right']), len(r['wrong']),
            r['crash_pool'], r['crash_a'], len(r['back'])))
    print('')
    print('If nothing reaches zero, the finding is that a FORBIDDEN GROUP CANNOT EXPRESS THIS.')
    print('is_charged_reactant_forbidden in family.py says so in its own docstring: a group')
    print('constrains the atom it is written on, never the molecule. The engine lever that exists,')
    print('allowChargedReactants, is all-or-nothing and would bar this family\'s own ion reactants.')
    return 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
