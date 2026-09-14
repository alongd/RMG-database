#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Associative_Ionization_Alkaline_Alkaline/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
HELD BACK BY I-224 -- NOT INSTALLED, NOT DELETED.

What this is. One training reaction, O + O <=> O2+ + e-, neutral associative ionization, with a
rank-6 literature rate from [Aiken2025] Table VIII. It is carried here verbatim: index, degeneracy,
rate coefficient, rank and reference are exactly what left the family. Nothing about it was judged
wrong.

Where it came from. `input/kinetics/families/Plasma_Associative_Ionization_Alkaline_Alkaline/
training/reactions.py`, where it was entry 1 of three. It keeps its index here so the two can be
matched up by number. Its three species definitions travel with it in `dictionary.txt`.

Why it left. I-224 narrowed that family's two top groups from `R u[2,3,4] px cx` to
`alkaline u2 px cx`, because the wildcard tops matched any species carrying an atom with 2-4
unpaired electrons -- C and N atoms, S, triplet carbenes, a carbene site inside an arbitrary
polyatomic -- and generated a bonded cation for every pairing. `alkaline` is Mg and Ca only
(rmgpy/molecule/atomtype.py), so oxygen now sits outside the narrowed template and the family can
no longer generate this reaction.

Why it could not simply stay. An unreachable training entry is not inert. `add_rules_from_training`
catches the forward template miss and re-tries the entry in reverse (rmgpy/data/kinetics/family.py,
the `reverse_entries` path at 1184-1191), and the reverse miss is NOT caught, so
`UndeterminableKineticsError` escapes the call `rmgpy/rmg/main.py:590` makes for every
non-auto-generated family on every real run. Left in place, this entry was green through all twelve
family checks and the whole database test suite, and still took a run down. Measured both ways; see
docs/i224-alkaline-family-top/report.md.

What it wants. A family named for neutral associative ionization -- A + B <=> AB+ + e- where the
partners are neutral non-metal atoms -- rather than one named for alkaline-earth pairs. That family
is deliberately NOT invented here: I-224 owns one family's top groups and nothing else.

What has to happen before that family can exist. The recipe for this chemistry applies GAIN_CHARGE
to the atom that becomes the cation, and `GroupAtom._gain_charge` raises ActionError unless every
atom type in the group carries an `increment_charge` action. `ATOMTYPES['O']` has
`increment_charge=[]` and `decrement_charge=[]`, while its bond, radical and lone-pair rows are all
self-preserving -- the charge row alone is missing, and no neutral oxygen atom type in RMG-Py has
one. So a group naming oxygen in that position cannot be loaded at all today. Giving the oxygen
atom types a charge row is RMG-Py work, owned outside this ticket, and it is the prerequisite for
giving this entry a home.

Reference:
[Aiken2025] T.T. Aiken, I.D. Boyd, I.V. Adamovich, Phys. Plasmas 2025, 32, 103512. DOI: 10.1063/5.0294530
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

Held back by I-224, not deleted and not judged wrong: oxygen fell outside the narrowed
`alkaline u2 px cx` top groups of Plasma_Associative_Ionization_Alkaline_Alkaline. Rate, rank and
reference are exactly as they were in that family. See the depository longDesc above.
"""
)
