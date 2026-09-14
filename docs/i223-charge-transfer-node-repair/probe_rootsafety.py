#!/usr/bin/env python
# encoding: utf-8
"""
I-223: are the narrowed roots crash-safe on species OUTSIDE the training set?

THE CLAIM UNDER TEST, and why it is the one worth testing. After the redesign the family
generates 45 reactions, reproduces 15 of 15 training entries and crashes on nothing -- but that
was measured over the **13 species the training entries name**. The roots are the one load-bearing
piece proven only over that pool, and the failure mode is the bad kind: when `generate_reactions`
raises, it propagates out of `react()` and aborts the whole RMG job. Over-generation only makes a
mechanism bigger. A raise makes it impossible.

So: treat "the roots are safe" as unverified and try to break it, over every species the installed
thermo libraries contain.

    python probe_rootsafety.py [--limit N] [--sample M] [--seed S]

THE POOL. Every entry of every library under `input/thermo/libraries/` -- 78 libraries, deduped by
(SMILES, net charge). That is the set of species an RMG job can name from a library today, and it
is ~1700x the training pool. Two things it is NOT:

  - It is not the set of species RMG *generates*. RMG makes species the libraries never list, and
    this probe cannot reach them. Stated again in the closing "could NOT reach" block.
  - It is almost entirely neutral. The installed database holds FOUR cations in total across all
    78 libraries, one of which is the plasma campaign's own `[Ar+]`. So the pool exercises root B
    (the neutral/anion partner) very hard and root A (the cation) barely at all. The cations named
    by the family's own training set and by `reactions-unrepresentable.py` are added for that
    reason, and they are the realistic root-A exposure for a plasma job.

WHY THIS IS MEASURED PER MOLECULE RATHER THAN PER PAIR. The recipe is

    GAIN_RADICAL *1 ; GAIN_RADICAL *2 ; LOSE_PAIR *2

-- every action carries one label, no action joins the two reactants, and `apply_recipe` applies
each to the structure holding that label. A crash therefore localises to ONE reactant, and pairing
a candidate with a known-safe partner is enough to find it. That is stages 2 and 3, each O(N).
Stage 4 does not take that on faith: it runs the full cross product over the cations and a random
sample of the partners, and if the per-molecule stages were missing a pair-specific crash it turns
up there.

VERDICT. Exit 0 iff no stage crashed. A crash is reported with its exception type, the species, and
which root admitted it -- which is what tells you whether a root has to change.
"""

import argparse
import collections
import logging
import os
import random
import sys
import time
import traceback

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.data.kinetics.depository import KineticsDepository
from rmgpy.data.thermo import ThermoDatabase

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family, FAMILY_ROOT, FAMILY  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.normpath(os.path.join(HERE, '..', '..', 'input'))
UNREP = os.path.normpath(os.path.join(
    FAMILY_ROOT, FAMILY, 'training', 'reactions-unrepresentable.py'))


def hdr(t):
    print('')
    print('=' * 100)
    print(t)
    print('=' * 100)


def key_of(m):
    return '{0}|{1:+d}'.format(m.to_smiles(), m.get_net_charge())


def add(pool, m, source):
    """Deduped insert. First source to name a species keeps the credit."""
    try:
        k = key_of(m)
    except Exception:
        return None
    if k not in pool:
        c = m.copy(deep=True)
        c.clear_labeled_atoms()
        pool[k] = (c, source)
    return k


def load_pool():
    pool = {}
    tdb = ThermoDatabase()
    tdb.load_libraries(os.path.join(INPUT, 'thermo', 'libraries'))
    for name, lib in tdb.libraries.items():
        for e in lib.entries.values():
            item = e.item
            mols = getattr(item, 'molecule', None) or [item]
            if mols:
                add(pool, mols[0], 'thermo/' + name)
    n_thermo = len(pool)

    # Reactants and products are tracked separately on purpose. probe_generate.py drove only the
    # REACTANTS; but a product enters the core and comes back as a reactant on the next iteration,
    # so the product side is an untested surface rather than an already-measured one.
    family = load_family()
    train_r, train_p = [], []
    for e in family.get_training_depository().entries.values():
        for s in e.item.reactants:
            k = add(pool, s.molecule[0], 'training-reactant')
            if k and k not in train_r:
                train_r.append(k)
        for s in e.item.products:
            k = add(pool, s.molecule[0], 'training-product')
            if k and k not in train_p:
                train_p.append(k)

    # The 12 entries this ticket could not represent still name real plasma species, and a real
    # plasma job contains them. They are the honest root-A exposure; the installed libraries are not.
    n_unrep = 0
    if os.path.exists(UNREP):
        dep = KineticsDepository(label='unrepresentable')
        try:
            dep.load(UNREP, KineticsDatabase().local_context, None)
            for e in dep.entries.values():
                for s in list(e.item.reactants) + list(e.item.products):
                    if add(pool, s.molecule[0], 'unrepresentable'):
                        n_unrep += 1
        except Exception as exc:
            print('  !! could not load {0}: {1}'.format(UNREP, exc))
    return family, pool, n_thermo, n_unrep, train_r, train_p


