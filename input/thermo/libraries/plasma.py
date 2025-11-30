#!/usr/bin/env python
# encoding: utf-8

name = "plasma"
shortDesc = u"Plasma related compounds, including metallic compounds and charged species"
longDesc = u"""
Plasma related compounds, including metallic compounds and charged species

References:
[1] G. Faingold, O. Kalitzky, J.K. Lefkowitz, Fuel Comm. 2022, 12, 100070, https://doi.org/10.1016/j.jfueco.2022.100070
[2] NASA Glenn Coefficients for Calculating Thermodynamic Properties of Individual Species, https://ntrs.nasa.gov/citations/20020085330
"""

entry(
    index = 1,
    label = "e-",
    molecule =
"""
1 e u1 p0 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, -11.720812], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, -11.720812], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, -11.720812], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Ref-Species. JANAF 1985 3/82.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.

Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (0.0,'kJ/mol'),
        S298 = (20.98,'J/(mol*K)'),
    )
Burcat
from [1] Lefkowitz 2022 (not used):
E  electron gas   g12/98E  1.   0.   0.   0.G   298.150  6000.000 1000.        1
 2.50000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
-7.45375000E+02-1.17208122E+01 2.50000000E+00 0.00000000E+00 0.00000000E+00    3
 0.00000000E+00 0.00000000E+00-7.45375000E+02-1.17208122E+01 0.00000000E+00    4
""",
)

entry(
    index = 2,
    label = "He",
    molecule =
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 0.92872397], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 0.92872397], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[3396845.4, -2194.0377, 3.0802319, -8.0689576e-05, 6.2527849e-09, -2.5749901e-13, 4.4299602e-18, 16505.19, -4.0488144], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Ref-Elm. Moore NSRDS-NBS 35 1971; NSRDS-NBS 34 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 3,
    label = "He+",
    molecule =
"""
1 He u1 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 285323.37, 1.6216656], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 285323.37, 1.6216656], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 285323.37, 1.6216656], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Moore NSRDS-NBS 35 1971; NSRDS-NBS 34 1970. Cp/R=2.5""",
    longDesc =
"""
Converted from NASA 9-coefficient format.

Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (2372.322,'kJ/mol'),
        S298 = (126.02,'J/(mol*K)'),
    )
He from BurkeH2O2, mod H298 from ATcT
from [1] Lefkowitz 2022 (not used):
He+               g 3/97HE 1.E -1.   0.   0.G   298.150  6000.000 1000.        1
 2.50000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
 2.85323374E+05 1.62166556E+00 2.50000000E+00 0.00000000E+00 0.00000000E+00    3
 0.00000000E+00 0.00000000E+00 2.85323374E+05 1.62166556E+00 2.86068749E+05    4
""",
)

entry(
    index = 4,
    label = "He-",
    molecule =
"""
1 He u1 p1 c-1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (51.0,'kJ/mol'),
        S298 = (126.14,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
He from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 5,
    label = "Ne",
    molecule =
"""
1 Ne u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 3.3553227], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 3.3553227], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-12382527, 6958.5796, 1.0167093, 0.00014246646, -4.8039339e-09, -1.1702132e-13, 8.4151537e-18, -56639.336, 16.484387], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Ref-Elm. Moore: NSRDS-NBS 35 1971; NSRDS-NBS 34 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 6,
    label = "Ne+",
    molecule =
"""
1 Ne u1 p3 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[72815.515, -869.5698, 6.108647, -0.0058413569, 5.0410442e-06, -2.2937592e-09, 4.3390657e-13, 254599.69, -16.734494], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-111274.26, 476.56979, 2.1966505, 0.00011025931, -2.2875644e-08, 2.5102182e-12, -1.1266461e-16, 247253.69, 7.4661405], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-56150.946, 141.89588, 2.4757173, 1.9443742e-06, -6.3227366e-11, -1.3145112e-16, 3.534859e-20, 249445.24, 5.366878], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Moore: NSRDS-NBS 35 1971; NSRDS-NBS 34 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 7,
    label = "Ar",
    molecule =
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 4.3796749], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[20.105385, -0.059926611, 2.5000694, -3.9921412e-08, 1.2052721e-11, -1.8190156e-15, 1.0785766e-19, -744.99396, 4.3791801], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-9.9512651e+08, 645888.73, -167.58947, 0.023199334, -1.7210809e-06, 6.5319385e-11, -9.7401477e-16, -5078300.3, 1465.2985], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Ref-Elm. Spec: NSRDS-NBS 35 1971.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 8,
    label = "Ar+",
    molecule =
"""
1 Ar u1 p3 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-57312.092, 793.07915, -1.7171212, 0.01044184, -1.1802075e-05, 6.5281348e-09, -1.4475581e-12, 179057.22, 29.491509], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-383596.54, 816.20197, 2.3013426, -4.9529838e-06, 1.2051085e-08, -2.1850503e-12, 1.2654939e-16, 177181.15, 7.9475075], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[10173728, -6685.1041, 4.4609538, -0.00030341653, 2.6234796e-08, -1.2051158e-12, 2.3038069e-17, 235435.35, -10.445193], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Levels: NSRDS-NBS 35 1971; IP:NSRDS-NBS 34 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (1520.580,'kJ/mol'),
        S298 = (154.84,'J/(mol*K)'),
    )
Ar from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 9,
    label = "Ar+2",
    molecule =
"""
1 Ar u0 p3 c+2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (4186.468,'kJ/mol'),
        S298 = (154.84,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Ar from primaryThermoLibrary, mod H298 from ATcT
""",
)

# entry(
#     index = 10,
#     label = "Ar-",
#     molecule =
# """
# 1 Ar u1 p4 c-1
# """,
#     thermo = ThermoData(
#         Tdata = ([300,400,500,600,800,1000,1500],'K'),
#         Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
#         H298 = (25.0,'kJ/mol'),
#         S298 = (154.84,'J/(mol*K)'),
#     ),
#     shortDesc = u"""""",
#     longDesc =
# u"""
# Ar from primaryThermoLibrary, mod H298 from ATcT
# """,
# )

# entry(
#     index = 11,
#     label = "Kr",
#     molecule =
# """
# 1 Ar u1 p3 c+1
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 5.4909565], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[264.36391, -0.79100508, 2.5009206, -5.3281641e-07, 1.6207302e-10, -2.467898e-14, 1.478585e-18, -740.34889, 5.4843981], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[-1.3755311e+09, 906403.05, -240.34814, 0.03378312, -2.5631039e-06, 9.9697878e-11, -1.5212497e-15, -7111667.4, 2086.8663], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """Ref-Elm. Spec:JPCRD v20 n5 1991 p859.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 12,
#     label = "Kr+",
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-5650.4029, 69.307408, 2.1570281, 0.00087112289, -1.1816097e-06, 7.8621986e-10, -1.8325894e-13, 162116.41, 8.8182423], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-221656.7, 1166.1678, 0.48696553, 0.0014292236, -3.9496286e-07, 4.9828535e-11, -2.4067193e-15, 155600.29, 20.59231], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[-33198760, 17979.531, -0.71550159, 0.0002671089, -6.1962519e-09, -4.107026e-13, 2.0006194e-17, 16481.143, 36.203257], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (298.15, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """Levels:JPCRD v20 n5 1991 p859.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )

# entry(
#     index = 13,
#     label = "Xe",
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, -745.375, 6.1644199], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[4025.2267, -12.095075, 2.5141533, -8.2481021e-06, 2.5302326e-09, -3.8923332e-13, 2.3604391e-17, -668.58007, 6.0636764], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[2.5403975e+08, -110537.38, 13.826441, 0.0015006146, -3.935359e-07, 2.7657906e-11, -5.9439906e-16, 928544.38, -110.98349], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """Ref-Elm. Spec: NSRDS-NBS 35 1971; NSRDS-NBS 34 1970.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 14,
#     label = "Xe+",
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[100.29236, -1.2187536, 2.5060165, -1.5474113e-05, 2.1913727e-08, -1.6236841e-11, 4.9291327e-15, 140766.54, 7.5166782], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-12416.839, -150.06546, 2.9646783, -0.00046933967, 1.9591387e-07, -3.0377619e-11, 1.6373611e-15, 141496.68, 4.5656515], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[-2.5622759e+08, 157047.69, -36.355372, 0.0050193926, -3.4381072e-07, 1.1405447e-11, -1.2956615e-16, -1103556.5, 343.61885], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (298.15, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """Moore: NSRDS-NBS 35 1971; NSRDS-NBS 34 1970.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )

entry(
    index = 15,
    label = "H",
    molecule =
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 25473.708, -0.44668285], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[60.787743, -0.18193544, 2.5002118, -1.2265129e-07, 3.7328763e-11, -5.6877446e-15, 3.4102102e-19, 25474.864, -0.44819178], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.1737577e+08, -131203.54, 33.991742, -0.0038139997, 2.4328548e-07, -7.6942755e-12, 9.6441056e-17, 1067638.1, -274.23011], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """D0(H2):JMolSpc,v33 1970 p147. NSRDS-NBS 3 SEC 6 1972.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 16,
    label = "H+",
    molecule =
"""
1 H u0 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 184021.49, -1.1406466], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 184021.49, -1.1406466], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 184021.49, -1.1406466], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """CP/R=2.5. IP: Moore,NSRDS-NBS 3,SEC 6,1972.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.

Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,4.97,4.97],'cal/(mol*K)'),
        H298 = (1530.047,'kcal/mol'),
        S298 = (27.39,'cal/(mol*K)'),
    )
modified H298 from ATcT
""",
)

entry(
    index = 17,
    label = "H-",
    molecule =
"""
1 H u0 p1 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 15976.155, -1.1390139], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 15976.155, -1.1390139], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 15976.155, -1.1390139], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """JPCRD v14 n3 1985 p731.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.

Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (145.228,'kJ/mol'),
        S298 = (114.72,'J/(mol*K)'),
    )
H from primaryThermoData, mod H298 from ATcT

from [1] Lefkowitz 2022 (not used):
H-                L/7/88H   1E   1    0    0G   298.150  6000.000 1000.        1
 0.25000000E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
 0.15976167E+05-0.11390139E+01 0.25000000E+01 0.00000000E+00 0.00000000E+00    3
 0.00000000E+00 0.00000000E+00 0.15976167E+05-0.11390139E+01 0.16721542E+05    4
""",
)

entry(
    index = 18,
    label = "H2",
    molecule =
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[40783.228, -800.91854, 8.2147017, -0.012697144, 1.7536049e-05, -1.2028602e-08, 3.3680932e-12, 2682.4844, -30.437887], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[560812.34, -837.14913, 2.975363, 0.0012522499, -3.7407184e-07, 5.9366282e-11, -3.6069957e-15, 5339.8158, -2.202764], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[4.9667161e+08, -314744.81, 79.838875, -0.0084145042, 4.7530604e-07, -1.3718097e-11, 1.6053746e-16, 2488354.7, -669.55242], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hydrogen. TPIS, v1, pt2, 1978, pp31-32.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 19,
    label = "H2+",
    molecule =
"""
1 H u1 p0 c0
2 H u0 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-31208.922, 230.463, 3.3355612, -0.0024190492, 7.0060126e-06, -5.6100042e-09, 1.564168e-12, 177410.46, -0.82783385], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1672226.2, -6595.1854, 12.79322, -0.0055093455, 2.0306695e-06, -3.3510275e-10, 1.9460891e-14, 218999.96, -67.927111], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-1.822062e+08, 101819.13, -12.458208, 0.0010766346, -3.9322097e-08, 6.2851434e-13, -2.094379e-18, -651306.16, 147.14056], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS, vol 1, part 2,1978 p33.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (2372.322,'kJ/mol'),
        S298 = (126.02,'J/(mol*K)'),
    )
