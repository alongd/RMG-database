#!/usr/bin/env python
# encoding: utf-8

name = "NOx2018"
shortDesc = u"NOx2018"
longDesc = u"""
P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002


 Hydrocarbon subset:

H. Hashemi, J.M. Christensen, S. Gersen, H. Levinsky, S.J. Klippenstein, P. Glarborg,
“High-Pressure Oxidation of Methane”, Combust. Flame 172 (2016) 349-364.

J. Gimenez-Lopez, C.T. Rasmussen, H. Hashemi, M.U. Alzueta, Y. Gao, P. Marshall, C.F. Goldsmith, P. Glarborg,
“Experimental and Kinetic Modeling Study of C2H2 Oxidation at High Pressure, Int. J. Chem. Kinet. 48 (2016) 724-738.

H. Hashemi, J.G. Jacobsen, C.T. Rasmussen, J.M. Christensen, P. Glarborg, S. Gersen, M. van Essen, H.B. Levinsky, S.J. Klippenstein, 
“High-Pressure Oxidation of Ethane”, Combust. Flame 182 (2017) 150-166.

 Nitrogen subset

P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002
"""

entry(
    index=1,
    label="CHCHOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 O u0 p2 c0 {1,S} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(224.700, 'K'),
        sigma=(4.162, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=2,
    label="OCHCO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,D}
    3 O u1 p2 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(440.200, 'K'),
        sigma=(4.010, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=3,
    label="HCOH",
    molecule=
    """
    multiplicity 3
    1 C u2 p0 c0 {2,S} {3,S}
    2 O u0 p2 c0 {1,S} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=4,
    label="CH2CHOOH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {5,S}
    2 C u0 p0 c0 {1,D} {6,S} {7,S}
    3 O u0 p2 c0 {1,S} {4,S}
    4 O u0 p2 c0 {3,S} {8,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=5,
    label="CH2CHOO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 O u0 p2 c0 {1,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=6,
    label="CH3CHOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,S} {7,S}
    3 O u0 p2 c0 {2,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=7,
    label="H2CC",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p1 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=8,
    label="CH2OOH",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 O u0 p2 c0 {2,S} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.700, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=9,
    label="CH2CH2OH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,S} {7,S}
    3 O u0 p2 c0 {1,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=10,
    label="CH2CHOH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 O u0 p2 c0 {1,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=11,
    label="cC2H4O",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
    3 O u0 p2 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=12,
    label="cC2H3O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {3,S} {6,S}
    3 O u0 p2 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=13,
    label="CH3CH2OOH",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
    3  O u0 p2 c0 {1,S} {4,S}
    4  O u0 p2 c0 {3,S} {10,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=14,
    label="CH3CH2OO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 O u0 p2 c0 {1,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=15,
    label="CH2CH2OOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {7,S} {8,S}
    3 O u0 p2 c0 {1,S} {4,S}
    4 O u0 p2 c0 {3,S} {9,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=16,
    label="CH3CHOOH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
    2 C u1 p0 c0 {1,S} {3,S} {8,S}
    3 O u0 p2 c0 {2,S} {4,S}
    4 O u0 p2 c0 {3,S} {9,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {1,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=17,
    label="HOCH2CH2OO",
    molecule=
    """
    multiplicity 2
    1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
    3  O u0 p2 c0 {1,S} {9,S}
    4  O u0 p2 c0 {2,S} {10,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  O u1 p2 c0 {3,S}
    10 H u0 p0 c0 {4,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(395.0, 'K'),
        sigma=(4.037, 'angstroms'),
        dipoleMoment=(1.3, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=18,
    label="HON",
    molecule=
    """
    1 O u0 p1 c+1 {2,D} {3,S}
    2 N u0 p2 c-1 {1,D}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=19,
    label="HNO2",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,D} {4,S}
    2 H u0 p0 c0 {1,S}
    3 O u0 p2 c0 {1,D}
    4 O u0 p3 c-1 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(350.000, 'K'),
        sigma=(3.950, 'angstroms'),
        dipoleMoment=(1.639, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=20,
    label="HONO2",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,D} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 O u0 p2 c0 {1,D}
    4 O u0 p3 c-1 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(400.000, 'K'),
        sigma=(4.200, 'angstroms'),
        dipoleMoment=(0.200, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=21,
    label="H2NN",
    molecule=
    """
    1 N u0 p0 c+1 {2,D} {3,S} {4,S}
    2 N u0 p2 c-1 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(71.400, 'K'),
        sigma=(3.798, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=22,
    label="NH2OH",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=23,
    label="HNC",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,T}
    2 H u0 p0 c0 {1,S}
    3 C u0 p1 c-1 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=24,
    label="HCNH",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,D} {3,S}
    2 N u0 p1 c0 {1,D} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=25,
    label="CH3NO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p1 c0 {1,S} {6,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=26,
    label="CH3NH2",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p1 c0 {1,S} {6,S} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=27,
    label="CH3NH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u1 p1 c0 {1,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=28,
    label="CH2NH2",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=29,
    label="CH2NH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 N u0 p1 c0 {1,D} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=30,
    label="CH3OO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u1 p2 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=31,
    label="CH3OOH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 O u0 p2 c0 {2,S} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=32,
    label="HOCH2O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {6,S}
    3 O u1 p2 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(470.600, 'K'),
        sigma=(4.410, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=33,
    label="HOCO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,D}
    2 O u0 p2 c0 {1,S} {4,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=34,
    label="HOCHO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=35,
    label="OCHO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 O u1 p2 c0 {1,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=36,
    label="AR",
    molecule=
    """
    1 Ar u0 p4 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(136.500, 'K'),
        sigma=(3.330, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=37,
    label="C",
    molecule=
    """
    1 C u2 p1 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(97.530, 'K'),
        sigma=(3.621, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=38,
    label="CH",
    molecule=
    """
    multiplicity 2
    1 C u1 p1 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(80.000, 'K'),
        sigma=(2.750, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=39,
    label="CH2(S)",
    molecule=
    """
    1 C u0 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(144.000, 'K'),
        sigma=(3.800, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=40,
    label="CH2",
    molecule=
    """
    multiplicity 3
    1 C u2 p0 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(144.000, 'K'),
        sigma=(3.800, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=41,
    label="CH3",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(144.000, 'K'),
        sigma=(3.800, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=42,
    label="CH4",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(141.400, 'K'),
        sigma=(3.746, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(2.600, 'angstroms^3'),
        rotrelaxcollnum=13.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=43,
    label="CO",
    molecule=
    """
    1 C u0 p1 c-1 {2,T}
    2 O u0 p1 c+1 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(98.100, 'K'),
        sigma=(3.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.950, 'angstroms^3'),
        rotrelaxcollnum=1.800,
    ),
    shortDesc=u"""""",
)

entry(
    index=44,
    label="CO2",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,D}
    2 O u0 p2 c0 {1,D}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(244.000, 'K'),
        sigma=(3.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(2.650, 'angstroms^3'),
        rotrelaxcollnum=2.100,
    ),
    shortDesc=u"""""",
)

entry(
    index=45,
    label="HCO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,D}
    2 H u0 p0 c0 {1,S}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=46,
    label="CH2O",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 O u0 p2 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(498.000, 'K'),
        sigma=(3.590, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=47,
    label="CH2OH",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 O u0 p2 c0 {1,S} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=48,
    label="CH3O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u1 p2 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(417.000, 'K'),
        sigma=(3.690, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=49,
    label="CH3OH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 O u0 p2 c0 {1,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.800, 'K'),
        sigma=(3.626, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=50,
    label="C2",
    molecule=
    """
    multiplicity 3
    1 C u1 p0 c0 {2,T}
    2 C u1 p0 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(97.530, 'K'),
        sigma=(3.621, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=51,
    label="C2O",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u1 p0 c0 {1,T}
    3 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=52,
    label="C2H",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u1 p0 c0 {1,T}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=53,
    label="C2H2",
    molecule=
    """
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=54,
    label="C2H3",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(209.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=55,
    label="C2H4",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(280.800, 'K'),
        sigma=(3.971, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=56,
    label="C2H5",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,S} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.300, 'K'),
        sigma=(4.302, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=57,
    label="C2H6",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.300, 'K'),
        sigma=(4.302, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=58,
    label="HCCO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,T} {4,S}
    2 C u0 p0 c0 {1,T} {3,S}
    3 O u1 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(150.000, 'K'),
        sigma=(2.500, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=59,
    label="HCCOH",
    molecule=
    """
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {4,S}
    3 O u0 p2 c0 {1,S} {5,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=60,
    label="CH2CO",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=61,
    label="CH2CHO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 C u0 p0 c0 {1,S} {5,D} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=62,
    label="H",
    molecule=
    """
    multiplicity 2
    1 H u1 p0 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(145.000, 'K'),
        sigma=(2.050, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=63,
    label="H2",
    molecule=
    """
    1 H u0 p0 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(38.000, 'K'),
        sigma=(2.920, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.790, 'angstroms^3'),
        rotrelaxcollnum=280.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=64,
    label="H2O",
    molecule=
    """
    1 O u0 p2 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(572.400, 'K'),
        sigma=(2.605, 'angstroms'),
        dipoleMoment=(1.844, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=65,
    label="H2O2",
    molecule=
    """
    1 O u0 p2 c0 {2,S} {3,S}
    2 O u0 p2 c0 {1,S} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(107.400, 'K'),
        sigma=(3.458, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=3.8,
    ),
    shortDesc=u"""""",
)

entry(
    index=66,
    label="HO2",
    molecule=
    """
    multiplicity 2
    1 O u0 p2 c0 {2,S} {3,S}
    2 O u1 p2 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(107.400, 'K'),
        sigma=(3.458, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=67,
    label="N2",
    molecule=
    """
    1 N u0 p1 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(97.530, 'K'),
        sigma=(3.621, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=68,
    label="O",
    molecule=
    """
    multiplicity 3
    1 O u2 p2 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(80.000, 'K'),
        sigma=(2.750, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=69,
    label="O2",
    molecule=
    """
    multiplicity 3
    1 O u1 p2 c0 {2,S}
    2 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(107.400, 'K'),
        sigma=(3.458, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(1.6, 'angstroms^3'),
        rotrelaxcollnum=3.8,
    ),
    shortDesc=u"""""",
)

entry(
    index=70,
    label="OH",
    molecule=
    """
    multiplicity 2
    1 O u1 p2 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(80.000, 'K'),
        sigma=(2.750, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=71,
    label="HE",
    molecule=
    """
    1 He u0 p1 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(10.200, 'K'),
        sigma=(2.576, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=72,
    label="HONO",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,D}
    2 O u0 p2 c0 {1,S} {4,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(350.000, 'K'),
        sigma=(3.950, 'angstroms'),
        dipoleMoment=(1.639, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=73,
    label="NO",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,D}
    2 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(139.320, 'K'),
        sigma=(3.339, 'angstroms'),
        dipoleMoment=(0.2, 'De'),
        polarizability=(1.76, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=74,
    label="HNO",
    molecule=
    """
    1 N u0 p1 c0 {2,D} {3,S}
    2 O u0 p2 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(170.000, 'K'),
        sigma=(3.430, 'angstroms'),
        dipoleMoment=(1.62, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=75,
    label="NO2",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,D} {3,S}
    2 O u0 p2 c0 {1,D}
    3 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(333.590, 'K'),
        sigma=(3.852, 'angstroms'),
        dipoleMoment=(0.4, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=76,
    label="CH3CH2OH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 O u0 p2 c0 {1,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=77,
    label="CH3CH2O",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
    3 O u1 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(362.600, 'K'),
        sigma=(4.530, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=78,
    label="CH3CO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=79,
    label="CH3CHO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,D} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=80,
    label="OCHCHO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,D} {5,S}
    2 C u0 p0 c0 {1,S} {4,D} {6,S}
    3 O u0 p2 c0 {1,D}
    4 O u0 p2 c0 {2,D}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(440.200, 'K'),
        sigma=(4.010, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=81,
    label="NO3",
    molecule=
    """
    multiplicity 2
    1 N u0 p0 c+1 {2,D} {3,S} {4,S}
    2 O u0 p2 c0 {1,D}
    3 O u0 p3 c-1 {1,S}
    4 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(400.000, 'K'),
        sigma=(4.200, 'angstroms'),
        dipoleMoment=(0.2, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=82,
    label="N2O",
    molecule=
    """
    1 N u0 p0 c+1 {2,D} {3,D}
    2 N u0 p2 c-1 {1,D}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.2, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=83,
    label="H2NO",
    molecule=
    """
    multiplicity 2
    1 N u1 p0 c+1 {2,S} {3,S} {4,S}
    2 O u0 p3 c-1 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=84,
    label="HNOH",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,S} {3,S}
    2 O u0 p2 c0 {1,S} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(116.700, 'K'),
        sigma=(3.492, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=85,
    label="CH2CN",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 C u0 p0 c0 {1,S} {5,T}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 N u0 p1 c0 {2,T}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(3.5, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=86,
    label="CH3CN",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,T}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 N u0 p1 c0 {2,T}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(3.5, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=87,
    label="NCN",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,D} {3,D}
    2 N u1 p1 c0 {1,D}
    3 N u1 p1 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(2.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=88,
    label="HNCN",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,T}
    2 N u1 p1 c0 {1,S} {4,S}
    3 N u0 p1 c0 {1,T}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(2.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=89,
    label="HNCNH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,D}
    2 N u0 p1 c0 {1,D} {4,S}
    3 N u0 p1 c0 {1,D} {5,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(2.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=90,
    label="CN",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(75.000, 'K'),
        sigma=(3.856, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=91,
    label="H2CN",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 N u1 p1 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=92,
    label="HCN",
    molecule=
    """
    1 C u0 p0 c0 {2,T} {3,S}
    2 N u0 p1 c0 {1,T}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=93,
    label="HCNO",
    molecule=
    """
    1 N u0 p0 c+1 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {4,S}
    3 O u0 p3 c-1 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=94,
    label="HOCN",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,T}
    2 O u0 p2 c0 {1,S} {4,S}
    3 N u0 p1 c0 {1,T}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=95,
    label="HNCO",
    molecule=
    """
    1 N u0 p1 c0 {2,D} {4,S}
    2 C u0 p0 c0 {1,D} {3,D}
    3 O u0 p2 c0 {2,D}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=96,
    label="HNNO",
    molecule=
    """
    multiplicity 2
    1 O u0 p2 c0 {2,D}
    2 N u0 p1 c0 {1,D} {3,S}
    3 N u1 p1 c0 {2,S} {4,S}
    4 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=97,
    label="N",
    molecule=
    """
    multiplicity 4
    1 N u3 p1 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(71.400, 'K'),
        sigma=(3.298, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=98,
    label="N2H2",
    molecule=
    """
    1 N u0 p1 c0 {2,D} {3,S}
    2 N u0 p1 c0 {1,D} {4,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(71.400, 'K'),
        sigma=(3.798, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=99,
    label="N2H3",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 N u1 p1 c0 {1,S} {5,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(200.000, 'K'),
        sigma=(3.900, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=100,
    label="N2H4",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(205.000, 'K'),
        sigma=(4.230, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(4.26, 'angstroms^3'),
        rotrelaxcollnum=1.5,
    ),
    shortDesc=u"""""",
)

entry(
    index=101,
    label="NCO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,D}
    2 N u1 p1 c0 {1,D}
    3 O u0 p2 c0 {1,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=102,
    label="NH",
    molecule=
    """
    multiplicity 3
    1 N u2 p1 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(80.000, 'K'),
        sigma=(2.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=103,
    label="NH2",
    molecule=
    """
    multiplicity 2
    1 N u1 p1 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(80.000, 'K'),
        sigma=(2.650, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(2.26, 'angstroms^3'),
        rotrelaxcollnum=4.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=104,
    label="NH3",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(481.000, 'K'),
        sigma=(2.920, 'angstroms'),
        dipoleMoment=(1.47, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=10.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=105,
    label="NNH",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,D} {3,S}
    2 N u1 p1 c0 {1,D}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(71.400, 'K'),
        sigma=(3.798, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=106,
    label="NCNO",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {3,D}
    2 C u0 p0 c0 {1,S} {4,T}
    3 O u0 p2 c0 {1,D}
    4 N u0 p1 c0 {2,T}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=107,
    label="NCCN",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,S} {3,T}
    2 C u1 p0 c0 {1,S} {4,D}
    3 N u0 p1 c0 {1,T}
    4 N u1 p1 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(374.000, 'K'),
        sigma=(4.361, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=108,
    label="O3",
    molecule=
    """
    1 O u0 p3 c-1 {2,S}
    2 O u0 p1 c+1 {1,S} {3,D}
    3 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(180.000, 'K'),
        sigma=(4.100, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=109,
    label="Cl",
    molecule=
    """
    multiplicity 2
    1 Cl u1 p3 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(130.800, 'K'),
        sigma=(3.613, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=110,
    label="HCl",
    molecule=
    """
    1 H  u0 p0 c0 {2,S}
    2 Cl u0 p3 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(344.700, 'K'),
        sigma=(3.339, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

# entry(
#    index = 111,
#    label = "F",
#    molecule =
# """
# multiplicity 2
# 1 F u1 p3 c0
# """,
#    transport = TransportData(
#        shapeIndex = 0,
#        epsilon = (80.000,'K'),
#        sigma = (2.750,'angstroms'),
#        dipoleMoment = (0.0,'De'),
#        polarizability = (0.0,'angstroms^3'),
#        rotrelaxcollnum = 0.0,
#    ),
#    shortDesc = u"""""",
# )

# entry(
#    index = 112,
#    label = "HF",
#    molecule =
# """
# 1 H u0 p0 c0 {2,S}
# 2 F u0 p3 c0 {1,S}
# """,
#    transport = TransportData(
#        shapeIndex = 1,
#        epsilon = (330.000,'K'),
#        sigma = (3.148,'angstroms'),
#        dipoleMoment = (1.92,'De'),
#        polarizability = (2.46,'angstroms^3'),
#        rotrelaxcollnum = 1.0,
#    ),
#    shortDesc = u"""""",
# )

# entry(
#    index = 113,
#    label = "F2",
#    molecule =
# """
# 1 F u0 p3 c0 {2,S}
# 2 F u0 p3 c0 {1,S}
# """,
#    transport = TransportData(
#        shapeIndex = 0,
#        epsilon = (80.000,'K'),
#        sigma = (2.750,'angstroms'),
#        dipoleMoment = (0.0,'De'),
#        polarizability = (0.0,'angstroms^3'),
#        rotrelaxcollnum = 0.0,
#    ),
#    shortDesc = u"""""",
# )

entry(
    index=114,
    label="H2S",
    molecule=
    """
    1 S u0 p2 c0 {2,S} {3,S}
    2 H u0 p0 c0 {1,S}
    3 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(301.000, 'K'),
        sigma=(3.600, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=115,
    label="HSO2",
    molecule=
    """
    multiplicity 2
    1 O u0 p2 c0 {2,D}
    2 S u1 p0 c0 {1,D} {3,S} {4,D}
    3 H u0 p0 c0 {2,S}
    4 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.290, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=116,
    label="S",
    molecule=
    """
    multiplicity 3
    1 S u2 p2 c0
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(847.000, 'K'),
        sigma=(3.839, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=0.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=117,
    label="S2",
    molecule=
    """
    multiplicity 3
    1 S u1 p2 c0 {2,S}
    2 S u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=0,
        epsilon=(847.000, 'K'),
        sigma=(3.900, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=118,
    label="SH",
    molecule=
    """
    multiplicity 2
    1 S u1 p2 c0 {2,S}
    2 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(847.000, 'K'),
        sigma=(3.900, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=119,
    label="SO",
    molecule=
    """
    multiplicity 3
    1 S u1 p2 c0 {2,S}
    2 O u1 p2 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(301.000, 'K'),
        sigma=(3.993, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=120,
    label="SO2",
    molecule=
    """
    1 O u0 p2 c0 {2,D}
    2 S u0 p1 c0 {1,D} {3,D}
    3 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(252.000, 'K'),
        sigma=(4.290, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=121,
    label="SO3",
    molecule=
    """
    1 O u0 p2 c0 {2,D}
    2 S u0 p0 c0 {1,D} {3,D} {4,D}
    3 O u0 p2 c0 {2,D}
    4 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(378.400, 'K'),
        sigma=(4.175, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=122,
    label="CH2NO",
    molecule=
    """
    multiplicity 2
    1 C u1 p0 c0 {2,S} {3,S} {4,S}
    2 N u0 p1 c0 {1,S} {5,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=123,
    label="C2H5NO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 N u0 p1 c0 {1,S} {9,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(252.000, 'K'),
        sigma=(4.760, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=124,
    label="CH3CHNO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,D} {7,S}
    3 N u0 p1 c0 {2,D} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(252.000, 'K'),
        sigma=(4.760, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=125,
    label="CHCHNO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 N u0 p1 c0 {1,S} {6,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(357.000, 'K'),
        sigma=(5.180, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=126,
    label="CH2CHNO",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u0 p0 c0 {1,D} {5,S} {6,S}
    3 N u0 p1 c0 {1,S} {7,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(357.000, 'K'),
        sigma=(5.176, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=127,
    label="CH3NO2",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p0 c+1 {1,S} {6,D} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    7 O u0 p3 c-1 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=128,
    label="CH3ONO",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 N u0 p1 c0 {2,S} {7,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 O u0 p2 c0 {3,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=129,
    label="CH2NO2",
    molecule=
    """
    multiplicity 2
    1 N u0 p0 c+1 {2,S} {3,D} {6,S}
    2 C u1 p0 c0 {1,S} {4,S} {5,S}
    3 O u0 p2 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    6 O u0 p3 c-1 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(232.400, 'K'),
        sigma=(3.828, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=130,
    label="C2H5NO2",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3  N u0 p0 c+1 {1,S} {9,D} {10,S}
    4  H u0 p0 c0 {1,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {2,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  O u0 p2 c0 {3,D}
    10 O u0 p3 c-1 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.88, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=131,
    label="CH2CH2NO2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 N u0 p0 c+1 {1,S} {6,D} {7,S}
    3 C u1 p0 c0 {1,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 O u0 p2 c0 {2,D}
    7 O u0 p3 c-1 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.88, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=132,
    label="CH3CHNO2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,S} {7,S}
    3 N u0 p0 c+1 {2,S} {8,D} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 O u0 p2 c0 {3,D}
    9 O u0 p3 c-1 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.88, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=133,
    label="CH3ONO2",
    molecule=
    """
    1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2 N u0 p0 c+1 {3,S} {7,D} {8,S}
    3 O u0 p2 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 O u0 p2 c0 {2,D}
    8 O u0 p3 c-1 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(459.500, 'K'),
        sigma=(5.036, 'angstroms'),
        dipoleMoment=(1.7, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=134,
    label="CH3CH2ONO",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
    3  O u0 p2 c0 {1,S} {4,S}
    4  N u0 p1 c0 {3,S} {10,D}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 O u0 p2 c0 {4,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(503.072, 'K'),
        sigma=(5.340, 'angstroms'),
        dipoleMoment=(1.67, 'De'),
        polarizability=(8.8, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=135,
    label="CH3CH2ONO2",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
    3  N u0 p0 c+1 {4,S} {10,D} {11,S}
    4  O u0 p2 c0 {1,S} {3,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 O u0 p2 c0 {3,D}
    11 O u0 p3 c-1 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(496.000, 'K'),
        sigma=(5.200, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=136,
    label="HNC",
    molecule=
    """
    1 N u0 p0 c+1 {2,S} {3,T}
    2 H u0 p0 c0 {1,S}
    3 C u0 p1 c-1 {1,T}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(569.000, 'K'),
        sigma=(3.630, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=137,
    label="CH3CH2NH2",
    molecule=
    """
    1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3  N u0 p1 c0 {1,S} {9,S} {10,S}
    4  H u0 p0 c0 {1,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {2,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {3,S}
    10 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=138,
    label="CH3NHCH3",
    molecule=
    """
    1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
    3  N u0 p1 c0 {1,S} {2,S} {10,S}
    4  H u0 p0 c0 {1,S}
    5  H u0 p0 c0 {1,S}
    6  H u0 p0 c0 {1,S}
    7  H u0 p0 c0 {2,S}
    8  H u0 p0 c0 {2,S}
    9  H u0 p0 c0 {2,S}
    10 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=139,
    label="CH2CH2NH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u1 p0 c0 {1,S} {6,S} {7,S}
    3 N u0 p1 c0 {1,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=140,
    label="CH3NCH3",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
    3 N u1 p1 c0 {1,S} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=141,
    label="CH3NHCH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 N u0 p1 c0 {1,S} {3,S} {7,S}
    3 C u1 p0 c0 {2,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=142,
    label="CH3CHNH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,S} {7,S}
    3 N u0 p1 c0 {2,S} {8,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=143,
    label="CH3CH2NH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
    3 N u1 p1 c0 {1,S} {9,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    9 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=144,
    label="CH2CHNH2",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 C u0 p0 c0 {1,D} {7,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(303.400, 'K'),
        sigma=(4.810, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=145,
    label="CH3CHNH",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,D} {7,S}
    3 N u0 p1 c0 {2,D} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(303.400, 'K'),
        sigma=(4.810, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=146,
    label="CH3NCH2",
    molecule=
    """
    1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {3,D} {7,S} {8,S}
    3 N u0 p1 c0 {1,S} {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {2,S}
    8 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(303.400, 'K'),
        sigma=(4.810, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=147,
    label="CH2CHNH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 C u1 p0 c0 {1,S} {5,S} {6,S}
    3 N u0 p1 c0 {1,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=148,
    label="CHCHNH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,D} {4,S}
    2 N u0 p1 c0 {1,S} {5,S} {6,S}
    3 C u1 p0 c0 {1,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=149,
    label="CH2NCH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {3,D} {6,S} {7,S}
    2 C u1 p0 c0 {3,S} {4,S} {5,S}
    3 N u0 p1 c0 {1,D} {2,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=150,
    label="CH3CHN",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {6,D} {7,S}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 N u1 p1 c0 {2,D}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=151,
    label="CH3NCH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 N u0 p1 c0 {1,S} {3,D}
    3 C u1 p0 c0 {2,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=152,
    label="CH3CNH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u1 p0 c0 {1,S} {3,D}
    3 N u0 p1 c0 {2,D} {7,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=153,
    label="CH2CNH2",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {3,D} {4,S} {5,S}
    2 N u0 p1 c0 {3,S} {6,S} {7,S}
    3 C u1 p0 c0 {1,D} {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    7 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=154,
    label="CH2CNH",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {4,S} {5,S}
    2 C u0 p0 c0 {1,D} {3,D}
    3 N u0 p1 c0 {2,D} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=155,
    label="CH2CHN",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,S} {3,D} {6,S}
    2 C u1 p0 c0 {1,S} {4,S} {5,S}
    3 N u1 p1 c0 {1,D}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    6 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=156,
    label="CH2CHN(S)",
    molecule=
    """
    1 C u0 p0 c0 {2,D} {4,S} {5,S}
    2 C u0 p0 c0 {1,D} {3,S} {6,S}
    3 N u0 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=157,
    label="c-C2H3N",
    molecule=
    """
    1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,D} {6,S}
    3 N u0 p1 c0 {1,S} {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=158,
    label="CHCNH2",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,T}
    3 C u0 p0 c0 {2,T} {6,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(260.000, 'K'),
        sigma=(4.850, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=159,
    label="CHCNH",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,T} {3,S}
    2 C u0 p0 c0 {1,T} {5,S}
    3 N u1 p1 c0 {1,S} {4,S}
    4 H u0 p0 c0 {3,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=1,
        epsilon=(252.000, 'K'),
        sigma=(4.760, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=160,
    label="H2NCHO",
    molecule=
    """
    1 N u0 p1 c0 {2,S} {4,S} {5,S}
    2 C u0 p0 c0 {1,S} {3,D} {6,S}
    3 O u0 p2 c0 {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=161,
    label="H2NCO",
    molecule=
    """
    multiplicity 2
    1 N u0 p1 c0 {2,S} {3,S} {4,S}
    2 C u1 p0 c0 {1,S} {5,D}
    3 H u0 p0 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 O u0 p2 c0 {2,D}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(307.800, 'K'),
        sigma=(4.140, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=162,
    label="CH3NC",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 N u0 p1 c0 {1,S} {3,D}
    3 C u2 p0 c0 {2,D}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(422.220, 'K'),
        sigma=(5.329, 'angstroms'),
        dipoleMoment=(3.5, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=163,
    label="CH3C(O)OO",
    molecule=
    """
    multiplicity 2
    1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
    2 C u0 p0 c0 {1,S} {3,S} {7,D}
    3 O u0 p2 c0 {2,S} {8,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {1,S}
    6 H u0 p0 c0 {1,S}
    7 O u0 p2 c0 {2,D}
    8 O u1 p2 c0 {3,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(435.500, 'K'),
        sigma=(4.860, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=1.0,
    ),
    shortDesc=u"""""",
)

entry(
    index=164,
    label="CHCHO",
    molecule=
    """
    multiplicity 3
    1 C u0 p0 c0 {2,D} {3,S} {4,S}
    2 C u1 p0 c0 {1,D} {5,S}
    3 O u1 p2 c0 {1,S}
    4 H u0 p0 c0 {1,S}
    5 H u0 p0 c0 {2,S}
    """,
    transport=TransportData(
        shapeIndex=2,
        epsilon=(436.000, 'K'),
        sigma=(3.970, 'angstroms'),
        dipoleMoment=(0.0, 'De'),
        polarizability=(0.0, 'angstroms^3'),
        rotrelaxcollnum=2.0,
    ),
    shortDesc=u"""""",
)

"""
Additional species which weren't added to this library, as well as general comments can be found in the original file:


! 2015-10-13:
! Replacing CH3CO2 by CH3C(O)O
! 16-06-22:
! Estimations were revised.
! 15-06-18:
! Transport data for CH3OO and CH3OOH were updated!
! 15-02-27:
! Changing nomenclature:
! CH3OCH2O2 => CH3OCH2OO
! CH3OCH2O2H => CH3OCH2OOH
! CH2OCH2O2H => CH2OCH2OOH
! 15-02-25:
! CYCOOC. was renamed to cC2H3O2, so CYCOOC. ==~~> cC2H3O2
!!===============================================================


! CHCHO was set equal to CH2CO
CHCHO              2   436.000     3.970     0.000     0.000     2.000

!!! Added for calculation of flame speed (just estimations!), revised on 2015-09-08:
CH3C(O)O           2   395.0       4.037     1.3       0.0       1.0   ! =CH3OCO => CH3OCH3
CH3C(O)OO 		   2   435.500     4.860     0.000     0.000     1.0   ! =OOCH2CHO => CH3COCH3
CH3C(O)OOH		   2   395.0       4.037     1.3       0.0       1.0   ! =HOCH2CH2OO => CH3OCH2OH 


!!! Added for calculation of flame speed (just estimations!), revised on 2015-06-22/24:

OCHCO             2   440.200     4.010     0.000     0.000     2.000 ! =chocho, Marinov
HCOH               2   498.000     3.590     0.000     0.000     1.000 ! =hcoh, Marinov
OCH2CHO            2   395.0       4.037     1.3       0.0       1.0   ! CH2OCHO
CH2CHOOH           2   395.0       4.037     1.3       0.0       1.0   ! CH2OCHO
cC2H3O2            2   395.0       4.037     1.3       0.0       1.0   ! CH2OCHO
CH2CHOO            2   395.0       4.037     1.3       0.0       1.0   ! CH2OCHO
OOCH2CHO           2   435.500     4.860     0.000     0.000     1.000 ! = CH3COCH3  
HOOCH2CO           2   435.500     4.860     0.000     0.000     1.000 ! = CH3COCH3  
CH3OC*OO 		   2   435.2       4.662     2.7       0.0       1.0   ! = CH3OC*OOO
HOCHOH             2   481.800     3.626     1.7       0.000     1.000 ! = HOCHO
CH3CHOH            2   362.600     4.530     0.000     0.000     1.500                              
H2CC               1   209.000     4.100     0.000     0.000     2.500 ! = C2H2
CH2OOH             2   417.000     3.690     1.700     0.000     2.000 ! = CH3OO
CH2CH2OH           2   362.600     4.530     0.000     0.000     1.500 ! = CH3CH2O (LLNL)
CH2CHOH            2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
cC2H4O             2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
cC2H3O             2   436.000     3.970     0.000     0.000     2.000 ! = CH3CO

CH3OCH2OH          2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3CH2OOH          2   395.0       4.037     1.3       0.0       1.0   ! =CH3OCH2OH
CH3CH2OO           2   395.0       4.037     1.3       0.0       1.0   ! =CH3OCH2OH
CH2CH2OOH          2   395.0       4.037     1.3       0.0       1.0   ! =CH3OCH2OH
CH3CHOOH           2   395.0       4.037     1.3       0.0       1.0   ! =CH3OCH2OH
HOCH2CH2OO         2   395.0       4.037     1.3       0.0       1.0   ! =CH3OCH2OH

HON                2   116.700     3.492     0.000     0.000     1.000 ! = HNO
HNO2               2   350.000     3.950     1.639     0.000     1.000 ! = HONO
HONO2              2   400.000     4.200     0.200     0.000     1.000 ! = NO3
H2NN               2    71.400     3.798     0.000     0.000     1.000 ! = N2H2
NH2OH              2   116.700     3.492     0.000     0.000     1.000 ! = NHOH
HNC                1   569.000     3.630     0.000     0.000     1.000 ! = HCN
HCNH               1   569.000     3.630     0.000     0.000     1.000 ! = H2CN
CH3NO              2   436.000     3.970     0.000     0.000     2.000 ! = CH3CO
CH3NH2             2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH3NH              2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH2NH2             2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH2NH              2   417.000     3.690     1.700     0.000     2.000 ! = CH2OH

!! Added from CRECK Modeling Group (Politecnico di Milano, http://creckmodeling.chem.polimi.it/)
CH3OO              2   417.000     3.690     1.700     0.000     2.000                              
CH3OOH             2   481.800     3.626     0.000     0.000     1.000                              


!!===============================================================
! HASGLA15/DME: From Dooley et al., Int J Chem Kinet 42 (2010) 527-549:
HOCH2O             2   470.600     4.410     0.000     0.000     1.500 ! WJP
HOCO               2   498.000     3.590     0.000     0.000     2.000 !WKM =OCHO LLNL
HOCHO              2   481.800     3.626     1.7       0.000     1.000 ! WJP: CH3OH
OCHO               2   498.000     3.590     0.000     0.000     2.000 ! WJP
CH3OCH3            2   395.0       4.037     1.3       0.0       1.0   ! SVE,RPD
CH3OCH2            2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3OCH2OO          2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH2OCH2OOH         2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3OCH2OOH         2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3OCH2O           2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3OCHO            2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3OCO             2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH2OCHO            2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3
CH3OC*OOOH         2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
HOOCH2OC*O         2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
CH2OC*OOOH         2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
CH3OC*OOO          2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
OOCH2OCHO          2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
CYOCH2OC*O         2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
OOCH2OC*OOOH       2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
O*CHOC*OOOH        2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000)
CHOOCO             2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000) 
HOOCH2OC*OOO       2   435.2       4.662     2.7       0.0       1.0   ! WJP (FISHER ET AL 2000)
!CH3CO2             2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)
OCH2O2H            2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)
EF                 2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)  
EFP                2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)  
EFS                2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)  
EFF                2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)  
ME                 2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007)   
ME2J               2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007) 
MEMJ               2   395.0       4.037     1.3       0.0       1.0   ! CH3OCH3 (ZHAO ET AL IJCK 2007) 




!WKM 
!THESE ARE CRUDE ESTIMATES BUT THESE SPECIES WILL NOT BE IMPORTANT AT HIGH TEMPERATURES.
O2CH2OCH2O2H         2   496.000     5.200     0.000     0.000     1.000 ! *
HO2CH2OCHO         2   496.000     5.200     0.000     0.000     1.000 ! *
OCH2OCHO         2   496.000     5.200     0.000     0.000     1.000 ! *
HOCH2OCO          2   496.000     5.200     0.000     0.000     1.000 ! *



!!===============================================================
! Transport properties below are from
! M. P. Burke, M. Chaos, Y. Ju, F. L. Dryer, S. J. Klippenstein, Int. J. Chem. Kinet. 44(2012) 444474.

AR                 0   136.500     3.330     0.000     0.000     0.000          
C                  0    71.400     3.298     0.000     0.000     0.000 ! *      
CH                 1    80.000     2.750     0.000     0.000     0.000          
CH2                1   144.000     3.800     0.000     0.000     0.000          
CH2*               1   144.000     3.800     0.000     0.000     0.000          
CH3                1   144.000     3.800     0.000     0.000     0.000          
CH4                2   141.400     3.746     0.000     2.600    13.000          
CO                 1    98.100     3.650     0.000     1.950     1.800          
CO2                1   244.000     3.763     0.000     2.650     2.100          
HCO                2   498.000     3.590     0.000     0.000     0.000          
CH2O               2   498.000     3.590     0.000     0.000     2.000          
CH2OH              2   417.000     3.690     1.700     0.000     2.000          
CH3O               2   417.000     3.690     1.700     0.000     2.000          
CH3OH              2   481.800     3.626     0.000     0.000     1.000 ! SVE    

C2                 1    97.530     3.621     0.000     1.760     4.000          
C2O                1   232.400     3.828     0.000     0.000     1.000 ! *      
C2H                1   209.000     4.100     0.000     0.000     2.500          
C2H2               1   209.000     4.100     0.000     0.000     2.500          
C2H3               2   209.000     4.100     0.000     0.000     1.000 ! *      
C2H4               2   280.800     3.971     0.000     0.000     1.500          
C2H5               2   252.300     4.302     0.000     0.000     1.500          
C2H6               2   252.300     4.302     0.000     0.000     1.500          
HCCO               2   150.000     2.500     0.000     0.000     1.000 ! *      
HCCOH              2   436.000     3.970     0.000     0.000     2.000          
CH2CO              2   436.000     3.970     0.000     0.000     2.000          
CH2CHO             2   436.000     3.970     0.000     0.000     2.000          
C2H2OH             2   224.700     4.162     0.000     0.000     1.000 ! *      

C3H2               2   209.000     4.100     0.000     0.000     1.000 ! *      
C3H3               2   252.000     4.760     0.000     0.000     1.000 ! JAM    
aC3H4              1   252.000     4.760     0.000     0.000     1.000          
pC3H4              1   252.000     4.760     0.000     0.000     1.000          
cC3H4              1   252.000     4.760     0.000     0.000     1.000
CH2OCH2            1   252.000     4.760     0.000     0.000     1.000
CH2OCH             1   252.000     4.760     0.000     0.000     1.000
CH3CH2CHO          1   252.000     4.760     0.000     0.000     1.000

C4H                1   357.000     5.180     0.000     0.000     1.000          
C4H2               1   357.000     5.180     0.000     0.000     1.000          
H2C4O              2   357.000     5.180     0.000     0.000     1.000 ! JAM    
C4H2OH             2   224.700     4.162     0.000     0.000     1.000 ! *      
iC4H3              2   357.000     5.180     0.000     0.000     1.000 ! JAM    
nC4H3              2   357.000     5.180     0.000     0.000     1.000 ! JAM    
C4H4               2   357.000     5.180     0.000     0.000     1.000 ! JAM    
iC4H5              2   357.000     5.180     0.000     0.000     1.000 ! JAM    
nC4H5              2   357.000     5.180     0.000     0.000     1.000 ! JAM    
C4H5-2             2   357.000     5.180     0.000     0.000     1.000 !
C4H6               2   357.000     5.180     0.000     0.000     1.000         
C4H6-2             2   357.000     5.180     0.000     0.000     1.000
C4H612             2   357.000     5.180     0.000     0.000     1.000 
CH3CHOCH2          2   357.000     5.180     0.000     0.000     1.000




H                  0   145.000     2.050     0.000     0.000     0.000          
H2                 1    38.000     2.920     0.000     0.790   280.000          
H2O                2   572.400     2.605     1.844     0.000     4.000          
H2O2               2   107.400     3.458     0.000     0.000     3.800          
HO2                2   107.400     3.458     0.000     0.000     1.000 ! *      
N2                 1    97.530     3.621     0.000     1.760     4.000          
O                  0    80.000     2.750     0.000     0.000     0.000          
O*                 0    80.000     2.750     0.000     0.000     0.000 ! dummy          
O2                 1   107.400     3.458     0.000     1.600     3.800          
OH                 1    80.000     2.750     0.000     0.000     0.000          










!!===============================================================
! Transport properties below are from
! M. P. Burke, M. Chaos, Y. Ju, F. L. Dryer, S. J. Klippenstein, Int. J. Chem. Kinet. 44(2012) 444474.

HE                 0    10.200     2.576     0.000     0.000     0.000 ! *      
C5H2               1   357.000     5.180     0.000     0.000     1.000          
C5H3               1   357.000     5.180     0.000     0.000     1.000          
C5H5               1   357.000     5.180     0.000     0.000     1.000          
C5H6               1   357.000     5.180     0.000     0.000     1.000          
lC5H7              1   357.000     5.180     0.000     0.000     1.000
C4H6O25            1   357.000     5.180     0.000     0.000     1.000
C4H6O23            1   357.000     5.180     0.000     0.000     1.000
C4H4O              1   357.000     5.180     0.000     0.000     1.000
CH2CHCO            1   357.000     5.180     0.000     0.000     1.000
CH3CHOCH2          1   357.000     5.180     0.000     0.000     1.000
CH2CHCHCHO         1   357.000     5.180     0.000     0.000     1.000
CH3CHCHCO          1   357.000     5.180     0.000     0.000     1.000
C2H3CHOCH2         1   357.000     5.180     0.000     0.000     1.000
CH3CHCHCHO         1   357.000     5.180     0.000     0.000     1.000

C6H                1   357.000     5.180     0.000     0.000     1.000          
C6H2               1   357.000     5.180     0.000     0.000     1.000          
C6H3               2   357.000     5.180     0.000     0.000     1.000  !       
l-C6H4             2   412.300     5.349     0.000     0.000     1.000  !(JAM)  
nC6H5              2   412.300     5.349     0.000     0.000     1.000  !(JAM)  
i-C6H5             2   412.300     5.349     0.000     0.000     1.000  !(JAM)  
l-C6H6             2   412.300     5.349     0.000     0.000     1.000  !(SVE)  
n-C6H7             2   412.300     5.349     0.000     0.000     1.000  !(JAM)  
i-C6H7             2   412.300     5.349     0.000     0.000     1.000  !(JAM)  
C6H8               2   412.300     5.349     0.000     0.000     1.000  !(JAM)  



!!===============================================================
!!===============================================================
!
!  Transport Properties obtained from GRI-Mech 3.0
!
!  Additions (at top) for "Glarborg" mechanism.
!  Some of these represent changes to the GRI data.
!  Entered by Joe Grcar as recommended by Chris Pope.
HONO               2   350.000     3.950     1.639     0.000     1.000 ! CJP
NO                 1   139.320     3.339     0.200     1.760     4.000 ! CJP
HNO                2   170.000     3.430     1.620     0.000     1.000 ! CJP
NO2                2   333.590     3.852     0.400     0.000     1.000 ! CJP
CH2(S)             1   144.000     3.800     0.000     0.000     0.000
CH3CH2OH           2   362.600     4.530     0.000     0.000     1.500 ! nmm (LLNL)   
CH3CH2O            2   362.600     4.530     0.000     0.000     1.500 ! nmm (LLNL)
CH3CO              2   436.000     3.970     0.000     0.000     2.000


CH3CHO             2   436.000     3.970     0.000     0.000     2.000
CH2CHCHO           2   443.200     4.120     0.000     0.000     1.000 ! nmm (LLNL)
CH4O               2   417.000     3.690     1.700     0.000     2.000
CHCHOH             2   224.700     4.162     0.000     0.000     1.000 ! *
OCHCHO             2   440.200     4.010     0.000     0.000     2.000 ! NMM CHOCHO
NO3                2   400.000     4.200     0.200     0.000     1.000 ! CJP
N2O                1   232.400     3.828     0.000     0.000     1.000 ! *
H2NO               2   116.700     3.492     0.000     0.000     1.000 ! JAM
HNOH               2   116.700     3.492     0.000     0.000     1.000 ! JAM




!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!! E N D !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!end
!!===============================================================
!!===============================================================
!
!  Transport Properties obtained from GRI-Mech 3.0
!
!  Additions (at top) for "Glarborg" mechanism.
!  Some of these represent changes to the GRI data.
!  Entered by Joe Grcar as recommended by Chris Pope.
!
C2H5CHO            2   424.600     4.820     0.000     0.000     1.000 ! NMM
C2H5CO             2   424.600     4.820     2.700     0.000     1.000 ! NMM, CJP
CH2CHCO            2   443.200     4.120     0.000     0.000     1.000 ! nmm (LLNL)
CH2CN              2   422.220     5.329     3.500     0.000     1.000 ! CJP
CH2HCO             2   436.000     3.970     0.000     0.000     2.000 ! CH2CHO
CH3CHCO            2   443.200     4.120     0.000     0.000     1.000 ! nmm (LLNL)
CH3CN              2   422.220     5.329     3.500     0.000     1.000 ! CJP
CH3HCO             2   436.000     3.970     0.000     0.000     2.000 ! CH3CHO
H2CCCH2            1   324.800     4.290     0.000     0.000     1.000 ! nmm (LLNL)
H3CCCH             1   324.800     4.290     0.000     0.000     1.000 ! nmm (LLNL)
cC3H4              2   324.800     4.290     0.000     0.000     1.000 ! nmm (LLNL)
CH2CCH3            2   260.000     4.850     0.000     0.000     1.000 ! JAM
HONO               2   350.000     3.950     1.639     0.000     1.000 ! CJP
NO3                2   400.000     4.200     0.200     0.000     1.000 ! CJP
OCHCHO             2   440.200     4.010     0.000     0.000     2.000 ! NMM CHOCHO
NCN                1   422.220     5.329     2.000     0.000     1.000 ! CJP
HNCN               1   422.220     5.329     2.000     0.000     1.000 ! NCN
HNCNH              1   422.220     5.329     2.000     0.000     1.000 ! NCN
NO                 1   139.320     3.339     0.200     1.760     4.000 ! CJP
HNO                2   170.000     3.430     1.620     0.000     1.000 ! CJP
NO2                2   333.590     3.852     0.400     0.000     1.000 ! CJP
!
AR                 0   136.500     3.330     0.000     0.000     0.000
C                  0    71.400     3.298     0.000     0.000     0.000 ! *
C2                 1    97.530     3.621     0.000     1.760     4.000
C2O                1   232.400     3.828     0.000     0.000     1.000 ! *
CN2                1   232.400     3.828     0.000     0.000     1.000 ! OIS
C2H                1   209.000     4.100     0.000     0.000     2.500
C2H2               1   209.000     4.100     0.000     0.000     2.500
!C2H2OH             2   224.700     4.162     0.000     0.000     1.000 ! *
CHCHOH             2   224.700     4.162     0.000     0.000     1.000 ! *
C2H3               2   209.000     4.100     0.000     0.000     1.000 ! *
C2H4               2   280.800     3.971     0.000     0.000     1.500
C2H5               2   252.300     4.302     0.000     0.000     1.500
C2H6               2   252.300     4.302     0.000     0.000     1.500
C2N                1   232.400     3.828     0.000     0.000     1.000 ! OIS
C2N2               1   349.000     4.361     0.000     0.000     1.000 ! OIS
C3H                1   232.400     3.828     0.000     0.000     1.000 ! (LLNL)
C3H2               2   209.000     4.100     0.000     0.000     1.000 ! *
C3H4               1   252.000     4.760     0.000     0.000     1.000
C3H6               2   266.800     4.982     0.000     0.000     1.000
C3H7               2   266.800     4.982     0.000     0.000     1.000
C4H6               2   357.000     5.180     0.000     0.000     1.000
I*C3H7             2   266.800     4.982     0.000     0.000     1.000
N*C3H7             2   266.800     4.982     0.000     0.000     1.000
C3H8               2   266.800     4.982     0.000     0.000     1.000
C4H                1   357.000     5.180     0.000     0.000     1.000
C4H2               1   357.000     5.180     0.000     0.000     1.000
C4H2OH             2   224.700     4.162     0.000     0.000     1.000 ! *
C4H8               2   357.000     5.176     0.000     0.000     1.000
C4H9               2   357.000     5.176     0.000     0.000     1.000
I*C4H9             2   357.000     5.176     0.000     0.000     1.000
C5H2               1   357.000     5.180     0.000     0.000     1.000
C5H3               1   357.000     5.180     0.000     0.000     1.000
C6H2               1   357.000     5.180     0.000     0.000     1.000
C6H5               2   412.300     5.349     0.000     0.000     1.000 ! JAM
C6H5O              2   450.000     5.500     0.000     0.000     1.000 ! JAM
C5H5OH             2   450.000     5.500     0.000     0.000     1.000 ! JAM
C6H6               2   412.300     5.349     0.000     0.000     1.000 ! SVE
C6H7               2   412.300     5.349     0.000     0.000     1.000 ! JAM
CH                 1    80.000     2.750     0.000     0.000     0.000
CH2                1   144.000     3.800     0.000     0.000     0.000
CH2(S)             1   144.000     3.800     0.000     0.000     0.000
CH2*               1   144.000     3.800     0.000     0.000     0.000
CH2CHCCH           2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CHCCH2          2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CHCH2           2   260.000     4.850     0.000     0.000     1.000 ! JAM
CH2CHCHCH          2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CHCHCH2         2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CO              2   436.000     3.970     0.000     0.000     2.000
CH2O               2   498.000     3.590     0.000     0.000     2.000
CH2OH              2   417.000     3.690     1.700     0.000     2.000
CH3CC              2   252.000     4.760     0.000     0.000     1.000 ! JAM
CH3CCCH2           2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH3CCCH3           2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH3CCH2            2   260.000     4.850     0.000     0.000     1.000 ! JAM
CH3CHCH            2   260.000     4.850     0.000     0.000     1.000 ! JAM
CH3CH2CCH          2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH3CHO             2   436.000     3.970     0.000     0.000     2.000
CH2CHCHO           2   443.200     4.120     0.000     0.000     1.000 ! nmm (LLNL)
CH2CHO             2   436.000     3.970     0.000     0.000     2.000
CH3CO              2   436.000     3.970     0.000     0.000     2.000
CH3O               2   417.000     3.690     1.700     0.000     2.000
CH4O               2   417.000     3.690     1.700     0.000     2.000
CN                 1    75.000     3.856     0.000     0.000     1.000 ! OIS
CNC                1   232.400     3.828     0.000     0.000     1.000 ! OIS
CNN                1   232.400     3.828     0.000     0.000     1.000 ! OIS

H2C4O              2   357.000     5.180     0.000     0.000     1.000 ! JAM
H2CCCCH            2   357.000     5.180     0.000     0.000     1.000 ! JAM
H2CCCCH2           2   357.000     5.180     0.000     0.000     1.000 ! JAM
H2CCCH             2   252.000     4.760     0.000     0.000     1.000 ! JAM
H2CN               1   569.000     3.630     0.000     0.000     1.000 ! os/jm
H2NO               2   116.700     3.492     0.000     0.000     1.000 ! JAM
HC2N2              1   349.000     4.361     0.000     0.000     1.000 ! OIS
HCCHCCH            2   357.000     5.180     0.000     0.000     1.000 ! JAM
HCCO               2   150.000     2.500     0.000     0.000     1.000 ! *
HCNN               2   150.000     2.500     0.000     0.000     1.000 ! *
HCCOH              2   436.000     3.970     0.000     0.000     2.000
HCN                1   569.000     3.630     0.000     0.000     1.000 ! OIS
HCO                2   498.000     3.590     0.000     0.000     0.000
HE                 0    10.200     2.576     0.000     0.000     0.000 ! *
HCNO               2   232.400     3.828     0.000     0.000     1.000 ! JAM
HOCN               2   232.400     3.828     0.000     0.000     1.000 ! JAM
HNCO               2   232.400     3.828     0.000     0.000     1.000 ! OIS
HNNO               2   232.400     3.828     0.000     0.000     1.000 ! *
HNO                2   116.700     3.492     0.000     0.000     1.000 ! *
HNOH               2   116.700     3.492     0.000     0.000     1.000 ! JAM
N                  0    71.400     3.298     0.000     0.000     0.000 ! *
N2                 1    97.530     3.621     0.000     1.760     4.000
N2H2               2    71.400     3.798     0.000     0.000     1.000 ! *
N2H3               2   200.000     3.900     0.000     0.000     1.000 ! *
N2H4               2   205.000     4.230     0.000     4.260     1.500
N2O                1   232.400     3.828     0.000     0.000     1.000 ! *
NCO                1   232.400     3.828     0.000     0.000     1.000 ! OIS
NH                 1    80.000     2.650     0.000     0.000     4.000
NH2                2    80.000     2.650     0.000     2.260     4.000
NH3                2   481.000     2.920     1.470     0.000    10.000
NNH                2    71.400     3.798     0.000     0.000     1.000 ! *
NCNO               2   232.400     3.828     0.000     0.000     1.000 ! OIS
CH3CH2OH           2   362.600     4.530     0.000     0.000     1.500 ! nmm (LLNL)   
CH3CH2O            2   362.600     4.530     0.000     0.000     1.500 ! nmm (LLNL)
AR                 0   136.500     3.330     0.000     0.000     0.000
AR*                 0   136.500     3.330     0.000     0.000     0.000
C                  0    71.400     3.298     0.000     0.000     0.000  !(*)
C2                 1    97.530     3.621     0.000     1.760     4.000
C2O                1   232.400     3.828     0.000     0.000     1.000 ! *
CN2                1   232.400     3.828     0.000     0.000     1.000 ! OIS
C2H                1   209.000     4.100     0.000     0.000     2.500
C2H2               1   209.000     4.100     0.000     0.000     2.500
C2H2OH             2   224.700     4.162     0.000     0.000     1.000  !(*)
CH2OH              2   417.000     3.690     1.700     0.000     2.000
C2H3               2   209.000     4.100     0.000     0.000     1.000  !(*)
C2H4               2   280.800     3.971     0.000     0.000     1.500
C2H5               2   252.300     4.302     0.000     0.000     1.500
C2H6               2   252.300     4.302     0.000     0.000     1.500
C2N                1   232.400     3.828     0.000     0.000     1.000 ! OIS
NCCN               1   349.000     4.361     0.000     0.000     1.000  !(OIS)
C3H2               2   209.000     4.100     0.000     0.000     1.000  !(*)
C3H3               1   252.000     4.760     0.000     0.000     1.000
C3H4               1   252.000     4.760     0.000     0.000     1.000
C3H4P              1   252.000     4.760     0.000     0.000     1.000 ! JAM
C3H6               2   266.800     4.982     0.000     0.000     1.000
C3H7               2   266.800     4.982     0.000     0.000     1.000
C4H6               2   357.000     5.180     0.000     0.000     1.000
I*C3H7             2   266.800     4.982     0.000     0.000     1.000
N*C3H7             2   266.800     4.982     0.000     0.000     1.000
C3H8               2   266.800     4.982     0.000     0.000     1.000
C4H                1   357.000     5.180     0.000     0.000     1.000
C4H2               1   357.000     5.180     0.000     0.000     1.000
C4H2OH             2   224.700     4.162     0.000     0.000     1.000  !(*)
C4H3               1   357.000     5.180     0.000     0.000     1.000
C4H4               1   357.000     5.180     0.000     0.000     1.000
C4H8               2   357.000     5.176     0.000     0.000     1.000
C4H9               2   357.000     5.176     0.000     0.000     1.000
S*C4H9             2   357.000     5.176     0.000     0.000     1.000
C4H9               2   357.000     5.176     0.000     0.000     1.000
I*C4H9             2   357.000     5.176     0.000     0.000     1.000
C5H2               1   357.000     5.180     0.000     0.000     1.000
C5H3               1   357.000     5.180     0.000     0.000     1.000
C6H2               1   357.000     5.180     0.000     0.000     1.000
C6H5               2   412.300     5.349     0.000     0.000     1.000 ! JAM
C6H5(L)            2   412.300     5.349     0.000     0.000     1.000 ! JAM
C6H5O              2   450.000     5.500     0.000     0.000     1.000 ! JAM
C5H5OH             2   450.000     5.500     0.000     0.000     1.000 ! JAM
C6H6               2   412.300     5.349     0.000     0.000     1.000 ! SVE
C6H7               2   412.300     5.349     0.000     0.000     1.000 ! JAM
CH                 1    80.000     2.750     0.000     0.000     0.000

CH2(SING)          1   144.000     3.800     0.000     0.000     0.000
CH2CHCCH           2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CHCCH2          2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CHCH2           2   260.000     4.850     0.000     0.000     1.000 ! JAM
CH2CHCHCH          2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CHCHCH2         2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH2CO              2   436.000     3.970     0.000     0.000     2.000
CH2O               2   498.000     3.590     0.000     0.000     2.000
CH3CC              2   252.000     4.760     0.000     0.000     1.000 ! JAM
CH3CCCH2           2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH3CCCH3           2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH3CCH2            2   260.000     4.850     0.000     0.000     1.000 ! JAM
CH3CHCH            2   260.000     4.850     0.000     0.000     1.000 ! JAM
CH3CH2CCH          2   357.000     5.180     0.000     0.000     1.000 ! JAM
CH3CHO             2   436.000     3.970     0.000     0.000     2.000
CH3CO              2   436.000     3.970     0.000     0.000     2.000
CH3O               2   417.000     3.690     1.700     0.000     2.000
CH4O               2   417.000     3.690     1.700     0.000     2.000
CN                 1    75.000     3.856     0.000     0.000     1.000  !(OIS)
CNC                1   232.400     3.828     0.000     0.000     1.000 ! OIS
CNN                1   232.400     3.828     0.000     0.000     1.000 ! OIS
CL                 0   130.8       3.613     0.000     0.000     1.000  !(singh)
CL-                0   130.8       3.613     0.000     0.000     1.000  !(singh)
E                  0   850.        425.      0.000     0.000     1.000  !(singh)
F                  0    80.000     2.750     0.000     0.000     0.000
F2                 1   125.700     3.301     0.000     1.600     3.800
H2C4O              2   357.000     5.180     0.000     0.000     1.000 ! JAM
H2CCCCH            2   357.000     5.180     0.000     0.000     1.000 ! JAM
H2CCCCH2           2   357.000     5.180     0.000     0.000     1.000 ! JAM
H2CCCH             2   252.000     4.760     0.000     0.000     1.000 ! JAM
H2CN               1   569.000     3.630     0.000     0.000     1.000 ! os/jm
H2NO               2   116.700     3.492     0.000     0.000     1.000 ! JAM
H2S                2   301.000     3.600     0.000     0.000     1.000  !(OIS)
HC2N2              1   349.000     4.361     0.000     0.000     1.000 ! OIS
HCCHCCH            2   357.000     5.180     0.000     0.000     1.000 ! JAM
HCCO               2   150.000     2.500     0.000     0.000     1.000  !(*)
HCCOH              2   436.000     3.970     0.000     0.000     2.000
HCN                1   569.000     3.630     0.000     0.000     1.000  !(OIS)
HCNO               2   232.400     3.828     0.000     0.000     1.000 ! JAM
HCO                2   498.000     3.590     0.000     0.000     0.000
HCO+               1   498.000     3.590     0.000     0.000     0.000
HCL                1   344.7       3.339     0.000     0.000     1.000  !(singh)
HF                 1   330.000     3.148     1.920     2.460     1.000 ! sv/mec
HF0                1   352.000     2.490     1.730     0.000     5.000
HF1                1   352.000     2.490     1.730     0.000     5.000
HF2                1   352.000     2.490     1.730     0.000     5.000
HF3                1   352.000     2.490     1.730     0.000     5.000
HF4                1   352.000     2.490     1.730     0.000     5.000
HF5                1   352.000     2.490     1.730     0.000     5.000
HF6                1   352.000     2.490     1.730     0.000     5.000
HF7                1   352.000     2.490     1.730     0.000     5.000
HF8                1   352.000     2.490     1.730     0.000     5.000
CH2HCO             2   436.000     3.970     0.000     0.000     2.000
HOCN               2   232.400     3.828     0.000     0.000     1.000  !(JAM)
HNCO               2   232.400     3.828     0.000     0.000     1.000  !(OIS)
HNNO               2   232.400     3.828     0.000     0.000     1.000  !(*)
HNO                2   116.700     3.492     0.000     0.000     1.000  !(*)
HNOH               2   116.700     3.492     0.000     0.000     1.000 ! JAM
HSO2               2   252.000     4.290     0.000     0.000     1.000  !(OIS)
HE                 0    10.200     2.576     0.000     0.000     0.000  !(*)
K                  0   850.        4.25      0.000     0.000     1.000  !(singh)
KCL                1  1989.        4.186     0.000     0.000     1.000  !(singh)
KO                 1   383.0       3.812     0.000     0.000     1.000  !(singh)
KOH                2  1213.        4.52      0.000     0.000     1.000  !(singh)
KO2                2  1213.        4.69      0.000     0.000     1.000  !(singh)
KH                 1    93.3       3.542     0.000     0.000     1.000  !(singh)
K+                 0   850.        4.25      0.000     0.000     1.000  !(singh)
N                  0    71.400     3.298     0.000     0.000     0.000  !(*)
N2                 1    97.530     3.621     0.000     1.760     4.000
N2H2               2    71.400     3.798     0.000     0.000     1.000  !(*)
N2H3               2   200.000     3.900     0.000     0.000     1.000  !(*)
N2H4               2   205.000     4.230     0.000     4.260     1.500
N2O                1   232.400     3.828     0.000     0.000     1.000  !(*)
NCN                1   232.400     3.828     0.000     0.000     1.000 ! OIS
NCO                1   232.400     3.828     0.000     0.000     1.000  !(OIS)
NH                 1    80.000     2.650     0.000     0.000     4.000
NH2                2    80.000     2.650     0.000     2.260     4.000
NH3                2   481.000     2.920     1.470     0.000    10.000
NNH                2    71.400     3.798     0.000     0.000     1.000  !(*)
NCNO               2   232.400     3.828     0.000     0.000     1.000 ! OIS
O3                 2   180.000     4.100     0.000     0.000     2.000
S                  0   847.000     3.839     0.000     0.000     0.000  !(OIS)
S2                 1   847.000     3.900     0.000     0.000     1.000  !(OIS)
SH                 1   847.000     3.900     0.000     0.000     1.000  !(OIS)
SO                 1   301.000     3.993     0.000     0.000     1.000  !(OIS)
SO2                2   252.000     4.290     0.000     0.000     1.000  !(OIS)
SO3                2   378.400     4.175     0.000     0.000     1.000  !(OIS)

CH3NO              2   436.000     3.970     0.000     0.000     2.000 ! = CH3CO
CH2NO              2   232.400     3.828     0.000     0.000     1.000 !=HCNO
C2H5NO             1   252.000      4.760           0.000   0.000     1.000 !CH3CH2CHO
CH3CHNO            1   252.000      4.760           0.000   0.000     1.000	!CH3CH2CHO
C2H3NO             2   357.000      5.176           0.000   0.000     1.000	!C2H3CHO
CHCHNO             1   357.000      5.180           0.000   0.000     1.000	!CH2CHCO
CH3CNO             2   357.000      5.176           0.000   0.000     1.000	!C2H3CHO
CH2CHNO             2   357.000      5.176           0.000   0.000     1.000	!C2H3CHO   !
!
CH3NO2             2   232.400     3.828     0.000     0.000     1.000  !refered to NCNO
CH3ONO             2   232.400     3.828     0.000     0.000     1.000  !refered to NCNO
CH2NO2             2   232.400     3.828     0.000     0.000     1.000  !refered to NCNO
C2H5NO2            2   503.0722    5.340     1.67      8.88	 1	! refered to C4H9OH
CH2CH2NO2          2   503.0722    5.340     1.67      8.88	 1	! refered to C4H9OH
CH3CHNO2           2   503.0722    5.340     1.67      8.88	 1	! refered to C4H9OH
CH3ONO             2   232.400     3.828     0.000     0.000     1.000  !refered to NCNO
CH3ONO2            2   459.5        5.036        1.7     0.0       1.0   !wjp
CH3CH2ONO          2   503.0722524  5.339941638	 1.67	8.88	  1	! refered to C4H9OH                                                       
CH2CH2NO2          2   503.0722524  5.339941638	 1.67	8.88	  1	! refered to C4H9OH                                                           
CH3CHNO2           2   503.0722524  5.339941638	 1.67	8.88	  1	! refered to C4H9OH                                                        
CH3CH2ONO2         2   496.000      5.200           0.000   0.000     1.000 ! wjp sc4h9o2h          					                        !
CH3NH2             2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH3NH              2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH2NH2             2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH2NH              2   417.000     3.690     1.700     0.000     2.000 ! = CH2OH
H2CN               1   569.000     3.630     0.000     0.000     1.000 ! os/jm
!
!CH3CH2NH2 CH2CH2NH2 CH3CHNH2 CH3CH2NH CH2CHNH2 CH3CHNH CH2CHNH CH2CNH2 CH3CNH CH3CHN CHCHNH2 
HNC                1   569.000     3.630     0.000     0.000     1.000 ! = HCN
HCNH               1   569.000     3.630     0.000     0.000     1.000 ! = H2CN
CH3NO              2   436.000     3.970     0.000     0.000     2.000 ! = CH3CO
CH3NH2             2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH3NH              2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH2NH2             2   481.800     3.626     0.000     0.000     1.000 ! = CH3OH
CH2NH              2   417.000     3.690     1.700     0.000     2.000 ! = CH2OH
CH3CH2NH2          2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH3NHCH3           2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH2CH2NH2          2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH3NCH3            2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH3NHCH2           2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH3CHNH2           2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH3CH2NH           2   436.000     3.970     0.000     0.000     2.000 ! = CH3CHO
CH2CHNH2           2   303.400     4.810     0.000     0.000     1.000 ! = c3h7
CH3CHNH            2   303.400     4.810     0.000     0.000     1.000 ! = c3h7
CH3NCH2            2   303.400     4.810     0.000     0.000     1.000 ! = c3h7
CH2CHNH            2   307.800     4.140     0.000     0.000     1.000 ! = c3h6
CHCHNH2            2   307.800     4.140     0.000     0.000     1.000 ! = c3h6 
CH2NCH2            2   307.800     4.140     0.000     0.000     1.000 ! = c3h6
CH3CHN             2   307.800     4.140     0.000     0.000     1.000 ! = c3h6
CH3NCH             2   307.800     4.140     0.000     0.000     1.000 ! = c3h6
CH3CNH             2   307.800     4.140     0.000     0.000     1.000 ! = c3h6
CH2CNH2            2   307.800     4.140     0.000     0.000     1.000 ! = c3h6
CH2CNH             2   260.000     4.850     0.000     0.000     1.000 ! = c3h5
CH2CHN             2   260.000     4.850     0.000     0.000     1.000 ! = c3h5
CH2CHN(S)          2   260.000     4.850     0.000     0.000     1.000 ! = c3h5
c-C2H3N            2   260.000     4.850     0.000     0.000     1.000 ! = c3h5
CHCNH2             2   260.000     4.850     0.000     0.000     1.000 ! = c3h5
CHCNH              1   252.000     4.760     0.000     0.000     1.000 ! = c3h4
H2NCHO             2   307.800     4.140     0.000     0.000     1.000 ! = c3h6 
H2NCO              2   307.800     4.140     0.000     0.000     1.000 ! = c3h6 
CH3NC              2   422.220     5.329     3.500     0.000     1.000 ! = ch3cn
!
!CH3CN CHCNH2 CH2CNH CH2CHN CH2CHN(S) c-C2H3N CH2CN CHCNH H2NCHO H2NCO 
!
CH3CN              2   422.220     5.329     3.500     0.000     1.000 ! CJP
CH2CN              2   422.220     5.329     3.500     0.000     1.000 ! CJP
!CH3NHCH3 CH3NHCH2 CH3NCH3 CH3NCH2 CH2NCH2 CH3NCH 
!
"""
