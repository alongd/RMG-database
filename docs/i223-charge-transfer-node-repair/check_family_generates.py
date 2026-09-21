#!/usr/bin/env python
# encoding: utf-8
"""
A CHECK THAT WOULD HAVE CAUGHT THE INERT RECIPE. Family-agnostic; run it over any family.

    python check_family_generates.py                 # every family under input/kinetics/families/
    python check_family_generates.py <path> <label>  # one family loaded from an explicit path
    python check_family_generates.py --selftest      # both assertions, against both controls

FOR THE RMG-Py TICKET PICKING THIS UP COLD -- read this block and you can stop reading.

    WHAT IT ASSERTS: two things, both about a family's own training set. (1) A family that
    generates NOTHING from its own training reactants is inert. (2) A family that RAISES on a
    species it produces itself cannot be used, because RMG puts that product in the core and hands
    it back to react() on the next iteration.

    WHERE IT GOES: `test/database/databaseTest.py`, beside the twelve existing family checks, as
    two methods on the same generator -- `kinetics_check_family_generates_its_training_reactions`
    and `kinetics_check_family_survives_its_own_products`. They are two assertions, not one, and
    keeping them separate matters: the first is about a family that does nothing, the second about
    a family that does something and then dies.

    WHAT IT PROVED HERE: run over all 103 families installed in RMG-database, plus the held-back
    family it was written for, every one passes both assertions -- 0 inert, 0 own-product raises.
    So landing it upstream is not expected to turn anything red. Both failing cases are covered by
    the fixtures in `fixtures/`, which are self-contained and carry no dependency on this
    repository; `--selftest` runs them.

    WHY IT IS NOT ALREADY THERE: the ticket that wrote it (I-223, RMG-database) may not modify
    RMG-Py. This file is the runnable stand-in -- a real check with a real exit code that has to be
    invoked rather than collected.

    WHAT IT DOES NOT CATCH: wrong products (that is probe_producibility.py), families with no
    training set at all (skipped, not passed), products of products (only the first generation is
    fed back), and anything past the first MAX_ENTRIES entries of a family.

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

THE CONTROLS. A check is only worth what its failing case proves, and both defects above were
found in a family that has since been repaired -- so the real family can now only ever demonstrate
the passing case. `fixtures/` holds three minimal families, one training entry each, that
demonstrate both failing cases and the passing case, and depend on nothing outside themselves.
`--selftest` asserts each produces its expected verdict.
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


FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')

# Each fixture carries exactly one defect, or none. See fixtures/README.md.
EXPECTED = [
    ('Fixture_Healthy', 'ok',
     'generates its training reaction and survives its own product'),
    ('Fixture_Inert_Recipe', 'inert',
     'charge-only recipe: apply_recipe returns the reactants, so nothing is generated'),
    ('Fixture_Own_Product_Raises', 'feedback',
     'root A says R, so the family raises on the N2+ it makes itself'),
    ('Fixture_Wrong_Products', 'wrong',
     'generates a reaction from every entry, but never the reaction the entry declares'),
    ('Fixture_Unary_Product_Raises', 'feedback',
     'unary family: its product raises only when fed back ALONE, which a two-reactant probe misses'),
]


def bare(species_list):
    mols = []
    for s in species_list:
        m = s.molecule[0].copy(deep=True)
        m.clear_labeled_atoms()
        mols.append(m)
    return mols


def same_set(a, b):
    """Are these two molecule lists the same multiset of species, up to isomorphism?"""
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


def arity(family):
    """How many reactants this family's forward template takes."""
    try:
        return len(family.forward_template.reactants)
    except Exception:
        return 2


