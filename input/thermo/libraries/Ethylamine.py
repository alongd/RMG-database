#!/usr/bin/env python
# encoding: utf-8

name = "Ethylamine"
shortDesc = u"Ethylamine"
longDesc = u"""
UCCSD(T)-F12A/cc-pVTZ-F12//UM06-2x/cc-pVTZ level of theory
calculated by alongd
"""

entry(
    index = 1,
    label = "NCC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.96049, 0.00242639, 8.03627e-05, -1.4551e-07, 8.69033e-11, -6946.84, 8.35476],
                Tmin = (10, 'K'),
                Tmax = (428.386, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.01959, 0.0298873, -1.57942e-05, 4.13548e-09, -4.29666e-13, -6694.88, 20.0497],
                Tmin = (428.386, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-57.7762, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (224.491, 'J/(mol*K)'),
    ),
)

