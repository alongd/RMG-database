#!/usr/bin/env python
# encoding: utf-8
"""
I-223 step 6: can this family's recipe actually MAKE each training reaction's declared products?

WHY THIS PROBE EXISTS.

`add_rules_from_training` turns every training entry into a rate rule keyed on
`get_reaction_template(entry.item)`.  That function descends the tree using the LABELLED ATOMS
OF THE REACTANTS only (family.py:2599 -> KineticsGroups.get_reaction_template); it never looks at
`reaction.products`.  So a training entry whose products the recipe cannot generate still yields a
rule, silently, and none of the twelve family checks notices:

  - kinetics_check_sample_can_react applies the recipe to GROUP SAMPLES and only requires that it
    return the right NUMBER of structures -- not that it changed anything;
  - kinetics_check_training_reactions_are_balanced checks stoichiometry, which products identical
    to the reactants satisfy perfectly;
  - the remaining ten are tree-shape checks and never touch the training depository.

Training entry 2 (`H2p_r1 + H-_r2 <=> H2 + H`) was found to be in that defect class by I-223, and
found only by going looking at it specifically.  The other 26 entries had never been audited this
way.  This probe audits all 27, by construction rather than by inspection.

WHAT THIS PROBE FOUND, and why it is bigger than the question it was sent to answer.

The recipe is charge-only:

    recipe(actions=[['LOSE_CHARGE', '*1', 1], ['GAIN_CHARGE', '*2', 1]])

`Atom.decrement_charge` / `increment_charge` change `atom.charge` AND NOTHING ELSE
(molecule.py:538-548).  `apply_recipe` then calls `struct.update_charge()` on every product
structure (family.py:1547), and `Atom.update_charge` re-derives the charge from the structure:

    charge = valence_electrons - bond_order - radical_electrons - 2 * lone_pairs      (molecule.py:596-598)

The recipe left bond order, radicals and lone pairs untouched, so that line puts the charge back
exactly where it was.  The products come out isomorphic to the reactants, and `_create_reaction`
rejects reactions whose products are the same species as their reactants (family.py:1757-1759).

**The family therefore generates no reactions at all.**  It is not that 26 entries have the wrong
products; it is that the recipe is a no-op and every entry's "products" are its own reactants.
That is measured three independent ways below (PART 0), not argued.

This is a defect in the FAMILY, not in RMG.  Part 0's census parses every recipe under
`input/kinetics/families/` and finds that all 20 mainline families using a charge action pair it
with a structural action -- a radical change, a lone-pair change, or a bond change -- that moves
the valence electron count the charge is derived from.  `Plasma_Charge_Transfer` is the only
recipe in the repository consisting of charge actions and nothing else.

WHAT THIS PROBE DELIBERATELY DOES NOT DO.

It does not fix the recipe.  PART 3 measures what each entry would need instead, and the answer is
that the required action set is NOT the same for all of them -- Ar+ -> Ar moves a radical into a
lone pair, O+ -> O does not, and NO+ -> NO changes a bond order, which no single-atom action can
express.  Choosing among "one recipe with more actions", "several families", and "these reactions
are not a family at all" is a chemistry decision, and the contract routes chemistry decisions that
cannot be sourced to the owner rather than guessing them.
"""

import glob
import logging
import os
import re
import sys
import traceback

from rmgpy import settings
from rmgpy.molecule.molecule import Molecule

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family  # noqa: E402

DB_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
FAMILIES_GLOB = os.path.join(DB_ROOT, 'input', 'kinetics', 'families', '*', 'groups.py')

CHARGE_ACTIONS = {'LOSE_CHARGE', 'GAIN_CHARGE'}
# Actions that move the quantity update_charge derives the charge FROM. Any one of them makes a
# charge action stick; a recipe with none of them cannot change a charge at all.
STRUCTURAL_ACTIONS = {'GAIN_RADICAL', 'LOSE_RADICAL', 'GAIN_PAIR', 'LOSE_PAIR',
                      'FORM_BOND', 'BREAK_BOND', 'CHANGE_BOND'}

# The three reactant pairs used for the minimal demonstration in PART 0, chosen to span the cases:
# a bare alkali cation, an open-shell main-group cation, and a rare gas cation with a full shell.
DEMO = {
    'Li+ + H-   (entry 24)': ('1 *1 Li u0 p0 c+1\n',
                              '1 *2 H u0 p1 c-1\n'),
    'O+ + O     (entry 13 partner)': ('1 *1 O u1 p2 c+1\n',
                                      'multiplicity 3\n1 *2 O u2 p2 c0\n'),
    'Ar+ + N2   (entry 19)': ('1 *1 Ar u1 p3 c+1\n',
                              '1 *2 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}\n'),
}