def audit(family):
    """Return (reproduces, other, nothing, raises, feedback, checked).

    `reproduces` counts entries for which the family generated the entry's OWN declared reaction.
    `other` counts entries for which it generated something else and nothing matching. Those two
    were one number until round 61 pointed out that "returned a non-empty list" and "generates its
    training reactions" are different claims -- a variant of Plasma_Charge_Transfer scored ok with
    3 of 15 entries generating, where all three products were wrong and no training reaction was
    reproduced at all.
    """
    try:
        dep = family.get_training_depository()
    except Exception:
        return None
    entries = sorted(dep.entries.values(), key=lambda e: e.index)[:MAX_ENTRIES]
    if not entries:
        return None
    n_react = arity(family)
    reproduces = other = nothing = raises = 0
    feedback = []
    for entry in entries:
        try:
            mols = bare(entry.item.reactants)
            declared = bare(entry.item.products)
        except Exception:
            raises += 1
            continue
        try:
            rxns = family.generate_reactions(mols)
        except Exception:
            raises += 1
            continue

        generated = []
        hit = False
        for rx in rxns:
            # BOTH SIDES, and that is not defensive padding. A reaction found in the reverse
            # direction is stored family-forward, so the molecules that were handed in can come
            # back as `rx.products` and the real products as `rx.reactants`. Reading `rx.products`
            # alone made this check report three installed families -- 1,4_Cyclic_birad_scission,
            # Li_Abstraction, Surface_Dissociation_Beta_vdW -- as generating the wrong products,
            # when what it had actually extracted was their own input handed straight back.
            sides = [[(o.molecule[0] if hasattr(o, 'molecule') else o) for o in side]
                     for side in (rx.products, rx.reactants)]
            far = [s for s in sides if not same_set(s, mols)] or [sides[0]]
            generated.extend(far[0])
            if any(same_set(s, declared) for s in sides):
                hit = True
        if hit:
            reproduces += 1
        elif rxns:
            other += 1
        else:
            nothing += 1

        # THE PRODUCT SIDE. A product is a future reactant: RMG adds it to the core and hands it
        # back to react() next iteration.
        #
        # Drive what the family actually MAKES, not only what the entry declares -- round 61's
        # point, and the sharper test, because a family that makes the wrong product will meet
        # that wrong product again next iteration and the declared one never. Declared products
        # are driven too: they are in the core by virtue of being in the training set.
        #
        # And respect the family's ARITY. Feeding two molecules to a unary family matches nothing
        # and returns [] without ever applying the recipe, so the old version reported such a
        # family ok while its real product raised when fed back alone.
        seen = set()
        candidates = []
        for p in generated + declared:
            try:
                k = p.to_smiles()
            except Exception:
                continue
            if k not in seen:
                seen.add(k)
                candidates.append(p)
        for p in candidates:
            if n_react <= 1:
                trials = [[p]]
            else:
                trials = [[p] + [r] * (n_react - 1) for r in mols]
            for trial in trials:
                try:
                    family.generate_reactions([m.copy(deep=True) for m in trial])
                except Exception as exc:
                    feedback.append((entry.index, p.to_smiles(), type(exc).__name__))
                    break
    return reproduces, other, nothing, raises, feedback, len(entries)


def classify(path, label):
    """The check's verdict for one family: one of unloadable/skip/inert/feedback/ok."""
    try:
        family = load(path, label)
    except Exception as exc:
        return 'unloadable', type(exc).__name__, None
    res = audit(family)
    if res is None:
        return 'skip', 'no training entries', None
    rep, other, none_, rais, feedback, n = res
    if rep == 0 and other == 0:
        return 'inert', '{0} of {1} entries generated nothing'.format(none_, n), res
    if rep == 0:
        return 'wrong', '{0} of {1} entries generate, none reproducing its own reaction'.format(
            other, n), res
    if feedback:
        return 'feedback', '; '.join(
            'entry {0}: {1} -> {2}'.format(*f) for f in feedback[:3]), res
    return 'ok', '{0} of {1} entries reproduce their own reaction'.format(rep, n), res


def selftest():
    """Both assertions, against both of their controls. Exits 0 only if every fixture matches."""
    print('SELFTEST -- the check against the fixtures in {0}'.format(FIXTURES))
    print('')
    print('A check is worth what its FAILING case proves. Both defects below were found in a real')
    print('family that has since been repaired, so the real family can now only demonstrate the')
    print('passing case; these fixtures hold the failing ones. See fixtures/README.md.')
    print('')
    if not os.path.isdir(FIXTURES):
        print('FAIL: {0} does not exist. The controls are missing, so this run proves'.format(
            FIXTURES))
        print('nothing about the check.')
        return 2
    row = '{0:<32} {1:<10} {2:<10} {3}'
    header = row.format('fixture', 'expected', 'got', 'detail')
    print(header)
    print('-' * (len(header) + 30))
    bad = []
    for label, expected, why in EXPECTED:
        got, detail, _ = classify(FIXTURES, label)
        print(row.format(label[:32], expected, got,
                         detail if got == expected else '*** MISMATCH *** ' + detail))
        print(row.format('', '', '', 'why: ' + why))
        if got != expected:
            bad.append((label, expected, got))
    print('')
    if bad:
        print('SELFTEST FAILED. The check did not behave as its own fixtures say it must:')
        for label, expected, got in bad:
            print('   {0}: expected {1}, got {2}'.format(label, expected, got))
        print('Until this passes, a green run of the check over real families means nothing.')
        return 1
    print('SELFTEST PASSED. Both assertions fire on their own control and stay quiet on the')
    print('healthy fixture, so a green run over real families is evidence.')
    return 0


