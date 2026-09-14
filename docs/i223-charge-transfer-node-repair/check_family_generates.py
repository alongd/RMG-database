#!/usr/bin/env python
# encoding: utf-8
"""
A CHECK THAT WOULD HAVE CAUGHT THE INERT RECIPE. Family-agnostic; run it over any family.

    python check_family_generates.py                 # every family under input/kinetics/families/
    python check_family_generates.py <path> <label>  # one family loaded from an explicit path

WHAT IT ASSERTS.

    A family whose training set describes reactions it cannot generate is broken, and a family
    that generates NOTHING from its own training set is inert.

For each training entry it hands the entry's own reactants to `generate_reactions` and asks
whether anything comes back. Three outcomes per entry: GENERATES (at least one reaction),
NOTHING (zero), or RAISES. A family fails when it generates nothing for EVERY entry -- that is
the inert case, and it is stated that way rather than per-entry because a single entry legitimately
producing nothing is common (a forbidden product, a species the roots exclude on purpose) while a
family producing nothing for all of them cannot be doing its job.

It also reports, separately and without failing on them, entries that RAISE. A raise is worse than
a zero in production -- it aborts the whole job rather than quietly omitting a reaction -- so the
count is surfaced even though a family may have reasons for one.

SECOND ASSERTION, added after I-223 section 13: **a family must survive its own products.**

    For each training entry, the entry's PRODUCTS are driven back in as reactants.

RMG puts a generated product into the core and hands it to react() on the next iteration, so every
product is a future reactant. Plasma_Charge_Transfer passed every check and every reactant-side
probe while N2+ -- which it makes itself, in training entries 15 and 23 -- raised an AtomTypeError
the moment it came back as a reactant. A job would have fired the reaction, then died on the next
iteration. The gap between "safe on its reactants" and "safe" is exactly one RMG iteration wide,
and nothing in the twelve checks is on the product side at all.

This one FAILS the family rather than merely reporting, because unlike a zero there is no benign
reading of it: the family cannot run a job that uses the family.

WHY THE EXISTING SUITE MISSES THIS. `kinetics_check_sample_can_react` is the only one of the twelve
family checks that runs the recipe, and it asserts that `apply_recipe` does not raise, does not
return None, and that resonance generation on the output does not throw. Its own comment is
"# Just check none of this throws errors". It never compares the products to the reactants, so a
recipe that returns its input passes by construction. Nothing else in the suite opens the training
depository except the electron-count check, which returns True immediately for a family declaring
`electrons = 0`.

WHERE THIS CHECK BELONGS, AND WHY IT IS NOT THERE.

It belongs beside the other twelve, in `test/database/databaseTest.py`, as
`kinetics_check_family_generates_its_training_reactions`. **That file is in the RMG-Py repository,
not this one, and this ticket may not modify it.** So the place where it would run automatically
DOES NOT YET EXIST for this repo, and this file is the runnable stand-in: it is a real check with a
real exit code, it just has to be invoked rather than collected. Landing it upstream is a separate
change to a separate repo, and until that happens nothing runs it on its own.
"""

import glob
import os
import sys
import traceback
import logging

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase

MAX_ENTRIES = 25  # enough to prove a family is not inert; keeps H_Abstraction-sized sets cheap


def load(path, label):
    kdb = KineticsDatabase()
    kdb.recommended_families = {}
    kdb.load_families(path, families=[label], depositories=['training'])
    return kdb.families[label]


def bare(species_list):
    mols = []
    for s in species_list:
        m = s.molecule[0].copy(deep=True)
        m.clear_labeled_atoms()
        mols.append(m)
    return mols


def audit(family):
    """Return (generates, nothing, raises, feedback, checked)."""
    try:
        dep = family.get_training_depository()
    except Exception:
        return None
    entries = sorted(dep.entries.values(), key=lambda e: e.index)[:MAX_ENTRIES]
    if not entries:
        return None
    generates = nothing = raises = 0
    feedback = []
    for entry in entries:
        try:
            mols = bare(entry.item.reactants)
        except Exception:
            raises += 1
            continue
        try:
            rxns = family.generate_reactions(mols)
        except Exception:
            raises += 1
            continue
        if rxns:
            generates += 1
        else:
            nothing += 1

        # The product side. A product is a future reactant: RMG adds it to the core and hands it
        # back to react() next iteration. Driven against this entry's own reactants, which are the
        # species guaranteed to be in the core beside it.
        try:
            prods = bare(entry.item.products)
        except Exception:
            continue
        for p in prods:
            for r in mols:
                try:
                    family.generate_reactions([p.copy(deep=True), r.copy(deep=True)])
                except Exception as exc:
                    feedback.append((entry.index, p.to_smiles(), type(exc).__name__))
                    break
    return generates, nothing, raises, feedback, len(entries)


