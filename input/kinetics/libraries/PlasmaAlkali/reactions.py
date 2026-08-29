#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaAlkali"
shortDesc = u"PlasmaAlkali"
longDesc = u"""
Plasma kinetics for Alkali and Alkali Earth metals in air plasma environments.

Reference legend:
[Golyatina2021]:  R.I. Golyatina, S.A. Marinov, Analytical Cross Section Approximation for Electron Impact Ionization of Alkali and Other Metals, Inert Gases and Hydrogen Atoms, Atoms 2021, 9(90), DOI: 10.3390/atoms9040090
[VernerFerland1996]: D.A. Verner, G.J. Ferland, Atomic data for astrophysics. I. Radiative recombination rates for H-like, He-like, Li-like and Na-like ions over a broad range of temperature, ApJ 1995, arXiv:astro-ph/9509083v1
[JensenJones1977]: D.E. Jensen and G.A. Jones, "Reaction Rate Coefficients for Flame Calculations", https://apps.dtic.mil/sti/tr/pdf/ADA047018.pdf
[AgerTalcottHoward1986]: J.W. Ager, C.L. Talcott, C.J. Howard, "Gas phase kinetics of the reactions of Na and NaO with O3 and N2O", J. Chem. Phys. 1986, 85, 5584-5592, DOI: 10.1063/1.451573
[AgerHoward1987]: J.W. Ager, C.J. Howard, "Gas phase kinetics of the reactions of NaO with H2, D2, H2O, and D2O", J. Chem. Phys. 1987, 87, 921-925, DOI: 10.1063/1.453726
[GlarborgMarshall2005]: P. Glarborg, P. Marshall, "Mechanism and modeling of the formation of gaseous alkali sulfates", Combust. Flame 2005, 141, 22-39, DOI: 10.1016/j.combustflame.2004.08.014
[GomezMartin2016]: J.C. Gomez Martin, S.M. Daly, J.M.C. Plane, "Kinetic studies of atmospherically relevant reactions of metal oxides", J. Phys. Chem. A 120, 1330-1339 (2016), DOI: 10.1021/acs.jpca.5b00622
[GomezMartin2017]: J.C. Gomez Martin, C. Seaton, M.P. de Miranda, J.M.C. Plane, "The reaction between sodium hydroxide and atomic hydrogen in atmospheric and flame chemistry", J. Phys. Chem. A 2017, 121, 7667-7674, DOI: 10.1021/acs.jpca.7b07808
[HelmerPlane1993]: M. Helmer, J.M.C. Plane, "A study of the reaction NaO2 + O -> NaO + O2: Implications for the chemistry of sodium in the upper atmosphere", J. Geophys. Res. 1993, 98, 23207-23222, DOI: 10.1029/93JD02033
[HusainMarshallPlane1986]: D. Husain, P. Marshall, J.M.C. Plane, "Rate constant for the reaction Na + O2 + N2 -> NaO2 + N2 under mesospheric conditions", J. Photochem. 1986, 32, 1-7, DOI: 10.1016/0047-2670(86)85001-8
[Plane2015]: J.M.C. Plane, W. Feng, E.C.M. Dawkins, "The mesosphere and metals: chemistry and changes", Chem. Rev. 2015, 115, 4497-4541, DOI: 10.1021/cr500501m
[PlaneHusain1986]: J.M.C. Plane, D. Husain, "Determination of the absolute rate constant for the reaction O + NaO -> Na + O2 by time-resolved atomic chemiluminescence at 589 nm", J. Chem. Soc. Faraday Trans. 2 1986, 82, 2047-2052, DOI: 10.1039/F29868202047
[PlaneRajasekhar1988a]: J.M.C. Plane, B. Rajasekhar, "Study of the reaction Li + H2O over the temperature range 850–1000 K by time-resolved laser-induced fluorescence of Li", J. Chem. Soc. Faraday Trans. 2 1988, 84, 273-285, DOI: 10.1039/F29888400273
[PlaneRajasekhar1988b]: J.M.C. Plane, B. Rajasekhar, "A study of the reaction Li + O2 + M (M = N2, He) over the temperature range 267-1100 K by Time-Resolved Lacer-Induced Fluorescence of Li", J. Phys. Chem. 93 1988, 3884-3890, DOI: 10.1021/j100324a041
[Sorvajarvi2015]: T. Sorvajarvi, J. Viljanen, J. Toivonen, P. Marshall, P. Glarborg, "Rate constant and thermochemistry for K + O2 + N2 = KO2 + N2", J. Phys. Chem. A 2015, 119, 3329-3336, DOI: 10.1021/acs.jpca.5b00755
[Plane1991]: J.M.C. Plane, "The chemistry of meteoric metals in the Earth's upper atmosphere", Int. Rev. Phys. Chem. 1991, 10, 55-106, DOI: 10.1080/01442359109353254

CARRY-OVER PROVENANCE (I-154)
-----------------------------
This library was authored on an earlier line of development (RMG-database branch
``99``) and re-applied here as a new file rather than merged, because the branch it
came from also carries edits to existing files that this line does not want. What
changed in the carry, and nothing else did:

* **Cation labels gained a ``p`` suffix** (``NO+`` -> ``NOp``, ``Ar+`` -> ``Arp``,
  ...). ``KineticsLibrary.load`` splits a reaction string on a bare ``+``, so a
  species whose own label contains ``+`` is torn in half and the loader reports a
  missing species with an empty name. Every other family in this database already
  spells cations this way; the shipped ionisation library's ``[Lip]`` is the
  precedent. Species, charges and rates are untouched.
* **``NO+`` was re-drawn.** It arrived as ``N u0 p1 c+1 {2,D}`` -- a nitrogen with
  six valence electrons, which this engine has no atom type for. It is now the
  octet form ``N#O+`` (``N u0 p1 c0 {2,T}`` / ``O u0 p1 c+1 {1,T}``), which
  resolves to N3t/O4tc with the same net charge. Same species, better Lewis
  structure.

* **14 entries were NOT carried**, because this line has no representation
  for them in a kinetics library. RMG carries a reaction's free-electron
  stoichiometry either as an explicit participant or as the scalar
  ``Reaction.electrons``; ``Reaction.is_balanced`` treats the free electron as a
  conserved pseudo-element, so an explicit-electron entry whose electron COUNT
  changes across the arrow fails the balance check
  (``test/rmgpy/i108ElectronRepresentationMatrixTest.py`` pins this), and the
  metadata form is only reachable through a rate law that carries the count
  itself -- ``VoronovEIArrhenius``, ``BadnellRRArrhenius``, or a charge-transfer
  law. The dropped entries use ``Arrhenius``, ``ThirdBody`` and
  ``TwoTemperaturePlasma``, none of which do. Extending
  ``KineticsLibrary.load_entry`` with an ``electrons=`` argument is the agreed
  fix and is a separate ticket; until it lands these reactions are a NAMED gap
  rather than a silent one. They are listed in
  ``docs/i154-carry-chemistry.md``, by shape:

      (1, 0) x 9   attachment or recombination, electron consumed
      (1, 2) x 5   electron-impact ionisation, one in and two out

  Every entry that survives conserves the free electron count, which is why this
  library correctly declares NO electron placement in
  ``rmgpy.electron_placement.FAMILY_ELECTRON_PLACEMENT``.

READ THE RATES BEFORE TRUSTING THEM
-----------------------------------
Many entries carried here are marked ``estimated`` by their original author rather
than sourced. That provenance is preserved verbatim in each entry's ``shortDesc``;
it was not upgraded, re-fitted or re-derived by the carry-over, which changed no
number anywhere.
"""

