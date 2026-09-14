#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Charge_Transfer/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.4.
This family describes reactions of the sort:

A+ + B <=> A + B+  ;  A+ + B- <=> A + B  ;  A++ + B- <=> A+ + B

References:
[Tanarro2015]: M. Jimenez-Redondo, E. Carrasco, V.J. Herrero, I. Tanarro, Chemistry in glow discharges of H2/O2 mixtures. Diagnostics and modeling, Plasma Sources Sci Technol 2015, 24(1), DOI: 10.1088/0963-0252/24/1/015029
[Gupta1990]: R.N. Gupta, J.M. Yos, R.A. Thompson, K.-P. Lee, NASA Reference Publication 1232, 1990, A Review of Reaction Rates and Thermodynamic and Transport Properties for an 11-Species Air Model for Chemical and Thermal Nonequilibrium Calculations to 30000 K
[Aiken2023] T.T. Aiken, PhD Thesis, Detailed Modeling and Sensitivity Analysis of Non-Equilibrium Thermochemistry in Shock-Heated Gases, 2023, University of Colorado.
[Ozawa2008]: T. Ozawa, J. Zhong, D.A. Levin, Development of kinetic-based energy exchange models for noncontinuum, ionized hypersonic flows, Physics of Fluids 2008, 20, 046102, DOI: 10.1063/1.2907198

A note on T0, because two entries here got it wrong (I-223):
[Tanarro2015] Table 1 is written k = A (T/300)^n, so its entries carry T0 = 300 K.
[Gupta1990] Table II is written k = Cf T^eta exp(-theta_d/T) -- a BARE T -- so a Gupta
entry must carry T0 = 1 K. Entries 13 and 17 sat immediately after the Tanarro block and
had inherited its T0 = 300 K while copying Cf verbatim, which makes every k they return
wrong by 300^n: 561x too high for entry 13 (n = -1.11), 2.64x too low for entry 17
(n = +0.17). Entry 13's T0 is corrected below; entry 17 was deleted (see next paragraph).
[Ozawa2008] Table III and [Aiken2023] Table 3.16 are likewise bare-T and already carry
T0 = 1 K. [Ozawa2008] and [Aiken2023] have NOT been checked against their primary documents.

[Tanarro2015] has (I-223). All twelve entries, indices 1-12, were audited row by row against
Table 1 of the open author manuscript (europepmc.org/articles/PMC4685741) -- reaction, A,
exponent, T0, Ea and units. Eleven match exactly. One correction, recorded on the entry itself:

  entry 1, row IN1, H+ + H- -> 2H : A was 1.88e-7, Table 1 prints 1.8e-7. 1.044x, corrected.

The rule used, worth keeping for the remaining two sources: a discrepancy under 10x is a
transcription slip and gets corrected in place with its table row recorded; a discrepancy of an
order of magnitude or more, or any mismatch in exponent, T0, Ea or units, is STOPPED and reported
without touching it, because that size of error is a units or convention problem and rescaling A
to make k(T) look right buries it. Entry 13 below is the precedent: it read as a wrong number and
was a wrong T0 convention worth 561x.

A caution on Table 1 that matters when reading rates out of it: 18 of its 23 ion-ion
neutralization rows carry the identical 2e-7 (Tg/300)^-0.5, and 16 of those cite one reference,
Kossyi 1992, a kinetic-scheme review rather than a measurement of any particular ion pair. Rows
with a pair-specific source carry pair-specific numbers (IN1, IN4, IN12, IN17, IN23). So where
two of these entries agree exactly, that is one class estimate quoted twice, not two independent
determinations -- see docs/i223-charge-transfer-node-repair/logs/tanarro.stdout.log.

