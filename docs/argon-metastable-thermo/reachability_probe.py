#!/usr/bin/env python
# encoding: utf-8
"""
Is metastable argon actually unreachable? -- I-221 round 55, HIGH-2.

The original report claimed the species is an inert island because no kinetics file MENTIONS
it. That test was grep over kinetics files for the literal adjacency text. Families do not
match on literals, they match on GROUPS, so a literal search can never establish that no
family matches a species. The only way to settle it is to generate reactions and look.

This probe runs every plasma family in the database against Ar(3P2) and reports what comes
back, including the provenance and rank of any rate it is handed. It also runs the same
question at the process_thermo_data level, so the E0/temperature-range measurements happen
against a fully loaded database rather than the half-loaded one a thermo-only probe gets.

Run:

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/reachability_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/reachability_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/reachability_probe.stderr.log >&2)
"""

import os

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
settings['database.directory'] = os.path.abspath(
    os.path.join(HERE, os.pardir, os.pardir, 'input'))

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402
from rmgpy.data.rmg import RMGDatabase                      # noqa: E402
from rmgpy.molecule import Molecule                         # noqa: E402
from rmgpy.species import Species                           # noqa: E402
from rmgpy.thermo import NASA                               # noqa: E402

T0 = 298.15
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
AR = '1 Ar u0 p4 c0\n'

PLASMA_FAMILIES = ['Plasma_Electron_Impact_Ionization',
                   'Plasma_Electron_Attachment',
                   'Plasma_Radiative_Recombination',
                   'Plasma_Associative_Ionization_Alkali_Alkali',
                   'Plasma_Associative_Ionization_Alkali_Alkaline',
                   'Plasma_Associative_Ionization_Alkaline_Alkaline']


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def sub(text):
    print("\n  " + text)
    print("  " + "-" * len(text))


def species(adj, label):
    return Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])


# =====================================================================================
banner("1. WHAT EVERY PLASMA FAMILY MAKES OF Ar u2 p3 c0")
# =====================================================================================
kdb = KineticsDatabase()
kdb.load_families(os.path.join(settings['database.directory'], 'kinetics', 'families'),
                  families=PLASMA_FAMILIES, depositories=['training'])
for name in PLASMA_FAMILIES:
    fam = kdb.families.get(name)
    if fam is None:
        print("  %-48s NOT LOADED" % name)
        continue
    try:
        fam.add_rules_from_training(thermo_database=None)
        fam.fill_rules_by_averaging_up(verbose=True)
    except Exception as exc:                                       # noqa: BLE001
        print("  %-48s rule build raised %s" % (name, type(exc).__name__))

total = 0
for name in PLASMA_FAMILIES:
    if name not in kdb.families:
        continue
    reactions = kdb.generate_reactions_from_families(
        [species(AR_META, 'Ar(3P2)')], products=None, only_families=[name], resonance=True)
    total += len(reactions)
    print("\n  %-48s -> %d reaction(s)" % (name, len(reactions)))
    for rxn in reactions:
        print("      %s" % rxn)
        template = getattr(rxn, 'template', None) or []
        print("      family=%s  template=%s  degeneracy=%s  electrons=%s  reversible=%s"
              % (rxn.family,
                 [getattr(g, 'label', g) for g in template],
                 getattr(rxn, 'degeneracy', None),
                 getattr(rxn, 'electrons', None),
                 rxn.reversible))
        print("      products: %s"
              % [(s.label, s.molecule[0].to_adjacency_list().strip().replace('\n', ' | '))
                 for s in rxn.products])
        k = rxn.kinetics
        print("      kinetics: %s" % (repr(k)[:200] if k is not None else None))
        if k is not None and getattr(k, 'A', None) is not None:
            print("      A = %.6e %s" % (k.A.value_si, k.A.units))
            print("      comment: %s" % (k.comment or '').strip().replace('\n', ' / '))

print("\n  TOTAL reactions generated from Ar(3P2) across the plasma families: %d" % total)

# =====================================================================================
banner("2. THE PROVENANCE OF THE RATE THAT CHANNEL IS HANDED")
# =====================================================================================
fam = kdb.families.get('Plasma_Electron_Impact_Ionization')
if fam is not None:
    sub("2a. every rate rule in the family")
    for label, entries in sorted(fam.rules.entries.items()):
        for e in entries:
            print("    node %-12s rank %-3s  %s"
                  % (label, e.rank, (e.short_desc or '').strip().replace('\n', ' ')))
            long_desc = (e.long_desc or '').strip()
            if long_desc:
                for line in long_desc.splitlines():
                    if line.strip():
                        print("        | %s" % line.strip())
            if getattr(e.data, 'A', None) is not None:
                print("        A = %.6e %s" % (e.data.A.value_si, e.data.A.units))

    sub("2b. the family's training depository")
    dep = fam.get_training_depository() if hasattr(fam, 'get_training_depository') else None
    if dep is not None:
        for _idx, e in sorted(dep.entries.items()):
            print("    training %-4s %s" % (_idx, e.label))
            print("             %s" % (e.short_desc or '').strip().replace('\n', ' '))