H2+ has a single electron in the sigma bond, RMG cannot represent it directly, using a VDW complex instead
from [1] Lefkowitz 2022 (not used):
H2+               ATcT AH  2.E -1.   0.   0.G   298.150  6000.000 1000.        1
 3.44204765E+00 5.99083239E-04 6.69133685E-08-3.43574373E-11 1.97626599E-15    2
 1.78650236E+05-2.79499055E+00 3.77256072E+00-1.95746590E-03 4.54812047E-06    3
-2.82152141E-09 5.33969209E-13 1.78694654E+05-3.96609192E+00 1.79767298E+05    4
""",
)

entry(
    index = 20,
    label = "H2-",
    molecule =
"""
1 H u1 p0 c-1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.8380142, -0.0031794768, 1.0043011e-05, -9.5518116e-09, 3.128133e-12, 27234.856, -3.9986236], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 3.2921076, 0.0014358626, -5.4705593e-07, 1.0433883e-10, -7.3827998e-15, 27216.181, -1.9827777], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (254.7,'kJ/mol'),
        S298 = (130.68,'J/(mol*K)'),
    )
H2 from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 21,
    label = "O",
    molecule =
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-7953.6113, 160.71778, 1.9662264, 0.0010136703, -1.1104154e-06, 6.5175075e-10, -1.5847793e-13, 28403.624, 8.4042418], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[261902.03, -729.8722, 3.3171773, -0.00042813344, 1.0361046e-07, -9.4383043e-12, 2.7250383e-16, 33924.281, -0.66795854], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[1.7790043e+08, -108232.83, 28.107784, -0.0029752323, 1.8549975e-07, -5.7962315e-12, 7.1917202e-17, 889094.26, -218.17282], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """D0(O2):CJP v32 1954 p110. Spec:NSRDS-NBS 3 sect 1976.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 22,
    label = "O+",
    molecule =
"""
1 O u1 p2 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 187935.28, 4.3933768], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-216651.32, 666.54561, 1.7020644, 0.00047149928, -1.4271318e-07, 2.0165959e-11, -9.1071578e-16, 183719.2, 10.056904], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-2.1438354e+08, 146951.85, -36.808645, 0.0050361645, -3.0878739e-07, 9.1868349e-12, -1.0741633e-16, -961420.9, 342.61931], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Spec:JPCRD v22 n5 1993.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
NASA(polynomials=[NASAPolynomial(coeffs=[2.5,0,0,0,0,187935,4.39338], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[2.48542,2.56979e-05,-1.28833e-08,1.65525e-12,1.09933e-16,187941,4.47425],
                                              Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="g 8/97")
[1] Lefkowitz 2022
""",
)

entry(
    index = 23,
    label = "O+2",
    molecule =
"""
1 O u0 p2 c+2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (4953.000,'kJ/mol'),
        S298 = (599.13,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
O from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 24,
    label = "O+3",
    molecule =
"""
1 O u1 p1 c+3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (10252.880,'kJ/mol'),
        S298 = (161.04,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
O from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 25,
    label = "O+4",
    molecule =
"""
1 O u0 p1 c+4
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (17721.064,'kJ/mol'),
        S298 = (599.13,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
O from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 26,
    label = "O+5",
    molecule =
"""
1 O u1 p0 c+5
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (28710.645,'kJ/mol'),
        S298 = (599.13,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
O from primaryThermoLibrary, mod H298 from ATcT
""",
)

entry(
    index = 27,
    label = "O-",
    molecule =
"""
1 O u1 p3 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-5695.8571, 109.92873, 2.1847197, 0.00053263598, -5.2988784e-07, 2.8702162e-10, -6.5246927e-14, 10932.875, 6.7298639], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[9769.3632, 7.1596048, 2.4949617, 1.9682409e-06, -4.3041749e-10, 4.9120831e-14, -2.2716001e-18, 11495.544, 4.8370364], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[566.2391, 7.5723403, 2.4983525, 1.8626324e-07, -1.1512272e-11, 3.6888142e-16, -4.7932976e-21, 11484.26, 4.8134066], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Spec:TPIS 1989 v1 pt1 p93. EA:JPCRD v14 n3 1985 p731.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (108.097,'kJ/mol'),
        S298 = (161.04,'J/(mol*K)'),
    )
O from primaryThermoData, mod H298 from ATcT
from [1] Lefkowitz 2022 (not used):
O-                g 1/97O  1.E  1.   0.   0.G   298.150  6000.000 1000.        1
 2.54474869E+00-4.66695513E-05 1.84912357E-08-3.18159223E-12 1.98962956E-16    2
 1.15042089E+04 4.52131015E+00 2.90805921E+00-1.69804907E-03 2.98069955E-06    3
-2.43835127E-09 7.61229311E-13 1.14357717E+04 2.80339097E+00 1.22492116E+04    4
""",
)

entry(
    index = 28,
    label = "OH",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-1998.859, 93.001362, 3.0508542, 0.0015295293, -3.157891e-06, 3.3154462e-09, -1.1387627e-12, 3239.6835, 4.6741108], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1017393.4, -2509.9573, 5.1165479, 0.00013052999, -8.2843223e-08, 2.0064759e-11, -1.5569937e-15, 20444.871, -11.012823], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.8472342e+08, -185953.26, 50.082409, -0.005142375, 2.8755366e-07, -8.228818e-12, 9.567229e-17, 1468642.4, -402.35556], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1978 pt1 p110; pt2 p37.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 29,
    label = "OH+",
    molecule =
"""
1 O u0 p2 c+1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[60316.309, -757.35203, 7.3077529, -0.0095068817, 1.2025558e-05, -6.8290261e-09, 1.5015887e-12, 157858, -19.50107], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[504072.91, -1380.053, 4.1254622, 0.00083319488, -3.4428563e-07, 6.792854e-11, -4.3638721e-15, 163315.71, -3.9970585], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[1.1582867e+09, -684128.04, 157.61946, -0.016184213, 8.8461288e-07, -2.4750385e-11, 2.8077309e-16, 5615529, -1351.879], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props:TPIS 1978 v1 pt2 p39.IP:TPIS 1989 v1 pt1 p117.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 30,
    label = "OH-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[29108.808, -321.69049, 4.8510291, -0.0025790354, 2.00498e-06, -7.956853e-11, -2.3204956e-13, -16640.393, -7.1215913], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[471133.12, -857.23367, 3.1661812, 0.0012335813, -3.9992446e-07, 6.2390817e-11, -3.3543432e-15, -12000.022, 1.4877363], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p118; pt2 p32.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.10,29.06,29.08,29.18,29.62,30.34,32.30],'J/(mol*K)'),
        H298 = (-229.756,'kJ/mol'),
        S298 = (183.92,'J/(mol*K)'),
    )
OH from primaryThermoData, mod H298 from ATcT
from [1] Lefkowitz 2022 (not used):
OH-               g 4/02O  1.H  1.E  1.   0.G   298.150  6000.000 1000.        1
 2.80023747E+00 1.13380509E-03-2.99666184E-07 4.01911483E-11-1.78988913E-15    2
-1.82535298E+04 4.69394620E+00 3.43126659E+00 6.31146866E-04-1.92914359E-06    3
 2.40618712E-09-8.66679361E-13-1.85085918E+04 1.07990541E+00-1.74702052E+04    4
""",
)

entry(
    index = 31,
    label = "H2O",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-39479.608, 575.5731, 0.93178265, 0.0072227129, -7.3425574e-06, 4.9550435e-09, -1.3369332e-12, -33039.743, 17.242058], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1034972.1, -2412.6986, 4.6461108, 0.0022919983, -6.8368305e-07, 9.4264689e-11, -4.8223805e-15, -13842.865, -7.9781485], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """CODATA 1989. JRNBS 1987 v92 p35. TRC tuv-25 10/88.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 32,
    label = "H2O+",
    molecule =
"""
1 O u1 p1 c+1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-42143.91, 675.35706, -0.019677133, 0.010716923, -1.280882e-05, 9.2101219e-09, -2.6533673e-12, 113695.27, 22.936644], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[626595.51, -2873.5517, 7.7263616, -0.0009069269, 6.1877578e-07, -1.2027507e-10, 7.4141236e-15, 134269.47, -26.430646], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-17539188, -2632.7043, 11.655274, -0.00077300808, 5.6303126e-08, -1.9648632e-12, 2.6816754e-17, 116816.84, -57.626287], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p125; pt2 p38.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 33,
    label = "H3O+",
    molecule =
"""
1 O u0 p1 c+1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-79273.617, 1321.8864, -4.3050896, 0.023067548, -2.5161499e-05, 1.5961194e-08, -4.162293e-12, 64576.003, 45.85348], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2961335.3, -9200.9969, 13.428453, -0.00056583835, 1.3074228e-08, 7.0484533e-12, -6.0289858e-16, 129153.94, -70.324346], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-15868884, 4874.1141, 8.8875193, 0.00012906942, -8.1040085e-09, 2.623759e-13, -3.4339087e-18, 21097.431, -32.229972], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p130; pt2 p41.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.63,34.23,35.06,36.08,38.47,40.86,46.10],'J/(mol*K)'),
        H298 = (599.13,'kJ/mol'),
        S298 = (188.63,'J/(mol*K)'),
    )
H2O from primaryThermoData, mod H298 from ATcT
from [1] Lefkowitz 2022 (not used):
H3O+              ATcT AH  3.O  1.E -1.   0.G   298.150  6000.000 1000.        1
 2.49647765E+00 5.72844840E-03-1.83953239E-06 2.73577348E-10-1.54093917E-14    2
 7.16244227E+04 7.45850493E+00 3.79295251E+00-9.10852723E-04 1.16363521E-05    3
-1.21364865E-08 4.26159624E-12 7.14027518E+04 1.47156927E+00 7.25739701E+04    4
""",
)

entry(
    index = 34,
    label = "O2",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-34255.634, 484.7001, 1.119011, 0.0042938892, -6.8363005e-07, -2.0233727e-09, 1.03904e-12, -3391.4549, 18.496995], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-1037939, 2344.8303, 1.819732, 0.0012678476, -2.188068e-07, 2.0537196e-11, -8.193467e-16, -16890.109, 17.387165], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[4.9752943e+08, -286610.69, 66.903522, -0.006169959, 3.016396e-07, -7.4214166e-12, 7.2781758e-17, 2293554, -553.06216], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p94; pt2 p9.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 35,
    label = "O2+",
    molecule =
"""
1 O u0 p2 c+1 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-86072.054, 1051.8759, -0.54323805, 0.0065711665, -3.2742638e-06, 5.9406453e-11, 3.2387848e-13, 134554.47, 29.027097], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[73846.549, -845.95595, 4.9851642, -0.00016110109, 6.427084e-08, -1.5049399e-11, 1.5784654e-15, 144632.1, -5.8112306], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-1.5621255e+09, 1161406.8, -330.25047, 0.047109375, -3.3544614e-06, 1.1679686e-10, -1.5897548e-15, -8857866.3, 2852.0356], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p98; pt2 p11.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
NASA(polynomials=[NASAPolynomial(coeffs=[4.61017,-0.00635952,1.42426e-05,-1.20998e-08,3.70957e-12,139742,-0.201327], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[3.31676,0.00111522,-3.83493e-07,5.72785e-11,-2.77648e-15,139877,5.44726], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="RUS 89")
[1] Lefkowitz 2022
""",
)

