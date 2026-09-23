#!/usr/bin/env python
# encoding: utf-8
"""
Does the reachability found by ``all_family_reachability_probe.py`` actually terminate a
job, and can anything on the database side stop it?

Two questions, both answered against the shipped engine code rather than by reading it:

1. **Does a real model-enlargement path raise?** ``CoreEdgeReactionModel.process_new_reactions``
   is the function ``enlarge`` calls for every generated reaction. It is run here on the
   ``Ar(3P2) + H`` reaction that ``Birad_R_Recombination`` generates, with nothing patched.

2. **Could a quarantine manifest have caught it?** The quarantine gate fires in
   ``apply_kinetics_to_reaction``. If product thermo is generated BEFORE that call, then no
   manifest on any of the ordinary families can prevent the crash, and "quarantine the
   families that turned red" is not an available fix. The ordering is measured by
   instrumenting both functions on the live class and recording which runs first.

NEGATIVE CONTROL. The same two steps are run for ``CH3 + H``, an ordinary reaction that must
go through cleanly. If the control raises, the probe is measuring its own setup.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/job_level_crash_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/job_level_crash_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/job_level_crash_probe.stderr.log >&2)
"""

import logging
import os
import sys
import traceback

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = DATABASE

from rmgpy.data.rmg import RMGDatabase                     # noqa: E402
from rmgpy.molecule import Molecule                        # noqa: E402
from rmgpy.rmg.model import CoreEdgeReactionModel          # noqa: E402
from rmgpy.species import Species                          # noqa: E402

logging.getLogger().setLevel(logging.CRITICAL)

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
H = 'multiplicity 2\n1 H u1 p0 c0\n'
CH3 = ('multiplicity 2\n1 C u1 p0 c0 {2,S} {3,S} {4,S}\n2 H u0 p0 c0 {1,S}\n'
       '3 H u0 p0 c0 {1,S}\n4 H u0 p0 c0 {1,S}\n')

#: The families a plain combustion deck gets. Read from the database's own file rather than
#: retyped, so this cannot drift away from what RMG would load.
RECOMMENDED = {}
with open(os.path.join(DATABASE, 'kinetics', 'families', 'recommended.py'),
          encoding='utf-8') as handle:
    exec(handle.read(), RECOMMENDED)                        # noqa: S102
DEFAULT_SET = RECOMMENDED['default']


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def species(adj, label):
    return Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])


banner("0. ARE THE MATCHING FAMILIES IN THE DEFAULT SET A DECK ACTUALLY GETS?")
MATCHED = ['Birad_R_Recombination', 'R_Addition_MultipleBond', 'Disproportionation',
           'CO_Disproportionation', 'Cl_Abstraction']
print("  families in recommended.py 'default': %d" % len(DEFAULT_SET))
for fam in MATCHED:
    print("    %-26s in default: %s" % (fam, fam in DEFAULT_SET))
print("  matched families that a default deck loads: %d of %d"
      % (sum(1 for f in MATCHED if f in DEFAULT_SET), len(MATCHED)))

banner("1. LOAD THE DEFAULT FAMILY SET, PLUS THE ONE PLASMA FAMILY")
db = RMGDatabase()
db.load(path=DATABASE,
        thermo_libraries=['primaryThermoLibrary', 'PlasmaExcitedNeutralThermo',
                          'PlasmaCationThermo'],
        kinetics_families=sorted(DEFAULT_SET),
        reaction_libraries=[], seed_mechanisms=[], kinetics_depositories=['training'],
        depository=False, solvation=True, surface=False)
print("  families loaded: %d" % len(db.kinetics.families))

banner("2. ORDERING: WHICH RUNS FIRST, PRODUCT THERMO OR THE QUARANTINE GATE?")
order = []
orig_generate_thermo = CoreEdgeReactionModel.generate_thermo
orig_apply_kinetics = CoreEdgeReactionModel.apply_kinetics_to_reaction


def traced_generate_thermo(self, spc, rename=False):
    order.append('generate_thermo(%s)' % spc)
    return orig_generate_thermo(self, spc, rename=rename)


def traced_apply_kinetics(self, reaction):
    order.append('apply_kinetics_to_reaction(%s)' % reaction)
    return orig_apply_kinetics(self, reaction)


CoreEdgeReactionModel.generate_thermo = traced_generate_thermo
CoreEdgeReactionModel.apply_kinetics_to_reaction = traced_apply_kinetics


def enlarge_on(reactants, label):
    """Run the shipped enlargement path on one reactant pair. Nothing is patched except
    the two tracers above, which only record."""
    del order[:]
    cerm = CoreEdgeReactionModel()
    cerm.kinetics_estimator = 'rate rules'
    rxns = db.kinetics.generate_reactions_from_families(reactants, products=None,
                                                        resonance=True)
    print("\n  %s -> %d reaction(s) generated" % (label, len(rxns)))
    for rxn in rxns:
        print("      %-26s %s" % (rxn.family, rxn))
    if not rxns:
        return None
    try:
        cerm.process_new_reactions(rxns, reactants[0])
    except Exception as exc:                                        # noqa: BLE001
        print("  process_new_reactions RAISED %s" % type(exc).__name__)
        print("      %s" % str(exc)[:220])
        traceback.print_exc()
        return exc
    print("  process_new_reactions completed with no exception")
    return None


banner("3. NEGATIVE CONTROL: CH3 + H through the same path")
control = enlarge_on([species(CH3, 'CH3'), species(H, 'H')], 'CH3 + H')
print("  call order recorded: %s" % ' -> '.join(o.split('(')[0] for o in order[:6]))
control_order = list(order)
if control is not None:
    print("  *** CONTROL RAISED. Everything below is unreliable. ***")
else:
    print("  control clean, so a raise below belongs to the chemistry and not the setup")

banner("4. THE REAL CASE: Ar(3P2) + H through the same path")
real = enlarge_on([species(AR_META, 'Ar(3P2)'), species(H, 'H')], 'Ar(3P2) + H')
print("  call order recorded: %s" % ' -> '.join(o.split('(')[0] for o in order[:6]))

CoreEdgeReactionModel.generate_thermo = orig_generate_thermo
CoreEdgeReactionModel.apply_kinetics_to_reaction = orig_apply_kinetics

banner("5. WHAT THIS SETTLES")
first_control = control_order[0].split('(')[0] if control_order else '(none)'
print("  first call in the control run          : %s" % first_control)
print("  Ar(3P2) + H raised                     : %s"
      % (type(real).__name__ if real is not None else 'NOTHING'))
print("  a kinetics quarantine could stop it    : %s"
      % ('NO - product thermo runs first' if first_control == 'generate_thermo'
         else 'possibly - check the order above'))
print("  matched families inside the default set: %d of %d"
      % (sum(1 for f in MATCHED if f in DEFAULT_SET), len(MATCHED)))
sys.stdout.flush()