entry(
    index = 4,
    label = "Lip + OH- <=> Li + OH",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=-0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 5,
    label = "Nap + OH- <=> Na + OH",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=-0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 6,
    label = "Kp + OH- <=> K + OH",
    kinetics=Arrhenius(A=(6.0e15, 'cm^3/(mol*s)'), n=-0.50, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 8,
    label = "LiH2Op <=> Lip + H2O",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.2e+17,'cm^3/(mol*s)'), n=0.0, Ea=(45700,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 9,
    label = "NaH2Op <=> Nap + H2O",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.8e+17,'cm^3/(mol*s)'), n=0.0, Ea=(29800,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 10,
    label = "KH2Op <=> Kp + H2O",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(6.0e+16,'cm^3/(mol*s)'), n=0.0, Ea=(19900,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 14,
    label = "LiH2Op + OH- => Li + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 15,
    label = "NaH2Op + OH- => Na + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 16,
    label = "KH2Op + OH- => K + OH + H2O",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e16, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 11
"""
)

entry(
    index = 17,
    label = "Li + O2 <=> LiO2",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(5.24e+20,'cm^6/(mol^2*s)'), n=-1.02, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[PlaneRajasekhar1988b]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Primary measurement covers 267-1100 K and is recommended for use over 300-6000 K.
Replaces the prior [JensenJones1977] value (3.6e+17 cm^6/mol^2/s, n=-1, Ea=0), which was ~1.2e+3 too low.
""",
)

entry(
    index = 18,
    label = "Na + O2 <=> NaO2",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.16e+21,'cm^6/(mol^2*s)'), n=-1.22, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[HusainMarshallPlane1986]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Primary measurement covers 415-1016 K and is recommended for use over 300-6000 K.
Replaces the prior [JensenJones1977] value (3.6e+17 cm^6/mol^2/s, n=-1, Ea=0), which was ~5e+2 to 6e+2 too low.
""",
)

entry(
    index = 19,
    label = "K + O2 <=> KO2",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.99e+22,'cm^6/(mol^2*s)'), n=-1.55, Ea=(20,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[Sorvajarvi2015]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Primary direct CPFAAS measurement covers 748-1323 K (the highest-T anchor for the entire alkali + O2 + M family);
recommended for use over 300-6000 K.
Replaces the prior [JensenJones1977] value (3.6e+17 cm^6/mol^2/s, n=-1, Ea=0), which was ~5e+2 to 1e+3 too low.
""",
)

entry(
    index = 20,
    label = "LiO2 + H2 <=> LiOH + OH",
    kinetics=Arrhenius(A=(1.8e12, 'cm^3/(mol*s)'), n=0.0, Ea=(19900.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 21,
    label = "NaO2 + H2 <=> NaOH + OH",
    kinetics=Arrhenius(A=(1.8e12, 'cm^3/(mol*s)'), n=0.0, Ea=(19900.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 22,
    label = "KO2 + H2 <=> KOH + OH",
    kinetics=Arrhenius(A=(1.8e12, 'cm^3/(mol*s)'), n=0.0, Ea=(19900.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 23,
    label = "LiO2 + OH <=> LiOH + O2",
    kinetics=Arrhenius(A=(1.2e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 24,
    label = "NaO2 + OH <=> NaOH + O2",
    kinetics=Arrhenius(A=(1.2e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 25,
    label = "KO2 + OH <=> KOH + O2",
    kinetics=Arrhenius(A=(1.2e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 26,
    label = "Na + HO2 <=> NaO2 + H",
    kinetics=Arrhenius(A=(6.0e12, 'cm^3/(mol*s)'), n=0.0, Ea=(1990.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 27,
    label = "K + HO2 <=> KO2 + H",
    kinetics=Arrhenius(A=(6.0e12, 'cm^3/(mol*s)'), n=0.0, Ea=(1990.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 12
"""
)

entry(
    index = 29,
    label = "CaOH + H <=> CaO + H2",
    kinetics=Arrhenius(A=(2.4e13, 'cm^3/(mol*s)'), n=0.0, Ea=(7300.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 30,
    label = "CaOH + H <=> Ca + H2O",
    kinetics=Arrhenius(A=(2.4e12, 'cm^3/(mol*s)'), n=0.0, Ea=(1200.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 31,
    label = "CaOH2 + H <=> CaOH + H2O",
    kinetics=Arrhenius(A=(1.8e13, 'cm^3/(mol*s)'), n=0.0, Ea=(1200.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 32,
    label = "CaO + H2O <=> CaOH2",
    kinetics=Arrhenius(A=(3.6e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 34,
    label = "CaOHp + H <=> Cap + H2O",
    kinetics=Arrhenius(A=(6.0e13, 'cm^3/(mol*s)'), n=-2.0, Ea=(2000.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 35,
    label = "H3Op + Li => Lip + H2O + H",
    reversible = False,
    kinetics=Arrhenius(A=(1.0e19, 'cm^3/(mol*s)'), n=-1.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 36,
    label = "H3Op + Na => Nap + H2O + H",
    reversible = False,
    kinetics=Arrhenius(A=(2.4e22, 'cm^3/(mol*s)'), n=-2.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 37,
    label = "H3Op + K => Kp + H2O + H",
    reversible = False,
    kinetics=Arrhenius(A=(2.7e22, 'cm^3/(mol*s)'), n=-2.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(10000, 'K')),
    shortDesc = u"[JensenJones1977]",
    longDesc = u"""
p. 14
"""
)

entry(
    index = 46,
    label = "Na + O3 <=> NaO + O2",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(231.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerTalcottHoward1986]",
    longDesc = u"""
Direct laboratory measurement of Na + O3.
Modified-Arrhenius form k = 1.1e-9 * exp(-116/T) cm^3 molecule^-1 s^-1 from the Plane mesospheric
recommendation, anchored to the [AgerTalcottHoward1986] data; converted using N_A = 6.022e23
(231 cal/mol = 116 K * R_cal). Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 47,
    label = "Li + O3 <=> LiO + O2",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(231.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerTalcottHoward1986]",
    longDesc = u"""
Assumed same rate as Na + O3 <=> NaO + O2 by analogy. No primary Li + O3 kinetics measurement
survived source triage. Confidence: ANALOGY.
""",
)

entry(
    index = 48,
    label = "K + O3 <=> KO + O2",
    kinetics=Arrhenius(A=(1.08e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[Plane2015]",
    longDesc = u"""
K-specific value taken from the [Plane2015] meteoric K scheme rather than copied from Na.
Confidence: EXTRAPOLATED_FLAT.
""",
)

entry(
    index = 49,
    label = "Na + O <=> NaO",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.10e+21,'cm^6/(mol^2*s)'), n=-1.50, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[GlarborgMarshall2005]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
No primary Na + O + M measurement is available; this rate is the alkali/alkaline-earth analogy form
adopted in the Glarborg-Marshall combustion modeling work. Note: NaO+ + e- (excited-state cation
chemistry of Griffin et al. 2001) was explicitly rejected as a source - that paper concerns the
NaO(A2Sigma+) + O system, not ground-state Na + O association. Confidence: ANALOGY.
""",
)

entry(
    index = 50,
    label = "Li + O <=> LiO",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.10e+21,'cm^6/(mol^2*s)'), n=-1.50, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[GlarborgMarshall2005]",
    longDesc = u"""
Assumed same rate as Na + O + M by analogy. No primary Li + O + M data. Confidence: ANALOGY.
""",
)

entry(
    index = 51,
    label = "K + O <=> KO",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(1.10e+21,'cm^6/(mol^2*s)'), n=-1.50, Ea=(0,'cal/mol'), T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[GlarborgMarshall2005]",
    longDesc = u"""
Assumed same rate as Na + O + M by analogy. No primary K + O + M data. Confidence: ANALOGY.
""",
)

entry(
    index = 52,
    label = "NaO + O <=> Na + O2",
    kinetics=Arrhenius(A=(9.37e12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneHusain1986]",
    longDesc = u"""
Ground-state NaO(X) + O direct measurement. Do not substitute the NaO(A2Sigma+) + O kinetics
of Griffin et al. 2001 here. Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 53,
    label = "LiO + O <=> Li + O2",
    kinetics=Arrhenius(A=(9.37e12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneHusain1986]",
    longDesc = u"""
Assumed same rate as NaO + O <=> Na + O2 by analogy. No primary LiO + O data. Confidence: ANALOGY.
""",
)

entry(
    index = 54,
    label = "KO + O <=> K + O2",
    kinetics=Arrhenius(A=(9.37e12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneHusain1986]",
    longDesc = u"""
Assumed same rate as NaO + O <=> Na + O2 by analogy. No primary KO + O data. Confidence: ANALOGY.
""",
)

entry(
    index = 55,
    label = "NaO + H2 <=> NaOH + H",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(2186.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerHoward1987]",
    longDesc = u"""
Modified-Arrhenius fit (Plane2015 review evaluation) to the [AgerHoward1987] room-T anchor
[k(308-471 K) = (2.6 +/- 0.7)e-11 cm^3 molecule^-1 s^-1]. An unresolved low-T discrepancy versus
[GomezMartin2016] remains. Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 56,
    label = "LiO + H2 <=> LiOH + H",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(2186.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerHoward1987]",
    longDesc = u"""
Assumed same rate as NaO + H2 <=> NaOH + H by analogy. No primary LiO + H2 data. Confidence: ANALOGY.
""",
)

entry(
    index = 57,
    label = "KO + H2 <=> KOH + H",
    kinetics=Arrhenius(A=(6.62e14, 'cm^3/(mol*s)'), n=0.0, Ea=(2186.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[AgerHoward1987]",
    longDesc = u"""
Assumed same rate as NaO + H2 <=> NaOH + H by analogy. No primary KO + H2 data. Confidence: ANALOGY.
""",
)

entry(
    index = 58,
    label = "NaO + H2O <=> NaOH + OH",
    kinetics=Arrhenius(A=(3.05e14, 'cm^3/(mol*s)'), n=0.0, Ea=(477.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[GomezMartin2016]",
    longDesc = u"""
[GomezMartin2016] direct measurement with explicit T-dependence; preferred over the older flat
[AgerHoward1987] surrogate. Confidence: EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 59,
    label = "LiO + H2O <=> LiOH + OH",
    kinetics=Arrhenius(A=(3.05e14, 'cm^3/(mol*s)'), n=0.0, Ea=(477.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[GomezMartin2016]",
    longDesc = u"""
Assumed same rate as NaO + H2O <=> NaOH + OH by analogy. No primary LiO + H2O data. Confidence: ANALOGY.
""",
)

entry(
    index = 60,
    label = "KO + H2O <=> KOH + OH",
    kinetics=Arrhenius(A=(1.32e14, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[Plane2015]",
    longDesc = u"""
K-specific direct value retained from the [Plane2015] meteoric K scheme. Confidence: EXTRAPOLATED_FLAT.
""",
)

entry(
    index = 61,
    label = "NaOH + H <=> Na + H2O",
    kinetics=Arrhenius(A=(2.29e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[GomezMartin2017]",
    longDesc = u"""
Direct measurement at 230-298 K with essentially no temperature dependence; validated against
flame chemistry. Confidence: MEASURED_HIGH_T (the cleanest entry in the alkali metal-oxide block).
""",
)

entry(
    index = 62,
    label = "LiOH + H <=> Li + H2O",
    kinetics=Arrhenius(A=(9.60e13, 'cm^3/(mol*s)'), n=0.0, Ea=(24400.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[PlaneRajasekhar1988a]",
    longDesc = u"""
Derived from the measured reverse reaction Li + H2O and Li/LiOH thermochemistry; the high barrier
(~24 kcal/mol) reflects LiOH stability and is required by detailed balance. Do NOT copy the Na rate
here. Confidence: EXTRAPOLATED_T_DEPENDENT.
""",
)

entry(
    index = 63,
    label = "KOH + H <=> K + H2O",
    kinetics=Arrhenius(A=(3.00e13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[Plane2015]",
    longDesc = u"""
High-T flame-inferred K-specific value from the [Plane2015] meteoric K scheme. Confidence: MEASURED_HIGH_T.
""",
)

entry(
    index = 64,
    label = "NaO2 + O <=> NaO + O2",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.0, Ea=(1868.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[HelmerPlane1993]",
    longDesc = u"""
Modified-Arrhenius fit (Plane2015 review evaluation) anchored to the 295 K direct flow-tube
measurement of [HelmerPlane1993] [k = (2.2 +/- 1.0)e-11 cm^3 molecule^-1 s^-1]. Confidence:
EXTRAPOLATED_T_DEPENDENT to 6000 K.
""",
)

entry(
    index = 65,
    label = "LiO2 + O <=> LiO + O2",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.0, Ea=(1868.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[HelmerPlane1993]",
    longDesc = u"""
Assumed same rate as NaO2 + O <=> NaO + O2 by analogy. No primary LiO2 + O data. Confidence: ANALOGY.
""",
)

entry(
    index = 66,
    label = "KO2 + O <=> KO + O2",
    kinetics=Arrhenius(A=(3.01e14, 'cm^3/(mol*s)'), n=0.0, Ea=(1868.0, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(6000, 'K')),
    shortDesc = u"[HelmerPlane1993]",
    longDesc = u"""
Assumed same rate as NaO2 + O <=> NaO + O2 by analogy. No primary KO2 + O data. Confidence: ANALOGY.
""",
)

# ----------------------------------------------------------------------
# Direct termolecular formation of alkali hydroxides:
#     A + OH + M  <=>  AOH + M
#
# This is the dominant mesospheric source of NaOH per Plane and Husain
# (1991 review); without it, the only paths to NaOH in this library are
# the slower NaO + H2 / NaO + H2O channels (entries 55, 58) and the
# NaO2 + H2 / NaO2 + OH channels (entries 21, 24). Adding the direct
# Na + OH + M recombination raises the steady-state NaOH so that the
# RMG enlarger has a chance of promoting NaOH into the core.
# ----------------------------------------------------------------------

entry(
    index = 67,
    label = "Na + OH <=> NaOH",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(4.24e+23,'cm^6/(mol^2*s)'),
                                                n=-2.0, Ea=(0,'cal/mol'),
                                                T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[Plane1991]",
    longDesc = u"""
Low-pressure-limit (k0) recombination, M = N2.
Plane 1991 / Plane 2015 mesospheric recommendation:
   k0(T) = 1.3e-29 * (T/300)^-2 cm^6 molecule^-2 s^-1
Converted to cm^6/(mol^2*s) by N_A^2 = 3.626e47:
   A = 1.3e-29 * 300^2 * 3.626e47 = 4.24e23 cm^6/(mol^2*s).
""",
)

entry(
    index = 68,
    label = "Li + OH <=> LiOH",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(4.24e+23,'cm^6/(mol^2*s)'),
                                                n=-2.0, Ea=(0,'cal/mol'),
                                                T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[Plane1991]",
    longDesc = u"""
Assumed same rate as Na + OH + M <=> NaOH + M by analogy. No primary
Li + OH + M kinetics measurement available; the alkali termolecular
recombination rate is expected to be only weakly Z-dependent.
Confidence: ANALOGY.
""",
)

entry(
    index = 69,
    label = "K + OH <=> KOH",
    kinetics = ThirdBody(arrheniusLow=Arrhenius(A=(4.24e+23,'cm^6/(mol^2*s)'),
                                                n=-2.0, Ea=(0,'cal/mol'),
                                                T0=(1,'K')),
                         efficiencies={}),
    shortDesc = u"[Plane1991]",
    longDesc = u"""
Assumed same rate as Na + OH + M <=> NaOH + M by analogy.
Confidence: ANALOGY.
""",
)


