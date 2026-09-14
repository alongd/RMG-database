#!/usr/bin/env python
# encoding: utf-8

"""
Does I-178 actually make three-body recombination representable end to end?

My first report concluded "the representational blocker is gone; data alone is now what is
missing". Review said that is false in *kind*, and pointed at the comment above
``FAMILY_ELECTRON_PLACEMENT``. This probe settles it by measurement rather than by reading
that comment:

  A. how many entries ``FAMILY_ELECTRON_PLACEMENT`` holds, and whether any is ``(2, 1)``;
  B. what happens to a stored three-body entry whose owner is absent from that map;
  C. what happens when it is forced under an owner that IS in the map
     (``PlasmaRadiativeRecombination``, declared ``(1, 0)``), whose net is right but whose
     incident order is wrong;
  D. what ``get_plasma_rate_order`` returns for third-order coefficients in several unit
     spellings - which decides whether the replacement tripwire can be a semantic check
     rather than a text grep.
"""

import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, 'test'))

import conftest  # noqa: F401

from rmgpy import electron_placement
from rmgpy.data.kinetics import KineticsDatabase
from rmgpy.electron_balance import get_plasma_rate_order
from rmgpy.kinetics import TwoTemperaturePlasma
from rmgpy.molecule import Molecule
from rmgpy.species import Species


def banner(title):
    print('\n' + '=' * 78)
    print(title)
    print('=' * 78)


banner('A. FAMILY_ELECTRON_PLACEMENT: SIZE, AND IS (2, 1) THERE?')
registry = electron_placement.FAMILY_ELECTRON_PLACEMENT
print('len(FAMILY_ELECTRON_PLACEMENT) :', len(registry))
for owner, decl in registry.items():
    print('  %-48s %s' % (owner, decl))
print('\nany declaration == (2, 1) :', any(d == (2, 1) for d in registry.values()))
print('owners declaring (2, 1)   :', [o for o, d in registry.items() if d == (2, 1)])


def species_list(rxn):
    """The model species list the resolver needs: the reaction's own species plus exactly
    one canonical electron."""
    electron = Species(label='e', molecule=[Molecule().from_adjacency_list('1 e u0 p0 c-1')])
    return list(rxn.reactants) + list(rxn.products) + [electron]


def store_three_body(owner_name):
    """Store a third-order TwoTemperaturePlasma entry in a library called ``owner_name``.
    Returns the loaded reaction (LibraryReaction, whose .family is the library label)."""
    tmp = tempfile.mkdtemp(prefix='tb-', dir=os.environ.get('TMPDIR', '/tmp'))
    lib = os.path.join(tmp, owner_name)
    os.mkdir(lib)
    with open(os.path.join(lib, 'dictionary.txt'), 'w') as fh:
        fh.write('[Lip]\n1 Li u0 p0 c+1\n\n[Li]\nmultiplicity 2\n1 Li u1 p0 c0\n\n')
    with open(os.path.join(lib, 'reactions.py'), 'w') as fh:
        fh.write(
            'name = "%s"\nshortDesc = u""\nlongDesc = u""\n'
            'entry(\n'
            '    index = 0,\n'
            '    label = "[Lip] => [Li]",\n'
            '    degeneracy = 1,\n'
            '    reversible = False,\n'
            "    kinetics = TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,\n"
            "                                    Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol'),\n"
            '                                    electrons=-1),\n'
            '    shortDesc = u"Li+ + 2 e- => Li + e-",\n'
            '    longDesc = u"",\n'
            ')\n' % owner_name)
    db = KineticsDatabase()
    db.load_libraries(tmp, libraries=[owner_name])
    # get_library_reactions() yields LibraryReaction, whose __init__ sets .family to the
    # library label - which is what the resolver reads. entry.item is a bare Reaction.
    reactions = db.libraries[owner_name].get_library_reactions()
    assert len(reactions) == 1
    shutil.rmtree(tmp, ignore_errors=True)
    return reactions[0], reactions[0].kinetics


banner('B. STORED UNDER AN OWNER ABSENT FROM THE MAP -> WHAT DOES PLACEMENT DO?')
owner = 'PlasmaThreeBodyRecombination'
print("owner %r in map : %s" % (owner, owner in registry))
rxn, kin = store_three_body(owner)
print('stored OK       : %r' % rxn)
print('reaction.family : %r' % rxn.family)
print('reaction.electrons :', rxn.electrons)
try:
    view = electron_placement.resolve_electron_placement(rxn, species_list(rxn))
except Exception as exc:
    print('resolve RAISED  : %s' % type(exc).__name__)
    print('  message       : %s' % exc)
else:
    print('resolve OK (!)  : %r' % view)

banner('C. FORCED UNDER PlasmaRadiativeRecombination, DECLARED (1, 0)')
owner = 'PlasmaRadiativeRecombination'
print("owner %r in map : %s -> %s" % (owner, owner in registry, registry.get(owner)))
rxn, kin = store_three_body(owner)
print('stored OK       : %r' % rxn)
print('reaction.family : %r' % rxn.family)
print('net electrons   : %s  (declaration net = %d)'
      % (rxn.electrons, registry[owner][1] - registry[owner][0]))
try:
    view = electron_placement.resolve_electron_placement(rxn, species_list(rxn))
except Exception as exc:
    print('resolve RAISED  : %s' % type(exc).__name__)
    print('  message       : %s' % exc)
    print("  mentions electron density : %s" % ('electron density' in str(exc)))
else:
    print('resolve OK (!)  : %r' % view)

banner('D. get_plasma_rate_order FOR THIRD-ORDER COEFFICIENTS IN SEVERAL SPELLINGS')
SPELLINGS = [
    'cm^6/(molecule^2*s)',
    'm^6/(molecule^2*s)',
    'cm^6/(mol^2*s)',
    'm^6/(mol^2*s)',
    'cm^3/(molecule*s)',
    'm^3/(mol*s)',
]
for units in SPELLINGS:
    k = TwoTemperaturePlasma(A=(8.75e-27, units), n=-4.5,
                             Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol'), electrons=-1)
    print('  %-24s A.units=%-24r order=%s'
          % (units, k.A.units, get_plasma_rate_order(k)))

banner('D2. THE SHIPPED LIBRARY, INTERROGATED SEMANTICALLY')
from rmgpy import settings
db = KineticsDatabase()
db.load_libraries(os.path.join(settings['database.directory'], 'kinetics', 'libraries'),
                  libraries=['PlasmaRadiativeRecombination'])
for key, entry in db.libraries['PlasmaRadiativeRecombination'].entries.items():
    k = entry.data
    print('  entry %-6s kinetics=%-22s A.units=%-24r order=%s'
          % (entry.index, k.__class__.__name__,
             getattr(getattr(k, 'A', None), 'units', None), get_plasma_rate_order(k)))

banner('DONE')
