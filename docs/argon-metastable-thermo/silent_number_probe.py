#!/usr/bin/env python
# encoding: utf-8
"""
Can any path from metastable argon produce a NUMBER instead of a crash?

``all_family_reachability_probe.py`` establishes that ordinary families match
``Ar u2 p3 c0`` and that their products die in ``get_thermo_data``. A crash is bad. A
number would be worse: it reaches a published mechanism without anything raising. So this
probe hunts specifically for the number.

Four searches, each able to come back either way:

1. **A wide partner sweep.** Forty ordinary gas-phase species against all 140 families,
   not the six the entry's own test picked and not the five partners the review named.
2. **The REAL thermo path**, ``rmgpy.thermo.thermoengine.submit`` -- the function RMG's
   ``CoreEdgeReactionModel.generate_thermo`` actually calls -- rather than a bare
   ``ThermoDatabase.get_thermo_data``. A defect that lives in resonance generation or in
   ``process_thermo_data`` is invisible to the shorter call.
3. **Second generation.** The first-generation argon products are fed back in as reactants.
   Nothing in a real run gets this far (the thermo crash comes first), so a number here is
   reported as latent rather than live -- but if the atom-type gap were ever filled from the
   engine side, this is what would be waiting.
4. **Can group additivity produce a number for a covalent argon at all?** Hand-built
   argon-containing molecules that DO perceive an atom type, put through the same path. This
   is the question the family sweep can only answer for the structures families happen to
   build.

NEGATIVE CONTROL. Search 4 includes ``CH3``, an ordinary species that MUST come back with a
number. If the control crashes, the probe is broken and every "CRASH" below is worthless.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/silent_number_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/silent_number_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/silent_number_probe.stderr.log >&2)
"""

import logging
import os
import sys

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = DATABASE

from rmgpy.data.rmg import RMGDatabase                     # noqa: E402
from rmgpy.molecule import Molecule                        # noqa: E402
from rmgpy.species import Species                          # noqa: E402
from rmgpy.thermo.thermoengine import submit               # noqa: E402

logging.getLogger().setLevel(logging.CRITICAL)

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'

#: Forty ordinary gas-phase species. Nothing exotic: this is the radical pool and bath gas
#: of any hydrocarbon / NOx / sulfur deck run in argon dilution.
PARTNER_SMILES = [
    ('H', '[H]'), ('H2', '[H][H]'), ('O', '[O]'), ('O2', '[O][O]'), ('OH', '[OH]'),
    ('H2O', 'O'), ('HO2', '[O]O'), ('H2O2', 'OO'), ('N2', 'N#N'), ('NH', '[NH]'),
    ('NH2', '[NH2]'), ('NH3', 'N'), ('NO', '[N]=O'), ('NO2', '[O][N]=O'),
    ('N2O', '[N-]=[N+]=O'), ('CH', '[CH]'), ('CH3', '[CH3]'), ('CH4', 'C'),
    ('C2H2', 'C#C'), ('C2H3', '[CH]=C'), ('C2H4', 'C=C'), ('C2H5', 'C[CH2]'),
    ('C2H6', 'CC'), ('HCO', '[CH]=O'), ('CH2O', 'C=O'), ('CH3O', 'C[O]'),
    ('CH2OH', '[CH2]O'), ('CH3OH', 'CO'), ('CO', '[C-]#[O+]'), ('CO2', 'O=C=O'),
    ('CH3OO', 'CO[O]'), ('HCCO', '[CH]=C=O'), ('C3H3', '[CH2]C#C'), ('C3H5', '[CH2]C=C'),
    ('C6H6', 'c1ccccc1'), ('C6H5', '[c]1ccccc1'), ('C7H7', '[CH2]c1ccccc1'),
    ('SH', '[SH]'), ('H2S', 'S'), ('SO2', 'O=S=O'), ('Cl', '[Cl]'), ('HCl', 'Cl'),
]
#: Species whose SMILES round trip is not safe here (monatomic ions, noble gases, the
#: metastable itself) are written as adjacency lists. See the SMILES warning in the entry.
PARTNER_ADJ = [
    ('Ar', '1 Ar u0 p4 c0\n'),
    ('Ar+', 'multiplicity 2\n1 Ar u1 p3 c+1\n'),
    ('He', '1 He u0 p1 c0\n'),
    ('Ne', '1 Ne u0 p4 c0\n'),
    ('Ar(3P2)', AR_META),
    ('CH2(T)', 'multiplicity 3\n1 C u2 p0 c0 {2,S} {3,S}\n2 H u0 p0 c0 {1,S}\n'
               '3 H u0 p0 c0 {1,S}\n'),
    ('CH2(S)', '1 C u0 p1 c0 {2,S} {3,S}\n2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n'),
    ('N', 'multiplicity 4\n1 N u3 p1 c0\n'),
]


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def adj1(mol):
    return mol.to_adjacency_list().strip().replace('\n', ' | ')


