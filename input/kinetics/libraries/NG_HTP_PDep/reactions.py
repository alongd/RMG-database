#!/usr/bin/env python
# encoding: utf-8

name = "NG_HTP_PDep"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 5,
    label = "H2_13_(2) <=> H_10_(3) + H_10_(3)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104.38, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0, '[C-]#[O+]': 1.9, '[Ar]': 0},
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 8,
    label = "O_11_(7) + O_11_(7) <=> O2_2_(13)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0, '[C-]#[O+]': 1.9, '[Ar]': 0},
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 11,
    label = "H_10_(3) + O_11_(7) <=> OH_12_(12)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.714e+18, 'cm^6/(mol^2*s)'),
            n = -1,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C-]#[O+]': 1.9, '[Ar]': 0.75},
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 12,
    label = "H2O_14_(6) <=> H_10_(3) + OH_12_(12)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.064e+27, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120.79, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 0, '[H][H]': 3, '[He]': 1.1, '[O][O]': 1.5, 'N#N': 2, '[C-]#[O+]': 1.9},
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 14,
    label = "H_10_(3) + O2_2_(13) <=> HO2_17_(5)",
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
        efficiencies = {'O=C=O': 3.8, 'O': 14, '[H][H]': 2, '[He]': 0.8, '[O][O]': 0.78, '[C-]#[O+]': 1.9, '[Ar]': 0.67},
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 20,
    label = "H2O2(15) <=> OH_12_(12) + OH_12_(12)",
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
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.5, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2, 'N#N': 1.5, '[C-]#[O+]': 2.8},
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 25,
    label = "H_10_(3) + HO2_17_(5) <=> H2O2(15)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.83, 0.8492, -0.181, 0.005425],
            [-0.6545, 0.5213, 0.01323, -0.02505],
            [-0.2353, 0.1171, 0.02973, -0.0009301],
            [-0.08189, 0.02258, 0.009526, 0.00232],
            [-0.02796, 0.00356, 0.001958, 0.0008424],
            [-0.009349, 0.0003293, 0.0002616, 0.0001435],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 27,
    label = "O_11_(7) + OH_12_(12) <=> HO2_17_(5)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.48, 1.791, -0.08651, -0.01675],
            [-0.7192, 0.1296, 0.05019, 0.007163],
            [-0.1666, 0.00969, 0.004234, 0.001213],
            [-0.04541, -0.00294, 0.001269, 0.0009795],
            [-0.01725, 0.004478, -0.000626, -0.0007378],
            [-0.001863, -0.00203, 0.0002147, 0.0003309],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 28,
    label = "O_11_(7) + CO_21_(14) <=> CO2_5_(8)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.88e+11, 'cm^3/(mol*s)'), n=0, Ea=(2.43, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+21, 'cm^6/(mol^2*s)'),
            n = -2.1,
            Ea = (5.5, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, 'C=O': 2.5, '[He]': 2.5, '[C-]#[O+]': 1.9, '[Ar]': 0.87},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 33,
    label = "C3H7(35) + C3H7(35) <=> C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 34,
    label = "H_10_(3) + CH3(17) <=> Cadd(4)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.801e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.93e+24, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.124,
        T3 = (1800, 'K'),
        T1 = (33.1, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 3.42, 'C=O': 2.5, '[He]': 0.42, '[O][O]': 0.59, 'N#N': 0.59, '[C-]#[O+]': 0.89, '[Ar]': 0.36},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 37,
    label = "CH3(17) + CH3(17) <=> CCadd(1)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.844e+16, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (0.62, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.77e+50, 'cm^6/(mol^2*s)'),
            n = -9.67,
            Ea = (6.22, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5325,
        T3 = (151, 'K'),
        T1 = (1040, 'K'),
        T2 = (4970, 'K'),
        efficiencies = {'C': 1.99, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[O][O]': 1, '[C-]#[O+]': 1.5, '[Ar]': 0.69},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 42,
    label = "H_10_(3) + C6H13(77) <=> C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;H_rad]
""",
)

entry(
    index = 49,
    label = "C3H7(35) <=> H_10_(3) + C3H6(38)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.465, 1.26, -0.1815, -0.00125],
            [4.337, 0.7197, 0.1099, -0.03228],
            [-0.1948, 0.009877, 0.0512, 0.01579],
            [-0.004694, -0.04035, -0.005799, 0.006226],
            [-0.003674, 0.000282, -0.004226, -0.001215],
            [-0.01265, 0.004952, 0.001537, -0.0002196],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 55,
    label = "C3H7(35) + C3H6(38) <=> C6H13(77)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2331, 'cm^3/(mol*s)'),
        n = 2.486,
        Ea = (4.895, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cds-HH_Cds-CsH;CsJ-CsHH] + [Cds-HH_Cds-Cs\\H3/H;CsJ] for rate rule [Cds-HH_Cds-Cs\\H3/H;CsJ-CsHH]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cds-HH_Cds-CsH;CsJ-CsHH] + [Cds-HH_Cds-Cs\H3/H;CsJ] for rate rule [Cds-HH_Cds-Cs\H3/H;CsJ-CsHH]
""",
)

entry(
    index = 59,
    label = "H_10_(3) + C2H5(31) <=> CCadd(1)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1.58, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6.685, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.842,
        T3 = (125, 'K'),
        T1 = (2220, 'K'),
        T2 = (6880, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 67,
    label = "C3H7(35) + C2H5(31) <=> C5H12(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 69,
    label = "C2H5(31) + C4H9(37) <=> C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 70,
    label = "C4H9(37) + CH3(17) <=> C5H12(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C_methyl]
""",
)

entry(
    index = 71,
    label = "OH_12_(12) + C4H9(37) <=> C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;C_rad/H2/Cs]
""",
)

entry(
    index = 72,
    label = "H_10_(3) + C2H4(30) <=> C2H5(31)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.232e+09, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1.355, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.9e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5.769, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1.569,
        T3 = (-9150, 'K'),
        T1 = (299, 'K'),
        T2 = (152, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 4.92, 'C=O': 2.5, '[He]': 0.7, 'N#N': 0.86, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 77,
    label = "C2H4(30) + CH3(17) <=> C3H7(35)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.783, 0.9684, -0.1337, -0.001489],
            [0.4752, 0.9042, 0.01558, -0.03081],
            [-0.1844, 0.1092, 0.06601, 0.003929],
            [-0.01256, -0.0395, 0.01216, 0.008908],
            [-0.003778, -0.01081, -0.001862, 0.001184],
            [-0.01123, 0.0011, 0.001101, 9.125e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 78,
    label = "C2H4(30) + C2H5(31) <=> C4H9(37)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.194, 0.7994, -0.1409, -0.002644],
            [0.6966, 0.8932, -0.05066, -0.03647],
            [-0.1706, 0.1913, 0.06909, -0.01093],
            [-0.06773, 0.007643, 0.03837, 0.008326],
            [-0.04939, 0.005181, 0.01234, 0.005844],
            [-0.0332, 0.002922, 0.006175, 0.003076],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 83,
    label = "C3H7(35) <=> C3H7(79)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (718000, 's^-1'),
        n = 2.05,
        Ea = (36.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 87,
    label = "H_10_(3) + C3H6(38) <=> C3H7(79)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e+09, 'cm^3/(mol*s)'),
        n = 1.553,
        Ea = (1.57, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-Cs\\H3/H;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-Cs\H3/H;HJ]
""",
)

entry(
    index = 93,
    label = "H2O_14_(6) + C4H8(78) <=> C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1816, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (56.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd/H/Nd_Cd/H2;H_OH]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd/H/Nd_Cd/H2;H_OH]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 94,
    label = "H_10_(3) + C4H8(78) <=> C4H9(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.17e+08, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-HH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-HH;HJ]
""",
)

entry(
    index = 102,
    label = "C3H6(38) <=> H_10_(3) + C3H5(41)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-4.589, 0.5537, -0.08034, 0.006212],
            [12.09, 0.7918, -0.06274, -0.009074],
            [-0.5699, 0.3193, 0.0263, -0.01105],
            [-0.2471, 0.0535, 0.03043, 0.0004006],
            [-0.07263, -0.02044, 0.008227, 0.003644],
            [-0.006513, -0.01907, -0.002315, 0.001102],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 112,
    label = "C3H5(41) + CH3(17) <=> C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C_methyl]
""",
)

entry(
    index = 114,
    label = "C4H8(82) <=> C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.718e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 116,
    label = "C4H8(82) <=> C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.105e+11, 's^-1'),
        n = 0.177,
        Ea = (7.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [singletcarbene_CH;CsJ2C;CH2(C)] + [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH2(C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [singletcarbene_CH;CsJ2C;CH2(C)] + [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH2(C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 117,
    label = "C3H5(41) + C3H5(41) <=> C6H10(84)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.26, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cd]
""",
)

entry(
    index = 126,
    label = "H_10_(3) + C3H4(39) <=> C3H5(41)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.46, 0.7205, -0.0919, 0.003997],
            [-0.3121, 0.8521, -0.02226, -0.01651],
            [-0.4643, 0.227, 0.0431, -0.003217],
            [-0.1332, -0.002253, 0.01621, 0.004745],
            [-0.006621, -0.02308, -0.002794, 0.001289],
            [0.01594, -0.00679, -0.003243, -0.0007156],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 128,
    label = "C3H7(35) + CH2OH(32) <=> C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.535e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.065, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C_rad/H2/Cs] for rate rule [C_rad/H2/O;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C_rad/H2/Cs] for rate rule [C_rad/H2/O;C_rad/H2/Cs]
""",
)

entry(
    index = 130,
    label = "CH2O(25) <=> H2_13_(2) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+13, 's^-1'), n=0, Ea=(71.976, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.4e+38, 'cm^3/(mol*s)'), n=-6.1, Ea=(94, 'kcal/mol'), T0=(1, 'K')),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 134,
    label = "CH2OH(32) <=> H_10_(3) + CH2O(25)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.37e+10, 's^-1'), n=0.811, Ea=(39.58, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.01e+13, 'cm^3/(mol*s)'),
            n = 0.184,
            Ea = (17.23, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.001,
        T3 = (50, 'K'),
        T1 = (600, 'K'),
        T2 = (2780, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'O': 5.97, 'C=O': 2.5, '[H][H]': 2, '[He]': 0.67, '[C-]#[O+]': 1.5, '[Ar]': 0.85},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 145,
    label = "H_10_(3) + C3H5(65) <=> C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;H_rad]
""",
)

entry(
    index = 157,
    label = "C3H5(65) <=> C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.53e+10, 's^-1'),
        n = 0.97,
        Ea = (37.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R3H_DS;Cd_rad_out_singleH;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R3H_DS;Cd_rad_out_singleH;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 159,
    label = "C3H5(65) + CH3(17) <=> C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;C_methyl]
""",
)

entry(
    index = 164,
    label = "C2H2(20) + CH3(17) <=> C3H5(41)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.654, -0.3073, -0.123, -0.02103],
            [2.619, 0.4171, 0.1521, 0.01587],
            [0.07617, -0.1082, -0.01945, 0.01122],
            [0.04211, -0.01689, -0.01689, -0.007157],
            [0.02041, 0.01252, 0.003941, -0.001158],
            [0.003403, 0.001688, 0.002221, 0.001238],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 165,
    label = "C2H2(20) + CH3(17) <=> C3H5(65)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (133800, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (6.77, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-H;CsJ-HHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-H;CsJ-HHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 167,
    label = "H_10_(3) + C3H3(19) <=> C3H4(39)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.56, 0.4492, -0.0843, 0.005199],
            [-0.6617, 0.6078, -0.06495, -0.01149],
            [-0.354, 0.2559, 0.009927, -0.01004],
            [-0.1528, 0.07253, 0.01779, -0.0007731],
            [-0.05514, 0.01017, 0.007507, 0.001976],
            [-0.01544, -0.003634, 0.001169, 0.001095],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 184,
    label = "HCO(22) <=> H_10_(3) + CO_21_(14)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.8e+17, 'cm^3/(mol*s)'),
            n = -1.2,
            Ea = (17.734, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.6, 'O=C=O': 2, 'CC': 3, 'O': 15.31, 'C=O': 3.29, '[H][H]': 1.31, '[He]': 1.31, '[O][O]': 1.32, 'N#N': 1.31, '[C-]#[O+]': 2.4, '[Ar]': 1.4},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 190,
    label = "H_10_(3) + HCO(22) <=> CH2O(25)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.913e+14, 'cm^3/(mol*s)'),
            n = -0.033,
            Ea = (-0.142, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.19e+34, 'cm^6/(mol^2*s)'),
            n = -5.533,
            Ea = (6.128, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (271, 'K'),
        T1 = (2760, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.84, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.79},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 209,
    label = "C3H6(81) <=> C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.347e+10, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH3]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH3]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 210,
    label = "CH2O(25) + C3H3(19) <=> C4H5O(93)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2330, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (6.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Od_CO-HH;YJ] for rate rule [Od_CO-HH;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Od_CO-HH;YJ] for rate rule [Od_CO-HH;CdsJ=Cdd]
""",
)

entry(
    index = 211,
    label = "CH3(17) + C3H3(19) <=> C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.822e+15, 'cm^3/(mol*s)'),
        n = -0.864,
        Ea = (0.195, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cs_rad;C_rad/H2/Ct] + [C_methyl;C_pri_rad] for rate rule [C_methyl;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cs_rad;C_rad/H2/Ct] + [C_methyl;C_pri_rad] for rate rule [C_methyl;C_rad/H2/Ct]
""",
)

entry(
    index = 213,
    label = "H_10_(3) + C2H2(20) <=> C2H3(29)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.54e+08, 'cm^3/(mol*s)'),
            n = 1.64,
            Ea = (2.096, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.63e+27, 'cm^6/(mol^2*s)'),
            n = -3.38,
            Ea = (0.847, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.215,
        T3 = (10.7, 'K'),
        T1 = (1040, 'K'),
        T2 = (2340, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 214,
    label = "H_10_(3) + C2H3(29) <=> C2H4(30)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.88e+13, 'cm^3/(mol*s)'), n=0.2, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3.32, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (208, 'K'),
        T1 = (2660, 'K'),
        T2 = (6100, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 227,
    label = "C3H6(38) <=> C2H3(29) + CH3(17)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.534, 0.9544, -0.181, 0.02048],
            [13.47, 0.8117, 0.04223, -0.04535],
            [-0.677, 0.1792, 0.07476, -0.002557],
            [-0.2282, -0.01485, 0.02174, 0.009982],
            [-0.04951, -0.03132, -0.003947, 0.004069],
            [0.005288, -0.01413, -0.005881, -0.0001332],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 243,
    label = "C2H3(29) + C2H5(31) <=> C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]
""",
)

entry(
    index = 249,
    label = "C2H2(40) <=> C2H2(20)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.448, 1.844, -0.09821, -0.04516],
            [0.8528, 0.05926, 0.0351, 0.01409],
            [-0.01188, 0.004472, 0.002927, 0.001448],
            [0.001476, -0.001062, -0.0003545, 0.0001196],
            [-0.03084, 0.009535, 0.005233, 0.001711],
            [-0.01446, 0.001708, 0.001237, 0.000718],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 250,
    label = "C4H6(95) <=> C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 254,
    label = "H_10_(3) + C2H(21) <=> C2H2(20)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.25e+13, 'cm^3/(mol*s)'), n=0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1.9, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.646,
        T3 = (132, 'K'),
        T1 = (1320, 'K'),
        T2 = (5570, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 271,
    label = "C2H(21) + C2H5(31) <=> C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.719e+12, 'cm^3/(mol*s)'),
        n = 0.314,
        Ea = (-0.44, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H2/Cs] for rate rule [Ct_rad/Ct;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H2/Cs] for rate rule [Ct_rad/Ct;C_rad/H2/Cs]
""",
)

entry(
    index = 283,
    label = "H_10_(3) + C3H3(19) <=> C3H4(45)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.27, 1.28, -0.263, -0.01893],
            [-0.7887, 0.4989, 0.1152, -0.03811],
            [-0.2849, 0.07865, 0.05228, 0.01183],
            [-0.07495, -0.01651, 0.004644, 0.009517],
            [-0.004869, -0.01942, -0.006849, 0.001718],
            [0.007973, -0.007214, -0.004461, -0.00118],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 287,
    label = "C3H4(45) <=> C2H(21) + CH3(17)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.86, 1.798, -0.1195, -0.04809],
            [17.74, 0.1562, 0.08622, 0.02889],
            [-0.3585, 0.01337, 0.01049, 0.006628],
            [-0.08777, -0.01023, -0.00519, -0.001231],
            [-0.005575, -0.006574, -0.004024, -0.001731],
            [0.006444, -0.001593, -0.001156, -0.0006714],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 293,
    label = "H_10_(3) + C3H4(45) <=> C3H5(65)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.276e+10, 'cm^3/(mol*s)'),
        n = 1.103,
        Ea = (4.911, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cs_Ct-H;HJ from training reaction 148\nExact match found for rate rule [Ct-Cs_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Ct-Cs_Ct-H;HJ from training reaction 148
Exact match found for rate rule [Ct-Cs_Ct-H;HJ]
""",
)

entry(
    index = 310,
    label = "H_10_(3) + C3H5(66) <=> C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cd_rad/NonDe;H_rad from training reaction 20\nExact match found for rate rule [Cd_rad/NonDe;H_rad]',
    ),
    longDesc = 
u"""
Cd_rad/NonDe;H_rad from training reaction 20
Exact match found for rate rule [Cd_rad/NonDe;H_rad]
""",
)

entry(
    index = 322,
    label = "C3H5(41) <=> C3H5(66)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.68e+11, 's^-1'),
        n = 0.63,
        Ea = (62.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_2H;Cd_H_out_doubleC]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_2H;Cd_H_out_doubleC]
""",
)

entry(
    index = 327,
    label = "H_10_(3) + C3H4(39) <=> C3H5(66)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.635e+09, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Ca;HJ from training reaction 144\nExact match found for rate rule [Cds-HH_Ca;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Cds-HH_Ca;HJ from training reaction 144
Exact match found for rate rule [Cds-HH_Ca;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 338,
    label = "C3H5(65) <=> C3H5(66)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.73,
        Ea = (42.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd]
""",
)

entry(
    index = 347,
    label = "H_10_(3) + C3H4(45) <=> C3H5(66)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.255e+11, 'cm^3/(mol*s)'),
        n = 1.005,
        Ea = (3.143, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-H_Ct-Cs;HJ from training reaction 147\nExact match found for rate rule [Ct-H_Ct-Cs;HJ]',
    ),
    longDesc = 
u"""
Ct-H_Ct-Cs;HJ from training reaction 147
Exact match found for rate rule [Ct-H_Ct-Cs;HJ]
""",
)

entry(
    index = 360,
    label = "C2H2(20) + C3H3(19) <=> C5H5(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.27e+06, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (10.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 361,
    label = "CH3(17) + C3H3(19) <=> C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methyl;Cd_allenic]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_methyl;Cd_allenic]
""",
)

entry(
    index = 362,
    label = "CO_21_(14) + C3H3(19) <=> C4H3O(88)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.056e+08, 'cm^3/(mol*s)'),
        n = 1.155,
        Ea = (7.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_pri_rad] for rate rule [COm;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_pri_rad] for rate rule [COm;C_rad/H2/Ct]
""",
)

entry(
    index = 363,
    label = "CO_21_(14) + C3H3(19) <=> C4H3O(89)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [COm;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [COm;Cd_pri_rad]
""",
)

entry(
    index = 364,
    label = "C4H6(98) <=> C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]
""",
)

entry(
    index = 365,
    label = "H_10_(3) + C3H3(19) <=> C3H4(44)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.82, -0.6545, -0.2437, -0.02023],
            [0.1399, 0.5292, 0.1407, -0.02884],
            [-0.1127, 0.06805, 0.05424, 0.01784],
            [-0.08633, -0.02477, 5.51e-05, 0.009343],
            [-0.03795, -0.01996, -0.008978, -5.994e-06],
            [-0.0113, -0.005264, -0.004197, -0.001915],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 366,
    label = "C3H4(44) <=> C3H4(45)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.783, 1.504, -0.2208, -0.04917],
            [0.659, 0.2835, 0.08538, -0.01031],
            [-0.1163, 0.05481, 0.02976, 0.007474],
            [-0.06516, 0.02449, 0.01483, 0.004966],
            [-0.01748, 0.0005182, 0.003433, 0.00281],
            [0.006906, -0.007988, -0.002478, 0.0007169],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 367,
    label = "C2H4(30) + C3H3(19) <=> C5H7(92)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18920, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (9.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-CtHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-CtHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 368,
    label = "C3H3(19) + C3H3(19) <=> C6H6(94)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.288e+09, 'cm^3/(mol*s)'),
        n = 0.795,
        Ea = (-1.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 28 C3H3-2 + C3H3-2 <=> CH2CCHCHCCH2 in R_Recombination/training',
    ),
    longDesc = 
u"""
Matched reaction 28 C3H3-2 + C3H3-2 <=> CH2CCHCHCCH2 in R_Recombination/training
""",
)

entry(
    index = 369,
    label = "C2H2(20) <=> H2CC(27)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+14, 's^-1'), n=-0.52, Ea=(50.75, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.45e+15, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49.7, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.69},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 373,
    label = "C2H4(30) <=> H2_13_(2) + H2CC(27)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3.985e+15, 's^-1'), n=0, Ea=(87.06, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.71e+16, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (67.816, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.01, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 374,
    label = "H_10_(3) + C4H7(85) <=> C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cd_rad/NonDe;H_rad from training reaction 20\nExact match found for rate rule [H_rad;Cd_rad/NonDe]',
    ),
    longDesc = 
u"""
Cd_rad/NonDe;H_rad from training reaction 20
Exact match found for rate rule [H_rad;Cd_rad/NonDe]
""",
)

entry(
    index = 388,
    label = "C3H4(45) + CH3(17) <=> C4H7(85)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Cs;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Cs;CsJ-HHH]
""",
)

entry(
    index = 405,
    label = "H_10_(3) + C4H6(91) <=> C4H7(85)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.175e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Ca;HJ from training reaction 144\nExact match found for rate rule [Cds-HH_Ca;HJ]',
    ),
    longDesc = 
u"""
Cds-HH_Ca;HJ from training reaction 144
Exact match found for rate rule [Cds-HH_Ca;HJ]
""",
)

entry(
    index = 406,
    label = "C6H6(94) <=> C6H6(100)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+11, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 C6H6 <=> C6H6-2 in Intra_2+2_cycloaddition_Cd/training',
    ),
    longDesc = 
u"""
Matched reaction 1 C6H6 <=> C6H6-2 in Intra_2+2_cycloaddition_Cd/training
""",
)

entry(
    index = 407,
    label = "C6H6(101) <=> C6H6(100)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2(C=C);CH2(C=C)] for rate rule [CsJ2-C;CsJ2(C=C);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2(C=C);CH2(C=C)] for rate rule [CsJ2-C;CsJ2(C=C);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 419,
    label = "H2_13_(2) + CH2(S)(28) <=> Cadd(4)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.14, 0.7462, -0.1682, 0.01161],
            [-0.5794, 0.626, -0.01613, -0.03025],
            [-0.2678, 0.1586, 0.0408, -0.00524],
            [-0.1094, 0.03173, 0.01748, 0.003682],
            [-0.04642, 0.00841, 0.003154, 0.001803],
            [-0.01527, -0.001976, 0.0007925, 0.0005426],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 420,
    label = "CCadd(1) <=> Cadd(4) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.12, 0.3924, -0.07045, 0.00458],
            [14.61, 0.5899, -0.0719, -0.00678],
            [-0.4554, 0.2893, 0.0006021, -0.01068],
            [-0.205, 0.09558, 0.01926, -0.002939],
            [-0.08169, 0.01695, 0.01114, 0.001828],
            [-0.02799, -0.003301, 0.002608, 0.001756],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 421,
    label = "C3H7(35) <=> CH2(S)(28) + C2H5(31)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.88, 1.992, -0.005314, -0.002925],
            [15.19, 0.006585, 0.004546, 0.00249],
            [-0.001199, -0.0023, -0.001582, -0.0008617],
            [0.02385, -8.23e-05, -6.086e-05, -3.705e-05],
            [-0.02644, 0.0003473, 0.0002408, 0.0001329],
            [-0.02663, 0.000139, 9.678e-05, 5.377e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 422,
    label = "C4H9(37) <=> C3H7(35) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.593, 1.96, -0.02702, -0.01425],
            [15.05, 0.03416, 0.02272, 0.01166],
            [-0.1082, -0.009399, -0.00604, -0.002901],
            [-0.1016, 0.00465, 0.003019, 0.00148],
            [-0.09803, 0.003545, 0.002428, 0.001312],
            [-0.04746, 0.0007795, 0.0005388, 0.0002959],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 423,
    label = "C3H6(38) <=> CH2(S)(28) + C2H4(30)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.11, 1.279, -0.2173, -0.0005583],
            [14.56, 0.6478, 0.1403, -0.03372],
            [-0.6803, 0.08754, 0.06294, 0.01634],
            [-0.2085, -0.0308, 0.001956, 0.009537],
            [-0.03584, -0.02455, -0.009535, 0.0002915],
            [0.01116, -0.007776, -0.005131, -0.001612],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 428,
    label = "C3H4(44) <=> CH2(S)(28) + C2H2(40)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.24, 1.888, -0.07382, -0.03702],
            [15.9, -0.01467, -0.008986, -0.003897],
            [-0.2213, 0.0174, 0.01071, 0.004697],
            [-0.1263, 0.02033, 0.01241, 0.005332],
            [-0.03304, 0.005692, 0.003441, 0.001448],
            [0.006374, -0.002987, -0.001739, -0.0006655],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 429,
    label = "C3H4(45) <=> C2H2(20) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.1, 1.629, -0.1874, -0.05044],
            [16.09, 0.2969, 0.1301, 0.01679],
            [-0.2872, 0.02524, 0.02232, 0.0136],
            [-0.06997, -0.01656, -0.005818, 0.001286],
            [0.002355, -0.01086, -0.006044, -0.001896],
            [0.01122, -0.002656, -0.002019, -0.001174],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 430,
    label = "C5H12(9) + CH2(S)(28) <=> C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.572e+13, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]\nMultiplied by reaction path degeneracy 36',
    ),
    longDesc = 
u"""
Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]
Multiplied by reaction path degeneracy 36
""",
)

entry(
    index = 431,
    label = "CH2(S)(28) + C3H6(38) <=> C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.87e+13, 'cm^3/(mol*s)'),
        n = -0.146,
        Ea = (0.003, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 7 CH2 + CH3CHCH2_r3 <=> CH3CH2CHCH2 in 1,2_Insertion_carbene/training',
    ),
    longDesc = 
u"""
Matched reaction 7 CH2 + CH3CHCH2_r3 <=> CH3CH2CHCH2 in 1,2_Insertion_carbene/training
""",
)

entry(
    index = 432,
    label = "CH2(S)(28) + C3H6(81) <=> C4H8(82)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.572e+13, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]\nMultiplied by reaction path degeneracy 36',
    ),
    longDesc = 
u"""
Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]
Multiplied by reaction path degeneracy 36
""",
)

entry(
    index = 433,
    label = "CH2(S)(28) + C3H6(38) <=> C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+13, 'cm^3/(mol*s)'),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 5 CH2 + CH3CHCH2_r1 <=> CH3CHCHCH3 in 1,2_Insertion_carbene/training',
    ),
    longDesc = 
u"""
Matched reaction 5 CH2 + CH3CHCH2_r1 <=> CH3CHCHCH3 in 1,2_Insertion_carbene/training
""",
)

entry(
    index = 434,
    label = "CH2(S)(28) + C2H3(29) <=> C3H5(65)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 435,
    label = "C3H4(45) + CH2(S)(28) <=> C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.18e+10, 'cm^3/(mol*s)'),
        n = 0.524,
        Ea = (-0.711, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 4 CH2 + CH3CCH_r2 <=> CH3CH2CCH in 1,2_Insertion_carbene/training',
    ),
    longDesc = 
u"""
Matched reaction 4 CH2 + CH3CCH_r2 <=> CH3CH2CCH in 1,2_Insertion_carbene/training
""",
)

entry(
    index = 436,
    label = "C3H4(44) + CH2(S)(28) <=> C4H6(95)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.122e+14, 'cm^3/(mol*s)'),
        n = -0.146,
        Ea = (0.003, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;C_pri/Cd from training reaction 7\nExact match found for rate rule [carbene;C_pri/Cd]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
carbene;C_pri/Cd from training reaction 7
Exact match found for rate rule [carbene;C_pri/Cd]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 437,
    label = "CH2(S)(28) + C3H4(39) <=> C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+11, 'cm^3/(mol*s)'),
        n = 0.465,
        Ea = (-1.742, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 8 CH2 + CH2CCH2 <=> CH3CHCCH2 in 1,2_Insertion_carbene/training',
    ),
    longDesc = 
u"""
Matched reaction 8 CH2 + CH2CCH2 <=> CH3CHCCH2 in 1,2_Insertion_carbene/training
""",
)

entry(
    index = 438,
    label = "CH2(S)(28) + C3H5(66) <=> C4H7(85)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 439,
    label = "C3H4(45) + C3H3(19) <=> C6H7(51)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7040, 'cm^3/(mol*s)'), n=2.87, Ea=(9.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 440,
    label = "C6H6(94) <=> C6H6(99)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.162e+12, 's^-1'),
        n = -0.046,
        Ea = (38.474, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 C6H6 <=> C6H6-2 in Intra_5_membered_conjugated_C=C_C=C_addition/training',
    ),
    longDesc = 
u"""
Matched reaction 1 C6H6 <=> C6H6-2 in Intra_5_membered_conjugated_C=C_C=C_addition/training
""",
)

entry(
    index = 441,
    label = "C6H6(99) <=> C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.067e+10, 's^-1'),
        n = 0.649,
        Ea = (8.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 C6H6 <=> C6H6-2 in Singlet_Carbene_Intra_Disproportionation/training',
    ),
    longDesc = 
u"""
Matched reaction 1 C6H6 <=> C6H6-2 in Singlet_Carbene_Intra_Disproportionation/training
""",
)

entry(
    index = 442,
    label = "C6H6(103) <=> C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2(C=C);CH2(C=C)] for rate rule [CsJ2-C;CsJ2(C=C);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2(C=C);CH2(C=C)] for rate rule [CsJ2-C;CsJ2(C=C);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 443,
    label = "C6H6(54) <=> C6H6(102)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.012e+13, 's^-1'),
        n = 0.1,
        Ea = (41.564, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 2 C6H6-3 <=> C6H6-4 in Intra_Diels_alder_monocyclic/training\nEa raised from 172.4 to 173.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Matched reaction 2 C6H6-3 <=> C6H6-4 in Intra_Diels_alder_monocyclic/training
Ea raised from 172.4 to 173.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 444,
    label = "H_10_(3) + C6H6(54) <=> C6H7(56)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.26e+09, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 458,
    label = "C6H6(107) <=> C6H6(102)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 459,
    label = "C6H6(54) <=> C6H6(104)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (47.51, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 460,
    label = "H_10_(3) + C6H6(54) <=> C6H7(53)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.52e+09, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 461,
    label = "C6H7(56) <=> C6H7(53)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9220, 's^-1'), n=2.81, Ea=(30.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 475,
    label = "H_10_(3) + C6H6(54) <=> C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (-0.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 489,
    label = "C6H7(53) <=> C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.64e+08, 's^-1'),
        n = 1.1,
        Ea = (29.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule [R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule [R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 490,
    label = "C3H3(86) <=> C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.818e+10, 's^-1'),
        n = 0.898,
        Ea = (41.241, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_MS;Y_rad_out;Cs_H_out_2H] for rate rule [R3H_TS;Ct_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R3H_MS;Y_rad_out;Cs_H_out_2H] for rate rule [R3H_TS;Ct_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 491,
    label = "H_10_(3) + C3H3(86) <=> C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Ct_rad/Ct]
""",
)

entry(
    index = 512,
    label = "H_10_(3) + C6H6(54) <=> C6H7(55)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.31e+08, 'cm^3/(mol*s)'), n=1.76, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 513,
    label = "C6H7(52) <=> C6H7(55)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00218, 's^-1'), n=4.91, Ea=(40.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 514,
    label = "C6H7(55) <=> C6H7(53)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+07, 's^-1'), n=1.54, Ea=(13.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 529,
    label = "C2H(21) + CH2(S)(28) <=> C3H3(86)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 530,
    label = "C6H7(55) <=> C6H7(57)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.18e+11, 's^-1'), n=0.17, Ea=(4.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 531,
    label = "H_10_(3) + C6H6(102) <=> C6H7(57)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.17e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsCs_Cds-CdH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsCs_Cds-CdH;HJ]
""",
)

entry(
    index = 532,
    label = "C2H2(20) + C2H(21) <=> C4H3(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-H;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-H;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 533,
    label = "C6H7(57) <=> cyC6H7(58)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.51e+11, 's^-1'), n=0.41, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 534,
    label = "H_10_(3) + C4H2(111) <=> C4H3(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.674e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-H;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-H;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 535,
    label = "cyC6H7(58) <=> H_10_(3) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.84e+09, 's^-1'), n=1.3, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Fulvene_H
""",
)

entry(
    index = 536,
    label = "C2H(21) + C2H(21) <=> C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Ct_rad/Ct] + [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Ct_rad/Ct] + [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Ct_rad/Ct]
""",
)

entry(
    index = 565,
    label = "C4H2(113) <=> C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 566,
    label = "C4H3(96) <=> C4H3(110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]
""",
)

entry(
    index = 569,
    label = "H_10_(3) + C4H2(111) <=> C4H3(110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.48e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 585,
    label = "H_10_(3) + C6H5(64) <=> C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]
""",
)

entry(
    index = 610,
    label = "C6H6(102) <=> C6H6(106)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+12, 's^-1'),
        n = 0.194,
        Ea = (32.274, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 C6H6 <=> C6H6-2 in Cyclopentadiene_scission/training',
    ),
    longDesc = 
u"""
Matched reaction 1 C6H6 <=> C6H6-2 in Cyclopentadiene_scission/training
""",
)

entry(
    index = 611,
    label = "C6H6(106) <=> C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.454e+12, 's^-1'),
        n = 0.178,
        Ea = (0.205, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 2 C6H6-3 <=> C6H6-4 in Singlet_Carbene_Intra_Disproportionation/training',
    ),
    longDesc = 
u"""
Matched reaction 2 C6H6-3 <=> C6H6-4 in Singlet_Carbene_Intra_Disproportionation/training
""",
)

entry(
    index = 614,
    label = "O2_2_(13) + C6H5(64) <=> S(123)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 615,
    label = "C6H5(122) <=> C6H5(64)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 616,
    label = "C2H2(20) + C4H3(96) <=> C6H5(122)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (251000, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-H;CdsJ-H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-H;CdsJ-H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 617,
    label = "H_10_(3) + C6H5(105) <=> C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;H_rad]
""",
)

entry(
    index = 642,
    label = "C6H5(122) <=> C6H5(105)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 643,
    label = "C2H4(30) + C6H5(64) <=> C8H9(124)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20840, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (1.695, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-HH;CdsJ] for rate rule [Cds-HH_Cds-HH;CdsJ-Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-HH;CdsJ] for rate rule [Cds-HH_Cds-HH;CdsJ-Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 644,
    label = "C8H9(124) <=> C8H9(126)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.399e+11, 's^-1'),
        n = 0.121,
        Ea = (16.958, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4_S_D;doublebond_intra_HDe_secDe_benzene;radadd_intra_cs2H from training reaction 7\nExact match found for rate rule [R4_S_D;doublebond_intra_HDe_secDe_benzene;radadd_intra_cs2H]\nEa raised from 69.1 to 71.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
R4_S_D;doublebond_intra_HDe_secDe_benzene;radadd_intra_cs2H from training reaction 7
Exact match found for rate rule [R4_S_D;doublebond_intra_HDe_secDe_benzene;radadd_intra_cs2H]
Ea raised from 69.1 to 71.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 645,
    label = "H_10_(3) + C6H5(108) <=> C6H6(102)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.936e+13, 'cm^3/(mol*s)'),
        n = -0.055,
        Ea = (7.745, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/CdCs;H_rad from training reaction 25\nExact match found for rate rule [C_rad/H/CdCs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H/CdCs;H_rad from training reaction 25
Exact match found for rate rule [C_rad/H/CdCs;H_rad]
""",
)

entry(
    index = 646,
    label = "C6H5(105) <=> C6H5(108)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.328e+12, 's^-1'),
        n = 0.3,
        Ea = (16.235, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule\n[Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4\nEa raised from 66.3 to 67.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule
[Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
Ea raised from 66.3 to 67.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 647,
    label = "CH3(17) + C4H2(111) <=> C5H5(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (578000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (3.39, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-HHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-HHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 648,
    label = "C2H2(20) + C6H5(64) <=> A3a(76)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20490, 'cm^3/(mol*s)'),
        n = 2.538,
        Ea = (5.46, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct_Ct;CdsJ-Cd] + [Ct-H_Ct-H;CdsJ] for rate rule [Ct-H_Ct-H;CdsJ-Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct_Ct;CdsJ-Cd] + [Ct-H_Ct-H;CdsJ] for rate rule [Ct-H_Ct-H;CdsJ-Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 649,
    label = "CH2(S)(28) + C4H3(110) <=> C5H5(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd_pri from training reaction 5\nExact match found for rate rule [carbene;Cd_pri]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd_pri from training reaction 5
Exact match found for rate rule [carbene;Cd_pri]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 650,
    label = "A3a(76) <=> C8H7(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+07, 's^-1'),
        n = 1.425,
        Ea = (7.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb from training reaction 81\nExact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb]',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb from training reaction 81
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb]
""",
)

entry(
    index = 651,
    label = "C5H5(117) <=> C5H5(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 652,
    label = "H_10_(3) + C5H4(130) <=> C5H5(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.71e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.77, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cs_Ct-Ct;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cs_Ct-Ct;HJ]
""",
)

entry(
    index = 653,
    label = "H_10_(3) + C8H6(74) <=> A3a(76)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.775e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (6.896, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cb_Ct-H;HJ from training reaction 187\nExact match found for rate rule [Ct-Cb_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Ct-Cb_Ct-H;HJ from training reaction 187
Exact match found for rate rule [Ct-Cb_Ct-H;HJ]
""",
)

entry(
    index = 654,
    label = "H_10_(3) + C8H6(74) <=> C8H7(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.905e+09, 'cm^3/(mol*s)'),
        n = 1.589,
        Ea = (2.838, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct-H_Ct-De;HJ] + [Ct-H_Ct-Cb;YJ] for rate rule [Ct-H_Ct-Cb;HJ]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct-H_Ct-De;HJ] + [Ct-H_Ct-Cb;YJ] for rate rule [Ct-H_Ct-Cb;HJ]
""",
)

entry(
    index = 655,
    label = "A3a(76) <=> C8H7(132)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.774e+11, 's^-1'),
        n = 0.174,
        Ea = (14.211, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule\n[Rn2c6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2\nEa raised from 57.4 to 59.5 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule
[Rn2c6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
Ea raised from 57.4 to 59.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 656,
    label = "CH2(S)(28) + C4H2(111) <=> C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.12e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 657,
    label = "C2H(21) + C3H3(86) <=> C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Ct_rad/Ct] + [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Ct_rad/Ct] + [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Ct_rad/Ct]
""",
)

entry(
    index = 658,
    label = "C2H(21) + C6H5(64) <=> C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Cb_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Cb_rad]
""",
)

entry(
    index = 702,
    label = "C8H6(143) <=> C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 703,
    label = "C5H5(127) <=> C5H5(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.578e+08, 's^-1'),
        n = 1.319,
        Ea = (37.223, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [RnH;Cd_rad_out_Cs;Cd_H_out_singleH] + [R4H;Cd_rad_out_single;Cd_H_out_singleH] for rate rule\n[R4H;Cd_rad_out_Cs;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [RnH;Cd_rad_out_Cs;Cd_H_out_singleH] + [R4H;Cd_rad_out_single;Cd_H_out_singleH] for rate rule
[R4H;Cd_rad_out_Cs;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 704,
    label = "C5H5(127) <=> C5H5(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.33e+08, 's^-1'),
        n = 1.192,
        Ea = (24.762, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out_2H] for rate rule [R4H_STS;Cd_rad_out_Cd;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out_2H] for rate rule [R4H_STS;Cd_rad_out_Cd;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 706,
    label = "H_10_(3) + C5H4(130) <=> C5H5(127)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;HJ]
""",
)

entry(
    index = 715,
    label = "CH3(17) + C8H6(74) <=> W5(68)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (713400, 'cm^3/(mol*s)'),
        n = 2.58,
        Ea = (7.568, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 716,
    label = "CH2(S)(28) + C4H3(110) <=> C5H5(127)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 717,
    label = "CH2(S)(28) + C8H7(131) <=> W5(68)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 718,
    label = "C5H4(140) <=> C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 719,
    label = "A3a(76) <=> C8H7(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.166e+07, 's^-1'),
        n = 1.697,
        Ea = (19.915, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70\nExact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70
Exact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 720,
    label = "C8H7(131) <=> C8H7(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260400, 's^-1'),
        n = 2.209,
        Ea = (29.053, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47\nExact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47
Exact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 721,
    label = "CH2(S)(28) + C4H2(113) <=> C5H4(140)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 722,
    label = "C8H6(74) <=> C8H6(146)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.31e+13, 's^-1'),
        n = -0.215,
        Ea = (68.355, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'linear_1_3_hexadien_5_yne from training reaction 1\nExact match found for rate rule [linear_1_3_hexadien_5_yne]\nMultiplied by reaction path degeneracy 2\nEa raised from 283.9 to 286.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
linear_1_3_hexadien_5_yne from training reaction 1
Exact match found for rate rule [linear_1_3_hexadien_5_yne]
Multiplied by reaction path degeneracy 2
Ea raised from 283.9 to 286.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 723,
    label = "C3H3(19) + C4H2(111) <=> C7H5(120)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408400, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 724,
    label = "C4H3(96) <=> C4H3(112)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.767e+11, 's^-1'),
        n = 0.248,
        Ea = (19.557, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D;multiplebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_T;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R4_D;multiplebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_T;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 725,
    label = "C3H4(45) + C6H5(64) <=> W3_4(69)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (630400, 'cm^3/(mol*s)'),
        n = 2.103,
        Ea = (6.093, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 726,
    label = "CH3(17) + C8H6(74) <=> W3_4(69)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (563200, 'cm^3/(mol*s)'),
        n = 2.488,
        Ea = (11.733, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 727,
    label = "CH2(S)(28) + A3a(76) <=> W3_4(69)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.438e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 728,
    label = "C5H5(129) <=> C5H5(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+11, 's^-1'),
        n = 0.633,
        Ea = (46.955, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_singleDe]
""",
)

entry(
    index = 730,
    label = "H_10_(3) + C5H4(130) <=> C5H5(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.44e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (5.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-Cs;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-Cs;HJ]
""",
)

entry(
    index = 739,
    label = "C8H7(134) <=> C8H7(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.12e+06, 's^-1'),
        n = 1.75,
        Ea = (25.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Y_rad_out;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R4H_MMS;Cd_rad_out_singleH;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Y_rad_out;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R4H_MMS;Cd_rad_out_singleH;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 742,
    label = "H_10_(3) + C8H6(74) <=> C8H7(134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (814100, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 758,
    label = "C3H4(45) + C2H(21) <=> C5H5(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_Ct;CtJ_Ct] for rate rule [Ct-H_Ct-Cs;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_Ct;CtJ_Ct] for rate rule [Ct-H_Ct-Cs;CtJ_Ct]
""",
)

entry(
    index = 759,
    label = "C8H7(135) <=> C8H7(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.329e+09, 's^-1'),
        n = 0.738,
        Ea = (52.276, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;CtH_2] for rate rule [1_3_unsaturated_pentane_backbone;CH2(C)_1;CtH_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;CtH_2] for rate rule [1_3_unsaturated_pentane_backbone;CH2(C)_1;CtH_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 762,
    label = "H_10_(3) + C8H6(74) <=> C8H7(135)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (814100, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 778,
    label = "C8H7(134) <=> C8H7(135)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.12e+06, 's^-1'),
        n = 1.75,
        Ea = (25.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;C_rad_out_H/Cd;Cs_H_out_H/OneDe] for rate rule [R4H_SDS;C_rad_out_H/Cd;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4H;C_rad_out_H/Cd;Cs_H_out_H/OneDe] for rate rule [R4H_SDS;C_rad_out_H/Cd;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 779,
    label = "C5H5(137) <=> C5H5(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 781,
    label = "H_10_(3) + C5H4(130) <=> C5H5(137)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.37e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-H;HJ]
""",
)

entry(
    index = 790,
    label = "C5H5(137) <=> C5H5(127)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]
""",
)

entry(
    index = 791,
    label = "C2H2(20) + C3H3(86) <=> C5H5(137)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-H;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-H;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 792,
    label = "CH2(S)(28) + C4H3(96) <=> C5H5(137)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 793,
    label = "OH_12_(12) + C8H6(74) <=> C8H7O(149)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.642e+12, 'cm^3/(mol*s)'),
        n = 0.497,
        Ea = (0.666, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 182 C8H6-2 + HO <=> C8H7O-9 in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 182 C8H6-2 + HO <=> C8H7O-9 in R_Addition_MultipleBond/training
""",
)

entry(
    index = 794,
    label = "H_10_(3) + C5H3(141) <=> C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.478e+13, 'cm^3/(mol*s)'),
        n = 0.009,
        Ea = (-0.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_pri_rad;H_rad] + [C_rad/H2/Ct;Y_rad] for rate rule [C_rad/H2/Ct;H_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_pri_rad;H_rad] + [C_rad/H2/Ct;Y_rad] for rate rule [C_rad/H2/Ct;H_rad]
""",
)

entry(
    index = 822,
    label = "C5H3(162) <=> C5H3(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46950, 's^-1'),
        n = 2.23,
        Ea = (28.947, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [RnH;Cd_rad_out_singleH;Cd_H_out_singleDe] + [R3H;Cd_rad_out_singleH;XH_out] for rate rule\n[R3H;Cd_rad_out_singleH;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [RnH;Cd_rad_out_singleH;Cd_H_out_singleDe] + [R3H;Cd_rad_out_singleH;XH_out] for rate rule
[R3H;Cd_rad_out_singleH;Cd_H_out_singleDe]
""",
)

entry(
    index = 823,
    label = "C5H3(162) <=> C5H3(167)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.88e+10, 's^-1'),
        n = 0.31,
        Ea = (40.457, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R5_MM;triplebond_intra_H;radadd_intra_cdsingleH]\nEa raised from 167.0 to 169.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R5;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R5_MM;triplebond_intra_H;radadd_intra_cdsingleH]
Ea raised from 167.0 to 169.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 824,
    label = "C8H7(136) <=> C8H7(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.692e+10, 's^-1'),
        n = 0.74,
        Ea = (34.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_1H] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_1H] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 827,
    label = "H_10_(3) + C8H6(74) <=> C8H7(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (407000, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 844,
    label = "C8H7(136) <=> C8H7(134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.366e+08, 's^-1'),
        n = 1.484,
        Ea = (25.648, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CdCJ_2] + [1_3_unsaturated_pentane_backbone;CH(CJ)_1;unsaturated_end]\nfor rate rule [1_3_pentadiene;CH(CJ)_1;CdCJ_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CdCJ_2] + [1_3_unsaturated_pentane_backbone;CH(CJ)_1;unsaturated_end]
for rate rule [1_3_pentadiene;CH(CJ)_1;CdCJ_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 845,
    label = "C8H7(136) <=> C8H7(135)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36880, 's^-1'),
        n = 2.81,
        Ea = (30.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R2H_S;C_rad_out_H/(Cd-Cd-Cd);Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R2H_S;C_rad_out_H/(Cd-Cd-Cd);Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 846,
    label = "H_10_(3) + C5H3(142) <=> C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Ct_rad/Ct]
""",
)

entry(
    index = 871,
    label = "C5H3(142) <=> C5H3(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 872,
    label = "C2H2(20) + C5H3(141) <=> C7H5(164)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.54e+06, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (10.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-H_Ct-H;CsJ-CtHH from training reaction 46\nExact match found for rate rule [Ct-H_Ct-H;CsJ-CtHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Ct-H_Ct-H;CsJ-CtHH from training reaction 46
Exact match found for rate rule [Ct-H_Ct-H;CsJ-CtHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 873,
    label = "C5H3(162) <=> C5H3(168)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+08, 's^-1'),
        n = 1.192,
        Ea = (54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3_T;triplebond_intra_H;radadd_intra_cs] for rate rule [R3_T;triplebond_intra_H;radadd_intra_csHCt]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3_T;triplebond_intra_H;radadd_intra_cs] for rate rule [R3_T;triplebond_intra_H;radadd_intra_csHCt]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 874,
    label = "C7H5(120) <=> C7H5(156)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.31,
        Ea = (2.962, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 875,
    label = "CH3(17) + C8H6(74) <=> C9H9(152)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8780, 'cm^3/(mol*s)'),
        n = 2.878,
        Ea = (10.912, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;CsJ-HHH from training reaction 114\nExact match found for rate rule [Cb-H_Cb-H;CsJ-HHH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;CsJ-HHH from training reaction 114
Exact match found for rate rule [Cb-H_Cb-H;CsJ-HHH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 876,
    label = "C5H3(141) <=> C5H3(160)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+08, 's^-1'),
        n = 1.192,
        Ea = (54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3_T;triplebond_intra;radadd_intra_cs2H] for rate rule [R3_T;triplebond_intra_De;radadd_intra_cs2H]',
    ),
    longDesc = 
u"""
Estimated using template [R3_T;triplebond_intra;radadd_intra_cs2H] for rate rule [R3_T;triplebond_intra_De;radadd_intra_cs2H]
""",
)

entry(
    index = 877,
    label = "CH2(S)(28) + C8H7(134) <=> C9H9(152)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 878,
    label = "C5H3(168) <=> C5H3(173)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.354e+10, 's^-1'),
        n = 0.839,
        Ea = (43.638, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;Cd_rad_out_Cd;Cs_H_out_noH] for rate rule [R2H_S_cy3;Cd_rad_out_Cd;Cs_H_out_noH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;Cd_rad_out_Cd;Cs_H_out_noH] for rate rule [R2H_S_cy3;Cd_rad_out_Cd;Cs_H_out_noH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 879,
    label = "C5H3(160) <=> C5H3(173)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+10, 's^-1'),
        n = 0.98,
        Ea = (26.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;Cd_rad_out_Cd;Cs_H_out_H/OneDe] for rate rule [R2H_S_cy3;Cd_rad_out_Cd;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;Cd_rad_out_Cd;Cs_H_out_H/OneDe] for rate rule [R2H_S_cy3;Cd_rad_out_Cd;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 880,
    label = "CH3(17) + C8H6(74) <=> C9H9(153)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8780, 'cm^3/(mol*s)'),
        n = 2.878,
        Ea = (10.912, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;CsJ-HHH from training reaction 114\nExact match found for rate rule [Cb-H_Cb-H;CsJ-HHH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;CsJ-HHH from training reaction 114
Exact match found for rate rule [Cb-H_Cb-H;CsJ-HHH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 881,
    label = "C9H9(152) <=> C9H9(153)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.847e+10, 's^-1'),
        n = 1.06,
        Ea = (49.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CH3Cs(-HR!H)CJ;CsJ-(CdCdCd)H from training reaction 4\nExact match found for rate rule [CH3Cs(-HR!H)CJ;CsJ-(CdCdCd)H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
CH3Cs(-HR!H)CJ;CsJ-(CdCdCd)H from training reaction 4
Exact match found for rate rule [CH3Cs(-HR!H)CJ;CsJ-(CdCdCd)H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 882,
    label = "CH2(S)(28) + C8H7(135) <=> C9H9(153)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 883,
    label = "C5H3(141) <=> C5H3(163)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+08, 's^-1'),
        n = 1.192,
        Ea = (54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R3_T;triplebond_intra_H;radadd_intra]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R3_T;triplebond_intra_H;radadd_intra]
""",
)

entry(
    index = 884,
    label = "C5H3(163) <=> C5H3(173)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.468e+09, 's^-1'),
        n = 1.123,
        Ea = (27.577, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;Cd_rad_out;Cd_H_out_singleH] + [R4H;Cd_rad_out_Cd;XH_out] for rate rule\n[R4H_SMM;Cd_rad_out_Cd;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;Cd_rad_out;Cd_H_out_singleH] + [R4H;Cd_rad_out_Cd;XH_out] for rate rule
[R4H_SMM;Cd_rad_out_Cd;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 885,
    label = "CO2_5_(8) + CH3(17) <=> C2H3O2(80)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.608e+07, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (15.709, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cdd_Od;CsJ] for rate rule [CO2;CsJ-HHH]\nMultiplied by reaction path degeneracy 2\nEa raised from 58.6 to 65.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cdd_Od;CsJ] for rate rule [CO2;CsJ-HHH]
Multiplied by reaction path degeneracy 2
Ea raised from 58.6 to 65.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 886,
    label = "H_10_(3) + C5H4(158) <=> C5H5(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.175e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Ca;HJ from training reaction 144\nExact match found for rate rule [Cds-HH_Ca;HJ]',
    ),
    longDesc = 
u"""
Cds-HH_Ca;HJ from training reaction 144
Exact match found for rate rule [Cds-HH_Ca;HJ]
""",
)

entry(
    index = 902,
    label = "C2H(21) + C3H3(19) <=> C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Cd_rad] for rate rule [Ct_rad/Ct;Cd_allenic]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;Cd_rad] for rate rule [Ct_rad/Ct;Cd_allenic]
""",
)

entry(
    index = 903,
    label = "H_10_(3) + C5H3(141) <=> C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 904,
    label = "H_10_(3) + C5H3(162) <=> C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 942,
    label = "C5H4(177) <=> C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]
""",
)

entry(
    index = 943,
    label = "C5H4(178) <=> C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 944,
    label = "C5H5(49) <=> C5H5(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.846e+10, 's^-1'),
        n = 0.74,
        Ea = (34.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_DS;Cd_rad_out_singleH;Cs_H_out_1H] for rate rule [R3H_DS;Cd_rad_out_singleH;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3H_DS;Cd_rad_out_singleH;Cs_H_out_1H] for rate rule [R3H_DS;Cd_rad_out_singleH;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 945,
    label = "C5H5(97) <=> C5H5(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.59e+07, 's^-1'),
        n = 1.464,
        Ea = (66.316, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R3H_SD;C_rad_out_2H;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R3H_SD;C_rad_out_2H;Cd_H_out_singleDe]
""",
)

entry(
    index = 946,
    label = "C5H5(128) <=> C5H5(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (960500, 's^-1'),
        n = 1.961,
        Ea = (31.873, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [RnH;Cd_rad_out_singleDe;Cd_H_out_singleH] + [R3H;Cd_rad_out_singleDe;XH_out] for rate rule\n[R3H;Cd_rad_out_singleDe_Cd;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [RnH;Cd_rad_out_singleDe;Cd_H_out_singleH] + [R3H;Cd_rad_out_singleDe;XH_out] for rate rule
[R3H;Cd_rad_out_singleDe_Cd;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 947,
    label = "C5H5(97) <=> C5H5(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.68e+11, 's^-1'),
        n = 0.63,
        Ea = (62.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_2H;Cd_H_out_doubleC]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_2H;Cd_H_out_doubleC]
""",
)

entry(
    index = 957,
    label = "C5H3(160) <=> C5H3(175)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+11, 's^-1'),
        n = 0.12,
        Ea = (12.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleNd] for rate rule [R4_D_T;triplebond_intra_H;radadd_intra_cdsingleNd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleNd] for rate rule [R4_D_T;triplebond_intra_H;radadd_intra_cdsingleNd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 958,
    label = "H_10_(3) + C5H4(158) <=> C5H5(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.84e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.82, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ca_Cds-HH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ca_Cds-HH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 959,
    label = "H_10_(3) + C5H4(138) <=> C5H5(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.111e+09, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (5.344, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ca-Cdd_Cds-HH;HJ from training reaction 110\nExact match found for rate rule [Ca-Cdd_Cds-HH;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Ca-Cdd_Cds-HH;HJ from training reaction 110
Exact match found for rate rule [Ca-Cdd_Cds-HH;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 960,
    label = "C5H4(138) <=> C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.336e+09, 's^-1'),
        n = 0.809,
        Ea = (39.151, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CdH2_1;unsaturated_end] for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;CdH2_2]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CdH2_1;unsaturated_end] for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;CdH2_2]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 961,
    label = "H_10_(3) + C5H4(138) <=> C5H5(127)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.635e+09, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Ca;HJ from training reaction 144\nExact match found for rate rule [Cds-HH_Ca;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Cds-HH_Ca;HJ from training reaction 144
Exact match found for rate rule [Cds-HH_Ca;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 973,
    label = "H_10_(3) + C8H6(74) <=> C8H7(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.762e+07, 'cm^3/(mol*s)'),
        n = 1.95,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-R!H_Cb-H;HJ from training reaction 54\nExact match found for rate rule [Cb-R!H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Cb-R!H_Cb-H;HJ from training reaction 54
Exact match found for rate rule [Cb-R!H_Cb-H;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 991,
    label = "C8H7(147) <=> C8H7(134)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.09e+09, 's^-1'),
        n = 1.248,
        Ea = (40.811, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;C_rad_out_H/OneDe;Cs_H_out_noH] + [R2H_S;C_rad_out_H/(Cd-Cd-Cd);Cs_H_out] for rate rule [R2H_S;C_rad_out_H\n/(Cd-Cd-Cd);Cs_H_out_noH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;C_rad_out_H/OneDe;Cs_H_out_noH] + [R2H_S;C_rad_out_H/(Cd-Cd-Cd);Cs_H_out] for rate rule [R2H_S;C_rad_out_H
/(Cd-Cd-Cd);Cs_H_out_noH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 992,
    label = "C8H7(147) <=> C8H7(135)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.183e+08, 's^-1'),
        n = 1.484,
        Ea = (25.648, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CdCJ_2] + [1_3_unsaturated_pentane_backbone;CH(CJ)_1;unsaturated_end]\nfor rate rule [1_3_pentadiene;CH(CJ)_1;CdCJ_2]',
    ),
    longDesc = 
u"""
Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CdCJ_2] + [1_3_unsaturated_pentane_backbone;CH(CJ)_1;unsaturated_end]
for rate rule [1_3_pentadiene;CH(CJ)_1;CdCJ_2]
""",
)

entry(
    index = 993,
    label = "C8H7(147) <=> C8H7(136)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+07, 's^-1'),
        n = 1.292,
        Ea = (55.581, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_H/Cd;Cs_H_out] + [R4H_SDS;C_rad_out_1H;Cs_H_out] + [R4H_SDS;C_rad_out_H/OneDe;XH_out] for rate\nrule [R4H_SDS;C_rad_out_H/Cd;Cs_H_out_noH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_H/Cd;Cs_H_out] + [R4H_SDS;C_rad_out_1H;Cs_H_out] + [R4H_SDS;C_rad_out_H/OneDe;XH_out] for rate
rule [R4H_SDS;C_rad_out_H/Cd;Cs_H_out_noH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 996,
    label = "H_10_(3) + C5H3(141) <=> C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 997,
    label = "C2H(21) + C6H6(48) <=> C8H7(147)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8944, 'cm^3/(mol*s)'),
        n = 2.807,
        Ea = (11.598, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cb-H_Cb-H;CJ] for rate rule [Cb-H_Cb-H;CtJ_Ct]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using template [Cb-H_Cb-H;CJ] for rate rule [Cb-H_Cb-H;CtJ_Ct]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 1005,
    label = "H_10_(3) + R1(63) <=> C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 1048,
    label = "C3H3(19) + C4H2(111) <=> C7H5(118)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (262000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (7.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-CtHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-CtHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1050,
    label = "R1(63) <=> C8H5(181)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.933e+10, 's^-1'),
        n = 0.398,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1051,
    label = "R1(63) <=> C8H5(180)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.97e+09, 's^-1'),
        n = 0.768,
        Ea = (31.842, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;triplebond_intra_H;radadd_intra] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R4;triplebond_intra_H;radadd_intra] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1052,
    label = "H_10_(3) + C8H5(145) <=> C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 1095,
    label = "R1(63) <=> C8H5(145)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.989e+08, 's^-1'),
        n = 1.306,
        Ea = (43.343, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1097,
    label = "H_10_(3) + C8H5(144) <=> C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 1140,
    label = "R1(63) <=> C8H5(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.137e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1142,
    label = "C8H5(145) <=> C8H5(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.137e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1146,
    label = "C8H5(145) <=> C8H5(186)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (9.548, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1147,
    label = "C8H5(145) <=> C8H5(187)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (14.636, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 58.0 to 61.2 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 58.0 to 61.2 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1148,
    label = "C8H5(188) <=> C8H5(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 1149,
    label = "C4H3(96) + C4H2(111) <=> C8H5(188)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (394000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-0.44, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;CdsJ-H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;CdsJ-H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1150,
    label = "C8H5(188) <=> C8H5(196)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 1151,
    label = "C4H3(96) <=> C4H3(109)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.547e+10, 's^-1'),
        n = 0.762,
        Ea = (29.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D;multiplebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_T;triplebond_intra_H;radadd_intra_cdsingleH]\nEa raised from 124.1 to 125.1 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R4_D;multiplebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_T;triplebond_intra_H;radadd_intra_cdsingleH]
Ea raised from 124.1 to 125.1 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1171,
    label = "C8H5(188) <=> C8H5(195)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1172,
    label = "OH_12_(12) + C4H2(111) <=> C4H3O(114)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.755e+12, 'cm^3/(mol*s)'),
        n = 0.581,
        Ea = (2.274, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-De_Ct-H;OJ_pri] for rate rule [Ct-Ct_Ct-H;OJ_pri]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-De_Ct-H;OJ_pri] for rate rule [Ct-Ct_Ct-H;OJ_pri]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1173,
    label = "CH3(17) + C4H2(111) <=> C5H5(116)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (204000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (8.33, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-H;CsJ-HHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-H;CsJ-HHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1188,
    label = "C3H4(45) + C2H(21) <=> C5H5(116)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_Ct;CtJ_Ct] for rate rule [Ct-Cs_Ct-H;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_Ct;CtJ_Ct] for rate rule [Ct-Cs_Ct-H;CtJ_Ct]
""",
)

entry(
    index = 1189,
    label = "CH2(S)(28) + C4H3(96) <=> C5H5(116)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.438e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1190,
    label = "H_10_(3) + C8H5(186) <=> C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;H_rad]
""",
)

entry(
    index = 1224,
    label = "C5H3(141) + C4H2(111) <=> C9H5(165)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408400, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1225,
    label = "CH3(17) + C8H6(190) <=> C9H9(202)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3307, 'cm^3/(mol*s)'),
        n = 2.981,
        Ea = (0.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-TwoDe;CsJ-HHH] for rate rule [Cds-HH_Cds-CbCb;CsJ-HHH]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-TwoDe;CsJ-HHH] for rate rule [Cds-HH_Cds-CbCb;CsJ-HHH]
""",
)

entry(
    index = 1226,
    label = "C5H3(141) + C4H2(111) <=> C9H5(166)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408400, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1229,
    label = "H_10_(3) + C8H6(190) <=> C8H7(200)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.744e+08, 'cm^3/(mol*s)'),
        n = 1.543,
        Ea = (0.658, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-TwoDe;HJ] for rate rule [Cds-HH_Cds-CbCb;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-TwoDe;HJ] for rate rule [Cds-HH_Cds-CbCb;HJ]
""",
)

entry(
    index = 1252,
    label = "CH2(S)(28) + C8H7(200) <=> C9H9(202)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.313e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1253,
    label = "CO_21_(14) + C5H3(162) <=> C6H3O(169)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.61e+07, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (4.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]
""",
)

entry(
    index = 1256,
    label = "H_10_(3) + C8H6(190) <=> C8H7(199)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.508e+08, 'cm^3/(mol*s)'),
        n = 1.522,
        Ea = (4.177, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-TwoDe_Cds;HJ] for rate rule [Cds-CbCb_Cds;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-TwoDe_Cds;HJ] for rate rule [Cds-CbCb_Cds;HJ]
""",
)

entry(
    index = 1279,
    label = "C8H7(199) <=> C8H7(200)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.899e+11, 's^-1'),
        n = 0.486,
        Ea = (31.961, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_S;C_rad_out_2H;Cs_H_out_AromDe from training reaction 34\nExact match found for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_AromDe]',
    ),
    longDesc = 
u"""
R2H_S;C_rad_out_2H;Cs_H_out_AromDe from training reaction 34
Exact match found for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_AromDe]
""",
)

entry(
    index = 1280,
    label = "C5H3(141) <=> C5H3(161)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.027e+11, 's^-1'),
        n = 0.227,
        Ea = (64.484, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SM;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_ST_T;triplebond_intra_H;radadd_intra_cs2H]\nEa raised from 266.9 to 269.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R5_SM;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_ST_T;triplebond_intra_H;radadd_intra_cs2H]
Ea raised from 266.9 to 269.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1281,
    label = "C7H5(118) <=> C7H5(184)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (7.299, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]\nEa raised from 26.7 to 30.5 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]
Ea raised from 26.7 to 30.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1282,
    label = "C4H2(111) + C5H3(162) <=> C9H5(170)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408400, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1283,
    label = "C3H3(19) + C5H4(130) <=> C8H7(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.553, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 1284,
    label = "CH2(S)(28) + C7H5(120) <=> C8H7(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1285,
    label = "CH3(17) + C5H4(130) <=> C6H7(150)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (597000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (5.42, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cs_Ct-Ct;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cs_Ct-Ct;CsJ-HHH]
""",
)

entry(
    index = 1286,
    label = "C7H5(174) <=> C7H5(156)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.57e+10, 's^-1'),
        n = 0.43,
        Ea = (1.924, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1287,
    label = "CH2(S)(28) + C5H5(117) <=> C6H7(150)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.26e+13, 'cm^3/(mol*s)'),
        n = -0.274,
        Ea = (-0.686, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/NonDeC from training reaction 6\nExact match found for rate rule [carbene;Cd/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/NonDeC from training reaction 6
Exact match found for rate rule [carbene;Cd/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1288,
    label = "C8H7(199) <=> C8H7(203)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.124e+08, 's^-1'),
        n = 1.057,
        Ea = (26.261, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1289,
    label = "C5H3(173) <=> C5H3(176)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.864e+11, 's^-1'),
                n = 0.237,
                Ea = (55.083, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rnx_cyclics;doublebond_intra;radadd_intra_cdsingleH] for rate rule [Rn2c3_alpha;doublebond_intra;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4',
            ),
            Arrhenius(
                A = (1.297e+12, 's^-1'),
                n = 0.065,
                Ea = (55.083, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_csHCd] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rnx_cyclics;doublebond_intra;radadd_intra_cdsingleH] for rate rule [Rn2c3_alpha;doublebond_intra;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
Estimated using template [Rn;triplebond_intra_H;radadd_intra_csHCd] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1291,
    label = "C5H3(175) <=> C5H3(176)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.177e+06, 's^-1'),
        n = 2.378,
        Ea = (40.083, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;C_rad_out_noH;Cs_H_out_H/OneDe] + [R2H_S;C_rad_out_Cd/Cd;Cs_H_out] + [R2H_S_cy3;C_rad_out_noH;Cs_H_out_1H]\nfor rate rule [R2H_S_cy3;C_rad_out_Cd/Cd;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;C_rad_out_noH;Cs_H_out_H/OneDe] + [R2H_S;C_rad_out_Cd/Cd;Cs_H_out] + [R2H_S_cy3;C_rad_out_noH;Cs_H_out_1H]
for rate rule [R2H_S_cy3;C_rad_out_Cd/Cd;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1292,
    label = "H_10_(3) + C7H4(157) <=> C7H5(120)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cd_Ct-Ct;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cd_Ct-Ct;HJ]
""",
)

entry(
    index = 1293,
    label = "CH3(17) + C7H4(157) <=> C8H7(154)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (159000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (5.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cd_Ct-Ct;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cd_Ct-Ct;CsJ-HHH]
""",
)

entry(
    index = 1294,
    label = "H_10_(3) + C7H4(157) <=> C7H5(174)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.37e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-H;HJ]
""",
)

entry(
    index = 1295,
    label = "CH3(17) + C5H4(130) <=> C6H7(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (289000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (3.39, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-HHH]
""",
)

entry(
    index = 1296,
    label = "CH2(S)(28) + C5H5(127) <=> C6H7(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1297,
    label = "CH2(S)(28) + C5H5(117) <=> C6H7(151)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1310,
    label = "C7H4(205) <=> C7H4(157)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]
""",
)

entry(
    index = 1311,
    label = "C5H5(97) <=> C5H5(179)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.623e+10, 's^-1'),
        n = 0.54,
        Ea = (35.752, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SD;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SD_T;triplebond_intra_H;radadd_intra_cs2H]',
    ),
    longDesc = 
u"""
Estimated using template [R5_SD;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SD_T;triplebond_intra_H;radadd_intra_cs2H]
""",
)

entry(
    index = 1312,
    label = "C5H5(139) <=> C5H5(128)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.806e+09, 's^-1'),
        n = 1.172,
        Ea = (51.258, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R2H_S;Cd_rad_out_Cd;Cd_H_out_doubleC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R2H_S;Cd_rad_out_Cd;Cd_H_out_doubleC]
""",
)

entry(
    index = 1325,
    label = "C5H5(139) <=> C5H5(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.342e+08, 's^-1'),
        n = 1.123,
        Ea = (27.577, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;Cd_rad_out;Cd_H_out_singleH] + [R4H;Cd_rad_out_Cd;XH_out] for rate rule\n[R4H_SMM;Cd_rad_out_Cd;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;Cd_rad_out;Cd_H_out_singleH] + [R4H;Cd_rad_out_Cd;XH_out] for rate rule
[R4H_SMM;Cd_rad_out_Cd;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1332,
    label = "H_10_(3) + C5H4(138) <=> C5H5(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.036e+13, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (0.09, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Ca_Ca;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Ca_Ca;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1333,
    label = "H_10_(3) + C5H4(158) <=> C5H5(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.64, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Cd;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Cd;HJ]
""",
)

entry(
    index = 1334,
    label = "C3H3(19) + C4H2(111) <=> C7H5(119)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (98420, 'cm^3/(mol*s)'),
        n = 2.322,
        Ea = (5.632, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Ct_Ct-H;CJ] for rate rule [Ct-Ct_Ct-H;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Ct_Ct-H;CJ] for rate rule [Ct-Ct_Ct-H;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1335,
    label = "C7H5(119) <=> C7H5(118)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.428e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_5_unsaturated_hexane from training reaction 3\nExact match found for rate rule [1_5_unsaturated_hexane]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
1_5_unsaturated_hexane from training reaction 3
Exact match found for rate rule [1_5_unsaturated_hexane]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1336,
    label = "H_10_(3) + C8H5(198) <=> C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 1384,
    label = "C2H(21) + C5H4(158) <=> C7H5(119)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.154e+08, 'cm^3/(mol*s)'),
        n = 1.169,
        Ea = (3.198, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-Cd_Ct-H;CJ] for rate rule [Ct-Cd_Ct-H;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-Cd_Ct-H;CJ] for rate rule [Ct-Cd_Ct-H;CtJ_Ct]
""",
)

entry(
    index = 1386,
    label = "C8H5(198) <=> C8H5(207)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.429e+11, 's^-1'),
        n = 0.399,
        Ea = (11.439, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;doublebond_intra_2H_secDe;radadd_intra] for rate rule [R4;doublebond_intra_2H_secDe;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4;doublebond_intra_2H_secDe;radadd_intra] for rate rule [R4;doublebond_intra_2H_secDe;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1387,
    label = "C8H5(198) <=> C8H5(208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+11, 's^-1'),
        n = 0.401,
        Ea = (27.981, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra_secDe_2H;radadd_intra] + [R4;doublebond_intra_secDe;radadd_intra] for rate rule\n[R4;doublebond_intra_secDe_2H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra_secDe_2H;radadd_intra] + [R4;doublebond_intra_secDe;radadd_intra] for rate rule
[R4;doublebond_intra_secDe_2H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1388,
    label = "C8H5(207) <=> C8H5(208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.562e+08, 's^-1'),
        n = 1.057,
        Ea = (15.061, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1389,
    label = "C8H5(210) <=> C8H5(208)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.072e+09, 's^-1'),
        n = 1.156,
        Ea = (33.922, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_noH] for rate rule [R2H_S_cy4;C_rad_out_H/Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_noH] for rate rule [R2H_S_cy4;C_rad_out_H/Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1390,
    label = "H_10_(3) + CH2(T)(24) <=> CH3(17)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.13e+13, 'cm^3/(mol*s)'), n=0.32, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.39e+34, 'cm^6/(mol^2*s)'),
            n = -5.04,
            Ea = (7.4, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.405,
        T3 = (258, 'K'),
        T1 = (2810, 'K'),
        T2 = (9910, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1461,
    label = "C6H7(150) <=> C6H7(204)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (816000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1462,
    label = "CH2(S)(28) + C5H5(128) <=> C6H7(204)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1463,
    label = "CH3(17) + C5H4(138) <=> C6H7(204)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (7.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ca_Cds-HH;CsJ-HHH] for rate rule [Ca-Cdd_Cds-HH;CsJ-HHH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Ca_Cds-HH;CsJ-HHH] for rate rule [Ca-Cdd_Cds-HH;CsJ-HHH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1465,
    label = "C7H5(164) <=> C7H5(171)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7_DSSM_T;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7_DSSM_T;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1466,
    label = "OH_12_(12) + C4H2(111) <=> C4H3O(115)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.843e+11, 'cm^3/(mol*s)'),
        n = 0.474,
        Ea = (-0.492, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 193 C4H2 + HO <=> C4H3O in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 193 C4H2 + HO <=> C4H3O in R_Addition_MultipleBond/training
""",
)

entry(
    index = 1467,
    label = "C7H5(164) <=> C7H5(172)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1468,
    label = "CO_21_(14) + C3H3(19) <=> C4H3O(87)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_birad;R_H] for rate rule [CO_birad;Ct_H]',
    ),
    longDesc = 
u"""
Estimated using template [CO_birad;R_H] for rate rule [CO_birad;Ct_H]
""",
)

entry(
    index = 1469,
    label = "C4H3O(89) <=> C4H3O(87)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.502e+11, 's^-1'),
        n = 0.754,
        Ea = (55.452, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R2H_S;CO_rad_out;Cd_H_out_doubleC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R2H_S;CO_rad_out;Cd_H_out_doubleC]
""",
)

entry(
    index = 1470,
    label = "C4H3O(115) <=> C4H3O(87)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (136000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;Cd_rad_out_singleH;XH_out] for rate rule [R5H;Cd_rad_out_singleH;O_H_out]',
    ),
    longDesc = 
u"""
Estimated using template [R5H;Cd_rad_out_singleH;XH_out] for rate rule [R5H;Cd_rad_out_singleH;O_H_out]
""",
)

entry(
    index = 1471,
    label = "O_11_(7) + C4H3(110) <=> C4H3O(87)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [Cd_pri_rad;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [Cd_pri_rad;Oa]
""",
)

entry(
    index = 1472,
    label = "C8H7(75) <=> C8H7(155)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.989e+08, 's^-1'),
        n = 1.306,
        Ea = (43.343, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1473,
    label = "C8H7(155) <=> C8H7(199)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.404e+08, 's^-1'),
        n = 0.746,
        Ea = (12.523, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra_2H_pri;radadd_intra_Cb] + [R6;doublebond_intra_2H_pri;radadd_intra] for rate rule\n[R6;doublebond_intra_2H_pri;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 51.6 to 52.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra_2H_pri;radadd_intra_Cb] + [R6;doublebond_intra_2H_pri;radadd_intra] for rate rule
[R6;doublebond_intra_2H_pri;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 51.6 to 52.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1477,
    label = "CO_21_(14) + CH2(T)(24) <=> CH2CO(16)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8.1e+11, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (4.51, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7.095, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.591,
        T3 = (275, 'K'),
        T1 = (1230, 'K'),
        T2 = (5180, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.7},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1484,
    label = "C2H(21) + CH2CO(16) <=> C4H3O(88)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.832e+09, 'cm^3/(mol*s)'),
        n = 1.415,
        Ea = (4.792, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CtJ_Ct]
""",
)

entry(
    index = 1485,
    label = "C8H7(155) <=> C8H7(203)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.966e+12, 's^-1'),
        n = -0.321,
        Ea = (38.193, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;doublebond_intra_pri_2H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 155.9 to 159.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;doublebond_intra_pri_2H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 155.9 to 159.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1486,
    label = "C8H7(155) <=> C8H7(211)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.262e+10, 's^-1'),
        n = 0.537,
        Ea = (7.728, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingle] for rate rule\n[R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingle] for rate rule
[R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1487,
    label = "H_10_(3) + CH2CO(16) <=> CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+08, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (2.627, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Ketene_related
""",
)

entry(
    index = 1489,
    label = "CH3CO(18) <=> CO_21_(14) + CH3(17)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(16.895, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.65e+18, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (14.585, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.36,
        T3 = (122, 'K'),
        T1 = (50000, 'K'),
        T2 = (16900, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1498,
    label = "O_11_(7) + CH3CO(18) <=> C2H3O2(80)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [CO_rad/NonDe;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [CO_rad/NonDe;Oa]
""",
)

entry(
    index = 1516,
    label = "CH3(17) + C8H6(190) <=> C9H9(201)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8695, 'cm^3/(mol*s)'),
        n = 2.506,
        Ea = (6.139, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-TwoDe_Cds;CsJ-HHH] for rate rule [Cds-CbCb_Cds;CsJ-HHH]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-TwoDe_Cds;CsJ-HHH] for rate rule [Cds-CbCb_Cds;CsJ-HHH]
""",
)

entry(
    index = 1517,
    label = "C9H9(201) <=> C9H9(202)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.98e+08, 's^-1'),
        n = 1.36,
        Ea = (37.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CH3Cs(-R!HR!H)CJ;CsJ-HH from training reaction 3\nExact match found for rate rule [CH3Cs(-R!HR!H)CJ;CsJ-HH]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
CH3Cs(-R!HR!H)CJ;CsJ-HH from training reaction 3
Exact match found for rate rule [CH3Cs(-R!HR!H)CJ;CsJ-HH]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1521,
    label = "H2_13_(2) + CH(D)(23) <=> CH3(17)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.13e+13, 'cm^3/(mol*s)'), n=0.15, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.43e+22, 'cm^6/(mol^2*s)'),
            n = -1.6,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.514,
        T3 = (152, 'K'),
        T1 = (22800, 'K'),
        T2 = (10400, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[He]': 0.7, '[C-]#[O+]': 1.5, '[Ar]': 0.71},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1537,
    label = "CH2(S)(28) + C8H7(199) <=> C9H9(201)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.438e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1540,
    label = "CH(Q)(33) <=> CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.85, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1555,
    label = "CH3(17) + C8H5(186) <=> C9H8(192)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methyl;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_methyl;Cd_pri_rad]
""",
)

entry(
    index = 1556,
    label = "H_10_(3) + C9H8(192) <=> C9H9(202)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.494e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-0.26, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CsH_Cds-TwoDe;HJ] for rate rule [Cds-CsH_Cds-CbCb;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CsH_Cds-TwoDe;HJ] for rate rule [Cds-CsH_Cds-CbCb;HJ]
""",
)

entry(
    index = 1557,
    label = "CH2(S)(28) + C8H6(190) <=> C9H8(192)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd_pri from training reaction 5\nExact match found for rate rule [carbene;Cd_pri]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd_pri from training reaction 5
Exact match found for rate rule [carbene;Cd_pri]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1572,
    label = "C6H5(64) + C4H2(111) <=> C10H7(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.667e+06, 'cm^3/(mol*s)'),
        n = 2.038,
        Ea = (-0.857, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 194 C4H2 + C6H5 <=> C10H7-8 in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 194 C4H2 + C6H5 <=> C10H7-8 in R_Addition_MultipleBond/training
""",
)

entry(
    index = 1573,
    label = "H_10_(3) + C10H6(212) <=> C10H7(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.61e+09, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (3.486, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Ct-De_Ct-De;HJ]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Ct-De_Ct-De;HJ]
""",
)

entry(
    index = 1589,
    label = "C10H6(214) <=> C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 1590,
    label = "C8H5(182) <=> R1(63)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6_DSM_T;triplebond_intra_De;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6_DSM_T;triplebond_intra_De;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1591,
    label = "C8H5(182) <=> C8H5(216)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1592,
    label = "C8H5(182) <=> C8H5(215)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6_DSM_T;triplebond_intra_De;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6_DSM_T;triplebond_intra_De;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1593,
    label = "C8H5(182) <=> C8H5(217)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1594,
    label = "C8H5(217) <=> C8H5(195)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.36e+07, 's^-1'),
        n = 1.464,
        Ea = (66.316, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_SD;Y_rad_out;Cd_H_out_singleDe] for rate rule [R3H_SD;Cd_rad_out_double;Cd_H_out_singleDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R3H_SD;Y_rad_out;Cd_H_out_singleDe] for rate rule [R3H_SD;Cd_rad_out_double;Cd_H_out_singleDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1595,
    label = "CO2_5_(8) + C8H5(186) <=> S(191)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 1.979,
        Ea = (5.066, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R_R;CdsJ-(CdCb)H] for rate rule [Od_Cdd-Od;CdsJ-(CdCb)H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R_R;CdsJ-(CdCb)H] for rate rule [Od_Cdd-Od;CdsJ-(CdCb)H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1596,
    label = "C2H2(20) + C8H5(186) <=> C10H7(193)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+06, 'cm^3/(mol*s)'),
        n = 1.979,
        Ea = (5.066, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-H_Ct-H;CdsJ-(CdCb)H from training reaction 174\nExact match found for rate rule [Ct-H_Ct-H;CdsJ-(CdCb)H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Ct-H_Ct-H;CdsJ-(CdCb)H from training reaction 174
Exact match found for rate rule [Ct-H_Ct-H;CdsJ-(CdCb)H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1597,
    label = "C10H7(220) <=> C10H7(193)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (239900, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H_RSMSR;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H_RSMSR;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1598,
    label = "C10H7(220) <=> C10H7(226)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.949e+12, 's^-1'),
        n = -0.321,
        Ea = (5.655, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R6_MSR_D;doublebond_intra_pri_2H;radadd_intra_Cb from training reaction 55\nExact match found for rate rule [R6_MSR_D;doublebond_intra_pri_2H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
R6_MSR_D;doublebond_intra_pri_2H;radadd_intra_Cb from training reaction 55
Exact match found for rate rule [R6_MSR_D;doublebond_intra_pri_2H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1599,
    label = "C10H7(227) <=> C10H7(226)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.358e+08, 's^-1'),
        n = 1.684,
        Ea = (33.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_S;C_rad_out_H/Cb;Cs_H_out_H/Cd/C/Cb from training reaction 86\nExact match found for rate rule [R2H_S;C_rad_out_H/Cb;Cs_H_out_H/Cd/C/Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
R2H_S;C_rad_out_H/Cb;Cs_H_out_H/Cd/C/Cb from training reaction 86
Exact match found for rate rule [R2H_S;C_rad_out_H/Cb;Cs_H_out_H/Cd/C/Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1600,
    label = "C10H7(229) <=> C10H7(227)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.371e+11, 's^-1'),
        n = 0.43,
        Ea = (1.924, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R6_DSB_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH from training reaction 80\nExact match found for rate rule [R6_DSB_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
R6_DSB_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH from training reaction 80
Exact match found for rate rule [R6_DSB_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1601,
    label = "C10H7(229) <=> C10H7(232)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_DSMS;Cd_rad_out_singleH;XH_out] for rate rule [R5H_DSMS;Cd_rad_out_singleH;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R5H_DSMS;Cd_rad_out_singleH;XH_out] for rate rule [R5H_DSMS;Cd_rad_out_singleH;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1602,
    label = "C10H7(227) <=> C10H7(228)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.53e+12, 's^-1'),
        n = 0.189,
        Ea = (29.234, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [2-hydro-nathphalene;doublebond_intra;radadd_intra_csHCb] for rate rule [2-hydro-\nnathphalene;doublebond_intra_DeDe_pri;radadd_intra_csHCb]',
    ),
    longDesc = 
u"""
Estimated using template [2-hydro-nathphalene;doublebond_intra;radadd_intra_csHCb] for rate rule [2-hydro-
nathphalene;doublebond_intra_DeDe_pri;radadd_intra_csHCb]
""",
)

entry(
    index = 1603,
    label = "C2H2(20) + C8H5(198) <=> C10H7(209)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26800, 'cm^3/(mol*s)'),
        n = 2.499,
        Ea = (1.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-H_Ct-H;CbJ from training reaction 113\nExact match found for rate rule [Ct-H_Ct-H;CbJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Ct-H_Ct-H;CbJ from training reaction 113
Exact match found for rate rule [Ct-H_Ct-H;CbJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1604,
    label = "C10H7(209) <=> C10H7(229)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.912e+11, 's^-1'),
        n = 0.86,
        Ea = (45.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_singleH] for rate rule [R6H_RSMSR;Cd_rad_out_singleH;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_singleH] for rate rule [R6H_RSMSR;Cd_rad_out_singleH;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1605,
    label = "C10H7(209) <=> C10H7(232)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+07, 's^-1'),
        n = 1.425,
        Ea = (7.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb from training reaction 81\nExact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb]',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb from training reaction 81
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb]
""",
)

entry(
    index = 1606,
    label = "C10H7(209) <=> C10H7(238)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.371e+11, 's^-1'),
        n = 0.43,
        Ea = (1.924, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSB_D;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R6_DSB_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSB_D;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R6_DSB_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1607,
    label = "C10H7(209) <=> C10H7(237)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.524e+10, 's^-1'),
        n = 0.537,
        Ea = (2.307, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_D;doublebond_intra_2H;radadd_intra_cdsingleH] for rate rule\n[R6_DSM_D;doublebond_intra_2H_secDe;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_D;doublebond_intra_2H;radadd_intra_cdsingleH] for rate rule
[R6_DSM_D;doublebond_intra_2H_secDe;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1608,
    label = "C10H7(238) <=> C10H7(239)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.53e+12, 's^-1'),
        n = 0.189,
        Ea = (29.234, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [2-hydro-nathphalene;doublebond_intra_HDe_pri;radadd_intra_cs] for rate rule [2-hydro-\nnathphalene;doublebond_intra_HDe_pri;radadd_intra_csDeDe]',
    ),
    longDesc = 
u"""
Estimated using template [2-hydro-nathphalene;doublebond_intra_HDe_pri;radadd_intra_cs] for rate rule [2-hydro-
nathphalene;doublebond_intra_HDe_pri;radadd_intra_csDeDe]
""",
)

entry(
    index = 1609,
    label = "C10H7(237) <=> C10H7(239)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.035e+11, 's^-1'),
        n = 0.535,
        Ea = (9.58, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Rn1c5_alpha_benzene;doublebond_intra_HDe_pri;radadd_intra_cs2H from training reaction 69\nExact match found for rate rule [Rn1c5_alpha_benzene;doublebond_intra_HDe_pri;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Rn1c5_alpha_benzene;doublebond_intra_HDe_pri;radadd_intra_cs2H from training reaction 69
Exact match found for rate rule [Rn1c5_alpha_benzene;doublebond_intra_HDe_pri;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1610,
    label = "C10H7(242) <=> C10H7(237)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.507e+09, 's^-1'),
        n = 0.63,
        Ea = (19.43, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra_2H;radadd_intra_Cb] + [Rn;doublebond_intra_2H_secDe;radadd_intra] +\n[R6;doublebond_intra_2H;radadd_intra] for rate rule [R6;doublebond_intra_2H_secDe;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4\nEa raised from 76.9 to 81.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra_2H;radadd_intra_Cb] + [Rn;doublebond_intra_2H_secDe;radadd_intra] +
[R6;doublebond_intra_2H;radadd_intra] for rate rule [R6;doublebond_intra_2H_secDe;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
Ea raised from 76.9 to 81.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1611,
    label = "H_10_(3) + C10H6(235) <=> C10H7(232)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.905e+09, 'cm^3/(mol*s)'),
        n = 1.589,
        Ea = (2.838, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct-H_Ct-De;HJ] + [Ct-H_Ct-Cb;YJ] for rate rule [Ct-H_Ct-Cb;HJ]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct-H_Ct-De;HJ] + [Ct-H_Ct-Cb;YJ] for rate rule [Ct-H_Ct-Cb;HJ]
""",
)

entry(
    index = 1612,
    label = "H_10_(3) + C10H6(235) <=> C10H7(209)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.775e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (6.896, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cb_Ct-H;HJ from training reaction 187\nExact match found for rate rule [Ct-Cb_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Ct-Cb_Ct-H;HJ from training reaction 187
Exact match found for rate rule [Ct-Cb_Ct-H;HJ]
""",
)

entry(
    index = 1613,
    label = "C2H(21) + C8H5(198) <=> C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Cb_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Cb_rad]
""",
)

entry(
    index = 1654,
    label = "C10H6(243) <=> C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 1655,
    label = "C10H7(220) <=> C10H7(224)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.969e+10, 's^-1'),
        n = 0.373,
        Ea = (18.396, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_MSR;doublebond_intra_2H_pri;radadd_intra] for rate rule [R6_MSR;doublebond_intra_2H_pri;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6_MSR;doublebond_intra_2H_pri;radadd_intra] for rate rule [R6_MSR;doublebond_intra_2H_pri;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1656,
    label = "C10H7(229) <=> C10H7(224)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.524e+10, 's^-1'),
        n = 0.537,
        Ea = (18.326, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH from training reaction 68\nExact match found for rate rule [R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH from training reaction 68
Exact match found for rate rule [R6_DSM_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1657,
    label = "C10H7(224) <=> C10H7(228)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.354e+10, 's^-1'),
        n = 0.185,
        Ea = (8.367, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn1c5_alpha;doublebond_intra_DeDe_pri;radadd_intra_cs2H] for rate rule\n[Rn1c5_alpha_benzene;doublebond_intra_DeDe_pri;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Rn1c5_alpha;doublebond_intra_DeDe_pri;radadd_intra_cs2H] for rate rule
[Rn1c5_alpha_benzene;doublebond_intra_DeDe_pri;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1658,
    label = "C10H7(193) <=> C10H7(218)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.547e+10, 's^-1'),
        n = 0.762,
        Ea = (22.305, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D_D;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_DeDe_pri;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R4_D_D;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_DeDe_pri;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1660,
    label = "H_10_(3) + C10H6(235) <=> C10H7(246)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.744e+08, 'cm^3/(mol*s)'),
        n = 1.543,
        Ea = (0.658, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-TwoDe;HJ] for rate rule [Cds-HH_Cds-CbCb;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-TwoDe;HJ] for rate rule [Cds-HH_Cds-CbCb;HJ]
""",
)

entry(
    index = 1680,
    label = "C10H7(232) <=> C10H7(234)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (195300, 's^-1'),
        n = 2.209,
        Ea = (29.053, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47\nExact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47
Exact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1681,
    label = "C10H7(209) <=> C10H7(234)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.745e+06, 's^-1'),
        n = 1.697,
        Ea = (19.915, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70\nExact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70
Exact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1682,
    label = "C10H7(234) <=> C10H7(248)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.429e+11, 's^-1'),
        n = 0.399,
        Ea = (11.439, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;doublebond_intra_2H_secDe;radadd_intra] for rate rule [R4;doublebond_intra_2H_secDe;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4;doublebond_intra_2H_secDe;radadd_intra] for rate rule [R4;doublebond_intra_2H_secDe;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1683,
    label = "C10H7(246) <=> C10H7(247)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.885e+11, 's^-1'),
        n = 0.481,
        Ea = (30.309, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csNdDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csNdDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1684,
    label = "C10H7(231) <=> C10H7(229)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (9.548, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1685,
    label = "C10H7(230) <=> C10H7(229)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (9.548, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1687,
    label = "H_10_(3) + C10H6(235) <=> C10H7(245)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.508e+08, 'cm^3/(mol*s)'),
        n = 1.522,
        Ea = (4.177, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-TwoDe_Cds;HJ] for rate rule [Cds-CbCb_Cds;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-TwoDe_Cds;HJ] for rate rule [Cds-CbCb_Cds;HJ]
""",
)

entry(
    index = 1707,
    label = "C10H7(245) <=> C10H7(246)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.899e+11, 's^-1'),
        n = 0.486,
        Ea = (31.961, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_S;C_rad_out_2H;Cs_H_out_AromDe from training reaction 34\nExact match found for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_AromDe]',
    ),
    longDesc = 
u"""
R2H_S;C_rad_out_2H;Cs_H_out_AromDe from training reaction 34
Exact match found for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_AromDe]
""",
)

entry(
    index = 1708,
    label = "C10H7(240) <=> C10H7(238)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.24e+09, 's^-1'),
        n = 0.924,
        Ea = (30.972, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_RSR;Cd_rad_out_singleDe_Cb;XH_out] for rate rule [R4H_DSS;Cd_rad_out_singleDe_Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R4H_RSR;Cd_rad_out_singleDe_Cb;XH_out] for rate rule [R4H_DSS;Cd_rad_out_singleDe_Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1709,
    label = "C10H7(245) <=> C10H7(240)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.508e+10, 's^-1'),
        n = 0.298,
        Ea = (15.205, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_SSM;multiplebond_intra;radadd_intra_cs] for rate rule [R6_SSM_T;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R6_SSM;multiplebond_intra;radadd_intra_cs] for rate rule [R6_SSM_T;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1710,
    label = "C10H7(193) <=> C10H7(222)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.767e+11, 's^-1'),
        n = 0.248,
        Ea = (19.557, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D_D;doublebond_intra_pri;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_pri_DeDe;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R4_D_D;doublebond_intra_pri;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_pri_DeDe;radadd_intra_cdsingleH]
""",
)

entry(
    index = 1711,
    label = "C10H7(248) <=> C10H7(251)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.086e+10, 's^-1'),
        n = 0.306,
        Ea = (9.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_SSM_D;doublebond_intra_pri_2H;radadd_intra_cs] for rate rule [R6_SSM_D;doublebond_intra_pri_2H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6_SSM_D;doublebond_intra_pri_2H;radadd_intra_cs] for rate rule [R6_SSM_D;doublebond_intra_pri_2H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1712,
    label = "C10H7(232) <=> C10H7(236)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.071e+11, 's^-1'),
        n = 0.542,
        Ea = (29.862, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SM;doublebond_intra_secDe_2H;radadd_intra] for rate rule [R5_SB;doublebond_intra_secDe_2H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5_SM;doublebond_intra_secDe_2H;radadd_intra] for rate rule [R5_SB;doublebond_intra_secDe_2H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1713,
    label = "C10H7(237) <=> C10H7(241)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.386e+12, 's^-1'),
        n = 0.06,
        Ea = (19.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc5_beta_long;doublebond_intra;radadd_intra_cs2H] for rate rule [Rn1c5_beta_long;doublebond_intra;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc5_beta_long;doublebond_intra;radadd_intra_cs2H] for rate rule [Rn1c5_beta_long;doublebond_intra;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1714,
    label = "C10H7(224) <=> C10H7(241)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.386e+12, 's^-1'),
        n = 0.06,
        Ea = (19.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc5_beta_long;doublebond_intra;radadd_intra_cs2H] for rate rule [Rn1c5_beta_long;doublebond_intra;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc5_beta_long;doublebond_intra;radadd_intra_cs2H] for rate rule [Rn1c5_beta_long;doublebond_intra;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1715,
    label = "C10H7(220) <=> C10H7(223)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.198e+11, 's^-1'),
        n = 0.54,
        Ea = (28.053, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;doublebond_intra_HDe_secDe;radadd_intra] for rate rule [R4;doublebond_intra_HDe_secDe;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4;doublebond_intra_HDe_secDe;radadd_intra] for rate rule [R4;doublebond_intra_HDe_secDe;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1716,
    label = "C10H7(220) <=> C10H7(225)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.56e+11, 's^-1'),
        n = 0.26,
        Ea = (26.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;doublebond_intra_secDe;radadd_intra] for rate rule [R4;doublebond_intra_secDe_HCd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4;doublebond_intra_secDe;radadd_intra] for rate rule [R4;doublebond_intra_secDe_HCd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1717,
    label = "C10H7(223) <=> C10H7(225)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.497e+08, 's^-1'),
        n = 1.079,
        Ea = (21.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4-Cs-Cb;rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4-Cs-Cb;rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1718,
    label = "C8H5(185) <=> C8H5(181)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.946e+09, 's^-1'),
                n = 0.774,
                Ea = (45.713, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CddC_2] + [1_3_unsaturated_pentane_backbone;CH=C_1;unsaturated_end] for\nrate rule [1_3_pentadiene;CH=C_1;CddC_2]',
            ),
            Arrhenius(
                A = (4.192e+09, 's^-1'),
                n = 0.924,
                Ea = (30.972, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R4H_DSD;Cd_rad_out_singleDe;Cd_H_out_single] for rate rule [R4H_DSD;Cd_rad_out_singleDe_Cd;Cd_H_out_singleDe]\nMultiplied by reaction path degeneracy 4',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CddC_2] + [1_3_unsaturated_pentane_backbone;CH=C_1;unsaturated_end] for
rate rule [1_3_pentadiene;CH=C_1;CddC_2]
Estimated using template [R4H_DSD;Cd_rad_out_singleDe;Cd_H_out_single] for rate rule [R4H_DSD;Cd_rad_out_singleDe_Cd;Cd_H_out_singleDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1720,
    label = "C8H5(185) <=> C8H5(210)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.545e+11, 's^-1'),
        n = 0.251,
        Ea = (23.246, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnx_cyclics;doublebond_intra_HDe_pri;radadd_intra] for rate rule [Rn3c4_alpha;doublebond_intra_HDe_pri;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Rnx_cyclics;doublebond_intra_HDe_pri;radadd_intra] for rate rule [Rn3c4_alpha;doublebond_intra_HDe_pri;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1721,
    label = "C10H7(232) <=> C10H7(233)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.885e+11, 's^-1'),
        n = 0.481,
        Ea = (30.309, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;doublebond_intra_2H;radadd_intra] for rate rule [R5_SB;doublebond_intra_2H_secDe;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;doublebond_intra_2H;radadd_intra] for rate rule [R5_SB;doublebond_intra_2H_secDe;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1722,
    label = "C10H7(247) <=> C10H7(233)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.445e+07, 's^-1'),
        n = 1.778,
        Ea = (22.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_RSR;Cd_rad_out_singleH;XH_out] for rate rule [R4H_DSS;Cd_rad_out_singleH;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 9',
    ),
    longDesc = 
u"""
Estimated using template [R4H_RSR;Cd_rad_out_singleH;XH_out] for rate rule [R4H_DSS;Cd_rad_out_singleH;Cs_H_out_2H]
Multiplied by reaction path degeneracy 9
""",
)

entry(
    index = 1723,
    label = "H_10_(3) + C6H4(121) <=> C6H5(64)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.984e+14, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cd_Ct-Cd_cyc6;HJ from training reaction 191\nExact match found for rate rule [Ct-Cd_Ct-Cd_cyc6;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Ct-Cd_Ct-Cd_cyc6;HJ from training reaction 191
Exact match found for rate rule [Ct-Cd_Ct-Cd_cyc6;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1730,
    label = "C2H3(29) + C6H4(121) <=> C8H7(75)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16420, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (1.99, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cd_Ct-Cd;CdsJ-H] for rate rule [Ct-Cd_Ct-Cd_cyc6;CdsJ-H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cd_Ct-Cd;CdsJ-H] for rate rule [Ct-Cd_Ct-Cd_cyc6;CdsJ-H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1731,
    label = "C2H(21) + C6H4(121) <=> R1(63)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10470, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.953, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cd_Ct-Cd;CJ] for rate rule [Ct-Cd_Ct-Cd_cyc6;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cd_Ct-Cd;CJ] for rate rule [Ct-Cd_Ct-Cd_cyc6;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1736,
    label = "C6H4(257) <=> C6H4(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2C;CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2C;CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1737,
    label = "C5H5(179) <=> C5H5(206)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.41e+10, 's^-1'),
        n = 0.21,
        Ea = (12.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5_DS_D;doublebond_intra;radadd_intra]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5_DS_D;doublebond_intra;radadd_intra]
""",
)

entry(
    index = 1738,
    label = "C10H7(234) <=> C10H7(249)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+11, 's^-1'),
        n = 0.401,
        Ea = (27.981, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra_secDe_2H;radadd_intra] + [R4;doublebond_intra_secDe;radadd_intra] for rate rule\n[R4;doublebond_intra_secDe_2H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra_secDe_2H;radadd_intra] + [R4;doublebond_intra_secDe;radadd_intra] for rate rule
[R4;doublebond_intra_secDe_2H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1739,
    label = "C10H7(248) <=> C10H7(249)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.562e+08, 's^-1'),
        n = 1.057,
        Ea = (15.061, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1740,
    label = "C8H5(183) <=> R1(63)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1741,
    label = "C8H5(183) <=> C8H5(196)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1742,
    label = "C8H5(196) <=> C8H5(197)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.64e+11, 's^-1'),
        n = 0.3,
        Ea = (16.232, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule\n[Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2\nEa raised from 66.3 to 67.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule
[Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
Ea raised from 66.3 to 67.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1743,
    label = "C10H7(250) <=> C10H7(248)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.632e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SMSS;Cd_rad_out_Cd;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using template [R5H;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SMSS;Cd_rad_out_Cd;Cs_H_out_2H]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 1744,
    label = "C10H7(231) <=> C10H7(252)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (17.609, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1745,
    label = "C10H7(230) <=> C10H7(252)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (17.609, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1746,
    label = "C10H7(231) <=> C10H7(253)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (17.609, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 2\nEa raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 2
Ea raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1747,
    label = "C10H7(230) <=> C10H7(253)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (17.609, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 2\nEa raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 2
Ea raised from 68.2 to 73.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1748,
    label = "C10H7(125) <=> C10H7(213)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (29.257, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;CddC_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CddC_2]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (1.774e+11, 's^-1'),
                n = 0.174,
                Ea = (22.718, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rnxc6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingle] for rate rule\n[Rn2c6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 92.8 to 95.1 kJ/mol to match endothermicity of reaction.',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;CddC_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CddC_2]
Multiplied by reaction path degeneracy 2
Estimated using template [Rnxc6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingle] for rate rule
[Rn2c6_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 92.8 to 95.1 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1750,
    label = "C8H7(134) <=> C8H7(159)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.774e+11, 's^-1'),
                n = 0.174,
                Ea = (10.324, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rnxc6;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule\n[Rn2c6_beta_short;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (1.297e+12, 's^-1'),
                n = 0.065,
                Ea = (27.941, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'R5_SS_T;triplebond_intra_H;radadd_intra_csH(CdCdCd) from training reaction 59\nExact match found for rate rule [R5_SS_T;triplebond_intra_H;radadd_intra_csH(CdCdCd)]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rnxc6;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] for rate rule
[Rn2c6_beta_short;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
R5_SS_T;triplebond_intra_H;radadd_intra_csH(CdCdCd) from training reaction 59
Exact match found for rate rule [R5_SS_T;triplebond_intra_H;radadd_intra_csH(CdCdCd)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1752,
    label = "C8H5(188) <=> C8H5(194)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (12.305, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]\nEa raised from 46.9 to 51.5 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_H;radadd_intra_cdsingleH]
Ea raised from 46.9 to 51.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1753,
    label = "C2H2(20) + C8H5(144) <=> C10H7(189)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26800, 'cm^3/(mol*s)'),
        n = 2.499,
        Ea = (1.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-H_Ct-H;CbJ from training reaction 113\nExact match found for rate rule [Ct-H_Ct-H;CbJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Ct-H_Ct-H;CbJ from training reaction 113
Exact match found for rate rule [Ct-H_Ct-H;CbJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1754,
    label = "C10H7(189) <=> C10H7(230)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+06, 's^-1'),
        n = 1.697,
        Ea = (19.915, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70\nExact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70
Exact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1759,
    label = "C10H7(189) <=> C10H7(258)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (8.296, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2\nEa raised from 28.5 to 34.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
Ea raised from 28.5 to 34.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1760,
    label = "C10H7(254) <=> C10H7(230)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130200, 's^-1'),
        n = 2.209,
        Ea = (29.053, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47\nExact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47
Exact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1761,
    label = "C10H7(189) <=> C10H7(254)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+07, 's^-1'),
        n = 1.425,
        Ea = (7.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb from training reaction 81\nExact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb]',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb from training reaction 81
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_Cb]
""",
)

entry(
    index = 1762,
    label = "C10H7(263) <=> C10H7(258)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.288e+09, 's^-1'),
        n = 0.924,
        Ea = (30.972, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4H_DSD;Cd_rad_out_singleDe_Cb;Cd_H_out_singleH from training reaction 48\nExact match found for rate rule [R4H_DSD;Cd_rad_out_singleDe_Cb;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
R4H_DSD;Cd_rad_out_singleDe_Cb;Cd_H_out_singleH from training reaction 48
Exact match found for rate rule [R4H_DSD;Cd_rad_out_singleDe_Cb;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1763,
    label = "C10H7(254) <=> C10H7(263)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.646e+10, 's^-1'),
        n = 0.358,
        Ea = (8.296, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 2\nEa raised from 28.5 to 34.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 2
Ea raised from 28.5 to 34.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1764,
    label = "H_10_(3) + C10H6(260) <=> C10H7(189)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (6.896, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cb_Ct-H;HJ from training reaction 187\nExact match found for rate rule [Ct-Cb_Ct-H;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Ct-Cb_Ct-H;HJ from training reaction 187
Exact match found for rate rule [Ct-Cb_Ct-H;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1765,
    label = "H_10_(3) + C10H6(260) <=> C10H7(254)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.81e+09, 'cm^3/(mol*s)'),
        n = 1.589,
        Ea = (2.838, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct-H_Ct-De;HJ] + [Ct-H_Ct-Cb;YJ] for rate rule [Ct-H_Ct-Cb;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct-H_Ct-De;HJ] + [Ct-H_Ct-Cb;YJ] for rate rule [Ct-H_Ct-Cb;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1766,
    label = "C2H(21) + C8H5(144) <=> C10H6(260)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Ct_rad/Ct] for rate rule [Cb_rad;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Ct_rad/Ct] for rate rule [Cb_rad;Ct_rad/Ct]
""",
)

entry(
    index = 1795,
    label = "C10H6(265) <=> C10H6(260)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 1796,
    label = "C10H7(189) <=> C10H7(261)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12, 's^-1'),
        n = 0.045,
        Ea = (17.255, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1797,
    label = "C10H7(254) <=> C10H7(264)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.339e+10, 's^-1'),
        n = 0.298,
        Ea = (15.205, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_SSM;multiplebond_intra;radadd_intra_csHCd] for rate rule [R6_SSM_T;triplebond_intra_H;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6_SSM;multiplebond_intra;radadd_intra_csHCd] for rate rule [R6_SSM_T;triplebond_intra_H;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1798,
    label = "C10H7(189) <=> C10H7(262)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.774e+11, 's^-1'),
        n = 0.174,
        Ea = (15.034, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc6_alpha;doublebond_intra;radadd_intra_cdsingleH] for rate rule\n[Rn2c6_alpha;doublebond_intra_DeDe_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2\nEa raised from 60.2 to 62.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc6_alpha;doublebond_intra;radadd_intra_cdsingleH] for rate rule
[Rn2c6_alpha;doublebond_intra_DeDe_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
Ea raised from 60.2 to 62.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1799,
    label = "C10H6(260) <=> C10H6(266)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.062e+14, 's^-1'),
        n = -0.215,
        Ea = (69.177, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'linear_1_3_hexadien_5_yne from training reaction 1\nExact match found for rate rule [linear_1_3_hexadien_5_yne]\nMultiplied by reaction path degeneracy 4\nEa raised from 286.6 to 289.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
linear_1_3_hexadien_5_yne from training reaction 1
Exact match found for rate rule [linear_1_3_hexadien_5_yne]
Multiplied by reaction path degeneracy 4
Ea raised from 286.6 to 289.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1800,
    label = "C8H7(131) <=> C8H7(133)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (8.251e+10, 's^-1'),
                n = 0.634,
                Ea = (44.066, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R5;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule [R5_SD_D;doublebond_intra_HCd_pri;radadd_intra_csHCd]',
            ),
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (29.257, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [R5;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule [R5_SD_D;doublebond_intra_HCd_pri;radadd_intra_csHCd]
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1802,
    label = "OH_12_(12) + C8H6(74) <=> C8H7O(148)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.773e+11, 'cm^3/(mol*s)'),
        n = 0.581,
        Ea = (2.274, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 183 C8H6 + HO <=> C8H7O-10 in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 183 C8H6 + HO <=> C8H7O-10 in R_Addition_MultipleBond/training
""",
)

entry(
    index = 1803,
    label = "C10H7(189) <=> C10H7(259)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.83e+06, 's^-1'),
        n = 1.697,
        Ea = (19.915, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70\nExact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4H_DSB;Cd_rad_out_singleH;Cb_H_out from training reaction 70
Exact match found for rate rule [R4H_DSB;Cd_rad_out_singleH;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1804,
    label = "C10H7(254) <=> C10H7(259)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130200, 's^-1'),
        n = 2.209,
        Ea = (29.053, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47\nExact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R3H_SB;Cd_rad_out_Cd;Cb_H_out from training reaction 47
Exact match found for rate rule [R3H_SB;Cd_rad_out_Cd;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1805,
    label = "C10H7(259) <=> C10H7(230)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.989e+08, 's^-1'),
        n = 1.306,
        Ea = (43.343, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1806,
    label = "C10H7(259) <=> C10H7(267)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.933e+10, 's^-1'),
        n = 0.398,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1807,
    label = "C10H7(245) <=> C10H7(255)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.562e+08, 's^-1'),
        n = 1.057,
        Ea = (26.261, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1808,
    label = "C10H7(245) <=> C10H7(256)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.562e+08, 's^-1'),
        n = 1.057,
        Ea = (26.261, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1809,
    label = "H_10_(3) + C10H5(244) <=> C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;H_rad]
""",
)

entry(
    index = 1850,
    label = "C10H5(244) <=> C10H5(268)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+11, 's^-1'),
        n = 0.258,
        Ea = (13.436, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R6_DSB_T;triplebond_intra_H;radadd_intra_cdsingleH from training reaction 75\nExact match found for rate rule [R6_DSB_T;triplebond_intra_H;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R6_DSB_T;triplebond_intra_H;radadd_intra_cdsingleH from training reaction 75
Exact match found for rate rule [R6_DSB_T;triplebond_intra_H;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1851,
    label = "C10H5(271) <=> C10H5(268)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+11, 's^-1'),
        n = 0.258,
        Ea = (9.976, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_MSR;triplebond_intra_H;radadd_intra] for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6_MSR;triplebond_intra_H;radadd_intra] for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1852,
    label = "C10H5(269) <=> C10H5(244)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (9.548, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1853,
    label = "C10H5(270) <=> C10H5(244)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (9.548, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 35.3 to 39.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1854,
    label = "C10H5(269) <=> C10H5(276)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (16.739, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 2\nEa raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 2
Ea raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1855,
    label = "C10H5(270) <=> C10H5(276)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (16.739, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 2\nEa raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 2
Ea raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1856,
    label = "C10H5(271) <=> C10H5(272)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.198e+11, 's^-1'),
        n = 0.54,
        Ea = (28.053, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;doublebond_intra_HDe_secDe;radadd_intra] for rate rule [R4;doublebond_intra_HDe_secDe;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4;doublebond_intra_HDe_secDe;radadd_intra] for rate rule [R4;doublebond_intra_HDe_secDe;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1857,
    label = "C10H5(269) <=> C10H5(277)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (16.739, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1858,
    label = "C10H5(270) <=> C10H5(277)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (16.739, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 66.0 to 70.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1859,
    label = "C10H5(271) <=> C10H5(273)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.56e+11, 's^-1'),
        n = 0.26,
        Ea = (26.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;doublebond_intra_secDe;radadd_intra] for rate rule [R4;doublebond_intra_secDe_HCt;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4;doublebond_intra_secDe;radadd_intra] for rate rule [R4;doublebond_intra_secDe_HCt;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1860,
    label = "C10H5(272) <=> C10H5(273)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.436e+08, 's^-1'),
        n = 1.101,
        Ea = (27.148, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-Ct from training reaction 1\nExact match found for rate rule [R4-Cs-Cb;rad-Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-Ct from training reaction 1
Exact match found for rate rule [R4-Cs-Cb;rad-Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1861,
    label = "C10H5(269) <=> C10H5(275)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.933e+10, 's^-1'),
        n = 0.398,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1862,
    label = "C10H5(272) <=> C10H5(278)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.902e+06, 's^-1'),
        n = 1.913,
        Ea = (38.452, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [RnH;Cd_rad_out_singleH;Cd_H_out_singleNd] + [R3H;Cd_rad_out_singleH;XH_out] for rate rule\n[R3H;Cd_rad_out_singleH;Cd_H_out_singleNd]',
    ),
    longDesc = 
u"""
Estimated using average of templates [RnH;Cd_rad_out_singleH;Cd_H_out_singleNd] + [R3H;Cd_rad_out_singleH;XH_out] for rate rule
[R3H;Cd_rad_out_singleH;Cd_H_out_singleNd]
""",
)

entry(
    index = 1863,
    label = "C10H5(278) <=> C10H5(289)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.497e+08, 's^-1'),
        n = 1.079,
        Ea = (21.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4-Cs-Cb;rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4-Cs-Cb;rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1864,
    label = "C10H5(281) <=> C10H5(272)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (479800, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 1865,
    label = "C10H5(280) <=> C10H5(272)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (359900, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1866,
    label = "C10H5(281) <=> C10H5(280)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.046e+09, 's^-1'),
        n = 1.306,
        Ea = (43.343, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1867,
    label = "C10H5(279) <=> C10H5(272)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (359900, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1868,
    label = "C10H5(281) <=> C10H5(279)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.422e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1869,
    label = "C10H5(280) <=> C10H5(279)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.601e+06, 's^-1'),
        n = 1.934,
        Ea = (28.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1870,
    label = "C10H5(288) <=> C10H5(278)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.941e+09, 's^-1'),
        n = 0.741,
        Ea = (18.902, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra;radadd_intra_Cb] + [R4;doublebond_intra;radadd_intra] for rate rule\n[R4;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra;radadd_intra_Cb] + [R4;doublebond_intra;radadd_intra] for rate rule
[R4;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1871,
    label = "C10H5(288) <=> C10H5(289)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.676e+09, 's^-1'),
        n = 0.657,
        Ea = (36.136, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1872,
    label = "C10H5(288) <=> C10H5(294)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (239900, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1873,
    label = "C10H5(296) <=> C10H5(294)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (4.488, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra;radadd_intra] for rate rule [R6;triplebond_intra_De;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 15.9 to 18.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra;radadd_intra] for rate rule [R6;triplebond_intra_De;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 15.9 to 18.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1874,
    label = "C10H5(296) <=> C10H5(300)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (9.576, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_De;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2\nEa raised from 37.1 to 40.1 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_De;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
Ea raised from 37.1 to 40.1 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1875,
    label = "C10H5(296) <=> C10H5(298)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.756e+10, 's^-1'),
        n = 0.433,
        Ea = (16.444, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra] + [R8;multiplebond_intra;radadd_intra] for rate rule\n[R8;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra] + [R8;multiplebond_intra;radadd_intra] for rate rule
[R8;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1876,
    label = "C10H5(281) <=> C10H5(290)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5_MS;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5_MS;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1877,
    label = "C10H5(302) <=> C10H5(290)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (41.259, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;doublebond_intra;radadd_intra_cs] for rate rule [R5_SB;doublebond_intra;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;doublebond_intra;radadd_intra_cs] for rate rule [R5_SB;doublebond_intra;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1878,
    label = "C10H5(304) <=> C10H5(302)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.022e+09, 's^-1'),
        n = 1.29,
        Ea = (28.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_noH] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_noH] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1879,
    label = "C10H5(302) <=> C10H5(303)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.92e+06, 's^-1'),
        n = 1.623,
        Ea = (44.071, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;C_rad_out_single;Cd_H_out_doubleC] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;C_rad_out_single;Cd_H_out_doubleC] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1880,
    label = "C10H5(304) <=> C10H5(303)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+07, 's^-1'),
        n = 1.425,
        Ea = (7.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_Cb] for rate rule [R3H;Cd_rad_out_singleH;Cd_H_out_Cb]',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_Cb] for rate rule [R3H;Cd_rad_out_singleH;Cd_H_out_Cb]
""",
)

entry(
    index = 1881,
    label = "C10H5(310) <=> C10H5(303)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (816000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_BSMS;Cb_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_BSMS;Cb_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1882,
    label = "C10H5(302) <=> C10H5(306)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.748e+10, 's^-1'),
        n = 0.262,
        Ea = (19.926, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_cs] for rate rule [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_csDeDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_cs] for rate rule [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_csDeDe]
""",
)

entry(
    index = 1883,
    label = "C10H5(303) <=> C10H5(311)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.428, 's^-1'),
        n = 3.67,
        Ea = (29.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6H_SMSMS;C_rad_out_2H;Cs_H_out_noH] for rate rule [R6H_SMSMS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6H_SMSMS;C_rad_out_2H;Cs_H_out_noH] for rate rule [R6H_SMSMS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1884,
    label = "C10H5(311) <=> C10H5(317)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (34.669, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_Nd;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_Nd;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1885,
    label = "C10H5(310) <=> C10H5(315)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.833e+10, 's^-1'),
        n = 0.399,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra;radadd_intra_Cb] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra;radadd_intra_Cb] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1886,
    label = "C10H5(311) <=> C10H5(318)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;triplebond_intra_Nd;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;triplebond_intra_Nd;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1887,
    label = "C10H5(310) <=> C10H5(313)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.993e+10, 's^-1'),
        n = 0.768,
        Ea = (20.183, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;triplebond_intra;radadd_intra] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R4;triplebond_intra;radadd_intra] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1888,
    label = "C10H5(319) <=> C10H5(313)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.993e+10, 's^-1'),
        n = 0.768,
        Ea = (20.183, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;triplebond_intra;radadd_intra] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R4;triplebond_intra;radadd_intra] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1889,
    label = "C10H5(319) <=> C10H5(321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (816000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_BSMS;Cb_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_BSMS;Cb_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1890,
    label = "C10H5(325) <=> C10H5(321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.193e+07, 's^-1'),
        n = 1.425,
        Ea = (7.283, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_Cb] for rate rule [R3H;Cd_rad_out_singleH;Cd_H_out_Cb]',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_Cb] for rate rule [R3H;Cd_rad_out_singleH;Cd_H_out_Cb]
""",
)

entry(
    index = 1891,
    label = "C10H5(326) <=> C10H5(321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.92e+06, 's^-1'),
        n = 1.623,
        Ea = (44.071, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;C_rad_out_single;Cd_H_out_doubleC] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;C_rad_out_single;Cd_H_out_doubleC] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1892,
    label = "C10H5(325) <=> C10H5(326)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.662e+08, 's^-1'),
        n = 1.29,
        Ea = (28.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_noH] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_noH] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1893,
    label = "C10H5(319) <=> C10H5(322)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.833e+10, 's^-1'),
        n = 0.399,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra;radadd_intra_Cb] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra;radadd_intra_Cb] for rate rule [R4;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1894,
    label = "C10H5(326) <=> C10H5(330)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.748e+10, 's^-1'),
        n = 0.262,
        Ea = (19.926, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_cs] for rate rule [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_csDeDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_cs] for rate rule [R6_SBS_D;doublebond_intra_CdCdd;radadd_intra_csDeDe]
""",
)

entry(
    index = 1895,
    label = "C10H5(321) <=> C10H5(323)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.321, 's^-1'),
        n = 3.67,
        Ea = (29.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6H_SMSMS;C_rad_out_2H;Cs_H_out_noH] for rate rule [R6H_SMSMS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R6H_SMSMS;C_rad_out_2H;Cs_H_out_noH] for rate rule [R6H_SMSMS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1896,
    label = "C10H5(323) <=> C10H5(332)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (32.665, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_Nd;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_Nd;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1897,
    label = "C10H5(279) <=> C10H5(293)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5_MS;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5_MS;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1898,
    label = "C10H5(326) <=> C10H5(293)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (39.471, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;doublebond_intra;radadd_intra_cs] for rate rule [R5_SB;doublebond_intra;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6\nEa raised from 164.2 to 165.1 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;doublebond_intra;radadd_intra_cs] for rate rule [R5_SB;doublebond_intra;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
Ea raised from 164.2 to 165.1 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1899,
    label = "C10H5(302) <=> C10H5(305)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;doublebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;doublebond_intra;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;doublebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;doublebond_intra;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1900,
    label = "C10H5(318) <=> C10H5(305)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (801600, 's^-1'),
        n = 2.305,
        Ea = (38.286, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H from training reaction 72\nExact match found for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 15',
    ),
    longDesc = 
u"""
R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H from training reaction 72
Exact match found for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H]
Multiplied by reaction path degeneracy 15
""",
)

entry(
    index = 1901,
    label = "C10H5(310) <=> C10H5(314)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.601e+06, 's^-1'),
        n = 1.934,
        Ea = (28.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1902,
    label = "C10H5(314) <=> C10H5(334)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.074e+12, 's^-1'),
        n = 0.102,
        Ea = (13.049, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5;triplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R5;triplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1903,
    label = "C10H5(314) <=> C10H5(333)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.152e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5;multiplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R5;multiplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1904,
    label = "C10H5(337) <=> C10H5(333)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.152e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5;multiplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R5;multiplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1905,
    label = "C10H5(337) <=> C10H5(338)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.074e+12, 's^-1'),
        n = 0.102,
        Ea = (13.049, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5;triplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R5;triplebond_intra;radadd_intra_Cb] for rate rule [R5;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1906,
    label = "C10H5(338) <=> C10H5(340)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.221e+09, 's^-1'),
        n = 1.192,
        Ea = (24.762, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 11',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 11
""",
)

entry(
    index = 1907,
    label = "C10H5(338) <=> C10H5(339)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (641300, 's^-1'),
        n = 2.305,
        Ea = (38.286, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H from training reaction 72\nExact match found for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H from training reaction 72
Exact match found for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 1908,
    label = "C10H5(339) <=> C10H5(340)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84000, 's^-1'),
        n = 2.14,
        Ea = (7.97, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;C_rad_out_2H;Cs_H_out_noH] for rate rule [R5H_SSMS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [R5H;C_rad_out_2H;Cs_H_out_noH] for rate rule [R5H_SSMS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 1909,
    label = "C10H5(344) <=> C10H5(339)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.898e+10, 's^-1'),
        n = 0.528,
        Ea = (12.873, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1910,
    label = "C10H5(339) <=> C10H5(341)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.562e+08, 's^-1'),
        n = 1.057,
        Ea = (28.475, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 2\nEa raised from 116.8 to 119.1 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 2
Ea raised from 116.8 to 119.1 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1911,
    label = "C10H5(344) <=> C10H5(341)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.565e+11, 's^-1'),
        n = -0.035,
        Ea = (16.253, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule\n[R6;doublebond_intra_CdCdd;radadd_intra_Cb]',
    ),
    longDesc = 
u"""
Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule
[R6;doublebond_intra_CdCdd;radadd_intra_Cb]
""",
)

entry(
    index = 1912,
    label = "C10H5(346) <=> C10H5(341)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.654e+09, 's^-1'),
        n = 0.695,
        Ea = (6.499, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1913,
    label = "C10H5(346) <=> C10H5(347)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.94e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1914,
    label = "C10H5(348) <=> C10H5(347)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.317e+09, 's^-1'),
        n = 1.062,
        Ea = (16.546, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cs2H] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cs2H] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1915,
    label = "C10H5(348) <=> C10H5(350)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (823.2, 's^-1'),
        n = 2.93,
        Ea = (18.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule\n[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule
[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1916,
    label = "C10H5(345) <=> C10H5(341)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.168e+08, 's^-1'),
        n = 1.29,
        Ea = (47.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd from training reaction 64\nExact match found for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd from training reaction 64
Exact match found for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1917,
    label = "C10H5(348) <=> C10H5(345)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.754e+09, 's^-1'),
        n = 0.743,
        Ea = (24.976, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra_cs2H] + [R6;multiplebond_intra;radadd_intra_cs2H] +\n[R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra_cs2H] + [R6;multiplebond_intra;radadd_intra_cs2H] +
[R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1918,
    label = "C10H5(350) <=> C10H5(351)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (41.327, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1919,
    label = "C10H5(342) <=> C10H5(339)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.497e+08, 's^-1'),
        n = 1.079,
        Ea = (21.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4-Cs-Cb;rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4-Cs-Cb;rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1920,
    label = "C10H5(344) <=> C10H5(342)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.152e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1921,
    label = "C10H5(353) <=> C10H5(342)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.152e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1922,
    label = "C10H5(334) <=> C10H5(335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (641300, 's^-1'),
        n = 2.305,
        Ea = (38.286, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H from training reaction 72\nExact match found for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H from training reaction 72
Exact match found for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_2H]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 1923,
    label = "C10H5(335) <=> C10H5(347)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+06, 's^-1'),
        n = 2.094,
        Ea = (61.014, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH from training reaction 74\nExact match found for rate rule [R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH from training reaction 74
Exact match found for rate rule [R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 1924,
    label = "C10H5(342) <=> C10H5(335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.497e+08, 's^-1'),
        n = 1.079,
        Ea = (21.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4-Cs-Cb;rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4-Cs-Cb;rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1925,
    label = "C10H5(353) <=> C10H5(335)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.898e+10, 's^-1'),
        n = 0.528,
        Ea = (12.873, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1926,
    label = "C10H5(334) <=> C10H5(336)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11e+09, 's^-1'),
        n = 1.192,
        Ea = (24.762, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 1927,
    label = "C10H5(335) <=> C10H5(336)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84000, 's^-1'),
        n = 2.14,
        Ea = (7.97, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;C_rad_out_2H;Cs_H_out_noH] for rate rule [R5H_SSMS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [R5H;C_rad_out_2H;Cs_H_out_noH] for rate rule [R5H_SSMS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 1928,
    label = "C10H5(353) <=> C10H5(354)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.565e+11, 's^-1'),
        n = -0.035,
        Ea = (16.253, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule\n[R6;doublebond_intra_CdCdd;radadd_intra_Cb]',
    ),
    longDesc = 
u"""
Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule
[R6;doublebond_intra_CdCdd;radadd_intra_Cb]
""",
)

entry(
    index = 1929,
    label = "C10H5(335) <=> C10H5(354)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.562e+08, 's^-1'),
        n = 1.057,
        Ea = (30.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4-Cs-Cb;rad-HH from training reaction 2\nExact match found for rate rule [R4-Cs-Cb;rad-HH]\nMultiplied by reaction path degeneracy 2\nEa raised from 123.8 to 125.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
R4-Cs-Cb;rad-HH from training reaction 2
Exact match found for rate rule [R4-Cs-Cb;rad-HH]
Multiplied by reaction path degeneracy 2
Ea raised from 123.8 to 125.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1930,
    label = "C10H5(356) <=> C10H5(354)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.654e+09, 's^-1'),
        n = 0.695,
        Ea = (6.499, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1931,
    label = "C10H5(339) <=> C10H5(343)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+06, 's^-1'),
        n = 2.094,
        Ea = (61.014, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH from training reaction 74\nExact match found for rate rule [R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH from training reaction 74
Exact match found for rate rule [R3H_SD;C_rad_out_H/Cb;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 1932,
    label = "C10H5(356) <=> C10H5(343)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.94e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1933,
    label = "C10H5(357) <=> C10H5(343)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.317e+09, 's^-1'),
        n = 1.062,
        Ea = (16.546, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cs2H] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cs2H] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1934,
    label = "C10H5(357) <=> C10H5(358)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (823.2, 's^-1'),
        n = 2.93,
        Ea = (18.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule\n[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule
[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1935,
    label = "C10H5(355) <=> C10H5(354)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.168e+08, 's^-1'),
        n = 1.29,
        Ea = (47.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd from training reaction 64\nExact match found for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd from training reaction 64
Exact match found for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1936,
    label = "C10H5(357) <=> C10H5(355)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.754e+09, 's^-1'),
        n = 0.743,
        Ea = (24.976, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra_cs2H] + [R6;multiplebond_intra;radadd_intra_cs2H] +\n[R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra_cs2H] + [R6;multiplebond_intra;radadd_intra_cs2H] +
[R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1937,
    label = "C10H5(358) <=> C10H5(359)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (35.159, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1938,
    label = "C10H5(358) <=> C10H5(360)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1939,
    label = "C10H5(360) <=> C10H5(363)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.672e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SMMS;Cd_rad_out_Cd;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 27',
    ),
    longDesc = 
u"""
Estimated using template [R5H;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SMMS;Cd_rad_out_Cd;Cs_H_out_2H]
Multiplied by reaction path degeneracy 27
""",
)

entry(
    index = 1940,
    label = "C10H5(362) <=> C10H5(360)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+12, 's^-1'),
        n = 0.633,
        Ea = (46.955, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb from training reaction 68\nExact match found for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb from training reaction 68
Exact match found for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1941,
    label = "C10H5(362) <=> C10H5(363)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.856e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 21',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_2H]
Multiplied by reaction path degeneracy 21
""",
)

entry(
    index = 1942,
    label = "C10H5(363) <=> C10H5(364)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.366e+12, 's^-1'),
        n = 0.06,
        Ea = (26.949, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnxc5_beta_long;doublebond_intra;radadd_intra_cs2H] for rate rule [Rn3c5_beta_long;doublebond_intra;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 17\nEa raised from 112.4 to 112.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Rnxc5_beta_long;doublebond_intra;radadd_intra_cs2H] for rate rule [Rn3c5_beta_long;doublebond_intra;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 17
Ea raised from 112.4 to 112.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1943,
    label = "C10H5(287) <=> C10H5(278)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.702e+11, 's^-1'),
        n = -0.5,
        Ea = (17.092, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6H;Y_rad_out;Cs_H_out_2H] for rate rule [R6H_RSSMS;Cb_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using template [R6H;Y_rad_out;Cs_H_out_2H] for rate rule [R6H_RSSMS;Cb_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 1944,
    label = "C10H5(287) <=> C10H5(317)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1945,
    label = "C10H5(286) <=> C10H5(278)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.026e+11, 's^-1'),
        n = -0.5,
        Ea = (17.092, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6H;Y_rad_out;Cs_H_out_2H] for rate rule [R6H_RSSMS;Cb_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 9',
    ),
    longDesc = 
u"""
Estimated using template [R6H;Y_rad_out;Cs_H_out_2H] for rate rule [R6H_RSSMS;Cb_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 9
""",
)

entry(
    index = 1946,
    label = "C10H5(286) <=> C10H5(332)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_Nd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_Nd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1947,
    label = "C10H5(287) <=> C10H5(286)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.422e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1948,
    label = "C10H5(331) <=> C10H5(330)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.045e+09, 's^-1'),
        n = 0.695,
        Ea = (6.499, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R6_MSR;triplebond_intra_H;radadd_intra_Cb from training reaction 54\nExact match found for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
R6_MSR;triplebond_intra_H;radadd_intra_Cb from training reaction 54
Exact match found for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1949,
    label = "C10H5(316) <=> C10H5(306)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.045e+09, 's^-1'),
        n = 0.695,
        Ea = (6.499, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R6_MSR;triplebond_intra_H;radadd_intra_Cb from training reaction 54\nExact match found for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
R6_MSR;triplebond_intra_H;radadd_intra_Cb from training reaction 54
Exact match found for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1950,
    label = "C10H5(331) <=> C10H5(316)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.422e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1951,
    label = "C10H5(316) <=> C10H5(365)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.52e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_MSR;triplebond_intra_H;radadd_intra] for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R6_MSR;triplebond_intra_H;radadd_intra] for rate rule [R6_MSR;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1952,
    label = "C10H5(349) <=> C10H5(348)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.068e+11, 's^-1'),
        n = 0.722,
        Ea = (41.878, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R3H_BS;Cb_rad_out;Cs_H_out_2H from training reaction 51\nExact match found for rate rule [R3H_BS;Cb_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 15',
    ),
    longDesc = 
u"""
R3H_BS;Cb_rad_out;Cs_H_out_2H from training reaction 51
Exact match found for rate rule [R3H_BS;Cb_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 15
""",
)

entry(
    index = 1953,
    label = "C10H5(349) <=> C10H5(366)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.94e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1954,
    label = "C10H5(367) <=> C10H5(366)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.94e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1955,
    label = "C10H5(366) <=> C10H5(368)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.04e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 15',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H]
Multiplied by reaction path degeneracy 15
""",
)

entry(
    index = 1956,
    label = "C10H5(368) <=> C10H5(369)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1372, 's^-1'),
        n = 2.93,
        Ea = (18.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule\n[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule
[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 1957,
    label = "C10H5(296) <=> C10H5(299)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.218e+09, 's^-1'),
        n = 0.695,
        Ea = (24.583, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_Cb] for rate rule [R8;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2\nEa raised from 97.0 to 102.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_Cb] for rate rule [R8;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
Ea raised from 97.0 to 102.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 1958,
    label = "H_10_(3) + C10H4(373) <=> C10H5(299)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.22e+09, 'cm^3/(mol*s)'),
        n = 1.524,
        Ea = (3.486, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Ct-De_Ct-De;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Ct-De_Ct-De;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1975,
    label = "C10H4(373) <=> C10H4(374)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1976,
    label = "C10H5(361) <=> C10H5(359)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1977,
    label = "C10H5(361) <=> C10H5(362)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1978,
    label = "C10H5(269) <=> C10H5(274)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.97e+09, 's^-1'),
        n = 0.768,
        Ea = (31.842, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;triplebond_intra_H;radadd_intra] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R4;triplebond_intra_H;radadd_intra] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1979,
    label = "C10H5(375) <=> C10H5(274)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.97e+09, 's^-1'),
        n = 0.768,
        Ea = (31.842, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;triplebond_intra_H;radadd_intra] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R4;triplebond_intra_H;radadd_intra] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1980,
    label = "C10H5(275) <=> C10H5(283)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.726e+09, 's^-1'),
        n = 1.159,
        Ea = (37.413, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_D;Cd_rad_out_single;Cd_H_out_Cb] + [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_single] for rate rule\n[R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_Cb]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_D;Cd_rad_out_single;Cd_H_out_Cb] + [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_single] for rate rule
[R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_Cb]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1981,
    label = "C10H5(375) <=> C10H5(283)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.933e+10, 's^-1'),
        n = 0.398,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_Cb] for rate rule [R4;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1982,
    label = "C10H5(283) <=> C10H5(376)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.031e+11, 's^-1'),
        n = 0.366,
        Ea = (5.94, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra] for rate rule [R7;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra] for rate rule [R7;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1983,
    label = "C10H5(352) <=> C10H5(351)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1984,
    label = "C10H5(288) <=> C10H5(295)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.565e+11, 's^-1'),
        n = -0.035,
        Ea = (16.253, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule\n[R6;doublebond_intra_CdCdd;radadd_intra_Cb]',
    ),
    longDesc = 
u"""
Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule
[R6;doublebond_intra_CdCdd;radadd_intra_Cb]
""",
)

entry(
    index = 1985,
    label = "C10H5(309) <=> C10H5(304)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13.71, 's^-1'),
        n = 3.311,
        Ea = (30.765, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1986,
    label = "C10H5(309) <=> C10H5(303)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (957.5, 's^-1'),
        n = 3.05,
        Ea = (53.137, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_MS;Y_rad_out;Cd_H_out_doubleC] for rate rule [R3H_BS;Cb_rad_out;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R3H_MS;Y_rad_out;Cd_H_out_doubleC] for rate rule [R3H_BS;Cb_rad_out;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1987,
    label = "C10H5(353) <=> C10H5(309)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.601e+06, 's^-1'),
        n = 1.934,
        Ea = (28.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 1988,
    label = "C10H5(309) <=> C10H5(378)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.118e+10, 's^-1'),
        n = 0.741,
        Ea = (18.902, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra;radadd_intra_Cb] + [R4;doublebond_intra;radadd_intra] for rate rule\n[R4;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra;radadd_intra_Cb] + [R4;doublebond_intra;radadd_intra] for rate rule
[R4;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1989,
    label = "C10H5(378) <=> C10H5(381)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out] for rate rule [R5H_SSMS;Cd_rad_out_Cd;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out] for rate rule [R5H_SSMS;Cd_rad_out_Cd;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 1990,
    label = "C10H5(324) <=> C10H5(321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (957.5, 's^-1'),
        n = 3.05,
        Ea = (53.137, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_MS;Y_rad_out;Cd_H_out_doubleC] for rate rule [R3H_BS;Cb_rad_out;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R3H_MS;Y_rad_out;Cd_H_out_doubleC] for rate rule [R3H_BS;Cb_rad_out;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1991,
    label = "C10H5(324) <=> C10H5(325)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13.71, 's^-1'),
        n = 3.311,
        Ea = (30.765, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1992,
    label = "C10H5(324) <=> C10H5(378)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.118e+10, 's^-1'),
        n = 0.741,
        Ea = (18.902, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra;radadd_intra_Cb] + [R4;doublebond_intra;radadd_intra] for rate rule\n[R4;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra;radadd_intra_Cb] + [R4;doublebond_intra;radadd_intra] for rate rule
[R4;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 1993,
    label = "C10H5(324) <=> C10H5(382)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.431e+11, 's^-1'),
        n = 0.114,
        Ea = (15.579, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb from training reaction 62\nExact match found for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb]',
    ),
    longDesc = 
u"""
R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb from training reaction 62
Exact match found for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb]
""",
)

entry(
    index = 1994,
    label = "C10H5(382) <=> C10H5(385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 1995,
    label = "C10H5(382) <=> C10H5(383)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.433e+10, 's^-1'),
        n = 1.173,
        Ea = (36.559, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;Cd_rad_out_Cd_Cb;Cs_H_out_1H] + [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_1H] for rate rule\n[R2H_S_cy5;Cd_rad_out_Cd_Cb;Cs_H_out_H/AromDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;Cd_rad_out_Cd_Cb;Cs_H_out_1H] + [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_1H] for rate rule
[R2H_S_cy5;Cd_rad_out_Cd_Cb;Cs_H_out_H/AromDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1996,
    label = "C10H5(385) <=> C10H5(383)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.872e+08, 's^-1'),
        n = 1.61,
        Ea = (27.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;C_rad_out_single;Cs_H_out_H/OneDe] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cs_H_out_H/Cd/C/Cb]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;C_rad_out_single;Cs_H_out_H/OneDe] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cs_H_out_H/Cd/C/Cb]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 1997,
    label = "C10H5(387) <=> C10H5(383)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.08e+08, 's^-1'),
        n = 1.61,
        Ea = (27.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;C_rad_out_single;Cs_H_out_H/OneDe] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cs_H_out_H/Cd/C/Cb]\nMultiplied by reaction path degeneracy 20',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;C_rad_out_single;Cs_H_out_H/OneDe] for rate rule [R4H_SBS;C_rad_out_TwoDe;Cs_H_out_H/Cd/C/Cb]
Multiplied by reaction path degeneracy 20
""",
)

entry(
    index = 1998,
    label = "C10H5(309) <=> C10H5(379)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.431e+11, 's^-1'),
        n = 0.114,
        Ea = (15.579, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb from training reaction 62\nExact match found for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb]',
    ),
    longDesc = 
u"""
R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb from training reaction 62
Exact match found for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_Cb]
""",
)

entry(
    index = 1999,
    label = "C10H5(379) <=> C10H5(383)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.433e+10, 's^-1'),
        n = 1.173,
        Ea = (36.559, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;Cd_rad_out_Cd_Cb;Cs_H_out_1H] + [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_1H] for rate rule\n[R2H_S_cy5;Cd_rad_out_Cd_Cb;Cs_H_out_H/AromDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;Cd_rad_out_Cd_Cb;Cs_H_out_1H] + [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_1H] for rate rule
[R2H_S_cy5;Cd_rad_out_Cd_Cb;Cs_H_out_H/AromDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2000,
    label = "C10H5(379) <=> C10H5(387)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2001,
    label = "C10H5(308) <=> C10H5(304)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.712e+11, 's^-1'),
        n = 0.722,
        Ea = (41.878, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_BS;Cb_rad_out;Cs_H_out] for rate rule [R3H_BS;Cb_rad_out;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R3H_BS;Cb_rad_out;Cs_H_out] for rate rule [R3H_BS;Cb_rad_out;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2002,
    label = "C10H5(346) <=> C10H5(308)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.601e+06, 's^-1'),
        n = 1.934,
        Ea = (28.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 2003,
    label = "C10H5(308) <=> C10H5(382)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.136e+11, 's^-1'),
        n = 0.102,
        Ea = (13.049, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R5_MS;triplebond_intra_H;radadd_intra_Cb from training reaction 61\nExact match found for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R5_MS;triplebond_intra_H;radadd_intra_Cb from training reaction 61
Exact match found for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2004,
    label = "C10H5(329) <=> C10H5(325)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.712e+11, 's^-1'),
        n = 0.722,
        Ea = (41.878, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_BS;Cb_rad_out;Cs_H_out] for rate rule [R3H_BS;Cb_rad_out;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R3H_BS;Cb_rad_out;Cs_H_out] for rate rule [R3H_BS;Cb_rad_out;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2005,
    label = "C10H5(329) <=> C10H5(379)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.136e+11, 's^-1'),
        n = 0.102,
        Ea = (13.049, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R5_MS;triplebond_intra_H;radadd_intra_Cb from training reaction 61\nExact match found for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R5_MS;triplebond_intra_H;radadd_intra_Cb from training reaction 61
Exact match found for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2006,
    label = "C10H5(329) <=> C10H5(389)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.966e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2007,
    label = "C10H5(390) <=> C10H5(389)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.356e+11, 's^-1'),
        n = 0.481,
        Ea = (30.309, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2008,
    label = "C10H5(390) <=> C10H5(391)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (823.2, 's^-1'),
        n = 2.93,
        Ea = (18.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule\n[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule
[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2009,
    label = "C10H5(386) <=> C10H5(383)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (534400, 's^-1'),
        n = 2.305,
        Ea = (38.286, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_H/AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_H/AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2010,
    label = "C10H5(386) <=> C10H5(387)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.99e+08, 's^-1'),
        n = 1.192,
        Ea = (24.762, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 9',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 9
""",
)

entry(
    index = 2011,
    label = "C10H5(379) <=> C10H5(386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.25e+11, 's^-1'),
        n = 0.633,
        Ea = (46.955, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb from training reaction 68\nExact match found for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb from training reaction 68
Exact match found for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2012,
    label = "C10H5(390) <=> C10H5(386)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.108e+13, 's^-1'),
        n = -0.237,
        Ea = (20.919, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2013,
    label = "C10H5(391) <=> C10H5(393)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (35.159, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2014,
    label = "C10H5(391) <=> C10H5(394)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_cs] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 2015,
    label = "C10H5(308) <=> C10H5(388)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.966e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2016,
    label = "C10H5(397) <=> C10H5(388)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.356e+11, 's^-1'),
        n = 0.481,
        Ea = (30.309, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2017,
    label = "C10H5(384) <=> C10H5(382)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.876e+08, 's^-1'),
        n = 1.29,
        Ea = (47.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd from training reaction 64\nExact match found for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd from training reaction 64
Exact match found for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleNd]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2018,
    label = "C10H5(384) <=> C10H5(385)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11e+09, 's^-1'),
        n = 1.192,
        Ea = (24.762, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out] for rate rule [R4H_SBS;Cd_rad_out_Cd;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2019,
    label = "C10H5(384) <=> C10H5(383)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (534400, 's^-1'),
        n = 2.305,
        Ea = (38.286, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_H/AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cb;Cs_H_out_H/AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2020,
    label = "C10H5(397) <=> C10H5(384)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.108e+13, 's^-1'),
        n = -0.237,
        Ea = (20.919, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs2H] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2021,
    label = "C10H5(397) <=> C10H5(398)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (823.2, 's^-1'),
        n = 2.93,
        Ea = (18.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule\n[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule
[R4H_SBS;C_rad_out_2H;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2022,
    label = "C10H5(398) <=> C10H5(400)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.828e+11, 's^-1'),
        n = 0.481,
        Ea = (33.155, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_SB;multiplebond_intra;radadd_intra_cs] for rate rule [R5_SB;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2023,
    label = "C10H5(352) <=> C10H5(377)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.601e+06, 's^-1'),
        n = 1.934,
        Ea = (28.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Y_rad_out;Cb_H_out] for rate rule [R4H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 2024,
    label = "C10H5(377) <=> C10H5(400)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2025,
    label = "C10H5(399) <=> C10H5(397)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (816000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2026,
    label = "C10H5(399) <=> C10H5(398)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.032e+06, 's^-1'),
        n = 1.749,
        Ea = (9.866, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R5H;Y_rad_out;Cs_H_out_noH] + [R5H_RSMS;Y_rad_out;Cs_H_out] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using average of templates [R5H;Y_rad_out;Cs_H_out_noH] + [R5H_RSMS;Y_rad_out;Cs_H_out] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2027,
    label = "C10H5(392) <=> C10H5(390)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (816000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Y_rad_out;Cs_H_out_2H] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2028,
    label = "C10H5(392) <=> C10H5(391)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.032e+06, 's^-1'),
        n = 1.749,
        Ea = (9.866, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R5H;Y_rad_out;Cs_H_out_noH] + [R5H_RSMS;Y_rad_out;Cs_H_out] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using average of templates [R5H;Y_rad_out;Cs_H_out_noH] + [R5H_RSMS;Y_rad_out;Cs_H_out] for rate rule [R5H_TSMS;Ct_rad_out;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2029,
    label = "C10H5(395) <=> C10H5(393)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (14.54, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;multiplebond_intra;radadd_intra_Cb] for rate rule [R5_MS;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2030,
    label = "C10H5(368) <=> C10H5(370)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.178e+11, 's^-1'),
        n = 0.542,
        Ea = (29.862, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SM;doublebond_intra_secDe_2H;radadd_intra_cs2H] for rate rule [R5_SB;doublebond_intra_secDe_2H;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using template [R5_SM;doublebond_intra_secDe_2H;radadd_intra_cs2H] for rate rule [R5_SB;doublebond_intra_secDe_2H;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2031,
    label = "C10H5(299) <=> C10H5(371)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.119e+12, 's^-1'),
                n = 0.315,
                Ea = (13.65, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rnx_cyclics;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule\n[Rn2c8_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 4',
            ),
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (29.257, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rnx_cyclics;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule
[Rn2c8_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 4
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2033,
    label = "C10H5(299) <=> C10H5(372)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.119e+12, 's^-1'),
        n = 0.315,
        Ea = (13.65, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnx_cyclics;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule\n[Rn1c8_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Rnx_cyclics;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule
[Rn1c8_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2034,
    label = "C10H5(275) <=> C10H5(285)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.979e+12, 's^-1'),
        n = 0.045,
        Ea = (19.682, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 4\nEa raised from 77.2 to 82.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 4
Ea raised from 77.2 to 82.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 2035,
    label = "C10H5(275) <=> C10H5(284)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.129e+11, 's^-1'),
        n = 0.358,
        Ea = (15.655, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 4\nEa raised from 60.5 to 65.5 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra_H;radadd_intra] for rate rule [R6;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 4
Ea raised from 60.5 to 65.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 2036,
    label = "H_10_(3) + C10H4(320) <=> C10H5(313)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.175e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Ca;HJ from training reaction 144\nExact match found for rate rule [Cds-HH_Ca;HJ]',
    ),
    longDesc = 
u"""
Cds-HH_Ca;HJ from training reaction 144
Exact match found for rate rule [Cds-HH_Ca;HJ]
""",
)

entry(
    index = 2037,
    label = "H_10_(3) + C10H4(320) <=> C10H5(378)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.199e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (4.493, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-TwoDe_Ca;HJ] for rate rule [Cds-CbCb_Ca;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-TwoDe_Ca;HJ] for rate rule [Cds-CbCb_Ca;HJ]
""",
)

entry(
    index = 2072,
    label = "H_10_(3) + C10H6(221) <=> C10H7(193)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.992e+09, 'cm^3/(mol*s)'),
        n = 1.129,
        Ea = (9.249, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cd_Ct-H;HJ from training reaction 102\nExact match found for rate rule [Ct-Cd_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Ct-Cd_Ct-H;HJ from training reaction 102
Exact match found for rate rule [Ct-Cd_Ct-H;HJ]
""",
)

entry(
    index = 2081,
    label = "H_10_(3) + C10H5(271) <=> C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2082,
    label = "C2H(21) + C8H5(186) <=> C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct_rad/Ct;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct_rad/Ct;Cd_pri_rad]
""",
)

entry(
    index = 2083,
    label = "H_10_(3) + C10H5(294) <=> C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/OneDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/OneDe;H_rad]
""",
)

entry(
    index = 2168,
    label = "C10H6(402) <=> C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 2169,
    label = "C10H7(193) <=> C10H7(219)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.56e+08, 's^-1'),
        n = 1.408,
        Ea = (41.295, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_singleH;Cd_H_out_CdCb from training reaction 49\nExact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_CdCb]',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_singleH;Cd_H_out_CdCb from training reaction 49
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_CdCb]
""",
)

entry(
    index = 2171,
    label = "H_10_(3) + C10H6(221) <=> C10H7(219)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.234e+10, 'cm^3/(mol*s)'),
        n = 1.162,
        Ea = (5.066, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-H_Ct-Cd-C-Cb;HJ from training reaction 104\nExact match found for rate rule [Ct-H_Ct-Cd-C-Cb;HJ]',
    ),
    longDesc = 
u"""
Ct-H_Ct-Cd-C-Cb;HJ from training reaction 104
Exact match found for rate rule [Ct-H_Ct-Cd-C-Cb;HJ]
""",
)

entry(
    index = 2200,
    label = "H_10_(3) + C10H6(297) <=> C10H7(219)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.036e+13, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (0.09, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Ca_Ca;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Ca_Ca;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2201,
    label = "H_10_(3) + C10H5(288) <=> C10H6(297)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2202,
    label = "H_10_(3) + C10H5(294) <=> C10H6(297)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 2215,
    label = "C10H6(401) <=> C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH(C)C]',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH(C)C]
""",
)

entry(
    index = 2217,
    label = "H_10_(3) + C10H6(221) <=> C10H7(404)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.037e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (0.49, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CtH_Cds-TwoDe;HJ] for rate rule [Cds-CtH_Cds-CbCb;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CtH_Cds-TwoDe;HJ] for rate rule [Cds-CtH_Cds-CbCb;HJ]
""",
)

entry(
    index = 2238,
    label = "C2H(21) + C8H6(190) <=> C10H7(404)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29750, 'cm^3/(mol*s)'),
        n = 2.442,
        Ea = (-1.714, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-TwoDe;CJ] for rate rule [Cds-HH_Cds-CbCb;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-TwoDe;CJ] for rate rule [Cds-HH_Cds-CbCb;CtJ_Ct]
""",
)

entry(
    index = 2239,
    label = "C10H7(404) <=> C10H7(406)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.985e+09, 's^-1'),
        n = 0.768,
        Ea = (20.183, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_S_T;triplebond_intra_H;radadd_intra_cs] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csDeDe]',
    ),
    longDesc = 
u"""
Estimated using template [R4_S_T;triplebond_intra_H;radadd_intra_cs] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csDeDe]
""",
)

entry(
    index = 2241,
    label = "H_10_(3) + C10H6(221) <=> C10H7(403)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.508e+08, 'cm^3/(mol*s)'),
        n = 1.522,
        Ea = (4.177, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-TwoDe_Cds;HJ] for rate rule [Cds-CbCb_Cds;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-TwoDe_Cds;HJ] for rate rule [Cds-CbCb_Cds;HJ]
""",
)

entry(
    index = 2262,
    label = "C10H7(403) <=> C10H7(219)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_MMS;Cd_rad_out;Cs_H_out] for rate rule [R4H_MMS;Cd_rad_out_singleH;Cs_H_out_AromDe]',
    ),
    longDesc = 
u"""
Estimated using template [R4H_MMS;Cd_rad_out;Cs_H_out] for rate rule [R4H_MMS;Cd_rad_out_singleH;Cs_H_out_AromDe]
""",
)

entry(
    index = 2263,
    label = "C10H7(403) <=> C10H7(404)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.814e+09, 's^-1'),
        n = 1.156,
        Ea = (33.922, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_noH] for rate rule [R2H_S;C_rad_out_H/Ct;Cs_H_out_AromDe]',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_noH] for rate rule [R2H_S;C_rad_out_H/Ct;Cs_H_out_AromDe]
""",
)

entry(
    index = 2264,
    label = "C10H7(407) <=> C10H7(403)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.838e+12, 's^-1'),
        n = 0.362,
        Ea = (16.391, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;doublebond_intra_HDe_pri;radadd_intra] for rate rule [R6;doublebond_intra_HCt_pri;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6;doublebond_intra_HDe_pri;radadd_intra] for rate rule [R6;doublebond_intra_HCt_pri;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2265,
    label = "C10H7(407) <=> C10H7(408)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.782e+11, 's^-1'),
        n = 0.407,
        Ea = (6.152, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_D;doublebond_intra_HDe;radadd_intra_cdsingle] for rate rule\n[R6_DSM_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_D;doublebond_intra_HDe;radadd_intra_cdsingle] for rate rule
[R6_DSM_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2266,
    label = "C10H5(280) <=> C10H5(292)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.13e+11, 's^-1'),
        n = -0.035,
        Ea = (16.253, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule\n[R6;doublebond_intra_CdCdd;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R6;doublebond_intra;radadd_intra_Cb] + [R6;doublebond_intra_CdCdd;radadd_intra] for rate rule
[R6;doublebond_intra_CdCdd;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2267,
    label = "C10H5(409) <=> C10H5(292)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.563e+10, 's^-1'),
        n = 0.346,
        Ea = (23.67, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_SMS;multiplebond_intra;radadd_intra_cs] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_csDeDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6_SMS;multiplebond_intra;radadd_intra_cs] for rate rule [R6_SMS_T;triplebond_intra_H;radadd_intra_csDeDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2268,
    label = "C10H5(280) <=> C10H5(291)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.559e+08, 's^-1'),
        n = 1.035,
        Ea = (17.967, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R5_MS;doublebond_intra;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R5_MS;doublebond_intra;radadd_intra_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2269,
    label = "C10H5(301) <=> C10H5(298)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.756e+10, 's^-1'),
        n = 0.433,
        Ea = (16.444, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra] + [R8;multiplebond_intra;radadd_intra] for rate rule\n[R8;triplebond_intra_H;radadd_intra]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;triplebond_intra_H;radadd_intra] + [R8;multiplebond_intra;radadd_intra] for rate rule
[R8;triplebond_intra_H;radadd_intra]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2270,
    label = "C10H5(301) <=> C10H5(375)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.571e+06, 's^-1'),
        n = 1.981,
        Ea = (31.05, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_RSB;Y_rad_out;Cb_H_out] for rate rule [R4H_TSB;Ct_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4H_RSB;Y_rad_out;Cb_H_out] for rate rule [R4H_TSB;Ct_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2283,
    label = "H_10_(3) + C10H5(323) <=> C10H6(327)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]
""",
)

entry(
    index = 2284,
    label = "H_10_(3) + C10H5(321) <=> C10H6(327)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.478e+13, 'cm^3/(mol*s)'),
        n = 0.009,
        Ea = (-0.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_pri_rad;H_rad] + [C_rad/H2/Ct;Y_rad] for rate rule [C_rad/H2/Ct;H_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_pri_rad;H_rad] + [C_rad/H2/Ct;Y_rad] for rate rule [C_rad/H2/Ct;H_rad]
""",
)

entry(
    index = 2285,
    label = "H_10_(3) + C10H5(319) <=> C10H6(327)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2361,
    label = "H_10_(3) + C10H5(311) <=> C10H6(312)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]
""",
)

entry(
    index = 2362,
    label = "H_10_(3) + C10H5(303) <=> C10H6(312)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.478e+13, 'cm^3/(mol*s)'),
        n = 0.009,
        Ea = (-0.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_pri_rad;H_rad] + [C_rad/H2/Ct;Y_rad] for rate rule [C_rad/H2/Ct;H_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_pri_rad;H_rad] + [C_rad/H2/Ct;Y_rad] for rate rule [C_rad/H2/Ct;H_rad]
""",
)

entry(
    index = 2363,
    label = "H_10_(3) + C10H5(314) <=> C10H6(312)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Cb_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Cb_rad]
""",
)

entry(
    index = 2364,
    label = "H_10_(3) + C10H5(310) <=> C10H6(312)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2449,
    label = "C10H5(394) <=> C10H5(396)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.331e+09, 's^-1'),
        n = 1.192,
        Ea = (24.762, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out_2H] for rate rule [R4H_SBS;Cd_rad_out_Cd;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 21',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SMS;Cd_rad_out_double;Cs_H_out_2H] for rate rule [R4H_SBS;Cd_rad_out_Cd;Cs_H_out_2H]
Multiplied by reaction path degeneracy 21
""",
)

entry(
    index = 2450,
    label = "C10H5(410) <=> C10H5(396)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.856e+06, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 21',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSMS;Cd_rad_out;Cs_H_out_2H] for rate rule [R5H_SSMS;Cd_rad_out_Cd_Cb;Cs_H_out_2H]
Multiplied by reaction path degeneracy 21
""",
)

entry(
    index = 2451,
    label = "C10H5(410) <=> C10H5(394)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+12, 's^-1'),
        n = 0.633,
        Ea = (46.955, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb from training reaction 68\nExact match found for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb from training reaction 68
Exact match found for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_Cb]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2452,
    label = "C10H5(395) <=> C10H5(410)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.19e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_Cb]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 2453,
    label = "C10H5(273) <=> C10H5(282)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.967e+11, 's^-1'),
        n = 0.667,
        Ea = (34.08, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;C_rad_out_noH;Cs_H_out_noH] for rate rule [R2H_S_cy4;C_rad_out_TwoDe;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 5',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;C_rad_out_noH;Cs_H_out_noH] for rate rule [R2H_S_cy4;C_rad_out_TwoDe;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 5
""",
)

entry(
    index = 2454,
    label = "C10H5(282) <=> C10H5(289)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_MMS;Cd_rad_out;Cs_H_out] for rate rule [R4H_MMS;Cd_rad_out_singleH;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R4H_MMS;Cd_rad_out;Cs_H_out] for rate rule [R4H_MMS;Cd_rad_out_singleH;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2455,
    label = "C10H7(405) <=> C10H7(219)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.826e+10, 's^-1'),
        n = 0.823,
        Ea = (41.025, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;Cd_rad_out_double;Cs_H_out_noH] for rate rule [R2H_S;Cd_rad_out_double;Cs_H_out_AromDe]',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;Cd_rad_out_double;Cs_H_out_noH] for rate rule [R2H_S;Cd_rad_out_double;Cs_H_out_AromDe]
""",
)

entry(
    index = 2462,
    label = "C10H7(405) <=> C10H7(403)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.74e+08, 's^-1'),
        n = 1.713,
        Ea = (43.474, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_Cs;Cd_H_out_singleH] for rate rule [R3H;Cd_rad_out_Cs;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_Cs;Cd_H_out_singleH] for rate rule [R3H;Cd_rad_out_Cs;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2463,
    label = "H_10_(3) + C10H6(297) <=> C10H7(405)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.199e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (4.493, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-TwoDe_Ca;HJ] for rate rule [Cds-CbCb_Ca;HJ]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-TwoDe_Ca;HJ] for rate rule [Cds-CbCb_Ca;HJ]
""",
)

entry(
    index = 2464,
    label = "C10H7(405) <=> C10H7(411)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (137.2, 's^-1'),
        n = 2.93,
        Ea = (18.085, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule\n[R4H_STS;C_rad_out_2H;Cs_H_out_AromDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_2H;Cs_H_out_noH] + [R4H_SMS;C_rad_out_2H;Cs_H_out] for rate rule
[R4H_STS;C_rad_out_2H;Cs_H_out_AromDe]
""",
)

entry(
    index = 2465,
    label = "H_10_(3) + C10H6(297) <=> C10H7(411)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.175e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Ca;HJ from training reaction 144\nExact match found for rate rule [Cds-HH_Ca;HJ]',
    ),
    longDesc = 
u"""
Cds-HH_Ca;HJ from training reaction 144
Exact match found for rate rule [Cds-HH_Ca;HJ]
""",
)

entry(
    index = 2478,
    label = "H_10_(3) + C10H5(302) <=> C10H6(307)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]
""",
)

entry(
    index = 2479,
    label = "H_10_(3) + C10H5(353) <=> C10H6(307)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2480,
    label = "H_10_(3) + C10H5(309) <=> C10H6(307)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2481,
    label = "H_10_(3) + C10H5(303) <=> C10H6(307)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.573e+11, 'cm^3/(mol*s)'),
        n = 0.643,
        Ea = (-16.179, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cd_allenic_Cb;H_rad from training reaction 22\nExact match found for rate rule [Cd_allenic_Cb;H_rad]',
    ),
    longDesc = 
u"""
Cd_allenic_Cb;H_rad from training reaction 22
Exact match found for rate rule [Cd_allenic_Cb;H_rad]
""",
)

entry(
    index = 2482,
    label = "H_10_(3) + C10H5(304) <=> C10H6(307)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 2498,
    label = "C10H6(412) <=> C10H6(307)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]
""",
)

entry(
    index = 2511,
    label = "H_10_(3) + C10H5(326) <=> C10H6(328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]
""",
)

entry(
    index = 2512,
    label = "H_10_(3) + C10H5(324) <=> C10H6(328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_rad;H_rad]
""",
)

entry(
    index = 2513,
    label = "H_10_(3) + C10H5(321) <=> C10H6(328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.573e+11, 'cm^3/(mol*s)'),
        n = 0.643,
        Ea = (-16.179, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cd_allenic_Cb;H_rad from training reaction 22\nExact match found for rate rule [Cd_allenic_Cb;H_rad]',
    ),
    longDesc = 
u"""
Cd_allenic_Cb;H_rad from training reaction 22
Exact match found for rate rule [Cd_allenic_Cb;H_rad]
""",
)

entry(
    index = 2514,
    label = "H_10_(3) + C10H5(325) <=> C10H6(328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 2527,
    label = "C10H6(413) <=> C10H6(328)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]
""",
)

entry(
    index = 2528,
    label = "C10H5(380) <=> C10H5(378)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.73,
        Ea = (42.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd]
""",
)

entry(
    index = 2529,
    label = "C10H5(380) <=> C10H5(381)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.788e+09, 's^-1'),
        n = 1.29,
        Ea = (28.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_noH] for rate rule [R6H_RSSMS;Cd_rad_out_singleH;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 7',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_noH] for rate rule [R6H_RSSMS;Cd_rad_out_singleH;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 7
""",
)

entry(
    index = 2530,
    label = "C2H2(20) + C8H3(414) <=> C10H5(380)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (10.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-H;CsJ-TwoDeH] for rate rule [Ct-H_Ct-H;CsJ-CbCbH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-H;CsJ-TwoDeH] for rate rule [Ct-H_Ct-H;CsJ-CbCbH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2532,
    label = "H_10_(3) + C8H3(414) <=> C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.038e+12, 'cm^3/(mol*s)'),
        n = -0.099,
        Ea = (0.544, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [H_rad;C_rad/H/TwoDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [H_rad;C_rad/H/TwoDe]
""",
)

entry(
    index = 2613,
    label = "C8H3(414) <=> C8H3(415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.601e+09, 's^-1'),
        n = 0.875,
        Ea = (62.65, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;C_rad_out_H/OneDe;Cs_H_out] + [R4H_SMS;C_rad_out_1H;Cs_H_out] for rate rule\n[R4H_SBS;C_rad_out_H/Cb;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;C_rad_out_H/OneDe;Cs_H_out] + [R4H_SMS;C_rad_out_1H;Cs_H_out] for rate rule
[R4H_SBS;C_rad_out_H/Cb;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 2614,
    label = "H_10_(3) + C8H3(415) <=> C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;H_rad] for rate rule [C_rad/ThreeDe;H_rad]
""",
)

entry(
    index = 2690,
    label = "CO_21_(14) + C8H3(414) <=> C9H3O(417)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.61e+07, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (5.32, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]\nEa raised from 20.1 to 22.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]
Ea raised from 20.1 to 22.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 2691,
    label = "CO_21_(14) + C8H3(415) <=> C9H3O(421)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.03e+07, 'cm^3/(mol*s)'),
        n = 1.468,
        Ea = (5.798, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;Cs_rad] for rate rule [COm;C_rad/ThreeDe]',
    ),
    longDesc = 
u"""
Estimated using template [COm;Cs_rad] for rate rule [COm;C_rad/ThreeDe]
""",
)

entry(
    index = 2692,
    label = "CH3(17) + C8H3(414) <=> C9H6(418)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_methyl;C_rad/H/TwoDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_methyl;C_rad/H/TwoDe]
""",
)

entry(
    index = 2693,
    label = "CH2(S)(28) + C8H4(416) <=> C9H6(418)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2694,
    label = "C2H2(20) + C8H3(415) <=> C10H5(423)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22610, 'cm^3/(mol*s)'),
        n = 2.392,
        Ea = (7.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-H;CsJ] for rate rule [Ct-H_Ct-H;CsJ-ThreeDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-H;CsJ] for rate rule [Ct-H_Ct-H;CsJ-ThreeDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2695,
    label = "CH3(17) + C8H3(415) <=> C9H6(422)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.596, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;C_ter_rad] for rate rule [C_methyl;C_rad/ThreeDe]',
    ),
    longDesc = 
u"""
Estimated using template [C_methyl;C_ter_rad] for rate rule [C_methyl;C_rad/ThreeDe]
""",
)

entry(
    index = 2696,
    label = "CH2(S)(28) + C8H4(416) <=> C9H6(422)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.735e+11, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/ThreeDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/ThreeDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2697,
    label = "H_10_(3) + C8H3(419) <=> C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Cb_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Cb_rad]
""",
)

entry(
    index = 2764,
    label = "CO_21_(14) + C8H3(415) <=> C9H3O(420)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.532e+06, 'cm^3/(mol*s)'),
        n = 2.07,
        Ea = (82.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_birad;C_sec] for rate rule [CO_birad;C/H2/TwoDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_birad;C_sec] for rate rule [CO_birad;C/H2/TwoDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2765,
    label = "C9H3O(417) <=> C9H3O(420)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.065e+06, 's^-1'),
        n = 1.749,
        Ea = (9.866, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R5H;Y_rad_out;Cs_H_out_noH] + [R5H_RSMS;Y_rad_out;Cs_H_out] for rate rule [R5H_SSMS;CO_rad_out;Cs_H_out_AromDe]\nMultiplied by reaction path degeneracy 10',
    ),
    longDesc = 
u"""
Estimated using average of templates [R5H;Y_rad_out;Cs_H_out_noH] + [R5H_RSMS;Y_rad_out;Cs_H_out] for rate rule [R5H_SSMS;CO_rad_out;Cs_H_out_AromDe]
Multiplied by reaction path degeneracy 10
""",
)

entry(
    index = 2766,
    label = "C3H8(34) <=> C2H5(31) + CH3(17)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.689, 0.5502, -0.06679, 0.002654],
            [11.76, 0.798, -0.05146, -0.009271],
            [-0.7161, 0.3293, 0.02385, -0.008101],
            [-0.2762, 0.05857, 0.02553, 0.001544],
            [-0.06977, -0.01908, 0.005502, 0.003247],
            [0.001664, -0.01849, -0.003079, 0.0005963],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2768,
    label = "C3H8(34) <=> H_10_(3) + C3H7(35)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.799, 0.9207, -0.15, 0.01516],
            [13.83, 0.8569, 0.03112, -0.03477],
            [-0.5979, 0.1988, 0.06739, -0.001634],
            [-0.1902, -0.01847, 0.02064, 0.007919],
            [-0.01983, -0.03735, -0.003808, 0.002938],
            [0.02409, -0.01638, -0.005695, -0.0003216],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2774,
    label = "C5H11(36) + CH3(17) <=> C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_methyl]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;C_methyl]
""",
)

entry(
    index = 2776,
    label = "C5H11(36) <=> C3H7(35) + C2H4(30)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.99, 0.7278, -0.1095, 0.001355],
            [3.393, 0.9354, -0.05526, -0.02319],
            [-0.4922, 0.2756, 0.06719, -0.01321],
            [-0.2003, 0.02889, 0.04556, 0.006293],
            [-0.08642, -0.008106, 0.01224, 0.006692],
            [-0.03268, -0.01493, 0.0026, 0.003031],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2781,
    label = "C3H8(34) <=> CCadd(1) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.389, 1.144, -0.1989, 0.01174],
            [14.19, 0.7258, 0.1057, -0.04022],
            [-0.6932, 0.1352, 0.06485, 0.008397],
            [-0.1991, -0.02907, 0.009311, 0.009273],
            [-0.01951, -0.03213, -0.007822, 0.001707],
            [0.02337, -0.01164, -0.005799, -0.0009991],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2782,
    label = "C5H11(36) <=> CH2(S)(28) + C4H9(37)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.497, 1.92, -0.0521, -0.02571],
            [15.01, 0.07156, 0.04527, 0.0211],
            [-0.2316, -0.01122, -0.006022, -0.00177],
            [-0.1875, 0.01329, 0.008167, 0.00358],
            [-0.1094, 0.004118, 0.002885, 0.00161],
            [-0.02941, -0.002065, -0.001285, -0.0005745],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2791,
    label = "CH2CO(16) <=> H_10_(3) + HCCO(26)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.757, 0.5289, -0.1204, 0.01549],
            [15.04, 0.6089, -0.05547, -0.01861],
            [-0.329, 0.2242, 0.02256, -0.01142],
            [-0.1398, 0.05623, 0.02045, 0.0005529],
            [-0.05397, 0.007145, 0.006942, 0.002519],
            [-0.01926, -0.001901, 0.000812, 0.001032],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2792,
    label = "HCCO(26) <=> O_11_(7) + C2H(21)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-21.8, 1.996, -0.002558, -0.001414],
            [21.73, 0.003475, 0.00241, 0.00133],
            [-0.2864, -3.947e-05, -2.567e-05, -1.26e-05],
            [-0.101, -7.46e-05, -5.18e-05, -2.865e-05],
            [-0.03526, -2.684e-05, -1.869e-05, -1.039e-05],
            [-0.01204, -7.923e-06, -5.522e-06, -3.073e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2810,
    label = "CHO2(42) <=> H_10_(3) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.246, 1.349, -0.1289, -0.01256],
            [1.94, 0.4865, 0.06483, -0.003087],
            [-0.04302, 0.01634, 0.01242, 0.00343],
            [0.01454, -0.004579, -0.0005861, 3.218e-05],
            [0.00541, 0.0006011, 0.0001612, -1.678e-05],
            [-0.000863, 0.0005008, 0.0003604, 5.799e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2812,
    label = "OH_12_(12) + CO_21_(14) <=> CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.847, 0.06315, -0.04012, 0.0189],
            [0.3975, 0.07915, -0.04909, 0.02198],
            [-0.01634, 0.02745, -0.01623, 0.0065],
            [-0.001253, 0.001962, -0.0008549, 3.436e-05],
            [0.002648, -0.004447, 0.002624, -0.001047],
            [0.002136, -0.003503, 0.001892, -0.0005821],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2813,
    label = "C3H3(43) <=> C3H3(19)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.306, 1.23, -0.1763, -0.006352],
            [1.858, 0.6011, 0.08221, -0.01932],
            [-0.1719, 0.03607, 0.035, 0.009649],
            [-0.04334, -0.004423, 0.00262, 0.002604],
            [-0.02168, 0.006555, 0.001335, -0.0002465],
            [-0.01305, 0.003897, 0.001411, 3.331e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2818,
    label = "C3H3(19) + C3H3(19) <=> C6H6(46)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.96, 0.5817, -0.07887, 0.003455],
            [-1.112, 0.8267, -0.06634, -0.00886],
            [-0.6021, 0.2901, 0.02884, -0.009937],
            [-0.2175, 0.01507, 0.03023, 0.001664],
            [-0.06215, -0.02321, 0.003783, 0.003642],
            [-0.0253, 0.0002268, -0.003784, 3.685e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2819,
    label = "C3H3(19) + C3H3(19) <=> C6H6(47)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.02, 0.6951, -0.1765, 0.0251],
            [-0.8148, 0.7034, -0.04604, -0.04054],
            [-0.3144, 0.1919, 0.06023, -0.02315],
            [-0.1271, 0.05588, 0.02455, 0.002221],
            [-0.06455, 0.03585, -0.0003648, 0.00296],
            [-0.027, 0.01085, 0.00222, -8.351e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2822,
    label = "C5H5(49) <=> C5H5(50)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+10, 's^-1'), n=0.31, Ea=(12.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 2823,
    label = "C7H9(59) <=> C6H6(54) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+11, 's^-1'), n=1.15, Ea=(39.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 2824,
    label = "C7H9(60) <=> C6H6(48) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.07e+11, 's^-1'), n=0.83, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 2825,
    label = "C7H9(60) <=> H_10_(3) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.03e+09, 's^-1'), n=1.36, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 2826,
    label = "C2H2(20) + R1(63) <=> W1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.068e+06, 'cm^3/(mol*s)'),
        n = 1.842,
        Ea = (3.272, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 2827,
    label = "W1_2(67) <=> W5(68)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+11, 's^-1'), n=0.633, Ea=(46.955, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2828,
    label = "W3_4(69) <=> W6(70)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 's^-1'), n=2.932, Ea=(30.907, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2829,
    label = "C3H4(45) + C6H5(64) <=> W1_2(67)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.075e+06, 'cm^3/(mol*s)'),
        n = 2.038,
        Ea = (3.037, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2830,
    label = "C3H4(39) + C6H5(64) <=> W6(70)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28890, 'cm^3/(mol*s)'),
        n = 2.595,
        Ea = (3.241, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2831,
    label = "H_10_(3) + P2(71) <=> W1_2(67)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.639e+10, 'cm^3/(mol*s)'),
        n = 1.06,
        Ea = (4.834, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2832,
    label = "H_10_(3) + P2(71) <=> W5(68)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.492e+10, 'cm^3/(mol*s)'),
        n = 1.051,
        Ea = (3.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2833,
    label = "H_10_(3) + C9H8(72) <=> W1_2(67)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.175e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 2834,
    label = "C6H5(64) + C3H3(19) <=> P4(73)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 2835,
    label = "C6H5(64) + C3H3(19) <=> C9H8(72)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 2837,
    label = "O2_2_(13) + C6H7(52) <=> S(425)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.132e+14, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/Cs] for rate rule [O2_birad;C_rad/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/Cs] for rate rule [O2_birad;C_rad/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2838,
    label = "S(425) <=> HO2_17_(5) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.956e+08, 's^-1'),
        n = 1.442,
        Ea = (28.462, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2OO_2H] for rate rule [R2OO_2H_DeDe]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [R2OO_2H] for rate rule [R2OO_2H_DeDe]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2843,
    label = "C6H5(122) <=> C6H5(426)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.423e+09, 's^-1'),
        n = 0.834,
        Ea = (24.235, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D_D;doublebond_intra_HDe;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R4_D_D;doublebond_intra_HDe;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH]
""",
)

entry(
    index = 2844,
    label = "C6H5(122) <=> C6H5(427)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.767e+11, 's^-1'),
        n = 0.248,
        Ea = (19.557, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D_D;doublebond_intra_pri_HDe;radadd_intra_cdsingleH] for rate rule\n[R4_D_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R4_D_D;doublebond_intra_pri_HDe;radadd_intra_cdsingleH] for rate rule
[R4_D_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH]
""",
)

entry(
    index = 2880,
    label = "CHO2(424) <=> H_10_(3) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.64, 1.965, -0.01944, -0.007273],
            [-0.1971, 0.03587, 0.01931, 0.006332],
            [-0.04853, -0.00344, -0.001509, -8.406e-05],
            [-0.01181, -0.001104, -0.0004979, -8.965e-05],
            [-0.003442, -3.731e-05, -3.953e-05, -3.866e-05],
            [-0.001157, 4.917e-05, 1.452e-05, -6.107e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2881,
    label = "CHO2(424) <=> CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.9638, 1.999, -0.0004722, -0.000262],
            [5.406, -0.0001163, -8.088e-05, -4.485e-05],
            [0.06602, 3.11e-05, 2.164e-05, 1.201e-05],
            [0.007445, 2.789e-05, 1.94e-05, 1.076e-05],
            [-0.0008377, 1.41e-05, 9.807e-06, 5.438e-06],
            [-0.001396, 6.176e-06, 4.296e-06, 2.382e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2883,
    label = "O_11_(7) + HCO(22) <=> CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.03, 1.041, -0.1927, -0.006258],
            [-0.596, 0.3912, 0.04081, -0.01218],
            [-0.2174, 0.09352, 0.02347, 0.0006051],
            [-0.07956, 0.02338, 0.006952, 0.001114],
            [-0.02841, 0.005422, 0.001792, 0.0004345],
            [-0.01012, 0.001199, 0.0004379, 0.0001241],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 2908,
    label = "H_10_(3) + S(433) <=> S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;H_rad]
""",
)

entry(
    index = 2917,
    label = "C2H5(31) + C3H7O(436) <=> S(429)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;C_rad/H2/Cs]
""",
)

entry(
    index = 2918,
    label = "C2H4(30) + C3H7O(436) <=> S(433)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001432, 'cm^3/(mol*s)'),
        n = 3.97,
        Ea = (78.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Cd/unsub_Cd/unsub;R_OH]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Cd/unsub_Cd/unsub;R_OH]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 2920,
    label = "H_10_(3) + C3H6O(437) <=> C3H7O(436)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.014e+08, 'cm^3/(mol*s)'),
        n = 1.733,
        Ea = (0.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-Cs\\Os/H;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-Cs\Os/H;HJ]
""",
)

entry(
    index = 2928,
    label = "H_10_(3) + S(434) <=> S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.464e+12, 'cm^3/(mol*s)'),
        n = 0.027,
        Ea = (0.223, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;H_rad] for rate rule [C_rad/H/CsO;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;H_rad] for rate rule [C_rad/H/CsO;H_rad]
""",
)

entry(
    index = 2937,
    label = "S(433) <=> S(434)",
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
    index = 2940,
    label = "OH_12_(12) + C3H6(38) <=> C3H7O(436)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-2.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-Cs\\H3/H;OJ_pri]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-Cs\H3/H;OJ_pri]
""",
)

entry(
    index = 2942,
    label = "H_10_(3) + S(435) <=> S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+12, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H2/Cs;H_rad from training reaction 17\nExact match found for rate rule [C_rad/H2/Cs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H2/Cs;H_rad from training reaction 17
Exact match found for rate rule [C_rad/H2/Cs;H_rad]
""",
)

entry(
    index = 2951,
    label = "S(433) <=> S(435)",
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
    index = 2954,
    label = "S(435) <=> S(434)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (92.2, 's^-1'),
        n = 3.21,
        Ea = (6.53, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_SSSS;C_rad_out_2H;Cs_H_out_1H] for rate rule [R5H_SSSS;C_rad_out_2H;Cs_H_out_H/NonDeO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R5H_SSSS;C_rad_out_2H;Cs_H_out_1H] for rate rule [R5H_SSSS;C_rad_out_2H;Cs_H_out_H/NonDeO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2960,
    label = "C2H5(31) + C3H7O(432) <=> S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 2961,
    label = "C2H4(30) + CH2OH(32) <=> C3H7O(432)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5100, 'cm^3/(mol*s)'),
        n = 2.562,
        Ea = (5.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-OsHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-OsHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2962,
    label = "C3H7O(436) <=> C3H7O(432)",
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
    index = 2970,
    label = "C2H4(30) + C3H7O(432) <=> S(435)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3980, 'cm^3/(mol*s)'),
                n = 2.44,
                Ea = (5.37, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-CsHH]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (0.0001432, 'cm^3/(mol*s)'),
                n = 3.97,
                Ea = (78.7, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Cd/unsub_Cd/unsub;Cs_OH] for rate rule [Cd/unsub_Cd/unsub;C_pri_OH]\nMultiplied by reaction path degeneracy 8',
            ),
        ],
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-CsHH]
Multiplied by reaction path degeneracy 2
Estimated using template [Cd/unsub_Cd/unsub;Cs_OH] for rate rule [Cd/unsub_Cd/unsub;C_pri_OH]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 2972,
    label = "C3H7(35) + C2H4O(438) <=> S(434)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1071, 'cm^3/(mol*s)'),
        n = 2.72,
        Ea = (8.24, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-OsH;CsJ-CsHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-OsH;CsJ-CsHH]
""",
)

entry(
    index = 2973,
    label = "H_10_(3) + C3H6O(437) <=> C3H7O(432)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.73e+08, 'cm^3/(mol*s)'),
        n = 1.583,
        Ea = (1.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-Cs\\Os/H_Cds-HH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-Cs\Os/H_Cds-HH;HJ]
""",
)

entry(
    index = 2974,
    label = "OH_12_(12) + C3H5(41) <=> C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C_pri_rad] for rate rule [O_pri_rad;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;C_pri_rad] for rate rule [O_pri_rad;C_rad/H2/Cd]
""",
)

entry(
    index = 2980,
    label = "C2H4O(431) <=> CO_21_(14) + Cadd(4)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(5.44e+21, 's^-1'), n=-1.74, Ea=(86.364, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.29e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95.922, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
        comment = 'Warning: SRI parameters from chemkin file ignored on import.',
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
Warning: SRI parameters from chemkin file ignored on import.
""",
)

entry(
    index = 2983,
    label = "C2H4O(438) <=> C2H4O(431)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7040, 's^-1'),
        n = 2.66,
        Ea = (48.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds/H2_Cds/HOH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds/H2_Cds/HOH]
""",
)

entry(
    index = 2984,
    label = "C2H4O(431) + CH3(17) <=> C3H7O(439)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (8.577, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Od_CO-CsH;YJ] for rate rule [Od_CO-CsH;CsJ-HHH]',
    ),
    longDesc = 
u"""
Estimated using template [Od_CO-CsH;YJ] for rate rule [Od_CO-CsH;CsJ-HHH]
""",
)

entry(
    index = 2993,
    label = "C2H4O(431) <=> HCO(22) + CH3(17)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(2.18e+22, 's^-1'), n=-1.74, Ea=(86.364, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.15e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95.922, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
        comment = 'Warning: SRI parameters from chemkin file ignored on import.',
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
Warning: SRI parameters from chemkin file ignored on import.
""",
)

entry(
    index = 3000,
    label = "C2H3(29) + CH2OH(32) <=> C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cd_rad] for rate rule [C_rad/H2/O;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cd_rad] for rate rule [C_rad/H2/O;Cd_pri_rad]
""",
)

entry(
    index = 3005,
    label = "OH_12_(12) + C2H3(29) <=> C2H4O(438)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.748e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.025, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_pri_rad] + [O_pri_rad;Y_rad] for rate rule [O_pri_rad;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_pri_rad] + [O_pri_rad;Y_rad] for rate rule [O_pri_rad;Cd_pri_rad]
""",
)

entry(
    index = 3014,
    label = "C2H4O(431) + C3H3(19) <=> C5H7O(442)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (8.577, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Od_CO-CsH;YJ] for rate rule [Od_CO-CsH;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Od_CO-CsH;YJ] for rate rule [Od_CO-CsH;CdsJ=Cdd]
""",
)

entry(
    index = 3029,
    label = "C2H4O(431) + C3H3(19) <=> C5H7O(441)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.76e+06, 'cm^3/(mol*s)'),
        n = 1.99,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO-CsH_O;YJ] for rate rule [CO-CsH_O;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [CO-CsH_O;YJ] for rate rule [CO-CsH_O;CdsJ=Cdd]
""",
)

entry(
    index = 3033,
    label = "C3H3(19) + C6H6(54) <=> C9H9(448)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5580, 'cm^3/(mol*s)'),
        n = 2.91,
        Ea = (1.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CdH_Cds-CdH_cyc5_2;CJ] for rate rule [Cds-CdH_Cds-CdH_cyc5_2;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CdH_Cds-CdH_cyc5_2;CJ] for rate rule [Cds-CdH_Cds-CdH_cyc5_2;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3034,
    label = "CH3(17) + C6H6(54) <=> C7H9(446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2790, 'cm^3/(mol*s)'),
        n = 2.91,
        Ea = (1.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 25 C6H6-4 + CH3 <=> C7H9-16 in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 25 C6H6-4 + CH3 <=> C7H9-16 in R_Addition_MultipleBond/training
""",
)

entry(
    index = 3035,
    label = "C3H3(19) + C6H6(54) <=> C9H9(449)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4940, 'cm^3/(mol*s)'),
        n = 2.88,
        Ea = (2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CdH_Cds-CdH_cyc5_1;CJ] for rate rule [Cds-CdH_Cds-CdH_cyc5_1;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CdH_Cds-CdH_cyc5_1;CJ] for rate rule [Cds-CdH_Cds-CdH_cyc5_1;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3036,
    label = "C3H3(19) + C6H6(54) <=> C9H9(450)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29750, 'cm^3/(mol*s)'),
        n = 2.442,
        Ea = (-1.714, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-CdCd;CJ] for rate rule [Cds-HH_Cds-CdCd;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-CdCd;CJ] for rate rule [Cds-HH_Cds-CdCd;CdsJ=Cdd]
""",
)

entry(
    index = 3037,
    label = "C6H6(47) <=> C6H6(94)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.309e+10, 's^-1'),
        n = 0.36,
        Ea = (34.586, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 C6H6 <=> C6H6-2 in 6_membered_central_C-C_shift/training',
    ),
    longDesc = 
u"""
Matched reaction 1 C6H6 <=> C6H6-2 in 6_membered_central_C-C_shift/training
""",
)

entry(
    index = 3038,
    label = "CH3(17) + C6H6(54) <=> C7H9(447)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2470, 'cm^3/(mol*s)'),
        n = 2.88,
        Ea = (2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 26 C6H6-5 + CH3 <=> C7H9-17 in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 26 C6H6-5 + CH3 <=> C7H9-17 in R_Addition_MultipleBond/training
""",
)

entry(
    index = 3039,
    label = "C7H9(447) <=> C7H9(446)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.59e+09, 's^-1'),
        n = 0.99,
        Ea = (43.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 2 C7H9-3 <=> C7H9-4 in 1,2_shiftC/training',
    ),
    longDesc = 
u"""
Matched reaction 2 C7H9-3 <=> C7H9-4 in 1,2_shiftC/training
""",
)

entry(
    index = 3040,
    label = "C6H6(102) <=> C6H6(452)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.39e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
""",
)

entry(
    index = 3041,
    label = "C6H6(107) <=> C6H6(453)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.726e+10, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH(C)C]',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH(C)C]
""",
)

entry(
    index = 3042,
    label = "C6H6(452) <=> C6H6(453)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.78e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3043,
    label = "C7H9(447) <=> C7H9(455)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.39e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
""",
)

entry(
    index = 3044,
    label = "C3H4(45) + CH3(17) <=> C4H7(440)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (138000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (8.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cs_Ct-H;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cs_Ct-H;CsJ-HHH]
""",
)

entry(
    index = 3045,
    label = "CH2(S)(28) + C3H5(65) <=> C4H7(440)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.438e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3046,
    label = "C3H3(19) + CH2CO(16) <=> C5H5O(464)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.832e+09, 'cm^3/(mol*s)'),
        n = 1.415,
        Ea = (4.792, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CdsJ=Cdd]
""",
)

entry(
    index = 3047,
    label = "CO_21_(14) + C4H5(465) <=> C5H5O(464)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.056e+08, 'cm^3/(mol*s)'),
        n = 1.155,
        Ea = (7.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_pri_rad] for rate rule [COm;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_pri_rad] for rate rule [COm;C_rad/H2/Cd]
""",
)

entry(
    index = 3048,
    label = "H_10_(3) + CH3CO(18) <=> C2H4O(431)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3085,
    label = "H_10_(3) + C4H5(443) <=> C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;H_rad] for rate rule [C_rad/H/CtCs;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;H_rad] for rate rule [C_rad/H/CtCs;H_rad]
""",
)

entry(
    index = 3099,
    label = "H_10_(3) + C4H5(443) <=> C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 3115,
    label = "C4H5(465) <=> C4H5(443)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.371e+06, 's^-1'),
        n = 1.693,
        Ea = (28.272, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;Y_rad_out;Cd_H_out_singleH] + [R4H;C_rad_out_2H;XH_out] for rate rule\n[R4H_SMM;C_rad_out_2H;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;Y_rad_out;Cd_H_out_singleH] + [R4H;C_rad_out_2H;XH_out] for rate rule
[R4H_SMM;C_rad_out_2H;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3122,
    label = "H_10_(3) + C4H4(444) <=> C4H5(465)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.64, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Cd;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Cd;HJ]
""",
)

entry(
    index = 3127,
    label = "H_10_(3) + C4H4(444) <=> C4H5(443)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-0.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-CtH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-CtH;HJ]
""",
)

entry(
    index = 3128,
    label = "C3H3(19) + CH2(S)(28) <=> C4H5(443)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd_pri from training reaction 5\nExact match found for rate rule [carbene;Cd_pri]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd_pri from training reaction 5
Exact match found for rate rule [carbene;Cd_pri]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3129,
    label = "C2H(21) + C2H3(29) <=> C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct_rad/Ct;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct_rad/Ct;Cd_pri_rad]
""",
)

entry(
    index = 3130,
    label = "H_10_(3) + C4H3(110) <=> C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/OneDe;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/OneDe;H_rad]
""",
)

entry(
    index = 3131,
    label = "H_10_(3) + C4H3(96) <=> C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;H_rad]
""",
)

entry(
    index = 3284,
    label = "C4H4(467) <=> C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 3285,
    label = "C4H4(466) <=> C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.674e+10, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3322,
    label = "O2_2_(13) + C5H3(141) <=> S(470)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.201e+12, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (-1.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3323,
    label = "O2_2_(13) + C5H3(141) <=> S(469)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.201e+12, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (0.484, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]\nMultiplied by reaction path degeneracy 2\nEa raised from -7.1 to 2.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]
Multiplied by reaction path degeneracy 2
Ea raised from -7.1 to 2.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3324,
    label = "O2_2_(13) + C5H3(141) <=> S(468)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.212e+13, 'cm^3/(mol*s)'),
        n = -0.229,
        Ea = (-0.036, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H2/Ct] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H2/Ct] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3325,
    label = "S(469) <=> S(468)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.168e+09, 's^-1'),
        n = 0.809,
        Ea = (39.151, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3326,
    label = "C3H3(19) + C5H4(130) <=> C8H7(454)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (204200, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 3327,
    label = "CH2(S)(28) + C7H5(120) <=> C8H7(454)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        Ea = (-2.214, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Ct_H from training reaction 3\nExact match found for rate rule [carbene;Ct_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Ct_H from training reaction 3
Exact match found for rate rule [carbene;Ct_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3328,
    label = "C9H5(166) <=> C9H5(472)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3329,
    label = "C9H5(170) <=> C9H5(473)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3330,
    label = "C9H5(170) <=> C9H5(474)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3331,
    label = "C9H5(170) <=> C9H5(475)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 3332,
    label = "C5H4(130) + C5H3(141) <=> C10H7(460)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.553, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 3333,
    label = "C5H4(130) + C5H3(141) <=> C10H7(461)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.553, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 3334,
    label = "CH2(S)(28) + C9H5(166) <=> C10H7(461)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3335,
    label = "C4H2(111) + C5H3(141) <=> C9H5(459)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (262000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (7.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-CtHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;CsJ-CtHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3336,
    label = "C9H5(165) <=> C9H5(459)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.168e+09, 's^-1'),
        n = 0.809,
        Ea = (39.151, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CdH2_1;unsaturated_end] for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;CdHC_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CdH2_1;unsaturated_end] for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;CdHC_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3337,
    label = "C9H5(459) <=> C9H5(476)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.42e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3338,
    label = "C9H5(459) <=> C9H5(478)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 3339,
    label = "C7H5(120) <=> C7H5(456)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.456e+11, 's^-1'),
        n = 0.86,
        Ea = (45.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_singleH] for rate rule [R7H;Cd_rad_out_singleH;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_singleH] for rate rule [R7H;Cd_rad_out_singleH;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3340,
    label = "C7H5(118) <=> C7H5(456)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (272000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;Cd_rad_out_singleH;Cs_H_out] for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R5H;Cd_rad_out_singleH;Cs_H_out] for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3341,
    label = "C7H5(456) <=> C7H5(481)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.31,
        Ea = (8.287, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]\nEa raised from 33.6 to 34.7 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]
Ea raised from 33.6 to 34.7 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3342,
    label = "C7H5(479) <=> C7H5(456)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (408000, 's^-1'),
                n = 1.92,
                Ea = (7.897, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R5H_DSMS;Cd_rad_out_single;Cs_H_out_2H] for rate rule [R5H_DSMS;Cd_rad_out_singleDe_Ct;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 3',
            ),
            Arrhenius(
                A = (6.252e+09, 's^-1'),
                n = 0.809,
                Ea = (39.151, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;CddC_2] for rate rule [1_3_unsaturated_pentane_backbone;CH3_1;CddC_2]\nMultiplied by reaction path degeneracy 3',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [R5H_DSMS;Cd_rad_out_single;Cs_H_out_2H] for rate rule [R5H_DSMS;Cd_rad_out_singleDe_Ct;Cs_H_out_2H]
Multiplied by reaction path degeneracy 3
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;CddC_2] for rate rule [1_3_unsaturated_pentane_backbone;CH3_1;CddC_2]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3344,
    label = "C7H5(481) <=> C7H5(156)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (383, 's^-1'),
        n = 3.05,
        Ea = (53.137, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_DS;Cd_rad_out_single;Cd_H_out_doubleC] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cd;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3H_DS;Cd_rad_out_single;Cd_H_out_doubleC] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cd;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3345,
    label = "C4H2(111) + C3H3(86) <=> C7H5(479)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.021e+09, 'cm^3/(mol*s)'),
        n = 1.143,
        Ea = (0.591, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3346,
    label = "C7H5(481) <=> C7H5(482)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1733, 's^-1'),
        n = 2.536,
        Ea = (34.52, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R5H;C_rad_out_2H;Cd_H_out_single] + [R5H_RSDD;Y_rad_out;Cd_H_out_single] for rate rule\n[R5H_RSDD;C_rad_out_2H;Cd_H_out_singleDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R5H;C_rad_out_2H;Cd_H_out_single] + [R5H_RSDD;Y_rad_out;Cd_H_out_single] for rate rule
[R5H_RSDD;C_rad_out_2H;Cd_H_out_singleDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3347,
    label = "C7H5(479) <=> C7H5(482)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6;triplebond_intra_Nd;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6;triplebond_intra_Nd;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3348,
    label = "C7H5(482) <=> C7H5(156)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.608e+09, 's^-1'),
        n = 1.24,
        Ea = (36.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_SS;Cd_rad_out_double;Cs_H_out_2H] for rate rule [R3H_SS_2Cd;Cd_rad_out_Cd;Cs_H_out_2H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [R3H_SS;Cd_rad_out_double;Cs_H_out_2H] for rate rule [R3H_SS_2Cd;Cd_rad_out_Cd;Cs_H_out_2H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 3349,
    label = "H_10_(3) + C7H4(484) <=> C7H5(479)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-Ct;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-Ct;HJ]
""",
)

entry(
    index = 3350,
    label = "C7H5(483) <=> C7H5(481)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (16.237, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;triplebond_intra_H;radadd_intra_cdsingleH]\nEa raised from 65.7 to 67.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;triplebond_intra_H;radadd_intra_cdsingleH]
Ea raised from 65.7 to 67.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3351,
    label = "C2H(21) + C5H3(142) <=> C7H4(484)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Ct_rad/Ct] + [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Ct_rad/Ct] + [Ct_rad/Ct;Y_rad] for rate rule [Ct_rad/Ct;Ct_rad/Ct]
""",
)

entry(
    index = 3352,
    label = "C5H4(158) + C2H(21) <=> C7H5(483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1745, 'cm^3/(mol*s)'),
        n = 2.674,
        Ea = (7.655, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ca_Cds-HH;CJ] for rate rule [Ca_Cds-HH;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ca_Cds-HH;CJ] for rate rule [Ca_Cds-HH;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3370,
    label = "C7H4(485) <=> C7H4(484)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 3371,
    label = "C7H5(456) <=> C7H5(480)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.73e+10, 's^-1'),
        n = 0.19,
        Ea = (11.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R5_MM;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R5;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R5_MM;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3372,
    label = "C7H5(119) <=> C7H5(483)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.854, 's^-1'),
        n = 3.311,
        Ea = (30.765, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cd_rad_out_singleH;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cd_rad_out_singleH;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3373,
    label = "C9H5(459) <=> C9H5(477)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (10.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R9;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3374,
    label = "C7H5(120) <=> C7H5(457)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.581e+09, 's^-1'),
        n = 0.409,
        Ea = (10.225, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;doublebond_intra;radadd_intra_cdsingle] for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;doublebond_intra;radadd_intra_cdsingle] for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 3375,
    label = "CO_21_(14) + C5H3(141) <=> C6H3O(458)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.056e+08, 'cm^3/(mol*s)'),
        n = 1.155,
        Ea = (7.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_pri_rad] for rate rule [COm;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_pri_rad] for rate rule [COm;C_rad/H2/Ct]
""",
)

entry(
    index = 3376,
    label = "C4H2(111) + C4H3(110) <=> C8H5(451)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (287600, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-0.545, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CdsJ] for rate rule [Ct-H_Ct-Ct;CdsJ-Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CdsJ] for rate rule [Ct-H_Ct-Ct;CdsJ-Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3377,
    label = "C8H5(451) <=> C8H5(486)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3378,
    label = "C5H5(462) <=> C5H5(97)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+10, 's^-1'),
        n = 0.98,
        Ea = (26.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;Cd_rad_out_Cd;Cs_H_out_H/OneDe] for rate rule [R2H_S;Cd_rad_out_Cd;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;Cd_rad_out_Cd;Cs_H_out_H/OneDe] for rate rule [R2H_S;Cd_rad_out_Cd;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3397,
    label = "C5H5(49) <=> C5H5(462)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.73,
        Ea = (42.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd]
""",
)

entry(
    index = 3398,
    label = "H_10_(3) + C5H4(158) <=> C5H5(462)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.78, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CtH_Ca;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CtH_Ca;HJ]
""",
)

entry(
    index = 3399,
    label = "C3H4(39) + C2H(21) <=> C5H5(462)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.27e+06, 'cm^3/(mol*s)'),
        n = 1.647,
        Ea = (3.997, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Ca;CJ] for rate rule [Cds-HH_Ca;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Ca;CJ] for rate rule [Cds-HH_Ca;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3400,
    label = "C5H5(462) <=> C5H5(487)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.47e+11, 's^-1'),
        n = 0.15,
        Ea = (14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cddouble] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_cddouble]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cddouble] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_cddouble]
""",
)

entry(
    index = 3401,
    label = "C9H5(166) <=> C9H5(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.31,
        Ea = (2.962, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3402,
    label = "C9H5(489) <=> C9H5(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.57e+10, 's^-1'),
        n = 0.43,
        Ea = (1.924, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_D;doublebond_intra;radadd_intra_cdsingle] for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_D;doublebond_intra;radadd_intra_cdsingle] for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 3403,
    label = "C9H5(170) <=> C9H5(489)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.165e+09, 's^-1'),
        n = 0.738,
        Ea = (52.276, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;CtH_2] for rate rule [1_3_unsaturated_pentane_backbone;CdHC_1;CtH_2]',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;CtH_2] for rate rule [1_3_unsaturated_pentane_backbone;CdHC_1;CtH_2]
""",
)

entry(
    index = 3404,
    label = "C9H5(488) <=> C9H5(471)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.428e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_5_unsaturated_hexane from training reaction 3\nExact match found for rate rule [1_5_unsaturated_hexane]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
1_5_unsaturated_hexane from training reaction 3
Exact match found for rate rule [1_5_unsaturated_hexane]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3405,
    label = "C9H5(489) <=> C9H5(488)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6;triplebond_intra_De;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R6;triplebond_intra_De;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3406,
    label = "C9H5(489) <=> C9H5(490)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.31,
        Ea = (2.962, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R8;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R8;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3411,
    label = "C4H3O(115) <=> C4H3O(463)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (0.181, 's^-1'),
                n = 3.889,
                Ea = (26.006, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R3H_DS;Cd_rad_out_singleDe;O_H_out] for rate rule [R3H_DS;Cd_rad_out_singleDe_Ct;O_H_out]',
            ),
            Arrhenius(
                A = (37990, 's^-1'),
                n = 2.515,
                Ea = (48.8, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using an average for rate rule [C_COH]',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [R3H_DS;Cd_rad_out_singleDe;O_H_out] for rate rule [R3H_DS;Cd_rad_out_singleDe_Ct;O_H_out]
Estimated using an average for rate rule [C_COH]
""",
)

entry(
    index = 3413,
    label = "C4H3O(463) <=> C4H3O(87)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46950, 's^-1'),
        n = 2.23,
        Ea = (28.947, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [RnH;Cd_rad_out_singleH;Cd_H_out_singleDe] + [R3H;Cd_rad_out_singleH;XH_out] for rate rule\n[R3H;Cd_rad_out_singleH;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [RnH;Cd_rad_out_singleH;Cd_H_out_singleDe] + [R3H;Cd_rad_out_singleH;XH_out] for rate rule
[R3H;Cd_rad_out_singleH;Cd_H_out_singleDe]
""",
)

entry(
    index = 3414,
    label = "O_11_(7) + C4H3(96) <=> C4H3O(463)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [Cd_pri_rad;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [Cd_pri_rad;Oa]
""",
)

entry(
    index = 3415,
    label = "C4H3O(463) <=> C4H3O(88)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3281, 's^-1'),
        n = 2.585,
        Ea = (36.928, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;C_rad_out_H/OneDe;CO_H_out] + [R2H_S;C_rad_out_H/Ct;XH_out] for rate rule [R2H_S;C_rad_out_H/Ct;CO_H_out]',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;C_rad_out_H/OneDe;CO_H_out] + [R2H_S;C_rad_out_H/Ct;XH_out] for rate rule [R2H_S;C_rad_out_H/Ct;CO_H_out]
""",
)

entry(
    index = 3416,
    label = "C4H3O(463) <=> C4H3O(89)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.164e+06, 's^-1'),
        n = 1.737,
        Ea = (21.095, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;Cd_rad_out_singleH;XH_out] for rate rule [R4H_MMS;Cd_rad_out_singleH;CO_H_out]',
    ),
    longDesc = 
u"""
Estimated using template [R4H;Cd_rad_out_singleH;XH_out] for rate rule [R4H_MMS;Cd_rad_out_singleH;CO_H_out]
""",
)

entry(
    index = 3417,
    label = "CO_21_(14) + C3H3(19) <=> C4H3O(463)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (118400, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_birad;R_H] for rate rule [CO_birad;Cd_pri]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_birad;R_H] for rate rule [CO_birad;Cd_pri]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3422,
    label = "H_10_(3) + C4H4(445) <=> C4H5(465)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.111e+09, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (5.344, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ca-Cdd_Cds-HH;HJ from training reaction 110\nExact match found for rate rule [Ca-Cdd_Cds-HH;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Ca-Cdd_Cds-HH;HJ from training reaction 110
Exact match found for rate rule [Ca-Cdd_Cds-HH;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3428,
    label = "H_10_(3) + C4H3(110) <=> C4H4(445)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_allenic;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_allenic;H_rad]
""",
)

entry(
    index = 3459,
    label = "C2H3O(430) <=> O_11_(7) + C2H3(29)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-15.95, 1.996, -0.002664, -0.001471],
            [17.62, 0.004169, 0.00289, 0.001594],
            [-0.2438, -0.0006333, -0.0004368, -0.0002388],
            [-0.02468, -0.000223, -0.0001554, -8.649e-05],
            [0.0118, -1.308e-05, -9.265e-06, -5.293e-06],
            [0.004627, 2.348e-05, 1.632e-05, 9.035e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 3475,
    label = "CO2_5_(8) + C3H3(19) <=> S(491)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5918, 'cm^3/(mol*s)'),
        n = 2.968,
        Ea = (25.666, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Od_Cdd;YJ] for rate rule [Od_Cdd-Od;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2\nEa raised from 103.8 to 107.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Od_Cdd;YJ] for rate rule [Od_Cdd-Od;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
Ea raised from 103.8 to 107.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3484,
    label = "O2_2_(13) + C5H3(162) <=> S(496)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.201e+12, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (-1.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3485,
    label = "CH3(17) + C5H3(141) <=> C6H6(495)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.822e+15, 'cm^3/(mol*s)'),
        n = -0.864,
        Ea = (0.195, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cs_rad;C_rad/H2/Ct] + [C_methyl;C_pri_rad] for rate rule [C_methyl;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cs_rad;C_rad/H2/Ct] + [C_methyl;C_pri_rad] for rate rule [C_methyl;C_rad/H2/Ct]
""",
)

entry(
    index = 3486,
    label = "CH2(S)(28) + C5H4(130) <=> C6H6(495)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.508e+11, 'cm^3/(mol*s)'),
        n = 0.524,
        Ea = (-0.711, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;C_pri/Ct from training reaction 4\nExact match found for rate rule [carbene;C_pri/Ct]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
carbene;C_pri/Ct from training reaction 4
Exact match found for rate rule [carbene;C_pri/Ct]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 3487,
    label = "C9H5(170) <=> C9H5(497)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.31,
        Ea = (2.962, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3488,
    label = "C9H5(488) <=> C9H5(497)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.854, 's^-1'),
                n = 3.311,
                Ea = (30.765, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cd_rad_out_Cd;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (4.168e+09, 's^-1'),
                n = 0.809,
                Ea = (39.151, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = '1_3_4_pentatriene;CdH2_1;CddC_2 from training reaction 4\nExact match found for rate rule [1_3_4_pentatriene;CdH2_1;CddC_2]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cd_rad_out_Cd;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
1_3_4_pentatriene;CdH2_1;CddC_2 from training reaction 4
Exact match found for rate rule [1_3_4_pentatriene;CdH2_1;CddC_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3490,
    label = "C9H5(497) <=> C9H5(501)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.42e+11, 's^-1'),
                n = 0.258,
                Ea = (3.797, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_De;radadd_intra_cdsingleH]',
            ),
            Arrhenius(
                A = (5.153e+10, 's^-1'),
                n = 0.366,
                Ea = (5.94, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra] for rate rule [R7;triplebond_intra_H;radadd_intra]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R8;triplebond_intra_De;radadd_intra_cdsingleH]
Estimated using template [R6plus;triplebond_intra_H;radadd_intra] for rate rule [R7;triplebond_intra_H;radadd_intra]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3492,
    label = "C9H5(459) <=> C9H5(498)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (272000, 's^-1'),
        n = 1.92,
        Ea = (7.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5H;Cd_rad_out_singleH;Cs_H_out] for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R5H;Cd_rad_out_singleH;Cs_H_out] for rate rule [R5H;Cd_rad_out_singleH;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3493,
    label = "C9H5(475) <=> C9H5(501)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+12, 's^-1'),
        n = 0.045,
        Ea = (5.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R6_DSM_T;triplebond_intra_H;radadd_intra_cdsingleDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3494,
    label = "C9H5(170) <=> C9H5(498)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+07, 's^-1'),
        n = 1.364,
        Ea = (23.389, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_singleDe] for rate rule [R7H;Cd_rad_out_singleH;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cd_H_out_singleDe] for rate rule [R7H;Cd_rad_out_singleH;Cd_H_out_singleDe]
""",
)

entry(
    index = 3495,
    label = "C9H5(498) <=> C9H5(504)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.576e+10, 's^-1'),
        n = 0.366,
        Ea = (10.654, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra_H;radadd_intra] for rate rule [R7;triplebond_intra_H;radadd_intra]\nEa raised from 41.6 to 44.6 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra_H;radadd_intra] for rate rule [R7;triplebond_intra_H;radadd_intra]
Ea raised from 41.6 to 44.6 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3496,
    label = "C9H5(498) <=> C9H5(505)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10, 's^-1'),
        n = 0.31,
        Ea = (13.014, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;doublebond_intra;radadd_intra_cdsingle] for rate rule [R6;doublebond_intra;radadd_intra_cdsingleDe]\nEa raised from 53.2 to 54.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6;doublebond_intra;radadd_intra_cdsingle] for rate rule [R6;doublebond_intra;radadd_intra_cdsingleDe]
Ea raised from 53.2 to 54.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3497,
    label = "C9H5(498) <=> C9H5(502)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.881e+08, 's^-1'),
        n = 1.062,
        Ea = (16.546, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_cs2H] for rate rule [R9;triplebond_intra_H;radadd_intra_cs2H]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_cs2H] for rate rule [R9;triplebond_intra_H;radadd_intra_cs2H]
""",
)

entry(
    index = 3498,
    label = "C9H5(498) <=> C9H5(503)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.461e+11, 's^-1'),
        n = 0.368,
        Ea = (25.266, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_SD;multiplebond_intra;radadd_intra] for rate rule [R5_SD_T;triplebond_intra_De;radadd_intra]',
    ),
    longDesc = 
u"""
Estimated using template [R5_SD;multiplebond_intra;radadd_intra] for rate rule [R5_SD_T;triplebond_intra_De;radadd_intra]
""",
)

entry(
    index = 3499,
    label = "H_10_(3) + C9H4(500) <=> C9H5(489)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (3.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-Ct;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-Ct;HJ]
""",
)

entry(
    index = 3505,
    label = "C9H4(506) <=> C9H4(500)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.912e+09, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [CsJ2-C;CsJ2C;CH=C]
""",
)

entry(
    index = 3506,
    label = "C9H5(459) <=> C9H5(499)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.948e+11, 's^-1'),
        n = 0.045,
        Ea = (12.026, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6plus;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_De;radadd_intra_cdsingleH]\nEa raised from 46.3 to 50.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R6plus;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R7;triplebond_intra_De;radadd_intra_cdsingleH]
Ea raised from 46.3 to 50.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 3507,
    label = "C7H4(507) <=> C7H4(157)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.757e+10, 's^-1'),
        n = 0.224,
        Ea = (6.816, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;singletcarbene;CH] for rate rule [CdJ2=C;CdJ2;CdHC]
""",
)

entry(
    index = 3508,
    label = "C5H3(141) + C4H2(111) <=> C9H5(494)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (98420, 'cm^3/(mol*s)'),
        n = 2.322,
        Ea = (5.632, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Ct_Ct-H;CJ] for rate rule [Ct-Ct_Ct-H;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Ct_Ct-H;CJ] for rate rule [Ct-Ct_Ct-H;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3509,
    label = "C9H5(165) <=> C9H5(494)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.813e+12, 's^-1'),
        n = -0.027,
        Ea = (39.809, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_2_4_5_hexatetraene from training reaction 2\nExact match found for rate rule [1_2_4_5_hexatetraene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
1_2_4_5_hexatetraene from training reaction 2
Exact match found for rate rule [1_2_4_5_hexatetraene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3510,
    label = "C9H5(494) <=> C9H5(459)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.428e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_5_unsaturated_hexane from training reaction 3\nExact match found for rate rule [1_5_unsaturated_hexane]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
1_5_unsaturated_hexane from training reaction 3
Exact match found for rate rule [1_5_unsaturated_hexane]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3511,
    label = "C5H3(141) + C4H2(111) <=> C9H5(493)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (98420, 'cm^3/(mol*s)'),
        n = 2.322,
        Ea = (5.632, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Ct_Ct-H;CJ] for rate rule [Ct-Ct_Ct-H;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Ct_Ct-H;CJ] for rate rule [Ct-Ct_Ct-H;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3512,
    label = "C9H5(493) <=> C9H5(166)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.428e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_5_unsaturated_hexane from training reaction 3\nExact match found for rate rule [1_5_unsaturated_hexane]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
1_5_unsaturated_hexane from training reaction 3
Exact match found for rate rule [1_5_unsaturated_hexane]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3513,
    label = "C4H3(110) + C4H2(111) <=> C8H5(492)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (408400, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3514,
    label = "H_10_(3) + C4H9O(512) <=> C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.464e+12, 'cm^3/(mol*s)'),
        n = 0.027,
        Ea = (0.223, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;H_rad] for rate rule [C_rad/H/CsO;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;H_rad] for rate rule [C_rad/H/CsO;H_rad]
""",
)

entry(
    index = 3522,
    label = "CH3(17) + C3H7O(432) <=> C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C_methyl]
""",
)

entry(
    index = 3523,
    label = "C2H4O(438) + C2H5(31) <=> C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1071, 'cm^3/(mol*s)'),
        n = 2.72,
        Ea = (8.24, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-OsH;CsJ-CsHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-OsH;CsJ-CsHH]
""",
)

entry(
    index = 3531,
    label = "C4H3(110) + C2H2(20) <=> C6H5(513)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110400, 'cm^3/(mol*s)'),
        n = 2.155,
        Ea = (2.42, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-H;CdsJ] for rate rule [Ct-H_Ct-H;CdsJ-Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-H;CdsJ] for rate rule [Ct-H_Ct-H;CdsJ-Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3536,
    label = "O_11_(7) + CH3(17) <=> CH3O(508)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.18, 0.8514, -0.1675, 0.005724],
            [-0.7699, 0.5551, 0.01918, -0.02259],
            [-0.3084, 0.1372, 0.03174, -0.0001589],
            [-0.1159, 0.02792, 0.01045, 0.002453],
            [-0.04023, 0.003349, 0.002057, 0.0008566],
            [-0.0126, -0.0006952, 9.674e-05, 0.0001222],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 3540,
    label = "CH3O(508) <=> CH2OH(32)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.723, 1.272, -0.1598, -0.00558],
            [3.196, 0.601, 0.09403, -0.01253],
            [-0.2112, 0.04358, 0.03032, 0.00775],
            [-0.02257, -0.01833, -0.00179, 0.001462],
            [0.01185, -0.005501, -0.002272, -0.0005078],
            [0.005889, 0.0008053, -0.000132, -0.0001494],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 3545,
    label = "C3H3(19) + C3H4(39) <=> C6H7(510)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(850, 'cm^3/(mol*s)'), n=2.81, Ea=(8.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 3548,
    label = "C6H12(516) <=> C6H12(514)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.718e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3549,
    label = "H_10_(3) + C6H11(518) <=> C6H12(514)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.936e+13, 'cm^3/(mol*s)'),
        n = -0.055,
        Ea = (7.745, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/CdCs;H_rad from training reaction 25\nExact match found for rate rule [C_rad/H/CdCs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H/CdCs;H_rad from training reaction 25
Exact match found for rate rule [C_rad/H/CdCs;H_rad]
""",
)

entry(
    index = 3556,
    label = "C3H7(35) + C3H5(41) <=> C6H12(514)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cs]
""",
)

entry(
    index = 3557,
    label = "C6H12(516) <=> C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.105e+11, 's^-1'),
        n = 0.177,
        Ea = (7.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [singletcarbene_CH;CsJ2C;CH2(C)] + [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH2(C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [singletcarbene_CH;CsJ2C;CH2(C)] + [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH2(C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3562,
    label = "H_10_(3) + C6H11(518) <=> C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C_rad/H2/Cd]
""",
)

entry(
    index = 3566,
    label = "C2H5(31) + C4H6(511) <=> C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4780, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (1.95, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-CdH;CsJ-CsHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-CdH;CsJ-CsHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3569,
    label = "C4H6(511) <=> C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH2_1;CdH2_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH2_1;CdH2_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3572,
    label = "C4H7(522) + C2H5(31) <=> C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cs]
""",
)

entry(
    index = 3578,
    label = "H_10_(3) + C4H6(511) <=> C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (-0.47, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-CdH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-CdH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3583,
    label = "C6H12(521) <=> C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.145e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3588,
    label = "C3H7(35) + C3H5(65) <=> C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]
""",
)

entry(
    index = 3593,
    label = "H_10_(3) + C6H12(514) <=> C6H13(77)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Cds-CsH;HJ from training reaction 10\nExact match found for rate rule [Cds-HH_Cds-CsH;HJ]',
    ),
    longDesc = 
u"""
Cds-HH_Cds-CsH;HJ from training reaction 10
Exact match found for rate rule [Cds-HH_Cds-CsH;HJ]
""",
)

entry(
    index = 3601,
    label = "H_10_(3) + C6H12(519) <=> C6H13(77)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.46e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.37, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-CsH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-CsH;HJ]
""",
)

entry(
    index = 3606,
    label = "H_10_(3) + C4H7(522) <=> C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.936e+13, 'cm^3/(mol*s)'),
        n = -0.055,
        Ea = (7.745, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/CdCs;H_rad from training reaction 25\nExact match found for rate rule [C_rad/H/CdCs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H/CdCs;H_rad from training reaction 25
Exact match found for rate rule [C_rad/H/CdCs;H_rad]
""",
)

entry(
    index = 3630,
    label = "C4H6(524) <=> C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.29e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3631,
    label = "C2H3(29) + C2H3(29) <=> C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;Cd_pri_rad]
""",
)

entry(
    index = 3638,
    label = "C4H7(517) + C2H5(31) <=> C6H12(514)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C_rad/H2/Cs]
""",
)

entry(
    index = 3644,
    label = "H_10_(3) + C4H6(511) <=> C4H7(517)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CdH_Cds-HH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CdH_Cds-HH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3650,
    label = "C4H7(517) <=> C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.523e+08, 's^-1'),
        n = 1.387,
        Ea = (30.221, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;C_rad_out_single;Cs_H_out_H/Cd] + [R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule\n[R2H_S;C_rad_out_2H;Cs_H_out_H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;C_rad_out_single;Cs_H_out_H/Cd] + [R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule
[R2H_S;C_rad_out_2H;Cs_H_out_H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3651,
    label = "H_10_(3) + C4H7(517) <=> C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+12, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H2/Cs;H_rad from training reaction 17\nExact match found for rate rule [C_rad/H2/Cs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H2/Cs;H_rad from training reaction 17
Exact match found for rate rule [C_rad/H2/Cs;H_rad]
""",
)

entry(
    index = 3670,
    label = "C4H7(517) + C2H3(29) <=> C6H10(84)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cd_rad] for rate rule [C_rad/H2/Cs;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cd_rad] for rate rule [C_rad/H2/Cs;Cd_pri_rad]
""",
)

entry(
    index = 3671,
    label = "C2H3(29) + C2H4(30) <=> C4H7(517)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28600, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (1.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-HH;CdsJ-H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-HH;CdsJ-H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3673,
    label = "C2H2(40) + C2H4(30) <=> C4H6(524)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.304e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (43.72, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [db;doublebond] for rate rule [db_2H_2H;mb_db_2H]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using template [db;doublebond] for rate rule [db_2H_2H;mb_db_2H]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 3674,
    label = "C4H7(517) <=> C4H7(527)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.84e+10, 's^-1'),
        n = 0.21,
        Ea = (8.78, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R4_S_D;doublebond_intra_2H_pri;radadd_intra_cs2H]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R4_S_D;doublebond_intra_2H_pri;radadd_intra_cs2H]
""",
)

entry(
    index = 3697,
    label = "H_10_(3) + C4H7(522) <=> C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C_rad/H2/Cd]
""",
)

entry(
    index = 3704,
    label = "C3H3(19) + C4H6(511) <=> C7H9(531)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75550, 'cm^3/(mol*s)'),
        n = 2.459,
        Ea = (1.176, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-CdH;CJ] for rate rule [Cds-HH_Cds-CdH;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-CdH;CJ] for rate rule [Cds-HH_Cds-CdH;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3726,
    label = "C3H5(41) + C3H3(19) <=> C6H8(529)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.891e+15, 'cm^3/(mol*s)'),
        n = -0.784,
        Ea = (0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_pri_rad;C_rad/H2/Ct] + [C_rad/H2/Cd;C_pri_rad] for rate rule [C_rad/H2/Cd;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_pri_rad;C_rad/H2/Ct] + [C_rad/H2/Cd;C_pri_rad] for rate rule [C_rad/H2/Cd;C_rad/H2/Ct]
""",
)

entry(
    index = 3727,
    label = "C4H7(517) + C2H(21) <=> C6H8(529)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.719e+12, 'cm^3/(mol*s)'),
        n = 0.314,
        Ea = (-0.44, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H2/Cs] for rate rule [Ct_rad/Ct;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H2/Cs] for rate rule [Ct_rad/Ct;C_rad/H2/Cs]
""",
)

entry(
    index = 3728,
    label = "H_10_(3) + C4H6(91) <=> C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.84e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.82, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ca_Cds-HH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ca_Cds-HH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3760,
    label = "C4H6(98) <=> C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.161e+09, 's^-1'),
        n = -0.561,
        Ea = (4.994, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(C=C);CH] for rate rule [CsJ2-C;CsJ2(C=C);CH3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(C=C);CH] for rate rule [CsJ2-C;CsJ2(C=C);CH3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3761,
    label = "CH3(17) + C4H6(511) <=> C5H9(520)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47200, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.52, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-CdH;CsJ-HHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-CdH;CsJ-HHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3762,
    label = "C3H3(19) + C4H6(511) <=> C7H9(530)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17250, 'cm^3/(mol*s)'),
        n = 2.49,
        Ea = (5.245, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-CdH_Cds-HH;CJ] for rate rule [Cds-CdH_Cds-HH;CdsJ=Cdd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-CdH_Cds-HH;CJ] for rate rule [Cds-CdH_Cds-HH;CdsJ=Cdd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3763,
    label = "OH_12_(12) + C3H3(19) <=> C3H4O(528)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.144e+13, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (-1.683, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O_pri_rad;Y_rad] for rate rule [O_pri_rad;Cd_allenic]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O_pri_rad;Y_rad] for rate rule [O_pri_rad;Cd_allenic]
""",
)

entry(
    index = 3764,
    label = "CO_21_(14) + C2H4(30) <=> C3H4O(526)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (236800, 'cm^3/(mol*s)'),
        n = 2.368,
        Ea = (72.97, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_birad;R_H] for rate rule [CO_birad;ethene]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [CO_birad;R_H] for rate rule [CO_birad;ethene]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3765,
    label = "C3H4O(528) <=> C3H4O(526)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37990, 's^-1'),
        n = 2.515,
        Ea = (48.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_COH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_COH]
""",
)

entry(
    index = 3766,
    label = "C3H4O(533) <=> C3H4O(526)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.674e+10, 's^-1'),
        n = -0.06,
        Ea = (10.442, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3788,
    label = "O2_2_(13) + C6H7(52) <=> S(534)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.741e+15, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3789,
    label = "O2_2_(13) + C6H7(52) <=> S(535)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.741e+15, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3794,
    label = "C6H5(64) + C4H6(511) <=> S(515)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(813000, 'cm^3/(mol*s)'), n=2.56, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2005_Ismail_C6H5_C4H6
""",
)

entry(
    index = 3796,
    label = "H_10_(3) + C4H5(509) <=> C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;H_rad]
""",
)

entry(
    index = 3818,
    label = "C2H2(20) + C2H3(29) <=> C4H5(509)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (251000, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-H;CdsJ-H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-H;CdsJ-H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3837,
    label = "H_10_(3) + C4H5(525) <=> C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.936e+13, 'cm^3/(mol*s)'),
        n = -0.055,
        Ea = (7.745, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H/CdCs;H_rad from training reaction 25\nExact match found for rate rule [C_rad/H/CdCs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H/CdCs;H_rad from training reaction 25
Exact match found for rate rule [C_rad/H/CdCs;H_rad]
""",
)

entry(
    index = 3861,
    label = "C4H5(509) <=> C4H5(525)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.767e+11, 's^-1'),
        n = 0.248,
        Ea = (19.557, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4_D_D;doublebond_intra_pri;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R4_D_D;doublebond_intra_pri;radadd_intra_cdsingleH] for rate rule [R4_D_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3862,
    label = "C4H5(509) <=> C4H5(536)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.54e+10, 's^-1'),
        n = 0.69,
        Ea = (23.975, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4_D_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH from training reaction 12\nExact match found for rate rule [R4_D_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
R4_D_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH from training reaction 12
Exact match found for rate rule [R4_D_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH]
""",
)

entry(
    index = 3865,
    label = "H_10_(3) + C4H5(465) <=> C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]
""",
)

entry(
    index = 3893,
    label = "H_10_(3) + C4H5(465) <=> C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;H_rad]
""",
)

entry(
    index = 3919,
    label = "C4H5(509) <=> C4H5(465)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3986,
    label = "H_10_(3) + C4H4(444) <=> C4H5(509)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.992e+09, 'cm^3/(mol*s)'),
        n = 1.129,
        Ea = (9.249, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct-Cd_Ct-H;HJ from training reaction 102\nExact match found for rate rule [Ct-Cd_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Ct-Cd_Ct-H;HJ from training reaction 102
Exact match found for rate rule [Ct-Cd_Ct-H;HJ]
""",
)

entry(
    index = 4120,
    label = "O2_2_(13) + C4H3(110) <=> S(537)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4157,
    label = "O2_2_(13) + C4H3(110) <=> S(538)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.201e+12, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (-1.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4203,
    label = "C7H5(184) <=> C7H5(172)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.823e+09, 's^-1'),
        n = 1.003,
        Ea = (33.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_SS;Cd_rad_out_double;XH_out] for rate rule [R3H_SS_Cs;Cd_rad_out_Cd;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3H_SS;Cd_rad_out_double;XH_out] for rate rule [R3H_SS_Cs;Cd_rad_out_Cd;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4204,
    label = "O2_2_(13) + C5H3(162) <=> S(539)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+13, 'cm^3/(mol*s)'),
        n = -0.11,
        Ea = (0.209, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H/TwoDe] + [O2_birad;C_sec_rad] for rate rule [O2_birad;C_rad/H/TwoDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H/TwoDe] + [O2_birad;C_sec_rad] for rate rule [O2_birad;C_rad/H/TwoDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4223,
    label = "C10H7(541) <=> C10H7(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.096e+09, 's^-1'),
        n = 0.924,
        Ea = (30.972, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4H;Cd_rad_out_singleDe_Cb;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4H;Cd_rad_out_singleDe_Cb;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4227,
    label = "H_10_(3) + C10H6(212) <=> C10H7(541)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.24e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-H_Ct-Ct;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-H_Ct-Ct;HJ]
""",
)

entry(
    index = 4252,
    label = "O_11_(7) + C4H3O(87) <=> S(538)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [O_rad/OneDe;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [O_rad/OneDe;Oa]
""",
)

entry(
    index = 4253,
    label = "O2_2_(13) + C4H3O(87) <=> S(548)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.201e+12, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (-1.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4254,
    label = "C5H9(520) + CH2(S)(28) <=> C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.861e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 4255,
    label = "C3H5(41) + CH2(S)(28) <=> C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd_pri from training reaction 5\nExact match found for rate rule [carbene;Cd_pri]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd_pri from training reaction 5
Exact match found for rate rule [carbene;Cd_pri]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4256,
    label = "C3H5(41) + CH2(S)(28) <=> C4H7(527)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+15, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (-0.097, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;mb_db]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;mb_db]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4257,
    label = "C4H7(522) + CH2(S)(28) <=> C5H9(520)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.122e+14, 'cm^3/(mol*s)'),
        n = -0.146,
        Ea = (0.003, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;C_pri/Cd from training reaction 7\nExact match found for rate rule [carbene;C_pri/Cd]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
carbene;C_pri/Cd from training reaction 7
Exact match found for rate rule [carbene;C_pri/Cd]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 4261,
    label = "H_10_(3) + C10H6(212) <=> C10H7(543)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.37e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Ct_Ct-H;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Ct_Ct-H;HJ]
""",
)

entry(
    index = 4286,
    label = "C10H7(543) <=> C10H7(541)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e-10, 's^-1'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_D;Cd_rad_out_singleH;Cd_H_out_singleDe]
""",
)

entry(
    index = 4287,
    label = "O2_2_(13) + C4H3O(87) <=> S(547)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.212e+13, 'cm^3/(mol*s)'),
        n = -0.229,
        Ea = (-0.036, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H2/Ct] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H2/Ct] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4288,
    label = "C10H7(546) <=> C10H7(541)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.658e+09, 's^-1'),
                n = 0.699,
                Ea = (7.063, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'R5H_BSMS;Cb_rad_out;Cd_H_out_doubleC from training reaction 50\nExact match found for rate rule [R5H_BSMS;Cb_rad_out;Cd_H_out_doubleC]',
            ),
            Arrhenius(
                A = (2.946e+09, 's^-1'),
                n = 0.774,
                Ea = (45.713, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CddC_2] + [1_3_unsaturated_pentane_backbone;CH=C_1;unsaturated_end] for\nrate rule [1_3_unsaturated_pentane_backbone;CH=C_1;CddC_2]',
            ),
        ],
    ),
    longDesc = 
u"""
R5H_BSMS;Cb_rad_out;Cd_H_out_doubleC from training reaction 50
Exact match found for rate rule [R5H_BSMS;Cb_rad_out;Cd_H_out_doubleC]
Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CddC_2] + [1_3_unsaturated_pentane_backbone;CH=C_1;unsaturated_end] for
rate rule [1_3_unsaturated_pentane_backbone;CH=C_1;CddC_2]
""",
)

entry(
    index = 4290,
    label = "C10H7(546) <=> C10H7(543)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H_RSMSR;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R6H_RSMSR;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4298,
    label = "C10H7(546) <=> C10H7(554)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.983e+12, 's^-1'),
        n = -0.321,
        Ea = (5.655, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_MSR;doublebond_intra_pri_2H;radadd_intra_Cb]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_MSR;doublebond_intra_pri_2H;radadd_intra_Cb]
""",
)

entry(
    index = 4311,
    label = "C10H7(543) <=> C10H7(551)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.352e+11, 's^-1'),
        n = 0.295,
        Ea = (16.285, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Rn;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] + [R8;doublebond_intra_HCd_pri;radadd_intra] for rate rule\n[R8;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Rn;doublebond_intra_HCd_pri;radadd_intra_cdsingleH] + [R8;doublebond_intra_HCd_pri;radadd_intra] for rate rule
[R8;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4312,
    label = "H_10_(3) + C4H5(532) <=> C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+12, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C_rad/H2/Cs;H_rad from training reaction 17\nExact match found for rate rule [C_rad/H2/Cs;H_rad]',
    ),
    longDesc = 
u"""
C_rad/H2/Cs;H_rad from training reaction 17
Exact match found for rate rule [C_rad/H2/Cs;H_rad]
""",
)

entry(
    index = 4313,
    label = "C2H3(29) + C4H5(532) <=> C6H8(529)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cd_rad] for rate rule [C_rad/H2/Cs;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cd_rad] for rate rule [C_rad/H2/Cs;Cd_pri_rad]
""",
)

entry(
    index = 4331,
    label = "C2H(21) + C4H5(532) <=> C6H6(47)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.719e+12, 'cm^3/(mol*s)'),
        n = 0.314,
        Ea = (-0.44, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Y_rad] for rate rule [C_rad/H2/Cs;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Y_rad] for rate rule [C_rad/H2/Cs;Ct_rad/Ct]
""",
)

entry(
    index = 4337,
    label = "C4H5(532) <=> C4H5(443)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.82e+08, 's^-1'),
        n = 1.28,
        Ea = (27.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_H/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule [R2H_S;C_rad_out_2H;Cs_H_out_H/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4344,
    label = "H_10_(3) + C4H4(444) <=> C4H5(532)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.49e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (2.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CtH_Cds-HH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CtH_Cds-HH;HJ]
""",
)

entry(
    index = 4384,
    label = "C2H(21) + C2H4(30) <=> C4H5(532)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1715, 'cm^3/(mol*s)'),
        n = 2.589,
        Ea = (5.194, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-HH;CJ] for rate rule [Cds-HH_Cds-HH;CtJ_Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-HH;CJ] for rate rule [Cds-HH_Cds-HH;CtJ_Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4385,
    label = "C4H5(532) <=> C4H5(555)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.881e+08, 's^-1'),
        n = 1.062,
        Ea = (18.39, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R4_S_T;triplebond_intra_H;radadd_intra_cs2H from training reaction 17\nExact match found for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_cs2H]\nEa raised from 75.4 to 76.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
R4_S_T;triplebond_intra_H;radadd_intra_cs2H from training reaction 17
Exact match found for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_cs2H]
Ea raised from 75.4 to 76.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 4386,
    label = "C10H7(550) <=> C10H7(543)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (239900, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R8H;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R8H;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4387,
    label = "C10H7(546) <=> C10H7(550)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.989e+08, 's^-1'),
        n = 1.306,
        Ea = (43.343, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H;Y_rad_out;Cb_H_out] + [R3H;Cb_rad_out;XH_out] for rate rule [R3H;Cb_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4388,
    label = "C3H3(19) + CH2(S)(28) <=> C4H5(555)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+15, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (-0.097, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;mb_db]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;mb_db]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4389,
    label = "HCO(22) + C2H3(29) <=> C3H4O(526)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;CO_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;CO_pri_rad]
""",
)

entry(
    index = 4390,
    label = "C10H7(550) <=> C10H7(556)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.84e+11, 's^-1'),
        n = 0.258,
        Ea = (3.797, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6;triplebond_intra;radadd_intra] for rate rule [R6;triplebond_intra_De;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6;triplebond_intra;radadd_intra] for rate rule [R6;triplebond_intra_De;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4391,
    label = "H_10_(3) + C10H6(297) <=> C10H7(556)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.036e+13, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (0.09, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Ca_Ca;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Ca_Ca;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4392,
    label = "C10H7(546) <=> C10H7(553)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.933e+10, 's^-1'),
        n = 0.399,
        Ea = (9.774, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra;radadd_intra_Cb] for rate rule [R4;triplebond_intra_De;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra;radadd_intra_Cb] for rate rule [R4;triplebond_intra_De;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4410,
    label = "H_10_(3) + C10H6(212) <=> C10H7(544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (814100, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4437,
    label = "C10H7(549) <=> C10H7(543)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 's^-1'),
        n = 1.941,
        Ea = (8.652, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R7H;Cb_rad_out;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cb_rad_out;Cd_H_out_singleH] for rate rule [R7H;Cb_rad_out;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4438,
    label = "C10H7(546) <=> C10H7(549)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.137e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4439,
    label = "C10H7(550) <=> C10H7(549)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.137e+09, 's^-1'),
        n = 1.605,
        Ea = (56.952, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_B;Y_rad_out;Cb_H_out from training reaction 89\nExact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_B;Y_rad_out;Cb_H_out from training reaction 89
Exact match found for rate rule [R2H_B;Y_rad_out;Cb_H_out]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4440,
    label = "C10H7(542) <=> C10H7(125)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.292e+08, 's^-1'),
        n = 1.29,
        Ea = (47.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_single] for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_single] for rate rule [R2H_D;Cd_rad_out_singleDe_Cb;Cd_H_out_singleDe]
""",
)

entry(
    index = 4444,
    label = "H_10_(3) + C10H6(212) <=> C10H7(542)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (3.846, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Ct-De_Ct-Cb;HJ]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Ct-De_Ct-Cb;HJ]
""",
)

entry(
    index = 4471,
    label = "C10H7(544) <=> C10H7(542)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.807e+09, 's^-1'),
        n = 1.021,
        Ea = (38.586, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule [1_3_unsaturated_pentane_backbone;CH2(C)_1;CtC_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule [1_3_unsaturated_pentane_backbone;CH2(C)_1;CtC_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4475,
    label = "C2H(21) + C8H6(74) <=> C10H7(542)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.889e+09, 'cm^3/(mol*s)'),
        n = 1.29,
        Ea = (3.784, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-H_Ct-Cb;CJ] for rate rule [Ct-H_Ct-Cb;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-H_Ct-Cb;CJ] for rate rule [Ct-H_Ct-Cb;CtJ_Ct]
""",
)

entry(
    index = 4512,
    label = "C3H3(19) + C7H4(484) <=> C10H7(540)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.553, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 4531,
    label = "H_10_(3) + C10H6(212) <=> C10H7(545)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (407000, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4558,
    label = "C10H7(545) <=> C10H7(541)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.692e+10, 's^-1'),
        n = 0.74,
        Ea = (34.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_1H] for rate rule [R8H;Cd_rad_out_singleH;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [RnH;Cd_rad_out_singleH;Cs_H_out_1H] for rate rule [R8H;Cd_rad_out_singleH;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4559,
    label = "C10H7(545) <=> C10H7(544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36880, 's^-1'),
        n = 2.81,
        Ea = (30.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R2H_S;C_rad_out_H/(Cd-Cd-Cd);Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R2H_S;C_rad_out_H/(Cd-Cd-Cd);Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4560,
    label = "C10H7(545) <=> C10H7(542)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (147000, 's^-1'),
        n = 2.169,
        Ea = (19.742, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6H;Y_rad_out;Cs_H_out_H/OneDe] for rate rule [R6H;Cd_rad_out_singleDe_Ct;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R6H;Y_rad_out;Cs_H_out_H/OneDe] for rate rule [R6H;Cd_rad_out_singleDe_Ct;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4570,
    label = "C10H7(550) <=> C10H7(557)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.936e+10, 's^-1'),
        n = 0.366,
        Ea = (14.829, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R6;triplebond_intra;radadd_intra] + [R6_SMS;multiplebond_intra;radadd_intra] for rate rule\n[R6_SMS_T;triplebond_intra_De;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [R6;triplebond_intra;radadd_intra] + [R6_SMS;multiplebond_intra;radadd_intra] for rate rule
[R6_SMS_T;triplebond_intra_De;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4571,
    label = "C10H7(546) <=> C10H7(552)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.97e+09, 's^-1'),
        n = 0.768,
        Ea = (20.183, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4;triplebond_intra;radadd_intra] for rate rule [R4;triplebond_intra_De;radadd_intra_Cb]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R4;triplebond_intra;radadd_intra] for rate rule [R4;triplebond_intra_De;radadd_intra_Cb]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4682,
    label = "C10H7(193) <=> C10H7(556)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (191.5, 's^-1'),
        n = 3.05,
        Ea = (53.137, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R3H_DS;Cd_rad_out_singleH;Cd_H_out_doubleC]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R3H_DS;Cd_rad_out_singleH;Cd_H_out_doubleC]
""",
)

entry(
    index = 4712,
    label = "O2_2_(13) + C4H7(522) <=> S(559)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.076e+13, 'cm^3/(mol*s)'),
        n = -0.033,
        Ea = (-0.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H2/Cd] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H2/Cd] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4714,
    label = "S(559) <=> HO2_17_(5) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+09, 's^-1'),
        n = 1.11,
        Ea = (42.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2OO_0H_2H]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2OO_0H_2H]
""",
)

entry(
    index = 4722,
    label = "CH2CO(16) + C5H3(141) <=> C7H5O(561)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.832e+09, 'cm^3/(mol*s)'),
        n = 1.415,
        Ea = (4.792, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CdsJ=Cdd]
""",
)

entry(
    index = 4723,
    label = "CH2CO(16) + C5H3(141) <=> C7H5O(562)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.832e+09, 'cm^3/(mol*s)'),
        n = 1.415,
        Ea = (4.792, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Ck;CJ] for rate rule [Cds-HH_Ck;CdsJ=Cdd]
""",
)

entry(
    index = 4724,
    label = "C7H5(483) <=> C7H5(563)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.485e+11, 's^-1'),
        n = 0.065,
        Ea = (27.941, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_csHDe] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csHCt]',
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_csHDe] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csHCt]
""",
)

entry(
    index = 4725,
    label = "C7H5(156) <=> C7H5(560)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6.228e+10, 's^-1'),
                n = 0.36,
                Ea = (37.203, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn1c6_gamma;multiplebond_intra;radadd_intra_cs2H] for rate rule [Rn1c6_gamma;triplebond_intra_De;radadd_intra_cs2H]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (1.036e+11, 's^-1'),
                n = 0.542,
                Ea = (29.862, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using an average for rate rule [R5_SD_D;doublebond_intra_secDe_2H;radadd_intra]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rn1c6_gamma;multiplebond_intra;radadd_intra_cs2H] for rate rule [Rn1c6_gamma;triplebond_intra_De;radadd_intra_cs2H]
Multiplied by reaction path degeneracy 2
Estimated using an average for rate rule [R5_SD_D;doublebond_intra_secDe_2H;radadd_intra]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4727,
    label = "C7H5(457) <=> C7H5(560)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.51e+10, 's^-1'),
        n = 0.34,
        Ea = (31.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_cddouble]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_cddouble]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4744,
    label = "H_10_(3) + C10H6(212) <=> C10H7(564)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (814100, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4768,
    label = "C10H7(564) <=> C10H7(541)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000, 's^-1'),
        n = 1.95,
        Ea = (24, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R6H;Y_rad_out;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R6H;Y_rad_out;Cs_H_out_H/(Cd-Cd-Cd)] for rate rule [R6H;Cd_rad_out_singleH;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4769,
    label = "C10H7(564) <=> C10H7(543)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.807e+09, 's^-1'),
        n = 1.021,
        Ea = (38.586, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule\n[1_3_unsaturated_pentane_backbone;CH2(C)_1;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule
[1_3_unsaturated_pentane_backbone;CH2(C)_1;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4770,
    label = "C10H7(564) <=> C10H7(544)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.12e+06, 's^-1'),
        n = 1.75,
        Ea = (25.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H;C_rad_out_H/Cd;Cs_H_out_H/OneDe] for rate rule [R4H_SDS;C_rad_out_H/Cd;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R4H;C_rad_out_H/Cd;Cs_H_out_H/OneDe] for rate rule [R4H_SDS;C_rad_out_H/Cd;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4771,
    label = "CO2_5_(8) + CH3(17) <=> S(558)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22280, 'cm^3/(mol*s)'),
        n = 2.62,
        Ea = (22.801, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R_R;CsJ-HHH] for rate rule [Od_Cdd-Od;CsJ-HHH]\nMultiplied by reaction path degeneracy 2\nEa raised from 89.0 to 95.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [R_R;CsJ-HHH] for rate rule [Od_Cdd-Od;CsJ-HHH]
Multiplied by reaction path degeneracy 2
Ea raised from 89.0 to 95.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 4772,
    label = "C10H7(564) <=> C10H7(542)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (389.7, 's^-1'),
        n = 2.871,
        Ea = (22.439, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R4H;Y_rad_out;Cs_H_out_H/(Cd-Cd-Cd)] + [R4H;Cd_rad_out_singleDe_Ct;XH_out] for rate rule\n[R4H_MMS;Cd_rad_out_singleDe_Ct;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [R4H;Y_rad_out;Cs_H_out_H/(Cd-Cd-Cd)] + [R4H;Cd_rad_out_singleDe_Ct;XH_out] for rate rule
[R4H_MMS;Cd_rad_out_singleDe_Ct;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4773,
    label = "C10H7(545) <=> C10H7(564)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.366e+08, 's^-1'),
        n = 1.484,
        Ea = (25.648, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CdCJ_2] + [1_3_unsaturated_pentane_backbone;CH(CJ)_1;unsaturated_end]\nfor rate rule [1_3_pentadiene;CH(CJ)_1;CdCJ_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [1_3_unsaturated_pentane_backbone;CH_end;CdCJ_2] + [1_3_unsaturated_pentane_backbone;CH(CJ)_1;unsaturated_end]
for rate rule [1_3_pentadiene;CH(CJ)_1;CdCJ_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4779,
    label = "H_10_(3) + C6H13(568) <=> C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;H_rad]
""",
)

entry(
    index = 4785,
    label = "C6H13(568) <=> C6H13(77)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.352e+10, 's^-1'),
        n = 0.88,
        Ea = (38, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4789,
    label = "CH3(17) + C5H10(570) <=> C6H13(568)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (5.32, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-CsH;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-CsH;CsJ-HHH]
""",
)

entry(
    index = 4792,
    label = "C3H5(41) + C2H5(31) <=> C5H10(570)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C_rad/H2/Cs]
""",
)

entry(
    index = 4798,
    label = "H_10_(3) + C5H10(570) <=> C5H11(36)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.17e+08, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-HH;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-HH;HJ]
""",
)

entry(
    index = 4806,
    label = "C2H5(31) + C4H8(78) <=> C6H13(568)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2130, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (4.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-CsH;CsJ-CsHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-CsH;CsJ-CsHH]
""",
)

entry(
    index = 4807,
    label = "C5H10(571) <=> C5H10(570)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.718e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4808,
    label = "H_10_(3) + C6H11(569) <=> C6H12(565)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;H_rad]
""",
)

entry(
    index = 4823,
    label = "H_10_(3) + C6H10(573) <=> C6H11(569)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.37, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-CsH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-CsH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4832,
    label = "C6H11(574) <=> C6H11(569)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+06, 's^-1'),
        n = 1.08,
        Ea = (6.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 35 C_CCCCCJ <=> cyclohexyl in Intra_R_Add_Endocyclic/training',
    ),
    longDesc = 
u"""
Matched reaction 35 C_CCCCCJ <=> cyclohexyl in Intra_R_Add_Endocyclic/training
""",
)

entry(
    index = 4835,
    label = "C5H10(571) <=> C5H10(572)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.105e+11, 's^-1'),
        n = 0.177,
        Ea = (7.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [singletcarbene_CH;CsJ2C;CH2(C)] + [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH2(C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [singletcarbene_CH;CsJ2C;CH2(C)] + [CsJ2-C;CsJ2C;CH] for rate rule [CsJ2-C;CsJ2C;CH2(C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4836,
    label = "C6H11(574) <=> C6H11(576)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+10, 's^-1'),
        n = 0,
        Ea = (6.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H]
""",
)

entry(
    index = 4837,
    label = "C6H11(574) <=> C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000226, 's^-1'),
        n = 4.37,
        Ea = (8.06, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R4H_SSS;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule [R4H_SSS;C_rad_out_2H;Cs_H_out_H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R4H_SSS;C_rad_out_2H;Cs_H_out_H/OneDe] for rate rule [R4H_SSS;C_rad_out_2H;Cs_H_out_H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4838,
    label = "C2H4(30) + C4H6(511) <=> C6H10(573)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.425e+09, 'cm^3/(mol*s)'),
        n = 0.245,
        Ea = (26.875, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [diene_out;diene_in_2H;ene_unsub_unsub] + [diene_unsub_unsub_out;diene_in;ene_unsub_unsub] +\n[diene_unsub_unsub_out;diene_in_2H;ene] for rate rule [diene_unsub_unsub_out;diene_in_2H;ene_unsub_unsub]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [diene_out;diene_in_2H;ene_unsub_unsub] + [diene_unsub_unsub_out;diene_in;ene_unsub_unsub] +
[diene_unsub_unsub_out;diene_in_2H;ene] for rate rule [diene_unsub_unsub_out;diene_in_2H;ene_unsub_unsub]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4839,
    label = "C5H10(577) <=> C5H10(572)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.29e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4840,
    label = "C6H10(575) <=> C6H10(573)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.29e+11, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4841,
    label = "H_10_(3) + C6H10(84) <=> C6H11(574)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.34e+08, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-HH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-HH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4852,
    label = "C2H5(31) + C3H5(65) <=> C5H10(572)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]
""",
)

entry(
    index = 4857,
    label = "CH3(17) + C4H7(522) <=> C5H10(572)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C_methyl]
""",
)

entry(
    index = 4866,
    label = "CH3(17) + C4H7(517) <=> C5H10(570)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cs;C_methyl]
""",
)

entry(
    index = 4869,
    label = "C2H4(30) + C4H7(517) <=> C6H11(574)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3980, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (5.37, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-CsHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-HH_Cds-HH;CsJ-CsHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4879,
    label = "C3H7(35) + C2H3(29) <=> C5H10(570)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.41e+15, 'cm^3/(mol*s)'),
        n = -0.985,
        Ea = (0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;C_pri_rad] for rate rule [Cd_pri_rad;C_rad/H2/Cs]
""",
)

entry(
    index = 4909,
    label = "C4H7(522) <=> C4H7(85)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+11, 's^-1'),
        n = 0.63,
        Ea = (62.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2H_S;C_rad_out_2H;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2H_S;C_rad_out_2H;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4914,
    label = "CH2(S)(28) + C4H8(78) <=> C5H10(570)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.861e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 4915,
    label = "C4H8(82) + CH2(S)(28) <=> C5H10(571)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.861e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 4916,
    label = "CH2(S)(28) + C4H8(83) <=> C5H10(572)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.244e+14, 'cm^3/(mol*s)'),
        n = -0.146,
        Ea = (0.003, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;C_pri/Cd from training reaction 7\nExact match found for rate rule [carbene;C_pri/Cd]\nMultiplied by reaction path degeneracy 36',
    ),
    longDesc = 
u"""
carbene;C_pri/Cd from training reaction 7
Exact match found for rate rule [carbene;C_pri/Cd]
Multiplied by reaction path degeneracy 36
""",
)

entry(
    index = 4917,
    label = "CH2(S)(28) + C4H8(78) <=> C5H10(572)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13, 'cm^3/(mol*s)'),
        n = -0.324,
        Ea = (-0.935, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd_pri from training reaction 5\nExact match found for rate rule [carbene;Cd_pri]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd_pri from training reaction 5
Exact match found for rate rule [carbene;Cd_pri]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4918,
    label = "C4H8(82) + CH2(S)(28) <=> C5H10(577)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.861e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]\nMultiplied by reaction path degeneracy 18',
    ),
    longDesc = 
u"""
Estimated using template [carbene;C_pri] for rate rule [carbene;C_pri/NonDeC]
Multiplied by reaction path degeneracy 18
""",
)

entry(
    index = 4926,
    label = "O2_2_(13) + C3H3(19) <=> S(566)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.7, 1.679, -0.09745, -0.01471],
            [-1.181, 0.3695, 0.09895, 0.007719],
            [-0.0523, -0.04245, -0.002939, 0.004323],
            [0.03178, -0.01561, -0.003794, -0.0007439],
            [-0.02172, 0.002027, -0.0001881, 0.0005173],
            [-0.02259, -0.001749, -8.341e-05, 0.0001437],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 4927,
    label = "O2_2_(13) + C3H3(19) <=> S(567)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.57, 1.743, -0.08453, -0.01344],
            [-1.034, 0.2947, 0.08861, 0.008759],
            [-0.05095, -0.0292, -0.00416, 0.003121],
            [0.01087, -0.01337, -0.002236, -0.0004579],
            [-0.03285, 0.001146, -0.0006979, 0.0004585],
            [-0.02593, -0.001968, -0.0002395, 1.609e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 4928,
    label = "CH2CO(16) + C6H5(64) <=> C8H7O(582)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.832e+09, 'cm^3/(mol*s)'),
        n = 1.415,
        Ea = (4.792, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 185 C2H2O-3 + C6H5 <=> C8H7O-7 in R_Addition_MultipleBond/training',
    ),
    longDesc = 
u"""
Matched reaction 185 C2H2O-3 + C6H5 <=> C8H7O-7 in R_Addition_MultipleBond/training
""",
)

entry(
    index = 4929,
    label = "CO_21_(14) + C7H7(580) <=> C8H7O(582)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (73810, 'cm^3/(mol*s)'),
        n = 2.309,
        Ea = (10.738, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 CO + C7H7 <=> C8H7O in R_Addition_COm/training',
    ),
    longDesc = 
u"""
Matched reaction 1 CO + C7H7 <=> C8H7O in R_Addition_COm/training
""",
)

entry(
    index = 4930,
    label = "C7H7(580) <=> C7H7(583)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (33.317, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (8.251e+10, 's^-1'),
                n = 0.634,
                Ea = (44.066, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R5;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule [R5_SD_D;doublebond_intra_HCd_pri;radadd_intra_csHCd]',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
Estimated using template [R5;doublebond_intra_HCd_pri;radadd_intra_csHCd] for rate rule [R5_SD_D;doublebond_intra_HCd_pri;radadd_intra_csHCd]
""",
)

entry(
    index = 4932,
    label = "C7H7(581) <=> C7H7(580)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.712e+10, 's^-1'), n=0.722, Ea=(41.878, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 4933,
    label = "O2_2_(13) + C7H7(580) <=> S(586)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.941e+14, 'cm^3/(mol*s)'),
        n = -0.214,
        Ea = (0.007, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [O2_birad;C_rad/H/CdCd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [O2_birad;C_rad/H/CdCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4934,
    label = "CH2(S)(28) + C6H5(64) <=> C7H7(581)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4935,
    label = "O2_2_(13) + C7H7(580) <=> S(587)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.941e+14, 'cm^3/(mol*s)'),
        n = -0.214,
        Ea = (2.623, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [O2_birad;C_rad/H/CdCd]\nMultiplied by reaction path degeneracy 2\nEa raised from 7.4 to 11.0 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [O2_birad;C_rad/H/CdCd]
Multiplied by reaction path degeneracy 2
Ea raised from 7.4 to 11.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 4936,
    label = "C7H7(581) <=> C7H7(588)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.168e+08, 's^-1'),
        n = 1.29,
        Ea = (47.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_D;Cd_rad_out_singleDe;Cd_H_out_single] for rate rule [R2H_D;Cd_rad_out_singleDe_Cd;Cd_H_out_singleDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [R2H_D;Cd_rad_out_singleDe;Cd_H_out_single] for rate rule [R2H_D;Cd_rad_out_singleDe_Cd;Cd_H_out_singleDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4937,
    label = "CH2(S)(28) + C6H5(64) <=> C7H7(588)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.468e+11, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4938,
    label = "C7H7(581) <=> C7H7(589)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (383, 's^-1'),
        n = 3.05,
        Ea = (53.137, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_DS;Cd_rad_out_single;Cd_H_out_doubleC] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cd;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3H_DS;Cd_rad_out_single;Cd_H_out_doubleC] for rate rule [R3H_DS;Cd_rad_out_singleDe_Cd;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4939,
    label = "C7H7(588) <=> C7H7(589)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.612e+09, 's^-1'),
        n = 1.172,
        Ea = (51.258, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R2H_S;Cd_rad_out_Cd;Cd_H_out_doubleC] for rate rule [R2H_S;Cd_rad_out_Cd;Cd_H_out_double(Cd-Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R2H_S;Cd_rad_out_Cd;Cd_H_out_doubleC] for rate rule [R2H_S;Cd_rad_out_Cd;Cd_H_out_double(Cd-Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4940,
    label = "O2_2_(13) + C7H7(580) <=> S(585)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.076e+13, 'cm^3/(mol*s)'),
        n = -0.033,
        Ea = (-0.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H2/Cd] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H2/Cd] + [O2_birad;C_pri_rad] for rate rule [O2_birad;C_rad/H2/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4941,
    label = "CH2(S)(28) + C6H5(64) <=> C7H7(589)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4942,
    label = "O2_2_(13) + C7H7(581) <=> S(590)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4943,
    label = "C7H7(579) <=> C7H7(580)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+11, 's^-1'), n=0.49, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 4944,
    label = "CH2(S)(28) + S(123) <=> S(590)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;R_H] for rate rule [carbene;Cb_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;R_H] for rate rule [carbene;Cb_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4945,
    label = "CH2(S)(28) + C6H5(64) <=> C7H7(579)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.072e+16, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (-0.097, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;mb_db]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;mb_db]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 4946,
    label = "O2_2_(13) + C7H7(588) <=> S(591)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cd_sec_rad] for rate rule [O2_birad;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4949,
    label = "CH3(17) + C6H5(64) <=> C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.901e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;Cd_rad] for rate rule [C_methyl;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [C_methyl;Cd_rad] for rate rule [C_methyl;Cd_rad/Cd]
""",
)

entry(
    index = 4991,
    label = "CH2(S)(28) + S(123) <=> S(591)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;R_H] for rate rule [carbene;Cb_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;R_H] for rate rule [carbene;Cb_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4992,
    label = "C6H6(48) + CH2(S)(28) <=> C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.48e+13, 'cm^3/(mol*s)'),
        n = -0.272,
        Ea = (-1.274, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 12 CH2 + benzene <=> toluene in 1,2_Insertion_carbene/training',
    ),
    longDesc = 
u"""
Matched reaction 12 CH2 + benzene <=> toluene in 1,2_Insertion_carbene/training
""",
)

entry(
    index = 4993,
    label = "H_10_(3) + C7H7(580) <=> C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;H_rad]
""",
)

entry(
    index = 4994,
    label = "H_10_(3) + C7H7(581) <=> C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]
""",
)

entry(
    index = 4995,
    label = "H_10_(3) + C7H7(589) <=> C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;Cd_sec_rad] for rate rule [H_rad;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;Cd_sec_rad] for rate rule [H_rad;Cd_rad/Cd]
""",
)

entry(
    index = 4996,
    label = "H_10_(3) + C7H7(588) <=> C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]
""",
)

entry(
    index = 5093,
    label = "C7H7(580) <=> C7H7(584)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.705e+10, 's^-1'),
        n = 0.586,
        Ea = (51.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R4_intra_6_member_ring_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCd]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R4_intra_6_member_ring_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCd]
""",
)

entry(
    index = 5110,
    label = "CH2(S)(28) + CHO2(42) <=> S(558)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.438e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5159,
    label = "CH3(17) + C6H4(121) <=> C7H7(581)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (5.82, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cd_Ct-Cd;CsJ-HHH] for rate rule [Ct-Cd_Ct-Cd_cyc6;CsJ-HHH]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cd_Ct-Cd;CsJ-HHH] for rate rule [Ct-Cd_Ct-Cd_cyc6;CsJ-HHH]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5165,
    label = "H_10_(3) + C7H8(61) <=> C7H9(592)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (814100, 'cm^3/(mol*s)'),
        n = 2.474,
        Ea = (4.029, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cb-H_Cb-H;HJ from training reaction 68\nExact match found for rate rule [Cb-H_Cb-H;HJ]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Cb-H_Cb-H;HJ from training reaction 68
Exact match found for rate rule [Cb-H_Cb-H;HJ]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5189,
    label = "cyC6H7(58) + CH2(S)(28) <=> C7H9(592)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5190,
    label = "C7H9(578) <=> H_10_(3) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+10, 's^-1'), n=1.26, Ea=(28.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 5191,
    label = "H_10_(3) + C5H11(593) <=> C5H12(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;H_rad]
""",
)

entry(
    index = 5199,
    label = "C3H6(38) + C2H5(31) <=> C5H11(593)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2331, 'cm^3/(mol*s)'),
        n = 2.486,
        Ea = (4.895, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cds-HH_Cds-CsH;CsJ-CsHH] + [Cds-HH_Cds-Cs\\H3/H;CsJ] for rate rule [Cds-HH_Cds-Cs\\H3/H;CsJ-CsHH]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cds-HH_Cds-CsH;CsJ-CsHH] + [Cds-HH_Cds-Cs\H3/H;CsJ] for rate rule [Cds-HH_Cds-Cs\H3/H;CsJ-CsHH]
""",
)

entry(
    index = 5215,
    label = "H_10_(3) + CH2O(25) <=> CH3O(508)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO-HH_O;HJ]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CO-HH_O;HJ]
""",
)

entry(
    index = 5231,
    label = "O_11_(7) + C6H5O(610) <=> S(123)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [O_rad/OneDe;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [O_rad/OneDe;Oa]
""",
)

entry(
    index = 5232,
    label = "O_11_(7) + C6H5(64) <=> C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [Cb_rad;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [Cb_rad;Oa]
""",
)

entry(
    index = 5233,
    label = "C6H5O(610) <=> C6H5O(612)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (29.257, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (1e+10, 's^-1'),
                n = 0,
                Ea = (46.85, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R5_SD_D;doublebond_intra;radadd_intra_cs] for rate rule [R5_SD_D;doublebond_intra_HDe_pri;radadd_intra_csHDe]',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
Estimated using template [R5_SD_D;doublebond_intra;radadd_intra_cs] for rate rule [R5_SD_D;doublebond_intra_HDe_pri;radadd_intra_csHDe]
""",
)

entry(
    index = 5235,
    label = "O2_2_(13) + C6H5O(610) <=> S(614)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.941e+14, 'cm^3/(mol*s)'),
        n = -0.214,
        Ea = (1.483, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [O2_birad;C_rad/H/CdCd]\nMultiplied by reaction path degeneracy 2\nEa raised from 3.0 to 6.2 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [O2_birad;C_rad/H/CdCd]
Multiplied by reaction path degeneracy 2
Ea raised from 3.0 to 6.2 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 5236,
    label = "C6H5O(610) <=> C6H5O(611)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.535e+12, 's^-1'),
                n = 0.436,
                Ea = (54.127, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn1c6b_alpha;doublebond_intra_HCd_pri;radadd_intra] for rate rule [Rn1c6b_alpha;doublebond_intra_HCd_pri;radadd_intra_O]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (2.338e+11, 's^-1'),
                n = 0.246,
                Ea = (36.212, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn;multiplebond_intra;radadd_intra_csH(CdCdCd)] for rate rule [R3_CO;carbonyl_intra_De;radadd_intra_csH(CdCdCd)]\nMultiplied by reaction path degeneracy 2\nEa raised from 150.5 to 151.5 kJ/mol to match endothermicity of reaction.',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rn1c6b_alpha;doublebond_intra_HCd_pri;radadd_intra] for rate rule [Rn1c6b_alpha;doublebond_intra_HCd_pri;radadd_intra_O]
Multiplied by reaction path degeneracy 2
Estimated using template [Rn;multiplebond_intra;radadd_intra_csH(CdCdCd)] for rate rule [R3_CO;carbonyl_intra_De;radadd_intra_csH(CdCdCd)]
Multiplied by reaction path degeneracy 2
Ea raised from 150.5 to 151.5 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 5238,
    label = "O2_2_(13) + C6H5O(610) <=> S(615)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+13, 'cm^3/(mol*s)'),
        n = -0.11,
        Ea = (0.209, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C_rad/H/TwoDe] + [O2_birad;C_sec_rad] for rate rule [O2_birad;C_rad/H/TwoDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C_rad/H/TwoDe] + [O2_birad;C_sec_rad] for rate rule [O2_birad;C_rad/H/TwoDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5239,
    label = "C6H5O(613) <=> C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.57e+10, 's^-1'),
        n = 0.43,
        Ea = (1.924, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 5240,
    label = "C3H3(19) + C6H5O(610) <=> C9H8O(616)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.471e+14, 'cm^3/(mol*s)'),
        n = -0.214,
        Ea = (0.007, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [Cd_allenic;C_rad/H/CdCd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H/CdCd] for rate rule [Cd_allenic;C_rad/H/CdCd]
""",
)

entry(
    index = 5241,
    label = "C6H5O(613) <=> C6H5O(617)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.371e+10, 's^-1'),
        n = 0.472,
        Ea = (4.23, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R6_DSM_D;doublebond_intra;radadd_intra_cdsingleH]
""",
)

entry(
    index = 5242,
    label = "CH2(S)(28) + CPDyl(596) <=> C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.936e+11, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 5243,
    label = "CH2(S)(28) + CPDyl(596) <=> C6H7(57)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.072e+16, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (-0.097, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;mb_db]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;mb_db]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 5244,
    label = "CO_21_(14) + CPDyl(596) <=> C6H5O(617)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.61e+07, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (8.949, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]\nEa raised from 32.4 to 37.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]
Ea raised from 32.4 to 37.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 5245,
    label = "CH2(S)(28) + S(609) <=> S(425)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.735e+11, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/TDMustO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/TDMustO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5246,
    label = "O2_2_(13) + CPDyl(596) <=> S(609)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.741e+15, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5247,
    label = "C5H5(50) <=> CPDyl(596)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+10, 's^-1'), n=0.98, Ea=(26.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 5248,
    label = "C3H3(19) + CPDyl(596) <=> C8H8(619)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.704e+14, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [Cd_allenic;C_rad_cyclopentadiene]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [Cd_allenic;C_rad_cyclopentadiene]
""",
)

entry(
    index = 5249,
    label = "C8H8(619) <=> C8H8(621)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.78e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5250,
    label = "C3H3(19) + C5H5(50) <=> C8H8(621)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.071e+11, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (-0.515, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_rad/NonDe] + [Cd_allenic;Cd_rad] for rate rule [Cd_allenic;Cd_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_rad/NonDe] + [Cd_allenic;Cd_rad] for rate rule [Cd_allenic;Cd_rad/NonDe]
""",
)

entry(
    index = 5251,
    label = "C8H8(622) <=> C8H8(621)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.78e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5252,
    label = "C8H8(621) <=> C8H8(623)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;CddC_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CddC_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;CddC_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CddC_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5253,
    label = "C3H3(19) + CPDyl(596) <=> C8H8(618)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C_rad_cyclopentadiene] for rate rule [C_rad/H2/Ct;C_rad_cyclopentadiene]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C_rad_cyclopentadiene] for rate rule [C_rad/H2/Ct;C_rad_cyclopentadiene]
""",
)

entry(
    index = 5254,
    label = "C8H8(619) <=> C8H8(618)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.856e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_5_unsaturated_hexane from training reaction 3\nExact match found for rate rule [1_5_unsaturated_hexane]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
1_5_unsaturated_hexane from training reaction 3
Exact match found for rate rule [1_5_unsaturated_hexane]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5255,
    label = "C2H(21) + C6H7(55) <=> C8H8(618)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.719e+12, 'cm^3/(mol*s)'),
        n = 0.314,
        Ea = (-0.44, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H2/Cs] for rate rule [Ct_rad/Ct;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H2/Cs] for rate rule [Ct_rad/Ct;C_rad/H2/Cs]
""",
)

entry(
    index = 5256,
    label = "C8H8(618) <=> C8H8(625)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.78e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5257,
    label = "C3H3(19) + C5H5(50) <=> C8H8(625)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.307e+12, 'cm^3/(mol*s)'),
        n = 0.192,
        Ea = (-0.671, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Ct;Cd_rad] for rate rule [C_rad/H2/Ct;Cd_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Ct;Cd_rad] for rate rule [C_rad/H2/Ct;Cd_rad/NonDe]
""",
)

entry(
    index = 5258,
    label = "C2H(21) + C6H7(53) <=> C8H8(625)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.765e+13, 'cm^3/(mol*s)'),
        n = -0.066,
        Ea = (-0.019, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H2/Cd] for rate rule [Ct_rad/Ct;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H2/Cd] for rate rule [Ct_rad/Ct;C_rad/H2/Cd]
""",
)

entry(
    index = 5259,
    label = "C8H8(626) <=> C8H8(625)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.78e+07, 's^-1'),
        n = 1.58,
        Ea = (21.7, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'cyclopentadiene;CH_end;unsaturated_end from training reaction 1\nExact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
cyclopentadiene;CH_end;unsaturated_end from training reaction 1
Exact match found for rate rule [cyclopentadiene;CH_end;unsaturated_end]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5260,
    label = "C2H(21) + C6H7(56) <=> C8H8(626)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.765e+13, 'cm^3/(mol*s)'),
        n = -0.066,
        Ea = (-0.019, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H2/Cd] for rate rule [Ct_rad/Ct;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H2/Cd] for rate rule [Ct_rad/Ct;C_rad/H2/Cd]
""",
)

entry(
    index = 5261,
    label = "S(609) <=> S(620)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.015e+12, 's^-1'),
        n = 0.22,
        Ea = (11.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rn2(SS)c5_alpha;doublebond_intra_HCd_pri;radadd_intra] for rate rule\n[Rn2(SS)c5_alpha;doublebond_intra_HCd_pri;radadd_intra_O]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Rn2(SS)c5_alpha;doublebond_intra_HCd_pri;radadd_intra] for rate rule
[Rn2(SS)c5_alpha;doublebond_intra_HCd_pri;radadd_intra_O]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5263,
    label = "CH3(17) + CPDyl(596) <=> C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5264,
    label = "H_10_(3) + C6H7(52) <=> C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.566e+14, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5265,
    label = "H_10_(3) + C6H7(55) <=> C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+12, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5266,
    label = "H2_13_(2) + C6H6(54) <=> C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(144200, 'cm^3/(mol*s)'), n=3.9, Ea=(81.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5295,
    label = "H_10_(3) + C6H7(52) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.094e+13, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5296,
    label = "H_10_(3) + C6H7(53) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+12, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (-0.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5297,
    label = "C6H8(608) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.033e+08, 's^-1'), n=1.2, Ea=(24.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5298,
    label = "H2_13_(2) + C6H6(54) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.079e+07, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (71, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5310,
    label = "CH3(17) + C5H5(50) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.379e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_rad;C_methyl] + [Cd_rad/NonDe;Y_rad] for rate rule [Cd_rad/NonDe;C_methyl]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_rad;C_methyl] + [Cd_rad/NonDe;Y_rad] for rate rule [Cd_rad/NonDe;C_methyl]
""",
)

entry(
    index = 5332,
    label = "H_10_(3) + C6H7(52) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.055e+13, 'cm^3/(mol*s)'), n=0.1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5333,
    label = "H_10_(3) + C6H7(56) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.428e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5334,
    label = "C6H8(597) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.654e+07, 's^-1'), n=2.1, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5335,
    label = "H2_13_(2) + C6H6(54) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.623e+06, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (55.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: c-C5H5_CH3_Sharma_TST
""",
)

entry(
    index = 5367,
    label = "C6H8(628) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5368,
    label = "C6H8(628) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5369,
    label = "C6H8(627) <=> C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5370,
    label = "C6H8(627) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.726e+10, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH(C)C]',
    ),
    longDesc = 
u"""
Estimated using template [CsJ2-C;CsJ2(CsC);CH] for rate rule [CsJ2-C;CsJ2(CsC);CH(C)C]
""",
)

entry(
    index = 5375,
    label = "H_10_(3) + CPDyl(596) <=> CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;C_rad_cyclopentadiene]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;C_rad_cyclopentadiene]
""",
)

entry(
    index = 5389,
    label = "CH2(S)(28) + CPD(595) <=> C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5392,
    label = "CH2(S)(28) + CPD(595) <=> C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.52e+13, 'cm^3/(mol*s)'),
        n = -0.274,
        Ea = (-0.686, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/NonDeC from training reaction 6\nExact match found for rate rule [carbene;Cd/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/NonDeC from training reaction 6
Exact match found for rate rule [carbene;Cd/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5395,
    label = "CH2(S)(28) + CPD(595) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.468e+11, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5398,
    label = "CPDyl(596) + CPDyl(596) <=> S(601)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad_cyclopentadiene;C_rad_cyclopentadiene]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad_cyclopentadiene;C_rad_cyclopentadiene]
""",
)

entry(
    index = 5399,
    label = "H_10_(3) + C5H5(50) <=> CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cd_rad/NonDe;H_rad from training reaction 20\nExact match found for rate rule [Cd_rad/NonDe;H_rad]',
    ),
    longDesc = 
u"""
Cd_rad/NonDe;H_rad from training reaction 20
Exact match found for rate rule [Cd_rad/NonDe;H_rad]
""",
)

entry(
    index = 5434,
    label = "CH2(S)(28) + C5H6(629) <=> C6H8(628)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.52e+13, 'cm^3/(mol*s)'),
        n = -0.274,
        Ea = (-0.686, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/NonDeC from training reaction 6\nExact match found for rate rule [carbene;Cd/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/NonDeC from training reaction 6
Exact match found for rate rule [carbene;Cd/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5435,
    label = "CH2(S)(28) + C5H6(629) <=> C6H8(627)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.494e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/OneDeC]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/OneDeC]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 5436,
    label = "C5H6(629) <=> CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37e+12, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5437,
    label = "CPD(595) <=> C5H6(630)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (46.66, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5438,
    label = "S(601) <=> S(602)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.11e+08, 's^-1'), n=1.6, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: biCPD_H_shift
""",
)

entry(
    index = 5439,
    label = "C5H5(50) + CPDyl(596) <=> S(602)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.704e+14, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [Cd_rad/NonDe;C_rad_cyclopentadiene]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [Cd_rad/NonDe;C_rad_cyclopentadiene]
""",
)

entry(
    index = 5440,
    label = "S(602) <=> S(603)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+08, 's^-1'), n=1.55, Ea=(19.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: biCPD_H_shift
""",
)

entry(
    index = 5441,
    label = "C5H5(50) + C5H5(50) <=> S(603)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_rad/NonDe] + [Cd_rad/NonDe;Y_rad] for rate rule [Cd_rad/NonDe;Cd_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_rad/NonDe] + [Cd_rad/NonDe;Y_rad] for rate rule [Cd_rad/NonDe;Cd_rad/NonDe]
""",
)

entry(
    index = 5446,
    label = "S(603) <=> S(604)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+07, 's^-1'), n=1.81, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: biCPD_H_shift
""",
)

entry(
    index = 5450,
    label = "S(602) <=> S(605)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.19e+07, 's^-1'), n=1.72, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: biCPD_H_shift
""",
)

entry(
    index = 5451,
    label = "S(605) <=> S(604)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+08, 's^-1'), n=1.55, Ea=(20.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: biCPD_H_shift
""",
)

entry(
    index = 5452,
    label = "S(604) <=> S(606)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.22e+07, 's^-1'), n=1.76, Ea=(25, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: biCPD_H_shift
""",
)

entry(
    index = 5453,
    label = "S(604) <=> S(631)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5454,
    label = "C8H8(622) <=> C8H8(624)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;CddC_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CddC_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;CddC_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CddC_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5455,
    label = "S(606) <=> S(632)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5484,
    label = "C5H5(179) <=> CPDyl(596)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.893e+08, 's^-1'),
        n = 1.24,
        Ea = (38.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R3H_DS;Cd_rad_out_single;Cs_H_out_1H] + [R3H_DS;Cd_rad_out_singleDe;Cs_H_out] for rate rule\n[R3H_DS;Cd_rad_out_singleDe_Cd;Cs_H_out_H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using average of templates [R3H_DS;Cd_rad_out_single;Cs_H_out_1H] + [R3H_DS;Cd_rad_out_singleDe;Cs_H_out] for rate rule
[R3H_DS;Cd_rad_out_singleDe_Cd;Cs_H_out_H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5485,
    label = "C5H5(50) <=> C5H5(179)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+11, 's^-1'),
        n = 0.633,
        Ea = (46.955, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_singleDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R2H_D;Cd_rad_out_Cs;Cd_H_out_singleDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5486,
    label = "C3H3(19) + C5H5(179) <=> C8H8(622)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.29e+09, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (-1.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_allenic;Cd_rad] for rate rule [Cd_allenic;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_allenic;Cd_rad] for rate rule [Cd_allenic;Cd_rad/Cd]
""",
)

entry(
    index = 5487,
    label = "C3H3(19) + C5H5(179) <=> C8H8(626)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.307e+12, 'cm^3/(mol*s)'),
        n = 0.192,
        Ea = (-0.671, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Ct;Cd_rad] for rate rule [C_rad/H2/Ct;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Ct;Cd_rad] for rate rule [C_rad/H2/Ct;Cd_rad/Cd]
""",
)

entry(
    index = 5488,
    label = "CH3(17) + C5H5(179) <=> C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.901e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;C_methyl] for rate rule [Cd_rad/Cd;C_methyl]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;C_methyl] for rate rule [Cd_rad/Cd;C_methyl]
""",
)

entry(
    index = 5489,
    label = "H_10_(3) + C5H5(179) <=> CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_sec_rad;H_rad] for rate rule [Cd_rad/Cd;H_rad]
""",
)

entry(
    index = 5518,
    label = "C5H5(50) + C5H5(179) <=> S(604)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cd_rad/NonDe] for rate rule [Cd_rad/Cd;Cd_rad/NonDe]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cd_rad/NonDe] for rate rule [Cd_rad/Cd;Cd_rad/NonDe]
""",
)

entry(
    index = 5519,
    label = "CPDyl(596) + C5H5(179) <=> S(605)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.704e+14, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [Cd_rad/Cd;C_rad_cyclopentadiene]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [Cd_rad/Cd;C_rad_cyclopentadiene]
""",
)

entry(
    index = 5520,
    label = "C5H5(179) + C5H5(179) <=> S(606)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.569e+11, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (-0.515, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cd_rad] for rate rule [Cd_rad/Cd;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cd_rad] for rate rule [Cd_rad/Cd;Cd_rad/Cd]
""",
)

entry(
    index = 5531,
    label = "CH2O2(594) <=> H2O_14_(6) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.6018, 0.6171, -0.1054, 0.007814],
            [8.628, 0.733, -0.04376, -0.01665],
            [-0.3676, 0.2191, 0.03794, -0.007406],
            [-0.1437, 0.02525, 0.02087, 0.003766],
            [-0.03995, -0.009088, 0.002114, 0.002521],
            [-0.006392, -0.006615, -0.001767, 4.68e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5532,
    label = "CH2O2(594) <=> H2_13_(2) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.156, 1.097, -0.2177, 0.008836],
            [9.52, 0.6935, 0.07305, -0.04772],
            [-0.4008, 0.0929, 0.06721, 0.006691],
            [-0.1286, -0.01301, 0.01006, 0.009467],
            [-0.02896, -0.01349, -0.003882, 0.001732],
            [-0.0009304, -0.005488, -0.002881, -0.0005185],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5536,
    label = "OH_12_(12) + HCO(22) <=> CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.31, 0.8941, -0.1819, 0.009001],
            [-0.8854, 0.6679, 0.01782, -0.03333],
            [-0.3355, 0.1313, 0.05116, 0.0001339],
            [-0.118, 0.01193, 0.01405, 0.005659],
            [-0.03993, -0.002922, 0.0007597, 0.001566],
            [-0.0128, -0.002, -0.0007325, -7.62e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5544,
    label = "H_10_(3) + CHO2(42) <=> CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.33, 0.4999, -0.1106, 0.008102],
            [-0.6296, 0.5661, -0.05764, -0.01709],
            [-0.2728, 0.1924, 0.01628, -0.009267],
            [-0.1036, 0.04678, 0.01463, 0.0004252],
            [-0.03727, 0.008509, 0.004722, 0.001597],
            [-0.01309, 0.0009182, 0.0008215, 0.0005934],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5545,
    label = "H_10_(3) + CHO2(424) <=> CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.35, 0.406, -0.0917, 0.007574],
            [-0.5263, 0.5381, -0.07575, -0.01054],
            [-0.263, 0.2133, 0.006062, -0.0117],
            [-0.1059, 0.05628, 0.01617, -0.001705],
            [-0.03819, 0.009199, 0.006698, 0.001739],
            [-0.01302, 1.412e-06, 0.001176, 0.001033],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5556,
    label = "C5H7(598) <=> H_10_(3) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.19e+09, 's^-1'), n=1.37, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 5557,
    label = "addB(599) <=> C7H9(59)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.37e+06, 's^-1'), n=1.6, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 5558,
    label = "addB(599) <=> C2H4(30) + CPDyl(596)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.87e+11, 's^-1'), n=0.68, Ea=(13.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 5559,
    label = "C2H2(20) + CPDyl(596) <=> C7H7(600)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25500, 'cm^3/(mol*s)'), n=2.27, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 5561,
    label = "H_10_(3) + C4H8(78) <=> C4H9(635)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Cds-HH_Cds-CsH;HJ from training reaction 10\nExact match found for rate rule [Cds-HH_Cds-CsH;HJ]',
    ),
    longDesc = 
u"""
Cds-HH_Cds-CsH;HJ from training reaction 10
Exact match found for rate rule [Cds-HH_Cds-CsH;HJ]
""",
)

entry(
    index = 5566,
    label = "H_10_(3) + C4H8(83) <=> C4H9(635)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.37, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cds-CsH_Cds-CsH;HJ]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cds-CsH_Cds-CsH;HJ]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5574,
    label = "C3H6(38) + CH3(17) <=> C4H9(635)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7318, 'cm^3/(mol*s)'),
        n = 2.486,
        Ea = (5.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cds-HH_Cds-CsH;CsJ-HHH] + [Cds-HH_Cds-Cs\\H3/H;CsJ] for rate rule [Cds-HH_Cds-Cs\\H3/H;CsJ-HHH]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cds-HH_Cds-CsH;CsJ-HHH] + [Cds-HH_Cds-Cs\H3/H;CsJ] for rate rule [Cds-HH_Cds-Cs\H3/H;CsJ-HHH]
""",
)

entry(
    index = 5589,
    label = "CH2(S)(28) + C3H7(79) <=> C4H9(635)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.626e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 5603,
    label = "C3H6(38) + C3H3(19) <=> C6H9(636)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6584, 'cm^3/(mol*s)'),
        n = 2.516,
        Ea = (2.887, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cds-HH_Cds-Cs\\H3/H;CJ] for rate rule [Cds-HH_Cds-Cs\\H3/H;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Cds-HH_Cds-Cs\H3/H;CJ] for rate rule [Cds-HH_Cds-Cs\H3/H;CdsJ=Cdd]
""",
)

entry(
    index = 5606,
    label = "C6H7(52) + CH2(S)(28) <=> C7H9(59)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.313e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [carbene;R_H]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [carbene;R_H]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 5662,
    label = "O2_2_(13) + C4H5(443) <=> S(637)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.861e+14, 'cm^3/(mol*s)'),
        n = -0.087,
        Ea = (3.562, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad/H/OneDeC] for rate rule [O2_birad;C_rad/H/CtCs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad/H/OneDeC] for rate rule [O2_birad;C_rad/H/CtCs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5663,
    label = "S(637) <=> HO2_17_(5) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.476e+06, 's^-1'),
        n = 1.829,
        Ea = (24.247, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [R2OO_2H_HDe]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [R2OO_2H_HDe]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5710,
    label = "C5H3(141) + C5H4(130) <=> C10H7(638)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (204200, 'cm^3/(mol*s)'),
        n = 2.286,
        Ea = (1.181, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-H_Ct-Ct;CJ] for rate rule [Ct-H_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 5724,
    label = "C5H3(162) + C5H4(130) <=> C10H7(639)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (260000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.553, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Cs_Ct-Ct;CJ] for rate rule [Ct-Cs_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 5725,
    label = "CH2(S)(28) + C9H5(170) <=> C10H7(639)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5728,
    label = "C3H3(19) + C7H4(484) <=> C10H7(643)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (192400, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.083, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Ct_Ct-Ct;CJ] for rate rule [Ct-Ct_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Ct_Ct-Ct;CJ] for rate rule [Ct-Ct_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 5729,
    label = "C3H3(19) + C7H4(484) <=> C10H7(644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (192400, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (2.083, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct-Ct_Ct-Ct;CJ] for rate rule [Ct-Ct_Ct-Ct;CdsJ=Cdd]',
    ),
    longDesc = 
u"""
Estimated using template [Ct-Ct_Ct-Ct;CJ] for rate rule [Ct-Ct_Ct-Ct;CdsJ=Cdd]
""",
)

entry(
    index = 5730,
    label = "C3H3(86) + C7H4(157) <=> C10H7(644)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.892e+08, 'cm^3/(mol*s)'),
        n = 1.205,
        Ea = (1.194, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-Cd_Ct-Ct;CJ] for rate rule [Ct-Cd_Ct-Ct;CtJ_Ct]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Ct_Ct;CtJ_Ct] + [Ct-Cd_Ct-Ct;CJ] for rate rule [Ct-Cd_Ct-Ct;CtJ_Ct]
""",
)

entry(
    index = 5774,
    label = "CH3(17) + C9H4(500) <=> C10H7(540)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (159000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (5.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cd_Ct-Ct;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cd_Ct-Ct;CsJ-HHH]
""",
)

entry(
    index = 5784,
    label = "CH3(17) + C7H4(484) <=> C8H7(642)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (597000, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (5.42, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct-Cs_Ct-Ct;CsJ-HHH]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct-Cs_Ct-Ct;CsJ-HHH]
""",
)

entry(
    index = 5789,
    label = "C7H5(457) <=> C7H5(640)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+10, 's^-1'),
        n = 0.98,
        Ea = (26.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd) from training reaction 20\nExact match found for rate rule [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd) from training reaction 20
Exact match found for rate rule [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5790,
    label = "C7H5(480) <=> C7H5(640)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (13.71, 's^-1'),
                n = 3.311,
                Ea = (30.765, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cd_rad_out_singleDe_Cd;Cd_H_out_singleH]\nMultiplied by reaction path degeneracy 4',
            ),
            Arrhenius(
                A = (4.168e+09, 's^-1'),
                n = 0.809,
                Ea = (39.151, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using an average for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;CddC_2]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [R5H_RSDD;Y_rad_out;Cd_H_out_singleH] for rate rule [R5H_RSDD;Cd_rad_out_singleDe_Cd;Cd_H_out_singleH]
Multiplied by reaction path degeneracy 4
Estimated using an average for rate rule [1_3_unsaturated_pentane_backbone;CdH2_1;CddC_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5792,
    label = "C7H5(640) <=> C7H5(646)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.297e+12, 's^-1'),
                n = 0.065,
                Ea = (27.941, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn;triplebond_intra_H;radadd_intra_csH(CdCdCd)] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csH(CdCdCd)]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (1.328e+12, 's^-1'),
                n = 0.3,
                Ea = (16.261, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using an average for rate rule [Rn2c5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4\nEa raised from 66.2 to 68.0 kJ/mol to match endothermicity of reaction.',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rn;triplebond_intra_H;radadd_intra_csH(CdCdCd)] for rate rule [R4_S_T;triplebond_intra_H;radadd_intra_csH(CdCdCd)]
Multiplied by reaction path degeneracy 2
Estimated using an average for rate rule [Rn2c5_alpha;doublebond_intra_HCd_pri;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
Ea raised from 66.2 to 68.0 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 5794,
    label = "C7H5(645) <=> C7H5(560)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.331e+11, 's^-1'),
        n = 0.625,
        Ea = (38.324, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [R2H_S_cy5;C_rad_out_H/Cd;Cs_H_out_noH]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [R2H_S_cy5;C_rad_out_H/Cd;Cs_H_out_noH]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5795,
    label = "C7H5(640) <=> C7H5(645)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.51e+10, 's^-1'),
                n = 0.34,
                Ea = (31.2, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_csHCd] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 3',
            ),
            Arrhenius(
                A = (1.026e+12, 's^-1'),
                n = 0.18,
                Ea = (17.787, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using average of templates [Rnxc5;doublebond_intra;radadd_intra_cdsingleH] + [Rn2c5_beta_long;doublebond_intra;radadd_intra] for rate rule\n[Rn2c5_beta_long;doublebond_intra;radadd_intra_cdsingleH]\nMultiplied by reaction path degeneracy 4\nEa raised from 70.4 to 74.4 kJ/mol to match endothermicity of reaction.',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rn2c5_beta;multiplebond_intra;radadd_intra_csHCd] for rate rule [Rn2c5_beta;triplebond_intra_H;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 3
Estimated using average of templates [Rnxc5;doublebond_intra;radadd_intra_cdsingleH] + [Rn2c5_beta_long;doublebond_intra;radadd_intra] for rate rule
[Rn2c5_beta_long;doublebond_intra;radadd_intra_cdsingleH]
Multiplied by reaction path degeneracy 4
Ea raised from 70.4 to 74.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 5797,
    label = "O2_2_(13) + C7H5(640) <=> S(647)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.741e+15, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5798,
    label = "O2_2_(13) + C7H5(640) <=> S(648)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.741e+15, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C_rad_cyclopentadiene] for rate rule [O2_birad;C_rad_cyclopentadiene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5799,
    label = "C7H5(118) <=> C7H5(641)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.372e+10, 's^-1'),
        n = 0.215,
        Ea = (12.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 5800,
    label = "C7H5(641) <=> C7H5(480)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.33e+09, 's^-1'),
        n = 0.738,
        Ea = (52.276, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_pentyn_3_ene;CH_end;CtH_2] for rate rule [1_pentyn_3_ene;CH(CJ)_1;CtH_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1_pentyn_3_ene;CH_end;CtH_2] for rate rule [1_pentyn_3_ene;CH(CJ)_1;CtH_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5801,
    label = "C7H5(119) <=> C7H5(641)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.73e+10, 's^-1'),
        n = 0.19,
        Ea = (11.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_MS;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R5_MS;doublebond_intra;radadd_intra_cdsingleH] for rate rule [R5_MS;doublebond_intra_CdCdd;radadd_intra_cdsingleH]
""",
)

entry(
    index = 5802,
    label = "C7H5(641) <=> C7H5(640)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+10, 's^-1'),
        n = 0.98,
        Ea = (26.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd) from training reaction 20\nExact match found for rate rule [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd) from training reaction 20
Exact match found for rate rule [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5803,
    label = "O2_2_(13) + C7H5(640) <=> S(649)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.201e+12, 'cm^3/(mol*s)'),
        n = 0.095,
        Ea = (-1.708, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cd_allenic] + [O2_birad;Cd_rad] for rate rule [O2_birad;Cd_allenic]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5807,
    label = "O2_2_(13) + C7H5(640) <=> S(650)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2_birad;C_ter_rad] for rate rule [O2_birad;C_rad/ThreeDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O2_birad;C_ter_rad] for rate rule [O2_birad;C_rad/ThreeDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5811,
    label = "CO_21_(14) + C7H5(640) <=> C8H5O(651)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.61e+07, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (6.664, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]\nEa raised from 20.6 to 27.9 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [COm;C_sec_rad] for rate rule [COm;C_rad/H/TwoDe]
Ea raised from 20.6 to 27.9 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 5812,
    label = "C7H5(645) <=> C7H5(652)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.64e+11, 's^-1'),
        n = 0.3,
        Ea = (10.358, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [Rn2(DS)c5_alpha;doublebond_intra;radadd_intra]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [Rn2(DS)c5_alpha;doublebond_intra;radadd_intra]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5813,
    label = "C7H5(652) <=> C7H5(654)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.312e+12, 's^-1'),
        n = 0.34,
        Ea = (11.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd from training reaction 24\nExact match found for rate rule [Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd from training reaction 24
Exact match found for rate rule [Rn1c5_alpha;doublebond_intra_HCd_pri;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 5814,
    label = "C7H5(653) <=> C7H5(652)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.594e+11, 's^-1'),
        n = 0.315,
        Ea = (24.834, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnx_cyclics;doublebond_intra;radadd_intra_csHCd] for rate rule [Rn2c3_alpha;doublebond_intra;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Rnx_cyclics;doublebond_intra;radadd_intra_csHCd] for rate rule [Rn2c3_alpha;doublebond_intra;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5815,
    label = "C7H5(653) <=> C7H5(656)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.392e+11, 's^-1'),
        n = 0.315,
        Ea = (13.65, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Rnx_cyclics;doublebond_intra;radadd_intra_csHCd] for rate rule [Rn2c3_alpha;doublebond_intra;radadd_intra_csHCd]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Rnx_cyclics;doublebond_intra;radadd_intra_csHCd] for rate rule [Rn2c3_alpha;doublebond_intra;radadd_intra_csHCd]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5816,
    label = "C7H5(653) <=> C7H5(655)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2.201e+11, 's^-1'),
                n = 0.36,
                Ea = (33.645, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [Rnxc6;doublebond_intra;radadd_intra_cs] for rate rule [Rn1c6_beta_long;doublebond_intra;radadd_intra_cs]\nMultiplied by reaction path degeneracy 4',
            ),
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (29.257, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;C=C_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
            ),
        ],
    ),
    longDesc = 
u"""
Estimated using template [Rnxc6;doublebond_intra;radadd_intra_cs] for rate rule [Rn1c6_beta_long;doublebond_intra;radadd_intra_cs]
Multiplied by reaction path degeneracy 4
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;C=C_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5818,
    label = "C7H5(655) <=> C7H5(656)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.428e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_5_unsaturated_hexane] for rate rule [1_5_hexadiene]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1_5_unsaturated_hexane] for rate rule [1_5_hexadiene]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5842,
    label = "O2_2_(13) + C3H5(41) <=> S(633)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.07, 1.678, -0.1052, -0.01916],
            [-1.162, 0.3696, 0.1046, 0.01103],
            [-0.2373, -0.02874, 0.006061, 0.007403],
            [-0.09765, -0.01364, -0.002661, 0.001215],
            [-0.03547, -0.006948, -0.002918, -9.637e-05],
            [0.006173, -0.003094, -0.00166, -0.001336],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5843,
    label = "HO2_17_(5) + C3H4(39) <=> S(633)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.787, 0.5038, -0.0954, -0.0006299],
            [2.459, 0.7441, -0.1056, -0.01508],
            [-0.1537, 0.2992, 0.003697, -0.01757],
            [-0.05415, 0.04319, 0.02918, -0.003852],
            [-0.007456, -0.01382, 0.01097, 0.003369],
            [-0.004848, -0.003062, -0.0006035, 0.001622],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 5844,
    label = "C3H5(41) + C2H2(20) <=> C5H7(634)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (238000, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (12.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 5848,
    label = "CH2(S)(28) + S(609) <=> S(535)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.52e+13, 'cm^3/(mol*s)'),
        n = -0.274,
        Ea = (-0.686, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/NonDeC from training reaction 6\nExact match found for rate rule [carbene;Cd/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/NonDeC from training reaction 6
Exact match found for rate rule [carbene;Cd/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5867,
    label = "CH2(S)(28) + S(609) <=> S(534)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.468e+11, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5876,
    label = "C3H3(19) + C6H5O(610) <=> C9H8O(667)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.919e+14, 'cm^3/(mol*s)'),
        n = -0.467,
        Ea = (-0.42, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C_rad/H/CdCd] for rate rule [C_rad/H2/Ct;C_rad/H/CdCd]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C_rad/H/CdCd] for rate rule [C_rad/H2/Ct;C_rad/H/CdCd]
""",
)

entry(
    index = 5877,
    label = "C3H3(19) + C6H5O(610) <=> C9H8O(668)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.233e+14, 'cm^3/(mol*s)'),
        n = -0.389,
        Ea = (-0.393, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;C_rad/H/TwoDe] for rate rule [C_rad/H2/Ct;C_rad/H/TwoDe]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;C_rad/H/TwoDe] for rate rule [C_rad/H2/Ct;C_rad/H/TwoDe]
""",
)

entry(
    index = 5878,
    label = "C9H8O(616) <=> C9H8O(668)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.856e+09, 's^-1'),
        n = 0.749,
        Ea = (47.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = '1_5_unsaturated_hexane from training reaction 3\nExact match found for rate rule [1_5_unsaturated_hexane]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
1_5_unsaturated_hexane from training reaction 3
Exact match found for rate rule [1_5_unsaturated_hexane]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5879,
    label = "C3H3(19) + C6H5O(610) <=> C9H8O(666)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.589e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cs_rad;O_sec_rad] + [C_pri_rad;O_rad] for rate rule [C_rad/H2/Ct;O_rad/OneDe]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cs_rad;O_sec_rad] + [C_pri_rad;O_rad] for rate rule [C_rad/H2/Ct;O_rad/OneDe]
""",
)

entry(
    index = 5880,
    label = "C9H8O(666) <=> C9H8O(668)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1636, 's^-1'),
        n = 2.877,
        Ea = (34.079, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R_ROR] for rate rule [C_COC]',
    ),
    longDesc = 
u"""
Estimated using template [R_ROR] for rate rule [C_COC]
""",
)

entry(
    index = 5894,
    label = "CH3(17) + C6H5O(610) <=> C7H8O(664)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_methyl;C_rad/H/CdCd]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_methyl;C_rad/H/CdCd]
""",
)

entry(
    index = 5895,
    label = "CH3(17) + C6H5O(610) <=> C7H8O(665)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_methyl;C_rad/H/TwoDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_methyl;C_rad/H/TwoDe]
""",
)

entry(
    index = 5896,
    label = "C7H8O(665) <=> C7H8O(675)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5897,
    label = "CH3(17) + C6H5O(612) <=> C7H8O(675)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.623e+14, 'cm^3/(mol*s)'),
        n = -0.383,
        Ea = (1.781, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec_rad;C_methyl] + [C_rad/H/OneDeC;Y_rad] for rate rule [C_rad/H/OneDeC;C_methyl]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec_rad;C_methyl] + [C_rad/H/OneDeC;Y_rad] for rate rule [C_rad/H/OneDeC;C_methyl]
""",
)

entry(
    index = 5898,
    label = "CH3(17) + C6H5O(610) <=> C7H8O(663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;O_sec_rad] for rate rule [C_methyl;O_rad/OneDe]',
    ),
    longDesc = 
u"""
Estimated using template [C_methyl;O_sec_rad] for rate rule [C_methyl;O_rad/OneDe]
""",
)

entry(
    index = 5899,
    label = "C7H8O(663) <=> C7H8O(665)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1636, 's^-1'),
        n = 2.877,
        Ea = (34.079, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R_ROR] for rate rule [C_COC]',
    ),
    longDesc = 
u"""
Estimated using template [R_ROR] for rate rule [C_COC]
""",
)

entry(
    index = 5912,
    label = "C7H8O(676) <=> C7H8O(665)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37990, 's^-1'),
        n = 2.515,
        Ea = (48.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_COH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_COH]
""",
)

entry(
    index = 5913,
    label = "C7H8O(665) <=> C7H8O(674)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.036e+08, 's^-1'),
        n = 1.021,
        Ea = (38.586, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule [1_3_pentadiene;CH(C)C_1;CdHC_2]',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule [1_3_pentadiene;CH(C)C_1;CdHC_2]
""",
)

entry(
    index = 5914,
    label = "C7H8O(676) <=> C7H8O(674)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37990, 's^-1'),
        n = 2.515,
        Ea = (48.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_COH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_COH]
""",
)

entry(
    index = 5915,
    label = "C7H8O(674) <=> C7H8O(677)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;Cd(C)C_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;Cd(C)C_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5920,
    label = "H_10_(3) + C6H5O(610) <=> C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.184e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_sec_rad] for rate rule [H_rad;O_rad/OneDe]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_sec_rad] for rate rule [H_rad;O_rad/OneDe]
""",
)

entry(
    index = 5942,
    label = "CH2(S)(28) + C6H6O(661) <=> C7H8O(663)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.438e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;R_H] for rate rule [carbene;RO_H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [carbene;R_H] for rate rule [carbene;RO_H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5943,
    label = "CH2(S)(28) + C6H6O(661) <=> C7H8O(676)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.875e+11, 'cm^3/(mol*s)'),
        n = 0.444,
        Ea = (-1.216, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;R_H] for rate rule [carbene;Cb_H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;R_H] for rate rule [carbene;Cb_H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5944,
    label = "OH_12_(12) + C6H5(64) <=> C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.805e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.05, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Y_rad] for rate rule [O_pri_rad;Cb_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Y_rad] for rate rule [O_pri_rad;Cb_rad]
""",
)

entry(
    index = 5969,
    label = "H_10_(3) + C6H5O(610) <=> C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.038e+12, 'cm^3/(mol*s)'),
        n = -0.099,
        Ea = (0.544, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [H_rad;C_rad/H/TwoDe]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [H_rad;C_rad/H/TwoDe]
""",
)

entry(
    index = 5991,
    label = "CH2(S)(28) + C6H6O(662) <=> C7H8O(665)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/TwoDe]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5992,
    label = "CH2(S)(28) + C6H6O(662) <=> C7H8O(674)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        Ea = (-1.758, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/OneDe from training reaction 10\nExact match found for rate rule [carbene;Cd/H/OneDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
carbene;Cd/H/OneDe from training reaction 10
Exact match found for rate rule [carbene;Cd/H/OneDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5993,
    label = "C6H6O(661) <=> C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37990, 's^-1'),
        n = 2.515,
        Ea = (48.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_COH]',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_COH]
""",
)

entry(
    index = 6006,
    label = "CH2(S)(28) + C6H6O(669) <=> C7H8O(675)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/OneDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/OneDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6007,
    label = "CH2(S)(28) + C6H6O(669) <=> C7H8O(677)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.735e+11, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6008,
    label = "C6H6O(662) <=> C6H6O(669)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.257, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6009,
    label = "C6H6O(678) <=> C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6010,
    label = "H_10_(3) + C6H5O(612) <=> C6H6O(669)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/OneDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/OneDeC;H_rad]
""",
)

entry(
    index = 6053,
    label = "C6H8(607) <=> C6H8(672)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (46.435, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2\nEa raised from 194.2 to 194.3 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
Ea raised from 194.2 to 194.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 6055,
    label = "CH2(S)(28) + C5H6(630) <=> C6H8(672)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.52e+13, 'cm^3/(mol*s)'),
        n = -0.274,
        Ea = (-0.686, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'carbene;Cd/H/NonDeC from training reaction 6\nExact match found for rate rule [carbene;Cd/H/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
carbene;Cd/H/NonDeC from training reaction 6
Exact match found for rate rule [carbene;Cd/H/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6056,
    label = "S(603) <=> S(679)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (29.872, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;CdH(C)_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6059,
    label = "S(680) <=> S(604)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.229e+09, 's^-1'),
        n = 1.021,
        Ea = (38.586, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule [1_3_pentadiene;CH2(C)_1;CdHC_2]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [1_3_unsaturated_pentane_backbone;CH_end;unsaturated_end] for rate rule [1_3_pentadiene;CH2(C)_1;CdHC_2]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 6063,
    label = "C6H8(597) <=> C6H8(671)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0.056,
        Ea = (46.281, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;Cd(C)C_1;CdH(C)_2]\nMultiplied by reaction path degeneracy 2\nEa raised from 193.3 to 193.6 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [1,3-butadiene_backbone;C=C_1;C=C_2] for rate rule [1,3-butadiene_backbone;Cd(C)C_1;CdH(C)_2]
Multiplied by reaction path degeneracy 2
Ea raised from 193.3 to 193.6 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 6064,
    label = "CH2(S)(28) + C5H6(630) <=> C6H8(671)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.747e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (-0.354, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/Cs2]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H/Cs2]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6067,
    label = "C5H6(673) <=> CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.359e+10, 's^-1'),
        n = -0.074,
        Ea = (4.556, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [singletcarbene_CH;CsJ2(C=C);CH2(C)] + [CsJ2-C;CsJ2(C=C);CH] for rate rule [CsJ2-C;CsJ2(C=C);CH2(C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [singletcarbene_CH;CsJ2(C=C);CH2(C)] + [CsJ2-C;CsJ2(C=C);CH] for rate rule [CsJ2-C;CsJ2(C=C);CH2(C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6068,
    label = "C5H6(673) <=> C5H6(681)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.726e+10, 's^-1'),
        n = 0.441,
        Ea = (15.891, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CsJ2-C;CsJ2(CsC);CH=C from training reaction 3\nExact match found for rate rule [CsJ2-C;CsJ2(CsC);CH=C]',
    ),
    longDesc = 
u"""
CsJ2-C;CsJ2(CsC);CH=C from training reaction 3
Exact match found for rate rule [CsJ2-C;CsJ2(CsC);CH=C]
""",
)

entry(
    index = 6071,
    label = "C8H8(670) <=> C8H8(621)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6072,
    label = "C8H8(670) <=> C8H8(622)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.85e+11, 's^-1'),
        n = 0.413,
        Ea = (4.117, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [singletcarbene_CH;CsJ2C;CH2(C=C)] for rate rule [CsJ2-C;CsJ2(CsC);CH2(C=C)]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6117,
    label = "O2_2_(13) + C3H3(19) <=> S(658)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [10.05, -0.06104, -0.03339, -0.01233],
            [0.4359, 0.08175, 0.04264, 0.01404],
            [0.09439, -0.02882, -0.01341, -0.003115],
            [0.03362, 0.003668, 0.001083, -0.0002929],
            [0.009097, 0.0017, 0.0009682, 0.0004377],
            [0.001516, -0.0003144, 0.0001039, 0.0001642],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6118,
    label = "O2_2_(13) + C3H3(19) <=> S(658)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [9.239, 1.086, -0.2044, -0.02362],
            [-0.6114, 0.848, 0.1101, -0.01431],
            [-0.08658, -0.005369, 0.03116, 0.005501],
            [0.02157, -0.01932, 0.004557, 0.004745],
            [-0.009055, 0.004073, 0.003469, 0.001868],
            [-0.01948, 0.002068, 0.002413, 0.00111],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6119,
    label = "S(658) <=> S(566)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.794, 1.132, -0.1494, -0.00885],
            [2.238, 0.7664, 0.048, -0.02595],
            [-0.2425, 0.03744, 0.04332, 0.009059],
            [-0.05536, -0.02555, 0.005089, 0.004817],
            [-0.04263, 0.001482, 0.002641, 0.0007793],
            [-0.03222, 0.003572, 0.002865, 0.000845],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6120,
    label = "S(567) <=> S(658)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.126, 1.757, -0.0951, -0.01336],
            [1.859, 0.2778, 0.1057, 0.01133],
            [-0.05629, -0.01532, -0.005871, 0.0005002],
            [0.0372, -0.02303, -0.006068, 0.000757],
            [-0.0239, 0.002034, -0.001549, -0.0009252],
            [-0.02324, -0.00674, 0.0002509, 0.001069],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6122,
    label = "CH3OO(657) <=> HO2_17_(5) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.841, 1.986, -0.00981, -0.005351],
            [14.35, 0.01451, 0.009956, 0.005398],
            [-0.1857, -0.001276, -0.0008476, -0.0004337],
            [-0.006478, -0.0008912, -0.0006182, -0.0003413],
            [0.02198, -0.0001938, -0.0001365, -7.727e-05],
            [0.01297, 3.568e-05, 2.415e-05, 1.278e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6126,
    label = "CHO3(659) <=> OH_12_(12) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.589, 1.981, -0.01201, -0.005509],
            [-0.1318, 0.02249, 0.01369, 0.005926],
            [-0.09971, -0.004758, -0.002706, -0.000983],
            [0.01458, -0.001543, -0.0009609, -0.0004416],
            [-0.01228, 0.001093, 0.0006084, 0.0002125],
            [-0.001738, -8.725e-05, -3.119e-05, 6.284e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6127,
    label = "O_11_(7) + CHO2(42) <=> CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.41, 0.6168, -0.1236, 0.007369],
            [-0.6984, 0.5893, -0.02811, -0.01964],
            [-0.2969, 0.1714, 0.02493, -0.004571],
            [-0.1109, 0.03609, 0.01242, 0.002028],
            [-0.03922, 0.005369, 0.002857, 0.001228],
            [-0.01336, 0.00022, 0.000287, 0.0002323],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6132,
    label = "C5H7(634) <=> C5H7(598)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+09, 's^-1'), n=0.62, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6133,
    label = "C3H6(38) + C6H5(64) <=> i1(660)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.735, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2006 Park',
    ),
    longDesc = 
u"""
Originally from reaction library: 2006_Park_Phenyl_Propene
From 2006 Park
""",
)

entry(
    index = 6177,
    label = "C8H5(451) <=> C8H5(684)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.372e+10, 's^-1'),
        n = 0.215,
        Ea = (12.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingleDe]',
    ),
    longDesc = 
u"""
Estimated using template [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingle] for rate rule [R5_DS_T;triplebond_intra_H;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 6178,
    label = "C7H5(164) <=> C7H5(683)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.88e+10, 's^-1'),
        n = 0.31,
        Ea = (12.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R5_DS_T;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R5_DS_T;triplebond_intra_De;radadd_intra_cdsingleH]',
    ),
    longDesc = 
u"""
Estimated using template [R5_DS_T;triplebond_intra;radadd_intra_cdsingleH] for rate rule [R5_DS_T;triplebond_intra_De;radadd_intra_cdsingleH]
""",
)

entry(
    index = 6179,
    label = "C7H5(683) <=> C7H5(640)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+10, 's^-1'),
        n = 0.98,
        Ea = (26.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd) from training reaction 20\nExact match found for rate rule [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd)]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd) from training reaction 20
Exact match found for rate rule [R2H_S_cy5;Cd_rad_out_Cd;Cs_H_out_H/(Cd-Cd-Cd)]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6180,
    label = "C7H5(641) <=> C7H5(683)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.823e+09, 's^-1'),
        n = 1.003,
        Ea = (33.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [R3H_SS;Cd_rad_out_double;XH_out] for rate rule [R3H_SS_Cs;Cd_rad_out_Cd;Cd_H_out_doubleC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [R3H_SS;Cd_rad_out_double;XH_out] for rate rule [R3H_SS_Cs;Cd_rad_out_Cd;Cd_H_out_doubleC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6181,
    label = "C7H5(120) <=> C7H5(682)",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1e+12, 's^-1'),
                n = 0.056,
                Ea = (29.257, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = '1,3-butadiene_backbone;CddC_1;CddC_2 from training reaction 1\nExact match found for rate rule [1,3-butadiene_backbone;CddC_1;CddC_2]\nMultiplied by reaction path degeneracy 2',
            ),
            Arrhenius(
                A = (1.767e+11, 's^-1'),
                n = 0.248,
                Ea = (19.557, 'kcal/mol'),
                T0 = (1, 'K'),
                comment = 'Estimated using template [R4_D_D;doublebond_intra;radadd_intra_cdsingle] for rate rule [R4_D_D;doublebond_intra;radadd_intra_cdsingleDe]',
            ),
        ],
    ),
    longDesc = 
u"""
1,3-butadiene_backbone;CddC_1;CddC_2 from training reaction 1
Exact match found for rate rule [1,3-butadiene_backbone;CddC_1;CddC_2]
Multiplied by reaction path degeneracy 2
Estimated using template [R4_D_D;doublebond_intra;radadd_intra_cdsingle] for rate rule [R4_D_D;doublebond_intra;radadd_intra_cdsingleDe]
""",
)

entry(
    index = 6196,
    label = "H_10_(3) + C4H9(635) <=> C4H10(685)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H/NonDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H/NonDeC;H_rad]
""",
)

entry(
    index = 6203,
    label = "C4H10(685) <=> C2H5(31) + C2H5(31)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.058, 0.5424, -0.05689, 0.0003419],
            [11.3, 0.83, -0.05573, -0.007263],
            [-0.8018, 0.3655, 0.01704, -0.007981],
            [-0.2907, 0.06074, 0.02725, 0.0004221],
            [-0.05777, -0.03009, 0.007209, 0.003467],
            [0.01009, -0.02171, -0.003573, 0.0009105],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6212,
    label = "CO2_5_(8) + C3H6(81) <=> S(687)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.196e+16, 'cm^3/(mol*s)'),
        n = -0.422,
        Ea = (-0.009, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [elec_def;multiplebond] for rate rule [dime_carbene;mb_carbonyl]\nMultiplied by reaction path degeneracy 144',
    ),
    longDesc = 
u"""
Estimated using template [elec_def;multiplebond] for rate rule [dime_carbene;mb_carbonyl]
Multiplied by reaction path degeneracy 144
""",
)

entry(
    index = 6273,
    label = "C4H10(685) <=> C3H7(35) + CH3(17)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.274, 0.5627, -0.06031, 0.0008394],
            [11.67, 0.8478, -0.05523, -0.007959],
            [-0.7678, 0.3591, 0.021, -0.008329],
            [-0.2747, 0.05175, 0.02828, 0.0008482],
            [-0.04962, -0.03347, 0.006552, 0.003566],
            [0.01323, -0.02185, -0.003832, 0.0007413],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6275,
    label = "C4H10(685) <=> H_10_(3) + C4H9(37)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.438, 0.8131, -0.1084, 0.008943],
            [13.76, 0.9477, -0.01118, -0.02343],
            [-0.6345, 0.2417, 0.06382, -0.006207],
            [-0.1703, -0.03238, 0.02642, 0.007039],
            [0.00834, -0.05224, -0.003617, 0.00357],
            [0.03326, -0.0163, -0.00648, -0.0004528],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6290,
    label = "C7H7(600) <=> C7H7(686)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6291,
    label = "CO_21_(14) + CH3O(508) <=> S(558)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.41e+07, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [COm;O_rad/NonDe]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [COm;O_rad/NonDe]
""",
)

entry(
    index = 6292,
    label = "O2_2_(13) + C2H3(29) <=> S(688)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2_birad;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2_birad;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6294,
    label = "C2H3O(430) <=> CO_21_(14) + CH3(17)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.93e+12, 's^-1'), n=0.29, Ea=(40.326, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.34e+27, 'cm^3/(mol*s)'),
            n = -3.18,
            Ea = (33.445, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.211,
        T3 = (199, 'K'),
        T1 = (2030, 'K'),
        T2 = (112000, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6296,
    label = "O_11_(7) + C2H3O(430) <=> S(688)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Oa] for rate rule [O_rad/OneDe;Oa]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Oa] for rate rule [O_rad/OneDe;Oa]
""",
)

entry(
    index = 6298,
    label = "C2H3O(430) <=> H_10_(3) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.43e+15, 's^-1'), n=-0.15, Ea=(45.606, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.44e+29, 'cm^3/(mol*s)'),
            n = -3.79,
            Ea = (43.577, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.796,
        T3 = (100, 'K'),
        T1 = (50000, 'K'),
        T2 = (34200, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[C-]#[O+]': 1.5, 'C=C': 3, 'C#C': 3},
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6302,
    label = "C2H3O(430) <=> CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10210, 's^-1'),
        n = 2.541,
        Ea = (38.006, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [R2H_S;C_rad_out_single;CO_H_out] + [R2H_S;C_rad_out_2H;XH_out] for rate rule [R2H_S;C_rad_out_2H;CO_H_out]',
    ),
    longDesc = 
u"""
Estimated using average of templates [R2H_S;C_rad_out_single;CO_H_out] + [R2H_S;C_rad_out_2H;XH_out] for rate rule [R2H_S;C_rad_out_2H;CO_H_out]
""",
)

entry(
    index = 6324,
    label = "C4H9(690) + CH3(17) <=> C5H12(691)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cs;C_methyl]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;C_methyl]
""",
)

entry(
    index = 6325,
    label = "O2_2_(13) + C2H5(31) <=> S(692)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.61, 1.14, -0.1701, -0.003511],
            [-1.069, 0.6464, 0.0554, -0.02672],
            [-0.267, 0.07137, 0.03174, 0.002435],
            [-0.03172, -0.01568, 0.004158, 0.002286],
            [-0.01443, -0.0001976, 0.0004474, 0.0004965],
            [-0.01683, 0.003968, 0.001597, 0.0003997],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6326,
    label = "HO2_17_(5) + C2H4(30) <=> S(692)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.929, 0.8024, -0.124, 0.0003579],
            [1.398, 0.8761, -0.03177, -0.02858],
            [-0.1214, 0.1768, 0.05302, -0.005439],
            [-0.009723, -0.01858, 0.01928, 0.006424],
            [0.0009905, -0.01206, -0.0002835, 0.001811],
            [-0.007284, 0.001624, 0.0003906, -0.0004789],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6327,
    label = "C3H6(38) + CH3(17) <=> C4H9(690)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.915, 0.9107, -0.1266, -0.002293],
            [0.6979, 0.9479, -0.007922, -0.03067],
            [-0.2306, 0.1411, 0.07661, 0.0005063],
            [-0.06376, -0.03073, 0.02516, 0.01143],
            [-0.04095, -0.01034, 0.002942, 0.004075],
            [-0.02996, -0.002481, 0.001842, 0.001597],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6328,
    label = "CH3OO(657) <=> O_11_(7) + CH3O(508)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.4886, 1.643, -0.1773, -0.04547],
            [7.962, 0.3177, 0.14, 0.0198],
            [-0.3172, 0.01589, 0.01895, 0.01382],
            [-0.05942, -0.01864, -0.007461, 0.0002979],
            [0.006325, -0.008165, -0.004971, -0.001946],
            [0.01021, -0.0005226, -0.0008296, -0.0007756],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6331,
    label = "S(693) <=> O_11_(7) + S(658)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-16.61, 1.999, -0.000945, -0.0005242],
            [19.12, 6.566e-05, 4.567e-05, 2.532e-05],
            [-0.3443, 0.0004274, 0.0002971, 0.0001647],
            [-0.06912, -5.027e-06, -3.475e-06, -1.908e-06],
            [-0.03301, 1.001e-08, 3.691e-08, 4.788e-08],
            [-0.02593, 5.338e-05, 3.711e-05, 2.056e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6332,
    label = "S(693) <=> S(694)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.616, 1.996, -0.002735, -0.001512],
            [-0.07164, 0.001949, 0.001351, 0.0007443],
            [-0.141, 0.0007353, 0.0005096, 0.0002809],
            [0.02142, -0.0005397, -0.000373, -0.0002046],
            [0.0001386, -6.322e-06, -4.589e-06, -2.72e-06],
            [-0.01257, 0.0001667, 0.0001152, 6.315e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6333,
    label = "S(694) <=> CH2O(25) + C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.415, 1.971, -0.01822, -0.008249],
            [0.08973, 0.02291, 0.01342, 0.005313],
            [-0.2504, 0.001321, 0.0006281, 0.0002055],
            [-0.06955, -0.003267, -0.001546, -0.0002903],
            [-0.009051, -0.0008487, -0.0005368, -0.0002901],
            [-0.01871, 0.0007167, 0.0002919, 1.361e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6334,
    label = "CH2(S)(28) + C4H10(685) <=> C5H12(691)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.494e+12, 'cm^3/(mol*s)'),
        n = 0.189,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/NonDeC]\nMultiplied by reaction path degeneracy 8\nEa raised from -1.5 to 0 kJ/mol.',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [carbene;Cs_H] for rate rule [carbene;C/H2/NonDeC]
Multiplied by reaction path degeneracy 8
Ea raised from -1.5 to 0 kJ/mol.
""",
)

entry(
    index = 6335,
    label = "C4H10(685) <=> CH2(S)(28) + C3H8(34)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.41, 0.9549, -0.1456, 0.01379],
            [14, 0.8957, 0.0369, -0.03513],
            [-0.7315, 0.1761, 0.07161, -7.959e-05],
            [-0.1749, -0.04905, 0.01723, 0.009462],
            [0.009348, -0.04723, -0.008343, 0.002874],
            [0.0306, -0.01057, -0.006688, -0.0009661],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6337,
    label = "C4H9(690) <=> CH2(S)(28) + C3H7(35)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.46, 1.98, -0.0136, -0.007372],
            [15.39, 0.01658, 0.01129, 0.006036],
            [-0.05259, -0.005591, -0.003762, -0.00197],
            [-0.0732, 0.002135, 0.001433, 0.0007479],
            [-0.0901, 0.001833, 0.001267, 0.000695],
            [-0.04605, 0.0005323, 0.0003677, 0.0002017],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6338,
    label = "S(692) <=> CH2(S)(28) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.97, 1.997, -0.002109, -0.001166],
            [16.19, -0.001581, -0.001094, -0.0006013],
            [0.003607, -0.0009895, -0.0006843, -0.0003759],
            [0.005712, -0.0003844, -0.0002653, -0.0001453],
            [-0.03235, 8.572e-05, 6.016e-05, 3.385e-05],
            [-0.02848, 0.0001943, 0.0001349, 7.457e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6339,
    label = "C2HO2(695) <=> CO_21_(14) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.621, 1.988, -0.00822, -0.004475],
            [-0.2207, 0.006054, 0.004096, 0.002168],
            [-0.05397, -0.002798, -0.001882, -0.0009864],
            [-0.01363, 4.5e-05, 1.48e-05, -6.638e-06],
            [-0.006379, -1.521e-06, 7.522e-07, 2.017e-06],
            [-0.003444, 4.386e-06, 3.161e-06, 1.858e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6345,
    label = "HO2_17_(5) + CH3(17) <=> CH4O2(696)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.96, 1.823, -0.1042, -0.04173],
            [-0.8822, 0.1942, 0.1082, 0.03742],
            [-0.1669, -0.02133, -0.006362, 0.003299],
            [0.01352, -0.01331, -0.008946, -0.004477],
            [0.02687, -0.0001937, -0.0008897, -0.001157],
            [0.01275, 0.0008409, 0.0005687, 0.0002811],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6359,
    label = "CH4O2(696) <=> CH2(S)(28) + H2O2(15)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.17, 1.958, -0.02838, -0.01484],
            [14, 0.04846, 0.0322, 0.01649],
            [-0.17, -0.009679, -0.006101, -0.002814],
            [0.009631, -0.002217, -0.001633, -0.0009868],
            [0.02153, 0.0004692, 0.000295, 0.0001346],
            [0.01003, 1.385e-05, 2.087e-05, 2.172e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6360,
    label = "CH4O2(696) <=> OH_12_(12) + CH3O(508)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.076, 0.9955, -0.1594, 0.005285],
            [5.153, 0.7976, 0.04204, -0.03285],
            [-0.458, 0.123, 0.06052, 0.004043],
            [-0.09153, -0.02521, 0.009112, 0.007223],
            [0.003637, -0.019, -0.005625, 0.0005722],
            [0.01252, -0.004332, -0.002692, -0.0009689],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6361,
    label = "CH4O2(696) <=> H_10_(3) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.943, 1.929, -0.04616, -0.02291],
            [11.74, 0.08333, 0.05342, 0.02556],
            [-0.1588, -0.01548, -0.008922, -0.003309],
            [0.01784, -0.004302, -0.003214, -0.001969],
            [0.02592, 0.0008126, 0.0004538, 0.0001485],
            [0.01128, 0.0002405, 0.0001958, 0.0001337],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6363,
    label = "O2_2_(13) + S(658) <=> S(697)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.79, 1.468, -0.2058, -0.02472],
            [-0.9811, 0.4736, 0.1437, -0.01038],
            [-0.2195, -0.008855, 0.02643, 0.0196],
            [-0.085, 0.007393, 0.0004162, 0.001065],
            [-0.06244, 0.01587, 0.00528, -0.0002202],
            [-0.03285, 0.0008339, 0.002305, 0.001526],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6364,
    label = "S(697) <=> O_11_(7) + S(693)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.546, 0.9302, -0.1399, 0.001961],
            [2.876, 0.8533, 0.01069, -0.02719],
            [-0.3278, 0.1415, 0.06415, 0.001781],
            [-0.102, -0.001824, 0.01993, 0.006279],
            [-0.04946, 0.005161, 0.003474, 0.001126],
            [-0.02717, 0.002806, 0.002226, 0.0005206],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6365,
    label = "O2_2_(13) + C3H7(35) <=> S(698)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.79, 1.071, -0.1988, 0.001897],
            [-0.9581, 0.6517, 0.04352, -0.04147],
            [-0.3061, 0.09856, 0.04874, -0.0004221],
            [-0.1268, 0.03588, 0.01507, 0.003778],
            [-0.06805, 0.01459, 0.009181, 0.002275],
            [-0.02716, -0.00316, 0.004734, 0.002181],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6366,
    label = "HO2_17_(5) + C3H6(38) <=> S(698)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.808, 0.6168, -0.1223, -0.0007332],
            [2.022, 0.818, -0.1001, -0.02543],
            [-0.1033, 0.2604, 0.03357, -0.02069],
            [-0.0548, 0.03818, 0.03766, -0.0009299],
            [-0.03893, 0.01077, 0.01354, 0.003407],
            [-0.02813, 0.007572, 0.006232, 0.001271],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6367,
    label = "S(698) <=> CH2(S)(28) + S(692)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10, 1.983, -0.01142, -0.006134],
            [15.95, -0.01687, -0.0114, -0.006024],
            [-0.09077, -0.003572, -0.002373, -0.001215],
            [-0.169, 0.004634, 0.003149, 0.001679],
            [-0.1023, 0.005648, 0.003783, 0.001967],
            [-0.03222, 0.003222, 0.002123, 0.00107],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6369,
    label = "O2_2_(13) + C2H3O(430) <=> S(699)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.74, 1.597, -0.1285, -0.01797],
            [-1.104, 0.4444, 0.1193, 0.004456],
            [-0.1153, -0.04151, 0.005347, 0.008324],
            [-0.01361, -0.01206, -0.00509, 6.775e-05],
            [-0.03604, 0.001105, 0.0008394, 0.0005995],
            [-0.03103, -0.0009174, 0.0004158, 0.0004822],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6370,
    label = "S(699) <=> CO_21_(14) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.608, 1.993, -0.004864, -0.002684],
            [12.01, 0.002985, 0.002063, 0.001132],
            [0.102, -0.001866, -0.001288, -0.000706],
            [-0.03067, 0.0007067, 0.0004875, 0.0002667],
            [-0.06476, 0.000716, 0.0004967, 0.0002742],
            [-0.04144, 0.0004909, 0.0003398, 0.000187],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6372,
    label = "S(566) <=> O_11_(7) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.364, 1.996, -0.002582, -0.001429],
            [8.389, -3.118e-05, -2.157e-05, -1.185e-05],
            [0.07421, -0.00127, -0.0008814, -0.0004867],
            [-0.02256, 4.063e-05, 2.807e-05, 1.54e-05],
            [-0.05762, 0.0003309, 0.0002297, 0.0001269],
            [-0.0383, 0.0003187, 0.000221, 0.0001219],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6374,
    label = "S(699) <=> HO2_17_(5) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.96, 1.919, -0.05061, -0.02305],
            [3.712, 0.09631, 0.05807, 0.02452],
            [0.06596, -0.02863, -0.01571, -0.005152],
            [-0.001468, 0.004204, 0.001718, -3.049e-05],
            [-0.04891, 0.002582, 0.001873, 0.001077],
            [-0.03645, 0.0001166, 0.0001585, 0.0001609],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6376,
    label = "C3H3O(700) <=> C2H(21) + CH2O(25)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.4772, 1.944, -0.03689, -0.0186],
            [7.269, 0.05593, 0.03613, 0.01756],
            [-0.03853, -0.01242, -0.007524, -0.00318],
            [-0.0198, 0.0004618, 9.528e-05, -0.0001443],
            [-0.02971, 0.0018, 0.001198, 0.0006137],
            [-0.01893, 0.0003636, 0.000262, 0.0001534],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6377,
    label = "C3H3O(700) <=> O_11_(7) + C3H3(19)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.022, 1.996, -0.002691, -0.001488],
            [11.57, 0.002996, 0.002077, 0.001145],
            [-0.03502, -0.001001, -0.0006927, -0.0003807],
            [-0.01881, 3.326e-05, 2.228e-05, 1.158e-05],
            [-0.02826, 0.0001222, 8.495e-05, 4.707e-05],
            [-0.01719, 4.731e-05, 3.29e-05, 1.824e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6380,
    label = "H_10_(3) + C3H2O(701) <=> C3H3O(700)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.63, 1.092, -0.1245, -0.00523],
            [0.1786, 0.7322, 0.04261, -0.01407],
            [-0.1572, 0.06295, 0.02873, 0.004455],
            [0.01678, -0.01962, 0.0002627, 0.001148],
            [0.01498, -0.002189, -0.000379, -0.0003575],
            [-0.001747, 0.002108, 0.001114, 0.0001274],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6381,
    label = "C3H2O(701) <=> CO_21_(14) + C2H2(20)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.345, 1.276, -0.2571, -0.01679],
            [9.886, 0.5137, 0.1142, -0.03827],
            [-0.2244, 0.06695, 0.05069, 0.01325],
            [-0.056, -0.01976, 0.00298, 0.009186],
            [-0.0004949, -0.01665, -0.006455, 0.001072],
            [0.005915, -0.004074, -0.003272, -0.001277],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6382,
    label = "C3H3O(702) <=> C3H3O(700)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.405, 1.853, -0.07848, -0.02472],
            [1.185, 0.1453, 0.07625, 0.02238],
            [-0.2044, 0.002455, 0.001408, 0.0008846],
            [-0.09291, 0.000963, 0.0001681, 3.804e-05],
            [-0.04661, -0.002884, -0.0009947, 0.000206],
            [-0.01072, -0.002646, -0.001079, -0.0001319],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6390,
    label = "C3H2O(701) <=> C2H(21) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.825, 1.875, -0.07842, -0.03623],
            [15.73, 0.1168, 0.07068, 0.0299],
            [-0.3227, -0.005014, -0.001019, 0.001544],
            [-0.06142, -0.008071, -0.005194, -0.002483],
            [-0.0001997, -0.002398, -0.001744, -0.001032],
            [0.003026, 0.0001963, 6.73e-05, -2.567e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6391,
    label = "CH3O2(703) <=> CH3OO(657)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.9394, 2, -0.0001265, -7.022e-05],
            [4.07, 0.0001747, 0.0001216, 6.751e-05],
            [-0.07186, -1.81e-05, -1.259e-05, -6.986e-06],
            [-0.02186, 3.877e-09, 1.696e-09, 2.44e-11],
            [-0.006033, -4.591e-07, -3.195e-07, -1.773e-07],
            [-0.001316, -1.709e-07, -1.19e-07, -6.607e-08],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6404,
    label = "CH4O2(696) <=> H_10_(3) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.804, 1.955, -0.02982, -0.0155],
            [14.08, 0.05262, 0.03485, 0.01775],
            [-0.02869, -0.01062, -0.006646, -0.003018],
            [0.05249, -0.00237, -0.00176, -0.001074],
            [0.02889, 0.0005936, 0.0003756, 0.0001737],
            [0.01476, 7.367e-05, 6.45e-05, 4.774e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6407,
    label = "CH3O2(703) <=> OH_12_(12) + CH2O(25)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.661, 1.995, -0.002957, -0.001282],
            [-0.2307, 0.007401, 0.004435, 0.001873],
            [-0.04344, -0.003264, -0.001883, -0.0007288],
            [-0.01053, 0.0007368, 0.0003851, 0.0001127],
            [-0.003604, -1.192e-05, 9.469e-06, 1.78e-05],
            [-0.001195, -2.616e-05, -1.596e-05, -6.532e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6411,
    label = "C2HO2(695) <=> O_11_(7) + HCCO(26)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-19.34, 2, -3.335e-08, -1.852e-08],
            [16.23, 4.946e-08, 3.443e-08, 1.912e-08],
            [-0.3015, -3.534e-09, -2.46e-09, -1.366e-09],
            [-0.09109, -1.169e-09, -8.136e-10, -4.518e-10],
            [-0.02813, -2.418e-10, -1.683e-10, -9.347e-11],
            [-0.008879, -2.844e-11, -1.981e-11, -1.099e-11],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6413,
    label = "C3H3O(702) <=> HCCO(26) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.057, 1.999, -0.0005362, -0.0002976],
            [10.69, -0.0001645, -0.0001144, -6.34e-05],
            [-0.2064, 2.195e-05, 1.528e-05, 8.478e-06],
            [-0.1534, 0.0001847, 0.0001285, 7.124e-05],
            [-0.07739, 0.000126, 8.759e-05, 4.856e-05],
            [-0.02024, 3.185e-05, 2.214e-05, 1.227e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6424,
    label = "O2_2_(13) + C3H5(41) <=> S(704)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.03, -0.1505, -0.06808, -0.0203],
            [-0.03059, 0.1927, 0.07878, 0.01853],
            [0.09434, -0.04818, -0.01137, 0.002007],
            [0.03751, 0.002974, -0.0008408, -0.0006894],
            [0.003783, 0.001983, 0.0005094, -9.976e-05],
            [-0.00319, -0.0009453, -0.0004893, -0.0003942],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6425,
    label = "S(704) <=> S(633)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.985, 1.073, -0.2331, -0.009651],
            [1.304, 0.5559, 0.02796, -0.04302],
            [-0.1598, 0.1013, 0.04831, 0.001393],
            [-0.09287, 0.05993, 0.02931, 0.001528],
            [-0.03358, 0.0406, 0.009835, 0.001888],
            [-0.1112, -0.05096, 0.009471, 0.006316],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6430,
    label = "O2_2_(13) + S(704) <=> S(705)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.2, 1.386, -0.1196, -0.00632],
            [-1.575, 0.6734, 0.1007, -0.00723],
            [-0.2944, -0.02003, 0.02217, 0.009345],
            [-0.03458, -0.03414, -0.004638, 0.001953],
            [-0.03475, -0.006743, -0.0004363, 0.0005554],
            [-0.02811, -0.004101, -0.0005241, 0.000243],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6463,
    label = "S(567) <=> O_11_(7) + C3H3O(706)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.344, 1.996, -0.002834, -0.001567],
            [5.6, 0.001364, 0.0009449, 0.0005207],
            [0.02998, -0.0007646, -0.0005299, -0.0002921],
            [-0.03487, 0.0002895, 0.0002004, 0.0001102],
            [-0.05612, 0.0003625, 0.0002515, 0.0001389],
            [-0.03777, 0.0002569, 0.0001782, 9.842e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6483,
    label = "H_10_(3) + C3H2O(701) <=> C3H3O(706)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.67, 1.039, -0.1608, 0.01015],
            [-0.4998, 0.739, 0.05073, -0.02715],
            [-0.3824, 0.1276, 0.05219, 0.0005122],
            [-0.1294, -0.0005669, 0.01205, 0.003787],
            [-0.03652, -0.009161, 0.0003098, 0.001268],
            [-0.008653, -0.004465, -0.0007818, 0.0003399],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6486,
    label = "OH_12_(12) + CHO2(42) <=> CH2O3(707)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.3, 0.5121, -0.1045, 0.007555],
            [-0.7274, 0.6457, -0.06643, -0.01639],
            [-0.3419, 0.2349, 0.02247, -0.01211],
            [-0.1368, 0.05522, 0.0221, 0.0006912],
            [-0.05003, 0.006241, 0.00722, 0.002907],
            [-0.01686, -0.002149, 0.0007869, 0.001167],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6491,
    label = "C3H3O(706) <=> O_11_(7) + C3H3(19)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.67, 1.998, -0.001591, -0.0008811],
            [14.11, 0.0007459, 0.0005185, 0.0002873],
            [-0.2478, 0.0005828, 0.0004047, 0.0002238],
            [-0.08765, 0.0001436, 9.968e-05, 5.513e-05],
            [-0.0273, 1.104e-05, 7.706e-06, 4.296e-06],
            [-0.007843, -1.078e-05, -7.453e-06, -4.095e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6492,
    label = "H_10_(3) + CHO3(659) <=> CH2O3(707)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.48, 0.2833, -0.06841, 0.004858],
            [-0.3852, 0.4358, -0.08466, -0.002849],
            [-0.2244, 0.2228, -0.0181, -0.01006],
            [-0.1047, 0.08219, 0.007916, -0.005531],
            [-0.04235, 0.02234, 0.008085, -0.0005402],
            [-0.01562, 0.003803, 0.003452, 0.0009227],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6495,
    label = "H_10_(3) + CH2O2(594) <=> CH3O2(703)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.129, 0.4007, -0.1553, 0.02052],
            [11.37, 0.449, -0.1392, -0.006444],
            [-0.07693, 0.1136, -0.01551, -0.01421],
            [0.003384, 0.00103, 0.006896, -0.00305],
            [0.00923, -0.006815, 0.001398, 0.0009828],
            [0.002129, 0.0001034, -0.001008, 0.0002698],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6496,
    label = "O2_2_(13) + C3H3O(706) <=> S(708)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.86, -0.1912, -0.114, -0.04691],
            [-0.4446, 0.1246, 0.07214, 0.02754],
            [-0.2803, 0.03047, 0.01973, 0.009612],
            [-0.1117, 0.02899, 0.01593, 0.00534],
            [-0.04063, 0.004906, 0.003018, 0.001353],
            [-0.01493, -0.005703, -0.002905, -0.0007222],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6497,
    label = "O2_2_(13) + C3H3O(706) <=> S(709)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.36, 1.783, -0.1274, -0.05089],
            [-0.6169, 0.1168, 0.06729, 0.02527],
            [-0.3301, 0.03795, 0.02346, 0.01046],
            [-0.2285, 0.03763, 0.02013, 0.006233],
            [-0.1035, 0.009723, 0.005469, 0.001999],
            [-0.02877, -0.004468, -0.00209, -0.0003169],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6498,
    label = "S(708) <=> S(709)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.198, 1.842, -0.0712, -0.02124],
            [0.387, 0.1295, 0.04299, 0.003169],
            [-0.233, -0.0008291, 0.004625, 0.004246],
            [-0.0765, -0.004588, 0.0009604, 0.001444],
            [0.008206, -0.005433, -0.003295, -0.001092],
            [0.0134, -0.002706, -0.002144, -0.0009014],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6499,
    label = "H_10_(3) + CO2_5_(8) <=> CHO2(710)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.641, -0.000267, -0.0001858, -0.0001032],
            [13.28, -8.926e-05, -6.212e-05, -3.448e-05],
            [0.1109, -5.973e-06, -4.155e-06, -2.304e-06],
            [0.0296, 6.181e-06, 4.301e-06, 2.388e-06],
            [0.007285, 4.948e-06, 3.443e-06, 1.911e-06],
            [0.001405, 2.674e-06, 1.86e-06, 1.032e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6500,
    label = "CHO2(710) <=> CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.562, 1.977, -0.01601, -0.008611],
            [-0.1163, 0.01799, 0.01219, 0.006464],
            [-0.1003, 0.002806, 0.001934, 0.001057],
            [0.009252, -0.002586, -0.00172, -0.0008821],
            [-0.004403, 0.0003602, 0.000231, 0.0001105],
            [-0.007373, 0.0004126, 0.0002739, 0.0001401],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6501,
    label = "CHO4(711) <=> HO2_17_(5) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.699, 1.568, -0.1511, -0.02786],
            [0.9415, 0.3845, 0.09717, -0.002526],
            [-0.1526, 0.007545, 0.02036, 0.01075],
            [-0.08751, 0.008885, 0.007864, 0.00477],
            [-0.03594, -0.002749, 0.003631, 0.00169],
            [-0.001586, -0.001384, -0.003545, -2.316e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6502,
    label = "O2_2_(13) + CHO2(42) <=> CHO4(711)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.87, 0.6846, -0.1342, 0.003716],
            [-0.7808, 0.7748, -0.05709, -0.03179],
            [-0.286, 0.2029, 0.04141, -0.01334],
            [-0.0517, 0.002682, 0.02123, 0.004362],
            [0.01539, -0.02371, -0.0003429, 0.003541],
            [0.02024, -0.01227, -0.004306, -1.224e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6503,
    label = "O_11_(7) + CHO3(659) <=> CHO4(711)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.53, 0.5184, -0.1039, 0.004682],
            [-0.6586, 0.6469, -0.06875, -0.01749],
            [-0.2967, 0.2255, 0.01655, -0.01131],
            [-0.09498, 0.04136, 0.01732, 0.0004396],
            [-0.01586, -0.006031, 0.004386, 0.002294],
            [0.006353, -0.009564, -0.0009782, 0.0007662],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6517,
    label = "OH_12_(12) + C3H3(19) <=> C3H4O(712)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.05, 0.8822, -0.2116, 0.02803],
            [-0.9379, 0.7102, 0.01752, -0.05158],
            [-0.3876, 0.1593, 0.06758, -0.007467],
            [-0.1089, -0.01228, 0.02297, 0.01018],
            [-0.01028, -0.0257, -0.002495, 0.005016],
            [0.007615, -0.007092, -0.005015, -0.0004104],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6520,
    label = "H_10_(3) + C3H3O(700) <=> C3H4O(712)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.48, 0.16, -0.04603, 0.003662],
            [-0.221, 0.2841, -0.07743, 0.003983],
            [-0.162, 0.1996, -0.04504, -0.002196],
            [-0.09733, 0.1104, -0.01526, -0.005509],
            [-0.04784, 0.04643, 0.00106, -0.004661],
            [-0.01878, 0.01271, 0.005415, -0.002059],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6528,
    label = "C3H4O(712) <=> C2H(21) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-12.16, 1.816, -0.1064, -0.04064],
            [16.85, 0.2099, 0.115, 0.03804],
            [-0.4119, -0.02294, -0.006449, 0.003901],
            [-0.06885, -0.01565, -0.01035, -0.00501],
            [0.009636, -0.001851, -0.001926, -0.001625],
            [0.007787, 0.001685, 0.0009742, 0.0003479],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6529,
    label = "CHO4(713) <=> HO2_17_(5) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.31, 1.219, -0.2093, -0.02394],
            [1.296, 0.5749, 0.05549, -0.0322],
            [-0.1862, 0.05754, 0.04887, 0.007283],
            [-0.08454, 0.02312, 0.01817, 0.005428],
            [-0.03489, 0.003401, 0.005921, 0.003088],
            [0.0008242, -0.01011, -0.002116, 0.001435],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6530,
    label = "CHO4(713) <=> CHO4(711)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.418, 1.733, -0.1535, -0.05817],
            [4.368, 0.1507, 0.07602, 0.0188],
            [0.07167, 0.02071, 0.01551, 0.008931],
            [-0.05242, 0.02935, 0.01581, 0.005052],
            [-0.02378, 0.006001, 0.004164, 0.002193],
            [0.009917, -0.006383, -0.003074, -0.0005561],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6536,
    label = "H_10_(3) + CH2O2(594) <=> CH3O2(714)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [10.13, 1.439, -0.1179, -0.01163],
            [0.5265, 0.4907, 0.07731, -0.001262],
            [-0.1197, 0.01567, 0.01229, 0.003339],
            [0.01078, -0.008649, -0.000363, 0.0002625],
            [0.003201, -0.000156, 0.0002619, 0.000222],
            [-0.002177, -0.0007197, 0.0003408, 0.0002172],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6537,
    label = "H_10_(3) + CH2O2(594) <=> CH3O2(714)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [10.11, 1.454, -0.1175, -0.01255],
            [0.5424, 0.4739, 0.07724, 2.893e-05],
            [-0.1246, 0.01878, 0.01245, 0.003105],
            [0.008821, -0.007887, -0.0004247, 0.000288],
            [0.005232, -0.001276, 0.0002672, 0.0001778],
            [-0.001452, -0.0005746, 0.0002905, 0.0001842],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6538,
    label = "OH_12_(12) + CHO3(659) <=> CH2O4(715)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.62, 0.6823, -0.1108, 0.003164],
            [-0.938, 0.8197, -0.04579, -0.02374],
            [-0.3899, 0.2321, 0.04486, -0.009203],
            [-0.09748, 0.008795, 0.02307, 0.005369],
            [0.00231, -0.02435, -6.795e-05, 0.003458],
            [0.01993, -0.01305, -0.004218, -0.0002261],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6540,
    label = "HO2_17_(5) + CHO2(42) <=> CH2O4(715)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.46, 0.2874, -0.07279, 0.003831],
            [-0.4088, 0.4661, -0.1016, -0.002733],
            [-0.2413, 0.2601, -0.03108, -0.01244],
            [-0.113, 0.1018, 0.006342, -0.009456],
            [-0.04178, 0.0251, 0.01156, -0.002466],
            [-0.01131, -3.42e-05, 0.006096, 0.001115],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6541,
    label = "H_10_(3) + CHO4(713) <=> CH2O4(715)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.58, 0.172, -0.04703, 0.003325],
            [-0.2395, 0.3, -0.07662, 0.00287],
            [-0.1682, 0.1998, -0.03997, -0.003477],
            [-0.09501, 0.1016, -0.009806, -0.005809],
            [-0.04364, 0.03822, 0.003567, -0.003861],
            [-0.01629, 0.009063, 0.005118, -0.001064],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6542,
    label = "H_10_(3) + CHO4(711) <=> CH2O4(715)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.45, 0.1869, -0.05105, 0.003426],
            [-0.2574, 0.323, -0.08199, 0.002483],
            [-0.1769, 0.2099, -0.04083, -0.004451],
            [-0.09641, 0.1023, -0.008488, -0.006468],
            [-0.04186, 0.03561, 0.004675, -0.003886],
            [-0.01408, 0.006565, 0.005425, -0.0008051],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6544,
    label = "C2HO3(716) <=> CO_21_(14) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.399, 1.879, -0.06624, -0.02639],
            [0.1645, 0.1154, 0.0551, 0.01645],
            [-0.1911, -0.01345, -0.001551, 0.002953],
            [-0.01863, -0.006006, -0.00379, -0.001601],
            [0.01939, -0.002656, -0.002155, -0.001295],
            [-0.003737, 0.002521, 0.001292, 0.0004021],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6546,
    label = "CO2_5_(8) + HCO(22) <=> C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.15, 0.3551, -0.1411, -0.02636],
            [10.06, 0.6668, -0.08302, -0.005966],
            [-0.1552, 0.2784, -0.000674, -0.01559],
            [-0.08666, 0.05878, 0.024, -0.003248],
            [-0.02153, -0.009425, 0.01092, 0.003492],
            [0.0009963, -0.01305, -3.241e-05, 0.002443],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6547,
    label = "CO2_5_(8) + OH_12_(12) <=> CHO3(717)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.088, -0.003458, -0.002403, -0.001331],
            [13.76, 0.00112, 0.0007772, 0.0004294],
            [0.189, 0.0003178, 0.0002207, 0.000122],
            [0.05116, -0.0002559, -0.0001774, -9.785e-05],
            [0.01564, 0.0001004, 6.961e-05, 3.838e-05],
            [0.00546, 1.236e-06, 8.505e-07, 4.633e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6548,
    label = "CHO3(717) <=> CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.513, 1.807, -0.1103, -0.04261],
            [-0.2306, 0.1671, 0.0871, 0.02616],
            [-0.1221, 0.0003164, 0.005548, 0.006435],
            [-0.06562, -0.003839, -0.001829, -0.0001574],
            [-0.03396, -0.000947, -0.0007409, -0.0004282],
            [-0.01565, -5.575e-05, -0.0001082, -0.0001212],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6549,
    label = "O2_2_(13) + HCO(22) <=> CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.942, -0.08605, -0.04374, -0.01527],
            [0.8525, 0.1229, 0.05964, 0.01916],
            [0.312, -0.04347, -0.01731, -0.00365],
            [0.0862, 0.002736, -0.001858, -0.001704],
            [0.02068, 0.001549, 0.001969, 0.0005161],
            [0.003581, 0.001015, -8.829e-05, 0.0002211],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6550,
    label = "CHO3(718) <=> CO2_5_(8) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.666, 1.99, -0.005669, -0.002229],
            [-0.2273, 0.0137, 0.007539, 0.002778],
            [-0.04446, -0.004395, -0.002211, -0.0006312],
            [-0.01059, 0.0003366, 9.529e-05, -4.415e-05],
            [-0.003455, 0.0001469, 7.878e-05, 2.762e-05],
            [-0.001193, -4.953e-06, 3.293e-06, 6.311e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6554,
    label = "CHO4(713) <=> O_11_(7) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-14.95, 1.966, -0.02346, -0.01265],
            [18.14, 0.004284, 0.002933, 0.001583],
            [-0.199, 0.005383, 0.003639, 0.001923],
            [-0.1458, 0.008151, 0.005483, 0.002871],
            [-0.0526, 0.002676, 0.001801, 0.0009437],
            [0.003859, -0.001257, -0.0008346, -0.0004267],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6555,
    label = "O_11_(7) + CHO2(424) <=> CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.23, -0.006329, -0.004382, -0.002412],
            [0.5712, 0.007125, 0.004924, 0.002702],
            [0.2075, -0.001934, -0.00133, -0.0007234],
            [0.05836, -0.00011, -8.047e-05, -4.826e-05],
            [0.01722, 3.042e-05, 2.143e-05, 1.213e-05],
            [0.00564, 2.346e-05, 1.635e-05, 9.102e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6556,
    label = "OH_12_(12) + CHO3(718) <=> CH2O4(715)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.68, 0.137, -0.04573, 0.005062],
            [-0.224, 0.2444, -0.07815, 0.00669],
            [-0.1399, 0.1735, -0.04787, -0.0001853],
            [-0.08123, 0.09785, -0.01881, -0.004764],
            [-0.03981, 0.04299, -0.001747, -0.005023],
            [-0.01616, 0.01374, 0.0038, -0.002866],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6557,
    label = "CHO3(718) <=> HO2_17_(5) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.005, 1.97, -0.01906, -0.008913],
            [-1.311, 0.02868, 0.01803, 0.008308],
            [-0.3434, 0.001097, 0.0007307, 0.0003782],
            [-0.0766, -0.00104, -0.000626, -0.0002627],
            [-0.0177, -0.0005267, -0.0003271, -0.0001472],
            [-0.004829, -0.0001157, -7.599e-05, -3.808e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6559,
    label = "CH3O2(703) <=> CH3O2(719)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.6348, 2, -0.0001542, -8.56e-05],
            [2.926, 0.0002177, 0.0001515, 8.411e-05],
            [-0.1182, -2.391e-05, -1.663e-05, -9.225e-06],
            [-0.03374, -2.634e-07, -1.849e-07, -1.042e-07],
            [-0.009374, -5.935e-07, -4.13e-07, -2.292e-07],
            [-0.002323, -2.003e-07, -1.394e-07, -7.743e-08],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6564,
    label = "CH3O2(719) <=> H_10_(3) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.112, 1.818, -0.06404, -0.01601],
            [0.5114, 0.1668, 0.0469, 0.006567],
            [-0.1382, 0.0112, 0.009871, 0.004814],
            [-0.0767, -0.001255, 0.002431, 0.001187],
            [-0.01458, -0.004845, -0.001494, -8.772e-05],
            [0.01101, -0.00327, -0.001688, -0.0003785],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6565,
    label = "CH3O2(719) <=> CH3O2(714)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.159, 1.997, -0.001914, -0.001059],
            [5.354, -0.00157, -0.001089, -0.0006006],
            [0.02761, 0.0005925, 0.0004113, 0.0002274],
            [-0.05542, 0.0008205, 0.0005685, 0.0003132],
            [-0.004623, 0.0002469, 0.0001706, 9.362e-05],
            [0.01726, -0.0001347, -9.345e-05, -5.158e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6566,
    label = "OH_12_(12) + CH2O(25) <=> CH3O2(719)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.157, 0.3379, -0.08725, 0.00463],
            [4.118, 0.5205, -0.1119, -0.005345],
            [0.003832, 0.2518, -0.02411, -0.01502],
            [-0.02458, 0.07201, 0.01231, -0.008337],
            [-0.0004947, 0.003308, 0.01117, -0.0003058],
            [0.007256, -0.008548, 0.003036, 0.001913],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6567,
    label = "CH3O2(719) <=> O_11_(7) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.32, 2, -0.0003467, -0.0001924],
            [14.52, -0.0005107, -0.0003553, -0.0001971],
            [-0.1418, -7.172e-05, -4.987e-05, -2.764e-05],
            [-0.1154, 8.734e-05, 6.077e-05, 3.372e-05],
            [-0.02878, 5.633e-05, 3.918e-05, 2.173e-05],
            [0.007301, -2.756e-06, -1.924e-06, -1.074e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6568,
    label = "O2_2_(13) + HCO(22) <=> CHO3(720)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.691, -0.07825, -0.04337, -0.01665],
            [0.5588, 0.107, 0.05722, 0.02039],
            [0.1607, -0.03278, -0.01524, -0.003775],
            [0.03985, -0.001544, -0.002125, -0.001579],
            [0.01226, 0.003555, 0.001744, 0.0003953],
            [0.0008775, -0.001087, -0.0002252, 0.0002088],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6569,
    label = "O_11_(7) + CHO2(424) <=> CHO3(720)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.68, -0.006609, -0.004576, -0.002519],
            [0.2192, 0.00723, 0.004996, 0.00274],
            [0.1074, -0.00195, -0.00134, -0.0007289],
            [0.005618, -0.000151, -0.0001089, -6.397e-05],
            [0.01916, 2.261e-05, 1.592e-05, 9.008e-06],
            [-0.008511, 1.773e-05, 1.24e-05, 6.933e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6570,
    label = "CHO3(720) <=> CHO3(717)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.017, 1.993, -0.004751, -0.00262],
            [5.659, 0.004928, 0.00341, 0.001874],
            [-0.09458, 0.0003566, 0.0002503, 0.0001409],
            [-0.03269, 7.989e-07, 1.028e-06, 1.002e-06],
            [-0.01099, -1.879e-05, -1.299e-05, -7.139e-06],
            [-0.003461, -1.452e-05, -1.006e-05, -5.542e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6571,
    label = "C2HO3(721) <=> CO2_5_(8) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.635, 1.979, -0.01425, -0.007719],
            [-0.2423, -0.004232, -0.002858, -0.001508],
            [-0.04391, -0.001815, -0.00123, -0.0006532],
            [-0.01265, -2.959e-05, -2.285e-05, -1.469e-05],
            [-0.004611, 0.0003208, 0.0002128, 0.0001087],
            [-0.001853, 0.000288, 0.0001912, 9.773e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6573,
    label = "C2HO3(721) <=> CO_21_(14) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.107, 1.846, -0.0972, -0.04524],
            [10.14, 0.09673, 0.05707, 0.02268],
            [-0.01274, 0.006276, 0.005566, 0.004074],
            [-0.01745, 0.003637, 0.002425, 0.001264],
            [-0.01084, 0.001764, 0.001199, 0.0006385],
            [-0.005606, 0.0006176, 0.0004396, 0.0002524],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6574,
    label = "C2HO3(721) <=> CO_21_(14) + CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.042, 1.964, -0.02482, -0.0133],
            [1.294, 0.006254, 0.004222, 0.002225],
            [-0.04476, -0.002293, -0.001537, -0.0008002],
            [-0.01531, 0.0003812, 0.0002426, 0.0001141],
            [-0.008343, 0.0005615, 0.0003709, 0.000188],
            [-0.004505, 0.0004036, 0.0002668, 0.0001354],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6585,
    label = "CHO3(720) <=> O_11_(7) + CHO2(710)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.693, 1.998, -0.001269, -0.0007037],
            [14.03, 0.001144, 0.0007948, 0.0004402],
            [-0.05457, 9.845e-05, 6.862e-05, 3.819e-05],
            [-0.002989, 1.368e-05, 9.538e-06, 5.313e-06],
            [0.02138, 1.213e-06, 8.483e-07, 4.75e-07],
            [0.01806, -9.816e-07, -6.811e-07, -3.763e-07],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6586,
    label = "O2_2_(13) + HCO(22) <=> CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.6, 1.728, -0.1097, -0.02306],
            [-1.079, 0.2765, 0.09684, 0.01422],
            [-0.146, -0.03048, 0.003469, 0.004621],
            [0.01905, -0.0003959, -0.007834, -0.001504],
            [0.03142, -0.008001, 0.002209, -1.381e-05],
            [0.003278, 0.007409, -0.001733, -0.0002302],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6587,
    label = "CO2_5_(8) + OH_12_(12) <=> CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.07, -0.0002704, -0.0001882, -0.0001045],
            [14.75, 0.000151, 0.0001051, 5.834e-05],
            [0.3362, 3.361e-05, 2.339e-05, 1.299e-05],
            [0.0885, 6.852e-07, 4.783e-07, 2.667e-07],
            [0.02797, -2.185e-06, -1.52e-06, -8.436e-07],
            [0.009576, -6.826e-07, -4.751e-07, -2.638e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6589,
    label = "O_11_(7) + CHO2(424) <=> CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.517, 1.993, -0.00509, -0.0028],
            [-0.5654, 0.007665, 0.005293, 0.0029],
            [0.007326, -0.00199, -0.001367, -0.0007417],
            [0.05826, -0.000216, -0.0001542, -8.912e-05],
            [0.02753, -1.543e-07, 4.772e-08, 1.651e-07],
            [0.004594, 2.259e-05, 1.573e-05, 8.741e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6590,
    label = "CHO3(718) <=> CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.2156, 2, -0.0001958, -0.0001087],
            [4.481, 0.0001491, 0.0001038, 5.759e-05],
            [0.09676, 3.56e-05, 2.477e-05, 1.375e-05],
            [0.02356, 1.544e-06, 1.076e-06, 5.985e-07],
            [0.009037, -2.056e-06, -1.43e-06, -7.935e-07],
            [0.003538, -7.012e-07, -4.88e-07, -2.709e-07],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6591,
    label = "CHO3(720) <=> CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.622, 1.907, -0.05344, -0.02177],
            [-0.1653, 0.1043, 0.05608, 0.02013],
            [-0.05122, -0.01363, -0.003608, 0.001276],
            [-0.01424, -0.002116, -0.002287, -0.001318],
            [-0.003121, -0.0003345, -0.0002733, -0.0002588],
            [-0.0005977, -0.0003296, 7.524e-05, 9.046e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6592,
    label = "CHO3(722) <=> HO2_17_(5) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.321, 1.997, -0.002151, -0.00119],
            [10.78, 0.002785, 0.001932, 0.001067],
            [0.02097, -0.0007341, -0.0005084, -0.00028],
            [0.06148, -0.0001483, -0.0001036, -5.785e-05],
            [0.02865, -2.497e-05, -1.737e-05, -9.631e-06],
            [0.004866, 1.583e-06, 1.11e-06, 6.238e-07],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6596,
    label = "CH3O3(723) <=> H_10_(3) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.355, 1.591, -0.1176, -0.01654],
            [0.3119, 0.488, 0.1195, 0.008552],
            [-0.1802, -0.03816, 0.0142, 0.00998],
            [-0.009574, -0.04909, -0.0139, -3.611e-05],
            [-0.008703, 0.004729, -0.003762, -0.002109],
            [0.001146, 0.001342, 9.557e-05, -0.0004573],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6597,
    label = "C2HO4(724) <=> CO2_5_(8) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.675, 1.979, -0.0146, -0.007875],
            [-0.2485, -0.009924, -0.006702, -0.003535],
            [-0.04365, -0.002625, -0.001763, -0.0009212],
            [-0.01242, -0.0001019, -6.801e-05, -3.511e-05],
            [-0.004355, 0.0003969, 0.0002624, 0.0001331],
            [-0.001738, 0.0003439, 0.0002261, 0.0001135],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6598,
    label = "CO2_5_(8) + CHO2(424) <=> C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.8983, 0.1876, -0.2128, -0.04983],
            [7.085, 0.6899, -0.05917, 0.01344],
            [-0.1025, 0.254, -0.02064, -0.01315],
            [-0.05048, 0.05114, 0.01666, -0.00717],
            [-0.006516, -0.009444, 0.01056, 0.001416],
            [0.001125, -0.008264, 0.0002697, 0.002181],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6599,
    label = "C2HO4(724) <=> CO_21_(14) + CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.137, 1.967, -0.02225, -0.01193],
            [0.891, -0.00324, -0.002137, -0.00108],
            [-0.05327, -0.002572, -0.001729, -0.0009041],
            [-0.01137, 0.0002186, 0.0001395, 6.612e-05],
            [-0.005673, 0.0005681, 0.0003724, 0.000186],
            [-0.002851, 0.0004209, 0.0002751, 0.0001367],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6601,
    label = "H_10_(3) + C2O2(725) <=> C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.798, 1.987, -0.008972, -0.004728],
            [-1.794, 0.01424, 0.009537, 0.00496],
            [-0.4643, -0.00183, -0.001168, -0.0005537],
            [-0.1238, -0.0001341, -0.000102, -6.432e-05],
            [-0.03272, -1.618e-05, -1.152e-05, -6.65e-06],
            [-0.008238, -1.882e-06, -1.378e-06, -8.176e-07],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6603,
    label = "OH_12_(12) + C2O2(725) <=> C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.674, 1.495, -0.09077, -0.005123],
            [-2.184, 0.4578, 0.07078, 0.001969],
            [-0.6791, -0.004284, 0.006212, 0.002038],
            [-0.1899, -0.006855, -0.001389, -0.0001929],
            [-0.05152, -0.001621, -0.0002318, -4.224e-05],
            [-0.0117, -0.00075, -9.443e-05, -2.127e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6610,
    label = "HO2_17_(5) + CO2_5_(8) <=> CHO4(726)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.127, -0.01825, -0.01257, -0.006864],
            [9.674, -0.003723, -0.002525, -0.001342],
            [0.2834, 0.001828, 0.00125, 0.0006744],
            [0.07721, 0.004629, 0.003154, 0.001689],
            [0.02916, 0.002284, 0.00155, 0.000825],
            [0.01243, -0.0002822, -0.0001921, -0.0001027],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6611,
    label = "CHO4(726) <=> CHO4(711)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.691, 1.903, -0.05347, -0.02019],
            [-0.1677, 0.113, 0.05894, 0.01966],
            [-0.05176, -0.01384, -0.003801, 0.001354],
            [-0.01354, -0.005011, -0.003211, -0.001423],
            [-0.003502, -0.0001183, -0.00045, -0.0004502],
            [-0.001105, 0.0002376, 0.0001129, 4.665e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6614,
    label = "CHO4(726) <=> O_11_(7) + CHO3(717)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.525, 2, -0.000281, -0.000156],
            [13.71, 0.0001622, 0.0001129, 6.263e-05],
            [-0.2205, 7.592e-05, 5.283e-05, 2.932e-05],
            [-0.07776, 1.094e-05, 7.613e-06, 4.227e-06],
            [-0.02106, -2.213e-07, -1.527e-07, -8.36e-08],
            [-0.003953, -7.664e-07, -5.331e-07, -2.956e-07],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6615,
    label = "OH_12_(12) + CHO2(424) <=> CH2O3(727)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.3, 1.471, -0.1359, -0.01243],
            [-1.574, 0.5156, 0.1109, 0.00156],
            [-0.4191, 0.002743, 0.01759, 0.007816],
            [-0.05271, -0.02271, -0.005445, -0.0001804],
            [0.02394, -0.006988, -0.002655, -0.0006931],
            [0.02043, -0.0001489, -0.0003549, -0.0001482],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6619,
    label = "CH2O3(727) <=> CO_21_(14) + H2O2(15)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-4.047, 1.989, -0.007487, -0.00407],
            [8.996, 0.01468, 0.01007, 0.005451],
            [-0.05719, -0.004206, -0.002851, -0.001513],
            [0.05553, -3.386e-05, -4.488e-05, -4.426e-05],
            [0.04986, 0.0001125, 8.004e-05, 4.601e-05],
            [0.02369, 4.476e-05, 3.151e-05, 1.782e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6620,
    label = "HO2_17_(5) + HCO(22) <=> CH2O3(727)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.81, 0.8004, -0.1554, 0.01001],
            [-0.8918, 0.6913, 0.00304, -0.02898],
            [-0.3883, 0.1913, 0.04495, -0.003161],
            [-0.1434, 0.02951, 0.01872, 0.004666],
            [-0.04356, -0.005073, 0.002961, 0.002334],
            [-0.00849, -0.006588, -0.001068, 0.0002886],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6634,
    label = "CH2O3(727) <=> H_10_(3) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.62, 1.998, -0.001062, -0.0005887],
            [13.92, 0.001798, 0.00125, 0.000692],
            [-0.1182, -0.0003867, -0.0002683, -0.0001482],
            [0.02464, -5.46e-05, -3.817e-05, -2.135e-05],
            [0.03774, -5.955e-06, -4.145e-06, -2.302e-06],
            [0.01931, 4.045e-06, 2.816e-06, 1.564e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6635,
    label = "CH2O3(727) <=> H_10_(3) + CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.33, 1.998, -0.001153, -0.0006389],
            [13.35, 0.001969, 0.001368, 0.0007577],
            [-0.1072, -0.0004295, -0.0002979, -0.0001645],
            [0.02803, -5.776e-05, -4.041e-05, -2.263e-05],
            [0.03671, -4.935e-06, -3.435e-06, -1.907e-06],
            [0.01843, 4.834e-06, 3.366e-06, 1.869e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6636,
    label = "CO2_5_(8) + HCO(22) <=> C2HO3(728)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-0.4588, -0.0913, -0.06034, -0.03061],
            [8.543, 0.04209, 0.02666, 0.01244],
            [0.1113, -0.001456, -0.0006125, 1.357e-05],
            [0.01517, 0.001625, 0.001002, 0.0004422],
            [-0.002943, 0.001384, 0.0009014, 0.0004441],
            [-0.004457, 0.0008059, 0.0005312, 0.0002679],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6637,
    label = "CO2_5_(8) + HCO(22) <=> C2HO3(728)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-3.184, 1.846, -0.09449, -0.04292],
            [8.275, 0.09663, 0.05443, 0.02068],
            [-0.02438, 0.003993, 0.00275, 0.002078],
            [-0.03231, -0.003061, -0.0004425, 0.0007398],
            [0.008516, -0.003, -0.00149, -0.0004994],
            [0.01588, -0.001329, -0.000972, -0.000517],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6638,
    label = "C2HO3(728) <=> C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.276, 1.925, -0.04738, -0.02231],
            [0.02377, 0.06387, 0.03994, 0.0182],
            [-0.2995, 0.01364, 0.008448, 0.003812],
            [-0.1072, -0.004014, -0.002054, -0.000501],
            [-0.009742, -0.005361, -0.003165, -0.001277],
            [0.0006691, -0.0006825, -0.0005559, -0.0003771],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6645,
    label = "CO2_5_(8) + CHO2(42) <=> C2HO4(729)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.069, 0.4543, -0.2021, -0.03972],
            [8.892, 0.8065, -0.04729, -0.006268],
            [-0.1157, 0.2143, 0.02149, -0.01423],
            [-0.03157, 0.01414, 0.02252, 0.001809],
            [-0.005646, -0.008343, 0.003666, 0.003221],
            [-0.005941, 0.000898, -0.0007565, 0.0002264],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6646,
    label = "C2HO4(729) <=> CO2_5_(8) + CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.635, 1.916, -0.05548, -0.02821],
            [-0.2313, 0.03118, 0.01971, 0.009164],
            [-0.04815, 0.0007738, 0.0006484, 0.0004539],
            [-0.01575, 0.002215, 0.001427, 0.0006891],
            [-0.007243, 0.001268, 0.0008276, 0.0004097],
            [-0.003692, 0.0006782, 0.0004443, 0.0002215],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6647,
    label = "C2HO4(729) <=> C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.233, 1.811, -0.116, -0.05109],
            [4.845, 0.1215, 0.06843, 0.02406],
            [0.04263, 0.005889, 0.006253, 0.005178],
            [-0.01058, 0.005104, 0.003254, 0.00158],
            [-0.01517, 0.002574, 0.001728, 0.000897],
            [-0.009275, 0.0006801, 0.0005188, 0.0003273],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6648,
    label = "C2HO4(729) <=> CO_21_(14) + CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.7235, 1.778, -0.1324, -0.05453],
            [7.782, 0.1601, 0.08652, 0.02694],
            [0.07765, 0.009954, 0.01037, 0.008344],
            [0.005256, 0.00385, 0.002769, 0.001699],
            [-0.00402, 0.001222, 0.0008859, 0.0005205],
            [-0.002473, -4.023e-05, 3.467e-05, 7.466e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6652,
    label = "C2HO4(729) <=> O_11_(7) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.841, 1.849, -0.09415, -0.04277],
            [14.74, 0.1232, 0.07287, 0.0292],
            [-0.2163, 0.00686, 0.006741, 0.005368],
            [-0.07392, -0.001018, -0.0003572, 0.000136],
            [-0.02783, -0.0006094, -0.00042, -0.0002256],
            [-0.01114, -0.0002358, -0.0001728, -0.0001038],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6655,
    label = "H_10_(3) + C2O4(730) <=> C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.47, 0.5136, -0.1308, -0.002705],
            [1.109, 0.6145, -0.1123, -0.02297],
            [-0.2359, 0.1424, 0.002145, -0.01292],
            [-0.06529, -0.0008135, 0.008787, 0.0005444],
            [-0.0177, 0.0008707, -0.0002817, 0.0008966],
            [-0.01187, 0.007333, -6.679e-05, -0.0007627],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6659,
    label = "CH3O3(731) <=> H_10_(3) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.772, 0.5131, -0.1635, 0.02114],
            [1.27, 0.6148, -0.1201, -0.02312],
            [-0.04794, 0.2691, -0.0008796, -0.02989],
            [-0.04991, 0.08548, 0.03134, -0.01459],
            [-0.009449, 0.02029, 0.02377, -0.002546],
            [-0.002873, 0.00993, 0.008884, 0.00188],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6660,
    label = "CH3O3(731) <=> CH3O3(723)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.603, 1.064, -0.2896, 0.004526],
            [5.532, 0.4427, 0.06935, -0.04742],
            [-0.2946, 0.2313, 0.0508, -0.0178],
            [-0.1167, 0.04738, 0.03324, 0.005226],
            [-0.0421, -0.001819, 0.01348, 0.007263],
            [-0.02476, 0.004815, 0.001914, 0.002255],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6661,
    label = "CH3O3(731) <=> OH_12_(12) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.958, 0.9115, -0.2753, 0.02329],
            [4.74, 0.4972, 0.03021, -0.05752],
            [-0.02168, 0.2484, 0.04122, -0.02348],
            [-0.03405, 0.06209, 0.03738, 0.0003261],
            [-0.002235, 0.0061, 0.01817, 0.005798],
            [-0.002797, 0.007145, 0.003385, 0.002889],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6666,
    label = "CH3O3(731) <=> O_11_(7) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.884, 1.801, -0.1212, -0.05216],
            [13.97, 0.09826, 0.05685, 0.02156],
            [-0.2177, 0.05985, 0.03438, 0.01285],
            [-0.06778, 0.01013, 0.00711, 0.003945],
            [0.0189, -0.0104, -0.004658, -0.0004267],
            [0.009975, -0.001577, -0.0008613, -0.0002576],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6667,
    label = "CO_21_(14) + CHO2(42) <=> C2HO3(732)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.7088, -0.1084, -0.07091, -0.03531],
            [8.471, 0.04609, 0.02917, 0.01358],
            [0.06408, 0.02825, 0.0179, 0.008363],
            [-0.05361, 0.0028, 0.002129, 0.001336],
            [-0.05255, -0.005123, -0.002955, -0.001099],
            [-0.02607, 0.0009641, 0.0005576, 0.0002107],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6668,
    label = "C2HO3(732) <=> CO2_5_(8) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.672, 1.981, -0.013, -0.007045],
            [-0.2578, -0.00843, -0.005708, -0.003024],
            [-0.05416, -0.002449, -0.001665, -0.0008882],
            [-0.01935, 0.0004489, 0.0002923, 0.0001441],
            [-0.009164, 0.001003, 0.0006649, 0.0003393],
            [-0.004597, 0.0007976, 0.0005298, 0.0002712],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6669,
    label = "C2HO3(732) <=> C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.493, 1.921, -0.05293, -0.02727],
            [4.779, 0.0278, 0.0179, 0.008626],
            [0.007527, 0.006829, 0.004527, 0.002308],
            [-0.03044, 0.005541, 0.003648, 0.001837],
            [-0.02443, 0.002653, 0.001789, 0.0009408],
            [-0.01238, 0.0007492, 0.0005312, 0.0003033],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6670,
    label = "C2HO3(728) <=> C2HO3(732)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.565, 1.974, -0.01762, -0.00946],
            [1.283, 0.01626, 0.01106, 0.005909],
            [-0.2883, 0.008884, 0.006014, 0.003185],
            [-0.1101, 0.0003397, 0.0002561, 0.0001599],
            [-0.003948, -0.002683, -0.00179, -0.0009239],
            [0.004462, -0.0008572, -0.0005813, -0.0003089],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6674,
    label = "H_10_(3) + CO3(733) <=> CHO3(717)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.969, 1.379, -0.1069, -0.008847],
            [0.7042, 0.5519, 0.0702, -0.00142],
            [-0.08139, 0.006822, 0.01177, 0.003511],
            [0.03284, -0.01113, -0.001556, -4.103e-05],
            [0.01662, -0.0008252, 0.0001273, 2.123e-05],
            [0.002979, -0.0003174, 0.0002736, 0.0001009],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6675,
    label = "H_10_(3) + CO3(733) <=> CHO3(720)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.817, 0.6585, -0.1773, 0.004405],
            [1.965, 0.5569, -0.07465, -0.03217],
            [-0.0418, 0.09293, 0.01014, -0.009685],
            [0.01891, -0.009324, 0.004394, 0.001101],
            [0.008048, -0.002846, -0.0004635, 0.0001127],
            [-0.007393, 0.01086, -0.00122, -0.001074],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6676,
    label = "CHO4(726) <=> OH_12_(12) + CO3(733)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.921, 1.996, -0.003059, -0.00169],
            [4.551, 0.003269, 0.002266, 0.00125],
            [-0.002179, 0.0006623, 0.0004602, 0.0002548],
            [-0.009092, -0.0001069, -7.352e-05, -3.999e-05],
            [-0.0038, -6.556e-05, -4.543e-05, -2.504e-05],
            [-0.00138, -1.443e-05, -1.007e-05, -5.617e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6683,
    label = "C2HO3(732) <=> O_11_(7) + C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.093, 1.908, -0.06015, -0.03005],
            [13.08, 0.06973, 0.04426, 0.02074],
            [-0.1834, 0.004017, 0.003391, 0.0024],
            [-0.04594, -0.00011, 7.665e-06, 8.293e-05],
            [-0.009106, -0.0001775, -0.0001185, -6.079e-05],
            [-0.000439, -9.22e-05, -6.404e-05, -3.541e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6684,
    label = "C3H3O(702) <=> O(734) + C3H3(19)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-15.5, 2, -0.0001311, -7.279e-05],
            [17.88, -0.0001243, -8.647e-05, -4.799e-05],
            [-0.08526, -5.182e-06, -3.604e-06, -1.998e-06],
            [-0.1123, 4.713e-05, 3.28e-05, 1.82e-05],
            [-0.06231, 3.958e-05, 2.754e-05, 1.528e-05],
            [-0.01484, 1.36e-05, 9.462e-06, 5.25e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6685,
    label = "CHO3(720) <=> CHO2(424) + O(734)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.802, 1.997, -0.002336, -0.001293],
            [9.704, 0.002219, 0.00154, 0.0008511],
            [-0.09249, 0.0002114, 0.0001475, 8.217e-05],
            [-0.01107, 9.422e-06, 6.675e-06, 3.813e-06],
            [-0.009565, -2.877e-06, -1.984e-06, -1.085e-06],
            [-0.01137, -1.846e-07, -1.32e-07, -7.64e-08],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6686,
    label = "CHO4(726) <=> CHO3(659) + O(734)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.7139, 1.998, -0.001271, -0.0007045],
            [7.083, 0.0009601, 0.0006673, 0.0003697],
            [-0.1493, 0.0003573, 0.0002484, 0.0001377],
            [-0.04867, 2.073e-05, 1.449e-05, 8.1e-06],
            [-0.01635, -1.399e-05, -9.7e-06, -5.349e-06],
            [-0.005557, -6.344e-06, -4.409e-06, -2.442e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6687,
    label = "C2HO3(728) <=> C2HO2(695) + O(734)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-17.57, 2, -0.0001058, -5.874e-05],
            [18.09, 2.797e-05, 1.947e-05, 1.081e-05],
            [-0.2469, 6.452e-05, 4.49e-05, 2.493e-05],
            [-0.07599, 1.676e-05, 1.166e-05, 6.474e-06],
            [0.01011, -1.481e-05, -1.03e-05, -5.719e-06],
            [0.008119, -8.232e-06, -5.729e-06, -3.18e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6688,
    label = "CO2_5_(8) + O(734) <=> CO3(733)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.09, 1.03, -0.187, -0.0004113],
            [-0.7492, 0.528, 0.04662, -0.0232],
            [-0.2405, 0.09688, 0.03218, 0.001602],
            [-0.0674, 0.01358, 0.004914, 0.002982],
            [-0.009737, -0.00489, 0.001125, 2.683e-05],
            [0.002025, -0.002019, -0.001217, 0.0001803],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6690,
    label = "CO2_5_(8) + CHO2(42) <=> C2HO4(735)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-2.26, -0.1403, -0.08966, -0.04269],
            [9.862, 0.07429, 0.04429, 0.01806],
            [0.1094, -0.001392, 0.0001858, 0.001085],
            [0.00701, 0.002854, 0.001675, 0.0006644],
            [-0.005446, 0.001991, 0.00128, 0.0006133],
            [-0.004279, 0.0008628, 0.0005772, 0.0002988],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6691,
    label = "CO2_5_(8) + CHO2(42) <=> C2HO4(735)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-4.832, 1.899, -0.06512, -0.03148],
            [9.152, 0.05848, 0.03535, 0.01495],
            [0.05656, -0.01288, -0.00726, -0.002572],
            [0.02388, -0.0004684, -0.0006443, -0.000616],
            [0.0007722, 0.001285, 0.0008647, 0.0004478],
            [-0.004625, 0.00067, 0.0004804, 0.0002791],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6692,
    label = "C2HO4(735) <=> C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.476, 1.96, -0.02591, -0.01272],
            [-0.2278, 0.0469, 0.02976, 0.01404],
            [-0.05316, -0.008149, -0.00452, -0.001533],
            [-0.01283, -0.0008791, -0.0007683, -0.0005503],
            [-0.004028, 0.0001927, 9.32e-05, 1.469e-05],
            [-0.001428, 4.16e-05, 3.871e-05, 2.909e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6693,
    label = "C2HO4(735) <=> C2HO3(716) + O(734)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-13.38, 1.999, -0.0008057, -0.0004469],
            [15.63, 0.0007039, 0.0004895, 0.0002714],
            [-0.1366, 8.962e-05, 6.239e-05, 3.466e-05],
            [-0.0625, 6.243e-06, 4.36e-06, 2.434e-06],
            [-0.0208, -3.467e-07, -2.386e-07, -1.3e-07],
            [-0.005263, -3.655e-07, -2.541e-07, -1.408e-07],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6694,
    label = "C2HO4(736) <=> CO2_5_(8) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.728, 1.988, -0.008608, -0.004714],
            [-0.2485, -0.007911, -0.005418, -0.002927],
            [-0.04362, -0.003595, -0.00245, -0.001313],
            [-0.01181, -0.0007348, -0.0004918, -0.0002552],
            [-0.003842, 0.0003062, 0.0002146, 0.0001205],
            [-0.001328, 0.0004727, 0.0003237, 0.0001749],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6695,
    label = "C2HO4(735) <=> C2HO4(736)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.421, 1.962, -0.02489, -0.01234],
            [-0.1993, 0.04473, 0.02856, 0.01363],
            [-0.03904, -0.007723, -0.004336, -0.001522],
            [-0.009255, -0.0008081, -0.0007138, -0.000517],
            [-0.002932, 0.0001644, 8.231e-05, 1.61e-05],
            [-0.001082, 3.729e-05, 3.486e-05, 2.641e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6696,
    label = "C2HO4(736) <=> O_11_(7) + C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.744, 1.96, -0.02738, -0.01468],
            [14.11, -0.01527, -0.01021, -0.005284],
            [-0.09691, 0.00269, 0.001831, 0.0009784],
            [-0.06769, 0.006149, 0.004095, 0.002106],
            [-0.03542, 0.004331, 0.002868, 0.001459],
            [-0.01581, 0.002037, 0.001348, 0.0006856],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6699,
    label = "CO2_5_(8) + CHO2(424) <=> C2HO4(737)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.143, 1.632, -0.1734, -0.05813],
            [5.687, 0.3321, 0.136, 0.03311],
            [-0.006651, -0.03454, -0.007405, 0.00347],
            [-0.01684, -0.008657, -0.003478, -0.0001456],
            [-0.05571, -0.002103, -5.079e-05, 0.0006317],
            [-0.04484, -0.001463, -6.89e-05, 0.0003487],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6700,
    label = "CO2_5_(8) + CHO2(42) <=> C2HO4(737)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.294, -0.1803, -0.1117, -0.04998],
            [11.93, 0.1146, 0.06518, 0.02357],
            [-0.1252, -0.002138, 0.001395, 0.003152],
            [-0.05646, 0.001144, 0.0006743, 0.0003086],
            [-0.02387, 0.000977, 0.0006356, 0.0003081],
            [-0.01079, 0.0002536, 0.0001729, 9.326e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6701,
    label = "C2HO4(737) <=> C2HO4(729)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.267, 1.898, -0.0605, -0.02454],
            [1.335, 0.1016, 0.06051, 0.02483],
            [-0.07404, 0.009525, 0.004681, 0.001019],
            [-0.03722, -0.01212, -0.006543, -0.002054],
            [-0.02537, 0.000532, 3.448e-05, -0.0002111],
            [-0.01124, 0.005066, 0.002551, 0.0006253],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6705,
    label = "H_10_(3) + C2O4(730) <=> C2HO4(737)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.767, 0.8854, -0.1344, -0.003071],
            [1.544, 0.7675, -0.00489, -0.0251],
            [-0.1562, 0.1109, 0.03537, 0.0001394],
            [0.01159, -0.01756, 0.005435, 0.003071],
            [0.009016, -0.001824, -0.001085, -0.0003479],
            [-0.009637, 0.007194, 0.001434, -0.0004123],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6710,
    label = "OH_12_(12) + CO3(733) <=> CHO4(713)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.1976, 0.09881, -0.03488, 0.004337],
            [8.304, 0.1812, -0.06032, 0.007147],
            [0.1865, 0.1354, -0.04137, 0.002001],
            [0.01367, 0.08438, -0.02031, -0.001836],
            [-0.00912, 0.04299, -0.005902, -0.003272],
            [-0.006135, 0.01758, 0.0008168, -0.002612],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6717,
    label = "S(738) <=> CO_21_(14) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.7762, 0.3392, -0.07212, 0.001357],
            [7.761, 0.5619, -0.1049, -0.003757],
            [-0.1056, 0.3143, -0.03077, -0.01155],
            [-0.0775, 0.1069, 0.01398, -0.00894],
            [-0.021, 0.01078, 0.01781, -0.001275],
            [-0.001418, -0.007744, 0.00633, 0.002445],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6718,
    label = "CO2_5_(8) + CHO2(424) <=> C2HO4(739)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-2.764, 1.832, -0.1043, -0.04691],
            [6.832, 0.08407, 0.0494, 0.01912],
            [0.2594, -0.01845, -0.00863, -0.001319],
            [0.1273, -0.01185, -0.007188, -0.002982],
            [0.03779, -0.008101, -0.004917, -0.002],
            [0.01822, -0.0055, -0.00336, -0.001387],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6719,
    label = "CO2_5_(8) + CHO2(424) <=> C2HO4(739)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [0.4128, -0.04021, -0.02666, -0.01362],
            [7.387, -0.04643, -0.03004, -0.01464],
            [0.3766, -0.02979, -0.01901, -0.009008],
            [0.09199, -0.01523, -0.009461, -0.004237],
            [0.02661, -0.007377, -0.004454, -0.001869],
            [0.008589, -0.003288, -0.00192, -0.0007394],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6720,
    label = "C2HO4(739) <=> C2HO4(729)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.557, 1.999, -0.0005696, -0.000316],
            [-0.2509, -8.633e-05, -6.005e-05, -3.33e-05],
            [-0.1698, 3.212e-05, 2.226e-05, 1.227e-05],
            [-0.04891, -1.212e-05, -8.444e-06, -4.696e-06],
            [-0.02582, 4.426e-06, 3.1e-06, 1.739e-06],
            [-0.01311, 1.523e-05, 1.06e-05, 5.889e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6730,
    label = "CHO2(42) + CHO2(424) <=> S(738)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.46, 0.3403, -0.06297, 0.0009238],
            [-0.592, 0.5699, -0.08956, -0.004544],
            [-0.3684, 0.3345, -0.02291, -0.01158],
            [-0.1842, 0.1309, 0.01608, -0.008447],
            [-0.07096, 0.02441, 0.01892, -0.0008892],
            [-0.01917, -0.008558, 0.008106, 0.002912],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6731,
    label = "S(738) <=> OH_12_(12) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.514, 1.294, -0.2451, -0.01534],
            [15.22, 0.6027, 0.1303, -0.04598],
            [-0.3646, 0.03553, 0.05818, 0.02188],
            [-0.05968, -0.04005, -0.005036, 0.01212],
            [-0.005811, -0.0138, -0.009636, -0.001102],
            [-0.008519, 0.004259, -0.0009377, -0.002637],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6732,
    label = "HCO(22) + CHO3(659) <=> S(738)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.44, 0.319, -0.06592, 0.001291],
            [-0.4825, 0.5363, -0.09603, -0.004223],
            [-0.3177, 0.3202, -0.02987, -0.01209],
            [-0.1613, 0.1314, 0.01116, -0.009753],
            [-0.06253, 0.02928, 0.01754, -0.002289],
            [-0.01673, -0.005238, 0.009056, 0.002218],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6733,
    label = "S(738) <=> H_10_(3) + C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.454, 1.173, -0.2332, 0.0005967],
            [13.68, 0.7193, 0.09948, -0.06086],
            [-0.3057, 0.05519, 0.07792, 0.01718],
            [-0.0555, -0.04672, 0.001399, 0.01708],
            [-0.002642, -0.01799, -0.01183, 0.0006986],
            [-0.00493, 0.003707, -0.002738, -0.003196],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6734,
    label = "S(738) <=> H_10_(3) + C2HO4(729)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.86, 1.315, -0.2361, -0.01432],
            [15.07, 0.6233, 0.1409, -0.04247],
            [-0.3299, 0.02862, 0.05953, 0.02503],
            [-0.05278, -0.0443, -0.007735, 0.01195],
            [-0.002546, -0.01399, -0.01075, -0.002132],
            [-0.00647, 0.004619, -0.0008179, -0.002921],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6735,
    label = "O2_2_(13) + HCCO(26) <=> C2HO3(740)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.247, -0.01475, -0.01002, -0.005347],
            [1.584, 0.01691, 0.0114, 0.005992],
            [0.1529, -0.005833, -0.00388, -0.001992],
            [0.03822, 0.0003114, 0.0001687, 5.048e-05],
            [0.009069, 0.0003246, 0.0002267, 0.0001265],
            [0.001817, -3.888e-05, -2.347e-05, -9.766e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6736,
    label = "CO2_5_(8) + HCO(22) <=> C2HO3(740)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.378, -0.0829, -0.05403, -0.02702],
            [10.38, 0.005573, 0.005376, 0.004012],
            [0.1638, -0.00703, -0.003986, -0.001228],
            [0.02331, -0.0006578, -0.0006785, -0.0003154],
            [-0.003709, 0.001263, 0.0004964, 8.535e-06],
            [-0.005746, 0.001214, 0.000658, 0.0001398],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6737,
    label = "C2HO3(740) <=> C2HO3(732)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.049, 1.947, -0.033, -0.01486],
            [0.5798, 0.04058, 0.02563, 0.01184],
            [-0.1637, 0.009639, 0.004635, 0.0009042],
            [-0.08259, -0.0001326, -0.00019, -8.457e-05],
            [-0.02249, -0.002479, -0.001047, -1.404e-05],
            [0.01174, -0.001369, -0.0006307, -0.0001298],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6738,
    label = "C2HO2(741) <=> C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.012, 0.6783, -0.1201, 0.005581],
            [6.443, 0.7378, -0.03441, -0.02307],
            [-0.3263, 0.2059, 0.03831, -0.006146],
            [-0.1037, 0.01953, 0.01857, 0.004232],
            [-0.01928, -0.01156, 0.001457, 0.002372],
            [0.002721, -0.007261, -0.001924, 1.998e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6739,
    label = "H_10_(3) + C2O2(725) <=> C2HO2(741)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.648, -0.01047, -0.007057, -0.003713],
            [-1.236, 0.0126, 0.008454, 0.004409],
            [-0.2833, -0.002114, -0.001371, -0.0006714],
            [-0.05001, -0.0001891, -0.000141, -8.654e-05],
            [-0.001961, -2.786e-05, -1.982e-05, -1.14e-05],
            [0.004276, -3.496e-06, -2.549e-06, -1.513e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6740,
    label = "C2HO3(728) <=> O_11_(7) + C2HO2(741)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.908, 2, -0.0003017, -0.0001674],
            [12.36, 0.0001279, 8.899e-05, 4.939e-05],
            [-0.2504, 0.0001885, 0.0001311, 7.277e-05],
            [-0.08217, 3.918e-05, 2.727e-05, 1.513e-05],
            [0.008877, -4.654e-05, -3.237e-05, -1.796e-05],
            [0.007983, -2.288e-05, -1.592e-05, -8.829e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6743,
    label = "C2HO2(741) <=> HCCO(26) + O(734)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-21.99, 1.994, -0.004248, -0.002343],
            [21.97, 0.005623, 0.003892, 0.00214],
            [-0.2742, -0.0002951, -0.0001998, -0.0001058],
            [-0.06457, -0.000269, -0.0001869, -0.0001034],
            [-0.006824, -0.0001072, -7.466e-05, -4.152e-05],
            [0.002581, -2.16e-05, -1.51e-05, -8.439e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6745,
    label = "C2HO4(742) <=> CO2_5_(8) + CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.639, 1.977, -0.01523, -0.007792],
            [-0.2702, -0.03485, -0.02288, -0.01147],
            [-0.06458, -0.02379, -0.01543, -0.007558],
            [-0.02756, -0.01411, -0.008993, -0.004252],
            [-0.01441, -0.00774, -0.00483, -0.002185],
            [-0.007921, -0.003962, -0.002414, -0.001035],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6746,
    label = "C2HO4(739) <=> C2HO4(742)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.027, 1.967, -0.02172, -0.01119],
            [-0.2025, 0.04264, 0.02836, 0.01455],
            [0.3156, -0.006978, -0.004576, -0.00229],
            [0.09289, -0.006473, -0.004373, -0.002307],
            [-0.04247, 0.001041, 0.000715, 0.0003882],
            [-0.02557, 0.002347, 0.001573, 0.0008186],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6747,
    label = "CO_21_(14) + CHO3(718) <=> C2HO4(742)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.18, 0.1281, -0.04082, 0.004247],
            [8.997, 0.2284, -0.06985, 0.005711],
            [0.127, 0.1614, -0.04279, 0.0001046],
            [-0.007458, 0.08935, -0.01663, -0.003629],
            [-0.01523, 0.03696, -0.001251, -0.003789],
            [-0.006297, 0.009441, 0.003628, -0.001982],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6748,
    label = "CO_21_(14) + CHO3(722) <=> C2HO4(742)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.883, 0.00102, -0.0007077, 0.0003908],
            [0.443, 0.001562, -0.001084, 0.0005986],
            [-0.0003431, 0.0006054, -0.0004201, 0.0002321],
            [7.79e-05, -0.0001372, 9.464e-05, -5.177e-05],
            [0.000228, -0.0004018, 0.0002779, -0.0001527],
            [0.0001861, -0.000328, 0.0002268, -0.0001245],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6750,
    label = "CO_21_(14) + CHO2(42) <=> C2HO3(743)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.17, -0.1063, -0.06967, -0.03479],
            [8.269, 0.04433, 0.02811, 0.01315],
            [0.08691, 0.02764, 0.01753, 0.008211],
            [-0.04671, 0.002863, 0.002149, 0.001327],
            [-0.05084, -0.004925, -0.002847, -0.001065],
            [-0.02615, 0.001005, 0.0005909, 0.0002334],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6751,
    label = "C2HO3(743) <=> C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.159, 1.171, -0.1178, -0.007699],
            [2.655, 0.7244, 0.05986, -0.009569],
            [-0.2334, 0.04537, 0.02667, 0.006883],
            [-0.01353, -0.01975, -0.001539, 0.0009685],
            [0.003121, -0.002971, -0.0001756, -0.0003375],
            [-0.003761, -2.443e-05, 0.0009393, 0.000203],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6752,
    label = "C2HO3(728) <=> C2HO3(743)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.838, 1.994, -0.004435, -0.002446],
            [4.294, 0.003077, 0.002133, 0.001176],
            [-0.3103, 0.002834, 0.001959, 0.001076],
            [-0.1044, 0.0003103, 0.0002152, 0.0001187],
            [0.002708, -0.000792, -0.0005458, -0.000298],
            [0.006673, -0.0003092, -0.0002133, -0.0001166],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6753,
    label = "C2HO4(735) <=> O_11_(7) + C2HO3(743)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.866, 1.998, -0.001074, -0.0005958],
            [13.31, 0.0009443, 0.0006564, 0.0003637],
            [-0.1189, 0.0001331, 9.264e-05, 5.145e-05],
            [-0.0375, 9.235e-06, 6.457e-06, 3.611e-06],
            [-0.01287, -1.484e-06, -1.027e-06, -5.643e-07],
            [-0.004533, -1.089e-06, -7.569e-07, -4.194e-07],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6757,
    label = "OH_12_(12) + CH2OH(32) <=> CH4O2(744)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [13.11, 0.7053, -0.118, 0.007335],
            [-1.021, 0.7428, -0.01841, -0.02093],
            [-0.4708, 0.2111, 0.04276, -0.003823],
            [-0.1755, 0.02712, 0.01832, 0.00454],
            [-0.05015, -0.009505, 0.001596, 0.002081],
            [-0.006445, -0.008553, -0.001871, -2.942e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6765,
    label = "CH4O2(744) <=> H_10_(3) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.024, 0.7822, -0.1068, 0.001799],
            [12.99, 0.839, -0.007245, -0.02025],
            [-0.6557, 0.2151, 0.04991, -0.0004491],
            [-0.2415, 0.01195, 0.01755, 0.006106],
            [-0.07613, -0.01704, -0.0005853, 0.001906],
            [-0.01699, -0.01035, -0.002673, -0.0003509],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6766,
    label = "CH4O2(744) <=> H_10_(3) + CH3O2(719)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.35, 1.255, -0.2021, 0.0002427],
            [14.23, 0.6686, 0.1227, -0.03191],
            [-0.5546, 0.07989, 0.06097, 0.01454],
            [-0.1865, -0.0225, 0.003958, 0.008191],
            [-0.05133, -0.01991, -0.006495, 0.0006503],
            [-0.006937, -0.00727, -0.004086, -0.0009646],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6768,
    label = "H_10_(3) + C2O3(745) <=> C2HO3(743)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [10.71, 1.213, -0.1224, -0.007576],
            [0.3123, 0.6952, 0.0608, -0.0103],
            [-0.1135, 0.01794, 0.02338, 0.005707],
            [0.03324, -0.02114, -0.002271, 0.0004218],
            [0.01155, 0.0004377, 0.0002751, -0.0001962],
            [-0.004221, 0.001306, 0.001075, 0.0002837],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6769,
    label = "C2O2(725) + O(734) <=> C2O3(745)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [11.25, 1.246, -0.1504, 0.002029],
            [-1.642, 0.4708, 0.07762, -0.008239],
            [-0.5386, 0.05234, 0.01643, 0.002037],
            [-0.1721, 0.004062, 0.001056, 0.0002144],
            [-0.05469, 0.0005856, 0.0001293, -6.281e-05],
            [-0.0173, 1.19e-05, 0.0001005, -6.875e-06],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6770,
    label = "C2O2(725) + O(734) <=> C2O3(745)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [10.96, 1.526, -0.1873, -0.02122],
            [-1.523, 0.3501, 0.1166, -0.0008901],
            [-0.5229, 0.02485, 0.01767, 0.005936],
            [-0.1682, -0.001569, 0.0006872, 0.0009259],
            [-0.05395, -0.000803, -0.0001281, 0.0001489],
            [-0.01734, -0.0003121, -8.179e-05, 4.331e-05],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6784,
    label = "H_10_(3) + C2O3(745) <=> C2HO3(728)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [9.44, 1.575, -0.09203, -0.01118],
            [0.4816, 0.4279, 0.0746, 0.002832],
            [-0.03789, -0.01356, 0.006051, 0.002933],
            [0.005753, -0.00791, -8.966e-05, 0.0005807],
            [-0.02377, -0.001326, 0.0008817, 0.000523],
            [-0.02587, -0.0007205, 0.0004336, 0.0002563],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6785,
    label = "OH_12_(12) + C2O3(745) <=> C2HO4(735)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.442, 0.6149, -0.1227, 0.0007969],
            [3.657, 0.7456, -0.08233, -0.02507],
            [-0.03196, 0.2001, 0.02436, -0.01353],
            [0.01618, 0.002861, 0.01886, 0.001941],
            [0.01814, -0.01071, 0.001219, 0.002263],
            [0.003397, 0.001886, -0.001165, -0.0003328],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6786,
    label = "OH_12_(12) + C2O3(745) <=> C2HO4(736)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.278, -0.09992, -0.2563, -0.03341],
            [5.809, 1.011, 0.04765, -0.01524],
            [-0.04186, 0.2018, -0.01406, 0.008563],
            [-0.08599, 0.07363, -0.0008858, -0.007798],
            [-0.03033, 0.0221, 0.0131, -0.001157],
            [-0.006809, -0.001914, 0.005393, 0.002469],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6789,
    label = "CO2_5_(8) + HCO(22) <=> C2HO3(746)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.44, 1.34, -0.1775, -0.03954],
            [6.804, 0.58, 0.1082, 0.007552],
            [0.04633, -0.01211, 0.009769, 0.003995],
            [0.09161, -0.02045, -0.005346, -0.0008977],
            [0.03901, -0.00239, -0.0009125, -0.000342],
            [0.01051, -0.0005037, 0.000188, 0.0001058],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6790,
    label = "C2HO3(746) <=> C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.956, 1.467, -0.1554, -0.005555],
            [2.498, 0.4957, 0.1193, -0.01214],
            [-0.2129, -0.007271, 0.01602, 0.00815],
            [0.002331, -0.004958, -0.007192, -0.001063],
            [0.02137, -0.006967, 9.316e-05, 0.0004528],
            [-0.005791, 0.003778, -0.0002661, 5.205e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6791,
    label = "C2HO4(737) <=> O_11_(7) + C2HO3(746)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.77, 2, -9.525e-05, -5.288e-05],
            [14.39, -6.077e-06, -4.229e-06, -2.347e-06],
            [0.1734, -2.886e-05, -2.009e-05, -1.115e-05],
            [0.01787, 4.023e-07, 2.799e-07, 1.554e-07],
            [-0.03962, 1.332e-05, 9.268e-06, 5.145e-06],
            [-0.03654, 1.364e-05, 9.49e-06, 5.268e-06],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6792,
    label = "HO2_17_(5) + C2O2(725) <=> C2HO4(736)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.453, 1.906, -0.06233, -0.03195],
            [2.571, 0.0359, 0.02398, 0.0124],
            [-0.3252, 0.004457, 0.002975, 0.001538],
            [-0.1813, 0.001449, 0.001042, 0.0006077],
            [-0.06096, 0.001377, 0.0009622, 0.0005367],
            [-0.01016, 0.0009774, 0.000637, 0.0003146],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6802,
    label = "S(747) <=> CO_21_(14) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.9926, 0.4504, -0.0776, 0.001334],
            [7.499, 0.687, -0.08735, -0.009316],
            [-0.1938, 0.3118, 0.002199, -0.01337],
            [-0.096, 0.07035, 0.02629, -0.003144],
            [-0.02048, -0.008092, 0.01229, 0.003381],
            [0.001587, -0.01206, 0.0001476, 0.002381],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6805,
    label = "HCO(22) + CHO2(424) <=> S(747)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.36, 1.43, -0.2343, -0.03182],
            [-0.8738, 0.4724, 0.1475, -0.01665],
            [-0.2765, 0.04314, 0.04316, 0.02001],
            [-0.05861, -0.02436, -0.00377, 0.007012],
            [-0.0003334, -0.01424, -0.007521, -0.001143],
            [0.003687, -0.00115, -0.002099, -0.001741],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6806,
    label = "CO2_5_(8) + CHO2(42) <=> C2HO4(748)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.627, 1.589, -0.1437, -0.04399],
            [6.579, 0.3839, 0.09986, 0.0187],
            [-0.1156, -0.01437, 0.007425, 0.004492],
            [-0.1266, -0.004187, 0.003826, 0.002515],
            [-0.06999, -0.002367, 0.000612, 0.00103],
            [-0.01328, -0.002729, -0.0014, -0.0001784],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6807,
    label = "C2HO4(748) <=> C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.763, 1.74, -0.1051, -0.02152],
            [0.7952, 0.2774, 0.1016, 0.01352],
            [-0.2209, -0.0135, 0.00214, 0.004994],
            [-0.136, -0.005115, -0.0009223, 0.001022],
            [-0.07029, -0.003391, -0.0006672, 0.0003301],
            [-0.01506, -0.0025, -0.001322, -0.0004636],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6811,
    label = "H_10_(3) + C2O4(730) <=> C2HO4(748)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.57, 1.495, 0.1545, 0.00292],
            [1.648, 0.2391, -0.1456, 0.03157],
            [-0.3054, 0.1732, -0.01843, -0.0248],
            [-0.1818, 0.01135, 0.01682, -0.003871],
            [-0.05709, -0.01403, 0.0009807, 0.003547],
            [-0.003056, -0.003986, -0.002665, 0.0004473],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6812,
    label = "C2HO4(737) <=> C2HO4(748)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.2021, 1.999, -0.0007709, -0.0004276],
            [5.76, 0.0006196, 0.0004309, 0.0002388],
            [0.01563, -5.516e-05, -3.831e-05, -2.12e-05],
            [0.002043, -8.225e-06, -5.715e-06, -3.164e-06],
            [-0.04511, 8.933e-05, 6.211e-05, 3.442e-05],
            [-0.04449, 8.881e-05, 6.174e-05, 3.421e-05],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6813,
    label = "S(747) <=> H_10_(3) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.828, 1.638, -0.1772, -0.04401],
            [13.64, 0.3639, 0.1577, 0.02023],
            [-0.3277, 0.000152, 0.01779, 0.01879],
            [-0.06661, -0.02568, -0.01191, -0.0008496],
            [0.002965, -0.008106, -0.006159, -0.003452],
            [0.005343, 0.00133, -9.203e-05, -0.000926],
        ],
        kunits = 's^-1',
        Tmin = (600, 'K'),
        Tmax = (3200, 'K'),
        Pmin = (0.01, 'atm'),
        Pmax = (98.692, 'atm'),
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
""",
)

entry(
    index = 6814,
    label = "C10H7(749) <=> i3(750)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.67, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: phenyl_diacetylene_benzofulvenyl_effective
""",
)

entry(
    index = 6815,
    label = "C10H7(749) <=> i4(751)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.67, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: phenyl_diacetylene_benzofulvenyl_effective
""",
)

entry(
    index = 6816,
    label = "CPD(595) + CPDyl(596) <=> S(752)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.8, Ea=(8.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6817,
    label = "CPD(595) + CPDyl(596) <=> S(753)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.74, Ea=(3.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6818,
    label = "S(753) <=> pdt7(754)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+11, 's^-1'), n=0.29, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6819,
    label = "pdt7(754) <=> pdt8(755)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.51e+11, 's^-1'), n=0.58, Ea=(29.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6820,
    label = "pdt8(755) <=> pdt9(756)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.39e+10, 's^-1'), n=0.91, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6821,
    label = "pdt9(756) <=> S(757)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.25e+09, 's^-1'), n=0.76, Ea=(6.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6822,
    label = "S(752) <=> pdt7(754)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43e+11, 's^-1'), n=0.21, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6823,
    label = "H_10_(3) + pdt11(758) <=> S(757)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.09e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6824,
    label = "S(757) <=> pdt12(759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.76e+10, 's^-1'), n=0.78, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6825,
    label = "pdt12(759) <=> C6H6(48) + C4H5(509)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.14e+12, 's^-1'), n=0.52, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6826,
    label = "H_10_(3) + pdt13(760) <=> pdt12(759)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.81e+06, 'cm^3/(mol*s)'),
        n = 1.95,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6827,
    label = "S(753) <=> pdt14(761)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+11, 's^-1'), n=0.85, Ea=(46.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6828,
    label = "S(753) <=> pdt15(762)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+08, 's^-1'), n=1.64, Ea=(22.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6829,
    label = "pdt15(762) <=> pdt16(763)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.29e+09, 's^-1'), n=1.04, Ea=(31.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6830,
    label = "pdt16(763) <=> pdt17(764)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.36e+10, 's^-1'), n=0.44, Ea=(32.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6831,
    label = "pdt17(764) <=> pdt18(765)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.47e+10, 's^-1'), n=0.79, Ea=(29, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6832,
    label = "pdt18(765) <=> pdt19(766)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6833,
    label = "pdt14(761) <=> pdt16(763)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+08, 's^-1'), n=1.55, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6834,
    label = "pdt14(761) <=> pdt20(767)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.107, 's^-1'), n=3.67, Ea=(29.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6835,
    label = "pdt20(767) <=> pdt21(768)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.9e+10, 's^-1'), n=0.29, Ea=(21.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6836,
    label = "pdt22(769) + CH3(17) <=> pdt21(768)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2480, 'cm^3/(mol*s)'), n=2.89, Ea=(-0.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6837,
    label = "pdt14(761) <=> pdt23(770)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6838,
    label = "pdt22(769) <=> C9H8(771)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+09, 's^-1'), n=0.96, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6839,
    label = "pdt23(770) <=> pdt9(756)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.27e+10, 's^-1'), n=1.01, Ea=(40.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6840,
    label = "pdt23(770) <=> H_10_(3) + pdt30(772)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=1.41, Ea=(38.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6841,
    label = "H_10_(3) + pdt26(773) <=> pdt19(766)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.09e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6842,
    label = "pdt18(765) <=> pdt25(774)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(250000, 's^-1'), n=1.95, Ea=(24, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6843,
    label = "H_10_(3) + pdt13(760) <=> pdt25(774)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (1.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6844,
    label = "H_10_(3) + pdt31(775) <=> pdt8(755)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6845,
    label = "pdt17(764) <=> pdt24(776)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.48e+11, 's^-1'), n=0.26, Ea=(7.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6846,
    label = "pdt24(776) <=> pdt28(777)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+12, 's^-1'), n=0.31, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6847,
    label = "pdt21(768) <=> pdt27(778)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.07e+06, 's^-1'), n=2, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6848,
    label = "C9H8(771) + CH3(17) <=> pdt27(778)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(643, 'cm^3/(mol*s)'), n=2.8, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6849,
    label = "pdt16(763) <=> pdt20(767)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+08, 's^-1'), n=1.01, Ea=(26.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6850,
    label = "pdt28(777) <=> pdt29(779)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+09, 's^-1'), n=1.14, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6851,
    label = "pdt28(777) <=> pdt23(770)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46e+07, 's^-1'), n=1.66, Ea=(31.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6852,
    label = "pdt25(774) <=> pdt32(780)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0.41, Ea=(32.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6853,
    label = "pdt32(780) <=> pdt22(769) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+10, 's^-1'), n=1.33, Ea=(51.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6854,
    label = "pdt16(763) <=> pdt33(781)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+07, 's^-1'), n=1.8, Ea=(15.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6855,
    label = "pdt33(781) <=> pdt20(767)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.27e+06, 's^-1'), n=1.5, Ea=(33.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6856,
    label = "pdt33(781) <=> pdt29(779)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.16e+10, 's^-1'), n=0.2, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6857,
    label = "H_10_(3) + pdt31(775) <=> pdt29(779)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6858,
    label = "H_10_(3) + pdt30(772) <=> pdt29(779)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6859,
    label = "H_10_(3) + pdt35(782) <=> pdt29(779)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6860,
    label = "S(757) <=> pdt37(783)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.83e+08, 's^-1'), n=1.45, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6861,
    label = "H_10_(3) + pdt38(784) <=> pdt37(783)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.61e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6862,
    label = "pdt15(762) <=> pdt39(785)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+08, 's^-1'), n=1.8, Ea=(21.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6863,
    label = "pdt39(785) <=> pdt33(781)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=1.08, Ea=(42.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6864,
    label = "pdt14(761) <=> pdt57(786)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.51e+11, 's^-1'), n=0.28, Ea=(12.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6865,
    label = "pdt57(786) <=> pdt12(759)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.75e+11, 's^-1'), n=0.44, Ea=(18.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6866,
    label = "S(753) <=> pdt55(787)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.36e+06, 's^-1'), n=1.7, Ea=(31.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6867,
    label = "pdt15(762) <=> pdt55(787)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+06, 's^-1'), n=1.75, Ea=(25.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6868,
    label = "pdt55(787) <=> pdt58(788)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6869,
    label = "pdt58(788) <=> pdt20(767)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+07, 's^-1'), n=1.61, Ea=(27.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6870,
    label = "C9H7(789) <=> C9H7(790)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6871,
    label = "C9H7(789) <=> C9H7(791)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6872,
    label = "C9H7(789) <=> C9H7(792)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6873,
    label = "C9H7(789) <=> C9H7(793)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H11
""",
)

entry(
    index = 6874,
    label = "C3H4(39) + C3H5(41) <=> C6H9(794)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(42, 'cm^3/(mol*s)'), n=3.27, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6875,
    label = "C6H9(794) <=> C6H9(795)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+09, 's^-1'), n=0.63, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6876,
    label = "C6H9(795) <=> H_10_(3) + C6H8(796)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.93e+09, 's^-1'), n=1.27, Ea=(31, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6877,
    label = "iC4H7(797) + C3H4(39) <=> C7H11(798)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18.6, 'cm^3/(mol*s)'), n=3, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6878,
    label = "C7H11(798) <=> C7H11(799)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+11, 's^-1'), n=0.2, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6879,
    label = "C7H11(799) <=> H_10_(3) + C7H10(800)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.37e+08, 's^-1'), n=1.3, Ea=(29.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6880,
    label = "C3H5(41) + C3H4(45) <=> C6H9(801)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (267000, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (12.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6881,
    label = "C6H9(801) <=> C6H9(802)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.53e+07, 's^-1'), n=1.05, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6882,
    label = "C6H9(802) <=> H_10_(3) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.99e+10, 's^-1'), n=1, Ea=(32.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6883,
    label = "iC4H7(797) + C3H4(45) <=> C7H11(803)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(121, 'cm^3/(mol*s)'), n=2.9, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6884,
    label = "C7H11(803) <=> C7H11(804)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+10, 's^-1'), n=0.2, Ea=(9.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6885,
    label = "C7H11(804) <=> H_10_(3) + C7H10(805)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.77e+09, 's^-1'), n=1.4, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6886,
    label = "C4H5(465) + C3H4(39) <=> C7H9(806)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(128, 'cm^3/(mol*s)'), n=3.05, Ea=(7.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6887,
    label = "C7H9(806) <=> C7H9(807)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+11, 's^-1'), n=0.34, Ea=(21.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6888,
    label = "C7H9(807) <=> H_10_(3) + C7H8(808)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=1.27, Ea=(44.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6889,
    label = "C4H5(465) + C3H4(45) <=> C7H9(809)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1900, 'cm^3/(mol*s)'), n=2.92, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6890,
    label = "C7H9(809) <=> C7H9(455)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.9e+10, 's^-1'), n=0.33, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6891,
    label = "C7H9(455) <=> H_10_(3) + C7H8(810)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.47e+10, 's^-1'), n=1.22, Ea=(45.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6892,
    label = "C3H4(39) + C3H5(41) <=> C6H9(811)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3960, 'cm^3/(mol*s)'), n=2.65, Ea=(11.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6893,
    label = "C6H9(811) <=> C6H9(795)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.47e+07, 's^-1'), n=0.85, Ea=(10.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6894,
    label = "iC4H7(797) + C3H4(39) <=> C7H11(812)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37, 'cm^3/(mol*s)'), n=2.89, Ea=(9.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6895,
    label = "C7H11(812) <=> C7H11(799)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+11, 's^-1'), n=0.27, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6896,
    label = "C6H7(51) <=> C6H7(813)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.05e+11, 's^-1'), n=0.12, Ea=(12.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6897,
    label = "C6H7(813) <=> C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+10, 's^-1'), n=1.01, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6898,
    label = "C3H4(45) + C3H3(19) <=> C6H7(814)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(285, 'cm^3/(mol*s)'), n=2.93, Ea=(11.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6899,
    label = "C6H7(814) <=> C6H7(815)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+11, 's^-1'), n=0.1, Ea=(11.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6900,
    label = "C6H7(815) <=> C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=1.01, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6901,
    label = "C6H7(510) <=> C6H7(816)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.47e+11, 's^-1'), n=0.15, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6902,
    label = "C6H7(816) <=> C6H7(53)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+09, 's^-1'), n=1.12, Ea=(39.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3
""",
)

entry(
    index = 6903,
    label = "H_10_(3) + C10H8(817) <=> C10H9(818)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+09, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6904,
    label = "H_10_(3) + C10H8(817) <=> C10H9(819)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6905,
    label = "H_10_(3) + C10H8(817) <=> C10H9(820)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6906,
    label = "C10H9(818) <=> C10H9(819)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+08, 's^-1'), n=1.46, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6907,
    label = "C10H9(819) <=> C10H9(820)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.46e+06, 's^-1'), n=2.01, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6908,
    label = "C10H9(818) <=> prod1(821)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.89e+11, 's^-1'), n=0.12, Ea=(9.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6909,
    label = "prod1(821) <=> prod2(822)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.73e+11, 's^-1'), n=0.31, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6910,
    label = "prod2(822) <=> prod5(823)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6911,
    label = "prod2(822) <=> prod3(824)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.14e+11, 's^-1'), n=0.34, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6912,
    label = "prod3(824) <=> prod4(825)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.79e+11, 's^-1'), n=0.33, Ea=(10.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6913,
    label = "prod4(825) <=> H_10_(3) + C10H8(826)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+08, 's^-1'), n=1.55, Ea=(15.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6914,
    label = "prod5(823) <=> prod4(825)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.42e+11, 's^-1'), n=0.22, Ea=(4.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: naphthalene_H
""",
)

entry(
    index = 6915,
    label = "H_10_(3) + C7H8(827) <=> addA(828)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6916,
    label = "H_10_(3) + C7H8(827) <=> addB(599)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (2.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6917,
    label = "H_10_(3) + C7H8(827) <=> addC(829)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+09, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6918,
    label = "H_10_(3) + C7H8(827) <=> addD(830)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.41e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (1.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6919,
    label = "addA(828) <=> addB(599)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.97e+06, 's^-1'), n=1.8, Ea=(37.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6920,
    label = "addC(829) <=> addD(830)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.81e+07, 's^-1'), n=1.72, Ea=(44.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6921,
    label = "addA(828) <=> C7H9(59)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+09, 's^-1'), n=1, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6922,
    label = "addD(830) <=> C7H9(831)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+08, 's^-1'), n=1.39, Ea=(24.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6923,
    label = "C7H9(832) <=> C7H9(833)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.11e+09, 's^-1'), n=1.34, Ea=(47.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6924,
    label = "addA(828) <=> C7H9(834)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.69e+11, 's^-1'), n=0.24, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6925,
    label = "C7H9(834) <=> C7H9(60)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.21e+11, 's^-1'), n=0.46, Ea=(16.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6926,
    label = "addB(599) <=> C7H9(835)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+11, 's^-1'), n=0.16, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6927,
    label = "C7H9(835) <=> C7H9(832)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+11, 's^-1'), n=0.55, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6928,
    label = "addC(829) <=> C7H9(836)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.77e+10, 's^-1'), n=0.87, Ea=(35, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6929,
    label = "C7H9(836) <=> C7H9(837)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.95e+10, 's^-1'), n=0.53, Ea=(31.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6930,
    label = "addC(829) <=> C7H9(838)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.17e+10, 's^-1'), n=0.34, Ea=(31.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6931,
    label = "C7H9(838) <=> C7H9(837)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.37e+11, 's^-1'), n=0.73, Ea=(25.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6932,
    label = "addD(830) <=> C2H3(29) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 's^-1'), n=0.81, Ea=(33.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6933,
    label = "C7H9(60) <=> C7H9(837)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.03e+06, 's^-1'), n=1.96, Ea=(50.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6934,
    label = "C7H9(837) <=> H_10_(3) + C7H8(839)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+09, 's^-1'), n=1.23, Ea=(28.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6935,
    label = "addD(830) <=> C7H9(840)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=0.51, Ea=(30.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6936,
    label = "C7H9(840) <=> C7H9(833)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+11, 's^-1'), n=0.59, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6937,
    label = "C7H9(831) <=> C7H9(841)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.56e+10, 's^-1'), n=1.17, Ea=(48.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6938,
    label = "C7H9(841) <=> C7H9(842)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+11, 's^-1'), n=0.26, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6939,
    label = "C7H9(842) <=> H_10_(3) + C7H8(843)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6940,
    label = "C7H9(832) <=> C7H9(836)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.03e+10, 's^-1'), n=1.1, Ea=(37, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6941,
    label = "C7H9(832) <=> H_10_(3) + C7H8(844)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.58e+10, 's^-1'), n=1.38, Ea=(48.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6942,
    label = "addC(829) <=> C2H3(29) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+12, 's^-1'), n=0.87, Ea=(45, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6943,
    label = "addB(599) <=> C7H9(845)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+11, 's^-1'), n=0.06, Ea=(19.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6944,
    label = "C7H9(845) <=> C7H9(838)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(367000, 's^-1'), n=2.24, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6945,
    label = "C7H9(59) <=> C7H9(846)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.53e+06, 's^-1'), n=1.73, Ea=(58.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6946,
    label = "C6H6(54) + CH3(17) <=> C7H9(846)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(263, 'cm^3/(mol*s)'), n=2.89, Ea=(6.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6947,
    label = "C7H9(846) <=> C7H9(847)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+12, 's^-1'), n=0.15, Ea=(2.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6948,
    label = "C7H9(847) <=> C7H9(578)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.58e+12, 's^-1'), n=0.31, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6949,
    label = "addB(599) <=> C7H9(848)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.39e+07, 's^-1'), n=1.58, Ea=(21.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6950,
    label = "C7H9(848) <=> C7H9(849)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+11, 's^-1'), n=0.2, Ea=(46.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6951,
    label = "C7H9(849) <=> C7H9(850)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+11, 's^-1'), n=0.82, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6952,
    label = "C7H9(850) <=> H_10_(3) + C7H8(839)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6953,
    label = "C7H9(848) <=> C7H9(851)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+07, 's^-1'), n=1.74, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6954,
    label = "C7H9(851) <=> C7H9(852)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+11, 's^-1'), n=0.26, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6955,
    label = "C7H9(852) <=> C7H9(853)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.95e+10, 's^-1'), n=1.05, Ea=(39.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6956,
    label = "C7H9(853) <=> C7H9(841)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.81e+10, 's^-1'), n=0.91, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6957,
    label = "C7H9(851) <=> C7H9(854)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.11e+10, 's^-1'), n=0.18, Ea=(66.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6958,
    label = "C7H9(854) <=> C7H9(849)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+10, 's^-1'), n=0.87, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6959,
    label = "C7H7(855) <=> C7H7(856)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6960,
    label = "C7H9(447) <=> C7H9(857)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(285000, 's^-1'), n=2.15, Ea=(43.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6961,
    label = "C7H9(857) <=> C7H9(858)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.51e+10, 's^-1'), n=0.25, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6962,
    label = "C7H9(858) <=> C7H9(859)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 's^-1'), n=0.39, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6963,
    label = "C7H9(446) <=> C7H9(860)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(671000, 's^-1'), n=2.07, Ea=(48.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6964,
    label = "C7H9(860) <=> C7H9(861)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6965,
    label = "C7H9(861) <=> C7H9(859)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6966,
    label = "C7H9(859) <=> H_10_(3) + C7H8(839)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6967,
    label = "C7H7(856) <=> C7H7(579)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+08, 's^-1'), n=1.52, Ea=(38.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6968,
    label = "C7H7(600) <=> C7H7(862)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6969,
    label = "C7H7(600) <=> C7H7(863)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.32e+11, 's^-1'), n=0.3, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6970,
    label = "C7H7(863) <=> C7H7(855)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.84e+11, 's^-1'), n=0.66, Ea=(23.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6971,
    label = "C7H7(862) <=> C7H7(686)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6972,
    label = "C7H7(863) <=> C7H7(864)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+08, 's^-1'), n=0.21, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6973,
    label = "C7H7(856) <=> C7H7(865)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+08, 's^-1'), n=0.21, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6974,
    label = "H_10_(3) + FA(866) <=> C7H7(862)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+09, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6975,
    label = "C2H5(31) + CPDyl(596) <=> C7H10(867)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: vinylCPD_H
""",
)

entry(
    index = 6976,
    label = "W1(62) <=> W2(868)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.926e+10, 's^-1'), n=0.198, Ea=(5.455, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6977,
    label = "W1(62) <=> i3(750)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.42e+11, 's^-1'), n=0.258, Ea=(3.797, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6978,
    label = "W2(868) <=> i4(751)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.843e+08, 's^-1'), n=1.605, Ea=(56.952, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6979,
    label = "i3(750) <=> W5(869)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(24740, 's^-1'), n=2.344, Ea=(38.798, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6980,
    label = "i3(750) <=> W7(870)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(191.5, 's^-1'), n=3.05, Ea=(53.137, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6981,
    label = "H_10_(3) + P1(871) <=> W1(62)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.775e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (6.896, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6982,
    label = "H_10_(3) + P2(872) <=> W2(868)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.586e+11, 'cm^3/(mol*s)'),
        n = 0.743,
        Ea = (0.228, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6983,
    label = "H_10_(3) + P2(872) <=> i4(751)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.409e+12, 'cm^3/(mol*s)'),
        n = 0.597,
        Ea = (0.436, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6984,
    label = "H_10_(3) + P3(873) <=> i4(751)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.179e+12, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (0.09, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6985,
    label = "H_10_(3) + P4(874) <=> W5(869)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6986,
    label = "H_10_(3) + P5(875) <=> W7(870)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H4C2H_C2H2_High_P
""",
)

entry(
    index = 6987,
    label = "C3H6(38) + C6H5(64) <=> i2(876)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (1.683, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2006 Park',
    ),
    longDesc = 
u"""
Originally from reaction library: 2006_Park_Phenyl_Propene
From 2006 Park
""",
)

entry(
    index = 6988,
    label = "i2(876) <=> H_10_(3) + p4(877)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.848e+10, 's^-1'),
        n = 0.848,
        Ea = (33.958, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6989,
    label = "i2(876) <=> p1(878) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.603e+12, 's^-1'),
        n = 0.523,
        Ea = (29.345, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6990,
    label = "i2(876) <=> i3(879)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.399e+11, 's^-1'),
        n = 0.121,
        Ea = (15.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6991,
    label = "i2(876) <=> i8(880)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.815e+11, 's^-1'),
        n = 0.121,
        Ea = (32.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6992,
    label = "i2(876) <=> i9(881)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.899e+11, 's^-1'),
        n = 0.486,
        Ea = (31.961, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6993,
    label = "i2(876) <=> i10(882)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.307e+10, 's^-1'),
        n = 0.713,
        Ea = (42.834, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6994,
    label = "i1(660) <=> i3(879)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.528e+11, 's^-1'),
        n = 0.199,
        Ea = (16.505, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6995,
    label = "i1(660) <=> H_10_(3) + p2(883)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.935e+11, 's^-1'),
        n = 0.894,
        Ea = (34.903, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6996,
    label = "i1(660) <=> H_10_(3) + p3(884)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.424e+10, 's^-1'),
        n = 0.914,
        Ea = (34.551, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6997,
    label = "i1(660) <=> i4(885)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.312e+11, 's^-1'),
        n = 0.608,
        Ea = (39.998, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6998,
    label = "i1(660) <=> i7(886)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.148e+11, 's^-1'),
        n = 0.537,
        Ea = (37.159, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 6999,
    label = "i1(660) <=> i6(887)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.224e+09, 's^-1'),
        n = 0.668,
        Ea = (40.429, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7000,
    label = "i8(880) <=> p7(888) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.662e+12, 's^-1'),
        n = 0.757,
        Ea = (48.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7001,
    label = "i8(880) <=> H_10_(3) + p8(889)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.732e+10, 's^-1'),
        n = 0.856,
        Ea = (26.921, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7002,
    label = "i9(881) <=> H_10_(3) + p4(877)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.13e+13, 's^-1'),
        n = -0.029,
        Ea = (41.271, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7003,
    label = "i10(882) <=> H_10_(3) + p4(877)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.715e+10, 's^-1'),
        n = 0.858,
        Ea = (25.452, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7004,
    label = "i4(885) <=> i5(890)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+11, 's^-1'),
        n = 0.001,
        Ea = (17.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7005,
    label = "i4(885) <=> H_10_(3) + p2(883)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.447e+10, 's^-1'),
        n = 0.874,
        Ea = (36.168, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7006,
    label = "i5(890) <=> H_10_(3) + p5(891)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.417e+10, 's^-1'),
        n = 0.841,
        Ea = (23.191, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7007,
    label = "i5(890) <=> H_10_(3) + p9(892)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.124e+12, 's^-1'),
        n = 0.476,
        Ea = (47.412, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7008,
    label = "i7(886) <=> p1(878) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.59e+12, 's^-1'),
        n = 0.733,
        Ea = (35.918, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7009,
    label = "i7(886) <=> H_10_(3) + p3(884)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.88e+11, 's^-1'),
        n = 0.972,
        Ea = (40.036, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7010,
    label = "i6(887) <=> H_10_(3) + p2(883)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.539e+11, 's^-1'),
        n = 0.868,
        Ea = (26.827, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: 2012_Kislov_Phenyl_Propene
From 2012 Kislov
""",
)

entry(
    index = 7011,
    label = "W1_2(67) <=> W8_9(893)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(401300, 's^-1'), n=2.064, Ea=(37.093, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7012,
    label = "W1_2(67) <=> W31(894)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.66e+11, 's^-1'), n=0.412, Ea=(27.805, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7013,
    label = "W3_4(69) <=> W13(895)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.915e+06, 's^-1'), n=1.697, Ea=(19.915, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7014,
    label = "W3_4(69) <=> W31(894)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.454e+11, 's^-1'), n=0.447, Ea=(24.536, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7015,
    label = "W5(68) <=> W8_9(893)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(53440, 's^-1'), n=2.305, Ea=(38.286, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7016,
    label = "W6(70) <=> W13(895)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.166e+07, 's^-1'), n=1.625, Ea=(37.367, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7017,
    label = "W6(70) <=> W29(896)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.185e+11, 's^-1'), n=0.586, Ea=(37.614, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7018,
    label = "W8_9(893) <=> W20(897)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(420000, 's^-1'), n=2.094, Ea=(61.014, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7019,
    label = "W8_9(893) <=> W11(898)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.5e+08, 's^-1'), n=0.835, Ea=(58.13, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7020,
    label = "W8_9(893) <=> W15(899)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.63e+12, 's^-1'), n=-0.455, Ea=(30.695, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7021,
    label = "W8_9(893) <=> W21(900)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.45e+06, 's^-1'), n=1.572, Ea=(60.563, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7022,
    label = "W11(898) <=> W21(900)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.286e+08, 's^-1'), n=1.323, Ea=(24.182, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7023,
    label = "W11(898) <=> W29(896)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.241e+10, 's^-1'), n=0.754, Ea=(22.335, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7024,
    label = "W11(898) <=> W20(897)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.37e+08, 's^-1'), n=1.713, Ea=(43.474, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7025,
    label = "W21(900) <=> W22(901)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.999e+07, 's^-1'), n=0.942, Ea=(10.168, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7026,
    label = "W21(900) <=> W24(902)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.932e+07, 's^-1'), n=1.035, Ea=(14.54, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7027,
    label = "W21(900) <=> W20(897)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59980, 's^-1'), n=1.941, Ea=(8.652, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7028,
    label = "W20(897) <=> W18(903)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.258e+10, 's^-1'), n=0.51, Ea=(12.883, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7029,
    label = "W45(904) <=> W23(905)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.315e+10, 's^-1'), n=0.447, Ea=(22.628, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7030,
    label = "W45(904) <=> W24(902)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.713e+10, 's^-1'), n=0.481, Ea=(30.309, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7031,
    label = "C3H4(39) + C6H5(64) <=> W11(898)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4578, 'cm^3/(mol*s)'), n=2.53, Ea=(1.932, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7032,
    label = "C2H2(20) + C7H7(580) <=> W20(897)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (892300, 'cm^3/(mol*s)'),
        n = 2.091,
        Ea = (11.371, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7033,
    label = "H_10_(3) + C9H8(771) <=> W15(899)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.954e+07, 'cm^3/(mol*s)'),
        n = 1.548,
        Ea = (4.985, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7034,
    label = "H_10_(3) + C9H8(771) <=> W22(901)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.514e+08, 'cm^3/(mol*s)'),
        n = 1.545,
        Ea = (3.073, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7035,
    label = "H_10_(3) + C9H8(771) <=> W23(905)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.739e+10, 'cm^3/(mol*s)'),
        n = 0.881,
        Ea = (-0.465, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7036,
    label = "H_10_(3) + C9H8(771) <=> W18(903)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.379e+07, 'cm^3/(mol*s)'),
        n = 1.723,
        Ea = (7.429, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7037,
    label = "H_10_(3) + C9H8(72) <=> W8_9(893)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.339e+08, 'cm^3/(mol*s)'),
        n = 1.587,
        Ea = (2.425, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7038,
    label = "H_10_(3) + C9H8(72) <=> W11(898)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.113e+08, 'cm^3/(mol*s)'),
        n = 1.511,
        Ea = (4.384, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7039,
    label = "H_10_(3) + P4(73) <=> W11(898)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.255e+11, 'cm^3/(mol*s)'),
        n = 1.005,
        Ea = (3.143, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7040,
    label = "H_10_(3) + P4(73) <=> W20(897)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.276e+10, 'cm^3/(mol*s)'),
        n = 1.103,
        Ea = (4.911, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C9H9
""",
)

entry(
    index = 7041,
    label = "C6H5(64) + C4H6(511) <=> S(906)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47900, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (3.991, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2005_Ismail_C6H5_C4H6
""",
)

entry(
    index = 7042,
    label = "S(515) <=> pdt37(783)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(324000, 's^-1'), n=1.64, Ea=(26.436, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2005_Ismail_C6H5_C4H6
""",
)

entry(
    index = 7043,
    label = "S(515) <=> H_10_(3) + pdt13(760)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.61e+07, 's^-1'), n=2.11, Ea=(38.628, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2005_Ismail_C6H5_C4H6
""",
)

entry(
    index = 7044,
    label = "H_10_(3) + S(907) <=> W1(908)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.059e+08, 'cm^3/(mol*s)'),
        n = 1.596,
        Ea = (4.69, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_Indene_CH3
""",
)

entry(
    index = 7045,
    label = "H_10_(3) + S(909) <=> W1(908)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.904e+08, 'cm^3/(mol*s)'),
        n = 1.534,
        Ea = (3.418, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_Indene_CH3
""",
)

entry(
    index = 7046,
    label = "C9H8(771) + CH3(17) <=> W1(908)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3206, 'cm^3/(mol*s)'),
        n = 2.611,
        Ea = (8.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_Indene_CH3
""",
)

entry(
    index = 7047,
    label = "H_10_(3) + S(910) <=> W2(911)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.441e+08, 'cm^3/(mol*s)'),
        n = 1.514,
        Ea = (2.403, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_Indene_CH3
""",
)

entry(
    index = 7048,
    label = "C9H8(771) + CH3(17) <=> W2(911)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5064, 'cm^3/(mol*s)'),
        n = 2.608,
        Ea = (5.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_Indene_CH3
""",
)

entry(
    index = 7049,
    label = "C6H9(912) <=> CPD(595) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.89e+14, 's^-1'), n=0, Ea=(38.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Wang_K_C6H9
""",
)

entry(
    index = 7050,
    label = "C2H3(29) + C4H6(511) <=> C6H9(913)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39130, 'cm^3/(mol*s)'),
        n = 2.404,
        Ea = (0.42, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7051,
    label = "C6H9(913) <=> H_10_(3) + C6H8(914)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.29e+06, 's^-1'), n=2.017, Ea=(40.664, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7052,
    label = "C6H9(913) <=> C6H9(915)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.041e+08, 's^-1'), n=0.7, Ea=(20.246, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7053,
    label = "C6H9(913) <=> C6H9(916)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.249e+08, 's^-1'), n=0.846, Ea=(19.298, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7054,
    label = "C6H9(916) <=> H_10_(3) + C6H8(917)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.972e+07, 's^-1'), n=1.802, Ea=(32.304, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7055,
    label = "C6H9(915) <=> H_10_(3) + C6H8(918)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.487e+08, 's^-1'), n=1.395, Ea=(33.132, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7056,
    label = "C6H9(915) <=> H_10_(3) + C6H8(919)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.097e+09, 's^-1'), n=1.299, Ea=(33.394, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7057,
    label = "C6H9(916) <=> C6H9(920)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.265e-07, 's^-1'), n=5.639, Ea=(24.541, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7058,
    label = "C6H9(916) <=> C6H9(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.537e-16, 's^-1'), n=8.138, Ea=(14.583, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7059,
    label = "C6H9(920) <=> C6H9(912)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.239e-08, 's^-1'), n=6.224, Ea=(24.481, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2015_Buras_Vinyl_1_3_Butadiene
""",
)

entry(
    index = 7060,
    label = "i1(660) <=> inew(921)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4555, 's^-1'),
        n = 3.436,
        Ea = (23.613, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'G3(CC,MP2)//B3LYP/6-311G**',
    ),
    longDesc = 
u"""
Originally from reaction library: New_Phenyl_Propene_Pathway
G3(CC,MP2)//B3LYP/6-311G**
""",
)

entry(
    index = 7061,
    label = "inew(921) <=> i4(885)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (241.9, 's^-1'),
        n = 2.452,
        Ea = (3.561, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'G3(CC,MP2)//B3LYP/6-311G**',
    ),
    longDesc = 
u"""
Originally from reaction library: New_Phenyl_Propene_Pathway
G3(CC,MP2)//B3LYP/6-311G**
""",
)

entry(
    index = 7062,
    label = "i4(885) <=> C2H4(30) + C7H7(580)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.836e+09, 's^-1'),
        n = 1.093,
        Ea = (22.805, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'G3(CC,MP2)//B3LYP/6-311G**',
    ),
    longDesc = 
u"""
Originally from reaction library: New_Phenyl_Propene_Pathway
G3(CC,MP2)//B3LYP/6-311G**
""",
)

entry(
    index = 7063,
    label = "C7H7(580) + C3H3(19) <=> W1(922)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.781e+17, 'cm^3/(mol*s)'),
        n = -1.568,
        Ea = (0.455, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7064,
    label = "C7H7(580) + C3H3(19) <=> W2(923)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.144e+19, 'cm^3/(mol*s)'),
        n = -2.163,
        Ea = (1.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7065,
    label = "W1(922) <=> W4(924)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(2.214e+09, 's^-1'), n=0.749, Ea=(47.859, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7066,
    label = "W4(924) <=> W1(922)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(3.213e+11, 's^-1'), n=0.07, Ea=(18.329, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7067,
    label = "W2(923) <=> W3(925)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(4.484e+11, 's^-1'), n=0.032, Ea=(50.631, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7068,
    label = "W3(925) <=> W2(923)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(3.626e+11, 's^-1'), n=0.119, Ea=(18.066, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7069,
    label = "W4(924) <=> W8(926)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.208e+11, 's^-1'), n=0.001, Ea=(25.838, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7070,
    label = "W8(926) <=> W10(927)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.949e+11, 's^-1'), n=0.486, Ea=(5.464, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7071,
    label = "W10(927) <=> H_10_(3) + P5(928)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.431e+15, 's^-1'), n=-0.34, Ea=(77.615, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7072,
    label = "W2(923) <=> W14(929)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.623e+09, 's^-1'), n=0.522, Ea=(43.633, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7073,
    label = "W14(929) <=> W17(930)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.437e+08, 's^-1'), n=1.045, Ea=(15.153, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7074,
    label = "W17(930) <=> H_10_(3) + P9(931)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.081e+15, 's^-1'), n=-0.263, Ea=(86.584, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7075,
    label = "W17(930) <=> H_10_(3) + P10(932)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.899e+16, 's^-1'), n=-0.42, Ea=(88.738, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7076,
    label = "W14(929) <=> H_10_(3) + P9(931)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.401e+11, 's^-1'), n=0.549, Ea=(19.678, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C3H3_C7H7_Matsugi
""",
)

entry(
    index = 7077,
    label = "W1(933) <=> W4(934)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(264300, 's^-1'), n=1.839, Ea=(33.509, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7078,
    label = "W1(933) <=> W14(935)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.179e+07, 's^-1'), n=1.101, Ea=(27.148, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7079,
    label = "W1(933) <=> W16(936)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 's^-1'), n=2.099, Ea=(35.296, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7080,
    label = "C4H4(444) + C6H5(64) <=> W1(933)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32420, 'cm^3/(mol*s)'),
        n = 2.179,
        Ea = (-0.282, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7081,
    label = "W1(933) <=> H_10_(3) + P2(937)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.456e+08, 's^-1'), n=1.511, Ea=(40.052, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7082,
    label = "W2(938) <=> W8(939)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.69, Ea=(20.376, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7083,
    label = "W2(938) <=> W19(940)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.423e+09, 's^-1'), n=0.834, Ea=(24.235, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7084,
    label = "C4H4(444) + C6H5(64) <=> W2(938)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (392600, 'cm^3/(mol*s)'),
        n = 2.192,
        Ea = (4.297, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7085,
    label = "W3(941) <=> W7(942)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62e+09, 's^-1'), n=1.05, Ea=(31.179, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7086,
    label = "W3(941) <=> W19(940)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.233e+11, 's^-1'), n=0.39, Ea=(35.846, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7087,
    label = "W3(941) <=> W20(943)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.806e+09, 's^-1'), n=1.172, Ea=(51.258, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7088,
    label = "C4H4(444) + C6H5(64) <=> W3(941)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44410, 'cm^3/(mol*s)'),
        n = 2.177,
        Ea = (1.454, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7089,
    label = "W4(934) <=> W5(944)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.09e+08, 's^-1'), n=0.695, Ea=(6.499, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7090,
    label = "W5(944) <=> W6(945)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.346e+08, 's^-1'), n=1.296, Ea=(39.967, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7091,
    label = "W7(942) <=> W6(945)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.983e+12, 's^-1'), n=-0.321, Ea=(5.655, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7092,
    label = "W9(946) <=> W7(942)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(65110, 's^-1'), n=2.209, Ea=(29.053, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7093,
    label = "W17(947) <=> W7(942)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.323e+10, 's^-1'), n=0.901, Ea=(33.428, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7094,
    label = "W9(946) <=> W8(939)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.126e+14, 's^-1'), n=-0.355, Ea=(28.539, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7095,
    label = "W9(946) <=> prod5(823)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.048e+09, 's^-1'), n=0.924, Ea=(30.972, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7096,
    label = "prod5(823) <=> H_10_(3) + P2(937)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.076e+12, 's^-1'), n=0.597, Ea=(36.928, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7097,
    label = "W11(948) <=> prod5(823)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.899e+10, 's^-1'), n=0.97, Ea=(33.321, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7098,
    label = "prod5(823) <=> W20(943)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.56e+08, 's^-1'), n=1.408, Ea=(41.295, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7099,
    label = "W14(935) <=> W15(949)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.881e+08, 's^-1'), n=1.062, Ea=(16.546, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7100,
    label = "W16(936) <=> W15(949)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.443e+10, 's^-1'), n=0.474, Ea=(23.82, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7101,
    label = "W16(936) <=> H_10_(3) + P2(937)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.394e+10, 's^-1'), n=1.133, Ea=(39.957, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7102,
    label = "W7(942) <=> W20(943)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.658e+09, 's^-1'), n=0.699, Ea=(7.063, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7103,
    label = "W20(943) <=> H_10_(3) + P2(937)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.951e+13, 's^-1'), n=0.612, Ea=(49.045, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7104,
    label = "C4H4(444) + C6H5(64) <=> W14(935)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1571, 'cm^3/(mol*s)'), n=2.63, Ea=(2.072, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7105,
    label = "H_10_(3) + C10H8(826) <=> W6(945)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.824e+09, 'cm^3/(mol*s)'),
        n = 1.551,
        Ea = (4.518, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7106,
    label = "H_10_(3) + P4(950) <=> W3(941)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.163e+11, 'cm^3/(mol*s)'),
        n = 1.054,
        Ea = (3.968, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7107,
    label = "H_10_(3) + P4(950) <=> W9(946)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (3.846, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7108,
    label = "H_10_(3) + P5(951) <=> W3(941)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.278e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (5.344, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7109,
    label = "H_10_(3) + P5(951) <=> W20(943)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.149e+09, 'cm^3/(mol*s)'),
        n = 1.595,
        Ea = (4.014, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7110,
    label = "H_10_(3) + P6(952) <=> W14(935)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.081e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (6.797, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7111,
    label = "W14(935) <=> W1(933)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.809e+07, 's^-1'), n=1.057, Ea=(15.061, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C6H5_C4H4_all_TST_rates
""",
)

entry(
    index = 7112,
    label = "W5(953) <=> W6(954)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.57e+10, 's^-1'), n=0.43, Ea=(1.924, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7113,
    label = "W5(953) <=> W8(955)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.311e+09, 's^-1'), n=0.537, Ea=(2.307, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7114,
    label = "W8(955) <=> W13(956)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.588e+10, 's^-1'), n=0.535, Ea=(9.58, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7115,
    label = "W6(954) <=> W13(956)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.53e+12, 's^-1'), n=0.189, Ea=(29.234, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7116,
    label = "W101(957) <=> W8(955)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.964e+07, 's^-1'), n=1.633, Ea=(47.984, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7117,
    label = "W8(955) <=> P10(932)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.429e+08, 's^-1'), n=1.267, Ea=(24.384, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7118,
    label = "W5(953) <=> W103(958)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.193e+07, 's^-1'), n=1.425, Ea=(7.283, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7119,
    label = "W104(959) <=> W6(954)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.09e+11, 's^-1'), n=0.703, Ea=(23.53, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7120,
    label = "P10(932) <=> W103(958)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.017e+13, 's^-1'), n=0.272, Ea=(49.677, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7121,
    label = "W103(958) <=> W104(959)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.69e+10, 's^-1'), n=0.239, Ea=(33.778, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7122,
    label = "W106(960) <=> W107(961)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.423e+08, 's^-1'), n=1.522, Ea=(63.602, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7123,
    label = "W106(960) <=> P5(928)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(68.8, 's^-1'), n=3.351, Ea=(60.931, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7124,
    label = "W107(961) <=> P5(928)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.548e+09, 's^-1'), n=0.934, Ea=(9.114, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7125,
    label = "P5(928) <=> W111(962)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.279e+13, 's^-1'), n=0.395, Ea=(53.699, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7126,
    label = "W6(954) <=> W6(945)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.93e+07, 's^-1'), n=1.684, Ea=(33.806, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7127,
    label = "W13(956) <=> W107(961)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.161e+12, 's^-1'), n=0.277, Ea=(28.025, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7128,
    label = "P5(928) <=> W115(963)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.473e+12, 's^-1'), n=0.247, Ea=(55.262, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7129,
    label = "W111(962) <=> W5(944)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.748e+10, 's^-1'), n=0.262, Ea=(19.926, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7130,
    label = "W115(963) <=> W117(964)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.401e+08, 's^-1'), n=1.453, Ea=(42.614, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7131,
    label = "W117(964) <=> W6(945)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.998e+12, 's^-1'), n=0.237, Ea=(16.277, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7132,
    label = "P10(932) <=> P9(931)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.181e+10, 's^-1'), n=0.964, Ea=(32.063, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7133,
    label = "C2H2(20) + C8H7(75) <=> W5(953)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.12e+07, 'cm^3/(mol*s)'),
        n = 1.489,
        Ea = (4.331, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7134,
    label = "W6(954) <=> H_10_(3) + C10H8(826)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.567e+11, 's^-1'), n=0.787, Ea=(28.205, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7135,
    label = "W8(955) <=> H_10_(3) + P2(965)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.191e+09, 's^-1'), n=1.264, Ea=(30.816, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7136,
    label = "W5(953) <=> H_10_(3) + P5(966)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.304e+10, 's^-1'), n=1.16, Ea=(37.552, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7137,
    label = "W101(957) <=> H_10_(3) + P2(965)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.05e+10, 's^-1'), n=1.329, Ea=(52.477, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7138,
    label = "P10(932) <=> H_10_(3) + P2(965)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.923e+11, 's^-1'), n=0.777, Ea=(40.274, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7139,
    label = "W103(958) <=> H_10_(3) + P105(967)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.568e+11, 's^-1'), n=0.972, Ea=(78.037, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7140,
    label = "W107(961) <=> H_10_(3) + P109(968)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.249e+08, 's^-1'), n=1.2, Ea=(27.426, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7141,
    label = "W106(960) <=> H_10_(3) + P109(968)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.427e+09, 's^-1'), n=1.431, Ea=(66.532, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7142,
    label = "P5(928) <=> H_10_(3) + P109(968)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.893e+15, 's^-1'), n=-0.16, Ea=(65.494, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7143,
    label = "W111(962) <=> H_10_(3) + P114(969)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+16, 's^-1'), n=-0.28, Ea=(68.378, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7144,
    label = "P9(931) <=> H_10_(3) + P2(965)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.234e+12, 's^-1'), n=0.766, Ea=(43.611, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: C10H9_Mebel_TST
""",
)

entry(
    index = 7145,
    label = "C2H2(20) + A3a(76) <=> prod5(823)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (750000, 'cm^3/(mol*s)'),
        n = 1.979,
        Ea = (5.066, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: C10H8_HACA
""",
)

entry(
    index = 7148,
    label = "C6H6(48) + C3H3(19) <=> C9H9(970)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (144.6, 'cm^3/(mol*s)'),
        n = 2.951,
        Ea = (14.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7149,
    label = "C6H6(48) + C3H3(19) <=> C9H9(971)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (312.3, 'cm^3/(mol*s)'),
        n = 2.973,
        Ea = (16.396, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7150,
    label = "C9H9(970) <=> C9H9(972)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.485e+11, 's^-1'), n=0.065, Ea=(27.941, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7151,
    label = "C9H9(971) <=> C9H9(972)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.565e+11, 's^-1'), n=0.009, Ea=(28.521, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7152,
    label = "C9H9(972) <=> C9H9(973)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.527e+10, 's^-1'), n=0.853, Ea=(47.848, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7153,
    label = "C9H9(973) <=> W18(903)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.438e+10, 's^-1'), n=0.625, Ea=(38.324, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7154,
    label = "C9H9(972) <=> C9H9(974)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.231e+11, 's^-1'), n=0.765, Ea=(55.941, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7155,
    label = "C9H9(974) <=> W15(899)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.677e+10, 's^-1'), n=0.839, Ea=(43.638, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7157,
    label = "C9H7(975) <=> C9H7(976)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.534e+11, 's^-1'), n=0.102, Ea=(13.049, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7159,
    label = "C9H7(977) <=> C9H7(976)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.431e+11, 's^-1'), n=0.114, Ea=(15.579, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

entry(
    index = 7160,
    label = "H_10_(3) + C9H7(976) <=> C9H8(771)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: kislovB
""",
)

