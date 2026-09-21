#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Impact_Ionization/quarantine"

# The campaign state, verbatim, and the same string Cation_R_Recombination uses so both
# refusals grep as one class of event. RMG quotes it back in the refusal.
state = "QUARANTINED FOR QUANTITATIVE PLASMA USE"

# The criterion. `applies_to` is an isinstance test, so this covers every kinetics class
# this family can currently hand to a model.
#
# It must be KineticsModel and NOT Arrhenius. A rate rule is returned as `ArrheniusEP`,
# which `fix_barrier_height` then converts to a plain `Arrhenius` -- and ArrheniusEP is
# NOT a subclass of Arrhenius (measured: both derive straight from KineticsModel). An
# `Arrhenius` criterion would therefore catch the converted form and miss the form the
# rate actually arrives in at the one gate that fires before `reaction.kinetics` is
# bound, making the refusal silently dependent on where in the pipeline it was checked.
#
# It would also cover nothing on the data side. The root rule below is WRITTEN as an
# `Arrhenius` in rules.py and is an `ArrheniusEP` once loaded, so `affected_entries`
# under an `Arrhenius` criterion reports 0 of 1 rules -- a manifest that looks right in
# the file and gates nothing. Measured, not assumed; it is pinned in the tests.
appliesToKineticsClass = "KineticsModel"

reason = "estimated rates reach the solver without uses_electron_temperature and are evaluated at the GAS temperature"

# ---------------------------------------------------------------------------
# I-221 -- why this family is quarantined, and what it is NOT saying.
#
# This is NOT a provenance quarantine. It says nothing against the family's
# chemistry, its groups, its tree, or the sourced Voronov lithium datum the single
# rank-10 root rule was generalised from. Those are all as good as they were.
#
# The defect is in DELIVERY, and it is in the engine rather than in this database.
# A rate this family supplies as an ESTIMATE cannot carry electron-temperature
# dependence to the solver, because no estimate can: only four kinetics classes set
# `uses_electron_temperature` anywhere in rmgpy/kinetics/arrhenius.pyx --
# TwoTemperaturePlasma, ElectronCollisionPlasma, BadnellRRArrhenius,
# VoronovEIArrhenius -- and none of them is a superclass of Arrhenius or of
# ArrheniusEP, so the flag can never be inherited by an estimated rate.
# PlasmaReactor.generate_rate_coefficients branches on
# `getattr(kin, 'uses_electron_temperature', False)` (rmgpy/solver/plasma.pyx:875)
# and the else branch evaluates at `self.T`, the gas temperature (:886). A check
# whose default is False fails silently: no raise, just a wrong number.
#
# Measured for the reaction this family generates for metastable argon,
# Ar(3P2) + e- => Ar+ + 2 e-, through real model admission and real reactor
# initialisation (docs/argon-metastable-thermo/report.md sections 13.1-13.3, probe
# and logs beside it):
#
#     delivered, 1000 K gas            3.664598e-14 m^3/(mol*s)
#     delivered, 300 K gas             1.933634e-64 m^3/(mol*s)
#     Te = 1 eV vs Te = 3 eV           bit-identical -- Te does not reach the rate
#     this family's OWN rule at 3 eV   3.109200e+07 m^3/(mol*s)
#     ratio at 1000 K                  20.9 orders of magnitude LOW
#
# The THIRD line is the whole justification and it needs no external comparison: an
# electron-impact ionisation rate that does not depend on the electron temperature
# is disqualified by inspection. The fourth and fifth lines are scale, and they are
# deliberately INTERNAL -- this family's own rule evaluated at the Te it never sees,
# against what the solver actually delivers. Nothing outside this repository is
# needed to read either of them.
#
# An earlier version of this manifest carried "published state-resolved model
# 2.0583e+10 m^3/(mol*s)" and a 23.7-order shortfall. That constant had NO citation
# anywhere in this repository and is withdrawn rather than reworded. It is not
# replaced by another external number: a state-resolved 1s5 expression of the usual
# shape, 6.8e-15 * Te^0.67 * exp(-4.2/Te), gives 2.108e9 m^3/(mol*s) at 3 eV read as
# m^3/s and 2.108e3 read as cm^3/s, and only the source can say which. Six orders
# turning on a unit convention is exactly why an uncited comparator has no place in
# an argument about orders of magnitude. The quarantine never rested on it.
#
# The Te-independence line is also the one that matters for lifting: re-anchoring the
# placeholder to a better source would not move the delivered number at all, because
# the two-temperature machinery the whole plasma engine exists to carry never reaches
# an estimate. Provenance is not what is wrong here, which is why no refit lifts this.
# ---------------------------------------------------------------------------

