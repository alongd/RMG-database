#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Radiative_Recombination_Pairing/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Empty, deliberately, and for the same reason the sibling family's training set is
empty: the one sourced number this family could be trained on is the argon entry
in the `PlasmaRadiativeRecombination` reaction library, and putting it here as a
training reaction would duplicate — and be confusable with — data the library
already carries exactly. The estimate lives in `rules.py` as a hand-written root
rule instead, which keeps it structurally distinct from its own source.

There is also a representational bar: `add_rules_from_training` accepts only plain
`Arrhenius` (and the Surface* types). The argon entry is a `TwoTemperaturePlasma`,
which cannot be trained from here at all, so the sourced electron-temperature
dependence could not survive the trip even if the duplication were acceptable.
"""
