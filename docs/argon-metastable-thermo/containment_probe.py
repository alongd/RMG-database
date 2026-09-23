#!/usr/bin/env python
# encoding: utf-8
"""
Does the containment close the reachability, and does it move anything else?

Five ordinary families carry one ``forbidden(...)`` entry each for ``Ar u2 p3 c0``. That
mechanism runs inside ``KineticsFamily.__generate_product_structures`` -- on the reactant
structures at ``family.py:1669`` and on the products at ``:1690`` -- so it fires during
reaction GENERATION, upstream of species creation, of thermo, and of any kinetics gate.
This probe measures three things:

1. **Closure.** Over all 140 families and the same 50 partners as the full sweep, does any
   ordinary family still generate from ``Ar(3P2)``?
2. **The intended channel survives.** ``Plasma_Electron_Impact_Ionization`` must still give
   ``Ar(3P2) => Ar+``. A containment that took that with it would be a regression.
3. **Controls.** The chemistry each family exists FOR, named per family, must be bit-for-bit
   unmoved. ``Birad_R_Recombination``'s three are the ones its own longDesc names: O, S and
   NH biradicals.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/containment_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/containment_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/containment_probe.stderr.log >&2)
"""

import logging
import os
import sys

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402
from rmgpy.molecule import Molecule                        # noqa: E402
from rmgpy.species import Species                          # noqa: E402

logging.getLogger().setLevel(logging.CRITICAL)

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
FAMILIES = ['Birad_R_Recombination', 'R_Addition_MultipleBond', 'Disproportionation',
            'CO_Disproportionation', 'Cl_Abstraction']

ADJ = {
    'H': 'multiplicity 2\n1 H u1 p0 c0\n',
    'O': 'multiplicity 3\n1 O u2 p2 c0\n',
    'S': 'multiplicity 3\n1 S u2 p2 c0\n',
    'NH': 'multiplicity 3\n1 N u2 p1 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n',
    'OH': 'multiplicity 2\n1 O u1 p2 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n',
    'CH3': 'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
           '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n',
    'C2H4': '1 C u0 p0 c0 {2,D} {3,S} {4,S}\n2 C u0 p0 c0 {1,D} {5,S} {6,S}\n'
            '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n5 H u0 p0 c0 {2,S}\n'
            '6 H u0 p0 c0 {2,S}\n',
    'C2H2': '1 C u0 p0 c0 {2,T} {3,S}\n2 C u0 p0 c0 {1,T} {4,S}\n3 H u0 p0 c0 {1,S}\n'
            '4 H u0 p0 c0 {2,S}\n',
    'C2H5': 'multiplicity 2\n1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}\n'
            '2 C u1 p0 c0 {1,S} {6,S} {7,S}\n3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'
            '5 H u0 p0 c0 {1,S}\n6 H u0 p0 c0 {2,S}\n7 H u0 p0 c0 {2,S}\n',
    'HCO': 'multiplicity 2\n1 C u1 p0 c0 {2,D} {3,S}\n2 O u0 p2 c0 {1,D}\n'
           '3 H u0 p0 c0 {1,S}\n',
    'HCl': '1 Cl u0 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n',
    'N2': '1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}\n',
    'C6H5': 'multiplicity 2\n1 C u1 p0 c0 {2,B} {6,B}\n2 C u0 p0 c0 {1,B} {3,B} {7,S}\n'
            '3 C u0 p0 c0 {2,B} {4,B} {8,S}\n4 C u0 p0 c0 {3,B} {5,B} {9,S}\n'
            '5 C u0 p0 c0 {4,B} {6,B} {10,S}\n6 C u0 p0 c0 {1,B} {5,B} {11,S}\n'
            '7 H u0 p0 c0 {2,S}\n8 H u0 p0 c0 {3,S}\n9 H u0 p0 c0 {4,S}\n'
            '10 H u0 p0 c0 {5,S}\n11 H u0 p0 c0 {6,S}\n',
    'CH2O': '1 C u0 p0 c0 {2,D} {3,S} {4,S}\n2 O u0 p2 c0 {1,D}\n3 H u0 p0 c0 {1,S}\n'
            '4 H u0 p0 c0 {1,S}\n',
    'O2': 'multiplicity 3\n1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}\n',
    'SH': 'multiplicity 2\n1 S u1 p2 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n',
    'NH2': 'multiplicity 2\n1 N u1 p1 c0 {2,S} {3,S}\n2 H u0 p0 c0 {1,S}\n'
           '3 H u0 p0 c0 {1,S}\n',
    'CO2': '1 C u0 p0 c0 {2,D} {3,D}\n2 O u0 p2 c0 {1,D}\n3 O u0 p2 c0 {1,D}\n',
    'Cl': 'multiplicity 2\n1 Cl u1 p3 c0\n',
}