#: Stated positively so nobody has to infer it from an absence. This IS a plasma
#: family and it is quarantined *because of* how plasma rates are delivered, not
#: because it was misfiled as one.
isPlasmaFamily = True

#: What it costs. KineticsModel is blunt on purpose and this is the price: it also
#: refuses a future *correct* VoronovEIArrhenius rule added to this family. No single
#: criterion can express "anything that is not one of the four safe classes", because
#: those four are siblings rather than a branch. The bluntness is judged acceptable and
#: arguably correct -- the family today holds exactly one rank-10 placeholder rule and
#: an empty training set, and whoever adds a genuinely Te-dependent rule should have to
#: come back to this file and say so.
criterionIsBlunt = True

shortDesc = """Estimated rates from this family are delivered to the solver as ordinary Arrhenius and evaluated at the gas temperature, with no dependence on Te at all -- ~21 orders below this family's own rule evaluated at Te"""

longDesc = """
What refuses and what does not. The family stays registered, still generates reactions,
and its rule, its tree and its groups are untouched. `get_rate_coefficient` still
evaluates. Only admission to a quantitative RMG reaction model refuses -- at
`apply_kinetics_to_reaction` (rmgpy/rmg/model.py), which fires before
`reaction.kinetics` is bound and before the edge, so a refused reaction is left exactly
as generated and a bad rate cannot steer enlargement from the edge either.

Why refusing is better than the alternatives here. The delivered number is not wrong by
a factor that a careful reader would notice; it is ~1e-21 of this family's own rule
evaluated at the electron temperature, and it is stable against the one input a plasma
modeller would vary to test it. A run that
admitted it would converge, report success, and declare electron-impact ionisation of
the metastable an unimportant channel -- which is the specific failure this whole
mechanism exists to prevent.

Explicitly NOT done, because each would let a run report success on a mechanism that is
quietly wrong: substituting a Te-evaluated rate by hand, re-anchoring the placeholder to
a better source (it changes nothing -- see above), forcing the estimate into a
TwoTemperaturePlasma shell so it inherits the flag, evaluating at an assumed Te,
dropping the reaction after generation, or marking it irreversible and continuing.

LIFTING THIS. Delete this file. Do that when EITHER of the following is true, and not
before:

  1. The engine carries electron-temperature dependence to estimated rates -- i.e. a
     rate this family estimates arrives at PlasmaReactor with
     `uses_electron_temperature` True, and changing Te changes the delivered
     coefficient. This is an RMG-Py fix and is tracked as its own ticket by the
     campaign owner; it is NOT a database change and cannot be made from here.
  2. This family's rates stop being estimates -- every reaction it can produce is
     supplied by one of the four flag-carrying classes. Note that this alone does not
     currently release the criterion, since KineticsModel covers those too; a release
     under this condition means narrowing or deleting this manifest deliberately, with
     the delivered rate re-measured to prove it.

Neither condition is "a run was inconvenient".

See rmgpy/data/kinetics/quarantine.py in RMG-Py for the loader and the gate, and
input/kinetics/families/Cation_R_Recombination/quarantine.py for the precedent. That
file's note that the loader is absent from RMG-Py-plasma is STALE: the loader is present
in both RMG-Py-plasma and RMG-Py-i222-metastable-argon-atomtype as of I-221, and is
absent only from the shared RMG-Py primary checkout, which is on an unrelated branch.

Evidence, tests and the measurement behind every number above:
docs/argon-metastable-thermo/report.md (sections 13.1-13.3) and
test/test_eii_quarantine.py.
"""
