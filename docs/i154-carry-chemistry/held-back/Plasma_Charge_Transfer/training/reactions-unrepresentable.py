#!/usr/bin/env python
# encoding: utf-8
"""
NOT A DEPOSITORY. This file is never loaded by RMG and must not be renamed to reactions.py.

Depositories are discovered by DIRECTORY name -- `load` walks the family directory and reads
`<subdir>/reactions.py` (family.py:749-762) -- so this file sits harmlessly beside the real one.

WHAT THESE ELEVEN ENTRIES ARE.

They are the chemistry that left Plasma_Charge_Transfer when I-223 narrowed it. What each has lost
is a family able to generate its reaction, not its rate. They are kept here, rather than deleted,
because the rate is the expensive part -- see report.md sections 5, 6 and 11 for the audits.

ONE RATE HERE IS NOT PRIMARY-SOURCE VERIFIED, and an earlier version of this header wrongly said
they all were. The [Ozawa2008] entries -- indices 14 and 21 -- rest on a Table III that this ticket
could not obtain: every route to it was blocked (report.md section 6, "Ozawa unreachable"). They
are carried on the secondary transcription they arrived with. Everything else here was read
against its primary table.

TWELVE ENTRIES LEFT AND ELEVEN REMAIN. Entry 18 (N+ + N2) came back in round 61: it was set aside
on a claim of impossibility that turned out to be wrong, which is recorded in its own longDesc in
training/reactions.py and in groups.py at root A. The count in this header, and the group 4 that
used to hold it, are corrected accordingly.

WHY EACH ONE LEFT. The headline distinction is NOT "needs more than two labels" -- that applies to
only four of the eleven. Seven need a DIFFERENT RECIPE on the same two-label template, which is a
much smaller obstacle, and one of the twelve needed neither and is no longer here:

GROUPS 1 AND 2 -- SEVEN DISTINCT ENTRIES (5, 9, 12, 13, 19, 20, 22; entry 20 is in both because
its cation and its donor each need a different action). These fit the two-label template perfectly.
What they need is a different RECIPE, and each recipe is already written out in report.md section
12.3. They are a sibling family waiting to be written, not a grammar limit.

1. THE CATION ACCEPTS ITS ELECTRON BY PAIRING, NOT AS A RADICAL  -- entries 5, 9, 12, 19, 20.
   H2O+ (`O u1 p1 c+1`) and Ar+ (`Ar u1 p3 c+1`) become closed-shell H2O and Ar, which is
   LOSE_RADICAL + GAIN_PAIR. The family's recipe is GAIN_RADICAL, which on H2O+ produces an
   oxygen with two single bonds, two radicals and one lone pair -- a structure with NO ATOM TYPE
   -- and on Ar+ produces `Ar u2 p3`, a valid molecule but not ground-state argon.

2. THE DONOR RELEASES AN UNPAIRED ELECTRON, NOT A LONE PAIR -- entries 13, 20, 22.
   O(3P) `u2 p2` and N(4S) `u3 p1` donate by LOSE_RADICAL. The recipe's GAIN_RADICAL + LOSE_PAIR
   would give O+ as `u3 p1` where the database writes `u1 p2`.

GROUP 3 -- THE ONLY FOUR THAT EXCEED THE TEMPLATE ITSELF.

3. THE REACTION NEEDS A BOND-ORDER CHANGE -- entries 2, 14, 16, 21.
   NO+ `N#[O+]` -> NO `[N]=O` and H2+ `[H+].[H]` -> H2 `[H][H]`. CHANGE_BOND and FORM_BOND take
   TWO labelled atoms; this family labels one atom per reactant and they are on different
   molecules, so no recipe on this template can express it. These four are unreachable by ANY of
   the four possible two-label recipes, not merely by the one chosen. THESE FOUR, and only these
   four, are the ones a two-label template genuinely cannot reach.

FORMER GROUP 4 -- entry 18, which is no longer here. It was set aside as needing a new atom type;
round 61 showed that a LogicOr root separates N+ from H2O+ and NO+ without one, and the entry is
back in training/reactions.py. It is named here so that a reader of an older report section does
not go looking for it.

WHERE THE CHEMISTRY GOES NOW. Nowhere, yet. Groups 1 and 2 -- seven entries, the majority of this
file -- are a coherent sibling family whose recipes are already written out in report.md section
12.3; splitting them off is a new ticket, not this one. Group 3's four need a three-label template.
Until then this chemistry is UNREPRESENTED, and a mechanism that needs it will silently lack it.
"""

