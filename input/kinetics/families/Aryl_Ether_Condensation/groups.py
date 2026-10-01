#!/usr/bin/env python
# encoding: utf-8

name = "Aryl_Ether_Condensation/groups"
shortDesc = u""
longDesc = u"""
Bimolecular phenolic condensation to a diaryl ether plus water:

    Ar-OH + Ar'-OH -> Ar-O-Ar' + H2O

This is the stage-I/II low-temperature water-release channel invoked by the
phenolic-resin TGA mechanism literature (Trick & Saliba, Carbon 33 (1995)
1509, DOI 10.1016/0008-6223(95)00092-R; Jackson & Conley, J. Appl. Polym.
Sci. 8 (1964), DOI 10.1002/app.1964.070080516) for the 150-400 C onset of
water evolution from cured phenolics, and the largest identified flux gap of
the phase-6 novolac TGA benchmark (no prior RMG family releases water from
closed-shell phenolic OH groups without radicals).

The transformation is an ipso substitution of one phenolic -OH by the other
phenol's oxygen: ring A's C-O bond breaks, ring A's ipso carbon bonds to ring
B's oxygen, ring B's O-H hydrogen transfers to ring A's departing oxygen,
which leaves as water with its own hydrogen. Both rings remain aromatic
throughout, so no dearomatization machinery is needed.

Atom labeling:
*1 - ipso carbon of ring A (loses its hydroxyl, gains the ether oxygen)
*2 - hydroxyl oxygen of ring A (departs as the water oxygen)
*3 - hydroxyl hydrogen of ring A (stays on *2; first water hydrogen)
*4 - ipso carbon of ring B (its oxygen becomes the ether oxygen)
*5 - hydroxyl oxygen of ring B (becomes the ether oxygen)
*6 - hydroxyl hydrogen of ring B (transfers to *2; second water hydrogen)

Kinetics status (honest): the 2026 DR2 deep-research pass confirmed a genuine
literature gap -- no MEASURED or QM/TST elementary rate exists for the
uncatalyzed gas-phase reaction. The training anchor is therefore an explicit
ESTIMATE (rank 10) bounded by (i) ReaxFF intrinsic water-formation barriers
in crosslinked phenolics, 42-49 kcal/mol (DOI 10.1016/j.polymer.2010.12.034),
(ii) condensed-phase isoconversional stage-I apparent Ea 81.6-93.5 kJ/mol
(DOI 10.2514/1.J059423; transport-convolved, not elementary), and (iii)
catalyzed etherification onsets of 300-480 C (US5288922, US5144094), which
bound the barrier from below. This reaction is the standing target for an
in-house ARC/Arkane CBS-QB3 (or G4) calculation; replace the estimate and
promote the rank when that lands.
"""

template(reactants=["ArOH_A", "ArOH_B"], products=["ArOAr", "H2O"], ownReverse=False)

reverse = "Diaryl_Ether_Hydrolysis"
reversible = True

reactantNum = 2

productNum = 2

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*5'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['FORM_BOND', '*2', 1, '*6'],
])

# Declared outcome (D-053): the family declares its own polymer-moment
# consequence, so the engine reads a declaration instead of re-deriving the
# outcome by graph analysis. The three signature slots are the per-pool
# moments the polymer solver actually consumes (pool.mu_indices in
# rmgpy/solver/polymer.pyx is the (mu0, mu1, mu2) triple): mu0 = chain
# count, mu1 = repeat units (mass), mu2 = second moment.
#
#   intermolecular -- the *1 and *4 sites live in DIFFERENT reactant
#   molecules: the condensation merges two chains of lengths a and b into
#   one, so the chain count drops by one (dmu0 = -1), repeat units are
#   conserved (dmu1 = 0), and the second moment rises by
#   (a+b)^2 - a^2 - b^2 = 2*a*b. Chain lengths are unknown until solve
#   time, so dmu2 is declared SYMBOLICALLY as the marker '2*a*b'; the
#   consumer evaluates it from its own chain-length state (cf.
#   _chain_bundle in rmgpy/solver/polymer.pyx).
#
#   intramolecular -- both sites in the SAME molecule: the condensation
#   closes a loop inside one chain. Two sites are consumed and water is
#   ejected, but nothing merges: dmu0 = dmu1 = dmu2 = 0.
#
# Water release is IDENTICAL in both cases: it comes from the recipe above
# and depends only on site consumption, never on the inter/intra case.
#
# The modified unit is declared as a whole subgraph, not a bond pair: the
# six labeled site atoms extended ('ring' extent) to the full ring carrying
# each ipso carbon plus that ring's hydrogens. The unit's boundary is
# implicit -- whichever bonds cross the declared atom set.
declaredOutcome = {
    'siteAnchors': ('*1', '*4'),
    'siteLabels': (('*1', '*2', '*3'), ('*4', '*5', '*6')),
    'unitExtent': 'ring',
    'intermolecular': (-1, 0, '2*a*b'),
    'intramolecular': (0, 0, 0),
}

entry(
    index = 0,
    label = "ArOH_A",
    group =
"""
1 *1 Cb  u0 {2,S}
2 *2 O2s u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "ArOH_B",
    group =
"""
1 *4 Cb  u0 {2,S}
2 *5 O2s u0 {1,S} {3,S}
3 *6 H   u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: ArOH_A
"""
)

tree(
"""
L1: ArOH_B
"""
)