def totals(mol):
    """(net charge, radicals, lone pairs, total bond order) -- the four quantities update_charge
    balances against each other."""
    order = 0.0
    for atom in mol.atoms:
        for bond in mol.get_bonds(atom).values():
            order += bond.get_order_num()
    return (mol.get_net_charge(),
            sum(a.radical_electrons for a in mol.atoms),
            sum(a.lone_pairs for a in mol.atoms),
            order / 2.0)


def describe(structures):
    out = []
    for s in structures:
        try:
            txt = s.to_smiles()
        except Exception:
            txt = s.to_adjacency_list().strip().replace('\n', ' | ')
        try:
            txt += ' ({0:+d})'.format(s.get_net_charge())
        except Exception:
            pass
        out.append(txt)
    return ' + '.join(out)


def same_set(a, b):
    if len(a) != len(b):
        return False
    remaining = list(b)
    for x in a:
        for i, y in enumerate(remaining):
            try:
                if x.is_isomorphic(y):
                    remaining.pop(i)
                    break
            except Exception:
                continue
        else:
            return False
    return True


def hdr(t):
    print('')
    print('=' * 100)
    print(t)
    print('=' * 100)


def mols(species_list):
    return [s.molecule[0] for s in species_list]


def implied_actions(label, dq, drad, dlp, dbond):
    """The actions that WOULD be needed on one labelled atom to get from reactant to product."""
    acts = []
    if dbond:
        acts.append('CHANGE_BOND({0:+g})'.format(dbond))
    if drad:
        acts.append('{0}_RADICAL {1}'.format('GAIN' if drad > 0 else 'LOSE', abs(drad)))
    if dlp:
        acts.append('{0}_PAIR {1}'.format('GAIN' if dlp > 0 else 'LOSE', abs(dlp)))
    if dq:
        acts.append('{0}_CHARGE {1}'.format('GAIN' if dq > 0 else 'LOSE', abs(dq)))
    return ' + '.join(acts) if acts else '(nothing)'


def census():
    """Parse every mainline recipe; classify those that use a charge action. Computed, not asserted."""
    bare, paired = [], []
    for path in sorted(glob.glob(FAMILIES_GLOB)):
        try:
            txt = open(path).read()
        except Exception:
            continue
        m = re.search(r'recipe\(actions=\[(.*?)\n\]\)', txt, re.S)
        if not m:
            continue
        acts = re.findall(r"\[\s*'(\w+)'", m.group(1))
        if not set(acts) & CHARGE_ACTIONS:
            continue
        name = os.path.basename(os.path.dirname(path))
        (paired if set(acts) & STRUCTURAL_ACTIONS else bare).append((name, acts))
    return bare, paired


def pair_by_formula(reactant, products, used):
    """Charge transfer conserves atoms per fragment, so each reactant species has exactly one
    product species of the same formula. Returns (product, ambiguous_flag)."""
    f = reactant.get_formula()
    candidates = [i for i, p in enumerate(products) if p.get_formula() == f and i not in used]
    if not candidates:
        return None, False
    ambiguous = False
    if len(candidates) > 1:
        # Only a real ambiguity if the candidates differ from one another.
        first = products[candidates[0]]
        ambiguous = not all(first.is_isomorphic(products[i]) for i in candidates[1:])
    used.add(candidates[0])
    return products[candidates[0]], ambiguous


