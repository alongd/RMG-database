#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkaline_Alkaline/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.5.
This family describes reactions of the sort:

A + B <=> AB+ + e-

Reference:
[Aiken2025] T.T. Aiken, I.D. Boyd, I.V. Adamovich, Phys. Plasmas 2025, 32, 103512. DOI: 10.1063/5.0294530

ORPHANED ENTRY -- READ BEFORE USING THIS DEPOSITORY (I-224).
Entry 1, O_A + O_B <=> O2p, is no longer reachable by this family. I-224 narrowed both top groups
from `R u[2,3,4] px cx` to `alkaline u2 px cx` so that the family stops generating reactions for
every species carrying a 2-4 radical atom. `alkaline` is Mg and Ca only, so oxygen is outside the
family's template and entry 1 cannot be generated from it. Measured: with the narrowed tops the
family generates 0 reactions from O + O, against 2 before.

The entry is kept, not deleted, and its rate is untouched. O + O <=> O2+ + e- is real associative
ionization with a rank-6 literature rate, and deleting it would lose sourced data to make a check
go green. It needs a home in a family named for that chemistry. That family cannot be built by
naming O in a group that GAIN_CHARGE acts on -- `ATOMTYPES['O']` carries no `increment_charge`
action, so such a group raises ActionError at load (see the groups.py longDesc). Giving the oxygen
atom types a charge row in RMG-Py is the prerequisite, and it is owned outside this ticket.

Until then this entry is inert: it produces no rate rule for this family, and any run that calls
`add_rules_from_training` on this family should be checked against the measurement recorded in
docs/i224-alkaline-family-top/report.md.
"""

entry(
    index = 1,
    label = "O_A + O_B <=> O2p",
    degeneracy = 2,
    kinetics=Arrhenius(A=(1.82e10, 'cm^3/(mol*s)'), n=0.6797, Ea=(160336, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2025]",
    longDesc = u"""
Table VIII
Associative ionization

ORPHANED by I-224: oxygen is outside the narrowed `alkaline u2 px cx` top groups, so this family
can no longer generate this reaction. Rate and rank are untouched. See the depository longDesc
above for why it is kept and what would give it a home.
"""
)

entry(
    index = 2,
    label = "Mg_A + Mg_B <=> Mg2p",
    degeneracy = 2,
    kinetics=Arrhenius(A=(6.02e13, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)

entry(
    index = 3,
    label = "Ca_A + Ca_B <=> Ca2p",
    degeneracy = 2,
    kinetics=Arrhenius(A=(1.87e13, 'cm^3/(mol*s)'), n=0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""
"""
)
