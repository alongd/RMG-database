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

ENTRY 1 WAS MOVED OUT BY I-224 -- IT WAS NOT DELETED.
Entry 1 was O_A + O_B <=> O2p, neutral associative ionization, rank 6, [Aiken2025] Table VIII. It
now lives verbatim, index included, at

  docs/i224-alkaline-family-top/held-back/Plasma_Associative_Ionization_Alkaline_Alkaline/training/

together with its three species definitions, which left dictionary.txt with it. Nothing about it
was judged wrong: I-224 narrowed both top groups from `R u[2,3,4] px cx` to `alkaline u2 px cx`,
`alkaline` is Mg and Ca only, and oxygen is therefore outside this family's template. The surviving
entries keep their original indices 2 and 3; index 1 is intentionally absent, so the two files can
be matched up by number.

It had to leave rather than sit here unreachable. `add_rules_from_training` catches the forward
template miss, re-tries the entry in reverse, and does not catch the reverse miss, so
`UndeterminableKineticsError` escaped the call `rmgpy/rmg/main.py:590` makes on every real run --
while all twelve family checks and the whole database test suite stayed green. Measured before and
after the move; see docs/i224-alkaline-family-top/report.md.

What that entry needs is a family named for neutral associative ionization, which I-224 does not
invent. The prerequisite is RMG-Py work owned elsewhere: `ATOMTYPES['O']` has no `increment_charge`
action, so no group naming oxygen can sit where this recipe applies GAIN_CHARGE (see the groups.py
longDesc).
"""

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