entry(
    index = 36,
    label = "O2-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[18839.445, 114.94603, 1.5189264, 0.0080159694, -9.8503493e-06, 6.0440191e-09, -1.4863836e-12, -7101.4944, 15.011828], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-56583.551, -236.69398, 4.6757392, -2.1921658e-05, 1.7100761e-08, -1.7556297e-12, 8.2371037e-17, -5960.741, -2.4362052], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Cons and Hf0: TPIS,v1 pt1 p100,1989.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.39,30.12,31.08,32.08,33.75,34.88,36.57],'J/(mol*K)'),
        H298 = (-42.72,'kJ/mol'),
        S298 = (205.11,'J/(mol*K)'),
    )
O2 from primaryThermoData, mod H298 from ATcT
from [1] Lefkowitz 2022 (not used):
O2-               L 4/89O   2E   1    0    0G   298.150  6000.000 1000.        1
 3.95666294E+00 5.98141823E-04-2.12133905E-07 3.63267581E-11-2.24989228E-15    2
-7.06287229E+03 2.27871017E+00 3.66442522E+00-9.28741138E-04 6.45477082E-06    3
-7.74703380E-09 2.93332662E-12-6.87076983E+03 4.35140681E+00-5.77639825E+03    4
""",
)

entry(
    index = 37,
    label = "HO2",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-75988.825, 1329.3839, -4.6773882, 0.025083082, -3.0065516e-05, 1.8956001e-08, -4.8285674e-12, -5809.3664, 51.936021], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-1810669.7, 4963.192, -1.039499, 0.0045601485, -1.0618594e-06, 1.1445679e-10, -4.7630642e-15, -31944.187, 40.668509], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hills JCP 1984 v81 p4458. Jacox JPCRD 1988 v17 p303.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 38,
    label = "HO2-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[598.05177, 453.21837, -0.78856418, 0.016606068, -2.000304e-05, 1.2732013e-08, -3.2714935e-12, -14672.238, 28.801954], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[888356.31, -3269.6062, 8.3818738, -0.00030270486, 3.1892308e-08, -9.6948963e-13, -4.2355967e-17, 7066.474, -27.506362], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p121; pt2 p35.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 39,
    label = "O3-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p1 c+1 {1,S} {3,D}
3 O u1 p1 c+1 {2,D}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.90241,0.0156105,-2.09606e-05,1.3589e-08,-3.46559e-12,-9165.17,15.1034], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[5.95188,0.00108039,-4.24643e-07,7.26564e-11,-4.52533e-15,-10108,-4.96701], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="""g 1/97"""),
    shortDesc = u"""""",
    longDesc =
u"""
[1] Lefkowitz 2022
""",
)

entry(
    index = 40,
    label = "N",
    molecule =
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 56104.638, 4.1939093], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[88765.014, -107.12315, 2.3621883, 0.00029167201, -1.7295151e-07, 4.0126579e-11, -2.6772276e-15, 56973.513, 4.8652358], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[5.475181e+08, -310757.5, 69.167827, -0.0068479881, 3.8275724e-07, -1.0983677e-11, 1.277986e-16, 2550585.6, -584.87697], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf:CODATA1989. Spec:NSRDS-NBS 3 sec5 1975.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 41,
    label = "N+",
    molecule =
"""
1 N u2 p1 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[5237.0792, 2.2999583, 2.4874888, 2.7374908e-05, -3.1344476e-08, 1.8501113e-11, -4.447351e-15, 225628.47, 5.0768351], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[290497.04, -855.79086, 3.4773893, -0.00052882672, 1.3523503e-07, -1.3898341e-11, 5.0461663e-16, 231081, -1.9941423], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[16460921, -11131.652, 4.9769866, -0.00020053936, 1.0224814e-08, -2.6914309e-13, 3.5399316e-18, 313628.47, -17.06646], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """NSRDS-NBS 3 sec5 1975.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (1875.687,'kJ/mol'),
        S298 = (153.27,'J/(mol*K)'),
    )
N from primaryThermoLibrary, mod H298 from ATcT
from [1] Lefkowitz 2022 (not used):
N+                g 6/97N  1.E -1.   0.   0.G   298.150  6000.000 1000.        1
 2.51210704E+00 1.75367440E-06-1.50557538E-08 7.06834189E-12-6.31861166E-16    2
 2.25597004E+05 4.92236293E+00 2.79781357E+00-1.41287178E-03 2.68686998E-06    3
-2.31615591E-09 7.49585578E-13 2.25548731E+05 3.59928845E+00 2.26339616E+05    4
""",
)

entry(
    index = 42,
    label = "N-",
    molecule =
"""
1 N u2 p2 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[1428.9346, 7.5206871, 2.4758588, 4.4150235e-05, -4.657766e-08, 2.6388624e-11, -6.2138191e-15, 56175.317, 5.1505028], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2051.106, 1.6353874, 2.4979363, 1.2734702e-06, -3.9656322e-10, 5.9542596e-14, -3.4158433e-18, 56205.9, 5.0194328], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2199.8314, 0.76822412, 2.4995112, 1.3518073e-07, -1.8189815e-11, 1.1081925e-15, -2.4192234e-20, 56210.924, 5.0087165], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """EA:JPCRD v14 n3 1985 p731. Spec:JANAF 1985 12/82.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 43,
    label = "NH",
    molecule =
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[13596.513, -190.02966, 4.5184968, -0.0024327769, 2.3775875e-06, -2.5927971e-10, -2.6596808e-13, 42809.722, -3.8865576], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1958142, -5782.8613, 9.335742, -0.0022929103, 6.0760925e-07, -6.6479427e-11, 2.3842348e-15, 78989.123, -41.1697], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[95246368, -85858.269, 29.804452, -0.0029795637, 1.6563342e-07, -4.7447918e-12, 5.5701483e-17, 696143.43, -222.90274], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props: TPIS 1978 v1 pt2 p223 DelH: JPC 1989 v93 p530.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 44,
    label = "NH+",
    molecule =
"""
1 N u1 p1 c+1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[4253.6569, -245.82222, 6.7089195, -0.010384894, 1.5090086e-05, -9.5805122e-09, 2.3332068e-12, 200107.78, -13.950572], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1405709.4, -4136.2157, 7.6320145, -0.0012283258, 2.7211877e-07, -2.0100983e-11, 3.7171902e-17, 225897.6, -27.867848], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.3929418e+08, -174165.86, 51.079079, -0.0055676237, 3.2733916e-07, -9.7979781e-12, 1.1865433e-16, 1554705.3, -406.59689], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props: TPIS 1989 v1 pt2 p216. Hf:JCP 1985 v83 p4319.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
NASA(polynomials=[NASAPolynomial(coeffs=[4.61611,-0.00313436,2.91705e-06,2.57385e-10,-7.31431e-13,199085,-2.92758], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[2.95919,0.00134992,-4.61488e-07,8.26978e-11,-5.55759e-15,199525,5.59978], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="L 2/89")
[1] Lefkowitz 2022
""",
)

entry(
    index = 45,
    label = "NH2+",
    molecule =
"""
1 N u0 p1 c+1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.11219,-0.00158942,5.72106e-06,-4.30115e-09,1.18452e-12,151544,-0.385152], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[2.66716,0.00342796,-1.12918e-06,1.71029e-10,-9.76275e-15,151884,6.81237], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="""cation T09/09"""),
    shortDesc = u"""""",
    longDesc =
u"""
[1] Lefkowitz 2022
""",
)

entry(
    index = 46,
    label = "NH3",
    molecule =
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-76812.261, 1270.9516, -3.8932291, 0.021459884, -2.1837667e-05, 1.3173857e-08, -3.3323221e-12, -12648.864, 43.660149], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2452389.5, -8040.8942, 12.713462, -0.00039801866, 3.5525028e-08, 2.5309236e-12, -3.3227005e-16, 43861.92, -64.623302], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 p219. JRNBS 1968 v72A p207 for low T.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 47,
    label = "NH3+",
    molecule =
"""
1 N u1 p0 c+1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.62055,0.000638853,8.28649e-06,-9.01954e-09,3.20297e-12,112287,2.80176], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[2.58855,0.00574164,-1.86472e-06,2.7972e-10,-1.58594e-14,112470,7.60835], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="""cation T09/09"""),
    shortDesc = u"""""",
    longDesc =
u"""
[1] Lefkowitz 2022
""",
)

entry(
    index = 48,
    label = "NH4+",
    molecule =
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-266831.58, 3763.0207, -15.713277, 0.045488202, -4.3799621e-05, 2.4644783e-08, -5.9615323e-12, 58232.847, 111.20872], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[4141889, -14420.72, 20.118936, -0.0019714926, 3.1127214e-07, -2.60298e-11, 8.8943421e-16, 166419.62, -120.15357], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0,Cons: TPIS 1989 v1 pt1 p355; pt2 p220.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 49,
    label = "NO",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-11439.165, 153.64676, 3.4314687, -0.0026685924, 8.4813991e-06, -7.6851111e-09, 2.3867977e-12, 9098.2144, 6.7287275], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[223901.87, -1289.6516, 5.433936, -0.00036560349, 9.8809664e-08, -1.4160769e-11, 9.3801846e-16, 17503.177, -8.5016671], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-9.5753035e+08, 591243.45, -138.45668, 0.016943394, -1.0073511e-06, 2.9125841e-11, -3.2951093e-16, -4677501.2, 1242.0812], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """D0,Props: TPIS 1978,1989 v1 pt1 p326; pt2 p203.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 50,
    label = "NO+",
    molecule =
"""
1 N u0 p1 c+1 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[1398.1066, -159.04469, 5.1228954, -0.0063943886, 1.1239183e-05, -7.9885813e-09, 2.1073837e-12, 118749.51, -4.3984318], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[606987.69, -2278.3954, 6.0803247, -0.00060668476, 1.4320026e-07, -1.7479905e-11, 8.9350141e-16, 132270.96, -15.198798], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.6764003e+09, -1832948.7, 509.92494, -0.071138193, 5.3176599e-06, -1.9632082e-10, 2.8052682e-15, 14433089, -4324.0445], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Cp,S,IP(NO): TPIS 1989 v1 pt1 p330;pt2 p205.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 51,
    label = "NO2",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-56420.388, 963.30857, -2.434511, 0.019277609, -1.8745593e-05, 9.1454977e-09, -1.7776476e-12, -1547.925, 40.678513], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[721300.16, -3832.6152, 11.139633, -0.0022380622, 6.5477234e-07, -7.6113359e-11, 3.3283611e-15, 25024.974, -43.051299], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0,Cons: TPIS 1989 v1 pt1 p332; pt2 p207.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 52,
    label = "NO2-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-12820.695, 699.01401, -2.8125971, 0.024128945, -2.831607e-05, 1.6705095e-08, -3.9833306e-12, -28099.157, 40.635382], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[132570.51, -1557.0309, 8.1267208, -0.00027286213, -4.7075556e-08, 2.8267307e-11, -2.3539863e-15, -17157.96, -22.28309], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """EA,Cons: TPIS 1989 v1 pt1 p334; pt2 p208.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 53,
    label = "NO3",
    molecule =
"""
1 O u1 p2 c0 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,D}
3 O u0 p3 c-1 {2,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[34053.984, 226.66707, -3.7930816, 0.041707327, -5.7099133e-05, 3.8341581e-08, -1.0219693e-11, 7088.1122, 42.730918], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-394387.27, -824.42635, 10.613258, -0.00024487498, 5.4060603e-08, -6.1954667e-12, 2.8700001e-16, 8982.0117, -34.446665], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """JANAF 12/64. JPCRD v14 sup1 1985 p1537.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 54,
    label = "NO3-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,S} {4,D}