def main():
    logging.getLogger().setLevel(logging.CRITICAL)
    print('database.directory = {0}'.format(settings['database.directory']))

    targets = []
    if len(sys.argv) >= 3:
        targets.append((sys.argv[1], sys.argv[2]))
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        root = os.path.normpath(os.path.join(here, '..', '..', 'input', 'kinetics', 'families'))
        for d in sorted(glob.glob(os.path.join(root, '*'))):
            if os.path.isdir(d) and os.path.exists(os.path.join(d, 'groups.py')):
                targets.append((root, os.path.basename(d)))
        # the held-back family this ticket is about, which is not installed
        held = os.path.normpath(os.path.join(here, '..', 'i154-carry-chemistry', 'held-back'))
        if os.path.isdir(os.path.join(held, 'Plasma_Charge_Transfer')):
            targets.append((held, 'Plasma_Charge_Transfer'))

    print('families to audit  = {0}  (first {1} training entries each)'.format(
        len(targets), MAX_ENTRIES))
    print('')
    row = '{0:<48} {1:>9} {2:>8} {3:>7}  {4}'
    header = row.format('family', 'generates', 'nothing', 'raises', 'verdict')
    print(header)
    print('-' * len(header))

    inert, skipped, ok, raisers, unloadable, feeders = [], [], 0, [], [], []
    for path, label in targets:
        try:
            family = load(path, label)
        except Exception as exc:
            # A load failure is NOT a skip. A family that will not load cannot be audited, and
            # reporting that as "skipped" would let this check pass on a family it never saw --
            # the same shape of hole it exists to close.
            print(row.format(label[:48], '-', '-', '-',
                             'FAIL (will not load: {0})'.format(type(exc).__name__)))
            unloadable.append(label)
            continue
        res = audit(family)
        if res is None:
            print(row.format(label[:48], '-', '-', '-', 'SKIP (no training entries)'))
            skipped.append(label)
            continue
        gen, none_, rais, feedback, n = res
        if gen == 0:
            verdict = 'INERT -- generates nothing from its own training set'
            inert.append(label)
        elif feedback:
            verdict = 'FAIL -- {0} of its own products RAISE when fed back in'.format(
                len(set(f[1] for f in feedback)))
            feeders.append((label, feedback))
        else:
            verdict = 'ok'
            ok += 1
        if rais:
            raisers.append((label, rais))
        print(row.format(label[:48], gen, none_, rais, verdict))

    print('')
    print('audited  : {0}'.format(len(targets) - len(skipped)))
    print('ok       : {0}'.format(ok))
    print('skipped  : {0}  {1}'.format(len(skipped), skipped if len(skipped) < 12 else ''))
    print('INERT    : {0}  {1}'.format(len(inert), inert))
    print('UNLOADABLE: {0}  {1}'.format(len(unloadable), unloadable))
    print('OWN PRODUCT RAISES: {0}  {1}'.format(len(feeders), [f[0] for f in feeders]))
    for label, feedback in feeders:
        for idx, smi, exc in feedback[:6]:
            print('   {0:<40} entry {1}: product {2} -> {3}'.format(label[:40], idx, smi, exc))
    if raisers:
        print('')
        print('Families where at least one training entry made generate_reactions RAISE.')
        print('Not a failure of this check, but a raise aborts a real job rather than omitting a')
        print('reaction, so it is surfaced rather than swallowed:')
        for label, n in raisers:
            print('   {0:<48} {1} entr{2}'.format(label, n, 'y' if n == 1 else 'ies'))

    print('')
    print('What this check does NOT catch:')
    print('  - A family that generates SOME reactions but the wrong products for a given entry.')
    print('    That needs the declared products compared against what the recipe makes, which is')
    print('    probe_producibility.py; this check is the cheap always-on version.')
    print('  - Families with no training set at all. They are skipped, not passed.')
    print('  - Products beyond the FIRST generation. A product of a product is not driven back in.')
    print('  - Anything beyond the first {0} entries of a family.'.format(MAX_ENTRIES))
    print('')
    if unloadable:
        print('VERDICT: {0} famil{1} would not load, so {2} not audited at all.'.format(
            len(unloadable), 'y' if len(unloadable) == 1 else 'ies',
            'it was' if len(unloadable) == 1 else 'they were'))
        return 1
    if inert:
        print('VERDICT: {0} famil{1} generate nothing from their own training reactions.'.format(
            len(inert), 'y' if len(inert) == 1 else 'ies'))
        return 1
    if feeders:
        print('VERDICT: {0} famil{1} on a species {2} produce{3} themselves. A job using'.format(
            len(feeders),
            'y raises' if len(feeders) == 1 else 'ies raise',
            'it' if len(feeders) == 1 else 'they',
            's' if len(feeders) == 1 else ''))
        print('such a family fires the reaction, then dies on the next iteration.')
        return 1
    print('VERDICT: every audited family generates at least one of its own training reactions.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
