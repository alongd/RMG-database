#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaOxygenHeavy"
shortDesc = u"Sourced oxygen-ion heavy-particle chemistry; grades stated per entry"
longDesc = u"""
Oxygen-ion charge transfer, mutual neutralisation and detachment; no electron-impact
rates. This is a partial library with P, A and explicitly retained S provenance.
Sources are transcribed without a new fit, averaging, or an Ar-for-O2 collider estimate.
Every rate depends on gas temperature only. Arrhenius A uses RMG molar units: a
particle-based m3/s coefficient is multiplied by Avogadro's number, and a m6/s
coefficient by its square. RMG's cm3/(mol*s) and cm6/(mol^2*s) inputs do that via
the exact 1e6 and 1e12 volume conversion factors.

All entries are irreversible source channels. The explicit electron has electrons=0;
no electron is also carried as implicit metadata. Three-body channels list O2 as an
explicit collider with ordinary termolecular Arrhenius, not ThirdBody. No Ar collider
coefficient is inferred. O2a is the existing O2(a1Delta_g) singlet graph.
Op is the O+(4S) quartet ground state; PlasmaAir's doublet Op is a different species.
The explicit electron reuses PlasmaAir/PlasmaArgon's exact u1 doublet adjacency;
zero H/S/Cp does not change its graph or introduce a second model species.

The paired engine currently collapses index 33 associative detachment with
PlasmaAir 55 dissociative electron attachment, keeping only the first offered
reaction. Both independently irreversible channels are needed with their own rates.
Six strict admission regressions expose this engine-blocked loss; a reverse object
is not a valid substitute. The unapplied engine proposal is in
docs/oxygen-ion-data/irreversible-reverse-proposal.md. No source rate is altered.

Overlapping PlasmaAir ion chemistry still requires source/state selection:
PlasmaAir 13 has reverse stoichiometric labels to index 34 but a different doublet
Op graph, and PlasmaAir 66 already contains O- + O2(a) detachment. That existing
detachment is not duplicated here. The two O2p+O- product channels 31 and 58 are
transcribed as separate channels exactly as in the source; both are included in the
source model, and the original branching measurement was not recovered. Their
coefficients are not interpreted as a measured total to be split or doubled by us.

Ar-O charge transfer and Ar* quenching below are sourced with grade S.
Ars uses the existing PlasmaArgon triplet graph with sourced 3P2 (Paschen 1s5)
thermo as a proxy for Dong et al.'s 1s5/1s3 kinetic lump. This is an explicit mapping
assumption: the 1s3 (3P0) energy and statistical weight are not represented by that
thermo. No population weighting, resolved level, or separate 1s3 rate is inferred.
Unresolved Ar+ + O- neutralisation and primary-source/branching details are listed in
docs/plasma-o2-charged-data.md. This is not a complete O2 admixture mechanism.
"""