3 O u0 p3 c-1 {2,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[92048.136, -391.11712, -0.23543568, 0.028360421, -3.4613241e-05, 2.0817875e-08, -5.0216013e-12, -35764.115, 22.999424], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-311000.58, -1369.0876, 11.013429, -0.00040368788, 8.9020865e-08, -1.0197335e-11, 4.7233308e-16, -33643.211, -38.784326], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0,Cons: TPIS 1989 v1 pt1 p335; pt2 p209.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 55,
    label = "N2",
    molecule =
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[22103.715, -381.84618, 6.0827384, -0.0085309144, 1.3846462e-05, -9.6257936e-09, 2.5197058e-12, 710.84609, -10.760033], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[587712.41, -2239.2491, 6.0669492, -0.00061396855, 1.4918067e-07, -1.9231055e-11, 1.0619544e-15, 12832.104, -15.866396], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[8.3101392e+08, -642073.35, 202.02646, -0.03065092, 2.4869033e-06, -9.7059541e-11, 1.4375389e-15, 4938707, -1672.0997], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1978 v1 pt2 p207.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 56,
    label = "N2+",
    molecule =
"""
1 N u1 p0 c+1 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-34740.475, 269.62227, 3.1649164, -0.0021322398, 6.7304764e-06, -5.637305e-09, 1.621756e-12, 179000.44, 6.8329784], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-2845599, 7058.893, -2.8848864, 0.0030686771, -4.3616523e-07, 2.1025145e-11, 5.4119965e-16, 134038.85, 50.908974], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-3.7128298e+08, 313928.72, -96.03518, 0.015711933, -1.1750655e-06, 4.1444412e-11, -5.6218931e-16, -2217361.9, 843.6271], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """TPIS 1989 v1 pt1 p323;pt2 p200.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
NASA(polynomials=[NASAPolynomial(coeffs=[3.77541,-0.00206459,4.75752e-06,-3.15664e-09,6.7051e-13,180481,2.69322], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[3.58661,0.000253072,1.84778e-07,-4.55257e-11,3.26818e-15,180391,3.09584], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="tpis89")
[1] Lefkowitz 2022
""",
)

entry(
    index = 57,
    label = "N2-",
    molecule =
"""
1 N u1 p1 c-1 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.8826848, -0.0031924446, 8.5227838e-06, -7.3403746e-09, 2.2056815e-12, 16796.935, 3.1118052], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 3.1156753, 0.0014588688, -6.0173148e-07, 1.1348423e-10, -7.9658518e-15, 16859.058, 6.389856], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 58,
    label = "N2H+",
    molecule =
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c+1 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.80587,0.00875014,-1.48964e-05,1.32708e-08,-4.53576e-12,18906.2,4.29885], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[5.30541,0.00158633,-5.88189e-07,9.69277e-11,-5.88439e-15,18606.6,-2.7911], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="""T 9/11"""),
    shortDesc = u"""""",
    longDesc =
u"""
[1] Lefkowitz 2022
""",
)

entry(
    index = 59,
    label = "N2O+",
    molecule =
"""
1 N u1 p1 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-56286.132, 670.12104, 0.085579888, 0.015249873, -1.5279238e-05, 7.8312716e-09, -1.6477774e-12, 155732.24, 25.636431], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-29899.559, -1179.2895, 8.3000231, -0.00028864872, 5.7031726e-08, -5.9564953e-12, 2.8345581e-16, 164606.32, -22.872368], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Nitrous oxide ion. IP & cons: JANAF p1555, 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 60,
    label = "C",
    molecule =
"""
multiplicity 3
1 C u2 p1 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[649.50315, -0.96490109, 2.5046755, -1.281448e-05, 1.9801337e-08, -1.606144e-11, 5.3144834e-15, 85457.631, 4.7479243], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-128913.65, 171.95286, 2.6460444, -0.0003353069, 1.7420927e-07, -2.9028178e-11, 1.6421824e-15, 84105.978, 4.1300474], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[4.432528e+08, -288601.84, 77.371083, -0.0097152819, 6.6495953e-07, -2.2300788e-11, 2.8993887e-16, 2355273.4, -640.51232], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf:CJP v33 1955 p125. NSRDS-NBS 3 sec3 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 61,
    label = "C+",
    molecule =
"""
multiplicity 2
1 C u1 p1 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[2258.5359, -1.5745757, 2.5036377, -5.2028784e-06, 4.5169084e-09, -2.1814311e-12, 4.495047e-16, 216895.19, 4.3456995], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[12551.126, -34.118747, 2.5433832, -2.8051208e-05, 9.751642e-09, -1.7368554e-12, 1.2461919e-16, 217100.18, 4.0639135], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[561813.53, -6047.0589, 5.8845415, -0.00072118945, 6.8234841e-08, -2.5998786e-12, 3.6338684e-17, 258137.05, -22.800198], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Spec: NSRDS-NBS 3 sec3 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.79,20.79,20.79,20.79,20.79,20.79,20.79],'J/(mol*K)'),
        H298 = (1803.447,'kJ/mol'),
        S298 = (148.85,'J/(mol*K)'),
    )
C from primaryThermoData, mod H298 from ATcT
""",
)

entry(
    index = 62,
    label = "C-",
    molecule =
"""
1 C u3 p1 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[4.6712915, -0.0019861694, 2.5000086, -1.9767509e-08, 2.4789475e-11, -1.610664e-14, 4.2365068e-18, 70012.186, 4.8795701], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[4.2531757, 0.00057781865, 2.4999994, 2.8361362e-10, -7.3272534e-14, 9.4785078e-18, -4.8304873e-22, 70012.172, 4.8796242], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[12.23289, -0.0051961858, 2.5000013, -1.7434973e-10, 1.206609e-14, -4.2524198e-19, 5.9923333e-24, 70012.216, 4.8796084], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """JPCRD v14 n3 1985 p731.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 63,
    label = "CH",
    molecule =
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[22205.641, -340.53717, 5.5313864, -0.0057948964, 7.9694617e-06, -4.4658599e-09, 9.5962288e-13, 72403.905, -9.1076361], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2060733.8, -5396.1296, 7.8561879, -0.0007965758, 1.7642738e-07, -1.9763459e-11, 5.0302867e-16, 106219.24, -31.54718], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-8.0682676e+08, 457539.32, -98.438513, 0.012352286, -8.4855022e-07, 3.0403726e-11, -4.4002603e-16, -3595809.6, 895.33644], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & Hf0: TPIS,v2,pt2,1979.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 64,
    label = "CH+",
    molecule =
"""
1 C u0 p1 c+1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[30195.67, -461.80814, 6.2255643, -0.0077756137, 1.0944757e-05, -6.6754038e-09, 1.5652126e-12, 197244.49, -14.315014], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-7102008.5, 18283.327, -13.126755, 0.0061916422, -2.9093845e-07, -1.1342301e-10, 1.1059489e-14, 75409.732, 124.39691], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-3.1600336e+08, 143668.27, -11.084312, 0.00015622789, 4.9284324e-08, -2.8968355e-12, 4.9821937e-17, -1013663.4, 148.93356], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & IP: TPIS,v2,pt2,1991,p41.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 65,
    label = "CH-(S)",
    molecule =
"""
1 C u0 p2 c-1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.07,29.10,29.25,29.54,30.48,31.59,33.8],'J/(mol*K)'),
        H298 = (479.07,'kJ/mol'),
        S298 = (182.60,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH2 from DFT_QCI_thermo, mod H298 from ATcT
""",
)

entry(
    index = 66,
    label = "CH-(T)",
    molecule =
"""
multiplicity 3
1 C u2 p1 c-1 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.07,29.10,29.25,29.54,30.48,31.59,33.8],'J/(mol*K)'),
        H298 = (479.07,'kJ/mol'),
        S298 = (182.60,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH from DFT_QCI_thermo, mod H298 from ATcT

We don't know which is the ground state, (S) or (T), the H298 here probably relates only to the ground state
""",
)

entry(
    index = 67,
    label = "CH2",
    molecule =
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[35259.142, -336.76544, 4.5089369, 0.002521066, -5.3115109e-06, 6.6542131e-09, -2.610073e-12, 47377.255, -3.8074043], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2510415.9, -7953.9324, 12.388296, -0.0017759097, 3.2174003e-07, -3.0688634e-11, 1.2049006e-15, 96010.286, -61.559844], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf298: TRC tables.  Cons: JPCRD v17,1988,p279.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 68,
    label = "CH2+",
    molecule =
"""
multiplicity 2
1 C u1 p0 c+1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.90,36.02,37.30,38.65,41.36,43.93,48.87],'J/(mol*K)'),
        H298 = (1394.04,'kJ/mol'),
        S298 = (195.13,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH2 from primaryThermoData, mod H298 from ATcT

from [1] Lefkowitz 2022 (not used):
NASA(polynomials=[NASAPolynomial(coeffs=[3.23157,0.00499864,-7.43125e-06,6.75316e-09,-2.24398e-12,167227,3.42744], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[3.13583,0.00301498,-9.81603e-07,1.47279e-10,-8.34385e-15,167369,4.49067], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="cation T06/09"),
""",
)

entry(
    index = 69,
    label = "CH2-",
    molecule =
"""
multiplicity 2
1 C u1 p1 c-1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.90,36.02,37.30,38.65,41.36,43.93,48.87],'J/(mol*K)'),
        H298 = (328.59,'kJ/mol'),
        S298 = (195.13,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH2 from primaryThermoData, mod H298 from ATcT
""",
)

entry(
    index = 70,
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
        NASAPolynomial(coeffs=[-28772.861, 509.50561, 0.19907306, 0.013639652, -1.4345589e-05, 1.0139674e-08, -3.0284389e-12, 14110.987, 20.233886], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2760904.3, -9336.5528, 14.876986, -0.0014392277, 2.4439239e-07, -2.2238458e-11, 8.3915885e-16, 74847.648, -79.194893], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf298: TRC Apr30,1989. Cons: JPCRD V17,1988,p3526.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 71,
    label = "CH3+",
    molecule =
"""
1 C u0 p0 c+1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.16,42.31,45.41,48.34,53.79,58.7,67.82],'J/(mol*K)'),
        H298 = (1095.403,'kJ/mol'),
        S298 = (147.12,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH3 from DFT_QCI_thermo, mod H298 from ATcT

from [1] Lefkowitz 2022 (not used):
NASA(polynomials=[NASAPolynomial(coeffs=[4.73044,-0.0086626,3.12269e-05,-3.13569e-08,1.09957e-11,131270,-3.03198], Tmin=(200,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[2.41724,0.00640288,-2.21302e-06,3.46739e-10,-2.02365e-14,131474,6.78764], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(200,'K'), Tmax=(6000,'K'), comment='A12/04'),
""",
)

entry(
    index = 72,
    label = "CH3-",
    molecule =
"""
1 C u0 p1 c-1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.16,42.32,45.41,48.34,53.97,58.70,68.82],'J/(mol*K)'),
        H298 = (137.71,'kJ/mol'),
        S298 = (194.28,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH3 from DFT_QCI_thermo, mod H298 from ATcT
""",
)

entry(
    index = 73,
    label = "CH4",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-176654.57, 2785.4778, -12.019355, 0.039146259, -3.6116561e-05, 2.0183879e-08, -4.9557721e-12, -23310.116, 89.010754], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[3746265.7, -13888.513, 20.540298, -0.0019441969, 4.3238714e-07, -4.0610128e-11, 1.6431593e-15, 75659.887, -122.29777], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Cons & Hf298: TPIS v2,pt1,1991.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 74,
    label = "CH4+",
    molecule =
"""
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c+1
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.57082,0.0112865,-8.25312e-06,5.64491e-09,-1.92662e-12,137106,5.94507], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[3.56972,0.00822825,-2.9131e-06,4.65241e-10,-2.76281e-14,136771,0.684968], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="""CATION T 6/09"""),
    shortDesc = u"""""",
    longDesc =
u"""
VDW
[1] Lefkowitz 2022
""",
)

