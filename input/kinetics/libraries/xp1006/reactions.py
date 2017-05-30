#!/usr/bin/env python
# encoding: utf-8

name = "xp1006"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "NO2 + NO2 <=> NO + NO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.51e+12, 'cm^3/(mol*s)'), n=0, Ea=(27.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "O2 + nC5H12 <=> HO2 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(50.16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "N2O2 <=> NO + NO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.93, 0.3866, -0.0005276, -7.364e-05],
            [-0.2208, 0.0003922, 6.718e-05, 5.821e-06],
            [-0.02422, -0.0006123, -0.0001235, -1.603e-05],
            [-0.004268, -0.0001417, -3.17e-05, -4.747e-06],
            [-0.001095, -6.014e-05, -1.254e-05, -1.734e-06],
            [-0.0002648, -2.109e-05, -4.408e-06, -5.981e-07],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 4,
    label = "nC5H12 <=> C2H5 + NC3H7",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 20, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.18e+96, 's^-1'), n=-23.17, Ea=(126.046, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.855e+89, 's^-1'), n=-20.9, Ea=(125.63, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.55e+76, 's^-1'), n=-17.02, Ea=(120.458, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (3.475e+71, 's^-1'),
                n = -15.54,
                Ea = (117.854, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2.16e+64, 's^-1'), n=-13.43, Ea=(113.815, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.55e+58, 's^-1'), n=-11.79, Ea=(110.456, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.02e+53, 's^-1'), n=-10.15, Ea=(106.996, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9e+45, 's^-1'), n=-8.13, Ea=(102.538, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 5,
    label = "nC5H12 + C5H11_A <=> nC5H12 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(12.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "O2 + nC5H12 <=> HO2 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(50.16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C5H11_A <=> C5H11_C",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(0.00048, 's^-1'), n=3.725, Ea=(28.298, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.41e+22, 's^-1'), n=-3.517, Ea=(42.976, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.57e+32, 's^-1'), n=-6.005, Ea=(50.425, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.12e+24, 's^-1'), n=-3.514, Ea=(48.305, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.59e+14, 's^-1'), n=-0.404, Ea=(43.709, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 8,
    label = "nC5H12 + C5H11_B <=> nC5H12 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "nC5H12 + C5H11_B <=> nC5H12 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(10.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "O2 + nC5H12 <=> HO2 + C5H11_B",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(52.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "C5H11_B <=> C5H11_A",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.61e+10, 's^-1'), n=-0.128, Ea=(16.305, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.88e+17, 's^-1'), n=-2.073, Ea=(21.414, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.09e+18, 's^-1'), n=-2.284, Ea=(23.337, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.38e+14, 's^-1'), n=-0.838, Ea=(21.871, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.6e+08, 's^-1'), n=0.954, Ea=(19.221, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 12,
    label = "C5H11_B <=> C5H11_C",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.08e-15, 's^-1'), n=6.876, Ea=(11.901, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.68e+07, 's^-1'), n=0.667, Ea=(25.012, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.26e+19, 's^-1'), n=-2.35, Ea=(32.938, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.16e+16, 's^-1'), n=-1.256, Ea=(33.072, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.06e+06, 's^-1'), n=1.57, Ea=(29.12, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 13,
    label = "O2 + C5H11_A <=> S42",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.487e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-0.536, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 14,
    label = "O2 + C5H11_C <=> S34",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.487e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-0.536, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 15,
    label = "NO3 <=> NO + O2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.916, 0.3855, -0.0007756, -0.000111],
            [-0.2068, 3.731e-05, 1.073e-05, 2.316e-06],
            [-0.02813, -0.0004672, -9.829e-05, -1.358e-05],
            [-0.003853, -0.0001023, -2.137e-05, -2.91e-06],
            [-0.0005392, -2.885e-05, -5.957e-06, -7.914e-07],
            [-0.001284, -1.262e-06, -2.009e-07, -9.482e-09],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 16,
    label = "O2 + NC3H7 <=> S37",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.2e+08, 'cm^3/(mol*s)'),
                n = 0.405,
                Ea = (-4.399, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.45e+14, 'cm^3/(mol*s)'),
                n = -0.984,
                Ea = (-1.711, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.09e+13, 'cm^3/(mol*s)'),
                n = -0.499,
                Ea = (-0.938, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.15e+20, 'cm^3/(mol*s)'),
                n = -2.42,
                Ea = (2.451, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.07e+16, 'cm^3/(mol*s)'),
                n = -1.3,
                Ea = (0.803, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 17,
    label = "O2 + C2H5 <=> S18",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.398e+53, 'cm^3/(mol*s)'),
                n = -13.9,
                Ea = (9.279, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.362e+59, 'cm^3/(mol*s)'),
                n = -15.28,
                Ea = (14.24, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.262e+60, 'cm^3/(mol*s)'),
                n = -14.91,
                Ea = (16.24, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 18,
    label = "O2 + C5H11_B <=> S64",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.865e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (0.199, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "N3O <=> NO + N2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.485, 0.233, -0.01007, -0.0002243],
            [-0.7757, -0.1771, -0.002639, 0.0008148],
            [-0.304, -0.04535, 0.00535, 0.0003998],
            [-0.1258, 0.005961, 0.003384, -0.0001953],
            [-0.02097, 0.006587, 4.704e-05, -0.0002419],
            [0.01292, 0.0007302, -0.0008038, -7.364e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 20,
    label = "S42 <=> S44",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.033e+10, 's^-1'), n=0.2, Ea=(18.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "N2 + NO3 <=> O2 + N3O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-15.17, -9.992e-05, -2.166e-05, -3.178e-06],
            [15, 6.56e-05, 1.422e-05, 2.086e-06],
            [-0.2921, 2.66e-05, 5.767e-06, 8.469e-07],
            [0.02977, 4.854e-06, 1.051e-06, 1.541e-07],
            [0.0309, -6.009e-06, -1.302e-06, -1.911e-07],
            [0.005099, -9.305e-07, -2.017e-07, -2.961e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 22,
    label = "S34 <=> S24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.877e+07, 's^-1'), n=1.4, Ea=(20.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "O2 + S44 <=> S15",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.569e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-0.536, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "NO2 + OH <=> NO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+06, 'cm^3/(mol*s)'), n=2, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "S64 <=> S96",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+07, 's^-1'), n=1.3, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "S54 <=> S37",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.498, 0.02607, -0.004473, 0.0004221],
            [1.419, 0.03038, -0.004704, 0.000337],
            [0.04409, 0.01432, -0.001864, 6.288e-05],
            [-0.02407, 0.008139, -0.0009492, 1.131e-05],
            [0.003245, 0.004506, -0.00047, -4.378e-06],
            [-0.003457, 0.001752, -0.0001176, -1.446e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 27,
    label = "S15 <=> S39 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(175.4, 's^-1'), n=3.1, Ea=(17.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "O2 + N3O <=> N3O3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.95, 0.006653, -0.00135, 0.0001731],
            [-0.09842, 0.009561, -0.001918, 0.00024],
            [-0.01803, 0.004171, -0.0008149, 9.588e-05],
            [-0.003765, 0.000973, -0.0001781, 1.759e-05],
            [-0.0004649, -7.59e-05, 2.015e-05, -3.817e-06],
            [8.739e-05, -0.0001669, 3.199e-05, -3.571e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 29,
    label = "HO2 + OH <=> O2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "nC5H12 + OH <=> H2O + C5H11_B",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.732e+07, 'cm^3/(mol*s)'),
        n = 1.813,
        Ea = (0.868, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = "nC5H12 + OH <=> H2O + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.411e+10, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (0.505, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = "nC5H12 + OH <=> H2O + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.721e+06, 'cm^3/(mol*s)'),
        n = 1.811,
        Ea = (-1.016, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = "S42 <=> S12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.233e+06, 's^-1'), n=1.5, Ea=(20, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "S44 <=> S12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.43e+09, 's^-1'),
        n = 1.32,
        Ea = (40.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 35,
    label = "S64 <=> S79",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.718e+06, 's^-1'), n=1.2, Ea=(16.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "S96 <=> S79",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.76e+09, 's^-1'),
        n = 0.88,
        Ea = (38, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 37,
    label = "NO + S42 <=> S10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.293e+16, 'cm^3/(mol*s)'),
        n = -0.753,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'O_rad/NonDe;N3d-Od from training reaction 34\nExact match found for rate rule [N3d-Od;O_rad/NonDe]\nEa raised from -1.7 to 0 kJ/mol.',
    ),
    longDesc = 
u"""
O_rad/NonDe;N3d-Od from training reaction 34
Exact match found for rate rule [N3d-Od;O_rad/NonDe]
Ea raised from -1.7 to 0 kJ/mol.
""",
)

entry(
    index = 38,
    label = "NO3 + C5H11_A <=> S10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_rad/NonDe]
""",
)

entry(
    index = 39,
    label = "HO2 + C5H11_A <=> S32 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "S42 + C5H11_A <=> S32 + S32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "S42 + S42 <=> O2 + S32 + S32",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 42,
    label = "S32 + NO2 <=> S10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]
""",
)

entry(
    index = 43,
    label = "S79 <=> S63 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+07, 's^-1'), n=0.94, Ea=(9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "S12 <=> S63 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.48e+09, 's^-1'), n=0.35, Ea=(11.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "O2 + S96 <=> S82",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.569e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-0.536, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "O2 + C5H11_A <=> HO2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9.322, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "O2 + C5H11_C <=> HO2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14, 'cm^3/(mol*s)'), n=3.71, Ea=(9.322, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "S42 <=> HO2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.14e+09, 's^-1'), n=1.01, Ea=(29.362, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "S34 <=> HO2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.2e+10, 's^-1'), n=0.73, Ea=(29.883, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "C5H11_A + C5H11_A <=> nC5H12 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.052e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 51,
    label = "C5H11_A + C5H11_C <=> nC5H12 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.078e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 52,
    label = "C5H11_C + C5H11_C <=> nC5H12 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.104e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 53,
    label = "C5H11_B + C5H11_A <=> nC5H12 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 54,
    label = "C5H11_B + C5H11_C <=> nC5H12 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 55,
    label = "C5H11_A + OH <=> H2O + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 56,
    label = "C5H11_C + OH <=> H2O + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 57,
    label = "O2 + C2H5 <=> OH + C2H4O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.908e-06, 'cm^3/(mol*s)'),
                n = 4.76,
                Ea = (0.254, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.06803, 'cm^3/(mol*s)'),
                n = 3.57,
                Ea = (2.643, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (826.5, 'cm^3/(mol*s)'),
                n = 2.41,
                Ea = (5.285, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 58,
    label = "S18 <=> OH + C2H4O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.237e+35, 's^-1'), n=-9.42, Ea=(36.36, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.687e+36, 's^-1'), n=-9.22, Ea=(38.7, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.52e+41, 's^-1'), n=-10.2, Ea=(43.71, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 59,
    label = "NC3H7 + C2H4O <=> S32",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.397, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 60,
    label = "HO2 + C5H11_A <=> NC3H7 + OH + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O2)',
    ),
    longDesc = 
u"""
=(iC3H7+O2)
""",
)

entry(
    index = 61,
    label = "NO + NO2 <=> N2O3_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.46, -0.004683, -0.0008662, -9.081e-05],
            [-0.1818, 0.004789, 0.000868, 8.552e-05],
            [0.0658, -0.0008024, -0.0001206, -5.236e-06],
            [0.02721, 0.0003431, 5.401e-05, 3.102e-06],
            [0.01309, -0.0005828, -7.951e-05, -1.364e-06],
            [0.002378, 7.797e-05, -1.013e-06, -3.623e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 62,
    label = "S82 <=> S91",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.877e+07, 's^-1'), n=1.4, Ea=(20.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "O2 + S24 <=> S36",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.089e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (0.199, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 64,
    label = "S36 <=> S91",
    degeneracy = 1,
    kinetics = Arrhenius(A=(294100, 's^-1'), n=1.5, Ea=(19.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "S36 <=> S82",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10170, 's^-1'),
        n = 1.674,
        Ea = (15.37, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R7H_OOCs4;O_rad_out;XH_out] for rate rule [R7H_OOCs4;O_rad_out;O_H_out]',
    ),
    longDesc = 
u"""
Estimated using template [R7H_OOCs4;O_rad_out;XH_out] for rate rule [R7H_OOCs4;O_rad_out;O_H_out]
""",
)

entry(
    index = 66,
    label = "S82 <=> S17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.432e+09, 's^-1'), n=0.9, Ea=(29.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "S36 <=> S17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.718e+06, 's^-1'), n=1.2, Ea=(16.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "S17 <=> S91",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.43e+09, 's^-1'),
        n = 1.32,
        Ea = (40.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 69,
    label = "O2 + NC3H7 <=> HO2 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "C5H11_A <=> C2H5 + C3H6",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.54e+25, 's^-1'), n=-4.241, Ea=(31.303, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.34e+31, 's^-1'), n=-5.581, Ea=(35.992, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.63e+28, 's^-1'), n=-4.592, Ea=(36.186, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.77e+20, 's^-1'), n=-2.108, Ea=(32.927, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.56e+14, 's^-1'), n=-0.301, Ea=(30.124, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 71,
    label = "S44 <=> C3H6 + OH + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+09, 's^-1'), n=1.2, Ea=(22.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "NC3H7 + OH <=> H2O + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 73,
    label = "C5H11_A + NC3H7 <=> nC5H12 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 74,
    label = "C5H11_C + NC3H7 <=> nC5H12 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 75,
    label = "C5H11_B + NC3H7 <=> nC5H12 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 76,
    label = "HO2 + C3H6 <=> S37",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.336, 0.01061, -0.001455, 7.428e-05],
            [3.717, 0.02021, -0.002609, 0.0001164],
            [0.07645, 0.01596, -0.001773, 5.143e-05],
            [0.005574, 0.01017, -0.0009085, 2.919e-06],
            [-0.005516, 0.005236, -0.0003209, -1.906e-05],
            [-0.004069, 0.002097, -2.683e-05, -2.102e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 77,
    label = "N2O3_A <=> NO + NO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.974, 0.3816, -0.001364, -0.0001395],
            [1.847, 0.005093, 0.0009476, 9.816e-05],
            [-0.1519, -0.001041, -0.0001281, 2.493e-06],
            [-0.07615, 0.0002461, 6.042e-05, 9.335e-06],
            [-0.01409, -0.001028, -0.0001376, -1.458e-06],
            [0.002512, 0.0002143, 1.159e-05, -5.231e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 78,
    label = "N2O3_A <=> N2O3_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.288, 0.1004, -0.01108, 0.0006064],
            [0.6351, 0.04109, -0.002142, 0.0002367],
            [-0.1935, 0.004619, 0.001022, 7.681e-05],
            [-0.08383, 0.007205, 0.0003678, -2.125e-05],
            [-0.02556, 0.003659, 0.0001944, -1.043e-05],
            [-0.003797, 0.0001725, 9.318e-05, 4.908e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 79,
    label = "S17 <=> S4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.408e+10, 's^-1'), n=0.784, Ea=(9.591, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 80,
    label = "NO + S37 <=> NO3 + NC3H7",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.161, -1.897e-06, -4.114e-07, -6.042e-08],
            [12.11, -2.058e-06, -4.462e-07, -6.554e-08],
            [0.01221, -1.283e-06, -2.783e-07, -4.087e-08],
            [0.003036, -7.989e-07, -1.732e-07, -2.544e-08],
            [0.0007698, -4.257e-07, -9.23e-08, -1.356e-08],
            [3.957e-05, -1.986e-07, -4.307e-08, -6.325e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 81,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.094e+09, 'cm^3/(mol*s)'),
                n = 0.49,
                Ea = (-0.391, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.843e+07, 'cm^3/(mol*s)'),
                n = 1.13,
                Ea = (-0.721, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.561e+14, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (4.749, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 921,
    label = "O2 + C2H5 <=> C2H4 + HO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(6.609, 'cm^3/(mol*s)'), n=3.51, Ea=(14160, 'cal/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 82,
    label = "S18 <=> C2H4 + HO2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.04, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.782e+32, 's^-1'), n=-7.1, Ea=(32.84, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.701e+37, 's^-1'), n=-8.47, Ea=(35.84, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.98e+38, 's^-1'), n=-8.46, Ea=(37.9, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 83,
    label = "C5H11_B <=> C2H4 + NC3H7",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(4410, 's^-1'), n=2.192, Ea=(18.827, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.06e+20, 's^-1'), n=-2.628, Ea=(29.232, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.17e+28, 's^-1'), n=-4.578, Ea=(34.864, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.47e+24, 's^-1'), n=-3.383, Ea=(34.388, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.34e+17, 's^-1'), n=-1.123, Ea=(31.176, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 84,
    label = "C2H5 + C5H11_A <=> nC5H12 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 85,
    label = "C2H5 + C5H11_C <=> nC5H12 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 86,
    label = "C2H5 + C5H11_B <=> nC5H12 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 87,
    label = "C2H5 + OH <=> C2H4 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 88,
    label = "O2 + S79 <=> S69",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.569e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-0.536, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 89,
    label = "HO2 + NC3H7 <=> C3H7O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 90,
    label = "S37 + S37 <=> O2 + C3H7O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 91,
    label = "NC3H7 + S37 <=> C3H7O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "NO + S37 <=> NO2 + C3H7O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [14.3, -9.413e-05, -2.04e-05, -2.992e-06],
            [-0.2316, -3.172e-05, -6.861e-06, -1.003e-06],
            [-0.05262, -1.957e-05, -4.232e-06, -6.184e-07],
            [-0.01754, -1.553e-05, -3.36e-06, -4.913e-07],
            [-0.006097, -6.474e-06, -1.399e-06, -2.042e-07],
            [-0.001948, -1.607e-06, -3.463e-07, -5.024e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 93,
    label = "S44 <=> S60 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.413e+09, 's^-1'), n=0.717, Ea=(15.402, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 94,
    label = "S60 <=> C3H6 + C2H4O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.442, 0.0309, -0.002179, 4.865e-05],
            [11.56, 0.05298, -0.003369, 3.622e-05],
            [-0.1713, 0.03416, -0.00154, -4.304e-05],
            [-0.08043, 0.01674, -0.0002422, -5.751e-05],
            [-0.0331, 0.005992, 0.0002141, -2.856e-05],
            [-0.01268, 0.001251, 0.000198, -2.048e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 95,
    label = "S69 <=> S72",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.033e+10, 's^-1'), n=0.2, Ea=(18.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "C2H4 + CH3 <=> NC3H7",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (8.67e+48, 'cm^3/(mol*s)'),
                        n = -12.54,
                        Ea = (18.206, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.06e+49, 'cm^3/(mol*s)'),
                        n = -12.04,
                        Ea = (20.001, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.67e+47, 'cm^3/(mol*s)'),
                        n = -11.17,
                        Ea = (22.366, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.81e+45, 'cm^3/(mol*s)'),
                        n = -10.03,
                        Ea = (23.769, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.04e+40, 'cm^3/(mol*s)'),
                        n = -8.25,
                        Ea = (24.214, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.12e+43, 'cm^3/(mol*s)'),
                        n = -11.3,
                        Ea = (13.08, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.28e+39, 'cm^3/(mol*s)'),
                        n = -9.88,
                        Ea = (13.164, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.6e+33, 'cm^3/(mol*s)'),
                        n = -7.46,
                        Ea = (12.416, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.85e+27, 'cm^3/(mol*s)'),
                        n = -5.38,
                        Ea = (11.455, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.66e+21, 'cm^3/(mol*s)'),
                        n = -3.17,
                        Ea = (10.241, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 97,
    label = "C3H6 + OH <=> CH3 + C2H4O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.013, 0.025, 0.1, 0.132, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (693000, 'cm^3/(mol*s)'),
                n = 1.49,
                Ea = (-0.536, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(5940, 'cm^3/(mol*s)'), n=2.01, Ea=(-0.56, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=2.22, Ea=(-0.68, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(107, 'cm^3/(mol*s)'), n=2.5, Ea=(-0.759, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (0.783, 'cm^3/(mol*s)'),
                n = 3.1,
                Ea = (-0.919, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.307, 'cm^3/(mol*s)'),
                n = 3.22,
                Ea = (-0.946, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.000316, 'cm^3/(mol*s)'),
                n = 4.05,
                Ea = (-1.144, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.59e-06, 'cm^3/(mol*s)'),
                n = 4.49,
                Ea = (-0.68, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.45e-05, 'cm^3/(mol*s)'),
                n = 4.22,
                Ea = (1.141, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 98,
    label = "O2 + CH3 <=> CH2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.641, 'cm^3/(mol*s)'),
        n = 3.283,
        Ea = (8.105, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "C2H4 + OH <=> CH2O + CH3",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.35, 'cm^3/(mol*s)'),
                n = 2.92,
                Ea = (-1.733, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (31.9, 'cm^3/(mol*s)'),
                n = 2.71,
                Ea = (-1.172, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(555, 'cm^3/(mol*s)'), n=2.36, Ea=(-0.181, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (178000, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (2.06, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.37e+09, 'cm^3/(mol*s)'),
                n = 0.56,
                Ea = (6.007, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.76e+13, 'cm^3/(mol*s)'),
                n = -0.5,
                Ea = (11.455, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 100,
    label = "S54 <=> CH2O + C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.89e+09, 's^-1'), n=1.3, Ea=(26.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 101,
    label = "C2H5 + HO2 <=> CH2O + CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 102,
    label = "HO2 + NC3H7 <=> CH2O + C2H5 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA',
    ),
    longDesc = 
u"""
88TSA
""",
)

entry(
    index = 103,
    label = "C3H7O <=> CH2O + C2H5",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.347, 0.2809, -0.0098, -0.0001348],
            [2.744, 0.05172, 0.005117, -5.623e-05],
            [-0.2334, 0.01072, 0.0006691, -3.912e-06],
            [-0.01929, -0.0005555, -4.373e-05, 4.02e-06],
            [0.009879, -0.0005136, -7.396e-05, -3.776e-06],
            [0.005081, 9.992e-05, -2.741e-05, -2.029e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 104,
    label = "S72 <=> S51 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+09, 's^-1'), n=0.93, Ea=(10.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 105,
    label = "S61 <=> S39",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (104, 's^-1'),
        n = 3.21,
        Ea = (18.64, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R_ROR;R1_doublebond;R2_doublebond_CH3;R_O_H] for rate rule [R_ROR;R1_doublebond_CHR;R2_doublebond_CH3;R_O_H]',
    ),
    longDesc = 
u"""
Estimated using template [R_ROR;R1_doublebond;R2_doublebond_CH3;R_O_H] for rate rule [R_ROR;R1_doublebond_CHR;R2_doublebond_CH3;R_O_H]
""",
)

entry(
    index = 106,
    label = "NO + S18 <=> NO3 + C2H5",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.408, -1.873e-06, -4.061e-07, -5.964e-08],
            [12.52, -2.372e-06, -5.144e-07, -7.555e-08],
            [0.1027, -1.486e-06, -3.223e-07, -4.733e-08],
            [0.01361, -9.084e-07, -1.97e-07, -2.893e-08],
            [0.001583, -4.962e-07, -1.076e-07, -1.58e-08],
            [3.541e-05, -2.415e-07, -5.236e-08, -7.69e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 107,
    label = "O2 + CH3 <=> CH3O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.812e+09, 'cm^3/(mol*s)'), n=0.9, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.85e+24, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1000, 'K'),
        T1 = (70, 'K'),
        T2 = (1700, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 108,
    label = "S39 <=> S66 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(42.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 109,
    label = "S36 <=> S92 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(57.86, 's^-1'), n=2.9, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "C2H5 + HO2 <=> OH + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 111,
    label = "O2 + C2H5O <=> HO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.097, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 112,
    label = "S18 + S37 <=> O2 + C3H7O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 113,
    label = "C2H5 + S37 <=> C3H7O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 114,
    label = "C5H11_A + C2H5O <=> nC5H12 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 115,
    label = "C5H11_C + C2H5O <=> nC5H12 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 116,
    label = "C5H11_B + C2H5O <=> nC5H12 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 117,
    label = "OH + C2H5O <=> H2O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 118,
    label = "NO + S18 <=> NO2 + C2H5O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [14.32, -8.46e-05, -1.833e-05, -2.689e-06],
            [-0.2136, -3.833e-05, -8.293e-06, -1.213e-06],
            [-0.04241, -1.954e-05, -4.226e-06, -6.171e-07],
            [-0.0133, -1.388e-05, -3.001e-06, -4.384e-07],
            [-0.00487, -5.985e-06, -1.293e-06, -1.885e-07],
            [-0.001787, -1.554e-06, -3.346e-07, -4.842e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 119,
    label = "CH2O + CH3 <=> C2H5O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.024, 0.1564, -0.009104, 9.572e-05],
            [1.098, 0.1408, -0.0006974, -0.0005047],
            [-0.1889, 0.02372, 0.002691, -3.638e-05],
            [-0.03919, -0.002586, 0.0005794, 8.917e-05],
            [0.0001743, -0.00241, -0.0001449, 1.632e-05],
            [0.004063, -0.0004926, -9.55e-05, -7.744e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 120,
    label = "S63 + OH <=> C2H4 + H2O + C3H5O_E",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "S66 <=> C3H5O_E + C2H4O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.654, 0.1808, -0.008138, -6.566e-05],
            [2.344, 0.1425, 1.937e-05, -0.0003683],
            [-0.1533, 0.01717, 0.001847, 1.205e-05],
            [-0.04167, 0.001135, 0.0003913, 2.629e-05],
            [-0.02421, 0.001399, 0.0002208, 3.954e-06],
            [-0.01669, 0.0006826, 0.0001665, 8.06e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 122,
    label = "NO + CH3O2 <=> NO3 + CH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.466, -2.948e-06, -6.392e-07, -9.387e-08],
            [11.82, -2.369e-06, -5.137e-07, -7.544e-08],
            [0.0803, -1.082e-06, -2.346e-07, -3.445e-08],
            [0.008947, -6.211e-07, -1.347e-07, -1.978e-08],
            [-0.0002482, -3.36e-07, -7.285e-08, -1.07e-08],
            [-7.061e-05, -1.517e-07, -3.288e-08, -4.829e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 123,
    label = "O2 + CH3O <=> CH2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.38e-19, 'cm^3/(mol*s)'),
        n = 9.5,
        Ea = (-5.501, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 124,
    label = "HO2 + CH3 <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0.269,
        Ea = (-0.688, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 125,
    label = "CH3O2 + CH3 <=> CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.08e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.411, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 126,
    label = "CH3O2 + CH3O2 <=> O2 + CH3O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 127,
    label = "C2H5 + CH3O2 <=> CH3O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "CH3O2 + NC3H7 <=> CH3O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 129,
    label = "CH3O2 + S37 <=> O2 + CH3O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 130,
    label = "CH3 + S37 <=> CH3O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 131,
    label = "CH3O2 + C5H11_A <=> CH3O + S32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 132,
    label = "CH3O2 + S42 <=> O2 + CH3O + S32",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 133,
    label = "CH3O + OH <=> CH2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 134,
    label = "NO2 + CH3 <=> NO + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 135,
    label = "CH3O + C5H11_A <=> nC5H12 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 136,
    label = "CH3O + C5H11_C <=> nC5H12 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 137,
    label = "CH3O + C5H11_B <=> nC5H12 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 138,
    label = "NO + CH3O2 <=> CH3O + NO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [14.28, -9.799e-05, -2.124e-05, -3.115e-06],
            [-0.2745, -4.034e-05, -8.733e-06, -1.278e-06],
            [-0.075, -1.242e-05, -2.684e-06, -3.917e-07],
            [-0.02669, -8.849e-06, -1.913e-06, -2.794e-07],
            [-0.009193, -4.976e-06, -1.076e-06, -1.57e-07],
            [-0.002833, -1.567e-06, -3.381e-07, -4.915e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 139,
    label = "NO + S34 <=> S73",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.293e+16, 'cm^3/(mol*s)'),
        n = -0.753,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'O_rad/NonDe;N3d-Od from training reaction 34\nExact match found for rate rule [N3d-Od;O_rad/NonDe]\nEa raised from -1.7 to 0 kJ/mol.',
    ),
    longDesc = 
u"""
O_rad/NonDe;N3d-Od from training reaction 34
Exact match found for rate rule [N3d-Od;O_rad/NonDe]
Ea raised from -1.7 to 0 kJ/mol.
""",
)

entry(
    index = 140,
    label = "NO3 + C5H11_C <=> S73",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_rad/NonDe]
""",
)

entry(
    index = 141,
    label = "HO2 + C5H11_C <=> S77 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 142,
    label = "CH3O2 + C5H11_C <=> CH3O + S77",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 143,
    label = "S34 + C5H11_A <=> S32 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "S42 + C5H11_C <=> S32 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "S34 + C5H11_C <=> S77 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "S42 + S34 <=> O2 + S32 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 147,
    label = "CH3O2 + S34 <=> O2 + CH3O + S77",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 148,
    label = "S34 + S34 <=> O2 + S77 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 149,
    label = "S77 + NO2 <=> S73",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]
""",
)

entry(
    index = 150,
    label = "O2 + C3H5O_E <=> S7",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.98, 0.04703, -0.003828, 7.714e-05],
            [-0.1714, 0.07569, -0.005416, 1.302e-05],
            [-0.1044, 0.04035, -0.001764, -0.0001267],
            [-0.04547, 0.01308, 0.0002277, -0.0001011],
            [-0.01222, 0.0008728, 0.0004956, -1.91e-05],
            [-8.745e-05, -0.001573, 0.0001738, 1.953e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 151,
    label = "C2H5 + C3H6O_A <=> S77",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.67e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.193, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 152,
    label = "S24 <=> C2H4 + C3H6O_A + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.096e+18, 's^-1'), n=-1.73, Ea=(26.82, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 153,
    label = "O2 + C3H7O <=> HO2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/Nd_Rrad] for rate rule [O2b;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H2/Nd_Rrad] for rate rule [O2b;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 154,
    label = "C5H11_A + C3H7O <=> nC5H12 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 155,
    label = "C5H11_C + C3H7O <=> nC5H12 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 156,
    label = "C5H11_B + C3H7O <=> nC5H12 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 157,
    label = "C3H7O + OH <=> H2O + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 158,
    label = "O2 + C3H5O_E <=> S16",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.535, -0.271, -0.0069, 2.98e-05],
            [1.894, 0.1621, -0.005938, -0.0003587],
            [0.1198, 0.05253, 0.001811, -0.000349],
            [-0.02754, -0.0008374, 0.002199, -1.276e-06],
            [-0.02195, -0.008482, 0.0004101, 0.0001001],
            [0.01106, -0.003092, -0.0003329, 3.404e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 159,
    label = "S16 <=> S7",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.285, 0.2375, -0.01655, -0.0003186],
            [5.334, 0.07404, 0.003625, -0.000635],
            [0.1098, -0.007964, 0.0009013, 0.0001939],
            [0.02651, -0.0006142, -0.0003021, 4.789e-06],
            [-0.001944, 0.002154, 9.083e-05, -2.807e-05],
            [-0.003562, 0.0007444, 0.0001009, 6.278e-07],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 160,
    label = "S89 <=> S92",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (87.5, 's^-1'),
        n = 3.23,
        Ea = (18.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R_ROR;R1_doublebond;R2_doublebond_CH2CH3;R_O_H] for rate rule [R_ROR;R1_doublebond_CHR;R2_doublebond_CH2CH3;R_O_H]',
    ),
    longDesc = 
u"""
Estimated using template [R_ROR;R1_doublebond;R2_doublebond_CH2CH3;R_O_H] for rate rule [R_ROR;R1_doublebond_CHR;R2_doublebond_CH2CH3;R_O_H]
""",
)

entry(
    index = 161,
    label = "C2H4 + C3H6 <=> C5H10_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-23.69, -0.0004425, -9.583e-05, -1.404e-05],
            [18.19, 0.0002029, 4.389e-05, 6.417e-06],
            [0.05037, -2.611e-06, -5.546e-07, -7.751e-08],
            [0.008862, 7.588e-07, 1.628e-07, 2.388e-08],
            [0.001721, 1.79e-07, 3.793e-08, 5.7e-09],
            [0.0006531, 5.084e-09, 4.562e-10, 1.694e-10],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 162,
    label = "NO3 + C5H11_B <=> S56",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.589e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cs_rad;O_rad/NonDe] + [C_rad/H2/Cs;O_rad] for rate rule [C_rad/H2/Cs;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cs_rad;O_rad/NonDe] + [C_rad/H2/Cs;O_rad] for rate rule [C_rad/H2/Cs;O_rad/NonDe]
""",
)

entry(
    index = 163,
    label = "NO + S64 <=> S56",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.293e+16, 'cm^3/(mol*s)'),
        n = -0.753,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'O_rad/NonDe;N3d-Od from training reaction 34\nExact match found for rate rule [N3d-Od;O_rad/NonDe]\nEa raised from -1.7 to 0 kJ/mol.',
    ),
    longDesc = 
u"""
O_rad/NonDe;N3d-Od from training reaction 34
Exact match found for rate rule [N3d-Od;O_rad/NonDe]
Ea raised from -1.7 to 0 kJ/mol.
""",
)

entry(
    index = 164,
    label = "HO2 + C5H11_B <=> S20 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 165,
    label = "CH3O2 + C5H11_B <=> CH3O + S20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 166,
    label = "S64 + C5H11_B <=> S20 + S20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 167,
    label = "S42 + C5H11_B <=> S20 + S32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 168,
    label = "S34 + C5H11_B <=> S20 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 169,
    label = "S64 + C5H11_A <=> S20 + S32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 170,
    label = "S64 + C5H11_C <=> S20 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 171,
    label = "S64 + S42 <=> O2 + S20 + S32",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 172,
    label = "S64 + S34 <=> O2 + S20 + S77",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 173,
    label = "CH3O2 + S64 <=> O2 + CH3O + S20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 174,
    label = "S64 + S64 <=> O2 + S20 + S20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 175,
    label = "S20 + NO2 <=> S56",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]
""",
)

entry(
    index = 176,
    label = "PC4H9 <=> C2H5 + C2H4",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.54e+41, 's^-1'), n=-9.46, Ea=(34.528, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.34e+43, 's^-1'), n=-9.52, Ea=(37.667, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.12e+39, 's^-1'), n=-8.15, Ea=(38.474, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.32e+30, 's^-1'), n=-5.12, Ea=(35.92, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 177,
    label = "nC5H12 <=> CH3 + PC4H9",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 20, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.09e+92, 's^-1'), n=-22.46, Ea=(126.235, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.83e+86, 's^-1'), n=-20.36, Ea=(126.331, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.24e+74, 's^-1'), n=-16.63, Ea=(121.64, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.03e+69, 's^-1'), n=-15.18, Ea=(119.142, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3e+62, 's^-1'), n=-13.09, Ea=(115.199, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.47e+56, 's^-1'), n=-11.44, Ea=(111.875, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.36e+51, 's^-1'), n=-9.8, Ea=(108.418, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.74e+43, 's^-1'), n=-7.75, Ea=(103.923, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 178,
    label = "CH2O + PC4H9 <=> S20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+10, 'cm^3/(mol*s)'), n=0, Ea=(3.457, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 179,
    label = "HO2 + PC4H9 <=> CH2O + NC3H7 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'BB75',
    ),
    longDesc = 
u"""
BB75
""",
)

entry(
    index = 180,
    label = "HO2 + C5H11_B <=> CH2O + PC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O2)',
    ),
    longDesc = 
u"""
=(nC3H7+O2)
""",
)

entry(
    index = 181,
    label = "S20 <=> S67",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 's^-1'),
        n = 0,
        Ea = (6.15, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R5H_CCC;O_rad_out;Cs_H_out_H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R5H_CCC;O_rad_out;Cs_H_out_H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 182,
    label = "O2 + S67 <=> S23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.637e+13, 'cm^3/(mol*s)'),
        n = -0.129,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H/NonDeC] + [O2_birad;C_sec_rad] for rate rule [O2_birad;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2\nEa raised from -0.0 to 0 kJ/mol.',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H/NonDeC] + [O2_birad;C_sec_rad] for rate rule [O2_birad;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
Ea raised from -0.0 to 0 kJ/mol.
""",
)

entry(
    index = 183,
    label = "S16 <=> S85",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.881, 0.07724, -0.007228, 0.0001791],
            [2.321, 0.09347, -0.006495, -0.0001433],
            [-0.001357, 0.02611, -0.0002894, -0.0001925],
            [-0.001356, 0.002591, 0.0004567, -2.802e-05],
            [-0.0002164, 0.0003683, 4.17e-05, 9.295e-06],
            [-0.001368, 0.000652, -1.898e-05, -3.723e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 184,
    label = "S85 <=> OH + S87",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.756, 0.3887, -7.383e-05, -1.073e-05],
            [0.2467, 0.0003278, 7.07e-05, 1.028e-05],
            [-0.1579, 3.656e-05, 7.787e-06, 1.103e-06],
            [-0.04231, -2.715e-05, -5.831e-06, -8.399e-07],
            [0.02127, -2.831e-05, -6.052e-06, -8.641e-07],
            [0.0178, -2.793e-06, -5.98e-07, -8.574e-08],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 185,
    label = "O2 + PC4H9 <=> S90",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.31, 0.0241, -0.003391, 0.0002408],
            [-0.4231, 0.03638, -0.004687, 0.0002537],
            [-0.09377, 0.01845, -0.001886, 1.879e-05],
            [-0.02446, 0.005741, -0.0002286, -6.247e-05],
            [-0.00528, 0.0004275, 0.0002124, -3.99e-05],
            [-0.0004626, -0.0005043, 0.0001219, -4.714e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 186,
    label = "S82 <=> S13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10980, 's^-1'), n=2.4, Ea=(19.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 187,
    label = "NO3 + PC4H9 <=> S47",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.589e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;C_rad/H2/Cs] + [O_rad/NonDe;Cs_rad] for rate rule [O_rad/NonDe;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;C_rad/H2/Cs] + [O_rad/NonDe;Cs_rad] for rate rule [O_rad/NonDe;C_rad/H2/Cs]
""",
)

entry(
    index = 188,
    label = "NO + S90 <=> S47",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.293e+16, 'cm^3/(mol*s)'),
        n = -0.753,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'O_rad/NonDe;N3d-Od from training reaction 34\nExact match found for rate rule [N3d-Od;O_rad/NonDe]\nEa raised from -1.7 to 0 kJ/mol.',
    ),
    longDesc = 
u"""
O_rad/NonDe;N3d-Od from training reaction 34
Exact match found for rate rule [N3d-Od;O_rad/NonDe]
Ea raised from -1.7 to 0 kJ/mol.
""",
)

entry(
    index = 189,
    label = "S75 <=> CH2O + C3H6 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+09, 's^-1'), n=1.3, Ea=(24.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 190,
    label = "O2 + PC4H9 <=> S75",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.49, -0.3478, -0.004867, 0.0002448],
            [0.4994, 0.06249, -0.00656, 0.0001942],
            [0.001346, 0.03009, -0.002201, -8.124e-05],
            [-0.06761, 0.007597, 0.0001259, -0.0001185],
            [-0.02657, -0.0008118, 0.0004766, -3.993e-05],
            [-0.0002867, -0.001422, 0.0001552, 1.256e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 191,
    label = "S75 <=> S90",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.21, 0.0153, -0.002729, 0.0002793],
            [1.559, 0.02196, -0.003705, 0.0003308],
            [0.01677, 0.01323, -0.002048, 0.0001424],
            [0.001899, 0.007696, -0.001095, 5.631e-05],
            [-0.0004688, 0.003653, -0.0004386, 5.443e-06],
            [-0.006926, 0.001107, -5.201e-05, -1.886e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 192,
    label = "PC4H9 + S37 <=> C4H9O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 193,
    label = "S90 + S90 <=> O2 + C4H9O + C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 194,
    label = "S90 + S37 <=> O2 + C4H9O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 195,
    label = "S18 + S90 <=> O2 + C4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 196,
    label = "CH3O2 + S90 <=> O2 + CH3O + C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1.86, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 197,
    label = "CH3 + S90 <=> CH3O + C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 198,
    label = "C2H5 + S90 <=> C4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 199,
    label = "S90 + NC3H7 <=> C4H9O + C3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 200,
    label = "PC4H9 + S90 <=> C4H9O + C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 201,
    label = "HO2 + PC4H9 <=> C4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 202,
    label = "CH3O2 + PC4H9 <=> CH3O + C4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 203,
    label = "C4H9O + NO2 <=> S47",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_rad/NonDe]
""",
)

entry(
    index = 204,
    label = "CH2O + NC3H7 <=> C4H9O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.682, 0.1372, -0.00751, 2.482e-05],
            [0.3974, 0.1535, -0.003298, -0.0004624],
            [-0.1608, 0.02939, 0.002185, -0.0001469],
            [-0.009341, -0.005853, 0.000695, 7.551e-05],
            [0.01176, -0.002638, -0.0002718, 1.721e-05],
            [0.001867, 0.0008947, -8.168e-05, -1.825e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 205,
    label = "H2O <=> H + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.064e+27, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120.79, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 0, '[H][H]': 3, '[O][O]': 1.5, 'N#N': 2, '[C-]#[O+]': 1.9},
    ),
)

entry(
    index = 206,
    label = "H2O + H2O <=> H2O + H + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.006e+26, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120.18, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 207,
    label = "O2 + H <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.651e+12, 'cm^3/(mol*s)'),
            n = 0.44,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.366e+20, 'cm^6/(mol^2*s)'),
            n = -1.72,
            Ea = (0.525, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=C=O': 3.8, 'O': 14, '[H][H]': 2, '[O][O]': 0.78, '[C-]#[O+]': 1.9, '[Ar]': 0.67},
    ),
)

entry(
    index = 208,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.079e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.295, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 209,
    label = "CH3O <=> CH2O + H",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.8e+13, 's^-1'), n=0, Ea=(26.17, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24.307, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (2500, 'K'),
        T1 = (1300, 'K'),
        T2 = (1e+99, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 210,
    label = "CH3 + OH <=> CH3O + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.186e+09, 'cm^3/(mol*s)'),
                n = 1.016,
                Ea = (11.94, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.188e+09, 'cm^3/(mol*s)'),
                n = 1.016,
                Ea = (11.94, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.23e+09, 'cm^3/(mol*s)'),
                n = 1.011,
                Ea = (11.95, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.798e+09, 'cm^3/(mol*s)'),
                n = 0.965,
                Ea = (12.06, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.242e+10, 'cm^3/(mol*s)'),
                n = 0.551,
                Ea = (13.07, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 211,
    label = "CH3O2 + H <=> CH3O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 212,
    label = "C2H4 + H <=> C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (9.569e+08, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1.355, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.419e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5.769, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (-9150, 'K'),
        T2 = (152, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, '[H][H]': 2, 'O=C=O': 2, 'O': 6, '[Ar]': 0.7},
    ),
)

entry(
    index = 213,
    label = "CH3 + CH3 <=> C2H5 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.74e+12, 'cm^3/(mol*s)'),
                n = 0.105,
                Ea = (10.664, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.57e+13, 'cm^3/(mol*s)'),
                n = -0.096,
                Ea = (11.406, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.1e+14, 'cm^3/(mol*s)'),
                n = -0.362,
                Ea = (13.373, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.15e+10, 'cm^3/(mol*s)'),
                n = 0.885,
                Ea = (13.533, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (103.2, 'cm^3/(mol*s)'),
                n = 3.23,
                Ea = (11.236, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 214,
    label = "C2H4 + OH <=> H + C2H4O",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.37e-07, 'cm^3/(mol*s)'),
                n = 5.3,
                Ea = (-2.051, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.73e-05, 'cm^3/(mol*s)'),
                n = 4.57,
                Ea = (-0.618, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.403, 'cm^3/(mol*s)'),
                n = 3.54,
                Ea = (1.882, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (0.0238, 'cm^3/(mol*s)'),
                n = 3.91,
                Ea = (1.723, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.25e+08, 'cm^3/(mol*s)'),
                n = 1.01,
                Ea = (10.507, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.8e+09, 'cm^3/(mol*s)'),
                n = 0.81,
                Ea = (13.867, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 215,
    label = "C3H6 + H <=> NC3H7",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.04, 1, 10], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.99e+81, 'cm^3/(mol*s)'),
                        n = -23.161,
                        Ea = (22.239, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.24e+68, 'cm^3/(mol*s)'),
                        n = -18.427,
                        Ea = (19.665, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.04e+49, 'cm^3/(mol*s)'),
                        n = -11.5,
                        Ea = (15.359, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.2e+41, 'cm^3/(mol*s)'),
                        n = -8.892,
                        Ea = (14.637, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([0.001, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.85e+26, 'cm^3/(mol*s)'),
                        n = -5.83,
                        Ea = (3.866, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.82e+30, 'cm^3/(mol*s)'),
                        n = -6.49,
                        Ea = (5.471, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3.78e+28, 'cm^3/(mol*s)'),
                        n = -5.57,
                        Ea = (5.625, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.46e+25, 'cm^3/(mol*s)'),
                        n = -4.28,
                        Ea = (5.248, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    MultiArrhenius(
                        arrhenius = [
                            Arrhenius(
                                A = (7.24e+26, 'cm^3/(mol*s)'),
                                n = -4.21,
                                Ea = (6.825, 'kcal/mol'),
                                T0 = (1, 'K'),
                            ),
                            Arrhenius(
                                A = (4.22e+27, 'cm^3/(mol*s)'),
                                n = -4.39,
                                Ea = (9.346, 'kcal/mol'),
                                T0 = (1, 'K'),
                            ),
                        ],
                    ),
                ],
            ),
        ],
    ),
)

entry(
    index = 216,
    label = "C3H6 + H <=> C2H4 + CH3",
    degeneracy = 1,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 0.04, 1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.54e+09, 'cm^3/(mol*s)'),
                        n = 1.35,
                        Ea = (2.542, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (7.88e+10, 'cm^3/(mol*s)'),
                        n = 0.87,
                        Ea = (3.6, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.67e+12, 'cm^3/(mol*s)'),
                        n = 0.47,
                        Ea = (5.431, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (9.25e+22, 'cm^3/(mol*s)'),
                        n = -2.6,
                        Ea = (12.898, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.32e+23, 'cm^3/(mol*s)'),
                        n = -2.42,
                        Ea = (16.5, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
            ),
            PDepArrhenius(
                pressures = ([10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (124000, 'cm^3/(mol*s)'),
                        n = 2.52,
                        Ea = (3.679, 'kcal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(2510, 'cm^3/(mol*s)'), n=2.91, Ea=(3.981, 'kcal/mol'), T0=(1, 'K')),
                ],
            ),
        ],
    ),
)

entry(
    index = 217,
    label = "nC5H12 <=> C5H11_B + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 20, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.99e+74, 's^-1'), n=-17.75, Ea=(124.798, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.72e+76, 's^-1'), n=-18.01, Ea=(131.106, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.42e+72, 's^-1'), n=-16.46, Ea=(132.942, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.56e+69, 's^-1'), n=-15.52, Ea=(132.148, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.64e+64, 's^-1'), n=-13.92, Ea=(130.026, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.8e+59, 's^-1'), n=-12.48, Ea=(127.648, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+54, 's^-1'), n=-10.89, Ea=(124.707, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.28e+46, 's^-1'), n=-8.67, Ea=(120.241, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 218,
    label = "nC5H12 <=> C5H11_A + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 20, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.93e+79, 's^-1'), n=-19.24, Ea=(125.716, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.69e+79, 's^-1'), n=-18.83, Ea=(130.425, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.34e+73, 's^-1'), n=-16.63, Ea=(130.412, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.64e+69, 's^-1'), n=-15.52, Ea=(129.087, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.77e+63, 's^-1'), n=-13.74, Ea=(126.353, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.3e+58, 's^-1'), n=-12.21, Ea=(123.622, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.06e+53, 's^-1'), n=-10.57, Ea=(120.451, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+45, 's^-1'), n=-8.36, Ea=(115.883, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 219,
    label = "nC5H12 <=> C5H11_C + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 2, 5, 10, 20, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.49e+79, 's^-1'), n=-19.24, Ea=(125.716, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.88e+79, 's^-1'), n=-18.84, Ea=(130.425, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.18e+73, 's^-1'), n=-16.63, Ea=(130.412, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.84e+69, 's^-1'), n=-15.52, Ea=(129.087, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.41e+63, 's^-1'), n=-13.74, Ea=(126.353, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.17e+58, 's^-1'), n=-12.21, Ea=(123.622, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.32e+52, 's^-1'), n=-10.57, Ea=(120.451, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.26e+45, 's^-1'), n=-8.36, Ea=(115.883, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 220,
    label = "C5H11_A <=> C5H10_A + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.797e+13, 's^-1'), n=-0.833, Ea=(30.423, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.922e+27, 's^-1'), n=-4.775, Ea=(39.987, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.504e+29, 's^-1'), n=-5.063, Ea=(43.151, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.026e+21, 's^-1'), n=-2.275, Ea=(39.953, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.141e+12, 's^-1'), n=0.287, Ea=(36.068, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 221,
    label = "C5H11_C <=> C5H10_A + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(5.119e+06, 's^-1'), n=1.511, Ea=(29.139, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.068e+22, 's^-1'), n=-2.949, Ea=(38.766, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.298e+25, 's^-1'), n=-3.569, Ea=(41.777, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.104e+16, 's^-1'), n=-0.983, Ea=(38.322, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.214e+10, 's^-1'), n=1.047, Ea=(35.009, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 222,
    label = "NC3H7 + H <=> C2H5 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12.505, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA\nnC3H7+H = C2H5+CH3                           3.40E+18  -1.33     5386.0    !88TSA RRKM 0.1 atm',
    ),
    longDesc = 
u"""
88TSA
nC3H7+H = C2H5+CH3                           3.40E+18  -1.33     5386.0    !88TSA RRKM 0.1 atm
""",
)

entry(
    index = 223,
    label = "PC4H9 + H <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12.505, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H) TS3 600 cm-1\npC4H9+H = C2H5+C2H5                          3.40E+18  -1.33       5386.0  ! =(nC3H7+H) TS3 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H) TS3 600 cm-1
pC4H9+H = C2H5+C2H5                          3.40E+18  -1.33       5386.0  ! =(nC3H7+H) TS3 0.1 atm
""",
)

entry(
    index = 224,
    label = "C5H11_A + H <=> C2H5 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+28, 'cm^3/(mol*s)'),
        n = -3.94,
        Ea = (15.916, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC5H11+H = nC3H7+C2H5                       5.90E+23   -2.81  10009.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC5H11+H = nC3H7+C2H5                       5.90E+23   -2.81  10009.0  ! =(iC3H7+H)
""",
)

entry(
    index = 225,
    label = "C5H11_B + H <=> C2H5 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+24, 'cm^3/(mol*s)'),
        n = -2.92,
        Ea = (12.505, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)\nPXC5H11+H = nC3H7+C2H5                       3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)
PXC5H11+H = nC3H7+C2H5                       3.40E+18   -1.33    5386.0 ! =(nC3H7+H) 0.1 atm
""",
)

entry(
    index = 226,
    label = "NO2 + H <=> NO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0, Ea=(0.357, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 227,
    label = "O2 + O2 + H <=> O2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.08e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 228,
    label = "O2 + H2O + H <=> H2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.126e+19, 'cm^6/(mol^2*s)'),
        n = -0.76,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 229,
    label = "N2 + O2 + H <=> N2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+19, 'cm^6/(mol^2*s)'),
        n = -1.24,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 230,
    label = "NO + HO2 <=> NO3 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-16.84, -0.0001257, -2.725e-05, -3.998e-06],
            [15.81, 0.0001098, 2.379e-05, 3.49e-06],
            [0.06333, -1.055e-05, -2.282e-06, -3.338e-07],
            [0.0133, 2.894e-07, 6.2e-08, 8.886e-09],
            [0.005516, -1.062e-06, -2.3e-07, -3.372e-08],
            [-0.0005764, 5.242e-07, 1.135e-07, 1.662e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 231,
    label = "C3H6O_A + H <=> C3H7O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.424, 0.07519, -0.004823, 8.533e-05],
            [1.305, 0.1041, -0.004541, -0.0001341],
            [-0.1563, 0.04063, -2.319e-05, -0.0001578],
            [-0.0518, 0.006879, 0.0007677, -2.233e-05],
            [-0.006938, -0.001919, 0.0002479, 2.701e-05],
            [0.003987, -0.001639, -5.589e-05, 1.202e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 232,
    label = "H + C2H4O <=> C2H5O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.62, 0.09135, -0.00511, 8.888e-05],
            [1.864, 0.1051, -0.002633, -0.0001745],
            [-0.1193, 0.03239, 0.0007399, -7.713e-05],
            [-0.04928, 0.005082, 0.0005132, 1.409e-05],
            [-0.01205, -0.0003496, 7.694e-05, 1.271e-05],
            [-0.000642, -0.000601, -1.847e-05, 1.473e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 233,
    label = "O2 + PC4H9 <=> S62",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.63, -0.3448, -0.0051, 0.0002435],
            [0.6018, 0.06681, -0.00681, 0.0001787],
            [0.03001, 0.03163, -0.002179, -0.0001007],
            [-0.06343, 0.00752, 0.000221, -0.0001257],
            [-0.02567, -0.001184, 0.0005177, -3.679e-05],
            [0.000148, -0.001578, 0.0001482, 1.641e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 234,
    label = "S62 <=> S90",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.354, 0.01437, -0.002666, 0.0002894],
            [1.364, 0.01971, -0.003478, 0.0003335],
            [0.02633, 0.01176, -0.001944, 0.0001545],
            [-0.001147, 0.006737, -0.001046, 6.751e-05],
            [-0.002726, 0.003061, -0.0004169, 1.3e-05],
            [-0.001051, 0.0008483, -5.929e-05, -1.301e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 235,
    label = "S62 <=> S75",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-4.808, 0.109, -0.01627, 0.0009901],
            [9.945, 0.009434, 7.303e-05, -0.0001799],
            [-0.01061, 0.02486, -0.00187, -0.0001883],
            [-0.02532, 0.01759, -0.001358, -0.0001183],
            [-0.007796, 0.004005, -5.444e-05, -5.303e-05],
            [0.001046, -0.001683, 0.0004543, -2.731e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 236,
    label = "S20 <=> S45",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (153000, 's^-1'),
        n = 2.26,
        Ea = (21.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;O_rad_out;Cs_H_out_H/(NonDeC/Cs)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;O_rad_out;Cs_H_out_H/(NonDeC/Cs)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 237,
    label = "S67 <=> S45",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003109, 's^-1'),
        n = 4.065,
        Ea = (11.055, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_1H] for rate rule [R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_1H] for rate rule [R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 238,
    label = "H + S11 <=> S20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.76e+06, 'cm^3/(mol*s)'),
        n = 1.99,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO-CsH_O;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO-CsH_O;HJ]
""",
)

entry(
    index = 239,
    label = "O2 + S20 <=> HO2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/Nd_Rrad] for rate rule [O2b;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H2/Nd_Rrad] for rate rule [O2b;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 240,
    label = "S20 + C5H11_A <=> nC5H12 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 241,
    label = "S20 + C5H11_C <=> nC5H12 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 242,
    label = "S20 + C5H11_B <=> nC5H12 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 243,
    label = "S20 + OH <=> H2O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 244,
    label = "H + S11 <=> S45",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (8.577, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Od_CO-CsH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Od_CO-CsH;HJ]
""",
)

entry(
    index = 245,
    label = "O2 + S45 <=> HO2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.288e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;O_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;O_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 246,
    label = "C5H11_A + S45 <=> nC5H12 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 247,
    label = "C5H11_C + S45 <=> nC5H12 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 248,
    label = "C5H11_B + S45 <=> nC5H12 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 249,
    label = "OH + S45 <=> H2O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;O_Csrad]
""",
)

entry(
    index = 250,
    label = "S20 <=> S57",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+09, 's^-1'),
        n = 0,
        Ea = (22.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R6H_SSSSS;O_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R6H_SSSSS;O_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 251,
    label = "S67 <=> S57",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.43e+09, 's^-1'),
        n = 1.32,
        Ea = (40.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 252,
    label = "S57 <=> S45",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (92.2, 's^-1'),
        n = 3.21,
        Ea = (6.53, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_SSSS;C_rad_out_2H;Cs_H_out_1H] for rate rule [R5H_CCC;C_rad_out_2H;Cs_H_out_H/NonDeO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R5H_SSSS;C_rad_out_2H;Cs_H_out_1H] for rate rule [R5H_CCC;C_rad_out_2H;Cs_H_out_H/NonDeO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 253,
    label = "S51 <=> OH + C3H5O_B + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 254,
    label = "C3H5O_B <=> C3H5O_D",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.17e+20, 's^-1'), n=-4.15, Ea=(12.121, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.79e+24, 's^-1'), n=-5.03, Ea=(14.606, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.9e+26, 's^-1'), n=-5.16, Ea=(16.124, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.51e+28, 's^-1'), n=-5.4, Ea=(18.165, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.42e+28, 's^-1'), n=-5.17, Ea=(19.691, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.57e+24, 's^-1'), n=-3.86, Ea=(19.395, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.35e+18, 's^-1'), n=-1.73, Ea=(17.387, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 255,
    label = "S80 <=> C3H5O_B",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.515, 0.08106, 0.012, 0.0007487],
            [6.232, -0.03837, -0.004746, 0.0001962],
            [0.02808, 0.009064, 3.405e-05, -0.0001176],
            [-0.02272, 0.004879, 0.0004593, 4.905e-05],
            [-0.01428, 0.0008981, 1.705e-05, 3.246e-05],
            [-0.005725, 0.0002641, -5.499e-05, 4.764e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 256,
    label = "S80 <=> C3H5O_D",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.72, 0.279, -0.01213, -0.0004098],
            [0.9645, 0.07071, 0.005127, -0.0002927],
            [-0.01514, -0.0007124, 0.0004985, 6.995e-05],
            [0.002756, -4.843e-05, -0.0001257, -3.428e-06],
            [-0.004862, 0.0007535, 5.929e-05, 9.597e-07],
            [-0.005433, 0.0003673, 7.241e-05, 6.311e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 257,
    label = "O2 + C3H5O_B <=> HO2 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 258,
    label = "C3H5O_B <=> C3H4O + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3e+15, 's^-1'), n=-2.31, Ea=(14.668, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+22, 's^-1'), n=-3.96, Ea=(18.283, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.95e+23, 's^-1'), n=-3.99, Ea=(19.143, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.15e+25, 's^-1'), n=-4.24, Ea=(20.311, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.76e+28, 's^-1'), n=-4.89, Ea=(22.765, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.41e+27, 's^-1'), n=-4.28, Ea=(23.771, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.57e+20, 's^-1'), n=-2.06, Ea=(22.04, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 259,
    label = "C3H5O_D <=> C3H4O + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.93e+24, 's^-1'), n=-5.05, Ea=(20.108, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.14e+28, 's^-1'), n=-5.8, Ea=(22.219, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.93e+32, 's^-1'), n=-6.64, Ea=(25.108, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.6e+34, 's^-1'), n=-7.11, Ea=(28.209, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.17e+34, 's^-1'), n=-6.64, Ea=(30.648, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.17e+28, 's^-1'), n=-4.71, Ea=(31.232, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.98e+18, 's^-1'), n=-1.62, Ea=(30.13, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 260,
    label = "C5H11_A + C3H5O_B <=> nC5H12 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 261,
    label = "C5H11_C + C3H5O_B <=> nC5H12 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 262,
    label = "C5H11_B + C3H5O_B <=> nC5H12 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 263,
    label = "OH + C3H5O_B <=> H2O + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 264,
    label = "CH2O + OH <=> CH3O2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-19.82, 0.02492, -0.002433, 0.0001006],
            [16.67, 0.04028, -0.00349, 8.591e-05],
            [0.01692, 0.02335, -0.001437, -3.252e-05],
            [-0.008023, 0.01014, -0.0002261, -5.295e-05],
            [-0.007635, 0.003265, 0.0001278, -2.56e-05],
            [-0.003709, 0.0006843, 0.0001118, -3.314e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 265,
    label = "O2 + C3H5O_D <=> S46",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.4, 0.1598, -0.01955, 0.0005034],
            [0.003828, -0.009366, 0.001626, 9.973e-05],
            [-0.007942, -0.0009388, 0.0007308, 1.53e-05],
            [-0.03295, 0.01341, -0.0002078, -0.000166],
            [-0.02167, 0.009287, -0.0003171, -9.634e-05],
            [-0.009081, 0.003752, -0.0001741, -2.552e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 266,
    label = "O2 + C3H5O_D <=> S35",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.12, -0.2261, -0.01957, 0.000467],
            [-0.1169, -0.005431, 0.001638, 5.991e-05],
            [-0.05904, 0.000879, 0.0007768, 6.554e-07],
            [0.01085, 0.01408, -0.0001421, -0.0001705],
            [0.01725, 0.009472, -0.0002615, -9.743e-05],
            [0.008708, 0.003772, -0.0001414, -2.546e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 267,
    label = "S35 <=> S46",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.71, 0.315, -0.01106, -0.0007898],
            [0.1707, 0.04338, 0.004865, 3.419e-05],
            [-0.1114, 0.01217, 0.00186, 0.000131],
            [-0.02083, -0.0008675, 0.0002047, 6.047e-05],
            [0.01418, -0.003549, -0.0003676, 6.019e-06],
            [0.003158, -0.0002646, -9.557e-05, -9.652e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 268,
    label = "CH2O + C2H4 <=> H + C3H5O_D",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-31.02, -0.0003066, -6.642e-05, -9.735e-06],
            [23.47, 0.0002131, 4.614e-05, 6.756e-06],
            [0.0676, 5.548e-06, 1.214e-06, 1.814e-07],
            [-0.001125, 9.347e-07, 2.028e-07, 2.981e-08],
            [-0.004611, -4.095e-07, -8.862e-08, -1.297e-08],
            [-0.001938, -2.712e-07, -5.879e-08, -8.626e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 269,
    label = "O2 + C3H5O_D <=> S25",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.37, -0.2255, -0.01956, 0.0004596],
            [-0.09741, -0.004469, 0.001654, 5.05e-05],
            [-0.051, 0.00139, 0.0007947, -3.439e-06],
            [0.01305, 0.0143, -0.0001241, -0.0001717],
            [0.01776, 0.009542, -0.0002475, -9.758e-05],
            [0.008772, 0.003786, -0.000133, -2.529e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 270,
    label = "S25 <=> S46",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.039, 0.322, -0.01113, -0.0009036],
            [0.764, 0.02506, 0.003923, 0.0002242],
            [0.01177, 0.002996, 0.000445, 1.809e-05],
            [-0.01261, 0.0007154, 3.973e-05, -1.064e-05],
            [-0.01069, 0.003358, 0.000355, -7.682e-06],
            [-0.01645, -0.0001367, 2.538e-05, 1.668e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 271,
    label = "H2 + OH <=> H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3.43, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 272,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104.38, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C-]#[O+]': 1.9, '[H][H]': 2.5, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0},
    ),
)

entry(
    index = 273,
    label = "Ar + H2 <=> Ar + H + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.84e+18, 'cm^3/(mol*s)'),
        n = -1.1,
        Ea = (104.38, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 274,
    label = "HO2 + H <=> O2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.75e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (-1.451, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 275,
    label = "CH3O + H <=> CH2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 276,
    label = "CH3 + OH <=> CH2O + H2",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (350200, 'cm^3/(mol*s)'),
                n = 1.441,
                Ea = (-3.244, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (885400, 'cm^3/(mol*s)'),
                n = 1.327,
                Ea = (-2.975, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.65e+07, 'cm^3/(mol*s)'),
                n = 0.973,
                Ea = (-2.01, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.374e+09, 'cm^3/(mol*s)'),
                n = 0.287,
                Ea = (0.28, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.494e+18, 'cm^3/(mol*s)'),
                n = -2.199,
                Ea = (9.769, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 277,
    label = "C2H5 + H <=> C2H4 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 278,
    label = "nC5H12 + H <=> H2 + C5H11_B",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (349000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (6.45, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 279,
    label = "nC5H12 + H <=> H2 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4.471, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 280,
    label = "nC5H12 + H <=> H2 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4.471, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 281,
    label = "H2 + H + H <=> H2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+16, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 1.78\nHE/0.63/',
    ),
    longDesc = 
u"""
GRI3.0 * 1.78
HE/0.63/
""",
)

entry(
    index = 282,
    label = "H2O + H + H <=> H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.624e+19, 'cm^6/(mol^2*s)'),
        n = -1.25,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0',
    ),
    longDesc = 
u"""
GRI3.0
""",
)

entry(
    index = 283,
    label = "NC3H7 + H <=> H2 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '88TSA RRKM 1 atm\nnC3H7+H = C2H5+CH3                           3.10E+27  -3.59    19059.0    !88TSA RRKM 10 atm',
    ),
    longDesc = 
u"""
88TSA RRKM 1 atm
nC3H7+H = C2H5+CH3                           3.10E+27  -3.59    19059.0    !88TSA RRKM 10 atm
""",
)

entry(
    index = 284,
    label = "C5H11_A + H <=> H2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 285,
    label = "C5H11_C + H <=> H2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.24e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 286,
    label = "C3H7O + H <=> H2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 287,
    label = "H + C2H5O <=> H2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 288,
    label = "S20 + H <=> H2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 289,
    label = "H + S45 <=> H2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;O_Csrad]
""",
)

entry(
    index = 290,
    label = "H + C3H5O_B <=> H2 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;Cpri_Rrad] for rate rule [H_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;Cpri_Rrad] for rate rule [H_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 291,
    label = "CH2O + C2H4 <=> C3H6O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-28.94, -0.0004706, -0.0001019, -1.493e-05],
            [20.64, 0.0002194, 4.745e-05, 6.936e-06],
            [0.03218, -2.519e-06, -5.318e-07, -7.37e-08],
            [0.008573, 1.136e-06, 2.451e-07, 3.581e-08],
            [0.001963, 3.986e-07, 8.611e-08, 1.267e-08],
            [0.0005644, 9.194e-08, 1.976e-08, 2.93e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 292,
    label = "CH2O + C2H4 <=> H + C3H5O_B",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-31.94, -0.0004625, -0.0001002, -1.467e-05],
            [24.34, 0.0002223, 4.808e-05, 7.028e-06],
            [0.1616, -2.665e-07, -4.358e-08, -2.251e-09],
            [0.02983, 2.053e-06, 4.442e-07, 6.495e-08],
            [0.004721, 7.436e-07, 1.612e-07, 2.364e-08],
            [0.0005345, 2.088e-07, 4.526e-08, 6.647e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 293,
    label = "CH2O + C3H6 <=> CH3 + C3H5O_D",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-29.34, -0.0003899, -8.444e-05, -1.237e-05],
            [22.71, 0.0002414, 5.225e-05, 7.644e-06],
            [0.1001, 1.348e-05, 2.933e-06, 4.342e-07],
            [-0.002378, 4.656e-06, 1.009e-06, 1.482e-07],
            [-0.007114, 4.595e-07, 9.996e-08, 1.478e-08],
            [-0.003091, -2.742e-07, -5.932e-08, -8.676e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 294,
    label = "CH2O + C3H6 <=> CH3 + C3H5O_B",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-30.39, -0.0004857, -0.0001052, -1.54e-05],
            [23.35, 0.0002385, 5.158e-05, 7.538e-06],
            [0.1472, 3.492e-07, 9.177e-08, 1.817e-08],
            [0.02262, 2.468e-06, 5.341e-07, 7.811e-08],
            [0.002758, 8.908e-07, 1.931e-07, 2.832e-08],
            [7.168e-05, 2.393e-07, 5.189e-08, 7.622e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 295,
    label = "S13 <=> S94 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(42.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 296,
    label = "H + C2H4O <=> H2 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2720, 'cm^3/(mol*s)'), n=3.1, Ea=(5.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 297,
    label = "OH + C2H4O <=> H2O + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (172000, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (0.815, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 298,
    label = "S63 + OH <=> H2O + C3H6 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 299,
    label = "H + C2H3O <=> C2H4O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.2e+39, 'cm^6/(mol^2*s)'),
            n = -7.297,
            Ea = (4.7, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.55,
        T3 = (8900, 'K'),
        T1 = (4350, 'K'),
        T2 = (7240, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, '[H][H]': 2, 'C=C': 3, 'O=C=O': 2, 'O': 6},
        comment = 'RRKM 1 atm\nCH2CHO = CH3+CO                              1.200E+37   -7.456   46100.00 !RRKM 10 atm',
    ),
    longDesc = 
u"""
RRKM 1 atm
CH2CHO = CH3+CO                              1.200E+37   -7.456   46100.00 !RRKM 10 atm
""",
)

entry(
    index = 300,
    label = "HO2 + C2H3O <=> O2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/CO] for rate rule [Orad_O_H;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/CO] for rate rule [Orad_O_H;C_rad/H2/CO]
""",
)

entry(
    index = 301,
    label = "nC5H12 + C2H3O <=> C5H11_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06904, 'cm^3/(mol*s)'),
        n = 4.154,
        Ea = (13.132, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/NonDeC;C_pri_rad] for rate rule [C/H2/NonDeC;C_rad/H2/CO]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/NonDeC;C_pri_rad] for rate rule [C/H2/NonDeC;C_rad/H2/CO]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 302,
    label = "C5H11_C + C2H4O <=> nC5H12 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001133, 'cm^3/(mol*s)'),
        n = 4.29,
        Ea = (6.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/OneDe;C_rad/H/NonDeC] for rate rule [C/H3/CO;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/OneDe;C_rad/H/NonDeC] for rate rule [C/H3/CO;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 303,
    label = "C5H11_B + C2H4O <=> nC5H12 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0006331, 'cm^3/(mol*s)'),
        n = 4.436,
        Ea = (5.225, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/OneDe;C_rad/H2/Cs] for rate rule [C/H3/CO;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/OneDe;C_rad/H2/Cs] for rate rule [C/H3/CO;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 304,
    label = "C5H11_A + C2H3O <=> C5H10_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 305,
    label = "C5H11_C + C2H3O <=> C5H10_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.018e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 306,
    label = "C2H5O + C2H3O <=> C2H4O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Rrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Rrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 307,
    label = "NC3H7 + C2H3O <=> C3H6 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 308,
    label = "C2H5 + C2H3O <=> C2H4 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Csrad] for rate rule [C_rad/H2/CO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cmethyl_Csrad] for rate rule [C_rad/H2/CO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 309,
    label = "CH3O + C2H3O <=> CH2O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/CO;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/CO;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 310,
    label = "C3H7O + C2H3O <=> C3H6O_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Rrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Rrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 311,
    label = "CH3 + C2H3O <=> C3H6O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.36, 0.001485, -0.0002496, 2.393e-05],
            [-0.1164, 0.00275, -0.000458, 4.304e-05],
            [-0.0197, 0.002209, -0.0003577, 3.167e-05],
            [-0.005536, 0.001563, -0.0002414, 1.918e-05],
            [-0.002215, 0.0009874, -0.0001422, 9.37e-06],
            [-0.001063, 0.0005627, -7.313e-05, 3.367e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 312,
    label = "S20 + C2H3O <=> C2H4O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Rrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Rrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 313,
    label = "C2H3O + S45 <=> C2H4O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/CO;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/CO;O_Csrad]
""",
)

entry(
    index = 314,
    label = "NC3H7 + C2H3O <=> S11",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.18, 5.387e-05, -1.131e-05, 1.562e-06],
            [-0.0893, 0.0001037, -2.176e-05, 3.001e-06],
            [-0.01321, 9.244e-05, -1.937e-05, 2.661e-06],
            [-0.00266, 7.666e-05, -1.601e-05, 2.187e-06],
            [-0.0006393, 5.94e-05, -1.235e-05, 1.673e-06],
            [-0.0001869, 4.318e-05, -8.929e-06, 1.195e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 315,
    label = "C3H5O_B + C2H3O <=> C3H4O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cpri_Rrad] for rate rule [C_rad/H2/CO;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cpri_Rrad] for rate rule [C_rad/H2/CO;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 316,
    label = "S94 <=> C3H6O_A + C2H3O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.423, 0.2017, -0.006283, -8.447e-05],
            [2.09, 0.1544, 0.001451, -0.0002319],
            [-0.1841, 0.01134, 0.001548, 5.569e-05],
            [-0.009055, -0.003643, 3.431e-05, 1.597e-05],
            [-0.0005501, -0.0002956, 5.462e-05, -2.785e-06],
            [-0.002503, -0.0003182, 6.519e-05, 4.11e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 317,
    label = "S94 <=> C2H5 + S93",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.303, 0.2379, -0.008129, -8.121e-05],
            [2.37, 0.1328, 0.003707, -0.000267],
            [-0.1651, -0.0007793, 0.001549, 8.544e-05],
            [-0.004045, -0.003368, -0.0001516, 1.503e-05],
            [-0.003784, 0.0006826, 9.786e-06, -1.163e-06],
            [-0.004584, 1.047e-05, 4.713e-05, 4.27e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 318,
    label = "O2 + CH2O <=> HO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.07e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (53.42, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 319,
    label = "HCO + H <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.09e+12, 'cm^3/(mol*s)'),
            n = 0.48,
            Ea = (-0.26, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.57,
            Ea = (1.425, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7824,
        T3 = (271, 'K'),
        T1 = (2760, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, '[H][H]': 2, 'O=C=O': 2, 'O': 6, '[Ar]': 0.7},
    ),
)

entry(
    index = 320,
    label = "CH2O + OH <=> H2O + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.82e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 321,
    label = "CH2O + H <=> H2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.74, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 322,
    label = "C2H4O <=> HCO + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.45e+22, 's^-1'), n=-1.74, Ea=(86.355, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.03e+59, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95.913, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.00249,
        T3 = (718, 'K'),
        T1 = (6.09, 'K'),
        T2 = (3780, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 323,
    label = "C3H5O_B <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.62e+16, 's^-1'), n=-2.84, Ea=(13.197, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.26e+20, 's^-1'), n=-3.53, Ea=(15.469, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.13e+21, 's^-1'), n=-3.64, Ea=(16.585, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.07e+24, 's^-1'), n=-4.16, Ea=(18.985, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.42e+25, 's^-1'), n=-4.4, Ea=(22.383, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.86e+21, 's^-1'), n=-2.73, Ea=(23.659, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.75e+08, 's^-1'), n=1.14, Ea=(20.923, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 324,
    label = "C3H5O_D <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.23e+26, 's^-1'), n=-5.84, Ea=(19.357, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.32e+29, 's^-1'), n=-6.21, Ea=(21.294, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.47e+32, 's^-1'), n=-6.96, Ea=(24.197, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+36, 's^-1'), n=-7.76, Ea=(28.008, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.72e+37, 's^-1'), n=-8.02, Ea=(32.395, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.43e+31, 's^-1'), n=-5.81, Ea=(34.296, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.73e+14, 's^-1'), n=-0.726, Ea=(32.008, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 325,
    label = "H + C2H3O <=> HCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 326,
    label = "C3H4O + H <=> C2H4 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0.454,
        Ea = (5.82, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '85BAL/HIS\nReactions of C2H3CHO',
    ),
    longDesc = 
u"""
85BAL/HIS
Reactions of C2H3CHO
""",
)

entry(
    index = 327,
    label = "O2 + C2H3O <=> HCO + HCO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 328,
    label = "CH2O + C5H11_A <=> nC5H12 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.96, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 329,
    label = "CH2O + C5H11_C <=> nC5H12 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.96, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 330,
    label = "CH2O + C5H11_B <=> nC5H12 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5500, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 331,
    label = "HCO + C5H11_A <=> CH2O + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 332,
    label = "HCO + C5H11_C <=> CH2O + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.727e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 333,
    label = "HCO + C2H5O <=> CH2O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 334,
    label = "HCO + NC3H7 <=> CH2O + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 335,
    label = "C2H5 + HCO <=> CH2O + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.517e+13, 'cm^3/(mol*s)'),
        n = -0.096,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 336,
    label = "CH3O + HCO <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.717e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cmethyl_Orad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cmethyl_Orad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 337,
    label = "HCO + C3H7O <=> CH2O + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 338,
    label = "C2H5 + HCO <=> C3H6O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.25, 0.002404, -0.0003801, 3.3e-05],
            [-0.006536, 0.004431, -0.0006915, 5.834e-05],
            [-0.005282, 0.003515, -0.0005282, 4.085e-05],
            [-0.003784, 0.002442, -0.000344, 2.253e-05],
            [-0.002439, 0.001506, -0.0001923, 9.114e-06],
            [-0.001431, 0.0008314, -9.136e-05, 1.747e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 339,
    label = "S20 + HCO <=> CH2O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 340,
    label = "HCO + S45 <=> CH2O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri_rad;O_Csrad]
""",
)

entry(
    index = 341,
    label = "HCO + PC4H9 <=> S11",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.26, 4.298e-05, -9.082e-06, 1.269e-06],
            [-0.0001028, 8.288e-05, -1.751e-05, 2.443e-06],
            [-9.229e-05, 7.439e-05, -1.569e-05, 2.184e-06],
            [-7.74e-05, 6.232e-05, -1.312e-05, 1.817e-06],
            [-6.085e-05, 4.892e-05, -1.026e-05, 1.413e-06],
            [-4.5e-05, 3.611e-05, -7.542e-06, 1.029e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 342,
    label = "HCO + C3H5O_B <=> CH2O + C3H4O",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (3.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 343,
    label = "CH2O + C2H3O <=> HCO + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18.36, 'cm^3/(mol*s)'),
        n = 3.38,
        Ea = (9.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri;C_pri_rad] for rate rule [CO_pri;C_rad/H2/CO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri;C_pri_rad] for rate rule [CO_pri;C_rad/H2/CO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 344,
    label = "HCO + C2H3O <=> S93",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.25, 0.005757, -0.0007627, 4.964e-05],
            [-0.01734, 0.01045, -0.001352, 8.264e-05],
            [-0.0136, 0.007932, -0.0009547, 4.73e-05],
            [-0.00927, 0.005112, -0.00054, 1.537e-05],
            [-0.005575, 0.002827, -0.0002382, -2.334e-06],
            [-0.00299, 0.001342, -7.213e-05, -7.304e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 345,
    label = "HCO <=> CO + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5.7e+11, 'cm^3/(mol*s)'),
            n = 0.66,
            Ea = (14.87, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C-]#[O+]': 1.5, '[H][H]': 2, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 346,
    label = "O2 + HCO <=> HO2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.58e+12, 'cm^3/(mol*s)'), n=0, Ea=(0.41, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 347,
    label = "HCO + H <=> H2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.34e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 348,
    label = "HCO + OH <=> H2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.011e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 349,
    label = "HCO + HCO <=> H2 + CO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 350,
    label = "HCO + HCO <=> CH2O + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 351,
    label = "H2 + CO <=> CH2O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.3e+07, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (79.6, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.07e+27, 'cm^6/(mol^2*s)'),
            n = -3.42,
            Ea = (84.348, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'[C-]#[O+]': 1.5, '[H][H]': 2, 'O=C=O': 2, 'O': 6, '[Ar]': 0.7},
    ),
)

entry(
    index = 352,
    label = "C2H3O <=> CO + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.93e+12, 's^-1'), n=0.29, Ea=(40.3, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.52e+33, 'cm^3/(mol*s)'),
            n = -5.07,
            Ea = (41.3, 'kcal/mol'),
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
    index = 353,
    label = "O2 + C2H3O <=> CH2O + CO + OH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2.68e+17, 'cm^3/(mol*s)'),
                n = -1.84,
                Ea = (6.53, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.52e+20, 'cm^3/(mol*s)'),
                n = -2.58,
                Ea = (8.98, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.65e+19, 'cm^3/(mol*s)'),
                n = -2.22,
                Ea = (10.34, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.953e+13, 'cm^3/(mol*s)'),
                n = -0.6,
                Ea = (10.12, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 354,
    label = "H2O + HCO <=> H2O + CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.244e+18, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (17, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '02FRI/DAV * 2.00',
    ),
    longDesc = 
u"""
02FRI/DAV * 2.00
""",
)

entry(
    index = 355,
    label = "C2H4 + HCO <=> C2H5 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '88LIU/MUL1',
    ),
    longDesc = 
u"""
88LIU/MUL1
""",
)

entry(
    index = 356,
    label = "HCO + C5H11_A <=> nC5H12 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+HO2)',
    ),
    longDesc = 
u"""
=(iC3H7+HO2)
""",
)

entry(
    index = 357,
    label = "HCO + C5H11_B <=> nC5H12 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+HO2)',
    ),
    longDesc = 
u"""
=(nC3H7+HO2)
""",
)

entry(
    index = 358,
    label = "O2 + C2H4O <=> HO2 + CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39.15, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 359,
    label = "H + C2H4O <=> H2 + CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 360,
    label = "OH + C2H4O <=> H2O + CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.343e+10, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (-1.113, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 361,
    label = "HCO + C5H11_C <=> nC5H12 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/NonDeC;HCO from training reaction 9\nExact match found for rate rule [C_rad/H/NonDeC;HCO]',
    ),
    longDesc = 
u"""
C_rad/H/NonDeC;HCO from training reaction 9
Exact match found for rate rule [C_rad/H/NonDeC;HCO]
""",
)

entry(
    index = 362,
    label = "HCO + C2H3O <=> CO + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;HCO] for rate rule [C_rad/H2/CO;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;HCO] for rate rule [C_rad/H2/CO;HCO]
""",
)

entry(
    index = 363,
    label = "S18 + CO <=> S7",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-37.35, 3.545e-05, -7.286e-06, 9.722e-07],
            [27.74, 6.843e-05, -1.405e-05, 1.872e-06],
            [0.1232, 6.155e-05, -1.261e-05, 1.671e-06],
            [0.02408, 5.174e-05, -1.055e-05, 1.387e-06],
            [0.005268, 4.076e-05, -8.256e-06, 1.072e-06],
            [0.001212, 3.017e-05, -6.06e-06, 7.747e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 364,
    label = "CO + C2H4O <=> S93",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-28.43, 0.001393, -0.0002242, 2.026e-05],
            [22.65, 0.002615, -0.0004175, 3.708e-05],
            [0.0916, 0.002172, -0.0003381, 2.846e-05],
            [0.01613, 0.001608, -0.0002394, 1.823e-05],
            [0.002418, 0.001069, -0.0001487, 9.498e-06],
            [-8.894e-05, 0.0006417, -8.066e-05, 3.66e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 365,
    label = "C2H4 + CO <=> C3H4O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-22.97, 0.003114, -0.0004656, 3.718e-05],
            [19.38, 0.005724, -0.0008426, 6.495e-05],
            [0.08168, 0.004491, -0.0006311, 4.353e-05],
            [0.0124, 0.003053, -0.0003957, 2.169e-05],
            [0.0006921, 0.00182, -0.0002071, 6.618e-06],
            [-0.0008845, 0.0009567, -8.793e-05, -6.778e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 366,
    label = "S4 <=> CH2O + C4H7O_B + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 367,
    label = "C2H4 + C2H4O <=> C4H7O_B + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-34.25, -0.0002015, -4.367e-05, -6.404e-06],
            [24.79, 0.0001667, 3.611e-05, 5.292e-06],
            [0.09529, -4.431e-06, -9.525e-07, -1.374e-07],
            [0.01301, -1.412e-06, -3.063e-07, -4.503e-08],
            [0.001747, -5.989e-07, -1.299e-07, -1.907e-08],
            [0.0004934, -1.778e-07, -3.856e-08, -5.666e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 368,
    label = "C3H6 + C2H4O <=> C4H7O_B + CH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-33.5, -4.175e-05, -9.051e-06, -1.329e-06],
            [23.67, 4.066e-05, 8.814e-06, 1.294e-06],
            [0.04046, -3.295e-06, -7.139e-07, -1.047e-07],
            [0.003961, -6.628e-07, -1.438e-07, -2.113e-08],
            [0.001894, -1.544e-07, -3.348e-08, -4.919e-09],
            [0.001237, -2.081e-08, -4.514e-09, -6.632e-10],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 369,
    label = "C4H7O_B <=> CH3 + C3H4O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.98, 0.2034, -0.00757, 6.302e-05],
            [3.882, 0.1434, 0.002745, -0.0002681],
            [-0.315, 0.01207, 0.001966, 5.834e-05],
            [-0.04234, -0.005635, -1.096e-06, 2.486e-05],
            [0.009542, -0.001579, -0.000149, -5.849e-06],
            [0.005622, 0.0003159, -2.127e-05, -1.879e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 370,
    label = "HO2 + HO2 <=> O2 + H2O2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4.2e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11.982, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.3e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1.629, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 371,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48.749, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.49e+24, 'cm^3/(mol*s)'),
            n = -2.3,
            Ea = (48.749, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.5, '[H][H]': 3.7, '[O][O]': 1.2, 'N#N': 1.5, '[C-]#[O+]': 2.8},
    ),
)

entry(
    index = 372,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3.97, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 373,
    label = "H2O2 + H <=> H2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.95, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 374,
    label = "H2O2 + OH <=> H2O + HO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.74e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (0.318, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.27, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 375,
    label = "CH2O + HO2 <=> H2O2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18800, 'cm^3/(mol*s)'), n=2.7, Ea=(11.52, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 376,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 377,
    label = "nC5H12 + HO2 <=> H2O2 + C5H11_B",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17.16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 378,
    label = "nC5H12 + HO2 <=> H2O2 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126.4, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (13.72, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 379,
    label = "nC5H12 + HO2 <=> H2O2 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(63.2, 'cm^3/(mol*s)'), n=3.37, Ea=(13.72, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 380,
    label = "S63 + HO2 <=> C2H4 + H2O2 + C3H5O_E",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 381,
    label = "S63 + HO2 <=> H2O2 + C3H6 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 382,
    label = "C2H5 + HO2 <=> C2H4 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '86TSA/HAM',
    ),
    longDesc = 
u"""
86TSA/HAM
""",
)

entry(
    index = 383,
    label = "HO2 + C2H4O <=> H2O2 + CO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.923, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 384,
    label = "HO2 + C5H11_A <=> H2O2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 385,
    label = "HO2 + NC3H7 <=> H2O2 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 386,
    label = "HO2 + C5H11_C <=> H2O2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 387,
    label = "H2O2 + C2H3O <=> HO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e-05, 'cm^3/(mol*s)'),
        n = 5.025,
        Ea = (1.657, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O/H/NonDeO;C_rad/H2/CO] + [H2O2;C_pri_rad] for rate rule [H2O2;C_rad/H2/CO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [O/H/NonDeO;C_rad/H2/CO] + [H2O2;C_pri_rad] for rate rule [H2O2;C_rad/H2/CO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 388,
    label = "HO2 + C3H7O <=> H2O2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 389,
    label = "HO2 + C2H5O <=> H2O2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 390,
    label = "S20 + HO2 <=> H2O2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 391,
    label = "HO2 + S45 <=> H2O2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 392,
    label = "HO2 + C3H5O_B <=> H2O2 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.318e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 393,
    label = "HO2 + HCO <=> H2O2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.24e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (2.355, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;HCO] for rate rule [O_rad/NonDeO;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;HCO] for rate rule [O_rad/NonDeO;HCO]
""",
)

entry(
    index = 394,
    label = "HO2 + H <=> H2O2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.9, 0.1148, -0.008609, 0.0001445],
            [-0.2978, 0.06585, -0.001008, -0.0001857],
            [-0.08178, 0.0119, 0.0006147, -2.357e-05],
            [-0.02239, 0.001874, 0.0002081, 2.007e-06],
            [-0.007174, 0.0008939, -2.303e-05, 4.597e-06],
            [-0.001244, -0.0001992, 4.196e-05, -2.502e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 395,
    label = "C3H4O + C2H4O <=> C4H7O_B + HCO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-29.45, -2.451e-05, -5.315e-06, -7.805e-07],
            [21.74, 1.82e-05, 3.945e-06, 5.793e-07],
            [0.08813, -5.624e-07, -1.219e-07, -1.787e-08],
            [0.01674, -1.831e-07, -3.971e-08, -5.833e-09],
            [0.003509, -3.442e-08, -7.465e-09, -1.097e-09],
            [0.0009855, -1.1e-08, -2.386e-09, -3.504e-10],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 396,
    label = "S92 <=> S43 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(43, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 397,
    label = "S43 <=> CH2O + C3H5O_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.637, 0.1995, -0.01097, 8.021e-05],
            [2.391, 0.121, 0.002614, -0.0005427],
            [-0.175, 0.02009, 0.002123, 1.507e-05],
            [-0.07615, 0.007026, 0.0004699, 3.415e-05],
            [-0.03739, 0.002343, 0.0003179, 1.341e-05],
            [-0.01512, -2.298e-05, 0.0001586, 1.142e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 398,
    label = "O2 + C3H5O_C <=> S1",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.63, 0.01717, -0.002311, 0.0001389],
            [-0.04605, 0.02838, -0.003612, 0.00018],
            [-0.03014, 0.01747, -0.001907, 4.174e-05],
            [-0.01706, 0.009062, -0.0007654, -1.994e-05],
            [-0.009374, 0.004563, -0.0002838, -2.375e-05],
            [-0.005305, 0.002419, -0.0001177, -1.463e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 399,
    label = "O2 + C3H5O_C <=> S74",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.326, -0.3553, -0.003894, 0.0001632],
            [0.5094, 0.054, -0.005724, 0.0001576],
            [0.03525, 0.03, -0.002431, -4.538e-05],
            [0.03931, 0.01322, -0.000579, -8.717e-05],
            [0.02994, 0.005773, -7.208e-05, -4.966e-05],
            [0.01423, 0.002956, -1.237e-05, -2.124e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 400,
    label = "S74 <=> S1",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.457, 0.0005455, -0.0001159, 1.634e-05],
            [2.378, 0.0009539, -0.0002022, 2.842e-05],
            [0.1219, 0.0006929, -0.0001462, 2.037e-05],
            [0.02348, 0.0004554, -9.552e-05, 1.314e-05],
            [0.004947, 0.0002809, -5.849e-05, 7.923e-06],
            [0.001041, 0.0001629, -3.358e-05, 4.46e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 401,
    label = "CH2O + C3H4O <=> HCO + C3H5O_D",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-24.91, -0.0004393, -9.514e-05, -1.394e-05],
            [20.77, 0.0002304, 4.984e-05, 7.288e-06],
            [0.008466, 4.517e-06, 9.927e-07, 1.497e-07],
            [-0.00724, 3.604e-06, 7.805e-07, 1.144e-07],
            [-0.004744, 1.176e-06, 2.55e-07, 3.744e-08],
            [-0.001971, 2.239e-07, 4.859e-08, 7.151e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 402,
    label = "C2H4 + C2H4O <=> C4H7O_A + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-33.51, -0.0002724, -5.901e-05, -8.651e-06],
            [23.24, 0.0002196, 4.754e-05, 6.963e-06],
            [0.05219, -1.907e-06, -4.001e-07, -5.486e-08],
            [0.002373, -1.492e-06, -3.236e-07, -4.752e-08],
            [-0.001051, -8.863e-07, -1.921e-07, -2.82e-08],
            [-0.0001784, -3.052e-07, -6.617e-08, -9.72e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 403,
    label = "C4H7O_A <=> C3H5O_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.552, 0.1074, -0.005283, -1.343e-05],
            [3.967, 0.1283, -0.003282, -0.000244],
            [-0.09241, 0.0337, 0.0008311, -7.75e-05],
            [-0.02391, 0.00257, 0.0004242, 2.897e-05],
            [-0.003173, 1.928e-06, -1.979e-05, 6.416e-06],
            [-0.001666, 0.0003928, 7.817e-06, -5.073e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 404,
    label = "CO + NC3H7 <=> C4H7O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-37.35, 3.13e-06, -6.738e-07, 9.754e-08],
            [27.74, 6.059e-06, -1.304e-06, 1.887e-07],
            [0.1233, 5.496e-06, -1.183e-06, 1.71e-07],
            [0.02414, 4.683e-06, -1.007e-06, 1.455e-07],
            [0.005315, 3.758e-06, -8.073e-07, 1.164e-07],
            [0.001247, 2.846e-06, -6.107e-07, 8.79e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 405,
    label = "H + C2H4O <=> H2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (131000, 'cm^3/(mol*s)'),
        n = 2.58,
        Ea = (1.22, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 406,
    label = "OH + C2H4O <=> H2O + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.619, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 407,
    label = "O2 + C2H4O <=> HO2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39.15, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 408,
    label = "HO2 + C2H4O <=> H2O2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 409,
    label = "CH3CO <=> CO + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(16.9, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.65e+18, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (14.6, 'kcal/mol'),
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
    index = 410,
    label = "S60 + OH <=> H2O + C3H6 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 411,
    label = "HO2 + S60 <=> H2O2 + C3H6 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(17.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 412,
    label = "H + C2H3O <=> H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 413,
    label = "H + CH3CO <=> C2H4O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.85e+44, 'cm^6/(mol^2*s)'),
            n = -8.569,
            Ea = (5.5, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (2900, 'K'),
        T1 = (2900, 'K'),
        T2 = (5130, 'K'),
        efficiencies = {'CO': 3, 'O=C=O': 2, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3},
    ),
)

entry(
    index = 414,
    label = "H + CH3CO <=> HCO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 415,
    label = "OH + CH3CO <=> CO + CH3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 416,
    label = "C5H11_A + C2H4O <=> nC5H12 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 417,
    label = "C5H11_C + C2H4O <=> nC5H12 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 418,
    label = "C5H11_B + C2H4O <=> nC5H12 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 419,
    label = "C5H11_A + CH3CO <=> C5H10_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 420,
    label = "C5H11_C + CH3CO <=> C5H10_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.727e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 421,
    label = "C2H5O + CH3CO <=> C2H4O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 422,
    label = "NC3H7 + CH3CO <=> C3H6 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 423,
    label = "C2H5 + CH3CO <=> C2H4 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 424,
    label = "CH3O + CH3CO <=> CH2O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [CO_rad/NonDe;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [CO_rad/NonDe;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 425,
    label = "C3H7O + CH3CO <=> C3H6O_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 426,
    label = "S20 + CH3CO <=> C2H4O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 427,
    label = "CH3CO + S45 <=> C2H4O + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 428,
    label = "C3H5O_B + CH3CO <=> C3H4O + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.196e+13, 'cm^3/(mol*s)'),
        n = 0.159,
        Ea = (-0.084, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cpri_Rrad] + [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cpri_Rrad] + [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 429,
    label = "C2H4O + C2H3O <=> C2H4O + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/CO]
""",
)

entry(
    index = 430,
    label = "C2H3O <=> CH3CO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.328, 0.01613, -0.001682, 7.847e-05],
            [10.07, 0.02765, -0.002691, 9.966e-05],
            [0.03623, 0.01813, -0.001444, 1.397e-05],
            [-0.008498, 0.009354, -0.0004789, -2.732e-05],
            [-0.008455, 0.003789, -2.92e-05, -2.582e-05],
            [-0.0043, 0.001139, 7.641e-05, -1.114e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 431,
    label = "CH2O + CH3CO <=> HCO + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri;CO_rad/NonDe] for rate rule [CO_pri;CO_rad/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri;CO_rad/NonDe] for rate rule [CO_pri;CO_rad/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 432,
    label = "C2H4 + CH3CO <=> C4H7O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.58, 0.129, -0.005906, 5.917e-05],
            [-0.2421, 0.1499, -0.00227, -0.0002894],
            [-0.181, 0.03576, 0.001971, -8.112e-05],
            [-0.03877, -0.002399, 0.0007313, 6.064e-05],
            [0.006739, -0.003565, -0.0001514, 1.787e-05],
            [0.007219, -0.0003948, -0.0001156, -9.835e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 433,
    label = "HCO + CH3CO <=> CO + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;HCO] for rate rule [CO_rad/NonDe;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;HCO] for rate rule [CO_rad/NonDe;HCO]
""",
)

entry(
    index = 434,
    label = "CH2O + C3H4O <=> HCO + C3H5O_B",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-26.21, -0.0005149, -0.0001115, -1.633e-05],
            [21.21, 0.0002457, 5.313e-05, 7.762e-06],
            [0.1084, -3.729e-06, -7.895e-07, -1.104e-07],
            [0.01888, 9.992e-07, 2.156e-07, 3.137e-08],
            [0.003409, 3.951e-07, 8.56e-08, 1.255e-08],
            [0.0006254, 7.217e-08, 1.566e-08, 2.304e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 435,
    label = "C5H11_B <=> S26 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.24e-14, 's^-1'), n=7.022, Ea=(15.354, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.1e+12, 's^-1'), n=-0.402, Ea=(29.991, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.07e+27, 's^-1'), n=-4.483, Ea=(39.814, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.02e+26, 's^-1'), n=-3.794, Ea=(40.806, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.52e+16, 's^-1'), n=-0.987, Ea=(36.957, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 436,
    label = "C5H11_A <=> S26 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10, 100, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.26e+10, 's^-1'), n=-0.118, Ea=(29.715, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.92e+26, 's^-1'), n=-4.456, Ea=(39.997, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.81e+29, 's^-1'), n=-4.969, Ea=(43.662, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.22e+20, 's^-1'), n=-2.16, Ea=(40.523, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.05e+11, 's^-1'), n=0.526, Ea=(36.461, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 437,
    label = "O2 + C5H11_B <=> HO2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.837, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (11.96, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 438,
    label = "O2 + C5H11_A <=> HO2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.535, 'cm^3/(mol*s)'),
        n = 3.71,
        Ea = (9.322, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 439,
    label = "S64 <=> HO2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.58e+07, 's^-1'), n=1.58, Ea=(28.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 440,
    label = "S42 <=> HO2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.403e+09, 's^-1'), n=1.13, Ea=(30.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 441,
    label = "S26 <=> C2H4 + C3H6",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.62e+06, 's^-1'),
        n = 1.81,
        Ea = (53.454, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 442,
    label = "S26 + H <=> C2H4 + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+21, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '08/TSAwip  !BS',
    ),
    longDesc = 
u"""
08/TSAwip  !BS
""",
)

entry(
    index = 443,
    label = "S26 + H <=> C2H5 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (11.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(C3H6+H)',
    ),
    longDesc = 
u"""
=(C3H6+H)
""",
)

entry(
    index = 444,
    label = "C5H11_A + H <=> H2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+H)\nSXC5H11+H = nC3H7+C2H5                       4.00E+24   -2.83  17542.0  ! =(iC3H7+H)',
    ),
    longDesc = 
u"""
=(iC3H7+H)
SXC5H11+H = nC3H7+C2H5                       4.00E+24   -2.83  17542.0  ! =(iC3H7+H)
""",
)

entry(
    index = 445,
    label = "C5H11_A + OH <=> H2O + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(iC3H7+O)',
    ),
    longDesc = 
u"""
=(iC3H7+O)
""",
)

entry(
    index = 446,
    label = "C5H11_B + H <=> H2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+H)  1 atm\nPXC5H11+H = nC3H7+C2H5                       3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm',
    ),
    longDesc = 
u"""
=(nC3H7+H)  1 atm
PXC5H11+H = nC3H7+C2H5                       3.10E+27   -3.59   19059.0 ! =(nC3H7+H) 10 atm
""",
)

entry(
    index = 447,
    label = "C5H11_B + OH <=> H2O + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '=(nC3H7+O)',
    ),
    longDesc = 
u"""
=(nC3H7+O)
""",
)

entry(
    index = 448,
    label = "HO2 + C5H11_A <=> H2O2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 449,
    label = "C5H11_A + C5H11_A <=> nC5H12 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.266e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 450,
    label = "C5H11_A + C5H11_C <=> nC5H12 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 451,
    label = "HO2 + C5H11_B <=> H2O2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 452,
    label = "C5H11_B + C5H11_A <=> nC5H12 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.565e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 453,
    label = "C5H11_B + C5H11_C <=> nC5H12 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 454,
    label = "C5H11_B + C5H11_B <=> nC5H12 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 455,
    label = "C2H4 + C3H6 <=> S26",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-20.31, -0.0004435, -9.604e-05, -1.407e-05],
            [16.58, 0.0002036, 4.405e-05, 6.441e-06],
            [0.05032, -2.655e-06, -5.627e-07, -7.887e-08],
            [0.008859, 7.516e-07, 1.623e-07, 2.365e-08],
            [0.001724, 1.743e-07, 3.779e-08, 5.551e-09],
            [0.0006548, 2.43e-09, 5.441e-10, 8.498e-11],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 456,
    label = "C5H11_A + C2H3O <=> S26 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Csrad] for rate rule [C_rad/H2/CO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cmethyl_Csrad] for rate rule [C_rad/H2/CO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 457,
    label = "C5H11_B + C2H3O <=> S26 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 458,
    label = "HCO + C5H11_A <=> CH2O + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.517e+13, 'cm^3/(mol*s)'),
        n = -0.096,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 459,
    label = "HCO + C5H11_B <=> CH2O + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 460,
    label = "C5H11_A + CH3CO <=> S26 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 461,
    label = "C5H11_B + CH3CO <=> S26 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 462,
    label = "CH2O + C3H5O_C <=> S94",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-39.38, -0.0001511, -3.274e-05, -4.804e-06],
            [25.52, 0.0001076, 2.331e-05, 3.418e-06],
            [0.01035, -1.801e-06, -3.871e-07, -5.584e-08],
            [-0.001598, -4.199e-07, -9.11e-08, -1.34e-08],
            [-0.0004058, -2.021e-07, -4.383e-08, -6.434e-09],
            [0.0002694, -7.468e-08, -1.619e-08, -2.378e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 463,
    label = "HO2 + C3H6 <=> S54",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.835, -0.01621, -0.003946, -0.0004299],
            [10.11, 0.01692, 0.001976, 0.0003597],
            [0.17, -0.001048, -0.001274, -2.873e-05],
            [0.03203, 0.002085, -0.0004529, 1.282e-05],
            [0.004741, 0.001852, -0.0001786, 2.31e-05],
            [-5.237e-05, 0.001018, -0.0001122, 9.549e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 464,
    label = "C2H4 + N2O3_C <=> S53",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.14, 0.001324, -0.0002858, 4.16e-05],
            [-0.0009131, 0.0007433, -0.0001601, 2.319e-05],
            [-3.228e-05, 2.616e-05, -5.582e-06, 7.935e-07],
            [3.23e-05, -2.625e-05, 5.635e-06, -8.107e-07],
            [8.804e-06, -7.155e-06, 1.535e-06, -2.209e-07],
            [1.196e-06, -9.793e-07, 2.136e-07, -3.175e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 465,
    label = "C2H4 + C2H3O <=> C4H7O_B",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-35.38, -6.771e-05, -1.468e-05, -2.155e-06],
            [23.92, 3.627e-05, 7.862e-06, 1.154e-06],
            [0.06272, -1.943e-08, -4.811e-09, -4.563e-10],
            [0.01058, 8.671e-08, 1.8e-08, 2.759e-09],
            [0.001393, 3.855e-08, 7.738e-09, 1.227e-09],
            [0.0003088, 3.764e-09, 3.66e-10, 1.201e-10],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 466,
    label = "C2H4 + C2H3O <=> C3H5O_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-35.38, -6.771e-05, -1.468e-05, -2.155e-06],
            [23.92, 3.627e-05, 7.862e-06, 1.154e-06],
            [0.06272, -2.163e-08, -4.334e-09, -5.264e-10],
            [0.01058, 8.489e-08, 1.839e-08, 2.701e-09],
            [0.001393, 3.714e-08, 8.044e-09, 1.182e-09],
            [0.0003088, 2.739e-09, 5.883e-10, 8.748e-11],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 467,
    label = "C3H6O_A + C2H3O <=> S43",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-42.79, -0.0002026, -4.39e-05, -6.436e-06],
            [26.57, 0.0001782, 3.86e-05, 5.657e-06],
            [-0.04484, -1.649e-06, -3.494e-07, -4.891e-08],
            [-0.02073, -2.968e-06, -6.43e-07, -9.43e-08],
            [-0.004715, -1.102e-06, -2.39e-07, -3.509e-08],
            [-0.0002094, -3.005e-07, -6.516e-08, -9.572e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 468,
    label = "C5H10_A + N2O3_C <=> S8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [o_atom_singlet;mb_db_twocdisub_Nd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [o_atom_singlet;mb_db_twocdisub_Nd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 469,
    label = "S30 <=> C3H6 + N2O3_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.956, 0.06441, -0.01046, 0.0008122],
            [0.1977, 0.03475, -0.00484, 0.0001876],
            [-0.06672, -0.001174, 0.0001332, -5.788e-06],
            [-0.01238, -0.002281, 0.00017, 2.093e-05],
            [-0.002225, -0.0005118, 2.794e-05, 6.838e-06],
            [-0.0006028, -5.957e-05, 1.019e-05, -2.017e-07],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 470,
    label = "CH2O + C3H5O_B <=> CH2O + C3H5O_D",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-14.64, -0.0002572, -5.573e-05, -8.174e-06],
            [14.71, 0.0001236, 2.676e-05, 3.92e-06],
            [0.1017, -1.484e-06, -3.17e-07, -4.517e-08],
            [0.01631, 8.735e-07, 1.891e-07, 2.768e-08],
            [0.001371, 4.684e-07, 1.015e-07, 1.489e-08],
            [-0.0003395, 2.046e-07, 4.434e-08, 6.508e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 471,
    label = "NO2 + HCO <=> HONO + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.24e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (2.355, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 472,
    label = "HONO + H <=> H2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.01e+08, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (6.614, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 473,
    label = "HONO + H <=> NO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+06, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (3.847, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 474,
    label = "HONO + HONO <=> NO + H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.349, 'cm^3/(mol*s)'),
        n = 3.64,
        Ea = (12.14, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 475,
    label = "CH2O + NO2 <=> HONO + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e-07, 'cm^3/(mol*s)'),
        n = 5.64,
        Ea = (9.221, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 476,
    label = "HONO <=> NO + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2e+31, 'cm^3/(mol*s)'),
            n = -4.56,
            Ea = (51.146, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
)

entry(
    index = 477,
    label = "HONO + OH <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.596, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 478,
    label = "HONO + C5H11_C <=> nC5H12 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93.4, 'cm^3/(mol*s)'),
        n = 2.872,
        Ea = (3.661, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]
""",
)

entry(
    index = 479,
    label = "HONO + C5H11_A <=> nC5H12 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93.4, 'cm^3/(mol*s)'),
        n = 2.872,
        Ea = (3.661, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]
""",
)

entry(
    index = 480,
    label = "HONO + C5H11_B <=> nC5H12 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.245,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeN;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeN;C_rad/H2/Cs]
""",
)

entry(
    index = 481,
    label = "HO2 + NO2 <=> O2 + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32600, 'cm^3/(mol*s)'),
        n = 2.725,
        Ea = (3.753, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;O_rad/OneDeN] for rate rule [Orad_O_H;O_rad/OneDeN]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;O_rad/OneDeN] for rate rule [Orad_O_H;O_rad/OneDeN]
""",
)

entry(
    index = 482,
    label = "NO2 + C5H11_A <=> HONO + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 483,
    label = "NO2 + C5H11_A <=> HONO + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_sec_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_sec_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 484,
    label = "C2H5 + NO2 <=> C2H4 + HONO",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_sec_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_sec_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 485,
    label = "NO2 + NC3H7 <=> HONO + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 486,
    label = "NO2 + C5H11_C <=> HONO + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 487,
    label = "NO2 + C5H11_B <=> HONO + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 488,
    label = "HONO + C2H3O <=> NO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.245,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeN;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeN;C_rad/H2/CO]
""",
)

entry(
    index = 489,
    label = "HONO + CH3CO <=> NO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33e-06, 'cm^3/(mol*s)'),
        n = 5.09,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;CO_rad/Cs] for rate rule [O/H/OneDeN;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;CO_rad/Cs] for rate rule [O/H/OneDeN;CO_rad/Cs]
""",
)

entry(
    index = 490,
    label = "NO2 + C3H7O <=> HONO + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_sec_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_sec_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 491,
    label = "NO2 + C2H5O <=> HONO + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_sec_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_sec_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 492,
    label = "CH3O + NO2 <=> CH2O + HONO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Rrad] for rate rule [O_sec_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Rrad] for rate rule [O_sec_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 493,
    label = "S20 + NO2 <=> HONO + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_sec_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_sec_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 494,
    label = "NO2 + S45 <=> HONO + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.708e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_Csrad]
""",
)

entry(
    index = 495,
    label = "NO2 + C3H5O_B <=> HONO + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cpri_Rrad] for rate rule [O_sec_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cpri_Rrad] for rate rule [O_sec_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 496,
    label = "HO2 + HONO <=> H2O2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2428, 'cm^3/(mol*s)'),
        n = 2.768,
        Ea = (2.98, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;O_rad/NonDeO] + [O/H/OneDeN;O_rad] for rate rule [O/H/OneDeN;O_rad/NonDeO]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;O_rad/NonDeO] + [O/H/OneDeN;O_rad] for rate rule [O/H/OneDeN;O_rad/NonDeO]
""",
)

entry(
    index = 497,
    label = "NO2 + H <=> HONO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.78, 0.05066, -0.005159, 0.0002427],
            [-0.1473, 0.05089, -0.00309, -7.572e-05],
            [-0.05757, 0.01675, -0.0001929, -8.802e-05],
            [-0.01942, 0.004035, 0.0001747, -1.912e-05],
            [-0.005865, 0.0007782, 6.646e-05, 2.537e-06],
            [-0.001578, 8.536e-05, 1.888e-05, 1.432e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 498,
    label = "NO2 + S26 <=> S81",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.908e+07, 'cm^3/(mol*s)'),
        n = 2.339,
        Ea = (6.697, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cds-HH_Cds;NJ] + [Cds-HH_Cds-CsH;YJ] for rate rule [Cds-HH_Cds-CsH;NJ]\nEa raised from 22.9 to 28.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cds-HH_Cds;NJ] + [Cds-HH_Cds-CsH;YJ] for rate rule [Cds-HH_Cds-CsH;NJ]
Ea raised from 22.9 to 28.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 499,
    label = "N2 + HONO <=> N3O + OH",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-30.32, -4.489e-09, -9.733e-10, -1.429e-10],
            [24.3, -6.862e-09, -1.488e-09, -2.185e-10],
            [0.03496, -3.897e-09, -8.451e-10, -1.241e-10],
            [0.009867, -1.86e-09, -4.034e-10, -5.924e-11],
            [0.002518, -7.937e-10, -1.721e-10, -2.526e-11],
            [0.0008647, -3.131e-10, -6.788e-11, -9.966e-12],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 500,
    label = "CH2O + C4H7O_B <=> C3H5O_D + C2H4O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-17.29, -0.0002454, -5.316e-05, -7.795e-06],
            [15.05, 0.0001735, 3.757e-05, 5.505e-06],
            [-0.08126, 1.6e-05, 3.474e-06, 5.115e-07],
            [-0.07139, 3.654e-06, 7.924e-07, 1.164e-07],
            [-0.02322, -6.839e-07, -1.481e-07, -2.169e-08],
            [-0.003222, -6.137e-07, -1.33e-07, -1.953e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 501,
    label = "CH2O + C4H7O_B <=> C3H5O_B + C2H4O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-18.2, -0.0002817, -6.103e-05, -8.947e-06],
            [14.68, 0.0001873, 4.056e-05, 5.941e-06],
            [-0.3211, 1.358e-05, 2.951e-06, 4.353e-07],
            [-0.1428, 3.544e-06, 7.682e-07, 1.128e-07],
            [-0.04265, -4.867e-08, -1.048e-08, -1.516e-09],
            [-0.007712, -5.316e-08, -1.154e-08, -1.7e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 502,
    label = "HO2 + C3H5O_E <=> S88 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 503,
    label = "CH3O2 + C3H5O_E <=> CH3O + S88",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.205e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 504,
    label = "CH2O + C2H4O <=> S88 + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-45.88, -8.817e-08, -1.912e-08, -2.808e-09],
            [27.2, 7.308e-08, 1.585e-08, 2.327e-09],
            [0.08477, -2.77e-09, -6.006e-10, -8.82e-11],
            [0.01616, -5.703e-10, -1.237e-10, -1.815e-11],
            [0.003682, -2.107e-10, -4.567e-11, -6.696e-12],
            [0.001123, -6.438e-11, -1.395e-11, -2.044e-12],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 505,
    label = "CO + C2H5O <=> S88",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-37.35, 0.0001497, -2.857e-05, 3.397e-06],
            [27.74, 0.000288, -5.484e-05, 6.495e-06],
            [0.123, 0.0002565, -4.851e-05, 5.68e-06],
            [0.02386, 0.0002119, -3.965e-05, 4.55e-06],
            [0.005101, 0.0001631, -3.002e-05, 3.344e-06],
            [0.001091, 0.0001172, -2.111e-05, 2.255e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 506,
    label = "S88 <=> CH2O + CH3CO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.833, 0.3212, -0.00769, -0.0002639],
            [1.64, 0.02718, 0.004168, 0.0001021],
            [-0.1341, 0.004975, 0.0001665, -5.785e-05],
            [-0.007785, 0.0006267, -0.0001931, -1.119e-05],
            [-0.006164, 0.0004258, -5.015e-05, 4.434e-06],
            [-0.005447, 9.715e-06, 4.898e-06, 5.664e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 507,
    label = "S26 + N2O3_C <=> S28",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.02, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [o_atom_singlet;mb_db]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [o_atom_singlet;mb_db]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 508,
    label = "NO + C3H4O <=> S38",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.313, 1.27e-15, 3.775e-15, 1.499e-15],
            [3.613, 1.31e-14, -2.776e-15, 2.609e-15],
            [0.2548, -3.927e-15, -4.274e-15, 3.469e-16],
            [0.04788, -1.776e-15, -9.437e-16, 1.624e-15],
            [0.009111, -9.243e-15, -2.442e-15, 2.331e-15],
            [0.001566, 6.384e-15, 2.72e-15, 7.216e-16],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 509,
    label = "C5H11_A + S27 <=> nC5H12 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 510,
    label = "C5H11_C + S27 <=> nC5H12 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 511,
    label = "C5H11_B + S27 <=> nC5H12 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 512,
    label = "O2 + S27 <=> HO2 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.288e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;O_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;O_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 513,
    label = "OH + S27 <=> H2O + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;O_Csrad]
""",
)

entry(
    index = 514,
    label = "C2H3O + S27 <=> C2H4O + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/CO;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/CO;O_Csrad]
""",
)

entry(
    index = 515,
    label = "CH3CO + S27 <=> C2H4O + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 516,
    label = "HCO + S27 <=> CH2O + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri_rad;O_Csrad]
""",
)

entry(
    index = 517,
    label = "H + S27 <=> H2 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;O_Csrad]
""",
)

entry(
    index = 518,
    label = "HO2 + S27 <=> H2O2 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 519,
    label = "NO2 + S27 <=> HONO + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.708e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_Csrad]
""",
)

entry(
    index = 520,
    label = "H + S87 <=> S27",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10, 0.007972, -0.0008305, 3.749e-05],
            [1.904, 0.01469, -0.001492, 6.246e-05],
            [0.07126, 0.01151, -0.001077, 3.383e-05],
            [0.001788, 0.007673, -0.0006117, 6.415e-06],
            [-0.006433, 0.004335, -0.0002528, -8.66e-06],
            [-0.004859, 0.002037, -5.151e-05, -1.126e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 521,
    label = "S58 <=> S38",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.303, 0.3663, -0.004195, -0.0004401],
            [3.492, -0.03315, -0.005896, -0.000565],
            [0.0874, -0.01433, -0.002271, -0.0001473],
            [-0.05085, -0.002623, -0.0001745, 5.325e-05],
            [-0.01655, 0.00078, 0.0002975, 6.227e-05],
            [0.009137, 0.0003429, 0.0001032, 1.53e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 522,
    label = "NO2 + HCO <=> NO + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.39e+15, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (1.93, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 523,
    label = "NO2 + CO <=> NO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.91e+13, 'cm^3/(mol*s)'), n=0, Ea=(67.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 524,
    label = "CO + OH <=> H + CO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (70150, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-0.356, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.757e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (0.332, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 525,
    label = "HO2 + CO <=> OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17.94, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 526,
    label = "HO2 + HCO <=> H + OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 527,
    label = "CH3O + CO <=> CH3 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 528,
    label = "HO2 + CH3CO <=> CH3 + OH + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 529,
    label = "H + H + CO2 <=> H2 + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.5e+20, 'cm^6/(mol^2*s)'),
        n = -2,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'GRI3.0 * 0.94',
    ),
    longDesc = 
u"""
GRI3.0 * 0.94
""",
)

entry(
    index = 530,
    label = "S58 <=> CO2 + S76",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.521, 0.3446, -0.007115, -0.0005872],
            [0.2479, -0.04569, -0.006609, -0.000393],
            [-0.1407, -0.01226, -0.001671, -5.003e-05],
            [-0.07312, -0.001231, -8.939e-05, 5.365e-05],
            [-0.01665, -8.502e-05, 0.0001863, 6.306e-05],
            [0.008839, -0.0008925, 2.593e-05, 1.578e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 531,
    label = "O2 + S76 <=> HO2 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.16e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;CH_d_Rrad] for rate rule [O2b;Cds/H/NonDe_d_Rrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O2b;CH_d_Rrad] for rate rule [O2b;Cds/H/NonDe_d_Rrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 532,
    label = "HO2 + S76 <=> H2O2 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 533,
    label = "NO2 + S76 <=> HONO + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_sec_rad;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_sec_rad;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 534,
    label = "C5H11_A + S76 <=> nC5H12 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 535,
    label = "C5H11_C + S76 <=> nC5H12 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 536,
    label = "C5H11_B + S76 <=> nC5H12 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 537,
    label = "OH + S76 <=> H2O + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 538,
    label = "H + S76 <=> H2 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;CH_d_Rrad] for rate rule [H_rad;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;CH_d_Rrad] for rate rule [H_rad;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 539,
    label = "C2H3O + S76 <=> CH3CN + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/CO;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/CO;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 540,
    label = "HCO + S76 <=> CH2O + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 541,
    label = "CH3CO + S76 <=> CH3CN + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 542,
    label = "CH3CN + H <=> S76",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.768, 0.004779, -0.0009032, 0.0001035],
            [0.1733, -0.004319, 0.000762, -7.545e-05],
            [-0.2586, 0.0008015, -0.0001185, 7.179e-06],
            [-0.05029, -7.035e-05, 6.231e-06, 3.913e-07],
            [-0.01109, -1.48e-05, 3.713e-06, -5.499e-07],
            [-0.002607, -2.467e-06, 5.873e-07, -9.97e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 543,
    label = "C2H4 + S88 <=> CH2O + C4H7O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-22.27, -0.0002899, -6.281e-05, -9.208e-06],
            [15.37, 0.0001748, 3.786e-05, 5.545e-06],
            [-0.3779, 7.745e-06, 1.686e-06, 2.496e-07],
            [-0.1565, 3.065e-06, 6.643e-07, 9.747e-08],
            [-0.0449, 9.028e-07, 1.957e-07, 2.873e-08],
            [-0.009137, 4.537e-07, 9.834e-08, 1.443e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 544,
    label = "CH2O + CH3O2 <=> CH4O2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.66, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 545,
    label = "CH3O2 + HO2 <=> O2 + CH4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.47e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.57, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 546,
    label = "CH3O2 + H2 <=> CH4O2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+14, 'cm^3/(mol*s)'), n=0, Ea=(26.03, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 547,
    label = "CH3O2 + C2H4O <=> CH4O2 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 548,
    label = "nC5H12 + CH3O2 <=> CH4O2 + C5H11_B",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.386, 'cm^3/(mol*s)'),
        n = 3.97,
        Ea = (18.28, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 549,
    label = "nC5H12 + CH3O2 <=> CH4O2 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20.37, 'cm^3/(mol*s)'),
        n = 3.58,
        Ea = (14.81, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 550,
    label = "nC5H12 + CH3O2 <=> CH4O2 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10.19, 'cm^3/(mol*s)'),
        n = 3.58,
        Ea = (14.81, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 551,
    label = "CH3O2 + C5H11_A <=> CH4O2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 552,
    label = "CH3O2 + C5H11_A <=> CH4O2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 553,
    label = "C2H5 + CH3O2 <=> CH4O2 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 554,
    label = "CH3O2 + NC3H7 <=> CH4O2 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 555,
    label = "CH3O2 + C5H11_C <=> CH4O2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 556,
    label = "CH3O2 + C5H11_B <=> CH4O2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 557,
    label = "CH4O2 + OH <=> CH3O2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40.7, 'cm^3/(mol*s)'),
        n = 3.161,
        Ea = (4.019, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]
""",
)

entry(
    index = 558,
    label = "CH4O2 + C2H3O <=> CH3O2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/CO]
""",
)

entry(
    index = 559,
    label = "CH3O2 + C3H7O <=> CH4O2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 560,
    label = "CH3O2 + C2H5O <=> CH4O2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 561,
    label = "CH3O + CH3O2 <=> CH2O + CH4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.248e+07, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 562,
    label = "CH3O2 + S20 <=> CH4O2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 563,
    label = "CH3O2 + S45 <=> CH4O2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 564,
    label = "CH3O2 + C3H5O_B <=> CH4O2 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.318e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 565,
    label = "CH3O2 + HCO <=> CH4O2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.24e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (2.355, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;HCO] for rate rule [O_rad/NonDeO;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;HCO] for rate rule [O_rad/NonDeO;HCO]
""",
)

entry(
    index = 566,
    label = "CH3O2 + H2O2 <=> CH4O2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.184, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (6.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 536 H2O2 + CH3O2 <=> HO2 + CH4O2 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Matched reaction 536 H2O2 + CH3O2 <=> HO2 + CH4O2 in H_Abstraction/training
""",
)

entry(
    index = 567,
    label = "CH3O2 + HONO <=> CH4O2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.092, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (6.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;OOC] for rate rule [O/H/OneDeN;OOC]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;OOC] for rate rule [O/H/OneDeN;OOC]
""",
)

entry(
    index = 568,
    label = "CH3O2 + S27 <=> CH4O2 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 569,
    label = "CH3O2 + S76 <=> CH4O2 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 570,
    label = "HO2 + CH3 <=> CH4O2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.97, 0.04783, -0.003877, 0.0001319],
            [-0.1821, 0.07117, -0.004503, 9.402e-06],
            [-0.1085, 0.03447, -0.0008814, -0.0001236],
            [-0.05093, 0.01119, 0.0004088, -6.58e-05],
            [-0.01957, 0.002032, 0.0003567, -1.255e-06],
            [-0.006314, -0.0001087, 0.0001057, 1.328e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 571,
    label = "CH3O + OH <=> CH4O2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.18, 0.05866, -0.004507, 0.0001641],
            [-0.5268, 0.07903, -0.003998, -6.537e-05],
            [-0.1363, 0.03397, -0.0002933, -0.0001274],
            [-0.05412, 0.009545, 0.0005214, -3.499e-05],
            [-0.01969, 0.001603, 0.0002423, 1.351e-05],
            [-0.006113, 6.062e-06, 2.441e-05, 1.248e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 572,
    label = "CH3O2 + H <=> CH4O2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.17, 0.004251, -0.0006125, 4.664e-05],
            [-0.07592, 0.007484, -0.001047, 7.418e-05],
            [-0.0182, 0.005344, -0.0006914, 3.99e-05],
            [-0.00745, 0.003217, -0.0003656, 1.319e-05],
            [-0.003567, 0.001672, -0.0001546, 1.722e-07],
            [-0.001695, 0.0007574, -4.893e-05, -3.276e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 573,
    label = "O2 + S74 <=> HO2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 574,
    label = "HO2 + S74 <=> H2O2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 575,
    label = "NO2 + S74 <=> HONO + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_sec_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_sec_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 576,
    label = "C5H11_A + S74 <=> nC5H12 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 577,
    label = "C5H11_C + S74 <=> nC5H12 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 578,
    label = "C5H11_B + S74 <=> nC5H12 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 579,
    label = "OH + S74 <=> H2O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 580,
    label = "CH3O2 + S74 <=> CH4O2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 581,
    label = "H + S74 <=> H2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 582,
    label = "C2H3O + S74 <=> C2H4O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Csrad] for rate rule [C_rad/H2/CO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cmethyl_Csrad] for rate rule [C_rad/H2/CO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 583,
    label = "HCO + S74 <=> CH2O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.517e+13, 'cm^3/(mol*s)'),
        n = -0.096,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 584,
    label = "H + S22 <=> S74",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.45, 0.0003433, -6.807e-05, 8.434e-06],
            [0.4931, 0.0006585, -0.0001304, 1.61e-05],
            [0.06071, 0.0005816, -0.0001145, 1.399e-05],
            [0.01143, 0.0004737, -9.243e-05, 1.107e-05],
            [0.002189, 0.0003567, -6.863e-05, 7.978e-06],
            [0.0002978, 0.0002487, -4.69e-05, 5.214e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 585,
    label = "CH3CO + S74 <=> C2H4O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 586,
    label = "N2O3_B <=> NO + NO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.58, 0.389, -6.031e-06, -8.853e-07],
            [1.485, 4.601e-06, 9.989e-07, 1.471e-07],
            [-0.07065, -4.63e-06, -1.003e-06, -1.469e-07],
            [0.003475, -1.319e-06, -2.855e-07, -4.175e-08],
            [0.004359, -4.242e-07, -9.166e-08, -1.337e-08],
            [0.001061, -1.041e-07, -2.241e-08, -3.246e-09],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 587,
    label = "NO + C5H10_A <=> S59",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (26.253, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds_Cds;N3J] for rate rule [Cds-CsH_Cds-CsH;N3dJ_O]\nEa raised from 106.0 to 109.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds_Cds;N3J] for rate rule [Cds-CsH_Cds-CsH;N3dJ_O]
Ea raised from 106.0 to 109.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 588,
    label = "C5H11_C + S86 <=> nC5H12 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.979e-06, 'cm^3/(mol*s)'),
        n = 4.886,
        Ea = (-2.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]
""",
)

entry(
    index = 589,
    label = "C5H11_A + S86 <=> nC5H12 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.979e-06, 'cm^3/(mol*s)'),
        n = 4.886,
        Ea = (-2.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]
""",
)

entry(
    index = 590,
    label = "C5H11_B + S86 <=> nC5H12 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002046, 'cm^3/(mol*s)'),
        n = 4.189,
        Ea = (-1.293, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]
""",
)

entry(
    index = 591,
    label = "HO2 + S46 <=> O2 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21380, 'cm^3/(mol*s)'),
        n = 2.068,
        Ea = (2.024, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;OOC] + [Orad_O_H;O_rad/NonDeO] for rate rule [Orad_O_H;OOC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [X_H;OOC] + [Orad_O_H;O_rad/NonDeO] for rate rule [Orad_O_H;OOC]
""",
)

entry(
    index = 592,
    label = "C5H11_A + S46 <=> C5H10_A + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 593,
    label = "C5H11_A + S46 <=> S26 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 594,
    label = "C2H5 + S46 <=> C2H4 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 595,
    label = "NC3H7 + S46 <=> C3H6 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 596,
    label = "C5H11_C + S46 <=> C5H10_A + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 597,
    label = "C5H11_B + S46 <=> S26 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 598,
    label = "OH + S86 <=> H2O + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40.7, 'cm^3/(mol*s)'),
        n = 3.161,
        Ea = (4.019, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]
""",
)

entry(
    index = 599,
    label = "C2H3O + S86 <=> C2H4O + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e-10, 'cm^3/(mol*s)'),
        n = 6.3,
        Ea = (-2.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/CO]
""",
)

entry(
    index = 600,
    label = "CH3CO + S86 <=> C2H4O + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33e-06, 'cm^3/(mol*s)'),
        n = 5.09,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;CO_rad/Cs]
""",
)

entry(
    index = 601,
    label = "C3H7O + S46 <=> C3H6O_A + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 602,
    label = "HCO + S86 <=> CH2O + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001496, 'cm^3/(mol*s)'),
        n = 4.67,
        Ea = (0.767, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;CO_rad] for rate rule [O/H/NonDeO;CO_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/NonDeO;CO_rad] for rate rule [O/H/NonDeO;CO_pri_rad]
""",
)

entry(
    index = 603,
    label = "C2H5O + S46 <=> C2H4O + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 604,
    label = "CH3O + S46 <=> CH2O + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.248e+07, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 605,
    label = "S20 + S46 <=> S11 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 606,
    label = "S45 + S46 <=> S11 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 607,
    label = "C3H5O_B + S46 <=> C3H4O + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.318e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 608,
    label = "H + S86 <=> H2 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.127, 'cm^3/(mol*s)'),
        n = 3.554,
        Ea = (2.65, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;H_rad] + [O/H/NonDeO;Y_rad] for rate rule [O/H/NonDeO;H_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;H_rad] + [O/H/NonDeO;Y_rad] for rate rule [O/H/NonDeO;H_rad]
""",
)

entry(
    index = 609,
    label = "HCO + S46 <=> CO + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.24e+23, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (2.355, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;HCO] for rate rule [O_rad/NonDeO;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;HCO] for rate rule [O_rad/NonDeO;HCO]
""",
)

entry(
    index = 610,
    label = "H2O2 + S46 <=> HO2 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.184, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (6.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;OOC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;OOC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 611,
    label = "S46 + S74 <=> S86 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.003e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 612,
    label = "HONO + S46 <=> NO2 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.092, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (6.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;OOC] for rate rule [O/H/OneDeN;OOC]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;OOC] for rate rule [O/H/OneDeN;OOC]
""",
)

entry(
    index = 613,
    label = "S27 + S46 <=> S87 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 614,
    label = "S46 + S76 <=> CH3CN + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 615,
    label = "CH4O2 + S46 <=> CH3O2 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.092, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (6.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;OOC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;OOC]
""",
)

entry(
    index = 616,
    label = "HO2 + C3H5O_D <=> S86",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.94, 0.0009841, -0.0001709, 1.723e-05],
            [-0.002581, 0.001861, -0.0003214, 3.204e-05],
            [-0.002205, 0.001576, -0.0002677, 2.578e-05],
            [-0.001708, 0.001203, -0.0001985, 1.795e-05],
            [-0.001209, 0.0008335, -0.0001315, 1.073e-05],
            [-0.0007876, 0.0005271, -7.801e-05, 5.365e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 617,
    label = "H + S46 <=> S86",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.18, 4.4e-06, -9.488e-07, 1.379e-07],
            [-0.06408, 8.471e-06, -1.827e-06, 2.653e-07],
            [-0.009419, 7.565e-06, -1.631e-06, 2.367e-07],
            [-0.001851, 6.286e-06, -1.354e-06, 1.964e-07],
            [-0.000412, 4.881e-06, -1.051e-06, 1.522e-07],
            [-9.978e-05, 3.555e-06, -7.646e-07, 1.105e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 618,
    label = "C5H10_A + OH <=> S3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.75e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.782, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 619,
    label = "S32 <=> S3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000, 's^-1'),
        n = 2.287,
        Ea = (20.24, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_SS;O_rad_out;Cs_H_out_H/(NonDeC/Cs)] for rate rule [R3H_SS_Cs;O_rad_out;Cs_H_out_H/(NonDeC/Cs)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3H_SS;O_rad_out;Cs_H_out_H/(NonDeC/Cs)] for rate rule [R3H_SS_Cs;O_rad_out;Cs_H_out_H/(NonDeC/Cs)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 620,
    label = "NO + C5H10_A <=> S70",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (26.253, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds_Cds;N3J] for rate rule [Cds-CsH_Cds-CsH;N3dJ_O]\nEa raised from 106.0 to 109.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds_Cds;N3J] for rate rule [Cds-CsH_Cds-CsH;N3dJ_O]
Ea raised from 106.0 to 109.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 621,
    label = "O2 + S3 <=> S31",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 622,
    label = "S31 <=> C3H6O_A + OH + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+10, 's^-1'), n=0, Ea=(18.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 623,
    label = "CH2O + HO2 <=> CH3O3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.616, 0.1237, -0.007921, 0.0001695],
            [-0.06221, 0.1221, -0.00209, -0.0003802],
            [-0.08868, 0.03074, 0.001581, -0.0001021],
            [-0.02678, 0.00158, 0.0006995, 3.886e-05],
            [-0.001415, -0.001875, 2.478e-05, 2.03e-05],
            [0.002884, -0.0007385, -6.782e-05, -9.379e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 624,
    label = "S19 <=> S74",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.17, 0.0809, -0.007875, 0.0003182],
            [9.346, 0.09973, -0.006717, -0.0001286],
            [-0.03323, 0.02956, 0.0003185, -0.0002974],
            [-0.01038, 0.001093, 0.001154, -6.199e-05],
            [-0.0009804, -0.001008, 0.0001402, 4.359e-05],
            [-0.002008, 0.001008, -0.0001764, 1.263e-05],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 625,
    label = "C5H11_A + S19 <=> nC5H12 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 626,
    label = "C5H11_C + S19 <=> nC5H12 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 627,
    label = "C5H11_B + S19 <=> nC5H12 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 628,
    label = "O2 + S19 <=> HO2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.288e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;O_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;O_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 629,
    label = "OH + S19 <=> H2O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;O_Csrad]
""",
)

entry(
    index = 630,
    label = "C2H3O + S19 <=> C2H4O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/CO;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/CO;O_Csrad]
""",
)

entry(
    index = 631,
    label = "CH3CO + S19 <=> C2H4O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 632,
    label = "HCO + S19 <=> CH2O + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri_rad;O_Csrad]
""",
)

entry(
    index = 633,
    label = "H + S19 <=> H2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;O_Csrad]
""",
)

entry(
    index = 634,
    label = "HO2 + S19 <=> H2O2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 635,
    label = "NO2 + S19 <=> HONO + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.708e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O_sec_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O_sec_rad;O_Csrad]
""",
)

entry(
    index = 636,
    label = "CH3O2 + S19 <=> CH4O2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 637,
    label = "S46 + S19 <=> S86 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 638,
    label = "H + S22 <=> S19",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.538, 0.001984, -0.0002951, 2.293e-05],
            [2.098, 0.003786, -0.000559, 4.275e-05],
            [0.07327, 0.00329, -0.0004749, 3.451e-05],
            [0.01126, 0.002604, -0.0003609, 2.376e-05],
            [0.0003501, 0.001877, -0.0002437, 1.34e-05],
            [-0.001276, 0.001228, -0.0001442, 5.45e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 639,
    label = "NO + S26 <=> S71",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (26.162, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds_Cds;N3J] for rate rule [Cds-CsH_Cds-HH;N3dJ_O]\nEa raised from 106.0 to 109.5 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds_Cds;N3J] for rate rule [Cds-CsH_Cds-HH;N3dJ_O]
Ea raised from 106.0 to 109.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 640,
    label = "S71 <=> S70",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.307e+07, 's^-1'),
        n = 1.53,
        Ea = (34.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H_SS;C_rad_out_single;Cs_H_out_H/(NonDeC/Cs)] + [R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC] for rate rule\n[R3H_SS_Cs;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H_SS;C_rad_out_single;Cs_H_out_H/(NonDeC/Cs)] + [R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC] for rate rule
[R3H_SS_Cs;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 641,
    label = "CH3O + CH2O <=> CH3OH + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.294, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 642,
    label = "CH3OH <=> CH3 + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.084e+18, 's^-1'), n=-0.615, Ea=(92.541, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.5e+43, 'cm^3/(mol*s)'),
            n = -6.995,
            Ea = (97.992, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.4748,
        T3 = (35600, 'K'),
        T1 = (1120, 'K'),
        T2 = (9020, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 643,
    label = "CH3OH + H <=> CH3O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (199000, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (10.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 644,
    label = "CH3OH + OH <=> CH3O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.03, Ea=(-0.763, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 645,
    label = "CH3O + CH3O <=> CH2O + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 646,
    label = "CH3O2 + CH3O2 <=> O2 + CH2O + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.11e+14, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (-1.051, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 647,
    label = "CH3O2 + OH <=> O2 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 648,
    label = "nC5H12 + CH3O <=> CH3OH + C5H11_B",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 649,
    label = "nC5H12 + CH3O <=> CH3OH + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 650,
    label = "nC5H12 + CH3O <=> CH3OH + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+11, 'cm^3/(mol*s)'), n=0, Ea=(5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 651,
    label = "CH3O + H <=> CH3OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.44e+11, 'cm^3/(mol*s)'), n=0.76, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.7e+40, 'cm^6/(mol^2*s)'),
            n = -7.38,
            Ea = (9.177, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.684,
        T3 = (37000, 'K'),
        T1 = (41500, 'K'),
        T2 = (3980, 'K'),
        efficiencies = {'C=O': 2.5, '[C-]#[O+]': 1.5, 'CO': 3, 'O=C=O': 2, 'O': 6},
    ),
)

entry(
    index = 652,
    label = "CH3OH + HO2 <=> CH3O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0334, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (16.233, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 653,
    label = "O2 + CH3OH <=> CH3O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56.09, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O/H/NonDeC;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 654,
    label = "CH3O + C5H11_A <=> CH3OH + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 655,
    label = "CH3O + C5H11_A <=> CH3OH + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 656,
    label = "CH3O + C2H5 <=> CH3OH + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 657,
    label = "CH3O + NC3H7 <=> CH3OH + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 658,
    label = "CH3O + C5H11_C <=> CH3OH + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 659,
    label = "CH3O + C5H11_B <=> CH3OH + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 660,
    label = "CH3O + C2H4O <=> CH3OH + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.7902, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/OneDe;O_rad/NonDeC] for rate rule [C/H3/CO;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/OneDe;O_rad/NonDeC] for rate rule [C/H3/CO;O_rad/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 661,
    label = "CH3O + C2H4O <=> CH3OH + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000191, 'cm^3/(mol*s)'),
        n = 4.25,
        Ea = (0.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/Cs;O_sec_rad] for rate rule [CO/H/Cs;O_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/Cs;O_sec_rad] for rate rule [CO/H/Cs;O_rad/NonDeC]
""",
)

entry(
    index = 662,
    label = "CH3O + C3H7O <=> CH3OH + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 663,
    label = "CH3O + C2H5O <=> CH3OH + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 664,
    label = "CH3O + S20 <=> CH3OH + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 665,
    label = "CH3O + S45 <=> CH3OH + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 666,
    label = "CH3O + C3H5O_B <=> CH3OH + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 667,
    label = "CH3O + HCO <=> CH3OH + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 5 HCO + CH3O <=> CO + CH3OH in CO_Disproportionation/training',
    ),
    longDesc = 
u"""
Matched reaction 5 HCO + CH3O <=> CO + CH3OH in CO_Disproportionation/training
""",
)

entry(
    index = 668,
    label = "CH3O + S74 <=> CH3OH + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 669,
    label = "CH3O + HONO <=> CH3OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeN;O_rad] for rate rule [O/H/OneDeN;O_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeN;O_rad] for rate rule [O/H/OneDeN;O_rad/NonDeC]
""",
)

entry(
    index = 670,
    label = "CH3O + S27 <=> CH3OH + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 671,
    label = "CH3O + S76 <=> CH3OH + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 672,
    label = "CH3O + CH4O2 <=> CH3OH + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0567, 'cm^3/(mol*s)'),
        n = 3.855,
        Ea = (8.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;O_sec_rad] for rate rule [O/H/NonDeO;O_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/NonDeO;O_sec_rad] for rate rule [O/H/NonDeO;O_rad/NonDeC]
""",
)

entry(
    index = 673,
    label = "CH3O + S86 <=> CH3OH + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0567, 'cm^3/(mol*s)'),
        n = 3.855,
        Ea = (8.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;O_sec_rad] for rate rule [O/H/NonDeO;O_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/NonDeO;O_sec_rad] for rate rule [O/H/NonDeO;O_rad/NonDeC]
""",
)

entry(
    index = 674,
    label = "CH3O + S19 <=> CH3OH + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 675,
    label = "S31 <=> S41",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.034e+07, 's^-1'),
        n = 1.35,
        Ea = (20.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 676,
    label = "S31 <=> S83",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.034e+07, 's^-1'),
        n = 1.35,
        Ea = (20.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 677,
    label = "S41 <=> S83",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.177e+07, 's^-1'),
        n = 0.812,
        Ea = (9.505, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R5H_SSSS;C_rad_out_single;Cs_H_out_2H] + [R5H_SSSS;C_rad_out_2H;Cs_H_out] for rate rule\n[R5H_CCC;C_rad_out_2H;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [R5H_SSSS;C_rad_out_single;Cs_H_out_2H] + [R5H_SSSS;C_rad_out_2H;Cs_H_out] for rate rule
[R5H_CCC;C_rad_out_2H;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 678,
    label = "HOCHO + OH <=> H2O + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+06, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (0.916, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 679,
    label = "HOCHO + OH <=> H2O + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.85e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-0.962, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 680,
    label = "HOCHO + H <=> H2 + H + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+06, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4.868, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 681,
    label = "HOCHO + H <=> H2 + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (2.988, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 682,
    label = "HOCHO + HO2 <=> H2O2 + CO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(11.92, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 683,
    label = "OH + C2H4O <=> HOCHO + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+15, 'cm^3/(mol*s)'), n=-1.076, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 684,
    label = "CH2O + OH <=> HOCHO + H",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.66, -0.001757, -0.0003783, -5.476e-05],
            [-0.2872, 0.001532, 0.0003288, 4.73e-05],
            [-0.04114, -7.057e-05, -1.456e-05, -1.923e-06],
            [-0.0075, -4.959e-05, -1.07e-05, -1.558e-06],
            [-0.001545, -1.111e-05, -2.423e-06, -3.601e-07],
            [-0.0003643, -6.887e-07, -1.551e-07, -2.445e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 685,
    label = "HCO + OH <=> HOCHO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.92, 0.004002, -0.0007222, 7.641e-05],
            [-0.01307, 0.006794, -0.001201, 0.0001215],
            [-0.006905, 0.004555, -0.0007655, 6.868e-05],
            [-0.003823, 0.002569, -0.0003969, 2.812e-05],
            [-0.001946, 0.001261, -0.0001706, 6.943e-06],
            [-0.0009038, 0.0005466, -5.952e-05, -7.299e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 686,
    label = "H2O + CO <=> HOCHO",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-16.03, 0.002463, -0.0004429, 4.666e-05],
            [14.14, 0.004289, -0.0007587, 7.714e-05],
            [0.03192, 0.003041, -0.000517, 4.805e-05],
            [0.01788, 0.001838, -0.0002931, 2.314e-05],
            [0.004809, 0.0009777, -0.000142, 8.305e-06],
            [0.0007791, 0.0004681, -5.944e-05, 1.728e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 687,
    label = "HOCHO <=> H2 + CO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-13.62, 1.541e-05, -3.335e-06, 4.884e-07],
            [12.49, 2.68e-05, -5.802e-06, 8.494e-07],
            [-2.39e-05, 1.95e-05, -4.221e-06, 6.175e-07],
            [-1.522e-05, 1.241e-05, -2.685e-06, 3.924e-07],
            [-8.754e-06, 7.138e-06, -1.543e-06, 2.252e-07],
            [-4.652e-06, 3.792e-06, -8.189e-07, 1.193e-07],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 688,
    label = "NO2 + NO2 <=> N2O4",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.427, 0.3485, -0.002463, -0.0002002],
            [-0.9947, 0.03431, 0.001951, 0.0001293],
            [-0.107, -0.001197, -0.000136, 8.243e-06],
            [0.01232, -0.000736, -6.527e-05, -1.118e-05],
            [0.01138, 0.000213, -4.38e-05, -2.339e-06],
            [0.0023, 0.0002533, 3.667e-06, 6.519e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 689,
    label = "NO + S26 <=> S5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (26.904, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds;N3J] for rate rule [Cds-HH_Cds-CsH;N3dJ_O]\nEa raised from 108.6 to 112.6 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds;N3J] for rate rule [Cds-HH_Cds-CsH;N3dJ_O]
Ea raised from 108.6 to 112.6 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 690,
    label = "H + S52 <=> S45",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.72e+08, 'cm^3/(mol*s)'),
        n = 1.477,
        Ea = (1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-OsH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-OsH;HJ]
""",
)

entry(
    index = 691,
    label = "O2 + S45 <=> HO2 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.666e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 692,
    label = "HO2 + S45 <=> H2O2 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 693,
    label = "NO2 + S45 <=> HONO + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_sec_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 694,
    label = "C5H11_A + S45 <=> nC5H12 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 695,
    label = "C5H11_C + S45 <=> nC5H12 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 696,
    label = "C5H11_B + S45 <=> nC5H12 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 697,
    label = "OH + S45 <=> H2O + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 698,
    label = "CH3O2 + S45 <=> CH4O2 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 699,
    label = "CH3O + S45 <=> CH3OH + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 700,
    label = "H + S45 <=> H2 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 701,
    label = "S52 <=> S11",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.599, 0.0006958, -0.0001319, 1.524e-05],
            [9.605, 0.001325, -0.0002504, 2.879e-05],
            [0.1094, 0.001144, -0.0002143, 2.423e-05],
            [0.02053, 0.0008957, -0.0001653, 1.812e-05],
            [0.003929, 0.0006365, -0.0001146, 1.194e-05],
            [0.0005634, 0.0004096, -7.11e-05, 6.815e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 702,
    label = "S45 + S46 <=> S52 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 703,
    label = "C2H3O + S45 <=> C2H4O + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.009e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H2/CO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 704,
    label = "HCO + S45 <=> CH2O + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 705,
    label = "CH3CO + S45 <=> C2H4O + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 706,
    label = "NO + S52 <=> S50",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (18.166, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds_Cds;N3J] for rate rule [Cds-OsH_Cds-CsH;N3dJ_O]\nEa raised from 66.7 to 76.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds_Cds;N3J] for rate rule [Cds-OsH_Cds-CsH;N3dJ_O]
Ea raised from 66.7 to 76.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 707,
    label = "CH3O + NO2 <=> CH2O + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e+10, 'cm^3/(mol*s)'), n=0, Ea=(6.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 708,
    label = "CH2O + NO2 <=> HNO2 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.107, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (19.852, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 709,
    label = "HNO2 <=> HONO",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1, 10], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.1e+27, 's^-1'), n=-5.4, Ea=(52.539, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+29, 's^-1'), n=-5.47, Ea=(52.817, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2e+30, 's^-1'), n=-5.5, Ea=(53.691, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 710,
    label = "HNO2 + H <=> H2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 711,
    label = "HNO2 + OH <=> H2O + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.794, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 712,
    label = "HNO2 + C5H11_C <=> nC5H12 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]
""",
)

entry(
    index = 713,
    label = "HNO2 + C5H11_A <=> nC5H12 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]
""",
)

entry(
    index = 714,
    label = "HNO2 + C5H11_B <=> nC5H12 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H2/Cs]
""",
)

entry(
    index = 715,
    label = "HO2 + NO2 <=> O2 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Orad_O_H;Y_rad] for rate rule [Orad_O_H;N5d_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Orad_O_H;Y_rad] for rate rule [Orad_O_H;N5d_rad]
""",
)

entry(
    index = 716,
    label = "NO2 + C5H11_A <=> HNO2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 717,
    label = "NO2 + C5H11_A <=> HNO2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [N5d_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [N5d_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 718,
    label = "C2H5 + NO2 <=> C2H4 + HNO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [N5d_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [N5d_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 719,
    label = "NO2 + NC3H7 <=> HNO2 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 720,
    label = "NO2 + C5H11_C <=> HNO2 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.727e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 721,
    label = "NO2 + C5H11_B <=> HNO2 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 722,
    label = "HNO2 + C2H3O <=> NO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H2/CO]
""",
)

entry(
    index = 723,
    label = "HNO2 + CH3CO <=> NO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33e-06, 'cm^3/(mol*s)'),
        n = 5.09,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;CO_rad/Cs] for rate rule [N5d/H/NonDeOO;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;CO_rad/Cs] for rate rule [N5d/H/NonDeOO;CO_rad/Cs]
""",
)

entry(
    index = 724,
    label = "NO2 + C3H7O <=> HNO2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [N5d_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [N5d_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 725,
    label = "NO2 + C2H5O <=> HNO2 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [N5d_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [N5d_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 726,
    label = "S20 + NO2 <=> HNO2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [N5d_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [N5d_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 727,
    label = "NO2 + S45 <=> HNO2 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [N5d_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 728,
    label = "NO2 + S45 <=> HNO2 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [N5d_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [N5d_rad;O_Csrad]
""",
)

entry(
    index = 729,
    label = "NO2 + C3H5O_B <=> HNO2 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.954e+11, 'cm^3/(mol*s)'),
        n = 0.318,
        Ea = (-0.168, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cpri_Rrad] for rate rule [N5d_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cpri_Rrad] for rate rule [N5d_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 730,
    label = "NO2 + HCO <=> HNO2 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.43e+15, 'cm^3/(mol*s)'),
        n = -0.548,
        Ea = (0.393, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;HCO] for rate rule [N5d_rad;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;HCO] for rate rule [N5d_rad;HCO]
""",
)

entry(
    index = 731,
    label = "HO2 + HNO2 <=> H2O2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.79, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;O_rad/NonDeO]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;O_rad/NonDeO]
""",
)

entry(
    index = 732,
    label = "NO2 + S74 <=> HNO2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [N5d_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [N5d_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 733,
    label = "NO2 + HNO2 <=> HONO + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (197800, 'cm^3/(mol*s)'),
        n = 2.363,
        Ea = (1.787, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;O_rad/OneDeN] + [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;O_rad/OneDeN]',
    ),
    longDesc = 
u"""
Estimated using average of templates [X_H;O_rad/OneDeN] + [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;O_rad/OneDeN]
""",
)

entry(
    index = 734,
    label = "NO2 + S27 <=> HNO2 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [N5d_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [N5d_rad;O_Csrad]
""",
)

entry(
    index = 735,
    label = "NO2 + S76 <=> HNO2 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [N5d_rad;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [N5d_rad;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 736,
    label = "CH3O2 + HNO2 <=> CH4O2 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177, 'cm^3/(mol*s)'),
        n = 3.068,
        Ea = (3.266, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;OOC] + [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;OOC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [X_H;OOC] + [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;OOC]
""",
)

entry(
    index = 737,
    label = "HNO2 + S46 <=> NO2 + S86",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (177, 'cm^3/(mol*s)'),
        n = 3.068,
        Ea = (3.266, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;OOC] + [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;OOC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [X_H;OOC] + [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;OOC]
""",
)

entry(
    index = 738,
    label = "NO2 + S19 <=> HNO2 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [N5d_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [N5d_rad;O_Csrad]
""",
)

entry(
    index = 739,
    label = "CH3O + HNO2 <=> CH3OH + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.79, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;O_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;O_rad] for rate rule [N5d/H/NonDeOO;O_rad/NonDeC]
""",
)

entry(
    index = 740,
    label = "NO2 + H <=> HNO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.12, 0.1952, -0.008943, -0.0001367],
            [-0.4659, 0.05708, 0.001087, -6.118e-05],
            [-0.1174, 0.007484, 0.0004696, 2.726e-05],
            [-0.02925, 0.0008686, 0.0001344, 3.375e-06],
            [-0.007325, 0.0001451, 2.846e-05, -4.221e-07],
            [-0.001953, 9.58e-05, -3.744e-06, 8.631e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 741,
    label = "HO2 + C2H4O <=> S68",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.042, 0.0747, -0.005613, 0.0001001],
            [0.2559, 0.1021, -0.005591, -0.0001479],
            [-0.01388, 0.03776, -0.0003102, -0.0001959],
            [-0.01245, 0.005012, 0.0007652, -3.809e-05],
            [0.002079, -0.00213, 0.000239, 2.842e-05],
            [0.003712, -0.001087, -6.955e-05, 1.311e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 742,
    label = "C3H6 + OH <=> H + C3H6O_B",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.013, 0.025, 0.1, 0.132, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.47e+06, 'cm^3/(mol*s)'),
                n = 1.53,
                Ea = (4.288, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.08e+07, 'cm^3/(mol*s)'),
                n = 1.34,
                Ea = (4.576, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.76e+06, 'cm^3/(mol*s)'),
                n = 1.33,
                Ea = (4.589, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.14e+06, 'cm^3/(mol*s)'),
                n = 1.36,
                Ea = (4.594, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (313000, 'cm^3/(mol*s)'),
                n = 1.69,
                Ea = (4.603, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (139000, 'cm^3/(mol*s)'),
                n = 1.8,
                Ea = (4.603, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(103, 'cm^3/(mol*s)'), n=2.83, Ea=(4.53, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(0.034, 'cm^3/(mol*s)'), n=3.89, Ea=(4.39, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.46e-06, 'cm^3/(mol*s)'),
                n = 5.03,
                Ea = (4.132, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 743,
    label = "O2 + C3H6O_B <=> HO2 + C3H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(39.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 744,
    label = "OH + C3H6O_B <=> H2O + C3H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.1e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.298, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 745,
    label = "H + C3H6O_B <=> H2 + C3H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (173000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2.492, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 746,
    label = "HO2 + C3H6O_B <=> H2O2 + C3H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 747,
    label = "CH3O2 + C3H6O_B <=> CH4O2 + C3H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600, 'cm^3/(mol*s)'), n=2.6, Ea=(13.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 748,
    label = "CH3O + C3H6O_B <=> CH3OH + C3H4O + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(2.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 749,
    label = "HO2 + C3H6O_B <=> HO2 + C3H6O_A",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (149000, 'cm^3/(mol*s)'),
        n = 1.67,
        Ea = (6.81, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 750,
    label = "HOCHO + C3H6O_B <=> HOCHO + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0281, 'cm^3/(mol*s)'),
        n = 3.286,
        Ea = (-4.509, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 751,
    label = "C3H6O_B <=> C3H6O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-13.81, 0.0002175, -4.439e-05, 5.834e-06],
            [14.47, 0.0004112, -8.377e-05, 1.097e-05],
            [0.01147, 0.0003492, -7.077e-05, 9.179e-06],
            [0.001991, 0.0002691, -5.407e-05, 6.894e-06],
            [0.0002706, 0.0001903, -3.775e-05, 4.694e-06],
            [-4.004e-05, 0.0001247, -2.431e-05, 2.918e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 752,
    label = "HO2 + C3H6O_A <=> HO2 + C3H6O_B",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [1.473, -0.1353, -0.01491, -0.0003457],
            [4.804, 0.1008, 0.006023, -0.0007028],
            [0.0904, -0.007641, 0.001496, 0.000281],
            [0.009392, -0.008384, -0.0008643, 6.59e-05],
            [0.004328, 0.0002018, -0.0002991, -4.993e-05],
            [0.001161, 0.001164, 0.0001182, -1.274e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 753,
    label = "C3H6O_A + H <=> H2 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(4.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 754,
    label = "C3H6O_A + OH <=> H2O + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+10, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-0.34, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 755,
    label = "HO2 + C3H6O_A <=> H2O2 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 756,
    label = "CH3O + C3H6O_A <=> CH3OH + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(3.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 757,
    label = "CH3O2 + C3H6O_A <=> CH4O2 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 758,
    label = "O2 + C3H6O_A <=> HO2 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.005e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 759,
    label = "HONO + C3H5O_A <=> NO2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33e-06, 'cm^3/(mol*s)'),
        n = 5.09,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;CO_rad/Cs] for rate rule [O/H/OneDeN;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;CO_rad/Cs] for rate rule [O/H/OneDeN;CO_rad/Cs]
""",
)

entry(
    index = 760,
    label = "HNO2 + C3H5O_A <=> NO2 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33e-06, 'cm^3/(mol*s)'),
        n = 5.09,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;CO_rad/Cs] for rate rule [N5d/H/NonDeOO;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;CO_rad/Cs] for rate rule [N5d/H/NonDeOO;CO_rad/Cs]
""",
)

entry(
    index = 761,
    label = "C5H11_A + C3H6O_A <=> nC5H12 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 762,
    label = "C5H11_C + C3H6O_A <=> nC5H12 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 763,
    label = "C5H11_B + C3H6O_A <=> nC5H12 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 764,
    label = "C5H11_A + C3H5O_A <=> C5H10_A + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 765,
    label = "C5H11_C + C3H5O_A <=> C5H10_A + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.727e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 766,
    label = "C3H5O_A + C2H5O <=> C3H6O_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 767,
    label = "NC3H7 + C3H5O_A <=> C3H6 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 768,
    label = "C2H5 + C3H5O_A <=> C2H4 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 769,
    label = "CH3O + C3H5O_A <=> CH2O + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [CO_rad/NonDe;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [CO_rad/NonDe;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 770,
    label = "C3H7O + C3H5O_A <=> C3H6O_A + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 771,
    label = "C3H5O_A + H <=> C3H6O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.83, 5.788e-05, -1.202e-05, 1.633e-06],
            [-0.03416, 0.0001097, -2.275e-05, 3.084e-06],
            [-0.005114, 9.374e-05, -1.938e-05, 2.61e-06],
            [-0.00107, 7.296e-05, -1.5e-05, 1.998e-06],
            [-0.0002816, 5.225e-05, -1.065e-05, 1.397e-06],
            [-9.478e-05, 3.474e-05, -7.003e-06, 8.991e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 772,
    label = "C3H5O_A + S27 <=> C3H6O_A + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 773,
    label = "S20 + C3H5O_A <=> C3H6O_A + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.442e+11, 'cm^3/(mol*s)'),
        n = 0.279,
        Ea = (-0.094, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 774,
    label = "C3H5O_A + S45 <=> C3H6O_A + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 775,
    label = "C3H5O_A + C3H5O_B <=> C3H4O + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.196e+13, 'cm^3/(mol*s)'),
        n = 0.159,
        Ea = (-0.084, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cpri_Rrad] + [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cpri_Rrad] + [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 776,
    label = "C3H5O_A + S86 <=> C3H6O_A + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.33e-06, 'cm^3/(mol*s)'),
        n = 5.09,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;CO_rad/Cs]
""",
)

entry(
    index = 777,
    label = "C3H6O_A + C2H3O <=> C3H5O_A + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/CO]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/CO]
""",
)

entry(
    index = 778,
    label = "CH2O + C3H5O_A <=> HCO + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri;CO_rad/NonDe] for rate rule [CO_pri;CO_rad/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri;CO_rad/NonDe] for rate rule [CO_pri;CO_rad/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 779,
    label = "C3H5O_A + C2H4O <=> C3H6O_A + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_H;CO_rad/NonDe] for rate rule [CO/H/Cs;CO_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [CO_H;CO_rad/NonDe] for rate rule [CO/H/Cs;CO_rad/Cs]
""",
)

entry(
    index = 780,
    label = "C5H11_B + C3H5O_A <=> S26 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 781,
    label = "C5H11_A + C3H5O_A <=> S26 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 782,
    label = "C3H5O_A + S76 <=> CH3CN + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 783,
    label = "C3H5O_A + S74 <=> C3H6O_A + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.668e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 784,
    label = "C3H5O_A + S19 <=> C3H6O_A + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 785,
    label = "C3H5O_A + S45 <=> C3H6O_A + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.363e+11, 'cm^3/(mol*s)'),
        n = 0.419,
        Ea = (0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 786,
    label = "C2H5 + CO <=> C3H5O_A",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.317, 0.1878, -0.00892, -4.974e-05],
            [0.6345, 0.1356, 0.001365, -0.0003937],
            [-0.1588, 0.0125, 0.002061, 6.676e-05],
            [-0.01198, -0.004029, 4.583e-05, 4.653e-05],
            [0.008201, -0.001185, -0.0001505, -7.739e-06],
            [0.003616, 0.0001305, -1.663e-05, -5.463e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 787,
    label = "HCO + C3H5O_A <=> CO + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;HCO] for rate rule [CO_rad/NonDe;HCO]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;HCO] for rate rule [CO_rad/NonDe;HCO]
""",
)

entry(
    index = 788,
    label = "NO2 + C3H5O_E <=> S33",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [14.23, -1.325e-15, 1.665e-16, -5.725e-16],
            [-0.3806, -1.11e-15, -2.22e-16, 6.245e-17],
            [-0.1162, 3.469e-17, 9.298e-16, -2.463e-16],
            [-0.04354, 8.465e-16, -3.331e-16, 8.5e-17],
            [-0.01687, 8.57e-16, 6.661e-16, -5.967e-16],
            [-0.006057, -6.523e-16, -6.037e-16, 8.674e-17],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 789,
    label = "NO2 + C3H5O_E <=> S2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.809, 0.3891, -8.882e-16, -4.996e-16],
            [-0.7399, -3.664e-15, -2.151e-16, -3.608e-16],
            [-0.1695, 1.24e-15, 1.416e-15, -6.939e-16],
            [-0.08983, -2.22e-16, -9.68e-16, -2.498e-16],
            [-0.05134, 1.207e-15, 1.929e-15, -2.776e-17],
            [-0.02744, -9.159e-16, -2.123e-15, -1.166e-15],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 790,
    label = "S2 <=> S33",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.063, 0.3876, -0.0002981, -3.962e-05],
            [0.7806, 0.001635, 0.0003403, 4.588e-05],
            [-0.01528, -0.0002412, -5.003e-05, -6.71e-06],
            [-0.01629, 3.314e-05, 5.543e-06, 3.66e-07],
            [-0.02157, -9.748e-06, -2.388e-06, -4.167e-07],
            [-0.01718, -9.794e-06, -2.11e-06, -2.988e-07],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 791,
    label = "NO2 + S26 <=> S29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (603100, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (8.02, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-HH;YJ] for rate rule [Cds-CsH_Cds-HH;NJ]\nEa raised from 28.7 to 33.6 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-HH;YJ] for rate rule [Cds-CsH_Cds-HH;NJ]
Ea raised from 28.7 to 33.6 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 792,
    label = "NO2 + S52 <=> S14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.72e+08, 'cm^3/(mol*s)'),
        n = 1.477,
        Ea = (8.148, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-OsH;YJ] for rate rule [Cds-CsH_Cds-OsH;NJ]\nEa raised from 31.6 to 34.1 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-OsH;YJ] for rate rule [Cds-CsH_Cds-OsH;NJ]
Ea raised from 31.6 to 34.1 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 793,
    label = "NO2 + C3H5O_E <=> NO + S88",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.68, -0.04692, -0.007539, -0.0005828],
            [0.1343, 0.04913, 0.007136, 0.000381],
            [-0.006371, -0.009102, -0.0008077, 7.026e-05],
            [-0.001799, -0.001742, -0.0004372, -5.612e-05],
            [9.691e-05, 0.0007636, 8.876e-05, -3.837e-06],
            [-0.0001712, 0.0002862, 6.409e-05, 7.924e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 794,
    label = "C5H10_A + N2O3_C <=> S115",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.08e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.601, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [o_atom_singlet;mb_db_twocdisub_Nd]\nMultiplied by reaction path degeneracy 2\nEa raised from 0.0 to 52.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Exact match found for rate rule [o_atom_singlet;mb_db_twocdisub_Nd]
Multiplied by reaction path degeneracy 2
Ea raised from 0.0 to 52.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 795,
    label = "NO2 + C5H10_A <=> S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30950, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (8.111, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-CsH;YJ] for rate rule [Cds-CsH_Cds-CsH;NJ]\nEa raised from 28.7 to 33.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-CsH;YJ] for rate rule [Cds-CsH_Cds-CsH;NJ]
Ea raised from 28.7 to 33.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 796,
    label = "S29 <=> S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.307e+07, 's^-1'),
        n = 1.53,
        Ea = (34.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H_SS;C_rad_out_single;Cs_H_out_H/(NonDeC/Cs)] + [R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC] for rate rule\n[R3H_SS_Cs;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H_SS;C_rad_out_single;Cs_H_out_H/(NonDeC/Cs)] + [R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC] for rate rule
[R3H_SS_Cs;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 797,
    label = "NO2 + C5H10_A <=> S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30950, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (8.111, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-CsH;YJ] for rate rule [Cds-CsH_Cds-CsH;NJ]\nEa raised from 28.7 to 33.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-CsH;YJ] for rate rule [Cds-CsH_Cds-CsH;NJ]
Ea raised from 28.7 to 33.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 798,
    label = "S26 + N2O3_C <=> S65",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.974, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [o_atom_singlet;mb_db]\nMultiplied by reaction path degeneracy 2\nEa raised from 49.5 to 54.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [o_atom_singlet;mb_db]
Multiplied by reaction path degeneracy 2
Ea raised from 49.5 to 54.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 799,
    label = "S78 <=> C3H6 + N2O3_C",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.547, 0.1629, -0.01835, 0.0003041],
            [-0.1032, 0.02902, -0.001684, -0.0002803],
            [-0.05629, -0.01159, 4.937e-05, 0.0001405],
            [-0.01053, -0.00364, -0.0001397, 5.579e-05],
            [-0.002812, -0.0007136, 8.296e-06, 1.269e-05],
            [-0.0008625, -0.0001843, 2.341e-05, 4.547e-06],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 800,
    label = "ONONO2 <=> NO2 + NO2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.108, 0.389, -9.134e-06, -1.34e-06],
            [1.271, -3.203e-06, -6.875e-07, -9.891e-08],
            [-0.05183, -9.432e-06, -2.04e-06, -2.979e-07],
            [0.002604, 1.95e-06, 4.242e-07, 6.271e-08],
            [0.01385, -3.082e-06, -6.677e-07, -9.793e-08],
            [-0.01166, 5.69e-06, 1.231e-06, 1.8e-07],
        ],
        kunits = 's^-1',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 801,
    label = "NO2 + C5H10_A <=> S95",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46.2, 'cm^3/(mol*s)'),
        n = 3.09,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-CsH;OJ_sec] for rate rule [Cds-CsH_Cds-CsH;OJ-NO]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-CsH;OJ_sec] for rate rule [Cds-CsH_Cds-CsH;OJ-NO]
""",
)

entry(
    index = 802,
    label = "S49 <=> S95",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.76e+14, 's^-1'),
        n = 0,
        Ea = (67, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [RNO2]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [RNO2]
""",
)

entry(
    index = 803,
    label = "NO2 + C5H10_A <=> S21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46.2, 'cm^3/(mol*s)'),
        n = 3.09,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-CsH;OJ_sec] for rate rule [Cds-CsH_Cds-CsH;OJ-NO]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-CsH;OJ_sec] for rate rule [Cds-CsH_Cds-CsH;OJ-NO]
""",
)

entry(
    index = 804,
    label = "S40 <=> S21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.76e+14, 's^-1'),
        n = 0,
        Ea = (67, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [RNO2]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [RNO2]
""",
)

entry(
    index = 805,
    label = "C3H6 + S38 <=> S55",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (1.658, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds_Cds;N3sJ] for rate rule [Cds-CsH_Cds-HH;N3sJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds_Cds;N3sJ] for rate rule [Cds-CsH_Cds-HH;N3sJ]
""",
)

entry(
    index = 806,
    label = "NO2 + S26 <=> S48",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (791, 'cm^3/(mol*s)'),
        n = 2.78,
        Ea = (9.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-CsH;OJ_sec] for rate rule [Cds-HH_Cds-CsH;OJ-NO]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-CsH;OJ_sec] for rate rule [Cds-HH_Cds-CsH;OJ-NO]
""",
)

entry(
    index = 807,
    label = "S81 <=> S48",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.76e+14, 's^-1'),
        n = 0,
        Ea = (67, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [RNO2]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [RNO2]
""",
)

entry(
    index = 808,
    label = "C3H6 + S38 <=> S9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.228e+09, 'cm^3/(mol*s)'),
        n = 2.756,
        Ea = (1.658, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds;N3sJ] for rate rule [Cds-HH_Cds-Cs\\H3/H;N3sJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds;N3sJ] for rate rule [Cds-HH_Cds-Cs\H3/H;N3sJ]
""",
)

entry(
    index = 809,
    label = "C2H5 + NO2 <=> C2H4 + HONO",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [3.372, -0.0004911, -0.0001062, -1.553e-05],
            [3.166, 0.0005564, 0.0001203, 1.756e-05],
            [0.2714, -8.662e-05, -1.864e-05, -2.697e-06],
            [0.05767, -6.849e-06, -1.508e-06, -2.28e-07],
            [0.01138, -1.208e-06, -2.614e-07, -3.82e-08],
            [0.002212, 1.72e-07, 3.701e-08, 5.353e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 810,
    label = "C2H5 + NO2 <=> NO + C2H5O",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.88, -0.002102, -0.000451, -6.489e-05],
            [0.002674, 0.002291, 0.0004903, 7.01e-05],
            [-0.0004454, -0.0002788, -5.824e-05, -7.918e-06],
            [-9.495e-05, -3.298e-05, -7.432e-06, -1.17e-06],
            [-4.279e-05, -1.222e-05, -2.633e-06, -3.821e-07],
            [-1.418e-05, -1.163e-06, -2.602e-07, -4.048e-08],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (298, 'K'),
        Tmax = (1000, 'K'),
        Pmin = (0.493, 'atm'),
        Pmax = (2.961, 'atm'),
    ),
)

entry(
    index = 811,
    label = "NO2 + C5H11_A <=> S84",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.316e+18, 'cm^3/(mol*s)'),
        n = -1.37,
        Ea = (0.278, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d-OdOs;Cs_rad] for rate rule [N5d-OdOs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d-OdOs;Cs_rad] for rate rule [N5d-OdOs;C_rad/H/NonDeC]
""",
)

entry(
    index = 812,
    label = "nC5H12 + S29 <=> S84 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00184, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 813,
    label = "nC5H12 + S29 <=> S84 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00368, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 814,
    label = "S84 + C5H11_B <=> nC5H12 + S29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00276, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cs;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cs;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 815,
    label = "O2 + S84 <=> HO2 + S29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51.997, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cs;O2b]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cs;O2b]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 816,
    label = "C5H11_A + S29 <=> S84 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 817,
    label = "C5H11_A + S29 <=> S84 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 818,
    label = "C2H5 + S29 <=> S84 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 819,
    label = "NC3H7 + S29 <=> S84 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 820,
    label = "C5H11_C + S29 <=> S84 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 821,
    label = "C5H11_B + S29 <=> S84 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 822,
    label = "S84 + OH <=> H2O + S29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.431e+09, 'cm^3/(mol*s)'),
        n = 1.152,
        Ea = (2.68, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cs;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cs;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 823,
    label = "C2H4O + S29 <=> S84 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0006331, 'cm^3/(mol*s)'),
        n = 4.436,
        Ea = (5.225, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/OneDe;C_rad/H2/Cs] for rate rule [C/H3/CO;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/OneDe;C_rad/H2/Cs] for rate rule [C/H3/CO;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 824,
    label = "C2H4O + S29 <=> S84 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 825,
    label = "C3H7O + S29 <=> S84 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 826,
    label = "CH2O + S29 <=> S84 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5500, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 827,
    label = "C2H5O + S29 <=> S84 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 828,
    label = "CH3O + S29 <=> S84 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 829,
    label = "C3H6O_A + S29 <=> S84 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 830,
    label = "S20 + S29 <=> S84 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;C/H2/Nd_Rrad] for rate rule [C_rad/H2/Cs;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 831,
    label = "H + S29 <=> S84",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C_rad/H2/Cs]
""",
)

entry(
    index = 832,
    label = "S45 + S29 <=> S84 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 833,
    label = "S45 + S29 <=> S84 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 834,
    label = "C3H5O_B + S29 <=> S84 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 835,
    label = "S84 + H <=> H2 + S29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3090, 'cm^3/(mol*s)'),
        n = 3.24,
        Ea = (7.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cs;H_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cs;H_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 836,
    label = "HCO + S29 <=> S84 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H2/Cs;HCO from training reaction 8\nExact match found for rate rule [C_rad/H2/Cs;HCO]',
    ),
    longDesc = 
u"""
C_rad/H2/Cs;HCO from training reaction 8
Exact match found for rate rule [C_rad/H2/Cs;HCO]
""",
)

entry(
    index = 837,
    label = "H2O2 + S29 <=> S84 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3, 'cm^3/(mol*s)'),
        n = 3.28,
        Ea = (1.05, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 838,
    label = "S74 + S29 <=> S84 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 839,
    label = "HONO + S29 <=> S84 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.245,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeN;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeN;C_rad/H2/Cs]
""",
)

entry(
    index = 840,
    label = "S27 + S29 <=> S84 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 841,
    label = "S29 + S76 <=> S84 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 842,
    label = "CH4O2 + S29 <=> S84 + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002046, 'cm^3/(mol*s)'),
        n = 4.189,
        Ea = (-1.293, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]
""",
)

entry(
    index = 843,
    label = "S86 + S29 <=> S84 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002046, 'cm^3/(mol*s)'),
        n = 4.189,
        Ea = (-1.293, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]
""",
)

entry(
    index = 844,
    label = "S19 + S29 <=> S84 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 845,
    label = "CH3OH + S29 <=> S84 + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (8.94, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O/H/NonDeC;C_rad/H2/Cs]
""",
)

entry(
    index = 846,
    label = "HNO2 + S29 <=> S84 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H2/Cs]
""",
)

entry(
    index = 847,
    label = "nC5H12 + S40 <=> S84 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00173, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 848,
    label = "nC5H12 + S40 <=> S84 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00346, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 849,
    label = "S84 + C5H11_B <=> nC5H12 + S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00184, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 850,
    label = "O2 + S84 <=> HO2 + S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49.347, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O2b]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O2b]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 851,
    label = "C5H11_A + S40 <=> S84 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 852,
    label = "C5H11_A + S40 <=> S84 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 853,
    label = "C2H5 + S40 <=> S84 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 854,
    label = "NC3H7 + S40 <=> S84 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 855,
    label = "C5H11_C + S40 <=> S84 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.052e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 856,
    label = "C5H11_B + S40 <=> S84 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 857,
    label = "S84 + OH <=> H2O + S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (0.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 858,
    label = "C2H4O + S40 <=> S84 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001133, 'cm^3/(mol*s)'),
        n = 4.29,
        Ea = (6.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/OneDe;C_rad/H/NonDeC] for rate rule [C/H3/CO;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/OneDe;C_rad/H/NonDeC] for rate rule [C/H3/CO;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 859,
    label = "C2H4O + S40 <=> S84 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 860,
    label = "C3H7O + S40 <=> S84 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 861,
    label = "CH2O + S40 <=> S84 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.96, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 862,
    label = "C2H5O + S40 <=> S84 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 863,
    label = "CH3O + S40 <=> S84 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 864,
    label = "C3H6O_A + S40 <=> S84 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 865,
    label = "S20 + S40 <=> S84 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 866,
    label = "H + S40 <=> S84",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C_rad/H/NonDeC]
""",
)

entry(
    index = 867,
    label = "S40 + S45 <=> S84 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 868,
    label = "S40 + S45 <=> S84 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 869,
    label = "C3H5O_B + S40 <=> S84 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 870,
    label = "S84 + H <=> H2 + S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.678, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;H_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;H_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 871,
    label = "HCO + S40 <=> S84 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/NonDeC;HCO from training reaction 9\nExact match found for rate rule [C_rad/H/NonDeC;HCO]',
    ),
    longDesc = 
u"""
C_rad/H/NonDeC;HCO from training reaction 9
Exact match found for rate rule [C_rad/H/NonDeC;HCO]
""",
)

entry(
    index = 872,
    label = "H2O2 + S40 <=> S84 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e-07, 'cm^3/(mol*s)'),
        n = 5.407,
        Ea = (0.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 873,
    label = "S40 + S74 <=> S84 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 874,
    label = "HONO + S40 <=> S84 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93.4, 'cm^3/(mol*s)'),
        n = 2.872,
        Ea = (3.661, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]
""",
)

entry(
    index = 875,
    label = "S40 + S27 <=> S84 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 876,
    label = "S40 + S76 <=> S84 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 877,
    label = "CH4O2 + S40 <=> S84 + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.979e-06, 'cm^3/(mol*s)'),
        n = 4.886,
        Ea = (-2.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]
""",
)

entry(
    index = 878,
    label = "S40 + S86 <=> S84 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.979e-06, 'cm^3/(mol*s)'),
        n = 4.886,
        Ea = (-2.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]
""",
)

entry(
    index = 879,
    label = "S40 + S19 <=> S84 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 880,
    label = "S84 + CH3O <=> CH3OH + S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.57, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_rad/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 881,
    label = "HNO2 + S40 <=> S84 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]
""",
)

entry(
    index = 882,
    label = "S84 + S29 <=> S84 + S40",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00184, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 883,
    label = "NO2 + C5H11_C <=> S6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.316e+18, 'cm^3/(mol*s)'),
        n = -1.37,
        Ea = (0.278, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d-OdOs;Cs_rad] for rate rule [N5d-OdOs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d-OdOs;Cs_rad] for rate rule [N5d-OdOs;C_rad/H/NonDeC]
""",
)

entry(
    index = 884,
    label = "nC5H12 + S49 <=> S6 + C5H11_C",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00173, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 885,
    label = "nC5H12 + S49 <=> S6 + C5H11_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00346, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 886,
    label = "S6 + C5H11_B <=> nC5H12 + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00368, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 887,
    label = "O2 + S6 <=> HO2 + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.588e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49.347, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O2b]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O2b]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 888,
    label = "C5H11_A + S49 <=> S6 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 889,
    label = "C5H11_A + S49 <=> S6 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 890,
    label = "C2H5 + S49 <=> S6 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 891,
    label = "NC3H7 + S49 <=> S6 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 892,
    label = "C5H11_C + S49 <=> S6 + C5H10_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.052e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 893,
    label = "C5H11_B + S49 <=> S6 + S26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 894,
    label = "S6 + OH <=> H2O + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (0.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 895,
    label = "C2H4O + S49 <=> S6 + C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001133, 'cm^3/(mol*s)'),
        n = 4.29,
        Ea = (6.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/OneDe;C_rad/H/NonDeC] for rate rule [C/H3/CO;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/OneDe;C_rad/H/NonDeC] for rate rule [C/H3/CO;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 896,
    label = "C2H4O + S49 <=> S6 + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 897,
    label = "C3H7O + S49 <=> S6 + C3H6O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 898,
    label = "CH2O + S49 <=> S6 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.96, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO_pri;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 899,
    label = "C2H5O + S49 <=> S6 + C2H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 900,
    label = "CH3O + S49 <=> S6 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cmethyl_Rrad] for rate rule [C_rad/H/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 901,
    label = "C3H6O_A + S49 <=> S6 + C3H5O_A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000194, 'cm^3/(mol*s)'),
        n = 4.68,
        Ea = (6.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_sec_rad] for rate rule [CO/H/Cs;C_rad/H/NonDeC]
""",
)

entry(
    index = 902,
    label = "S20 + S49 <=> S6 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;C/H2/Nd_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 903,
    label = "H + S49 <=> S6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C_rad/H/NonDeC]
""",
)

entry(
    index = 904,
    label = "S49 + S45 <=> S6 + S52",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 905,
    label = "S49 + S45 <=> S6 + S11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 906,
    label = "C3H5O_B + S49 <=> S6 + C3H4O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;Cpri_Rrad] for rate rule [C_rad/H/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 907,
    label = "S6 + H <=> H2 + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.356, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (3.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;H_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;H_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 908,
    label = "HCO + S49 <=> S6 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/NonDeC;HCO from training reaction 9\nExact match found for rate rule [C_rad/H/NonDeC;HCO]',
    ),
    longDesc = 
u"""
C_rad/H/NonDeC;HCO from training reaction 9
Exact match found for rate rule [C_rad/H/NonDeC;HCO]
""",
)

entry(
    index = 909,
    label = "H2O2 + S49 <=> S6 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e-07, 'cm^3/(mol*s)'),
        n = 5.407,
        Ea = (0.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 910,
    label = "S49 + S74 <=> S6 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 911,
    label = "HONO + S49 <=> S6 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93.4, 'cm^3/(mol*s)'),
        n = 2.872,
        Ea = (3.661, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeN;Cs_rad] for rate rule [O/H/OneDeN;C_rad/H/NonDeC]
""",
)

entry(
    index = 912,
    label = "S49 + S27 <=> S6 + S87",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 913,
    label = "S49 + S76 <=> S6 + CH3CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/NonDeC;Cds/H/NonDe_d_Rrad]
""",
)

entry(
    index = 914,
    label = "CH4O2 + S49 <=> S6 + CH3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.979e-06, 'cm^3/(mol*s)'),
        n = 4.886,
        Ea = (-2.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]
""",
)

entry(
    index = 915,
    label = "S49 + S86 <=> S6 + S46",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.979e-06, 'cm^3/(mol*s)'),
        n = 4.886,
        Ea = (-2.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H/NonDeC]
""",
)

entry(
    index = 916,
    label = "S49 + S19 <=> S6 + S22",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;O_Csrad]
""",
)

entry(
    index = 917,
    label = "S6 + CH3O <=> CH3OH + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.57, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_rad/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 918,
    label = "HNO2 + S49 <=> S6 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (810000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (4.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [N5d/H/NonDeOO;Cs_rad] for rate rule [N5d/H/NonDeOO;C_rad/H/NonDeC]
""",
)

entry(
    index = 919,
    label = "S6 + S40 <=> S84 + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00346, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 920,
    label = "S6 + S29 <=> S84 + S49",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00368, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 4
""",
)

