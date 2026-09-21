#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 6 -- the twelve family checks in databaseTest.py, one at a time,
for Plasma_Radiative_Recombination, against whichever tree I236_DB names.

The check bodies are imported from the engine's own test class, not reimplemented,
so a check that changes upstream changes here too.
"""
import os
import sys
import traceback

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))

sys.path.insert(0, '/home/alon/Code/RMG-Py-plasma/test/database')
from databaseTest import TestDatabase

FAMILY = os.environ.get('I236_FAMILY', 'Plasma_Radiative_Recombination')

TestDatabase.setup_class()
t = TestDatabase()
fam = t.database.kinetics.families[FAMILY]
print('family loaded: {0} | electrons = {1} | auto_generated = {2}'.format(
    fam.label, fam.electrons, fam.auto_generated))
print('groups.top = {0} | forward_template.reactants = {1}'.format(
    [e.label for e in fam.groups.top],
    [e.label for e in fam.forward_template.reactants]))
print('root group: {0}'.format(
    fam.groups.top[0].item.to_adjacency_list().strip().replace('\n', ' / ')))
print()

CHECKS = [
    'kinetics_check_correct_number_of_nodes_in_rules',
    'kinetics_check_nodes_in_rules_found_in_groups',
    'kinetics_check_groups_found_in_tree',
    'kinetics_check_groups_nonidentical',
    'kinetics_check_child_parent_relationships',
    'kinetics_check_siblings_for_parents',
    'kinetics_check_cd_atom_type',
    'kinetics_check_reactant_and_product_template',
    'kinetics_check_num_reactant_and_product',
    'kinetics_check_family_electrons_reach_training_reactions',
    'kinetics_check_sample_descends_to_group',
    'kinetics_check_sample_can_react',
]

npass = 0
for name in CHECKS:
    try:
        ok = getattr(t, name)(FAMILY)
        status = 'PASS' if ok else 'RETURNED-FALSY'
        if ok:
            npass += 1
    except Exception as exc:
        status = 'RAISED {0}: {1}'.format(type(exc).__name__, exc)
        traceback.print_exc(file=sys.stdout)
    print('{0:60s} {1}'.format(name, status))

print()
print('FAMILY CHECKS PASSING: {0} of {1}'.format(npass, len(CHECKS)))

# the two depository checks the same loop runs
ndep = 0
for depository in fam.depositories:
    for name, kwargs in (('kinetics_check_adjlists_nonidentical', {}),
                         ('kinetics_check_rate_units_are_correct', {'tag': 'depository'})):
        try:
            ok = getattr(t, name)(depository, **kwargs)
            print('{0:60s} {1}  [{2}]'.format(name, 'PASS' if ok else 'RETURNED-FALSY',
                                              depository.label))
            ndep += 1 if ok else 0
        except Exception as exc:
            print('{0:60s} RAISED {1}: {2}'.format(name, type(exc).__name__, exc))
print('DEPOSITORY CHECKS PASSING: {0}'.format(ndep))