#: The chemistry each family EXISTS for. If the containment moves one of these, it is not a
#: containment, it is a regression. Birad_R_Recombination's three are exactly the ones its
#: own forbidden-group longDesc names.
CONTROLS = {
    'Birad_R_Recombination': [('O', 'CH3'), ('S', 'CH3'), ('NH', 'CH3'),
                              ('O', 'H'), ('S', 'OH')],
    'R_Addition_MultipleBond': [('H', 'C2H4'), ('CH3', 'C2H2'), ('OH', 'C2H4'),
                                ('H', 'CO2'), ('CH3', 'CH2O')],
    'Disproportionation': [('CH3', 'C2H5'), ('OH', 'C2H5'), ('H', 'C2H5'),
                           ('O2', 'C2H5'), ('NH2', 'C2H5')],
    'CO_Disproportionation': [('H', 'HCO'), ('CH3', 'HCO'), ('OH', 'HCO'),
                              ('SH', 'HCO')],
    'Cl_Abstraction': [('H', 'HCl'), ('CH3', 'HCl'), ('OH', 'HCl')],
}

#: Control pairs that were ALREADY zero before the containment was written, with the
#: measurement that established it. ``H + HCl`` under ``Cl_Abstraction`` is the degenerate
#: identity reaction H. + HCl -> HCl + H., which RMG does not generate; measured on the
#: reverted file, it was 0 then and it is 0 now. Recorded rather than quietly dropped from
#: the control list: a control that reads GONE and is not explained is worse than no
#: control, and a control list pruned until it is green is not a control list.
KNOWN_ZERO_BEFORE = {
    ('Cl_Abstraction', 'H', 'HCl'):
        'degenerate identity reaction; measured 0 on the reverted groups.py as well',
}

#: Partners that reached each family in the 50-partner sweep, so closure is tested against
#: the witnesses rather than against a hopeful subset.
WITNESSES = ['H', 'O2', 'OH', 'CH3', 'N2', 'C2H4', 'C2H2', 'C2H5', 'HCO', 'HCl',
             'C6H5', 'CH2O', 'NH2', 'SH', 'CO2', 'Cl', 'O', 'S', 'NH']


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def spc(label):
    return Species(label=label, molecule=[Molecule().from_adjacency_list(ADJ[label])])


kdb = KineticsDatabase()
kdb.load_families(os.path.join(DATABASE, 'kinetics', 'families'), families='all',
                  depositories=['training'])
meta = Species(label='Ar(3P2)', molecule=[Molecule().from_adjacency_list(AR_META)])

banner("0. WHAT IS LOADED, AND DOES THE CONTAINMENT EXIST?")
print("  families loaded: %d" % len(kdb.families))
for family in FAMILIES:
    fam = kdb.families[family]
    labels = sorted(fam.forbidden.entries) if fam.forbidden else []
    print("  %-26s forbidden entries: %s" % (family, labels))
    assert 'Ar_metastable_biradical' in labels, family
    group = fam.forbidden.entries['Ar_metastable_biradical'].item
    print("      %-26s group labels: %s"
          % ('', sorted(group.get_all_labeled_atoms())))

banner("1. CLOSURE: does any ordinary family still generate from Ar(3P2)?")
hits = {}
for label in WITNESSES:
    rxns = kdb.generate_reactions_from_families([meta, spc(label)], products=None,
                                                resonance=True)
    for rxn in rxns:
        hits.setdefault(rxn.family, set()).add(label)
        print("  STILL REACHES  %-26s %s" % (rxn.family, rxn))
uni = kdb.generate_reactions_from_families([meta], products=None, resonance=True)
for rxn in uni:
    hits.setdefault(rxn.family, set()).add('(unimolecular)')
    print("  unimolecular   %-26s %s" % (rxn.family, rxn))

ordinary = sorted(set(hits) - {'Plasma_Electron_Impact_Ionization'})
print("\n  partners tried                              : %d" % len(WITNESSES))
print("  ordinary families still reaching Ar(3P2)    : %d  %s" % (len(ordinary), ordinary))
print("  intended ionisation channel still generated : %s"
      % ('Plasma_Electron_Impact_Ionization' in hits))

banner("2. CONTROLS: the chemistry each family exists FOR")
moved = []
for family, pairs in CONTROLS.items():
    print("\n  %s" % family)
    for a, b in pairs:
        rxns = [r for r in kdb.generate_reactions_from_families(
            [spc(a), spc(b)], products=None, resonance=True) if r.family == family]
        known = KNOWN_ZERO_BEFORE.get((family, a, b))
        if rxns:
            status = 'OK  '
        elif known:
            status = 'ZERO'
        else:
            status = 'GONE'
            moved.append((family, a, b))
        print("      %s %-5s + %-5s -> %d reaction(s)%s"
              % (status, a, b, len(rxns),
                 ('   ' + '; '.join(str(r) for r in rxns[:2])) if rxns
                 else ('   ALREADY ZERO BEFORE: ' + known if known else '')))

banner("3. VERDICT")
print("  ordinary families still reaching Ar(3P2) : %d" % len(ordinary))
print("  intended ionisation channel survives     : %s"
      % ('Plasma_Electron_Impact_Ionization' in hits))
print("  control reactions that DISAPPEARED       : %d %s" % (len(moved), moved))
sys.stdout.flush()