entry(
    index = 31,
    label = "O2p + O- => O2 + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.5657565976e+16, 'cm^3/(mol*s)'),
        n = -0.44,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-31; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-31: k = 2.6e-14 * (300/Tgas)**0.44 m3/s, per particles.
    Original cited source: Gudmundsson and Lieberman, Recombination rate coefficients in oxygen discharges, report RH-16-2004 (Kemaneci ref. 83). This report was not retrieved. Related primary merged-beam measurement: Moseley et al. (1972), doi:10.1029/JA077i001p00255, not full-text read. Retain grade S.

ENCODING
    Grade S. A = 1.5657565976e+16 cm^3/(mol*s), n = -0.44, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 32,
    label = "Op + O- => O + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (2.408856304e+16, 'cm^3/(mol*s)'),
        n = -0.43,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-32; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-32: k = 4e-14 * (300/Tgas)**0.43 m3/s, per particles.
    Original cited source: Gudmundsson and Lieberman, Recombination rate coefficients in oxygen discharges, report RH-16-2004 (Kemaneci ref. 83). This report was not retrieved. Related primary merged-beam measurement: Moseley et al. (1972), doi:10.1029/JA077i001p00255, not full-text read. Retain grade S.

ENCODING
    Grade S. A = 2.408856304e+16 cm^3/(mol*s), n = -0.43, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 33,
    label = "O + O- => O2 + e-",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.3850923748e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-33; grade P",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. This compiled row is independently confirmed by the primary Belostotsky measurement below, so this entry has grade P.
    Source row V-33: k = 2.3e-16 * (300/Tgas)**-0 m3/s, per particles.
    Belostotsky, Economou, Lopaev and Rakhimova (2005), PSST 14, 532-542, doi:10.1088/0963-0252/14/3/016; full text read from the primary author publication listing https://www.chee.uh.edu/faculty/economou and its linked psst_oxygen_2005.pdf. Table 1 (R2), p. 540, and discussion pp. 540-541 give (2.3 +/- 0.5)e-10 cm3/s. The published experimental determination includes a 0.3e-10 correction discussed on p. 540; this is the published result, not an independent re-fit. Gas temperature was measured (Fig. 2); no independent thermal validity interval is claimed here.

ENCODING
    Grade P. A = 1.3850923748e+14 cm^3/(mol*s), n = 0, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 34,
    label = "O2 + Op => O + O2p",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.2646495596e+13, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-34; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-34: k = 2.1e-17 * (300/Tgas)**0.5 m3/s, per particles.
    Original cited source: Eliasson and Kogelschatz, Basic data for modeling of electrical discharges in gases: Oxygen, report KLR-11C, Brown Boveri (1986), Kemaneci ref. 85. The report and its underlying measurement have not been read; the entry retains grade S.

ENCODING
    Grade S. A = 1.2646495596e+13 cm^3/(mol*s), n = -0.5, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 38,
    label = "O2p + O2- => O2 + O2",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.21045029276e+17, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-38; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-38: k = 2.01e-13 * (300/Tgas)**0.5 m3/s, per particles.
    Original cited source: Eliasson and Kogelschatz, Basic data for modeling of electrical discharges in gases: Oxygen, report KLR-11C, Brown Boveri (1986), Kemaneci ref. 85. The report and its underlying measurement have not been read; the entry retains grade S.

ENCODING
    Grade S. A = 1.21045029276e+17 cm^3/(mol*s), n = -0.5, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 39,
    label = "Op + O2- => O2 + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.6259780052e+17, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-39; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-39: k = 2.7e-13 * (300/Tgas)**0.5 m3/s, per particles.
    Kossyi et al. (1992), PSST 1, 207, doi:10.1088/0963-0252/1/3/011, Kemaneci ref. 86; not full-text read, so grade S.

ENCODING
    Grade S. A = 1.6259780052e+17 cm^3/(mol*s), n = -0.5, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 40,
    label = "O + O2- => O2 + O-",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.99332859156e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-40; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-40: k = 3.31e-16 * (300/Tgas)**-0 m3/s, per particles.
    Original cited source: Eliasson and Kogelschatz, Basic data for modeling of electrical discharges in gases: Oxygen, report KLR-11C, Brown Boveri (1986), Kemaneci ref. 85. The report and its underlying measurement have not been read; the entry retains grade S.

ENCODING
    Grade S. A = 1.99332859156e+14 cm^3/(mol*s), n = 0, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 41,
    label = "O2a + O2- => O2 + O2 + e-",
    reversible = False,
    kinetics = Arrhenius(
        A = (4.215498532e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
        Tmin = (200, 'K'),
        Tmax = (700, 'K'),
    ),
    shortDesc = u"Midey abstract; grade A",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Selected newer primary abstract (not Kemaneci V-41): k = 7e-16 * (300/Tgas)**-0 m3/s, per particles.
    Midey, Dotan and Viggiano (2008), J. Phys. Chem. A 112, 3040-3045, doi:10.1021/jp710539s, ABSTRACT read in the authors university record https://cris.openu.ac.il/en/publications/temperature-dependences-for-the-reactions-of-osup-sup-and-o-sub2s/ . The abstract gives approximately 7e-10 cm3/s at all measured temperatures 200-700 K; electron detachment was the only product observed. Grade A. This supersedes the older 2e-10 cm3/s coefficient in Kemaneci V-41; no averaging or interpolation between the two measurements is made. The full publisher paper was inaccessible; its DOI is provided for follow-up.

ENCODING
    Grade A. A = 4.215498532e+14 cm^3/(mol*s), n = 0, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 42,
    label = "O2 + O- => O3 + e-",
    reversible = False,
    kinetics = Arrhenius(
        A = (3011070380, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-42; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-42: k = 5e-21 * (300/Tgas)**-0 m3/s, per particles.
    Kossyi et al. (1992), PSST 1, 207, doi:10.1088/0963-0252/1/3/011, Kemaneci ref. 86; not full-text read, so grade S. This is the published small constant, not a replacement with the larger 1e-18 or 2.4e-18 alternatives found in model compilations. The conflicting provenance remains open, and no broad thermal validity is asserted.

ENCODING
    Grade S. A = 3011070380 cm^3/(mol*s), n = 0, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 52,
    label = "O + O2- => O3 + e-",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.9873064508e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-52; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-52: k = 3.3e-16 * (300/Tgas)**-0 m3/s, per particles.
    Original cited measurement: Fehsenfeld, Schmeltekopf, Schiff and Ferguson, Laboratory measurements of negative ion reactions of atmospheric interest, Planet. Space Sci. 15 (1967) 373-379, Kemaneci ref. 88; the primary full text was not read. Retain grade S.

ENCODING
    Grade S. A = 1.9873064508e+14 cm^3/(mol*s), n = 0, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 58,
    label = "O2p + O- => O + O + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (1.5657565976e+16, 'cm^3/(mol*s)'),
        n = -0.44,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-58; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-58: k = 2.6e-14 * (300/Tgas)**0.44 m3/s, per particles.
    Original cited source: Gudmundsson and Lieberman, Recombination rate coefficients in oxygen discharges, report RH-16-2004 (Kemaneci ref. 83). This report was not retrieved. Related primary merged-beam measurement: Moseley et al. (1972), doi:10.1029/JA077i001p00255, not full-text read. Retain grade S.

ENCODING
    Grade S. A = 1.5657565976e+16 cm^3/(mol*s), n = -0.44, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 67,
    label = "O2p + O2- => O2 + O + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (6.0823621676e+16, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"V-67; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row V-67: k = 1.01e-13 * (300/Tgas)**0.5 m3/s, per particles.
    Original cited source: Eliasson and Kogelschatz, Basic data for modeling of electrical discharges in gases: Oxygen, report KLR-11C, Brown Boveri (1986), Kemaneci ref. 85. The report and its underlying measurement have not been read; the entry retains grade S.

ENCODING
    Grade S. A = 6.0823621676e+16 cm^3/(mol*s), n = -0.5, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 80,
    label = "O2 + Op + O- => O2 + O2",
    reversible = False,
    kinetics = Arrhenius(
        A = (7.61589765998e+22, 'cm^6/(mol^2*s)'),
        n = -2.5,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"VI-80; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row VI-80: k = 2.1e-37 * (300/Tgas)**2.5 m6/s, per particles.
    Original cited source: Eliasson and Kogelschatz, Basic data for modeling of electrical discharges in gases: Oxygen, report KLR-11C, Brown Boveri (1986), Kemaneci ref. 85. The report and its underlying measurement have not been read; the entry retains grade S.

ENCODING
    Grade S. A = 7.61589765998e+22 cm^6/(mol^2*s), n = -2.5, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)

entry(
    index = 81,
    label = "O2 + O2p + O- => O2 + O3",
    reversible = False,
    kinetics = Arrhenius(
        A = (7.28950204598e+22, 'cm^6/(mol^2*s)'),
        n = -2.5,
        Ea = (0, 'J/mol'),
        T0 = (300, 'K'),
    ),
    shortDesc = u"VI-81; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Kemaneci et al., A global model of cylindrical and coaxial surface-wave discharges, arXiv:1612.07268v1 (2016), Tables V-VI, pp. 17-18; https://arxiv.org/abs/1612.07268. Full manuscript read, but these are compiled coefficients, so their value provenance is grade S (secondary), not P.
    Source row VI-81: k = 2.01e-37 * (300/Tgas)**2.5 m6/s, per particles.
    Original cited source: Eliasson and Kogelschatz, Basic data for modeling of electrical discharges in gases: Oxygen, report KLR-11C, Brown Boveri (1986), Kemaneci ref. 85. The report and its underlying measurement have not been read; the entry retains grade S.

ENCODING
    Grade S. A = 7.28950204598e+22 cm^6/(mol^2*s), n = -2.5, T0 = 300 K, Ea = 0. The Avogadro conversion uses exactly 6.02214076e23 mol^-1. The label is an irreversible net channel; atoms and explicit charge are balanced, with electrons=0. Neutral product states follow the source lumped reaction labels; no new excited oxygen state or product-state branching is inferred. Source tables do not supply independent bounds for all these thermal rate laws; absence of Tmin/Tmax is not a claim of validity at arbitrary temperatures.
""",
)


entry(
    index = 101,
    label = "Arp + O2 => Ar + O2p",
    reversible = False,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(29508489724000, 'cm^3/(mol*s)'), n=-0.78,
                      Ea=(0, 'J/mol'), T0=(300, 'K')),
            Arrhenius(A=(5.5403694992e+14, 'cm^3/(mol*s)'), n=0,
                      Ea=(41801.8394272, 'J/mol'), T0=(300, 'K')),
        ],
        Tmin = (300, 'K'), Tmax = (1400, 'K'),
    ),
    shortDesc = u"Kutasi p. 2, sec. 3, ref. 23; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Grade S (secondary coefficient). Kutasi, J. Phys. D 43 (2010) 055201, doi:10.1088/0022-3727/43/5/055201,
    p. 2, section 3, charge-transfer expression and ref. 23. Full text read from
    the author's public archive https://plasma.szfki.kfki.hu/~kuki/publist/K10.pdf.
    The rate is cited from Midey and Viggiano, J. Chem. Phys. 109 (1998)
    5257-5263, doi:10.1063/1.477142, measured from 300 to 1400 K.
    Original full text unavailable at publisher (403); expression retained S.
    k = 4.9e-17*(300/Tgas)**0.78 + 9.2e-16*exp(-5027.6/Tgas) m3/s.
    The published two-term expression is transcribed, not refitted or averaged
    with Dong A1-32's 1.2e-17. The two terms are one net channel.
    MultiArrhenius encodes the published sum exactly, Ea=R_runtime*5027.6 J/mol.
    The pinned RMG-Py-plasma Arrhenius runtime uses R_runtime=8.314472
    J/(mol*K), so Ea=41801.8394272 J/mol is a runtime coordinate conversion
    preserving the published activation temperature. It is not a new fit.
    Thermochemistry uses the exact modern SI R stated in its own entries.
    298 K is just below the original 300 K lower bound; numeric checks there
    are an explicitly flagged extrapolation, not evidence of validity.

ENCODING
    Particle-based m3/s -> cm3/(mol*s) multiplies by NA*1e6, with
    NA=6.02214076e23 mol^-1. Irreversible, balanced atoms and explicit charge.
    Default electrons=0; the electron is not an implicit participant.
""",
)

entry(
    index = 102,
    label = "Arp + O => Ar + Op",
    reversible = False,
    kinetics = Arrhenius(
        A = (7286790319600, 'cm^3/(mol*s)'), n = 0.0,
        Ea = (0, 'J/mol'), T0 = (300, 'K'),
    ),
    shortDesc = u"Dong A1-35; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Grade S (secondary coefficient). Dong et al., arXiv:2601.08138v1 (2026), Table A1, p. 21,
    row 35, and species-list section defining Ar* as the 1s5 and 1s3 lump.
    https://arxiv.org/abs/2601.08138. Full manuscript read, but the rate is
    compiled from Liu et al., PSST 24 (2015) 025035,
    doi:10.1088/0963-0252/24/2/025035, ref. 43; retain grade S.
    Liu's publisher full text was unavailable; the author's public archive
    https://pseg.dlut.edu.cn/info/1087/1666.htm links the paper but requires
    a CAPTCHA. No restricted access was bypassed. No original measurement
    source beyond Liu's model was recovered.
    k = 1.21e-17 m3/s, no temperature dependence given in the source.
    No independent validity interval is claimed. Product labels retain the
    source's chemical-state lumping; no additional excited oxygen state.
    Ars uses the existing triplet graph and the PlasmaExcitedNeutralThermo
    3P2 (Paschen 1s5) thermo as a proxy for the published kinetic 1s5/1s3
    lump. This is an explicit mapping assumption: 1s3 is 3P0 and is not
    represented by that thermo. No population weighting or separate 1s3
    enthalpy is inferred. The rates cannot resolve individual 1s5/1s3 states.

ENCODING
    Particle-based m3/s -> cm3/(mol*s) multiplies by NA*1e6, with
    NA=6.02214076e23 mol^-1. Irreversible, balanced atoms and explicit charge.
    Default electrons=0; the electron is not an implicit participant.
""",
)

entry(
    index = 103,
    label = "Ars + O2 => Ar + O2",
    reversible = False,
    kinetics = Arrhenius(
        A = (6.7447976512e+14, 'cm^3/(mol*s)'), n = 0.0,
        Ea = (0, 'J/mol'), T0 = (300, 'K'),
    ),
    shortDesc = u"Dong A1-31; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Grade S (secondary coefficient). Dong et al., arXiv:2601.08138v1 (2026), Table A1, p. 21,
    row 31, and species-list section defining Ar* as the 1s5 and 1s3 lump.
    https://arxiv.org/abs/2601.08138. Full manuscript read, but the rate is
    compiled from Liu et al., PSST 24 (2015) 025035,
    doi:10.1088/0963-0252/24/2/025035, ref. 43; retain grade S.
    Liu's publisher full text was unavailable; the author's public archive
    https://pseg.dlut.edu.cn/info/1087/1666.htm links the paper but requires
    a CAPTCHA. No restricted access was bypassed. No original measurement
    source beyond Liu's model was recovered.
    k = 1.12e-15 m3/s, no temperature dependence given in the source.
    No independent validity interval is claimed. Product labels retain the
    source's chemical-state lumping; no additional excited oxygen state.
    Ars uses the existing triplet graph and the PlasmaExcitedNeutralThermo
    3P2 (Paschen 1s5) thermo as a proxy for the published kinetic 1s5/1s3
    lump. This is an explicit mapping assumption: 1s3 is 3P0 and is not
    represented by that thermo. No population weighting or separate 1s3
    enthalpy is inferred. The rates cannot resolve individual 1s5/1s3 states.

ENCODING
    Particle-based m3/s -> cm3/(mol*s) multiplies by NA*1e6, with
    NA=6.02214076e23 mol^-1. Irreversible, balanced atoms and explicit charge.
    Default electrons=0; the electron is not an implicit participant.
""",
)

entry(
    index = 104,
    label = "Ars + O2 => Ar + O + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (34928416408000, 'cm^3/(mol*s)'), n = 0.0,
        Ea = (0, 'J/mol'), T0 = (300, 'K'),
    ),
    shortDesc = u"Dong A1-33; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Grade S (secondary coefficient). Dong et al., arXiv:2601.08138v1 (2026), Table A1, p. 21,
    row 33, and species-list section defining Ar* as the 1s5 and 1s3 lump.
    https://arxiv.org/abs/2601.08138. Full manuscript read, but the rate is
    compiled from Liu et al., PSST 24 (2015) 025035,
    doi:10.1088/0963-0252/24/2/025035, ref. 43; retain grade S.
    Liu's publisher full text was unavailable; the author's public archive
    https://pseg.dlut.edu.cn/info/1087/1666.htm links the paper but requires
    a CAPTCHA. No restricted access was bypassed. No original measurement
    source beyond Liu's model was recovered.
    k = 5.8e-17 m3/s, no temperature dependence given in the source.
    No independent validity interval is claimed. Product labels retain the
    source's chemical-state lumping; no additional excited oxygen state.
    Ars uses the existing triplet graph and the PlasmaExcitedNeutralThermo
    3P2 (Paschen 1s5) thermo as a proxy for the published kinetic 1s5/1s3
    lump. This is an explicit mapping assumption: 1s3 is 3P0 and is not
    represented by that thermo. No population weighting or separate 1s3
    enthalpy is inferred. The rates cannot resolve individual 1s5/1s3 states.

ENCODING
    Particle-based m3/s -> cm3/(mol*s) multiplies by NA*1e6, with
    NA=6.02214076e23 mol^-1. Irreversible, balanced atoms and explicit charge.
    Default electrons=0; the electron is not an implicit participant.
""",
)

entry(
    index = 105,
    label = "Ars + O => Ar + O",
    reversible = False,
    kinetics = Arrhenius(
        A = (4877934015600, 'cm^3/(mol*s)'), n = 0.0,
        Ea = (0, 'J/mol'), T0 = (300, 'K'),
    ),
    shortDesc = u"Dong A1-34; grade S",
    longDesc = u"""
VALUE, SOURCE, LOCATION AND GRADE
    Grade S (secondary coefficient). Dong et al., arXiv:2601.08138v1 (2026), Table A1, p. 21,
    row 34, and species-list section defining Ar* as the 1s5 and 1s3 lump.
    https://arxiv.org/abs/2601.08138. Full manuscript read, but the rate is
    compiled from Liu et al., PSST 24 (2015) 025035,
    doi:10.1088/0963-0252/24/2/025035, ref. 43; retain grade S.
    Liu's publisher full text was unavailable; the author's public archive
    https://pseg.dlut.edu.cn/info/1087/1666.htm links the paper but requires
    a CAPTCHA. No restricted access was bypassed. No original measurement
    source beyond Liu's model was recovered.
    k = 8.1e-18 m3/s, no temperature dependence given in the source.
    No independent validity interval is claimed. Product labels retain the
    source's chemical-state lumping; no additional excited oxygen state.
    Ars uses the existing triplet graph and the PlasmaExcitedNeutralThermo
    3P2 (Paschen 1s5) thermo as a proxy for the published kinetic 1s5/1s3
    lump. This is an explicit mapping assumption: 1s3 is 3P0 and is not
    represented by that thermo. No population weighting or separate 1s3
    enthalpy is inferred. The rates cannot resolve individual 1s5/1s3 states.

ENCODING
    Particle-based m3/s -> cm3/(mol*s) multiplies by NA*1e6, with
    NA=6.02214076e23 mol^-1. Irreversible, balanced atoms and explicit charge.
    Default electrons=0; the electron is not an implicit participant.
""",
)
