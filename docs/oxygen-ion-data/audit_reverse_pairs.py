"""Scan every branch library for independent irreversible cross-library reverses.

AST inventories all active entry calls. Only libraries containing irreversible
arrows need loading; actual loaded reactions, model species admission and the
actual duplicate check determine state matches and order-dependent collapses.
"""
from pathlib import Path
import ast
import copy
import itertools
import json
import sys

from rmgpy import settings
from rmgpy.rmg.model import CoreEdgeReactionModel
from rmgpy.electron_balance import get_electron_placement_counts

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
settings['database.directory'] = str(ROOT/'input')
sys.path.insert(0, str(ROOT/'test'))
import test_plasma_oxygen_charged as checks

paths = sorted((ROOT/'input/kinetics/libraries').rglob('reactions.py'))
needed = []
entry_count = irreversible_count = 0
for path in paths:
    has_irreversible = False
    for node in ast.walk(ast.parse(path.read_text(encoding='utf-8-sig'))):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name) or node.func.id != 'entry':
            continue
        args = {kw.arg: kw.value for kw in node.keywords}
        # Fail loudly on a dynamically generated index/label rather than omit it.
        label = ast.literal_eval(args['label'])
        ast.literal_eval(args['index'])
        entry_count += 1
        if '=>' in label and '<=>' not in label:
            has_irreversible = True
            irreversible_count += 1
    if has_irreversible:
        needed.append(str(path.parent.relative_to(ROOT/'input/kinetics/libraries')))

fixture = checks.database.__wrapped__()
db = next(fixture)
result = dict(scanned_library_files=len(paths), active_source_entries=entry_count,
              irreversible_source_entries=irreversible_count, loaded_libraries=needed,
              criterion='Both reactions irreversible, opposite actual model species, matching collider and electron placement',
              pairs=[])
try:
    db.kinetics.load_libraries(str(ROOT/'input/kinetics/libraries'), libraries=needed)
    species_model = CoreEdgeReactionModel()
    buckets = {}
    loaded_count = 0
    for name in needed:
        for reaction in db.kinetics.libraries[name].get_library_reactions():
            if reaction.reversible:
                continue
            loaded_count += 1
            reaction.reactants = [species_model.make_new_species(s, generate_thermo=False)[0] for s in reaction.reactants]
            reaction.products = [species_model.make_new_species(s, generate_thermo=False)[0] for s in reaction.products]
            if reaction.specific_collider is not None:
                reaction.specific_collider = species_model.make_new_species(reaction.specific_collider, generate_thermo=False)[0]
            reactants = tuple(sorted(s.index for s in reaction.reactants))
            products = tuple(sorted(s.index for s in reaction.products))
            collider = None if reaction.specific_collider is None else reaction.specific_collider.index
            counts = tuple(get_electron_placement_counts(reaction))
            key = (reactants, products, collider, counts)
            buckets.setdefault(key, []).append(reaction)
    result['loaded_irreversible_reactions'] = loaded_count
    seen = set()
    for key, reactions in buckets.items():
        left, right, collider, counts = key
        if left == right:
            continue
        reverse = (right, left, collider, counts[::-1])
        for a, b in itertools.product(reactions, buckets.get(reverse, [])):
            if a.family == b.family:
                continue
            pair_key = tuple(sorted(((a.family, a.entry.index), (b.family, b.entry.index))))
            if pair_key in seen:
                continue
            seen.add(pair_key)
            trials = []
            for first, second in ((a, b), (b, a)):
                model = CoreEdgeReactionModel()
                r1, new1 = model.make_new_reaction(copy.deepcopy(first), generate_thermo=False, generate_kinetics=False)
                r2, new2 = model.make_new_reaction(copy.deepcopy(second), generate_thermo=False, generate_kinetics=False)
                trials.append(dict(order=[[first.family, first.entry.index], [second.family, second.entry.index]],
                                   new=[new1, new2], returned_same_object=r1 is r2,
                                   survivors=[[r.family, r.entry.index] for r in model.new_reaction_list]))
            result['pairs'].append(dict(entries=[dict(library=r.family, index=r.entry.index, label=r.entry.label,
                                                     rate_class=type(r.kinetics).__name__) for r in (a, b)],
                                        trials=trials,
                                        collapses_both_orders=all(t['new'] == [True, False] and t['returned_same_object'] for t in trials)))
    result['pairs'].sort(key=lambda p: sorted((e['library'], e['index']) for e in p['entries']))
finally:
    fixture.close()
print(json.dumps(result, indent=2))
