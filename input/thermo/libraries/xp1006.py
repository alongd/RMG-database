#!/usr/bin/env python
# encoding: utf-8

name = "xp1006"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.06333e-12,1.30802e-15,-5.21436e-19,6.38303e-23,-745,4.3663], Tmin=(100,'K'), Tmax=(4950.76,'K')),
            NASAPolynomial(coeffs=[2.77499,-0.000212693,6.15681e-08,-7.90365e-12,3.79566e-16,-1028.91,2.58803], Tmin=(4950.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Ne",
    molecule = 
"""
1 Ne u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Thermo library: primaryThermoLibrary""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "nC5H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.299552,0.0594963,-3.41764e-05,9.47896e-09,-9.73675e-13,-19896,27.5742], Tmin=(200,'K'), Tmax=(1393,'K')),
            NASAPolynomial(coeffs=[15.8289,0.0259345,-8.83016e-06,1.36655e-09,-7.91029e-14,-25939.7,-60.5558], Tmin=(1393,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53764,-0.00122827,5.36759e-06,-4.93128e-09,1.45955e-12,-1037.99,4.6718], Tmin=(100,'K'), Tmax=(1087.71,'K')),
            NASAPolynomial(coeffs=[3.16427,0.00169454,-8.00335e-07,1.5903e-10,-1.14891e-14,-1048.45,6.08303], Tmin=(1087.71,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55718,-0.000890582,2.98556e-06,-2.08691e-09,4.6596e-13,9952.4,4.55251], Tmin=(100,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[2.93796,0.00175427,-7.77019e-07,1.42655e-10,-9.57864e-15,10039.1,7.44023], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61263,-0.00100893,2.49898e-06,-1.43375e-09,2.58634e-13,-1051.1,2.6527], Tmin=(100,'K'), Tmax=(1817.04,'K')),
            NASAPolynomial(coeffs=[2.97592,0.00164138,-7.19709e-07,1.25375e-10,-7.91507e-15,-1025.85,5.53745], Tmin=(1817.04,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.06333e-12,1.30802e-15,-5.21436e-19,6.38303e-23,25472.7,-0.459566], Tmin=(100,'K'), Tmax=(4950.76,'K')),
            NASAPolynomial(coeffs=[2.77499,-0.000212693,6.15681e-08,-7.90365e-12,3.79566e-16,25188.8,-2.23784], Tmin=(4950.76,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4858,0.00133395,-4.70037e-06,5.64371e-09,-2.06314e-12,3411.96,1.99787], Tmin=(100,'K'), Tmax=(1005.25,'K')),
            NASAPolynomial(coeffs=[2.88225,0.0010387,-2.35658e-07,1.40243e-11,6.3447e-16,3669.56,5.59057], Tmin=(1005.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42254,0.00028665,-4.14671e-07,4.27548e-10,-9.38119e-14,-1029.78,-3.86365], Tmin=(100,'K'), Tmax=(1962.85,'K')),
            NASAPolynomial(coeffs=[2.74219,0.00057954,1.97202e-07,-6.41094e-11,4.96003e-15,-552.037,0.414101], Tmin=(1962.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99882,-0.000554832,2.76775e-06,-1.55665e-09,3.02331e-13,-30274.6,-0.0308948], Tmin=(100,'K'), Tmax=(1281.44,'K')),
            NASAPolynomial(coeffs=[3.1956,0.0019524,-1.67117e-07,-2.97941e-11,4.45141e-15,-30068.7,4.04334], Tmin=(1281.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02957,-0.00263999,1.52235e-05,-1.71678e-08,6.26771e-12,322.677,4.84424], Tmin=(100,'K'), Tmax=(923.9,'K')),
            NASAPolynomial(coeffs=[4.1513,0.00191152,-4.11307e-07,6.35036e-11,-4.86451e-15,83.4339,3.09359], Tmin=(923.9,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72867,0.00413383,5.67477e-06,-1.01863e-08,4.28599e-12,-17696.4,5.35913], Tmin=(100,'K'), Tmax=(923.28,'K')),
            NASAPolynomial(coeffs=[4.95153,0.00354227,-1.01039e-06,1.61939e-10,-1.10207e-14,-18122.8,-1.52919], Tmin=(923.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "HONO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58324,0.00677956,2.80768e-06,-7.92847e-09,3.26002e-12,-10523,7.64225], Tmin=(100,'K'), Tmax=(1030.67,'K')),
            NASAPolynomial(coeffs=[5.61861,0.00445477,-1.92172e-06,3.7824e-10,-2.77202e-14,-11238.6,-3.67508], Tmin=(1030.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "NO2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95018,-0.00110889,1.34101e-05,-1.53107e-08,5.31016e-12,2973.3,6.19456], Tmin=(100,'K'), Tmax=(1003.62,'K')),
            NASAPolynomial(coeffs=[4.42985,0.00284581,-1.26849e-06,2.63845e-10,-2.02208e-14,2581.56,2.40676], Tmin=(1003.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "HNO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98439,-0.00290724,2.4218e-05,-2.60191e-08,8.72133e-12,-6458.17,6.63658], Tmin=(100,'K'), Tmax=(1007.87,'K')),
            NASAPolynomial(coeffs=[3.92435,0.00624036,-2.6559e-06,5.27586e-10,-3.90798e-14,-6898.57,4.68184], Tmin=(1007.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05937,-0.00173848,9.14985e-06,-8.01136e-09,2.25739e-12,3843.78,3.32449], Tmin=(100,'K'), Tmax=(1112.1,'K')),
            NASAPolynomial(coeffs=[3.05136,0.00411707,-1.75587e-06,3.29304e-10,-2.29175e-14,3930.08,7.67468], Tmin=(1112.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5971,-0.00102424,2.83336e-06,-1.75825e-09,3.42587e-13,-14343.2,3.45822], Tmin=(100,'K'), Tmax=(1669.93,'K')),
            NASAPolynomial(coeffs=[2.92796,0.00181931,-8.35309e-07,1.51269e-10,-9.88872e-15,-14292.7,6.51157], Tmin=(1669.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96043,0.000592934,8.78578e-06,-9.88034e-09,3.63236e-12,16421.9,0.339864], Tmin=(100,'K'), Tmax=(697.67,'K')),
            NASAPolynomial(coeffs=[3.09511,0.0055543,-1.88159e-06,3.13335e-10,-2.05195e-14,16542.6,4.20298], Tmin=(697.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CH3CN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 N u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58343,0.00602816,1.4705e-05,-1.93939e-08,6.81846e-12,7381.15,6.47483], Tmin=(100,'K'), Tmax=(1014.53,'K')),
            NASAPolynomial(coeffs=[4.3592,0.0109113,-4.25705e-06,7.82398e-10,-5.47678e-14,6815.04,0.70673], Tmin=(1014.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "ONONO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {4,S} {5,D}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {6,D}
4 O u0 p3 c-1 {1,S}
5 O u0 p2 c0 {1,D}
6 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63108,0.0321363,-3.85878e-05,2.38435e-08,-5.95703e-12,3424.36,15.4148], Tmin=(100,'K'), Tmax=(965.52,'K')),
            NASAPolynomial(coeffs=[7.73489,0.0109919,-5.73863e-06,1.16194e-09,-8.41366e-14,2438.79,-9.02911], Tmin=(965.52,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "N2O4",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,D} {4,S}
2 N u0 p0 c+1 {1,S} {5,S} {6,D}
3 O u0 p2 c0 {1,D}
4 O u0 p3 c-1 {1,S}
5 O u0 p3 c-1 {2,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60498,0.0316418,-3.50812e-05,1.94247e-08,-4.30588e-12,-725.491,14.3529], Tmin=(100,'K'), Tmax=(1086.82,'K')),
            NASAPolynomial(coeffs=[8.508,0.00991579,-5.09548e-06,1.03099e-09,-7.47841e-14,-2008.59,-14.6172], Tmin=(1086.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "N2O3_A",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 N u0 p1 c0 {1,S} {5,D}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68866,0.0319245,-5.47804e-05,4.87699e-08,-1.70332e-11,8190.41,13.4214], Tmin=(100,'K'), Tmax=(797.73,'K')),
            NASAPolynomial(coeffs=[6.29753,0.00974444,-5.39453e-06,1.0796e-09,-7.6115e-14,7744.58,-2.35928], Tmin=(797.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9561,-0.00306272,3.0687e-05,-3.34105e-08,1.13921e-11,1192.54,4.69447], Tmin=(100,'K'), Tmax=(985.48,'K')),
            NASAPolynomial(coeffs=[3.74504,0.00852607,-3.28779e-06,6.23936e-10,-4.53253e-14,713.002,3.06553], Tmin=(985.48,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12928,-0.00408399,2.03229e-05,-1.83523e-08,5.37972e-12,-14429.5,3.22419], Tmin=(100,'K'), Tmax=(1070.44,'K')),
            NASAPolynomial(coeffs=[2.21174,0.00794264,-3.34192e-06,6.28469e-10,-4.40429e-14,-14297.5,11.3048], Tmin=(1070.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84007,0.00138239,1.91668e-05,-2.0157e-08,6.39109e-12,-25608.3,5.90977], Tmin=(100,'K'), Tmax=(1035.75,'K')),
            NASAPolynomial(coeffs=[2.79183,0.0115828,-4.51553e-06,8.2121e-10,-5.67066e-14,-25721.2,9.41069], Tmin=(1035.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2779,0.00275782,7.12789e-06,-1.07855e-08,4.14229e-12,-48475.6,5.97856], Tmin=(100,'K'), Tmax=(988.18,'K')),
            NASAPolynomial(coeffs=[4.55071,0.00290729,-1.14643e-06,2.25798e-10,-1.69527e-14,-48986,-1.45661], Tmin=(988.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: BurkeH2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C2H5",
    molecule = 
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68745,0.0030691,2.55866e-05,-2.94067e-08,9.94036e-12,13115.4,6.96691], Tmin=(100,'K'), Tmax=(1006.88,'K')),
            NASAPolynomial(coeffs=[3.53788,0.013731,-5.29558e-06,9.71466e-10,-6.80276e-14,12635.1,5.15526], Tmin=(1006.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "HOCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76241,-0.000943943,3.38782e-05,-4.04988e-08,1.43988e-11,-46821.2,7.63273], Tmin=(100,'K'), Tmax=(993.73,'K')),
            NASAPolynomial(coeffs=[5.64497,0.00755187,-3.20854e-06,6.58926e-10,-5.05061e-14,-47989,-5.43087], Tmin=(993.73,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "CH3O3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69194,0.0271135,-2.49832e-05,1.1931e-08,-2.28596e-12,-21673.7,14.0558], Tmin=(100,'K'), Tmax=(1253.51,'K')),
            NASAPolynomial(coeffs=[8.21381,0.00949295,-3.89778e-06,7.16891e-10,-4.94195e-14,-23058.1,-13.8317], Tmin=(1253.51,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CH3O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58601,0.00615349,1.33269e-05,-1.76582e-08,6.13211e-12,248.234,9.74096], Tmin=(100,'K'), Tmax=(1031.35,'K')),
            NASAPolynomial(coeffs=[4.35022,0.0107183,-4.26215e-06,7.89578e-10,-5.53846e-14,-309.81,4.08928], Tmin=(1031.35,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CH4O2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42342,0.0100732,6.61594e-06,-1.1963e-08,4.37121e-12,-16948.1,8.99053], Tmin=(100,'K'), Tmax=(1042.7,'K')),
            NASAPolynomial(coeffs=[4.64752,0.0115696,-4.44495e-06,8.04481e-10,-5.54882e-14,-17540,1.41959], Tmin=(1042.7,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97472,-0.00475844,4.16784e-05,-4.51393e-08,1.54225e-11,4915.41,3.62431], Tmin=(100,'K'), Tmax=(979.36,'K')),
            NASAPolynomial(coeffs=[3.55661,0.0110627,-4.17019e-06,7.85587e-10,-5.70061e-14,4320.46,2.17719], Tmin=(979.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "S18",
    molecule = 
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88897,0.018523,1.04553e-05,-2.35214e-08,9.42836e-12,-4266.36,15.0608], Tmin=(100,'K'), Tmax=(1009.28,'K')),
            NASAPolynomial(coeffs=[7.15138,0.0156283,-6.04681e-06,1.12074e-09,-7.93659e-14,-5839.72,-9.0743], Tmin=(1009.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C2H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57992,0.00518983,2.26898e-05,-2.73743e-08,9.2848e-12,-21369.7,8.96972], Tmin=(100,'K'), Tmax=(1028.81,'K')),
            NASAPolynomial(coeffs=[4.08564,0.0139061,-5.5937e-06,1.04609e-09,-7.38739e-14,-22039.1,3.76802], Tmin=(1028.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C2H5O",
    molecule = 
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.13417,0.0154299,5.47054e-06,-1.32607e-08,4.93293e-12,-3182.88,11.0478], Tmin=(100,'K'), Tmax=(1075.82,'K')),
            NASAPolynomial(coeffs=[5.34725,0.0154988,-6.19437e-06,1.13688e-09,-7.87695e-14,-4139.21,-2.0224], Tmin=(1075.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63679,0.00450831,1.80299e-05,-2.25976e-08,7.8865e-12,-2544.95,9.39479], Tmin=(100,'K'), Tmax=(1011.56,'K')),
            NASAPolynomial(coeffs=[4.39396,0.0104824,-4.12731e-06,7.69406e-10,-5.45067e-14,-3156.98,3.4652], Tmin=(1011.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C2H3O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51489,0.00449266,2.7071e-05,-3.7273e-08,1.43014e-11,808.795,8.86074], Tmin=(100,'K'), Tmax=(956.36,'K')),
            NASAPolynomial(coeffs=[6.48037,0.00773055,-2.53963e-06,4.6928e-10,-3.50521e-14,-473.709,-9.05334], Tmin=(956.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C3H5O_E",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u1 p0 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84503,0.0188974,1.21542e-05,-2.63169e-08,1.05759e-11,-5215.39,14.5336], Tmin=(100,'K'), Tmax=(1004.36,'K')),
            NASAPolynomial(coeffs=[7.57164,0.0155753,-6.03677e-06,1.12556e-09,-8.02212e-14,-6946.72,-12.1826], Tmin=(1004.36,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "S88",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u1 p2 c0 {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34419,0.0284803,2.09197e-06,-2.15819e-08,9.66852e-12,-17717,17.6523], Tmin=(100,'K'), Tmax=(1024.44,'K')),
            NASAPolynomial(coeffs=[10.0095,0.0165278,-6.72996e-06,1.28902e-09,-9.31498e-14,-20230.9,-24.1178], Tmin=(1024.44,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "S7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.84097,0.0464944,-4.03241e-05,1.85914e-08,-3.52551e-12,-18394.8,21.0358], Tmin=(100,'K'), Tmax=(1242.86,'K')),
            NASAPolynomial(coeffs=[9.98393,0.020287,-8.69443e-06,1.62515e-09,-1.12755e-13,-20418.9,-20.0196], Tmin=(1242.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C3H4O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94493,0.017528,8.67159e-06,-2.09292e-08,8.38191e-12,-9500.47,10.6675], Tmin=(100,'K'), Tmax=(1025.08,'K')),
            NASAPolynomial(coeffs=[7.2666,0.0139912,-5.65425e-06,1.07053e-09,-7.65801e-14,-11086.7,-13.7044], Tmin=(1025.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C3H6O_A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90578,0.0240644,-7.06358e-06,-9.81818e-10,5.5582e-13,-24535.9,13.5806], Tmin=(100,'K'), Tmax=(1712.49,'K')),
            NASAPolynomial(coeffs=[7.69114,0.0189242,-7.84931e-06,1.38272e-09,-8.99052e-14,-27060.2,-14.665], Tmin=(1712.49,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C3H5O_A",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91313,0.0225012,-8.59335e-06,4.80387e-10,2.48724e-13,-5274.24,14.655], Tmin=(100,'K'), Tmax=(1673.19,'K')),
            NASAPolynomial(coeffs=[7.4632,0.015851,-6.42131e-06,1.12497e-09,-7.3204e-14,-7388.61,-11.4068], Tmin=(1673.19,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "NC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02815,0.0147024,2.40506e-05,-3.66733e-08,1.38609e-11,10512.1,12.4699], Tmin=(100,'K'), Tmax=(984.47,'K')),
            NASAPolynomial(coeffs=[6.16547,0.0184494,-6.79026e-06,1.23048e-09,-8.6386e-14,9095.05,-6.67625], Tmin=(984.47,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31912,0.00817957,3.34737e-05,-4.36194e-08,1.58214e-11,749.325,9.54025], Tmin=(100,'K'), Tmax=(983.75,'K')),
            NASAPolynomial(coeffs=[5.36755,0.0170743,-6.35108e-06,1.1662e-09,-8.27621e-14,-487.136,-4.54465], Tmin=(983.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "S37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15077,0.0341093,-6.28775e-06,-1.16905e-08,5.70826e-12,-6992.04,19.9651], Tmin=(100,'K'), Tmax=(1072.55,'K')),
            NASAPolynomial(coeffs=[8.78442,0.0227415,-9.09063e-06,1.67579e-09,-1.16717e-13,-9184.16,-16.0886], Tmin=(1072.55,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "S54",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73075,0.0457841,-3.51689e-05,1.42448e-08,-2.36091e-12,1161.01,22.4746], Tmin=(100,'K'), Tmax=(1415.64,'K')),
            NASAPolynomial(coeffs=[10.8294,0.0200752,-7.92782e-06,1.41611e-09,-9.53844e-14,-1415.06,-24.5835], Tmin=(1415.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C3H5O_B",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74067,0.0217951,4.87759e-06,-1.91825e-08,8.13707e-12,10130.3,14.3776], Tmin=(100,'K'), Tmax=(1016.98,'K')),
            NASAPolynomial(coeffs=[7.73995,0.0156908,-6.11761e-06,1.13522e-09,-8.0312e-14,8412.28,-13.2725], Tmin=(1016.98,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C3H5O_D",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u1 p0 c0 {4,S} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59643,0.0244142,9.36948e-07,-1.83877e-08,8.69512e-12,9280.22,14.7231], Tmin=(100,'K'), Tmax=(988.88,'K')),
            NASAPolynomial(coeffs=[9.07407,0.0132332,-4.8876e-06,8.99482e-10,-6.42037e-14,7264.66,-20.1688], Tmin=(988.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C3H6O_B",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  O u0 p2 c0 {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43519,0.0321429,-2.11365e-05,7.43424e-09,-1.09823e-12,-20020.5,13.0756], Tmin=(100,'K'), Tmax=(1529.29,'K')),
            NASAPolynomial(coeffs=[8.00323,0.0175792,-6.85175e-06,1.20709e-09,-8.02559e-14,-21723.5,-16.1524], Tmin=(1529.29,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C3H7O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49,0.0272741,1.66495e-06,-1.66157e-08,7.01496e-12,-6000.76,15.8164], Tmin=(100,'K'), Tmax=(1050.43,'K')),
            NASAPolynomial(coeffs=[7.46139,0.0213308,-8.39409e-06,1.5387e-09,-1.07024e-13,-7761.71,-11.8229], Tmin=(1050.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "N2N0",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25388,0.0316763,2.89995e-06,-1.98049e-08,8.20504e-12,7652.64,17.2725], Tmin=(100,'K'), Tmax=(1050.57,'K')),
            NASAPolynomial(coeffs=[7.59591,0.0260842,-1.01719e-05,1.85189e-09,-1.28169e-13,5716.37,-12.6366], Tmin=(1050.57,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "S90",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.16958,0.0522745,-3.32955e-05,1.03031e-08,-1.20771e-12,-10718.1,20.3542], Tmin=(200,'K'), Tmax=(1663,'K')),
            NASAPolynomial(coeffs=[15.8558,0.0204564,-6.9323e-06,1.07505e-09,-6.24729e-14,-15165.1,-52.7319], Tmin=(1663,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C4H7O_B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60619,0.0558563,-4.35596e-05,1.70589e-08,-2.65635e-12,4850.9,34.7113], Tmin=(200,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[15.3138,0.0143427,-4.81626e-06,7.39575e-10,-4.26141e-14,-729.343,-55.2938], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C4H9O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.499965,0.0537157,-3.44427e-05,1.08146e-08,-1.296e-12,-9116.44,30.9183], Tmin=(200,'K'), Tmax=(1403,'K')),
            NASAPolynomial(coeffs=[14.9316,0.0195927,-6.66958e-06,1.03223e-09,-5.97584e-14,-14617.9,-52.5562], Tmin=(1403,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "S75",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38642,0.0494794,-3.11731e-05,9.34789e-09,-9.92349e-13,-4340.49,16.5183], Tmin=(200,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[17.5958,0.0178823,-5.84602e-06,8.80852e-10,-5.00663e-14,-9316.09,-60.1626], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "S62",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.16451,0.0572956,-3.91319e-05,1.28721e-08,-1.58263e-12,-2587.87,26.7435], Tmin=(200,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[18.5836,0.0174941,-5.81083e-06,8.85582e-10,-5.07537e-14,-8582.6,-66.8842], Tmin=(1400,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C4H7O_A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40256,0.0367294,-1.97317e-05,5.07323e-09,-4.99655e-13,-6150.07,19.3993], Tmin=(200,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[12.4694,0.0171022,-5.92157e-06,9.26817e-10,-5.40731e-14,-10137.8,-36.2186], Tmin=(1380,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C3H5O_C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54014,0.0439486,-2.97002e-05,1.05495e-08,-1.58599e-12,-9507.97,19.9707], Tmin=(200,'K'), Tmax=(1383,'K')),
            NASAPolynomial(coeffs=[14.2099,0.0157866,-5.50529e-06,8.65871e-10,-5.06913e-14,-14128.5,-48.7133], Tmin=(1383,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C5H11_B",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.098319,0.0558654,-3.28856e-05,9.58367e-09,-1.08641e-12,4820.66,28.6921], Tmin=(200,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[15.1918,0.0240339,-8.19718e-06,1.27003e-09,-7.35728e-14,-802.149,-53.6479], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C5H11_A",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {4,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.817689,0.0492654,-2.13786e-05,1.85532e-09,7.06259e-13,3262.21,26.5876], Tmin=(200,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[14.7177,0.0241668,-8.18648e-06,1.26272e-09,-7.29268e-14,-2260.28,-50.6071], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C5H11_C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.817689,0.0492654,-2.13786e-05,1.85532e-09,7.06259e-13,3262.21,25.8981], Tmin=(200,'K'), Tmax=(1395,'K')),
            NASAPolynomial(coeffs=[14.7177,0.0241668,-8.18648e-06,1.26272e-09,-7.29268e-14,-2260.28,-51.2966], Tmin=(1395,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "S26",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.165024,0.0530727,-3.10862e-05,8.92413e-09,-9.8162e-13,-4593.76,28.057], Tmin=(200,'K'), Tmax=(1390,'K')),
            NASAPolynomial(coeffs=[14.3625,0.0226076,-7.70501e-06,1.1933e-09,-6.91126e-14,-10019.3,-51.2512], Tmin=(1390,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C5H10_A",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.590529,0.0485275,-2.43232e-05,4.86096e-09,-1.13099e-13,-5997.78,24.1816], Tmin=(200,'K'), Tmax=(1385,'K')),
            NASAPolynomial(coeffs=[13.9426,0.0228735,-7.778e-06,1.20285e-09,-6.95972e-14,-11216.6,-49.538], Tmin=(1385,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "S20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {12,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61443,0.0584449,-3.26028e-05,7.76525e-09,-4.4874e-13,-12021,22.3621], Tmin=(200,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[18.7118,0.0236055,-8.05611e-06,1.24901e-09,-7.23989e-14,-18413.3,-71.1769], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "S32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.80798,0.0595687,-3.62937e-05,1.05786e-08,-1.11087e-12,-14129.5,20.1085], Tmin=(200,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[18.5178,0.023356,-7.87897e-06,1.21191e-09,-6.98573e-14,-20148.9,-70.5224], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "S77",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.80798,0.0595687,-3.62937e-05,1.05786e-08,-1.11087e-12,-14129.5,18.7296], Tmin=(200,'K'), Tmax=(1407,'K')),
            NASAPolynomial(coeffs=[18.5178,0.023356,-7.87897e-06,1.21191e-09,-6.98573e-14,-20148.9,-71.9014], Tmin=(1407,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "S64",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {4,S} {18,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4785,0.0656223,-4.24002e-05,1.39456e-08,-1.86036e-12,-13306.5,25.7185], Tmin=(200,'K'), Tmax=(1392,'K')),
            NASAPolynomial(coeffs=[19.9509,0.0248182,-8.50415e-06,1.32191e-09,-7.67597e-14,-19978.3,-74.3587], Tmin=(1392,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "S42",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {1,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95945,0.0673013,-4.74262e-05,1.76453e-08,-2.71599e-12,-15510.2,21.5326], Tmin=(200,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[20.1379,0.0243049,-8.24745e-06,1.27345e-09,-7.35954e-14,-21777.8,-75.9194], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "S34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95945,0.0673013,-4.74262e-05,1.76453e-08,-2.71599e-12,-15510.2,20.1536], Tmin=(200,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[20.1379,0.0243049,-8.24745e-06,1.27345e-09,-7.35954e-14,-21777.8,-77.2984], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "S96",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {2,S} {17,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21642,0.0596427,-3.30151e-05,7.82802e-09,-4.53627e-13,-6890.38,25.3166], Tmin=(200,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[19.4584,0.0246032,-8.38535e-06,1.29884e-09,-7.52367e-14,-13354.9,-69.0616], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "S79",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {4,S} {17,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21642,0.0596427,-3.30151e-05,7.82802e-09,-4.53627e-13,-6890.38,25.3166], Tmin=(200,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[19.4584,0.0246032,-8.38535e-06,1.29884e-09,-7.52367e-14,-13354.9,-69.0616], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "S44",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {4,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69411,0.0613273,-3.77803e-05,1.1181e-08,-1.20044e-12,-9095,21.1389], Tmin=(200,'K'), Tmax=(1410,'K')),
            NASAPolynomial(coeffs=[19.8844,0.0237471,-7.98274e-06,1.22497e-09,-7.04947e-14,-15241.3,-71.9594], Tmin=(1410,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "S12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {3,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.46239,0.0700774,-5.18935e-05,2.03024e-08,-3.27212e-12,-7458.96,25.6256], Tmin=(200,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[20.5595,0.0235924,-8.01737e-06,1.23919e-09,-7.16674e-14,-13905.9,-76.2752], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "S24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {3,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.46239,0.0700774,-5.18935e-05,2.03024e-08,-3.27212e-12,-7458.96,24.9361], Tmin=(200,'K'), Tmax=(1401,'K')),
            NASAPolynomial(coeffs=[20.5595,0.0235924,-8.01737e-06,1.23919e-09,-7.16674e-14,-13905.9,-76.9647], Tmin=(1401,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "S63",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.99511,0.0848028,-6.84821e-05,2.79647e-08,-4.48602e-12,-27934.7,63.6835], Tmin=(200,'K'), Tmax=(1470,'K')),
            NASAPolynomial(coeffs=[15.6838,0.0228597,-7.36869e-06,1.09856e-09,-6.19426e-14,-35236.5,-60.6987], Tmin=(1470,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "S60",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.91381,0.0865695,-7.51445e-05,3.29307e-08,-5.77631e-12,-20233.7,56.6267], Tmin=(200,'K'), Tmax=(1396,'K')),
            NASAPolynomial(coeffs=[15.8873,0.0248574,-1.03963e-05,1.95193e-09,-1.29465e-13,-27222.4,-62.6943], Tmin=(1396,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "S82",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92124,0.0767602,-5.10112e-05,1.59643e-08,-1.8298e-12,-25548.7,22.7306], Tmin=(200,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[27.1106,0.0234082,-8.1172e-06,1.27231e-09,-7.43222e-14,-34140.6,-108.093], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "S69",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92124,0.0767602,-5.10112e-05,1.59643e-08,-1.8298e-12,-25548.7,22.7306], Tmin=(200,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[27.1106,0.0234082,-8.1172e-06,1.27231e-09,-7.43222e-14,-34140.6,-108.093], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "S15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94959,0.0794697,-6.123e-05,2.45361e-08,-3.99244e-12,-27626.3,21.0066], Tmin=(200,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[25.1554,0.0242477,-8.22109e-06,1.26886e-09,-7.33158e-14,-34952.2,-96.9776], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "S36",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.92124,0.0767602,-5.10112e-05,1.59643e-08,-1.8298e-12,-25548.7,22.7306], Tmin=(200,'K'), Tmax=(1394,'K')),
            NASAPolynomial(coeffs=[27.1106,0.0234082,-8.1172e-06,1.27231e-09,-7.43222e-14,-34140.6,-108.093], Tmin=(1394,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "S13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,D} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00527,0.0657859,-4.36349e-05,1.39803e-08,-1.68002e-12,-42409.5,19.0078], Tmin=(200,'K'), Tmax=(1405,'K')),
            NASAPolynomial(coeffs=[22.5902,0.0217812,-7.38064e-06,1.13911e-09,-6.58296e-14,-49267.9,-86.5971], Tmin=(1405,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "S17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {4,S} {18,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {7,S} {19,S}
9  O u0 p2 c0 {6,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42923,0.0733174,-5.05533e-05,1.77709e-08,-2.53421e-12,-18921.3,22.6144], Tmin=(200,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[24.6778,0.0247897,-8.53168e-06,1.33018e-09,-7.7405e-14,-26400.9,-91.8794], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "S91",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
5  C u1 p0 c0 {3,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {19,S}
9  O u0 p2 c0 {6,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.50133,0.0793141,-5.51609e-05,1.83964e-08,-2.32881e-12,-17513,26.433], Tmin=(200,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[27.5716,0.0226282,-7.85652e-06,1.23252e-09,-7.20427e-14,-26270.3,-108.648], Tmin=(1397,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "S72",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
5  C u1 p0 c0 {2,S} {4,S} {18,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {19,S}
9  O u0 p2 c0 {6,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42923,0.0733174,-5.05533e-05,1.77709e-08,-2.53421e-12,-18921.3,22.6144], Tmin=(200,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[24.6778,0.0247897,-8.53168e-06,1.33018e-09,-7.7405e-14,-26400.9,-91.8794], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "S39",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {4,S} {17,D}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70378,0.062214,-4.08904e-05,1.31907e-08,-1.60742e-12,-46241.1,15.8017], Tmin=(200,'K'), Tmax=(1417,'K')),
            NASAPolynomial(coeffs=[21.3558,0.0220059,-7.28286e-06,1.10611e-09,-6.32057e-14,-52344.6,-79.1469], Tmin=(1417,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "S92",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {2,S} {17,D}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06394,0.0546275,-2.50666e-05,2.02313e-09,1.0015e-12,-44162.5,15.9655], Tmin=(200,'K'), Tmax=(1431,'K')),
            NASAPolynomial(coeffs=[21.4963,0.0220659,-7.3549e-06,1.12359e-09,-6.45028e-14,-50847.1,-80.243], Tmin=(1431,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "S51",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {4,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.63459,0.0837429,-6.46449e-05,2.45435e-08,-3.63638e-12,-30244.4,38.101], Tmin=(200,'K'), Tmax=(1422,'K')),
            NASAPolynomial(coeffs=[24.0742,0.021005,-7.12966e-06,1.10196e-09,-6.37577e-14,-38690.6,-98.6615], Tmin=(1422,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "S4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {2,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.95212,0.0890845,-7.32339e-05,2.98425e-08,-4.76173e-12,-30028.1,44.5335], Tmin=(200,'K'), Tmax=(1436,'K')),
            NASAPolynomial(coeffs=[23.731,0.0206752,-6.88444e-06,1.05045e-09,-6.02362e-14,-38436.3,-96.1946], Tmin=(1436,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "S94",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,D} {16,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92095,0.0494039,-1.996e-05,-1.05667e-09,1.70331e-12,-24364.9,13.3503], Tmin=(200,'K'), Tmax=(1323,'K')),
            NASAPolynomial(coeffs=[21.1225,0.019083,-6.52403e-06,1.01368e-09,-5.88793e-14,-31115.2,-82.1812], Tmin=(1323,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "S66",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {4,S} {16,D}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.40946,0.0475587,-2.19238e-05,2.4325e-09,5.88505e-13,-27653.6,11.7394], Tmin=(200,'K'), Tmax=(1382,'K')),
            NASAPolynomial(coeffs=[18.7901,0.021001,-7.16188e-06,1.11001e-09,-6.43339e-14,-33289.9,-67.8863], Tmin=(1382,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "S43",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {2,S} {16,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.37525,0.0349659,3.6792e-06,-1.56751e-08,4.84743e-12,-26124.8,8.64756], Tmin=(200,'K'), Tmax=(1426,'K')),
            NASAPolynomial(coeffs=[19.2416,0.0207625,-7.12773e-06,1.11093e-09,-6.46776e-14,-32571.1,-71.9638], Tmin=(1426,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "S3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  O u0 p2 c0 {1,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.923102,0.0584732,-3.47947e-05,9.61257e-09,-8.64039e-13,-17275.8,28.4228], Tmin=(200,'K'), Tmax=(1447,'K')),
            NASAPolynomial(coeffs=[17.015,0.0235005,-7.77848e-06,1.18103e-09,-6.74585e-14,-23001.4,-58.7179], Tmin=(1447,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "S31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {1,S} {18,S}
7  O u0 p2 c0 {2,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.48293,0.0792101,-6.45239e-05,2.75598e-08,-4.74651e-12,-35966.3,26.0236], Tmin=(200,'K'), Tmax=(1413,'K')),
            NASAPolynomial(coeffs=[22.5663,0.0236961,-7.8932e-06,1.20343e-09,-6.89317e-14,-42596.4,-84.873], Tmin=(1413,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "NO3",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 O u1 p2 c0 {1,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00798,0.025696,-5.0371e-05,4.78978e-08,-1.69753e-11,15168.3,12.5756], Tmin=(100,'K'), Tmax=(867.17,'K')),
            NASAPolynomial(coeffs=[5.00463,0.00775544,-4.23598e-06,8.19641e-10,-5.57663e-14,15150.3,5.12019], Tmin=(867.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "PC4H9",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16764,0.0127185,7.75537e-07,-1.45166e-08,7.32103e-12,19896.5,10.3783], Tmin=(100,'K'), Tmax=(977.06,'K')),
            NASAPolynomial(coeffs=[9.61834,-0.000251582,5.6424e-08,5.10617e-11,-8.2774e-15,17994.5,-23.8755], Tmin=(977.06,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "N3O",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 O u0 p2 c0 {1,D}
4 N u1 p1 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06581,0.0232233,-3.19213e-05,2.8481e-08,-1.00682e-11,21775.7,20.9366], Tmin=(100,'K'), Tmax=(889.05,'K')),
            NASAPolynomial(coeffs=[3.54681,0.014578,-6.40027e-06,1.14399e-09,-7.53697e-14,21946.3,20.1131], Tmin=(889.05,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(N3d-N3dH) + other(R) + group(Od-N3d) + other(R) +
radical(N3dJ_N)""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "N2O3_B",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {1,S} {5,D}
4 O u0 p2 c0 {2,D}
5 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24881,0.0326008,-3.2293e-05,9.64907e-09,5.98206e-13,9102.95,13.6637], Tmin=(100,'K'), Tmax=(1001.15,'K')),
            NASAPolynomial(coeffs=[13.7258,-0.00118331,2.39146e-07,2.9289e-11,-7.01668e-15,6199.98,-44.7404], Tmin=(1001.15,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: thermo_DFT_CCSDTF12_BAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "S84",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  N u0 p0 c+1 {1,S} {18,D} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.414208,0.0687662,-3.67899e-05,6.2813e-09,4.28404e-13,-22415.9,29.4144], Tmin=(100,'K'), Tmax=(1377.38,'K')),
            NASAPolynomial(coeffs=[15.9507,0.0365722,-1.58056e-05,2.93741e-09,-2.01198e-13,-27921.9,-54.9654], Tmin=(1377.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHON""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "S6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {1,S} {18,D} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.414208,0.0687662,-3.67899e-05,6.2813e-09,4.28404e-13,-22415.9,29.4144], Tmin=(100,'K'), Tmax=(1377.38,'K')),
            NASAPolynomial(coeffs=[15.9507,0.0365722,-1.58056e-05,2.93741e-09,-2.01198e-13,-27921.9,-54.9654], Tmin=(1377.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHON""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "S10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {20,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.245543,0.0986555,-9.43149e-05,5.07006e-08,-1.15653e-11,-16884.6,32.1704], Tmin=(100,'K'), Tmax=(1028,'K')),
            NASAPolynomial(coeffs=[12.3193,0.0497635,-2.29722e-05,4.4328e-09,-3.13006e-13,-19467.8,-28.7942], Tmin=(1028,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsCsR)R)) + other(R) + group(Os-Os(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-
OdOs) + other(R) + group(Od-N3d) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "S73",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {20,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.245543,0.0986555,-9.43149e-05,5.07006e-08,-1.15653e-11,-16884.6,32.1704], Tmin=(100,'K'), Tmax=(1028,'K')),
            NASAPolynomial(coeffs=[12.3193,0.0497635,-2.29722e-05,4.4328e-09,-3.13006e-13,-19467.8,-28.7942], Tmin=(1028,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsCsR)R)) + other(R) + group(Os-Os(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-
OdOs) + other(R) + group(Od-N3d) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "S56",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {20,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.267935,0.100993,-0.000105226,6.46512e-08,-1.70445e-11,-15364.9,33.2982], Tmin=(100,'K'), Tmax=(895.5,'K')),
            NASAPolynomial(coeffs=[10.4758,0.0530044,-2.4847e-05,4.81422e-09,-3.40274e-13,-17289.2,-17.3487], Tmin=(895.5,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsOsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsRR)R)) + other(R) + group(Os-Os(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-
OdOs) + other(R) + group(Od-N3d) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "N3O3",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {4,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 N u0 p1 c0 {1,S} {6,D}
5 O u1 p2 c0 {3,S}
6 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48169,0.0418003,-7.37929e-05,7.32829e-08,-2.65387e-11,15132,35.0547], Tmin=(100,'K'), Tmax=(918.86,'K')),
            NASAPolynomial(coeffs=[1.37837,0.0249071,-1.07972e-05,1.87981e-09,-1.19887e-13,16250.6,45.2682], Tmin=(918.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-ON) + gauche(Os(RR)) + other(R) + group(N3s-
CsHH) + other(R) + group(Os-OsH) + gauche(Os(RR)) + other(R) + group(Od-N3d) + other(R) + radical(ROOJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "S61",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {1,S} {4,D} {16,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.518752,0.0878029,-7.2119e-05,2.47723e-08,-1.70315e-12,-44136.5,31.498], Tmin=(100,'K'), Tmax=(1056.11,'K')),
            NASAPolynomial(coeffs=[20.6368,0.0258523,-9.94501e-06,1.8206e-09,-1.27489e-13,-49618.7,-76.5189], Tmin=(1056.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)CsOsH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) +
group(Cs-(Cds-Cds)HHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-CdsCsOs) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) +
other(R) + group(Os-OsCs) + gauche(Os(Cs(CsRR)R)) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) + group(Os-OsH) + gauche(Os(RR)) +
other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "N2O3_C",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p0 c+1 {1,D} {5,D}
3 O u0 p2 c0 {1,S} {4,S}
4 O u0 p3 c-1 {3,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25338,0.0200254,-2.75587e-05,2.88545e-08,-1.17049e-11,-6704.18,11.4233], Tmin=(100,'K'), Tmax=(854.88,'K')),
            NASAPolynomial(coeffs=[1.71301,0.0181849,-8.45352e-06,1.5751e-09,-1.06859e-13,-6110.19,20.5469], Tmin=(854.88,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-ON) + gauche(Os(RR)) + other(R) + group(Os
-(Cds-Cd)(Cds-Cd)) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "S47",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {7,S}
7  N u0 p1 c0 {6,S} {17,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.342441,0.0866659,-9.30955e-05,5.89374e-08,-1.59473e-11,-12526,28.8595], Tmin=(100,'K'), Tmax=(875.8,'K')),
            NASAPolynomial(coeffs=[9.5553,0.0445889,-2.10301e-05,4.08115e-09,-2.88569e-13,-14139.8,-14.3655], Tmin=(875.8,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) +
group(Cs-CsOsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsRR)R))
+ other(R) + group(Os-Os(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-OdOs) + other(R) + group(Od-N3d) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "S59",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {4,S} {16,S}
6  N u0 p1 c0 {1,S} {17,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42818,0.0622721,-4.60321e-05,2.10661e-08,-4.64089e-12,17046.7,26.9215], Tmin=(100,'K'), Tmax=(975.32,'K')),
            NASAPolynomial(coeffs=[5.36678,0.0461191,-2.11895e-05,4.08536e-09,-2.88309e-13,16278.4,8.01844], Tmin=(975.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(N3dOd)CsCsH) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group
(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(N3d-OdC) + other(R) + group(Od-N3d) + other(R) + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "S70",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  N u0 p1 c0 {1,S} {17,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.42818,0.0622721,-4.60321e-05,2.10661e-08,-4.64089e-12,17046.7,26.9215], Tmin=(100,'K'), Tmax=(975.32,'K')),
            NASAPolynomial(coeffs=[5.36678,0.0461191,-2.11895e-05,4.08536e-09,-2.88309e-13,16278.4,8.01844], Tmin=(975.32,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(N3dOd)CsCsH) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group
(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(N3d-OdC) + other(R) + group(Od-N3d) + other(R) + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "S68",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  O u0 p2 c0 {1,S} {9,S}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18811,0.0420711,-4.32162e-05,2.58455e-08,-6.53767e-12,-27995.2,18.3165], Tmin=(100,'K'), Tmax=(938.27,'K')),
            NASAPolynomial(coeffs=[7.15874,0.0208805,-9.33937e-06,1.77516e-09,-1.2422e-13,-28928,-5.34725], Tmin=(938.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsOsOsH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Os-OsCs)
+ gauche(Os(Cs(CsRR)R)) + other(R) + group(Os-CsH) + gauche(Os(Cs(CsRR)R)) + other(R) + group(Os-OsH) + gauche(Os(RR)) + other(R) + radical(ROOJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "S95",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {4,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  N u0 p1 c0 {6,S} {18,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.565867,0.0766039,-6.00588e-05,2.50987e-08,-4.42666e-12,172.974,29.8198], Tmin=(100,'K'), Tmax=(1295.38,'K')),
            NASAPolynomial(coeffs=[12.3665,0.0401649,-1.78642e-05,3.38345e-09,-2.358e-13,-2884.32,-30.1657], Tmin=(1295.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-Cs(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-OdOs) + other(R) + group(Od-N3d) + other(R) +
radical(CCJCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "S21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {2,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  N u0 p1 c0 {6,S} {18,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.565867,0.0766039,-6.00588e-05,2.50987e-08,-4.42666e-12,172.974,29.8198], Tmin=(100,'K'), Tmax=(1295.38,'K')),
            NASAPolynomial(coeffs=[12.3665,0.0401649,-1.78642e-05,3.38345e-09,-2.358e-13,-2884.32,-30.1657], Tmin=(1295.38,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-Cs(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-OdOs) + other(R) + group(Od-N3d) + other(R) +
radical(CCJCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "S49",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {4,S} {16,S}
6  N u0 p0 c+1 {1,S} {17,D} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 O u0 p3 c-1 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.835012,0.0646686,-3.7415e-05,9.76815e-09,-9.88237e-13,962.628,30.4722], Tmin=(100,'K'), Tmax=(2286.1,'K')),
            NASAPolynomial(coeffs=[24.7238,0.0228691,-9.98793e-06,1.76971e-09,-1.13531e-13,-9959.48,-104.529], Tmin=(2286.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHON + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "S40",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  N u0 p0 c+1 {1,S} {17,D} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 O u0 p3 c-1 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.835012,0.0646686,-3.7415e-05,9.76815e-09,-9.88237e-13,962.628,30.4722], Tmin=(100,'K'), Tmax=(2286.1,'K')),
            NASAPolynomial(coeffs=[24.7238,0.0228691,-9.98793e-06,1.76971e-09,-1.13531e-13,-9959.48,-104.529], Tmin=(2286.1,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHON + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "S115",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  O u0 p2 c-1 {1,S} {2,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {9,D}
9  N u0 p0 c+1 {8,D} {20,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.830201,0.091583,-7.36524e-05,3.35148e-08,-6.16963e-12,-6406.89,50.9408], Tmin=(100,'K'), Tmax=(1406.89,'K')),
            NASAPolynomial(coeffs=[16.5006,0.0377216,-1.13353e-05,1.66763e-09,-9.86364e-14,-10829.4,-36.9729], Tmin=(1406.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + other(R) + group(Cs-CsCsOsH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsHHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Os-OsCs) + other(R) + group(Os-ON) + other(R) + group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R)
+ group(Od-Cd) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "S8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  O u0 p2 c-1 {1,S} {2,S} {7,S}
7  N u0 p0 c+1 {6,S} {8,T}
8  N u0 p0 c+1 {7,T} {9,S}
9  O u0 p2 c0 {8,S} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p3 c-1 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.717842,0.0901777,-7.30749e-05,3.38522e-08,-6.35723e-12,-13534.4,51.4259], Tmin=(100,'K'), Tmax=(1380.41,'K')),
            NASAPolynomial(coeffs=[15.785,0.0378468,-1.13089e-05,1.65518e-09,-9.74685e-14,-17660.8,-31.9543], Tmin=(1380.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + other(R) + group(Cs-CsCsOsH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsHHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Os-CN) + other(R) + group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-ON) + other(R) +
group(Os-(Cds-Cd)(Cds-Cd)) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "S78",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  O u0 p2 c-1 {1,S} {2,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  N u0 p1 c0 {5,S} {7,D}
7  N u0 p0 c+1 {6,D} {14,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.642182,0.0621635,-5.00469e-05,2.35268e-08,-4.41689e-12,778.461,42.1999], Tmin=(100,'K'), Tmax=(1475.67,'K')),
            NASAPolynomial(coeffs=[11.256,0.0265385,-6.86668e-06,8.7133e-10,-4.54126e-14,-1607.69,-10.6069], Tmin=(1475.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + other(R) + group(Cs-CsOsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Os-OsCs) +
other(R) + group(Os-ON) + other(R) + group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(Od-Cd) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "S30",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  O u0 p2 c-1 {1,S} {2,S} {5,S}
5  N u0 p0 c+1 {4,S} {6,T}
6  N u0 p0 c+1 {5,T} {7,S}
7  O u0 p2 c0 {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p3 c-1 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.755523,0.0607477,-4.94365e-05,2.38259e-08,-4.58988e-12,-6349.08,42.6814], Tmin=(100,'K'), Tmax=(1445.16,'K')),
            NASAPolynomial(coeffs=[10.6182,0.0265513,-6.78277e-06,8.4647e-10,-4.3284e-14,-8479.39,-6.03961], Tmin=(1445.16,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + other(R) + group(Cs-CsOsHH) + other(R) + group(Cs-CsHHH) + other(R) + group(Os-CN) + other(R)
+ group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-ON) + other(R) + group(Os-(Cds-Cd)(Cds-Cd)) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "S53",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  O u0 p2 c-1 {1,S} {2,S} {4,S}
4  N u0 p0 c+1 {3,S} {5,T}
5  N u0 p0 c+1 {4,T} {6,S}
6  O u0 p2 c0 {5,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p3 c-1 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61818,0.0456869,-3.82172e-05,2.00162e-08,-4.17061e-12,-2002.75,38.3736], Tmin=(100,'K'), Tmax=(1390.28,'K')),
            NASAPolynomial(coeffs=[7.39579,0.0220801,-5.2122e-06,5.76402e-10,-2.52138e-14,-2934.3,11.0237], Tmin=(1390.28,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsOsHH) + other(R) + group(Cs-CsOsHH) + other(R) + group(Os-CN) + other(R) + group(N3s-CsHH) + other(R) +
group(N3s-CsHH) + other(R) + group(Os-ON) + other(R) + group(Os-(Cds-Cd)(Cds-Cd)) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "S80",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 O u0 p2 c0 {1,S} {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82502,0.0153712,3.12893e-05,-5.25704e-08,2.14865e-11,11358.7,13.5451], Tmin=(100,'K'), Tmax=(953.41,'K')),
            NASAPolynomial(coeffs=[10.0994,0.0111444,-3.4268e-06,6.294e-10,-4.78455e-14,8776.64,-27.4696], Tmin=(953.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: DFT_QCI_thermo""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "S89",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,D} {7,S}
5  C u0 p0 c0 {2,S} {4,D} {16,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.372981,0.0877706,-7.96765e-05,3.72229e-08,-6.92491e-12,-41778.9,32.1577], Tmin=(100,'K'), Tmax=(1297.17,'K')),
            NASAPolynomial(coeffs=[18.8483,0.0284983,-1.11351e-05,1.9962e-09,-1.35652e-13,-46765.5,-65.5744], Tmin=(1297.17,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)CsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-(Cds-Cds)OsHH) + gauche(Cs(RRRR)) + other(R) +
group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cds-CdsCsOs) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) +
group(Os-OsCs) + gauche(Os(CsR)) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) + group(Os-OsH) + gauche(Os(RR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "S2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  N u0 p0 c+1 {1,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 O u0 p2 c0 {4,D}
12 O u0 p3 c-1 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00444,0.00893429,4.41674e-05,-6.45526e-08,2.49543e-11,-22374.1,-17.262], Tmin=(100,'K'), Tmax=(987.64,'K')),
            NASAPolynomial(coeffs=[11.5956,0.00693274,-2.59745e-06,6.32608e-10,-5.56938e-14,-25670.5,-66.6994], Tmin=(987.64,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsCsCs) + gauche(Cs(RRRR)) + other(R) + group(Cs-(Cds-Od)HHH) + gauche(Cs(RRRR)) + other(R) + group
(Cds-OdCsCs) + other(R) + group(N5d-OdOsCs) + other(R) + group(Od-Cd) + other(R) + group(Od-N5d) + other(R) + group(Os-N) + gauche(Os(RR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "S16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  O u0 p2 c0 {2,S} {10,S}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.830751,0.0593933,-6.44123e-05,3.4045e-08,-6.78267e-12,-16802.7,23.2584], Tmin=(100,'K'), Tmax=(1373.81,'K')),
            NASAPolynomial(coeffs=[16.4658,0.00766343,-1.15397e-06,5.91345e-11,3.73323e-16,-20512.9,-55.0054], Tmin=(1373.81,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)HHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-CdsCsOs) + gauche(CsOsCdSs) + other(R) + group
(Cds-CdsOsH) + gauche(CsOsCdSs) + other(R) + group(Os-Os(Cds-Cd)) + gauche(Os(RR)) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) +
group(Os-OsH) + gauche(Os(RR)) + other(R) + radical(ROOJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "S85",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,D} {8,S} {9,S}
4  O u0 p2 c0 {2,S} {6,S}
5  O u0 p2 c0 {1,S} {10,S}
6  O u0 p2 c0 {4,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.02856,0.0497694,-1.08854e-05,-3.5398e-08,2.0658e-11,-16792.2,23.575], Tmin=(100,'K'), Tmax=(948.25,'K')),
            NASAPolynomial(coeffs=[20.9279,0.00443848,-2.53578e-07,6.60895e-11,-1.2239e-14,-22302,-80.5233], Tmin=(948.25,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane + radical(C=CCJO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "S11",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89964,0.050542,-2.22571e-05,3.14865e-09,2.65514e-14,-30016.9,21.1165], Tmin=(100,'K'), Tmax=(2030.45,'K')),
            NASAPolynomial(coeffs=[18.9587,0.0266688,-1.18113e-05,2.07983e-09,-1.32536e-13,-38950.8,-78.2065], Tmin=(2030.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHO""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "S45",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {3,S} {6,S} {16,S}
6  O u0 p2 c0 {5,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.29768,0.0603782,-3.73733e-05,1.12055e-08,-1.37324e-12,-17076,26.0491], Tmin=(100,'K'), Tmax=(1786.86,'K')),
            NASAPolynomial(coeffs=[13.4315,0.0332159,-1.45715e-05,2.6983e-09,-1.82987e-13,-21412.2,-39.5327], Tmin=(1786.86,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHO + radical(CCsJOH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "S67",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {4,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7203,0.0519663,-2.45108e-05,4.50882e-09,-2.18334e-13,-15389.4,27.7524], Tmin=(100,'K'), Tmax=(2054.85,'K')),
            NASAPolynomial(coeffs=[19.1131,0.025728,-1.09188e-05,1.90347e-09,-1.20883e-13,-24145.7,-72.598], Tmin=(2054.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHO + radical(RCCJC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "S57",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  O u0 p2 c0 {4,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.12335,0.0573707,-3.14916e-05,7.54279e-09,-6.26655e-13,-14062.1,28.9641], Tmin=(100,'K'), Tmax=(1784.75,'K')),
            NASAPolynomial(coeffs=[17.2884,0.027411,-1.15811e-05,2.07373e-09,-1.36277e-13,-20830.7,-61.1842], Tmin=(1784.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHO + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "S23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {18,S}
7  O u0 p2 c0 {4,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.154865,0.0894588,-9.32267e-05,5.79349e-08,-1.53171e-11,-33165.8,31.5559], Tmin=(100,'K'), Tmax=(898.69,'K')),
            NASAPolynomial(coeffs=[9.97178,0.0457644,-2.02964e-05,3.83364e-09,-2.67041e-13,-34930.3,-14.7564], Tmin=(898.69,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsOsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsCsR)R)) + other(R) + group(Os-CsH) + gauche(Os(Cs(CsRR)R)) + other(R) + group(Os-
OsH) + gauche(Os(RR)) + other(R) + radical(ROOJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "S87",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 O u0 p2 c0 {1,S} {9,S}
5 O u0 p2 c0 {2,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79428,0.040622,-2.7502e-05,3.77208e-10,4.12303e-12,-34539.5,15.0215], Tmin=(100,'K'), Tmax=(1003.99,'K')),
            NASAPolynomial(coeffs=[14.2809,0.00753018,-2.94622e-06,5.9551e-10,-4.58432e-14,-37886.2,-49.4493], Tmin=(1003.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cds-Cds(Cds-Od)Os) + gauche(CsOsCdSs) + other(R) + group(Cds-Od(Cds-Cds)H) + other(R) + group(Cds-CdsHH) +
gauche(CsOsCdSs) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "S27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  O u0 p2 c0 {1,S} {9,S}
5  O u0 p2 c0 {2,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.22186,0.0433995,3.59638e-06,-6.20636e-08,3.53572e-11,-30950.7,17.0548], Tmin=(100,'K'), Tmax=(883.01,'K')),
            NASAPolynomial(coeffs=[24.0666,-0.00996424,9.10368e-06,-1.93909e-09,1.34864e-13,-36939.2,-101.38], Tmin=(883.01,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)HHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-CdsCsOs) + gauche(CsOsCdSs) + other(R) + group
(Cds-CdsOsH) + gauche(CsOsCdSs) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) +
radical(C=C(O)CJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "S52",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {14,S}
5  C u0 p0 c0 {4,D} {6,S} {15,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.884173,0.0518218,8.85704e-06,-5.69284e-08,2.817e-11,-29831.7,23.3649], Tmin=(100,'K'), Tmax=(936.84,'K')),
            NASAPolynomial(coeffs=[18.6801,0.018043,-4.63272e-06,7.57349e-10,-5.57152e-14,-35018.1,-71.2139], Tmin=(936.84,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group(Cs-(Cds-Cds)CsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) +
group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsOsH) + gauche(CsOsCdSs) +
other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "S46",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.945391,0.0422886,3.1398e-05,-9.95553e-08,4.96808e-11,-13867,21.2508], Tmin=(100,'K'), Tmax=(903.92,'K')),
            NASAPolynomial(coeffs=[28.1096,-0.0112685,9.67392e-06,-1.96408e-09,1.30045e-13,-21500.8,-122.118], Tmin=(903.92,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-OsOsHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-CdsOsH) + gauche(CsOsCdSs) + other(R) + group(Cds-
CdsHH) + gauche(CsOsCdSs) + other(R) + group(Os-Cs(Cds-Cd)) + gauche(Os(CsR)) + other(R) + group(Os-OsCs) + gauche(Os(CsR)) + other(R) + group(Os-OsH)
+ gauche(Os(RR)) + other(R) + radical(ROOJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "S86",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,D} {4,S} {9,S}
3  C u0 p0 c0 {2,D} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.66044,0.0461373,3.51545e-05,-1.07537e-07,5.2816e-11,-32136.6,21.514], Tmin=(100,'K'), Tmax=(912.35,'K')),
            NASAPolynomial(coeffs=[29.8828,-0.00992907,8.87084e-06,-1.76826e-09,1.13674e-13,-40467.5,-133.221], Tmin=(912.35,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-OsOsHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-CdsOsH) + gauche(CsOsCdSs) + other(R) + group(Cds-
CdsHH) + gauche(CsOsCdSs) + other(R) + group(Os-Cs(Cds-Cd)) + gauche(Os(CsR)) + other(R) + group(Os-OsCs) + gauche(Os(CsR)) + other(R) + group(Os-OsH)
+ gauche(Os(RR)) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "S35",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {2,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93712,0.0081278,0.000139369,-2.2214e-07,9.76597e-11,-9871.61,20.4644], Tmin=(100,'K'), Tmax=(886.43,'K')),
            NASAPolynomial(coeffs=[30.2333,-0.019793,1.77955e-05,-3.74184e-09,2.56851e-13,-18807.7,-134.746], Tmin=(886.43,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsOsOsH) + other(R) + group(Cs-CsHHH) + other(R) + group(Cs-OsOsHH) + other(R) + group(Os-CsCs) +
other(R) + group(Os-OsCs) + other(R) + group(Os-OsCs) + other(R) + ring(124trioxolane) + radical(CJCOOH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "S25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {4,S} {11,S}
4  O u0 p2 c0 {2,S} {3,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.55387,0.0205308,0.00010924,-1.9808e-07,9.26026e-11,-12049.4,16.3706], Tmin=(100,'K'), Tmax=(863.37,'K')),
            NASAPolynomial(coeffs=[30.7968,-0.0216909,2.0566e-05,-4.49644e-09,3.20347e-13,-20574.8,-140.543], Tmin=(863.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsOsHH) + other(R) + group(Cs-CsOsHH) + other(R) + group(Cs-OsOsHH) + other(R) + group(Os-CsCs) +
other(R) + group(Os-OsCs) + other(R) + group(Os-OsCs) + other(R) + ring(124trioxane) + radical(CCsJOCs)""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "S38",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u1 p0 c0 {1,S} {7,S} {8,S}
3  C u0 p0 c0 {5,S} {9,D} {10,S}
4  N u0 p1 c0 {1,D} {5,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.14926,0.0327233,1.29776e-07,-1.93565e-08,8.3532e-12,-10426.1,32.0063], Tmin=(100,'K'), Tmax=(1070.27,'K')),
            NASAPolynomial(coeffs=[9.57291,0.0223141,-9.57779e-06,1.82443e-09,-1.29516e-13,-13008,-8.95106], Tmin=(1070.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(CdN3d)HHH) + gauche(Cs(RRRR)) + other(R) + group(Cd-N3dCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-
OdOsH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-CN) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R) + radical(Allyl_P)""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "S93",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 C u0 p0 c0 {1,S} {8,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60725,0.0276497,-1.51512e-05,3.74763e-09,-3.45665e-13,-32764.1,16.6664], Tmin=(100,'K'), Tmax=(1863.45,'K')),
            NASAPolynomial(coeffs=[10.4166,0.0132385,-5.44398e-06,9.52125e-10,-6.14894e-14,-36083,-26.9657], Tmin=(1863.45,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Od)(Cds-Od)HH) + gauche(Cs(RRRR)) + other(R) + group(Cds-OdCsH) + other(R) + group(Cds-OdCsH) +
other(R) + group(Od-Cd) + other(R) + group(Od-Cd) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "S1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {13,D}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 O u0 p2 c0 {4,D}
14 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.15647,0.0738468,-0.000116795,1.18322e-07,-4.69003e-11,-23082.2,26.9248], Tmin=(100,'K'), Tmax=(814.53,'K')),
            NASAPolynomial(coeffs=[0.987894,0.0493063,-2.48853e-05,4.85953e-09,-3.39553e-13,-22213.2,32.8693], Tmin=(814.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane + radical(ROOJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "S74",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {13,D}
4  C u1 p0 c0 {2,S} {3,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {3,D}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.80328,0.0578659,-2.46604e-05,-4.90188e-08,5.88067e-11,-21886.6,24.3827], Tmin=(100,'K'), Tmax=(462.18,'K')),
            NASAPolynomial(coeffs=[4.59523,0.0455829,-2.33536e-05,4.71255e-09,-3.40797e-13,-22271.5,11.6952], Tmin=(462.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CurranPentane + radical(CCJC=O)""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "S22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57767,0.059562,-5.56714e-05,2.96861e-08,-7.00084e-12,-24001.6,22.8529], Tmin=(100,'K'), Tmax=(968.67,'K')),
            NASAPolynomial(coeffs=[7.51563,0.0350417,-1.7701e-05,3.5535e-09,-2.56328e-13,-25152,-5.60527], Tmin=(968.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Od)OsHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-Od(Cds-Cds)Cs) + other(R) + group(Cd-Cd(CO)H) +
gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) + gauche(CsOsCdSs) + other(R) + group(Os-OsCs) + gauche(Os(CsR)) + other(R) + group(Os-OsH) +
gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R)""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "S19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u1 p0 c0 {3,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {2,S} {13,S}
7  O u0 p2 c0 {5,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.140862,0.0749799,-7.4172e-05,3.65523e-08,-7.0076e-12,-20851.3,26.9893], Tmin=(100,'K'), Tmax=(1280.12,'K')),
            NASAPolynomial(coeffs=[18.7756,0.0167511,-5.94079e-06,1.01811e-09,-6.79047e-14,-25622.1,-67.5142], Tmin=(1280.12,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)OsHH) + gauche(Cs(RRRR)) + other(R) + group(Cs-(Cds-Cds)HHH) + gauche(Cs(RRRR)) + other(R) +
group(Cds-CdsCsOs) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsCsH) + gauche(CsOsCdSs) + other(R) + group(Os-OsCs) + gauche(Os(CsR)) + other(R) +
group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) + group(Os-OsH) + gauche(Os(RR)) + other(R) + radical(Allyl_P)""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "S71",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  N u0 p1 c0 {3,S} {17,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.20757,0.0651955,-4.92367e-05,2.13681e-08,-4.13481e-12,18343.6,26.9304], Tmin=(100,'K'), Tmax=(1148.62,'K')),
            NASAPolynomial(coeffs=[7.981,0.0416075,-1.84328e-05,3.48936e-09,-2.43456e-13,16787.6,-6.68606], Tmin=(1148.62,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(N3dOd)CsCsH) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group
(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(N3d-OdC) + other(R) + group(Od-N3d) + other(R) + radical(Cs_P)""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "S5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {4,S} {16,S}
6  N u0 p1 c0 {4,S} {17,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.5221,0.0604433,-3.99878e-05,1.47183e-08,-2.4984e-12,18703.6,27.9191], Tmin=(100,'K'), Tmax=(1220.78,'K')),
            NASAPolynomial(coeffs=[6.47689,0.0442086,-2.00399e-05,3.82479e-09,-2.67569e-13,17493.9,3.02664], Tmin=(1220.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) +
group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-(N3dOd)CHH) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(N3d-OdC) + other(R) + group(Od-N3d) + other(R) + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "S48",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {2,S} {3,S} {17,S}
6  O u0 p2 c0 {3,S} {7,S}
7  N u0 p1 c0 {6,S} {18,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.722869,0.0768265,-6.36759e-05,2.98397e-08,-6.10884e-12,1685.12,30.3056], Tmin=(100,'K'), Tmax=(1109.65,'K')),
            NASAPolynomial(coeffs=[9.56202,0.0449641,-2.06057e-05,3.96399e-09,-2.7923e-13,-276.588,-13.258], Tmin=(1109.65,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsOsHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-Cs(N3dOd)) + gauche(Os(RR)) + other(R) + group(N3d-OdOs) + other(R) + group(Od-N3d) + other(R) +
radical(CCJCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "S29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  N u0 p0 c+1 {1,S} {15,D} {16,S}
6  C u1 p0 c0 {1,S} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 O u0 p3 c-1 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.551544,0.0683021,-4.28988e-05,1.27292e-08,-1.49716e-12,2262.07,30.7074], Tmin=(100,'K'), Tmax=(1951.37,'K')),
            NASAPolynomial(coeffs=[20.1896,0.0280474,-1.19557e-05,2.15782e-09,-1.42823e-13,-5402.21,-77.1638], Tmin=(1951.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHON + radical(Cs_P)""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "S81",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {3,S} {16,S}
6  N u0 p0 c+1 {3,S} {17,D} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 O u0 p3 c-1 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.99637,0.0639413,-3.66014e-05,9.39521e-09,-9.33902e-13,1575.43,30.8821], Tmin=(100,'K'), Tmax=(2310.53,'K')),
            NASAPolynomial(coeffs=[24.1358,0.0238819,-1.05946e-05,1.89126e-09,-1.21965e-13,-9117.31,-100.131], Tmin=(2310.53,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHON + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "S65",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  O u0 p2 c-1 {1,S} {4,S} {7,S}
7  O u0 p2 c0 {6,S} {8,S}
8  N u0 p1 c0 {7,S} {9,D}
9  N u0 p0 c+1 {8,D} {20,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.137962,0.0856197,-5.60384e-05,1.09522e-08,3.83648e-12,-4918.53,49.4958], Tmin=(100,'K'), Tmax=(882.93,'K')),
            NASAPolynomial(coeffs=[13.028,0.0436315,-1.47045e-05,2.39399e-09,-1.53996e-13,-7931.73,-16.2806], Tmin=(882.93,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsOsHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Os-OsCs) + other(R) + group(Os-ON) + other(R) + group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R)
+ group(Od-Cd) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "S28",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  O u0 p2 c-1 {1,S} {4,S} {7,S}
7  N u0 p0 c+1 {6,S} {8,T}
8  N u0 p0 c+1 {7,T} {9,S}
9  O u0 p2 c0 {8,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p3 c-1 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0368976,0.0842711,-5.52835e-05,1.04776e-08,4.27548e-12,-12045.4,50.0264], Tmin=(100,'K'), Tmax=(862.13,'K')),
            NASAPolynomial(coeffs=[12.5093,0.0434493,-1.45122e-05,2.34431e-09,-1.49863e-13,-14855,-12.3884], Tmin=(862.13,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsCsHH) + other(R) + group(Cs-CsOsHH) +
other(R) + group(Cs-CsHHH) + other(R) + group(Os-CN) + other(R) + group(N3s-CsHH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-ON) + other(R) +
group(Os-(Cds-Cd)(Cds-Cd)) + other(R) + ring(Ethylene_oxide)""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "S58",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  N u0 p1 c0 {2,D} {4,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u1 p0 c0 {4,S} {10,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23797,0.0396167,-2.52796e-05,8.17463e-09,-1.12136e-12,-5031.17,30.7164], Tmin=(100,'K'), Tmax=(1572.41,'K')),
            NASAPolynomial(coeffs=[8.27755,0.0242528,-1.06233e-05,1.96066e-09,-1.33394e-13,-6930.51,-1.15463], Tmin=(1572.41,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(CdN3d)HHH) + gauche(Cs(RRRR)) + other(R) + group(Cd-N3dCsH) + gauche(CsOsCdSs) + other(R) + group(Cds-
OdOsH) + other(R) + group(N3s-CsHH) + other(R) + group(Os-CN) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R) + radical((O)CJOC)""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "S55",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  N u0 p1 c0 {1,S} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {6,D} {13,S}
5  C u1 p0 c0 {1,S} {14,S} {15,S}
6  C u0 p0 c0 {4,D} {16,S} {17,S}
7  C u0 p0 c0 {8,S} {18,D} {19,S}
8  O u0 p2 c0 {3,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {7,D}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.144071,0.0723611,-2.86862e-05,-1.12625e-08,8.66349e-12,-10011.9,50.5473], Tmin=(100,'K'), Tmax=(1039.67,'K')),
            NASAPolynomial(coeffs=[15.4728,0.038077,-1.48457e-05,2.70534e-09,-1.87951e-13,-14533.7,-30.4191], Tmin=(1039.67,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-N3sCsCsH) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-
CsHHH) + gauche(Cs(CsRRR)) + other(R) + group(N3s-CsHH) + other(R) + group(Cd-CdHN3s) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) +
gauche(CsOsCdSs) + other(R) + group(Cds-OdOsH) + other(R) + group(Os-CN) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R) + radical(Cs_P)""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "S9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3  N u0 p1 c0 {1,S} {5,S} {8,S}
4  C u1 p0 c0 {1,S} {2,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  C u0 p0 c0 {8,S} {18,D} {19,S}
8  O u0 p2 c0 {3,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 O u0 p2 c0 {7,D}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.20212,0.0728859,-4.08508e-05,8.6365e-09,1.94017e-14,-9366.43,52.3125], Tmin=(100,'K'), Tmax=(1310.18,'K')),
            NASAPolynomial(coeffs=[14.9745,0.0395491,-1.61518e-05,2.92166e-09,-1.97748e-13,-14247,-26.7997], Tmin=(1310.18,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group(Cs-N3sCsHH) + gauche(Cs(RRRR)) + other(R) + group(Cs-
CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(N3s-CsHH) + other(R) + group(Cd-CdHN3s) + gauche(CsOsCdSs) + other(R) + group(Cds-CdsHH) +
gauche(CsOsCdSs) + other(R) + group(Cds-OdOsH) + other(R) + group(Os-CN) + gauche(Os(RR)) + other(R) + group(Od-Cd) + other(R) + radical(Cs_S)""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "S76",
    molecule = 
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42509,0.00627187,2.81987e-05,-3.81545e-08,1.42456e-11,22116.6,8.84373], Tmin=(100,'K'), Tmax=(976.11,'K')),
            NASAPolynomial(coeffs=[6.19525,0.0110573,-3.95349e-06,7.41856e-10,-5.43445e-14,20807,-8.39168], Tmin=(976.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo library: CHN + radical(N3dJ_C)""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "S41",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {18,S}
8  O u0 p2 c0 {6,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.268228,0.096211,-9.82654e-05,5.47811e-08,-1.25489e-11,-27502.5,31.9042], Tmin=(100,'K'), Tmax=(1043.87,'K')),
            NASAPolynomial(coeffs=[14.3548,0.0401794,-1.77534e-05,3.36426e-09,-2.35426e-13,-30555.5,-39.2717], Tmin=(1043.87,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsCsR)R)) + other(R) + group(Os-CsH) + gauche(Os(Cs(CsCsR)R)) + other(R) + group
(Os-OsH) + gauche(Os(RR)) + other(R) + radical(CJCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "S83",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {3,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {18,S}
8  O u0 p2 c0 {6,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0463832,0.0913907,-8.775e-05,4.63356e-08,-1.01729e-11,-28273.4,32.2594], Tmin=(100,'K'), Tmax=(1078.56,'K')),
            NASAPolynomial(coeffs=[13.3879,0.041568,-1.84597e-05,3.50691e-09,-2.45701e-13,-31171.4,-33.5692], Tmin=(1078.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsOsH) + gauche(Cs(Cs(CsRR)CsRR)) +
other(R) + group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Cs-CsHHH) +
gauche(Cs(Cs(CsRR)RRR)) + other(R) + group(Os-OsCs) + gauche(Os(Cs(CsCsR)R)) + other(R) + group(Os-CsH) + gauche(Os(Cs(CsCsR)R)) + other(R) + group
(Os-OsH) + gauche(Os(RR)) + other(R) + radical(RCCJ)""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "S50",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {3,S} {16,S}
6  N u0 p1 c0 {3,S} {17,D}
7  O u0 p2 c0 {3,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14996,0.050998,-1.0285e-05,-2.11056e-08,1.08958e-11,-10750.4,6.36709], Tmin=(100,'K'), Tmax=(1043.89,'K')),
            NASAPolynomial(coeffs=[14.1913,0.0260774,-1.04734e-05,2.00422e-09,-1.44526e-13,-14838.1,-63.6478], Tmin=(1043.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)Cs(CsRR)RR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) +
group(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsCsCsCs) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR))
+ other(R) + group(N3d-OdC) + other(R) + group(Os-CsH) + gauche(Os(CsR)) + other(R) + group(Od-N3d) + other(R) + radical(CCJCO)""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "S14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {7,S} {16,S}
6  N u0 p0 c+1 {1,S} {17,D} {18,S}
7  O u0 p2 c0 {5,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 O u0 p2 c0 {6,D}
18 O u0 p3 c-1 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.222369,0.098086,-0.000111247,7.24947e-08,-1.96234e-11,-22742.1,33.9632], Tmin=(100,'K'), Tmax=(887.85,'K')),
            NASAPolynomial(coeffs=[11.8103,0.0438761,-1.9662e-05,3.72604e-09,-2.59805e-13,-24878.8,-22.6564], Tmin=(887.85,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(N5dOdOs)CsCsH) + gauche(Cs(RRRR)) + other(R) + group(Cs-CsCsHH) + gauche(Cs(CsCsRR)) + other(R) + group
(Cs-CsCsHH) + gauche(Cs(Cs(CsRR)CsRR)) + other(R) + group(Cs-CsOsHH) + gauche(Cs(CsRRR)) + other(R) + group(Cs-CsHHH) + gauche(Cs(Cs(CsRR)RRR)) +
other(R) + group(N5d-OdOsCs) + other(R) + group(Os-CsH) + gauche(Os(Cs(CsRR)R)) + other(R) + group(Od-N5d) + other(R) + group(Os-N) + gauche(Os(RR)) +
other(R) + radical(CCsJOH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "S33",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {5,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  N u0 p0 c+1 {3,S} {10,D} {11,S}
5  O u0 p2 c0 {2,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 O u0 p2 c0 {4,D}
11 O u0 p3 c-1 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09945,0.0533213,-2.9456e-05,-7.925e-09,8.97577e-12,-27648.8,22.2889], Tmin=(100,'K'), Tmax=(965.14,'K')),
            NASAPolynomial(coeffs=[16.8205,0.0125724,-4.05724e-06,7.3272e-10,-5.39192e-14,-31820.1,-58.8872], Tmin=(965.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Thermo group additivity estimation: group(Cs-(Cds-Cds)HHH) + gauche(Cs(RRRR)) + other(R) + group(Cds-CdsCsOs) + gauche(CsOsCdSs) + other(R) + group
(Cd-CdH(N5dOdOs)) + gauche(CsOsCdSs) + other(R) + group(N5d-OdOsCd) + other(R) + group(Os-(Cds-Cd)H) + gauche(Os(RR)) + other(R) + group(Od-N5d) +
other(R) + group(Os-N) + gauche(Os(RR)) + other(R)""",
    longDesc = 
u"""

""",
)

