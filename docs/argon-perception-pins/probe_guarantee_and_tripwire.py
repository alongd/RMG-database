#!/usr/bin/env python
# encoding: utf-8

"""
Two measurements that decide how the re-pins are written.

A. **The guarantee question.** The two buildtime tests guaranteed that a nonsense argon
   species reaches the thermo layer and is refused with a loud ``DatabaseError`` rather
   than handed a fabricated group-additivity number. Today both die earlier with
   ``AtomTypeError``. Whether that guarantee is *lost* or merely *relocated* turns on one
   thing this probe answers: is there a +2 argon species that still builds, and does the
   thermo layer still refuse it loudly? If yes, the guarantee survives on a different
   spelling and the re-pin can keep testing it.

B. **The tripwire.** ``test_three_body_recombination_still_cannot_be_stored_at_all`` is
   not a stale pin - it is a tripwire whose docstring says it fires when RMG-Py gives
   ``TwoTemperaturePlasma`` an ``electrons`` field. The engine tip is the merge that did
   exactly that. This probe measures what the field now is and whether a three-body entry
   can now actually be stored - which is the question the tripwire was really guarding.
"""

import os
import sys
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, 'test'))

import conftest  # noqa: F401

from rmgpy.molecule import Molecule
from rmgpy.species import Species

import test_argon_cation_buildtime as bt


def banner(title):
    print('\n' + '=' * 78)
    print(title)
    print('=' * 78)


banner('A. IS THERE A +2 ARGON THAT STILL BUILDS, AND IS IT STILL REFUSED LOUDLY?')

CANDIDATES = [
    ('DICATION as the test spells it (3P ground state)', bt.DICATION),
    ('closed-shell +2 argon, u0 p3 c+2', '1 Ar u0 p3 c+2\n'),
    ('bonded +2 argon, u0 p3 c+2 with one bond to Ar0', None),
]

db = bt._db_with(bt.ARGON_CAPABLE_DECK)

for name, adjlist in CANDIDATES:
    if adjlist is None:
        continue
    print('\n--- %s ---' % name)
    print('adjlist : %r' % adjlist)
    try:
        mol = Molecule().from_adjacency_list(adjlist)
    except Exception as exc:
        print('  BUILD RAISED    : %s: %s' % (type(exc).__name__, exc))
        continue
    print('  BUILD OK        : %r atomtypes=%s net_charge=%d'
          % (mol, [a.atomtype.label for a in mol.atoms], mol.get_net_charge()))
    sp = Species(label=name, molecule=[mol])
    try:
        sp.generate_resonance_structures()
    except Exception as exc:
        print('  RESONANCE RAISED: %s: %s' % (type(exc).__name__, exc))
        continue
    try:
        data = db.get_thermo_data(sp)
    except Exception as exc:
        print('  THERMO RAISED   : %s: %s' % (type(exc).__name__, exc))
        print('    -> type       : %s' % type(exc).__name__)
        print("    -> 'Ar++' in message : %s" % ('Ar++' in str(exc)))
        continue
    print('  THERMO OK (!)   : comment=%r' % data.comment)
    print('    H298 kJ/mol   :', data.get_enthalpy(298.15) / 1000.0)

banner('B. THE TRIPWIRE: DOES TwoTemperaturePlasma NOW CARRY AN electrons FIELD?')

from rmgpy.kinetics import TwoTemperaturePlasma
from rmgpy import electron_placement

k = TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,
                         Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol'))
print("hasattr(k, 'electrons')            :", hasattr(k, 'electrons'))
try:
    print('k.electrons                        :', k.electrons)
except Exception as exc:
    print('k.electrons RAISED                 : %s: %s' % (type(exc).__name__, exc))

print('_NET_ELECTRON_KINETICS_CLASSES     :', electron_placement._NET_ELECTRON_KINETICS_CLASSES)
print("'TwoTemperaturePlasma' in it       :",
      'TwoTemperaturePlasma' in electron_placement._NET_ELECTRON_KINETICS_CLASSES)

banner('B2. CAN A THREE-BODY TWO-TEMPERATURE ENTRY NOW BE STORED?')

import shutil
import tempfile

from rmgpy.data.kinetics import KineticsDatabase
from rmgpy.exceptions import DatabaseError


def try_store(electrons_literal, tag):
    """Write the tripwire's own ThreeBodyTrial library, optionally declaring electrons,
    and try to load it. Prints what load_libraries does."""
    tmp = tempfile.mkdtemp(prefix='threebody-%s-' % tag, dir=os.environ.get('TMPDIR', '/tmp'))
    trial = os.path.join(tmp, 'ThreeBodyTrial')
    os.mkdir(trial)
    with open(os.path.join(trial, 'dictionary.txt'), 'w') as fh:
        fh.write('[Lip]\n1 Li u0 p0 c+1\n\n[Li]\nmultiplicity 2\n1 Li u1 p0 c0\n\n')
    kin = ("TwoTemperaturePlasma(A=(8.75e-27, 'cm^6/(molecule^2*s)'), n=-4.5,\n"
           "                                    Ea_g=(0, 'kJ/mol'), Ea_e=(0, 'kJ/mol')")
    if electrons_literal is not None:
        kin += ', electrons=%s' % electrons_literal
    kin += ')'
    with open(os.path.join(trial, 'reactions.py'), 'w') as fh:
        fh.write(
            'name = "ThreeBodyTrial"\n'
            'shortDesc = u""\n'
            'longDesc = u""\n'
            'entry(\n'
            '    index = 0,\n'
            '    label = "[Lip] => [Li]",\n'
            '    degeneracy = 1,\n'
            '    reversible = False,\n'
            '    kinetics = %s,\n'
            '    shortDesc = u"Li+ + 2 e- => Li + e-",\n'
            '    longDesc = u"",\n'
            ')\n' % kin)

    print('\n--- store attempt: electrons=%s ---' % electrons_literal)
    db = KineticsDatabase()
    try:
        db.load_libraries(tmp, libraries=['ThreeBodyTrial'])
    except DatabaseError as exc:
        print('  DatabaseError : %s' % exc)
        print("    'was not balanced' in message : %s" % ('was not balanced' in str(exc)))
    except Exception as exc:
        print('  %s : %s' % (type(exc).__name__, exc))
        traceback.print_exc(file=sys.stdout)
    else:
        lib = db.libraries['ThreeBodyTrial']
        print('  STORED OK -- %d entry/entries' % len(lib.entries))
        for key, entry in lib.entries.items():
            rxn = entry.item
            print('    %r' % rxn)
            print('    kinetics            : %r' % entry.data)
            print('    reaction.electrons  : %s' % getattr(rxn, 'electrons', '<absent>'))
            print('    kinetics.electrons  : %s' % getattr(entry.data, 'electrons', '<absent>'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


try_store(None, 'noelec')
try_store('-1', 'minus1')
try_store('1', 'plus1')

banner('DONE')
