#!/usr/bin/env python
# encoding: utf-8
"""
I-223 follow-up: can RMG's recipe grammar express "one electron moves from *2 to *1" at all?

The previous probe (probe_producibility.py) established that this family's charge-only recipe is
inert and the family generates zero reactions. This one asks the question that decides whether the
family can exist: is there a recipe -- ANY recipe in the nine-action grammar -- that realises
charge transfer for every structure the templates admit?

HOW THE GRAMMAR ACTUALLY WORKS, established here rather than assumed.

An atom's charge is DERIVED, not stored: `update_charge` computes
    charge = valence_electrons - bond_order - radical_electrons - 2 * lone_pairs
so "one electron arrives at this atom" means the right-hand side must fall by exactly one. PART 1
measures what each of the nine actions does to that quantity, by applying it to a probe atom and
reading the derived charge back, and reports how many labelled atoms each action needs.

The consequence, which PART 1 measures rather than argues: LOSE_CHARGE and GAIN_CHARGE move ZERO
electrons -- they set a field that is immediately recomputed -- and every recipe that really moves
an electron does so with radical, lone-pair or bond actions, with no charge action present at all.

THE FOUR CANDIDATE RECIPES.

Moving exactly one electron ONTO *1 can be done two ways, and only two:
    A1  GAIN_RADICAL *1            the electron stays unpaired      (needs room for a radical)
    A2  LOSE_RADICAL *1 + GAIN_PAIR *1   the electron pairs up      (needs an existing radical)
Taking exactly one electron OFF *2, likewise:
    B1  LOSE_RADICAL *2                  an unpaired electron leaves (needs an existing radical)
    B2  GAIN_RADICAL *2 + LOSE_PAIR *2   a pair is broken            (needs an existing lone pair)
GAIN_PAIR/LOSE_PAIR alone move TWO electrons, so neither can serve on its own; bond actions move an
electron onto two atoms at once and need a second label. That is the whole space for a two-label
template, and PART 2 runs all four combinations against all 27 training entries.

WHY THIS IS NOT A MATTER OF TASTE. The wrong choice does not merely produce a different molecule --
`LOSE_RADICAL` on a closed-shell atom RAISES `ActionError`, because radical counts cannot go
negative. So a single recipe is not something one can settle by picking a convention.
"""

import glob
import os
import re
import sys
import traceback

from rmgpy import settings
from rmgpy.data.kinetics.family import ReactionRecipe
from rmgpy.molecule.molecule import Molecule

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from probe_nodes import load_family  # noqa: E402

DB_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
FAMILIES_GLOB = os.path.join(DB_ROOT, 'input', 'kinetics', 'families', '*', 'groups.py')
ENGINE = os.environ.get('RMGPY_ROOT', '/home/alon/Code/RMG-Py-plasma')
FAMILY_PY = os.path.join(ENGINE, 'rmgpy', 'data', 'kinetics', 'family.py')

CHARGE_ACTIONS = {'LOSE_CHARGE', 'GAIN_CHARGE'}
STRUCTURAL_ACTIONS = {'GAIN_RADICAL', 'LOSE_RADICAL', 'GAIN_PAIR', 'LOSE_PAIR',
                      'FORM_BOND', 'BREAK_BOND', 'CHANGE_BOND'}

# One electron onto *1; one electron off *2. Named so the matrix in PART 2 stays readable.
ACCEPT = {
    'A1 GAIN_RADICAL': [['GAIN_RADICAL', '*1', 1]],
    'A2 LOSE_RAD+GAIN_PAIR': [['LOSE_RADICAL', '*1', 1], ['GAIN_PAIR', '*1', 1]],
}
DONATE = {
    'B1 LOSE_RADICAL': [['LOSE_RADICAL', '*2', 1]],
    'B2 GAIN_RAD+LOSE_PAIR': [['GAIN_RADICAL', '*2', 1], ['LOSE_PAIR', '*2', 1]],
}
CONTROL = ('as shipped (charge-only)', [['LOSE_CHARGE', '*1', 1], ['GAIN_CHARGE', '*2', 1]])