entry(
    index = 75,
    label = "CO",
    molecule =
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[14890.276, -292.22509, 5.7244584, -0.0081761369, 1.456886e-05, -1.0877332e-08, 3.0279055e-12, -13030.697, -7.8591793], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[461915.86, -1944.6857, 5.9166471, -0.00056642341, 1.3988026e-07, -1.787665e-11, 9.6208504e-16, -2465.7384, -13.874026], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[8.8685524e+08, -750028.54, 249.54445, -0.03956303, 3.2977321e-06, -1.318394e-10, 1.9989138e-15, 5701351.2, -2060.6796], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & Hf298: TPIS vo2,pt2,1979,p29.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 76,
    label = "CO+",
    molecule =
"""
1 C u1 p0 c0 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-21787.4, 128.88182, 3.7690229, -0.0034317139, 8.1938791e-06, -6.4637579e-09, 1.8037114e-12, 148234.83, 3.9904057], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[231681.66, -1057.6326, 4.5542023, 0.00044954693, -2.4894778e-07, 5.2675039e-11, -3.2894711e-15, 155505.2, -3.873443], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-3.0355572e+08, 239308.39, -70.34902, 0.011395363, -8.315064e-07, 2.8636681e-11, -3.8032198e-16, -1688590.8, 629.18933], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props and Hf0: TPIS,v2,pt2,1991,p22.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.10,29.27,29.68,30.29,31.69,32.9,34.90],'J/(mol*K)'),
        H298 = (1241.590,'kJ/mol'),
        S298 = (197.22,'J/(mol*K)'),
    )
CO from DFT_QCI_thermo, mod H298 from ATcT
""",
)

entry(
    index = 77,
    label = "HCO",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-11899.068, 215.16118, 2.7301839, 0.0018066215, 4.9841531e-06, -5.8144627e-09, 1.8696597e-12, 2905.7191, 11.367935], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[691133.57, -3643.2178, 9.5870849, -0.0011048918, 2.8294885e-07, -3.5379729e-11, 1.7396901e-15, 25356.227, -35.701987], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """HF: Chem.Phys.Let.v258,1996 p626. Cons:JPCRD v17,1988 p296.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 78,
    label = "HCO+",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c+1 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[118316.52, -1604.6676, 10.671712, -0.011688993, 1.6149493e-05, -9.9783142e-09, 2.3762971e-12, 106939.57, -38.203399], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1203649.2, -4460.9802, 9.932598, -0.00075407498, 1.3515824e-07, -1.3028334e-11, 5.2210607e-16, 126349.21, -41.066993], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-1518062.4, -552.66808, 7.610716, -1.1854358e-05, 7.0509671e-10, -2.1959367e-14, 2.7914707e-19, 98744.602, -23.054717], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """FORMYL ION.  JANAF, 12/70 INPUT.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.53, 36.33, 38.39, 40.50, 44.37, 47.45, 52.17],'J/(mol*K)'),
        H298 = (827.170,'kJ/mol'),
        S298 = (223.90,'J/(mol*K)'),
    )
HCO from DFT_QCI_thermo, mod H298 from ATcT
""",
)

entry(
    index = 79,
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
        NASAPolynomial(coeffs=[-28296.27, 676.19633, -2.2791656, 0.024233448, -2.2093516e-05, 1.2304588e-08, -3.1046731e-12, -2609.2915, 36.337858], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2224626.8, -9720.5655, 18.82482, -0.0019615228, 3.7907691e-07, -3.9646907e-11, 1.79238e-15, 58429.319, -100.41681], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf298: TPIS 1991. Cons: JPCRD v17 n2,1988,p419.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 80,
    label = "CH3O-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([227.7, 41.3, 48.7, 55.75, 61.95, 72.01, 79.65, 91.58],'J/(mol*K)'),
        H298 = (-130.19,'kJ/mol'),
        S298 = (227.70,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CH3O from DFT_QCI_thermo, mod H298 from ATcT
""",
)

entry(
    index = 81,
    label = "CH2OH",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-82331.72, 1300.5364, -4.1663783, 0.030339348, -3.4079341e-05, 2.1789488e-08, -5.7947306e-12, -8602.0101, 49.261769], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[2528592.3, -9235.952, 17.129085, -0.0013107553, 2.1364691e-07, -1.8710029e-11, 6.8497188e-16, 54183.956, -86.74895], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hydroxymethylene rad. Multiple refns.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 82,
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
        NASAPolynomial(coeffs=[-241663.75, 4032.1381, -20.464095, 0.069036793, -7.5989023e-05, 4.5981844e-08, -1.1586995e-11, -44332.57, 140.01389], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[3411560.8, -13454.975, 22.614046, -0.002141012, 3.7299975e-07, -3.4987633e-11, 1.3660221e-15, 56360.639, -127.78123], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Cons: JPCRD v6 n1,1977,p105. Hf298: TRC w5030,6/30/87.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 83,
    label = "CO2",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[49437.836, -626.42921, 5.3018134, 0.0025036006, -2.1247001e-07, -7.6914868e-10, 2.8499799e-13, -45281.899, -7.0487901], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[117696.94, -1788.8015, 8.2915435, -9.2247783e-05, 4.8696354e-09, -1.8920638e-12, 6.3306751e-16, -39083.45, -26.52684], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-1.5444062e+09, 1016836.1, -256.13771, 0.033693639, -2.1811579e-06, 6.9913249e-11, -8.8422121e-16, -8043128.5, 2254.1532], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & Hf298: TPIS v2,pt1,1991,p27.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 84,
    label = "CO2+",
    molecule =
"""
1 O u1 p1 c+1 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-73830.681, 1086.218, -2.7711503, 0.023184741, -2.5702554e-05, 1.4503461e-08, -3.3344993e-12, 107178.09, 40.549049], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-169511.5, -806.62623, 8.0028021, -0.00015770464, 2.5662055e-08, -2.403303e-12, 1.6768994e-16, 115438.45, -21.335503], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-83638025, 53323.286, -5.6191979, 0.0014911177, -7.5510131e-08, 1.7938567e-12, -1.6263711e-17, -311113.14, 96.717225], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Cons&Hf0: TPIS,v2,pt1,1991,p30.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 85,
    label = "CO3-",
    molecule =
"""
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 O u0 p3 c-1 {2,S}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.89975,0.0129851,-6.3595e-06,-2.85214e-09,2.4841e-12,-71227.6,12.7959], Tmin=(298.15,'K'), Tmax=(1000,'K')),
                               NASAPolynomial(coeffs=[7.34758,0.00268967,-1.04696e-06,1.7803e-10,-1.10419e-14,-72557.1,-10.6758], Tmin=(1000,'K'), Tmax=(6000,'K'))],
                  Tmin=(298.15,'K'), Tmax=(6000,'K'), comment="""gas T 1/12"""),
    shortDesc = u"""""",
    longDesc =
u"""
[1] Lefkowitz 2022
""",
)

entry(
    index = 86,
    label = "CN",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[3949.1017, -139.15739, 4.930776, -0.0063045947, 1.2568214e-05, -9.8781818e-09, 2.843103e-12, 52284.547, -2.7631146], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-2227976.1, 5040.6645, -0.21217945, 0.0013548812, 1.3259228e-07, -6.936934e-11, 5.4948916e-15, 17845.423, 32.825155], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-1.7947731e+08, 105433.14, -17.295989, 0.0021948638, -8.5088017e-08, 9.3184683e-13, 6.3582141e-18, -796247.65, 191.31124], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props:TPIS v2 pt2 1991. Hf:JPC v96 1992 p425.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 87,
    label = "CN+",
    molecule =
"""
1 C u0 p0 c+1 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-830280.1, 8775.572, -29.774032, 0.049768266, -1.3021968e-05, -2.0583094e-08, 1.1268327e-11, 170579.09, 203.98914], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-7153374.5, 18572.275, -10.845205, 0.0061066053, -1.1911936e-06, 1.1848337e-10, -4.7997769e-15, 92620.412, 113.53262], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-1.8129463e+08, 112880.45, -22.873084, 0.0034845857, -2.2097626e-07, 6.5797654e-12, -7.5564959e-17, -678420.86, 236.26335], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & Hf0: TPIS v2,pt2,1991,p203.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 88,
    label = "CN-",
    molecule =
"""
1 C u0 p1 c-1 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-45944.177, 426.66177, 2.3476244, -0.00018130252, 4.5662513e-06, -4.4679348e-09, 1.3671385e-12, 4566.9713, 11.327224], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[347882.46, -1621.4679, 5.6024587, -0.00039444824, 8.7316434e-08, -9.6847114e-12, 4.377564e-16, 16612.271, -11.699386], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Cons & Hf0: TPIS v2,pts1&2,1991.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 89,
    label = "CNN",
    molecule =
"""
multiplicity 3
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 N u1 p1 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-1347.0696, -138.4816, 4.5917604, 0.0042970207, -4.2657774e-06, 2.9405653e-09, -8.9101376e-13, 75445.829, 0.16090012], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[608532.72, -2582.4351, 8.6949262, -0.00018268968, -1.3603502e-08, 8.5766799e-12, -5.807255e-16, 90212.15, -27.213433], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """TPIS 1991. JPCRD v17,1988,p314. JCP v67 n2,1977,p664.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 90,
    label = "NCO",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[9507.9692, -195.73299, 4.2351279, 0.0039037192, 3.8551401e-07, -2.8535196e-09, 1.2345138e-12, 15569.626, 2.0425034], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[73929.298, -1617.2584, 8.5749195, -0.0003764555, 7.0382959e-08, -6.6865322e-12, 2.9889342e-16, 22894.071, -25.52768], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0: JCP,v99,1993 p4638. Cons: JPCRD v27 n2,1988 p269.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 91,
    label = "C2",
    molecule =
"""
multiplicity 3
1 C u1 p0 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[555956.76, -9980.0062, 66.815399, -0.17434117, 0.00024484936, -1.7034471e-07, 4.6844713e-11, 144586.39, -344.81889], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-968890.96, 3560.9902, -0.50635117, 0.0029450928, -7.1392891e-07, 8.6704701e-11, -4.0768167e-15, 76818.6, 33.398961], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[6316167.4, 13653.441, -3.9967232, 0.001937523, -1.5844182e-07, 5.5207655e-12, -7.2536097e-17, 9392.9053, 66.141268], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Gurvich et.al.1991,v2,pt1,pp9-14,pt2,pp8-9.8/93""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 92,
    label = "C2+",
    molecule =
"""
1 C u0 p0 c+1 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-99133.367, 1347.1581, -3.4767281, 0.016764132, -1.8658906e-05, 1.0911248e-08, -2.4348933e-12, 233545.54, 44.065937], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[3836171.5, -6241.7871, 2.7790004, 0.0060659088, -2.452804e-06, 3.8829441e-10, -2.1906404e-14, 285742.91, 0.73118006], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[49933414, -20176.83, 6.3430441, 0.00063688163, -1.0366839e-07, 4.9430055e-12, -7.988437e-17, 412115.61, -21.137308], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Gurvich et.al. Vol 2, Pt 2, 1991, p 10.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 93,
    label = "C2-",
    molecule =
