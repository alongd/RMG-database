#!/usr/bin/env python
# encoding: utf-8

name = "CurranPentanol"
shortDesc = u"N-pentanol oxidation"
longDesc = u"""
K. Alexander Heufer, S. Mani Sarathy, Henry J. Curran, Alexander C. Davis, Charles K. Westbrook, William J. Pitz,
"A Detailed kinetic modeling study of n-pentanol oxidation"
Energy and Fuels 2012
"""

entry(
    index = 1,
    label = "h + o2 <=> o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.65e+14, 'cm^3/(mol*s)'),
        n = -0.262,
        Ea = (16200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "o + h2 <=> h + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6292, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "oh + h2 <=> h + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.247e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (3450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "o + h2o <=> oh + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.445e+06, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (13400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "h2 <=> h + h",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.83, '[C]=O': 1.9},
    ),
)

entry(
    index = 6,
    label = "o + o <=> o2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.83, '[C]=O': 1.9, '[Ar]': 0.83},
    ),
)

entry(
    index = 7,
    label = "o + h <=> oh",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.5, '[Ar]': 0.75},
    ),
)

entry(
    index = 8,
    label = "h + oh <=> h2o",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, '[H][H]': 2.5, '[He]': 0.38, '[C]=O': 1.9, '[Ar]': 0.38},
    ),
)

entry(
    index = 9,
    label = "h + o2 <=> ho2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.65e+12, 'cm^3/(mol*s)'), n=0.44, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.737e+19, 'cm^6/(mol^2*s)'),
            n = -1.23,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.67,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 10, '[H][H]': 1.3, '[He]': 0, '[C]=O': 1.9, '[Ar]': 0},
    ),
)

entry(
    index = 10,
    label = "ho2 + h <=> oh + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "h2 + o2 <=> h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (517600, 'cm^3/(mol*s)'),
        n = 2.433,
        Ea = (53502, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "ho2 + o <=> oh + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "ho2 + oh <=> h2o + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "ho2 + ho2 <=> h2o2 + o2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.03e+14, 'cm^3/(mol*s)'), n=0, Ea=(11040, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1409, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 15,
    label = "h2o2 <=> oh + oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.658e+24, 'cm^3/(mol*s)'),
            n = -2.3,
            Ea = (48749, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'OO': 5.2, 'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 0, '[H][H]': 2.5, '[He]': 0, '[O][O]': 0.68, '[C]=O': 1.9, '[Ar]': 0.68},
    ),
)

entry(
    index = 16,
    label = "h2o2 + h <=> h2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "h2o2 + h <=> h2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.15e+10, 'cm^3/(mol*s)'), n=1, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "h2o2 + o <=> oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "h2o2 + oh <=> h2o + ho2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7269, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 20,
    label = "co + o <=> co2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 6, '[H][H]': 2.5, '[He]': 0.5, '[C]=O': 1.9},
    ),
)

