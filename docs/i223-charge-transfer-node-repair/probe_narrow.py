#!/usr/bin/env python
# encoding: utf-8
"""
I-223 follow-up, part 2: what is the NARROWEST pair of root templates for which one recipe works?

probe_grammar.py established the answer to the prior question: no single recipe serves all 27
training entries, but `A1|B2` --

    recipe(actions=[['GAIN_RADICAL', '*1', 1],
                    ['GAIN_RADICAL', '*2', 1],
                    ['LOSE_PAIR',    '*2', 1]])

-- serves 16 of them, which is the largest single-recipe block. No charge action appears in it,
because charge actions move no electrons; the charges fall out of `update_charge` on their own.

This probe asks what the templates then have to say. It is not a formality, because the current
roots are `*1 R ux px c[+1..+4]` and `*2 R ux px c[0..-4]`, and those admit structures the recipe
cannot process:

  - `*2 R ux px c[0,...]` matches ANY neutral atom -- including the hydrogen inside a cation like
    OH+. The family then tries to take an electron from that hydrogen, `LOSE_PAIR` finds no lone
    pair, and `ActionError` propagates out of `generate_reactions`.
  - `GAIN_RADICAL` on a cation whose radical-richer form has no atom type (H2O+ -> `O u2 p1` with
    two single bonds; NO+ -> `O u1 p1` with a triple bond) raises `AtomTypeError`, likewise out of
    `generate_reactions`.

**Those are crashes, not over-generation.** A family that aborts `generate_reactions` takes the
whole RMG job with it, so narrowing the roots here is a safety requirement before it is a chemistry
preference. That is what this probe measures: for each candidate pair of roots, how many reactant
pairs crash, how many reactions come out, and how many training entries are reproduced correctly
versus reproduced WRONG.

WHAT CANNOT BE FIXED BY NARROWING, and why it bounds the answer.

A group's `u` and `p` lists are independent -- `u[0,1] p[0,2]` is a cross product, not a
disjunction -- so a single flat root cannot express "nitrogen with p1 but not oxygen with p1".
N+ is `N u2 p1 c+1` and must be admitted; H2O+ (`O u1 p1 c+1`) and NO+ (`O u0 p1 c+1`) sit at the
same `p1` and must be excluded. The only vocabulary that would separate them is a charge-specific
atom type per element, and the engine defines exactly six (`Li+ Na+ K+ Mg+ Ca+ Ar+`) -- none for
O, N or H -- and adding one is out of scope by the contract.

So the cost of admitting N+ is measured here rather than asserted, and the narrowest SAFE root is
whichever candidate reaches zero crashes.
"""

import itertools
import logging
import os
import sys
import traceback

from rmgpy import settings
from rmgpy.data.kinetics.family import ReactionRecipe
from rmgpy.molecule.group import Group

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family  # noqa: E402

A1B2 = [['GAIN_RADICAL', '*1', 1], ['GAIN_RADICAL', '*2', 1], ['LOSE_PAIR', '*2', 1]]

CATION_C = 'c[+1,+2,+3,+4]'
PARTNER_C = 'c[0,-1,-2,-3,-4]'

# Candidate roots, from the shipped one downwards. Each is a real adjacency list.
ROOTS_A = [
    ('A0 ux px      (as shipped)', '1 *1 R ux px ' + CATION_C + '\n'),
    ('A1 ux p[0,1,2]', '1 *1 R ux p[0,1,2] ' + CATION_C + '\n'),
    ('A2 ux p[0,2]', '1 *1 R ux p[0,2] ' + CATION_C + '\n'),
    ('A3 u[0,1] p[0,2]', '1 *1 R u[0,1] p[0,2] ' + CATION_C + '\n'),
]
ROOTS_B = [
    ('B0 ux px      (as shipped)', '1 *2 R ux px ' + PARTNER_C + '\n'),
    ('B1 ux p[1,2,3,4]', '1 *2 R ux p[1,2,3,4] ' + PARTNER_C + '\n'),
    ('B2 u[0,1] p[1,2,3,4]', '1 *2 R u[0,1] p[1,2,3,4] ' + PARTNER_C + '\n'),
]


def hdr(t):
    print('')
    print('=' * 100)
    print(t)
    print('=' * 100)


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


def set_recipe(family, actions):
    r = ReactionRecipe()
    for a in actions:
        r.add_action(list(a))
    family.forward_recipe = r


def set_roots(family, adj_a, adj_b):
    """Swap the two top groups in memory. The Entry objects are reused so that every other
    reference into the tree (children, template) keeps pointing at the same nodes."""
    tops = family.forward_template.reactants
    tops[0].item = Group().from_adjacency_list(adj_a)
    tops[1].item = Group().from_adjacency_list(adj_b)