def matches(family, mol, which):
    """Number of labelled-atom mappings of `mol` onto root A (0) or root B (1)."""
    try:
        return len(family._match_reactant_to_template(
            mol, family.forward_template.reactants[which]))
    except Exception:
        return 0


def run(family, probe_mol, partner_mol):
    """Return (n_reactions, exception or None)."""
    try:
        rxns = family.generate_reactions(
            [probe_mol.copy(deep=True), partner_mol.copy(deep=True)])
        return len(rxns), None
    except Exception as exc:
        return 0, exc


def report_crashes(crashes, family, pool):
    if not crashes:
        print('  crashes: 0')
        return
    by_type = collections.Counter(type(e).__name__ for _, e in crashes)
    print('  crashes: {0}   by exception type: {1}'.format(len(crashes), dict(by_type)))
    print('')
    print('  {0:<34} {1:>3} {2:>3}  {3:<20} {4}'.format(
        'species', '*1', '*2', 'exception', 'message (first line)'))
    print('  ' + '-' * 118)
    for k, exc in crashes[:40]:
        mol = pool[k][0]
        msg = str(exc).strip().split('\n')[0][:52]
        print('  {0:<34} {1:>3} {2:>3}  {3:<20} {4}'.format(
            k[:34], matches(family, mol, 0), matches(family, mol, 1),
            type(exc).__name__[:20], msg))
    if len(crashes) > 40:
        print('  ... and {0} more'.format(len(crashes) - 40))
    print('')
    print('  The *1 / *2 columns are the number of labelled-atom mappings the species has onto')
    print('  root A and root B. A non-zero column names the root that admitted it, and therefore')
    print('  the root that would have to change.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0,
                    help='cap the pool (0 = no cap). For timing runs only.')
    ap.add_argument('--sample', type=int, default=400,
                    help='stage 4: how many root-B matchers to draw')
    ap.add_argument('--asample', type=int, default=40,
                    help='stage 4: how many root-A matchers to draw')
    ap.add_argument('--seed', type=int, default=223)
    args = ap.parse_args()

    logging.getLogger().setLevel(logging.CRITICAL)
    print('cwd                 = {0}'.format(os.getcwd()))
    print('engine              = {0}'.format(os.environ.get('RMGPY_ROOT', '(default)')))
    print('database.directory  = {0}'.format(settings['database.directory']))
    print('family loaded from  = {0}'.format(os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('thermo pool from    = {0}'.format(os.path.join(INPUT, 'thermo', 'libraries')))
    print('')
    print('NOTE: database.directory above is the engine rmgrc\'s setting and points at a DIFFERENT')
    print('worktree. This probe never uses it -- both paths above are explicit.')

    t0 = time.time()
    family, pool, n_thermo, n_unrep, train_r, train_p = load_pool()
    print('')
    print('recipe              = {0}'.format([list(a) for a in family.forward_recipe.actions]))
    print('root A (*1)         = {0}'.format(
        family.forward_template.reactants[0].item.to_adjacency_list().strip().replace('\n', ' | ')))
    print('root B (*2)         = {0}'.format(
        family.forward_template.reactants[1].item.to_adjacency_list().strip().replace('\n', ' | ')))
    print('reversible          = {0}'.format(family.reversible))
    print('pool                = {0} distinct species  ({1} from thermo libraries, '
          '+{2} from the unrepresentable set, rest from training) in {3:.1f}s'.format(
              len(pool), n_thermo, n_unrep, time.time() - t0))

    keys = sorted(pool)
    if args.limit:
        # Never drop the family's own species: the fixed safe partners come from there, and a
        # capped run that loses them silently changes what stages 2 and 3 are measuring.
        held = [k for k in keys if pool[k][1].startswith(('training', 'unrepresentable'))]
        rest = [k for k in keys if k not in held]
        random.Random(args.seed).shuffle(rest)
        keys = sorted(set(held) | set(rest[:max(0, args.limit - len(held))]))
        print('pool CAPPED to {0} by --limit (all {1} family species retained); this run is a '
              'timing run, not a verdict.'.format(len(keys), len(held)))

    hdr('PART 1 -- which pool species match which root')
    a_keys, b_keys, charges = [], [], collections.Counter()
    for k in keys:
        mol = pool[k][0]
        charges[mol.get_net_charge()] += 1
        if matches(family, mol, 0):
            a_keys.append(k)
        if matches(family, mol, 1):
            b_keys.append(k)
    print('net charge census   : {0}'.format(dict(sorted(charges.items()))))
    print('match root A (*1)   : {0:>6} of {1}'.format(len(a_keys), len(keys)))
    print('match root B (*2)   : {0:>6} of {1}'.format(len(b_keys), len(keys)))
    print('')
    a_charged = [k for k in a_keys if pool[k][0].get_net_charge() > 0]
    a_neutral = [k for k in a_keys if pool[k][0].get_net_charge() <= 0]
    print('root-A matchers that are actually CATIONS ({0}) -- the intended exposure:'.format(
        len(a_charged)))
    for k in a_charged:
        print('   {0:<34} {1}'.format(k, pool[k][1]))
    print('')
    print('root-A matchers that are NOT cations ({0}). A group constrains ATOMS, not molecular'.format(
        len(a_neutral)))
    print('charge, so any neutral carrying a formally positive atom -- a nitro N, a diazo, an')
    print('N-oxide -- is admitted by a root written to mean "a cation". First 25:')
    for k in a_neutral[:25]:
        print('   {0:<34} {1}'.format(k, pool[k][1]))
    if len(a_neutral) > 25:
        print('   ... and {0} more'.format(len(a_neutral) - 25))
    print('')
    print('{0} species match NEITHER root and can never reach this family.'.format(
        len(keys) - len(set(a_keys) | set(b_keys))))

    # Fixed partners. Both MUST come from the family's own training set, where they are measured
    # crash-free -- a fallback to "whatever matched first" silently makes every stage-2 pair crash
    # on the PARTNER and reports it against the species. That is what the first run of this probe
    # did. Li+ matches root A only; N2 matches root B only; neither is ambiguous.
    safe_cation, safe_neutral = '[Li+]|+1', 'N#N|+0'
    for k in (safe_cation, safe_neutral):
        if k not in pool:
            print('')
            print('ABORT: fixed safe partner {0} is not in the pool. Stages 2 and 3 cannot'.format(k))
            print('attribute a crash without a partner known to be safe.')
            return 2
    print('')
    print('fixed safe cation  (root A partner for stage 2) = {0}  [{1}]  {2}'.format(
        safe_cation, pool[safe_cation][1],
        pool[safe_cation][0].to_adjacency_list().strip().replace('\n', ' | ')))
    print('fixed safe neutral (root B partner for stage 3) = {0}  [{1}]  {2}'.format(
        safe_neutral, pool[safe_neutral][1],
        pool[safe_neutral][0].to_adjacency_list().strip().replace('\n', ' | ')))

    hdr('PART 1b -- self-check on the fixed partners')
    print('Stages 2 and 3 attribute every crash to the varying species. That is only sound if the')
    print('fixed partner never crashes. The control is the training REACTANT pool, which')
    print('probe_generate.py already measured crash-free over all of its own pairs.')
    bad = []
    for fixed in (safe_cation, safe_neutral):
        for k in train_r:
            _, exc = run(family, pool[k][0], pool[fixed][0])
            if exc is not None:
                bad.append((fixed, k, exc))
    print('  training reactants checked per partner : {0}'.format(len(train_r)))
    print('  crashes involving a fixed partner      : {0}'.format(len(bad)))
    for fixed, k, exc in bad[:10]:
        print('     {0} + {1}: {2}'.format(fixed, k, type(exc).__name__))
    if bad:
        print('')
        print('ABORT: a fixed partner crashes on the family\'s own training reactants, so it')
        print('cannot be used to attribute crashes in stages 2 and 3.')
        return 2

    hdr('PART 1c -- feedback safety: the family\'s own PRODUCTS, driven back in as reactants')
    print('probe_generate.py drove the training REACTANTS and measured zero crashes. But RMG puts')
    print('a generated product into the core and hands it back to react() on the next iteration,')
    print('so every product is a future reactant. This stage drives each of the {0} distinct'.format(
        len(train_p)))
    print('training products against the {0} training reactants -- {1} pairs.'.format(
        len(train_r), len(train_p) * len(train_r)))
    print('')
    feedback = []
    print('  {0:<22} {1:>3} {2:>3}  {3}'.format('product species', '*1', '*2', 'result'))
    print('  ' + '-' * 80)
    for pk in sorted(train_p):
        mol = pool[pk][0]
        excs, nrx = [], 0
        for rk in train_r:
            n, exc = run(family, mol, pool[rk][0])
            if exc is not None:
                excs.append((rk, exc))
            else:
                nrx += n
        if excs:
            feedback.append((pk, excs))
        print('  {0:<22} {1:>3} {2:>3}  {3}'.format(
            pk[:22], matches(family, mol, 0), matches(family, mol, 1),
            'CRASHES on {0} of {1} partners ({2})'.format(
                len(excs), len(train_r), type(excs[0][1]).__name__)
            if excs else '{0} reactions, no crash'.format(nrx)))
    print('')
    if feedback:
        print('  {0} of the family\'s own products ABORT the family when fed back in.'.format(
            len(feedback)))
        for pk, excs in feedback:
            print('     {0}: {1}'.format(pk, str(excs[0][1]).strip().split('\n')[0][:88]))
        print('')
        print('  This is not a hypothetical: a product of a training entry is a core species by')
        print('  construction, so an RMG job reaches it on the iteration after it is made.')
    else:
        print('  No product crashes the family when fed back in.')

    hdr('PART 2 -- root B safety: every pool species, paired with the fixed safe cation')
    print('{0} species x 1 partner. A crash here is attributable to the species, because the'.format(
        len(keys)))
    print('partner is known safe and no recipe action joins the two reactants.')
    print('')
    t0 = time.time()
    crashes_b, reacted_b, total_b = [], 0, 0
    for i, k in enumerate(keys):
        n, exc = run(family, pool[k][0], pool[safe_cation][0])
        if exc is not None:
            crashes_b.append((k, exc))
        elif n:
            reacted_b += 1
            total_b += n
        if (i + 1) % 2500 == 0:
            print('   ... {0}/{1} in {2:.0f}s, {3} crashes so far'.format(
                i + 1, len(keys), time.time() - t0, len(crashes_b)))
    print('')
    print('  species that reacted with the fixed cation : {0}'.format(reacted_b))
    print('  reactions generated                        : {0}'.format(total_b))
    report_crashes(crashes_b, family, pool)
    print('')
    print('  elapsed: {0:.0f}s'.format(time.time() - t0))

    hdr('PART 3 -- root A safety: every root-A matcher, paired with the fixed safe neutral')
    crashes_a, reacted_a, total_a = [], 0, 0
    print('{0} species match root A. Pairing each with the fixed neutral is what puts the *1'.format(
        len(a_keys)))
    print('label on it, so this is the stage that exercises root A -- including the {0} that are'.format(
        len(a_neutral)))
    print('not cations at all and that stage 2 only ever saw as the *2 partner.')
    print('')
    t0 = time.time()
    for k in a_keys:
        n, exc = run(family, pool[k][0], pool[safe_neutral][0])
        if exc is not None:
            crashes_a.append((k, exc))
        elif n:
            reacted_a += 1
            total_a += n
    print('  species that reacted with the fixed neutral : {0}'.format(reacted_a))
    print('  reactions generated                         : {0}'.format(total_a))
    report_crashes(crashes_a, family, pool)
    print('')
    print('  of the crashes above, {0} are on molecules with net charge 0 or less'.format(
        sum(1 for k, _ in crashes_a if pool[k][0].get_net_charge() <= 0)))
    print('  elapsed: {0:.0f}s'.format(time.time() - t0))

    hdr('PART 4 -- independence control: full cross product, sampled A-matchers x sampled partners')
    rng = random.Random(args.seed)
    sample = sorted(rng.sample(b_keys, min(args.sample, len(b_keys))))
    a_sample = sorted(rng.sample(a_keys, min(args.asample, len(a_keys))))
    print('The per-molecule stages above rest on the claim that a crash localises to one reactant:')
    print('every recipe action carries one label and none joins the reactants. This stage does not')
    print('assume it: {0} sampled root-A matchers x {1} sampled root-B matchers = {2} pairs, each'.format(
        len(a_sample), len(sample), len(a_sample) * len(sample)))
    print('a real two-reactant call. A crash appearing ONLY here refutes the localisation argument')
    print('and would invalidate stages 2 and 3.')
    print('')
    t0 = time.time()
    crashes_x, total_x, like = [], 0, 0
    for ck in a_sample:
        for bk in sample:
            try:
                rxns = family.generate_reactions(
                    [pool[ck][0].copy(deep=True), pool[bk][0].copy(deep=True)])
            except Exception as exc:
                crashes_x.append(('{0} + {1}'.format(ck, bk), exc))
                continue
            total_x += len(rxns)
            for rx in rxns:
                qs = [(o.molecule[0] if hasattr(o, 'molecule') else o).get_net_charge()
                      for o in rx.reactants]
                if all(q > 0 for q in qs) or all(q < 0 for q in qs):
                    like += 1
    print('  reactions generated        : {0}'.format(total_x))
    print('  like-charge reactant pairs : {0}   (the labelled forbidden groups should hold these'
          ' at 0)'.format(like))
    print('  crashes                    : {0}'.format(len(crashes_x)))
    for label, exc in crashes_x[:20]:
        print('     {0:<60} {1}: {2}'.format(
            label[:60], type(exc).__name__, str(exc).strip().split('\n')[0][:40]))
    crashes_x_new = [c for c in crashes_x
                     if c[0].split(' + ')[0] not in [k for k, _ in crashes_a]
                     and c[0].split(' + ')[1] not in [k for k, _ in crashes_b]]
    print('  crashes NOT explained by a stage 2/3 crash of either reactant : {0}'.format(
        len(crashes_x_new)))
    print('  elapsed: {0:.0f}s'.format(time.time() - t0))

    hdr('SUMMARY')
    n_crash = len(crashes_b) + len(crashes_a) + len(crashes_x) + len(feedback)
    print('  pool                                 : {0} species'.format(len(keys)))
    print('  own products that crash on feedback  : {0}  {1}'.format(
        len(feedback), [k for k, _ in feedback]))
    print('  match root A / root B                : {0} / {1}'.format(len(a_keys), len(b_keys)))
    print('  of the root-A matchers, NOT cations  : {0}'.format(len(a_neutral)))
    print('  stage 2 crashes (root B, per species): {0}'.format(len(crashes_b)))
    print('  stage 3 crashes (root A, per matcher): {0}'.format(len(crashes_a)))
    print('  stage 4 crashes (cross product)      : {0}  ({1} unexplained by stages 2/3)'.format(
        len(crashes_x), len(crashes_x_new)))
    print('  like-charge reactions surviving      : {0}'.format(like))
    print('')
    print('What this probe could NOT reach:')
    print('  - Species RMG GENERATES rather than reads from a library. The pool is every species')
    print('    the installed thermo libraries name; a running job invents more.')
    print('  - Root A over real CATIONS at scale. The installed database holds 4 cations in 78')
    print('    libraries, so the genuine cation exposure is the {0} listed in PART 1 plus the'.format(
        len(a_charged)))
    print('    family\'s own training set, and nothing else.')
    print('  - Reactor admissibility, rates, and anything downstream of generation.')
    print('  - Trimolecular or surface paths. This family is bimolecular and gas phase.')
    print('')
    if n_crash == 0:
        print('VERDICT: no crash, over {0} species. The roots are safe on everything the'.format(
            len(keys)))
        print('installed thermo libraries can name, not merely on the 13 training species.')
        return 0
    print('VERDICT: {0} crashes. The roots are NOT safe outside the training pool; see the'.format(
        n_crash))
    print('per-species tables above for which root admitted each offender.')
    return 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
