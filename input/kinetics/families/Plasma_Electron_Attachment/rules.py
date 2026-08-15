#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Attachment/rules"
shortDesc = u""
longDesc = u"""
Rate rules for non-dissociative electron attachment, A + e- => A-.

This file is intentionally empty of hand-written rules: every rule for this
family is generated from the training set in `training/reactions.py` by
`KineticsFamily.add_rules_from_training`.

Every node of the group tree is reached by a training reaction - `Attacher` by
entry 3, `O_in_OH` by entry 2, `O_in_O2` by entry 1 - so `fill_rules_by_averaging_up`
creates nothing at all and no rule in this family is a derived number. A rule
written here would necessarily be a rate with no measurement behind it, handed
to whatever the tree happens to match; if a species needs a rate, give it a
training reaction and a group, not a rule here.
"""