"""
multiplicity 2
1 C u0 p1 c0 {2,D}
2 C u1 p1 c-1 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-118191.34, 1438.1712, -3.1960875, 0.014655293, -1.5455171e-05, 9.0611159e-09, -2.1359337e-12, 49653.294, 42.255474], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[4478264.2, -11541.809, 13.101797, -0.0018629584, 4.0148394e-08, 3.7090519e-11, -3.336619e-15, 132537.9, -69.762626], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Gurvich et.al. Vol 2, Pt 2,1991,p 12.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
Alternative source:
ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.95,44.12,41.14,37.71,35.30,35.67,33.22],'J/(mol*K)'),
        H298 = (510.98,'kJ/mol'),
        S298 = (219.03,'J/(mol*K)'),
    )
C2 from GAV, mod H298 from ATcT
""",
)

entry(
    index = 94,
    label = "Ca",
    molecule =
"""
1 Ca u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 20638.928, 4.3845483], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[7547341.2, -21486.427, 25.308496, -0.011037737, 2.2932496e-06, -1.2090754e-10, -4.0153333e-15, 158586.23, -160.9513], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.2917816e+09, -1608863, 431.24664, -0.05396509, 3.5318562e-06, -1.1644038e-10, 1.5271342e-15, 12586514, -3692.1016], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf:CODATA 1989. JPCRD v14 sup.2 1985.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 95,
    label = "Ca+",
    molecule =
"""
1 Ca u1 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 92324.178, 5.077675], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[3747070.8, -11747.077, 16.72547, -0.0083347977, 2.3945933e-06, -2.9882435e-10, 1.356563e-14, 166432.91, -95.828213], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[9.1171284e+08, -622042.85, 168.37411, -0.021408627, 1.4529477e-06, -4.9207909e-11, 6.5753692e-16, 4959472.1, -1422.6007], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Spec:JPCRD v14 sup.2 1985.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 96,
    label = "CaH",
    molecule =
"""
1 Ca u1 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-45137.822, 762.94292, -1.2808742, 0.013187747, -1.4815953e-05, 8.5365732e-09, -1.9899589e-12, 23003.788, 30.534215], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-2696952.5, 8607.0598, -7.0274548, 0.0074679163, -2.3186107e-06, 3.4230724e-10, -1.8926798e-14, -27738.191, 78.45822], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Props & D0: TPIS 1996 pt1 p447, pt2 p353.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 97,
    label = "CaO",
    molecule =
"""
1 Ca u0 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[38897.331, -483.56774, 5.0777133, 0.00030762352, -1.1597599e-06, 8.4934333e-10, -1.4953334e-13, 5937.6435, -3.9553207], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-49131062, 149586.6, -168.16541, 0.093819503, -2.4555294e-05, 3.0749807e-09, -1.4859142e-13, -946151.17, 1235.6948], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-3.5040551e+08, 208321.24, -39.782093, 0.0050392687, -3.2207077e-07, 1.0573794e-11, -1.3960442e-16, -1662378.7, 393.44919], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & D0: TPIS 1996 pt1 p443, pt2 p349.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 98,
    label = "CaO+",
    molecule =
"""
1 Ca u0 p0 c0 {2,D}
2 O u1 p1 c+1 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[109806.03, -1459.9924, 9.8807779, -0.0091575646, 8.7075826e-06, -4.3904111e-09, 9.2648547e-13, 91500.573, -30.099477], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[939784.31, -2993.3622, 8.3361918, -0.0023032951, 7.3739675e-07, -1.0528883e-10, 5.2571384e-15, 102809.84, -24.615478], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[-76486453, 17392.453, 8.4202887, -0.0011683868, 8.4136849e-08, -2.7707993e-12, 3.5694744e-17, -86434.898, -23.765131], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Props & Hf0: TPIS 1996 pt1 p445, pt2 p351.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 99,
    label = "CaOH",
    molecule =
"""
1 Ca u1 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[46200.289, -928.56728, 9.1758288, -0.0039628288, 2.5054473e-06, 3.8520682e-11, -3.3527785e-13, -17980.097, -25.337049], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1979973, -5598.881, 11.513487, -0.0016682647, 3.3125739e-07, -1.7890566e-11, -3.5807164e-16, 13401.968, -46.460843], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0 & cons: TPIS v3 pt1 p451; pt2 p355.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 100,
    label = "CaOH+",
    molecule =
"""
1 Ca u0 p0 c+1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[48843.427, -983.24151, 9.610183, -0.0052043607, 4.2630498e-06, -1.1975909e-09, 9.0284119e-15, 47950.563, -28.270773], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[863761.54, -2347.302, 7.9819112, 0.00010031609, -6.2400742e-08, 1.0195409e-11, -5.6989253e-16, 58305.801, -21.521819], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0 & cons: TPIS v3 pt1 p452; pt2 p356.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 101,
    label = "Ca(OH)2",
    molecule =
"""
1 O u0 p2 c0 {2,S} {4,S}
2 Ca u0 p0 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[83892.575, -1791.9021, 16.21891, -0.0078408572, 5.0951116e-06, -6.9554875e-11, -6.1321526e-13, -66004.056, -60.709139], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1721854.9, -4702.2177, 13.969477, 0.00019837914, -1.2430506e-07, 2.0334024e-11, -1.1371578e-15, -44437.613, -52.874449], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0 & cons: TPIS v3 pt1 p455; pt2 p358.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 102,
    label = "K",
    molecule =
"""
1 K u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[9.6651439, -0.14580595, 2.5008659, -2.6012193e-06, 4.1873066e-09, -3.4397221e-12, 1.131569e-15, 9959.4935, 5.0358223], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-3566422.4, 10852.898, -10.541349, 0.0080098013, -2.696681e-06, 4.7152942e-10, -2.9768974e-14, -58753.37, 97.385512], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[9.2057866e+08, -693530.03, 191.12708, -0.023059317, 1.4302949e-06, -4.409335e-11, 5.3667692e-16, 5395082.2, -1622.1588], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf: CODATA 89. Spec: JPCRD v14 sup2 1985 p11.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 103,
    label = "K+",
    molecule =
"""
1 K u0 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 61075.169, 4.3474044], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 61075.169, 4.3474044], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[21779012, -14150.766, 6.2489543, -0.00051874368, 3.9596407e-08, -1.5843355e-12, 2.6035589e-17, 172275.36, -27.81729], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """JPCRD v14 sup2 1985 p26.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 104,
    label = "K-",
    molecule =
"""
1 K u0 p1 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 3394.1507, 4.3474465], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 3394.1507, 4.3474465], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 3394.1507, 4.3474465], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """JPCRD v14 n3 1985 p731.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 105,
    label = "KCN",
    molecule =
"""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p1 c0 {1,T}
3 K u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 5.0810711, 0.0055265956, -9.1157121e-06, 8.4488817e-09, -3.0051548e-12, 7866.2161, 0.18633305], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.800712, 0.0017200786, -7.0791074e-07, 1.3199247e-10, -9.1908323e-15, 7727.2628, -3.158848], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 106,
    label = "KH",
    molecule =
"""
1 K u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.8157756, 0.003987106, -3.3410548e-06, 8.8602942e-10, 1.1402847e-13, 13805.838, 6.725179], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 3.9603386, 0.00072190323, -2.6918715e-07, 5.26173e-11, -3.7872683e-15, 13501.837, 0.85534508], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 107,
    label = "KO",
    molecule =
"""
1 O u1 p2 c0 {2,S}
2 K u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.7410778, 0.0031242017, -4.8020039e-06, 3.4660605e-09, -9.3599791e-13, 7336.8714, 6.5669239], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.4244778, 0.00019936155, -3.7128837e-08, 7.13083e-12, -5.0369687e-16, 7205.2331, 3.3076685], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 108,
    label = "KO-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 K u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.708366, 0.003237648, -4.96905e-06, 3.5728846e-09, -9.6080268e-13, -17818.607, 5.3166259], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.4201084, 0.00020124266, -3.9330996e-08, 7.5598511e-12, -5.3442275e-16, -17956.109, 1.9200041], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 109,
    label = "KOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 K u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[17706.842, -615.32052, 8.6840757, -0.0039628495, 3.4086506e-06, -9.6019722e-10, 8.494055e-15, -26779.033, -21.744957], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[891727.19, -2334.1791, 7.9725787, 0.00010388632, -6.3158935e-08, 1.0279381e-11, -5.7366858e-16, -14436.965, -20.764014], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """JPCRD v26 n4 1997 p1031.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 110,
    label = "KOH+",
    molecule =
"""
1 O u1 p1 c+1 {2,S} {3,S}
2 K u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 4.4325167, 0.0084631625, -1.4247855e-05, 1.1106625e-08, -3.1563612e-12, 58292.632, 2.8733457], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.680614, 0.0012120951, -3.3447117e-07, 4.1727932e-11, -1.8793913e-15, 58167.602, -2.5541514], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 111,
    label = "K2",
    molecule =
"""
1 K u0 p0 c0 {2,S}
2 K u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[19500.255, -396.25241, 7.4803064, -0.011078682, 2.251547e-05, -2.1026449e-08, 6.8438175e-12, 15298.901, -11.333519], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-4205896.4, 11705.709, -5.4923802, 0.002862953, -5.6962453e-07, 5.9491285e-11, -2.5417364e-15, -62729.196, 80.551743], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """JANAF tabulated data.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 112,
    label = "Li",
    molecule =
"""
1 Li u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 18413.902, 2.447623], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1125610.7, -3463.5367, 6.5666119, -0.0022609834, 5.9222892e-07, -6.2816351e-11, 2.8849482e-15, 40346.374, -26.559182], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.6043526e+09, -1521952.2, 345.44005, -0.037796748, 2.2224201e-06, -6.6915708e-11, 8.0880236e-16, 12177918, -3006.6802], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf:CODATA1989. NSRDS-NBS 35 1971;NSRDS-NBS 34 1970.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 113,
    label = "Li+",
    molecule =
"""
1 Li u0 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 81727.246, 1.7543572], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 81727.246, 1.7543572], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 81727.246, 1.7543572], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Cp/R=2.5. IP: Moore, NSRDS-NBS 35 v1 1971""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 114,
    label = "Li-",
    molecule =
"""
multiplicity 1
1 Li u0 p1 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 10496.987, 1.7545943], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 10496.987, 1.7545943], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 10496.987, 1.7545943], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """JPCRD v14 n3 1985 p731.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 115,
    label = "LiH",
    molecule =
"""
1 Li u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.4209486, -0.00068067366, 5.6527381e-06, -6.2180348e-09, 2.1531755e-12, 15884.945, 1.0657419], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 3.5884297, 0.0010727691, -4.0194588e-07, 7.3828557e-11, -4.9269644e-15, 15717.625, -0.37503897], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 116,
    label = "LiN",
    molecule =
"""
1 N u2 p1 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.88943, 0.0052212534, -6.5969021e-06, 3.7288997e-09, -7.2355143e-13, 39216.323, 7.2888715], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.2258077, 0.00039667187, -1.2493993e-07, 2.3174759e-11, -1.5851917e-15, 38916.952, 0.70085148], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 117,
    label = "LiO",
    molecule =
"""
1 O u1 p2 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.8389007, 0.0051538626, -6.3082382e-06, 3.4114385e-09, -6.1631343e-13, 9088.4314, 7.9131179], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.1876205, 0.00041186574, -1.4520296e-07, 2.725307e-11, -1.8864775e-15, 8779.5259, 1.231426], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 118,
    label = "LiO-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.8515866, 0.005016988, -5.9547475e-06, 3.0399451e-09, -4.7872969e-13, -9077.8076, 6.4594707], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.1810217, 0.00041785, -1.5024845e-07, 2.8397732e-11, -1.9789181e-15, -9384.9702, -0.14239234], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 119,
    label = "LiOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[4573.9173, -103.09121, 4.2723881, 0.0084652695, -1.3861556e-05, 1.1011049e-08, -3.2912631e-12, -28487.306, -0.87746614], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[850066.92, -2430.5197, 8.0552938, 6.8967069e-05, -5.5274744e-08, 9.3684028e-12, -5.3139654e-16, -13659.081, -24.575829], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """JPCRD v25 n4,1996 p1211.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 120,
    label = "LiOH+",
    molecule =
