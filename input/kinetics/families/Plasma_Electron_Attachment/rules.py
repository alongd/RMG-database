#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Electron_Attachment/rules"
shortDesc = u""
longDesc = u"""
Rate rules for non-dissociative electron attachment, A + e- => A-.

This file is intentionally empty of hand-written rules: every rule for this
family is generated from the training set in `training/reactions.py` by
`KineticsFamily.add_rules_from_training`.

Every L2 node of the group tree is reached by its own training reaction -
`O_atom` by entry 3, `O_in_OH` by entry 2, `O_in_O2` by entry 1 - so every rule
a species can actually be given is an exact training hit, not a derived number.

`fill_rules_by_averaging_up` does create one derived rule, on the root
`Attacher`, and that rule is a mean of a pressure-baked effective coefficient
and a radiative one - not a rate coefficient of any kind. It is tolerated
because no *generated* reaction can be given it: the root is a LogicOr whose
members are exactly its L2 children, so every structure the root admits matches
a child and `descend_tree` never stops at the root. That identity is an
invariant of `groups.py`, pinned by
test/test_plasma_electron_attachment.py::test_no_union_member_lacks_an_l2_child.

It is not unreachable in the wider sense, and this file should not be read as
claiming that: `get_kinetics_for_template(retrieve_template(['Attacher']))`
returns it on request. Asking a family root for its averaged rule by name is a
general property of the rate-rule API, not something a database entry can
prevent.

A rule written by hand here would necessarily be a rate with no measurement
behind it, handed to whatever the tree happens to match; if a species needs a
rate, give it a training reaction, a group *and* an L2 node - not a rule here.
"""
