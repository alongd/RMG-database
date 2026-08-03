#!/usr/bin/env python
# encoding: utf-8

name = "Aryl_Decarbonylation/training"
shortDesc = u"Reaction kinetics used as training data to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "phenoxy <=> cyclopentadienyl + CO",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+11, 's^-1'),
        n = 0,
        Ea = (43.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (1000, 'K'),
        Tmax = (1580, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Shock-tube measurement, phenoxy -> C5H5 + CO (Lin & Lin 1986)""",
    longDesc = u"""
Phenoxy radical decarbonylation to cyclopentadienyl + CO, gas phase.

Source: C.-Y. Lin & M. C. Lin, "Thermal decomposition of methyl phenyl
ether in shock waves: the kinetics of phenoxy radical reactions",
J. Phys. Chem. 90 (1986) 425-431 (anisole shock-tube pyrolysis; phenoxy
decay by CO formation), DOI 10.1021/j100275a014 (verified via Crossref and
OpenAlex, 2026-08-03). MEASURED effective first-order rate, reported by
Lin & Lin in log form as

    k2 = 10^(11.40 +/- 0.20) * exp(-(22100 +/- 450)/T) s^-1

i.e. A = 10^11.40 = 2.51e11 s^-1, Ea = 22100 K * R = 43.92 kcal/mol,
valid 1000-1580 K. Source locator: the phenoxy decarbonylation channel is
their reaction 2 (C6H5O -> c-C5H5 + CO), J. Phys. Chem. 90 (1986) 425-431.

A-FACTOR CORRECTED 2026-08-03 (D-008; ruling by Alon, ruling date
2026-08-03). This entry previously carried A = 7.4e11 s^-1 while citing
Lin & Lin as the source. That attribution was WRONG: Lin & Lin do not
report 7.4e11. The A factor is now 2.51e11, which is the value the cited
paper actually reports. Ea (43.9 kcal/mol), the temperature range, the
degeneracy and the rank are unchanged -- only A moved, by a factor of 2.95
(the family is correspondingly ~3x slower).

Evidence for the correction:
  - 10^11.40 = 2.512e11 exactly, and 22100 K * R = 43.92 kcal/mol, which
    reproduces the 43.9 kcal/mol this entry already carried. The coded Ea
    and the log-form expression are self-consistent, so the original
    author had Lin & Lin's expression in hand for Ea but paired it with an
    A factor from elsewhere.
  - Independent discriminator that does not require reading Lin & Lin at
    all: Shu et al. 2017 (DOI 10.1002/kin.21105) state their measured rate
    exceeds Lin & Lin / Frank et al. / Carstensen & Dean by factors of
    6 / 2 / 1.5. Evaluating at 1070 K (mid-range of their phenoxy data):
    A=2.51e11 gives Shu/k = 5.98 (the Lin & Lin slot); A=7.4e11 gives
    Shu/k = 2.02 (the Frank slot). Both close to within 0.02.

Confidence, stated honestly: the DOI and bibliographic record are CONFIRMED
(Crossref, OpenAlex). The expression 10^(11.40) exp(-22100/T) was NOT read
off the primary PDF -- ACS returns 403 to automated access and the abstract
is not indexed by Crossref, OpenAlex or Semantic Scholar. It is corroborated
by multiple independent retrievals and by the Shu arithmetic above.

NOT relied upon: the hypothesis that 7.4e11 originates from Frank, Herzler,
Just & Wahl, Symp. (Int.) Combust. 25 (1994) 833-840
(DOI 10.1016/S0082-0784(06)80717-4). The Shu arithmetic is consistent with
it, but the primary text was never accessible (publisher blocked), so that
attribution remains UNCONFIRMED and is deliberately not encoded here. The
correction above stands on the Lin & Lin value alone.

See docs/D-008_aryl_decarbonylation_template_diagnosis.md.

Consistency band (recorded per phase-6 provenance practice; RESTATED
2026-08-03 -- the previous "agree within a factor of ~2-3" claim was
computed against the incorrect A = 7.4e11 and no longer held once A was
corrected):
- A newer shock-tube CO-absorption determination reports
  k = 9.1e13 * exp(-220.3 kJ/mol / RT) s^-1 (~52.7 kcal/mol; Shu,
  Herzler, Peukert, Fikri & Schulz, Int. J. Chem. Kinet. 49 (2017)
  656-667, DOI 10.1002/kin.21105 -- DOI and bibliographic record
  CONFIRMED via Crossref/Semantic Scholar 2026-08-03; the Arrhenius
  numbers themselves were NOT read off the publisher page, which blocks
  automated access). Against the corrected A = 2.51e11 the two
  expressions differ by a factor of 4.5 at 1000 K rising to 22 at 1580 K
  (9.3 at 1200 K). They do NOT agree within a factor of 2-3. This spread
  is expected and is not evidence against either measurement: the two
  fits carry very different activation energies (43.9 vs 52.7 kcal/mol)
  because they sample different falloff regimes -- see next point.
- The higher computed barriers do not contradict the ~44 kcal/mol
  measured Ea. Carstensen & Dean, Int. J. Chem. Kinet. 44 (2012) 75-89,
  DOI 10.1002/kin.20622 (abstract retrieved and read), state verbatim:
  "All methods predict the experimentally determined phenoxy
  decomposition rate constant to be in the falloff region. This explains
  the almost 10 kcal mol-1 difference between reported activation
  energies and calculated barriers. Both the Lin and Lin (1986) and
  Frank et al. (1994) data can be reproduced within the assumed
  uncertainty limits without any adjustments of the PES."
  So the value carried here is an APPARENT FALLOFF activation energy at
  ~1 atm, not a barrier. (An earlier revision of this entry stated the
  theoretical barrier as "~54 kcal/mol" citing this DOI; that specific
  number was an inference from the "almost 10 kcal/mol" sentence above,
  not a value read from the paper, and has been replaced by the verbatim
  quotation. Liu, Morokuma, Mebel & Lin, J. Phys. Chem. 100 (1996) 9314,
  DOI 10.1021/jp953566w, independently place the rate-limiting barrier
  at 52 kcal/mol at G2M.)
- PRESSURE-DEPENDENCE CAVEAT: because this is a ~1 atm falloff fit coded
  as a pressure-independent Arrhenius rule, it is used in the regime it
  was fitted for only when the deck sits near 1 atm. It will be wrong off
  that pressure. Carrying a PLOG / high-pressure-limit form is an open
  scope decision, not taken here.

Degeneracy note: the reaction proceeds through either of the two
equivalent ortho keto resonance forms (degeneracy 2 as written); the A
factor above is the total measured phenoxy disappearance rate, and RMG
divides by the degeneracy when deriving the per-site rule.

Effect scope: this family is not auto-generated, so this entry folds into
the Root rate rule at load and generalizes to substituted aryloxy radicals
(methylphenoxy from cresols, hydroxyphenoxy from novolac daughters) at
honestly-labeled ANALOGY tier. Note DR2's caution that cresol-derived
(methylphenoxy) decarbonylation is somewhat slower than phenoxy; when
isomer-specific G4 rates are imported (carbon_phenol library), the library
values take precedence for those exact species.
""",
)
