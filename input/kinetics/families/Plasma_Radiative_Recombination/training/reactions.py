#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.

Empty on carry from branch `99`: this family holds no training data. The one
defensible number the family can return is the estimated top-node rule in
`rules.py`, derived from the sourced `PlasmaRadiativeRecombination` library (see
that file). A training reaction is deliberately NOT used for the estimate — see
the "WHY A RULE AND NOT A TRAINING REACTION" note in `rules.py`.

If real radiative-recombination training data arrives, note the representational
constraint that binds every plasma family training set: `add_rules_from_training`
accepts only plain `Arrhenius` (and the Surface* types); `BadnellRRArrhenius` raises
`NotImplementedError` and cannot be trained from here. The sourced per-species
rates therefore live in the `PlasmaRadiativeRecombination` library, not here.
"""