DEMO = {
    'Li+ + H-': ('1 *1 Li u0 p0 c+1\n', '1 *2 H u0 p1 c-1\n'),
    'O+ + O': ('1 *1 O u1 p2 c+1\n', 'multiplicity 3\n1 *2 O u2 p2 c0\n'),
    'Ar+ + N2': ('1 *1 Ar u1 p3 c+1\n', '1 *2 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}\n'),
}

# Probe atoms for PART 1: one closed-shell-ish, one with a radical and a spare lone pair, so that
# every action's precondition is satisfiable by at least one of them.
PROBE_ATOMS = {
    'O  u2 p2 c0': 'multiplicity 3\n1 *1 O u2 p2 c0\n2    O u2 p2 c0\n',
}


def hdr(t):
    print('')
    print('=' * 100)
    print(t)
    print('=' * 100)


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


def mols(species_list):
    return [s.molecule[0] for s in species_list]


def make_recipe(actions):
    r = ReactionRecipe()
    for a in actions:
        r.add_action(list(a))
    return r


def run_recipe(family, actions, reactants):
    """Apply an arbitrary candidate recipe through the family's own apply_recipe.
    Returns (products or None, error string or None). The family object is restored."""
    saved = family.forward_recipe
    family.forward_recipe = make_recipe(actions)
    try:
        out = family.apply_recipe([m.copy(deep=True) for m in reactants])
        return out, None
    except Exception as exc:
        return None, '{0}: {1}'.format(type(exc).__name__, str(exc).split('\n')[0][:58])
    finally:
        family.forward_recipe = saved


def valid_actions_from_source():
    """Read the authoritative action list out of the engine rather than quoting it."""
    try:
        txt = open(FAMILY_PY).read()
    except Exception:
        return None
    m = re.search(r'valid_actions\s*=\s*\[(.*?)\]', txt, re.S)
    if not m:
        return None
    return re.findall(r"'(\w+)'", m.group(1))


def census():
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


def measure_action_effects():
    """For each action in the grammar, MEASURE the change in derived charge it causes, by applying
    it to a probe molecule and reading update_charge back. Returns list of rows."""
    singles = [
        ('GAIN_RADICAL', [['GAIN_RADICAL', '*1', 1]], 1),
        ('LOSE_RADICAL', [['LOSE_RADICAL', '*1', 1]], 1),
        ('GAIN_PAIR', [['GAIN_PAIR', '*1', 1]], 1),
        ('LOSE_PAIR', [['LOSE_PAIR', '*1', 1]], 1),
        ('GAIN_CHARGE', [['GAIN_CHARGE', '*1', 1]], 1),
        ('LOSE_CHARGE', [['LOSE_CHARGE', '*1', 1]], 1),
        ('CHANGE_BOND(+1)', [['CHANGE_BOND', '*1', 1, '*2']], 2),
        ('BREAK_BOND', [['BREAK_BOND', '*1', 1, '*2']], 2),
        ('FORM_BOND', [['FORM_BOND', '*1', 1, '*2']], 2),
    ]
    # Probe structures chosen so every action's precondition holds: *1 carries a radical (so
    # LOSE_RADICAL is possible), lone pairs (so LOSE_PAIR is), and room for more of each.
    # Singly-bonded O-O biradical for the bond actions; two triplet O atoms for FORM_BOND.
    base_two_atom = 'multiplicity 3\n1 *1 O u1 p2 c0 {2,S}\n2 *2 O u1 p2 c0 {1,S}\n'
    base_unbonded = 'multiplicity 5\n1 *1 O u2 p2 c0\n2 *2 O u2 p2 c0\n'
    rows = []
    for name, actions, nlabels in singles:
        adj = base_unbonded if name == 'FORM_BOND' else base_two_atom
        m = Molecule().from_adjacency_list(adj)
        before = m.atoms[0].charge
        recipe = make_recipe(actions)
        try:
            recipe.apply_forward(m, unique=True)
            m.update_charge()
            after = m.atoms[0].charge
            delta_q = after - before
            note = 'moves {0:+d} electron(s) onto *1'.format(-delta_q) if delta_q else 'moves NO electron'
            rows.append((name, nlabels, '{0:+d}'.format(delta_q), note))
        except Exception as exc:
            rows.append((name, nlabels, '--', 'raised {0}'.format(type(exc).__name__)))
    return rows