"""
1 O u1 p1 c+1 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.6379739, 0.010897154, -1.722967e-05, 1.2667927e-08, -3.4165259e-12, 92161.193, 3.6377609], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.5329269, 0.0013777931, -4.0659309e-07, 5.559091e-11, -2.8604624e-15, 91888.579, -4.9935927], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 121,
    label = "LiON",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u2 p1 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.6701164, 0.0072568177, -5.8681146e-06, 1.1628312e-09, 4.2704122e-13, 20271.703, 6.6824951], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.8123496, 0.0012870626, -5.466771e-07, 1.0314987e-10, -7.1930447e-15, 19692.302, -4.3447056], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 122,
    label = "Li2",
    molecule =
"""
1 Li u0 p0 c0 {2,S}
2 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[6778.4865, -224.62066, 5.2960379, -0.0012724133, 1.2058456e-06, -9.8186856e-11, -2.4166984e-13, 25736.382, -6.86926], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[37676452, -118574.71, 148.21677, -0.083785319, 2.4249197e-05, -3.2758202e-09, 1.652e-13, 772307.17, -1021.6973], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """JANAF tabulated data.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 123,
    label = "Li2O",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 Li u0 p0 c0 {1,S}
3 Li u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.9721708, 0.0092460921, -9.3596149e-06, 3.463916e-09, -7.565888e-14, -21596.988, 2.5523041], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 6.6198748, 0.00096879448, -4.1490506e-07, 7.8637337e-11, -5.4969292e-15, -22255.325, -10.821559], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 124,
    label = "Li2O2",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 Li u0 p0 c0 {1,S}
4 Li u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 5.5375232, 0.017344223, -2.7197971e-05, 1.9305629e-08, -5.1207957e-12, -31402.044, -2.7683129], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 9.527526, 0.00053021013, -2.3005862e-07, 4.4030831e-11, -3.1018702e-15, -32182.484, -21.859112], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 125,
    label = "Mg",
    molecule =
"""
1 Mg u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 16946.588, 3.6343301], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-536483.16, 1973.7096, -0.36337769, 0.0020717956, -7.7380517e-07, 1.3592778e-10, -7.7668984e-15, 4829.1881, 23.39105], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2.1660126e+09, -1008355.7, 161.968, -0.0087901303, -1.925691e-08, 1.7250452e-11, -4.2349461e-16, 8349525.9, -1469.3553], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf:CODATA 1989. Spec:JPCRD v20 n1 1991 p83-152.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 126,
    label = "Mg+",
    molecule =
"""
1 Mg u1 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 106422.34, 4.3274435], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-19147.588, 48.773479, 2.4576627, 1.2181047e-05, 1.8972617e-09, -1.5804338e-12, 2.1357322e-16, 106102.24, 4.6464429], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[4.0159496e+08, -228159.17, 54.217457, -0.0059830172, 3.6571891e-07, -1.0207377e-11, 1.0242029e-16, 1932464, -448.01578], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Spec:JPCRD v20 n1 1991 p97.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 127,
    label = "MgH",
    molecule =
"""
1 Mg u1 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[-49586.791, 750.02787, -0.64420475, 0.009826301, -8.7898224e-06, 3.8233535e-09, -6.0037258e-13, 23022.794, 26.571653], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-100574.86, 1952.8901, -1.3171915, 0.0056036658, -2.137335e-06, 3.3248805e-10, -1.8246727e-14, 15985.828, 34.312332], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Props & D0: TPIS 1996 pt1 p401, pt2 p320.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 128,
    label = "MgN",
    molecule =
"""
1 N u1 p1 c0 {2,D}
2 Mg u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.8894549, 0.0051757175, -6.5849016e-06, 3.7218933e-09, -7.2305964e-13, 33681.058, 9.2975895], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.2214417, 0.0003648924, -1.299573e-07, 2.441894e-11, -1.6917759e-15, 33382.931, 2.732052], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 129,
    label = "MgO",
    molecule =
"""
1 Mg u0 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[351365.97, -5287.1972, 33.820601, -0.084004896, 0.00012100162, -7.630795e-08, 1.7010229e-11, 27906.795, -162.48862], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[-15867384, 34204.681, -17.740877, 0.0070049631, -1.1041382e-06, 8.9574885e-11, -3.0525136e-15, -230050.44, 173.89845], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[2290059, -20734.996, 14.4415, -0.0014906099, 1.0521193e-07, -3.5230306e-12, 4.6131118e-17, 149021.88, -80.072817], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """D0,Props: TPIS 1996 pt1 p398, pt2 p318.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 130,
    label = "MgOH",
    molecule =
"""
1 Mg u1 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[38398.516, -736.73836, 7.9206645, -0.00059509406, -2.1129412e-06, 3.2282821e-09, -1.2141593e-12, -13923.262, -19.160781], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[664866.47, -1770.7504, 7.2699993, 0.00053368428, -1.9808944e-07, 3.0256771e-11, -1.5548495e-15, -6149.1146, -16.71027], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0 & cons: TPIS v3 pt1 p404; pt2 p322.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 140,
    label = "MgOH+",
    molecule =
"""
1 Mg u0 p0 c+1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 1.7831421, 0.019228527, -3.3503143e-05, 2.7491364e-08, -8.5151007e-12, 69150.584, 11.930524], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.2824479, 0.0016640437, -5.4016651e-07, 8.3467824e-11, -5.0036168e-15, 68595.816, -4.1503886], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 141,
    label = "Mg(OH)2",
    molecule =
"""
1 O u0 p2 c0 {2,S} {4,S}
2 Mg u0 p0 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[52458.947, -1289.0564, 13.893276, -0.00078066937, -4.1512572e-06, 6.109473e-09, -2.2741388e-12, -62950.891, -50.153533], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[1713709.3, -4730.0054, 14.48926, 0.00019078199, -1.2268341e-07, 2.0153438e-11, -1.1289933e-15, -38877.247, -58.404981], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Hf0 & cons: TPIS v3 pt1 p407; pt2 p324.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 142,
    label = "Mg2",
    molecule =
"""
1 Mg u0 p0 c0 {2,D}
2 Mg u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[4545.1956, 411.585, 0.48411962, 0.0048919697, -6.3955368e-06, 4.2997645e-09, -1.1646244e-12, 31816.418, 26.404321], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[30382.25, 59.452405, 2.3527067, 0.00013785379, -5.895692e-08, 1.1040453e-11, -6.5588683e-16, 33510.366, 15.881774], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Props and D0: TPIS 1996 pt1 p393 pt2 p316.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 143,
    label = "Na",
    molecule =
"""
1 Na u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 12183.829, 4.2440282], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[952572.34, -2623.8073, 5.1625966, -0.0012102186, 2.3063018e-07, -1.2495978e-11, 7.2267712e-16, 29129.636, -15.197171], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[1.5925334e+09, -971783.67, 223.8444, -0.023809306, 1.3520181e-06, -3.9369711e-11, 4.6306891e-16, 7748677.3, -1939.6155], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Hf:CODATA 1989 p27. Levels:JPCRD v10 n1 p153 1981""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 144,
    label = "Na+",
    molecule =
"""
1 Na u0 p0 c+1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 72565.371, 3.5508452], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 72565.371, 3.5508452], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[34012.03, -21.377746, 2.5054439, -7.1866317e-07, 5.1887964e-11, -1.9445116e-15, 2.9593551e-20, 72734.136, 3.5039042], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """Spec:JPCRD v10 n1 1981 p153.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 145,
    label = "Na-",
    molecule =
"""
1 Na u0 p1 c-1
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 5082.1997, 3.5509168], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 5082.1997, 3.5509168], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 2.5, 0, 0, 0, 0, 5082.1997, 3.5509168], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
        ],
        Tmin = (298.15, 'K'),
        Tmax = (20000.0, 'K'),
    ),
    shortDesc = """JPCRD v14 n3 1985 p731.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 146,
    label = "NaCN",
    molecule =
"""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p1 c0 {1,T}
3 Na u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 4.9772558, 0.0053225937, -7.5552441e-06, 6.1839794e-09, -2.0071427e-12, 9673.149, -0.38822558], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.7989775, 0.0016827946, -6.7437924e-07, 1.2234502e-10, -8.2966091e-15, 9493.3444, -4.3442787], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 147,
    label = "NaH",
    molecule =
"""
1 Na u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.120395, 0.0013996217, 2.2141234e-06, -3.9950795e-09, 1.6726178e-12, 13940.065, 4.3945613], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 3.8130579, 0.000856438, -3.1226816e-07, 5.8502471e-11, -4.0513924e-15, 13683.062, 0.48416821], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 148,
    label = "NaO",
    molecule =
"""
1 O u1 p2 c0 {2,S}
2 Na u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.4421007, 0.0041617241, -6.3118368e-06, 4.4479199e-09, -1.1720486e-12, 8901.1477, 6.9503254], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.3924158, 0.00021320574, -4.5220598e-08, 7.9751821e-12, -5.1735989e-16, 8711.8995, 2.3880897], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 149,
    label = "NaO-",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 Na u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 3.4186855, 0.0042117382, -6.3104646e-06, 4.3873515e-09, -1.1372639e-12, -15752.234, 5.6685565], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 4.3868008, 0.00022344672, -4.8212472e-08, 8.5720862e-12, -5.6094334e-16, -15946.268, 1.0136349], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 150,
    label = "NaOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 Na u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[34420.091, -792.31841, 8.9979172, -0.0040798122, 3.065747e-06, -5.1189688e-10, -1.5410713e-13, -20869.528, -25.105813], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[875381.55, -2342.5216, 7.9784764, 0.00010164209, -6.2684568e-08, 1.0227059e-11, -5.7132413e-16, -9509.8565, -22.023152], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """JPCRD 1996 v25 n4 p1211.""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 151,
    label = "NaOH+",
    molecule =