# =====================================================================================
banner("3. THE SAME QUESTIONS, AGAINST A FULLY LOADED DATABASE")
# =====================================================================================
full = RMGDatabase()
full.load(settings['database.directory'],
          thermo_libraries=None,
          kinetics_families=['Plasma_Electron_Impact_Ionization'],
          reaction_libraries=[],
          seed_mechanisms=[],
          kinetics_depositories=['training'],
          depository=False,
          solvation=True,
          surface=False)

from rmgpy.thermo.thermoengine import process_thermo_data      # noqa: E402

sub("3a. process_thermo_data on the entry -- E0 and the surviving temperature range")
spc = species(AR_META, 'Ar(3P2)')
resolved = full.thermo.get_thermo_data(spc)
print("    library returns %s : %s"
      % (type(resolved).__name__, (resolved.comment or '').strip()))
print("    stored ThermoData.E0            : %s"
      % ("%.4f kJ/mol" % (resolved.E0.value_si / 1000.0) if resolved.E0 is not None
         else "None"))
nasa = process_thermo_data(spc, resolved, thermo_class=NASA)
print("    processed to %s, Tmin = %.1f K, Tmax = %.1f K"
      % (type(nasa).__name__, nasa.Tmin.value_si, nasa.Tmax.value_si))
print("    NASA.E0                         : %.4f kJ/mol" % (nasa.E0.value_si / 1000.0))
print("    spc.conformer.E0                : %.4f kJ/mol" % (spc.conformer.E0.value_si / 1000.0))
for T in (298.15, 1000.0, 5000.0, 6000.0):
    try:
        print("      NASA at %7.2f K: Cp = %8.4f  S = %9.4f  H = %10.4f"
              % (T, nasa.get_heat_capacity(T), nasa.get_entropy(T),
                 nasa.get_enthalpy(T) / 1000.0))
    except Exception as exc:                                       # noqa: BLE001
        print("      NASA at %7.2f K RAISED %s: %s"
              % (T, type(exc).__name__, str(exc).strip().splitlines()[0]))

sub("3b. the conformer's electronic degeneracy after normal processing")
conf = spc.conformer
print("    conformer type                  : %s" % type(conf).__name__)
print("    conformer.spin_multiplicity     : %s" % conf.spin_multiplicity)
print("    conformer.optical_isomers       : %s" % conf.optical_isomers)
print("    molecule.multiplicity           : %s" % spc.molecule[0].multiplicity)
print("    g this entry's S298 assumes     : 5   (2J+1, J = 2)")

sub("3c. explicit statmech generation, with the statmech database loaded")
spc2 = species(AR_META, 'Ar(3P2)')
spc2.thermo = full.thermo.get_thermo_data(spc2)
try:
    spc2.generate_statmech()
    c = spc2.conformer
    print("    generate_statmech spin_multiplicity : %s" % c.spin_multiplicity)
    print("                      optical_isomers   : %s" % c.optical_isomers)
    print("                      modes             : %s" % c.modes)
    print("                      Q(298.15)         : %s"
          % (c.get_partition_function(T0) if c.modes else '<no modes>'))
except Exception as exc:                                           # noqa: BLE001
    print("    generate_statmech RAISED %s: %s"
          % (type(exc).__name__, str(exc).strip().splitlines()[0]))

sub("3d. the ground state, for contrast: it is a NASA in the library")
ar = species(AR, 'Ar')
ar_resolved = full.thermo.get_thermo_data(ar)
print("    Ar resolves to %s : %s"
      % (type(ar_resolved).__name__, (ar_resolved.comment or '').strip()))
ar_nasa = process_thermo_data(ar, ar_resolved, thermo_class=NASA)
print("    processed to %s, Tmin = %.1f K, Tmax = %.1f K"
      % (type(ar_nasa).__name__, ar_nasa.Tmin.value_si, ar_nasa.Tmax.value_si))
print("    -> a library entry that is ALREADY a NASA is kept verbatim")
print("       (thermoengine.py:93-99); a ThermoData is refitted to 100-5000 K.")
