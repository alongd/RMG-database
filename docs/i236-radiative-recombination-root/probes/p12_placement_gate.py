#!/usr/bin/env python
# encoding: utf-8
"""I-236 probe 12 -- where the electron-placement declaration actually bites.

Probe 11 measured that `generate_reactions` works for the new family with the
registry exactly as RMG-Py ships it, which contradicts what the sibling family's
docstring says ("raises the moment it is asked to produce a reaction"). This
probe finds the real gate by calling the resolver itself, which the plasma
reactor calls at `rmgpy/solver/plasma.pyx:276` -- i.e. at reactor setup, not at
reaction generation.
"""
import os
import traceback

DB = os.environ['I236_DB']
from rmgpy import settings
settings['database.directory'] = DB
print('RESOLVED database.directory = {0}'.format(settings['database.directory']))

from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy import electron_placement

FAMILY = 'Plasma_Radiative_Recombination_Pairing'

kdb = KineticsDatabase()
kdb.load_families(os.path.join(DB, 'kinetics', 'families'), families=[FAMILY],
                  depositories=['training'])
fam = kdb.families[FAMILY]

rxn = fam.generate_reactions([Molecule().from_adjacency_list(
    'multiplicity 2\n1 Ar u1 p3 c+1')])[0]
print('generated (registry does NOT contain this family): {0}'.format(rxn))
print('  reaction.electrons = {0}'.format(rxn.electrons))
print('  family attribute   = {0!r}'.format(getattr(rxn, 'family', None)))

# The resolver works on Species, as the reactor does; generate_reactions hands
# back Molecules. Promote them exactly once and keep the same objects on both the
# reaction and the species list, so identity checks inside the resolver hold.
rxn.reactants = [Species(molecule=[m]) for m in rxn.reactants]
rxn.products = [Species(molecule=[m]) for m in rxn.products]
species = list(rxn.reactants) + list(rxn.products)
electron = Species(label='e', molecule=[Molecule().from_adjacency_list('1 e u0 p0 c-1')])
species.append(electron)

from rmgpy.kinetics import Arrhenius

for arm, present, with_kinetics in (('WITHOUT the registry entry', False, True),
                                    ('WITH the registry entry, no kinetics on the reaction', True, False),
                                    ('WITH the registry entry and the family rule attached', True, True)):
    rxn.kinetics = Arrhenius(A=(1.007892e+05, 'm^3/(mol*s)'), n=0.0,
                             Ea=(0.0, 'kJ/mol'), T0=(1, 'K')) if with_kinetics else None
    if present:
        electron_placement.FAMILY_ELECTRON_PLACEMENT[FAMILY] = (1, 0)
    else:
        electron_placement.FAMILY_ELECTRON_PLACEMENT.pop(FAMILY, None)
    print('\n--- resolve_electron_placement, {0}'.format(arm))
    try:
        view = electron_placement.resolve_electron_placement(rxn, species)
        print('    OK: {0!r}'.format(view))
    except Exception:
        for line in traceback.format_exc().strip().splitlines()[-4:]:
            print('    {0}'.format(line))