"""
1 O u1 p1 c+1 {2,S} {3,S}
2 Na u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 4.3505204, 0.0087465015, -1.4642673e-05, 1.1351501e-08, -3.2110026e-12, 79946.399, 2.3448408], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.6688547, 0.001225393, -3.4029563e-07, 4.2853268e-11, -1.959376e-15, 79806.514, -3.4246826], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 152,
    label = "Na2",
    molecule =
"""
1 Na u0 p0 c0 {2,S}
2 Na u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 4.1156826, 0.0025290404, -5.6216864e-06, 6.4617167e-09, -2.7512831e-12, 15782.462, 3.6867245], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 5.962019, -0.0010604951, -4.3927977e-07, 3.0517481e-10, -3.3948882e-14, 14999.093, -6.6961363], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
        ],
        Tmin = (200.0, 'K'),
        Tmax = (6000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

entry(
    index = 153,
    label = "Na2O",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 Na u0 p0 c0 {1,S}
3 Na u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
        NASAPolynomial(coeffs=[0, 0, 4.7787177, 0.0099487716, -1.4814456e-05, 1.0003239e-08, -2.5137874e-12, -6736.0206, 1.7994763], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
        NASAPolynomial(coeffs=[0, 0, 7.1470582, 0.00039833099, -1.7408911e-07, 3.3565162e-11, -2.3810801e-15, -7219.1261, -9.6348105], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
        ],
        Tmin = (300.0, 'K'),
        Tmax = (5000.0, 'K'),
    ),
    shortDesc = """Parsed from text""",
    longDesc =
"""
Converted from NASA 9-coefficient format.
""",
)

# entry(
#     index = 154,
#     label = "Si",
#     molecule =
# """
# multiplicity 5
# 1 Si u4 p0 c0
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[98.361408, 154.65445, 1.8764367, 0.001320638, -1.5297201e-06, 8.9505628e-10, -1.9528735e-13, 52635.103, 9.6982889], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-616929.89, 2240.6839, -0.44486193, 0.0017100563, -4.1077142e-07, 4.5588848e-11, -1.8895154e-15, 39535.588, 26.796681], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[-9.2865489e+08, 544398.99, -120.67397, 0.013596627, -7.6064987e-07, 2.1497461e-11, -2.4741168e-16, -4293792.1, 1086.3828], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """Hf:CODATA1989. Levels:NIST data version1.1 [Online]1997.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 155,
#     label = "Si+",
#     molecule =
# """
# 1 Si u3 p0 c+1
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-43297.919, 679.58945, 0.22570461, 0.0041186005, -4.2348816e-06, 2.3279956e-09, -5.3183881e-13, 145203.98, 19.346505], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[59193.902, -48.56731, 2.556312, -3.5033972e-05, 1.1902988e-08, -2.0829238e-12, 1.471452e-16, 149143.14, 5.2442671], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[-13642233, 7022.7772, 1.23301, 0.00012117894, -1.4552236e-08, 1.5302935e-12, -3.8043505e-17, 91492.381, 17.083378], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (298.15, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """JPCRD v12 n2 1983 p323.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 156,
#     label = "Si-",
#     molecule =
# """
# 1 Si u3 p1 c-1
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-794.01467, 5.5674184, 2.4998372, -9.4813945e-05, 3.1712469e-07, -4.1913232e-10, 2.0359244e-13, 36364.434, 5.2701198], Tmin=(298.15,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-6162070.1, 18833.104, -18.993025, 0.011110217, -2.5357902e-06, 2.6999629e-10, -1.1050629e-14, -83140.893, 159.52983], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
#         NASAPolynomial(coeffs=[-54295180, 32971.057, -2.4705797, 0.00039665776, -1.7641413e-08, 4.1157698e-13, -3.9043694e-18, -231588.15, 52.266018], Tmin=(6000.0,'K'), Tmax=(20000.0,'K'))
#         ],
#         Tmin = (298.15, 'K'),
#         Tmax = (20000.0, 'K'),
#     ),
#     shortDesc = """Spec: JANAF 3/83. EA:JPCRD v14 n3 1985 p731.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 157,
#     label = "SiC",
#     molecule =
# """
# 1 Si u1 p0 c0 {2,T}
# 2 C u1 p0 c0 {1,T}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-6223.3309, 314.17905, 0.38931308, 0.011875075, -1.6392772e-05, 1.1318082e-08, -3.0453242e-12, 86062.277, 23.101645], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-62688.06, 720.98369, 2.1628797, 0.0022012996, -6.5694666e-07, 9.1771103e-11, -4.9691667e-15, 83212.258, 16.016731], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """Hf0,Props: TPIS 1991 V2 pt1 p301; pt2 p265.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 158,
#     label = "SiC2",
#     molecule =
# """
# 1 C u0 p0 c0 {2,S} {3,T}
# 2 Si u0 p1 c0 {1,S} {3,S}
# 3 C u0 p0 c0 {1,T} {2,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-41196.584, 686.97907, 0.02358757, 0.015329471, -1.4356019e-05, 6.3753386e-09, -1.0592417e-12, 71308.886, 28.288628], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[7026788, -24661.186, 39.154203, -0.020028664, 6.3073044e-06, -8.8483154e-10, 4.5305132e-14, 226730.6, -236.65987], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS, vol 2, part 1,1991 p246,302-4.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 159,
#     label = "SiH",
#     molecule =
# """
# 1 Si u1 p1 c0 {2,S}
# 2 H u0 p0 c0 {1,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-2665.6005, 29.246113, 4.2101471, -0.0047801241, 1.1122309e-05, -9.2316947e-09, 2.7476276e-12, 43046.687, 0.92113302], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-1470883.2, 3710.0351, -0.08805992, 0.0023752958, -4.7819142e-07, 4.8399081e-11, -1.7501289e-15, 18969.663, 29.797585], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 v2 pt1 p257; pt2 p234.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 160,
#     label = "SiH+",
#     molecule =
# """
# 1 Si u0 p1 c+1 {2,S}
# 2 H u0 p0 c0 {1,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[0, 0, 3.7292588, -0.0017881611, 4.2469257e-06, -2.558013e-09, 4.063374e-13, 136970.71, 1.5838731], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[0, 0, 2.9828595, 0.0015455222, -5.9038555e-07, 1.05174e-10, -6.8220234e-15, 137079.54, 5.0403501], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
#         ],
#         Tmin = (300.0, 'K'),
#         Tmax = (5000.0, 'K'),
#     ),
#     shortDesc = """Parsed from text""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 161,
#     label = "SiH2",
#     molecule =
# """
# 1 Si u0 p1 c0 {2,S} {3,S}
# 2 H u0 p0 c0 {1,S}
# 3 H u0 p0 c0 {1,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-195834.11, 2758.775, -9.908961, 0.027631746, -1.0306554e-05, -9.0506591e-09, 5.8927008e-12, 18333.442, 81.858894], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-2005373.3, 3817.5633, 4.1581256, 0.0010349776, -2.0580471e-07, 2.278902e-11, -1.0643185e-15, 3984.8238, 4.8362727], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 v2 pt1 p260; pt2 p235.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 162,
#     label = "SiH3",
#     molecule =
# """
# 1 Si u1 p0 c0 {2,S} {3,S} {4,S}
# 2 H u0 p0 c0 {1,S}
# 3 H u0 p0 c0 {1,S}
# 4 H u0 p0 c0 {1,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[4341.1428, 227.71851, 0.65082503, 0.012214386, -4.3476043e-06, -1.7749168e-09, 1.1841914e-12, 22599.938, 19.683475], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[605632.12, -4721.2541, 13.291295, -0.0012568249, 2.6882859e-07, -3.0107416e-11, 1.3709459e-15, 49744.206, -61.405031], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 v2 pt1 p261; pt2 p236.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 163,
#     label = "SiH4",
#     molecule =
# """
# 1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
# 2 H u0 p0 c0 {1,S}
# 3 H u0 p0 c0 {1,S}
# 4 H u0 p0 c0 {1,S}
# 5 H u0 p0 c0 {1,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[78730.746, -552.62209, 2.4990293, 0.014420919, -8.4666862e-06, 2.7258364e-09, -5.4357706e-13, 6269.7313, 4.9650001], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[1290384.9, -7813.4308, 18.288563, -0.0019756505, 4.156596e-07, -4.5968886e-11, 2.0728601e-15, 47669.066, -98.017294], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """Silane. TPIS 1991 v2 pt1 p263 pt 2 p237.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 164,
#     label = "SiN",
#     molecule =
# """
# 1 Si u1 p0 c0 {2,T}
# 2 N u0 p1 c0 {1,T}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-14646.722, 137.49935, 3.6785086, -0.0061584992, 2.3094171e-05, -2.2944615e-08, 7.3956657e-12, 46732.13, 6.4945655], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-2932685.1, 5853.6886, 1.3214517, 0.0012583293, -3.7738864e-07, 6.887761e-11, -4.1898426e-15, 6527.1488, 25.531459], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 V2 pt1 p295; pt2 p261.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 165,
#     label = "SiO",
#     molecule =
# """
# 1 Si u0 p1 c-1 {2,T}
# 2 O u0 p1 c+1 {1,T}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-47227.711, 806.31376, -1.6369761, 0.014542755, -1.723202e-05, 1.0423973e-08, -2.5593653e-12, -16665.859, 33.557957], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-176513.42, -31.991771, 4.4774419, 4.5917647e-06, 3.5581432e-08, -1.3270126e-11, 1.6132533e-15, -13508.424, -0.83869573], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """Hf0,Props: TPIS 1991 V2 pt1 p247; pt2 p227""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 166,
#     label = "SiO2",
#     molecule =
# """
# 1 O u0 p2 c0 {2,D}
# 2 Si u0 p0 c0 {1,D} {3,D}
# 3 O u0 p2 c0 {2,D}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-33629.488, 473.40789, 0.23097707, 0.018502308, -2.2427867e-05, 1.3649816e-08, -3.351935e-12, -42264.875, 22.958032], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-146403.12, -626.14411, 7.9645637, -0.00018541191, 4.0952147e-08, -4.6972068e-12, 2.1780543e-16, -37918.348, -20.452854], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 V2 pt1 p256; pt2 p233.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 167,
#     label = "Si2",
#     molecule =
# """
# 1 Si u1 p0 c0 {2,T}
# 2 Si u1 p0 c0 {1,T}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[12375.962, -102.49044, 4.3548485, 0.0012810633, -2.5319916e-06, 2.2656942e-09, -7.0012901e-13, 69069.428, 3.2511252], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[1370060.7, -4207.06, 9.3374329, -0.0027492172, 9.586346e-07, -1.3724497e-10, 6.7650281e-15, 95108.845, -31.683852], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 v2 pt1 p240; pt2 p225.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 168,
#     label = "Si2C",
#     molecule =
# """
# 1 Si u0 p1 c0 {2,D}
# 2 C u0 p0 c0 {1,D} {3,D}
# 3 Si u0 p1 c0 {2,D}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-4553.6124, 131.48234, 2.4690973, 0.012765217, -1.6569097e-05, 1.0652869e-08, -2.7391792e-12, 64700.485, 14.688442], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-125436.66, -341.27469, 7.2541967, -0.00010167177, 2.2483009e-08, -2.5804216e-12, 1.1968838e-16, 66079.113, -11.460961], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 V2 pt1 p304; pt2 p267.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 169,
#     label = "Si2N",
#     molecule =
# """
# 1 Si u0 p1 c0 {2,D}
# 2 N u0 p0 c+1 {1,D} {3,D}
# 3 Si u1 p1 c-1 {2,D}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[0, 0, 3.6686735, 0.01130184, -1.3637119e-05, 7.168805e-09, -1.237831e-12, 46318.083, 7.1227096], Tmin=(300.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[0, 0, 6.6709912, 0.00091917882, -3.951713e-07, 7.4397145e-11, -5.0284691e-15, 45620.154, -7.7982777], Tmin=(1000.0,'K'), Tmax=(5000.0,'K'))
#         ],
#         Tmin = (300.0, 'K'),
#         Tmax = (5000.0, 'K'),
#     ),
#     shortDesc = """Parsed from text""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
#
# entry(
#     index = 170,
#     label = "Si3",
#     molecule =
# """
# 1 Si u0 p1 c0 {2,S} {3,S}
# 2 Si u0 p1 c0 {1,S} {3,S}
# 3 Si u0 p1 c0 {1,S} {2,S}
# """,
#     thermo = NASA(
#         polynomials = [
#         NASAPolynomial(coeffs=[-11142.944, 157.59102, 2.4860675, 0.016316545, -2.2082613e-05, 1.3720198e-08, -3.2623487e-12, 73282.479, 15.881192], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
#         NASAPolynomial(coeffs=[-1699325.8, 4697.6153, 2.6184211, 0.0019589598, -2.5808132e-07, 6.0985659e-12, 6.0889865e-16, 42780.448, 25.863805], Tmin=(1000.0,'K'), Tmax=(6000.0,'K'))
#         ],
#         Tmin = (200.0, 'K'),
#         Tmax = (6000.0, 'K'),
#     ),
#     shortDesc = """TPIS 1991 V2 pt1 p246; pt2 p226.""",
#     longDesc =
# """
# Converted from NASA 9-coefficient format.
# """,
# )
