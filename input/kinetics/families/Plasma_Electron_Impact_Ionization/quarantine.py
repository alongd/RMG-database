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

# ---------------------------------------------------------------------------
# ROUND 77 -- THE COMPATIBILITY PIN, AND THE HONEST SCOPE OF THIS MANIFEST.
#
# Raised in review: this quarantine is RUNTIME-DEPENDENT and the database said
# nothing about which runtime it needs. A manifest that is silently inert on the
# wrong engine is worse than no manifest, because the file reads like protection.
# So the requirement is now declared here, machine-readably, and
# test/test_eii_quarantine.py asserts the RUNNING engine satisfies it -- a run
# against an engine without the gate now fails loudly instead of proceeding
# unguarded.
#
# What is required of the engine:
#   * rmgpy.data.kinetics.quarantine, providing check_quarantine -- the function the
#     reaction model calls, not the one that reads this file; and
#   * KineticsFamily.quarantine populated at load (family.py:621-623, :699); and
#   * the refusal firing in apply_kinetics_to_reaction, i.e. at model admission.
# First provided by RMG-Py commit 541e6498f, 2026-08-25, "kinetics: hard-fail when
# quarantined database data reaches a reaction model". Present on RMG-Py-plasma and
# RMG-Py-i222-metastable-argon-atomtype; ABSENT from the shared RMG-Py primary
# checkout, which is on an unrelated branch.
#
# ROUND 80 -- WHAT IS ENFORCED, AND WHAT IS ONLY RECORDED. Review was right that until
# round 80 nothing read these three fields: the engine ignored them and only the
# database's own tests checked them, which confirms the runtime you happened to select
# and protects no actual run. The loader now HONOURS the two capability fields --
# `load_family_quarantine` imports the module, looks up the symbol, and refuses the load
# with a DatabaseError naming this family if either is absent. Two limits, stated so the
# word "pin" stays honest:
#   * `requiresEngineCommit` is NOT checked and is NOT a pin. An installed engine has no
#     reliable commit to compare against, and a check that passes on every checkout is a
#     check that cannot fail. It is PROVENANCE: the commit that first provided the
#     capability. The capability is the thing enforced.
#   * an engine old enough to lack the quarantine loader entirely never reads this file,
#     so it cannot be refused from here. That is bypass route 1 below, and it is why the
#     routes are enumerated rather than claimed closed.
#
# ROUND 87 -- THE PIN WAS WEAKER THAN ROUND 80 CLAIMED, AND IS NOW WHAT IT SAYS.
# Review reproduced three holes in the enforcement: a `requiresEngineSymbol` declared
# without a module was silently skipped; ANY non-None attribute satisfied the symbol
# check, so a manifest naming `math.pi` as its gate loaded clean; and symbol existence
# never showed the gate was REACHED from model admission. Round 80's "the pin is now
# real" was an overstatement -- it was realer. Three changes, all in the engine's loader,
# declared from here:
#   * the symbol must be CALLABLE, not merely present;
#   * `requiresEngineCallSites` names the module(s) that must bind that exact object, so
#     an engine that defines the gate and never wires it into the reaction model is
#     refused. Existence proves the capability was written; this proves it is reached;
#   * `requiresEngineCommit` is no longer DECLARABLE. Round 80 relabelled it as
#     provenance in prose while leaving the field name saying "requires", which is the
#     same defect one layer up -- a reader greps the name, not the comment. The engine
#     now refuses a manifest that declares it. The commit moves to
#     `recordedEngineCommit`, which the loader reads and logs as provenance, so the field
#     is not merely tolerated in silence.
requiresEngineModule = "rmgpy.data.kinetics.quarantine"
requiresEngineSymbol = "check_quarantine"
requiresEngineCallSites = ("rmgpy.rmg.model",)
recordedEngineCommit = "541e6498f"

# WHAT THIS MANIFEST DOES NOT COVER. Enumerated because a reader who believes the
# quarantine is a hard boundary will draw the wrong conclusion from a green run.
# Each of these reaches a solver with the same Te-independent rate and never passes
# the gate:
#   1. an engine WITHOUT the module above -- the family loads and is unguarded;
#   2. a direct database consumer (a script that calls generate_reactions and reads
#      .kinetics itself) -- the gate lives at model admission, not at the data;
#   3. a rate copied into a reaction library or seed mechanism by hand, with the
#      authorship comment stripped -- NARROWED in round 87, see below;
#   4. any consumer that reads rules.py as a file rather than through RMG.
# The quarantine is therefore a guard on ONE path -- the standard model-admission
# path -- and the defect it guards against is a property of the RATE, which travels
# wherever the number travels. The durable fix is the engine-side one in condition 1
# above, not this file.
#
# ROUND 87 NARROWED ROUTE 3, WHICH THIS FILE HAD WRITTEN OFF TOO EARLY. It read "that
# data is not this family and this manifest says nothing about it" -- treating a closable
# hole as a fact of life because the previous sentence had correctly identified the
# defect as a property of the rate. If the defect travels with the number, so must the
# refusal; what was missing was not the principle but the KEY. The engine gate used to
# resolve the family through `reaction.family`, and LibraryReaction overwrites that slot
# with the LIBRARY's label, so a quarantined rate copied into a seed was admitted (and,
# in the other direction, an innocent library named like a quarantined family was
# refused). The gate now resolves AUTHORSHIP -- the `family: <label>` line RMG writes
# into an estimated rate's comment and saves into the entry's longDesc -- so a copy made
# by RMG itself is now caught. What remains of route 3 is strictly smaller: a
# hand-written entry carrying no authorship at all, where there is genuinely nothing to
# read. The engine warns on exactly that case rather than guessing.
bypassRoutes = (
    "engine lacking rmgpy.data.kinetics.quarantine",
    "direct database consumer reading .kinetics without model admission",
    "hand-written library/seed entry with the authoring-family comment stripped",
    "consumer reading rules.py as a file",
)