def partners():
    out = []
    for label, smi in PARTNER_SMILES:
        try:
            out.append((label, Molecule().from_smiles(smi)))
        except Exception as exc:                                    # noqa: BLE001
            print("  partner %s unbuildable from SMILES %r: %s" % (label, smi, exc))
    for label, adj in PARTNER_ADJ:
        out.append((label, Molecule().from_adjacency_list(adj)))
    return out


def thermo_verdict(mol):
    """Run the path RMG itself runs: resonance structures, then ``submit``.

    Returns ('NUMBER', thermo) or ('CRASH', exception).
    """
    spc = Species(molecule=[mol.copy(deep=True)])
    try:
        spc.generate_resonance_structures()
        submit(spc)
        if spc.thermo is None:
            return 'CRASH', RuntimeError('submit returned None thermo')
        # force the numbers out, in case laziness hides the failure
        spc.thermo.get_enthalpy(298.15)
        spc.thermo.get_entropy(298.15)
    except Exception as exc:                                        # noqa: BLE001
        return 'CRASH', exc
    return 'NUMBER', spc.thermo


db = RMGDatabase()
db.load(path=DATABASE, thermo_libraries=None, kinetics_families='all',
        reaction_libraries=[], kinetics_depositories=['training'])
kdb = db.kinetics
print("families loaded: %d" % len(kdb.families))

meta = Species(label='Ar(3P2)', molecule=[Molecule().from_adjacency_list(AR_META)])
PARTNERS = partners()

banner("1+2. WIDE PARTNER SWEEP, THERMO THROUGH thermoengine.submit")
first_gen = {}      # adjacency -> (family, partner)
per_family = {}
for label, mol in PARTNERS:
    spc = Species(label=label, molecule=[mol.copy(deep=True)])
    try:
        rxns = kdb.generate_reactions_from_families([meta, spc], products=None,
                                                    resonance=True)
    except Exception as exc:                                        # noqa: BLE001
        print("  %-9s GENERATION RAISED %s: %s" % (label, type(exc).__name__, exc))
        continue
    if not rxns:
        continue
    for rxn in rxns:
        per_family.setdefault(rxn.family, set()).add(label)
        print("  %-9s %-28s %s" % (label, rxn.family, rxn))
        for prod in rxn.products:
            first_gen.setdefault(adj1(prod.molecule[0]), (rxn.family, label))

uni = kdb.generate_reactions_from_families([meta], products=None, resonance=True)
for rxn in uni:
    per_family.setdefault(rxn.family, set()).add('(unimolecular)')
    for prod in rxn.products:
        first_gen.setdefault(adj1(prod.molecule[0]), (rxn.family, '(unimolecular)'))

print("\n  partners tried                 : %d" % len(PARTNERS))
print("  families loaded                : %d" % len(kdb.families))
print("  families that matched Ar(3P2)  : %d  %s"
      % (len(per_family), sorted(per_family)))
