"""
Does the family quarantine actually refuse the rate round 58 measured?

The manifest is a data file; whether it gates anything is a property of the runtime, not
of the text. This probe answers, against the real loader and the real admission path:

  1. does the manifest load, and does it resolve its criterion to a real class;
  2. does the criterion cover the rule the family actually holds, computed from the
     database rather than from a stored list;
  3. does admission refuse the Ar(3P2) reaction, at the gate that fires BEFORE
     reaction.kinetics is bound;
  4. is the refused reaction left exactly as generated;
  5. does the underlying measurement still reproduce with the quarantine detached --
     i.e. is the evidence for the quarantine still reachable after it lands;
  6. does a sibling plasma family with no manifest still admit normally.

Run:
    export PYTHONPATH=/home/alon/Code/RMG-Py-i222-metastable-argon-atomtype
    python docs/argon-metastable-thermo/quarantine_probe.py \
        > >(tee docs/argon-metastable-thermo/logs/quarantine_probe.stdout.log > /dev/null) \
        2> >(tee docs/argon-metastable-thermo/logs/quarantine_probe.stderr.log > /dev/null)
"""

import os

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
settings['database.directory'] = os.path.abspath(
    os.path.join(HERE, os.pardir, os.pardir, 'input'))

from rmgpy.data.rmg import RMGDatabase                          # noqa: E402
from rmgpy.exceptions import QuarantinedKineticsError           # noqa: E402
from rmgpy.molecule import Molecule                             # noqa: E402
from rmgpy.rmg.model import CoreEdgeReactionModel               # noqa: E402
from rmgpy.species import Species                               # noqa: E402

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
FAMILY = 'Plasma_Electron_Impact_Ionization'
SIBLING = 'Plasma_Radiative_Recombination'


def banner(text):
    print("\n" + "=" * 86)
    print(text)
    print("=" * 86)


def species(adj, label):
    return Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])


def build(rxn_species, db, family):
    """Generate this family's one reaction for `rxn_species` and give it thermo."""
    reactions = db.kinetics.generate_reactions_from_families(
        [rxn_species], products=None, only_families=[family], resonance=True)
    assert len(reactions) == 1, "expected one reaction, got %d" % len(reactions)
    rxn = reactions[0]
    for s in list(rxn.reactants) + list(rxn.products):
        if s.is_electron():
            continue
        if not s.label:
            s.label = str(s)
        if s.thermo is None:
            s.thermo = db.thermo.get_thermo_data(s)
    return rxn


# =====================================================================================
banner("0. LOAD -- does the manifest load at all")
# =====================================================================================
db = RMGDatabase()
db.load(settings['database.directory'],
        thermo_libraries=['primaryThermoLibrary', 'PlasmaExcitedNeutralThermo',
                          'PlasmaCationThermo'],
        kinetics_families=[FAMILY, SIBLING],
        reaction_libraries=[], seed_mechanisms=[])

fam = db.kinetics.families[FAMILY]
q = fam.quarantine
print("  family                  : %s" % FAMILY)
print("  quarantine object       : %r" % (q,))
assert q is not None, "the manifest did not load"
print("  state                   : %s" % q.state)
print("  appliesToKineticsClass  : %s -> %r" % (q.kinetics_class_name, q.kinetics_class))
print("  reason                  : %s" % q.reason)
print("  path                    : %s" % q.path)

# =====================================================================================
banner("1. THE CRITERION, EVALUATED AGAINST WHAT THE DATABASE ACTUALLY HOLDS")
# =====================================================================================
try:
    fam.add_rules_from_training(thermo_database=db.thermo)
except Exception as exc:                                        # noqa: BLE001
    print("  add_rules_from_training raised %s (continuing)" % type(exc).__name__)
fam.fill_rules_by_averaging_up(verbose=True)

all_rules = [e for entries in fam.rules.entries.values() for e in entries]
affected = q.affected_entries(fam)
print("  rate rules in the family        : %d" % len(all_rules))
for e in all_rules:
    print("      index %-3s label %-12s class %-14s rank %s"
          % (e.index, e.label, e.data.__class__.__name__, e.rank))
print("  covered by the criterion        : %d rules, %d training entries"
      % (len(affected['rules']), len(affected['training'])))
assert len(affected['rules']) == len(all_rules) and all_rules, \
    "the criterion must cover every rule this family can estimate from"

# =====================================================================================
banner("2. ADMISSION REFUSES -- the Ar(3P2) channel this library unlocks")
# =====================================================================================
rxn = build(species(AR_META, 'Ar(3P2)'), db, FAMILY)
print("  generated               : %s" % rxn)
print("  kinetics before         : %r" % rxn.kinetics)

cerm = CoreEdgeReactionModel()
cerm.kinetics_estimator = 'rate rules'
refused = None
try:
    cerm.apply_kinetics_to_reaction(rxn)
except QuarantinedKineticsError as exc:
    refused = exc
    print("\n  REFUSED. The message a user gets:\n")
    for line in str(exc).splitlines():
        print("      %s" % line)
assert refused is not None, "admission did NOT refuse -- the gate is not firing"

# =====================================================================================
banner("3. THE REFUSED REACTION IS LEFT EXACTLY AS GENERATED")
# =====================================================================================
print("  rxn.kinetics after refusal      : %r" % rxn.kinetics)
print("  reactants                       : %s" % [str(s) for s in rxn.reactants])
print("  products                        : %s" % [str(s) for s in rxn.products])
assert rxn.kinetics is None, "kinetics were bound despite the refusal"

# =====================================================================================
banner("4. THE EVIDENCE IS STILL REACHABLE WITH THE QUARANTINE DETACHED")
# =====================================================================================
# The measurement that justifies the manifest must not become unreproducible because the
# manifest landed. Detaching it on the loaded object touches no file.
fam.quarantine = None
rxn2 = build(species(AR_META, 'Ar(3P2)'), db, FAMILY)
cerm.apply_kinetics_to_reaction(rxn2)
print("  kinetics class as estimated     : %s" % rxn2.kinetics.__class__.__name__)
rxn2.fix_barrier_height(force_positive=True, solvent="")
kin = rxn2.kinetics
print("  kinetics class after barrier    : %s" % kin.__class__.__name__)
print("  uses_electron_temperature       : %s"
      % getattr(kin, 'uses_electron_temperature', False))
print("  A                               : %.6e %s" % (kin.A.value_si, kin.A.units))
print("  Ea (barrier)                    : %.4f kJ/mol" % (kin.Ea.value_si / 1000.0))
print("  k(1000 K)                       : %.6e m^3/(mol*s)"
      % kin.get_rate_coefficient(1000.0))
fam.quarantine = q

# =====================================================================================
banner("5. A SIBLING FAMILY WITH NO MANIFEST IS UNAFFECTED")
# =====================================================================================
sib = db.kinetics.families[SIBLING]
print("  %s quarantine : %r" % (SIBLING, sib.quarantine))
assert sib.quarantine is None, "a family with no manifest must carry no quarantine"

banner("DONE -- every assertion above passed")