entry(
    index = 21,
    label = "co + o2 <=> co2 + o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+12, 'cm^3/(mol*s)'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "co + oh <=> co2 + h",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (63410, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-355.67, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.757e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (331.83, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 23,
    label = "co + ho2 <=> co2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "hco <=> h + co",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.75e+11, 'cm^3/(mol*s)'),
            n = 0.66,
            Ea = (14870, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 12, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 25,
    label = "hco + o2 <=> co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "hco + h <=> co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "hco + o <=> co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "hco + o <=> co2 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "hco + oh <=> co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "hco + ho2 => co2 + h + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "hco + hco => h2 + co + co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "hco + ch3 <=> ch4 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.65e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "ch2o + o2 <=> hco + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.07e+15, 'cm^3/(mol*s)'), n=0, Ea=(53420, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "hco + o2 <=> o2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "ch2o + o2cho <=> hco + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "ocho + oh <=> ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "h + co2 <=> ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "hco + hco <=> ch2o + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 39,
#     label = "h + o <=> oh*",
#     degeneracy = 1,
#     duplicate = True,
#     kinetics = ThirdBody(
#         arrheniusLow = Arrhenius(A=(1.5e+13, 'cm^6/(mol^2*s)'), n=0, Ea=(5975, 'cal/mol'), T0=(1, 'K')),
#         efficiencies = {'[H][H]': 1, '[O][O]': 0.4, 'O': 6.5, 'N#N': 0.4, '[Ar]': 0.35},
#     ),
# )
#
# entry(
#     index = 40,
#     label = "oh* + h2o <=> oh + h2o",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (5.93e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-860, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 41,
#     label = "oh* + h2 <=> oh + h2",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (2.95e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-444, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 42,
#     label = "oh* + n2 <=> oh + n2",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (1.08e+11, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-1242, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 43,
#     label = "oh* + oh <=> oh + oh",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (6.01e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-764, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 44,
#     label = "oh* + h <=> oh + h",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (1.31e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-167, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 45,
#     label = "oh* + ar <=> oh + ar",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(1.69e+12, 'cm^3/(mol*s)'), n=0, Ea=(4135, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 46,
#     label = "oh* <=> oh",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(1.45e+06, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 47,
#     label = "oh* + o2 <=> oh + o2",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(2.1e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(-478, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 48,
#     label = "oh* + co2 <=> oh + co2",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (2.75e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-968, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 49,
#     label = "oh* + co <=> oh + co",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (3.23e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-787, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 50,
#     label = "oh* + ch4 <=> oh + ch4",
#     degeneracy = 1,
#     kinetics = Arrhenius(
#         A = (3.36e+12, 'cm^3/(mol*s)'),
#         n = 0.5,
#         Ea = (-635, 'cal/mol'),
#         T0 = (1, 'K'),
#     ),
# )
#
# entry(
#     index = 51,
#     label = "ch + o2 <=> co + oh*",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(4.04e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 52,
    label = "c2h + o <=> co + CH(Q)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "c + h <=> CH(Q)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(6940, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 54,
    label = "c2h + o2 <=> co2 + CH(Q)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "CH(Q) + ar <=> ch + ar",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "CH(Q) + h2o <=> ch + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "CH(Q) + co <=> ch + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "CH(Q) + co2 <=> ch + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.241, 'cm^3/(mol*s)'), n=4.3, Ea=(-1694, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "CH(Q) + o2 <=> ch + o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.48e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (-1720, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 60,
    label = "CH(Q) + h2 <=> ch + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.47e+14, 'cm^3/(mol*s)'), n=0, Ea=(1361, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "CH(Q) + ch4 <=> ch + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+13, 'cm^3/(mol*s)'), n=0, Ea=(167, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "CH(Q) <=> ch",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.86e+06, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "CH(Q) + n2 <=> ch + n2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(303, 'cm^3/(mol*s)'), n=3.4, Ea=(-381, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "hco + h <=> ch2o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (1425, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 65,
    label = "co + h2 <=> ch2o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84348, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 66,
    label = "ch2o + oh <=> hco + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.82e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 67,
    label = "ch2o + h <=> hco + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2740, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 68,
    label = "ch2o + o <=> hco + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.26e+09, 'cm^3/(mol*s)'),
        n = 1.15,
        Ea = (2260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 69,
    label = "ch2o + ch3 <=> hco + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(38.3, 'cm^3/(mol*s)'), n=3.36, Ea=(4312, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "ch2o + ho2 <=> hco + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18800, 'cm^3/(mol*s)'), n=2.7, Ea=(11520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 71,
    label = "ch2o + oh <=> hoch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+15, 'cm^3/(mol*s)'), n=-1.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "hoch2o <=> hocho + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "hocho <=> co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.45e+12, 's^-1'), n=0, Ea=(60470, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "hocho <=> co2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+09, 's^-1'), n=0, Ea=(48520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "ocho + ho2 <=> hocho + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "hocho + oh => h2o + co2 + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (2.62e+06, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (916, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 77,
    label = "hocho + oh => h2o + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.85e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 78,
    label = "hocho + h => h2 + co2 + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.24e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 79,
    label = "hocho + h => h2 + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (2988, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "hocho + ch3 => ch4 + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 81,
    label = "ocho + h2o2 <=> hocho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 82,
    label = "hocho + ho2 => h2o2 + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 83,
    label = "hocho + o => co + oh + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.77e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 84,
    label = "ch2o + ocho <=> hocho + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 85,
    label = "ch3o <=> ch2o + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.8e+13, 's^-1'), n=0, Ea=(26170, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24307, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (2500, 'K'),
        T1 = (1300, 'K'),
        T2 = (1e+99, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 86,
    label = "ch3o + o2 <=> ch2o + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-19, 'cm^3/(mol*s)'),
        n = 9.5,
        Ea = (-5501, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 87,
    label = "ch2o + ch3o <=> ch3oh + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(2294, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 88,
    label = "ch3 + ch3oh <=> ch4 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6935, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 89,
    label = "ch3o + ch3 <=> ch2o + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "ch3o + h <=> ch2o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "ch3o + ho2 <=> ch2o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "ch2o + h <=> ch2oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.4e+11, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (3600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.27e+32, 'cm^6/(mol^2*s)'),
            n = -4.82,
            Ea = (6530, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7187,
        T3 = (103, 'K'),
        T1 = (1291, 'K'),
        T2 = (4160, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

entry(
    index = 93,
    label = "ch2oh + o2 <=> ch2o + ho2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.51e+15, 'cm^3/(mol*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.41e+14, 'cm^3/(mol*s)'), n=0, Ea=(5017, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 94,
    label = "ch2oh + h <=> ch2o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 95,
    label = "ch2oh + ho2 <=> ch2o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "ch2oh + hco <=> ch2o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "ch2oh + ch3o <=> ch2o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 98,
    label = "ch3oh + hco <=> ch2oh + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9630, 'cm^3/(mol*s)'), n=2.9, Ea=(13110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 99,
    label = "oh + ch2oh <=> h2o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 100,
    label = "o + ch2oh <=> oh + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "ch2oh + ch2oh <=> ch2o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 102,
    label = "ch2oh + ho2 <=> hoch2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 103,
    label = "ch2o + ho2 <=> och2o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 104,
    label = "och2o2h <=> hoch2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "hoch2o2 + ho2 <=> hoch2o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 106,
    label = "hoch2o + oh <=> hoch2o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "ch3oh <=> ch3 + oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.084e+18, 's^-1'), n=-0.615, Ea=(92540.6, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.5e+43, 'cm^3/(mol*s)'),
            n = -6.99452,
            Ea = (97992.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.4748,
        T3 = (35578.5, 'K'),
        T1 = (1116.46, 'K'),
        T2 = (9023, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 108,
    label = "ch3oh <=> ch2(s) + h2o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.121e+18, 's^-1'), n=-1.017, Ea=(91712, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.43e+47, 'cm^3/(mol*s)'),
            n = -8.22668,
            Ea = (99417.1, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 2.545,
        T3 = (3289.78, 'K'),
        T1 = (47315.6, 'K'),
        T2 = (47110, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 109,
    label = "ch3oh <=> ch2oh + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(0.007896, 's^-1'), n=5.038, Ea=(84467.4, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.39e+42, 'cm^3/(mol*s)'),
            n = -7.24388,
            Ea = (105230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -73.91,
        T3 = (37053.8, 'K'),
        T1 = (41496.4, 'K'),
        T2 = (5220, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 110,
    label = "ch3oh + h <=> ch2oh + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(307000, 'cm^3/(mol*s)'), n=2.55, Ea=(5440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "ch3oh + h <=> ch3o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (199000, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (10300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 112,
    label = "ch3oh + o <=> ch2oh + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 113,
    label = "ch3oh + oh <=> ch2oh + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30800, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-806.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 114,
    label = "ch3oh + oh <=> ch3o + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.03, Ea=(-763, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 115,
    label = "ch3oh + o2 <=> ch2oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(44900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "ch3oh + ho2 <=> ch2oh + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10800, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 117,
    label = "ch3oh + ch3 <=> ch2oh + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "ch3o + ch3oh <=> ch2oh + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 119,
    label = "ch3o + ch3o <=> ch3oh + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "ch3 + h <=> ch4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.35e+15, 'cm^3/(mol*s)'),
            n = -0.63,
            Ea = (383, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.477e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 121,
    label = "ch4 + h <=> ch3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(614000, 'cm^3/(mol*s)'), n=2.5, Ea=(9587, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "ch4 + oh <=> ch3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58300, 'cm^3/(mol*s)'), n=2.6, Ea=(2190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "ch4 + o <=> ch3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 124,
    label = "ch4 + ho2 <=> ch3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11.3, 'cm^3/(mol*s)'), n=3.74, Ea=(21010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "ch4 + ch2 <=> ch3 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 126,
    label = "ch3 + oh <=> ch2(s) + h2o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (0.002394, 'cm^3/(mol*s)'),
            n = 4.096,
            Ea = (-1241.88, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.128e+15, 'cm^6/(mol^2*s)'),
            n = -0.63327,
            Ea = (-493.156, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 2.122,
        T3 = (837.667, 'K'),
        T1 = (2326.05, 'K'),
        T2 = (4432, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 127,
    label = "ch3 + oh <=> ch2o + h2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.88e-14, 'cm^3/(mol*s)'),
            n = 6.721,
            Ea = (-3022.23, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (282320, 'cm^6/(mol^2*s)'),
            n = 1.46878,
            Ea = (-3270.56, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1.671,
        T3 = (434.782, 'K'),
        T1 = (2934.21, 'K'),
        T2 = (3919, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 128,
    label = "ch3 + oh <=> ch2oh + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.86e-06, 'cm^3/(mol*s)'),
            n = 5.009,
            Ea = (1886.46, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.58e+09, 'cm^6/(mol^2*s)'),
            n = 0.996,
            Ea = (3191.12, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1.349,
        T3 = (612.15, 'K'),
        T1 = (2296.27, 'K'),
        T2 = (4411, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 129,
    label = "ch3 + oh <=> h + ch3o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.78e-46, 'cm^3/(mol*s)'),
            n = 18.59,
            Ea = (-27.4138, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.2e+09, 'cm^6/(mol^2*s)'),
            n = 1.014,
            Ea = (11947.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 2.897,
        T3 = (1873.28, 'K'),
        T1 = (3323.16, 'K'),
        T2 = (3675, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 130,
    label = "ch3 + oh <=> hcoh + h2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3e-11, 'cm^3/(mol*s)'),
            n = 6.225,
            Ea = (-3125.55, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.39e+08, 'cm^6/(mol^2*s)'),
            n = 0.82548,
            Ea = (-3097.96, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 2.386,
        T3 = (806.021, 'K'),
        T1 = (2201.7, 'K'),
        T2 = (4440, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 131,
    label = "hcoh + oh <=> hco + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "hcoh + h <=> ch2o + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 133,
    label = "hcoh + o <=> co2 + h + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "hcoh + o <=> co + oh + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "hcoh + o2 <=> co2 + h + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 136,
    label = "hcoh + o2 <=> co2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 137,
    label = "ch3 + ho2 <=> ch3o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0.269,
        Ea = (-687.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 138,
    label = "ch3 + ho2 <=> ch4 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.23,
        Ea = (-3022, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 139,
    label = "ch3 + o <=> ch2o + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.54e+13, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (-136, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 140,
    label = "ch3 + o2 <=> ch3o + o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.546e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 141,
    label = "ch3 + o2 <=> ch2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.641, 'cm^3/(mol*s)'), n=3.283, Ea=(8105, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "ch3 + o2 <=> ch3o2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.812e+09, 'cm^3/(mol*s)'), n=0.9, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.85e+24, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1000, 'K'),
        T1 = (70, 'K'),
        T2 = (1700, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 143,
    label = "ch3o2 + ch2o <=> ch3o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "ch4 + ch3o2 <=> ch3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.64, 'cm^3/(mol*s)'), n=3.77, Ea=(17810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "ch3oh + ch3o2 <=> ch2oh + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "ch3o2 + ch3 <=> ch3o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1411, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "ch3o2 + ho2 <=> ch3o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.47e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1570, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "ch3o2 + ch3o2 => ch2o + ch3oh + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3.11e+14, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (-1051, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 149,
    label = "ch3o2 + ch3o2 => o2 + ch3o + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 150,
    label = "ch3o2 + h <=> ch3o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 151,
    label = "ch3o2 + o <=> ch3o + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 152,
    label = "ch3o2 + oh <=> ch3oh + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "ch3o2h <=> ch3o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 154,
    label = "ch2(s) + n2 <=> ch2 + n2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 155,
    label = "ch2(s) + ar <=> ch2 + ar",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 156,
    label = "ch2(s) + h <=> ch + h2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=-1.56, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.7e+11, 'cm^3/(mol*s)'),
                n = 0.67,
                Ea = (25700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 157,
    label = "ch2(s) + o <=> co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 158,
    label = "ch2(s) + o <=> hco + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 159,
    label = "ch2(s) + oh <=> ch2o + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 160,
    label = "ch2(s) + h2 <=> ch3 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 161,
    label = "ch2(s) + o2 <=> ch2 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 162,
    label = "ch2(s) + h2o <=> ch2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 163,
    label = "ch2(s) + co <=> ch2 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 164,
    label = "ch2(s) + co2 <=> ch2 + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "ch2(s) + co2 <=> ch2o + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "ch2 + h <=> ch3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.2e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 167,
    label = "ch2 + o2 <=> ch2o + o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+06, 'cm^3/(mol*s)'),
        n = 2.4202,
        Ea = (1604, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 168,
    label = "ch2 + o2 <=> co2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 0.9929,
        Ea = (-269.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 169,
    label = "ch2 + o => co + h + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 170,
    label = "ch2 + oh <=> ch + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+07, 'cm^3/(mol*s)'), n=2, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "ch + o2 <=> hco + o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 172,
    label = "c + oh <=> co + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 173,
    label = "c + o2 <=> co + o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 174,
    label = "ch + h <=> c + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 175,
    label = "ch + o <=> co + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 176,
    label = "ch + oh <=> hco + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 177,
    label = "ch + h2o <=> h + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.713e+13, 'cm^3/(mol*s)'), n=0, Ea=(-755, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 178,
    label = "ch + co2 <=> hco + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(685, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "ch3 + ch3 <=> c2h6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.277e+15, 'cm^3/(mol*s)'),
            n = -0.69,
            Ea = (174.86, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.054e+31, 'cm^6/(mol^2*s)'),
            n = -3.75,
            Ea = (981.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        T3 = (570, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[C]=O': 2, 'O=C=O': 3, 'O': 5},
    ),
)

entry(
    index = 180,
    label = "c2h5 + h <=> c2h6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.842,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 181,
    label = "c2h6 + h <=> c2h5 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 182,
    label = "c2h6 + o <=> c2h5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 183,
    label = "c2h6 + oh <=> c2h5 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 184,
    label = "c2h6 + o2 <=> c2h5 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(51870, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 185,
    label = "c2h6 + ch3 <=> c2h5 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.548, 'cm^3/(mol*s)'), n=4, Ea=(8280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 186,
    label = "c2h6 + ho2 <=> c2h5 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34.6, 'cm^3/(mol*s)'), n=3.61, Ea=(16920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "c2h6 + ch3o2 <=> c2h5 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.4, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 188,
    label = "c2h6 + ch3o <=> c2h5 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+11, 'cm^3/(mol*s)'), n=0, Ea=(7090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 189,
    label = "c2h6 + ch <=> c2h5 + ch2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(-260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "ch2(s) + c2h6 <=> ch3 + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 191,
    label = "c2h4 + h <=> c2h5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.27e+09, 'cm^3/(mol*s)'),
            n = 1.183,
            Ea = (1272.7, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.027e+40, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.976,
        T3 = (9.99e+09, 'K'),
        T1 = (384, 'K'),
        T2 = (3.29e+09, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 192,
    label = "h2 + ch3o2 <=> h + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "h2 + c2h5o2 <=> h + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 194,
    label = "c2h4 + c2h4 <=> c2h5 + c2h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+14, 'cm^3/(mol*s)'), n=0, Ea=(71530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 195,
    label = "ch3 + c2h5 <=> ch4 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.45, Ea=(-2921, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 196,
    label = "ch3 + ch3 <=> c2h5 + h",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (3.802e-07, 'cm^3/(mol*s)'),
            n = 4.838,
            Ea = (7710, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.989e+12, 'cm^6/(mol^2*s)'),
            n = 0.099,
            Ea = (10600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 197,
    label = "c2h5 + h <=> c2h4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "c2h5 + o <=> ch3cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "c2h5 + ho2 <=> c2h5o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "ch3o2 + c2h5 <=> ch3o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "c2h5o + o2 <=> ch3cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.28e+10, 'cm^3/(mol*s)'), n=0, Ea=(1097, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "ch3 + ch2o <=> c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(6336, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "ch3cho + h <=> c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.61e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (7090, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 204,
    label = "c2h5o2 + ch2o <=> c2h5o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 205,
    label = "ch4 + c2h5o2 <=> ch3 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 206,
    label = "ch3oh + c2h5o2 <=> ch2oh + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(13710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 207,
    label = "c2h5o2 + ho2 <=> c2h5o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 208,
    label = "c2h6 + c2h5o2 <=> c2h5 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 209,
    label = "c2h5o2h <=> c2h5o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+14, 's^-1'), n=0, Ea=(42300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 210,
    label = "c2h5 + o2 <=> c2h5o2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.398e+53, 'cm^3/(mol*s)'),
                n = -13.9,
                Ea = (9279, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.362e+59, 'cm^3/(mol*s)'),
                n = -15.28,
                Ea = (14240, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.262e+60, 'cm^3/(mol*s)'),
                n = -14.91,
                Ea = (16240, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 211,
    label = "c2h5 + o2 <=> c2h4o2h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.103e+34, 'cm^3/(mol*s)'),
                n = -9.01,
                Ea = (5444, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.884e+33, 'cm^3/(mol*s)'),
                n = -8.31,
                Ea = (7710, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.705e+45, 'cm^3/(mol*s)'),
                n = -11.49,
                Ea = (14590, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 212,
    label = "c2h5 + o2 <=> c2h4 + ho2",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.094e+09, 'cm^3/(mol*s)'),
                n = 0.49,
                Ea = (-391.4, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.843e+07, 'cm^3/(mol*s)'),
                n = 1.13,
                Ea = (-720.6, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.561e+14, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (4749, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 213,
    label = "c2h5 + o2 <=> c2h4 + ho2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(6.609, 'cm^3/(mol*s)'), n=3.51, Ea=(14160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 214,
    label = "c2h5 + o2 <=> c2h4o1-2 + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1303, 'cm^3/(mol*s)'), n=1.93, Ea=(-502.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (243.8, 'cm^3/(mol*s)'),
                n = 2.18,
                Ea = (-62.49, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.621e+09, 'cm^3/(mol*s)'),
                n = 0.15,
                Ea = (5409, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 215,
    label = "c2h5 + o2 <=> ch3cho + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.908e-06, 'cm^3/(mol*s)'),
                n = 4.76,
                Ea = (254.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.06803, 'cm^3/(mol*s)'),
                n = 3.57,
                Ea = (2643, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(826.5, 'cm^3/(mol*s)'), n=2.41, Ea=(5285, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 216,
    label = "c2h4o2h <=> c2h5o2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.653e-16, 's^-1'), n=6.96, Ea=(2396, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.064e+41, 's^-1'), n=-10.1, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.203e+36, 's^-1'), n=-8.13, Ea=(27020, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 217,
    label = "c2h5o2 <=> ch3cho + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.237e+35, 's^-1'), n=-9.42, Ea=(36360, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.687e+36, 's^-1'), n=-9.22, Ea=(38700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.52e+41, 's^-1'), n=-10.2, Ea=(43710, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 218,
    label = "c2h5o2 <=> c2h4 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.782e+32, 's^-1'), n=-7.1, Ea=(32840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.701e+37, 's^-1'), n=-8.47, Ea=(35840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.98e+38, 's^-1'), n=-8.46, Ea=(37900, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 219,
    label = "c2h5o2 <=> c2h4o1-2 + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.778e+45, 's^-1'), n=-11.9, Ea=(4112, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.916e+43, 's^-1'), n=-10.75, Ea=(42400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.965e+43, 's^-1'), n=-10.46, Ea=(45580, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 220,
    label = "c2h4o2h <=> c2h4o1-2 + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.959e+38, 's^-1'), n=-9.4, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.224e+37, 's^-1'), n=-8.32, Ea=(21460, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.848e+30, 's^-1'), n=-6.08, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 221,
    label = "c2h4o2h <=> c2h4 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.918e+40, 's^-1'), n=-10.2, Ea=(22250, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.825e+40, 's^-1'), n=-9.61, Ea=(23840, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.98e+34, 's^-1'), n=-7.25, Ea=(23250, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 222,
    label = "c2h4o2h <=> ch3cho + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.819e+26, 's^-1'), n=-7.97, Ea=(20860, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.52e+34, 's^-1'), n=-9.88, Ea=(26230, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.188e+34, 's^-1'), n=-9.02, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 223,
    label = "c2h4o1-2 <=> ch3 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.63e+13, 's^-1'), n=0, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 224,
    label = "c2h4o1-2 <=> ch3cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.407e+12, 's^-1'), n=0, Ea=(53800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 225,
    label = "c2h4o1-2 + oh <=> c2h3o1-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 'cm^3/(mol*s)'), n=0, Ea=(3610, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 226,
    label = "c2h4o1-2 + h <=> c2h3o1-2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(9680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "c2h4o1-2 + ho2 <=> c2h3o1-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 228,
    label = "c2h4o1-2 + ch3o2 <=> c2h3o1-2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 229,
    label = "c2h4o1-2 + c2h5o2 <=> c2h3o1-2 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 230,
    label = "c2h4o1-2 + ch3 <=> c2h3o1-2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07e+12, 'cm^3/(mol*s)'), n=0, Ea=(11830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 231,
    label = "c2h4o1-2 + ch3o <=> c2h3o1-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 232,
    label = "c2h3o1-2 <=> ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 233,
    label = "c2h3o1-2 <=> ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 234,
    label = "ch3cho <=> ch3 + hco",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.45e+22, 's^-1'), n=-1.74, Ea=(86355, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.02976e+59, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95912.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00249,
        T3 = (718.119, 'K'),
        T1 = (6.08949, 'K'),
        T2 = (3780.02, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 235,
    label = "ch3cho <=> ch4 + co",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.72e+21, 's^-1'), n=-1.74, Ea=(86355, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.14418e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95912.5, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00249,
        T3 = (718.119, 'K'),
        T1 = (6.08949, 'K'),
        T2 = (3780.02, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 236,
    label = "ch3cho + h <=> ch3co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(131000, 'cm^3/(mol*s)'), n=2.58, Ea=(1220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 237,
    label = "ch3cho + h <=> ch2cho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2720, 'cm^3/(mol*s)'), n=3.1, Ea=(5210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 238,
    label = "ch3cho + o <=> ch3co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 239,
    label = "ch3cho + oh <=> ch3co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.37e+12, 'cm^3/(mol*s)'), n=0, Ea=(-619, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 240,
    label = "ch3cho + o2 <=> ch3co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(39150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 241,
    label = "ch3cho + ch3 <=> ch3co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000708, 'cm^3/(mol*s)'),
        n = 4.58,
        Ea = (1966, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 242,
    label = "ch3cho + ho2 <=> ch3co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 243,
    label = "ch3o2 + ch3cho <=> ch3o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 244,
    label = "ch3cho + ch3co3 <=> ch3co + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 245,
    label = "ch3cho + oh <=> ch3 + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-1.076, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 246,
    label = "ch3cho + oh <=> ch2cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(172000, 'cm^3/(mol*s)'), n=2.4, Ea=(815, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 247,
    label = "ch3co <=> ch3 + co",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(16900, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.65e+18, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (14600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.629,
        T3 = (8.73e+09, 'K'),
        T1 = (5.52, 'K'),
        T2 = (7.6e+07, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 248,
    label = "ch3co + h <=> ch2co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 249,
    label = "ch3co + o <=> ch2co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 250,
    label = "ch3co + ch3 <=> ch2co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 251,
    label = "ch3co + o2 <=> ch3co3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 252,
    label = "ch3co3 + ho2 <=> ch3co3h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 253,
    label = "h2o2 + ch3co3 <=> ho2 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+12, 'cm^3/(mol*s)'), n=0, Ea=(9936, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "ch4 + ch3co3 <=> ch3 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+11, 'cm^3/(mol*s)'), n=0, Ea=(18480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 255,
    label = "ch2o + ch3co3 <=> hco + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 256,
    label = "c2h6 + ch3co3 <=> c2h5 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 257,
    label = "ch3co3h <=> ch3co2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(40150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "ch3co2 <=> ch3 + co2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.4e+15, 'cm^3/(mol*s)'), n=0, Ea=(10500, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

entry(
    index = 259,
    label = "ch2cho <=> ch2co + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.43e+15, 's^-1'), n=-0.15, Ea=(45600, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6e+29, 'cm^3/(mol*s)'),
            n = -3.8,
            Ea = (43423.9, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.985,
        T3 = (393, 'K'),
        T1 = (9.8e+09, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 260,
    label = "ch2cho <=> ch3 + co",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.93e+12, 's^-1'), n=0.29, Ea=(40300, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.52e+33, 'cm^3/(mol*s)'),
            n = -5.07,
            Ea = (41300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 7.13e-17,
        T3 = (1150, 'K'),
        T1 = (4.99e+09, 'K'),
        T2 = (1.79e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 261,
    label = "ch2cho + o2 <=> o2ch2cho",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.58e+77, 'cm^3/(mol*s)'),
                n = -21.9,
                Ea = (19350, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.88e+69, 'cm^3/(mol*s)'),
                n = -18.84,
                Ea = (19240, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.8e+59, 'cm^3/(mol*s)'),
                n = -15.4,
                Ea = (17650, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.05e+50, 'cm^3/(mol*s)'),
                n = -12.2,
                Ea = (15630, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 262,
    label = "ch2cho + o2 <=> ch2co + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (188000, 'cm^3/(mol*s)'),
                n = 2.37,
                Ea = (23730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (188000, 'cm^3/(mol*s)'),
                n = 2.37,
                Ea = (27370, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (251000, 'cm^3/(mol*s)'),
                n = 2.33,
                Ea = (23800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.05e+07, 'cm^3/(mol*s)'),
                n = 1.63,
                Ea = (25290, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 263,
    label = "ch2cho + o2 <=> ch2o + co + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.68e+17, 'cm^3/(mol*s)'),
                n = -1.84,
                Ea = (6530, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.52e+20, 'cm^3/(mol*s)'),
                n = -2.58,
                Ea = (8980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.65e+19, 'cm^3/(mol*s)'),
                n = -2.22,
                Ea = (10340, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.953e+13, 'cm^3/(mol*s)'),
                n = -0.6,
                Ea = (10120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 264,
    label = "ch2cho + o2 <=> ho2ch2co",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.64e+65, 'cm^3/(mol*s)'),
                n = -21.87,
                Ea = (19020, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.64e+58, 'cm^3/(mol*s)'),
                n = -19,
                Ea = (19090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.65e+48, 'cm^3/(mol*s)'),
                n = -15.55,
                Ea = (17460, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.8e+38, 'cm^3/(mol*s)'),
                n = -12.14,
                Ea = (14960, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 265,
    label = "o2ch2cho <=> ho2ch2co",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.27e+30, 's^-1'), n=-6.65, Ea=(24500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.73e+26, 's^-1'), n=-4.99, Ea=(23760, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.03e+19, 's^-1'), n=-2.92, Ea=(22170, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.43e+16, 's^-1'), n=-1.67, Ea=(21210, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 266,
    label = "o2ch2cho <=> ch2co + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.05e+40, 's^-1'), n=-13.31, Ea=(52150, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.72e+45, 's^-1'), n=-14, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.16e+55, 's^-1'), n=-15.76, Ea=(55080, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.12e+61, 's^-1'), n=-16.04, Ea=(60010, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 267,
    label = "ho2ch2co <=> co + ch2o + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.36e+17, 's^-1'), n=-2.95, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.38e+18, 's^-1'), n=-2.95, Ea=(8100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.51e+19, 's^-1'), n=-2.95, Ea=(8110, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.16e+20, 's^-1'), n=-3.02, Ea=(8240, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 268,
    label = "ho2ch2co <=> ch2co + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.12e+07, 's^-1'), n=-3.76, Ea=(21680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+08, 's^-1'), n=-3.76, Ea=(21680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.2e+08, 's^-1'), n=-3.73, Ea=(21630, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.09e+09, 's^-1'), n=-3.55, Ea=(21220, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 269,
    label = "ch2 + co <=> ch2co",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 270,
    label = "ch3co <=> ch2co + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.413e+07, 's^-1'), n=1.9166, Ea=(44987.2, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.516e+51, 'cm^3/(mol*s)'),
            n = -10.27,
            Ea = (55390, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.600884,
        T3 = (8.10341e+09, 'K'),
        T1 = (667.669, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 271,
    label = "ch2co + h <=> hcco + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.40068e+15, 'cm^3/(mol*s)'),
        n = -0.17131,
        Ea = (8783.15, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 272,
    label = "ch2co + h <=> ch3 + co",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.70374e+13, 'cm^3/(mol*s)'),
        n = -0.17131,
        Ea = (4183.15, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 273,
    label = "ch2co + o <=> ch2 + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+12, 'cm^3/(mol*s)'), n=0, Ea=(1350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 274,
    label = "ch2co + o <=> hcco + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 275,
    label = "ch2co + oh <=> hcco + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 276,
    label = "ch2co + oh <=> ch2oh + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 277,
    label = "ch2co + ch3 <=> c2h5 + co",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47690, 'cm^3/(mol*s)'),
        n = 2.31199,
        Ea = (9468, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 278,
    label = "ch2(s) + ch2co <=> c2h4 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 279,
    label = "hcco + oh => h2 + co + co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 280,
    label = "hcco + o => h + co + co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 281,
    label = "hcco + h <=> ch2(s) + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 282,
    label = "hcco + o2 => oh + co + co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.91e+11, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 283,
    label = "hcco + o2 => co2 + co + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (4.78e+12, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 284,
    label = "ch + co <=> hcco",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (7.57e+22, 'cm^6/(mol^2*s)'),
            n = -1.9,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 285,
    label = "ch + ch2o <=> h + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.46e+13, 'cm^3/(mol*s)'), n=0, Ea=(-515, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 286,
    label = "ch + hcco <=> co + c2h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 287,
    label = "c2h3 + h <=> c2h4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.08e+12, 'cm^3/(mol*s)'),
            n = 0.27,
            Ea = (280, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 288,
    label = "c2h4 <=> h2 + h2cc",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12, 's^-1'), n=0.44, Ea=(88770, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7e+50, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (99860, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7345,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 289,
    label = "c2h4 + h <=> c2h3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.07e+07, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (12950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 290,
    label = "c2h4 + o <=> ch3 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.775e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 291,
    label = "c2h4 + o <=> ch2cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.775e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 292,
    label = "c2h4 + oh <=> c2h3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22300, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (2215.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 293,
    label = "c2h4 + oh <=> ch3 + ch2o",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.35, 'cm^3/(mol*s)'),
                n = 2.92,
                Ea = (-1732.66, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (31.9, 'cm^3/(mol*s)'),
                n = 2.71,
                Ea = (-1172.33, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (555, 'cm^3/(mol*s)'),
                n = 2.36,
                Ea = (-180.817, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (178000, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (2060.52, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.37e+09, 'cm^3/(mol*s)'),
                n = 0.56,
                Ea = (6006.7, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.76e+13, 'cm^3/(mol*s)'),
                n = -0.5,
                Ea = (11455.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 294,
    label = "c2h4 + oh <=> ch3cho + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.37e-07, 'cm^3/(mol*s)'),
                n = 5.3,
                Ea = (-2050.58, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.73e-05, 'cm^3/(mol*s)'),
                n = 4.57,
                Ea = (-617.957, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.403, 'cm^3/(mol*s)'),
                n = 3.54,
                Ea = (1881.69, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.0238, 'cm^3/(mol*s)'),
                n = 3.91,
                Ea = (1722.73, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.25e+08, 'cm^3/(mol*s)'),
                n = 1.01,
                Ea = (10507.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.8e+09, 'cm^3/(mol*s)'),
                n = 0.81,
                Ea = (13867.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 295,
    label = "c2h4 + oh <=> c2h3oh + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (10400, 'cm^3/(mol*s)'),
                n = 2.6,
                Ea = (4121.04, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (10700, 'cm^3/(mol*s)'),
                n = 2.6,
                Ea = (4128.99, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (15200, 'cm^3/(mol*s)'),
                n = 2.56,
                Ea = (4238.27, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (319000, 'cm^3/(mol*s)'),
                n = 2.19,
                Ea = (5255.61, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.94e+08, 'cm^3/(mol*s)'),
                n = 1.43,
                Ea = (7828.78, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.55e+10, 'cm^3/(mol*s)'),
                n = 0.75,
                Ea = (11490.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 296,
    label = "c2h4 + oh <=> pc2h4oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.74e+43, 'cm^3/(mol*s)'),
                n = -10.4609,
                Ea = (7698.73, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.25e+37, 'cm^3/(mol*s)'),
                n = -8.62888,
                Ea = (5214.66, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.84e+35, 'cm^3/(mol*s)'),
                n = -7.75006,
                Ea = (4908.86, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.56e+36, 'cm^3/(mol*s)'),
                n = -7.75206,
                Ea = (6946.11, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.7e+33, 'cm^3/(mol*s)'),
                n = -6.57294,
                Ea = (7605.89, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.12e+26, 'cm^3/(mol*s)'),
                n = -4.10119,
                Ea = (5756.95, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 297,
    label = "c2h3oh + o2 <=> ch2cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.31e+11, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (39830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 298,
    label = "c2h3oh + o <=> ch2cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.875e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 299,
    label = "c2h3oh + oh <=> ch2cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (540.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 300,
    label = "c2h3oh + ch3 <=> ch2cho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.03e-08, 'cm^3/(mol*s)'),
        n = 5.9,
        Ea = (1052, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 301,
    label = "c2h3oh + ch3o2 <=> ch2cho + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3400, 'cm^3/(mol*s)'), n=2.5, Ea=(8922, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 302,
    label = "c2h3oh + h <=> ch2cho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1480, 'cm^3/(mol*s)'), n=3.077, Ea=(7220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 303,
    label = "c2h3oh + h <=> c2h2oh + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+07, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (15200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 304,
    label = "c2h3oh + h <=> pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+08, 'cm^3/(mol*s)'),
        n = 1.577,
        Ea = (3670, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 305,
    label = "c2h3oh + ho2 <=> ch3cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 306,
    label = "c2h3oh <=> ch3cho",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.42e+46, 's^-1'), n=-10.56, Ea=(67420, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.42e+42, 's^-1'), n=-9.09, Ea=(67069.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.9e+27, 's^-1'), n=-4.35, Ea=(61612.9, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 307,
    label = "c2h4 + ch3 <=> c2h3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62, 'cm^3/(mol*s)'), n=3.7, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 308,
    label = "c2h4 + o2 <=> c2h3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (57623.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 309,
    label = "c2h4 + ch3o <=> c2h3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 310,
    label = "c2h4 + ch3o2 <=> c2h3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 311,
    label = "c2h4 + c2h5o2 <=> c2h3 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 312,
    label = "c2h4 + ch3co3 <=> c2h3 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 313,
    label = "c2h4 + ch3o2 <=> c2h4o1-2 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 314,
    label = "c2h4 + c2h5o2 <=> c2h4o1-2 + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.82e+12, 'cm^3/(mol*s)'), n=0, Ea=(17110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 315,
    label = "c2h4 + ho2 <=> c2h4o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.575e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 316,
    label = "ch + ch4 <=> c2h4 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 317,
    label = "ch2(s) + ch3 <=> c2h4 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 318,
    label = "c2h2 + h <=> c2h3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.71e+10, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.346e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.76,
        T3 = (1e+30, 'K'),
        T1 = (1e-30, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 319,
    label = "c2h3 + o2 <=> ch2o + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+29, 'cm^3/(mol*s)'),
        n = -5.312,
        Ea = (6503.11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 320,
    label = "c2h3 + o2 <=> ch2cho + o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+14, 'cm^3/(mol*s)'),
        n = -0.611,
        Ea = (5262.43, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 321,
    label = "c2h3 + o2 => h + co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5.19e+15, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3312.62, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 322,
    label = "ch3 + c2h3 <=> ch4 + c2h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 323,
    label = "c2h3 + h <=> c2h2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 324,
    label = "c2h3 + h <=> h2cc + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 325,
    label = "c2h3 + oh <=> c2h2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "c2h3 + c2h3 <=> c2h2 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 327,
    label = "c2h + h <=> c2h2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.646,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 328,
    label = "c2h2 <=> h2cc",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+14, 's^-1'), n=-0.52, Ea=(50750, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.45e+15, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 329,
    label = "c2h2 + o <=> ch2 + co",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.395e+08, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (2472, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 330,
    label = "c2h2 + o <=> hcco + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.958e+09, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (2472, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 331,
    label = "c2h2 + oh <=> c2h + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.632e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17060, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 332,
    label = "c2h2 + oh <=> hccoh + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (280000, 'cm^3/(mol*s)'),
                n = 2.28,
                Ea = (12420, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (746700, 'cm^3/(mol*s)'),
                n = 2.16,
                Ea = (12550, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.776e+06, 'cm^3/(mol*s)'),
                n = 2.04,
                Ea = (12670, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.415e+06, 'cm^3/(mol*s)'),
                n = 2,
                Ea = (12710, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.21e+06, 'cm^3/(mol*s)'),
                n = 1.97,
                Ea = (12810, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.347e+06, 'cm^3/(mol*s)'),
                n = 1.89,
                Ea = (13600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 333,
    label = "c2h2 + oh <=> ch2co + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1578, 'cm^3/(mol*s)'), n=2.56, Ea=(-844.5, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (15180, 'cm^3/(mol*s)'),
                n = 2.28,
                Ea = (-292.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (301700, 'cm^3/(mol*s)'),
                n = 1.92,
                Ea = (598.1, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.528e+06, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (2106, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.101e+06, 'cm^3/(mol*s)'),
                n = 1.65,
                Ea = (3400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(14570, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 334,
    label = "c2h2 + oh <=> ch3 + co",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (475700, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (-329.8, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.372e+06, 'cm^3/(mol*s)'),
                n = 1.4,
                Ea = (226.5, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.648e+07, 'cm^3/(mol*s)'),
                n = 1.05,
                Ea = (1115, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.277e+09, 'cm^3/(mol*s)'),
                n = 0.73,
                Ea = (2579, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.312e+08, 'cm^3/(mol*s)'),
                n = 0.92,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(825000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 335,
    label = "c2h2 + oh <=> c2h2oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.913e+32, 'cm^3/(mol*s)'),
                n = -7.126,
                Ea = (5824, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.067e+32, 'cm^3/(mol*s)'),
                n = -6.847,
                Ea = (5508, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.646e+32, 'cm^3/(mol*s)'),
                n = -6.717,
                Ea = (5822, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.387e+31, 'cm^3/(mol*s)'),
                n = -6.087,
                Ea = (6348, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.892e+29, 'cm^3/(mol*s)'),
                n = -5.288,
                Ea = (7055, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.367e+25, 'cm^3/(mol*s)'),
                n = -3.754,
                Ea = (6543, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 336,
    label = "c2h2 + hco <=> c2h3 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 337,
    label = "c2h2 + ch2 <=> c3h3 + h",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(6620, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 338,
    label = "c2h2 + hcco <=> c3h3 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 339,
    label = "h2cc + h <=> c2h2 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 340,
    label = "h2cc + oh <=> ch2co + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 341,
    label = "h2cc + o2 <=> hco + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 342,
    label = "h + hccoh <=> h + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 343,
    label = "c2h5oh <=> c2h4 + h2o",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.41e+59, 's^-1'), n=-14.2, Ea=(83672.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.62e+57, 's^-1'), n=-13.3, Ea=(85262.2, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.65e+52, 's^-1'), n=-11.5, Ea=(84745.6, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.23e+43, 's^-1'), n=-8.9, Ea=(81506.7, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.59e+32, 's^-1'), n=-5.6, Ea=(76062.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.84e+20, 's^-1'), n=-2.06, Ea=(69465.5, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 344,
    label = "c2h5oh <=> ch3 + ch2oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.2e+54, 's^-1'), n=-12.9, Ea=(100006, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.18e+59, 's^-1'), n=-14, Ea=(99906.4, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.62e+66, 's^-1'), n=-15.3, Ea=(105390, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.55e+64, 's^-1'), n=-14.5, Ea=(106183, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.55e+58, 's^-1'), n=-12.3, Ea=(105768, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.78e+47, 's^-1'), n=-8.96, Ea=(101059, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 345,
    label = "c2h5oh <=> c2h5 + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.1e+46, 's^-1'), n=-11.3, Ea=(111053, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.86e+56, 's^-1'), n=-13.5, Ea=(107238, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.65e+63, 's^-1'), n=-15, Ea=(109623, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.46e+65, 's^-1'), n=-14.9, Ea=(112345, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.79e+61, 's^-1'), n=-13.4, Ea=(113080, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.17e+51, 's^-1'), n=-10.3, Ea=(109941, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 346,
    label = "c2h5oh + o2 <=> pc2h4oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(52800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "c2h5oh + o2 <=> sc2h4oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(50150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 348,
    label = "c2h5oh + h <=> sc2h4oh + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(87900, 'cm^3/(mol*s)'), n=2.68, Ea=(2910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 349,
    label = "c2h5oh + h <=> pc2h4oh + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(53100, 'cm^3/(mol*s)'), n=2.81, Ea=(7490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "c2h5oh + h <=> c2h5o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701.07, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 351,
    label = "c2h5oh + oh <=> sc2h4oh + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (71700, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (-1533.96, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 352,
    label = "c2h5oh + oh <=> pc2h4oh + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7, 'cm^3/(mol*s)'),
        n = 3.38,
        Ea = (-2394.34, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 353,
    label = "c2h5oh + oh <=> c2h5o + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00581, 'cm^3/(mol*s)'),
        n = 4.28,
        Ea = (-3560, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 354,
    label = "c2h5oh + ho2 <=> sc2h4oh + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.028, 'cm^3/(mol*s)'), n=4.32, Ea=(8530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 355,
    label = "c2h5oh + ho2 <=> pc2h4oh + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00904, 'cm^3/(mol*s)'),
        n = 4.54,
        Ea = (11967.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 356,
    label = "c2h5oh + ho2 <=> c2h5o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00562, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (17400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 357,
    label = "c2h5oh + ch3o2 <=> pc2h4oh + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 358,
    label = "c2h5oh + ch3o2 <=> sc2h4oh + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 359,
    label = "c2h5oh + ch3o2 <=> c2h5o + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 360,
    label = "c2h5oh + o <=> pc2h4oh + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(969, 'cm^3/(mol*s)'), n=3.23, Ea=(4658, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 361,
    label = "c2h5oh + o <=> sc2h4oh + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 362,
    label = "c2h5oh + o <=> c2h5o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 363,
    label = "c2h5oh + ch3 <=> pc2h4oh + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(330, 'cm^3/(mol*s)'), n=3.3, Ea=(12290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 364,
    label = "c2h5oh + ch3 <=> sc2h4oh + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 365,
    label = "c2h5oh + ch3 <=> c2h5o + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.035, 'cm^3/(mol*s)'), n=3.57, Ea=(7721, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 366,
    label = "c2h5oh + c2h5 <=> pc2h4oh + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "c2h5oh + c2h5 <=> sc2h4oh + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 368,
    label = "sc2h4oh <=> ch3cho + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.69e+52, 's^-1'), n=-13.38, Ea=(45049, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.29e+56, 's^-1'), n=-14.12, Ea=(48129, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.58e+57, 's^-1'), n=-14.16, Ea=(50743, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.36e+55, 's^-1'), n=-13.15, Ea=(51886, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.66e+48, 's^-1'), n=-10.64, Ea=(50297, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.26e+44, 's^-1'), n=-9.59, Ea=(49218, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.01e+40, 's^-1'), n=-8.06, Ea=(47439, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+36, 's^-1'), n=-6.84, Ea=(45899, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 369,
    label = "sc2h4oh <=> c2h3oh + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.4e+46, 's^-1'), n=-11.63, Ea=(44323, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.21e+51, 's^-1'), n=-12.55, Ea=(47240, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.87e+54, 's^-1'), n=-13.15, Ea=(50702, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.79e+53, 's^-1'), n=-12.51, Ea=(52560, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.33e+46, 's^-1'), n=-10.2, Ea=(51441, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.87e+43, 's^-1'), n=-9.17, Ea=(50440, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.08e+38, 's^-1'), n=-7.65, Ea=(48713, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.12e+34, 's^-1'), n=-6.41, Ea=(47182, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 370,
    label = "sc2h4oh <=> c2h5o",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.48e+45, 's^-1'), n=-11.63, Ea=(44328, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.54e+49, 's^-1'), n=-12.37, Ea=(46445, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.65e+54, 's^-1'), n=-13.4, Ea=(50330, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.81e+55, 's^-1'), n=-13.31, Ea=(53132, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.58e+49, 's^-1'), n=-11.32, Ea=(52714, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.11e+46, 's^-1'), n=-10.33, Ea=(51834, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.68e+41, 's^-1'), n=-8.83, Ea=(50202, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.54e+37, 's^-1'), n=-7.58, Ea=(48697, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 371,
    label = "sc2h4oh <=> pc2h4oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.65e+36, 's^-1'), n=-8.86, Ea=(51019, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.56e+37, 's^-1'), n=-8.89, Ea=(51114, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.14e+39, 's^-1'), n=-9.19, Ea=(51912, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.82e+44, 's^-1'), n=-10.34, Ea=(55296, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.26e+48, 's^-1'), n=-11.06, Ea=(59458, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.84e+47, 's^-1'), n=-10.74, Ea=(59901, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.23e+45, 's^-1'), n=-9.84, Ea=(59604, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.7e+42, 's^-1'), n=-8.83, Ea=(58737, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 372,
    label = "o2c2h4oh <=> pc2h4oh + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+16, 's^-1'), n=-1, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "o2c2h4oh => oh + ch2o + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 374,
    label = "sc2h4oh + o2 <=> ch3cho + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 375,
    label = "sc2h4oh + o2 <=> c2h3oh + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(512, 'cm^3/(mol*s)'), n=2.496, Ea=(-414, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(533, 'cm^3/(mol*s)'), n=2.49, Ea=(-402, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(762, 'cm^3/(mol*s)'), n=2.446, Ea=(-296, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8920, 'cm^3/(mol*s)'), n=2.146, Ea=(470, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (438000, 'cm^3/(mol*s)'),
                n = 1.699,
                Ea = (2330, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 376,
    label = "ch3coch3 <=> ch3co + ch3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.108e+21, 's^-1'), n=-1.57, Ea=(84680, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.013e+89, 'cm^3/(mol*s)'),
            n = -20.38,
            Ea = (107150, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.863,
        T3 = (1e+10, 'K'),
        T1 = (416.4, 'K'),
        T2 = (3.29e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 377,
    label = "ch3coch3 + oh <=> ch3coch2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(125000, 'cm^3/(mol*s)'), n=2.483, Ea=(445, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 378,
    label = "ch3coch3 + h <=> ch3coch2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(5160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 379,
    label = "ch3coch3 + o <=> ch3coch2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.13e+11, 'cm^3/(mol*s)'),
        n = 0.211,
        Ea = (4890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 380,
    label = "ch3coch3 + ch3 <=> ch3coch2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.96e+11, 'cm^3/(mol*s)'), n=0, Ea=(9784, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "ch3coch3 + ch3o <=> ch3coch2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.34e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "ch3coch3 + o2 <=> ch3coch2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 383,
    label = "ch3coch3 + ho2 <=> ch3coch2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 384,
    label = "ch3coch3 + ch3o2 <=> ch3coch2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 385,
    label = "ch2co + ch3 <=> ch3coch2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 386,
    label = "ch3coch2 + o2 <=> ch3coch2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 387,
    label = "ch3coch3 + ch3coch2o2 <=> ch3coch2 + c3ket21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 388,
    label = "ch2o + ch3coch2o2 <=> hco + c3ket21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.288e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 389,
    label = "ho2 + ch3coch2o2 <=> c3ket21 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 390,
    label = "c2h3 + hco <=> c2h3cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 391,
    label = "c2h3cho + h <=> c2h3co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 392,
    label = "c2h3cho + o <=> c2h3co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 393,
    label = "c2h3cho + oh <=> c2h3co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.24e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 394,
    label = "c2h3cho + o2 <=> c2h3co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 395,
    label = "c2h3cho + ho2 <=> c2h3co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 396,
    label = "c2h3cho + ch3 <=> c2h3co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 397,
    label = "c2h3cho + c2h3 <=> c2h3co + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 398,
    label = "c2h3cho + ch3o <=> c2h3co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 399,
    label = "c2h3cho + ch3o2 <=> c2h3co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 400,
    label = "c2h3 + co <=> c2h3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 401,
    label = "c2h5 + hco <=> c2h5cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 402,
    label = "c2h5cho + h <=> c2h5co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 403,
    label = "c2h5cho + o <=> c2h5co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 404,
    label = "c2h5cho + oh <=> c2h5co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 405,
    label = "c2h5cho + ch3 <=> c2h5co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.608e+06, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 406,
    label = "c2h5cho + ho2 <=> c2h5co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 407,
    label = "c2h5cho + ch3o <=> c2h5co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 408,
    label = "c2h5cho + ch3o2 <=> c2h5co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 409,
    label = "c2h5cho + c2h5 <=> c2h5co + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 410,
    label = "c2h5cho + c2h5o <=> c2h5co + c2h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.026e+11, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "c2h5cho + c2h5o2 <=> c2h5co + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "c2h5cho + o2 <=> c2h5co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 413,
    label = "c2h5cho + ch3co3 <=> c2h5co + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 414,
    label = "c2h5cho + c2h3 <=> c2h5co + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 415,
    label = "c2h5 + co <=> c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 416,
    label = "ch3och3 <=> ch3 + ch3o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.38e+21, 's^-1'), n=-1.57, Ea=(83890, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(7.52e+15, 'cm^3/(mol*s)'), n=0, Ea=(42790, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.454,
        T3 = (1e-30, 'K'),
        T1 = (2510, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 417,
    label = "ch3och3 + oh <=> ch3och2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.324e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-651.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 418,
    label = "ch3och3 + h <=> ch3och2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.721e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (3384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 419,
    label = "ch3och3 + o <=> ch3och2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.75e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 420,
    label = "ch3och3 + ho2 <=> ch3och2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 421,
    label = "ch3och3 + ch3o2 <=> ch3och2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(312, 'cm^3/(mol*s)'), n=3.12, Ea=(13190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 422,
    label = "ch3och3 + ch3 <=> ch3och2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.445e-06, 'cm^3/(mol*s)'),
        n = 5.73,
        Ea = (5700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 423,
    label = "ch3och3 + o2 <=> ch3och2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(44910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 424,
    label = "ch3och3 + ch3o <=> ch3och2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(4074, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 425,
    label = "ch3och3 + ch3och2o2 <=> ch3och2 + ch3och2o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 426,
    label = "ch3och3 + o2cho <=> ch3och2 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44250, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 427,
    label = "ch3och3 + ocho <=> ch3och2 + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 428,
    label = "ch3och2 <=> ch2o + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 's^-1'), n=0, Ea=(25500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 429,
    label = "ch3och2 + ch3o <=> ch3och3 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 430,
    label = "ch3och2 + ch2o <=> ch3och3 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5490, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 431,
    label = "ch3och2 + ch3cho <=> ch3och3 + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(8499, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 432,
    label = "ch3och2 + o2 <=> ch3och2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 433,
    label = "ch3och2o2 + ch2o <=> ch3och2o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 434,
    label = "ch3och2o2 + ch3cho <=> ch3och2o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 435,
    label = "ch3och2o2 + ch3och2o2 => o2 + ch3och2o + ch3och2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.547e+23, 'cm^3/(mol*s)'), n=-4.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 436,
    label = "ch3och2o + oh <=> ch3och2o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 437,
    label = "ch3o + ch2o <=> ch3och2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 438,
    label = "ch3och2o + o2 <=> ch3ocho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 439,
    label = "ch3ocho + h <=> ch3och2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(7838, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "ch3och2o2 <=> ch2och2o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+10, 's^-1'), n=0, Ea=(21580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 441,
    label = "ch2och2o2h => oh + ch2o + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+13, 's^-1'), n=0, Ea=(19760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 442,
    label = "ch2och2o2h + o2 <=> o2ch2och2o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 443,
    label = "o2ch2och2o2h <=> ho2ch2ocho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=0, Ea=(18580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 444,
    label = "ho2ch2ocho <=> och2ocho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+16, 's^-1'), n=0, Ea=(41500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 445,
    label = "ch2o + ocho <=> och2ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 446,
    label = "och2ocho <=> hoch2oco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 447,
    label = "hoch2o + co <=> hoch2oco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 448,
    label = "ch2oh + co2 <=> hoch2oco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(35720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 449,
    label = "ch2ocho + h <=> ch3ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 450,
    label = "ch3oco + h <=> ch3ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 451,
    label = "ch3ocho <=> ch3oh + co",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(62500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.143e+60, 'cm^3/(mol*s)'),
            n = -12.07,
            Ea = (75400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.78,
        T3 = (8.28e+09, 'K'),
        T1 = (438.9, 'K'),
        T2 = (6.7e+08, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 452,
    label = "ch3o + hco <=> ch3ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 453,
    label = "ch3 + ocho <=> ch3ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 454,
    label = "ch3ocho + o2 <=> ch3oco + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(49700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 455,
    label = "ch3ocho + o2 <=> ch2ocho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(52000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 456,
    label = "ch3ocho + oh <=> ch3oco + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(934, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 457,
    label = "ch3ocho + oh <=> ch2ocho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 458,
    label = "ch3ocho + ho2 <=> ch3oco + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 459,
    label = "ch3ocho + ho2 <=> ch2ocho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 460,
    label = "ch3ocho + o <=> ch3oco + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(275500, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 461,
    label = "ch3ocho + o <=> ch2ocho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 462,
    label = "ch3ocho + h <=> ch3oco + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(650000, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 463,
    label = "ch3ocho + h <=> ch2ocho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 464,
    label = "ch3ocho + ch3 <=> ch3oco + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.755, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 465,
    label = "ch3ocho + ch3 <=> ch2ocho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 466,
    label = "ch3ocho + ch3o <=> ch3oco + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.48e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 467,
    label = "ch3ocho + ch3o <=> ch2ocho + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 468,
    label = "ch3ocho + ch3o2 <=> ch3oco + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 469,
    label = "ch3ocho + ch3o2 <=> ch2ocho + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 470,
    label = "ch3ocho + hco <=> ch3oco + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 471,
    label = "ch3ocho + hco <=> ch2ocho + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102500, 'cm^3/(mol*s)'), n=2.5, Ea=(18430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 472,
    label = "ch3oco <=> ch2ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.629e+12, 's^-1'), n=-0.18, Ea=(40670, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 473,
    label = "ch3 + co2 <=> ch3oco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.76e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (34700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 474,
    label = "ch3o + co <=> ch3oco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55e+06, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (5730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 475,
    label = "ch2o + hco <=> ch2ocho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 476,
    label = "c3h8 <=> ch3 + c2h5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97380, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.64e+74, 'cm^3/(mol*s)'),
            n = -15.74,
            Ea = (98714, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.31,
        T3 = (50, 'K'),
        T1 = (3000, 'K'),
        T2 = (9000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 477,
    label = "nc3h7 + h <=> c3h8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 478,
    label = "ic3h7 + h <=> c3h8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 479,
    label = "c3h8 + o2 <=> ic3h7 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 480,
    label = "c3h8 + o2 <=> nc3h7 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 481,
    label = "h + c3h8 <=> h2 + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 482,
    label = "h + c3h8 <=> h2 + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 483,
    label = "c3h8 + o <=> ic3h7 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(549000, 'cm^3/(mol*s)'), n=2.5, Ea=(3140, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 484,
    label = "c3h8 + o <=> nc3h7 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.71e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 485,
    label = "c3h8 + oh <=> nc3h7 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 486,
    label = "c3h8 + oh <=> ic3h7 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 487,
    label = "c3h8 + ho2 <=> ic3h7 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 488,
    label = "c3h8 + ho2 <=> nc3h7 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 489,
    label = "ch3 + c3h8 <=> ch4 + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(64000, 'cm^3/(mol*s)'), n=2.17, Ea=(7520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 490,
    label = "ch3 + c3h8 <=> ch4 + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 491,
    label = "ic3h7 + c3h8 <=> nc3h7 + c3h8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(12900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 492,
    label = "c2h3 + c3h8 <=> c2h4 + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 493,
    label = "c2h3 + c3h8 <=> c2h4 + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 494,
    label = "c2h5 + c3h8 <=> c2h6 + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 495,
    label = "c2h5 + c3h8 <=> c2h6 + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 496,
    label = "c3h8 + c3h5-a <=> nc3h7 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 497,
    label = "c3h8 + c3h5-a <=> ic3h7 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(16200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 498,
    label = "c3h8 + ch3o <=> nc3h7 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 499,
    label = "c3h8 + ch3o <=> ic3h7 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 500,
    label = "ch3o2 + c3h8 <=> ch3o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 501,
    label = "ch3o2 + c3h8 <=> ch3o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 502,
    label = "c2h5o2 + c3h8 <=> c2h5o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "c2h5o2 + c3h8 <=> c2h5o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 504,
    label = "nc3h7o2 + c3h8 <=> nc3h7o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 505,
    label = "nc3h7o2 + c3h8 <=> nc3h7o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 506,
    label = "ic3h7o2 + c3h8 <=> ic3h7o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 507,
    label = "ic3h7o2 + c3h8 <=> ic3h7o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 508,
    label = "c3h8 + ch3co3 <=> ic3h7 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 509,
    label = "c3h8 + ch3co3 <=> nc3h7 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 510,
    label = "c3h8 + o2cho <=> nc3h7 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(55200, 'cm^3/(mol*s)'), n=2.55, Ea=(16480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 511,
    label = "c3h8 + o2cho <=> ic3h7 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14750, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 512,
    label = "h + c3h6 <=> ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 513,
    label = "ic3h7 + h <=> c2h5 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 514,
    label = "ic3h7 + o2 <=> c3h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e-19, 'cm^3/(mol*s)'), n=0, Ea=(5020, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 515,
    label = "ic3h7 + oh <=> c3h6 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 516,
    label = "ic3h7 + o <=> ch3coch3 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 517,
    label = "ic3h7 + o <=> ch3cho + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.818e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 518,
    label = "ch3 + c2h4 <=> nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 519,
    label = "h + c3h6 <=> nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 520,
    label = "nc3h7 + o2 <=> c3h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 521,
    label = "c2h5cho + nc3h7 <=> c2h5co + c3h8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 522,
    label = "c2h5cho + ic3h7 <=> c2h5co + c3h8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 523,
    label = "c2h5cho + c3h5-a <=> c2h5co + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "c2h3 + ch3 <=> c3h6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (10140, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 525,
    label = "c3h5-a + h <=> c3h6",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5967.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1096.6, 'K'),
        T1 = (1096.6, 'K'),
        T2 = (6859.5, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 526,
    label = "c3h6 <=> c3h5-s + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "c3h6 <=> c3h5-t + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+71, 's^-1'), n=-16.58, Ea=(139300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 528,
    label = "c3h6 + o <=> c2h5 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-1216, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 529,
    label = "c3h6 + o => ch2co + ch3 + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 530,
    label = "c3h6 + o => ch3chco + h + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 531,
    label = "c3h6 + o <=> c3h5-a + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 532,
    label = "c3h6 + o <=> c3h5-s + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(8959, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 533,
    label = "c3h6 + o <=> c3h5-t + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 534,
    label = "c3h6 + oh <=> c3h5-a + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.97e+06, 'cm^3/(mol*s)'), n=2.2, Ea=(540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 535,
    label = "c3h6 + oh <=> c3h5-s + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(2778, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 536,
    label = "c3h6 + oh <=> c3h5-t + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 537,
    label = "c3h6 + ho2 <=> c3h5-a + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 538,
    label = "c3h6 + ho2 <=> c3h5-s + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18000, 'cm^3/(mol*s)'), n=2.5, Ea=(27620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 539,
    label = "c3h6 + ho2 <=> c3h5-t + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9000, 'cm^3/(mol*s)'), n=2.5, Ea=(23590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 540,
    label = "c3h6 + h <=> c3h5-a + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 541,
    label = "c3h6 + h <=> c3h5-s + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(804000, 'cm^3/(mol*s)'), n=2.5, Ea=(12280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 542,
    label = "c3h6 + h <=> c3h5-t + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(405000, 'cm^3/(mol*s)'), n=2.5, Ea=(9794, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 543,
    label = "c3h6 + h <=> c2h4 + ch3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.8e+16, 'cm^3/(mol*s)'),
                n = -1.05,
                Ea = (6461, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8e+21, 'cm^3/(mol*s)'),
                n = -2.39,
                Ea = (11180, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.3e+24, 'cm^3/(mol*s)'),
                n = -3.04,
                Ea = (15610, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 544,
    label = "c3h6 + o2 <=> c3h5-a + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 545,
    label = "c3h6 + o2 <=> c3h5-s + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(62900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 546,
    label = "c3h6 + o2 <=> c3h5-t + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(60700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 547,
    label = "c3h6 + ch3 <=> c3h5-a + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 548,
    label = "c3h6 + ch3 <=> c3h5-s + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 549,
    label = "c3h6 + ch3 <=> c3h5-t + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 550,
    label = "c3h6 + c2h5 <=> c3h5-a + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 551,
    label = "c3h6 + ch3co3 <=> c3h5-a + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 552,
    label = "c3h6 + ch3o2 <=> c3h5-a + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 553,
    label = "c3h6 + ho2 <=> c3h6o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 554,
    label = "c3h6 + c2h5o2 <=> c3h5-a + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 555,
    label = "c3h6 + nc3h7o2 <=> c3h5-a + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 556,
    label = "c3h6 + ic3h7o2 <=> c3h5-a + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 557,
    label = "c3h6 + oh <=> c3h6oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 558,
    label = "c3h6oh-3 + o2 <=> hoc3h6o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 559,
    label = "hoc3h6o2 => ch3cho + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 560,
    label = "c2h2 + ch3 <=> c3h5-a",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (8.2e+53, 'cm^3/(mol*s)'),
                n = -13.32,
                Ea = (33200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.68e+53, 'cm^3/(mol*s)'),
                n = -12.82,
                Ea = (35730, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.64e+52, 'cm^3/(mol*s)'),
                n = -12.46,
                Ea = (36127, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.04e+51, 'cm^3/(mol*s)'),
                n = -11.89,
                Ea = (36476, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.4e+49, 'cm^3/(mol*s)'),
                n = -11.4,
                Ea = (36700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8e+44, 'cm^3/(mol*s)'),
                n = -9.63,
                Ea = (37600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 561,
    label = "c3h4-a + h <=> c3h5-a",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.6e+61, 'cm^3/(mol*s)'),
                n = -14.67,
                Ea = (26000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.52e+59, 'cm^3/(mol*s)'),
                n = -13.54,
                Ea = (26949, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+57, 'cm^3/(mol*s)'),
                n = -12.98,
                Ea = (26785, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.34e+54, 'cm^3/(mol*s)'),
                n = -12.09,
                Ea = (26187, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+52, 'cm^3/(mol*s)'),
                n = -11.3,
                Ea = (25400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.9e+41, 'cm^3/(mol*s)'),
                n = -8.06,
                Ea = (21300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 562,
    label = "c3h5-a + ho2 <=> c3h5o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 563,
    label = "c3h5-a + ch3o2 <=> c3h5o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 564,
    label = "c3h5-a + h <=> c3h4-a + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1232, 'cm^3/(mol*s)'), n=3.035, Ea=(2582, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 565,
    label = "c3h5-a + o <=> c2h3cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 566,
    label = "c3h5-a + oh => c2h3cho + h + h",
    degeneracy = 1,
    reversible = False,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.3e+37, 'cm^3/(mol*s)'),
                n = -6.71,
                Ea = (29306, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.2e+32, 'cm^3/(mol*s)'),
                n = -5.16,
                Ea = (30126, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+20, 'cm^3/(mol*s)'),
                n = -1.56,
                Ea = (26330, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 567,
    label = "c3h5-a + oh <=> c3h4-a + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 568,
    label = "c3h5-a + ch3 <=> c3h4-a + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=-0.32, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 569,
    label = "c3h5-a + c2h5 <=> c2h6 + c3h4-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 570,
    label = "c3h5-a + c2h5 <=> c2h4 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 571,
    label = "c3h5-a + c2h3 <=> c2h4 + c3h4-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 572,
    label = "c3h5-a + c3h5-a <=> c3h4-a + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.43e+10, 'cm^3/(mol*s)'), n=0, Ea=(-262, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 573,
    label = "c3h5-a + o2 <=> c3h4-a + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.99e+15, 'cm^3/(mol*s)'),
                n = -1.4,
                Ea = (22428, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.18e+21, 'cm^3/(mol*s)'),
                n = -2.85,
                Ea = (30755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 574,
    label = "c3h5-a + o2 <=> ch3co + ch2o",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.19e+15, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (20128, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.14e+15, 'cm^3/(mol*s)'),
                n = -1.21,
                Ea = (21046, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 575,
    label = "c3h5-a + o2 <=> c2h3cho + oh",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.82e+13, 'cm^3/(mol*s)'),
                n = -0.41,
                Ea = (22859, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.47e+13, 'cm^3/(mol*s)'),
                n = -0.45,
                Ea = (23017, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 576,
    label = "c3h5-a + hco <=> c3h6 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 577,
    label = "c2h3 + ch3 <=> c3h5-a + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+24, 'cm^3/(mol*s)'),
        n = -2.83,
        Ea = (18618, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 578,
    label = "c3h5-a <=> c3h5-t",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.9e+59, 's^-1'), n=-15.42, Ea=(75400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.06e+56, 's^-1'), n=-14.08, Ea=(75868, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.8e+55, 's^-1'), n=-13.59, Ea=(75949, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+53, 's^-1'), n=-12.81, Ea=(75883, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.4e+51, 's^-1'), n=-12.12, Ea=(75700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+43, 's^-1'), n=-9.27, Ea=(74000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 579,
    label = "c3h5-a <=> c3h5-s",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.3e+55, 's^-1'), n=-14.53, Ea=(73800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5e+51, 's^-1'), n=-13.02, Ea=(73300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.86e+44, 's^-1'), n=-9.84, Ea=(73400, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 580,
    label = "c2h2 + ch3 <=> c3h5-s",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.4e+32, 'cm^3/(mol*s)'),
                n = -7.14,
                Ea = (10000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+35, 'cm^3/(mol*s)'),
                n = -7.76,
                Ea = (13300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+38, 'cm^3/(mol*s)'),
                n = -8.21,
                Ea = (17100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.4e+39, 'cm^3/(mol*s)'),
                n = -8.06,
                Ea = (20200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 581,
    label = "c3h5-s + o2 <=> ch3cho + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 582,
    label = "c3h5-s + h <=> c3h4-a + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.333e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 583,
    label = "c3h5-s + ch3 <=> c3h4-a + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 584,
    label = "c2h2 + ch3 <=> c3h5-t",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.8e+20, 'cm^3/(mol*s)'),
                n = -4.16,
                Ea = (18000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.99e+22, 'cm^3/(mol*s)'),
                n = -4.39,
                Ea = (18850, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(6e+23, 'cm^3/(mol*s)'), n=-4.6, Ea=(19571, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (7.31e+25, 'cm^3/(mol*s)'),
                n = -5.06,
                Ea = (21150, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.3e+27, 'cm^3/(mol*s)'),
                n = -5.55,
                Ea = (22900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.8e+36, 'cm^3/(mol*s)'),
                n = -7.58,
                Ea = (31300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 585,
    label = "c3h4-a + h <=> c3h5-t",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.2e+38, 'cm^3/(mol*s)'),
                n = -8.65,
                Ea = (7000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.46e+42, 'cm^3/(mol*s)'),
                n = -9.43,
                Ea = (11190, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.47e+43, 'cm^3/(mol*s)'),
                n = -9.59,
                Ea = (12462, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.98e+44, 'cm^3/(mol*s)'),
                n = -9.7,
                Ea = (14032, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+45, 'cm^3/(mol*s)'),
                n = -9.69,
                Ea = (15100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.8e+43, 'cm^3/(mol*s)'),
                n = -8.78,
                Ea = (16800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 586,
    label = "c3h4-p + h <=> c3h5-t",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.6e+44, 'cm^3/(mol*s)'),
                n = -10.21,
                Ea = (10200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.66e+47, 'cm^3/(mol*s)'),
                n = -10.58,
                Ea = (13690, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.04e+47, 'cm^3/(mol*s)'),
                n = -10.61,
                Ea = (14707, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.62e+47, 'cm^3/(mol*s)'),
                n = -10.55,
                Ea = (15910, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7e+47, 'cm^3/(mol*s)'),
                n = -10.4,
                Ea = (16600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+44, 'cm^3/(mol*s)'),
                n = -9.11,
                Ea = (17400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 587,
    label = "c3h5-s + h <=> c3h4-p + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 588,
    label = "c3h5-s + o <=> c2h4 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 589,
    label = "c3h5-s + oh => c2h4 + hco + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 590,
    label = "c3h5-s + ho2 => c2h4 + hco + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 591,
    label = "c3h5-s + hco <=> c3h6 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 592,
    label = "c3h5-s + ch3 <=> c3h4-p + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 593,
    label = "c3h5-t <=> c3h5-s",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.6e+44, 's^-1'), n=-12.16, Ea=(52200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+48, 's^-1'), n=-12.71, Ea=(53900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.1e+52, 's^-1'), n=-13.37, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.8e+51, 's^-1'), n=-12.43, Ea=(59200, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 594,
    label = "c3h4-a + h <=> c3h5-s",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+30, 'cm^3/(mol*s)'),
                n = -6.52,
                Ea = (15200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.4e+29, 'cm^3/(mol*s)'),
                n = -6.09,
                Ea = (16300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.6e+31, 'cm^3/(mol*s)'),
                n = -6.23,
                Ea = (18700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.2e+31, 'cm^3/(mol*s)'),
                n = -5.88,
                Ea = (21500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 595,
    label = "c3h4-a + c3h4-a <=> c3h5-a + c3h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=0, Ea=(64746.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 596,
    label = "c3h5-t + o2 <=> c3h4-a + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.89e+30, 'cm^3/(mol*s)'),
        n = -5.59,
        Ea = (15540, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 597,
    label = "c3h5-t + o2 <=> ch3coch2 + o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.81e+17, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (5580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 598,
    label = "c3h5-t + o2 <=> ch3co + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 599,
    label = "c3h5-t + h <=> c3h4-p + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.34e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 600,
    label = "c3h5-t + ch3 <=> c3h4-p + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 601,
    label = "c3h5-t + o <=> ch3 + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 602,
    label = "c3h5-t + oh => ch3 + ch2co + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 603,
    label = "c3h5-t + ho2 => ch3 + ch2co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 604,
    label = "c3h5-t + hco <=> c3h6 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 605,
    label = "c3h4-p <=> c3h4-a",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 0.4, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.4e+61, 's^-1'), n=-14.59, Ea=(88200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.81e+62, 's^-1'), n=-14.63, Ea=(91211, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.15e+60, 's^-1'), n=-13.93, Ea=(91117, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.64e+59, 's^-1'), n=-13.59, Ea=(91817, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.12e+58, 's^-1'), n=-13.07, Ea=(92680, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+57, 's^-1'), n=-12.62, Ea=(93300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.4e+52, 's^-1'), n=-10.86, Ea=(95400, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 606,
    label = "c3h3 + ho2 <=> c3h4-a + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 607,
    label = "c3h4-a + ho2 => ch2co + ch2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 608,
    label = "c3h4-a + oh <=> ch2co + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+12, 'cm^3/(mol*s)'), n=0, Ea=(-397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 609,
    label = "c3h4-a + oh <=> c3h3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 610,
    label = "c3h4-a + o <=> c2h4 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 611,
    label = "c3h4-a + o <=> c2h2 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.003, 'cm^3/(mol*s)'), n=4.61, Ea=(-4243, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 612,
    label = "c3h4-a + h <=> c3h3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 613,
    label = "c3h4-a + ch3 <=> c3h3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 614,
    label = "c3h4-a + c3h5-a <=> c3h3 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 615,
    label = "c3h4-a + c2h <=> c2h2 + c3h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 616,
    label = "c3h4-p <=> cc3h4",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 0.4, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.4e+46, 's^-1'), n=-10.97, Ea=(68900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.84e+45, 's^-1'), n=-10.45, Ea=(69284, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.2e+44, 's^-1'), n=-9.92, Ea=(69250, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.47e+42, 's^-1'), n=-9.43, Ea=(69089, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.92e+40, 's^-1'), n=-8.69, Ea=(68706, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.3e+38, 's^-1'), n=-8.06, Ea=(68300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+31, 's^-1'), n=-5.69, Ea=(66400, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 617,
    label = "c3h4-p + h <=> c3h4-a + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.3e+15, 'cm^3/(mol*s)'),
                n = -0.26,
                Ea = (7600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.27e+17, 'cm^3/(mol*s)'),
                n = -0.91,
                Ea = (10079, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1.5e+18, 'cm^3/(mol*s)'), n=-1, Ea=(10756, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.93e+18, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (11523, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1e+22, 'cm^3/(mol*s)'),
                n = -2.18,
                Ea = (14800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.4e+27, 'cm^3/(mol*s)'),
                n = -3.58,
                Ea = (21200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 618,
    label = "c3h4-p + h <=> c3h5-s",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1e+25, 'cm^3/(mol*s)'), n=-5, Ea=(1800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (5.5e+28, 'cm^3/(mol*s)'),
                n = -5.74,
                Ea = (4300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1e+34, 'cm^3/(mol*s)'), n=-6.88, Ea=(8900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (9.7e+37, 'cm^3/(mol*s)'),
                n = -7.63,
                Ea = (13800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 619,
    label = "c3h4-p + h <=> c3h5-a",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+60, 'cm^3/(mol*s)'),
                n = -14.56,
                Ea = (28100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.91e+60, 'cm^3/(mol*s)'),
                n = -14.37,
                Ea = (31644, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.04e+60, 'cm^3/(mol*s)'),
                n = -14.19,
                Ea = (32642, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.02e+59, 'cm^3/(mol*s)'),
                n = -13.89,
                Ea = (33953, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.2e+59, 'cm^3/(mol*s)'),
                n = -13.61,
                Ea = (34900, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+55, 'cm^3/(mol*s)'),
                n = -12.07,
                Ea = (37500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 620,
    label = "c3h4-p + h <=> c3h3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 621,
    label = "c3h4-p + c3h3 <=> c3h4-a + c3h3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 622,
    label = "c3h4-p + o <=> hcco + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 623,
    label = "c3h4-p + o <=> c2h4 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(2250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 624,
    label = "c3h4-p + oh <=> c3h3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+06, 'cm^3/(mol*s)'), n=2, Ea=(100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 625,
    label = "c3h4-p + c2h <=> c2h2 + c3h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 626,
    label = "c3h4-p + ch3 <=> c3h3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 627,
    label = "c2h2 + ch3 <=> c3h4-p + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.5e+06, 'cm^3/(mol*s)'),
                n = 1.86,
                Ea = (11600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.56e+09, 'cm^3/(mol*s)'),
                n = 1.1,
                Ea = (13644, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.07e+10, 'cm^3/(mol*s)'),
                n = 0.85,
                Ea = (14415, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.51e+11, 'cm^3/(mol*s)'),
                n = 0.56,
                Ea = (15453, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+12, 'cm^3/(mol*s)'),
                n = 0.39,
                Ea = (16200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.1e+12, 'cm^3/(mol*s)'),
                n = 0.37,
                Ea = (18100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 628,
    label = "cc3h4 <=> c3h4-a",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 0.4, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.3e+39, 's^-1'), n=-8.81, Ea=(47800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+40, 's^-1'), n=-9.07, Ea=(48831, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.89e+41, 's^-1'), n=-9.17, Ea=(49594, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.81e+41, 's^-1'), n=-9.15, Ea=(50073, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.33e+41, 's^-1'), n=-8.93, Ea=(50475, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.2e+40, 's^-1'), n=-8.6, Ea=(50600, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.6e+35, 's^-1'), n=-6.64, Ea=(49500, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 629,
    label = "c3h3 + h <=> c3h4-p",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 630,
    label = "c3h3 + h <=> c3h4-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 631,
    label = "c2h + ch3 <=> c3h4-p",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 632,
    label = "c3h3 + ho2 <=> c3h4-p + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 633,
    label = "c3h4-p + ho2 => c2h4 + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 634,
    label = "c3h4-p + oh <=> ch2co + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0005, 'cm^3/(mol*s)'), n=4.5, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 635,
    label = "c3h4-p + o <=> c2h3 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(2010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 636,
    label = "c3h4-p + o <=> c3h3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.65e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 637,
    label = "c3h4-p + c2h3 <=> c3h3 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 638,
    label = "c3h4-p + c3h5-a <=> c3h3 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 639,
    label = "c3h3 + o <=> ch2o + c2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 640,
    label = "c3h3 + o2 <=> ch2co + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 641,
    label = "c3h3 + ho2 => oh + co + c2h3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 642,
    label = "c3h3 + hco <=> c3h4-a + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 643,
    label = "c3h3 + hco <=> c3h4-p + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 644,
    label = "c2h5 + c2h <=> c3h3 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 645,
    label = "c3h4-a + ho2 => c2h4 + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 646,
    label = "c3h4-a + ho2 <=> c3h3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 647,
    label = "c2h2 + ch3 <=> c3h4-a + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 2, 5, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.4e+09, 'cm^3/(mol*s)'),
                n = 0.91,
                Ea = (20700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.14e+09, 'cm^3/(mol*s)'),
                n = 0.86,
                Ea = (22153, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.33e+10, 'cm^3/(mol*s)'),
                n = 0.75,
                Ea = (22811, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.2e+10, 'cm^3/(mol*s)'),
                n = 0.54,
                Ea = (23950, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.1e+11, 'cm^3/(mol*s)'),
                n = 0.35,
                Ea = (25000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.3e+12, 'cm^3/(mol*s)'),
                n = 0.11,
                Ea = (28500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 648,
    label = "ch3chco + oh <=> c2h5 + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 649,
    label = "ch3chco + oh <=> sc2h4oh + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 650,
    label = "ch3chco + h <=> c2h5 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 651,
    label = "ch3chco + o <=> ch3cho + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 652,
    label = "nc3h7 + ho2 <=> nc3h7o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 653,
    label = "ic3h7 + ho2 <=> ic3h7o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 654,
    label = "ch3o2 + nc3h7 <=> ch3o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 655,
    label = "ch3o2 + ic3h7 <=> ch3o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 656,
    label = "nc3h7 + o2 <=> nc3h7o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 657,
    label = "ic3h7 + o2 <=> ic3h7o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 658,
    label = "nc3h7o2 + ch2o <=> nc3h7o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 659,
    label = "nc3h7o2 + ch3cho <=> nc3h7o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 660,
    label = "ic3h7o2 + ch2o <=> ic3h7o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 661,
    label = "ic3h7o2 + ch3cho <=> ic3h7o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 662,
    label = "nc3h7o2 + ho2 <=> nc3h7o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 663,
    label = "ic3h7o2 + ho2 <=> ic3h7o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 664,
    label = "c2h4 + nc3h7o2 <=> c2h3 + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 665,
    label = "c2h4 + ic3h7o2 <=> c2h3 + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 666,
    label = "ch3oh + nc3h7o2 <=> ch2oh + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 667,
    label = "ch3oh + ic3h7o2 <=> ch2oh + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 668,
    label = "c2h3cho + nc3h7o2 <=> c2h3co + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 669,
    label = "c2h3cho + ic3h7o2 <=> c2h3co + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 670,
    label = "ch4 + nc3h7o2 <=> ch3 + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 671,
    label = "ch4 + ic3h7o2 <=> ch3 + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 672,
    label = "nc3h7o2 + ch3o2 => nc3h7o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 673,
    label = "ic3h7o2 + ch3o2 => ic3h7o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 674,
    label = "h2 + nc3h7o2 <=> h + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 675,
    label = "h2 + ic3h7o2 <=> h + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 676,
    label = "ic3h7o2 + c2h6 <=> ic3h7o2h + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 677,
    label = "nc3h7o2 + c2h6 <=> nc3h7o2h + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 678,
    label = "ic3h7o2 + c2h5cho <=> ic3h7o2h + c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 679,
    label = "nc3h7o2 + c2h5cho <=> nc3h7o2h + c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 680,
    label = "ic3h7o2 + ch3co3 => ic3h7o + ch3co2 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 681,
    label = "nc3h7o2 + ch3co3 => nc3h7o + ch3co2 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 682,
    label = "ic3h7o2 + c2h5o2 => ic3h7o + c2h5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 683,
    label = "nc3h7o2 + c2h5o2 => nc3h7o + c2h5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 684,
    label = "ic3h7o2 + ic3h7o2 => o2 + ic3h7o + ic3h7o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 685,
    label = "nc3h7o2 + nc3h7o2 => o2 + nc3h7o + nc3h7o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 686,
    label = "ic3h7o2 + nc3h7o2 => ic3h7o + nc3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 687,
    label = "ic3h7o2 + ch3 <=> ic3h7o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 688,
    label = "ic3h7o2 + c2h5 <=> ic3h7o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 689,
    label = "ic3h7o2 + ic3h7 <=> ic3h7o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 690,
    label = "ic3h7o2 + nc3h7 <=> ic3h7o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 691,
    label = "ic3h7o2 + c3h5-a <=> ic3h7o + c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 692,
    label = "nc3h7o2 + ch3 <=> nc3h7o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 693,
    label = "nc3h7o2 + c2h5 <=> nc3h7o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 694,
    label = "nc3h7o2 + ic3h7 <=> nc3h7o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 695,
    label = "nc3h7o2 + nc3h7 <=> nc3h7o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 696,
    label = "nc3h7o2 + c3h5-a <=> nc3h7o + c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 697,
    label = "nc3h7o2h <=> nc3h7o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 698,
    label = "ic3h7o + oh <=> ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 699,
    label = "c2h5 + ch2o <=> nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(3496, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 700,
    label = "c2h5cho + h <=> nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(6260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 701,
    label = "ch3 + ch3cho <=> ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9256, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 702,
    label = "ch3coch3 + h <=> ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 703,
    label = "ic3h7o + o2 <=> ch3coch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.09e+09, 'cm^3/(mol*s)'), n=0, Ea=(390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 704,
    label = "nc3h7o2 <=> c3h6ooh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 705,
    label = "nc3h7o2 <=> c3h6ooh1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.125e+11, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 706,
    label = "ic3h7o2 <=> c3h6ooh2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+12, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 707,
    label = "ic3h7o2 <=> c3h6ooh2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+35, 's^-1'), n=-6.96, Ea=(48880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 708,
    label = "c3h6ooh1-2 <=> c3h6o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 709,
    label = "c3h6ooh1-3 <=> c3h6o1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 710,
    label = "c3h6ooh2-1 <=> c3h6o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 711,
    label = "c3h6 + ho2 <=> c3h6ooh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 712,
    label = "c3h6 + ho2 <=> c3h6ooh2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 713,
    label = "c3h6ooh1-3 => oh + ch2o + c2h4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.035e+15, 's^-1'), n=-0.79, Ea=(27400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 714,
    label = "c3h6ooh2-1 <=> c2h3ooh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.54e+27, 's^-1'), n=-5.14, Ea=(38320, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 715,
    label = "c3h6ooh1-2 => c2h4 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.31e+33, 's^-1'), n=-7.01, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 716,
    label = "c3h6ooh2-2 <=> ch3coch3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 717,
    label = "c3h6ooh1-2 + o2 <=> c3h6ooh1-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 718,
    label = "c3h6ooh1-3 + o2 <=> c3h6ooh1-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 719,
    label = "c3h6ooh2-1 + o2 <=> c3h6ooh2-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 720,
    label = "c3h6ooh1-2o2 <=> c3ket12 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 721,
    label = "c3h6ooh1-3o2 <=> c3ket13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 722,
    label = "c3h6ooh2-1o2 <=> c3ket21 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(23850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 723,
    label = "c3h6ooh2-1o2 <=> c3h51-2,3ooh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.125e+11, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 724,
    label = "c3h6ooh1-2o2 <=> c3h51-2,3ooh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 725,
    label = "c3h51-2,3ooh <=> ac3h5ooh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.56e+13, 's^-1'), n=-0.49, Ea=(17770, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 726,
    label = "c3h6ooh1-3o2 <=> c3h52-1,3ooh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 727,
    label = "c3h52-1,3ooh <=> ac3h5ooh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+14, 's^-1'), n=-0.63, Ea=(17250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 728,
    label = "c3ket12 => ch3cho + hco + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.45e+15, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 729,
    label = "c3ket13 => ch2o + ch2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 730,
    label = "c3ket21 => ch2o + ch3co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 731,
    label = "c3h5o + oh <=> ac3h5ooh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 732,
    label = "c3h5o <=> c2h3cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(29100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 733,
    label = "c2h3 + ch2o <=> c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 734,
    label = "c3h5o + o2 <=> c2h3cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 735,
    label = "c2h3ooh <=> ch2cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.4e+14, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 736,
    label = "c3h6o1-2 <=> c2h4 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 737,
    label = "c3h6o1-2 + oh => ch2o + c2h3 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 738,
    label = "c3h6o1-2 + h => ch2o + c2h3 + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 739,
    label = "c3h6o1-2 + o => ch2o + c2h3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 740,
    label = "c3h6o1-2 + ho2 => ch2o + c2h3 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 741,
    label = "c3h6o1-2 + ch3o2 => ch2o + c2h3 + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 742,
    label = "c3h6o1-2 + ch3 => ch2o + c2h3 + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 743,
    label = "c3h6o1-3 <=> c2h4 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+14, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 744,
    label = "c3h6o1-3 + oh => ch2o + c2h3 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 745,
    label = "c3h6o1-3 + o => ch2o + c2h3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.43e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 746,
    label = "c3h6o1-3 + h => ch2o + c2h3 + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.63e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 747,
    label = "c3h6o1-3 + ch3o2 => ch2o + c2h3 + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 748,
    label = "c3h6o1-3 + ho2 => ch2o + c2h3 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 749,
    label = "c3h6o1-3 + ch3 => ch2o + c2h3 + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 750,
    label = "ic3h7o2 <=> c3h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.196e+43, 's^-1'), n=-9.43, Ea=(41530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 751,
    label = "nc3h7o2 <=> c3h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 752,
    label = "c4h10 <=> c2h5 + c2h5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3554e+37, 's^-1'), n=-6.036, Ea=(92929, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.72e+18, 'cm^3/(mol*s)'), n=0, Ea=(49578, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.079982,
        T3 = (1e-20, 'K'),
        T1 = (32428, 'K'),
        T2 = (4858.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 753,
    label = "c4h10 <=> nc3h7 + ch3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.5998e+52, 's^-1'),
            n = -10.626,
            Ea = (100330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(5.34e+17, 'cm^3/(mol*s)'), n=0, Ea=(42959, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.095015,
        T3 = (1e-20, 'K'),
        T1 = (5347.6, 'K'),
        T2 = (4325.6, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 754,
    label = "pc4h9 + h <=> c4h10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 755,
    label = "sc4h9 + h <=> c4h10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.61e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 756,
    label = "c4h10 + o2 <=> pc4h9 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 757,
    label = "c4h10 + o2 <=> sc4h9 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 758,
    label = "c4h10 + c3h5-a <=> pc4h9 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 759,
    label = "c4h10 + c3h5-a <=> sc4h9 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+11, 'cm^3/(mol*s)'), n=0, Ea=(16400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 760,
    label = "c4h10 + c2h5 <=> pc4h9 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+11, 'cm^3/(mol*s)'), n=0, Ea=(12300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 761,
    label = "c4h10 + c2h5 <=> sc4h9 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 762,
    label = "c4h10 + c2h3 <=> pc4h9 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 763,
    label = "c4h10 + c2h3 <=> sc4h9 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(16800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 764,
    label = "c4h10 + ch3 <=> pc4h9 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 765,
    label = "c4h10 + ch3 <=> sc4h9 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 766,
    label = "c4h10 + h <=> pc4h9 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 767,
    label = "c4h10 + h <=> sc4h9 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 768,
    label = "c4h10 + oh <=> pc4h9 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 769,
    label = "c4h10 + oh <=> sc4h9 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.34e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 770,
    label = "c4h10 + o <=> pc4h9 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+14, 'cm^3/(mol*s)'), n=0, Ea=(7850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 771,
    label = "c4h10 + o <=> sc4h9 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 772,
    label = "c4h10 + ho2 <=> pc4h9 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 773,
    label = "c4h10 + ho2 <=> sc4h9 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 774,
    label = "c4h10 + ch3o <=> pc4h9 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 775,
    label = "c4h10 + ch3o <=> sc4h9 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 776,
    label = "c4h10 + c2h5o <=> pc4h9 + c2h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 777,
    label = "c4h10 + c2h5o <=> sc4h9 + c2h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 778,
    label = "c4h10 + pc4h9 <=> sc4h9 + c4h10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 779,
    label = "c4h10 + ch3co3 <=> pc4h9 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 780,
    label = "c4h10 + ch3co3 <=> sc4h9 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 781,
    label = "c4h10 + o2cho <=> pc4h9 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 782,
    label = "c4h10 + o2cho <=> sc4h9 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 783,
    label = "ch3o2 + c4h10 <=> ch3o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 784,
    label = "ch3o2 + c4h10 <=> ch3o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20.37, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 785,
    label = "c2h5o2 + c4h10 <=> c2h5o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 786,
    label = "c2h5o2 + c4h10 <=> c2h5o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 787,
    label = "nc3h7o2 + c4h10 <=> nc3h7o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 788,
    label = "nc3h7o2 + c4h10 <=> nc3h7o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 789,
    label = "ic3h7o2 + c4h10 <=> ic3h7o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 790,
    label = "ic3h7o2 + c4h10 <=> ic3h7o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 791,
    label = "pc4h9o2 + c3h8 <=> pc4h9o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 792,
    label = "pc4h9o2 + c3h8 <=> pc4h9o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 793,
    label = "pc4h9o2 + c4h10 <=> pc4h9o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 794,
    label = "pc4h9o2 + c4h10 <=> pc4h9o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 795,
    label = "sc4h9o2 + c3h8 <=> sc4h9o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 796,
    label = "sc4h9o2 + c3h8 <=> sc4h9o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 797,
    label = "sc4h9o2 + c4h10 <=> sc4h9o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 798,
    label = "sc4h9o2 + c4h10 <=> sc4h9o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 799,
    label = "pc4h9 <=> sc4h9",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(37300, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.8e+10, 's^-1'), n=0.67, Ea=(36600, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 800,
    label = "c2h5 + c2h4 <=> pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13200, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 801,
    label = "c3h6 + ch3 <=> sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 802,
    label = "c4h8-1 + h <=> pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 803,
    label = "c4h8-2 + h <=> sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 804,
    label = "c4h8-1 + h <=> sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 805,
    label = "pc4h9 + o2 <=> c4h8-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 806,
    label = "sc4h9 + o2 <=> c4h8-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.535, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 807,
    label = "sc4h9 + o2 <=> c4h8-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 808,
    label = "c2h3 + c2h5 <=> c4h8-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 809,
    label = "c3h5-a + ch3 <=> c4h8-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1e+14, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118.4, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 810,
    label = "h + c4h71-3 <=> c4h8-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 811,
    label = "c4h8-1 + o2 <=> c4h71-3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 812,
    label = "c4h8-1 + o <=> c4h71-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 813,
    label = "c4h8-2 + o <=> c4h71-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.19e+11, 'cm^3/(mol*s)'),
        n = 0.81,
        Ea = (7550, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 814,
    label = "c4h8-1 + h <=> c4h71-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 815,
    label = "c4h8-1 + h <=> c4h71-4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665100, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 816,
    label = "c4h8-1 + oh <=> c4h71-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(900000, 'cm^3/(mol*s)'), n=2, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 817,
    label = "c4h8-1 + oh <=> c4h71-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.22e+06, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 818,
    label = "c4h8-1 + oh <=> c4h71-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 819,
    label = "c4h8-1 + oh <=> c4h71-4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 820,
    label = "c4h8-1 + ch3 <=> c4h71-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 821,
    label = "c4h8-1 + ch3 <=> c4h71-4 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 822,
    label = "c4h8-1 + ho2 <=> c4h71-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 823,
    label = "c4h8-1 + ho2 <=> c4h71-4 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2380, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 824,
    label = "c4h8-1 + ch3o2 <=> c4h71-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=0.7, Ea=(5884, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 825,
    label = "c4h8-1 + ch3o2 <=> c4h71-4 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2380, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 826,
    label = "c4h8-1 + ch3o <=> c4h71-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 827,
    label = "c4h8-1 + ch3o <=> c4h71-4 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 828,
    label = "c4h8-1 + ch3co3 <=> c4h71-3 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 829,
    label = "c4h8-1 + c3h5-a <=> c4h71-3 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(12400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 830,
    label = "c4h71-3 + c4h71-3 <=> c4h8-1 + c4h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 831,
    label = "c4h8-1 + c2h5o2 <=> c4h71-3 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 832,
    label = "c4h8-1 + nc3h7o2 <=> c4h71-3 + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 833,
    label = "c4h8-1 + ic3h7o2 <=> c4h71-3 + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 834,
    label = "c4h8-1 + pc4h9o2 <=> c4h71-3 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 835,
    label = "c4h8-1 + sc4h9o2 <=> c4h71-3 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 836,
    label = "c4h8-1 + ch3o2 <=> c4h8o1-2 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 837,
    label = "h + c4h71-3 <=> c4h8-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 838,
    label = "c4h8-2 + o2 <=> c4h71-3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(39390, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 839,
    label = "c4h8-2 + h <=> c4h71-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44400, 'cm^3/(mol*s)'), n=2.81, Ea=(4414, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 840,
    label = "c4h8-2 + oh <=> c4h71-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+08, 'cm^3/(mol*s)'), n=1.4, Ea=(1250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 841,
    label = "c4h8-2 + ch3 <=> c4h71-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.14, 'cm^3/(mol*s)'), n=3.57, Ea=(7642, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 842,
    label = "c4h8-2 + ho2 <=> c4h71-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59400, 'cm^3/(mol*s)'), n=2.57, Ea=(16140, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 843,
    label = "c4h8-2 + ch3o2 <=> c4h71-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59400, 'cm^3/(mol*s)'), n=2.57, Ea=(16140, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 844,
    label = "c4h8-2 + ch3o <=> c4h71-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 845,
    label = "c4h8-2 + c2h5o2 <=> c4h71-3 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 846,
    label = "c4h8-2 + nc3h7o2 <=> c4h71-3 + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 847,
    label = "c4h8-2 + ic3h7o2 <=> c4h71-3 + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 848,
    label = "c4h8-2 + pc4h9o2 <=> c4h71-3 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 849,
    label = "c4h8-2 + sc4h9o2 <=> c4h71-3 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 850,
    label = "c4h8-1 + ho2 <=> c4h8o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(14340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 851,
    label = "c4h8-2 + ho2 <=> c4h8o2-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(12310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 852,
    label = "c4h8-2 + ch3o2 <=> c4h8o2-3 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(12310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 853,
    label = "c2h2 + c2h5 <=> c4h71-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 854,
    label = "c3h4-a + ch3 <=> c4h71-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 855,
    label = "c2h4 + c2h3 <=> c4h71-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 856,
    label = "c3h4-p + ch3 <=> c4h72-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 857,
    label = "c4h6 + h <=> c4h71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(1300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 858,
    label = "c4h71-3 + c2h5 <=> c4h8-1 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(-131, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 859,
    label = "c4h71-3 + ch3o <=> c4h8-1 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 860,
    label = "c4h71-3 + o <=> c2h3cho + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 861,
    label = "c4h71-3 + ho2 <=> c4h7o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 862,
    label = "c4h71-3 + ch3o2 <=> c4h7o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 863,
    label = "c3h5-a + c4h71-3 <=> c3h6 + c4h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 864,
    label = "c4h71-3 + o2 <=> c4h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+09, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 865,
    label = "h + c4h71-3 <=> c4h6 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 866,
    label = "c2h5 + c4h71-3 <=> c4h6 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 867,
    label = "c2h3 + c4h71-3 <=> c2h4 + c4h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 868,
    label = "c4h71-3 + c2h5o2 <=> c4h7o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 869,
    label = "ic3h7o2 + c4h71-3 <=> ic3h7o + c4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 870,
    label = "nc3h7o2 + c4h71-3 <=> nc3h7o + c4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 871,
    label = "c4h7o <=> ch3cho + c2h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 872,
    label = "c4h7o <=> c2h3cho + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+14, 's^-1'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 873,
    label = "c4h6 <=> c4h5-i + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+36, 's^-1'), n=-6.27, Ea=(112353, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 874,
    label = "c4h6 <=> c4h5-n + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+44, 's^-1'), n=-8.62, Ea=(123608, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 875,
    label = "c4h6 <=> c4h4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+15, 's^-1'), n=0, Ea=(94700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 876,
    label = "c4h6 + h <=> c4h5-n + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+06, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 877,
    label = "c4h6 + h <=> c4h5-i + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.53, Ea=(9240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 878,
    label = "c4h6 + h <=> c2h4 + c2h3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.46e+30, 'cm^3/(mol*s)'),
                n = -4.34,
                Ea = (21647, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.45e+30, 'cm^3/(mol*s)'),
                n = -4.51,
                Ea = (21877, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 879,
    label = "c4h6 + h <=> c3h4-p + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 880,
    label = "c4h6 + h <=> c3h4-a + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 881,
    label = "c4h6 + o <=> c4h5-n + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(3740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 882,
    label = "c4h6 + o <=> c4h5-i + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(3740, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 883,
    label = "c4h6 + o <=> c2h2 + c2h4o1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 884,
    label = "c4h6 + o <=> ch3chchco + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+07, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 885,
    label = "c4h6 + o <=> c2h3chcho + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 886,
    label = "c4h6 + oh <=> c4h5-n + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(3430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 887,
    label = "c4h6 + oh <=> c4h5-i + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 888,
    label = "c4h6 + ho2 <=> c4h6o25 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 889,
    label = "c4h6 + ho2 <=> c2h3choch2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 890,
    label = "c4h6 + ch3 <=> c4h5-n + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 891,
    label = "c4h6 + ch3 <=> c4h5-i + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 892,
    label = "c4h6 + c2h3 <=> c4h5-n + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(22800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 893,
    label = "c4h6 + c2h3 <=> c4h5-i + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(19800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 894,
    label = "c4h6 + c3h3 <=> c4h5-n + c3h4-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(22500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 895,
    label = "c4h6 + c3h3 <=> c4h5-i + c3h4-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 896,
    label = "c4h6 + c3h5-a <=> c4h5-n + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(22500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 897,
    label = "c4h6 + c3h5-a <=> c4h5-i + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 898,
    label = "c4h71-4 <=> c4h6 + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.48e+53, 's^-1'), n=-12.3, Ea=(52000, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.85e+48, 's^-1'), n=-10.5, Ea=(51770, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 899,
    label = "c2h3 + c2h2 <=> c4h4 + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7.2e+13, 'cm^3/(mol*s)'),
                n = -0.48,
                Ea = (6100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(5e+14, 'cm^3/(mol*s)'), n=-0.71, Ea=(6700, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.6e+16, 'cm^3/(mol*s)'),
                n = -1.25,
                Ea = (8400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2e+18, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (10600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.9e+16, 'cm^3/(mol*s)'),
                n = -1.13,
                Ea = (11800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 900,
    label = "c2h3 + c2h2 <=> c4h5-n",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+31, 'cm^3/(mol*s)'),
                n = -7.14,
                Ea = (5600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+32, 'cm^3/(mol*s)'),
                n = -7.33,
                Ea = (6200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+31, 'cm^3/(mol*s)'),
                n = -6.95,
                Ea = (5600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.3e+38, 'cm^3/(mol*s)'),
                n = -8.76,
                Ea = (12000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.1e+37, 'cm^3/(mol*s)'),
                n = -8.09,
                Ea = (13400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 901,
    label = "c2h3 + c2h2 <=> c4h5-i",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(5e+34, 'cm^3/(mol*s)'), n=-8.42, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.1e+36, 'cm^3/(mol*s)'),
                n = -8.78,
                Ea = (9100, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1e+37, 'cm^3/(mol*s)'), n=-8.77, Ea=(9800, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.6e+46, 'cm^3/(mol*s)'),
                n = -10.98,
                Ea = (18600, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.1e+53, 'cm^3/(mol*s)'),
                n = -12.64,
                Ea = (28800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 902,
    label = "c2h3 + c2h3 <=> c4h6",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.12, 1], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7e+57, 'cm^3/(mol*s)'),
                n = -13.82,
                Ea = (17629, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+52, 'cm^3/(mol*s)'),
                n = -11.97,
                Ea = (16056, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+42, 'cm^3/(mol*s)'),
                n = -8.84,
                Ea = (12483, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 903,
    label = "c2h3 + c2h3 <=> c4h5-i + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.12, 1], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.5e+30, 'cm^3/(mol*s)'),
                n = -4.95,
                Ea = (12958, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.2e+28, 'cm^3/(mol*s)'),
                n = -4.49,
                Ea = (14273, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.2e+22, 'cm^3/(mol*s)'),
                n = -2.44,
                Ea = (13654, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 904,
    label = "c2h3 + c2h3 <=> c4h5-n + h",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.12, 1], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.1e+24, 'cm^3/(mol*s)'),
                n = -3.28,
                Ea = (12395, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.6e+24, 'cm^3/(mol*s)'),
                n = -3.38,
                Ea = (14650, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.4e+20, 'cm^3/(mol*s)'),
                n = -2.04,
                Ea = (15361, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 905,
    label = "c4h5-n <=> c4h5-i",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.4e+60, 's^-1'), n=-16.08, Ea=(47500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+62, 's^-1'), n=-16.38, Ea=(49600, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.9e+66, 's^-1'), n=-17.26, Ea=(55400, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59100, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+60, 's^-1'), n=-14.46, Ea=(58600, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 906,
    label = "c4h5-n + h <=> c4h5-i + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 907,
    label = "c4h5-n + h <=> c4h4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 908,
    label = "c4h5-n + oh <=> c4h4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 909,
    label = "c4h5-n + hco <=> c4h6 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 910,
    label = "c4h5-n + ho2 => c2h3 + ch2co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 911,
    label = "c4h5-n + h2o2 <=> c4h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+10, 'cm^3/(mol*s)'), n=0, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 912,
    label = "c4h5-n + ho2 <=> c4h6 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 913,
    label = "c4h5-n + o2 <=> c2h3chcho + o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0.29, Ea=(11, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 914,
    label = "c4h5-n + o2 <=> hco + c2h3cho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.2e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 915,
    label = "c4h5-i + h <=> c4h4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 916,
    label = "c4h5-i + h <=> c3h3 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 917,
    label = "c4h5-i + oh <=> c4h4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 918,
    label = "c4h5-i + hco <=> c4h6 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 919,
    label = "c4h5-i + ho2 <=> c4h6 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 920,
    label = "c4h5-i + ho2 => c2h3 + ch2co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 921,
    label = "c4h5-i + h2o2 <=> c4h6 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+10, 'cm^3/(mol*s)'), n=0, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 922,
    label = "c4h5-i + o2 <=> ch2co + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 923,
    label = "c4h5-2 <=> c4h5-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+67, 's^-1'), n=-16.89, Ea=(59100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 924,
    label = "c4h5-2 + h <=> c4h5-i + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+26, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (17423, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 925,
    label = "c4h5-2 + ho2 => oh + c2h2 + ch3co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 926,
    label = "c4h5-2 + o2 <=> ch3co + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+10, 'cm^3/(mol*s)'), n=0, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 927,
    label = "c4h612 <=> c4h5-i + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+15, 's^-1'), n=0, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 928,
    label = "c4h612 + h <=> c4h6 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 929,
    label = "c4h612 + h <=> c4h5-i + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 930,
    label = "c4h612 + h <=> c3h4-a + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 931,
    label = "c4h612 + h <=> c3h4-p + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 932,
    label = "c4h612 + ch3 <=> c4h5-i + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+13, 'cm^3/(mol*s)'), n=0, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 933,
    label = "c4h612 + o <=> ch2co + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+08, 'cm^3/(mol*s)'), n=1.65, Ea=(327, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 934,
    label = "c4h612 + o <=> c4h5-i + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+11, 'cm^3/(mol*s)'), n=0.7, Ea=(5880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 935,
    label = "c4h612 + oh <=> c4h5-i + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 936,
    label = "c4h612 <=> c4h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 937,
    label = "c4h6-2 <=> c4h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(65000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 938,
    label = "c4h6-2 <=> c4h612",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 's^-1'), n=0, Ea=(67000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 939,
    label = "c4h6-2 + h <=> c4h612 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 940,
    label = "c4h6-2 + h <=> c4h5-2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(340000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 941,
    label = "c4h6-2 + h <=> ch3 + c3h4-p",
    degeneracy = 1,
    kinetics = Arrhenius(A=(260000, 'cm^3/(mol*s)'), n=2.5, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 942,
    label = "c4h6-2 <=> h + c4h5-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+15, 's^-1'), n=0, Ea=(87300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 943,
    label = "c4h6-2 + ch3 <=> c4h5-2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+14, 'cm^3/(mol*s)'), n=0, Ea=(18500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 944,
    label = "c2h3choch2 <=> c4h6o23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 's^-1'), n=0, Ea=(50600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 945,
    label = "c4h6o23 <=> ch3chchcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.95e+13, 's^-1'), n=0, Ea=(49400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 946,
    label = "c4h6o23 <=> c2h4 + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.75e+15, 's^-1'), n=0, Ea=(69300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 947,
    label = "c4h6o23 <=> c2h2 + c2h4o1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(75800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 948,
    label = "c4h6o25 <=> c4h4o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 's^-1'), n=0, Ea=(48500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 949,
    label = "c4h4o <=> co + c3h4-p",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+15, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 950,
    label = "c4h4o <=> c2h2 + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+14, 's^-1'), n=0, Ea=(77500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 951,
    label = "ch3chchcho <=> c3h6 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+14, 's^-1'), n=0, Ea=(69000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 952,
    label = "ch3chchcho + h <=> c2h3chcho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(170000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 953,
    label = "ch3chchcho + h <=> ch3chchco + h2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(100000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 954,
    label = "ch3chchcho + h <=> ch3 + c2h3cho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 955,
    label = "ch3chchcho + h <=> c3h6 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 956,
    label = "ch3chchcho + ch3 <=> c2h3chcho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 957,
    label = "ch3chchcho + ch3 <=> ch3chchco + ch4",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.1, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 958,
    label = "ch3chchcho + c2h3 <=> c2h3chcho + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(4682, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 959,
    label = "ch3chchcho + c2h3 <=> ch3chchco + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.11, 'cm^3/(mol*s)'), n=3.5, Ea=(4682, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 960,
    label = "ch3chchco <=> c3h5-s + co",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 961,
    label = "ch3chchco + h <=> ch3chchcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 962,
    label = "c2h3chcho <=> c3h5-a + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 963,
    label = "c2h3chcho + h <=> ch3chchcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 964,
    label = "c4h4 + h <=> c4h5-n",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.2e+51, 'cm^3/(mol*s)'),
                n = -12.57,
                Ea = (12300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.2e+50, 'cm^3/(mol*s)'),
                n = -12.34,
                Ea = (12500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.1e+50, 'cm^3/(mol*s)'),
                n = -11.94,
                Ea = (13400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.3e+51, 'cm^3/(mol*s)'),
                n = -11.92,
                Ea = (16500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.2e+45, 'cm^3/(mol*s)'),
                n = -10.08,
                Ea = (15800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 965,
    label = "c4h4 + h <=> c4h5-i",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.0263, 0.12, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (6.1e+53, 'cm^3/(mol*s)'),
                n = -13.19,
                Ea = (14200, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.6e+52, 'cm^3/(mol*s)'),
                n = -12.85,
                Ea = (14300, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.1e+52, 'cm^3/(mol*s)'),
                n = -12.44,
                Ea = (15500, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.9e+51, 'cm^3/(mol*s)'),
                n = -11.92,
                Ea = (17700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e+48, 'cm^3/(mol*s)'),
                n = -10.58,
                Ea = (18800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 966,
    label = "c4h4 + h <=> c4h3-n + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (12240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 967,
    label = "c4h4 + h <=> c4h3-i + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(333000, 'cm^3/(mol*s)'), n=2.53, Ea=(9240, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 968,
    label = "c4h4 + oh <=> c4h3-n + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+07, 'cm^3/(mol*s)'), n=2, Ea=(3430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 969,
    label = "c4h4 + oh <=> c4h3-i + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+07, 'cm^3/(mol*s)'), n=2, Ea=(430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 970,
    label = "c4h4 + o <=> c3h3 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+08, 'cm^3/(mol*s)'), n=1.45, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 971,
    label = "c3h3 + hcco <=> c4h4 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 972,
    label = "c3h3 + ch <=> c4h3-i + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 973,
    label = "c3h3 + ch2 <=> c4h4 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 974,
    label = "c3h3 + ch3 <=> c4h612",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+57, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (9769.8, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, '[H][H]': 2, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 975,
    label = "c2h2 + c2h <=> c4h3-n",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.3e+10, 'cm^3/(mol*s)'),
            n = 0.899,
            Ea = (-363, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.24e+31, 'cm^6/(mol^2*s)'),
            n = -4.718,
            Ea = (1871, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (100, 'K'),
        T1 = (5613, 'K'),
        T2 = (13387, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 976,
    label = "c4h3-n <=> c4h3-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1e+43, 's^-1'), n=-9.49, Ea=(53000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 977,
    label = "c4h3-n + h <=> c4h3-i + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -1.67,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 978,
    label = "c4h3-n + h <=> c2h2 + h2cc",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+25, 'cm^3/(mol*s)'),
        n = -3.34,
        Ea = (10014, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 979,
    label = "c4h3-n + h <=> c4h4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+47, 'cm^3/(mol*s)'),
        n = -10.26,
        Ea = (13070, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 980,
    label = "c4h3-n + h <=> c4h2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 981,
    label = "c4h3-n + oh <=> c4h2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 982,
    label = "c2h2 + c2h <=> c4h3-i",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.3e+10, 'cm^3/(mol*s)'),
            n = 0.899,
            Ea = (-363, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.24e+31, 'cm^6/(mol^2*s)'),
            n = -4.718,
            Ea = (1871, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (100, 'K'),
        T1 = (5613, 'K'),
        T2 = (13387, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 983,
    label = "c4h3-i + h <=> c2h2 + h2cc",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+23, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (10780, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 984,
    label = "c4h3-i + h <=> c4h4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+43, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (12120, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 985,
    label = "c4h3-i + h <=> c4h2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 986,
    label = "c4h3-i + oh <=> c4h2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 987,
    label = "c4h3-i + o2 <=> hcco + ch2co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.86e+16, 'cm^3/(mol*s)'), n=-1.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 988,
    label = "c4h3-i + ch2 <=> c3h4-a + c2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 989,
    label = "c2h2 + c2h <=> c4h2 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 990,
    label = "c4h2 + h <=> c4h3-n",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+42, 'cm^3/(mol*s)'),
        n = -8.72,
        Ea = (15300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 991,
    label = "c4h2 + h <=> c4h3-i",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+30, 'cm^3/(mol*s)'),
        n = -4.92,
        Ea = (10800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 992,
    label = "c4h2 + oh <=> h2c4o + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(-410, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 993,
    label = "h2c4o + h <=> c2h2 + hcco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 994,
    label = "h2c4o + oh <=> ch2co + hcco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 995,
    label = "h2cc + c2h2 <=> c4h4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (350000, 'cm^3/(mol*s)'),
            n = 2.055,
            Ea = (-2400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+60, 'cm^6/(mol^2*s)'),
            n = -12.599,
            Ea = (7417, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.98,
        T3 = (56, 'K'),
        T1 = (580, 'K'),
        T2 = (4164, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 996,
    label = "h2cc + c2h4 <=> c4h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 997,
    label = "c4h8o1-2 + oh => ch2o + c3h5-a + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 998,
    label = "c4h8o1-2 + h => ch2o + c3h5-a + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 999,
    label = "c4h8o1-2 + o => ch2o + c3h5-a + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1000,
    label = "c4h8o1-2 + ho2 => ch2o + c3h5-a + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1001,
    label = "c4h8o1-2 + ch3o2 => ch2o + c3h5-a + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1002,
    label = "c4h8o1-2 + ch3 => ch2o + c3h5-a + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1003,
    label = "c4h8o1-3 + oh => ch2o + c3h5-a + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1004,
    label = "c4h8o1-3 + h => ch2o + c3h5-a + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1005,
    label = "c4h8o1-3 + o => ch2o + c3h5-a + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1006,
    label = "c4h8o1-3 + ho2 => ch2o + c3h5-a + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1007,
    label = "c4h8o1-3 + ch3o2 => ch2o + c3h5-a + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1008,
    label = "c4h8o1-3 + ch3 => ch2o + c3h5-a + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1009,
    label = "c4h8o1-4 + oh => ch2o + c3h5-a + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1010,
    label = "c4h8o1-4 + h => ch2o + c3h5-a + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1011,
    label = "c4h8o1-4 + o => ch2o + c3h5-a + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1012,
    label = "c4h8o1-4 + ho2 => ch2o + c3h5-a + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1013,
    label = "c4h8o1-4 + ch3o2 => ch2o + c3h5-a + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1014,
    label = "c4h8o1-4 + ch3 => ch2o + c3h5-a + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1015,
    label = "c4h8o2-3 + oh => ch2o + c3h5-a + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1016,
    label = "c4h8o2-3 + h => ch2o + c3h5-a + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1017,
    label = "c4h8o2-3 + o => ch2o + c3h5-a + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1018,
    label = "c4h8o2-3 + ho2 => ch2o + c3h5-a + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1019,
    label = "c4h8o2-3 + ch3o2 => ch2o + c3h5-a + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1020,
    label = "c4h8o2-3 + ch3 => ch2o + c3h5-a + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1021,
    label = "pc4h9 + o2 <=> pc4h9o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1022,
    label = "sc4h9 + o2 <=> sc4h9o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1023,
    label = "sc4h9o2 + ch2o <=> sc4h9o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1024,
    label = "sc4h9o2 + ch3cho <=> sc4h9o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1025,
    label = "sc4h9o2 + ho2 <=> sc4h9o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1026,
    label = "ic3h7o2 + pc4h9 <=> ic3h7o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1027,
    label = "ic3h7o2 + sc4h9 <=> ic3h7o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1028,
    label = "nc3h7o2 + pc4h9 <=> nc3h7o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1029,
    label = "nc3h7o2 + sc4h9 <=> nc3h7o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1030,
    label = "sc4h9o2 + sc4h9o2 => o2 + sc4h9o + sc4h9o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1031,
    label = "sc4h9o2 + nc3h7o2 => sc4h9o + nc3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1032,
    label = "sc4h9o2 + ic3h7o2 => sc4h9o + ic3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1033,
    label = "sc4h9o2 + c2h5o2 => sc4h9o + c2h5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1034,
    label = "sc4h9o2 + ch3o2 => sc4h9o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1035,
    label = "sc4h9o2 + ch3co3 => sc4h9o + ch3co2 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1036,
    label = "h2 + pc4h9o2 <=> h + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1037,
    label = "h2 + sc4h9o2 <=> h + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1038,
    label = "c2h6 + pc4h9o2 <=> c2h5 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1039,
    label = "c2h6 + sc4h9o2 <=> c2h5 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1040,
    label = "pc4h9o2 + c2h5cho <=> pc4h9o2h + c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1041,
    label = "sc4h9o2 + c2h5cho <=> sc4h9o2h + c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1042,
    label = "sc4h9o2 + ch3 <=> sc4h9o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1043,
    label = "sc4h9o2 + c2h5 <=> sc4h9o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1044,
    label = "sc4h9o2 + ic3h7 <=> sc4h9o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1045,
    label = "sc4h9o2 + nc3h7 <=> sc4h9o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1046,
    label = "sc4h9o2 + pc4h9 <=> sc4h9o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1047,
    label = "sc4h9o2 + sc4h9 <=> sc4h9o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1048,
    label = "sc4h9o2 + c3h5-a <=> sc4h9o + c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1049,
    label = "pc4h9o2 + ch2o <=> pc4h9o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1050,
    label = "pc4h9o2 + ch3cho <=> pc4h9o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1051,
    label = "pc4h9o2 + ho2 <=> pc4h9o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1052,
    label = "c3h6 + pc4h9o2 <=> c3h5-a + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1053,
    label = "c3h6 + sc4h9o2 <=> c3h5-a + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1054,
    label = "c2h4 + pc4h9o2 <=> c2h3 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1055,
    label = "c2h4 + sc4h9o2 <=> c2h3 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1056,
    label = "ch3oh + pc4h9o2 <=> ch2oh + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1057,
    label = "ch3oh + sc4h9o2 <=> ch2oh + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1058,
    label = "c2h3cho + pc4h9o2 <=> c2h3co + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1059,
    label = "c2h3cho + sc4h9o2 <=> c2h3co + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1060,
    label = "ch4 + pc4h9o2 <=> ch3 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1061,
    label = "ch4 + sc4h9o2 <=> ch3 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1062,
    label = "c4h71-3 + pc4h9o2 <=> c4h7o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1063,
    label = "c4h71-3 + sc4h9o2 <=> c4h7o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1064,
    label = "h2o2 + pc4h9o2 <=> ho2 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1065,
    label = "h2o2 + sc4h9o2 <=> ho2 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1066,
    label = "pc4h9o2 + pc4h9o2 => o2 + pc4h9o + pc4h9o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1067,
    label = "pc4h9o2 + sc4h9o2 => pc4h9o + sc4h9o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1068,
    label = "pc4h9o2 + nc3h7o2 => pc4h9o + nc3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1069,
    label = "pc4h9o2 + ic3h7o2 => pc4h9o + ic3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1070,
    label = "pc4h9o2 + c2h5o2 => pc4h9o + c2h5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1071,
    label = "pc4h9o2 + ch3o2 => pc4h9o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1072,
    label = "pc4h9o2 + ch3co3 => pc4h9o + ch3co2 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1073,
    label = "pc4h9o2 + ch3 <=> pc4h9o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1074,
    label = "pc4h9o2 + c2h5 <=> pc4h9o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1075,
    label = "pc4h9o2 + ic3h7 <=> pc4h9o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1076,
    label = "pc4h9o2 + nc3h7 <=> pc4h9o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1077,
    label = "pc4h9o2 + pc4h9 <=> pc4h9o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1078,
    label = "pc4h9o2 + sc4h9 <=> pc4h9o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1079,
    label = "pc4h9o2 + c3h5-a <=> pc4h9o + c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1080,
    label = "pc4h9 + ho2 <=> pc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1081,
    label = "sc4h9 + ho2 <=> sc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1082,
    label = "ch3o2 + pc4h9 <=> ch3o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1083,
    label = "ch3o2 + sc4h9 <=> ch3o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1084,
    label = "pc4h9o2h <=> pc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1085,
    label = "sc4h9o + oh <=> sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1086,
    label = "nc3h7 + ch2o <=> pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(3457, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1087,
    label = "ch3 + c2h5cho <=> sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(9043, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1088,
    label = "c2h5 + ch3cho <=> sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+10, 'cm^3/(mol*s)'), n=0, Ea=(6397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1089,
    label = "pc4h9o2 <=> c4h8ooh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(31850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1090,
    label = "pc4h9o2 <=> c4h8ooh1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1091,
    label = "pc4h9o2 <=> c4h8ooh1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(22350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1092,
    label = "sc4h9o2 <=> c4h8ooh2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1093,
    label = "sc4h9o2 <=> c4h8ooh2-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(31850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1094,
    label = "sc4h9o2 <=> c4h8ooh2-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1095,
    label = "pc4h9o2 <=> c4h8-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1096,
    label = "sc4h9o2 <=> c4h8-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.98e+42, 's^-1'), n=-9.43, Ea=(41530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1097,
    label = "sc4h9o2 <=> c4h8-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1098,
    label = "c4h8-1 + ho2 <=> c4h8ooh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1099,
    label = "c4h8-1 + ho2 <=> c4h8ooh2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1100,
    label = "c4h8-2 + ho2 <=> c4h8ooh2-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1101,
    label = "c4h8ooh1-2 <=> c4h8o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.38e+12, 's^-1'), n=0, Ea=(15900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1102,
    label = "c4h8ooh1-3 <=> c4h8o1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.04e+11, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1103,
    label = "c4h8ooh1-4 <=> c4h8o1-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+10, 's^-1'), n=0, Ea=(14800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1104,
    label = "c4h8ooh2-1 <=> c4h8o1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 's^-1'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1105,
    label = "c4h8ooh2-3 <=> c4h8o2-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.38e+12, 's^-1'), n=0, Ea=(15900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1106,
    label = "c4h8ooh2-4 <=> c4h8o1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+11, 's^-1'), n=0, Ea=(21900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1107,
    label = "c4h8ooh1-1 <=> nc3h7cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1108,
    label = "c4h8ooh2-2 <=> c2h5coch3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1109,
    label = "c4h8ooh1-3 => oh + ch2o + c3h6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.635e+13, 's^-1'), n=-0.16, Ea=(29900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1110,
    label = "c4h8ooh2-4 => oh + ch3cho + c2h4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.945e+18, 's^-1'), n=-1.63, Ea=(26790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1111,
    label = "c4h8ooh1-2 + o2 <=> c4h8ooh1-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1112,
    label = "c4h8ooh1-3 + o2 <=> c4h8ooh1-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1113,
    label = "c4h8ooh1-4 + o2 <=> c4h8ooh1-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1114,
    label = "c4h8ooh2-1 + o2 <=> c4h8ooh2-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1115,
    label = "c4h8ooh2-3 + o2 <=> c4h8ooh2-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1116,
    label = "c4h8ooh2-4 + o2 <=> c4h8ooh2-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1117,
    label = "c4h8ooh1-2o2 <=> nc4ket12 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1118,
    label = "c4h8ooh1-3o2 <=> nc4ket13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1119,
    label = "c4h8ooh1-4o2 <=> nc4ket14 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(19350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1120,
    label = "c4h8ooh2-1o2 <=> nc4ket21 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(28850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1121,
    label = "c4h8ooh2-3o2 <=> nc4ket23 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(28850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1122,
    label = "c4h8ooh2-4o2 <=> nc4ket24 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1123,
    label = "nc4ket12 => c2h5cho + hco + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1124,
    label = "nc4ket13 => ch3cho + ch2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1125,
    label = "nc4ket14 => ch2ch2cho + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1126,
    label = "nc4ket21 => ch2o + c2h5co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1127,
    label = "nc4ket23 => ch3cho + ch3co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1128,
    label = "nc4ket24 => ch2o + ch3coch2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1129,
    label = "c2h5coch3 + oh <=> ch2ch2coch3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.55e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1130,
    label = "c2h5coch3 + oh <=> ch3chcoch3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(-228, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1131,
    label = "c2h5coch3 + oh <=> c2h5coch2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1132,
    label = "c2h5coch3 + ho2 <=> ch2ch2coch3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1133,
    label = "c2h5coch3 + ho2 <=> ch3chcoch3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(8698, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1134,
    label = "c2h5coch3 + ho2 <=> c2h5coch2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(14690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1135,
    label = "c2h5coch3 + o <=> ch2ch2coch3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1136,
    label = "c2h5coch3 + o <=> ch3chcoch3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.07e+13, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1137,
    label = "c2h5coch3 + o <=> c2h5coch2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(5962, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1138,
    label = "c2h5coch3 + h <=> ch2ch2coch3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.16e+06, 'cm^3/(mol*s)'), n=2, Ea=(7700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1139,
    label = "c2h5coch3 + h <=> ch3chcoch3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.46e+06, 'cm^3/(mol*s)'), n=2, Ea=(3200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1140,
    label = "c2h5coch3 + h <=> c2h5coch2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(6357, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1141,
    label = "c2h5coch3 + o2 <=> ch2ch2coch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(51310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1142,
    label = "c2h5coch3 + o2 <=> ch3chcoch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(41970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1143,
    label = "c2h5coch3 + o2 <=> c2h5coch2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+13, 'cm^3/(mol*s)'), n=0, Ea=(49150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1144,
    label = "c2h5coch3 + ch3 <=> ch2ch2coch3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1145,
    label = "c2h5coch3 + ch3 <=> ch3chcoch3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.74, 'cm^3/(mol*s)'), n=3.46, Ea=(3680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1146,
    label = "c2h5coch3 + ch3 <=> c2h5coch2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62e+11, 'cm^3/(mol*s)'), n=0, Ea=(9630, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1147,
    label = "c2h5coch3 + ch3o <=> ch2ch2coch3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1148,
    label = "c2h5coch3 + ch3o <=> ch3chcoch3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(2771, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1149,
    label = "c2h5coch3 + ch3o <=> c2h5coch2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(4660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1150,
    label = "c2h5coch3 + ch3o2 <=> ch2ch2coch3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(19380, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1151,
    label = "c2h5coch3 + ch3o2 <=> ch3chcoch3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1152,
    label = "c2h5coch3 + ch3o2 <=> c2h5coch2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(17580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1153,
    label = "c2h5coch3 + c2h3 <=> ch2ch2coch3 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1154,
    label = "c2h5coch3 + c2h3 <=> ch3chcoch3 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(3400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1155,
    label = "c2h5coch3 + c2h3 <=> c2h5coch2 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.15e+10, 'cm^3/(mol*s)'), n=0, Ea=(4278, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1156,
    label = "c2h5coch3 + c2h5 <=> ch2ch2coch3 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1157,
    label = "c2h5coch3 + c2h5 <=> ch3chcoch3 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1158,
    label = "c2h5coch3 + c2h5 <=> c2h5coch2 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(11600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1159,
    label = "ch3chcoch3 + o2 <=> ch3choococh3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1160,
    label = "ch3choococh3 <=> ch2choohcoch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.9e+12, 's^-1'), n=0, Ea=(29700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1161,
    label = "c2h3coch3 + ho2 <=> ch2choohcoch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+10, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1162,
    label = "ch2ch2cho <=> c2h4 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.127e+13, 's^-1'), n=-0.52, Ea=(24590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1163,
    label = "ch2ch2coch3 <=> c2h4 + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1164,
    label = "c2h5coch2 <=> ch2co + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(35000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1165,
    label = "c2h3coch3 + h <=> ch3chcoch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1166,
    label = "ch3chco + ch3 <=> ch3chcoch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1167,
    label = "nc3h7cho + o2 <=> nc3h7co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37560, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1168,
    label = "nc3h7cho + oh <=> nc3h7co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1169,
    label = "nc3h7cho + h <=> nc3h7co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.14e+09, 'cm^3/(mol*s)'),
        n = 1.12,
        Ea = (2320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1170,
    label = "nc3h7cho + o <=> nc3h7co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1171,
    label = "nc3h7cho + ho2 <=> nc3h7co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40900, 'cm^3/(mol*s)'), n=2.5, Ea=(10200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1172,
    label = "nc3h7cho + ch3 <=> nc3h7co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00289, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (3210, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1173,
    label = "nc3h7cho + ch3o <=> nc3h7co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1174,
    label = "nc3h7cho + ch3o2 <=> nc3h7co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40900, 'cm^3/(mol*s)'), n=2.5, Ea=(10200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1175,
    label = "nc3h7cho + oh <=> c3h6cho-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.28e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1176,
    label = "nc3h7cho + oh <=> c3h6cho-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1177,
    label = "nc3h7cho + oh <=> c3h6cho-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(552, 'cm^3/(mol*s)'), n=3.12, Ea=(-1176, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1178,
    label = "nc3h7cho + ho2 <=> c3h6cho-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1179,
    label = "nc3h7cho + ho2 <=> c3h6cho-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1180,
    label = "nc3h7cho + ho2 <=> c3h6cho-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (17880, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1181,
    label = "nc3h7cho + ch3o2 <=> c3h6cho-1 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1182,
    label = "nc3h7cho + ch3o2 <=> c3h6cho-2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1183,
    label = "nc3h7cho + ch3o2 <=> c3h6cho-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (17880, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1184,
    label = "nc3h7co <=> nc3h7 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1185,
    label = "c3h6cho-1 <=> c2h4 + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.4e+11, 's^-1'), n=0, Ea=(21970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1186,
    label = "c2h5chco + h <=> c3h6cho-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1187,
    label = "c2h3cho + ch3 <=> c3h6cho-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1188,
    label = "ch3chchcho + h <=> c3h6cho-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1189,
    label = "c3h6 + hco <=> c3h6cho-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1190,
    label = "c2h5chco + oh <=> nc3h7 + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1191,
    label = "c2h5chco + h <=> nc3h7 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(1459, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1192,
    label = "c2h5chco + o <=> c3h6 + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-437, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1193,
    label = "ch3chchcho + oh <=> ch3chchco + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1194,
    label = "c3h5-s + co <=> ch3chchco",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(8000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1195,
    label = "ch3chchcho + ho2 <=> ch3chchco + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1196,
    label = "ch3chchcho + o <=> ch3chchco + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1197,
    label = "ch3chchcho + o2 <=> ch3chchco + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1198,
    label = "c2h3coch3 + oh <=> ch3cho + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1199,
    label = "c2h3coch3 + oh => ch2co + c2h3 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(1192, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1200,
    label = "c2h3coch3 + ho2 => ch2cho + ch3co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6.03e+09, 'cm^3/(mol*s)'), n=0, Ea=(7949, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1201,
    label = "c2h3coch3 + ho2 => ch2co + c2h3 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1202,
    label = "c2h3coch3 + ch3o2 => ch2cho + ch3co + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(17050, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1203,
    label = "c2h3coch3 + ch3o2 => ch2co + c2h3 + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(17580, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1204,
    label = "ic4h10 <=> ch3 + ic3h7",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5203e+31, 's^-1'), n=-4.102, Ea=(91495, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.41e+19, 'cm^3/(mol*s)'), n=0, Ea=(52576, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.3662,
        T3 = (815.3, 'K'),
        T1 = (60.786, 'K'),
        T2 = (1e+20, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1205,
    label = "ic4h10 <=> tc4h9 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+98, 's^-1'), n=-23.81, Ea=(145300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1206,
    label = "ic4h10 <=> ic4h9 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.85e+95, 's^-1'), n=-23.11, Ea=(147600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1207,
    label = "ic4h10 + h <=> tc4h9 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(602000, 'cm^3/(mol*s)'), n=2.4, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1208,
    label = "ic4h10 + h <=> ic4h9 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1209,
    label = "ic4h10 + ch3 <=> tc4h9 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.46, Ea=(4598, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1210,
    label = "ic4h10 + ch3 <=> ic4h9 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1211,
    label = "ic4h10 + oh <=> tc4h9 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29250, 'cm^3/(mol*s)'),
        n = 2.531,
        Ea = (-1659, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1212,
    label = "ic4h10 + oh <=> ic4h9 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66540, 'cm^3/(mol*s)'),
        n = 2.665,
        Ea = (-168.9, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1213,
    label = "ic4h10 + c2h5 <=> ic4h9 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1214,
    label = "ic4h10 + c2h5 <=> tc4h9 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1215,
    label = "ic4h10 + ho2 <=> ic4h9 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(61.2, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1216,
    label = "ic4h10 + ho2 <=> tc4h9 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(433.2, 'cm^3/(mol*s)'), n=3.01, Ea=(12090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1217,
    label = "ic4h10 + o <=> tc4h9 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (196800, 'cm^3/(mol*s)'),
        n = 2.402,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1218,
    label = "ic4h10 + o <=> ic4h9 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.046e+07, 'cm^3/(mol*s)'),
        n = 2.034,
        Ea = (5136, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1219,
    label = "ic4h10 + ch3o <=> ic4h9 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1220,
    label = "ic4h10 + ch3o <=> tc4h9 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+10, 'cm^3/(mol*s)'), n=0, Ea=(2800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1221,
    label = "ic4h10 + o2 <=> ic4h9 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1222,
    label = "ic4h10 + o2 <=> tc4h9 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(48200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1223,
    label = "ic4h10 + ch3o2 <=> ic4h9 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.079, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1224,
    label = "ic4h10 + c2h5o2 <=> ic4h9 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1225,
    label = "ic4h10 + ch3co3 <=> ic4h9 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1226,
    label = "ic4h10 + nc3h7o2 <=> ic4h9 + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1227,
    label = "ic4h10 + ic3h7o2 <=> ic4h9 + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1228,
    label = "ic4h10 + ic4h9o2 <=> ic4h9 + ic4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1229,
    label = "ic4h10 + tc4h9o2 <=> ic4h9 + tc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.55e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1230,
    label = "ic4h10 + o2cho <=> ic4h9 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1231,
    label = "ic4h10 + o2cho <=> tc4h9 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1232,
    label = "ic4h10 + sc4h9o2 <=> ic4h9 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1233,
    label = "ic4h10 + sc4h9o2 <=> tc4h9 + sc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1234,
    label = "ic4h10 + pc4h9o2 <=> ic4h9 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1235,
    label = "ic4h10 + pc4h9o2 <=> tc4h9 + pc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1236,
    label = "ic4h10 + ch3o2 <=> tc4h9 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(136.6, 'cm^3/(mol*s)'), n=3.12, Ea=(13190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1237,
    label = "ic4h10 + c2h5o2 <=> tc4h9 + c2h5o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1238,
    label = "ic4h10 + ch3co3 <=> tc4h9 + ch3co3h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1239,
    label = "ic4h10 + nc3h7o2 <=> tc4h9 + nc3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1240,
    label = "ic4h10 + ic3h7o2 <=> tc4h9 + ic3h7o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1241,
    label = "ic4h10 + ic4h9o2 <=> tc4h9 + ic4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1242,
    label = "ic4h10 + tc4h9o2 <=> tc4h9 + tc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1243,
    label = "ic4h10 + ic4h9 <=> tc4h9 + ic4h10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1244,
    label = "ic4h9 + ho2 <=> ic4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1245,
    label = "tc4h9 + ho2 <=> tc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1246,
    label = "ch3o2 + ic4h9 <=> ch3o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1247,
    label = "ch3o2 + tc4h9 <=> ch3o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1248,
    label = "ic4h9 <=> tc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(34600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1249,
    label = "ic4h8 + h <=> ic4h9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1250,
    label = "c3h6 + ch3 <=> ic4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1251,
    label = "h + ic4h8 <=> tc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+12, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1252,
    label = "tc4h9 + o2 <=> ic4h8 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1253,
    label = "ic4h9 + o2 <=> ic4h8 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1254,
    label = "nc3h7o2 + ic4h9 <=> nc3h7o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1255,
    label = "nc3h7o2 + tc4h9 <=> nc3h7o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1256,
    label = "nc3h7o2 + ic4h7 <=> nc3h7o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1257,
    label = "sc4h9o2 + ic4h9 <=> sc4h9o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1258,
    label = "sc4h9o2 + tc4h9 <=> sc4h9o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1259,
    label = "pc4h9o2 + ic4h9 <=> pc4h9o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1260,
    label = "pc4h9o2 + tc4h9 <=> pc4h9o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1261,
    label = "pc4h9o2 + ic4h7 <=> pc4h9o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1262,
    label = "sc4h9o2 + ic4h7 <=> sc4h9o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1263,
    label = "ic4h9 + o2 <=> ic4h9o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1264,
    label = "tc4h9 + o2 <=> tc4h9o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1265,
    label = "ic4h9o2 + c4h10 <=> ic4h9o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1266,
    label = "tc4h9o2 + c4h10 <=> tc4h9o2h + sc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1267,
    label = "ic4h9o2 + c4h10 <=> ic4h9o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1268,
    label = "tc4h9o2 + c4h10 <=> tc4h9o2h + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1269,
    label = "ic3h7o2 + ic4h9 <=> ic3h7o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1270,
    label = "ic3h7o2 + tc4h9 <=> ic3h7o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1271,
    label = "ic3h7o2 + ic4h7 <=> ic3h7o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1272,
    label = "ic4h9o2 + c3h6 <=> ic4h9o2h + c3h5-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1273,
    label = "tc4h9o2 + c3h6 <=> tc4h9o2h + c3h5-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+11, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1274,
    label = "ic4h9o2 + ic4h8 <=> ic4h9o2h + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1275,
    label = "tc4h9o2 + ic4h8 <=> tc4h9o2h + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1276,
    label = "pc4h9o2 + ic4h8 <=> pc4h9o2h + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1277,
    label = "sc4h9o2 + ic4h8 <=> sc4h9o2h + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1278,
    label = "ic3h7o2 + ic4h8 <=> ic3h7o2h + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1279,
    label = "nc3h7o2 + ic4h8 <=> nc3h7o2h + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1280,
    label = "ic4h9o2 + c4h8-1 <=> ic4h9o2h + c4h71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1281,
    label = "tc4h9o2 + c4h8-1 <=> tc4h9o2h + c4h71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1282,
    label = "ic4h9o2 + c4h8-2 <=> ic4h9o2h + c4h71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1283,
    label = "tc4h9o2 + c4h8-2 <=> tc4h9o2h + c4h71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(14900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1284,
    label = "cc4h8o + oh => ch2o + c3h5-a + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1285,
    label = "cc4h8o + h => ch2o + c3h5-a + h2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.51e+07, 'cm^3/(mol*s)'), n=2, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1286,
    label = "cc4h8o + o => ch2o + c3h5-a + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.124e+14, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1287,
    label = "cc4h8o + ho2 => ch2o + c3h5-a + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1288,
    label = "cc4h8o + ch3o2 => ch2o + c3h5-a + ch3o2h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1289,
    label = "cc4h8o + ch3 => ch2o + c3h5-a + ch4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1290,
    label = "c2h4 + tc4h9o2 <=> c2h3 + tc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59, 'cm^3/(mol*s)'), n=3.754, Ea=(27132, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1291,
    label = "tc4h9o2 + ch4 <=> tc4h9o2h + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1292,
    label = "h2 + tc4h9o2 <=> h + tc4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1293,
    label = "tc4h9o2 + c2h6 <=> tc4h9o2h + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1294,
    label = "tc4h9o2 + c3h8 <=> tc4h9o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1295,
    label = "tc4h9o2 + c3h8 <=> tc4h9o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1296,
    label = "tc4h9o2 + ch3oh <=> tc4h9o2h + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1297,
    label = "tc4h9o2 + c2h5oh <=> tc4h9o2h + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1298,
    label = "tc4h9o2 + c2h5oh <=> tc4h9o2h + sc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1299,
    label = "ic4h9o2 + ch3cho <=> ic4h9o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1300,
    label = "tc4h9o2 + ch3cho <=> tc4h9o2h + ch3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1301,
    label = "ic4h9o2 + c2h3cho <=> ic4h9o2h + c2h3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1302,
    label = "tc4h9o2 + c2h3cho <=> tc4h9o2h + c2h3co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1303,
    label = "ic4h9o2 + c2h5cho <=> ic4h9o2h + c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1304,
    label = "tc4h9o2 + c2h5cho <=> tc4h9o2h + c2h5co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1305,
    label = "ic4h9o2 + ho2 <=> ic4h9o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1306,
    label = "tc4h9o2 + ho2 <=> tc4h9o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1307,
    label = "ic4h9o2 + h2o2 <=> ic4h9o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1308,
    label = "tc4h9o2 + h2o2 <=> tc4h9o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1309,
    label = "ic4h9o2 + ch2o <=> ic4h9o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1310,
    label = "tc4h9o2 + ch2o <=> tc4h9o2h + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+11, 'cm^3/(mol*s)'), n=0, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1311,
    label = "ic4h9o2 + ch3o2 => ic4h9o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1312,
    label = "tc4h9o2 + ch3o2 => tc4h9o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1313,
    label = "ic4h9o2 + c2h5o2 => ic4h9o + c2h5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1314,
    label = "tc4h9o2 + c2h5o2 => tc4h9o + c2h5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1315,
    label = "ic4h9o2 + ch3co3 => ic4h9o + ch3co2 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1316,
    label = "tc4h9o2 + ch3co3 => tc4h9o + ch3co2 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1317,
    label = "ic4h9o2 + ic4h9o2 => o2 + ic4h9o + ic4h9o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1318,
    label = "ic4h9o2 + tc4h9o2 => ic4h9o + tc4h9o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1319,
    label = "tc4h9o2 + tc4h9o2 => o2 + tc4h9o + tc4h9o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1320,
    label = "ic4h9o2 + pc4h9o2 => ic4h9o + pc4h9o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1321,
    label = "tc4h9o2 + pc4h9o2 => tc4h9o + pc4h9o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1322,
    label = "ic4h9o2 + sc4h9o2 => ic4h9o + sc4h9o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1323,
    label = "tc4h9o2 + sc4h9o2 => tc4h9o + sc4h9o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1324,
    label = "ic4h9o2 + nc3h7o2 => ic4h9o + nc3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1325,
    label = "tc4h9o2 + nc3h7o2 => tc4h9o + nc3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1326,
    label = "ic4h9o2 + ic3h7o2 => ic4h9o + ic3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1327,
    label = "tc4h9o2 + ic3h7o2 => tc4h9o + ic3h7o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1328,
    label = "ic4h9o2 + ho2 => ic4h9o + oh + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1329,
    label = "tc4h9o2 + ho2 => tc4h9o + oh + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1330,
    label = "ic4h9o2 + ch3 <=> ic4h9o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1331,
    label = "ic4h9o2 + c2h5 <=> ic4h9o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1332,
    label = "ic4h9o2 + ic3h7 <=> ic4h9o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1333,
    label = "ic4h9o2 + nc3h7 <=> ic4h9o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1334,
    label = "ic4h9o2 + pc4h9 <=> ic4h9o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1335,
    label = "ic4h9o2 + sc4h9 <=> ic4h9o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1336,
    label = "ic4h9o2 + ic4h9 <=> ic4h9o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1337,
    label = "ic4h9o2 + tc4h9 <=> ic4h9o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1338,
    label = "ic4h9o2 + c3h5-a <=> ic4h9o + c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1339,
    label = "ic4h9o2 + c4h71-3 <=> ic4h9o + c4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1340,
    label = "ic4h9o2 + ic4h7 <=> ic4h9o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1341,
    label = "tc4h9o2 + ch3 <=> tc4h9o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1342,
    label = "tc4h9o2 + c2h5 <=> tc4h9o + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1343,
    label = "tc4h9o2 + ic3h7 <=> tc4h9o + ic3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1344,
    label = "tc4h9o2 + nc3h7 <=> tc4h9o + nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1345,
    label = "tc4h9o2 + pc4h9 <=> tc4h9o + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1346,
    label = "tc4h9o2 + sc4h9 <=> tc4h9o + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1347,
    label = "tc4h9o2 + ic4h9 <=> tc4h9o + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1348,
    label = "tc4h9o2 + tc4h9 <=> tc4h9o + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1349,
    label = "tc4h9o2 + c3h5-a <=> tc4h9o + c3h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1350,
    label = "tc4h9o2 + c4h71-3 <=> tc4h9o + c4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1351,
    label = "tc4h9o2 + ic4h7 <=> tc4h9o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1352,
    label = "ic4h9o2 + c2h4 <=> ic4h9o2h + c2h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1353,
    label = "ic4h9o2 + ch4 <=> ic4h9o2h + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1354,
    label = "h2 + ic4h9o2 <=> h + ic4h9o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1355,
    label = "ic4h9o2 + c2h6 <=> ic4h9o2h + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1356,
    label = "ic4h9o2 + c3h8 <=> ic4h9o2h + ic3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1357,
    label = "ic4h9o2 + c3h8 <=> ic4h9o2h + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1358,
    label = "ic4h9o2 + ch3oh <=> ic4h9o2h + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1359,
    label = "ic4h9o2 + c2h5oh <=> ic4h9o2h + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1360,
    label = "ic4h9o2 + c2h5oh <=> ic4h9o2h + sc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1361,
    label = "ic4h9o2h <=> ic4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1362,
    label = "tc4h9o2h <=> tc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.95e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1363,
    label = "ic4h9o + ho2 <=> ic3h7cho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1364,
    label = "ic4h9o + oh <=> ic3h7cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1365,
    label = "ic4h9o + ch3 <=> ic3h7cho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1366,
    label = "ic4h9o + o <=> ic3h7cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1367,
    label = "ic4h9o + h <=> ic3h7cho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1368,
    label = "ic3h7cho + h <=> ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1369,
    label = "ch2o + ic3h7 <=> ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(2330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1370,
    label = "ch3coch3 + ch3 <=> tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1371,
    label = "ic4h9o + o2 <=> ic3h7cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(1660, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1372,
    label = "tc4h9o + o2 <=> ic4h8o + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(4700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1373,
    label = "ic4h8o <=> ic3h7cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.18e+13, 's^-1'), n=0, Ea=(52720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1374,
    label = "ic4h8o + oh <=> ic3h6cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1375,
    label = "ic4h8o + h <=> ic3h6cho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1376,
    label = "ic4h8o + ho2 <=> ic3h6cho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1377,
    label = "ic4h8o + ch3o2 <=> ic3h6cho + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1378,
    label = "ic4h8o + ch3 <=> ic3h6cho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1379,
    label = "ic4h8o + o <=> ic3h6cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1380,
    label = "tc3h6cho + h <=> ic3h7cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1381,
    label = "ic3h7 + hco <=> ic3h7cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1382,
    label = "ic3h7cho + ho2 <=> ic3h7co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1383,
    label = "ic3h7cho + ho2 <=> tc3h6cho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+10, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1384,
    label = "ic3h7cho + ch3 <=> ic3h7co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1385,
    label = "ic3h7cho + o <=> ic3h7co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1386,
    label = "ic3h7cho + o2 <=> ic3h7co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(37600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1387,
    label = "ic3h7cho + oh <=> ic3h7co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1388,
    label = "ic3h7cho + oh <=> tc3h6cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.684e+12, 'cm^3/(mol*s)'), n=0, Ea=(-781, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1389,
    label = "ic3h7cho + h <=> ic3h7co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1390,
    label = "ic3h7cho + oh <=> ic3h6cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1391,
    label = "ic3h7cho + ho2 <=> ic3h6cho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27400, 'cm^3/(mol*s)'), n=2.55, Ea=(15500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1392,
    label = "ic3h7cho + ch3o2 <=> ic3h6cho + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47600, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1393,
    label = "ic3h7 + co <=> ic3h7co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1394,
    label = "c3h6 + hco <=> ic3h6cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1395,
    label = "c2h3cho + ch3 <=> ic3h6cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1396,
    label = "ic4h9o2 <=> ic4h8o2h-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1397,
    label = "tc4h9o2 <=> tc4h8o2h-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1398,
    label = "ic4h9o2 <=> ic4h8o2h-t",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(29200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1399,
    label = "ic4h9o2 <=> ic4h8 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.265e+35, 's^-1'), n=-7.22, Ea=(39490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1400,
    label = "tc4h9o2 <=> ic4h8 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.612e+42, 's^-1'), n=-9.41, Ea=(41490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1401,
    label = "ic4h8o2h-i + o2 <=> ic4h8ooh-io2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1402,
    label = "tc4h8o2h-i + o2 <=> tc4h8ooh-io2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.26e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1403,
    label = "ic4h8o2h-t + o2 <=> ic4h8ooh-to2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1404,
    label = "ic4h8ooh-io2 <=> ic4ketii + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1405,
    label = "ic4h8ooh-to2 <=> ic4ketit + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 's^-1'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1406,
    label = "tc4h8ooh-io2 <=> tic4h7q2-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1407,
    label = "ic4h7ooh + ho2 <=> tic4h7q2-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1408,
    label = "ic4h8ooh-io2 <=> iic4h7q2-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1409,
    label = "ic4h8ooh-io2 <=> iic4h7q2-t",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(29200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1410,
    label = "ic4h8ooh-to2 <=> tic4h7q2-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(34500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1411,
    label = "ac3h5ooh + ch2o2h <=> iic4h7q2-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1412,
    label = "ic4h7ooh + ho2 <=> iic4h7q2-t",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(7800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1413,
    label = "ch2o2h <=> ch2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+14, 's^-1'), n=0, Ea=(1500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1414,
    label = "ic4ketii => ch2o + c2h5co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1415,
    label = "ic4ketit => ch3coch3 + hco + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.5e+15, 's^-1'), n=0, Ea=(42540, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1416,
    label = "ic4h8 + ho2 <=> tc4h8o2h-i",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(12620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1417,
    label = "ic4h8 + ho2 <=> ic4h8o2h-t",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.97e+11, 'cm^3/(mol*s)'), n=0, Ea=(12620, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1418,
    label = "ic4h8o2h-i <=> cc4h8o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+11, 's^-1'), n=0, Ea=(21900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1419,
    label = "ic4h8o2h-t <=> ic4h8o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.09e+12, 's^-1'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1420,
    label = "tc4h8o2h-i <=> ic4h8o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 's^-1'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1421,
    label = "ic4h8o2h-i => oh + ch2o + c3h6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.451e+15, 's^-1'), n=-0.68, Ea=(29170, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1422,
    label = "ic4h8 <=> c3h5-t + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.92e+66, 's^-1'), n=-14.22, Ea=(128100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1423,
    label = "ic4h8 <=> ic4h7 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.07e+55, 's^-1'), n=-11.49, Ea=(114300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1424,
    label = "ic4h8 + h <=> c3h6 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+33, 'cm^3/(mol*s)'),
        n = -5.72,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1425,
    label = "ic4h8 + h <=> ic4h7 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(340000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1426,
    label = "ic4h8 + o => ch2co + ch3 + ch3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.33e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1427,
    label = "ic4h8 + o => ic3h6co + h + h",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.66e+07, 'cm^3/(mol*s)'), n=1.76, Ea=(76, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1428,
    label = "ic4h8 + o <=> ic4h7 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7633, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1429,
    label = "ic4h8 + ch3 <=> ic4h7 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1430,
    label = "ic4h8 + ho2 <=> ic4h7 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1431,
    label = "ic4h8 + o2cho <=> ic4h7 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1432,
    label = "ic4h8 + o2 <=> ic4h7 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1433,
    label = "ic4h8 + c3h5-a <=> ic4h7 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1434,
    label = "ic4h8 + c3h5-s <=> ic4h7 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1435,
    label = "ic4h8 + c3h5-t <=> ic4h7 + c3h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1436,
    label = "ic4h8 + oh <=> ic4h7 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1437,
    label = "ic4h8 + o <=> ic3h7 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-1216, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1438,
    label = "ic4h8 + ch3o2 <=> ic4h7 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19280, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1439,
    label = "ic4h8 + ho2 <=> ic4h8o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+12, 'cm^3/(mol*s)'), n=0, Ea=(13340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1440,
    label = "ic4h7 + o2 <=> ic3h5cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+13, 'cm^3/(mol*s)'),
        n = -0.45,
        Ea = (23020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1441,
    label = "ic4h7 + o2 <=> ch3coch2 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.14e+15, 'cm^3/(mol*s)'),
        n = -1.21,
        Ea = (21050, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1442,
    label = "ic4h7 + o2 => c3h4-a + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7.29e+29, 'cm^3/(mol*s)'),
        n = -5.71,
        Ea = (21450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1443,
    label = "ic4h7 + o <=> ic3h5cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1444,
    label = "ic4h7 <=> c3h4-a + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+47, 's^-1'), n=-9.74, Ea=(74260, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1445,
    label = "ch3o2 + ic4h7 <=> ch3o + ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1446,
    label = "ic4h7 + ho2 <=> ic4h7o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1447,
    label = "c3h5-t + ch2o <=> ic4h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(12600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1448,
    label = "ic4h7o <=> ic4h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.391e+11, 's^-1'), n=0, Ea=(15600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1449,
    label = "ic4h7o <=> ic3h5cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(29100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1450,
    label = "ic4h6oh + h2 <=> ic4h7oh + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(21600, 'cm^3/(mol*s)'), n=2.38, Ea=(18990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1451,
    label = "ic4h7oh + o2 <=> ic4h6oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1452,
    label = "ic4h6oh + ch2o <=> ic4h7oh + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (18190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1453,
    label = "ic4h6oh + ic4h8 <=> ic4h7oh + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.3, Ea=(19840, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1454,
    label = "ic4h6oh + h <=> ic4h7oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1455,
    label = "ic4h6oh + h2o2 <=> ic4h7oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (783000, 'cm^3/(mol*s)'),
        n = 2.05,
        Ea = (13580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1456,
    label = "c3h4-a + ch2oh <=> ic4h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(9200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1457,
    label = "ic4h7o + o2 <=> ic3h5cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+10, 'cm^3/(mol*s)'), n=0, Ea=(1649, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1458,
    label = "ic4h7o + ho2 <=> ic3h5cho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1459,
    label = "ic4h7o + ch3 <=> ic3h5cho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1460,
    label = "ic4h7o + o <=> ic3h5cho + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1461,
    label = "ic4h7o + oh <=> ic3h5cho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1462,
    label = "ic4h7o + h <=> ic3h5cho + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1463,
    label = "ic3h5cho + oh <=> ic3h5co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1464,
    label = "ic3h5cho + ho2 <=> ic3h5co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1465,
    label = "ic3h5cho + ch3 <=> ic3h5co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+12, 'cm^3/(mol*s)'), n=0, Ea=(8700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1466,
    label = "ic3h5cho + o <=> ic3h5co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.18e+12, 'cm^3/(mol*s)'), n=0, Ea=(1389, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1467,
    label = "ic3h5cho + o2 <=> ic3h5co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(40700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1468,
    label = "ic3h5cho + h <=> ic3h5co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(2600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1469,
    label = "ic3h5co <=> c3h5-t + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.278e+20, 's^-1'), n=-1.89, Ea=(34460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1470,
    label = "tc3h6ocho + oh <=> tc3h6cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.018e+17, 'cm^3/(mol*s)'),
        n = -1.2,
        Ea = (21010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1471,
    label = "tc3h6ocho <=> ch3coch3 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+13, 's^-1'), n=0, Ea=(9700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1472,
    label = "ic3h5cho + h <=> tc3h6cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1473,
    label = "ic3h6co + h <=> tc3h6cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1474,
    label = "tc3h6cho + h2 <=> ic3h7cho + h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (18990, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1475,
    label = "ic4h7o + oh <=> ic4h7ooh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1476,
    label = "ic4h7o + h <=> ic4h7oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1477,
    label = "ic4h7oh + h <=> ic4h8oh-1",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(1200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.06e+12, 'cm^3/(mol*s)'),
                n = 0.51,
                Ea = (1230, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1478,
    label = "ic4h7o + h2 <=> ic4h7oh + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.05e+06, 'cm^3/(mol*s)'), n=2, Ea=(17830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1479,
    label = "ic4h7 + oh <=> ic4h7oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1480,
    label = "ic4h7oh + hco <=> ic4h7o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02e+11, 'cm^3/(mol*s)'), n=0, Ea=(18160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1481,
    label = "tc3h6cho + ch2o <=> ic3h7cho + hco",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (18190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1482,
    label = "tc3h6cho + ic4h8 <=> ic3h7cho + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(470, 'cm^3/(mol*s)'), n=3.3, Ea=(19840, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1483,
    label = "ic3h6co + oh <=> ic3h7 + co2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.73e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1484,
    label = "tc3h6cho + oh <=> tc3h6ohcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1485,
    label = "tc3h6oh + hco <=> tc3h6ohcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1486,
    label = "ch3coch3 + h <=> tc3h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1487,
    label = "ic3h5oh + h <=> tc3h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (4020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1488,
    label = "c3h5-t + oh <=> ic3h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1489,
    label = "tc3h6cho + o2 <=> tc3h6o2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+17, 'cm^3/(mol*s)'), n=-2.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1490,
    label = "tc3h6o2cho <=> ic3h5o2hcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(29880, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1491,
    label = "tc3h6o2cho <=> tc3h6o2hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1492,
    label = "ic3h5cho + ho2 <=> ic3h5o2hcho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+11, 'cm^3/(mol*s)'), n=0, Ea=(10600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1493,
    label = "tc3h6o2hco => ch3coch3 + co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.244e+18, 's^-1'), n=-1.43, Ea=(4800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1494,
    label = "tc3h6oh + o2 <=> ch3coch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1495,
    label = "ic3h6co + oh <=> tc3h6oh + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1010, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1496,
    label = "tc3h6cho + ho2 <=> ic3h7cho + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.675e+12, 'cm^3/(mol*s)'), n=0, Ea=(1310, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1497,
    label = "tc3h6cho + ch3 <=> ic3h5cho + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-131, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1498,
    label = "tc4h8cho <=> ic3h5cho + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(26290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1499,
    label = "tc4h8cho <=> ic4h8 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.52e+12, 's^-1'), n=0, Ea=(20090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1500,
    label = "tc4h8cho + o2 <=> o2c4h8cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1501,
    label = "o2c4h8cho <=> o2hc4h8co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.16e+11, 's^-1'), n=0, Ea=(15360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1502,
    label = "ic4h8o2h-t + co <=> o2hc4h8co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4809, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1503,
    label = "ic4h7o + ic4h8 <=> ic4h7oh + ic4h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1504,
    label = "ic4h6oh + ho2 => ch2cch2oh + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.446e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1505,
    label = "ic4h8 + ch2cch2oh <=> ic4h7 + c3h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1506,
    label = "ch2cch2oh + h2o2 <=> c3h5oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+09, 'cm^3/(mol*s)'), n=0, Ea=(2583, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1507,
    label = "c3h5oh + oh <=> ch2cch2oh + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+12, 'cm^3/(mol*s)'), n=0, Ea=(5960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1508,
    label = "c3h5oh + h <=> ch2cch2oh + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(390000, 'cm^3/(mol*s)'), n=2.5, Ea=(5821, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1509,
    label = "c3h5oh + o2 <=> ch2cch2oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(60690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1510,
    label = "c3h5oh + ch3 <=> ch2cch2oh + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+11, 'cm^3/(mol*s)'), n=0, Ea=(8030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1511,
    label = "ch2cch2oh + ch3 <=> ic4h7oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1512,
    label = "ch2cch2oh + h <=> c3h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1513,
    label = "ch2cch2oh + o2 => ch2oh + co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(4.335e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1514,
    label = "ch2cch2oh <=> c2h2 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.163e+40, 's^-1'), n=-8.31, Ea=(45110, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1515,
    label = "c3h4-a + oh <=> ch2cch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1516,
    label = "nc4h9oh <=> ch3 + c3h6oh-3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.79e+24, 's^-1'), n=-2.23, Ea=(88070, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.782e+60, 'cm^3/(mol*s)'),
            n = -12.28,
            Ea = (83980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.2352,
        T3 = (724, 'K'),
        T1 = (5e+09, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1517,
    label = "nc4h9oh <=> c2h5 + pc2h4oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.53e+24, 's^-1'), n=-2.23, Ea=(89010, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.632e+59, 'cm^3/(mol*s)'),
            n = -12.13,
            Ea = (84720, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.2438,
        T3 = (744.06, 'K'),
        T1 = (5e+09, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1518,
    label = "nc4h9oh <=> nc3h7 + ch2oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.02e+23, 's^-1'), n=-1.88, Ea=(85710, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.416e+59, 'cm^3/(mol*s)'),
            n = -11.93,
            Ea = (83980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7646,
        T3 = (8.344e+09, 'K'),
        T1 = (724.8, 'K'),
        T2 = (8.214e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1519,
    label = "nc4h9oh <=> oh + pc4h9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.33e+20, 's^-1'), n=-1.37, Ea=(94930, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.902e+51, 'cm^3/(mol*s)'),
            n = -10.21,
            Ea = (89200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.703,
        T3 = (9.882e+09, 'K'),
        T1 = (634.68, 'K'),
        T2 = (1.786e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1520,
    label = "nc4h9oh <=> h + pc4h9o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.04e+14, 's^-1'), n=0.1, Ea=(103800, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.408e+39, 'cm^3/(mol*s)'),
            n = -7.03,
            Ea = (95960, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.3865,
        T3 = (564.91, 'K'),
        T1 = (4.438e+09, 'K'),
        T2 = (6.71e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1521,
    label = "nc4h9oh <=> c4h8-1 + h2o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.52e+13, 's^-1'), n=0, Ea=(67230, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.69e+75, 'cm^3/(mol*s)'),
            n = -17.04,
            Ea = (64750, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.08,
        T3 = (1, 'K'),
        T1 = (9.924e+09, 'K'),
        T2 = (9.924e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1522,
    label = "h + c4h8oh-1 <=> nc4h9oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1523,
    label = "h + c4h8oh-2 <=> nc4h9oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1524,
    label = "h + c4h8oh-3 <=> nc4h9oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1525,
    label = "h + c4h8oh-4 <=> nc4h9oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1526,
    label = "nc4h9oh + h <=> c4h8oh-4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(666000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1527,
    label = "nc4h9oh + h <=> c4h8oh-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1528,
    label = "nc4h9oh + h <=> c4h8oh-2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(108000, 'cm^3/(mol*s)'), n=2.69, Ea=(4440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1529,
    label = "nc4h9oh + h <=> c4h8oh-1 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(87890, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1530,
    label = "nc4h9oh + h <=> pc4h9o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1531,
    label = "nc4h9oh + oh <=> c4h8oh-4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.28e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1532,
    label = "nc4h9oh + oh <=> c4h8oh-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1141, 'cm^3/(mol*s)'), n=2.87, Ea=(-2926, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1533,
    label = "nc4h9oh + oh <=> c4h8oh-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54, 'cm^3/(mol*s)'), n=3.7, Ea=(-3736, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1534,
    label = "nc4h9oh + oh <=> c4h8oh-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3610, 'cm^3/(mol*s)'), n=2.89, Ea=(-2291, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1535,
    label = "nc4h9oh + oh <=> pc4h9o + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1536,
    label = "nc4h9oh + o <=> c4h8oh-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(981000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1537,
    label = "nc4h9oh + o <=> c4h8oh-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(552000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1538,
    label = "nc4h9oh + o <=> c4h8oh-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(144000, 'cm^3/(mol*s)'), n=2.61, Ea=(3029, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1539,
    label = "nc4h9oh + o <=> c4h8oh-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1540,
    label = "nc4h9oh + o <=> pc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1541,
    label = "nc4h9oh + o2 <=> ho2 + c4h8oh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1542,
    label = "nc4h9oh + o2 <=> ho2 + c4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1543,
    label = "nc4h9oh + o2 <=> ho2 + c4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1544,
    label = "nc4h9oh + o2 <=> ho2 + c4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1545,
    label = "nc4h9oh + o2 <=> ho2 + pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1546,
    label = "nc4h9oh + ho2 <=> c4h8oh-4 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.088, 'cm^3/(mol*s)'), n=4.31, Ea=(17270, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1547,
    label = "nc4h9oh + ho2 <=> c4h8oh-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000276, 'cm^3/(mol*s)'),
        n = 4.76,
        Ea = (11850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1548,
    label = "nc4h9oh + ho2 <=> c4h8oh-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00751, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (14710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1549,
    label = "nc4h9oh + ho2 <=> c4h8oh-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (8268, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1550,
    label = "nc4h9oh + ho2 <=> pc4h9o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1551,
    label = "nc4h9oh + ch3 <=> c4h8oh-4 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.453, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1552,
    label = "nc4h9oh + ch3 <=> c4h8oh-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1553,
    label = "nc4h9oh + ch3 <=> c4h8oh-2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.02, 'cm^3/(mol*s)'), n=3.23, Ea=(6461, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1554,
    label = "nc4h9oh + ch3 <=> c4h8oh-1 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1555,
    label = "nc4h9oh + ch3 <=> pc4h9o + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1556,
    label = "nc4h9oh + hco <=> c4h8oh-4 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1557,
    label = "nc4h9oh + hco <=> c4h8oh-3 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1558,
    label = "nc4h9oh + hco <=> c4h8oh-2 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (516000, 'cm^3/(mol*s)'),
        n = 2.25,
        Ea = (16760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1559,
    label = "nc4h9oh + hco <=> c4h8oh-1 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1560,
    label = "nc4h9oh + hco <=> pc4h9o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1561,
    label = "nc4h9oh + ch2oh <=> c4h8oh-4 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(101, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1562,
    label = "nc4h9oh + ch2oh <=> c4h8oh-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60.2, 'cm^3/(mol*s)'), n=2.95, Ea=(11980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1563,
    label = "nc4h9oh + ch2oh <=> c4h8oh-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15.3, 'cm^3/(mol*s)'), n=3.11, Ea=(12210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1564,
    label = "nc4h9oh + ch2oh <=> c4h8oh-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1565,
    label = "nc4h9oh + ch2oh <=> pc4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1566,
    label = "nc4h9oh + ch3o <=> c4h8oh-4 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1567,
    label = "nc4h9oh + ch3o <=> c4h8oh-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1568,
    label = "nc4h9oh + ch3o <=> c4h8oh-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+10, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (4703, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1569,
    label = "nc4h9oh + ch3o <=> c4h8oh-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1570,
    label = "nc4h9oh + ch3o <=> pc4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1571,
    label = "nc4h9oh + ch3o2 <=> c4h8oh-4 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1572,
    label = "nc4h9oh + ch3o2 <=> c4h8oh-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1573,
    label = "nc4h9oh + ch3o2 <=> c4h8oh-2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1580, 'cm^3/(mol*s)'), n=2.81, Ea=(14050, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1574,
    label = "nc4h9oh + ch3o2 <=> c4h8oh-1 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(17500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1575,
    label = "nc4h9oh + ch3o2 <=> pc4h9o + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1576,
    label = "nc4h9oh + c2h5 <=> c4h8oh-4 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1577,
    label = "nc4h9oh + c2h5 <=> c4h8oh-3 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1578,
    label = "nc4h9oh + c2h5 <=> c4h8oh-2 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1579,
    label = "nc4h9oh + c2h5 <=> c4h8oh-1 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1580,
    label = "nc4h9oh + c2h5 <=> pc4h9o + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1581,
    label = "c2h3oh + c2h5 <=> c4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1582,
    label = "nc3h7cho + h <=> c4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1583,
    label = "c4h7oh1-1 + h <=> c4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1584,
    label = "c4h8-1 + oh <=> c4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1585,
    label = "c3h5oh + ch3 <=> c4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1586,
    label = "h + c4h7oh2-1 <=> c4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1587,
    label = "h + c4h7oh1-1 <=> c4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1588,
    label = "c3h6 + ch2oh <=> c4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1589,
    label = "c4h7oh1-4 + h <=> c4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1590,
    label = "c4h7oh2-1 + h <=> c4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1591,
    label = "c2h4 + pc2h4oh <=> c4h8oh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1592,
    label = "h + c4h7oh1-4 <=> c4h8oh-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1593,
    label = "h + nc3h7cho <=> pc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1594,
    label = "pc4h9o <=> c4h8oh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.132, 's^-1'), n=3.632, Ea=(2689, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1595,
    label = "pc4h9o <=> c4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.32e-10, 's^-1'), n=6.204, Ea=(6710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1596,
    label = "c4h8oh-4 <=> c4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e-19, 's^-1'), n=8.638, Ea=(5268, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1597,
    label = "c4h7oh1-3 + h <=> c4h6oh1-32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1598,
    label = "c4h7oh1-3 + o <=> c4h6oh1-32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(1967, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1599,
    label = "c4h7oh1-3 + oh <=> c4h6oh1-32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1600,
    label = "c4h7oh1-3 + ch3 <=> c4h6oh1-32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1601,
    label = "c4h7oh1-3 + ho2 <=> c4h6oh1-32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1602,
    label = "c4h7oh1-3 + ch3o2 <=> c4h6oh1-32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1603,
    label = "c4h7oh1-3 + ch3o <=> c4h6oh1-32 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1604,
    label = "c4h7oh2-1 + h <=> c4h6oh1-32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1605,
    label = "c4h7oh2-1 + o <=> c4h6oh1-32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1606,
    label = "c4h7oh2-1 + oh <=> c4h6oh1-32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1607,
    label = "c4h7oh2-1 + ch3 <=> c4h6oh1-32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1608,
    label = "c4h7oh2-1 + ho2 <=> c4h6oh1-32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1609,
    label = "c4h7oh2-1 + ch3o2 <=> c4h6oh1-32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1610,
    label = "c4h7oh1-4 + h <=> c4h6oh1-32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1611,
    label = "c4h7oh1-4 + o <=> c4h6oh1-32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(1967, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1612,
    label = "c4h7oh1-4 + oh <=> c4h6oh1-32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1613,
    label = "c4h7oh1-4 + ch3 <=> c4h6oh1-32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1614,
    label = "c4h7oh1-4 + ho2 <=> c4h6oh1-32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1615,
    label = "c4h7oh1-4 + ch3o2 <=> c4h6oh1-32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1616,
    label = "c4h7oh1-4 + ch3o <=> c4h6oh1-32 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1617,
    label = "c4h7oh2-2 + h <=> c4h6oh1-32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1618,
    label = "c4h7oh2-2 + o <=> c4h6oh1-32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1619,
    label = "c4h7oh2-2 + oh <=> c4h6oh1-32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1620,
    label = "c4h7oh2-2 + ch3 <=> c4h6oh1-32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1621,
    label = "c4h7oh2-2 + ho2 <=> c4h6oh1-32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1622,
    label = "c4h7oh2-2 + ch3o2 <=> c4h6oh1-32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1623,
    label = "c4h7oh1-2 + h <=> c4h6oh1-32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1624,
    label = "c4h7oh1-2 + o <=> c4h6oh1-32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1625,
    label = "c4h7oh1-2 + oh <=> c4h6oh1-32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1626,
    label = "c4h7oh1-2 + ch3 <=> c4h6oh1-32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1627,
    label = "c4h7oh1-2 + ho2 <=> c4h6oh1-32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1628,
    label = "c4h7oh1-2 + ch3o2 <=> c4h6oh1-32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1629,
    label = "c4h7oh1-1 + h <=> c4h6oh1-13 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1630,
    label = "c4h7oh1-1 + o <=> c4h6oh1-13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.59e+12, 'cm^3/(mol*s)'), n=0, Ea=(1967, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1631,
    label = "c4h7oh1-1 + oh <=> c4h6oh1-13 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1632,
    label = "c4h7oh1-1 + ch3 <=> c4h6oh1-13 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1633,
    label = "c4h7oh1-1 + ho2 <=> c4h6oh1-13 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1634,
    label = "c4h7oh1-1 + ch3o2 <=> c4h6oh1-13 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1635,
    label = "c4h7oh1-1 + ch3o <=> c4h6oh1-13 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1636,
    label = "c4h7oh1-1 + ho2 <=> nc3h7cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1637,
    label = "c4h7oh1-2 + ho2 <=> c2h5coch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1638,
    label = "c4h7oh2-2 + ho2 <=> c2h5coch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1639,
    label = "ch3chchoh + ho2 <=> c2h5cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1640,
    label = "ic3h5oh + ho2 <=> ch3coch3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1641,
    label = "c2h3oh + hocho <=> ch3cho + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1642,
    label = "c4h7oh1-1 + hocho <=> nc3h7cho + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1643,
    label = "c4h7oh1-2 + hocho <=> c2h5coch3 + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1644,
    label = "c4h7oh2-2 + hocho <=> c2h5coch3 + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1645,
    label = "ch3chchoh + hocho <=> c2h5cho + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1646,
    label = "ic3h5oh + hocho <=> ch3coch3 + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1647,
    label = "ch3chchoh <=> c2h5cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1648,
    label = "ic3h5oh <=> ch3coch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1649,
    label = "c4h7oh1-1 <=> nc3h7cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1650,
    label = "c4h7oh2-1 <=> c2h5coch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1651,
    label = "c4h7oh2-2 <=> c2h5coch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1652,
    label = "ic3h6choh <=> ic3h7cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.59e+11, 's^-1'), n=0.318, Ea=(55900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1653,
    label = "c4h7oh1-3 + o2 <=> c4h6oh1-32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1654,
    label = "c4h7oh2-1 + o2 <=> c4h6oh1-32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1655,
    label = "c4h7oh1-4 + o2 <=> c4h6oh1-32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1656,
    label = "c4h7oh2-2 + o2 <=> c4h6oh1-32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1657,
    label = "c4h7oh1-2 + o2 <=> c4h6oh1-32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1658,
    label = "c4h7oh1-1 + o2 <=> c4h6oh1-13 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 'cm^3/(mol*s)'), n=0, Ea=(37190, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1659,
    label = "c3h5oh + h <=> c2h4 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1660,
    label = "ic3h5oh + h <=> c2h3oh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1661,
    label = "ic3h5oh + h <=> c3h6 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1662,
    label = "ch3chchoh + h <=> c2h3oh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1663,
    label = "ch3chchoh + h <=> c3h6 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1664,
    label = "ic3h6choh + h <=> ch3chchoh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1665,
    label = "ic3h6choh + h <=> ic4h8 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1666,
    label = "c4h7oh1-1 + h <=> c4h8-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1667,
    label = "c4h7oh1-1 + h <=> c2h3oh + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1668,
    label = "c4h7oh1-2 + h <=> c4h8-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1669,
    label = "c4h7oh1-2 + h <=> c2h3oh + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1670,
    label = "c4h7oh2-2 + h <=> ic3h5oh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1671,
    label = "c4h7oh2-2 + h <=> c4h8-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1672,
    label = "c4h7oh2-2 + h <=> ch3chchoh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1673,
    label = "ic4h7oh + h <=> ch3 + c3h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1674,
    label = "c4h7oh1-3 + h <=> c2h4 + sc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1675,
    label = "c4h7oh1-4 + h <=> c2h4 + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1676,
    label = "c4h7oh2-1 + h <=> c3h6 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1677,
    label = "c4h7oh2-1 + h <=> c4h8-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1678,
    label = "c4h7oh2-1 + h <=> ch3chchoh + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1679,
    label = "c4h6oh1-32 <=> c4h6 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.035e+16, 's^-1'), n=-1.012, Ea=(36070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1680,
    label = "c4h6oh1-13 <=> c4h5oh-13 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.722e+12, 's^-1'), n=0.488, Ea=(43940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1681,
    label = "c3h6 + oh <=> ic3h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.92e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1682,
    label = "c2h3oh + ch3 <=> ic3h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1683,
    label = "ic3h5oh + h <=> ic3h6oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1684,
    label = "c2h5cho + h <=> c3h6oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1685,
    label = "ch3chchoh + h <=> c3h6oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1686,
    label = "ch3 + c2h3oh <=> c3h6oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1687,
    label = "c3h6 + oh <=> c3h6oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.95e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1688,
    label = "h + ch3chchoh <=> c3h6oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1689,
    label = "h + c3h5oh <=> c3h6oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1690,
    label = "c4h7oh1-3 <=> c4h71-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1691,
    label = "c4h7oh1-3 <=> c2h3 + sc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1692,
    label = "c4h7oh2-1 <=> c4h71-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1693,
    label = "c4h7oh2-1 <=> c3h5-a + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1694,
    label = "c4h7oh1-4 <=> c4h71-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1695,
    label = "c4h7oh1-4 <=> c2h3 + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1696,
    label = "c4h7oh2-2 <=> c4h72-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1697,
    label = "c4h7oh1-2 <=> c4h71-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.887e+19, 's^-1'), n=-0.956, Ea=(95950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1698,
    label = "c4h7oh1-2 <=> c2h5 + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.214e+22, 's^-1'), n=-1.576, Ea=(97520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1699,
    label = "c4h7oh1-1 <=> c2h5 + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.214e+22, 's^-1'), n=-1.576, Ea=(97520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1700,
    label = "c4h7oh1-1 <=> c4h71-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.887e+19, 's^-1'), n=-0.956, Ea=(95950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1701,
    label = "c4h5oh-13 <=> c4h5-n + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.61e+21, 's^-1'), n=-1.612, Ea=(106000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1702,
    label = "c4h5oh-13 <=> c2h3 + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.816e+24, 's^-1'), n=-2.381, Ea=(90130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1703,
    label = "tc4h9oh <=> ch3 + tc3h6oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.31e+16, 's^-1'), n=0, Ea=(81277, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.8207e+74, 'cm^3/(mol*s)'),
            n = -16.121,
            Ea = (92918, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.40865,
        T3 = (1104.3, 'K'),
        T1 = (490, 'K'),
        T2 = (2851.9, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1704,
    label = "tc4h9oh <=> oh + tc4h9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.2e+24, 's^-1'), n=-2.13, Ea=(97281, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.5291e+74, 'cm^3/(mol*s)'),
            n = -16.275,
            Ea = (107810, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.36787,
        T3 = (469.09, 'K'),
        T1 = (2.9117e+12, 'K'),
        T2 = (3672.8, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1705,
    label = "tc4h9oh <=> h + tc4h9o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+15, 's^-1'), n=0.028, Ea=(105150, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.4443e+61, 'cm^3/(mol*s)'),
            n = -13.089,
            Ea = (114690, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.30333,
        T3 = (515.66, 'K'),
        T1 = (3.9578e+07, 'K'),
        T2 = (2386.5, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1706,
    label = "tc4h9oh <=> h + tc4h8oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+18, 's^-1'), n=-0.449, Ea=(104460, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.542e+65, 'cm^3/(mol*s)'),
            n = -13.668,
            Ea = (114110, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.32112,
        T3 = (507.26, 'K'),
        T1 = (7.9992e+06, 'K'),
        T2 = (2535.1, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1707,
    label = "tc4h9oh <=> h2o + ic4h8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.48e+14, 's^-1'), n=0, Ea=(64200, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.8705e+95, 'cm^3/(mol*s)'),
            n = -22.63,
            Ea = (79171, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 3.2677e-05,
        T3 = (332.6, 'K'),
        T1 = (1.4141e+10, 'K'),
        T2 = (3823.8, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1708,
    label = "sc4h9oh <=> ch3 + ic3h6oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.1e+26, 's^-1'), n=-2.815, Ea=(92354, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.5323e+84, 'cm^3/(mol*s)'),
            n = -19.166,
            Ea = (104670, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.042546,
        T3 = (277.51, 'K'),
        T1 = (3.3602e+06, 'K'),
        T2 = (2193.4, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1709,
    label = "sc4h9oh <=> c2h5 + sc2h4oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.728e+26, 's^-1'), n=-2.72, Ea=(86207, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.6771e+89, 'cm^3/(mol*s)'),
            n = -20.364,
            Ea = (99453, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.0055845,
        T3 = (358.2, 'K'),
        T1 = (4.9325e+07, 'K'),
        T2 = (2476.1, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1710,
    label = "sc4h9oh <=> ch3 + c3h6oh-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.5e+24, 's^-1'), n=-2.53, Ea=(88444, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.9116e+85, 'cm^3/(mol*s)'),
            n = -19.664,
            Ea = (101200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.39928,
        T3 = (217.47, 'K'),
        T1 = (465.57, 'K'),
        T2 = (2284.1, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1711,
    label = "sc4h9oh <=> oh + sc4h9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.43e+22, 's^-1'), n=-1.865, Ea=(96229, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.9022e+78, 'cm^3/(mol*s)'),
            n = -17.503,
            Ea = (108350, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 8.6766e-05,
        T3 = (293.41, 'K'),
        T1 = (19749, 'K'),
        T2 = (1674.6, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1712,
    label = "sc4h9oh <=> h + sc4h8ohm",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.33e+16, 's^-1'), n=0.017, Ea=(102430, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.218e+66, 'cm^3/(mol*s)'),
            n = -14.289,
            Ea = (113840, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.089358,
        T3 = (336.51, 'K'),
        T1 = (7.8352e+09, 'K'),
        T2 = (1663.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1713,
    label = "sc4h9oh <=> h + sc4h8oh-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.86e+18, 's^-1'), n=-0.818, Ea=(94238, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.4242e+75, 'cm^3/(mol*s)'),
            n = -16.831,
            Ea = (106460, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.10896,
        T3 = (86.767, 'K'),
        T1 = (5.7087e+09, 'K'),
        T2 = (2439.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1714,
    label = "sc4h9oh <=> h + sc4h8oh-2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.63e+20, 's^-1'), n=-1.323, Ea=(102100, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.7063e+71, 'cm^3/(mol*s)'),
            n = -15.706,
            Ea = (113570, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.18033,
        T3 = (274.39, 'K'),
        T1 = (1.0791e+07, 'K'),
        T2 = (2148, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1715,
    label = "sc4h9oh <=> h + sc4h8oh-3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.31e+16, 's^-1'), n=0.018, Ea=(101830, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7414e+67, 'cm^3/(mol*s)'),
            n = -14.434,
            Ea = (113350, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.16051,
        T3 = (285.87, 'K'),
        T1 = (1.5444e+06, 'K'),
        T2 = (2057.6, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1716,
    label = "sc4h9oh <=> h + sc4h9o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.2e+14, 's^-1'), n=0.245, Ea=(104850, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.597e+62, 'cm^3/(mol*s)'),
            n = -13.509,
            Ea = (115890, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.48822,
        T3 = (27.191, 'K'),
        T1 = (2.1032e+10, 'K'),
        T2 = (2.2461e+06, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1717,
    label = "sc4h9oh <=> h2o + c4h8-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13, 's^-1'), n=0, Ea=(67960, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.8206e+94, 'cm^3/(mol*s)'),
            n = -22.464,
            Ea = (83529, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00028246,
        T3 = (361.97, 'K'),
        T1 = (12873, 'K'),
        T2 = (4491, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1718,
    label = "sc4h9oh <=> h2o + c4h8-2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.5e+13, 's^-1'), n=0, Ea=(65900, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.6273e+101, 'cm^3/(mol*s)'),
            n = -24.473,
            Ea = (83466, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.0029457,
        T3 = (293.4, 'K'),
        T1 = (5.2057e+10, 'K'),
        T2 = (5081.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1719,
    label = "ic4h9oh <=> ic3h7 + ch2oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.25e+25, 's^-1'), n=-2.413, Ea=(87976, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.2327e+73, 'cm^3/(mol*s)'),
            n = -15.724,
            Ea = (92616, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.13423,
        T3 = (775.39, 'K'),
        T1 = (4.0069e+07, 'K'),
        T2 = (4428.1, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1720,
    label = "ic4h9oh <=> c3h6oh-2 + ch3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4e+27, 's^-1'), n=-3.11, Ea=(92179, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.0463e+66, 'cm^3/(mol*s)'),
            n = -14.122,
            Ea = (90777, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.14416,
        T3 = (835.91, 'K'),
        T1 = (4.8482e+06, 'K'),
        T2 = (4547.3, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1721,
    label = "ic4h9oh <=> oh + ic4h9",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.4e+21, 's^-1'), n=-1.481, Ea=(94894, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.0872e+55, 'cm^3/(mol*s)'),
            n = -11.191,
            Ea = (90431, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00054471,
        T3 = (1125.4, 'K'),
        T1 = (1.6818e+10, 'K'),
        T2 = (3635.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1722,
    label = "ic4h9oh <=> ic4h8oh-1 + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.68e+16, 's^-1'), n=-0.297, Ea=(95908, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.8895e+49, 'cm^3/(mol*s)'),
            n = -9.561,
            Ea = (90472, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 2.0948e-05,
        T3 = (1164.2, 'K'),
        T1 = (1.6818e+10, 'K'),
        T2 = (3704.9, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1723,
    label = "ic4h9oh <=> ic4h8oh-2 + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.7e+17, 's^-1'), n=-0.467, Ea=(98199, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4779e+46, 'cm^3/(mol*s)'),
            n = -8.823,
            Ea = (90945, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.14595,
        T3 = (1034, 'K'),
        T1 = (1.0695e+11, 'K'),
        T2 = (5129.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1724,
    label = "ic4h9oh <=> ic4h8oh-3 + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+17, 's^-1'), n=-0.462, Ea=(102490, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.3167e+41, 'cm^3/(mol*s)'),
            n = -7.365,
            Ea = (92821, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.27069,
        T3 = (2741.9, 'K'),
        T1 = (128.72, 'K'),
        T2 = (9656.2, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1725,
    label = "ic4h9oh <=> ic4h9o + h",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.2e+15, 's^-1'), n=0.016, Ea=(105180, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4939e+36, 'cm^3/(mol*s)'),
            n = -6.144,
            Ea = (94567, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.49994,
        T3 = (6209.6, 'K'),
        T1 = (665.5, 'K'),
        T2 = (2.9e+06, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1726,
    label = "ic4h9oh <=> h2o + ic4h8",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.56e+13, 's^-1'), n=0, Ea=(64970, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.0967e+101, 'cm^3/(mol*s)'),
            n = -23.781,
            Ea = (106720, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.20182,
        T3 = (1286.4, 'K'),
        T1 = (1282.4, 'K'),
        T2 = (67921, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 1727,
    label = "tc4h9oh + h <=> tc4h9o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1728,
    label = "tc4h9oh + h <=> tc4h8oh + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.998e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1729,
    label = "tc4h9oh + oh <=> tc4h9o + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1730,
    label = "tc4h9oh + oh <=> tc4h8oh + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.93, 'cm^3/(mol*s)'), n=3.7, Ea=(-2416, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1731,
    label = "tc4h9oh + o <=> tc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1732,
    label = "tc4h9oh + o <=> tc4h8oh + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.943e+06, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (4750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1733,
    label = "tc4h9oh + ho2 <=> tc4h9o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1734,
    label = "tc4h9oh + ho2 <=> tc4h8oh + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71400, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1735,
    label = "tc4h9oh + ch3 <=> tc4h9o + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1736,
    label = "tc4h9oh + ch3 <=> tc4h8oh + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.359, 'cm^3/(mol*s)'), n=3.65, Ea=(9154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1737,
    label = "tc4h9oh + ch3o <=> tc4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1738,
    label = "tc4h9oh + ch3o <=> tc4h8oh + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.51e+11, 'cm^3/(mol*s)'), n=0, Ea=(8458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1739,
    label = "tc4h9oh + hco <=> tc4h9o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1740,
    label = "tc4h9oh + hco <=> tc4h8oh + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(306000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1741,
    label = "tc4h9oh + ch2oh <=> tc4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1742,
    label = "tc4h9oh + ch2oh <=> tc4h8oh + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(303, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1743,
    label = "tc4h9oh + ch3o2 <=> tc4h9o + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0168, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (16730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1744,
    label = "tc4h9oh + ch3o2 <=> tc4h8oh + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71400, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1745,
    label = "tc4h9oh + c2h5 <=> tc4h9o + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1746,
    label = "tc4h9oh + c2h5 <=> tc4h8oh + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.503e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1747,
    label = "tc4h9oh + o2 <=> ho2 + tc4h8oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1748,
    label = "tc4h9oh + o2 <=> ho2 + tc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1749,
    label = "sc4h9oh + h <=> sc4h9o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1750,
    label = "sc4h9oh + h <=> sc4h8ohm + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(666000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1751,
    label = "sc4h9oh + h <=> sc4h8oh-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(666000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1752,
    label = "sc4h9oh + h <=> sc4h8oh-2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(108000, 'cm^3/(mol*s)'), n=2.69, Ea=(4440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1753,
    label = "sc4h9oh + h <=> sc4h8oh-1 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(43950, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1754,
    label = "sc4h9oh + oh <=> sc4h9o + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1755,
    label = "sc4h9oh + oh <=> sc4h8ohm + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.31, 'cm^3/(mol*s)'), n=3.7, Ea=(-2946, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1756,
    label = "sc4h9oh + oh <=> sc4h8oh-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.17e+06, 'cm^3/(mol*s)'),
        n = 1.806,
        Ea = (12.48, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1757,
    label = "sc4h9oh + oh <=> sc4h8oh-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54, 'cm^3/(mol*s)'), n=3.7, Ea=(-3736, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1758,
    label = "sc4h9oh + oh <=> sc4h8oh-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1805, 'cm^3/(mol*s)'), n=2.89, Ea=(-2611, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1759,
    label = "sc4h9oh + o <=> sc4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1760,
    label = "sc4h9oh + o <=> sc4h8ohm + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(981000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1761,
    label = "sc4h9oh + o <=> sc4h8oh-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(981000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1762,
    label = "sc4h9oh + o <=> sc4h8oh-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(144000, 'cm^3/(mol*s)'), n=2.61, Ea=(3029, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1763,
    label = "sc4h9oh + o <=> sc4h8oh-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(72500, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1764,
    label = "sc4h9oh + ho2 <=> sc4h9o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1765,
    label = "sc4h9oh + ho2 <=> sc4h8ohm + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0113, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (13850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1766,
    label = "sc4h9oh + ho2 <=> sc4h8oh-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000414, 'cm^3/(mol*s)'),
        n = 4.76,
        Ea = (15050, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1767,
    label = "sc4h9oh + ho2 <=> sc4h8oh-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00751, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (14710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1768,
    label = "sc4h9oh + ho2 <=> sc4h8oh-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (7468, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1769,
    label = "sc4h9oh + ch3 <=> sc4h9o + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1770,
    label = "sc4h9oh + ch3 <=> sc4h8ohm + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.453, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1771,
    label = "sc4h9oh + ch3 <=> sc4h8oh-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.453, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1772,
    label = "sc4h9oh + ch3 <=> sc4h8oh-2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.02, 'cm^3/(mol*s)'), n=3.23, Ea=(6461, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1773,
    label = "sc4h9oh + ch3 <=> sc4h8oh-1 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.965, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1774,
    label = "sc4h9oh + hco <=> sc4h9o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1775,
    label = "sc4h9oh + hco <=> sc4h8ohm + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1776,
    label = "sc4h9oh + hco <=> sc4h8oh-3 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1777,
    label = "sc4h9oh + hco <=> sc4h8oh-2 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (516000, 'cm^3/(mol*s)'),
        n = 2.25,
        Ea = (16760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1778,
    label = "sc4h9oh + hco <=> sc4h8oh-1 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+06, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1779,
    label = "sc4h9oh + ch2oh <=> sc4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1780,
    label = "sc4h9oh + ch2oh <=> sc4h8ohm + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.1, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1781,
    label = "sc4h9oh + ch2oh <=> sc4h8oh-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.1, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1782,
    label = "sc4h9oh + ch2oh <=> sc4h8oh-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15.3, 'cm^3/(mol*s)'), n=3.11, Ea=(12210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1783,
    label = "sc4h9oh + ch2oh <=> sc4h8oh-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(30, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1784,
    label = "sc4h9oh + ch3o <=> sc4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1785,
    label = "sc4h9oh + ch3o <=> sc4h8ohm + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1786,
    label = "sc4h9oh + ch3o <=> sc4h8oh-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1787,
    label = "sc4h9oh + ch3o <=> sc4h8oh-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+10, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (4703, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1788,
    label = "sc4h9oh + ch3o <=> sc4h8oh-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1789,
    label = "sc4h9oh + ch3o2 <=> sc4h9o + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1790,
    label = "sc4h9oh + ch3o2 <=> sc4h8ohm + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1791,
    label = "sc4h9oh + ch3o2 <=> sc4h8oh-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1792,
    label = "sc4h9oh + ch3o2 <=> sc4h8oh-2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1580, 'cm^3/(mol*s)'), n=2.81, Ea=(14050, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1793,
    label = "sc4h9oh + ch3o2 <=> sc4h8oh-1 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1794,
    label = "sc4h9oh + c2h5 <=> sc4h9o + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1795,
    label = "sc4h9oh + c2h5 <=> sc4h8ohm + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1796,
    label = "sc4h9oh + c2h5 <=> sc4h8oh-3 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1797,
    label = "sc4h9oh + c2h5 <=> sc4h8oh-2 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1798,
    label = "sc4h9oh + c2h5 <=> sc4h8oh-1 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1799,
    label = "sc4h9oh + o2 <=> ho2 + sc4h8ohm",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1800,
    label = "sc4h9oh + o2 <=> ho2 + sc4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1801,
    label = "sc4h9oh + o2 <=> ho2 + sc4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1802,
    label = "sc4h9oh + o2 <=> ho2 + sc4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1803,
    label = "sc4h9oh + o2 <=> ho2 + sc4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1804,
    label = "ic4h9oh + h <=> ic4h9o + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1805,
    label = "ic4h9oh + h <=> ic4h8oh-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.332e+06, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1806,
    label = "ic4h9oh + h <=> ic4h8oh-2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(650000, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1807,
    label = "ic4h9oh + h <=> ic4h8oh-1 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(87890, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1808,
    label = "ic4h9oh + oh <=> ic4h9o + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1809,
    label = "ic4h9oh + oh <=> ic4h8oh-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.67e+06, 'cm^3/(mol*s)'),
        n = 1.843,
        Ea = (-147.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1810,
    label = "ic4h9oh + oh <=> ic4h8oh-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.77, 'cm^3/(mol*s)'), n=3.7, Ea=(-4940, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1811,
    label = "ic4h9oh + oh <=> ic4h8oh-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3610, 'cm^3/(mol*s)'), n=2.89, Ea=(-2331, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1812,
    label = "ic4h9oh + o <=> ic4h9o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1813,
    label = "ic4h9oh + o <=> ic4h8oh-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.962e+06, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (4750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1814,
    label = "ic4h9oh + o <=> ic4h8oh-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(276000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1815,
    label = "ic4h9oh + o <=> ic4h8oh-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(72500, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1816,
    label = "ic4h9oh + ho2 <=> ic4h9o + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1817,
    label = "ic4h9oh + ho2 <=> ic4h8oh-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000414, 'cm^3/(mol*s)'),
        n = 4.76,
        Ea = (14850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1818,
    label = "ic4h9oh + ho2 <=> ic4h8oh-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00376, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (11710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1819,
    label = "ic4h9oh + ho2 <=> ic4h8oh-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (8668, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1820,
    label = "ic4h9oh + ch3 <=> ic4h9o + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1821,
    label = "ic4h9oh + ch3 <=> ic4h8oh-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.906, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1822,
    label = "ic4h9oh + ch3 <=> ic4h8oh-2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.755, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1823,
    label = "ic4h9oh + ch3 <=> ic4h8oh-1 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1824,
    label = "ic4h9oh + hco <=> ic4h9o + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1825,
    label = "ic4h9oh + hco <=> ic4h8oh-3 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(204000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1826,
    label = "ic4h9oh + hco <=> ic4h8oh-2 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.45e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1827,
    label = "ic4h9oh + hco <=> ic4h8oh-1 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1828,
    label = "ic4h9oh + ch2oh <=> ic4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1829,
    label = "ic4h9oh + ch2oh <=> ic4h8oh-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(202, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1830,
    label = "ic4h9oh + ch2oh <=> ic4h8oh-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(30.1, 'cm^3/(mol*s)'), n=2.95, Ea=(11980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1831,
    label = "ic4h9oh + ch2oh <=> ic4h8oh-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1832,
    label = "ic4h9oh + ch3o <=> ic4h9o + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1833,
    label = "ic4h9oh + ch3o <=> ic4h8oh-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.34e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1834,
    label = "ic4h9oh + ch3o <=> ic4h8oh-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.25e+10, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1835,
    label = "ic4h9oh + ch3o <=> ic4h8oh-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1836,
    label = "ic4h9oh + ch3o2 <=> ic4h9o + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1837,
    label = "ic4h9oh + ch3o2 <=> ic4h8oh-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47600, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1838,
    label = "ic4h9oh + ch3o2 <=> ic4h8oh-2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1839,
    label = "ic4h9oh + ch3o2 <=> ic4h8oh-1 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1840,
    label = "ic4h9oh + c2h5 <=> ic4h9o + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1841,
    label = "ic4h9oh + c2h5 <=> ic4h8oh-3 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1842,
    label = "ic4h9oh + c2h5 <=> ic4h8oh-2 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1843,
    label = "ic4h9oh + c2h5 <=> ic4h8oh-1 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1844,
    label = "ic4h9oh + o2 <=> ho2 + ic4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1845,
    label = "ic4h9oh + o2 <=> ho2 + ic4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(48200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1846,
    label = "ic4h9oh + o2 <=> ho2 + ic4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1847,
    label = "ic4h9oh + o2 <=> ho2 + ic4h9o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1848,
    label = "ic4h8 + oh <=> tc4h8oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1849,
    label = "ic3h5oh + ch3 <=> tc4h8oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1300, 'cm^3/(mol*s)'), n=2.48, Ea=(8520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1850,
    label = "ch3chchoh + ch3 <=> ic4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1851,
    label = "ic3h6choh + h <=> ic4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1852,
    label = "ic3h7cho + h <=> ic4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1853,
    label = "ic3h6choh + h <=> ic4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1854,
    label = "ic4h8 + oh <=> ic4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1855,
    label = "ch2oh + c3h6 <=> ic4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1856,
    label = "ch3 + c3h5oh <=> ic4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1857,
    label = "ic4h7oh + h <=> ic4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.25e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1858,
    label = "h + c4h7oh1-2 <=> sc4h8ohm",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1859,
    label = "oh + c4h8-1 <=> sc4h8ohm",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1860,
    label = "c2h3oh + c2h5 <=> sc4h8ohm",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1861,
    label = "c4h7oh1-2 + h <=> sc4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1862,
    label = "c2h5coch3 + h <=> sc4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1863,
    label = "c4h7oh2-2 + h <=> sc4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1864,
    label = "ch3 + ic3h5oh <=> sc4h8oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1865,
    label = "ch3chchoh + ch3 <=> sc4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1890, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1866,
    label = "c4h7oh2-2 + h <=> sc4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1867,
    label = "c4h8-2 + oh <=> sc4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1868,
    label = "c4h7oh1-3 + h <=> sc4h8oh-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1869,
    label = "c4h7oh1-3 + h <=> sc4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1870,
    label = "sc2h4oh + c2h4 <=> sc4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=2.67, Ea=(6850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1871,
    label = "sc4h9o <=> sc4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e-16, 's^-1'), n=8.112, Ea=(4449, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1872,
    label = "ic4h9o <=> ic4h8oh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.59e-15, 's^-1'), n=7.838, Ea=(4655, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1873,
    label = "c4h8oh-1 + o2 <=> nc3h7cho + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1874,
    label = "ic4h8oh-1 + o2 <=> ic3h7cho + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1875,
    label = "sc4h8oh-1 + o2 <=> c2h5coch3 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1876,
    label = "c4h8oh-1 + o2 <=> c4h8oh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1877,
    label = "c4h8oh-2 + o2 <=> c4h8oh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1878,
    label = "c4h8oh-3 + o2 <=> c4h8oh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1879,
    label = "c4h8oh-4 + o2 <=> c4h8oh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1880,
    label = "c4h8oh-1 + c4h8oh-1o2 <=> c4h8oh-1o + c4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1881,
    label = "c4h8oh-1 + c4h8oh-2o2 <=> c4h8oh-1o + c4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1882,
    label = "c4h8oh-1 + c4h8oh-3o2 <=> c4h8oh-1o + c4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1883,
    label = "c4h8oh-1 + c4h8oh-4o2 <=> c4h8oh-1o + c4h8oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1884,
    label = "c4h8oh-2 + c4h8oh-1o2 <=> c4h8oh-2o + c4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1885,
    label = "c4h8oh-2 + c4h8oh-2o2 <=> c4h8oh-2o + c4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1886,
    label = "c4h8oh-2 + c4h8oh-3o2 <=> c4h8oh-2o + c4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1887,
    label = "c4h8oh-2 + c4h8oh-4o2 <=> c4h8oh-2o + c4h8oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1888,
    label = "c4h8oh-3 + c4h8oh-1o2 <=> c4h8oh-3o + c4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1889,
    label = "c4h8oh-3 + c4h8oh-2o2 <=> c4h8oh-3o + c4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1890,
    label = "c4h8oh-3 + c4h8oh-3o2 <=> c4h8oh-3o + c4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1891,
    label = "c4h8oh-3 + c4h8oh-4o2 <=> c4h8oh-3o + c4h8oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1892,
    label = "c4h8oh-4 + c4h8oh-1o2 <=> c4h8oh-4o + c4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1893,
    label = "c4h8oh-4 + c4h8oh-2o2 <=> c4h8oh-4o + c4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1894,
    label = "c4h8oh-4 + c4h8oh-3o2 <=> c4h8oh-4o + c4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1895,
    label = "c4h8oh-4 + c4h8oh-4o2 <=> c4h8oh-4o + c4h8oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1896,
    label = "c4h8oh-1 + ho2 <=> c4h8oh-1o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1897,
    label = "c4h8oh-2 + ho2 <=> c4h8oh-2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1898,
    label = "c4h8oh-3 + ho2 <=> c4h8oh-3o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1899,
    label = "c4h8oh-4 + ho2 <=> c4h8oh-4o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1900,
    label = "c4h8oh-1 + ch3o2 <=> c4h8oh-1o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1901,
    label = "c4h8oh-2 + ch3o2 <=> c4h8oh-2o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1902,
    label = "c4h8oh-3 + ch3o2 <=> c4h8oh-3o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1903,
    label = "c4h8oh-4 + ch3o2 <=> c4h8oh-4o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1904,
    label = "c4h8oh-1o2 <=> c4h7oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1905,
    label = "c4h8oh-1o2 <=> c4h7oh-1ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1906,
    label = "c4h8oh-1o2 <=> c4h7oh-1ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(21950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1907,
    label = "c4h8oh-2o2 => c2h5cho + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1908,
    label = "c4h8oh-2o2 <=> c4h7oh-2ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1909,
    label = "c4h8oh-2o2 <=> c4h7oh-2ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1910,
    label = "c4h8oh-2o2 <=> c4h7oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1911,
    label = "c4h8oh-3o2 <=> c4h7oh-3ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(18450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1912,
    label = "c4h8oh-3o2 <=> c4h7oh-3ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1913,
    label = "c4h8oh-3o2 <=> c4h7oh-3ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1914,
    label = "c4h8oh-4o2 <=> c4h7oh-4ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1915,
    label = "c4h8oh-4o2 <=> c4h7oh-4ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1916,
    label = "c4h8oh-4o2 <=> c4h7oh-4ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(16650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1917,
    label = "c4h8oh-1o2 <=> c4h7oh1-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1918,
    label = "c4h8oh-2o2 <=> c4h7oh1-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1919,
    label = "c4h8oh-2o2 <=> c4h7oh2-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1920,
    label = "c4h8oh-3o2 <=> ho2 + c4h7oh2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1921,
    label = "c4h8oh-3o2 <=> c4h7oh1-4 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1922,
    label = "c4h8oh-4o2 <=> ho2 + c4h7oh1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1923,
    label = "c4h8oh-1o2 + ho2 <=> c4h8oh-1o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1924,
    label = "c4h8oh-2o2 + ho2 <=> c4h8oh-2o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1925,
    label = "c4h8oh-3o2 + ho2 <=> c4h8oh-3o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1926,
    label = "c4h8oh-4o2 + ho2 <=> c4h8oh-4o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1927,
    label = "c4h8oh-1o2 + h2o2 <=> c4h8oh-1o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1928,
    label = "c4h8oh-2o2 + h2o2 <=> c4h8oh-2o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1929,
    label = "c4h8oh-3o2 + h2o2 <=> c4h8oh-3o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1930,
    label = "c4h8oh-4o2 + h2o2 <=> c4h8oh-4o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1931,
    label = "c4h8oh-1o2 + ch3o2 => c4h8oh-1o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1932,
    label = "c4h8oh-2o2 + ch3o2 => c4h8oh-2o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1933,
    label = "c4h8oh-3o2 + ch3o2 => c4h8oh-3o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1934,
    label = "c4h8oh-4o2 + ch3o2 => c4h8oh-4o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1935,
    label = "c4h8oh-1o2 + c4h8oh-1o2 => c4h8oh-1o + c4h8oh-1o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1936,
    label = "c4h8oh-1o2 + c4h8oh-2o2 => c4h8oh-1o + c4h8oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1937,
    label = "c4h8oh-1o2 + c4h8oh-3o2 => c4h8oh-1o + c4h8oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1938,
    label = "c4h8oh-1o2 + c4h8oh-4o2 => c4h8oh-1o + c4h8oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1939,
    label = "c4h8oh-2o2 + c4h8oh-2o2 => c4h8oh-2o + c4h8oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1940,
    label = "c4h8oh-2o2 + c4h8oh-3o2 => c4h8oh-2o + c4h8oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1941,
    label = "c4h8oh-2o2 + c4h8oh-4o2 => c4h8oh-2o + c4h8oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1942,
    label = "c4h8oh-3o2 + c4h8oh-3o2 => c4h8oh-3o + c4h8oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1943,
    label = "c4h8oh-3o2 + c4h8oh-4o2 => c4h8oh-3o + c4h8oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1944,
    label = "c4h8oh-4o2 + c4h8oh-4o2 => c4h8oh-4o + c4h8oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1945,
    label = "c4h8oh-1o2h => c4h8oh-1o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1946,
    label = "c4h8oh-2o2h => c4h8oh-2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1947,
    label = "c4h8oh-3o2h => c4h8oh-3o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1948,
    label = "c4h8oh-4o2h => c4h8oh-4o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1949,
    label = "hocho + nc3h7 <=> c4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1950,
    label = "c2h5cho + ch2oh <=> c4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1951,
    label = "ch3cho + pc2h4oh <=> c4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1952,
    label = "ch2o + c3h6oh-1 <=> c4h8oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1953,
    label = "c4h7oh-1ooh-2 => c4h7oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1954,
    label = "c4h7oh-1ooh-3 => c4h7oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1955,
    label = "c4h7oh-1ooh-4 => c4h7oho1-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1956,
    label = "c4h7oh-2ooh-1 => c4h7oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1957,
    label = "c4h7oh-2ooh-3 => c4h7oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1958,
    label = "c4h7oh-2ooh-4 => c4h7oho2-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1959,
    label = "c4h7oh-3ooh-1 => c4h7oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1960,
    label = "c4h7oh-3ooh-2 => c4h7oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1961,
    label = "c4h7oh-3ooh-4 => c4h7oho3-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1962,
    label = "c4h7oh-4ooh-1 => c4h7oho1-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1963,
    label = "c4h7oh-4ooh-2 => c4h7oho2-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1964,
    label = "c4h7oh-4ooh-3 => c4h7oho3-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1965,
    label = "c4h7oh1-1 + ho2 <=> c4h7oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1966,
    label = "c4h7oh1-1 + ho2 <=> c4h7oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1967,
    label = "c4h7oh2-1 + ho2 <=> c4h7oh-2ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1968,
    label = "c4h7oh2-1 + ho2 <=> c4h7oh-3ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1969,
    label = "c4h7oh1-4 + ho2 <=> c4h7oh-3ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1970,
    label = "c4h7oh1-4 + ho2 <=> c4h7oh-4ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1971,
    label = "c4h7oh-1ooh-3 => oh + hocho + c3h6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1972,
    label = "c4h7oh-2ooh-4 => oh + hoch2cho + c2h4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1973,
    label = "c4h7oh-3ooh-1 => oh + ch3cho + c2h3oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1974,
    label = "c4h7oh-4ooh-2 => oh + ch2o + c3h5oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1975,
    label = "c4h7oh-1ooh-2 + o2 <=> c4h7oh-1ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1976,
    label = "c4h7oh-1ooh-3 + o2 <=> c4h7oh-1ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1977,
    label = "c4h7oh-1ooh-4 + o2 <=> c4h7oh-1ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1978,
    label = "c4h7oh-2ooh-1 + o2 <=> c4h7oh-2ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1979,
    label = "c4h7oh-2ooh-3 + o2 <=> c4h7oh-2ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1980,
    label = "c4h7oh-2ooh-4 + o2 <=> c4h7oh-2ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1981,
    label = "c4h7oh-3ooh-1 + o2 <=> c4h7oh-3ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1982,
    label = "c4h7oh-3ooh-2 + o2 <=> c4h7oh-3ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1983,
    label = "c4h7oh-3ooh-4 + o2 <=> c4h7oh-3ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1984,
    label = "c4h7oh-4ooh-1 + o2 <=> c4h7oh-4ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1985,
    label = "c4h7oh-4ooh-2 + o2 <=> c4h7oh-4ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1986,
    label = "c4h7oh-4ooh-3 + o2 <=> c4h7oh-4ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1987,
    label = "c4h7oh-2ooh-1 + o2 <=> nc4ket12 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1988,
    label = "c4h7oh-3ooh-1 + o2 <=> nc4ket13 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1989,
    label = "c4h7oh-4ooh-1 + o2 <=> nc4ket14 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 1990,
    label = "c4h7oh-1ooh-2o2 => c2h5cho + ho2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1991,
    label = "c4h7oh-3ooh-2o2 => c3ket12 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1992,
    label = "c4h7oh-4ooh-2o2 => c3ket13 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1993,
    label = "c4h7oh-1ooh-2o2 <=> c4ohket1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(21450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1994,
    label = "c4h7oh-1ooh-3o2 <=> c4ohket1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(15450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1995,
    label = "c4h7oh-1ooh-4o2 <=> c4ohket1-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+09, 's^-1'), n=0, Ea=(13650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1996,
    label = "c4h7oh-2ooh-1o2 <=> c4ohket2-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1997,
    label = "c4h7oh-2ooh-3o2 <=> c4ohket2-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1998,
    label = "c4h7oh-2ooh-4o2 <=> c4ohket2-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1999,
    label = "c4h7oh-3ooh-1o2 <=> c4ohket3-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2000,
    label = "c4h7oh-3ooh-2o2 <=> c4ohket3-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2001,
    label = "c4h7oh-3ooh-4o2 <=> c4ohket3-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2002,
    label = "c4h7oh-4ooh-1o2 <=> c4ohket4-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(18950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2003,
    label = "c4h7oh-4ooh-2o2 <=> c4ohket4-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2004,
    label = "c4h7oh-4ooh-3o2 <=> c4ohket4-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2005,
    label = "c4ohket1-2 => oh + ocho + c2h5cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2006,
    label = "c4ohket1-3 => oh + ch2ocho + ch3cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2007,
#     label = "c4ohket1-4 => oh + c2h4 + ocho + ch2o",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2008,
    label = "c4ohket2-1 => oh + hocho + c2h5co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2009,
    label = "c4ohket2-3 => oh + hoch2co + ch3cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2010,
#     label = "c4ohket2-4 => oh + ch2co + ch2oh + ch2o",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2011,
    label = "c4ohket3-1 => oh + hocho + ch3coch2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2012,
    label = "c4ohket3-2 => oh + hoch2cho + ch3co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2013,
    label = "c4ohket3-4 => oh + hoc2h4co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2014,
    label = "c4ohket4-1 => oh + hocho + ch2ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2015,
    label = "c4ohket4-2 => oh + hoch2cho + ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2016,
    label = "c4ohket4-3 => oh + hoc2h4cho + hco",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2017,
    label = "c4h7oho1-2 + oh => c3h5-s + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2018,
    label = "c4h7oho1-3 + oh => c3h5-a + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2019,
    label = "c4h7oho1-4 + oh => c3h5-a + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2020,
    label = "c4h7oho2-3 + oh => c2h3cho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2021,
    label = "c4h7oho2-4 + oh => c2h3cho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2022,
    label = "c4h7oho3-4 + oh => pc2h4oh + ch2co + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2023,
    label = "c4h7oho1-2 + ho2 => c3h5-s + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2024,
    label = "c4h7oho1-3 + ho2 => c3h5-a + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2025,
    label = "c4h7oho1-4 + ho2 => c3h5-a + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2026,
    label = "c4h7oho2-3 + ho2 => c2h3cho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2027,
    label = "c4h7oho2-4 + ho2 => c2h3cho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2028,
    label = "c4h7oho3-4 + ho2 => pc2h4oh + ch2co + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2029,
    label = "hoch2cho + o2 <=> hoch2co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0.5, Ea=(42200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2030,
    label = "hoch2cho + oh <=> hoch2co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2031,
    label = "hoch2cho + h <=> hoch2co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2032,
    label = "hoch2cho + o <=> hoch2co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2033,
    label = "hoch2cho + ho2 <=> hoch2co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2034,
    label = "hoch2cho + ch3 <=> hoch2co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2035,
    label = "hoch2cho + ch3o <=> hoch2co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+11, 'cm^3/(mol*s)'), n=0, Ea=(1280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2036,
    label = "hoch2cho + ch3o2 <=> hoch2co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2037,
    label = "hoch2co <=> ch2oh + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2038,
    label = "hoc2h4cho + o2 <=> hoc2h4co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0.5, Ea=(42200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2039,
    label = "hoc2h4cho + oh <=> hoc2h4co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2040,
    label = "hoc2h4cho + h <=> hoc2h4co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2041,
    label = "hoc2h4cho + o <=> hoc2h4co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2042,
    label = "hoc2h4cho + ho2 <=> hoc2h4co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2043,
    label = "hoc2h4cho + ch3 <=> hoc2h4co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2044,
    label = "hoc2h4cho + ch3o <=> hoc2h4co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+11, 'cm^3/(mol*s)'), n=0, Ea=(1280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2045,
    label = "hoc2h4cho + ch3o2 <=> hoc2h4co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2046,
    label = "hoc2h4co <=> pc2h4oh + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2047,
    label = "ic4h8oh-1 + o2 <=> ic4h8oh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2048,
    label = "ic4h8oh-2 + o2 <=> ic4h8oh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2049,
    label = "ic4h8oh-3 + o2 <=> ic4h8oh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2050,
    label = "ic4h8oh-1 + ic4h8oh-1o2 <=> ic4h8oh-1o + ic4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2051,
    label = "ic4h8oh-1 + ic4h8oh-2o2 <=> ic4h8oh-1o + ic4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2052,
    label = "ic4h8oh-1 + ic4h8oh-3o2 <=> ic4h8oh-1o + ic4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2053,
    label = "ic4h8oh-2 + ic4h8oh-1o2 <=> ic4h8oh-2o + ic4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2054,
    label = "ic4h8oh-2 + ic4h8oh-2o2 <=> ic4h8oh-2o + ic4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2055,
    label = "ic4h8oh-2 + ic4h8oh-3o2 <=> ic4h8oh-2o + ic4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2056,
    label = "ic4h8oh-3 + ic4h8oh-1o2 <=> ic4h8oh-3o + ic4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2057,
    label = "ic4h8oh-3 + ic4h8oh-2o2 <=> ic4h8oh-3o + ic4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2058,
    label = "ic4h8oh-3 + ic4h8oh-3o2 <=> ic4h8oh-3o + ic4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2059,
    label = "ic4h8oh-1 + ho2 <=> ic4h8oh-1o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2060,
    label = "ic4h8oh-2 + ho2 <=> ic4h8oh-2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2061,
    label = "ic4h8oh-3 + ho2 <=> ic4h8oh-3o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2062,
    label = "ic4h8oh-1 + ch3o2 <=> ic4h8oh-1o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2063,
    label = "ic4h8oh-2 + ch3o2 <=> ic4h8oh-2o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2064,
    label = "ic4h8oh-3 + ch3o2 <=> ic4h8oh-3o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2065,
    label = "ic4h8oh-1o2 <=> ic4h7oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2066,
    label = "ic4h8oh-1o2 <=> ic4h7oh-1ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2067,
    label = "ic4h8oh-2o2 => ch3coch3 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2068,
    label = "ic4h8oh-2o2 <=> ic4h7oh-2ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2069,
    label = "ic4h8oh-2o2 <=> ic4h7oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2070,
    label = "ic4h8oh-3o2 <=> ic4h7oh-3ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2071,
    label = "ic4h8oh-3o2 <=> ic4h7oh-3ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2072,
    label = "ic4h8oh-3o2 <=> ic4h7oh-3ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2073,
    label = "ic4h8oh-1o2 <=> ic3h6choh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2074,
    label = "ic4h8oh-2o2 <=> ic3h6choh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2075,
    label = "ic4h8oh-2o2 <=> ic4h7oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2076,
    label = "ic4h8oh-3o2 <=> ic4h7oh + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2077,
    label = "ic4h8oh-1o2 + ho2 <=> ic4h8oh-1o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2078,
    label = "ic4h8oh-2o2 + ho2 <=> ic4h8oh-2o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2079,
    label = "ic4h8oh-3o2 + ho2 <=> ic4h8oh-3o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2080,
    label = "ic4h8oh-1o2 + h2o2 <=> ic4h8oh-1o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2081,
    label = "ic4h8oh-2o2 + h2o2 <=> ic4h8oh-2o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2082,
    label = "ic4h8oh-3o2 + h2o2 <=> ic4h8oh-3o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2083,
    label = "ic4h8oh-1o2 + ch3o2 => ic4h8oh-1o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2084,
    label = "ic4h8oh-2o2 + ch3o2 => ic4h8oh-2o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2085,
    label = "ic4h8oh-3o2 + ch3o2 => ic4h8oh-3o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2086,
    label = "ic4h8oh-1o2 + ic4h8oh-1o2 => ic4h8oh-1o + ic4h8oh-1o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2087,
    label = "ic4h8oh-1o2 + ic4h8oh-2o2 => ic4h8oh-1o + ic4h8oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2088,
    label = "ic4h8oh-1o2 + ic4h8oh-3o2 => ic4h8oh-1o + ic4h8oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2089,
    label = "ic4h8oh-2o2 + ic4h8oh-2o2 => ic4h8oh-2o + ic4h8oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2090,
    label = "ic4h8oh-2o2 + ic4h8oh-3o2 => ic4h8oh-2o + ic4h8oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2091,
    label = "ic4h8oh-3o2 + ic4h8oh-3o2 => ic4h8oh-3o + ic4h8oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2092,
    label = "ic4h8oh-1o2h => ic4h8oh-1o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2093,
    label = "ic4h8oh-2o2h => ic4h8oh-2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2094,
    label = "ic4h8oh-3o2h => ic4h8oh-3o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2095,
    label = "hocho + ic3h7 <=> ic4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2096,
    label = "ch3coch3 + ch2oh <=> ic4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2097,
    label = "ch2o + c3h6oh-2 <=> ic4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2098,
    label = "ic4h7oh-1ooh-2 => ic4h7oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2099,
    label = "ic4h7oh-1ooh-3 => ic4h7oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2100,
    label = "ic4h7oh-2ooh-1 => ic4h7oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2101,
    label = "ic4h7oh-2ooh-3 => ic4h7oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2102,
    label = "ic4h7oh-3ooh-1 => ic4h7oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2103,
    label = "ic4h7oh-3ooh-2 => ic4h7oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2104,
    label = "ic4h7oh-3ooh-3 => ic4h7oho3-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2105,
    label = "ic3h6choh + ho2 <=> ic4h7oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2106,
    label = "ic3h6choh + ho2 <=> ic4h7oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2107,
    label = "ic4h7oh + ho2 <=> ic4h7oh-2ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2108,
    label = "ic4h7oh + ho2 <=> ic4h7oh-3ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2109,
    label = "ic4h7oh-1ooh-3 => oh + hocho + c3h6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2110,
    label = "ic4h7oh-3ooh-1 => oh + ch2o + c3h5oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2111,
    label = "ic4h7oh-3ooh-3 => oh + ch2o + c3h5oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2112,
    label = "ic4h7oh-1ooh-2 + o2 <=> ic4h7oh-1ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2113,
    label = "ic4h7oh-1ooh-3 + o2 <=> ic4h7oh-1ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2114,
    label = "ic4h7oh-2ooh-1 + o2 <=> ic4h7oh-2ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2115,
    label = "ic4h7oh-2ooh-3 + o2 <=> ic4h7oh-2ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2116,
    label = "ic4h7oh-3ooh-1 + o2 <=> ic4h7oh-3ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2117,
    label = "ic4h7oh-3ooh-2 + o2 <=> ic4h7oh-3ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2118,
    label = "ic4h7oh-3ooh-3 + o2 <=> ic4h7oh-3ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2119,
    label = "ic4h7oh-2ooh-1 + o2 <=> ic4ketit + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2120,
    label = "ic4h7oh-3ooh-1 + o2 <=> ic4ketii + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2121,
    label = "ic4h7oh-1ooh-2o2 => ch3coch3 + ho2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2122,
    label = "ic4h7oh-3ooh-2o2 => c3ket21 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2123,
    label = "ic4h7oh-1ooh-2o2 <=> ic4ohket1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2124,
    label = "ic4h7oh-1ooh-3o2 <=> ic4ohket1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(16450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2125,
    label = "ic4h7oh-2ooh-1o2 => ac3h5ooh + hocho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2126,
#     label = "ic4h7oh-2ooh-3o2 => c3h4-a + ch2o + oh + oh + ho2",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2127,
    label = "ic4h7oh-3ooh-1o2 <=> ic4ohket3-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2128,
    label = "ic4h7oh-3ooh-2o2 <=> ic4ohket3-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2129,
    label = "ic4h7oh-3ooh-3o2 <=> ic4ohket3-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2130,
    label = "ic4ohket1-2 => oh + ocho + ch3coch3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2131,
#     label = "ic4ohket1-3 => oh + oh + ch3chco + ch2o",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2132,
    label = "ic4ohket3-1 => oh + hocho + ch2ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2133,
    label = "ic4ohket3-2 => oh + hoc2h4co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2134,
    label = "ic4ohket3-3 => oh + hoc2h4cho + hco",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2135,
    label = "ic4h7oho1-2 + oh => c3h5-s + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2136,
    label = "ic4h7oho1-3 + oh => c3h5-a + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2137,
    label = "ic4h7oho2-3 + oh => ch2o + ch2cch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2138,
    label = "ic4h7oho3-3 + oh => ch2o + ch2cch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2139,
    label = "ic4h7oho1-2 + ho2 => c3h5-s + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2140,
    label = "ic4h7oho1-3 + ho2 => c3h5-a + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2141,
    label = "ic4h7oho2-3 + ho2 => ch2o + ch2cch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2142,
    label = "ic4h7oho3-3 + ho2 => ch2o + ch2cch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2143,
    label = "tc4h8oh + o2 <=> tc4h8oh-o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2144,
    label = "tc4h8oh + tc4h8oh-o2 <=> tc4h8oh-o + tc4h8oh-o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2145,
    label = "tc4h8oh + ho2 <=> tc4h8oh-o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2146,
    label = "tc4h8oh + ch3o2 <=> tc4h8oh-o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2147,
    label = "tc4h8oh-o2 <=> tc4h7oh-ooh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(27000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2148,
    label = "tc4h8oh-o2 => ch3coch3 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.3e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2149,
    label = "tc4h8oh-o2 => c3ket12 + ch3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+09, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2150,
    label = "tc4h8oh-o2 + ho2 <=> tc4h8oh-o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2151,
    label = "tc4h8oh-o2 + h2o2 <=> tc4h8oh-o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2152,
    label = "tc4h8oh-o2 + ch3o2 => tc4h8oh-o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2153,
    label = "tc4h8oh-o2 + tc4h8oh-o2 => tc4h8oh-o + tc4h8oh-o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2154,
    label = "tc4h8oh-o2h => tc4h8oh-o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2155,
    label = "ch2o + ic3h6oh <=> tc4h8oh-o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2156,
    label = "tc4h7oh-ooh => tc4h7oho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2157,
    label = "tc4h7oh-ooh => oh + ch2o + ic3h5oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2158,
    label = "tc4h7oh-ooh + o2 <=> tc4h7oh-ooh-o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2159,
    label = "tc4h7oh-ooh-o2 => c3ket21 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2160,
    label = "tc4h7oh-ooh-o2 <=> tc4ohket + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2161,
    label = "tc4ohket => oh + hoc2h4co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2162,
    label = "tc4h7oho + oh => ch2o + ch2cch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2163,
    label = "tc4h7oho + ho2 => ch2o + ch2cch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2164,
    label = "sc4h8oh-1 + o2 <=> sc4h8oh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2165,
    label = "sc4h8oh-2 + o2 <=> sc4h8oh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2166,
    label = "sc4h8oh-3 + o2 <=> sc4h8oh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2167,
    label = "sc4h8ohm + o2 <=> sc4h8oh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2168,
    label = "sc4h8oh-1 + sc4h8oh-1o2 => sc4h8oh-1o + sc4h8oh-1o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2170,
    label = "sc4h8oh-1 + sc4h8oh-2o2 => sc4h8oh-1o + sc4h8oh-2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2171,
    label = "sc4h8oh-2 + sc4h8oh-1o2 => sc4h8oh-2o + sc4h8oh-1o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2172,
#     label = "sc4h8oh-2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2173,
    label = "sc4h8oh-2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2174,
    label = "sc4h8oh-3 + sc4h8oh-1o2 => sc4h8oh-3o + sc4h8oh-1o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2175,
#     label = "sc4h8oh-3 + sc4h8oh-2o2 => sc4h8oh-3o + sc4h8oh-2o",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2176,
    label = "sc4h8oh-3 + sc4h8oh-2o2 => sc4h8oh-3o + sc4h8oh-2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2177,
    label = "sc4h8ohm + sc4h8oh-1o2 => sc4h8oh-2o + sc4h8oh-1o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2178,
#     label = "sc4h8ohm + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2179,
    label = "sc4h8ohm + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2180,
    label = "sc4h8oh-1 + ho2 => sc4h8oh-1o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2181,
    label = "sc4h8oh-2 + ho2 => sc4h8oh-2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2182,
    label = "sc4h8oh-3 + ho2 => sc4h8oh-3o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2183,
    label = "sc4h8ohm + ho2 => sc4h8oh-2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2184,
    label = "sc4h8oh-1 + ch3o2 => sc4h8oh-1o + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2185,
    label = "sc4h8oh-2 + ch3o2 => sc4h8oh-2o + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2186,
    label = "sc4h8oh-3 + ch3o2 => sc4h8oh-3o + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2187,
    label = "sc4h8ohm + ch3o2 => sc4h8oh-2o + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2188,
    label = "sc4h8oh-1o2 <=> sc4h7oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2189,
    label = "sc4h8oh-1o2 <=> sc4h7oh-1ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2190,
    label = "sc4h8oh-1o2 <=> sc4h7oh-1ooh-m",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2191,
    label = "sc4h8oh-2o2 => ch3cho + ch3cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.3e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2192,
    label = "sc4h8oh-2o2 => c3ket12 + ch3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+09, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2193,
    label = "sc4h8oh-2o2 <=> sc4h7oh-2ooh-m",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2194,
    label = "sc4h8oh-2o2 <=> sc4h7oh-2ooh-3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2195,
    label = "sc4h8oh-2o2 <=> sc4h7oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2196,
    label = "sc4h8oh-3o2 <=> sc4h7oh-3ooh-1",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(18450, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(22950, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2197,
    label = "sc4h8oh-2o2 => c2h5cho + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.3e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2198,
#     label = "sc4h8oh-2o2 => ch2o + hco + c2h5 + oh",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(2e+09, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2199,
    label = "sc4h8oh-2o2 <=> sc4h7oh-2ooh-3",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(21950, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2200,
    label = "sc4h8oh-2o2 <=> sc4h7oh-mooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2201,
    label = "sc4h8oh-1o2 <=> c4h7oh1-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2202,
    label = "sc4h8oh-1o2 <=> c4h7oh2-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2203,
    label = "sc4h8oh-2o2 <=> c4h7oh2-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2204,
    label = "sc4h8oh-2o2 <=> c4h7oh1-3 + ho2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2205,
    label = "sc4h8oh-2o2 <=> ho2 + c4h7oh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2206,
    label = "sc4h8oh-1o2 + ho2 <=> sc4h8oh-1o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2207,
#     label = "sc4h8oh-2o2 + ho2 <=> sc4h8oh-2o2h + o2",
#     degeneracy = 1,
#     duplicate = True,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2208,
    label = "sc4h8oh-2o2 + ho2 <=> sc4h8oh-2o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2209,
    label = "sc4h8oh-1o2 + h2o2 <=> sc4h8oh-1o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2210,
#     label = "sc4h8oh-2o2 + h2o2 <=> sc4h8oh-2o2h + ho2",
#     degeneracy = 1,
#     duplicate = True,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2211,
    label = "sc4h8oh-2o2 + h2o2 <=> sc4h8oh-2o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2212,
    label = "sc4h8oh-1o2 + ch3o2 => sc4h8oh-1o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

# entry(
#     index = 2213,
#     label = "sc4h8oh-2o2 + ch3o2 => sc4h8oh-2o + ch3o + o2",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#         ],
#     ),
# )

entry(
    index = 2214,
    label = "sc4h8oh-2o2 + ch3o2 => sc4h8oh-2o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2215,
    label = "sc4h8oh-1o2 + sc4h8oh-1o2 => sc4h8oh-1o + sc4h8oh-1o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

# entry(
#     index = 2216,
#     label = "sc4h8oh-1o2 + sc4h8oh-2o2 => sc4h8oh-1o + sc4h8oh-2o + o2",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#         ],
#     ),
# )

entry(
    index = 2217,
    label = "sc4h8oh-1o2 + sc4h8oh-2o2 => sc4h8oh-1o + sc4h8oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

# entry(
#     index = 2218,
#     label = "sc4h8oh-2o2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o + o2",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#         ],
#     ),
# )

# entry(
#     index = 2219,
#     label = "sc4h8oh-2o2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o + o2",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#             Arrhenius(
#                 A = (1.4e+16, 'cm^3/(mol*s)'),
#                 n = -1.61,
#                 Ea = (1860, 'cal/mol'),
#                 T0 = (1, 'K'),
#             ),
#         ],
#     ),
# )

entry(
    index = 2220,
    label = "sc4h8oh-2o2 + sc4h8oh-2o2 => sc4h8oh-2o + sc4h8oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2221,
    label = "sc4h8oh-1o2h => sc4h8oh-1o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2222,
#     label = "sc4h8oh-2o2h => sc4h8oh-2o + oh",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2223,
    label = "sc4h8oh-2o2h => sc4h8oh-2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2224,
    label = "ch3ocho + c2h5 <=> sc4h8oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2225,
    label = "ch3cho + sc2h4oh <=> sc4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2226,
    label = "ch2o + ic3h6oh <=> sc4h8oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2227,
    label = "ch2o + c3h6oh-1 <=> sc4h8oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2228,
    label = "sc4h7oh-1ooh-2 => sc4h7oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2229,
    label = "sc4h7oh-1ooh-3 => sc4h7oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2230,
    label = "sc4h7oh-1ooh-m => sc4h7oho1-m + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2231,
    label = "sc4h7oh-2ooh-1 => sc4h7oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2232,
#     label = "sc4h7oh-2ooh-3 => sc4h7oho2-3 + oh",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2233,
    label = "sc4h7oh-2ooh-m => sc4h7oho2-m + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2234,
    label = "sc4h7oh-3ooh-1 => sc4h7oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2235,
    label = "sc4h7oh-3ooh-1 => sc4h7oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2236,
    label = "sc4h7oh-mooh-1 => sc4h7oho1-m + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2237,
    label = "sc4h7oh-2ooh-3 => sc4h7oho2-m + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2238,
    label = "sc4h7oh-2ooh-3 => sc4h7oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2239,
    label = "c4h7oh2-2 + ho2 => sc4h7oh-1ooh-2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2240,
    label = "c4h7oh1-2 + ho2 => sc4h7oh-1ooh-m",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2241,
    label = "c4h7oh2-2 + ho2 => sc4h7oh-2ooh-1",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2242,
    label = "c4h7oh1-3 + ho2 => sc4h7oh-2ooh-3",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2243,
    label = "c4h7oh2-2 + ho2 => sc4h7oh-mooh-1",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2244,
    label = "sc4h7oh-1ooh-3 => oh + ch3ocho + c2h4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2245,
    label = "sc4h7oh-2ooh-m => oh + ch3cho + c2h3oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2246,
    label = "sc4h7oh-3ooh-1 => oh + ch2o + ic3h5oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2247,
    label = "sc4h7oh-2ooh-3 => oh + ch2o + ch3chchoh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2248,
    label = "sc4h7oh-2ooh-1 + o2 <=> nc4ket23 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2249,
    label = "sc4h7oh-3ooh-1 + o2 <=> nc4ket24 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2250,
    label = "sc4h7oh-mooh-1 + o2 <=> nc4ket21 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.26e+17, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.28e+17, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.54e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.78e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2251,
    label = "sc4h7oh-1ooh-2 + o2 <=> sc4h7oh-1ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2252,
    label = "sc4h7oh-1ooh-3 + o2 <=> sc4h7oh-1ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2253,
    label = "sc4h7oh-1ooh-m + o2 <=> sc4h7oh-1ooh-mo2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2254,
    label = "sc4h7oh-2ooh-1 + o2 <=> sc4h7oh-2ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2255,
    label = "sc4h7oh-2ooh-3 + o2 <=> sc4h7oh-2ooh-3o2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 2256,
    label = "sc4h7oh-2ooh-m + o2 <=> sc4h7oh-2ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2257,
    label = "sc4h7oh-3ooh-1 + o2 <=> sc4h7oh-3ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2258,
    label = "sc4h7oh-3ooh-1 + o2 <=> sc4h7oh-3ooh-mo2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2259,
    label = "sc4h7oh-mooh-1 + o2 <=> sc4h7oh-mooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2260,
    label = "sc4h7oh-2ooh-3 + o2 <=> sc4h7oh-3ooh-2o2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

# entry(
#     index = 2261,
#     label = "sc4h7oh-1ooh-2o2 => ch3cho + co2 + ch3 + oh + oh",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 2262,
#     label = "sc4h7oh-3ooh-2o2 => ch3cho + ch2o + hco + oh + oh",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 2263,
#     label = "sc4h7oh-3ooh-2o2 <=> ch3cho + ch2o + hco + oh + oh",
#     degeneracy = 1,
#     kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 2264,
#     label = "sc4h7oh-1ooh-mo2 => ch3cho + co2 + ch3 + oh + oh",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 2265,
#     label = "sc4h7oh-3ooh-mo2 => ch3cho + ch2o + hco + oh + oh",
#     degeneracy = 1,
#     duplicate = True,
#     reversible = False,
#     kinetics = MultiArrhenius(
#         arrhenius = [
#             Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
#             Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
#         ],
#     ),
# )

entry(
    index = 2266,
    label = "sc4h7oh-2ooh-1o2 <=> sc4ohket2-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2267,
    label = "sc4h7oh-2ooh-3o2 <=> sc4ohket2-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2268,
    label = "sc4h7oh-2ooh-3o2 <=> sc4ohket2-m + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2269,
    label = "sc4h7oh-1ooh-2o2 <=> sc4ohket2-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2270,
    label = "sc4h7oh-1ooh-3o2 <=> sc4ohket2-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.68e+09, 's^-1'), n=0, Ea=(22950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2271,
    label = "sc4h7oh-1ooh-mo2 <=> sc4ohket2-m + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2272,
    label = "sc4h7oh-3ooh-1o2 <=> sc4ohket3-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2273,
    label = "sc4h7oh-3ooh-2o2 <=> sc4ohket3-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2274,
    label = "sc4h7oh-3ooh-mo2 <=> sc4ohket2-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(18950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2275,
    label = "sc4h7oh-mooh-1o2 <=> sc4ohket3-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(27000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2276,
    label = "sc4h7oh-3ooh-2o2 <=> c4ohket3-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2277,
    label = "sc4h7oh-3ooh-2o2 <=> c4ohket3-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(19950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2278,
    label = "sc4ohket2-1 => oh + hocho + c2h5co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2279,
    label = "sc4ohket2-3 => oh + hoch2co + ch3cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2280,
#     label = "sc4ohket2-m => oh + ch2co + ch2oh + ch2o",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2281,
    label = "sc4ohket3-1 => oh + hocho + ch3coch2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2282,
    label = "sc4ohket3-2 => oh + hoch2cho + ch3co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2283,
    label = "sc4ohket2-1 => oh + hoc2h4co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2284,
    label = "sc4ohket3-1 => oh + hocho + ch2ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2285,
    label = "c4ohket3-2 => oh + hoch2cho + ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2286,
    label = "c4ohket3-1 => oh + hoc2h4cho + hco",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2287,
    label = "sc4h7oho1-2 + oh => c3h5-s + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2288,
    label = "sc4h7oho1-3 + oh => c3h5-a + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2289,
    label = "sc4h7oho1-m + oh => c3h5-a + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2290,
    label = "sc4h7oho2-3 + oh => c2h3cho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2291,
    label = "sc4h7oho2-m + oh => c2h3cho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2292,
    label = "sc4h7oho2-3 + oh => pc2h4oh + ch2co + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2293,
    label = "sc4h7oho1-2 + ho2 => c3h5-s + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2294,
    label = "sc4h7oho1-3 + ho2 => c3h5-a + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2295,
    label = "sc4h7oho1-m + ho2 => c3h5-a + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2296,
    label = "sc4h7oho2-3 + ho2 => c2h3cho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2297,
    label = "sc4h7oho2-m + ho2 => c2h3cho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2298,
    label = "sc4h7oho2-3 + ho2 => pc2h4oh + ch2co + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2299,
    label = "nc5h12 <=> c5h11-1 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.375e+17, 's^-1'), n=-0.36, Ea=(101200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2300,
    label = "nc5h12 <=> c5h11-2 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.325e+18, 's^-1'), n=-0.763, Ea=(98800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2301,
    label = "nc5h12 <=> c5h11-3 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.602e+18, 's^-1'), n=-0.758, Ea=(98790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2302,
    label = "nc5h12 <=> ch3 + pc4h9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.101e+22, 's^-1'), n=-1.862, Ea=(89430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2303,
    label = "nc5h12 <=> nc3h7 + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.082e+24, 's^-1'), n=-2.269, Ea=(88440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2304,
    label = "nc5h12 + h <=> c5h11-1 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2305,
    label = "nc5h12 + h <=> c5h11-2 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2306,
    label = "nc5h12 + h <=> c5h11-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2307,
    label = "nc5h12 + oh <=> c5h11-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.57e+07, 'cm^3/(mol*s)'), n=1.8, Ea=(954, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2308,
    label = "nc5h12 + oh <=> c5h11-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.9e+06, 'cm^3/(mol*s)'), n=2, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2309,
    label = "nc5h12 + oh <=> c5h11-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.45e+06, 'cm^3/(mol*s)'), n=2, Ea=(-596, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2310,
    label = "nc5h12 + o <=> c5h11-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.092e+06, 'cm^3/(mol*s)'),
        n = 2.424,
        Ea = (4766, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2311,
    label = "nc5h12 + o <=> c5h11-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.189e+06, 'cm^3/(mol*s)'),
        n = 2.439,
        Ea = (2846, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2312,
    label = "nc5h12 + o <=> c5h11-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (594600, 'cm^3/(mol*s)'),
        n = 2.439,
        Ea = (2846, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2313,
    label = "nc5h12 + ch3 <=> c5h11-1 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2314,
    label = "nc5h12 + ch3 <=> c5h11-2 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (168000, 'cm^3/(mol*s)'),
        n = 2.133,
        Ea = (7574, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2315,
    label = "nc5h12 + ch3 <=> c5h11-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(84000, 'cm^3/(mol*s)'), n=2.133, Ea=(7574, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2316,
    label = "nc5h12 + ho2 <=> c5h11-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2317,
    label = "nc5h12 + ho2 <=> c5h11-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2318,
    label = "nc5h12 + ho2 <=> c5h11-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2319,
    label = "nc5h12 + ch3o2 <=> c5h11-1 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2320,
    label = "nc5h12 + ch3o2 <=> c5h11-2 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20.37, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2321,
    label = "nc5h12 + ch3o2 <=> c5h11-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10.19, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2322,
    label = "nc5h12 + c2h5 <=> c5h11-1 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2323,
    label = "nc5h12 + c2h5 <=> c5h11-2 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2324,
    label = "nc5h12 + c2h5 <=> c5h11-3 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2325,
    label = "nc5h12 + c2h3 <=> c5h11-1 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2326,
    label = "nc5h12 + c2h3 <=> c5h11-2 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(16800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2327,
    label = "nc5h12 + c2h3 <=> c5h11-3 + c2h4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 'cm^3/(mol*s)'), n=0, Ea=(16800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2328,
    label = "nc5h12 + c5h11-1 <=> c5h11-2 + nc5h12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2329,
    label = "nc5h12 + c5h11-1 <=> c5h11-3 + nc5h12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2330,
    label = "nc5h12 + c5h11-2 <=> c5h11-3 + nc5h12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(12300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2331,
    label = "nc5h12 + o2cho <=> c5h11-1 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2332,
    label = "nc5h12 + o2cho <=> c5h11-2 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2333,
    label = "nc5h12 + o2cho <=> c5h11-3 + ho2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2334,
    label = "nc5h12 + ch3o <=> c5h11-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2335,
    label = "nc5h12 + ch3o <=> c5h11-2 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2336,
    label = "nc5h12 + ch3o <=> c5h11-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2337,
    label = "nc5h12 + o2 <=> c5h11-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(52800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2338,
    label = "nc5h12 + o2 <=> c5h11-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(50160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2339,
    label = "nc5h12 + o2 <=> c5h11-3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(50160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2340,
    label = "c5h11-1 <=> c2h4 + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.094e+12, 's^-1'), n=0.451, Ea=(29430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2341,
    label = "c5h11-1 <=> h + c5h10-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.354e+11, 's^-1'), n=0.608, Ea=(35640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2342,
    label = "c5h11-1 <=> c5h11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.875e+09, 's^-1'), n=0.353, Ea=(19760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2343,
    label = "c5h11-1 <=> c5h11-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.8e+10, 's^-1'), n=0.67, Ea=(36600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2344,
    label = "c5h11-2 <=> c5h11-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.56e+10, 's^-1'), n=0.88, Ea=(39100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2345,
    label = "c5h11-2 <=> c3h6 + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.99e+11, 's^-1'), n=0.635, Ea=(29360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2346,
    label = "c5h11-2 <=> c5h10-1 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.353e+10, 's^-1'), n=1.011, Ea=(36680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2347,
    label = "c5h11-2 <=> c5h10-2 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.988e+11, 's^-1'), n=0.41, Ea=(35220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2348,
    label = "c5h11-3 <=> c4h8-1 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.072e+10, 's^-1'), n=1.119, Ea=(30460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2349,
    label = "c5h11-3 <=> c5h10-2 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.277e+11, 's^-1'), n=0.405, Ea=(35230, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2350,
    label = "c5h10-1 <=> c2h5 + c3h5-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.864e+21, 's^-1'), n=-2.086, Ea=(75060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2351,
    label = "c5h10-1 + h <=> c5h91-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2352,
    label = "c5h10-1 + h <=> c5h91-4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2353,
    label = "c5h10-1 + h <=> c5h91-5 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665000, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2354,
    label = "c5h10-1 + o <=> c5h91-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(660000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2355,
    label = "c5h10-1 + o <=> c5h91-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(551000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2356,
    label = "c5h10-1 + o <=> c5h91-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2357,
    label = "c5h10-1 + oh <=> c5h91-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2358,
    label = "c5h10-1 + oh <=> c5h91-4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2359,
    label = "c5h10-1 + oh <=> c5h91-5 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2360,
    label = "c5h10-1 + ch3 <=> c5h91-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2361,
    label = "c5h10-1 + ch3 <=> c5h91-4 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2362,
    label = "c5h10-1 + ch3 <=> c5h91-5 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.4521, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2363,
    label = "c5h10-1 + o2 <=> c5h91-3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2364,
    label = "c5h10-1 + o2 <=> c5h91-4 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2365,
    label = "c5h10-1 + o2 <=> c5h91-5 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2366,
    label = "c5h10-1 + ho2 <=> c5h91-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2367,
    label = "c5h10-1 + ho2 <=> c5h91-4 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2368,
    label = "c5h10-1 + ho2 <=> c5h91-5 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2369,
    label = "c5h10-1 + ch3o2 <=> c5h91-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2370,
    label = "c5h10-1 + ch3o2 <=> c5h91-4 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2371,
    label = "c5h10-1 + ch3o2 <=> c5h91-5 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2372,
    label = "c5h10-1 + ch3o <=> c5h91-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2373,
    label = "c5h10-1 + ch3o <=> c5h91-4 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2374,
    label = "c5h10-1 + ch3o <=> c5h91-5 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2375,
    label = "c5h10-2 + h <=> c5h91-3 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2492, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2376,
    label = "c5h10-2 + h <=> c5h92-4 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2377,
    label = "c5h10-2 + h <=> c5h92-5 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(665100, 'cm^3/(mol*s)'), n=2.54, Ea=(6756, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2378,
    label = "c5h10-2 + o <=> c5h91-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(441000, 'cm^3/(mol*s)'), n=2.42, Ea=(3150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2379,
    label = "c5h10-2 + o <=> c5h92-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(990000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2380,
    label = "c5h10-2 + o <=> c5h92-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(4750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2381,
    label = "c5h10-2 + oh <=> c5h91-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2382,
    label = "c5h10-2 + oh <=> c5h92-4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2383,
    label = "c5h10-2 + oh <=> c5h92-5 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2384,
    label = "c5h10-2 + ch3 <=> c5h91-3 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2385,
    label = "c5h10-2 + ch3 <=> c5h92-4 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2386,
    label = "c5h10-2 + ch3 <=> c5h92-5 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.4521, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2387,
    label = "c5h10-2 + o2 <=> c5h91-3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(39900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2388,
    label = "c5h10-2 + o2 <=> c5h92-4 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2389,
    label = "c5h10-2 + o2 <=> c5h92-5 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52290, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2390,
    label = "c5h10-2 + ho2 <=> c5h91-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2391,
    label = "c5h10-2 + ho2 <=> c5h92-4 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2392,
    label = "c5h10-2 + ho2 <=> c5h92-5 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2393,
    label = "c5h10-2 + ch3o2 <=> c5h91-3 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9639, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2394,
    label = "c5h10-2 + ch3o2 <=> c5h92-4 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2395,
    label = "c5h10-2 + ch3o2 <=> c5h92-5 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23800, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2396,
    label = "c5h10-2 + ch3o <=> c5h91-3 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(90, 'cm^3/(mol*s)'), n=2.95, Ea=(11990, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2397,
    label = "c5h10-2 + ch3o <=> c5h92-4 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2398,
    label = "c5h10-2 + ch3o <=> c5h92-5 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.17e+11, 'cm^3/(mol*s)'), n=0, Ea=(6458, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2399,
    label = "c5h91-3 + ho2 <=> c5h9o1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2400,
    label = "c5h91-3 + ch3o2 <=> c5h9o1-3 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2401,
    label = "c5h91-3 + c2h5o2 <=> c5h9o1-3 + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2402,
    label = "c5h92-4 + ho2 <=> c5h9o2-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2403,
    label = "c5h92-4 + ch3o2 <=> c5h9o2-4 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2404,
    label = "c5h92-4 + c2h5o2 <=> c5h9o2-4 + c2h5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.64e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2405,
    label = "c5h91-3 <=> c4h6 + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.554e+14, 's^-1'), n=-0.52, Ea=(38520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2406,
    label = "c5h91-3 <=> c5h81-3 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.733e+11, 's^-1'), n=0.636, Ea=(42640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2407,
    label = "c5h91-4 <=> c3h6 + c2h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.814e+11, 's^-1'), n=0.17, Ea=(35850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2408,
    label = "c5h91-5 <=> c2h4 + c3h5-a",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.157e+16, 's^-1'), n=-1.42, Ea=(17750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2409,
    label = "c5h92-4 <=> c5h81-3 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.015e+15, 's^-1'), n=-0.34, Ea=(46030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2410,
    label = "c5h92-5 <=> c2h4 + c3h5-s",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.899e+16, 's^-1'), n=-1.18, Ea=(42180, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2411,
    label = "c5h9o1-3 <=> c2h3cho + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.131e+19, 's^-1'), n=-1.85, Ea=(10670, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2412,
    label = "c5h9o1-3 <=> c2h5cho + c2h3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.417e+18, 's^-1'), n=-1.56, Ea=(23340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2413,
    label = "c5h81-3 + oh <=> ch2o + c4h71-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2414,
    label = "c5h81-3 + oh <=> c2h3cho + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2415,
    label = "c5h81-3 + oh <=> ch3cho + c3h5-s",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2416,
    label = "c5h9o2-4 <=> ch3chchcho + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.983e+15, 's^-1'), n=-1.13, Ea=(9941, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2417,
    label = "c5h9o2-4 <=> ch3cho + c3h5-s",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.073e+22, 's^-1'), n=-2.66, Ea=(29650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2418,
    label = "c5h10-2 <=> ch3 + c4h71-3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.486e+19, 's^-1'), n=-1.367, Ea=(76320, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (15270, 'cm^3/(mol*s)'),
            n = -24.826,
            Ea = (94800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.005301,
        T3 = (143.7, 'K'),
        T1 = (1.677e+13, 'K'),
        T2 = (3671, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2419,
    label = "c5h11-1 + o2 <=> c5h10-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2420,
    label = "c5h11-2 + o2 <=> c5h10-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.535, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2421,
    label = "c5h11-2 + o2 <=> c5h10-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2422,
    label = "c5h11-3 + o2 <=> c5h10-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2423,
    label = "c5h11-1 + ho2 <=> c5h11o-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2424,
    label = "c5h11-2 + ho2 <=> c5h11o-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2425,
    label = "c5h11-3 + ho2 <=> c5h11o-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2426,
    label = "c5h11-1 + ch3o2 <=> c5h11o-1 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2427,
    label = "c5h11-2 + ch3o2 <=> c5h11o-2 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2428,
    label = "c5h11-3 + ch3o2 <=> c5h11o-3 + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2429,
    label = "c5h11o2-1 + nc5h12 <=> c5h11o2h-1 + c5h11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(20430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2430,
    label = "c5h11o2-2 + nc5h12 <=> c5h11o2h-2 + c5h11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(20430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2431,
    label = "c5h11o2-3 + nc5h12 <=> c5h11o2h-3 + c5h11-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+13, 'cm^3/(mol*s)'), n=0, Ea=(20430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2432,
    label = "c5h11o2-1 + nc5h12 <=> c5h11o2h-1 + c5h11-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.064e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2433,
    label = "c5h11o2-2 + nc5h12 <=> c5h11o2h-2 + c5h11-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.064e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2434,
    label = "c5h11o2-3 + nc5h12 <=> c5h11o2h-3 + c5h11-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.064e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2435,
    label = "c5h11o2-1 + nc5h12 <=> c5h11o2h-1 + c5h11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.032e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2436,
    label = "c5h11o2-2 + nc5h12 <=> c5h11o2h-2 + c5h11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.032e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2437,
    label = "c5h11o2-3 + nc5h12 <=> c5h11o2h-3 + c5h11-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.032e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2438,
    label = "c5h11-1 + c5h11o2-1 <=> c5h11o-1 + c5h11o-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2439,
    label = "c5h11-1 + c5h11o2-2 <=> c5h11o-1 + c5h11o-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2440,
    label = "c5h11-1 + c5h11o2-3 <=> c5h11o-1 + c5h11o-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2441,
    label = "c5h11-2 + c5h11o2-1 <=> c5h11o-2 + c5h11o-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2442,
    label = "c5h11-2 + c5h11o2-2 <=> c5h11o-2 + c5h11o-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2443,
    label = "c5h11-2 + c5h11o2-3 <=> c5h11o-2 + c5h11o-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2444,
    label = "c5h11-3 + c5h11o2-1 <=> c5h11o-3 + c5h11o-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2445,
    label = "c5h11-3 + c5h11o2-2 <=> c5h11o-3 + c5h11o-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2446,
    label = "c5h11-3 + c5h11o2-3 <=> c5h11o-3 + c5h11o-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2447,
    label = "c5h11o2-1 + c5h11o2-2 => o2 + c5h11o-1 + c5h11o-2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2448,
    label = "c5h11o2-1 + c5h11o2-3 => o2 + c5h11o-1 + c5h11o-3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2449,
    label = "c5h11o2-1 + ch3o2 => o2 + c5h11o-1 + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2450,
    label = "c5h11o2-1 + c5h11o2-1 => o2 + c5h11o-1 + c5h11o-1",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2451,
    label = "h2o2 + c5h11o2-1 <=> ho2 + c5h11o2h-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2452,
    label = "c5h11o2-1 + ho2 <=> c5h11o2h-1 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2453,
    label = "c5h11o2-2 + ch3o2 => o2 + c5h11o-2 + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2454,
    label = "c5h11o2-2 + c5h11o2-3 => c5h11o-2 + c5h11o-3 + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2455,
    label = "c5h11o2-2 + c5h11o2-2 => o2 + c5h11o-2 + c5h11o-2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2456,
    label = "h2o2 + c5h11o2-2 <=> ho2 + c5h11o2h-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2457,
    label = "c5h11o2-2 + ho2 <=> c5h11o2h-2 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2458,
    label = "c5h11o2-3 + ch3o2 => o2 + c5h11o-3 + ch3o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2459,
    label = "c5h11o2-3 + c5h11o2-3 => o2 + c5h11o-3 + c5h11o-3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2460,
    label = "h2o2 + c5h11o2-3 <=> ho2 + c5h11o2h-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2461,
    label = "c5h11o2-3 + ho2 <=> c5h11o2h-3 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2462,
    label = "c5h11o2h-1 <=> c5h11o-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2463,
    label = "c5h11o2h-2 <=> c5h11o-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2464,
    label = "c5h11o2h-3 <=> c5h11o-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2465,
    label = "c5h11o-2 <=> ch3cho + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.689e+22, 's^-1'), n=-2.601, Ea=(19550, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2466,
    label = "c5h11o-3 <=> c2h5 + c2h5cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.239e+18, 's^-1'), n=-1.199, Ea=(18590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2467,
    label = "c5h11o2-1 <=> c5h11-1 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.338e+20, 's^-1'), n=-1.62, Ea=(35830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2468,
    label = "c5h11o2-2 <=> c5h11-2 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.087e+22, 's^-1'), n=-2.287, Ea=(38150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2469,
    label = "c5h11o2-3 <=> c5h11-3 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.415e+22, 's^-1'), n=-2.282, Ea=(38150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2470,
    label = "c5h11o2-1 <=> c5h10ooh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2471,
    label = "c5h11o2-1 <=> c5h10ooh1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2472,
    label = "c5h11o2-1 <=> c5h10ooh1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(18650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2473,
    label = "c5h11o2-1 <=> c5h10ooh1-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.86e+08, 's^-1'), n=0, Ea=(25150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2474,
    label = "c5h11o2-2 <=> c5h10ooh2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2475,
    label = "c5h11o2-2 <=> c5h10ooh2-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2476,
    label = "c5h11o2-2 <=> c5h10ooh2-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2477,
    label = "c5h11o2-2 <=> c5h10ooh2-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(21950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2478,
    label = "c5h11o2-3 <=> c5h10ooh3-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2479,
    label = "c5h11o2-3 <=> c5h10ooh3-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2480,
    label = "c5h11o2-1 <=> c5h10-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.044e+38, 's^-1'), n=-8.11, Ea=(40490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2481,
    label = "c5h11o2-2 <=> c5h10-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.075e+42, 's^-1'), n=-9.41, Ea=(41490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2482,
    label = "c5h11o2-2 <=> c5h10-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.044e+38, 's^-1'), n=-8.11, Ea=(40490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2483,
    label = "c5h11o2-3 <=> c5h10-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.009e+39, 's^-1'), n=-8.11, Ea=(40490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2484,
    label = "c5h10ooh1-2 => c5h10o1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2485,
    label = "c5h10ooh1-3 => c5h10o1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2486,
    label = "c5h10ooh1-4 => c5h10o1-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.375e+09, 's^-1'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2487,
    label = "c5h10ooh1-5 => c5h10o1-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.172e+09, 's^-1'), n=0, Ea=(1800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2488,
    label = "c5h10ooh2-1 => c5h10o1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2489,
    label = "c5h10ooh2-3 => c5h10o2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2490,
    label = "c5h10ooh2-4 => c5h10o2-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2491,
    label = "c5h10ooh2-5 => c5h10o1-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.375e+09, 's^-1'), n=0, Ea=(6000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2492,
    label = "c5h10ooh3-2 => c5h10o2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2493,
    label = "c5h10ooh3-1 => c5h10o1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2494,
    label = "c5h10o1-2 + oh => ch2co + nc3h7 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2495,
    label = "c5h10o1-3 + oh => c2h4 + c2h5co + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2496,
    label = "c5h10o1-4 + oh => ch3coch2 + c2h4 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2497,
    label = "c5h10o1-5 + oh => ch2ch2cho + c2h4 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2498,
    label = "c5h10o2-3 + oh => ch3chco + c2h5 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2499,
    label = "c5h10o2-4 + oh => ch3co + c3h6 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2500,
    label = "c5h10o1-2 + oh => c2h3cho + c2h5 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2501,
    label = "c5h10o1-3 + oh => hco + c4h8-1 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2502,
    label = "c5h10o1-4 + oh => ch2cho + c3h6 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2503,
    label = "c5h10o1-5 + oh => ch2o + c4h71-3 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2504,
    label = "c5h10o2-3 + oh => c2h3coch3 + ch3 + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2505,
    label = "c5h10o2-4 + oh => ch3cho + c3h5-s + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2506,
    label = "c5h10o1-2 + ho2 => ch2co + nc3h7 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2507,
    label = "c5h10o1-3 + ho2 => c2h4 + c2h5co + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2508,
    label = "c5h10o1-4 + ho2 => ch3coch2 + c2h4 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2509,
    label = "c5h10o1-5 + ho2 => ch2ch2cho + c2h4 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2510,
    label = "c5h10o2-3 + ho2 => ch3chco + c2h5 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2511,
    label = "c5h10o2-4 + ho2 => ch3co + c3h6 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2512,
    label = "c5h10o1-2 + ho2 => c2h3cho + c2h5 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2513,
    label = "c5h10o1-3 + ho2 => hco + c4h8-1 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2514,
    label = "c5h10o1-4 + ho2 => ch2cho + c3h6 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2515,
    label = "c5h10o1-5 + ho2 => ch2o + c4h71-3 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2516,
    label = "c5h10o2-3 + ho2 => c2h3coch3 + ch3 + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2517,
    label = "c5h10o2-4 + ho2 => ch3cho + c3h5-s + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2518,
    label = "c5h10ooh1-2 <=> c5h10-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.449e+17, 's^-1'), n=-1.556, Ea=(17980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2519,
    label = "c5h10ooh2-1 <=> c5h10-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.462e+19, 's^-1'), n=-2.231, Ea=(21050, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2520,
    label = "c5h10ooh2-3 <=> c5h10-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.651e+19, 's^-1'), n=-2.455, Ea=(20680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2521,
    label = "c5h10ooh3-2 <=> c5h10-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.651e+19, 's^-1'), n=-2.455, Ea=(20680, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2522,
    label = "c5h10ooh1-3 => oh + ch2o + c4h8-1",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.283e+13, 's^-1'), n=-0.17, Ea=(30090, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2523,
    label = "c5h10ooh2-4 => oh + ch3cho + c3h6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.312e+17, 's^-1'), n=-1.4, Ea=(27170, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2524,
    label = "c5h10ooh3-1 => oh + c2h5cho + c2h4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.096e+18, 's^-1'), n=-1.73, Ea=(26820, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2525,
    label = "c5h10ooh1-2o2 <=> c5h10ooh1-2 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.039e+22, 's^-1'), n=-2.295, Ea=(37970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2526,
    label = "c5h10ooh1-3o2 <=> c5h10ooh1-3 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.039e+22, 's^-1'), n=-2.295, Ea=(37970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2527,
    label = "c5h10ooh1-4o2 <=> c5h10ooh1-4 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.039e+22, 's^-1'), n=-2.295, Ea=(37970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2528,
    label = "c5h10ooh1-5o2 <=> c5h10ooh1-5 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.777e+20, 's^-1'), n=-1.623, Ea=(35690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2529,
    label = "c5h10ooh2-1o2 <=> c5h10ooh2-1 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.572e+20, 's^-1'), n=-1.62, Ea=(35650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2530,
    label = "c5h10ooh2-3o2 <=> c5h10ooh2-3 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.251e+22, 's^-1'), n=-2.29, Ea=(37910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2531,
    label = "c5h10ooh2-4o2 <=> c5h10ooh2-4 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.251e+22, 's^-1'), n=-2.29, Ea=(37910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2532,
    label = "c5h10ooh2-5o2 <=> c5h10ooh2-5 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.572e+20, 's^-1'), n=-1.62, Ea=(35650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2533,
    label = "c5h10ooh3-1o2 <=> c5h10ooh3-1 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.572e+20, 's^-1'), n=-1.62, Ea=(35650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2534,
    label = "c5h10ooh3-2o2 <=> c5h10ooh3-2 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.251e+22, 's^-1'), n=-2.29, Ea=(37910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2535,
    label = "c5h10ooh1-2o2 <=> nc5ket12 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2536,
    label = "c5h10ooh1-3o2 <=> nc5ket13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2537,
    label = "c5h10ooh1-4o2 <=> nc5ket14 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.125e+09, 's^-1'), n=0, Ea=(18950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2538,
    label = "c5h10ooh1-5o2 <=> nc5ket15 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.907e+08, 's^-1'), n=0, Ea=(22150, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2539,
    label = "c5h10ooh2-1o2 <=> nc5ket21 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2540,
    label = "c5h10ooh2-3o2 <=> nc5ket23 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2541,
    label = "c5h10ooh2-4o2 <=> nc5ket24 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2542,
    label = "c5h10ooh2-5o2 <=> nc5ket25 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.563e+09, 's^-1'), n=0, Ea=(15650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2543,
    label = "c5h10ooh3-1o2 <=> nc5ket31 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2544,
    label = "c5h10ooh3-2o2 <=> nc5ket32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2545,
    label = "nc5ket12 => nc3h7cho + hco + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2546,
    label = "nc5ket13 => c2h5cho + ch2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2547,
    label = "nc5ket14 => ch3cho + ch2ch2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2548,
    label = "nc5ket15 => ch2o + c3h6cho-1 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2549,
    label = "nc5ket21 => ch2o + nc3h7co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2550,
    label = "nc5ket23 => c2h5cho + ch3co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2551,
    label = "nc5ket24 => ch3cho + ch3coch2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2552,
    label = "nc5ket25 => ch2o + ch2ch2coch3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2553,
    label = "nc5ket31 => ch2o + c2h5coch2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2554,
    label = "nc5ket32 => ch3cho + c2h5co + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2555,
    label = "c5h10oh-1 <=> c5h10-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 's^-1'), n=0, Ea=(25830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2556,
    label = "c5h10oh-2 <=> c5h10-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+13, 's^-1'), n=0, Ea=(25830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2557,
    label = "o2c5h10oh-1 <=> c5h10oh-1 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.058e+21, 's^-1'), n=-1.84, Ea=(37750, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2558,
    label = "o2c5h10oh-1 => nc3h7cho + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(18860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2559,
    label = "o2c5h10oh-2 <=> c5h10oh-2 + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.385e+21, 's^-1'), n=-2.01, Ea=(37870, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2560,
    label = "o2c5h10oh-2 => c2h5cho + ch3cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(18860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2561,
    label = "nc5h11oh <=> ch3 + c4h8oh-4",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.79e+24, 's^-1'), n=-2.23, Ea=(88070, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.782e+60, 'cm^3/(mol*s)'),
            n = -12.28,
            Ea = (83980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.2352,
        T3 = (724, 'K'),
        T1 = (5e+09, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2562,
    label = "nc5h11oh <=> c2h5 + c3h6oh-3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.082e+24, 's^-1'), n=-2.269, Ea=(88440, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (8.025e+113, 'cm^3/(mol*s)'),
            n = -27.65,
            Ea = (96450, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 9.7028e-05,
        T3 = (268.4, 'K'),
        T1 = (268.4, 'K'),
        T2 = (4740.1, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2563,
    label = "nc5h11oh <=> nc3h7 + pc2h4oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.53e+24, 's^-1'), n=-2.23, Ea=(89010, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.632e+59, 'cm^3/(mol*s)'),
            n = -12.13,
            Ea = (84720, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.2438,
        T3 = (744.06, 'K'),
        T1 = (5e+09, 'K'),
        T2 = (5e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2564,
    label = "nc5h11oh <=> pc4h9 + ch2oh",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.02e+23, 's^-1'), n=-1.88, Ea=(85710, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.416e+59, 'cm^3/(mol*s)'),
            n = -11.93,
            Ea = (83980, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7646,
        T3 = (8.344e+09, 'K'),
        T1 = (724.8, 'K'),
        T2 = (8.214e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2565,
    label = "nc5h11oh <=> oh + c5h11-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.33e+20, 's^-1'), n=-1.37, Ea=(94930, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.902e+51, 'cm^3/(mol*s)'),
            n = -10.21,
            Ea = (89200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.703,
        T3 = (9.882e+09, 'K'),
        T1 = (634.68, 'K'),
        T2 = (1.786e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2566,
    label = "nc5h11oh <=> h + c5h11o-1",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.04e+14, 's^-1'), n=0.1, Ea=(103800, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.408e+39, 'cm^3/(mol*s)'),
            n = -7.03,
            Ea = (95960, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.3865,
        T3 = (564.91, 'K'),
        T1 = (4.438e+09, 'K'),
        T2 = (6.71e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2567,
    label = "nc5h11oh <=> c5h10-1 + h2o",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.52e+13, 's^-1'), n=0, Ea=(67230, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.69e+75, 'cm^3/(mol*s)'),
            n = -17.04,
            Ea = (64750, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.08,
        T3 = (1, 'K'),
        T1 = (9.924e+09, 'K'),
        T2 = (9.924e+09, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 2568,
    label = "h + c5h10oh11 <=> nc5h11oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2569,
    label = "h + c5h10oh12 <=> nc5h11oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2570,
    label = "h + c5h10oh13 <=> nc5h11oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2571,
    label = "h + c5h10oh14 <=> nc5h11oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2572,
    label = "h + c5h10oh15 <=> nc5h11oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2573,
    label = "nc5h11oh + h <=> c5h10oh15 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(174500, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2574,
    label = "nc5h11oh + h <=> c5h10oh14 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2575,
    label = "nc5h11oh + h <=> c5h10oh13 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2576,
    label = "nc5h11oh + h <=> c5h10oh12 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(108000, 'cm^3/(mol*s)'), n=2.69, Ea=(4440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2577,
    label = "nc5h11oh + h <=> c5h10oh11 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(87890, 'cm^3/(mol*s)'), n=2.68, Ea=(2915, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2578,
    label = "nc5h11oh + h <=> c5h11o-1 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(945, 'cm^3/(mol*s)'), n=3.14, Ea=(8701, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2579,
    label = "nc5h11oh + oh <=> c5h10oh15 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.28e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1590, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2580,
    label = "nc5h11oh + oh <=> c5h10oh14 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2581,
    label = "nc5h11oh + oh <=> c5h10oh13 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1141, 'cm^3/(mol*s)'), n=2.87, Ea=(-2926, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2582,
    label = "nc5h11oh + oh <=> c5h10oh12 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54, 'cm^3/(mol*s)'), n=3.7, Ea=(-3736, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2583,
    label = "nc5h11oh + oh <=> c5h10oh11 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3610, 'cm^3/(mol*s)'), n=2.89, Ea=(-2291, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2584,
    label = "nc5h11oh + oh <=> c5h11o-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(588, 'cm^3/(mol*s)'), n=2.82, Ea=(-585, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2585,
    label = "nc5h11oh + o <=> c5h10oh15 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.046e+06, 'cm^3/(mol*s)'),
        n = 2.424,
        Ea = (4766, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2586,
    label = "nc5h11oh + o <=> c5h10oh14 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (594600, 'cm^3/(mol*s)'),
        n = 2.439,
        Ea = (2846, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2587,
    label = "nc5h11oh + o <=> c5h10oh13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(552000, 'cm^3/(mol*s)'), n=2.45, Ea=(2830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2588,
    label = "nc5h11oh + o <=> c5h10oh12 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(144000, 'cm^3/(mol*s)'), n=2.61, Ea=(3029, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2589,
    label = "nc5h11oh + o <=> c5h10oh11 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(145000, 'cm^3/(mol*s)'), n=2.47, Ea=(876, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2590,
    label = "nc5h11oh + o <=> c5h11o-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00146, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2591,
    label = "nc5h11oh + o2 <=> ho2 + c5h10oh15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2592,
    label = "nc5h11oh + o2 <=> ho2 + c5h10oh14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2593,
    label = "nc5h11oh + o2 <=> ho2 + c5h10oh13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2594,
    label = "nc5h11oh + o2 <=> ho2 + c5h10oh12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2595,
    label = "nc5h11oh + o2 <=> ho2 + c5h10oh11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(46800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2596,
    label = "nc5h11oh + o2 <=> ho2 + c5h11o-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(56340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2597,
    label = "nc5h11oh + ho2 <=> c5h10oh15 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20.4, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2598,
    label = "nc5h11oh + ho2 <=> c5h10oh14 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2599,
    label = "nc5h11oh + ho2 <=> c5h10oh13 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000276, 'cm^3/(mol*s)'),
        n = 4.76,
        Ea = (11850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2600,
    label = "nc5h11oh + ho2 <=> c5h10oh12 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00751, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (14710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2601,
    label = "nc5h11oh + ho2 <=> c5h10oh11 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e-05, 'cm^3/(mol*s)'),
        n = 5.26,
        Ea = (8268, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2602,
    label = "nc5h11oh + ho2 <=> c5h11o-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.47e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (10530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2603,
    label = "nc5h11oh + ch3 <=> c5h10oh15 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.452, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2604,
    label = "nc5h11oh + ch3 <=> c5h10oh14 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(84000, 'cm^3/(mol*s)'), n=2.133, Ea=(7574, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2605,
    label = "nc5h11oh + ch3 <=> c5h10oh13 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2606,
    label = "nc5h11oh + ch3 <=> c5h10oh12 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.02, 'cm^3/(mol*s)'), n=3.23, Ea=(6461, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2607,
    label = "nc5h11oh + ch3 <=> c5h10oh11 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.93, 'cm^3/(mol*s)'), n=3.37, Ea=(7634, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2608,
    label = "nc5h11oh + ch3 <=> c5h11o-1 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02, 'cm^3/(mol*s)'), n=3.57, Ea=(8221, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2609,
    label = "nc5h11oh + hco <=> c5h10oh15 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102000, 'cm^3/(mol*s)'), n=2.5, Ea=(18440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2610,
    label = "nc5h11oh + hco <=> c5h10oh14 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2611,
    label = "nc5h11oh + hco <=> c5h10oh13 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.09e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2612,
    label = "nc5h11oh + hco <=> c5h10oh12 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (516000, 'cm^3/(mol*s)'),
        n = 2.25,
        Ea = (16760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2613,
    label = "nc5h11oh + hco <=> c5h10oh11 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+07, 'cm^3/(mol*s)'), n=1.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2614,
    label = "nc5h11oh + hco <=> c5h11o-1 + ch2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34000, 'cm^3/(mol*s)'), n=2.5, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2615,
    label = "nc5h11oh + ch2oh <=> c5h10oh15 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(101, 'cm^3/(mol*s)'), n=2.95, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2616,
    label = "nc5h11oh + ch2oh <=> c5h10oh14 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60.2, 'cm^3/(mol*s)'), n=2.95, Ea=(11980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2617,
    label = "nc5h11oh + ch2oh <=> c5h10oh13 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60.2, 'cm^3/(mol*s)'), n=2.95, Ea=(11980, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2618,
    label = "nc5h11oh + ch2oh <=> c5h10oh12 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15.3, 'cm^3/(mol*s)'), n=3.11, Ea=(12210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2619,
    label = "nc5h11oh + ch2oh <=> c5h10oh11 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60, 'cm^3/(mol*s)'), n=2.95, Ea=(12000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2620,
    label = "nc5h11oh + ch2oh <=> c5h11o-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120, 'cm^3/(mol*s)'), n=2.76, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2621,
    label = "nc5h11oh + ch3o <=> c5h10oh15 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2622,
    label = "nc5h11oh + ch3o <=> c5h10oh14 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2623,
    label = "nc5h11oh + ch3o <=> c5h10oh13 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+11, 'cm^3/(mol*s)'), n=0, Ea=(4571, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2624,
    label = "nc5h11oh + ch3o <=> c5h10oh12 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.02e+10, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (4703, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2625,
    label = "nc5h11oh + ch3o <=> c5h10oh11 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+11, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2626,
    label = "nc5h11oh + ch3o <=> c5h11o-1 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2627,
    label = "nc5h11oh + ch3o2 <=> c5h10oh15 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.693, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2628,
    label = "nc5h11oh + ch3o2 <=> c5h10oh14 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10.185, 'cm^3/(mol*s)'),
        n = 3.58,
        Ea = (14810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2629,
    label = "nc5h11oh + ch3o2 <=> c5h10oh13 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.88e-05, 'cm^3/(mol*s)'),
        n = 4.7,
        Ea = (11470, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2630,
    label = "nc5h11oh + ch3o2 <=> c5h10oh12 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000536, 'cm^3/(mol*s)'),
        n = 4.66,
        Ea = (13520, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2631,
    label = "nc5h11oh + ch3o2 <=> c5h10oh11 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0255, 'cm^3/(mol*s)'), n=4.34, Ea=(9022, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2632,
    label = "nc5h11oh + ch3o2 <=> c5h11o-1 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0056, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (16730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2633,
    label = "nc5h11oh + c2h5 <=> c5h10oh15 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2634,
    label = "nc5h11oh + c2h5 <=> c5h10oh14 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2635,
    label = "nc5h11oh + c2h5 <=> c5h10oh13 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2636,
    label = "nc5h11oh + c2h5 <=> c5h10oh12 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.01e+10, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2637,
    label = "nc5h11oh + c2h5 <=> c5h10oh11 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(7900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2638,
    label = "nc5h11oh + c2h5 <=> c5h11o-1 + c2h6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+10, 'cm^3/(mol*s)'), n=0, Ea=(13400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2639,
    label = "c5h11o-1 <=> c5h10oh14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.132, 's^-1'), n=3.632, Ea=(2689, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2640,
    label = "c5h11o-1 <=> c5h10oh13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.32e-10, 's^-1'), n=6.204, Ea=(6710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2641,
    label = "c5h11o-1 <=> c5h10oh15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.32e-10, 's^-1'), n=6.204, Ea=(6710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2642,
    label = "c5h10oh15 <=> c5h10oh11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386e+09, 's^-1'), n=0.98, Ea=(33760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2643,
    label = "c5h10oh15 <=> c5h10oh12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.541e+09, 's^-1'), n=0.35, Ea=(19760, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2644,
    label = "c5h10oh14 <=> c5h10oh11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.587e+08, 's^-1'), n=1.39, Ea=(39700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2645,
    label = "c2h4 + c3h6oh-3 <=> c5h10oh15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2646,
    label = "h + c5h9oh1-4 <=> c5h10oh15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2647,
    label = "c3h6 + pc2h4oh <=> c5h10oh14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2648,
    label = "h + c5h9oh1-4 <=> c5h10oh14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2649,
    label = "h + c5h9oh1-3 <=> c5h10oh14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2650,
    label = "c4h8-1 + ch2oh <=> c5h10oh13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2651,
    label = "c4h7oh1-4 + ch3 <=> c5h10oh13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17600, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2652,
    label = "h + c5h9oh1-3 <=> c5h10oh13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2653,
    label = "h + c5h9oh1-2 <=> c5h10oh13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2654,
    label = "c5h10-1 + oh <=> c5h10oh12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.93e+11, 'cm^3/(mol*s)'), n=0, Ea=(-960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2655,
    label = "c3h5oh + c2h5 <=> c5h10oh12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2656,
    label = "h + c5h9oh1-2 <=> c5h10oh12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2657,
    label = "h + c5h9oh1-1 <=> c5h10oh12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2658,
    label = "c2h3oh + nc3h7 <=> c5h10oh11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8800, 'cm^3/(mol*s)'), n=2.48, Ea=(6130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2659,
    label = "nc4h9cho + h <=> c5h10oh11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2660,
    label = "c5h9oh1-1 + h <=> c5h10oh11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (2620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2661,
    label = "h + nc4h9cho <=> c5h11o-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2662,
    label = "pc4h9 + ch2o <=> c5h11o-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(3457, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2663,
    label = "c3h6oh-3 <=> c2h4 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.231e+10, 's^-1'), n=1.035, Ea=(28170, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2664,
    label = "c3h6oh-3 <=> h + c3h5oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.432e+12, 's^-1'), n=0.225, Ea=(36340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2665,
    label = "c3h6oh-3 <=> nc3h7o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.32e-10, 's^-1'), n=6.204, Ea=(6710, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2666,
    label = "c5h9oh1-4 + h <=> c5h8oh43 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2667,
    label = "c5h9oh1-4 + o <=> c5h8oh43 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(660000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2668,
    label = "c5h9oh1-4 + oh <=> c5h8oh43 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2669,
    label = "c5h9oh1-4 + ch3 <=> c5h8oh43 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2670,
    label = "c5h9oh1-4 + ho2 <=> c5h8oh43 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2671,
    label = "c5h9oh1-4 + ch3o2 <=> c5h8oh43 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2672,
    label = "c5h9oh1-4 + ch3o <=> c5h8oh43 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2673,
    label = "c5h9oh1-4 + o2 <=> c5h8oh43 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(49640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2674,
    label = "c5h9oh1-3 + h <=> c5h8oh32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2675,
    label = "c5h9oh1-3 + o <=> c5h8oh32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(990000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2676,
    label = "c5h9oh1-3 + oh <=> c5h8oh32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2677,
    label = "c5h9oh1-3 + ch3 <=> c5h8oh32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2678,
    label = "c5h9oh1-3 + ho2 <=> c5h8oh32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2679,
    label = "c5h9oh1-3 + ch3o2 <=> c5h8oh32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2680,
    label = "c5h9oh1-3 + ch3o <=> c5h8oh32 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2681,
    label = "c5h9oh1-3 + o2 <=> c5h8oh32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2682,
    label = "c5h9oh1-2 + h <=> c5h8oh32 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2683,
    label = "c5h9oh1-2 + o <=> c5h8oh32 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(990000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2684,
    label = "c5h9oh1-2 + oh <=> c5h8oh32 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2685,
    label = "c5h9oh1-2 + ch3 <=> c5h8oh32 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2686,
    label = "c5h9oh1-2 + ho2 <=> c5h8oh32 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2687,
    label = "c5h9oh1-2 + ch3o2 <=> c5h8oh32 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2688,
    label = "c5h9oh1-2 + ch3o <=> c5h8oh32 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2689,
    label = "c5h9oh1-2 + o2 <=> c5h8oh32 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2690,
    label = "c5h9oh1-1 + h <=> c5h8oh21 + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(337600, 'cm^3/(mol*s)'), n=2.36, Ea=(207, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2691,
    label = "c5h9oh1-1 + o <=> c5h8oh21 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(990000, 'cm^3/(mol*s)'), n=2.43, Ea=(1210, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2692,
    label = "c5h9oh1-1 + oh <=> c5h8oh21 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27640, 'cm^3/(mol*s)'), n=2.64, Ea=(-1919, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2693,
    label = "c5h9oh1-1 + ch3 <=> c5h8oh21 + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.69, 'cm^3/(mol*s)'), n=3.31, Ea=(4002, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2694,
    label = "c5h9oh1-1 + ho2 <=> c5h8oh21 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2695,
    label = "c5h9oh1-1 + ch3o2 <=> c5h8oh21 + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4820, 'cm^3/(mol*s)'), n=2.55, Ea=(10530, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2696,
    label = "c5h9oh1-1 + ch3o <=> c5h8oh21 + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40, 'cm^3/(mol*s)'), n=2.9, Ea=(8609, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2697,
    label = "c5h9oh1-1 + o2 <=> c5h8oh21 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+12, 'cm^3/(mol*s)'), n=0, Ea=(37220, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2698,
    label = "c5h9oh1-1 + ho2 <=> nc4h9cho + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(149000, 'cm^3/(mol*s)'), n=1.67, Ea=(6810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2699,
    label = "c5h9oh1-1 + hocho <=> nc4h9cho + hocho",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4509, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2700,
    label = "c5h9oh1-1 + h <=> c5h10-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2701,
    label = "c5h9oh1-1 + h <=> c2h3oh + nc3h7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2702,
    label = "c5h9oh1-2 + h <=> c5h10-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2703,
    label = "c5h9oh1-2 + h <=> c4h8-1 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2704,
    label = "c5h9oh1-3 + h <=> c3h6 + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2705,
    label = "c5h9oh1-3 + h <=> c4h8-1 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2706,
    label = "c5h9oh1-4 + h <=> c2h4 + c3h6oh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2707,
    label = "c5h9oh1-4 + h <=> c3h6 + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.26e+13, 'cm^3/(mol*s)'), n=0, Ea=(4500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2708,
    label = "c5h8oh43 <=> c4h6 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.554e+14, 's^-1'), n=-0.52, Ea=(38520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2709,
    label = "c5h8oh43 <=> c5h7oh42 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.733e+11, 's^-1'), n=0.636, Ea=(42640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2710,
    label = "c5h8oh32 <=> c5h7oh42 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.015e+15, 's^-1'), n=-0.34, Ea=(46030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2711,
    label = "c5h8oh32 <=> c5h81-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.035e+16, 's^-1'), n=-1.012, Ea=(36070, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2712,
    label = "c5h8oh32 <=> c5h7oh13 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.733e+11, 's^-1'), n=0.636, Ea=(42640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2713,
    label = "c5h8oh21 <=> c5h7oh13 + h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.733e+11, 's^-1'), n=0.636, Ea=(42640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2714,
    label = "c5h8oh21 <=> ch3 + c4h5oh-13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.554e+14, 's^-1'), n=-0.52, Ea=(38520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2715,
    label = "c5h7oh42 <=> c4h5-n + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.61e+21, 's^-1'), n=-1.612, Ea=(106000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2716,
    label = "c5h7oh13 <=> c3h5-s + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.816e+24, 's^-1'), n=-2.381, Ea=(90130, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2717,
    label = "c5h9oh1-4 <=> c5h91-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2718,
    label = "c5h9oh1-3 <=> c5h92-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2719,
    label = "c5h9oh1-2 <=> c5h91-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.367e+20, 's^-1'), n=-1.189, Ea=(94340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2720,
    label = "c5h9oh1-1 <=> c5h91-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.887e+19, 's^-1'), n=-0.956, Ea=(95950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2721,
    label = "c5h9oh1-1 <=> nc3h7 + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.214e+22, 's^-1'), n=-1.576, Ea=(97520, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2722,
    label = "c5h9oh1-2 <=> c4h71-1 + ch2oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2723,
    label = "c5h9oh1-3 <=> c3h5-a + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.644e+19, 's^-1'), n=-1.132, Ea=(74590, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2724,
    label = "c5h9oh1-4 <=> c3h5-a + pc2h4oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.864e+21, 's^-1'), n=-2.086, Ea=(75060, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2725,
    label = "c5h10oh11 + o2 <=> nc4h9cho + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.85e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.512e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2726,
    label = "c5h10oh11 + o2 <=> c5h10oh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2727,
    label = "c5h10oh12 + o2 <=> c5h10oh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2728,
    label = "c5h10oh13 + o2 <=> c5h10oh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2729,
    label = "c5h10oh14 + o2 <=> c5h10oh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2730,
    label = "c5h10oh15 + o2 <=> c5h10oh-5o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2731,
    label = "c5h10oh11 + c5h10oh-1o2 <=> c5h10oh-1o + c5h10oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2732,
    label = "c5h10oh11 + c5h10oh-2o2 <=> c5h10oh-1o + c5h10oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2733,
    label = "c5h10oh11 + c5h10oh-3o2 <=> c5h10oh-1o + c5h10oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2734,
    label = "c5h10oh11 + c5h10oh-4o2 <=> c5h10oh-1o + c5h10oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2735,
    label = "c5h10oh11 + c5h10oh-5o2 <=> c5h10oh-1o + c5h10oh-5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2736,
    label = "c5h10oh12 + c5h10oh-1o2 <=> c5h10oh-2o + c5h10oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2737,
    label = "c5h10oh12 + c5h10oh-2o2 <=> c5h10oh-2o + c5h10oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2738,
    label = "c5h10oh12 + c5h10oh-3o2 <=> c5h10oh-2o + c5h10oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2739,
    label = "c5h10oh12 + c5h10oh-4o2 <=> c5h10oh-2o + c5h10oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2740,
    label = "c5h10oh12 + c5h10oh-5o2 <=> c5h10oh-2o + c5h10oh-5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2741,
    label = "c5h10oh13 + c5h10oh-1o2 <=> c5h10oh-3o + c5h10oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2742,
    label = "c5h10oh13 + c5h10oh-2o2 <=> c5h10oh-3o + c5h10oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2743,
    label = "c5h10oh13 + c5h10oh-3o2 <=> c5h10oh-3o + c5h10oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2744,
    label = "c5h10oh13 + c5h10oh-4o2 <=> c5h10oh-3o + c5h10oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2745,
    label = "c5h10oh13 + c5h10oh-5o2 <=> c5h10oh-3o + c5h10oh-5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2746,
    label = "c5h10oh14 + c5h10oh-1o2 <=> c5h10oh-4o + c5h10oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2747,
    label = "c5h10oh14 + c5h10oh-2o2 <=> c5h10oh-4o + c5h10oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2748,
    label = "c5h10oh14 + c5h10oh-3o2 <=> c5h10oh-4o + c5h10oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2749,
    label = "c5h10oh14 + c5h10oh-4o2 <=> c5h10oh-4o + c5h10oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2750,
    label = "c5h10oh14 + c5h10oh-5o2 <=> c5h10oh-4o + c5h10oh-5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2751,
    label = "c5h10oh15 + c5h10oh-1o2 <=> c5h10oh-5o + c5h10oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2752,
    label = "c5h10oh15 + c5h10oh-2o2 <=> c5h10oh-5o + c5h10oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2753,
    label = "c5h10oh15 + c5h10oh-3o2 <=> c5h10oh-5o + c5h10oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2754,
    label = "c5h10oh15 + c5h10oh-4o2 <=> c5h10oh-5o + c5h10oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2755,
    label = "c5h10oh15 + c5h10oh-5o2 <=> c5h10oh-5o + c5h10oh-5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2756,
    label = "c5h10oh11 + ho2 <=> c5h10oh-1o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2757,
    label = "c5h10oh12 + ho2 <=> c5h10oh-2o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2758,
    label = "c5h10oh13 + ho2 <=> c5h10oh-3o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2759,
    label = "c5h10oh14 + ho2 <=> c5h10oh-4o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2760,
    label = "c5h10oh15 + ho2 <=> c5h10oh-5o + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2761,
    label = "c5h10oh11 + ch3o2 <=> c5h10oh-1o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2762,
    label = "c5h10oh12 + ch3o2 <=> c5h10oh-2o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2763,
    label = "c5h10oh13 + ch3o2 <=> c5h10oh-3o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2764,
    label = "c5h10oh14 + ch3o2 <=> c5h10oh-4o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2765,
    label = "c5h10oh15 + ch3o2 <=> c5h10oh-5o + ch3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2766,
    label = "c5h10oh-1o2 <=> c5h9oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2767,
    label = "c5h10oh-1o2 <=> c5h9oh-1ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2768,
    label = "c5h10oh-1o2 <=> c5h9oh-1ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(18650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2769,
    label = "c5h10oh-2o2 => nc3h7cho + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2770,
    label = "c5h10oh-2o2 <=> c5h9oh-2ooh-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.688e+09, 's^-1'), n=0, Ea=(21950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2771,
    label = "c5h10oh-2o2 <=> c5h9oh-2ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2772,
    label = "c5h10oh-2o2 <=> c5h9oh-2ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2773,
    label = "c5h10oh-2o2 <=> c5h9oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(24450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2774,
    label = "c5h10oh-3o2 <=> c5h9oh-3ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(18450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2775,
    label = "c5h10oh-3o2 <=> c5h9oh-3ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2776,
    label = "c5h10oh-3o2 <=> c5h9oh-3ooh-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.75e+10, 's^-1'), n=0, Ea=(24000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2777,
    label = "c5h10oh-3o2 <=> c5h9oh-3ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(28450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2778,
    label = "c5h10oh-4o2 <=> c5h9oh-4ooh-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 's^-1'), n=0, Ea=(29000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2779,
    label = "c5h10oh-4o2 <=> c5h9oh-4ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2780,
    label = "c5h10oh-4o2 <=> c5h9oh-4ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(22450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2781,
    label = "c5h10oh-4o2 <=> c5h9oh-4ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(16650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2782,
    label = "c5h10oh-5o2 <=> c5h9oh-5ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2783,
    label = "c5h10oh-5o2 <=> c5h9oh-5ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(20450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2784,
    label = "c5h10oh-5o2 <=> c5h9oh-5ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(20650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2785,
    label = "c5h10oh-1o2 <=> c5h9oh1-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2786,
    label = "c5h10oh-2o2 <=> c5h9oh1-1 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2787,
    label = "c5h10oh-2o2 <=> c5h9oh1-2 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2788,
    label = "c5h10oh-3o2 <=> ho2 + c5h9oh1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2789,
    label = "c5h10oh-3o2 <=> c5h9oh1-3 + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2790,
    label = "c5h10oh-4o2 <=> ho2 + c5h9oh1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2791,
    label = "c5h10oh-4o2 <=> ho2 + c5h9oh1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2792,
    label = "c5h10oh-5o2 <=> ho2 + c5h9oh1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.308e+36, 's^-1'), n=-7.5, Ea=(39510, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2793,
    label = "c5h10oh-1o2 + ho2 <=> c5h10oh-1o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2794,
    label = "c5h10oh-2o2 + ho2 <=> c5h10oh-2o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2795,
    label = "c5h10oh-3o2 + ho2 <=> c5h10oh-3o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2796,
    label = "c5h10oh-4o2 + ho2 <=> c5h10oh-4o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2797,
    label = "c5h10oh-5o2 + ho2 <=> c5h10oh-5o2h + o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2798,
    label = "c5h10oh-1o2 + h2o2 <=> c5h10oh-1o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2799,
    label = "c5h10oh-2o2 + h2o2 <=> c5h10oh-2o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2800,
    label = "c5h10oh-3o2 + h2o2 <=> c5h10oh-3o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2801,
    label = "c5h10oh-4o2 + h2o2 <=> c5h10oh-4o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2802,
    label = "c5h10oh-5o2 + h2o2 <=> c5h10oh-5o2h + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2803,
    label = "c5h10oh-1o2 + ch3o2 => c5h10oh-1o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2804,
    label = "c5h10oh-2o2 + ch3o2 => c5h10oh-2o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2805,
    label = "c5h10oh-3o2 + ch3o2 => c5h10oh-3o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2806,
    label = "c5h10oh-4o2 + ch3o2 => c5h10oh-4o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2807,
    label = "c5h10oh-5o2 + ch3o2 => c5h10oh-5o + ch3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2808,
    label = "c5h10oh-1o2 + c5h10oh-1o2 => c5h10oh-1o + c5h10oh-1o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2809,
    label = "c5h10oh-1o2 + c5h10oh-2o2 => c5h10oh-1o + c5h10oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2810,
    label = "c5h10oh-1o2 + c5h10oh-3o2 => c5h10oh-1o + c5h10oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2811,
    label = "c5h10oh-1o2 + c5h10oh-4o2 => c5h10oh-1o + c5h10oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2812,
    label = "c5h10oh-1o2 + c5h10oh-5o2 => c5h10oh-1o + c5h10oh-5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2813,
    label = "c5h10oh-2o2 + c5h10oh-2o2 => c5h10oh-2o + c5h10oh-2o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2814,
    label = "c5h10oh-2o2 + c5h10oh-3o2 => c5h10oh-2o + c5h10oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2815,
    label = "c5h10oh-2o2 + c5h10oh-4o2 => c5h10oh-2o + c5h10oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2816,
    label = "c5h10oh-2o2 + c5h10oh-5o2 => c5h10oh-2o + c5h10oh-5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2817,
    label = "c5h10oh-3o2 + c5h10oh-3o2 => c5h10oh-3o + c5h10oh-3o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2818,
    label = "c5h10oh-3o2 + c5h10oh-4o2 => c5h10oh-3o + c5h10oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2819,
    label = "c5h10oh-3o2 + c5h10oh-5o2 => c5h10oh-3o + c5h10oh-5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2820,
    label = "c5h10oh-4o2 + c5h10oh-4o2 => c5h10oh-4o + c5h10oh-4o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2821,
    label = "c5h10oh-4o2 + c5h10oh-5o2 => c5h10oh-4o + c5h10oh-5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2822,
    label = "c5h10oh-5o2 + c5h10oh-5o2 => c5h10oh-5o + c5h10oh-5o + o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2823,
    label = "c5h10oh-1o2h => c5h10oh-1o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2824,
    label = "c5h10oh-2o2h => c5h10oh-2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2825,
    label = "c5h10oh-3o2h => c5h10oh-3o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2826,
    label = "c5h10oh-4o2h => c5h10oh-4o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2827,
    label = "c5h10oh-5o2h => c5h10oh-5o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2828,
    label = "hocho + pc4h9 <=> c5h10oh-1o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2829,
    label = "nc3h7cho + ch2oh <=> c5h10oh-2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2830,
    label = "c2h5cho + pc2h4oh <=> c5h10oh-3o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2831,
    label = "ch3cho + c3h6oh-3 <=> c5h10oh-4o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2832,
    label = "ch2o + c4h8oh-4 <=> c5h10oh-5o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2833,
    label = "c5h9oh-1ooh-2 => c5h9oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2834,
    label = "c5h9oh-1ooh-3 => c5h9oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2835,
    label = "c5h9oh-1ooh-4 => c5h9oho1-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2836,
    label = "c5h9oh-2ooh-1 => c5h9oho1-2 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2837,
    label = "c5h9oh-2ooh-3 => c5h9oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2838,
    label = "c5h9oh-2ooh-4 => c5h9oho2-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2839,
    label = "c5h9oh-2ooh-5 => c5h9oho2-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2840,
    label = "c5h9oh-3ooh-1 => c5h9oho1-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2841,
    label = "c5h9oh-3ooh-2 => c5h9oho2-3 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2842,
    label = "c5h9oh-3ooh-4 => c5h9oho3-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2843,
    label = "c5h9oh-3ooh-5 => c5h9oho3-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2844,
    label = "c5h9oh-4ooh-1 => c5h9oho1-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2845,
    label = "c5h9oh-4ooh-2 => c5h9oho2-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2846,
    label = "c5h9oh-4ooh-3 => c5h9oho3-4 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2847,
    label = "c5h9oh-4ooh-5 => c5h9oho4-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2848,
    label = "c5h9oh-5ooh-2 => c5h9oho2-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2849,
    label = "c5h9oh-5ooh-3 => c5h9oho3-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(7.5e+10, 's^-1'), n=0, Ea=(15300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2850,
    label = "c5h9oh-5ooh-4 => c5h9oho4-5 + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(6e+11, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2851,
    label = "c5h9oh1-1 + ho2 <=> c5h9oh-1ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2852,
    label = "c5h9oh1-1 + ho2 <=> c5h9oh-2ooh-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2853,
    label = "c5h9oh1-2 + ho2 <=> c5h9oh-2ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2854,
    label = "c5h9oh1-2 + ho2 <=> c5h9oh-3ooh-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2855,
    label = "c5h9oh1-3 + ho2 <=> c5h9oh-3ooh-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2856,
    label = "c5h9oh1-3 + ho2 <=> c5h9oh-4ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2857,
    label = "c5h9oh1-4 + ho2 <=> c5h9oh-4ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2858,
    label = "c5h9oh1-4 + ho2 <=> c5h9oh-5ooh-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(11900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2859,
    label = "c5h9oh-1ooh-3 => oh + hocho + c4h8-1",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2860,
    label = "c5h9oh-2ooh-4 => oh + hoch2cho + c3h6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2861,
    label = "c5h9oh-3ooh-1 => oh + c2h5cho + c2h3oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2862,
    label = "c5h9oh-3ooh-5 => oh + hoc2h4cho + c2h4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2863,
    label = "c5h9oh-4ooh-2 => oh + ch3cho + c3h5oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2864,
    label = "c5h9oh-5ooh-3 => oh + ch2o + c4h7oh1-4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 's^-1'), n=0, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2865,
    label = "c5h9oh-1ooh-2 + o2 <=> c5h9oh-1ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2866,
    label = "c5h9oh-1ooh-3 + o2 <=> c5h9oh-1ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2867,
    label = "c5h9oh-1ooh-4 + o2 <=> c5h9oh-1ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2868,
    label = "c5h9oh-2ooh-1 + o2 <=> c5h9oh-2ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2869,
    label = "c5h9oh-2ooh-3 + o2 <=> c5h9oh-2ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2870,
    label = "c5h9oh-2ooh-4 + o2 <=> c5h9oh-2ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2871,
    label = "c5h9oh-2ooh-5 + o2 <=> c5h9oh-2ooh-5o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2872,
    label = "c5h9oh-3ooh-1 + o2 <=> c5h9oh-3ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2873,
    label = "c5h9oh-3ooh-2 + o2 <=> c5h9oh-3ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2874,
    label = "c5h9oh-3ooh-4 + o2 <=> c5h9oh-3ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2875,
    label = "c5h9oh-3ooh-5 + o2 <=> c5h9oh-3ooh-5o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2876,
    label = "c5h9oh-4ooh-1 + o2 <=> c5h9oh-4ooh-1o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2877,
    label = "c5h9oh-4ooh-2 + o2 <=> c5h9oh-4ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2878,
    label = "c5h9oh-4ooh-3 + o2 <=> c5h9oh-4ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2879,
    label = "c5h9oh-4ooh-5 + o2 <=> c5h9oh-4ooh-5o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.52e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2880,
    label = "c5h9oh-5ooh-2 + o2 <=> c5h9oh-5ooh-2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2881,
    label = "c5h9oh-5ooh-3 + o2 <=> c5h9oh-5ooh-3o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2882,
    label = "c5h9oh-5ooh-4 + o2 <=> c5h9oh-5ooh-4o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.54e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2883,
    label = "c5h9oh-2ooh-1 + o2 <=> nc5ket12 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.85e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.512e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2884,
    label = "c5h9oh-3ooh-1 + o2 <=> nc5ket13 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.85e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.512e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2885,
    label = "c5h9oh-4ooh-1 + o2 <=> nc5ket14 + ho2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.637,
                Ea = (838, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.315e+18, 'cm^3/(mol*s)'),
                n = -1.638,
                Ea = (839, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.85e+18, 'cm^3/(mol*s)'),
                n = -1.771,
                Ea = (1120, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.512e+20, 'cm^3/(mol*s)'),
                n = -2.429,
                Ea = (3090, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 2886,
    label = "c5h9oh-1ooh-2o2 => nc3h7cho + ho2cho + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2887,
    label = "c5h9oh-3ooh-2o2 => nc4ket12 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2888,
    label = "c5h9oh-4ooh-2o2 => nc4ket13 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2889,
    label = "c5h9oh-5ooh-2o2 => nc4ket14 + ch2o + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21886, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2890,
    label = "c5h9oh-1ooh-2o2 <=> c5ohket1-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(21450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2891,
    label = "c5h9oh-1ooh-3o2 <=> c5ohket1-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(15450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2892,
    label = "c5h9oh-1ooh-4o2 <=> c5ohket1-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(13650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2893,
    label = "c5h9oh-2ooh-1o2 <=> c5ohket2-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2894,
    label = "c5h9oh-2ooh-3o2 <=> c5ohket2-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(25450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2895,
    label = "c5h9oh-2ooh-4o2 <=> c5ohket2-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2896,
    label = "c5h9oh-2ooh-5o2 <=> c5ohket2-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(19450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2897,
    label = "c5h9oh-3ooh-1o2 <=> c5ohket3-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2898,
    label = "c5h9oh-3ooh-2o2 <=> c5ohket3-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2899,
    label = "c5h9oh-3ooh-4o2 <=> c5ohket3-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2900,
    label = "c5h9oh-3ooh-5o2 <=> c5ohket3-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2901,
    label = "c5h9oh-4ooh-1o2 <=> c5ohket4-1 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(15650, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2902,
    label = "c5h9oh-4ooh-2o2 <=> c5ohket4-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.25e+10, 's^-1'), n=0, Ea=(17450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2903,
    label = "c5h9oh-4ooh-3o2 <=> c5ohket4-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2904,
    label = "c5h9oh-4ooh-3o2 <=> c5ohket4-5 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(23450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2905,
    label = "c5h9oh-5ooh-2o2 <=> c5ohket5-2 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+09, 's^-1'), n=0, Ea=(18950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2906,
    label = "c5h9oh-5ooh-3o2 <=> c5ohket5-3 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2907,
    label = "c5h9oh-5ooh-4o2 <=> c5ohket5-4 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 's^-1'), n=0, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2908,
    label = "c5ohket1-2 => oh + ocho + nc3h7cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2909,
    label = "c5ohket1-3 => oh + ch2ocho + c2h5cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2910,
#     label = "c5ohket1-4 => oh + c2h4 + ocho + ch3cho",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2911,
    label = "c5ohket2-1 => oh + hocho + nc3h7co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2912,
    label = "c5ohket2-3 => oh + hoch2co + c2h5cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

# entry(
#     index = 2913,
#     label = "c5ohket2-4 => oh + ch2co + ch2oh + ch3cho",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )
#
# entry(
#     index = 2914,
#     label = "c5ohket2-5 => oh + ch2co + pc2h4oh + ch2o",
#     degeneracy = 1,
#     reversible = False,
#     kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
# )

entry(
    index = 2915,
    label = "c5ohket3-1 => oh + hocho + c2h5coch2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2916,
    label = "c5ohket3-2 => oh + hoch2cho + c2h5co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2917,
    label = "c5ohket3-4 => oh + hoc2h4co + ch3cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2918,
    label = "c5ohket3-5 => oh + hoc3h6co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2919,
    label = "c5ohket4-1 => oh + hocho + ch2ch2coch3",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2920,
    label = "c5ohket4-2 => oh + hoch2cho + ch3coch2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2921,
    label = "c5ohket4-3 => oh + hoc2h4cho + ch3co",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2922,
    label = "c5ohket4-5 => oh + hoc3h6co + ch2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2923,
    label = "c5ohket5-2 => oh + hoch2cho + ch2ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2924,
    label = "c5ohket5-3 => oh + hoc2h4cho + ch2cho",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2925,
    label = "c5ohket5-4 => oh + hoc3h6cho + hco",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(39000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2926,
    label = "c5h9oho1-2 + oh => c4h71-1 + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2927,
    label = "c5h9oho1-3 + oh => c4h71-1 + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2928,
    label = "c5h9oho1-4 + oh => c4h71-2 + hocho + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2929,
    label = "c5h9oho2-3 + oh => ch3chchcho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2930,
    label = "c5h9oho2-4 + oh => ch3chchcho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2931,
    label = "c5h9oho2-5 + oh => ch3chchcho + ch2oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2932,
    label = "c5h9oho3-4 + oh => c2h3cho + pc2h4oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2933,
    label = "c5h9oho3-5 + oh => c2h3cho + pc2h4oh + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2934,
    label = "c5h9oho4-5 + oh => c4h6oh1-32 + ch2o + h2o",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2935,
    label = "c5h9oho1-2 + ho2 => c4h71-1 + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2936,
    label = "c5h9oho1-3 + ho2 => c4h71-1 + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2937,
    label = "c5h9oho1-4 + ho2 => c4h71-2 + hocho + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2938,
    label = "c5h9oho2-3 + ho2 => ch3chchcho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2939,
    label = "c5h9oho2-4 + ho2 => ch3chchcho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2940,
    label = "c5h9oho2-5 + ho2 => ch3chchcho + ch2oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2941,
    label = "c5h9oho3-4 + ho2 => c2h3cho + pc2h4oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2942,
    label = "c5h9oho3-5 + ho2 => c2h3cho + pc2h4oh + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2943,
    label = "c5h9oho4-5 + ho2 => c4h6oh1-32 + ch2o + h2o2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2944,
    label = "hoc3h6cho + o2 <=> hoc3h6co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0.5, Ea=(42200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2945,
    label = "hoc3h6cho + oh <=> hoc3h6co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2946,
    label = "hoc3h6cho + h <=> hoc3h6co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2947,
    label = "hoc3h6cho + o <=> hoc3h6co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(1790, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2948,
    label = "hoc3h6cho + ho2 <=> hoc3h6co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2949,
    label = "hoc3h6cho + ch3 <=> hoc3h6co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(8440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2950,
    label = "hoc3h6cho + ch3o <=> hoc3h6co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+11, 'cm^3/(mol*s)'), n=0, Ea=(1280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2951,
    label = "hoc3h6cho + ch3o2 <=> hoc3h6co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2952,
    label = "hoc3h6co <=> c3h6oh-3 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2953,
    label = "nc4h9cho + o2 <=> nc4h9co + ho2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37560, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2954,
    label = "nc4h9cho + oh <=> nc4h9co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=1.8, Ea=(-1300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2955,
    label = "nc4h9cho + h <=> nc4h9co + h2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.14e+09, 'cm^3/(mol*s)'),
        n = 1.12,
        Ea = (2320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2956,
    label = "nc4h9cho + o <=> nc4h9co + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.94e+12, 'cm^3/(mol*s)'), n=0, Ea=(1868, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2957,
    label = "nc4h9cho + ho2 <=> nc4h9co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40900, 'cm^3/(mol*s)'), n=2.5, Ea=(10200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2958,
    label = "nc4h9cho + ch3 <=> nc4h9co + ch4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00089, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (3210, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2959,
    label = "nc4h9cho + ch3o <=> nc4h9co + ch3oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2960,
    label = "nc4h9cho + ch3o2 <=> nc4h9co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40900, 'cm^3/(mol*s)'), n=2.5, Ea=(10200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2961,
    label = "nc4h9cho + oh <=> c4h8cho-1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.27e+09, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2962,
    label = "nc4h9cho + oh <=> c4h8cho-2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2963,
    label = "nc4h9cho + oh <=> c4h8cho-3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.67e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2964,
    label = "nc4h9cho + oh <=> c4h8cho-4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(552, 'cm^3/(mol*s)'), n=3.12, Ea=(-1176, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2965,
    label = "nc4h9cho + ho2 <=> c4h8cho-1 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(23790, 'cm^3/(mol*s)'), n=2.55, Ea=(16490, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2966,
    label = "nc4h9cho + ho2 <=> c4h8cho-2 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2967,
    label = "nc4h9cho + ho2 <=> c4h8cho-3 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9640, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2968,
    label = "nc4h9cho + ho2 <=> c4h8cho-4 + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.44e+12, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (17880, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2969,
    label = "nc4h9co <=> pc4h9 + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0, Ea=(9600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2970,
    label = "c4h8cho-1 <=> c2h4 + ch2ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.984e+18, 's^-1'), n=-1.6, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2971,
    label = "c4h8cho-2 <=> c3h6 + ch2cho",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.984e+14, 's^-1'), n=-0.76, Ea=(23320, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2972,
    label = "c4h8cho-3 <=> c4h8-1 + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.797e+14, 's^-1'), n=-0.72, Ea=(24350, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2973,
    label = "c4h8cho-3 <=> ac3h5cho + ch3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.643e+13, 's^-1'), n=-0.36, Ea=(30330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2974,
    label = "c4h8cho-4 <=> c2h3cho + c2h5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.863e+18, 's^-1'), n=-1.3, Ea=(30830, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2975,
    label = "ac3h5cho <=> c3h5-a + hco",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.813e+19, 's^-1'), n=-1.08, Ea=(68480, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2976,
    label = "ac3h5cho + oh <=> ac3h5co + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2977,
    label = "ac3h5cho + oh <=> c2h3chcho + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+06, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2978,
    label = "ac3h5cho + ho2 <=> ac3h5co + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2979,
    label = "ac3h5cho + ho2 <=> c2h3chcho + h2o2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9630, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2980,
    label = "ac3h5cho + ch3o2 <=> ac3h5co + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11920, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2981,
    label = "ac3h5cho + ch3o2 <=> c2h3chcho + ch3o2h",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.99e+12, 'cm^3/(mol*s)'), n=0, Ea=(17050, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2982,
    label = "ac3h5co <=> c3h5-a + co",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.199e+15, 's^-1'), n=-1.09, Ea=(-330, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2983,
    label = "c2h3chcho + ho2 => c2h3cho + hco + oh",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(8.91e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)
