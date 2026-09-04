#!/usr/bin/env python
# encoding: utf-8

name = "Plasma_Collisional_Ionization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
4.1. a.
This family describes reactions of the sort:

A  + M => A+ + e- + M

References:
[Gupta1990]: R.N. Gupta, J.M. Yos, R.A. Thompson, K.-P. Lee, NASA Reference Publication 1232, 1990, A Review of Reaction Rates and Thermodynamic and Transport Properties for an 11-Species Air Model for Chemical and Thermal Nonequilibrium Calculations to 30000 K

-------------------------------------------------------------------------------
TRAINING SET HELD (both entries) pending a decision on the NO+ representation.
-------------------------------------------------------------------------------
The two training entries carried from branch `99` were translated to the target
branch's convention (electron demoted from a template species to the family's
`electrons = 1` scalar; cation relabelled NO+ -> NOp). Their kinetics, ranks and
descriptions are unchanged. They are commented out below, not deleted, so their
provenance travels with them.

They are held because the species `NO+` (nitrosonium) as written on branch `99`
does not load on the target branch:

    NO+
    1 N u0 p1 c+1 {2,D}      # +1 on N, double bond  -> AtomTypeError, no such atom type
    2 O u0 p2 c0  {1,D}

This is chemically wrong: nitrosonium is [N#O]+ with the formal charge on OXYGEN,
and the only adjacency that both is correct and loads on this branch is the
charge-on-O triple-bond form (the same motif this database uses for the
isoelectronic CO):

    NOp
    1 N u0 p1 c0  {2,T}
    2 O u0 p1 c+1 {1,T}      # N#[O+]

Adopting that adjacency is a species-identity change (a gated action) and would
be "refitting" a training entry, so it is deferred. To re-enable the two entries:
add the corrected NOp above (plus NO, O2, N2) to dictionary.txt and un-comment the
entries below.
"""

# entry(
#     index = 1,
#     label = "NO + O2 <=> NOp + O2",
#     degeneracy = 1,
#     kinetics=Arrhenius(A=(2.2e15, 'cm^3/(mol*s)'), n=-0.35, Ea=(215000, 'cal/mol'),
#                        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
#     rank = 6,
#     shortDesc = u"[Guptap1990]",
#     longDesc = u"""
# Table II R15
# """
# )

# entry(
#     index = 2,
#     label = "NO + N2 <=> NOp + N2",
#     degeneracy = 1,
#     kinetics=Arrhenius(A=(2.2e15, 'cm^3/(mol*s)'), n=-0.35, Ea=(215000, 'cal/mol'),
#                        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
#     rank = 6,
#     shortDesc = u"[Guptap1990]",
#     longDesc = u"""
# Table II R15
# (same rate as above)
# """
# )