Deleted entry 17 (I-223): a second copy of NOp_r1 + O2_r2 <=> O2p + NO, from [Gupta1990]
Table II R19, k = 1.8e15 T^0.17 exp(-3.3e4/T). It duplicated entry 21 at the same rank 6,
so KineticsRules.get_rule broke the tie on index alone and entry 21 was silently never
used. Entry 21 ([Ozawa2008]) is kept: the Gupta fit demands 10-19x the Langevin capture
rate for NO+ + O2 over 300-10000 K (Ozawa 0.55-2.3x), Ozawa's Ea of 271.1 kJ/mol matches
the endothermicity IE(O2) - IE(NO) = 270.7 kJ/mol, and the rest of the air charge-exchange
block here (entries 14, 15, 16, 21, 22, 23) is [Ozawa2008] Table III.
Evidence: docs/i223-charge-transfer-node-repair/{report.md,logs/kt.stdout.log,logs/t0.stdout.log}.
"""

entry(
    index = 1,
    label = "Hp_r1 + H-_r2 <=> H + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.8e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN1

A was 1.88e-7 here until I-223 read Table 1 directly; row IN1 prints 1.8e-7 (Tg/300)^-0.5.
A 1.044x transcription slip, corrected in place. The other eleven [Tanarro2015] entries were
audited against their rows at the same time and match exactly (logs/tanarro.stdout.log).
Table 1 cites [21] Konstantinovskii 2005 for this row specifically, not the generic ion-ion
value it gives most of the block.
"""
)

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
The H2_ion group node that used to try to host it was removed by I-223 for the same reason; see
the comment at its former position in groups.py.

It is kept, where the duplicate at index 17 was deleted, because the two cases are not alike:
index 17 was a rival fit for a reaction this family DOES cover, so deleting it lost nothing that
could not be recovered from the surviving entry. This is the only sourced rate in the repo for
H2+ + H-, so deleting it would destroy information with no fallback.

It is inert where it sits. It resolves to the template H_ion;H_anion, where entry 1 wins the
rank-6 tie on the lower index, and that is the correct outcome: a rule at that template can only
ever be applied to reactions this family can actually generate, i.e. H+ + H-, which entry 1
describes exactly. The two rates differ by 1.1x in any case (logs/collisions.stdout.log).
"""
)

entry(
    index = 3,
    label = "Op_r1 + H-_r2 <=> O + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.3e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN4
"""
)

entry(
    index = 4,
    label = "O2p_r1 + H-_r2 <=> O2 + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN5
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
    index = 6,
    label = "Hp_r1 + O-_r2 <=> H + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN9
"""
)

entry(
    index = 7,
    label = "Op_r1 + O-_r2 <=> O + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-1.0, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN12
"""
)

entry(
    index = 8,
    label = "O2p_r1 + O-_r2 <=> O2 + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN13
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
    index = 10,
    label = "O2p_r1 + OH-_r2 <=> O2 + OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN20
"""
)

entry(
    index = 11,
    label = "OHp_r1 + OH-_r2 <=> OH + OH",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.0e-7, 'cm^3/(molecule*s)'), n=-0.5, Ea=(0.0, 'kJ/mol'),
                       T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Tanarro2015]",
    longDesc = u"""
Table 1, IN21
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
    index = 15,
    label = "Op_r1 + N2_r2 <=> N2p + O",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.1e13, 'cm^3/(mol*s)'), n=0.36, Ea=(189.6, 'kJ/mol'),
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
    index = 18,
    label = "Np_r1 + N2_r2 <=> N2p + N",
    degeneracy = 1,
    kinetics=Arrhenius(A=(6.99e6, 'cm^3/(mol*s)'), n=1.47, Ea=(26090, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16
"""
)

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

entry(
    index = 23,
    label = "O2p_r1 + N2_r2 <=> N2p + O2",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.88e12, 'cm^3/(mol*s)'), n=0.0, Ea=(338.4, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Ozawa2008]",
    longDesc = u"""
Table III
"""
)

entry(
    index = 24,
    label = "Lip_r1 + H-_r2 <=> Li + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.81e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 25,
    label = "Nap_r1 + H-_r2 <=> Na + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.66e16, 'cm^3/(mol*s)'), n=0.2, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 26,
    label = "Kp_r1 + H-_r2 <=> K + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(4.43e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 27,
    label = "Mgp_r1 + H-_r2 <=> Mg + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(9.03e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)

entry(
    index = 28,
    label = "Cap_r1 + H-_r2 <=> Ca + H",
    degeneracy = 1,
    kinetics=Arrhenius(A=(1.2e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 9,
    shortDesc = u"estimated",
    longDesc = u"""

"""
)