def main():
    print('cwd                 = {0}'.format(os.getcwd()))
    print('engine              = {0}'.format(os.environ.get('RMGPY_ROOT', '(default)')))
    print('database.directory  = {0}'.format(settings['database.directory']))
    print('family loaded from  = docs/i154-carry-chemistry/held-back/Plasma_Charge_Transfer')
    logging.getLogger().setLevel(logging.CRITICAL)

    family = load_family()
    original_a = family.forward_template.reactants[0].item.to_adjacency_list().strip()
    original_b = family.forward_template.reactants[1].item.to_adjacency_list().strip()
    print('')
    print('shipped root A      = {0}'.format(original_a.replace('\n', ' | ')))
    print('shipped root B      = {0}'.format(original_b.replace('\n', ' | ')))
    print('recipe under test   = {0}'.format(A1B2))

    dep = family.get_training_depository()
    entries = sorted(dep.entries.values(), key=lambda e: e.index)

    declared = []
    for e in entries:
        declared.append((e.index,
                         [s.molecule[0] for s in e.item.reactants],
                         [s.molecule[0] for s in e.item.products]))

    # every distinct reactant in the training set, labels stripped, as a real job would meet them
    pool = {}
    for e in entries:
        for s in e.item.reactants:
            m = s.molecule[0].copy(deep=True)
            m.clear_labeled_atoms()
            pool.setdefault('{0}|{1:+d}'.format(m.to_smiles(), m.get_net_charge()), m)
    keys = sorted(pool)
    pairs = list(itertools.combinations_with_replacement(keys, 2))

    hdr('PART 1 -- the pool the family is driven over.')
    print('{0} distinct reactants from the 27 training entries -> {1} unordered pairs.'.format(
        len(keys), len(pairs)))
    print('Every pair is offered to generate_reactions, which is what a real job does when it')
    print('meets these species in a mechanism.')
    print('')
    print('  ' + ', '.join(keys))

    set_recipe(family, A1B2)

    hdr('PART 2 -- candidate root pairs, measured.')
    print('crashes  : reactant pairs where generate_reactions raised. Each one aborts an RMG job.')
    print('reactions: total generated over all pairs (the shipped family generates 0).')
    print('right    : training entries reproduced with their declared products.')
    print('WRONG    : training entries reproduced with DIFFERENT products -- silent bad chemistry.')
    print('')
    row = '{0:<28} {1:<24} {2:>8} {3:>10} {4:>7} {5:>7}'
    header = row.format('root A (*1 cation)', 'root B (*2 partner)', 'crashes', 'reactions', 'right', 'WRONG')
    print(header)
    print('-' * len(header))

    results = []
    for aname, aadj in ROOTS_A:
        for bname, badj in ROOTS_B:
            set_roots(family, aadj, badj)
            crashes = 0
            total = 0
            right, wrong = set(), set()
            for k1, k2 in pairs:
                m1 = pool[k1].copy(deep=True)
                m2 = pool[k2].copy(deep=True)
                try:
                    rxns = family.generate_reactions([m1, m2])
                except Exception:
                    crashes += 1
                    continue
                total += len(rxns)
                for rx in rxns:
                    rm = as_mols(rx.reactants)
                    pm = as_mols(rx.products)
                    for idx, dr, dp in declared:
                        if same(rm, dr):
                            (right if same(pm, dp) else wrong).add(idx)
                        elif same(rm, dp):
                            (right if same(pm, dr) else wrong).add(idx)
            results.append((aname, bname, crashes, total, right, wrong))
            print(row.format(aname, bname, crashes, total, len(right), len(wrong)))

    hdr('PART 3 -- the narrowest SAFE pair.')
    safe = [r for r in results if r[2] == 0]
    if not safe:
        print('NONE of the candidate root pairs reaches zero crashes.')
        print('Every one of them lets generate_reactions raise on at least one pair drawn from the')
        print('family\'s own training set, which means the family cannot be run at all.')
        best = None
    else:
        best = max(safe, key=lambda r: (len(r[4]), -len(r[5])))
        print('{0} of {1} candidate pairs are crash-free.'.format(len(safe), len(results)))
        print('')
        for aname, bname, crashes, total, right, wrong in safe:
            print('  {0:<28} {1:<24} reactions {2:>4}  right {3:>2}  WRONG {4:>2}  {5}'.format(
                aname, bname, total, len(right), len(wrong), sorted(right)))
        print('')
        print('Best crash-free pair: {0}  +  {1}'.format(best[0], best[1]))
        print('  reactions generated              : {0}'.format(best[3]))
        print('  training entries right           : {0}  {1}'.format(len(best[4]), sorted(best[4])))
        print('  training entries WRONG           : {0}  {1}'.format(len(best[5]), sorted(best[5])))
        lost = [e.index for e in entries if e.index not in best[4] and e.index not in best[5]]
        print('  training entries no longer covered: {0}  {1}'.format(len(lost), lost))
        print('')
        print('  Those uncovered entries are the chemistry that leaves the family. Each still has a')
        print('  correct, source-audited rate; what it no longer has is a family that can generate')
        print('  its reaction.')
        for e in entries:
            if e.index in lost:
                print('    {0:>3}  {1:<34} {2}'.format(e.index, e.label, e.short_desc))

    hdr('SUMMARY')
    print('  candidate root pairs measured     : {0}'.format(len(results)))
    print('  crash-free pairs                  : {0}'.format(len(safe)))
    if best:
        print('  chosen                            : {0} + {1}'.format(best[0], best[1]))
        print('  reactions generated (was 0)       : {0}'.format(best[3]))
        print('  training entries served           : {0} of {1}'.format(len(best[4]), len(entries)))
        print('  training entries served WRONGLY   : {0}'.format(len(best[5])))
    print('')
    print('What this probe could NOT reach:')
    print('  - Reactants outside the training set. The pool is the 21 species the training entries')
    print('    name; a real mechanism contains more, and a root that is safe over this pool is not')
    print('    proven safe over every molecule RMG might hand it.')
    print('  - Whether the narrowed roots keep the twelve family checks green. Measured separately.')
    print('  - Any root that is not a single flat group. A LogicOr top might express the exact set,')
    print('    but tops are consumed as Groups by _match_reactant_to_template, so that is a')
    print('    separate experiment and is not attempted here.')
    return 0 if safe else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
