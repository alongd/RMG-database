#!/usr/bin/env python
# encoding: utf-8
"""
I-223: does the family actually generate its own training reactions? Loaded from disk, as shipped.

This is the number that decides whether the narrowing worked, and it is deliberately measured
against the family FILES rather than against an in-memory mock. probe_grammar.py and
probe_narrow.py both mutate a loaded family object to try candidates; this one changes nothing. If
the files and the design have drifted apart, this probe is where it shows.

WHAT IT MEASURES, over every unordered pair drawn from the distinct species the training entries
name -- which is what a real job meets when those species appear in a mechanism:

  crashes      pairs where generate_reactions RAISED. Each one aborts an RMG job, so this is the
               number that has to be zero before anything else matters.
  reactions    total generated. The charge-only family generated 0; that is the "before".
  right        training entries the family reproduces with their declared products.
  WRONG        training entries it reproduces with DIFFERENT products. Silent bad chemistry, and
               the only category here that is worse than generating nothing.
  like-charge  generated reactions whose reactants are both cations or both anions.

               READ THE ZERO CAREFULLY. It is zero over THIS pool, which is the 13 species the
               training entries name. It does NOT mean the family generates no like-charge
               reactions: the forbidden groups only block two BONDED positive centres, and
               probe_likecharge.py measures 470 like-charge reactions over a 150-cation set that
               nothing here can block. See report.md section 15.

It also reports reactions generated BEYOND the training set. Those are not errors -- a family is
supposed to generalise -- so they are counted and shown, not judged.
"""

import itertools
import logging
import os
import sys
import traceback

from rmgpy import settings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402


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


