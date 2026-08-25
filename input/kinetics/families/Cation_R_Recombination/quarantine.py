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
"""