def main():
    print('cwd                 = {0}'.format(os.getcwd()))
    print('engine              = {0}'.format(ENGINE))
    print('database.directory  = {0}'.format(settings['database.directory']))

    family = load_family()
    print('family loaded from  = docs/i154-carry-chemistry/held-back/Plasma_Charge_Transfer')
    print('shipped recipe      = {0}'.format([list(a) for a in family.forward_recipe.actions]))

    # ------------------------------------------------------------------ PART 0
    hdr('PART 0 -- reproduce the two prior numbers on THIS engine, as my own measurements.')
    print('(0a) the shipped recipe, applied by hand')
    inert = 0
    for name, (a, b) in DEMO.items():
        ma = Molecule().from_adjacency_list(a)
        mb = Molecule().from_adjacency_list(b)
        made, err = run_recipe(family, CONTROL[1], [ma, mb])
        if made is None:
            print('  {0:<12} -> {1}'.format(name, err or 'None'))
            continue
        unchanged = same_set(made, [ma, mb])
        inert += 1 if unchanged else 0
        print('  {0:<12} in {1:<28} out {2:<28} {3}'.format(
            name, describe([ma, mb]), describe(made),
            'IDENTICAL' if unchanged else 'changed'))
    print('  -> {0} of {1} unchanged'.format(inert, len(DEMO)))

    print('')
    print('(0b) generate_reactions on the same pairs')
    total_rxn = 0
    for name, (a, b) in DEMO.items():
        ma = Molecule().from_adjacency_list(a)
        mb = Molecule().from_adjacency_list(b)
        ma.clear_labeled_atoms()
        mb.clear_labeled_atoms()
        n = len(family.generate_reactions([ma, mb]))
        total_rxn += n
        print('  {0:<12} -> {1} reaction(s)'.format(name, n))

    print('')
    print('(0c) census of charge-action recipes under input/kinetics/families/')
    bare, paired = census()
    print('  use a charge action                      : {0}'.format(len(bare) + len(paired)))
    print('  ... paired with a structural action      : {0}'.format(len(paired)))
    print('  ... charge actions only                  : {0}'.format(len(bare)))

    # ------------------------------------------------------------------ PART 1
    hdr('PART 1 -- the action grammar, read from the engine and measured.')
    va = valid_actions_from_source()
    print('valid_actions, read from {0}:'.format(os.path.relpath(FAMILY_PY, ENGINE)))
    print('  {0}'.format(va))
    print('')
    print('Effect of each on the DERIVED charge of *1, measured by applying it and reading back:')
    print('')
    r1 = '  {0:<18} {1:>7}  {2:>9}  {3}'
    print(r1.format('action', 'labels', 'd(charge)', 'meaning'))
    print('  ' + '-' * 74)
    for name, nlabels, dq, note in measure_action_effects():
        print(r1.format(name, nlabels, dq, note))
    print('')
    print('Reading: an electron arriving at an atom must lower valence - bonds - radicals - 2*lp by')
    print('one. GAIN_RADICAL does exactly that with one label. GAIN_PAIR/LOSE_PAIR move two')
    print('electrons. Bond actions move one onto EACH of two atoms and need a second label. The two')
    print('charge actions move none -- they are the only actions in the grammar with no effect on')
    print('the quantity the charge is derived from.')

    # ------------------------------------------------------------------ PART 2
    hdr('PART 2 -- all four candidate recipes against all 27 training entries.')
    print('A candidate is CORRECT for an entry when apply_recipe returns exactly the declared')
    print('products. "raise" means the action is impossible on that structure, not merely wrong.')
    print('')

    dep = family.get_training_depository()
    entries = sorted(dep.entries.values(), key=lambda e: e.index)
    combos = []
    for an, aa in ACCEPT.items():
        for bn, ba in DONATE.items():
            combos.append(('{0} | {1}'.format(an.split()[0], bn.split()[0]), aa + ba))

    r2 = '{0:>4}  {1:<30} {2:<12} {3:<12} {4:<12} {5:<12}'
    h2 = r2.format('idx', 'reaction', *[c[0] for c in combos])
    print(h2)
    print('-' * len(h2))

    outcome = {}
    served_by = {}
    for entry in entries:
        reactants = mols(entry.item.reactants)
        products = mols(entry.item.products)
        cells, winners = [], []
        for cname, cactions in combos:
            made, err = run_recipe(family, cactions, reactants)
            if err:
                cells.append('raise')
            elif made is None:
                cells.append('n-prod')
            elif same_set(made, products):
                cells.append('CORRECT')
                winners.append(cname)
            elif same_set(made, reactants):
                cells.append('inert')
            else:
                cells.append('wrong')
        outcome[entry.index] = (entry, cells, winners)
        for w in winners:
            served_by.setdefault(w, []).append(entry.index)
        print(r2.format(entry.index, entry.label[:30], *cells))

    unserved = [i for i, v in outcome.items() if not v[2]]
    multi = [i for i, v in outcome.items() if len(v[2]) > 1]

    # ------------------------------------------------------------------ PART 3
    hdr('PART 3 -- what that partition means.')
    print('entries served, per candidate recipe:')
    for cname, _ in combos:
        idxs = sorted(served_by.get(cname, []))
        print('  {0:<26} {1:>2} entries  {2}'.format(cname, len(idxs), idxs))
    print('')
    print('  served by exactly one candidate : {0}'.format(
        len([i for i, v in outcome.items() if len(v[2]) == 1])))
    print('  served by more than one         : {0}  {1}'.format(len(multi), sorted(multi)))
    print('  served by NO candidate          : {0}  {1}'.format(len(unserved), sorted(unserved)))
    print('')
    best = max((len(v) for v in served_by.values()), default=0)
    print('  largest single-recipe family    : {0} of {1} entries'.format(best, len(entries)))
    print('  distinct recipes needed to cover the rest: {0}'.format(
        len([c for c, _ in combos if served_by.get(c)])))

    if unserved:
        print('')
        print('Entries no two-label recipe in the grammar can serve, with what they need:')
        for i in sorted(unserved):
            entry = outcome[i][0]
            print('  {0:>3}  {1:<34} {2} -> {3}'.format(
                i, entry.label,
                describe(mols(entry.item.reactants)), describe(mols(entry.item.products))))

    # ------------------------------------------------------------------ PART 4
    hdr('SUMMARY')
    print('  shipped recipe, demo pairs unchanged      : {0} of {1}'.format(inert, len(DEMO)))
    print('  shipped recipe, reactions generated       : {0}'.format(total_rxn))
    print('  mainline charge-only recipes              : {0} of {1}'.format(
        len(bare), len(bare) + len(paired)))
    print('  candidate recipes tried                   : {0}'.format(len(combos)))
    print('  entries served by a single recipe (best)  : {0} of {1}'.format(best, len(entries)))
    print('  entries served by no recipe at all        : {0}'.format(len(unserved)))
    print('')
    print('What this probe could NOT reach:')
    print('  - Recipes using a THIRD label. The template is two-label, so a bond action inside one')
    print('    reactant cannot be written without changing the template as well as the recipe.')
    print('    PART 3 lists the entries that would need one; it does not design that template.')
    print('  - Whether the narrowed groups can still be written so every node samples and descends.')
    print('    That is the twelve-check question and is measured separately.')
    print('  - The reverse family, which does not exist in this repository.')
    print('')
    if best == len(entries):
        print('VERDICT: OUTCOME 1 -- one recipe serves the whole family.')
        return 0
    if best > 0:
        print('VERDICT: OUTCOME 2 -- no single recipe serves all {0} entries, but {1} of them are'.format(
            len(entries), best))
        print('served by one, and the grammar does express charge transfer. The family must narrow.')
        return 1
    print('VERDICT: OUTCOME 3 -- no recipe in the grammar serves any entry.')
    return 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(3)