def main():
    print('cwd                 = {0}'.format(os.getcwd()))
    print('engine              = {0}'.format(os.environ.get('RMGPY_ROOT', '(default)')))
    print('database.directory  = {0}'.format(settings['database.directory']))
    # The path is derived the same way load_family() derives it, rather than written out here.
    # It was hardcoded until round 61 pointed out that loading honours I223_FAMILY_ROOT while the
    # printed line did not, so a run against a pre-edit checkout printed the post-edit path.
    print('family loaded from  = {0}'.format(
        os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('I223_FAMILY_ROOT    = {0}'.format(
        os.environ.get('I223_FAMILY_ROOT', '(unset -- the default above)')))
    print('')
    print('NOTE: database.directory above points at a DIFFERENT worktree -- the engine\'s rmgrc')
    print('decides it and this probe never uses it. The family is loaded from the explicit path')
    print('on the line above. Stated because a reader checking provenance will notice.')
    logging.getLogger().setLevel(logging.CRITICAL)

    family = load_family()
    print('')
    print('recipe              = {0}'.format([list(a) for a in family.forward_recipe.actions]))
    for i, star in ((0, '*1'), (1, '*2')):
        item = family.forward_template.reactants[i].item
        # A root may be a LogicOr, which has no adjacency list. Root A is one.
        shown = (item.to_adjacency_list().strip().replace('\n', ' | ')
                 if hasattr(item, 'to_adjacency_list') else 'LogicNode {0}'.format(item))
        print('root {0} ({1})         = {2}'.format('AB'[i], star, shown))
    forb = sorted(family.forbidden.entries) if family.forbidden else []
    print('forbidden groups    = {0}'.format(forb))
    if family.forbidden:
        unlabelled = [k for k, e in family.forbidden.entries.items()
                      if not e.item.get_all_labeled_atoms()]
        if unlabelled:
            print('  !! UNLABELLED, therefore INERT at generation time: {0}'.format(unlabelled))

    dep = family.get_training_depository()
    entries = sorted(dep.entries.values(), key=lambda e: e.index)
    print('training entries    = {0}  {1}'.format(len(entries), [e.index for e in entries]))

    declared = [(e.index,
                 [s.molecule[0] for s in e.item.reactants],
                 [s.molecule[0] for s in e.item.products]) for e in entries]

    pool = {}
    for e in entries:
        for s in e.item.reactants:
            m = s.molecule[0].copy(deep=True)
            m.clear_labeled_atoms()
            pool.setdefault('{0}|{1:+d}'.format(m.to_smiles(), m.get_net_charge()), m)
    keys = sorted(pool)
    pairs = list(itertools.combinations_with_replacement(keys, 2))

    hdr('PART 1 -- driving the family over its own training species.')
    print('{0} distinct reactants -> {1} unordered pairs.'.format(len(keys), len(pairs)))
    print('  ' + ', '.join(keys))
    print('')

    crashes, total, like = 0, 0, 0
    right, wrong = set(), set()
    beyond = []
    crash_detail = []
    for k1, k2 in pairs:
        try:
            rxns = family.generate_reactions([pool[k1].copy(deep=True), pool[k2].copy(deep=True)])
        except Exception as exc:
            crashes += 1
            crash_detail.append('{0} + {1}: {2}'.format(k1, k2, type(exc).__name__))
            continue
        for rx in rxns:
            rm, pm = as_mols(rx.reactants), as_mols(rx.products)
            total += 1
            qs = [m.get_net_charge() for m in rm]
            if all(q > 0 for q in qs) or all(q < 0 for q in qs):
                like += 1
            hit = False
            for idx, dr, dp in declared:
                if same(rm, dr):
                    (right if same(pm, dp) else wrong).add(idx)
                    hit = True
                elif same(rm, dp):
                    (right if same(pm, dr) else wrong).add(idx)
                    hit = True
            if not hit:
                beyond.append('{0} -> {1}'.format(
                    ' + '.join(m.to_smiles() for m in rm),
                    ' + '.join(m.to_smiles() for m in pm)))

    print('crashes                       : {0}'.format(crashes))
    for c in crash_detail[:10]:
        print('    {0}'.format(c))
    print('reactions generated           : {0}'.format(total))
    print('like-charge reactant pairs    : {0}'.format(like))
    print('training entries reproduced   : {0} of {1}  {2}'.format(
        len(right), len(entries), sorted(right)))
    print('training entries WRONG        : {0}  {1}'.format(len(wrong), sorted(wrong)))
    missing = [e.index for e in entries if e.index not in right and e.index not in wrong]
    print('training entries not generated: {0}  {1}'.format(len(missing), missing))

    hdr('PART 2 -- reactions beyond the training set. Not errors; a family generalises.')
    uniq = sorted(set(beyond))
    print('{0} distinct, of {1} generated. First 20:'.format(len(uniq), total))
    for s in uniq[:20]:
        print('   {0}'.format(s))

    hdr('SUMMARY')
    print('  before this change (charge-only recipe) : 0 reactions')
    print('  after                                   : {0} reactions'.format(total))
    print('  crashes                                 : {0}'.format(crashes))
    print('  training entries reproduced correctly   : {0} of {1}'.format(len(right), len(entries)))
    print('  training entries reproduced wrongly     : {0}'.format(len(wrong)))
    print('  like-charge reactions surviving         : {0}'.format(like))
    print('')
    print('What this probe could NOT reach:')
    print('  - Species outside the training set. A root safe over these {0} is not proven safe'.format(len(keys)))
    print('    over every molecule a real mechanism contains.')
    print('  - Rate correctness. That is the source audits, and they are untouched by this change.')
    print('  - The reverse family, which does not exist in this repository.')
    print('')
    ok = (crashes == 0 and len(wrong) == 0 and len(right) == len(entries) and total > 0)
    if ok:
        print('VERDICT: the family generates reactions, reproduces every one of its {0} training'.format(
            len(entries)))
        print('entries correctly, reproduces none wrongly, and crashes on nothing.')
        return 0
    print('VERDICT: NOT clean -- crashes {0}, wrong {1}, unreproduced {2}, total {3}.'.format(
        crashes, len(wrong), len(missing), total))
    return 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