for fam, labels in sorted(per_family.items()):
    print("      %-34s via %s" % (fam, sorted(labels)))
print("  distinct first-generation products: %d" % len(first_gen))

print("\n  verdict per product:")
gen1_numbers, gen1_crashes = [], []
gen1_mols = {}
for key, (fam, label) in sorted(first_gen.items()):
    mol = Molecule().from_adjacency_list(key.replace(' | ', '\n'))
    gen1_mols[key] = mol
    verdict, payload = thermo_verdict(mol)
    if verdict == 'NUMBER':
        gen1_numbers.append((key, fam, label, payload))
        print("    NUMBER  %-26s %-9s %s" % (fam, label, key))
        print("            H298 = %.4f kJ/mol  S298 = %.4f  src = %s"
              % (payload.get_enthalpy(298.15) / 1000.0, payload.get_entropy(298.15),
                 (payload.comment or '').strip().replace('\n', ' / ')[:120]))
    else:
        gen1_crashes.append((key, fam, label, payload))
        print("    CRASH   %-26s %-9s %s" % (fam, label, key))
        print("            %s: %s" % (type(payload).__name__, str(payload)[:150]))

banner("2b. PER-REACTION ROLL-UP -- the level at which 'silent number' is defined")
print("  A product-level crash is only a job-killer if the reaction that builds it is")
print("  generated at all; and a reaction is a SILENT NUMBER only if EVERY one of its")
print("  products gets thermo. Counted per reaction, not per product.")
verdict_by_key = {}
for key, fam, label, _ in gen1_numbers:
    verdict_by_key[key] = 'NUMBER'
for key, fam, label, _ in gen1_crashes:
    verdict_by_key[key] = 'CRASH'
all_rxns = list(uni)
for label, mol in PARTNERS:
    spc = Species(label=label, molecule=[mol.copy(deep=True)])
    try:
        all_rxns.extend(kdb.generate_reactions_from_families([meta, spc], products=None,
                                                             resonance=True))
    except Exception:                                               # noqa: BLE001
        continue
fully_numbered, partly_crashed = [], []
for rxn in all_rxns:
    verdicts = [verdict_by_key.get(adj1(p.molecule[0]), 'CRASH') for p in rxn.products]
    (fully_numbered if all(v == 'NUMBER' for v in verdicts) else partly_crashed).append(rxn)
print("\n  reactions generated                                     : %d" % len(all_rxns))
print("  reactions where EVERY product gets thermo (SILENT NUMBER): %d" % len(fully_numbered))
for rxn in fully_numbered:
    print("      %-34s %s" % (rxn.family, rxn))
print("  reactions with at least one product that CRASHES         : %d" % len(partly_crashed))

banner("3. SECOND GENERATION (latent: a real run crashes before reaching this)")
argon_gen1 = [k for k in gen1_mols if any(a.element.symbol == 'Ar'
                                          for a in gen1_mols[k].atoms)]
print("  argon-bearing first-generation products fed back: %d" % len(argon_gen1))
second_gen = {}
for key in argon_gen1:
    react = Species(molecule=[gen1_mols[key].copy(deep=True)])
    for label, mol in PARTNERS:
        spc = Species(label=label, molecule=[mol.copy(deep=True)])
        try:
            rxns = kdb.generate_reactions_from_families([react, spc], products=None,
                                                        resonance=True)
        except Exception:                                           # noqa: BLE001
            continue
        for rxn in rxns:
            for prod in rxn.products:
                pkey = adj1(prod.molecule[0])
                if pkey not in first_gen:
                    second_gen.setdefault(pkey, (rxn.family, '%s + %s' % (key[:24], label)))
