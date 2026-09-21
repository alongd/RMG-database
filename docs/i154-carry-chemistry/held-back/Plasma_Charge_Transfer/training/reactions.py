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
[Aiken2023] Table 3.16 prints its own form, k = A T^eta exp(-theta/T_tr) -- bare T, so the
three entries citing it carry T0 = 1 K and that is now READ, not inferred. All three (18, 19,
20) were audited against it and match; note its A column is in m^3/s per particle, so the
conversion to the cm^3/(mol*s) used here is x6.02214e29.
[Ozawa2008] Table III is ALSO bare-T on the entries here, but that has NOT been read. The paper
is closed and there is no open copy: pubs.aip.org returns 403, and OpenAlex and Semantic Scholar
independently report oa_status "closed" with no repository full text. So entries 14, 15, 16, 21,
22 and 23 are checked by surrogate only -- their Ea against spectroscopic ionization energies
(all six within 1%), their theta against [Gupta1990] RP-1232 Table II where the two compilations
overlap (four of six, within 1.2%), and their A against the Langevin capture rate. Their n and
their T0 are NOT verified. Do not read the surrogates as more than they are.
What that gap can cost is bounded, and the bound is why it does not block: a wrong T0 rescales A
by 300^n, but both tree splits this family makes are Ozawa-against-Ozawa (14 vs 21, 22 vs 23), so
the ratio the split criterion tests moves only by 300^(n1-n2). Under the wrong convention the
splits fall to 22.2x and 48.1x, still far above the 4x criterion. See
docs/i223-charge-transfer-node-repair/probe_ozawa_aiken.py.

THIS SET WAS 27 ENTRIES AND IS NOW 15 (I-223). The twelve that left are in
training/reactions-unrepresentable.py, with the reason for each; that file is never loaded.

The family's recipe used to be charge-only -- LOSE_CHARGE *1, GAIN_CHARGE *2 -- and a charge-only
recipe cannot move a charge in RMG, because apply_recipe re-derives every product's charge from a
structure the action never touched (molecule.py:596-598, family.py:1547). The family generated
ZERO reactions while all twelve checks passed. The recipe is now
GAIN_RADICAL *1 + GAIN_RADICAL *2 + LOSE_PAIR *2, with no charge action at all, and the two root
templates are narrowed to the structures that recipe can process without raising. Measured after
the change: 45 reactions generated over the training set's own species, all 15 entries below
reproduced with their declared products, none reproduced wrongly, zero crashes.

The rates were never the problem and none of the audits below is retracted. What changed is which
of them the family can reach. Numbering is unchanged and therefore now has gaps -- the gaps are
the entries that moved out, and they are deliberate, but see the note on index 102 in groups.py:
any save through RMG renumbers everything and the gaps will not survive it.
See docs/i223-charge-transfer-node-repair/{probe_producibility.py,probe_grammar.py,probe_narrow.py}
and report.md sections 11 and 12.

[Tanarro2015] has (I-223). All twelve entries, indices 1-12, were audited row by row against
Table 1 of the open author manuscript (europepmc.org/articles/PMC4685741) -- reaction, A,
exponent, T0, Ea and units. Eleven match exactly. One correction, recorded on the entry itself:

  entry 1, row IN1, H+ + H- -> 2H : A was 1.88e-7, Table 1 prints 1.8e-7. 1.044x, corrected.

The rule used -- since applied unchanged to [Aiken2023], and the one still owed to [Ozawa2008] if
its table is ever reached: a discrepancy under 10x is a
transcription slip and gets corrected in place with its table row recorded; a discrepancy of an
order of magnitude or more, or any mismatch in exponent, T0, Ea or units, is STOPPED and reported
without touching it, because that size of error is a units or convention problem and rescaling A
to make k(T) look right buries it. Entry 13 below is the precedent: it read as a wrong number and
was a wrong T0 convention worth 561x.

A caution on Table 1 that matters when reading rates out of it: 17 of its 23 ion-ion
neutralization rows carry the identical 2e-7 (Tg/300)^-0.5, and 14 of those cite one reference,
Kossyi 1992, a kinetic-scheme review rather than a measurement of any particular ion pair. Six
rows differ -- IN1, IN4, IN8, IN12, IN17, IN23 -- and five of those six carry a pair-specific
source; IN17 cites Kossyi and differs anyway, so "cites Kossyi" and "carries the generic value"
are not the same predicate. So where two of these entries agree exactly, that is one class
estimate quoted twice, not two independent determinations.
These counts are recomputed from the transcribed table on every run of
docs/i223-charge-transfer-node-repair/probe_tanarro.py; an earlier hand tally in this note said
18 and 16, having miscounted IN8 (2.3e-7) as generic. The conclusion is unchanged.

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
    index = 18,
    label = "Np_r1 + N2_r2 <=> N2p + N",
    degeneracy = 1,
    kinetics=Arrhenius(A=(6.99e6, 'cm^3/(mol*s)'), n=1.47, Ea=(26090, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    rank = 6,
    shortDesc = u"[Aiken2023]",
    longDesc = u"""
Table 3.16

Set aside by I-223 as unrepresentable, and brought back in round 61 when that turned out to be
wrong. The claim was that root A could not admit N+ (`N u2 p1 c+1`) without also admitting H2O+
and NO+, which crash. True of a FLAT root; false of a LogicOr over per-element children, which is
what root A is now. The rate and its source are untouched -- only the family's ability to make the
reaction changed. Measured back at 16 of 27 entries reproduced, 0 crashes (logs/nitrogen.stdout.log).
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