def main():
    print('cwd                 = {0}'.format(os.getcwd()))
    print('database.directory  = {0}'.format(settings['database.directory']))
    print('family loaded from  = Plasma_Charge_Transfer under docs/i154-carry-chemistry/held-back')

    logging.getLogger().setLevel(logging.ERROR)
    family = load_family()

    actions = [list(a) for a in family.forward_recipe.actions]
    print('recipe              = {0}'.format(actions))
    print('template            = {0} -> {1}'.format(
        [e.label for e in family.forward_template.reactants],
        [e.label for e in family.forward_template.products]))

    hdr('PART 0 -- is the recipe capable of moving a charge at all? Three independent measurements.')
    print('Mechanism, read from source: LOSE_CHARGE/GAIN_CHARGE set atom.charge and nothing else')
    print('(molecule.py:538-548); apply_recipe then calls update_charge() on every product')
    print('(family.py:1547); update_charge re-derives charge = valence - bonds - radicals - 2*lp')
    print('(molecule.py:596-598). Nothing on the right-hand side was touched, so the charge returns')
    print('to its starting value. Below: whether that is what actually happens.')

    print('')
    print('(0a) apply the recipe by hand to three representative reactant pairs')
    print('')
    inert = 0
    for name, (a, b) in DEMO.items():
        ma = Molecule().from_adjacency_list(a)
        mb = Molecule().from_adjacency_list(b)
        made = family.apply_recipe([ma.copy(deep=True), mb.copy(deep=True)])
        if made is None:
            print('  {0:<30} apply_recipe -> None'.format(name))
            continue
        unchanged = same_set(made, [ma, mb])
        inert += 1 if unchanged else 0
        print('  {0:<30} in  {1}'.format(name, describe([ma, mb])))
        print('  {0:<30} out {1}   {2}'.format(
            '', describe(made), 'IDENTICAL -- no charge moved' if unchanged else 'changed'))
    print('')
    print('  {0} of {1} demonstration pairs came back unchanged.'.format(inert, len(DEMO)))

    print('')
    print('(0b) ask the family to generate reactions for those same reactants')
    print('     _create_reaction rejects a reaction whose products are its reactants')
    print('     (family.py:1757-1759), so an inert recipe shows up here as zero.')
    print('')
    for name, (a, b) in DEMO.items():
        ma = Molecule().from_adjacency_list(a)
        mb = Molecule().from_adjacency_list(b)
        ma.clear_labeled_atoms()
        mb.clear_labeled_atoms()
        try:
            rxns = family.generate_reactions([ma, mb])
            print('  {0:<30} generate_reactions -> {1} reaction(s)'.format(name, len(rxns)))
        except Exception as exc:
            print('  {0:<30} generate_reactions RAISED {1}'.format(name, type(exc).__name__))

    print('')
    print('(0c) census of every recipe under input/kinetics/families/ that uses a charge action.')
    print('     Parsed on each run rather than quoted, so it cannot drift from the repo.')
    print('')
    bare, paired = census()
    print('  families whose recipe uses LOSE_CHARGE or GAIN_CHARGE   : {0}'.format(
        len(bare) + len(paired)))
    print('  ... paired with a structural action (radical/pair/bond) : {0}'.format(len(paired)))
    print('  ... charge actions ONLY, nothing structural             : {0}'.format(len(bare)))
    for name, acts in bare:
        print('        {0}: {1}'.format(name, acts))
    print('')
    print('  this family: {0}'.format([a[0] for a in actions]))
    print('  -> {0}'.format(
        'charge actions only; no mainline family does this'
        if not (set(a[0] for a in actions) & STRUCTURAL_ACTIONS)
        else 'contains a structural action'))

    dep = family.get_training_depository()
    entries = sorted(dep.entries.values(), key=lambda e: e.index)

    hdr('PART 1 -- every training entry. 27 of them, none exempt.')
    print('"template" is what add_rules_from_training keys the rule on -- reactant side only, so')
    print('the rule is created regardless of anything in this table.')
    print('')
    row = '{0:>4}  {1:<34} {2:<26} {3:<10} {4}'
    header = row.format('idx', 'reaction', 'rule keyed on', 'verdict', 'what the recipe returns')
    print(header)
    print('-' * len(header))

    results = {}
    for entry in entries:
        reactants = mols(entry.item.reactants)
        products = mols(entry.item.products)
        try:
            tlabels = '[{0}]'.format(';'.join(g.label for g in family.get_reaction_template(entry.item)))
        except Exception as exc:
            tlabels = '!! ' + type(exc).__name__
        try:
            made = family.apply_recipe([m.copy(deep=True) for m in reactants])
        except Exception as exc:
            made, desc = None, 'RAISED {0}'.format(type(exc).__name__)
        else:
            desc = 'None (product count != 2)' if made is None else describe(made)

        if made is None:
            verdict = 'NO OUTPUT'
        elif same_set(made, reactants):
            verdict = 'INERT'
        elif same_set(made, products):
            verdict = 'PRODUCIBLE'
        else:
            verdict = 'WRONG'
        results[entry.index] = (entry, tlabels, verdict, desc)
        print(row.format(entry.index, entry.label[:34], tlabels[:26], verdict, desc[:46]))

    verdicts = {}
    for _, _, v, _ in results.values():
        verdicts[v] = verdicts.get(v, 0) + 1

    hdr('PART 2 -- what the recipe would have to do instead, per entry.')
    print('For each side, the change between the reactant species and the product species of the')
    print('same formula, in the four quantities update_charge balances. The rightmost column is the')
    print('action set that change implies. If those action sets are not all the same, one recipe')
    print('cannot serve this training set.')
    print('')
    r2 = '{0:>4}  {1:<12} {2:<34}  {3:<12} {4}'
    h2 = r2.format('idx', 'side', 'required actions', 'd(rad,lp,bond)', 'species')
    print(h2)
    print('-' * len(h2))

    cation_sets, neutral_sets, bond_movers, ambiguous = {}, {}, [], []
    for entry in entries:
        reactants = mols(entry.item.reactants)
        products = mols(entry.item.products)
        used = set()
        for reactant in reactants:
            product, amb = pair_by_formula(reactant, products, used)
            if product is None:
                print(r2.format(entry.index, '?', 'no product of matching formula', '--',
                                reactant.to_smiles()))
                continue
            if amb:
                ambiguous.append(entry.index)
            q0, rad0, lp0, b0 = totals(reactant)
            q1, rad1, lp1, b1 = totals(product)
            dq, drad, dlp, dbond = q1 - q0, rad1 - rad0, lp1 - lp0, b1 - b0
            side = 'cation *1' if q0 > 0 else ('anion *2' if q0 < 0 else 'neutral *2')
            acts = implied_actions(side, dq, drad, dlp, dbond)
            if dbond:
                bond_movers.append(entry.index)
            bucket = cation_sets if q0 > 0 else neutral_sets
            bucket.setdefault(acts, []).append(entry.index)
            print(r2.format(entry.index, side, acts,
                            '({0:+g},{1:+g},{2:+g})'.format(drad, dlp, dbond),
                            '{0} -> {1}'.format(reactant.to_smiles(), product.to_smiles())))

    hdr('PART 3 -- how many distinct recipes would the 27 entries need?')
    print('cation side (*1), distinct action sets: {0}'.format(len(cation_sets)))
    for acts, idxs in sorted(cation_sets.items(), key=lambda kv: -len(kv[1])):
        print('  {0:<40} entries {1}'.format(acts, sorted(set(idxs))))
    print('')
    print('partner side (*2), distinct action sets: {0}'.format(len(neutral_sets)))
    for acts, idxs in sorted(neutral_sets.items(), key=lambda kv: -len(kv[1])):
        print('  {0:<40} entries {1}'.format(acts, sorted(set(idxs))))
    print('')
    if bond_movers:
        print('Entries needing a BOND-ORDER change: {0}'.format(sorted(set(bond_movers))))
        print('  No single-atom action can express one. CHANGE_BOND takes two labelled atoms, so')
        print('  these entries would need a second label on the partner atom, which the present')
        print('  two-label template does not have.')
    if ambiguous:
        print('Formula pairing ambiguous (two non-isomorphic products share a formula): {0}'.format(
            sorted(set(ambiguous))))

    hdr('SUMMARY')
    print('  training entries audited                 : {0}'.format(len(results)))
    for v in ('PRODUCIBLE', 'INERT', 'WRONG', 'NO OUTPUT'):
        if v in verdicts:
            print('  {0:<40} : {1}'.format(v, verdicts[v]))
    print('  distinct recipes the training set needs  : cation side {0}, partner side {1}'.format(
        len(cation_sets), len(neutral_sets)))
    print('  mainline families with a bare charge recipe: {0}'.format(len(bare)))
    print('')
    print('What this probe could NOT reach:')
    print('  - The REVERSE family. groups.py declares reverse = "Plasma_Charge_Transfer_Reverse"')
    print('    and own_reverse is False, so the reverse object is a separate family that does not')
    print('    exist in this repository. Whether it has the same defect is unmeasured here.')
    print('  - Whether any RMG job has ever RUN this family. The finding is that it generates no')
    print('    reactions; that it was never noticed is consistent with it never having been run,')
    print('    but this probe cannot establish that.')
    print('  - The rates themselves. Those are the source audits (probe_tanarro.py,')
    print('    probe_ozawa_aiken.py), and they are unaffected: a rate can be correctly transcribed')
    print('    for a reaction the family cannot generate.')
    print('  - The right repair. PART 3 measures what would be needed; it does not choose.')
    print('')

    if verdicts.get('PRODUCIBLE', 0) == len(results):
        print('VERDICT: every training entry is producible.')
        return 0
    print('VERDICT: {0} of {1} training entries are not producible by this recipe, and the reason is'.format(
        len(results) - verdicts.get('PRODUCIBLE', 0), len(results)))
    print('not per-entry: the recipe is inert. It returns its reactants, so the family generates no')
    print('reactions at all. No check in the twelve-check suite reports this. STOPPING here rather')
    print('than repairing it -- PART 3 shows the repair is a family redesign, not a correction.')
    return 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