entry(
    index = 2,
    label = "H2p_r1 + H-_r2 <=> H2 + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN2

This reaction is NOT a member of this family, and I-223 kept the entry anyway. Deliberately.

The recipe here only moves charge -- LOSE_CHARGE on *1, GAIN_CHARGE on *2 -- and has no
bond-forming action. H2+ cannot be written with a bond at all (its one-electron bond has no
integer order), so the dictionary writes H2p_r1 as two unbonded atoms, `[H+].[H]`; applying the
recipe to that gives `[H].[H]`, two separate H atoms, never the bonded H2 this reaction produces.
apply_recipe returns None on it (logs/h2-recipe.stdout.log). This is mutual neutralisation
followed by recombination and it belongs in a library, not in a charge-transfer family.

Amended (I-223, producibility audit): this entry is NOT the exception it was written up as. It is
the only one apply_recipe returns None for -- the other 26 it accepts and hands back unchanged --
but none of the 27 is producible, for the reason in the header note above. What is specific to
this entry is the bond, not the charge: even a recipe that correctly neutralised H2+ would still
have to FORM the H-H bond, and no other entry here needs that. The paragraph below about why it
is kept rather than deleted is unaffected.
The H2_ion group node that used to try to host it was removed by I-223 for the same reason; see
the comment at its former position in groups.py.

It is kept, where the duplicate at index 17 was deleted, because the two cases are not alike:
index 17 was a rival fit for a reaction this family DOES cover, so deleting it lost nothing that
could not be recovered from the surviving entry. This is the only sourced rate in the repo for
H2+ + H-, so deleting it would destroy information with no fallback.

It is inert where it sits, and the reason is narrower than "nothing else can land there". It
resolves to the template H_ion;H_anion, where entry 1 wins the rank-6 tie on the lower index.
H_ion is a one-atom group, `H u0 p0 c+1`, with no bond constraint, so the template catches any
reaction whose *1 atom is a bare proton -- within THIS training set that is only H+ + H-, which
entry 1 describes exactly, but a real run carrying a larger H-bearing cation could reach it too.
What makes the shadowing harmless is not that nothing else matches; it is that the number being
shadowed is within 1.1x of the one that wins (logs/collisions.stdout.log), so the choice between
them cannot change an answer either way. Whether entry 1's H+ + H- rate is the right value for
some larger cation that descends to H_ion is a separate question this ticket did not examine.
"""
)

entry(
    index = 5,
    label = "H2Op_r1 + H-_r2 <=> H2O + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN7
"""
)

entry(
    index = 9,
    label = "H2Op_r1 + O-_r2 <=> H2O + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN15
"""
)

entry(
    index = 12,
    label = "H2Op_r1 + OH-_r2 <=> H2O + OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN22
"""
)

entry(
    index = 13,
    label = "O2p_r1 + O_r2 <=> O2 + Op",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.92e18, 'cm^3/(mol*s)'), n=-1.11, Ea=(55650, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Gupta1990]",
    longDesc = u"""
Table II, R11:  2.92e18 T^-1.11 exp(-2.8e4/T) cm^3/(mol*s).

T0 is 1 K, not 300 K: Gupta's Table II is a bare-T fit and A here is his Cf verbatim.
It carried T0 = 300 K until I-223, which made every k it returned 300^1.11 = 561x too
high. Ea = 55650 cal/mol is theta_d = 2.8e4 K (Ea/R = 28004 K).
"""
)

entry(
    index = 14,
    label = "NOp_r1 + O_r2 <=> NO + Op",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.76e13, 'cm^3/(mol*s)'), n=0.01, Ea=(424.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 16,
    label = "NOp_r1 + N_r2 <=> NO + Np",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.11e15, 'cm^3/(mol*s)'), n=-0.02, Ea=(507.7, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

# Index 17 deleted by I-223. It was a duplicate of index 21 below: the same reaction,
# NOp_r1 + O2_r2 <=> O2p + NO, at the same rank 6, from [Gupta1990] Table II R19. See the
# longDesc at the top of this file for the evidence behind keeping the [Ozawa2008] fit.
# The index is deliberately left unused rather than renumbering the entries after it.


entry(
    index = 19,
    label = "Arp_r1 + N2_r2 <=> Ar + N2p",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.55e13, 'cm^3/(mol*s)'), n=0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 20,
    label = "Arp_r1 + O_r2 <=> Ar + Op",
    degeneracy = 1,
    kinetics=Arrhenius(A=(3.85e12, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

entry(
    index = 21,
    label = "NOp_r1 + O2_r2 <=> O2p + NO",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.4e13, 'cm^3/(mol*s)'), n=0.41, Ea=(271.1, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III.

The surviving fit for this reaction; a rival [Gupta1990] Table II R19 copy sat at index 17
at the same rank until I-223 deleted it. Ea = 271.1 kJ/mol is the endothermicity
IE(O2) - IE(NO) = 12.0697 - 9.2642 eV = 270.7 kJ/mol, and A*T^n stays within 0.55-2.3x of
the Langevin capture rate for NO+ + O2 (4.5e14 cm^3/(mol*s)) over 300-10000 K.
"""
)

entry(
    index = 22,
    label = "O2p_r1 + N_r2 <=> Np + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(8.67e13, 'cm^3/(mol*s)'), n=0.14, Ea=(237.8, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

