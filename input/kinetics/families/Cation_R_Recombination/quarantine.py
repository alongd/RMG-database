#!/usr/bin/env python
# encoding: utf-8

name = "Cation_R_Recombination/quarantine"

# The campaign state, verbatim. RMG quotes this string back in the refusal.
state = "QUARANTINED FOR QUANTITATIVE PLASMA USE"

# The criterion. RMG computes the affected set by testing every rate rule and every
# training entry of this family against this kinetics class, so this manifest never
# names an entry and cannot fall out of step with the data below it: add a Marcus
# entry and it is quarantined automatically, refit one to a different kinetics class
# and it is released automatically, renumber or relabel entries and nothing changes.
# The name is resolved against rmgpy.kinetics when the family loads -- a typo raises
# rather than quietly quarantining nothing.
appliesToKineticsClass = "Marcus"

reason = "electrochemical reference/domain unavailable"

# ---------------------------------------------------------------------------
# I-111 -- what this family actually is.
#
# Two limitations live here and they are SEPARATE. `state` above is the first:
# the plasma-domain exclusion, gated by the loader. `classification` below is the
# second: the provenance limitation, which survives even inside the SEI domain
# these rates were written for. A consumer that supplies an electrode and a
# reference lifts the first and still does not get validated data.
#
# The domain was recovered by I-111's evidence base, not guessed; see
# PROVENANCE.md beside this file for the recovered conditions, the mapping of the
# twelve database objects onto five underlying calculations, and the four facts
# that remain unresolved.
# ---------------------------------------------------------------------------

#: The provenance label, verbatim. NOT "validated", not even for SEI use.
classification = "LEGACY SEI ELECTROCHEMISTRY — INCOMPLETE QUANTITATIVE PROVENANCE"

#: The physical domain the rates were actually fitted in.
domain = "lithium-ion battery solid-electrolyte-interphase (SEI) electrochemistry"

#: Stated positively so no reader has to infer it from an absence. The reactions
#: carry electron metadata (`electrons = -1`, a LOSE_CHARGE recipe); that is
#: electrode electron transfer bookkeeping and is NOT evidence of free-electron
#: plasma chemistry.
isPlasmaFamily = False

#: The curated selections this family belongs in, in input/kinetics/families/
#: recommended.py. One entry, and it is the electrochemical one.
familySets = ["electrochem"]

#: Documentation beside the family, relative to this manifest.
provenance = "PROVENANCE.md"

shortDesc = """Marcus rates fitted as electrode electron-transfer; no electrochemical reference exists in a gas-phase or plasma mechanism"""

longDesc = """
These Marcus parameters were fitted to electrode electron-transfer rates. Evaluating
them in a gas-phase or plasma mechanism, where there is no electrode, no reference
potential, and no electrochemical domain, produces rate coefficients of 1e-23 to
1e-226 m^3/(mol*s) -- thirty to two hundred and thirty orders of magnitude below
anything physical. The rate law is being evaluated correctly; the evaluation has lost
the semantics of the source model. The number is not wrong by a factor, it is not the
quantity the data means.

Nothing here is deleted, repaired, refitted, or reinterpreted. The rates, the
reorganisation energies, the training reactions and their level of theory all stay
exactly as they were: they are the provenance evidence any recovery track needs, and
they remain valid for an electrode/electrolyte model that supplies the missing
reference. The family stays registered and still generates reactions; only admission
to a quantitative RMG reaction model refuses.

Explicitly NOT done, because each would let a run report success on a mechanism that
is quietly wrong: removing the reaction after generation, substituting an averaged
rule, evaluating at potential = 0, marking the reaction irreversible and continuing,
deriving a reverse rate, seeding a product or cation to bypass the channel, or
falling back on a generic collision rate.

Lifting the quarantine means deleting this file, and should happen only when the
electrochemical reference and domain these rates were fitted in are actually
available to the consumer -- not when a run is inconvenient.

See rmgpy/data/kinetics/quarantine.py in RMG-Py for the loader and the gate.

I-111 note on where the gate does and does not exist. The loader named above is
present in the RMG-Py worktree that landed it and is NOT present in every plasma
runtime -- `/home/alon/Code/RMG-Py-plasma` (branch `plasma`) has no
`rmgpy/data/kinetics/quarantine.py`, so under that runtime this manifest is an
inert data file and no refusal fires. Where the gate is absent, the plasma-domain
exclusion rests entirely on declared configuration: this family is a member of the
`electrochem` set and of no other set in recommended.py, so no plasma deck that
selects families by set can reach it. A plasma deck that names the family
individually bypasses both, and that residual is documented in
docs/i111-sei-reclassification.md rather than papered over.
"""