def main():
    logging.getLogger().setLevel(logging.CRITICAL)
    if '--selftest' in sys.argv[1:]:
        return selftest()

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

    # PRINT THE PATHS ACTUALLY LOADED, not settings['database.directory'].
    #
    # This used to open by printing `database.directory` from rmgpy.settings, which is whatever
    # the engine worktree's rmgrc says and has nothing to do with what this script loads -- main()
    # resolves every target from __file__ and load() passes that path explicitly. The committed
    # sweep log therefore opened by naming a database that does not contain Plasma_Charge_Transfer
    # at all, while correctly auditing this tree, and run.sh tells its reader to check exactly
    # that line before trusting anything. The result was right and the only line a reader was told
    # to check was wrong.
    print('families to audit  = {0}  (first {1} training entries each)'.format(
        len(targets), MAX_ENTRIES))
    for p in sorted({t[0] for t in targets}):
        print('  loaded from      : {0}   ({1} famil{2})'.format(
            p, sum(1 for t in targets if t[0] == p),
            'y' if sum(1 for t in targets if t[0] == p) == 1 else 'ies'))
    print('  rmgpy settings database.directory = {0}'.format(settings['database.directory']))
    print('    ^ NOT used by this script. Shown only so the difference is visible rather than')
    print('      silent; the paths above are the ones that were read.')
    print('')
    row = '{0:<44} {1:>10} {2:>7} {3:>8} {4:>7}  {5}'
    header = row.format('family', 'reproduces', 'other', 'nothing', 'raises', 'verdict')
    print(header)
    print('-' * len(header))
    print('"reproduces" = entries whose OWN declared reaction the family generated.')
    print('"other"      = entries where it generated something, but never that reaction.')
    print('')

    inert, skipped, ok, raisers, unloadable, feeders, wrongs = [], [], 0, [], [], [], []
    for path, label in targets:
        try:
            family = load(path, label)
        except Exception as exc:
            # A load failure is NOT a skip. A family that will not load cannot be audited, and
            # reporting that as "skipped" would let this check pass on a family it never saw --
            # the same shape of hole it exists to close.
            print(row.format(label[:44], '-', '-', '-', '-',
                             'FAIL (will not load: {0})'.format(type(exc).__name__)))
            unloadable.append(label)
            continue
        verdict_key, detail, res = classify(path, label)
        if res is None:
            print(row.format(label[:44], '-', '-', '-', '-', 'SKIP (no training entries)'))
            skipped.append(label)
            continue
        rep, other, none_, rais, feedback, n = res
        if verdict_key == 'inert':
            verdict = 'INERT -- generates nothing from its own training set'
            inert.append(label)
        elif verdict_key == 'wrong':
            verdict = 'FAIL -- generates, but reproduces NONE of its own reactions'
            wrongs.append(label)
        elif verdict_key == 'feedback':
            verdict = 'FAIL -- {0} of its own products RAISE when fed back in'.format(
                len(set(f[1] for f in feedback)))
            feeders.append((label, feedback))
        else:
            verdict = 'ok'
            ok += 1
        if rais:
            raisers.append((label, rais))
        print(row.format(label[:44], rep, other, none_, rais, verdict))

    print('')
    print('audited  : {0}'.format(len(targets) - len(skipped)))
    print('ok       : {0}'.format(ok))
    print('skipped  : {0}  {1}'.format(len(skipped), skipped if len(skipped) < 12 else ''))
    print('INERT    : {0}  {1}'.format(len(inert), inert))
    print('WRONG    : {0}  {1}   (generate, but reproduce none of their own)'.format(
        len(wrongs), wrongs))
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
    print('  - A family that reproduces SOME of its entries and gets others wrong. It fails only')
    print('    when NOT ONE entry is reproduced; the per-entry breakdown is probe_producibility.py.')
    print('  - Families with no training set at all. They are skipped, not passed.')
    print('  - Products beyond the FIRST generation. A product of a product is not driven back in.')
    print('  - Anything beyond the first {0} entries of a family.'.format(MAX_ENTRIES))
    print('  - Whether the RATE attached to a reproduced reaction is right. Reproduction here is')
    print('    structural: the generated products are isomorphic to the declared ones.')
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
    if wrongs:
        print('VERDICT: {0} famil{1} reactions from their own training reactants but'.format(
            len(wrongs), 'y generates' if len(wrongs) == 1 else 'ies generate'))
        print('reproduce NONE of their own training reactions. Generating something is not the')
        print('same as generating the right thing.')
        return 1
    if feeders:
        print('VERDICT: {0} famil{1} on a species {2} produce{3} themselves. A job using'.format(
            len(feeders),
            'y raises' if len(feeders) == 1 else 'ies raise',
            'it' if len(feeders) == 1 else 'they',
            's' if len(feeders) == 1 else ''))
        print('such a family fires the reaction, then dies on the next iteration.')
        return 1
    print('VERDICT: every audited family reproduced at least one of its own training reactions')
    print('with the products that entry declares, and none raised on a species it produces.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