print("  distinct second-generation products: %d" % len(second_gen))
gen2_numbers = []
for key, (fam, how) in sorted(second_gen.items()):
    mol = Molecule().from_adjacency_list(key.replace(' | ', '\n'))
    if not any(a.element.symbol == 'Ar' for a in mol.atoms):
        continue
    verdict, payload = thermo_verdict(mol)
    tag = 'NUMBER ' if verdict == 'NUMBER' else 'CRASH  '
    print("    %s %-26s %s" % (tag, fam, key))
    if verdict == 'NUMBER':
        gen2_numbers.append((key, fam, how, payload))
        print("            H298 = %.4f kJ/mol  src = %s"
              % (payload.get_enthalpy(298.15) / 1000.0,
                 (payload.comment or '').strip().replace('\n', ' / ')[:120]))

banner("4. CAN GROUP ADDITIVITY NUMBER A COVALENT ARGON AT ALL?")
HAND_BUILT = [
    ('CH3 (NEGATIVE CONTROL, must be NUMBER)',
     'multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
     '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n'),
    ('Ar u0 p4 c0 (ground state, must be NUMBER)', '1 Ar u0 p4 c0\n'),
    ('Ar(3P2) itself, must be NUMBER from this library', AR_META),
    ('ArH, Ar0s u1 one single bond',
     'multiplicity 2\n1 Ar u1 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n'),
    ('Ar-Ar, both Ar0s u1',
     'multiplicity 3\n1 Ar u1 p3 c0 {2,S}\n2 Ar u1 p3 c0 {1,S}\n'),
    ('ArH closed shell, Ar0s u0 one single bond',
     '1 Ar u0 p3 c0 {2,S}\n2 H u0 p0 c0 {1,S}\n'),
    ('Ar2+ (Ar0s-Ar+), the one bonded argon this database already ships',
     'multiplicity 2\n1 Ar u0 p3 c0 {2,S}\n2 Ar u1 p3 c+1 {1,S}\n'),
    ('ArH2, what HBI saturation builds',
     '1 Ar u0 p3 c0 {2,S} {3,S}\n2 H u0 p0 c0 {1,S}\n3 H u0 p0 c0 {1,S}\n'),
]
hand_numbers = []
for name, adj in HAND_BUILT:
    try:
        mol = Molecule().from_adjacency_list(adj)
    except Exception as exc:                                        # noqa: BLE001
        print("  UNBUILDABLE  %-52s %s: %s" % (name, type(exc).__name__, str(exc)[:110]))
        continue
    try:
        types = [a.atomtype.label for a in mol.atoms]
    except Exception as exc:                                        # noqa: BLE001
        types = 'NO ATOM TYPE (%s)' % type(exc).__name__
    verdict, payload = thermo_verdict(mol)
    print("\n  %-52s types=%s" % (name, types))
    if verdict == 'NUMBER':
        hand_numbers.append((name, payload))
        print("      NUMBER  H298 = %.4f kJ/mol  S298 = %.4f  src = %s"
              % (payload.get_enthalpy(298.15) / 1000.0, payload.get_entropy(298.15),
                 (payload.comment or '').strip().replace('\n', ' / ')[:120]))
    else:
        print("      CRASH   %s: %s" % (type(payload).__name__, str(payload)[:150]))

banner("5. THE ANSWER")
print("  first-generation products that got a NUMBER : %d" % len(gen1_numbers))
for key, fam, label, _ in gen1_numbers:
    print("      %s   via %s + %s" % (key, fam, label))
print("  first-generation products that CRASHED      : %d" % len(gen1_crashes))
print("  second-generation argon products NUMBERED   : %d" % len(gen2_numbers))
for key, fam, how, _ in gen2_numbers:
    print("      %s   via %s (%s)" % (key, fam, how))
print("  reactions where EVERY product numbers       : %d" % len(fully_numbered))
for rxn in fully_numbered:
    print("      %s   (%s)" % (rxn, rxn.family))
print("  hand-built argon structures that NUMBERED   : %d" % len(hand_numbers))
for name, _ in hand_numbers:
    print("      %s" % name)
sys.stdout.flush()
