#!/usr/bin/env python
# encoding: utf-8

name = "NG_HTP-Ox"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "H_10_(3) + O2_2_(13) <=> O_11_(7) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.286, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 2,
    label = "H2_13_(2) + O_11_(7) <=> H_10_(3) + OH_12_(12)",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.818e+12, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7.948, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (8.792e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19.17, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 3,
    label = "H2_13_(2) + OH_12_(12) <=> H_10_(3) + H2O_14_(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3.43, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 4,
    label = "OH_12_(12) + OH_12_(12) <=> H2O_14_(6) + O_11_(7)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33400, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (-1.93, 'kcal/mol'),
        T0 = (1, 'K'),
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
    index = 9,
    label = "O_11_(7) + O_11_(7) + Ar(15) <=> O2_2_(13) + Ar(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.886e+13, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (-1.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 10,
    label = "O_11_(7) + O_11_(7) + He(16) <=> O2_2_(13) + He(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.886e+13, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (-1.788, 'kcal/mol'),
        T0 = (1, 'K'),
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
    index = 13,
    label = "H2O_14_(6) + H2O_14_(6) <=> H_10_(3) + H2O_14_(6) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.006e+26, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120.18, 'kcal/mol'),
        T0 = (1, 'K'),
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
    index = 15,
    label = "H_10_(3) + HO2_17_(5) <=> H2_13_(2) + O2_2_(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.75e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (-1.451, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 16,
    label = "H_10_(3) + HO2_17_(5) <=> OH_12_(12) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.079e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.295, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 17,
    label = "HO2_17_(5) + O_11_(7) <=> OH_12_(12) + O2_2_(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.724, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 18,
    label = "HO2_17_(5) + OH_12_(12) <=> H2O_14_(6) + O2_2_(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 19,
    label = "HO2_17_(5) + HO2_17_(5) <=> O2_2_(13) + H2O2(15)",
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
    index = 21,
    label = "H_10_(3) + H2O2(15) <=> H2O_14_(6) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3.97, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 22,
    label = "H_10_(3) + H2O2(15) <=> H2_13_(2) + HO2_17_(5)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.95, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 23,
    label = "O_11_(7) + H2O2(15) <=> HO2_17_(5) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3.97, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: BurkeH2O2inN2
""",
)

entry(
    index = 24,
    label = "OH_12_(12) + H2O2(15) <=> HO2_17_(5) + H2O_14_(6)",
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
    index = 26,
    label = "H_10_(3) + HO2_17_(5) <=> H2O_14_(6) + O_11_(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.632e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 29,
    label = "O2_2_(13) + CO_21_(14) <=> O_11_(7) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.533e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 30,
    label = "OH_12_(12) + CO_21_(14) <=> H_10_(3) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (61870, 'cm^3/(mol*s)'),
                n = 2.053,
                Ea = (-0.356, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.017e+12, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (0.332, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 31,
    label = "HO2_17_(5) + CO_21_(14) <=> CO2_5_(8) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17.944, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 32,
    label = "H2O_14_(6) + CO_21_(14) <=> H2_13_(2) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.538, -0.6739, -0.1899, -0.003739],
            [10.65, 0.6945, 0.1383, -0.02884],
            [0.115, 0.01101, 0.05622, 0.02215],
            [0.01104, -0.04253, -0.008895, 0.007327],
            [0.00552, -0.01416, -0.009418, -0.002118],
            [0.003977, -0.001495, -0.002421, -0.001664],
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
    index = 35,
    label = "O_11_(7) + CH3(17) <=> H2_13_(2) + H_10_(3) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.384e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 36,
    label = "HO2_17_(5) + CH3(17) <=> Cadd(4) + O2_2_(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126900, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3.022, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 39,
    label = "Cadd(4) + O_11_(7) <=> OH_12_(12) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (8.485, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 40,
    label = "Cadd(4) + OH_12_(12) <=> H2O_14_(6) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (983900, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2.446, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 41,
    label = "Cadd(4) + HO2_17_(5) <=> H2O2(15) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47780, 'cm^3/(mol*s)'), n=2.5, Ea=(21, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 44,
    label = "H2O2(15) + C6H13(77) <=> HO2_17_(5) + C6H14(10)",
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
    index = 45,
    label = "O_11_(7) + C6H14(10) <=> OH_12_(12) + C6H13(77)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (95600, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 46,
    label = "C6H14(10) + OH_12_(12) <=> H2O_14_(6) + C6H13(77)",
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
    index = 47,
    label = "C6H14(10) + O2_2_(13) <=> HO2_17_(5) + C6H13(77)",
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
    index = 50,
    label = "O2_2_(13) + C3H7(35) <=> HO2_17_(5) + C3H6(38)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O2b;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 53,
    label = "OH_12_(12) + C3H7(35) <=> H2O_14_(6) + C3H6(38)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 54,
    label = "HO2_17_(5) + C3H7(35) <=> C3H6(38) + H2O2(15)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 56,
    label = "O_11_(7) + C3H7(35) <=> OH_12_(12) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 61,
    label = "CCadd(1) + O_11_(7) <=> OH_12_(12) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (176300, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (5.803, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 62,
    label = "CCadd(1) + OH_12_(12) <=> H2O_14_(6) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.463e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (0.994, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 64,
    label = "CCadd(1) + O2_2_(13) <=> HO2_17_(5) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (729000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (49.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 65,
    label = "CCadd(1) + HO2_17_(5) <=> C2H5(31) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (16.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 74,
    label = "O_11_(7) + C2H5(31) <=> OH_12_(12) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.94e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 75,
    label = "O2_2_(13) + C2H5(31) <=> HO2_17_(5) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.355e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1.975, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 80,
    label = "OH_12_(12) + C2H5(31) <=> H2O_14_(6) + C2H4(30)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 81,
    label = "HO2_17_(5) + C2H5(31) <=> C2H4(30) + H2O2(15)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 84,
    label = "HO2_17_(5) + C3H7(79) <=> C3H6(38) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.007e+10, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 89,
    label = "O2_2_(13) + C3H7(79) <=> HO2_17_(5) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.735e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 24',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 24
""",
)

entry(
    index = 90,
    label = "OH_12_(12) + C3H7(79) <=> H2O_14_(6) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.446e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 92,
    label = "O_11_(7) + C3H7(79) <=> OH_12_(12) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.361e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
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
    index = 98,
    label = "O2_2_(13) + C4H9(37) <=> HO2_17_(5) + C4H8(78)",
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
    index = 99,
    label = "OH_12_(12) + C4H9(37) <=> H2O_14_(6) + C4H8(78)",
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
    index = 101,
    label = "HO2_17_(5) + C3H5(41) <=> O2_2_(13) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd\\H_Cd\\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\\H_Cd\\H2]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;C_rad/H2/Cd\H_Cd\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\H_Cd\H2]
""",
)

entry(
    index = 103,
    label = "C3H5(41) + H2O2(15) <=> HO2_17_(5) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0351, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 539 H2O2 + C3H5 <=> HO2 + C3H6 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Matched reaction 539 H2O2 + C3H5 <=> HO2 + C3H6 in H_Abstraction/training
""",
)

entry(
    index = 108,
    label = "OH_12_(12) + C3H6(38) <=> H2O_14_(6) + C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.469, 'cm^3/(mol*s)'),
        n = 3.792,
        Ea = (0.265, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/Cd;O_pri_rad] + [C/H3/Cd\\H_Cd\\H2;O_rad] for rate rule [C/H3/Cd\\H_Cd\\H2;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [C/H3/Cd;O_pri_rad] + [C/H3/Cd\H_Cd\H2;O_rad] for rate rule [C/H3/Cd\H_Cd\H2;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 110,
    label = "O_11_(7) + C3H6(38) <=> OH_12_(12) + C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.9017, 'cm^3/(mol*s)'),
        n = 3.899,
        Ea = (3.039, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd\\H_Cd\\H2;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Cd\\H_Cd\\H2;O_atom_triplet]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd\H_Cd\H2;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Cd\H_Cd\H2;O_atom_triplet]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 120,
    label = "O_11_(7) + C3H5(41) <=> OH_12_(12) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.684e+09, 'cm^3/(mol*s)'),
        n = 0.625,
        Ea = (-0.237, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad_birad_trirad_quadrad;Cdpri_Csrad] + [O_atom_triplet;XH_s_Rrad] for rate rule [O_atom_triplet;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [Y_rad_birad_trirad_quadrad;Cdpri_Csrad] + [O_atom_triplet;XH_s_Rrad] for rate rule [O_atom_triplet;Cdpri_Csrad]
""",
)

entry(
    index = 122,
    label = "OH_12_(12) + C3H5(41) <=> H2O_14_(6) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 123,
    label = "O2_2_(13) + C3H5(41) <=> HO2_17_(5) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cdpri_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O2b;Cdpri_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 124,
    label = "HO2_17_(5) + C3H5(41) <=> C3H4(39) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.008e+09, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (2.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cdpri_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cdpri_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cdpri_Csrad]
""",
)

entry(
    index = 127,
    label = "H_10_(3) + CH2OH(32) <=> OH_12_(12) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.006e+13, 'cm^3/(mol*s)'),
        n = 0.198,
        Ea = (-0.241, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 131,
    label = "O_11_(7) + CH3(17) <=> H_10_(3) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.722e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 132,
    label = "OH_12_(12) + CH3(17) <=> H2_13_(2) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.735e+09, 'cm^3/(mol*s)'),
        n = 0.734,
        Ea = (-2.177, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 133,
    label = "O2_2_(13) + CH3(17) <=> OH_12_(12) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (99.77, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (9.768, 'kcal/mol'),
        T0 = (1, 'K'),
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
    index = 135,
    label = "H_10_(3) + CH2OH(32) <=> H2_13_(2) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 136,
    label = "O_11_(7) + CH2OH(32) <=> OH_12_(12) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 137,
    label = "OH_12_(12) + CH2OH(32) <=> H2O_14_(6) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 138,
    label = "O2_2_(13) + CH2OH(32) <=> HO2_17_(5) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.298e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.736, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 139,
    label = "CH2OH(32) + CH3(17) <=> Cadd(4) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 140,
    label = "OH_12_(12) + C2H4(30) <=> CH2O(25) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178000, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 141,
    label = "O_11_(7) + C2H5(31) <=> CH2O(25) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 142,
    label = "C2H5(31) + CH2OH(32) <=> CCadd(1) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 143,
    label = "HO2_17_(5) + CH2OH(32) <=> CH2O(25) + H2O2(15)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 144,
    label = "CH2OH(32) + C3H5(41) <=> CH2O(25) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cd;O_Csrad]
""",
)

entry(
    index = 147,
    label = "C3H5(65) + H2O2(15) <=> HO2_17_(5) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [H2O2;Cd_Cd\\H\\Cs_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [H2O2;Cd_Cd\H\Cs_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 148,
    label = "OH_12_(12) + C3H5(65) <=> O_11_(7) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Cd_Cd\\H\\Cs_pri_rad] for rate rule [OH_rad_H;Cd_Cd\\H\\Cs_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Cd_Cd\H\Cs_pri_rad] for rate rule [OH_rad_H;Cd_Cd\H\Cs_pri_rad]
""",
)

entry(
    index = 149,
    label = "OH_12_(12) + C3H6(38) <=> H2O_14_(6) + C3H5(65)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.026e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.94, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri;O_pri_rad] for rate rule [Cd/H2/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri;O_pri_rad] for rate rule [Cd/H2/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 150,
    label = "HO2_17_(5) + C3H5(65) <=> O2_2_(13) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cd\\H\\Cs_pri_rad] for rate rule [Orad_O_H;Cd_Cd\\H\\Cs_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_Cd\H\Cs_pri_rad] for rate rule [Orad_O_H;Cd_Cd\H\Cs_pri_rad]
""",
)

entry(
    index = 161,
    label = "CH2OH(32) + C6H13(77) <=> C6H14(10) + CH2O(25)",
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
    index = 162,
    label = "CH2OH(32) + C3H5(65) <=> CH2O(25) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 163,
    label = "OH_12_(12) + C2H2(20) <=> CO_21_(14) + CH3(17)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (475700, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (-0.33, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.372e+06, 'cm^3/(mol*s)'),
                n = 1.4,
                Ea = (0.227, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.648e+07, 'cm^3/(mol*s)'),
                n = 1.05,
                Ea = (1.115, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.277e+09, 'cm^3/(mol*s)'),
                n = 0.73,
                Ea = (2.579, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.312e+08, 'cm^3/(mol*s)'),
                n = 0.92,
                Ea = (3.736, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (825000, 'cm^3/(mol*s)'),
                n = 1.77,
                Ea = (4.698, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Originally from reaction library: 2005_Senosiain_OH_C2H2
""",
)

entry(
    index = 166,
    label = "HO2_17_(5) + C3H3(19) <=> O2_2_(13) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (16.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]
""",
)

entry(
    index = 169,
    label = "O_11_(7) + C3H4(39) <=> OH_12_(12) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18610, 'cm^3/(mol*s)'),
        n = 2.824,
        Ea = (6.568, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_H;O_atom_triplet] + [Cd_Cdd/H2;Y_rad_birad_trirad_quadrad] for rate rule [Cd_Cdd/H2;O_atom_triplet]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [Cd_H;O_atom_triplet] + [Cd_Cdd/H2;Y_rad_birad_trirad_quadrad] for rate rule [Cd_Cdd/H2;O_atom_triplet]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 170,
    label = "OH_12_(12) + C3H4(39) <=> H2O_14_(6) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0084, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 171,
    label = "H2O2(15) + C3H3(19) <=> HO2_17_(5) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.323, 'cm^3/(mol*s)'),
        n = 3.555,
        Ea = (-5.755, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_rad] for rate rule [H2O2;Cd_Cdd_rad/H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;Cd_rad] for rate rule [H2O2;Cd_Cdd_rad/H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 176,
    label = "CH2OH(32) + C3H3(19) <=> CH2O(25) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 179,
    label = "OH_12_(12) + C3H3(19) <=> CO_21_(14) + C2H4(30)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.97, -0.9281, -0.3308, -0.04047],
            [0.2764, 0.8318, 0.3068, 0.01134],
            [-0.1642, -0.03297, 0.03881, 0.03034],
            [-0.08224, -0.06899, -0.021, 0.004832],
            [-0.01629, -0.0177, -0.01138, -0.001331],
            [0.003668, 0.003921, -0.001432, -0.00114],
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
    index = 185,
    label = "H_10_(3) + HCO(22) <=> H2_13_(2) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.482e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 186,
    label = "O_11_(7) + HCO(22) <=> OH_12_(12) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 187,
    label = "O_11_(7) + HCO(22) <=> H_10_(3) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.001e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 188,
    label = "OH_12_(12) + HCO(22) <=> H2O_14_(6) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.199e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 189,
    label = "O2_2_(13) + HCO(22) <=> HO2_17_(5) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.562e+10, 'cm^3/(mol*s)'),
        n = 0.521,
        Ea = (-0.521, 'kcal/mol'),
        T0 = (1, 'K'),
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
    index = 191,
    label = "H_10_(3) + CH2O(25) <=> H2_13_(2) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.149e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 192,
    label = "O_11_(7) + CH2O(25) <=> OH_12_(12) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.244e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2.762, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 193,
    label = "OH_12_(12) + CH2O(25) <=> H2O_14_(6) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.338e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 194,
    label = "O2_2_(13) + CH2O(25) <=> HO2_17_(5) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (329700, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (36.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 195,
    label = "HO2_17_(5) + CH2O(25) <=> HCO(22) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71110, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 196,
    label = "HCO(22) + CH3(17) <=> Cadd(4) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 197,
    label = "CH2O(25) + CH3(17) <=> Cadd(4) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32.13, 'cm^3/(mol*s)'), n=3.36, Ea=(4.31, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 198,
    label = "O_11_(7) + C2H4(30) <=> HCO(22) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.355e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (0.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 199,
    label = "CH2O(25) + C2H5(31) <=> CCadd(1) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 200,
    label = "HCO(22) + C2H5(31) <=> CH2O(25) + C2H4(30)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 201,
    label = "HCO(22) + CH2OH(32) <=> CH2O(25) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO_pri_rad;O_Csrad]
""",
)

entry(
    index = 202,
    label = "C3H7(35) + HCO(22) <=> CH2O(25) + C3H6(38)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;C/H2/Nd_Csrad] for rate rule [CO_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 203,
    label = "CH2O(25) + C3H3(19) <=> HCO(22) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.78, 'cm^3/(mol*s)'),
        n = 3.575,
        Ea = (11.095, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;Cd_Cdd_rad/H] + [CO_pri;Cd_rad] for rate rule [CO_pri;Cd_Cdd_rad/H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [X_H;Cd_Cdd_rad/H] + [CO_pri;Cd_rad] for rate rule [CO_pri;Cd_Cdd_rad/H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 204,
    label = "HCO(22) + C3H5(41) <=> CH2O(25) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cdpri_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [Y_rad;Cdpri_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 205,
    label = "H2_13_(2) + CO2_5_(8) <=> OH_12_(12) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.548, -0.06038, -0.03983, -0.02014],
            [16.52, 0.06983, 0.04538, 0.0223],
            [-0.0855, -0.00998, -0.005736, -0.002106],
            [-0.02595, -0.002072, -0.001602, -0.001027],
            [-0.009506, -0.0002373, -0.0001824, -0.0001184],
            [-0.003808, -1.682e-05, -9.017e-06, -2.553e-06],
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
    index = 206,
    label = "HCO(22) + C3H7(79) <=> CH2O(25) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.903e+14, 'cm^3/(mol*s)'),
        n = -0.096,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cmethyl_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 207,
    label = "HCO(22) + C4H9(37) <=> CH2O(25) + C4H8(78)",
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
    index = 208,
    label = "CH2O(25) + C3H5(41) <=> HCO(22) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0613, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (12.22, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri;C_rad/H2/Cd] for rate rule [CO_pri;C_rad/H2/Cd\\H_Cd\\H2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri;C_rad/H2/Cd] for rate rule [CO_pri;C_rad/H2/Cd\H_Cd\H2]
Multiplied by reaction path degeneracy 2
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
    index = 212,
    label = "CH2O(25) + C2H3(29) <=> HCO(22) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5400, 'cm^3/(mol*s)'), n=2.81, Ea=(5.862, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 216,
    label = "OH_12_(12) + C2H3(29) <=> H2O_14_(6) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 217,
    label = "OH_12_(12) + C2H3(29) <=> HCO(22) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 218,
    label = "O2_2_(13) + C2H3(29) <=> HCO(22) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.936e+15, 'cm^3/(mol*s)'),
        n = -0.959,
        Ea = (0.58, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 219,
    label = "O2_2_(13) + C2H3(29) <=> HO2_17_(5) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44, 'cm^3/(mol*s)'), n=2.95, Ea=(0.186, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 222,
    label = "OH_12_(12) + C2H4(30) <=> H2O_14_(6) + C2H3(29)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21440, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (2.216, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 224,
    label = "O2_2_(13) + C2H4(30) <=> HO2_17_(5) + C2H3(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(60.01, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 225,
    label = "OH_12_(12) + C2H3(29) <=> O_11_(7) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003692, 'cm^3/(mol*s)'),
        n = 4.35,
        Ea = (3.702, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Cd_Cd\\H2_pri_rad] for rate rule [OH_rad_H;Cd_Cd\\H2_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Cd_Cd\H2_pri_rad] for rate rule [OH_rad_H;Cd_Cd\H2_pri_rad]
""",
)

entry(
    index = 228,
    label = "C2H3(29) + H2O2(15) <=> HO2_17_(5) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_pri_rad] for rate rule [H2O2;Cd_Cd\\H2_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;Cd_pri_rad] for rate rule [H2O2;Cd_Cd\H2_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 230,
    label = "C2H3(29) + CH2OH(32) <=> CH2O(25) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 232,
    label = "HO2_17_(5) + C2H3(29) <=> C2H2(20) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 235,
    label = "HCO(22) + C2H3(29) <=> C2H2(20) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 237,
    label = "O_11_(7) + C2H3(29) <=> OH_12_(12) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 241,
    label = "OH_12_(12) + C3H3(19) <=> HCO(22) + C2H3(29)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.09, -0.8416, -0.3029, -0.0433],
            [0.5738, 0.768, 0.3034, 0.02176],
            [-0.1145, -0.0598, 0.02457, 0.02909],
            [-0.07326, -0.06413, -0.02416, 0.002695],
            [-0.01621, -0.01264, -0.01077, -0.001966],
            [0.001711, 0.005068, -0.000869, -0.001194],
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
    index = 251,
    label = "OH_12_(12) + C2H2(20) <=> H2O_14_(6) + C2H(21)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.632e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17.062, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: 2005_Senosiain_OH_C2H2
""",
)

entry(
    index = 252,
    label = "C2H(21) + CH2O(25) <=> C2H2(20) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5400, 'cm^3/(mol*s)'), n=2.81, Ea=(5.862, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 256,
    label = "O2_2_(13) + C2H(21) <=> CO_21_(14) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 257,
    label = "HO2_17_(5) + C2H(21) <=> O2_2_(13) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.067e+11, 'cm^3/(mol*s)'),
        n = 0.263,
        Ea = (1.555, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Ct_rad] for rate rule [Orad_O_H;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;Ct_rad] for rate rule [Orad_O_H;Ct_rad/Ct]
""",
)

entry(
    index = 260,
    label = "C2H(21) + H2O2(15) <=> HO2_17_(5) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01381, 'cm^3/(mol*s)'),
        n = 4.118,
        Ea = (1.722, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Y_rad] for rate rule [H2O2;Ct_rad/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;Y_rad] for rate rule [H2O2;Ct_rad/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 262,
    label = "C2H(21) + CH2OH(32) <=> C2H2(20) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1 C2H + CH3O <=> C2H2 + CH2O in Disproportionation/training',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Matched reaction 1 C2H + CH3O <=> C2H2 + CH2O in Disproportionation/training
""",
)

entry(
    index = 263,
    label = "OH_12_(12) + C3H3(19) <=> C2H(21) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.51, -0.163, -0.09482, -0.03694],
            [5.707, 0.1992, 0.1113, 0.03894],
            [-0.1052, -0.02998, -0.01134, 0.001329],
            [-0.04426, -0.01427, -0.01001, -0.005366],
            [-0.01685, 1.704e-05, -0.0006864, -0.001009],
            [-0.006755, 0.001996, 0.001288, 0.0006077],
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
    index = 276,
    label = "OH_12_(12) + C3H4(45) <=> H2O_14_(6) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.453e+06, 'cm^3/(mol*s)'),
        n = 1.916,
        Ea = (3.086, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 279,
    label = "H2O2(15) + C3H3(19) <=> HO2_17_(5) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.3245, 'cm^3/(mol*s)'),
        n = 3.75,
        Ea = (5.455, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;C_pri_rad] for rate rule [H2O2;C_rad/H2/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;C_pri_rad] for rate rule [H2O2;C_rad/H2/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 280,
    label = "CH2O(25) + C3H3(19) <=> C3H4(45) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18.36, 'cm^3/(mol*s)'),
        n = 3.38,
        Ea = (9.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri;C_pri_rad] for rate rule [CO_pri;C_rad/H2/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_pri;C_pri_rad] for rate rule [CO_pri;C_rad/H2/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 282,
    label = "O_11_(7) + C3H4(45) <=> OH_12_(12) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3590, 'cm^3/(mol*s)'),
        n = 2.973,
        Ea = (5.078, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_pri;O_atom_triplet] + [C/H3/Ct;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Ct;O_atom_triplet]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [C_pri;O_atom_triplet] + [C/H3/Ct;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Ct;O_atom_triplet]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 284,
    label = "HO2_17_(5) + C3H3(19) <=> O2_2_(13) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.03522, 'cm^3/(mol*s)'),
        n = 4.144,
        Ea = (12.506, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Ct] for rate rule [Orad_O_H;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;C_rad/H2/Ct] for rate rule [Orad_O_H;C_rad/H2/Ct]
""",
)

entry(
    index = 286,
    label = "CH2OH(32) + C3H3(19) <=> C3H4(45) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/Ct;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/Ct;O_Csrad]
""",
)

entry(
    index = 300,
    label = "OH_12_(12) + C3H5(65) <=> H2O_14_(6) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 307,
    label = "HCO(22) + C3H5(65) <=> C3H4(45) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 312,
    label = "C3H5(66) + H2O2(15) <=> HO2_17_(5) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_rad/NonDeC] for rate rule [H2O2;Cd_Cd\\H2_rad/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H2O2;Cd_rad/NonDeC] for rate rule [H2O2;Cd_Cd\H2_rad/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 313,
    label = "O_11_(7) + C3H6(38) <=> OH_12_(12) + C3H5(66)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7.63, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd/H/NonDeC;O_atom_triplet]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd/H/NonDeC;O_atom_triplet]
""",
)

entry(
    index = 314,
    label = "OH_12_(12) + C3H6(38) <=> H2O_14_(6) + C3H5(66)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.11e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd/H/NonDeC;O_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd/H/NonDeC;O_pri_rad]
""",
)

entry(
    index = 315,
    label = "HO2_17_(5) + C3H5(66) <=> O2_2_(13) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0006309, 'cm^3/(mol*s)'),
        n = 4.48,
        Ea = (2.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cd\\H2_rad/Cs] for rate rule [Orad_O_H;Cd_Cd\\H2_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_Cd\H2_rad/Cs] for rate rule [Orad_O_H;Cd_Cd\H2_rad/Cs]
""",
)

entry(
    index = 324,
    label = "HO2_17_(5) + C3H5(66) <=> C3H4(39) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.248e+07, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 329,
    label = "O2_2_(13) + C3H5(66) <=> HO2_17_(5) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.99, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;Cmethyl_Rrad] for rate rule [O2b;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Estimated using template [O2b;Cmethyl_Rrad] for rate rule [O2b;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 330,
    label = "OH_12_(12) + C3H5(66) <=> H2O_14_(6) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 332,
    label = "O_11_(7) + C3H5(66) <=> OH_12_(12) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 339,
    label = "CH2OH(32) + C3H5(66) <=> CH2O(25) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 340,
    label = "HCO(22) + C3H5(66) <=> CH2O(25) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 349,
    label = "OH_12_(12) + C3H5(66) <=> H2O_14_(6) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 355,
    label = "HCO(22) + C3H5(66) <=> C3H4(45) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 371,
    label = "O2_2_(13) + H2CC(27) <=> HCO(22) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.124e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 375,
    label = "HO2_17_(5) + C4H7(85) <=> O2_2_(13) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cd\\H\\Cs_rad/Cs] for rate rule [Orad_O_H;Cd_Cd\\H\\Cs_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_Cd\H\Cs_rad/Cs] for rate rule [Orad_O_H;Cd_Cd\H\Cs_rad/Cs]
""",
)

entry(
    index = 384,
    label = "CH2OH(32) + C4H7(85) <=> CH2O(25) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 394,
    label = "OH_12_(12) + C4H7(85) <=> H2O_14_(6) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 402,
    label = "HCO(22) + C4H7(85) <=> CH2O(25) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 408,
    label = "O_11_(7) + CH2(S)(28) <=> H_10_(3) + H_10_(3) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 409,
    label = "OH_12_(12) + CH2(S)(28) <=> H_10_(3) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 411,
    label = "H2O_14_(6) + CH2(S)(28) <=> H2_13_(2) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.67e+21, 'cm^3/(mol*s)'),
        n = -3.134,
        Ea = (3.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 412,
    label = "CO2_5_(8) + CH2(S)(28) <=> CO_21_(14) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 413,
    label = "CH2O(25) + CH2(S)(28) <=> HCO(22) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 414,
    label = "OH_12_(12) + CH3(17) <=> H2O_14_(6) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.81e+15, 'cm^3/(mol*s)'),
        n = -0.91,
        Ea = (0.546, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 416,
    label = "H_10_(3) + CH2OH(32) <=> H2O_14_(6) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+11, 'cm^3/(mol*s)'),
        n = 0.516,
        Ea = (0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 424,
    label = "CH2O(25) + CH3(17) <=> CH2(S)(28) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.676, -9.271e-05, -6.453e-05, -3.583e-05],
            [13.64, 8.813e-06, 6.134e-06, 3.406e-06],
            [0.09091, -4.388e-06, -3.054e-06, -1.696e-06],
            [0.02532, 1.775e-05, 1.235e-05, 6.857e-06],
            [0.005281, 1.286e-05, 8.953e-06, 4.971e-06],
            [0.0007736, 5.451e-06, 3.794e-06, 2.106e-06],
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
    index = 425,
    label = "HO2_17_(5) + CH3(17) <=> CH2(S)(28) + H2O2(15)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.179, -0.04021, -0.02705, -0.01416],
            [5.109, 0.04729, 0.03148, 0.01618],
            [0.07937, -0.009917, -0.006289, -0.002938],
            [0.009613, -0.002037, -0.001515, -0.0009264],
            [-0.002594, 0.0005387, 0.0003466, 0.0001662],
            [-0.00414, 2.564e-05, 2.915e-05, 2.641e-05],
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
    index = 448,
    label = "OH_12_(12) + C6H7(56) <=> H2O_14_(6) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 455,
    label = "HCO(22) + C6H7(56) <=> CH2O(25) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 465,
    label = "OH_12_(12) + C6H7(53) <=> H2O_14_(6) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 472,
    label = "HCO(22) + C6H7(53) <=> CH2O(25) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 479,
    label = "OH_12_(12) + C6H7(52) <=> H2O_14_(6) + C6H6(54)",
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
    index = 486,
    label = "HCO(22) + C6H7(52) <=> CH2O(25) + C6H6(54)",
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
    index = 493,
    label = "HO2_17_(5) + C3H3(86) <=> O2_2_(13) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.067e+11, 'cm^3/(mol*s)'),
        n = 0.263,
        Ea = (1.555, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Ct_rad] for rate rule [Orad_O_H;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Ct_rad] for rate rule [Orad_O_H;Ct_rad/Ct]
""",
)

entry(
    index = 502,
    label = "CH2OH(32) + C3H3(86) <=> C3H4(45) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct_rad/Ct;O_Csrad from training reaction 1\nExact match found for rate rule [Ct_rad/Ct;O_Csrad]',
    ),
    longDesc = 
u"""
Ct_rad/Ct;O_Csrad from training reaction 1
Exact match found for rate rule [Ct_rad/Ct;O_Csrad]
""",
)

entry(
    index = 518,
    label = "OH_12_(12) + C6H7(55) <=> H2O_14_(6) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.598e+11, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (1.005, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]
""",
)

entry(
    index = 525,
    label = "HCO(22) + C6H7(55) <=> CH2O(25) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [CO_pri_rad;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [CO_pri_rad;C/H/DeDe_Csrad]
""",
)

entry(
    index = 543,
    label = "OH_12_(12) + C4H3(96) <=> H2O_14_(6) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 544,
    label = "OH_12_(12) + cyC6H7(58) <=> H2O_14_(6) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 545,
    label = "O_11_(7) + C4H3(96) <=> OH_12_(12) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
""",
)

entry(
    index = 546,
    label = "O_11_(7) + cyC6H7(58) <=> OH_12_(12) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 558,
    label = "HCO(22) + cyC6H7(58) <=> CH2O(25) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 571,
    label = "OH_12_(12) + C4H3(110) <=> H2O_14_(6) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 572,
    label = "O_11_(7) + C4H3(110) <=> OH_12_(12) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 587,
    label = "OH_12_(12) + C6H6(48) <=> H2O_14_(6) + C6H5(64)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3988, 'cm^3/(mol*s)'),
        n = 3.048,
        Ea = (5.843, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 588,
    label = "HO2_17_(5) + C6H5(64) <=> O2_2_(13) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02545, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (9.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]
""",
)

entry(
    index = 595,
    label = "CH2OH(32) + C6H5(64) <=> CH2O(25) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
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
    index = 618,
    label = "HO2_17_(5) + C6H5(105) <=> O2_2_(13) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.514, 'cm^3/(mol*s)'),
        n = 3.539,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]
""",
)

entry(
    index = 627,
    label = "CH2OH(32) + C6H5(105) <=> CH2O(25) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 667,
    label = "OH_12_(12) + C5H5(117) <=> H2O_14_(6) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 668,
    label = "OH_12_(12) + A3a(76) <=> H2O_14_(6) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 669,
    label = "OH_12_(12) + C8H7(131) <=> H2O_14_(6) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 670,
    label = "O_11_(7) + A3a(76) <=> OH_12_(12) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
""",
)

entry(
    index = 671,
    label = "O_11_(7) + C8H7(131) <=> OH_12_(12) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 686,
    label = "HCO(22) + A3a(76) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 687,
    label = "HCO(22) + C8H7(131) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 708,
    label = "OH_12_(12) + C5H5(127) <=> H2O_14_(6) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 732,
    label = "OH_12_(12) + C5H5(129) <=> H2O_14_(6) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 744,
    label = "OH_12_(12) + C8H7(134) <=> H2O_14_(6) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 745,
    label = "O_11_(7) + C8H7(134) <=> OH_12_(12) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 752,
    label = "HCO(22) + C8H7(134) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 764,
    label = "OH_12_(12) + C8H7(135) <=> H2O_14_(6) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 765,
    label = "O_11_(7) + C8H7(135) <=> OH_12_(12) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 772,
    label = "HCO(22) + C8H7(135) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 783,
    label = "OH_12_(12) + C5H5(137) <=> H2O_14_(6) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
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
    index = 796,
    label = "HO2_17_(5) + C5H3(141) <=> O2_2_(13) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.03522, 'cm^3/(mol*s)'),
        n = 4.144,
        Ea = (12.506, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Ct] for rate rule [Orad_O_H;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Ct] for rate rule [Orad_O_H;C_rad/H2/Ct]
""",
)

entry(
    index = 818,
    label = "OH_12_(12) + C5H4(130) <=> H2O_14_(6) + C5H3(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.453e+06, 'cm^3/(mol*s)'),
        n = 1.916,
        Ea = (2.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 829,
    label = "OH_12_(12) + C8H7(136) <=> H2O_14_(6) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 830,
    label = "O_11_(7) + C8H7(136) <=> OH_12_(12) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 837,
    label = "HCO(22) + C8H7(136) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 848,
    label = "HO2_17_(5) + C5H3(142) <=> O2_2_(13) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.067e+11, 'cm^3/(mol*s)'),
        n = 0.263,
        Ea = (1.555, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Ct_rad] for rate rule [Orad_O_H;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Ct_rad] for rate rule [Orad_O_H;Ct_rad/Ct]
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
    index = 889,
    label = "OH_12_(12) + C5H4(158) <=> H2O_14_(6) + C5H3(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2239, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (8.947, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_H;O_pri_rad] + [Cd_allenic;O_rad] for rate rule [Cd_allenic;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_H;O_pri_rad] + [Cd_allenic;O_rad] for rate rule [Cd_allenic;O_pri_rad]
""",
)

entry(
    index = 898,
    label = "OH_12_(12) + C5H4(158) <=> H2O_14_(6) + C5H3(162)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0042, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 907,
    label = "OH_12_(12) + C5H5(129) <=> H2O_14_(6) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 950,
    label = "OH_12_(12) + C5H5(97) <=> H2O_14_(6) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 964,
    label = "OH_12_(12) + C5H4(138) <=> H2O_14_(6) + C5H3(141)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0084, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 975,
    label = "OH_12_(12) + C8H7(147) <=> H2O_14_(6) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad/H/Cd] for rate rule [O_pri_rad;C/H/DeDe_Csrad/H/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad/H/Cd] for rate rule [O_pri_rad;C/H/DeDe_Csrad/H/Cd]
""",
)

entry(
    index = 976,
    label = "O_11_(7) + C8H7(147) <=> OH_12_(12) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H/DeDe_Csrad/H/Cd] for rate rule [O_atom_triplet;C/H/DeDe_Csrad/H/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H/DeDe_Csrad/H/Cd] for rate rule [O_atom_triplet;C/H/DeDe_Csrad/H/Cd]
""",
)

entry(
    index = 983,
    label = "HCO(22) + C8H7(147) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad/H/Cd] for rate rule [CO_pri_rad;C/H/DeDe_Csrad/H/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad/H/Cd] for rate rule [CO_pri_rad;C/H/DeDe_Csrad/H/Cd]
""",
)

entry(
    index = 1000,
    label = "OH_12_(12) + C5H5(127) <=> H2O_14_(6) + C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1001,
    label = "OH_12_(12) + C5H5(128) <=> H2O_14_(6) + C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 1007,
    label = "OH_12_(12) + C8H6(74) <=> H2O_14_(6) + R1(63)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.44e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1008,
    label = "O2_2_(13) + C8H6(74) <=> HO2_17_(5) + R1(63)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.208e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O2b]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O2b]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1016,
    label = "CH2OH(32) + R1(63) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]
""",
)

entry(
    index = 1054,
    label = "OH_12_(12) + C8H6(74) <=> H2O_14_(6) + C8H5(145)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O_pri_rad]
""",
)

entry(
    index = 1055,
    label = "O2_2_(13) + C8H6(74) <=> HO2_17_(5) + C8H5(145)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.104e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1063,
    label = "CH2OH(32) + C8H5(145) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]
""",
)

entry(
    index = 1099,
    label = "OH_12_(12) + C8H6(74) <=> H2O_14_(6) + C8H5(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.44e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1100,
    label = "O2_2_(13) + C8H6(74) <=> HO2_17_(5) + C8H5(144)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.208e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O2b]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O2b]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1108,
    label = "CH2OH(32) + C8H5(144) <=> CH2O(25) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]
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
    index = 1176,
    label = "H2O_14_(6) + C8H5(186) <=> OH_12_(12) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (484, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (14.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1191,
    label = "HO2_17_(5) + C8H5(186) <=> O2_2_(13) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.514, 'cm^3/(mol*s)'),
        n = 3.539,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]
""",
)

entry(
    index = 1197,
    label = "CH2OH(32) + C8H5(186) <=> CH2O(25) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 1231,
    label = "OH_12_(12) + C8H7(200) <=> H2O_14_(6) + C8H6(190)",
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
    index = 1232,
    label = "O_11_(7) + C8H7(200) <=> OH_12_(12) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.68e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1238,
    label = "HCO(22) + C8H7(200) <=> CH2O(25) + C8H6(190)",
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
    index = 1258,
    label = "OH_12_(12) + C8H7(199) <=> H2O_14_(6) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.598e+11, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (1.005, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]
""",
)

entry(
    index = 1259,
    label = "O_11_(7) + C8H7(199) <=> OH_12_(12) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H/DeDe_Csrad] for rate rule [O_atom_triplet;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H/DeDe_Csrad] for rate rule [O_atom_triplet;C/H/DeDe_Csrad]
""",
)

entry(
    index = 1265,
    label = "HCO(22) + C8H7(199) <=> CH2O(25) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [CO_pri_rad;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [CO_pri_rad;C/H/DeDe_Csrad]
""",
)

entry(
    index = 1302,
    label = "OH_12_(12) + C7H5(120) <=> H2O_14_(6) + C7H4(157)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 1303,
    label = "OH_12_(12) + C7H5(174) <=> H2O_14_(6) + C7H4(157)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 1315,
    label = "OH_12_(12) + C5H5(139) <=> H2O_14_(6) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1327,
    label = "OH_12_(12) + C5H5(139) <=> H2O_14_(6) + C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cdpri_Rrad] for rate rule [O_pri_rad;Cdpri_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cdpri_Rrad] for rate rule [O_pri_rad;Cdpri_Cdrad]
""",
)

entry(
    index = 1338,
    label = "OH_12_(12) + C8H6(190) <=> H2O_14_(6) + C8H5(198)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.088e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1339,
    label = "O2_2_(13) + C8H6(190) <=> HO2_17_(5) + C8H5(198)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.416e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O2b]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O2b]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 1346,
    label = "CH2OH(32) + C8H5(198) <=> CH2O(25) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.556e+13, 'cm^3/(mol*s)'),
        n = -0.031,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Csrad] for rate rule [Cb_rad;O_Csrad]
""",
)

entry(
    index = 1391,
    label = "O_11_(7) + CH2(T)(24) <=> H_10_(3) + H_10_(3) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1392,
    label = "OH_12_(12) + CH2(T)(24) <=> H_10_(3) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.899e+13, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (-0.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1393,
    label = "HO2_17_(5) + CH2(T)(24) <=> OH_12_(12) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1395,
    label = "O2_2_(13) + CH2(T)(24) <=> H_10_(3) + OH_12_(12) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.643e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1396,
    label = "O2_2_(13) + CH2(T)(24) <=> H_10_(3) + H_10_(3) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.844e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1397,
    label = "O2_2_(13) + CH2(T)(24) <=> O_11_(7) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1398,
    label = "O2_2_(13) + CH2(T)(24) <=> H2_13_(2) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.836e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1399,
    label = "O2_2_(13) + CH2(T)(24) <=> H2O_14_(6) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1405,
    label = "O2_2_(13) + CH2(S)(28) <=> O2_2_(13) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1406,
    label = "H2O_14_(6) + CH2(S)(28) <=> H2O_14_(6) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.431, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1407,
    label = "CO_21_(14) + CH2(S)(28) <=> CO_21_(14) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1408,
    label = "CO2_5_(8) + CH2(S)(28) <=> CO2_5_(8) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1409,
    label = "CH2(T)(24) + CH2O(25) <=> HCO(22) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.074, 'cm^3/(mol*s)'), n=4.21, Ea=(1.12, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1410,
    label = "OH_12_(12) + CH3(17) <=> H2O_14_(6) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44640, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (3.998, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1413,
    label = "O_11_(7) + C2H2(20) <=> CO_21_(14) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.304e+08, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (2.206, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1414,
    label = "O_11_(7) + C2H4(30) <=> CH2(T)(24) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.62,
        Ea = (0.459, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1415,
    label = "OH_12_(12) + CH2(T)(24) <=> O_11_(7) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.806e+10, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Xrad_H;Y_1centerbirad] for rate rule [OH_rad_H;CH2_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Xrad_H;Y_1centerbirad] for rate rule [OH_rad_H;CH2_triplet]
""",
)

entry(
    index = 1416,
    label = "CH2(T)(24) + H2O2(15) <=> HO2_17_(5) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.6307, 'cm^3/(mol*s)'),
        n = 3.609,
        Ea = (4.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;CH2_triplet] + [H2O2;Y_rad_birad_trirad_quadrad] for rate rule [H2O2;CH2_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;CH2_triplet] + [H2O2;Y_rad_birad_trirad_quadrad] for rate rule [H2O2;CH2_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1417,
    label = "HO2_17_(5) + CH2(T)(24) <=> O2_2_(13) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340400, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (4.377, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;CH2_triplet] for rate rule [Orad_O_H;CH2_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;CH2_triplet] for rate rule [Orad_O_H;CH2_triplet]
""",
)

entry(
    index = 1419,
    label = "CH2(T)(24) + CH2OH(32) <=> CH2O(25) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CH2_triplet;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CH2_triplet;O_Csrad]
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
    index = 1474,
    label = "H_10_(3) + CH2CO(16) <=> CO_21_(14) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.428, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Ketene_related
""",
)

entry(
    index = 1475,
    label = "OH_12_(12) + C2H2(20) <=> H_10_(3) + CH2CO(16)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1578, 'cm^3/(mol*s)'),
                n = 2.56,
                Ea = (-0.845, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (15180, 'cm^3/(mol*s)'),
                n = 2.28,
                Ea = (-0.292, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (301700, 'cm^3/(mol*s)'),
                n = 1.92,
                Ea = (0.598, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.528e+06, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (2.106, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5.101e+06, 'cm^3/(mol*s)'),
                n = 1.65,
                Ea = (3.4, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (14570, 'cm^3/(mol*s)'),
                n = 2.45,
                Ea = (4.477, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Originally from reaction library: 2005_Senosiain_OH_C2H2
""",
)

entry(
    index = 1476,
    label = "OH_12_(12) + H2CC(27) <=> H_10_(3) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 1478,
    label = "O_11_(7) + CH2CO(16) <=> CO2_5_(8) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.351, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1479,
    label = "O_11_(7) + CH2CO(16) <=> HCO(22) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.351, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1480,
    label = "O_11_(7) + CH2CO(16) <=> CO_21_(14) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.351, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1481,
    label = "OH_12_(12) + CH2CO(16) <=> CO2_5_(8) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.013, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1482,
    label = "OH_12_(12) + CH2CO(16) <=> CO_21_(14) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.013, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1483,
    label = "O_11_(7) + C2H3(29) <=> H_10_(3) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
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
    index = 1488,
    label = "OH_12_(12) + C2H3(29) <=> H_10_(3) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 1490,
    label = "H_10_(3) + CH3CO(18) <=> HCO(22) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1491,
    label = "O_11_(7) + CH3CO(18) <=> OH_12_(12) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.27e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1492,
    label = "O_11_(7) + CH3CO(18) <=> CO2_5_(8) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1493,
    label = "OH_12_(12) + CH3CO(18) <=> H2O_14_(6) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1494,
    label = "OH_12_(12) + CH3CO(18) <=> OH_12_(12) + CO_21_(14) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1495,
    label = "HO2_17_(5) + CH3CO(18) <=> CO2_5_(8) + OH_12_(12) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1496,
    label = "O2_2_(13) + CH3CO(18) <=> HO2_17_(5) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1497,
    label = "CH3(17) + CH3CO(18) <=> Cadd(4) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.08e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
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
    index = 1499,
    label = "C2H5(31) + CH3CO(18) <=> CCadd(1) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1500,
    label = "H_10_(3) + CH3CO(18) <=> H2_13_(2) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.166e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-0.297, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;Cmethyl_Rrad] for rate rule [H_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [H_rad;Cmethyl_Rrad] for rate rule [H_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 1501,
    label = "CH2(T)(24) + CH3CO(18) <=> CH3(17) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1502,
    label = "C3H5(41) + CH3CO(18) <=> C3H6(38) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1503,
    label = "C3H5(66) + CH3CO(18) <=> C3H6(38) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1504,
    label = "C3H5(65) + CH3CO(18) <=> C3H6(38) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1505,
    label = "C2H3(29) + CH3CO(18) <=> C2H4(30) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1506,
    label = "CH3CO(18) + C3H3(19) <=> C3H4(39) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1507,
    label = "C2H(21) + CH3CO(18) <=> C2H2(20) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1508,
    label = "CH3CO(18) + C3H3(19) <=> C3H4(45) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/Ct;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/Ct;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1509,
    label = "CH3CO(18) + C3H3(86) <=> C3H4(45) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1510,
    label = "C6H5(64) + CH3CO(18) <=> C6H6(48) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1511,
    label = "R1(63) + CH3CO(18) <=> CH2CO(16) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.608e+12, 'cm^3/(mol*s)'),
        n = 0.246,
        Ea = (-0.224, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1512,
    label = "CH3CO(18) + C8H5(144) <=> CH2CO(16) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.608e+12, 'cm^3/(mol*s)'),
        n = 0.246,
        Ea = (-0.224, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1513,
    label = "CH3CO(18) + C8H5(145) <=> CH2CO(16) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.608e+12, 'cm^3/(mol*s)'),
        n = 0.246,
        Ea = (-0.224, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1514,
    label = "CH3CO(18) + C8H5(198) <=> CH2CO(16) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.608e+12, 'cm^3/(mol*s)'),
        n = 0.246,
        Ea = (-0.224, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1515,
    label = "CH3CO(18) + C8H5(186) <=> CH2CO(16) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1518,
    label = "O_11_(7) + CH(D)(23) <=> H_10_(3) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1519,
    label = "OH_12_(12) + CH(D)(23) <=> H_10_(3) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1522,
    label = "H2O_14_(6) + CH(D)(23) <=> H_10_(3) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.884, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1523,
    label = "O2_2_(13) + CH(D)(23) <=> O_11_(7) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1524,
    label = "O2_2_(13) + CH(D)(23) <=> H_10_(3) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.781e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1525,
    label = "O2_2_(13) + CH(D)(23) <=> OH_12_(12) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1526,
    label = "O2_2_(13) + CH(D)(23) <=> H_10_(3) + O_11_(7) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.789e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1527,
    label = "CO2_5_(8) + CH(D)(23) <=> CO_21_(14) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.38e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-0.715, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1528,
    label = "OH_12_(12) + CH2(T)(24) <=> H2O_14_(6) + CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (863000, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (6.776, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1531,
    label = "CH(D)(23) + CH2O(25) <=> H_10_(3) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.517, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1534,
    label = "O_11_(7) + C2H(21) <=> CO_21_(14) + CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1535,
    label = "CH(D)(23) + CH2CO(16) <=> CO_21_(14) + C2H3(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1538,
    label = "O_11_(7) + C2H(21) <=> CO_21_(14) + CH(Q)(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1539,
    label = "O2_2_(13) + C2H(21) <=> CO2_5_(8) + CH(Q)(33)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(1.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1542,
    label = "O2_2_(13) + CH(Q)(33) <=> O2_2_(13) + CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (-1.72, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1543,
    label = "H2O_14_(6) + CH(Q)(33) <=> H2O_14_(6) + CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1545,
    label = "CO2_5_(8) + CH(Q)(33) <=> CO2_5_(8) + CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.241, 'cm^3/(mol*s)'),
        n = 4.3,
        Ea = (-1.694, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1546,
    label = "CO_21_(14) + CH(Q)(33) <=> CO_21_(14) + CH(D)(23)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 1550,
    label = "HO2_17_(5) + CH(Q)(33) <=> O2_2_(13) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Orad_O_H;Y_rad_birad_trirad_quadrad] for rate rule [Orad_O_H;CH_quartet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Orad_O_H;Y_rad_birad_trirad_quadrad] for rate rule [Orad_O_H;CH_quartet]
""",
)

entry(
    index = 1551,
    label = "OH_12_(12) + CH2(T)(24) <=> H2O_14_(6) + CH(Q)(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.49, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Xbirad_H;O_pri_rad] for rate rule [CH2_triplet_H;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Xbirad_H;O_pri_rad] for rate rule [CH2_triplet_H;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1553,
    label = "O_11_(7) + CH2(T)(24) <=> OH_12_(12) + CH(Q)(33)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3.37, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Xbirad_H;O_atom_triplet] for rate rule [CH2_triplet_H;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Xbirad_H;O_atom_triplet] for rate rule [CH2_triplet_H;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1560,
    label = "OH_12_(12) + C9H9(202) <=> H2O_14_(6) + C9H8(192)",
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
    index = 1576,
    label = "OH_12_(12) + C10H7(125) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
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
    index = 1618,
    label = "OH_12_(12) + C10H7(209) <=> H2O_14_(6) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 1619,
    label = "OH_12_(12) + C10H7(232) <=> H2O_14_(6) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1662,
    label = "OH_12_(12) + C10H7(246) <=> H2O_14_(6) + C10H6(235)",
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
    index = 1689,
    label = "OH_12_(12) + C10H7(245) <=> H2O_14_(6) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.598e+11, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (1.005, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]
""",
)

entry(
    index = 1725,
    label = "O2_2_(13) + C6H5(64) <=> HO2_17_(5) + C6H4(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+15, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (44.02, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 1733,
    label = "OH_12_(12) + C6H5(64) <=> H2O_14_(6) + C6H4(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 1771,
    label = "OH_12_(12) + C10H7(189) <=> H2O_14_(6) + C10H6(260)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 1772,
    label = "OH_12_(12) + C10H7(254) <=> H2O_14_(6) + C10H6(260)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
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
    index = 1811,
    label = "HO2_17_(5) + C10H5(244) <=> O2_2_(13) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.514, 'cm^3/(mol*s)'),
        n = 3.539,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]
""",
)

entry(
    index = 1839,
    label = "CH3CO(18) + C10H5(244) <=> CH2CO(16) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 1848,
    label = "H2O_14_(6) + C10H5(244) <=> OH_12_(12) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (484, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (14.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 1961,
    label = "OH_12_(12) + C10H5(299) <=> H2O_14_(6) + C10H4(373)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 2042,
    label = "OH_12_(12) + C10H5(378) <=> H2O_14_(6) + C10H4(320)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Cdrad]
""",
)

entry(
    index = 2043,
    label = "OH_12_(12) + C10H5(313) <=> H2O_14_(6) + C10H4(320)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2074,
    label = "OH_12_(12) + C10H6(221) <=> H2O_14_(6) + C10H5(271)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.088e+08, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2077,
    label = "OH_12_(12) + C10H6(221) <=> H2O_14_(6) + C10H5(294)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (154.8, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (4.588, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Ct;Y_rad] for rate rule [Cd/H/Ct;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Ct;Y_rad] for rate rule [Cd/H/Ct;O_pri_rad]
""",
)

entry(
    index = 2086,
    label = "OH_12_(12) + C10H7(193) <=> H2O_14_(6) + C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 2173,
    label = "OH_12_(12) + C10H7(219) <=> H2O_14_(6) + C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2192,
    label = "O2_2_(13) + C10H6(221) <=> HO2_17_(5) + C10H5(271)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.416e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O2b]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O2b]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 2193,
    label = "HO2_17_(5) + C10H5(294) <=> O2_2_(13) + C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005694, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (6.332, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Ct] for rate rule [Orad_O_H;Cd_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Ct] for rate rule [Orad_O_H;Cd_rad/Ct]
""",
)

entry(
    index = 2196,
    label = "OH_12_(12) + C10H6(297) <=> H2O_14_(6) + C10H5(294)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0042, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2205,
    label = "OH_12_(12) + C10H7(219) <=> H2O_14_(6) + C10H6(297)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 2219,
    label = "OH_12_(12) + C10H7(404) <=> H2O_14_(6) + C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.406e+11, 'cm^3/(mol*s)'),
        n = 0.623,
        Ea = (1.703, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H2/De_Csrad] + [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H2/De_Csrad] + [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2243,
    label = "OH_12_(12) + C10H7(403) <=> H2O_14_(6) + C10H6(221)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.598e+11, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (1.005, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Csrad]
""",
)

entry(
    index = 2273,
    label = "OH_12_(12) + C10H6(327) <=> H2O_14_(6) + C10H5(321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.453e+06, 'cm^3/(mol*s)'),
        n = 1.916,
        Ea = (2.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2279,
    label = "OH_12_(12) + C10H6(327) <=> H2O_14_(6) + C10H5(323)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.759e+07, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (-0.964, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]
""",
)

entry(
    index = 2351,
    label = "OH_12_(12) + C10H6(312) <=> H2O_14_(6) + C10H5(303)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.453e+06, 'cm^3/(mol*s)'),
        n = 1.916,
        Ea = (2.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H3/OneDe;O_pri_rad] + [C/H3/Ct;O_rad] for rate rule [C/H3/Ct;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2357,
    label = "OH_12_(12) + C10H6(312) <=> H2O_14_(6) + C10H5(311)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.759e+07, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (-0.964, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]
""",
)

entry(
    index = 2458,
    label = "OH_12_(12) + C10H7(405) <=> H2O_14_(6) + C10H6(297)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/DeDe_Cdrad]
""",
)

entry(
    index = 2468,
    label = "OH_12_(12) + C10H6(307) <=> H2O_14_(6) + C10H5(302)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.759e+07, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (-0.964, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]
""",
)

entry(
    index = 2471,
    label = "OH_12_(12) + C10H6(307) <=> H2O_14_(6) + C10H5(304)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0042, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2474,
    label = "OH_12_(12) + C10H6(307) <=> H2O_14_(6) + C10H5(303)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2239, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (8.947, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_H;O_pri_rad] + [Cd_allenic;O_rad] for rate rule [Cd_allenic;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_H;O_pri_rad] + [Cd_allenic;O_rad] for rate rule [Cd_allenic;O_pri_rad]
""",
)

entry(
    index = 2501,
    label = "OH_12_(12) + C10H6(328) <=> H2O_14_(6) + C10H5(321)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2239, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (8.947, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_H;O_pri_rad] + [Cd_allenic;O_rad] for rate rule [Cd_allenic;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_H;O_pri_rad] + [Cd_allenic;O_rad] for rate rule [Cd_allenic;O_pri_rad]
""",
)

entry(
    index = 2506,
    label = "OH_12_(12) + C10H6(328) <=> H2O_14_(6) + C10H5(325)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0042, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2509,
    label = "OH_12_(12) + C10H6(328) <=> H2O_14_(6) + C10H5(326)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.759e+07, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (-0.964, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]
""",
)

entry(
    index = 2534,
    label = "OH_12_(12) + C8H4(416) <=> H2O_14_(6) + C8H3(414)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.355e+06, 'cm^3/(mol*s)'),
        n = 1.953,
        Ea = (-0.478, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec;O_pri_rad] for rate rule [C/H2/CbCb;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_sec;O_pri_rad] for rate rule [C/H2/CbCb;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2561,
    label = "HO2_17_(5) + C8H3(414) <=> O2_2_(13) + C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.08667, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (22.68, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/TwoDe] for rate rule [Orad_O_H;C_rad/H/CbCb]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/TwoDe] for rate rule [Orad_O_H;C_rad/H/CbCb]
""",
)

entry(
    index = 2591,
    label = "CH3CO(18) + C8H3(414) <=> CH2CO(16) + C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;Cmethyl_Rrad] for rate rule [C_rad/H/TwoDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;Cmethyl_Rrad] for rate rule [C_rad/H/TwoDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2616,
    label = "HO2_17_(5) + C8H3(415) <=> O2_2_(13) + C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1106, 'cm^3/(mol*s)'),
        n = 3.706,
        Ea = (13.874, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_ter_rad] for rate rule [Orad_O_H;C_rad/ThreeDe]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_ter_rad] for rate rule [Orad_O_H;C_rad/ThreeDe]
""",
)

entry(
    index = 2652,
    label = "CH3CO(18) + C8H3(415) <=> CH2CO(16) + C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.58e+15, 'cm^3/(mol*s)'),
        n = -1.1,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;Cmethyl_Rrad] for rate rule [C_rad/ThreeDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;Cmethyl_Rrad] for rate rule [C_rad/ThreeDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2678,
    label = "OH_12_(12) + C8H4(416) <=> H2O_14_(6) + C8H3(415)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.759e+07, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (-0.964, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter;O_pri_rad] for rate rule [C/H/ThreeDe;O_pri_rad]
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
    index = 2699,
    label = "O2_2_(13) + C8H4(416) <=> HO2_17_(5) + C8H3(419)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.104e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (63.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2735,
    label = "CH3CO(18) + C8H3(419) <=> CH2CO(16) + C8H4(416)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.608e+12, 'cm^3/(mol*s)'),
        n = 0.246,
        Ea = (-0.224, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Rrad] for rate rule [Cb_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2762,
    label = "OH_12_(12) + C8H4(416) <=> H2O_14_(6) + C8H3(419)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cb_H;O_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cb_H;O_pri_rad]
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
    index = 2767,
    label = "HO2_17_(5) + C3H7(35) <=> O2_2_(13) + C3H8(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5763, 'cm^3/(mol*s)'),
        n = 3.502,
        Ea = (5.889, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]
""",
)

entry(
    index = 2770,
    label = "O_11_(7) + C3H8(34) <=> OH_12_(12) + C3H7(35)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.031, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (3.312, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/Cs;O_atom_triplet] + [C/H3/Cs\\H2\\Cs;Y_rad_birad_trirad_quadrad] for rate rule\n[C/H3/Cs\\H2\\Cs;O_atom_triplet]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [C/H3/Cs;O_atom_triplet] + [C/H3/Cs\H2\Cs;Y_rad_birad_trirad_quadrad] for rate rule
[C/H3/Cs\H2\Cs;O_atom_triplet]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2771,
    label = "H2O_14_(6) + C3H7(35) <=> OH_12_(12) + C3H8(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+06, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (20.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2772,
    label = "C3H7(35) + H2O2(15) <=> HO2_17_(5) + C3H8(34)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H2O2;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2780,
    label = "C3H7(35) + CH2OH(32) <=> CH2O(25) + C3H8(34)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 2784,
    label = "HCCO(26) + H2O2(15) <=> HO2_17_(5) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.323, 'cm^3/(mol*s)'),
        n = 3.555,
        Ea = (-5.755, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_rad] for rate rule [H2O2;Cd_Cdd_rad/H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;Cd_rad] for rate rule [H2O2;Cd_Cdd_rad/H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2785,
    label = "HO2_17_(5) + HCCO(26) <=> O2_2_(13) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (16.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]
""",
)

entry(
    index = 2786,
    label = "Cadd(4) + HCCO(26) <=> CH3(17) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0636, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (20.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methane;Cd_Cdd_rad/H]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_methane;Cd_Cdd_rad/H]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2787,
    label = "HCCO(26) + C2H5(31) <=> C2H4(30) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2788,
    label = "C3H7(35) + HCCO(26) <=> C3H6(38) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [Cd_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2789,
    label = "HCCO(26) + CH2OH(32) <=> CH2O(25) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 2790,
    label = "HCCO(26) + C2H3(29) <=> C2H2(20) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 2794,
    label = "HCCO(26) + C3H5(41) <=> C3H4(39) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [Cd_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 2796,
    label = "CHO2(42) + CH3(17) <=> Cadd(4) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.166e+10, 'cm^3/(mol*s)'),
        n = 0.935,
        Ea = (1.05, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;O_Rrad] for rate rule [C_methyl;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_methyl;O_Rrad] for rate rule [C_methyl;O_COrad]
""",
)

entry(
    index = 2797,
    label = "CHO2(42) + C3H3(19) <=> CO2_5_(8) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2798,
    label = "C3H7(35) + CHO2(42) <=> CO2_5_(8) + C3H8(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 2799,
    label = "C2H5(31) + CHO2(42) <=> CCadd(1) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 2800,
    label = "O_11_(7) + CHO2(42) <=> CO2_5_(8) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.727e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;O_Rrad] for rate rule [O_atom_triplet;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_atom_triplet;O_Rrad] for rate rule [O_atom_triplet;O_COrad]
""",
)

entry(
    index = 2801,
    label = "H_10_(3) + CHO2(42) <=> H2_13_(2) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.96e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (0.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;O_Rrad] for rate rule [H_rad;O_COrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;O_Rrad] for rate rule [H_rad;O_COrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2802,
    label = "OH_12_(12) + CHO2(42) <=> H2O_14_(6) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.605e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;O_Rrad] for rate rule [O_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;O_Rrad] for rate rule [O_pri_rad;O_COrad]
""",
)

entry(
    index = 2803,
    label = "O2_2_(13) + CHO2(42) <=> HO2_17_(5) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.288e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;O_Rrad] for rate rule [O2b;O_COrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;O_Rrad] for rate rule [O2b;O_COrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2804,
    label = "HO2_17_(5) + CHO2(42) <=> CO2_5_(8) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.964e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]
""",
)

entry(
    index = 2805,
    label = "CH2(T)(24) + CHO2(42) <=> CO2_5_(8) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;O_Rrad] for rate rule [CH2_triplet;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CH2_triplet;O_Rrad] for rate rule [CH2_triplet;O_COrad]
""",
)

entry(
    index = 2806,
    label = "C2H3(29) + CHO2(42) <=> CO2_5_(8) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2807,
    label = "CHO2(42) + C3H5(41) <=> CO2_5_(8) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 2808,
    label = "HCO(22) + CHO2(42) <=> CO2_5_(8) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;O_Rrad] for rate rule [CO_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_pri_rad;O_Rrad] for rate rule [CO_pri_rad;O_COrad]
""",
)

entry(
    index = 2809,
    label = "C2H(21) + CHO2(42) <=> CO2_5_(8) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;O_Rrad] for rate rule [Ct_rad/Ct;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Ct_rad/Ct;O_Rrad] for rate rule [Ct_rad/Ct;O_COrad]
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
    index = 2811,
    label = "HCCO(26) + CHO2(42) <=> CO2_5_(8) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
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
    index = 2815,
    label = "CHO2(42) + C3H3(19) <=> CO2_5_(8) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Rrad] for rate rule [C_rad/H2/Ct;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;O_Rrad] for rate rule [C_rad/H2/Ct;O_COrad]
""",
)

entry(
    index = 2816,
    label = "H2O_14_(6) + CO_21_(14) <=> H_10_(3) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.188, -0.09711, -0.06112, -0.02824],
            [14.19, 0.1183, 0.07267, 0.03189],
            [0.0986, -0.01948, -0.009838, -0.002253],
            [0.01908, -0.004448, -0.003547, -0.002321],
            [0.004776, 6.338e-05, -6.635e-05, -0.0001458],
            [0.001834, 0.0002253, 0.0001704, 0.0001062],
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
    index = 2817,
    label = "CO2_5_(8) + HCO(22) <=> CO_21_(14) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.099, -0.165, -0.1037, -0.04779],
            [13.76, 0.0917, 0.0534, 0.02055],
            [0.1341, 0.004251, 0.004167, 0.003316],
            [0.01723, 0.003982, 0.00251, 0.001177],
            [-0.002005, 0.002577, 0.001666, 0.0008046],
            [-0.003751, 0.001203, 0.0008129, 0.0004265],
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
    index = 2820,
    label = "CH(Q)(33) + CHO2(42) <=> CO2_5_(8) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.404e+09, 'cm^3/(mol*s)'),
        n = 0.956,
        Ea = (-0.316, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;O_Rrad] for rate rule [CH_quartet;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad_birad_trirad_quadrad;O_Rrad] for rate rule [CH_quartet;O_COrad]
""",
)

entry(
    index = 2821,
    label = "CO2_5_(8) + CH3(17) <=> CH2(S)(28) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.13, -0.003104, -0.002156, -0.001192],
            [17.64, 0.003599, 0.002498, 0.00138],
            [0.02062, -0.0007861, -0.0005436, -0.0002985],
            [-0.003059, 6.635e-05, 4.517e-05, 2.416e-05],
            [-0.002774, 6.095e-06, 4.404e-06, 2.593e-06],
            [-0.001176, -1.502e-07, -1.154e-07, -7.396e-08],
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
    index = 2836,
    label = "O2_2_(13) + C6H7(52) <=> HO2_17_(5) + C6H6(54)",
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
    index = 2839,
    label = "O2_2_(13) + cyC6H7(58) <=> HO2_17_(5) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 2840,
    label = "H2O_14_(6) + C6H5(105) <=> OH_12_(12) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (484, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (14.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2848,
    label = "CH3CO(18) + HCO(22) <=> CH2CO(16) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2849,
    label = "CHO2(42) + C6H13(77) <=> CO2_5_(8) + C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]
""",
)

entry(
    index = 2850,
    label = "CHO2(42) + C3H5(66) <=> CO2_5_(8) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/NonDeC;O_COrad]
""",
)

entry(
    index = 2851,
    label = "CHO2(42) + C3H5(65) <=> CO2_5_(8) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2852,
    label = "CHO2(42) + C4H7(85) <=> CO2_5_(8) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/NonDeC;O_COrad]
""",
)

entry(
    index = 2853,
    label = "CHO2(42) + C3H3(86) <=> CO2_5_(8) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;O_Rrad] for rate rule [Ct_rad/Ct;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;O_Rrad] for rate rule [Ct_rad/Ct;O_COrad]
""",
)

entry(
    index = 2854,
    label = "CHO2(42) + C6H5(105) <=> CO2_5_(8) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2855,
    label = "CHO2(42) + C6H5(64) <=> CO2_5_(8) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 2856,
    label = "CHO2(42) + R1(63) <=> CO2_5_(8) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.663e+10, 'cm^3/(mol*s)'),
        n = 0.929,
        Ea = (-0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]
""",
)

entry(
    index = 2857,
    label = "CHO2(42) + C8H5(144) <=> CO2_5_(8) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.663e+10, 'cm^3/(mol*s)'),
        n = 0.929,
        Ea = (-0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]
""",
)

entry(
    index = 2858,
    label = "CHO2(42) + C8H5(145) <=> CO2_5_(8) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.663e+10, 'cm^3/(mol*s)'),
        n = 0.929,
        Ea = (-0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]
""",
)

entry(
    index = 2859,
    label = "CHO2(42) + C5H3(141) <=> CO2_5_(8) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Rrad] for rate rule [C_rad/H2/Ct;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;O_Rrad] for rate rule [C_rad/H2/Ct;O_COrad]
""",
)

entry(
    index = 2860,
    label = "CHO2(42) + C5H3(142) <=> CO2_5_(8) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;O_Rrad] for rate rule [Ct_rad/Ct;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;O_Rrad] for rate rule [Ct_rad/Ct;O_COrad]
""",
)

entry(
    index = 2861,
    label = "CHO2(42) + C5H3(141) <=> CO2_5_(8) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 2862,
    label = "CHO2(42) + C5H3(162) <=> CO2_5_(8) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2863,
    label = "CHO2(42) + C5H3(141) <=> CO2_5_(8) + C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2864,
    label = "CHO2(42) + C8H5(198) <=> CO2_5_(8) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.663e+10, 'cm^3/(mol*s)'),
        n = 0.929,
        Ea = (-0.262, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;O_Rrad] for rate rule [Cb_rad;O_COrad]
""",
)

entry(
    index = 2865,
    label = "CHO2(42) + C8H5(186) <=> CO2_5_(8) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 2866,
    label = "CHO2(424) + CH3(17) <=> Cadd(4) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.439e+10, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (1.313, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;XH_s_Rrad] for rate rule [C_methyl;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_methyl;XH_s_Rrad] for rate rule [C_methyl;COpri_Orad]
""",
)

entry(
    index = 2867,
    label = "CHO2(424) + C3H3(19) <=> CO2_5_(8) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2868,
    label = "CHO2(424) + C2H5(31) <=> CCadd(1) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]
""",
)

entry(
    index = 2869,
    label = "O_11_(7) + CHO2(424) <=> CO2_5_(8) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;XH_s_Rrad] for rate rule [O_atom_triplet;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_atom_triplet;XH_s_Rrad] for rate rule [O_atom_triplet;COpri_Orad]
""",
)

entry(
    index = 2870,
    label = "H_10_(3) + CHO2(424) <=> H2_13_(2) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.089e+10, 'cm^3/(mol*s)'),
        n = 0.783,
        Ea = (0.565, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;XH_s_Rrad] for rate rule [H_rad;COpri_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;XH_s_Rrad] for rate rule [H_rad;COpri_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2871,
    label = "OH_12_(12) + CHO2(424) <=> H2O_14_(6) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.868e+10, 'cm^3/(mol*s)'),
        n = 0.667,
        Ea = (0.603, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;XH_s_Rrad] for rate rule [O_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;XH_s_Rrad] for rate rule [O_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2872,
    label = "O2_2_(13) + CHO2(424) <=> HO2_17_(5) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.908, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;XH_s_Rrad] for rate rule [O2b;COpri_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;XH_s_Rrad] for rate rule [O2b;COpri_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 2873,
    label = "HO2_17_(5) + CHO2(424) <=> CO2_5_(8) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.159e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]
""",
)

entry(
    index = 2874,
    label = "CHO2(424) + CH2(T)(24) <=> CO2_5_(8) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.04e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;XH_s_Rrad] for rate rule [CH2_triplet;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CH2_triplet;XH_s_Rrad] for rate rule [CH2_triplet;COpri_Orad]
""",
)

entry(
    index = 2875,
    label = "CHO2(424) + C2H3(29) <=> CO2_5_(8) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2876,
    label = "C3H5(41) + CHO2(424) <=> CO2_5_(8) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]
""",
)

entry(
    index = 2877,
    label = "CHO2(424) + HCO(22) <=> CO2_5_(8) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2878,
    label = "O_11_(7) + CHO2(424) <=> O2_2_(13) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.96, -0.007076, -0.004899, -0.002695],
            [-0.05266, 0.007448, 0.005144, 0.00282],
            [-0.03511, -0.001991, -0.001368, -0.0007431],
            [-0.01683, -0.0001982, -0.0001418, -8.224e-05],
            [-0.007342, 4.852e-07, 5.332e-07, 4.718e-07],
            [-0.002829, 1.907e-05, 1.329e-05, 7.391e-06],
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
    index = 2879,
    label = "CHO2(424) + C2H(21) <=> CO2_5_(8) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.297e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Orad]
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
    index = 2882,
    label = "CHO2(424) + C3H3(19) <=> CO2_5_(8) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+12, 'cm^3/(mol*s)'),
        n = -0.047,
        Ea = (1.024, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;XH_s_Rrad] for rate rule [C_rad/H2/Ct;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;XH_s_Rrad] for rate rule [C_rad/H2/Ct;COpri_Orad]
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
    index = 2884,
    label = "H2O_14_(6) + CO_21_(14) <=> H_10_(3) + CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.04, -0.04187, -0.02802, -0.01453],
            [16.26, 0.05159, 0.03419, 0.01743],
            [0.1279, -0.009827, -0.006114, -0.002743],
            [0.02541, -0.001182, -0.0009577, -0.000651],
            [0.003858, 4.808e-05, 2.99e-05, 1.251e-05],
            [0.0001098, 3.652e-05, 2.864e-05, 1.888e-05],
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
    index = 2885,
    label = "OH_12_(12) + CHO2(424) <=> CO_21_(14) + H2O2(15)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.787, -0.009277, -0.006385, -0.003479],
            [3.395, 0.01273, 0.008746, 0.004749],
            [0.2083, -0.003943, -0.002683, -0.001434],
            [0.06151, 0.0001065, 5.524e-05, 1.351e-05],
            [0.02057, 0.0001092, 7.828e-05, 4.547e-05],
            [0.007336, 2.806e-05, 1.979e-05, 1.123e-05],
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
    index = 2886,
    label = "OH_12_(12) + CHO2(424) <=> HO2_17_(5) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.658, -0.003415, -0.00237, -0.00131],
            [4.819, 0.004161, 0.002886, 0.001593],
            [-0.05285, -0.000907, -0.0006267, -0.0003438],
            [-0.006094, -0.0001198, -8.431e-05, -4.765e-05],
            [0.0009421, -1.363e-06, -9.621e-07, -5.464e-07],
            [0.001425, 1.47e-05, 1.024e-05, 5.689e-06],
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
    index = 2887,
    label = "CO2_5_(8) + HCO(22) <=> CO_21_(14) + CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.832, -0.03251, -0.0222, -0.01194],
            [4.636, 0.00792, 0.005369, 0.00285],
            [0.01719, -0.002345, -0.001562, -0.0008034],
            [-0.002176, 1.957e-05, 9.62e-06, 1.539e-06],
            [-0.003263, 0.0002446, 0.0001658, 8.786e-05],
            [-0.002216, 0.0001939, 0.0001306, 6.849e-05],
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
    index = 2888,
    label = "O_11_(7) + CHO2(424) <=> HO2_17_(5) + CO_21_(14)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.386, -0.002818, -0.001957, -0.001083],
            [3.634, 0.002724, 0.001891, 0.001045],
            [0.1307, -0.0007028, -0.0004868, -0.0002681],
            [0.03251, -0.000116, -8.115e-05, -4.542e-05],
            [0.008626, -1.087e-05, -7.56e-06, -4.193e-06],
            [0.002827, 4.532e-06, 3.161e-06, 1.761e-06],
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
    index = 2889,
    label = "CHO2(424) + CH(Q)(33) <=> CO2_5_(8) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.169e+10, 'cm^3/(mol*s)'),
        n = 0.598,
        Ea = (1.839, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;XH_s_Rrad] for rate rule [CH_quartet;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad_birad_trirad_quadrad;XH_s_Rrad] for rate rule [CH_quartet;COpri_Orad]
""",
)

entry(
    index = 2890,
    label = "CHO2(424) + C6H13(77) <=> CO2_5_(8) + C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.972e+13, 'cm^3/(mol*s)'),
        n = -0.28,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]
""",
)

entry(
    index = 2891,
    label = "CHO2(424) + C3H5(66) <=> CO2_5_(8) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/NonDeC;COpri_Orad]
""",
)

entry(
    index = 2892,
    label = "CHO2(424) + C3H5(65) <=> CO2_5_(8) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2893,
    label = "CHO2(424) + C4H7(85) <=> CO2_5_(8) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/NonDeC;COpri_Orad]
""",
)

entry(
    index = 2894,
    label = "CHO2(424) + C3H3(86) <=> CO2_5_(8) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.297e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Orad]
""",
)

entry(
    index = 2895,
    label = "CHO2(424) + C6H5(105) <=> CO2_5_(8) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2896,
    label = "CHO2(424) + C6H5(64) <=> CO2_5_(8) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 2897,
    label = "CHO2(424) + R1(63) <=> CO2_5_(8) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+10, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (0.562, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]
""",
)

entry(
    index = 2898,
    label = "CHO2(424) + C8H5(144) <=> CO2_5_(8) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+10, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (0.562, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]
""",
)

entry(
    index = 2899,
    label = "CHO2(424) + C8H5(145) <=> CO2_5_(8) + C8H6(74)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+10, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (0.562, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]
""",
)

entry(
    index = 2900,
    label = "CHO2(424) + C5H3(141) <=> CO2_5_(8) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+12, 'cm^3/(mol*s)'),
        n = -0.047,
        Ea = (1.024, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;XH_s_Rrad] for rate rule [C_rad/H2/Ct;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;XH_s_Rrad] for rate rule [C_rad/H2/Ct;COpri_Orad]
""",
)

entry(
    index = 2901,
    label = "CHO2(424) + C5H3(142) <=> CO2_5_(8) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.297e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Orad]
""",
)

entry(
    index = 2902,
    label = "CHO2(424) + C5H3(141) <=> CO2_5_(8) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 2903,
    label = "CHO2(424) + C5H3(162) <=> CO2_5_(8) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2904,
    label = "CHO2(424) + C5H3(141) <=> CO2_5_(8) + C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2905,
    label = "CHO2(424) + C8H5(198) <=> CO2_5_(8) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.06e+10, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (0.562, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;XH_s_Rrad] for rate rule [Cb_rad;COpri_Orad]
""",
)

entry(
    index = 2906,
    label = "CHO2(424) + C8H5(186) <=> CO2_5_(8) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2907,
    label = "CHO2(424) + HCCO(26) <=> CO2_5_(8) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 2909,
    label = "S(433) + H2O2(15) <=> HO2_17_(5) + S(428)",
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
    index = 2911,
    label = "O2_2_(13) + S(428) <=> HO2_17_(5) + S(433)",
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
    index = 2912,
    label = "S(428) + O_11_(7) <=> OH_12_(12) + S(433)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47800, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2913,
    label = "S(428) + OH_12_(12) <=> H2O_14_(6) + S(433)",
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
    index = 2919,
    label = "CH2OH(32) + S(433) <=> S(428) + CH2O(25)",
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
    index = 2921,
    label = "HO2_17_(5) + C3H7O(436) <=> C3H6O(437) + H2O2(15)",
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
    index = 2922,
    label = "H_10_(3) + C3H7O(436) <=> H2_13_(2) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.166e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 2923,
    label = "O2_2_(13) + C3H7O(436) <=> HO2_17_(5) + C3H6O(437)",
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
    index = 2924,
    label = "OH_12_(12) + C3H7O(436) <=> H2O_14_(6) + C3H6O(437)",
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
    index = 2925,
    label = "C3H7O(436) + CH3(17) <=> Cadd(4) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.57e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methyl;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_methyl;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2926,
    label = "C2H5(31) + C3H7O(436) <=> CCadd(1) + C3H6O(437)",
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
    index = 2927,
    label = "S(433) + C3H7O(436) <=> S(428) + C3H6O(437)",
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
    index = 2929,
    label = "S(434) + H2O2(15) <=> HO2_17_(5) + S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.97, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [H2O2;C_rad/H/Cs\\H2\\Cs/O]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [H2O2;C_rad/H/Cs\H2\Cs/O]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2931,
    label = "HO2_17_(5) + S(434) <=> O2_2_(13) + S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.485, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/Cs\\H2\\Cs/O] for rate rule [Orad_O_H;C_rad/H/Cs\\H2\\Cs/O]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/Cs\H2\Cs/O] for rate rule [Orad_O_H;C_rad/H/Cs\H2\Cs/O]
""",
)

entry(
    index = 2932,
    label = "S(428) + O_11_(7) <=> OH_12_(12) + S(434)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H2/CsO;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C/H2/CsO;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2933,
    label = "S(428) + OH_12_(12) <=> H2O_14_(6) + S(434)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43100, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (-1.738, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/CsO;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/CsO;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2939,
    label = "CH2OH(32) + S(434) <=> S(428) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Csrad] for rate rule [C_rad/H/CsO;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Csrad] for rate rule [C_rad/H/CsO;O_Csrad]
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
    index = 2941,
    label = "S(434) + C3H7O(436) <=> S(428) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.424e+12, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;Cmethyl_Csrad] for rate rule [C_rad/H/CsO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;Cmethyl_Csrad] for rate rule [C_rad/H/CsO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2943,
    label = "S(435) + H2O2(15) <=> HO2_17_(5) + S(428)",
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
    index = 2945,
    label = "HO2_17_(5) + S(435) <=> O2_2_(13) + S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5763, 'cm^3/(mol*s)'),
        n = 3.502,
        Ea = (5.889, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]
""",
)

entry(
    index = 2946,
    label = "S(428) + O_11_(7) <=> OH_12_(12) + S(435)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5157, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (3.312, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/Cs;O_atom_triplet] + [C/H3/Cs\\H2\\Cs;Y_rad_birad_trirad_quadrad] for rate rule\n[C/H3/Cs\\H2\\Cs;O_atom_triplet]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H3/Cs;O_atom_triplet] + [C/H3/Cs\H2\Cs;Y_rad_birad_trirad_quadrad] for rate rule
[C/H3/Cs\H2\Cs;O_atom_triplet]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 2947,
    label = "H2O_14_(6) + S(435) <=> S(428) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+06, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (20.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2953,
    label = "CH2OH(32) + S(435) <=> S(428) + CH2O(25)",
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
    index = 2955,
    label = "S(435) + C3H7O(436) <=> S(428) + C3H6O(437)",
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
    index = 2963,
    label = "C2H5(31) + C3H7O(432) <=> CCadd(1) + C3H6O(437)",
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
    index = 2964,
    label = "C3H7O(432) + CH3(17) <=> Cadd(4) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methyl;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_methyl;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2965,
    label = "H_10_(3) + C3H7O(432) <=> H2_13_(2) + C3H6O(437)",
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
    index = 2966,
    label = "C3H7O(432) + S(433) <=> S(428) + C3H6O(437)",
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
    index = 2967,
    label = "C3H7O(432) + S(434) <=> S(428) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26300, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (0.57, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H/CsO;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;C/H2/Nd_Csrad] for rate rule [C_rad/H/CsO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2968,
    label = "C3H7O(432) + S(435) <=> S(428) + C3H6O(437)",
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
    index = 2969,
    label = "OH_12_(12) + C3H7O(432) <=> H2O_14_(6) + C3H6O(437)",
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
    index = 2976,
    label = "C3H5(41) + C3H7O(432) <=> C3H6(38) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2977,
    label = "C3H5(41) + C3H7O(436) <=> C3H6(38) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 2981,
    label = "OH_12_(12) + C2H4(30) <=> H_10_(3) + C2H4O(431)",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (0.0238, 'cm^3/(mol*s)'),
                n = 3.91,
                Ea = (1.723, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (319000, 'cm^3/(mol*s)'),
                n = 2.19,
                Ea = (5.256, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 2982,
    label = "O_11_(7) + C2H5(31) <=> H_10_(3) + C2H4O(431)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 2989,
    label = "C3H7O(432) + C3H5(65) <=> C3H6(38) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2990,
    label = "C3H7O(436) + C3H5(65) <=> C3H6(38) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 2994,
    label = "CH2O(25) + S(433) <=> S(428) + HCO(22)",
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
    index = 2995,
    label = "HCO(22) + C3H7O(432) <=> CH2O(25) + C3H6O(437)",
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
    index = 2996,
    label = "HCO(22) + C3H7O(436) <=> CH2O(25) + C3H6O(437)",
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
    index = 2997,
    label = "CH2O(25) + S(434) <=> S(428) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.97, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/Cs\\H2\\Cs/O] for rate rule [CO_pri;C_rad/H/Cs\\H2\\Cs/O]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/Cs\H2\Cs/O] for rate rule [CO_pri;C_rad/H/Cs\H2\Cs/O]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 2998,
    label = "CH2O(25) + S(435) <=> S(428) + HCO(22)",
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
    index = 3001,
    label = "C2H3(29) + C3H7O(432) <=> C2H4(30) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3002,
    label = "C2H3(29) + C3H7O(436) <=> C2H4(30) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 3009,
    label = "C2H(21) + C3H7O(432) <=> C2H2(20) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct_rad/Ct;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct_rad/Ct;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3010,
    label = "C2H(21) + C3H7O(436) <=> C2H2(20) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Ct_rad/Ct;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Ct_rad/Ct;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 3016,
    label = "C3H7O(432) + C3H5(66) <=> C3H6(38) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;C/H2/Nd_Csrad] for rate rule [Cd_rad/NonDeC;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;C/H2/Nd_Csrad] for rate rule [Cd_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3017,
    label = "C3H7O(436) + C3H5(66) <=> C3H6(38) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Csrad] for rate rule [Cd_rad/NonDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Csrad] for rate rule [Cd_rad/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 3049,
    label = "H_10_(3) + C2H4O(431) <=> H2_13_(2) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2.405, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3050,
    label = "O_11_(7) + C2H4O(431) <=> OH_12_(12) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3051,
    label = "OH_12_(12) + C2H4O(431) <=> H2O_14_(6) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+08, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1.574, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3052,
    label = "O2_2_(13) + C2H4O(431) <=> HO2_17_(5) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3053,
    label = "HO2_17_(5) + C2H4O(431) <=> H2O2(15) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3054,
    label = "C2H4O(431) + CH3(17) <=> Cadd(4) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+06, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5.92, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 3055,
    label = "C2H4O(431) + C2H5(31) <=> CCadd(1) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs\\H3]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Cs\H3]
""",
)

entry(
    index = 3056,
    label = "C2H5(31) + CH3CO(18) <=> C2H4O(431) + C2H4(30)",
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
    index = 3057,
    label = "CH2OH(32) + CH3CO(18) <=> C2H4O(431) + CH2O(25)",
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
    index = 3058,
    label = "C3H7O(432) + CH3CO(18) <=> C2H4O(431) + C3H6O(437)",
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
    index = 3059,
    label = "C3H7O(436) + CH3CO(18) <=> C2H4O(431) + C3H6O(437)",
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
    index = 3060,
    label = "C3H7(35) + CH3CO(18) <=> C2H4O(431) + C3H6(38)",
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
    index = 3061,
    label = "CH3CO(18) + C3H7(79) <=> C2H4O(431) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.336e+13, 'cm^3/(mol*s)'),
        n = -0.192,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad] for rate rule [CO_rad/NonDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 3062,
    label = "C3H6(38) + CH3CO(18) <=> C2H4O(431) + C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9060, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (17.53, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri;CO_rad/NonDe] for rate rule [C/H3/Cd\\H_Cd\\H2;CO_rad/Cs]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri;CO_rad/NonDe] for rate rule [C/H3/Cd\H_Cd\H2;CO_rad/Cs]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3063,
    label = "C2H3(29) + CH3CO(18) <=> C2H4O(431) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3064,
    label = "C3H5(65) + CH3CO(18) <=> C2H4O(431) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
""",
)

entry(
    index = 3065,
    label = "C3H5(66) + CH3CO(18) <=> C2H4O(431) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3066,
    label = "C3H5(66) + CH3CO(18) <=> C2H4O(431) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3067,
    label = "C3H5(41) + CH3CO(18) <=> C2H4O(431) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cdpri_Csrad] for rate rule [CO_rad/NonDe;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cdpri_Csrad] for rate rule [CO_rad/NonDe;Cdpri_Csrad]
""",
)

entry(
    index = 3068,
    label = "C2H4O(431) + C3H3(19) <=> C3H4(45) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;C_pri_rad] for rate rule [CO/H/Cs;C_rad/H2/Ct]
""",
)

entry(
    index = 3069,
    label = "C2H4O(431) + C3H3(19) <=> C3H4(39) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.68, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;Cd_rad] for rate rule [CO/H/Cs;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;Cd_rad] for rate rule [CO/H/Cs;Cd_Cdd_rad/H]
""",
)

entry(
    index = 3070,
    label = "CH3CO(18) + C4H7(85) <=> C2H4O(431) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3071,
    label = "CH3CO(18) + CH3CO(18) <=> C2H4O(431) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.086e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 3075,
    label = "OH_12_(12) + C4H6(91) <=> H2O_14_(6) + C4H5(465)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.045, 'cm^3/(mol*s)'),
        n = 3.684,
        Ea = (-1.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H3/Cd;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C/H3/Cd;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3086,
    label = "HO2_17_(5) + C4H5(443) <=> O2_2_(13) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01699, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (14.366, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CtCs] for rate rule [Orad_O_H;C_rad/H/CtCs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CtCs] for rate rule [Orad_O_H;C_rad/H/CtCs]
""",
)

entry(
    index = 3089,
    label = "CH2OH(32) + C4H5(443) <=> CH2O(25) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.339e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec_rad;O_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec_rad;O_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_Csrad]
""",
)

entry(
    index = 3100,
    label = "HO2_17_(5) + C4H5(443) <=> O2_2_(13) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (16.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]
""",
)

entry(
    index = 3103,
    label = "CH2OH(32) + C4H5(443) <=> CH2O(25) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 3117,
    label = "H2O_14_(6) + C4H3(96) <=> OH_12_(12) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (484, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (14.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3120,
    label = "OH_12_(12) + C4H4(444) <=> H2O_14_(6) + C4H3(110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (154.8, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (4.588, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Ct;Y_rad] for rate rule [Cd/H/Ct;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Ct;Y_rad] for rate rule [Cd/H/Ct;O_pri_rad]
""",
)

entry(
    index = 3123,
    label = "O2_2_(13) + C4H5(465) <=> HO2_17_(5) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 3149,
    label = "HO2_17_(5) + C5H3(141) <=> O2_2_(13) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (16.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_allenic_rad] for rate rule [Orad_O_H;Cd_allenic_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_allenic_rad] for rate rule [Orad_O_H;Cd_allenic_rad]
""",
)

entry(
    index = 3150,
    label = "HO2_17_(5) + C5H3(162) <=> O2_2_(13) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (16.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]
""",
)

entry(
    index = 3151,
    label = "HO2_17_(5) + C4H3(110) <=> O2_2_(13) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.005694, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (6.332, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Ct] for rate rule [Orad_O_H;Cd_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Ct] for rate rule [Orad_O_H;Cd_rad/Ct]
""",
)

entry(
    index = 3152,
    label = "HO2_17_(5) + C4H3(96) <=> O2_2_(13) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.514, 'cm^3/(mol*s)'),
        n = 3.539,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]
""",
)

entry(
    index = 3153,
    label = "OH_12_(12) + C#CCC(90) <=> H2O_14_(6) + C4H5(443)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (125.7, 'cm^3/(mol*s)'),
        n = 3.312,
        Ea = (-2.924, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/OneDeC;O_pri_rad] for rate rule [C/H2/CtCs;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/OneDeC;O_pri_rad] for rate rule [C/H2/CtCs;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3154,
    label = "OH_12_(12) + C4H6(91) <=> H2O_14_(6) + C4H5(443)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0042, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3155,
    label = "OH_12_(12) + C4H5(443) <=> H2O_14_(6) + C4H4(444)",
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
    index = 3156,
    label = "OH_12_(12) + C4H5(465) <=> H2O_14_(6) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3165,
    label = "HCO(22) + C4H3(96) <=> CH2O(25) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 3166,
    label = "HCO(22) + C4H3(110) <=> CH2O(25) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3167,
    label = "HCO(22) + C5H5(117) <=> CH2O(25) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 3168,
    label = "HCO(22) + C5H5(129) <=> CH2O(25) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 3169,
    label = "HCO(22) + C5H5(137) <=> CH2O(25) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 3170,
    label = "HCO(22) + C5H5(127) <=> CH2O(25) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3171,
    label = "CH2OH(32) + C5H3(141) <=> CH2O(25) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.946e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/Ct;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;O_Csrad] for rate rule [C_rad/H2/Ct;O_Csrad]
""",
)

entry(
    index = 3172,
    label = "CH2OH(32) + C5H3(142) <=> CH2O(25) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Ct_rad/Ct;O_Csrad from training reaction 1\nExact match found for rate rule [Ct_rad/Ct;O_Csrad]',
    ),
    longDesc = 
u"""
Ct_rad/Ct;O_Csrad from training reaction 1
Exact match found for rate rule [Ct_rad/Ct;O_Csrad]
""",
)

entry(
    index = 3173,
    label = "HCO(22) + C4H5(443) <=> CH2O(25) + C4H4(444)",
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
    index = 3174,
    label = "HCO(22) + C4H5(465) <=> CH2O(25) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3175,
    label = "CH2OH(32) + C4H3(110) <=> CH2O(25) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 3176,
    label = "CH2OH(32) + C4H3(96) <=> CH2O(25) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 3216,
    label = "CH3CO(18) + C4H3(96) <=> C2H4O(431) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
""",
)

entry(
    index = 3217,
    label = "C4H3(110) + CH3CO(18) <=> C2H4O(431) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3218,
    label = "C5H5(117) + CH3CO(18) <=> C2H4O(431) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
""",
)

entry(
    index = 3219,
    label = "C5H5(129) + CH3CO(18) <=> C2H4O(431) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
""",
)

entry(
    index = 3220,
    label = "C5H5(137) + CH3CO(18) <=> C2H4O(431) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
""",
)

entry(
    index = 3221,
    label = "C5H5(127) + CH3CO(18) <=> C2H4O(431) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3222,
    label = "C4H5(443) + CH3CO(18) <=> C2H4O(431) + C4H4(444)",
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
    index = 3223,
    label = "CH3CO(18) + C4H5(465) <=> C2H4O(431) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_rad/NonDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3292,
    label = "HCO(22) + C5H5(129) <=> C5H4(158) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3293,
    label = "HCO(22) + C5H5(97) <=> C5H4(158) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cdpri_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cdpri_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 3294,
    label = "HCO(22) + C5H5(139) <=> C5H4(158) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3295,
    label = "CH2OH(32) + C5H3(141) <=> C5H4(158) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 3296,
    label = "CH2OH(32) + C5H3(162) <=> C5H4(158) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 3314,
    label = "CHO2(42) + S(433) <=> CO2_5_(8) + S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]
""",
)

entry(
    index = 3315,
    label = "CHO2(42) + S(434) <=> CO2_5_(8) + S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/CsO;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/CsO;O_COrad]
""",
)

entry(
    index = 3316,
    label = "CHO2(42) + S(435) <=> CO2_5_(8) + S(428)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 3317,
    label = "CHO2(42) + CH3CO(18) <=> CO2_5_(8) + C2H4O(431)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]
""",
)

entry(
    index = 3318,
    label = "CHO2(42) + C4H5(443) <=> CO2_5_(8) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]
""",
)

entry(
    index = 3319,
    label = "CHO2(42) + C4H5(443) <=> CO2_5_(8) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 3320,
    label = "CHO2(42) + C4H3(110) <=> CO2_5_(8) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 3321,
    label = "CHO2(42) + C4H3(96) <=> CO2_5_(8) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
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
    index = 3356,
    label = "OH_12_(12) + C7H5(479) <=> H2O_14_(6) + C7H4(484)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 3358,
    label = "HCO(22) + C7H5(479) <=> C7H4(484) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.224e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
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
    index = 3381,
    label = "OH_12_(12) + C5H5(462) <=> H2O_14_(6) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3396,
    label = "HCO(22) + C5H5(462) <=> C5H4(158) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Rrad] for rate rule [CO_pri_rad;C/H2/De_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Rrad] for rate rule [CO_pri_rad;C/H2/De_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 3420,
    label = "OH_12_(12) + C4H4(445) <=> H2O_14_(6) + C4H3(110)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0084, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Cd_Cdd/H2;O_rad] for rate rule [Cd_Cdd/H2;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3423,
    label = "O2_2_(13) + C4H5(465) <=> HO2_17_(5) + C4H4(445)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cdpri_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cdpri_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3430,
    label = "CHO2(42) + C4H3(110) <=> CO2_5_(8) + C4H4(445)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 3432,
    label = "HO2_17_(5) + C4H3(110) <=> O2_2_(13) + C4H4(445)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02016, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (16.331, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_Cdd_rad/H] for rate rule [Orad_O_H;Cd_Cdd_rad/H]
""",
)

entry(
    index = 3433,
    label = "OH_12_(12) + C4H5(465) <=> H2O_14_(6) + C4H4(445)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
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
    index = 3460,
    label = "O2_2_(13) + C2H3O(430) <=> HO2_17_(5) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;Cdpri_Rrad] for rate rule [O2b;Cdpri_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;Cdpri_Rrad] for rate rule [O2b;Cdpri_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3461,
    label = "HO2_17_(5) + C2H3O(430) <=> H2O2(15) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.159e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Csrad]
""",
)

entry(
    index = 3462,
    label = "C2H3O(430) + CH3(17) <=> Cadd(4) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.439e+10, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (1.313, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;XH_s_Rrad] for rate rule [C_methyl;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_methyl;XH_s_Rrad] for rate rule [C_methyl;COpri_Csrad]
""",
)

entry(
    index = 3463,
    label = "C3H7(35) + C2H3O(430) <=> C3H8(34) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]
""",
)

entry(
    index = 3464,
    label = "C2H3O(430) + C2H5(31) <=> CCadd(1) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]
""",
)

entry(
    index = 3465,
    label = "C2H3O(430) + CH2(T)(24) <=> CH3(17) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.04e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;XH_s_Rrad] for rate rule [CH2_triplet;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CH2_triplet;XH_s_Rrad] for rate rule [CH2_triplet;COpri_Csrad]
""",
)

entry(
    index = 3466,
    label = "C2H3O(430) + C2H3(29) <=> C2H4(30) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]
""",
)

entry(
    index = 3467,
    label = "C2H3O(430) + HCO(22) <=> CH2O(25) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;COpri_Csrad]
""",
)

entry(
    index = 3468,
    label = "C2H3O(430) + C2H(21) <=> C2H2(20) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.297e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Ct_rad/Ct;XH_s_Rrad] for rate rule [Ct_rad/Ct;COpri_Csrad]
""",
)

entry(
    index = 3469,
    label = "CH3(17) + CH2CO(16) <=> C2H3O(430) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.002, -0.007675, -0.005316, -0.002928],
            [12.47, 0.005738, 0.003962, 0.00217],
            [0.01503, -0.002582, -0.001779, -0.0009714],
            [-0.003211, -0.0001983, -0.0001409, -8.091e-05],
            [-0.004679, 0.0003118, 0.0002164, 0.0001196],
            [-0.002683, 9.707e-05, 6.779e-05, 3.784e-05],
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
    index = 3470,
    label = "C3H3(19) + C2H3O(430) <=> C3H4(39) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]
""",
)

entry(
    index = 3471,
    label = "C2H3O(430) + HCCO(26) <=> CH2CO(16) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]
""",
)

entry(
    index = 3472,
    label = "C2H3O(430) + C3H5(41) <=> C3H6(38) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Csrad]
""",
)

entry(
    index = 3473,
    label = "C3H7(35) + CHO2(424) <=> CO2_5_(8) + C3H8(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]
""",
)

entry(
    index = 3474,
    label = "C3H3(19) + C2H3O(430) <=> C3H4(45) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+12, 'cm^3/(mol*s)'),
        n = -0.047,
        Ea = (1.024, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;XH_s_Rrad] for rate rule [C_rad/H2/Ct;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;XH_s_Rrad] for rate rule [C_rad/H2/Ct;COpri_Csrad]
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
    index = 3476,
    label = "CHO2(424) + S(433) <=> S(428) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.972e+13, 'cm^3/(mol*s)'),
        n = -0.28,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]
""",
)

entry(
    index = 3477,
    label = "CHO2(424) + S(434) <=> S(428) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.013e+10, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (0.912, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;XH_s_Rrad] for rate rule [C_rad/H/CsO;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;XH_s_Rrad] for rate rule [C_rad/H/CsO;COpri_Orad]
""",
)

entry(
    index = 3478,
    label = "CHO2(424) + S(435) <=> S(428) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]
""",
)

entry(
    index = 3479,
    label = "CHO2(424) + CH3CO(18) <=> CO2_5_(8) + C2H4O(431)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]
""",
)

entry(
    index = 3480,
    label = "CHO2(424) + C4H5(443) <=> CO2_5_(8) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]
""",
)

entry(
    index = 3481,
    label = "CHO2(424) + C4H5(443) <=> CO2_5_(8) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 3482,
    label = "CHO2(424) + C4H3(110) <=> CO2_5_(8) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 3483,
    label = "CHO2(424) + C4H3(96) <=> CO2_5_(8) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
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
    index = 3502,
    label = "OH_12_(12) + C9H5(489) <=> H2O_14_(6) + C9H4(500)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
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
    index = 3515,
    label = "H2O2(15) + C4H9O(512) <=> HO2_17_(5) + C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.97, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 304 H2O2 + C4H9O-4 <=> HO2 + C4H10O-4 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Matched reaction 304 H2O2 + C4H9O-4 <=> HO2 + C4H10O-4 in H_Abstraction/training
""",
)

entry(
    index = 3516,
    label = "H_10_(3) + C4H10O(11) <=> H2_13_(2) + C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5220, 'cm^3/(mol*s)'),
        n = 3.04,
        Ea = (2.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/CsO;H_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/CsO;H_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3517,
    label = "HO2_17_(5) + C4H9O(512) <=> O2_2_(13) + C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.485, 'cm^3/(mol*s)'),
        n = 3.39,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/Cs\\H2\\Cs|H2|Cs/O] for rate rule [Orad_O_H;C_rad/H/Cs\\H2\\Cs|H2|Cs/O]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/Cs\H2\Cs|H2|Cs/O] for rate rule [Orad_O_H;C_rad/H/Cs\H2\Cs|H2|Cs/O]
""",
)

entry(
    index = 3518,
    label = "C4H10O(11) + O_11_(7) <=> OH_12_(12) + C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H2/CsO;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C/H2/CsO;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3519,
    label = "C4H10O(11) + OH_12_(12) <=> H2O_14_(6) + C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.89,
        Ea = (-2.291, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 1010 C4H10O-4 + OH <=> H2O + C4H9O-4 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Matched reaction 1010 C4H10O-4 + OH <=> H2O + C4H9O-4 in H_Abstraction/training
""",
)

entry(
    index = 3520,
    label = "C4H10O(11) + CH3(17) <=> Cadd(4) + C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00248, 'cm^3/(mol*s)'),
        n = 4.44,
        Ea = (4.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/CsO;C_methyl]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/CsO;C_methyl]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3521,
    label = "C4H10O(11) + C2H5(31) <=> CCadd(1) + C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.5e-06, 'cm^3/(mol*s)'),
        n = 5.01,
        Ea = (5.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H2/CsO;C_rad/H2/Cs\\H3]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C/H2/CsO;C_rad/H2/Cs\H3]
Multiplied by reaction path degeneracy 2
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
    index = 3524,
    label = "C2H5(31) + C4H9O(512) <=> C4H10O(11) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.424e+12, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;Cmethyl_Csrad] for rate rule [C_rad/H/CsO;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;Cmethyl_Csrad] for rate rule [C_rad/H/CsO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3525,
    label = "CH2OH(32) + C4H9O(512) <=> C4H10O(11) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Csrad] for rate rule [C_rad/H/CsO;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Csrad] for rate rule [C_rad/H/CsO;O_Csrad]
""",
)

entry(
    index = 3526,
    label = "C2H3(29) + C4H9O(512) <=> C4H10O(11) + C2H2(20)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/CsO;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/CsO;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3527,
    label = "C2H4O(431) + C2H3(29) <=> CH3CO(18) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.68, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;Cd_pri_rad] for rate rule [CO/H/Cs;Cd_Cd\\H2_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [CO/H/NonDe;Cd_pri_rad] for rate rule [CO/H/Cs;Cd_Cd\H2_pri_rad]
""",
)

entry(
    index = 3528,
    label = "C4H10O(11) + CH2(T)(24) <=> CH3(17) + C4H9O(512)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/CsO;Y_1centerbirad] for rate rule [C/H2/CsO;CH2_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/CsO;Y_1centerbirad] for rate rule [C/H2/CsO;CH2_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3530,
    label = "CHO2(42) + C4H9O(512) <=> CO2_5_(8) + C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/CsO;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/CsO;O_COrad]
""",
)

entry(
    index = 3532,
    label = "CH2(T)(24) + CH3O(508) <=> CH3(17) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3533,
    label = "HCO(22) + CH3O(508) <=> CH2O(25) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [Y_rad;Cmethyl_Orad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3534,
    label = "CH3O(508) + C3H7(35) <=> CH2O(25) + C3H8(34)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3535,
    label = "CH3O(508) + C2H5(31) <=> CCadd(1) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
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
    index = 3537,
    label = "CH3O(508) + C2H3(29) <=> CH2O(25) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3538,
    label = "HO2_17_(5) + CH3O(508) <=> H2O2(15) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3539,
    label = "C3H3(19) + CH3O(508) <=> CH2O(25) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
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
    index = 3541,
    label = "C2H(21) + CH3O(508) <=> C2H2(20) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3542,
    label = "HCCO(26) + CH3O(508) <=> CH2CO(16) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3543,
    label = "C3H5(41) + CH3O(508) <=> CH2O(25) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3544,
    label = "C3H3(19) + CH3O(508) <=> C3H4(45) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/Ct;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/Ct;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3547,
    label = "CHO2(424) + C4H9O(512) <=> CO2_5_(8) + C4H10O(11)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.013e+10, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (0.912, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;XH_s_Rrad] for rate rule [C_rad/H/CsO;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;XH_s_Rrad] for rate rule [C_rad/H/CsO;COpri_Orad]
""",
)

entry(
    index = 3550,
    label = "HO2_17_(5) + C6H12(514) <=> H2O2(15) + C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002744, 'cm^3/(mol*s)'),
        n = 4.451,
        Ea = (7.588, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H2/CdCs;O_rad/NonDeO]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C/H2/CdCs;O_rad/NonDeO]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3552,
    label = "HO2_17_(5) + C6H11(518) <=> O2_2_(13) + C6H12(514)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.05702, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (17.906, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CdCs] for rate rule [Orad_O_H;C_rad/H/CdCs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CdCs] for rate rule [Orad_O_H;C_rad/H/CdCs]
""",
)

entry(
    index = 3553,
    label = "C6H12(514) + O_11_(7) <=> OH_12_(12) + C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00692, 'cm^3/(mol*s)'),
        n = 4.347,
        Ea = (5.846, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/CdCs;Y_rad_birad_trirad_quadrad] for rate rule [C/H2/CdCs;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/CdCs;Y_rad_birad_trirad_quadrad] for rate rule [C/H2/CdCs;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3554,
    label = "C6H12(514) + OH_12_(12) <=> H2O_14_(6) + C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (67, 'cm^3/(mol*s)'),
        n = 3.475,
        Ea = (-2.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/CdCs;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/CdCs;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3558,
    label = "H2O2(15) + C6H11(518) <=> HO2_17_(5) + C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0351, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;C_rad/H2/Cd\\H_Cd\\H2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;C_rad/H2/Cd\H_Cd\H2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3559,
    label = "HO2_17_(5) + C6H11(518) <=> O2_2_(13) + C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd\\H_Cd\\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\\H_Cd\\H2]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cd\H_Cd\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\H_Cd\H2]
""",
)

entry(
    index = 3564,
    label = "OH_12_(12) + C6H12(519) <=> H2O_14_(6) + C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.09, 'cm^3/(mol*s)'),
        n = 3.774,
        Ea = (-1.49, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cd\\H_Cd\\H\\Cs;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cd\H_Cd\H\Cs;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3565,
    label = "O_11_(7) + C6H12(519) <=> OH_12_(12) + C6H11(518)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.919, 'cm^3/(mol*s)'),
        n = 3.867,
        Ea = (5.322, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd\\H_Cd\\H\\Cs;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Cd\\H_Cd\\H\\Cs;O_atom_triplet]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd\H_Cd\H\Cs;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Cd\H_Cd\H\Cs;O_atom_triplet]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3573,
    label = "HO2_17_(5) + C4H7(522) <=> H2O2(15) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad/H/Cd]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3574,
    label = "O2_2_(13) + C4H7(522) <=> HO2_17_(5) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.676e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cmethyl_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cmethyl_Csrad/H/Cd]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 3580,
    label = "OH_12_(12) + C4H7(522) <=> H2O_14_(6) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Csrad] for rate rule [O_pri_rad;Cmethyl_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Csrad] for rate rule [O_pri_rad;Cmethyl_Csrad/H/Cd]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3581,
    label = "O_11_(7) + C4H7(522) <=> OH_12_(12) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;Cmethyl_Csrad] for rate rule [O_atom_triplet;Cmethyl_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_1centerbirad;Cmethyl_Csrad] for rate rule [O_atom_triplet;Cmethyl_Csrad/H/Cd]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3587,
    label = "OH_12_(12) + C4H8(78) <=> H2O_14_(6) + C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1845, 'cm^3/(mol*s)'),
        n = 4.032,
        Ea = (2.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H2/CdCs;O_pri_rad] + [C/H2/Cd\\H_Cd\\H2/Cs\\H3;O_rad] for rate rule [C/H2/Cd\\H_Cd\\H2/Cs\\H3;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H2/CdCs;O_pri_rad] + [C/H2/Cd\H_Cd\H2/Cs\H3;O_rad] for rate rule [C/H2/Cd\H_Cd\H2/Cs\H3;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3589,
    label = "O2_2_(13) + C6H13(77) <=> HO2_17_(5) + C6H12(514)",
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
    index = 3595,
    label = "OH_12_(12) + C6H13(77) <=> C6H12(514) + H2O_14_(6)",
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
    index = 3596,
    label = "O_11_(7) + C6H13(77) <=> C6H12(514) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.68e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 3597,
    label = "HO2_17_(5) + C6H13(77) <=> C6H12(514) + H2O2(15)",
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
    index = 3603,
    label = "OH_12_(12) + C6H13(77) <=> H2O_14_(6) + C6H12(519)",
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
    index = 3604,
    label = "O_11_(7) + C6H13(77) <=> OH_12_(12) + C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3607,
    label = "HO2_17_(5) + C4H8(78) <=> H2O2(15) + C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000508, 'cm^3/(mol*s)'),
        n = 4.59,
        Ea = (7.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 529 C4H8-4 + HO2 <=> C4H7-4 + H2O2 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Matched reaction 529 C4H8-4 + HO2 <=> C4H7-4 + H2O2 in H_Abstraction/training
""",
)

entry(
    index = 3610,
    label = "HO2_17_(5) + C4H7(522) <=> O2_2_(13) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.05702, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (17.906, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CdCs] for rate rule [Orad_O_H;C_rad/H/CdCs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CdCs] for rate rule [Orad_O_H;C_rad/H/CdCs]
""",
)

entry(
    index = 3639,
    label = "HO2_17_(5) + C4H7(517) <=> H2O2(15) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Cd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Cd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3640,
    label = "O2_2_(13) + C4H7(517) <=> HO2_17_(5) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/Cd_Csrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/Cd_Csrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 3646,
    label = "OH_12_(12) + C4H7(517) <=> H2O_14_(6) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [O_pri_rad;C/H2/Cd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [O_pri_rad;C/H2/Cd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3647,
    label = "O_11_(7) + C4H7(517) <=> OH_12_(12) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/Cd_Csrad] for rate rule [O_atom_triplet;C/H2/Cd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/Cd_Csrad] for rate rule [O_atom_triplet;C/H2/Cd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3652,
    label = "H2O2(15) + C4H7(517) <=> HO2_17_(5) + C4H8(78)",
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
    index = 3655,
    label = "O2_2_(13) + C4H8(78) <=> HO2_17_(5) + C4H7(517)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (52.807, 'kcal/mol'),
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
    index = 3672,
    label = "OH_12_(12) + C4H8(78) <=> H2O_14_(6) + C4H7(517)",
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
    index = 3694,
    label = "OH_12_(12) + C4H8(83) <=> H2O_14_(6) + C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12.18, 'cm^3/(mol*s)'),
        n = 3.774,
        Ea = (-1.49, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cd\\H_Cd\\H\\Cs;O_pri_rad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cd\H_Cd\H\Cs;O_pri_rad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 3705,
    label = "O2_2_(13) + C3H5(65) <=> HO2_17_(5) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+15, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3712,
    label = "HO2_17_(5) + C4H7(522) <=> O2_2_(13) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd\\H_Cd\\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\\H_Cd\\H2]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cd\H_Cd\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\H_Cd\H2]
""",
)

entry(
    index = 3729,
    label = "O2_2_(13) + C4H7(522) <=> HO2_17_(5) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cdpri_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cdpri_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3750,
    label = "OH_12_(12) + C4H7(522) <=> H2O_14_(6) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
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
    index = 3773,
    label = "O2_2_(13) + C6H7(53) <=> HO2_17_(5) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.044, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 8\nEa raised from 0.0 to 8.6 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 8
Ea raised from 0.0 to 8.6 kJ/mol to match endothermicity of reaction.
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
    index = 3797,
    label = "C4H5(509) + H2O2(15) <=> HO2_17_(5) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3800,
    label = "HO2_17_(5) + C4H5(509) <=> O2_2_(13) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.514, 'cm^3/(mol*s)'),
        n = 3.539,
        Ea = (1.808, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_pri_rad] for rate rule [Orad_O_H;Cd_pri_rad]
""",
)

entry(
    index = 3801,
    label = "OH_12_(12) + C4H5(509) <=> O_11_(7) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.2102, 'cm^3/(mol*s)'),
        n = 3.803,
        Ea = (-0.657, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Cd_pri_rad] for rate rule [OH_rad_H;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Cd_pri_rad] for rate rule [OH_rad_H;Cd_pri_rad]
""",
)

entry(
    index = 3802,
    label = "H2O_14_(6) + C4H5(509) <=> OH_12_(12) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (484, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (14.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3839,
    label = "HO2_17_(5) + C4H5(525) <=> O2_2_(13) + C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.05702, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (17.906, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CdCs] for rate rule [Orad_O_H;C_rad/H/CdCs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CdCs] for rate rule [Orad_O_H;C_rad/H/CdCs]
""",
)

entry(
    index = 3840,
    label = "OH_12_(12) + C4H6(523) <=> H2O_14_(6) + C4H5(525)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (134, 'cm^3/(mol*s)'),
        n = 3.475,
        Ea = (-2.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/CdCs;O_pri_rad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/CdCs;O_pri_rad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 3866,
    label = "H2O2(15) + C4H5(465) <=> HO2_17_(5) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_sec_rad] for rate rule [H2O2;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H2O2;Cd_sec_rad] for rate rule [H2O2;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3869,
    label = "HO2_17_(5) + C4H5(465) <=> O2_2_(13) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02545, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (9.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]
""",
)

entry(
    index = 3870,
    label = "O_11_(7) + C4H6(511) <=> OH_12_(12) + C4H5(465)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (309600, 'cm^3/(mol*s)'),
        n = 2.398,
        Ea = (8.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_atom_triplet] + [Cd/H/Cd;Y_rad_birad_trirad_quadrad] for rate rule [Cd/H/Cd;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_atom_triplet] + [Cd/H/Cd;Y_rad_birad_trirad_quadrad] for rate rule [Cd/H/Cd;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3871,
    label = "OH_12_(12) + C4H6(511) <=> H2O_14_(6) + C4H5(465)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1329, 'cm^3/(mol*s)'),
        n = 3.048,
        Ea = (5.843, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 3895,
    label = "HO2_17_(5) + C4H5(465) <=> O2_2_(13) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd\\H_Cd\\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\\H_Cd\\H2]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cd\H_Cd\H2] for rate rule [Orad_O_H;C_rad/H2/Cd\H_Cd\H2]
""",
)

entry(
    index = 3950,
    label = "O2_2_(13) + C4H3(110) <=> HO2_17_(5) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 4002,
    label = "OH_12_(12) + C4H5(509) <=> H2O_14_(6) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
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
    index = 4121,
    label = "O2_2_(13) + C5H5(97) <=> HO2_17_(5) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16.173, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cdpri_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cdpri_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4151,
    label = "O2_2_(13) + C5H5(128) <=> HO2_17_(5) + C5H4(138)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.409e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22.233, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cdpri_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cdpri_Csrad]
Multiplied by reaction path degeneracy 4
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
    index = 4206,
    label = "O_11_(7) + C10H7(125) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
""",
)

entry(
    index = 4228,
    label = "OH_12_(12) + C10H7(541) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4229,
    label = "O_11_(7) + C10H7(541) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 4262,
    label = "OH_12_(12) + C10H7(543) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 4263,
    label = "O_11_(7) + C10H7(543) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
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
    index = 4291,
    label = "CH3CO(18) + C4H5(465) <=> CH2CO(16) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4292,
    label = "C4H5(509) + CH3CO(18) <=> CH2CO(16) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4293,
    label = "CH3CO(18) + C4H3(110) <=> CH2CO(16) + C4H4(445)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4294,
    label = "CH3CO(18) + C4H3(110) <=> C4H4(444) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4295,
    label = "CH3CO(18) + C4H3(96) <=> C4H4(444) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4296,
    label = "CH3CO(18) + C5H3(141) <=> CH2CO(16) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.451e+13, 'cm^3/(mol*s)'),
        n = -0.233,
        Ea = (-0.043, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/Ct;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_pri_rad;Cmethyl_Rrad] for rate rule [C_rad/H2/Ct;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4297,
    label = "CH3CO(18) + C5H3(142) <=> CH2CO(16) + C5H4(130)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Ct_rad/Ct;Cmethyl_Rrad] for rate rule [Ct_rad/Ct;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4315,
    label = "O2_2_(13) + C#CCC(90) <=> HO2_17_(5) + C4H5(532)",
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
    index = 4346,
    label = "OH_12_(12) + C4H5(532) <=> H2O_14_(6) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.406e+11, 'cm^3/(mol*s)'),
        n = 0.623,
        Ea = (1.703, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H2/De_Csrad] + [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H2/De_Csrad] + [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Csrad]
Multiplied by reaction path degeneracy 2
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
    index = 4395,
    label = "OH_12_(12) + C10H7(556) <=> H2O_14_(6) + C10H6(297)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 4411,
    label = "OH_12_(12) + C10H7(544) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4412,
    label = "O_11_(7) + C10H7(544) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4445,
    label = "OH_12_(12) + C10H7(542) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.697e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
""",
)

entry(
    index = 4446,
    label = "O_11_(7) + C10H7(542) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
""",
)

entry(
    index = 4532,
    label = "OH_12_(12) + C10H7(545) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4533,
    label = "O_11_(7) + C10H7(545) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4706,
    label = "O_11_(7) + C3H7O(436) <=> OH_12_(12) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.68e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4707,
    label = "C3H7O(436) + C6H11(518) <=> C6H12(514) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.356e+12, 'cm^3/(mol*s)'),
        n = -0.117,
        Ea = (-0.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec_rad;Cmethyl_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec_rad;Cmethyl_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4708,
    label = "C4H7(522) + C3H7O(436) <=> C3H6O(437) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.356e+12, 'cm^3/(mol*s)'),
        n = -0.117,
        Ea = (-0.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec_rad;Cmethyl_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec_rad;Cmethyl_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4709,
    label = "C3H7O(436) + C4H7(517) <=> C3H6O(437) + C4H8(78)",
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
    index = 4711,
    label = "O_11_(7) + C3H5(65) <=> OH_12_(12) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
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
    index = 4713,
    label = "O_11_(7) + C3H5(66) <=> OH_12_(12) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
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
    index = 4715,
    label = "C4H5(509) + C3H7O(436) <=> C3H6O(437) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4717,
    label = "C3H7O(436) + C4H5(525) <=> C3H6O(437) + C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.356e+12, 'cm^3/(mol*s)'),
        n = -0.117,
        Ea = (-0.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec_rad;Cmethyl_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec_rad;Cmethyl_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4718,
    label = "C4H5(465) + C3H7O(436) <=> C3H6O(437) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Csrad] for rate rule [Cd_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Csrad] for rate rule [Cd_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4721,
    label = "O2_2_(13) + C4H3(96) <=> HO2_17_(5) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+15, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 4
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
    index = 4728,
    label = "CH3CO(18) + C5H3(141) <=> CH2CO(16) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4729,
    label = "CH3CO(18) + C5H3(162) <=> CH2CO(16) + C5H4(158)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4730,
    label = "CH2(T)(24) + C3H7O(436) <=> CH3(17) + C3H6O(437)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CH2_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [CH2_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4731,
    label = "CHO2(42) + C6H11(518) <=> CO2_5_(8) + C6H12(514)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]
""",
)

entry(
    index = 4732,
    label = "CHO2(42) + C6H11(518) <=> CO2_5_(8) + C6H12(519)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 4733,
    label = "C4H5(465) + CHO2(42) <=> CO2_5_(8) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 4734,
    label = "C4H5(509) + CHO2(42) <=> CO2_5_(8) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;O_Rrad] for rate rule [Cd_pri_rad;O_COrad]
""",
)

entry(
    index = 4735,
    label = "CHO2(42) + C4H5(525) <=> CO2_5_(8) + C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]
""",
)

entry(
    index = 4736,
    label = "CHO2(42) + C4H7(522) <=> CO2_5_(8) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]
""",
)

entry(
    index = 4737,
    label = "CHO2(42) + C4H7(517) <=> CO2_5_(8) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 4738,
    label = "CHO2(42) + C4H7(522) <=> CO2_5_(8) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 4739,
    label = "CHO2(42) + C4H5(532) <=> CO2_5_(8) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 4740,
    label = "C4H5(465) + CHO2(42) <=> CO2_5_(8) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 4745,
    label = "OH_12_(12) + C10H7(564) <=> H2O_14_(6) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
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
    index = 4780,
    label = "H2O2(15) + C6H13(568) <=> HO2_17_(5) + C6H14(10)",
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
    index = 4782,
    label = "O2_2_(13) + C6H14(10) <=> HO2_17_(5) + C6H13(568)",
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
    index = 4783,
    label = "C6H14(10) + O_11_(7) <=> OH_12_(12) + C6H13(568)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (95600, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4784,
    label = "C6H14(10) + OH_12_(12) <=> H2O_14_(6) + C6H13(568)",
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
    index = 4795,
    label = "O2_2_(13) + C5H11(36) <=> HO2_17_(5) + C5H10(570)",
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
    index = 4801,
    label = "OH_12_(12) + C5H11(36) <=> H2O_14_(6) + C5H10(570)",
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
    index = 4802,
    label = "O_11_(7) + C5H11(36) <=> OH_12_(12) + C5H10(570)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4804,
    label = "HO2_17_(5) + C5H11(36) <=> H2O2(15) + C5H10(570)",
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
    index = 4809,
    label = "H2O2(15) + C6H11(569) <=> HO2_17_(5) + C6H12(565)",
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
    index = 4811,
    label = "O2_2_(13) + C6H12(565) <=> HO2_17_(5) + C6H11(569)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.764e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47.69, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O2b]\nMultiplied by reaction path degeneracy 24',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O2b]
Multiplied by reaction path degeneracy 24
""",
)

entry(
    index = 4812,
    label = "C6H12(565) + O_11_(7) <=> OH_12_(12) + C6H11(569)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (286800, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 4813,
    label = "C6H12(565) + OH_12_(12) <=> H2O_14_(6) + C6H11(569)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.74e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (0.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 4825,
    label = "O2_2_(13) + C6H11(569) <=> HO2_17_(5) + C6H10(573)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.332e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 16',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 16
""",
)

entry(
    index = 4826,
    label = "O_11_(7) + C6H11(569) <=> OH_12_(12) + C6H10(573)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.24e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 4827,
    label = "OH_12_(12) + C6H11(569) <=> H2O_14_(6) + C6H10(573)",
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
    index = 4847,
    label = "OH_12_(12) + C6H11(574) <=> H2O_14_(6) + C6H10(84)",
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
    index = 4924,
    label = "CHO2(42) + C6H13(568) <=> CO2_5_(8) + C6H14(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]
""",
)

entry(
    index = 4925,
    label = "CHO2(42) + C6H11(569) <=> CO2_5_(8) + C6H12(565)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]
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
    index = 4951,
    label = "OH_12_(12) + C7H8(61) <=> H2O_14_(6) + C7H7(580)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.045, 'cm^3/(mol*s)'),
        n = 3.684,
        Ea = (-1.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H3/Cd;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C/H3/Cd;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 4963,
    label = "OH_12_(12) + C7H8(61) <=> H2O_14_(6) + C7H7(581)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1329, 'cm^3/(mol*s)'),
        n = 3.048,
        Ea = (5.843, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4975,
    label = "OH_12_(12) + C7H8(61) <=> H2O_14_(6) + C7H7(588)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1329, 'cm^3/(mol*s)'),
        n = 3.048,
        Ea = (5.843, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 4984,
    label = "OH_12_(12) + C7H8(61) <=> H2O_14_(6) + C7H7(589)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (664.7, 'cm^3/(mol*s)'),
        n = 3.048,
        Ea = (5.843, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cd_sec;O_pri_rad] + [Cd/H/Cd;Y_rad] for rate rule [Cd/H/Cd;O_pri_rad]
""",
)

entry(
    index = 4997,
    label = "HO2_17_(5) + C7H7(580) <=> O2_2_(13) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1313, 'cm^3/(mol*s)'),
        n = 3.978,
        Ea = (14.261, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd] for rate rule [Orad_O_H;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cd] for rate rule [Orad_O_H;C_rad/H2/Cd]
""",
)

entry(
    index = 4998,
    label = "HO2_17_(5) + C7H7(581) <=> O2_2_(13) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02545, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (9.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]
""",
)

entry(
    index = 4999,
    label = "HO2_17_(5) + C7H7(589) <=> O2_2_(13) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02545, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (9.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]
""",
)

entry(
    index = 5000,
    label = "HO2_17_(5) + C7H7(588) <=> O2_2_(13) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02545, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (9.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]
""",
)

entry(
    index = 5098,
    label = "C7H7(580) + CHO2(42) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 5099,
    label = "CHO2(42) + C7H7(588) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 5100,
    label = "CHO2(42) + C7H7(581) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 5101,
    label = "CHO2(42) + C7H7(589) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
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
    index = 5111,
    label = "CH2OH(32) + C6H13(568) <=> C6H14(10) + CH2O(25)",
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
    index = 5112,
    label = "HCO(22) + C5H11(36) <=> CH2O(25) + C5H10(570)",
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
    index = 5113,
    label = "CH2OH(32) + C4H7(522) <=> CH2O(25) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.339e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.275, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec_rad;O_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec_rad;O_Csrad] + [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_Csrad]
""",
)

entry(
    index = 5114,
    label = "CH2OH(32) + C4H7(517) <=> CH2O(25) + C4H8(78)",
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
    index = 5115,
    label = "C4H5(509) + CH2OH(32) <=> C4H6(511) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd_pri_rad;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd_pri_rad;O_Csrad]
""",
)

entry(
    index = 5116,
    label = "HCO(22) + C4H7(517) <=> C4H6(511) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [CO_pri_rad;C/H2/Cd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [CO_pri_rad;C/H2/Cd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5117,
    label = "HCO(22) + C4H7(522) <=> C4H6(511) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Csrad/H/Cd] for rate rule [CO_pri_rad;Cmethyl_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Csrad/H/Cd] for rate rule [CO_pri_rad;Cmethyl_Csrad/H/Cd]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5118,
    label = "CH2OH(32) + C4H7(522) <=> CH2O(25) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;O_Csrad]
""",
)

entry(
    index = 5119,
    label = "HCO(22) + C4H7(522) <=> CH2O(25) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;Cdpri_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;Cdpri_Csrad] + [CO_pri_rad;XH_s_Rrad] for rate rule [CO_pri_rad;Cdpri_Csrad]
""",
)

entry(
    index = 5120,
    label = "CH2OH(32) + C7H7(580) <=> C7H8(61) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/Cd;O_Csrad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C_rad/H2/Cd;O_Csrad]
""",
)

entry(
    index = 5121,
    label = "CH2OH(32) + C7H7(588) <=> C7H8(61) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 5122,
    label = "CH2OH(32) + C7H7(581) <=> C7H8(61) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 5123,
    label = "CH2OH(32) + C7H7(589) <=> C7H8(61) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 5124,
    label = "CHO2(424) + C6H11(569) <=> C6H12(565) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.972e+13, 'cm^3/(mol*s)'),
        n = -0.28,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]
""",
)

entry(
    index = 5125,
    label = "CHO2(424) + C6H13(568) <=> C6H14(10) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.972e+13, 'cm^3/(mol*s)'),
        n = -0.28,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]
""",
)

entry(
    index = 5126,
    label = "C4H7(522) + CHO2(424) <=> CO2_5_(8) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]
""",
)

entry(
    index = 5127,
    label = "CHO2(424) + C4H7(517) <=> CO2_5_(8) + C4H8(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]
""",
)

entry(
    index = 5128,
    label = "C4H5(509) + CHO2(424) <=> CO2_5_(8) + C4H6(511)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Orad]
""",
)

entry(
    index = 5129,
    label = "CHO2(424) + C4H5(525) <=> CO2_5_(8) + C4H6(523)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]
""",
)

entry(
    index = 5130,
    label = "C4H7(522) + CHO2(424) <=> CO2_5_(8) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]
""",
)

entry(
    index = 5131,
    label = "C7H7(580) + CHO2(424) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]
""",
)

entry(
    index = 5132,
    label = "CHO2(424) + C7H7(588) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 5133,
    label = "CHO2(424) + C7H7(581) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 5134,
    label = "CHO2(424) + C7H7(589) <=> CO2_5_(8) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 5166,
    label = "OH_12_(12) + C7H9(592) <=> H2O_14_(6) + C7H8(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5186,
    label = "HCO(22) + C7H9(592) <=> C7H8(61) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5192,
    label = "H2O2(15) + C5H11(593) <=> HO2_17_(5) + C5H12(9)",
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
    index = 5194,
    label = "C5H12(9) + O2_2_(13) <=> HO2_17_(5) + C5H11(593)",
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
    index = 5195,
    label = "C5H12(9) + O_11_(7) <=> OH_12_(12) + C5H11(593)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (95600, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5196,
    label = "C5H12(9) + OH_12_(12) <=> H2O_14_(6) + C5H11(593)",
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
    index = 5214,
    label = "CHO2(42) + C5H11(593) <=> C5H12(9) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]
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
    index = 5216,
    label = "CH3(17) + CH3O(508) <=> Cadd(4) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.878e+10, 'cm^3/(mol*s)'),
        n = 0.595,
        Ea = (-0.555, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;Cmethyl_Rrad] for rate rule [C_methyl;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_methyl;Cmethyl_Rrad] for rate rule [C_methyl;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5217,
    label = "H_10_(3) + CH3O(508) <=> H2_13_(2) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.086e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 5218,
    label = "CH3O(508) + C5H11(593) <=> C5H12(9) + CH2O(25)",
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
    index = 5219,
    label = "CH2OH(32) + C5H11(593) <=> C5H12(9) + CH2O(25)",
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
    index = 5220,
    label = "OH_12_(12) + CH3O(508) <=> H2O_14_(6) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.794e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.595, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_pri_rad;Cmethyl_Rrad] for rate rule [O_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5221,
    label = "C3H5(66) + CH3O(508) <=> C3H6(38) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5222,
    label = "C3H5(65) + CH3O(508) <=> C3H6(38) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5223,
    label = "C4H7(85) + CH3O(508) <=> CH2O(25) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5224,
    label = "C6H5(64) + CH3O(508) <=> CH2O(25) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5225,
    label = "R1(63) + CH3O(508) <=> C8H6(74) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5226,
    label = "CH3O(508) + C8H5(144) <=> C8H6(74) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5227,
    label = "CH3O(508) + C8H5(145) <=> C8H6(74) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5228,
    label = "CH3O(508) + C8H5(198) <=> CH2O(25) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [Cb_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5229,
    label = "CH3O(508) + C8H5(186) <=> CH2O(25) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5230,
    label = "CHO2(424) + C5H11(593) <=> C5H12(9) + CO2_5_(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.972e+13, 'cm^3/(mol*s)'),
        n = -0.28,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]
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
    index = 5269,
    label = "OH_12_(12) + C6H8(608) <=> H2O_14_(6) + C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.007296, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-0.451, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H/CdCd;Y_rad] for rate rule [C/H/CdCd;O_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [C/H/CdCd;Y_rad] for rate rule [C/H/CdCd;O_pri_rad]
""",
)

entry(
    index = 5274,
    label = "HO2_17_(5) + C6H7(52) <=> O2_2_(13) + C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.007642, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (25.299, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/CdCdCs] for rate rule [Orad_O_H;C_rad/CdCdCs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/CdCdCs] for rate rule [Orad_O_H;C_rad/CdCdCs]
""",
)

entry(
    index = 5275,
    label = "HO2_17_(5) + C6H7(55) <=> O2_2_(13) + C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5763, 'cm^3/(mol*s)'),
        n = 3.502,
        Ea = (5.889, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]
""",
)

entry(
    index = 5300,
    label = "OH_12_(12) + C6H8(597) <=> H2O_14_(6) + C6H7(53)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.045, 'cm^3/(mol*s)'),
        n = 3.684,
        Ea = (-1.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd;O_pri_rad] for rate rule [1_methyl_CPD;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd;O_pri_rad] for rate rule [1_methyl_CPD;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5305,
    label = "OH_12_(12) + C6H8(597) <=> H2O_14_(6) + C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (374.3, 'cm^3/(mol*s)'),
        n = 3.147,
        Ea = (0.219, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec;O_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec;O_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5311,
    label = "HO2_17_(5) + C6H7(52) <=> O2_2_(13) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1513, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (25.223, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CdCd] for rate rule [Orad_O_H;C_rad/H/CdCd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CdCd] for rate rule [Orad_O_H;C_rad/H/CdCd]
""",
)

entry(
    index = 5312,
    label = "HO2_17_(5) + C6H7(53) <=> O2_2_(13) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1313, 'cm^3/(mol*s)'),
        n = 3.978,
        Ea = (14.261, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd] for rate rule [Orad_O_H;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cd] for rate rule [Orad_O_H;C_rad/H2/Cd]
""",
)

entry(
    index = 5337,
    label = "OH_12_(12) + C6H8(607) <=> H2O_14_(6) + C6H7(56)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.045, 'cm^3/(mol*s)'),
        n = 3.684,
        Ea = (-1.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd;O_pri_rad] for rate rule [2_methyl_CPD;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd;O_pri_rad] for rate rule [2_methyl_CPD;O_pri_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5341,
    label = "OH_12_(12) + C6H8(607) <=> H2O_14_(6) + C6H7(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (374.3, 'cm^3/(mol*s)'),
        n = 3.147,
        Ea = (0.219, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec;O_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec;O_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5347,
    label = "HO2_17_(5) + C6H7(52) <=> O2_2_(13) + C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1513, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (25.223, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CdCd] for rate rule [Orad_O_H;C_rad/H/CdCd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CdCd] for rate rule [Orad_O_H;C_rad/H/CdCd]
""",
)

entry(
    index = 5348,
    label = "HO2_17_(5) + C6H7(56) <=> O2_2_(13) + C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1313, 'cm^3/(mol*s)'),
        n = 3.978,
        Ea = (14.261, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cd] for rate rule [Orad_O_H;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H2/Cd] for rate rule [Orad_O_H;C_rad/H2/Cd]
""",
)

entry(
    index = 5372,
    label = "O_11_(7) + CPD(595) <=> OH_12_(12) + CPDyl(596)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51.75, 'cm^3/(mol*s)'),
        n = 3.465,
        Ea = (1.205, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec;O_atom_triplet] + [C/H2/CdCd;Y_rad_birad_trirad_quadrad] for rate rule [C/H2/CdCd;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec;O_atom_triplet] + [C/H2/CdCd;Y_rad_birad_trirad_quadrad] for rate rule [C/H2/CdCd;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5376,
    label = "OH_12_(12) + CPD(595) <=> H2O_14_(6) + CPDyl(596)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (374.3, 'cm^3/(mol*s)'),
        n = 3.147,
        Ea = (0.219, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec;O_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec;O_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5400,
    label = "HO2_17_(5) + CPDyl(596) <=> O2_2_(13) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1513, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (25.223, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/CdCd] for rate rule [Orad_O_H;C_rad/H/CdCd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/CdCd] for rate rule [Orad_O_H;C_rad/H/CdCd]
""",
)

entry(
    index = 5401,
    label = "HO2_17_(5) + C5H5(50) <=> O2_2_(13) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.03678, 'cm^3/(mol*s)'),
        n = 4.051,
        Ea = (0.898, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/NonDeC] for rate rule [Orad_O_H;Cd_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/NonDeC] for rate rule [Orad_O_H;Cd_rad/NonDeC]
""",
)

entry(
    index = 5448,
    label = "CH3CO(18) + CPDyl(596) <=> CH2CO(16) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;Cmethyl_Rrad] for rate rule [C_rad/H/TwoDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;Cmethyl_Rrad] for rate rule [C_rad/H/TwoDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5449,
    label = "CH3CO(18) + C5H5(50) <=> CH2CO(16) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5456,
    label = "CHO2(42) + C6H7(52) <=> CO2_5_(8) + C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.47e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;O_Rrad] for rate rule [C_rad/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;O_Rrad] for rate rule [C_rad/Cs;O_COrad]
""",
)

entry(
    index = 5457,
    label = "CHO2(42) + C6H7(55) <=> CO2_5_(8) + C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 5458,
    label = "CHO2(42) + C6H7(52) <=> CO2_5_(8) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]
""",
)

entry(
    index = 5459,
    label = "CHO2(42) + C6H7(53) <=> CO2_5_(8) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 5460,
    label = "CHO2(42) + C6H7(52) <=> CO2_5_(8) + C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]
""",
)

entry(
    index = 5461,
    label = "CHO2(42) + C6H7(56) <=> CO2_5_(8) + C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;O_Rrad] for rate rule [C_rad/H2/Cd;O_COrad]
""",
)

entry(
    index = 5462,
    label = "CHO2(42) + CPDyl(596) <=> CO2_5_(8) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]
""",
)

entry(
    index = 5463,
    label = "CHO2(42) + C5H5(50) <=> CO2_5_(8) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/NonDeC;O_COrad]
""",
)

entry(
    index = 5466,
    label = "HCO(22) + CPD(595) <=> CH2O(25) + CPDyl(596)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (589.4, 'cm^3/(mol*s)'),
        n = 3.12,
        Ea = (8.963, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec;CO_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;CO_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec;CO_pri_rad] + [C/H2/CdCd;Y_rad] for rate rule [C/H2/CdCd;CO_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5467,
    label = "CH2OH(32) + CPDyl(596) <=> CH2O(25) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Csrad] for rate rule [C_rad/H/TwoDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Csrad] for rate rule [C_rad/H/TwoDe;O_Csrad]
""",
)

entry(
    index = 5468,
    label = "CH2OH(32) + C5H5(50) <=> CH2O(25) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/NonDeC;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 5469,
    label = "CHO2(424) + C6H7(52) <=> CO2_5_(8) + C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.318e+14, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_ter_rad;XH_s_Rrad] for rate rule [C_rad/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_ter_rad;XH_s_Rrad] for rate rule [C_rad/Cs;COpri_Orad]
""",
)

entry(
    index = 5470,
    label = "CHO2(424) + C6H7(55) <=> CO2_5_(8) + C6H8(608)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]
""",
)

entry(
    index = 5471,
    label = "CHO2(424) + C6H7(52) <=> CO2_5_(8) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.114e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]
""",
)

entry(
    index = 5472,
    label = "CHO2(424) + C6H7(53) <=> CO2_5_(8) + C6H8(597)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]
""",
)

entry(
    index = 5473,
    label = "CHO2(424) + C6H7(52) <=> CO2_5_(8) + C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.114e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]
""",
)

entry(
    index = 5474,
    label = "CHO2(424) + C6H7(56) <=> CO2_5_(8) + C6H8(607)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Orad]
""",
)

entry(
    index = 5475,
    label = "CHO2(424) + CPDyl(596) <=> CO2_5_(8) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.114e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]
""",
)

entry(
    index = 5476,
    label = "CHO2(424) + C5H5(50) <=> CO2_5_(8) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/NonDeC;COpri_Orad]
""",
)

entry(
    index = 5490,
    label = "HO2_17_(5) + C5H5(179) <=> O2_2_(13) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02545, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (9.01, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;Cd_rad/Cd] for rate rule [Orad_O_H;Cd_rad/Cd]
""",
)

entry(
    index = 5491,
    label = "CHO2(424) + C5H5(179) <=> CO2_5_(8) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 5492,
    label = "CHO2(42) + C5H5(179) <=> CO2_5_(8) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Rrad] for rate rule [Cd_rad/OneDe;O_COrad]
""",
)

entry(
    index = 5511,
    label = "CH3CO(18) + C5H5(179) <=> CH2CO(16) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5521,
    label = "CH2OH(32) + C5H5(179) <=> CH2O(25) + CPD(595)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;O_Csrad] for rate rule [Cd_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 5530,
    label = "OH_12_(12) + CH2O2(594) <=> H2O_14_(6) + CHO2(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-1.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_pri_rad]
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
    index = 5533,
    label = "H_10_(3) + CH2O2(594) <=> H2_13_(2) + CHO2(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;H_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;H_rad]
""",
)

entry(
    index = 5534,
    label = "H_10_(3) + CH2O2(594) <=> H2_13_(2) + CHO2(424)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (8.159, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;H_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;H_rad]
""",
)

entry(
    index = 5535,
    label = "OH_12_(12) + CH2O2(594) <=> H2O_14_(6) + CHO2(424)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;O_pri_rad]
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
    index = 5537,
    label = "O_11_(7) + CH2O2(594) <=> OH_12_(12) + CHO2(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.79, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_atom_triplet]
""",
)

entry(
    index = 5538,
    label = "O_11_(7) + CH2O2(594) <=> OH_12_(12) + CHO2(424)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9.599, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]
""",
)

entry(
    index = 5539,
    label = "O2_2_(13) + CH2O2(594) <=> HO2_17_(5) + CHO2(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49.785, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5540,
    label = "HO2_17_(5) + CHO2(424) <=> O2_2_(13) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000188, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (12.422, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]
""",
)

entry(
    index = 5541,
    label = "CHO2(42) + CHO2(424) <=> CO2_5_(8) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5542,
    label = "CHO2(424) + CHO2(424) <=> CO2_5_(8) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.156e+07, 'cm^3/(mol*s)'),
        n = 1.793,
        Ea = (-1.067, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5543,
    label = "CHO2(42) + CHO2(42) <=> CO2_5_(8) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]
Multiplied by reaction path degeneracy 2
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
    index = 5546,
    label = "H_10_(3) + CH2O2(594) <=> OH_12_(12) + CH2O(25)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.504, -0.001254, -0.0008718, -0.0004834],
            [7.261, -0.0009713, -0.0006751, -0.000374],
            [0.1108, 8.356e-05, 5.821e-05, 3.235e-05],
            [0.03287, 0.0003203, 0.0002226, 0.0001233],
            [0.01074, 0.0001315, 9.132e-05, 5.05e-05],
            [0.003091, -3.845e-05, -2.674e-05, -1.483e-05],
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
    index = 5547,
    label = "H_10_(3) + CH2O2(594) <=> O_11_(7) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-5.408, -0.0004923, -0.0003424, -0.00019],
            [13.75, -0.0005023, -0.0003493, -0.0001937],
            [-0.07782, -7.001e-05, -4.856e-05, -2.686e-05],
            [-0.01855, 8.493e-05, 5.917e-05, 3.288e-05],
            [-0.003165, 5.345e-05, 3.723e-05, 2.067e-05],
            [-0.0003777, -4.386e-06, -3.03e-06, -1.673e-06],
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
    index = 5548,
    label = "CHO2(42) + CH2O(25) <=> CH2O2(594) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12.92, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;CO_rad/NonDe]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO_pri;CO_rad/NonDe]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5549,
    label = "CHO2(424) + CH2O(25) <=> CH2O2(594) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156.1, 'cm^3/(mol*s)'),
        n = 2.935,
        Ea = (9.509, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;O_rad/OneDeC] + [CO_pri;O_sec_rad] for rate rule [CO_pri;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [X_H;O_rad/OneDeC] + [CO_pri;O_sec_rad] for rate rule [CO_pri;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5550,
    label = "HO2_17_(5) + CH2O2(594) <=> CHO2(42) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.92, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_rad/NonDeO]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_rad/NonDeO]
""",
)

entry(
    index = 5551,
    label = "CHO2(424) + H2O2(15) <=> HO2_17_(5) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0699, 'cm^3/(mol*s)'),
        n = 3.75,
        Ea = (10.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [H2O2;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [H2O2;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5552,
    label = "CHO2(424) + CH2O2(594) <=> CHO2(42) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23980, 'cm^3/(mol*s)'),
        n = 2.125,
        Ea = (6.365, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;O_sec_rad] for rate rule [CO/H/NonDe;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO/H/NonDe;O_sec_rad] for rate rule [CO/H/NonDe;O_rad/OneDeC]
""",
)

entry(
    index = 5553,
    label = "CHO2(424) + HCO(22) <=> CO_21_(14) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.35, -0.5036, -0.2106, -0.0309],
            [0.2834, 0.4888, 0.1684, -0.004422],
            [-0.02956, 0.02289, 0.0381, 0.02406],
            [-0.0378, -0.03397, -0.01052, 0.00457],
            [-0.01256, -0.01401, -0.009163, -0.003256],
            [0.0002716, 0.0005493, -0.001428, -0.001997],
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
    index = 5554,
    label = "CHO2(42) + CH2OH(32) <=> CH2O2(594) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
""",
)

entry(
    index = 5555,
    label = "CHO2(424) + CH2OH(32) <=> CH2O2(594) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.708e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 5562,
    label = "O2_2_(13) + C4H9(635) <=> HO2_17_(5) + C4H8(78)",
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
    index = 5563,
    label = "OH_12_(12) + C4H9(635) <=> H2O_14_(6) + C4H8(78)",
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
    index = 5564,
    label = "O_11_(7) + C4H9(635) <=> C4H8(78) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.68e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5565,
    label = "HO2_17_(5) + C4H9(635) <=> C4H8(78) + H2O2(15)",
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
    index = 5568,
    label = "HO2_17_(5) + C4H9(635) <=> H2O2(15) + C4H8(83)",
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
    index = 5569,
    label = "O_11_(7) + C4H9(635) <=> OH_12_(12) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_1centerbirad;C/H2/Nd_Csrad] for rate rule [O_atom_triplet;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5570,
    label = "OH_12_(12) + C4H9(635) <=> H2O_14_(6) + C4H8(83)",
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
    index = 5571,
    label = "O2_2_(13) + C4H9(635) <=> HO2_17_(5) + C4H8(83)",
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
    index = 5579,
    label = "C4H8(78) + O_11_(7) <=> OH_12_(12) + C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000508, 'cm^3/(mol*s)'),
        n = 4.59,
        Ea = (7.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/Cd\\H_Cd\\H2/Cs\\H3;Y_rad_birad_trirad_quadrad] for rate rule [C/H2/Cd\\H_Cd\\H2/Cs\\H3;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/Cd\H_Cd\H2/Cs\H3;Y_rad_birad_trirad_quadrad] for rate rule [C/H2/Cd\H_Cd\H2/Cs\H3;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5581,
    label = "HO2_17_(5) + C4H8(83) <=> H2O2(15) + C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00347, 'cm^3/(mol*s)'),
        n = 4.65,
        Ea = (9.78, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 525 C4H8-2 + HO2 <=> C4H7-2 + H2O2 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Matched reaction 525 C4H8-2 + HO2 <=> C4H7-2 + H2O2 in H_Abstraction/training
""",
)

entry(
    index = 5584,
    label = "O_11_(7) + C4H8(83) <=> OH_12_(12) + C4H7(522)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.838, 'cm^3/(mol*s)'),
        n = 3.867,
        Ea = (5.322, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd\\H_Cd\\H\\Cs;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Cd\\H_Cd\\H\\Cs;O_atom_triplet]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd\H_Cd\H\Cs;Y_rad_birad_trirad_quadrad] for rate rule [C/H3/Cd\H_Cd\H\Cs;O_atom_triplet]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 5592,
    label = "C4H8(78) + O_11_(7) <=> OH_12_(12) + C4H7(517)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2850, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (3.123, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/Cs;O_atom_triplet]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H3/Cs;O_atom_triplet]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5607,
    label = "HO2_17_(5) + C6H7(55) <=> C6H6(54) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.368e+07, 'cm^3/(mol*s)'),
        n = 1.549,
        Ea = (0.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_rad;C/H/DeDe_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H/DeDe_Csrad]
""",
)

entry(
    index = 5608,
    label = "HO2_17_(5) + C6H7(53) <=> C6H6(54) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/NonDeO;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/NonDeO;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5609,
    label = "HO2_17_(5) + C6H7(56) <=> C6H6(54) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/NonDeO;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/NonDeO;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5610,
    label = "HO2_17_(5) + C6H7(52) <=> C6H6(54) + H2O2(15)",
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
    index = 5611,
    label = "O2_2_(13) + C6H7(55) <=> HO2_17_(5) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H/DeDe_Rrad] for rate rule [O2b;C/H/DeDe_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H/DeDe_Rrad] for rate rule [O2b;C/H/DeDe_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 5612,
    label = "O2_2_(13) + C6H7(56) <=> HO2_17_(5) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Estimated using template [O2b;C/H2/De_Csrad] for rate rule [O2b;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 5620,
    label = "H2O2(15) + C6H5(105) <=> HO2_17_(5) + C6H6(54)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5650,
    label = "O2_2_(13) + C4H5(443) <=> HO2_17_(5) + C4H4(444)",
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
    index = 5671,
    label = "HO2_17_(5) + C4H3(110) <=> H2O2(15) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5678,
    label = "HO2_17_(5) + C4H3(96) <=> H2O2(15) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
""",
)

entry(
    index = 5711,
    label = "CH3CO(18) + C4H7(522) <=> C4H8(78) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.289e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5712,
    label = "CH3CO(18) + C4H7(517) <=> C4H8(78) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5713,
    label = "CH3CO(18) + C4H7(522) <=> CH2CO(16) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5714,
    label = "CH3CO(18) + C6H5(105) <=> C6H6(54) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5732,
    label = "H2O2(15) + C4H7(85) <=> HO2_17_(5) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Matched reaction 527 H2O2 + C4H7-3 <=> HO2 + C4H8-3 in H_Abstraction/training',
    ),
    longDesc = 
u"""
Matched reaction 527 H2O2 + C4H7-3 <=> HO2 + C4H8-3 in H_Abstraction/training
""",
)

entry(
    index = 5734,
    label = "OH_12_(12) + C4H8(83) <=> H2O_14_(6) + C4H7(85)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.22e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd/H/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd/H/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5761,
    label = "CH3CO(18) + C4H7(85) <=> CH2CO(16) + C4H8(83)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/NonDeC;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
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
    index = 5845,
    label = "HO2_17_(5) + C3H5(65) <=> H2O2(15) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
""",
)

entry(
    index = 5846,
    label = "HO2_17_(5) + C3H5(66) <=> H2O2(15) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5847,
    label = "O2_2_(13) + C3H5(66) <=> HO2_17_(5) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 8
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
    index = 5881,
    label = "OH_12_(12) + CPD(595) <=> H2O_14_(6) + C5H5(50)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.22e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [Cd/H/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Cd/H/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 2
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
    index = 5916,
    label = "C2H5(31) + C6H6O(661) <=> CCadd(1) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.05784, 'cm^3/(mol*s)'),
        n = 3.835,
        Ea = (4.561, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H2/Cs] + [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeC;C_rad/H2/Cs\\H3]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;C_rad/H2/Cs] + [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeC;C_rad/H2/Cs\H3]
""",
)

entry(
    index = 5917,
    label = "O_11_(7) + C6H6O(661) <=> OH_12_(12) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]
""",
)

entry(
    index = 5918,
    label = "CH3(17) + C6H6O(661) <=> Cadd(4) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (6.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;C_methyl]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O/H/OneDeC;C_methyl]
""",
)

entry(
    index = 5919,
    label = "H_10_(3) + C6H6O(661) <=> H2_13_(2) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;H_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O/H/OneDeC;H_rad]
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
    index = 5921,
    label = "OH_12_(12) + C6H6O(661) <=> H2O_14_(6) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_pri_rad]',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O/H/OneDeC;O_pri_rad]
""",
)

entry(
    index = 5922,
    label = "CH2(T)(24) + C6H6O(661) <=> CH3(17) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeC;Y_1centerbirad] for rate rule [O/H/OneDeC;CH2_triplet]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeC;Y_1centerbirad] for rate rule [O/H/OneDeC;CH2_triplet]
""",
)

entry(
    index = 5923,
    label = "C3H5(41) + C6H5O(610) <=> C3H4(39) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cdpri_Csrad] for rate rule [O_rad/OneDe;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cdpri_Csrad] for rate rule [O_rad/OneDe;Cdpri_Csrad]
""",
)

entry(
    index = 5924,
    label = "C3H5(41) + C6H6O(661) <=> C3H6(38) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;C_rad/H2/Cd\\H_Cd\\H2] for rate rule [O/H/OneDeC;C_rad/H2/Cd\\H_Cd\\H2]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;C_rad/H2/Cd\H_Cd\H2] for rate rule [O/H/OneDeC;C_rad/H2/Cd\H_Cd\H2]
""",
)

entry(
    index = 5925,
    label = "C3H5(66) + C6H6O(661) <=> C3H6(38) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_rad/NonDeC] for rate rule [O/H/OneDeC;Cd_Cd\\H2_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_rad/NonDeC] for rate rule [O/H/OneDeC;Cd_Cd\H2_rad/Cs]
""",
)

entry(
    index = 5926,
    label = "C3H5(65) + C6H6O(661) <=> C3H6(38) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_Cd\\H\\Cs_pri_rad] for rate rule [O/H/OneDeC;Cd_Cd\\H\\Cs_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_Cd\H\Cs_pri_rad] for rate rule [O/H/OneDeC;Cd_Cd\H\Cs_pri_rad]
""",
)

entry(
    index = 5927,
    label = "C2H(21) + C6H6O(661) <=> C2H2(20) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.839e+06, 'cm^3/(mol*s)'),
        n = 1.828,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Ct_rad/Ct]
""",
)

entry(
    index = 5928,
    label = "C2H3(29) + C6H6O(661) <=> C2H4(30) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.433, 'cm^3/(mol*s)'),
        n = 3.38,
        Ea = (-2.673, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_pri_rad] for rate rule [O/H/OneDeC;Cd_Cd\\H2_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_pri_rad] for rate rule [O/H/OneDeC;Cd_Cd\H2_pri_rad]
""",
)

entry(
    index = 5929,
    label = "C3H3(19) + C6H6O(661) <=> C3H4(39) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.839e+06, 'cm^3/(mol*s)'),
        n = 1.828,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cd_Cdd_rad/H]
""",
)

entry(
    index = 5930,
    label = "C3H3(19) + C6H6O(661) <=> C3H4(45) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.245,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDe;C_rad/H2/Ct] for rate rule [O/H/OneDeC;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDe;C_rad/H2/Ct] for rate rule [O/H/OneDeC;C_rad/H2/Ct]
""",
)

entry(
    index = 5931,
    label = "C6H6O(661) + C6H5(105) <=> C6H6(54) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3056, 'cm^3/(mol*s)'),
        n = 2.604,
        Ea = (0.743, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;Cd_pri_rad] + [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cd_pri_rad]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;Cd_pri_rad] + [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cd_pri_rad]
""",
)

entry(
    index = 5932,
    label = "C6H5(64) + C6H6O(661) <=> C6H6(48) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]
""",
)

entry(
    index = 5933,
    label = "C4H3(110) + C6H5O(610) <=> C6H6O(661) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5934,
    label = "C6H8(608) + C6H5O(610) <=> C6H7(52) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.342e-05, 'cm^3/(mol*s)'),
        n = 5.055,
        Ea = (5.795, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Cs_H;O_rad/OneDeC] + [C/H/CdCd;Y_rad] for rate rule [C/H/CdCd;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [Cs_H;O_rad/OneDeC] + [C/H/CdCd;Y_rad] for rate rule [C/H/CdCd;O_rad/OneDeC]
""",
)

entry(
    index = 5935,
    label = "C6H7(55) + C6H6O(661) <=> C6H8(608) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.245,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeC;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeC;C_rad/H2/Cs]
""",
)

entry(
    index = 5936,
    label = "C6H8(597) + C6H5O(610) <=> C6H7(52) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.504e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCd;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCd;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5937,
    label = "C6H8(597) + C6H5O(610) <=> C6H7(53) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.256e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd;O_rad/OneDeC] for rate rule [1_methyl_CPD;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd;O_rad/OneDeC] for rate rule [1_methyl_CPD;O_rad/OneDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5938,
    label = "C6H8(607) + C6H5O(610) <=> C6H7(52) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.504e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCd;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCd;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5939,
    label = "C6H8(607) + C6H5O(610) <=> C6H7(56) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.256e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd;O_rad/OneDeC] for rate rule [2_methyl_CPD;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cd;O_rad/OneDeC] for rate rule [2_methyl_CPD;O_rad/OneDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5940,
    label = "CPD(595) + C6H5O(610) <=> CPDyl(596) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.504e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCd;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCd;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5941,
    label = "C5H5(50) + C6H6O(661) <=> CPD(595) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_rad/NonDeC] for rate rule [O/H/OneDeC;Cd_rad/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_rad/NonDeC] for rate rule [O/H/OneDeC;Cd_rad/NonDeC]
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
    index = 5945,
    label = "HO2_17_(5) + C6H5O(610) <=> O2_2_(13) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000188, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (12.422, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]
""",
)

entry(
    index = 5946,
    label = "C4H9(635) + C6H5O(610) <=> C4H8(78) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5947,
    label = "C4H9(635) + C6H5O(610) <=> C4H8(83) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/OneDe;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/OneDe;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5948,
    label = "C3H7(79) + C6H5O(610) <=> C3H6(38) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.446e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 5949,
    label = "C2H3(29) + C6H5O(610) <=> C2H2(20) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5950,
    label = "C2H5(31) + C6H5O(610) <=> C2H4(30) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5951,
    label = "C3H5(66) + C6H5O(610) <=> C3H4(39) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.47e+09, 'cm^3/(mol*s)'),
        n = 1.397,
        Ea = (-0.831, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5952,
    label = "C3H5(65) + C6H5O(610) <=> C3H4(45) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 5953,
    label = "C3H5(66) + C6H5O(610) <=> C3H4(45) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5954,
    label = "C6H7(55) + C6H5O(610) <=> C6H6(54) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad]
""",
)

entry(
    index = 5955,
    label = "C6H7(53) + C6H5O(610) <=> C6H6(54) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5956,
    label = "C6H7(56) + C6H5O(610) <=> C6H6(54) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5957,
    label = "C6H7(52) + C6H5O(610) <=> C6H6(54) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5958,
    label = "C4H3(96) + C6H5O(610) <=> C6H6O(661) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 5959,
    label = "cyC6H7(58) + C6H5O(610) <=> C6H6(48) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5960,
    label = "C5H5(117) + C6H5O(610) <=> C5H4(130) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 5961,
    label = "C5H5(129) + C6H5O(610) <=> C5H4(130) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 5962,
    label = "C5H5(127) + C6H5O(610) <=> C5H4(130) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5963,
    label = "A3a(76) + C6H5O(610) <=> C8H6(74) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 5964,
    label = "C6H5O(610) + C8H7(131) <=> C8H6(74) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5965,
    label = "C2H5(31) + C6H6O(662) <=> CCadd(1) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002306, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (1.05, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H2/Cs] for rate rule [C/H2/CdCO;C_rad/H2/Cs\\H3]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H2/Cs] for rate rule [C/H2/CdCO;C_rad/H2/Cs\H3]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5966,
    label = "O_11_(7) + C6H6O(662) <=> OH_12_(12) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (83250, 'cm^3/(mol*s)'),
        n = 2.59,
        Ea = (1.495, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec;O_atom_triplet] for rate rule [C/H2/CdCO;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_sec;O_atom_triplet] for rate rule [C/H2/CdCO;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5967,
    label = "CH3(17) + C6H6O(662) <=> Cadd(4) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02003, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (1.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_methyl] for rate rule [C/H2/CdCO;C_methyl]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_methyl] for rate rule [C/H2/CdCO;C_methyl]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5968,
    label = "H_10_(3) + C6H6O(662) <=> H2_13_(2) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.8446, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-0.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;H_rad] for rate rule [C/H2/CdCO;H_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;H_rad] for rate rule [C/H2/CdCO;H_rad]
Multiplied by reaction path degeneracy 2
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
    index = 5970,
    label = "OH_12_(12) + C6H6O(662) <=> H2O_14_(6) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.355e+06, 'cm^3/(mol*s)'),
        n = 1.953,
        Ea = (-0.478, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec;O_pri_rad] for rate rule [C/H2/CdCO;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_sec;O_pri_rad] for rate rule [C/H2/CdCO;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5971,
    label = "CH2(T)(24) + C6H6O(662) <=> CH3(17) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (7.47, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec;CH2_triplet] for rate rule [C/H2/CdCO;CH2_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_sec;CH2_triplet] for rate rule [C/H2/CdCO;CH2_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5972,
    label = "C3H5(41) + C6H5O(610) <=> C3H4(39) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;Cdpri_Csrad] for rate rule [C_rad/H/TwoDe;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;Cdpri_Csrad] for rate rule [C_rad/H/TwoDe;Cdpri_Csrad]
""",
)

entry(
    index = 5973,
    label = "C3H5(41) + C6H6O(662) <=> C3H6(38) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003644, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (6.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H2/Cd] for rate rule [C/H2/CdCO;C_rad/H2/Cd\\H_Cd\\H2]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H2/Cd] for rate rule [C/H2/CdCO;C_rad/H2/Cd\H_Cd\H2]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5974,
    label = "C3H5(66) + C6H6O(662) <=> C3H6(38) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01001, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-4.15, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_rad/NonDeC] for rate rule [C/H2/CdCO;Cd_Cd\\H2_rad/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_rad/NonDeC] for rate rule [C/H2/CdCO;Cd_Cd\H2_rad/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5975,
    label = "C3H5(65) + C6H6O(662) <=> C3H6(38) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02157, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-2.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_pri_rad] for rate rule [C/H2/CdCO;Cd_Cd\\H\\Cs_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_pri_rad] for rate rule [C/H2/CdCO;Cd_Cd\H\Cs_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5976,
    label = "C2H(21) + C6H6O(662) <=> C2H2(20) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (196600, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (0.564, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C_sec;Ct_rad] + [C/H2/TwoDe;Y_rad] for rate rule [C/H2/CdCO;Ct_rad/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C_sec;Ct_rad] + [C/H2/TwoDe;Y_rad] for rate rule [C/H2/CdCO;Ct_rad/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5977,
    label = "C2H3(29) + C6H6O(662) <=> C2H4(30) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02157, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-2.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_pri_rad] for rate rule [C/H2/CdCO;Cd_Cd\\H2_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_pri_rad] for rate rule [C/H2/CdCO;Cd_Cd\H2_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5978,
    label = "C3H3(19) + C6H6O(662) <=> C3H4(39) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004124, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.15, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_Cdd_rad/H] for rate rule [C/H2/CdCO;Cd_Cdd_rad/H]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_Cdd_rad/H] for rate rule [C/H2/CdCO;Cd_Cdd_rad/H]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5979,
    label = "C3H3(19) + C6H6O(662) <=> C3H4(45) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004619, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H2/Ct] for rate rule [C/H2/CdCO;C_rad/H2/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H2/Ct] for rate rule [C/H2/CdCO;C_rad/H2/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5980,
    label = "C6H6O(662) + C6H5(105) <=> C6H6(54) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02157, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-2.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_pri_rad] for rate rule [C/H2/CdCO;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_pri_rad] for rate rule [C/H2/CdCO;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5981,
    label = "C6H5(64) + C6H6O(662) <=> C6H6(48) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009964, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_rad/Cd] for rate rule [C/H2/CdCO;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_rad/Cd] for rate rule [C/H2/CdCO;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5982,
    label = "C4H3(110) + C6H5O(610) <=> C6H6O(662) + C4H2(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5983,
    label = "C6H7(52) + C6H6O(662) <=> C6H8(608) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.726e-05, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (7.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/CdCdCs] for rate rule [C/H2/CdCO;C_rad/CdCdCs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/CdCdCs] for rate rule [C/H2/CdCO;C_rad/CdCdCs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5984,
    label = "C6H7(55) + C6H6O(662) <=> C6H8(608) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002306, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (1.05, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H2/Cs] for rate rule [C/H2/CdCO;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H2/Cs] for rate rule [C/H2/CdCO;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5985,
    label = "C6H7(52) + C6H6O(662) <=> C6H8(597) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0007399, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.95, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H/CdCd] for rate rule [C/H2/CdCO;C_rad/H/CdCd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H/CdCd] for rate rule [C/H2/CdCO;C_rad/H/CdCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5986,
    label = "C6H7(53) + C6H6O(662) <=> C6H8(597) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003644, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (6.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H2/Cd] for rate rule [C/H2/CdCO;C_rad/H2/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H2/Cd] for rate rule [C/H2/CdCO;C_rad/H2/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5987,
    label = "C6H7(52) + C6H6O(662) <=> C6H8(607) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0007399, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.95, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H/CdCd] for rate rule [C/H2/CdCO;C_rad/H/CdCd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H/CdCd] for rate rule [C/H2/CdCO;C_rad/H/CdCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5988,
    label = "C6H7(56) + C6H6O(662) <=> C6H8(607) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003644, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (6.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H2/Cd] for rate rule [C/H2/CdCO;C_rad/H2/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H2/Cd] for rate rule [C/H2/CdCO;C_rad/H2/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5989,
    label = "CPDyl(596) + C6H6O(662) <=> CPD(595) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0007399, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (8.95, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H/CdCd] for rate rule [C/H2/CdCO;C_rad/H/CdCd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H/CdCd] for rate rule [C/H2/CdCO;C_rad/H/CdCd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5990,
    label = "C5H5(50) + C6H6O(662) <=> CPD(595) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01001, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-4.15, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_rad/NonDeC] for rate rule [C/H2/CdCO;Cd_rad/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_rad/NonDeC] for rate rule [C/H2/CdCO;Cd_rad/NonDeC]
Multiplied by reaction path degeneracy 2
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
    index = 5994,
    label = "C6H6O(662) + C6H5O(610) <=> C6H6O(661) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.504e-07, 'cm^3/(mol*s)'),
        n = 5.77,
        Ea = (12.04, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCO;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_H;O_rad/OneDeC] for rate rule [C/H2/CdCO;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5995,
    label = "HO2_17_(5) + C6H5O(610) <=> O2_2_(13) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.08667, 'cm^3/(mol*s)'),
        n = 4.127,
        Ea = (22.68, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/TwoDe] for rate rule [Orad_O_H;C_rad/H/CdCO]',
    ),
    longDesc = 
u"""
Estimated using template [X_H;C_rad/H/TwoDe] for rate rule [Orad_O_H;C_rad/H/CdCO]
""",
)

entry(
    index = 5996,
    label = "C2H3(29) + C6H5O(610) <=> C2H2(20) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 5997,
    label = "C2H5(31) + C6H5O(610) <=> C2H4(30) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C_rad/H/TwoDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using an average for rate rule [C_rad/H/TwoDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5998,
    label = "C3H5(66) + C6H5O(610) <=> C3H4(39) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;Cmethyl_Rrad] for rate rule [C_rad/H/TwoDe;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;Cmethyl_Rrad] for rate rule [C_rad/H/TwoDe;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 5999,
    label = "C3H5(65) + C6H5O(610) <=> C3H4(45) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]
""",
)

entry(
    index = 6000,
    label = "C3H5(66) + C6H5O(610) <=> C3H4(45) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6001,
    label = "cyC6H7(58) + C6H5O(610) <=> C6H6(48) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.88e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.36, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;Cpri_Rrad] for rate rule [C_rad/H/TwoDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;Cpri_Rrad] for rate rule [C_rad/H/TwoDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6002,
    label = "CH3(17) + C6H6O(669) <=> Cadd(4) + C6H5O(612)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002512, 'cm^3/(mol*s)'),
        n = 4.281,
        Ea = (3.766, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H2/OneDeC;C_methyl] + [C/H2/COCs;Cs_rad] for rate rule [C/H2/COCs;C_methyl]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H2/OneDeC;C_methyl] + [C/H2/COCs;Cs_rad] for rate rule [C/H2/COCs;C_methyl]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6003,
    label = "H_10_(3) + C6H6O(669) <=> H2_13_(2) + C6H5O(612)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4544, 'cm^3/(mol*s)'),
        n = 3.923,
        Ea = (1.544, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H2/OneDeC;H_rad] + [C/H2/COCs;Y_rad] for rate rule [C/H2/COCs;H_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using average of templates [C/H2/OneDeC;H_rad] + [C/H2/COCs;Y_rad] for rate rule [C/H2/COCs;H_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6004,
    label = "OH_12_(12) + C6H6O(669) <=> H2O_14_(6) + C6H5O(612)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (236, 'cm^3/(mol*s)'),
        n = 3.15,
        Ea = (-3.048, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'C/H2/COCs;O_pri_rad from training reaction 1005\nExact match found for rate rule [C/H2/COCs;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
C/H2/COCs;O_pri_rad from training reaction 1005
Exact match found for rate rule [C/H2/COCs;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6005,
    label = "C2H(21) + C6H6O(669) <=> C2H2(20) + C6H5O(612)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02843, 'cm^3/(mol*s)'),
        n = 3.923,
        Ea = (1.244, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/COCs;Y_rad] for rate rule [C/H2/COCs;Ct_rad/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/COCs;Y_rad] for rate rule [C/H2/COCs;Ct_rad/Ct]
Multiplied by reaction path degeneracy 2
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
    index = 6013,
    label = "C5H5(137) + C6H5O(610) <=> C5H4(130) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 6020,
    label = "C8H7(135) + C6H5O(610) <=> C8H6(74) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6021,
    label = "C4H7(85) + C6H6O(661) <=> C4H8(83) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_Cd\\H\\Cs_rad/Cs] for rate rule [O/H/OneDeC;Cd_Cd\\H\\Cs_rad/Cs]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_Cd\H\Cs_rad/Cs] for rate rule [O/H/OneDeC;Cd_Cd\H\Cs_rad/Cs]
""",
)

entry(
    index = 6022,
    label = "C4H7(85) + C6H6O(662) <=> C4H8(83) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01001, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-4.15, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_rad/NonDeC] for rate rule [C/H2/CdCO;Cd_Cd\\H\\Cs_rad/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_rad/NonDeC] for rate rule [C/H2/CdCO;Cd_Cd\H\Cs_rad/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6030,
    label = "C4H7(85) + C6H5O(610) <=> C4H6(91) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.47e+09, 'cm^3/(mol*s)'),
        n = 1.397,
        Ea = (-0.831, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_Cdrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_Cdrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6037,
    label = "C8H7(136) + C6H5O(610) <=> C8H6(74) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6044,
    label = "C6H5O(610) + C8H7(147) <=> C8H6(74) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad/H/Cd] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad/H/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad/H/Cd] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad/H/Cd]
""",
)

entry(
    index = 6045,
    label = "CH3CO(18) + C6H5O(610) <=> CH2CO(16) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.47e+09, 'cm^3/(mol*s)'),
        n = 1.397,
        Ea = (-0.831, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6052,
    label = "C8H7(134) + C6H5O(610) <=> C8H6(74) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [O_rad/OneDe;C/H2/Cd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/Cd_Csrad] for rate rule [O_rad/OneDe;C/H2/Cd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6057,
    label = "R1(63) + C6H6O(661) <=> C8H6(74) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.839e+06, 'cm^3/(mol*s)'),
        n = 1.828,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cb_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cb_rad]
""",
)

entry(
    index = 6058,
    label = "R1(63) + C6H6O(662) <=> C8H6(74) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02746, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-5.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cb_rad] for rate rule [C/H2/CdCO;Cb_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cb_rad] for rate rule [C/H2/CdCO;Cb_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6060,
    label = "CHO2(42) + C6H5O(610) <=> CO2_5_(8) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.351e+08, 'cm^3/(mol*s)'),
        n = 1.569,
        Ea = (-0.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]
""",
)

entry(
    index = 6061,
    label = "CHO2(42) + C6H5O(610) <=> CO2_5_(8) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/TwoDe;O_COrad]
""",
)

entry(
    index = 6062,
    label = "CHO2(42) + C6H5O(612) <=> CO2_5_(8) + C6H6O(669)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;O_COrad]
""",
)

entry(
    index = 6065,
    label = "C6H6O(661) + C8H5(145) <=> C8H6(74) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.839e+06, 'cm^3/(mol*s)'),
        n = 1.828,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cb_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cb_rad]
""",
)

entry(
    index = 6066,
    label = "C6H6O(662) + C8H5(145) <=> C8H6(74) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02746, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-5.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cb_rad] for rate rule [C/H2/CdCO;Cb_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cb_rad] for rate rule [C/H2/CdCO;Cb_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6069,
    label = "C6H6O(661) + C8H5(144) <=> C8H6(74) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.839e+06, 'cm^3/(mol*s)'),
        n = 1.828,
        Ea = (4.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cb_rad]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDeC;Y_rad] for rate rule [O/H/OneDeC;Cb_rad]
""",
)

entry(
    index = 6070,
    label = "C6H6O(662) + C8H5(144) <=> C8H6(74) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.02746, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (-5.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cb_rad] for rate rule [C/H2/CdCO;Cb_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cb_rad] for rate rule [C/H2/CdCO;Cb_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6073,
    label = "HCO(22) + C4H9(635) <=> C4H8(78) + CH2O(25)",
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
    index = 6074,
    label = "HCO(22) + C4H9(635) <=> CH2O(25) + C4H8(83)",
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
    index = 6075,
    label = "CH2OH(32) + C6H5O(610) <=> CH2O(25) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.708e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]
""",
)

entry(
    index = 6076,
    label = "CHO2(424) + C6H5O(610) <=> CO2_5_(8) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.578e+07, 'cm^3/(mol*s)'),
        n = 1.793,
        Ea = (-1.067, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 6077,
    label = "CHO2(424) + C6H5O(610) <=> CO2_5_(8) + C6H6O(662)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.114e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.18, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/TwoDe;XH_s_Rrad] for rate rule [C_rad/H/TwoDe;COpri_Orad]
""",
)

entry(
    index = 6078,
    label = "CHO2(424) + C6H5O(612) <=> CO2_5_(8) + C6H6O(669)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Orad]
""",
)

entry(
    index = 6082,
    label = "C6H5O(610) + C8H7(200) <=> C6H6O(661) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6085,
    label = "C6H5O(610) + C8H7(199) <=> C6H6O(661) + C8H6(190)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad]
""",
)

entry(
    index = 6091,
    label = "C6H6O(661) + C5H5(179) <=> CPD(595) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]
""",
)

entry(
    index = 6092,
    label = "C6H6O(662) + C5H5(179) <=> CPD(595) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009964, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4.85, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;Cd_rad/Cd] for rate rule [C/H2/CdCO;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;Cd_rad/Cd] for rate rule [C/H2/CdCO;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6099,
    label = "C6H5(64) + C6H5O(610) <=> C6H6O(661) + C6H4(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (4.922, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nEa raised from -6.7 to 20.6 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Ea raised from -6.7 to 20.6 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 6100,
    label = "C6H5(64) + C6H5O(610) <=> C6H6O(662) + C6H4(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (26.635, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]\nEa raised from -4.6 to 111.4 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H/TwoDe;Cd_Cdrad]
Ea raised from -4.6 to 111.4 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 6101,
    label = "C6H5O(610) + C10H7(209) <=> C6H6O(661) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
""",
)

entry(
    index = 6102,
    label = "C6H5O(610) + C10H7(232) <=> C6H6O(661) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/OneDe;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6109,
    label = "C6H5O(610) + C10H7(246) <=> C6H6O(661) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [O_rad;Cmethyl_Csrad] for rate rule [O_rad/OneDe;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6113,
    label = "C6H5O(610) + C10H7(245) <=> C6H6O(661) + C10H6(235)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2.011, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H/DeDe_Csrad] for rate rule [O_rad/OneDe;C/H/DeDe_Csrad]
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
    index = 6121,
    label = "O2_2_(13) + C2H5(31) <=> CH3OO(657) + CH2(S)(28)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.492, -0.002666, -0.001852, -0.001025],
            [11.14, -0.001071, -0.0007418, -0.0004083],
            [-0.1471, -0.0007178, -0.000497, -0.0002735],
            [-0.06993, -0.0002735, -0.0001891, -0.0001039],
            [-0.0283, 9.999e-05, 6.972e-05, 3.882e-05],
            [-0.009548, 0.0001693, 0.0001175, 6.49e-05],
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
    index = 6123,
    label = "HO2_17_(5) + CH3(17) <=> H_10_(3) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.964, -0.06368, -0.04174, -0.02086],
            [3.169, 0.07803, 0.05033, 0.02439],
            [0.1547, -0.01675, -0.009938, -0.003986],
            [0.02237, -0.003481, -0.002695, -0.00173],
            [-0.00201, 0.001088, 0.0006703, 0.0002908],
            [-0.003972, 0.0002015, 0.0001728, 0.000125],
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
    index = 6124,
    label = "CH3OO(657) + C3H3(19) <=> S(566) + CH3(17)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.215, -0.03661, -0.02443, -0.01262],
            [3.237, 0.02017, 0.01323, 0.00662],
            [0.2291, -0.01073, -0.006973, -0.00343],
            [0.02936, -0.002575, -0.001739, -0.0009172],
            [0.006465, 0.00191, 0.00124, 0.0006089],
            [0.001774, 0.001169, 0.0007781, 0.0004004],
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
    index = 6125,
    label = "HO2_17_(5) + CO2_5_(8) <=> O_11_(7) + CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.3468, -0.01801, -0.01241, -0.006776],
            [9.53, -0.004459, -0.003031, -0.001617],
            [0.07184, 0.001713, 0.001172, 0.0006322],
            [0.01474, 0.004668, 0.003181, 0.001704],
            [0.003821, 0.00238, 0.001615, 0.0008599],
            [0.0008707, -0.0002338, -0.0001593, -8.526e-05],
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
    index = 6128,
    label = "CH3OO(657) + C3H3(19) <=> S(567) + CH3(17)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.117, -0.0009938, -0.0006911, -0.000383],
            [3.993, -0.001097, -0.0007624, -0.0004222],
            [0.3755, -0.0004635, -0.000322, -0.0001782],
            [0.05712, 3.703e-05, 2.585e-05, 1.442e-05],
            [0.01215, 0.0001783, 0.0001239, 6.864e-05],
            [0.00418, 0.0001262, 8.763e-05, 4.845e-05],
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
    index = 6129,
    label = "OH_12_(12) + CHO3(659) <=> HO2_17_(5) + CHO2(42)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.993, -0.2061, -0.1175, -0.04358],
            [5.684, 0.231, 0.1235, 0.03788],
            [-0.05681, -0.02666, -0.006257, 0.006032],
            [-0.01459, -0.01371, -0.009828, -0.005231],
            [-0.003041, -0.003696, -0.002997, -0.0021],
            [0.0001678, 0.0002889, 4.506e-05, -0.0001192],
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
    index = 6130,
    label = "CO2_5_(8) + CHO2(42) <=> CO_21_(14) + CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.464, -0.02974, -0.02028, -0.01088],
            [3.882, 0.0009758, 0.0007154, 0.0004249],
            [-0.002191, -0.002707, -0.001799, -0.0009263],
            [-0.002751, -2.535e-05, -4.57e-06, 6.29e-06],
            [-0.001858, 0.0002815, 0.000198, 0.0001099],
            [-0.001022, 0.0002206, 0.000153, 8.344e-05],
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
    index = 6131,
    label = "CO2_5_(8) + CHO2(424) <=> CO_21_(14) + CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.854, -0.2501, -0.1444, -0.05657],
            [10.6, 0.1222, 0.06728, 0.02296],
            [0.2089, -0.008331, -0.000574, 0.00487],
            [0.04383, -0.001942, -0.001072, -0.0002772],
            [0.008392, 0.0005964, 0.000449, -5.013e-06],
            [0.0002999, 0.0006531, 0.0004744, 0.0002148],
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
    index = 6150,
    label = "H2O_14_(6) + C3H3(86) <=> OH_12_(12) + C3H4(45)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.56e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.45, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri;Ct_rad] for rate rule [O_pri;Ct_rad/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_pri;Ct_rad] for rate rule [O_pri;Ct_rad/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6176,
    label = "O_11_(7) + C10H7(564) <=> OH_12_(12) + C10H6(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6191,
    label = "H2O2(15) + C6H5(64) <=> HO2_17_(5) + C6H6(48)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_sec_rad] for rate rule [H2O2;Cd_rad/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H2O2;Cd_sec_rad] for rate rule [H2O2;Cd_rad/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6192,
    label = "O2_2_(13) + C4H5(509) <=> HO2_17_(5) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+15, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6193,
    label = "H2O2(15) + C4H3(110) <=> HO2_17_(5) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.875, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;Cd_sec_rad] for rate rule [H2O2;Cd_rad/Ct]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [H2O2;Cd_sec_rad] for rate rule [H2O2;Cd_rad/Ct]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6194,
    label = "H2O2(15) + C4H3(96) <=> HO2_17_(5) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2O2;Cd_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Exact match found for rate rule [H2O2;Cd_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6195,
    label = "O2_2_(13) + C4H5(532) <=> HO2_17_(5) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;C/H2/De_Csrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Exact match found for rate rule [O2b;C/H2/De_Csrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 6197,
    label = "C4H9(635) + H2O2(15) <=> HO2_17_(5) + C4H10(685)",
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
    index = 6199,
    label = "O2_2_(13) + C4H10(685) <=> HO2_17_(5) + C4H9(635)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.588e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49.66, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O2b]\nMultiplied by reaction path degeneracy 8\nEa raised from 207.7 to 207.8 kJ/mol to match endothermicity of reaction.',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O2b]
Multiplied by reaction path degeneracy 8
Ea raised from 207.7 to 207.8 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 6200,
    label = "C4H10(685) + O_11_(7) <=> OH_12_(12) + C4H9(635)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (95600, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (2.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Exact match found for rate rule [C/H2/NonDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6201,
    label = "C4H10(685) + OH_12_(12) <=> H2O_14_(6) + C4H9(635)",
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
    index = 6224,
    label = "C4H9(635) + C6H6O(661) <=> C4H10(685) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (93.97, 'cm^3/(mol*s)'),
        n = 2.872,
        Ea = (4.221, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeC;Cs_rad] for rate rule [O/H/OneDeC;C_rad/H/NonDeC]',
    ),
    longDesc = 
u"""
Estimated using average of templates [O_sec;C_rad/H/NonDeC] + [O/H/OneDeC;Cs_rad] for rate rule [O/H/OneDeC;C_rad/H/NonDeC]
""",
)

entry(
    index = 6225,
    label = "C4H9(635) + C6H6O(662) <=> C4H10(685) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0009727, 'cm^3/(mol*s)'),
        n = 4.273,
        Ea = (4.633, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/TwoDe;C_rad/H/NonDeC] for rate rule [C/H2/CdCO;C_rad/H/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [C/H2/TwoDe;C_rad/H/NonDeC] for rate rule [C/H2/CdCO;C_rad/H/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6231,
    label = "C7H7(580) + C6H6O(661) <=> C7H8(61) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0065, 'cm^3/(mol*s)'),
        n = 4.245,
        Ea = (7.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeC;C_rad/H2/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O/H/OneDe;C_pri_rad] for rate rule [O/H/OneDeC;C_rad/H2/Cd]
""",
)

entry(
    index = 6232,
    label = "C7H7(581) + C6H6O(661) <=> C7H8(61) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]
""",
)

entry(
    index = 6236,
    label = "C6H6O(661) + C7H7(589) <=> C7H8(61) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]
""",
)

entry(
    index = 6240,
    label = "C6H6O(661) + C7H7(588) <=> C7H8(61) + C6H5O(610)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.4375, 'cm^3/(mol*s)'),
        n = 3.59,
        Ea = (-4.03, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]',
    ),
    longDesc = 
u"""
Estimated using template [O_sec;Cd_sec_rad] for rate rule [O/H/OneDeC;Cd_rad/Cd]
""",
)

entry(
    index = 6267,
    label = "C6H5O(610) + C7H9(592) <=> C7H8(61) + C6H6O(661)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [O_rad/OneDe;C/H2/De_Csrad/H/Cd]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6268,
    label = "CHO2(42) + C4H9(635) <=> CO2_5_(8) + C4H10(685)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;O_Rrad] for rate rule [C_rad/H/NonDeC;O_COrad]
""",
)

entry(
    index = 6269,
    label = "C4H9(635) + CH2OH(32) <=> C4H10(685) + CH2O(25)",
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
    index = 6270,
    label = "CHO2(424) + C4H9(635) <=> CO2_5_(8) + C4H10(685)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.972e+13, 'cm^3/(mol*s)'),
        n = -0.28,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/NonDeC;XH_s_Rrad] for rate rule [C_rad/H/NonDeC;COpri_Orad]
""",
)

entry(
    index = 6274,
    label = "HO2_17_(5) + C4H9(37) <=> O2_2_(13) + C4H10(685)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.5763, 'cm^3/(mol*s)'),
        n = 3.502,
        Ea = (5.889, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;C_rad/H2/Cs] for rate rule [Orad_O_H;C_rad/H2/Cs]
""",
)

entry(
    index = 6277,
    label = "C4H10(685) + O_11_(7) <=> OH_12_(12) + C4H9(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.031, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (3.312, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [C/H3/Cs;O_atom_triplet] + [C/H3/Cs\\H2\\Cs;Y_rad_birad_trirad_quadrad] for rate rule\n[C/H3/Cs\\H2\\Cs;O_atom_triplet]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [C/H3/Cs;O_atom_triplet] + [C/H3/Cs\H2\Cs;Y_rad_birad_trirad_quadrad] for rate rule
[C/H3/Cs\H2\Cs;O_atom_triplet]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 6278,
    label = "H2O_14_(6) + C4H9(37) <=> C4H10(685) + OH_12_(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+06, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (20.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6279,
    label = "C4H9(37) + H2O2(15) <=> HO2_17_(5) + C4H10(685)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H2O2;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6285,
    label = "C4H9(37) + CH2OH(32) <=> C4H10(685) + CH2O(25)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/Cs;O_Csrad]
""",
)

entry(
    index = 6287,
    label = "CHO2(42) + C4H9(37) <=> CO2_5_(8) + C4H10(685)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;O_Rrad] for rate rule [C_rad/H2/Cs;O_COrad]
""",
)

entry(
    index = 6289,
    label = "CHO2(424) + C4H9(37) <=> CO2_5_(8) + C4H10(685)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Orad]
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
    index = 6293,
    label = "O2_2_(13) + C2H3(29) <=> O_11_(7) + C2H3O(430)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.849e+09, 'cm^3/(mol*s)'),
        n = 0.923,
        Ea = (0.226, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 6295,
    label = "O_11_(7) + C2H4(30) <=> H_10_(3) + C2H3O(430)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+09, 'cm^3/(mol*s)'),
        n = 0.907,
        Ea = (0.839, 'kcal/mol'),
        T0 = (1, 'K'),
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
    index = 6297,
    label = "O_11_(7) + C2H3O(430) <=> H_10_(3) + CO2_5_(8) + CH2(T)(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
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
    index = 6299,
    label = "H_10_(3) + C2H3O(430) <=> H2_13_(2) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6300,
    label = "OH_12_(12) + C2H3O(430) <=> H2O_14_(6) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6301,
    label = "H_10_(3) + C2H3O(430) <=> H_10_(3) + CH3CO(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
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
    index = 6303,
    label = "CH3CO(18) + C4H5(465) <=> CH2CO(16) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.87e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;Cmethyl_Rrad] for rate rule [C_rad/H2/Cd;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6304,
    label = "C2H3O(430) + C4H5(465) <=> CH2CO(16) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.088e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.122, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cd;XH_s_Rrad] for rate rule [C_rad/H2/Cd;COpri_Csrad]
""",
)

entry(
    index = 6305,
    label = "CH3CO(18) + C4H5(443) <=> CH2CO(16) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.289e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6306,
    label = "C2H3O(430) + C4H5(443) <=> CH2CO(16) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H/OneDeC;XH_s_Rrad] for rate rule [C_rad/H/OneDeC;COpri_Csrad]
""",
)

entry(
    index = 6307,
    label = "CH3CO(18) + C4H5(443) <=> CH2CO(16) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6308,
    label = "C2H3O(430) + C4H5(443) <=> CH2CO(16) + C4H6(91)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]
""",
)

entry(
    index = 6309,
    label = "O_11_(7) + C4H5(443) <=> OH_12_(12) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.68e+11, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (-0.445, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using average of templates [Y_1centerbirad;Cmethyl_Csrad] + [O_atom_triplet;Cmethyl_Rrad] for rate rule [O_atom_triplet;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6310,
    label = "O_11_(7) + C4H5(465) <=> OH_12_(12) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6311,
    label = "CH3CO(18) + C4H5(532) <=> CH2CO(16) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_COrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_COrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6312,
    label = "C2H3O(430) + C4H5(532) <=> CH2CO(16) + C#CCC(90)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]
""",
)

entry(
    index = 6313,
    label = "O_11_(7) + C4H5(532) <=> OH_12_(12) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.498e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad_birad_trirad_quadrad;C/H2/De_Csrad] for rate rule [O_atom_triplet;C/H2/De_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6314,
    label = "C4H3(110) + C2H3O(430) <=> CH2CO(16) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;XH_s_Rrad] for rate rule [Cd_rad/OneDe;COpri_Csrad]
""",
)

entry(
    index = 6315,
    label = "OH_12_(12) + C#CCC(90) <=> H2O_14_(6) + C4H5(532)",
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
    index = 6316,
    label = "C2H3O(430) + C4H3(96) <=> CH2CO(16) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;XH_s_Rrad] for rate rule [Cd_pri_rad;COpri_Csrad]
""",
)

entry(
    index = 6317,
    label = "H_10_(3) + C2H3O(430) <=> CH3(17) + HCO(22)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6318,
    label = "OH_12_(12) + C2H3O(430) <=> HCO(22) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6319,
    label = "O2_2_(13) + C2H3O(430) <=> CO_21_(14) + OH_12_(12) + CH2O(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: FFCM1(-)
""",
)

entry(
    index = 6320,
    label = "C4H3(110) + CH3O(508) <=> CH2O(25) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_rad;Cmethyl_Rrad] for rate rule [Cd_rad/OneDe;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6321,
    label = "C4H3(96) + CH3O(508) <=> CH2O(25) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Estimated using template [Cd_pri_rad;Cmethyl_Rrad] for rate rule [Cd_pri_rad;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6322,
    label = "HCO(22) + C4H5(532) <=> CH2O(25) + C4H4(444)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Estimated using template [Y_rad;C/H2/De_Csrad] for rate rule [CO_pri_rad;C/H2/De_Csrad]
Multiplied by reaction path degeneracy 2
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
    index = 6329,
    label = "CH3O(508) + C4H9(37) <=> CH2O(25) + C4H10(685)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;Cmethyl_Rrad] for rate rule [C_rad/H2/Cs;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6330,
    label = "O2_2_(13) + S(658) <=> O_11_(7) + S(693)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.72, -0.398, -0.1669, -0.02853],
            [0.002004, 0.434, 0.1548, 0.006048],
            [-0.1315, -0.0551, 0.003743, 0.01764],
            [-0.007968, -0.006189, -0.007354, -0.002065],
            [0.01009, 0.01037, 0.003914, -0.0001521],
            [-0.001156, -0.0004237, 0.001267, 0.001234],
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
    index = 6336,
    label = "O2_2_(13) + C3H7(35) <=> CH2(S)(28) + S(692)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.155, -0.01109, -0.007632, -0.004155],
            [10.79, -0.009653, -0.006594, -0.003548],
            [-0.06776, -0.001435, -0.0009681, -0.0005096],
            [-0.04663, 0.003455, 0.002362, 0.001272],
            [-0.02668, 0.003699, 0.002511, 0.001336],
            [-0.01318, 0.001935, 0.001302, 0.0006818],
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
    index = 6340,
    label = "CH4O2(696) + CH3(17) <=> Cadd(4) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004442, 'cm^3/(mol*s)'),
        n = 4.228,
        Ea = (1.851, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_methyl] + [O/H/NonDeO;Cs_rad] for rate rule [O/H/NonDeO;C_methyl]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;C_methyl] + [O/H/NonDeO;Cs_rad] for rate rule [O/H/NonDeO;C_methyl]
""",
)

entry(
    index = 6341,
    label = "CH4O2(696) + C3H3(19) <=> C3H4(39) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.6614, 'cm^3/(mol*s)'),
        n = 3.555,
        Ea = (-5.755, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;Cd_rad] for rate rule [O/H/NonDeO;Cd_Cdd_rad/H]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeO;Cd_rad] for rate rule [O/H/NonDeO;Cd_Cdd_rad/H]
""",
)

entry(
    index = 6342,
    label = "C3H7(35) + CH4O2(696) <=> C3H8(34) + CH3OO(657)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]
""",
)

entry(
    index = 6343,
    label = "C2H5(31) + CH4O2(696) <=> CCadd(1) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002046, 'cm^3/(mol*s)'),
        n = 4.189,
        Ea = (-1.293, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;C_rad/H2/Cs] for rate rule [O/H/NonDeO;C_rad/H2/Cs\\H3]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeO;C_rad/H2/Cs] for rate rule [O/H/NonDeO;C_rad/H2/Cs\H3]
""",
)

entry(
    index = 6344,
    label = "C4H9(37) + CH4O2(696) <=> C4H10(685) + CH3OO(657)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cs]
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
    index = 6346,
    label = "O_11_(7) + CH4O2(696) <=> OH_12_(12) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;O_atom_triplet] for rate rule [O/H/NonDeO;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec;O_atom_triplet] for rate rule [O/H/NonDeO;O_atom_triplet]
""",
)

entry(
    index = 6347,
    label = "H_10_(3) + CH4O2(696) <=> H2_13_(2) + CH3OO(657)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;H_rad] + [O/H/NonDeO;Y_rad] for rate rule [O/H/NonDeO;H_rad]
""",
)

entry(
    index = 6348,
    label = "OH_12_(12) + CH4O2(696) <=> H2O_14_(6) + CH3OO(657)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]
""",
)

entry(
    index = 6349,
    label = "HO2_17_(5) + CH3OO(657) <=> O2_2_(13) + CH4O2(696)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [X_H;OOC] + [Orad_O_H;O_rad/NonDeO] for rate rule [Orad_O_H;OOC]
""",
)

entry(
    index = 6350,
    label = "H2O2(15) + CH3OO(657) <=> HO2_17_(5) + CH4O2(696)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Matched reaction 536 H2O2 + CH3O2 <=> HO2 + CH4O2 in H_Abstraction/training
""",
)

entry(
    index = 6351,
    label = "CH2(T)(24) + CH4O2(696) <=> CH3(17) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (6.94, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;CH2_triplet] for rate rule [O/H/NonDeO;CH2_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec;CH2_triplet] for rate rule [O/H/NonDeO;CH2_triplet]
""",
)

entry(
    index = 6352,
    label = "C2H3(29) + CH4O2(696) <=> C2H4(30) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (-7.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;Cd_pri_rad] for rate rule [O/H/NonDeO;Cd_Cd\\H2_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeO;Cd_pri_rad] for rate rule [O/H/NonDeO;Cd_Cd\H2_pri_rad]
""",
)

entry(
    index = 6353,
    label = "HCO(22) + CH4O2(696) <=> CH2O(25) + CH3OO(657)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeO;CO_rad] for rate rule [O/H/NonDeO;CO_pri_rad]
""",
)

entry(
    index = 6354,
    label = "C2H5(31) + CH3OO(657) <=> C2H4(30) + CH4O2(696)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6355,
    label = "C3H7(35) + CH3OO(657) <=> C3H6(38) + CH4O2(696)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6356,
    label = "CH3O(508) + CH3OO(657) <=> CH2O(25) + CH4O2(696)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6357,
    label = "CH2OH(32) + CH3OO(657) <=> CH2O(25) + CH4O2(696)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
""",
)

entry(
    index = 6358,
    label = "C2H3(29) + CH3OO(657) <=> C2H2(20) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 6362,
    label = "HO2_17_(5) + C3H6(38) <=> CH2(S)(28) + S(692)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.979, -0.000781, -0.0005432, -0.0003012],
            [14.17, -0.0006323, -0.0004395, -0.0002434],
            [0.1493, -0.0003871, -0.000269, -0.000149],
            [0.02856, -6.052e-05, -4.2e-05, -2.321e-05],
            [0.003929, 0.000104, 7.23e-05, 4.008e-05],
            [-0.0007547, 0.000121, 8.403e-05, 4.652e-05],
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
    index = 6368,
    label = "O2_2_(13) + C2H3O(430) <=> CO_21_(14) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.5658, -0.006967, -0.004832, -0.002667],
            [9.177, 0.002982, 0.002061, 0.001131],
            [0.0706, -0.001868, -0.00129, -0.0007069],
            [0.005645, 0.0006953, 0.0004797, 0.0002624],
            [-0.004846, 0.0007048, 0.0004889, 0.0002699],
            [-0.004206, 0.0004841, 0.0003351, 0.0001844],
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
    index = 6371,
    label = "O2_2_(13) + C3H3(19) <=> O_11_(7) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.96, -0.004488, -0.003105, -0.001707],
            [5.516, 0.0005709, 0.0003843, 0.0002017],
            [0.03283, -0.00156, -0.001075, -0.0005872],
            [0.0164, -1.934e-05, -1.522e-05, -9.98e-06],
            [0.001976, 0.0003852, 0.0002668, 0.0001469],
            [-0.002028, 0.000284, 0.0001965, 0.000108],
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
    index = 6373,
    label = "CH3OO(657) + C3H3(19) <=> CH3O(508) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.85, -0.1282, -0.07467, -0.02957],
            [0.0427, 0.1166, 0.06364, 0.02125],
            [-0.03841, -0.02526, -0.0126, -0.0031],
            [-0.01973, -0.00656, -0.004119, -0.001883],
            [-0.006299, 0.006122, 0.003209, 0.0009526],
            [-0.004333, 0.002634, 0.00169, 0.0007989],
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
    index = 6375,
    label = "C2H3O(430) + C4H9(37) <=> C4H10(685) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.307e+12, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;XH_s_Rrad] for rate rule [C_rad/H2/Cs;COpri_Csrad]
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
    index = 6378,
    label = "HO2_17_(5) + C3H3O(700) <=> C3H2O(701) + H2O2(15)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6379,
    label = "O2_2_(13) + C3H3O(700) <=> HO2_17_(5) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H2/De_Rrad] for rate rule [O2b;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;C/H2/De_Rrad] for rate rule [O2b;C/H2/De_Orad]
Multiplied by reaction path degeneracy 8
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
    index = 6383,
    label = "H_10_(3) + C3H3O(700) <=> H2_13_(2) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.2e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H2/De_Rrad] for rate rule [H_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;C/H2/De_Rrad] for rate rule [H_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6384,
    label = "OH_12_(12) + C3H3O(700) <=> H2O_14_(6) + C3H2O(701)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;Cpri_Rrad] for rate rule [O_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6385,
    label = "C3H3O(700) + CH3(17) <=> Cadd(4) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;Cpri_Rrad] for rate rule [C_methyl;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_methyl;Cpri_Rrad] for rate rule [C_methyl;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6386,
    label = "C3H3O(700) + C3H3(19) <=> C3H4(39) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cpri_Rrad] for rate rule [Cd_pri_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;Cpri_Rrad] for rate rule [Cd_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6387,
    label = "C3H7(35) + C3H3O(700) <=> C3H8(34) + C3H2O(701)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6388,
    label = "C2H5(31) + C3H3O(700) <=> CCadd(1) + C3H2O(701)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6389,
    label = "C4H9(37) + C3H3O(700) <=> C4H10(685) + C3H2O(701)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cs;Cpri_Rrad] for rate rule [C_rad/H2/Cs;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
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
    index = 6392,
    label = "HO2_17_(5) + CH3(17) <=> H_10_(3) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.546, -0.04194, -0.02813, -0.01465],
            [5.291, 0.05083, 0.03374, 0.01725],
            [0.2398, -0.01107, -0.006986, -0.003233],
            [0.04853, -0.002085, -0.001572, -0.0009796],
            [-0.0001588, 0.00069, 0.0004483, 0.0002192],
            [-0.001168, 7.273e-05, 6.434e-05, 4.813e-05],
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
    index = 6393,
    label = "O_11_(7) + CH4O2(696) <=> OH_12_(12) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.502e+07, 'cm^3/(mol*s)'),
        n = 2.017,
        Ea = (3.981, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri;O_atom_triplet] for rate rule [C/H3/O;O_atom_triplet]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri;O_atom_triplet] for rate rule [C/H3/O;O_atom_triplet]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6394,
    label = "CH3O2(703) + H2O2(15) <=> HO2_17_(5) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.3245, 'cm^3/(mol*s)'),
        n = 3.75,
        Ea = (5.455, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;C_pri_rad] for rate rule [H2O2;C_rad/H2/O]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;C_pri_rad] for rate rule [H2O2;C_rad/H2/O]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6395,
    label = "HO2_17_(5) + CH3O2(703) <=> O2_2_(13) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30.2, 'cm^3/(mol*s)'),
        n = 2.95,
        Ea = (11.98, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H2/O] for rate rule [Orad_O_H;C_rad/H2/O]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;C_rad/H2/O] for rate rule [Orad_O_H;C_rad/H2/O]
""",
)

entry(
    index = 6396,
    label = "CH4O2(696) + CH3(17) <=> Cadd(4) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000615, 'cm^3/(mol*s)'),
        n = 4.9,
        Ea = (6.72, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/O;C_methyl]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C/H3/O;C_methyl]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6397,
    label = "CH4O2(696) + CH3O2(703) <=> CH4O2(696) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.279e-06, 'cm^3/(mol*s)'),
        n = 5.255,
        Ea = (0.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;C_pri_rad] for rate rule [O/H/NonDeO;C_rad/H2/O]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeO;C_pri_rad] for rate rule [O/H/NonDeO;C_rad/H2/O]
""",
)

entry(
    index = 6398,
    label = "C2H5(31) + CH3O2(703) <=> C2H4(30) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.67e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/O;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/O;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6399,
    label = "C3H7(35) + CH3O2(703) <=> C3H6(38) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/O;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/O;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6400,
    label = "C3H4(39) + CH3O2(703) <=> CH4O2(696) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.06082, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.183, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;C_pri_rad] for rate rule [Cd_Cdd/H2;C_rad/H2/O]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_Cdd/H2;C_pri_rad] for rate rule [Cd_Cdd/H2;C_rad/H2/O]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6401,
    label = "CH3O(508) + CH3O2(703) <=> CH2O(25) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.67e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;Cmethyl_Rrad] for rate rule [C_rad/H2/O;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;Cmethyl_Rrad] for rate rule [C_rad/H2/O;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6402,
    label = "CH2OH(32) + CH3O2(703) <=> CH2O(25) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/O;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/O;O_Csrad]
""",
)

entry(
    index = 6403,
    label = "C2H3(29) + CH3O2(703) <=> C2H2(20) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/O;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/O;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 6405,
    label = "C2H5(31) + CH4O2(696) <=> CCadd(1) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0003983, 'cm^3/(mol*s)'),
        n = 4.542,
        Ea = (6.707, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri;C_rad/H2/Cs] for rate rule [C/H3/O;C_rad/H2/Cs\\H3]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri;C_rad/H2/Cs] for rate rule [C/H3/O;C_rad/H2/Cs\H3]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6406,
    label = "OH_12_(12) + CH4O2(696) <=> H2O_14_(6) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24420, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (-0.42, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/O;O_pri_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C/H3/O;O_pri_rad]
Multiplied by reaction path degeneracy 3
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
    index = 6408,
    label = "C2H3(29) + C3H3O(700) <=> C2H4(30) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cpri_Rrad] for rate rule [Cd_pri_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;Cpri_Rrad] for rate rule [Cd_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6409,
    label = "HCO(22) + C3H3O(700) <=> CH2O(25) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3.405, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H2/De_Rrad] for rate rule [CO_pri_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;C/H2/De_Rrad] for rate rule [CO_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
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
    index = 6412,
    label = "HCCO(26) + C3H3O(700) <=> C3H2O(701) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_pri_rad;Cpri_Rrad] for rate rule [Cd_pri_rad;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_pri_rad;Cpri_Rrad] for rate rule [Cd_pri_rad;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
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
    index = 6414,
    label = "H_10_(3) + CH4O2(696) <=> H2_13_(2) + CH3O2(703)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1353, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (3.49, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C/H3/O;H_rad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C/H3/O;H_rad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6415,
    label = "O2_2_(13) + HCCO(26) <=> O_11_(7) + C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.03, -0.03014, -0.01957, -0.009628],
            [0.4443, 0.03764, 0.02399, 0.01139],
            [0.03028, -0.01292, -0.007917, -0.003462],
            [0.01139, 0.0009172, 0.0003527, -4.552e-05],
            [0.00316, 0.0007228, 0.000508, 0.0002824],
            [0.0007192, -5.135e-05, -1.706e-05, 7.444e-06],
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
    index = 6416,
    label = "CH3O2(703) + C3H5(41) <=> C3H4(39) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.851e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cdpri_Csrad] for rate rule [C_rad/H2/O;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;Cdpri_Csrad] for rate rule [C_rad/H2/O;Cdpri_Csrad]
""",
)

entry(
    index = 6417,
    label = "C3H5(41) + CH3OO(657) <=> C3H4(39) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.008e+09, 'cm^3/(mol*s)'),
        n = 1.009,
        Ea = (2.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cdpri_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cdpri_Csrad] + [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;Cdpri_Csrad]
""",
)

entry(
    index = 6418,
    label = "C3H3O(700) + C3H5(41) <=> C3H6(38) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/Cd;Cpri_Rrad] for rate rule [C_rad/H2/Cd;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/Cd;Cpri_Rrad] for rate rule [C_rad/H2/Cd;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6419,
    label = "C3H6(38) + CH3O2(703) <=> CH4O2(696) + C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001008, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd\\H_Cd\\H2;C_pri_rad] for rate rule [C/H3/Cd\\H_Cd\\H2;C_rad/H2/O]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C/H3/Cd\H_Cd\H2;C_pri_rad] for rate rule [C/H3/Cd\H_Cd\H2;C_rad/H2/O]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6420,
    label = "CH4O2(696) + C3H5(41) <=> C3H6(38) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.01755, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (9.86, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cd\\H_Cd\\H2]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [O/H/NonDeO;C_rad/H2/Cd\H_Cd\H2]
""",
)

entry(
    index = 6421,
    label = "OH_12_(12) + C3H3(19) <=> H_10_(3) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.466, -0.3663, -0.1629, -0.03083],
            [3.494, 0.4387, 0.1762, 0.01762],
            [-0.0109, -0.04487, 0.004334, 0.01912],
            [-0.01651, -0.03912, -0.02173, -0.005262],
            [-0.004638, -0.003009, -0.005132, -0.004588],
            [-0.001637, 0.004948, 0.002185, -5.28e-05],
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
    index = 6422,
    label = "CHO2(42) + CH3O2(703) <=> CO2_5_(8) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;O_Rrad] for rate rule [C_rad/H2/O;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;O_Rrad] for rate rule [C_rad/H2/O;O_COrad]
""",
)

entry(
    index = 6423,
    label = "CHO2(42) + CH3OO(657) <=> CO2_5_(8) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.964e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]
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
    index = 6426,
    label = "CH3O2(703) + C3H4(45) <=> CH4O2(696) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.009283, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (11.333, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Ct;C_pri_rad] for rate rule [C/H3/Ct;C_rad/H2/O]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C/H3/Ct;C_pri_rad] for rate rule [C/H3/Ct;C_rad/H2/O]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6427,
    label = "CH4O2(696) + C3H3(19) <=> C3H4(45) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.118e-05, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (3.695, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_rad/H2/Ct] + [O/H/NonDeO;C_pri_rad] for rate rule [O/H/NonDeO;C_rad/H2/Ct]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;C_rad/H2/Ct] + [O/H/NonDeO;C_pri_rad] for rate rule [O/H/NonDeO;C_rad/H2/Ct]
""",
)

entry(
    index = 6428,
    label = "CH3O2(703) + CHO2(424) <=> CO2_5_(8) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.128e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;XH_s_Rrad] for rate rule [C_rad/H2/O;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;XH_s_Rrad] for rate rule [C_rad/H2/O;COpri_Orad]
""",
)

entry(
    index = 6429,
    label = "CHO2(424) + CH3OO(657) <=> CO2_5_(8) + CH4O2(696)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.159e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]
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
    index = 6431,
    label = "CH3O(508) + C3H4(39) <=> CH3OH(689) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0084, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_sec_rad] for rate rule [Cd_Cdd/H2;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_Cdd/H2;O_sec_rad] for rate rule [Cd_Cdd/H2;O_rad/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6432,
    label = "CH3OH(689) + C3H7(35) <=> CH3O(508) + C3H8(34)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;C_rad/H2/Cs]
""",
)

entry(
    index = 6433,
    label = "CCadd(1) + CH3O(508) <=> CH3OH(689) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.03042, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (2.34, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H3/Cs\\H3;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [C/H3/Cs\H3;O_rad/NonDeC]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 6434,
    label = "CH3O(508) + C3H3O(700) <=> CH3OH(689) + C3H2O(701)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6435,
    label = "CH3O(508) + C3H6(38) <=> CH3OH(689) + C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.357, 'cm^3/(mol*s)'),
        n = 3.9,
        Ea = (1.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H3/Cd\\H_Cd\\H2;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [C/H3/Cd\H_Cd\H2;O_rad/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6436,
    label = "O2_2_(13) + CH3OH(689) <=> HO2_17_(5) + CH3O(508)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56.124, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6437,
    label = "CH2OH(32) + C3H5(41) <=> CH3OH(689) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.851e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri_rad;Cdpri_Csrad] for rate rule [C_rad/H2/O;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri_rad;Cdpri_Csrad] for rate rule [C_rad/H2/O;Cdpri_Csrad]
""",
)

entry(
    index = 6438,
    label = "CH3O(508) + C3H5(41) <=> CH3OH(689) + C3H4(39)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.205e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cdpri_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cdpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cdpri_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cdpri_Csrad]
""",
)

entry(
    index = 6439,
    label = "CH2OH(32) + CHO2(424) <=> CO2_5_(8) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.128e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;XH_s_Rrad] for rate rule [C_rad/H2/O;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;XH_s_Rrad] for rate rule [C_rad/H2/O;COpri_Orad]
""",
)

entry(
    index = 6440,
    label = "CH3O(508) + CHO2(424) <=> CO2_5_(8) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Orad]
""",
)

entry(
    index = 6441,
    label = "CH2OH(32) + CHO2(42) <=> CO2_5_(8) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;O_Rrad] for rate rule [C_rad/H2/O;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;O_Rrad] for rate rule [C_rad/H2/O;O_COrad]
""",
)

entry(
    index = 6442,
    label = "CH3O(508) + CHO2(42) <=> CO2_5_(8) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;O_Rrad] for rate rule [O_rad/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;O_Rrad] for rate rule [O_rad/NonDeC;O_COrad]
""",
)

entry(
    index = 6443,
    label = "C2H5(31) + CH2OH(32) <=> CH3OH(689) + C2H4(30)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.67e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/O;Cmethyl_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/O;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6444,
    label = "CH3O(508) + C2H5(31) <=> CH3OH(689) + C2H4(30)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6445,
    label = "CH2OH(32) + C3H7(35) <=> CH3OH(689) + C3H6(38)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/O;C/H2/Nd_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/O;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6446,
    label = "CH3O(508) + C3H7(35) <=> CH3OH(689) + C3H6(38)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H2/Nd_Csrad] for rate rule [O_rad/NonDeC;C/H2/Nd_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6447,
    label = "CH3O(508) + CH2OH(32) <=> CH2O(25) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.156e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;Cmethyl_Rrad] for rate rule [C_rad/H2/O;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;Cmethyl_Rrad] for rate rule [C_rad/H2/O;Cmethyl_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6448,
    label = "CH3O(508) + CH3O(508) <=> CH2O(25) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.446e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 6449,
    label = "CH2OH(32) + CH2OH(32) <=> CH2O(25) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_rad/H2/O;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_rad/H2/O;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6450,
    label = "CH3OH(689) + CH3O(508) <=> CH3OH(689) + CH2OH(32)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2393, 'cm^3/(mol*s)'),
        n = 2.663,
        Ea = (3.538, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri;O_rad/NonDeC] for rate rule [C/H3/O;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri;O_rad/NonDeC] for rate rule [C/H3/O;O_rad/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6451,
    label = "C2H3(29) + CH2OH(32) <=> C2H2(20) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/O;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/O;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6452,
    label = "CH3O(508) + C2H3(29) <=> C2H2(20) + CH3OH(689)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6453,
    label = "CH2OH(32) + C2H3O(430) <=> CH3OH(689) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.128e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;XH_s_Rrad] for rate rule [C_rad/H2/O;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;XH_s_Rrad] for rate rule [C_rad/H2/O;COpri_Csrad]
""",
)

entry(
    index = 6454,
    label = "CH3O(508) + C2H3O(430) <=> CH3OH(689) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Csrad]
""",
)

entry(
    index = 6455,
    label = "CH2OH(32) + C3H3O(700) <=> CH3OH(689) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_rad/H2/O;Cpri_Rrad] for rate rule [C_rad/H2/O;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_rad/H2/O;Cpri_Rrad] for rate rule [C_rad/H2/O;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6456,
    label = "CH2OH(32) + C3H6(38) <=> CH3OH(689) + C3H5(41)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0001008, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cd\\H_Cd\\H2;C_pri_rad] for rate rule [C/H3/Cd\\H_Cd\\H2;C_rad/H2/O]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C/H3/Cd\H_Cd\H2;C_pri_rad] for rate rule [C/H3/Cd\H_Cd\H2;C_rad/H2/O]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6457,
    label = "O_11_(7) + C3H3O(700) <=> OH_12_(12) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.139e+10, 'cm^3/(mol*s)'),
        n = 0.346,
        Ea = (0.946, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [Y_rad_birad_trirad_quadrad;C/H2/De_Rrad] + [Y_1centerbirad;Cpri_Rrad] for rate rule\n[O_atom_triplet;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [Y_rad_birad_trirad_quadrad;C/H2/De_Rrad] + [Y_1centerbirad;Cpri_Rrad] for rate rule
[O_atom_triplet;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6458,
    label = "CH2(T)(24) + C3H3O(700) <=> C3H2O(701) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CH2_triplet;Cpri_Rrad] for rate rule [CH2_triplet;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CH2_triplet;Cpri_Rrad] for rate rule [CH2_triplet;C/H2/De_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6459,
    label = "CH3OH(689) + C3H7(35) <=> CH2OH(32) + C3H8(34)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0003983, 'cm^3/(mol*s)'),
        n = 4.542,
        Ea = (6.707, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri;C_rad/H2/Cs] for rate rule [C/H3/O;C_rad/H2/Cs]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri;C_rad/H2/Cs] for rate rule [C/H3/O;C_rad/H2/Cs]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6460,
    label = "C2H(21) + CH4O2(696) <=> C2H2(20) + CH3OO(657)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;Ct_rad] for rate rule [O/H/NonDeO;Ct_rad/Ct]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec;Ct_rad] for rate rule [O/H/NonDeO;Ct_rad/Ct]
""",
)

entry(
    index = 6461,
    label = "H_10_(3) + C3H2O(701) <=> O_11_(7) + C3H3(19)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.29, -0.001913, -0.00133, -0.0007368],
            [8.749, 0.0009189, 0.0006387, 0.0003538],
            [-0.03677, 0.0004911, 0.0003412, 0.0001888],
            [-0.008049, 6.206e-05, 4.316e-05, 2.393e-05],
            [-0.0005158, -1.979e-05, -1.37e-05, -7.537e-06],
            [0.0005992, -1.586e-05, -1.1e-05, -6.067e-06],
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
    index = 6462,
    label = "O2_2_(13) + C3H3(19) <=> O_11_(7) + C3H3O(706)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.411, -0.004189, -0.00289, -0.001583],
            [3.138, 0.00154, 0.001048, 0.000562],
            [0.04191, -0.0009569, -0.0006571, -0.0003577],
            [0.01153, 0.0001846, 0.0001271, 6.957e-05],
            [0.001636, 0.0004048, 0.0002796, 0.0001532],
            [5.836e-05, 0.0002055, 0.0001423, 7.824e-05],
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
    index = 6464,
    label = "H_10_(3) + C3H3O(706) <=> H2_13_(2) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.358e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;CH_d_Rrad] for rate rule [H_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;CH_d_Rrad] for rate rule [H_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6465,
    label = "OH_12_(12) + C3H3O(706) <=> H2O_14_(6) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.394e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;CH_d_Rrad] for rate rule [O_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6466,
    label = "O2_2_(13) + C3H3O(706) <=> HO2_17_(5) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;Cd_Cdrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O2b;Cd_Cdrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 6467,
    label = "HO2_17_(5) + C3H3O(706) <=> C3H2O(701) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;CH_d_Rrad] for rate rule [O_rad/NonDeO;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6468,
    label = "C3H3O(706) + CH3(17) <=> Cadd(4) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;CH_d_Rrad] for rate rule [C_methyl;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_methyl;CH_d_Rrad] for rate rule [C_methyl;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6469,
    label = "C3H3O(706) + C3H3(19) <=> C3H4(39) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6470,
    label = "C3H7(35) + C3H3O(706) <=> C3H8(34) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6471,
    label = "C2H5(31) + C3H3O(706) <=> CCadd(1) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6472,
    label = "C4H9(37) + C3H3O(706) <=> C4H10(685) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cs;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6473,
    label = "HCCO(26) + C3H3O(706) <=> C3H2O(701) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6474,
    label = "C2H3(29) + C3H3O(706) <=> C2H4(30) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [Cd_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6475,
    label = "HCO(22) + C3H3O(706) <=> CH2O(25) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.447e+06, 'cm^3/(mol*s)'),
        n = 1.902,
        Ea = (-1.131, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;CH_d_Rrad] for rate rule [CO_pri_rad;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6476,
    label = "C3H5(41) + C3H3O(706) <=> C3H6(38) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cd;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/Cd;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6477,
    label = "OH_12_(12) + C3H3(19) <=> H_10_(3) + C3H3O(706)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.848, -0.4826, -0.1446, -0.02056],
            [1.941, 0.3619, 0.1837, 0.0266],
            [0.1033, -0.05138, 0.007668, 0.02328],
            [-0.01241, -0.0408, -0.0234, -8.012e-05],
            [0.0003977, -0.003822, -0.00863, -0.002604],
            [0.004477, 0.006458, 0.0004214, -0.0007245],
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
    index = 6478,
    label = "CH2OH(32) + C3H3O(706) <=> CH3OH(689) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.277e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1.11, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/O;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cs_rad;CH_d_Rrad] for rate rule [C_rad/H2/O;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6479,
    label = "CH3O(508) + C3H3O(706) <=> CH3OH(689) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6480,
    label = "CH3OO(657) + C3H3(19) <=> CH3O(508) + C3H3O(706)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.6, -0.001961, -0.001362, -0.0007536],
            [-0.004729, -0.001643, -0.00114, -0.0006292],
            [-0.003568, -0.0004842, -0.0003357, -0.0001852],
            [-0.002427, 0.0003461, 0.0002401, 0.0001325],
            [-0.001687, 0.0004279, 0.0002964, 0.0001632],
            [-0.00119, 0.0002075, 0.0001434, 7.874e-05],
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
    index = 6481,
    label = "O_11_(7) + C3H3O(706) <=> OH_12_(12) + C3H2O(701)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_atom_triplet;CH_d_Rrad] for rate rule [O_atom_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6482,
    label = "CH2(T)(24) + C3H3O(706) <=> C3H2O(701) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-0.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;CH_d_Rrad] for rate rule [CH2_triplet;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_1centerbirad;CH_d_Rrad] for rate rule [CH2_triplet;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 6484,
    label = "H_10_(3) + CH2O3(707) <=> H2_13_(2) + CHO3(659)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;H_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;H_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6485,
    label = "OH_12_(12) + CH2O3(707) <=> H2O_14_(6) + CHO3(659)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;O_pri_rad]
Multiplied by reaction path degeneracy 2
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
    index = 6487,
    label = "O_11_(7) + CH2O3(707) <=> OH_12_(12) + CHO3(659)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6488,
    label = "HO2_17_(5) + CHO3(659) <=> O2_2_(13) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000188, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (12.422, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]
""",
)

entry(
    index = 6489,
    label = "CHO2(424) + CHO3(659) <=> CO2_5_(8) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.578e+07, 'cm^3/(mol*s)'),
        n = 1.793,
        Ea = (-1.067, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 6490,
    label = "CHO2(42) + CHO3(659) <=> CO2_5_(8) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.351e+08, 'cm^3/(mol*s)'),
        n = 1.569,
        Ea = (-0.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]
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
    index = 6493,
    label = "H_10_(3) + C3H2O(701) <=> C2H2(20) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.68, -0.1698, -0.09862, -0.03835],
            [1.13, 0.2023, 0.1119, 0.0382],
            [0.01439, -0.02999, -0.01024, 0.002736],
            [-0.008319, -0.007946, -0.006456, -0.004032],
            [-0.004084, 0.000309, -0.0002394, -0.0005911],
            [-0.00149, 0.0005163, 0.0003859, 0.0002282],
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
    index = 6494,
    label = "H_10_(3) + C3H2O(701) <=> CO_21_(14) + C2H3(29)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.324, -0.0418, -0.02797, -0.01452],
            [5.528, 0.04926, 0.03262, 0.01661],
            [0.1152, -0.007979, -0.004904, -0.002139],
            [0.03035, -0.001158, -0.0009021, -0.0005854],
            [0.007369, 7.569e-05, 4.263e-05, 1.395e-05],
            [0.001896, 4.106e-05, 3.135e-05, 1.992e-05],
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
    index = 6504,
    label = "H2_13_(2) + C3H3O(700) <=> H_10_(3) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1264, 'cm^3/(mol*s)'),
        n = 4,
        Ea = (4.91, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H2;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H2;O_rad/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6505,
    label = "OH_12_(12) + C3H4O(712) <=> H2O_14_(6) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17.3, 'cm^3/(mol*s)'),
        n = 3.4,
        Ea = (-1.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;O_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;O_pri_rad]
""",
)

entry(
    index = 6506,
    label = "O2_2_(13) + C3H4O(712) <=> HO2_17_(5) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56.753, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6507,
    label = "C3H3O(700) + H2O2(15) <=> HO2_17_(5) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.1134, 'cm^3/(mol*s)'),
        n = 3.855,
        Ea = (8.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H2O2;O_sec_rad] for rate rule [H2O2;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H2O2;O_sec_rad] for rate rule [H2O2;O_rad/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6508,
    label = "Cadd(4) + C3H3O(700) <=> C3H4O(712) + CH3(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00062, 'cm^3/(mol*s)'),
        n = 5,
        Ea = (5.58, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methane;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_methane;O_rad/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6509,
    label = "C3H4(39) + C3H3O(700) <=> C3H4O(712) + C3H3(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0084, 'cm^3/(mol*s)'),
        n = 4.36,
        Ea = (14.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Cd_Cdd/H2;O_sec_rad] for rate rule [Cd_Cdd/H2;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Cd_Cdd/H2;O_sec_rad] for rate rule [Cd_Cdd/H2;O_rad/NonDeC]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6510,
    label = "C3H7(35) + C3H4O(712) <=> C3H8(34) + C3H3O(700)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;C_rad/H2/Cs]
""",
)

entry(
    index = 6511,
    label = "CCadd(1) + C3H3O(700) <=> C2H5(31) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.03042, 'cm^3/(mol*s)'),
        n = 4.52,
        Ea = (2.34, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [C/H3/Cs\\H3;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [C/H3/Cs\H3;O_rad/NonDeC]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 6512,
    label = "C4H9(37) + C3H4O(712) <=> C4H10(685) + C3H3O(700)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;C_rad/H2/Cs]
""",
)

entry(
    index = 6513,
    label = "C2H3(29) + C3H4O(712) <=> C2H4(30) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (6.94, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeC;Cd_pri_rad] for rate rule [O/H/NonDeC;Cd_Cd\\H2_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeC;Cd_pri_rad] for rate rule [O/H/NonDeC;Cd_Cd\H2_pri_rad]
""",
)

entry(
    index = 6514,
    label = "CH2O(25) + C3H3O(700) <=> HCO(22) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.98, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO_pri;O_rad/NonDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6515,
    label = "CH3O(508) + C3H3O(700) <=> CH2O(25) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6516,
    label = "C3H3O(700) + C3H3O(700) <=> C3H2O(701) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;C/H2/De_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;C/H2/De_Orad]
Multiplied by reaction path degeneracy 4
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
    index = 6518,
    label = "CH3OH(689) + C3H3O(700) <=> CH2OH(32) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2393, 'cm^3/(mol*s)'),
        n = 2.663,
        Ea = (3.538, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_pri;O_rad/NonDeC] for rate rule [C/H3/O;O_rad/NonDeC]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_pri;O_rad/NonDeC] for rate rule [C/H3/O;O_rad/NonDeC]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6519,
    label = "CH3O(508) + C3H4O(712) <=> CH3OH(689) + C3H3O(700)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.417, 'cm^3/(mol*s)'),
        n = 3.458,
        Ea = (8.157, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;O_sec_rad] for rate rule [O/H/NonDeC;O_rad/NonDeC]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec;O_sec_rad] for rate rule [O/H/NonDeC;O_rad/NonDeC]
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
    index = 6521,
    label = "OH_12_(12) + CHO3(659) <=> H_10_(3) + CHO4(711)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4, -0.2207, -0.1214, -0.04151],
            [5.452, 0.2628, 0.1354, 0.03747],
            [0.1508, -0.04013, -0.01062, 0.006892],
            [0.03952, -0.01509, -0.0116, -0.006495],
            [0.0183, -0.001925, -0.002125, -0.002007],
            [0.009806, 0.001051, 0.0006209, 0.0002289],
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
    index = 6522,
    label = "C3H3O(700) + CHO2(424) <=> CO2_5_(8) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Orad]
""",
)

entry(
    index = 6523,
    label = "CHO2(42) + C3H3O(700) <=> CO2_5_(8) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;O_Rrad] for rate rule [O_rad/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;O_Rrad] for rate rule [O_rad/NonDeC;O_COrad]
""",
)

entry(
    index = 6524,
    label = "C2H5(31) + C3H3O(700) <=> C2H4(30) + C3H4O(712)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cmethyl_Csrad] + [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;Cmethyl_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6525,
    label = "CH2OH(32) + C3H3O(700) <=> CH2O(25) + C3H4O(712)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_rad/NonDeC;O_Csrad]
""",
)

entry(
    index = 6526,
    label = "C2H3O(430) + C3H3O(700) <=> C3H4O(712) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Csrad]
""",
)

entry(
    index = 6527,
    label = "C3H3O(700) + C3H3O(706) <=> C3H2O(701) + C3H4O(712)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-1.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cd_Cdrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;CH_d_Rrad] for rate rule [O_rad/NonDeC;Cd_Cdrad]
Multiplied by reaction path degeneracy 2
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
    index = 6531,
    label = "OH_12_(12) + CHO3(659) <=> H_10_(3) + CHO4(713)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.85, -0.1471, -0.08847, -0.03715],
            [7.141, 0.175, 0.1009, 0.03818],
            [0.1734, -0.02985, -0.01254, -0.0001295],
            [0.0481, -0.008554, -0.006965, -0.00455],
            [0.0195, -0.001274, -0.00111, -0.000863],
            [0.009683, 0.0004919, 0.0003277, 0.0001702],
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
    index = 6532,
    label = "O_11_(7) + CH3O2(714) <=> OH_12_(12) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.808e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_atom_triplet;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_atom_triplet;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6533,
    label = "H_10_(3) + CH3O2(714) <=> H2_13_(2) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H_rad;O_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6534,
    label = "OH_12_(12) + CH3O2(714) <=> H2O_14_(6) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6535,
    label = "CH3O2(714) + CH3(17) <=> Cadd(4) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.698e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [C_methyl;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [C_methyl;O_Csrad]
Multiplied by reaction path degeneracy 2
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
    index = 6539,
    label = "OH_12_(12) + CH2O4(715) <=> H2O_14_(6) + CHO4(711)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]
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
    index = 6543,
    label = "CO2_5_(8) + HCO(22) <=> O_11_(7) + C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-14.57, -0.2634, -0.1418, -0.04619],
            [19.26, 0.142, 0.0561, -0.0002313],
            [0.01174, 0.02335, 0.01857, 0.009906],
            [-0.01263, 0.003797, 0.004654, 0.004566],
            [-0.007561, -0.0006219, 6.629e-05, 0.0005802],
            [-0.002651, -0.0008312, -0.0006483, -0.0004141],
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
    index = 6545,
    label = "CO2_5_(8) + CHO2(42) <=> O_11_(7) + C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-13.19, -0.04506, -0.03027, -0.01584],
            [18.54, -0.02163, -0.01432, -0.007265],
            [0.01794, -0.0002317, -0.0001788, -0.0001105],
            [-0.02462, 0.005439, 0.003539, 0.001743],
            [-0.02169, 0.00463, 0.003012, 0.001482],
            [-0.01243, 0.002573, 0.001679, 0.0008309],
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
    index = 6551,
    label = "HO2_17_(5) + CO2_5_(8) <=> O_11_(7) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-14.45, -0.03752, -0.02568, -0.01386],
            [19.59, 0.003095, 0.002114, 0.001137],
            [0.1331, 0.005145, 0.003474, 0.001831],
            [0.03723, 0.008681, 0.005843, 0.003063],
            [0.01455, 0.00298, 0.002007, 0.001054],
            [0.005824, -0.001306, -0.0008684, -0.0004452],
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
    index = 6552,
    label = "OH_12_(12) + CHO2(424) <=> H_10_(3) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.4095, -0.001539, -0.00107, -0.0005927],
            [8.083, 0.001816, 0.001262, 0.0006989],
            [0.1281, -0.0003886, -0.0002696, -0.0001489],
            [0.041, -5.728e-05, -4.004e-05, -2.239e-05],
            [0.01571, -5.358e-06, -3.732e-06, -2.074e-06],
            [0.006424, 4.483e-06, 3.121e-06, 1.733e-06],
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
    index = 6553,
    label = "OH_12_(12) + CHO3(659) <=> OH_12_(12) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-1.342, -0.07257, -0.04737, -0.02348],
            [10.05, 0.08528, 0.05456, 0.02601],
            [0.04031, -0.01703, -0.009791, -0.003605],
            [0.01292, -0.002775, -0.002342, -0.001652],
            [0.008, -0.0008374, -0.0005652, -0.0003034],
            [0.005551, -1.182e-05, -1.225e-05, -9.548e-06],
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
    index = 6558,
    label = "HO2_17_(5) + CH2O(25) <=> O_11_(7) + CH3O2(719)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.618, -0.009202, -0.006359, -0.003488],
            [6.633, -0.0003126, -0.0001977, -9.165e-05],
            [0.05595, -0.0008592, -0.000588, -0.0003173],
            [0.01065, 0.001108, 0.0007599, 0.0004113],
            [0.002826, 0.001296, 0.000886, 0.000477],
            [0.0006689, 0.0009121, 0.0006211, 0.0003324],
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
    index = 6560,
    label = "O_11_(7) + CH3O2(719) <=> OH_12_(12) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_1centerbirad;C/H2/Nd_Rrad] for rate rule [O_atom_triplet;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_1centerbirad;C/H2/Nd_Rrad] for rate rule [O_atom_triplet;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6561,
    label = "H_10_(3) + CH3O2(719) <=> H2_13_(2) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.24e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;C/H2/Nd_Rrad] for rate rule [H_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6562,
    label = "OH_12_(12) + CH3O2(719) <=> H2O_14_(6) + CH2O2(594)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;C/H2/Nd_Rrad] for rate rule [O_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6563,
    label = "CH3O2(719) + CH3(17) <=> Cadd(4) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_methyl;C/H2/Nd_Rrad] for rate rule [C_methyl;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_methyl;C/H2/Nd_Rrad] for rate rule [C_methyl;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
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
    index = 6572,
    label = "CO2_5_(8) + CHO2(424) <=> O_11_(7) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-11.92, -0.3806, -0.1784, -0.04181],
            [17.6, 0.2216, 0.06858, -0.009466],
            [-0.1035, 0.01856, 0.02142, 0.009322],
            [-0.06492, 0.0005773, 0.004477, 0.006568],
            [-0.03286, -0.0003999, 0.0004157, 0.001438],
            [-0.01488, 0.0004524, -0.0001198, -0.00042],
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
    index = 6575,
    label = "H_10_(3) + CH2O4(715) <=> H2_13_(2) + CHO4(711)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;H_rad] + [O/H/NonDeO;Y_rad] for rate rule [O/H/NonDeO;H_rad]
""",
)

entry(
    index = 6576,
    label = "OH_12_(12) + CH2O4(715) <=> H2O_14_(6) + CHO4(713)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-0.25, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;O_pri_rad]
""",
)

entry(
    index = 6577,
    label = "CHO2(424) + CHO4(713) <=> CO2_5_(8) + CH2O4(715)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.578e+07, 'cm^3/(mol*s)'),
        n = 1.793,
        Ea = (-1.067, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 6578,
    label = "CHO2(424) + CHO4(711) <=> CO2_5_(8) + CH2O4(715)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.159e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]
""",
)

entry(
    index = 6579,
    label = "CHO2(42) + CHO4(713) <=> CO2_5_(8) + CH2O4(715)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.351e+08, 'cm^3/(mol*s)'),
        n = 1.569,
        Ea = (-0.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]
""",
)

entry(
    index = 6580,
    label = "CHO2(42) + CHO4(711) <=> CO2_5_(8) + CH2O4(715)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.964e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]
""",
)

entry(
    index = 6581,
    label = "CHO2(42) + CH3O2(719) <=> CH2O2(594) + CH2O2(594)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_rad/NonDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6582,
    label = "CHO2(42) + CH3O2(714) <=> CH2O2(594) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6583,
    label = "CHO2(424) + CH3O2(719) <=> CH2O2(594) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/OneDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/OneDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6584,
    label = "CHO2(424) + CH3O2(714) <=> CH2O2(594) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.415e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]
Multiplied by reaction path degeneracy 2
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
    index = 6588,
    label = "OH_12_(12) + CHO2(424) <=> H_10_(3) + CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.08145, -0.001753, -0.001219, -0.0006752],
            [7.432, 0.00209, 0.001452, 0.0008038],
            [0.1039, -0.0004525, -0.0003138, -0.0001732],
            [0.03526, -6.375e-05, -4.46e-05, -2.497e-05],
            [0.01409, -4.287e-06, -2.987e-06, -1.661e-06],
            [0.005954, 5.679e-06, 3.954e-06, 2.196e-06],
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
    index = 6593,
    label = "O_11_(7) + CH3O3(723) <=> OH_12_(12) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.712e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_atom_triplet;O_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_atom_triplet;O_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6594,
    label = "H_10_(3) + CH3O3(723) <=> H2_13_(2) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H_rad;O_Csrad]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 6595,
    label = "OH_12_(12) + CH3O3(723) <=> H2O_14_(6) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_pri_rad;O_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;O_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 6600,
    label = "O2_2_(13) + C2HO2(695) <=> HO2_17_(5) + C2O2(725)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.206e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36.209, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;XH_s_Rrad] for rate rule [O2b;COpri_COrad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;XH_s_Rrad] for rate rule [O2b;COpri_COrad]
Multiplied by reaction path degeneracy 4
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
    index = 6602,
    label = "CO_21_(14) + CHO2(42) <=> OH_12_(12) + C2O2(725)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.701, -0.08566, -0.05467, -0.02595],
            [13.57, 0.07334, 0.04605, 0.02113],
            [-0.3686, 0.01386, 0.008874, 0.004237],
            [-0.1241, -0.005229, -0.002944, -0.001025],
            [-0.04049, -0.005323, -0.003186, -0.001311],
            [-0.01046, 0.00143, 0.0007311, 0.0001778],
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
    index = 6604,
    label = "O_11_(7) + C2HO2(695) <=> OH_12_(12) + C2O2(725)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.837e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-0.473, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_atom_triplet;XH_s_Rrad] for rate rule [O_atom_triplet;COpri_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_atom_triplet;XH_s_Rrad] for rate rule [O_atom_triplet;COpri_COrad]
""",
)

entry(
    index = 6605,
    label = "H_10_(3) + C2HO2(695) <=> H2_13_(2) + C2O2(725)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.089e+10, 'cm^3/(mol*s)'),
        n = 0.783,
        Ea = (0.565, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;XH_s_Rrad] for rate rule [H_rad;COpri_COrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;XH_s_Rrad] for rate rule [H_rad;COpri_COrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6606,
    label = "OH_12_(12) + C2HO2(695) <=> H2O_14_(6) + C2O2(725)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.868e+10, 'cm^3/(mol*s)'),
        n = 0.667,
        Ea = (0.603, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;XH_s_Rrad] for rate rule [O_pri_rad;COpri_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;XH_s_Rrad] for rate rule [O_pri_rad;COpri_COrad]
""",
)

entry(
    index = 6607,
    label = "H_10_(3) + C2O2(725) <=> CO_21_(14) + HCO(22)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [12.17, -0.01367, -0.009229, -0.004864],
            [-1.419, 0.0144, 0.009644, 0.005013],
            [-0.4118, -0.001807, -0.001151, -0.0005437],
            [-0.1141, -0.0001308, -9.966e-05, -6.292e-05],
            [-0.03134, -1.554e-05, -1.106e-05, -6.375e-06],
            [-0.008294, -1.681e-06, -1.232e-06, -7.317e-07],
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
    index = 6608,
    label = "H_10_(3) + C2O2(725) <=> O_11_(7) + HCCO(26)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.393, -1.744e-08, -1.214e-08, -6.741e-09],
            [4.453, 1.705e-08, 1.187e-08, 6.589e-09],
            [-0.05135, -2.682e-10, -1.867e-10, -1.037e-10],
            [-0.008221, -5.727e-10, -3.986e-10, -2.213e-10],
            [0.0006295, -1.867e-10, -1.3e-10, -7.217e-11],
            [0.001483, -2.752e-11, -1.916e-11, -1.064e-11],
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
    index = 6609,
    label = "HO2_17_(5) + C2O2(725) <=> O_11_(7) + C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.065, -9.779e-05, -6.806e-05, -3.779e-05],
            [0.7358, -8.62e-05, -6e-05, -3.331e-05],
            [0.1617, -2.996e-05, -2.085e-05, -1.157e-05],
            [0.04351, -1.262e-05, -8.78e-06, -4.874e-06],
            [0.02092, -7.799e-06, -5.428e-06, -3.013e-06],
            [0.01152, -5.149e-06, -3.583e-06, -1.989e-06],
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
    index = 6612,
    label = "CO2_5_(8) + CHO2(424) <=> CO_21_(14) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-16.98, -0.2019, -0.122, -0.05332],
            [20.41, -0.01118, -0.01081, -0.005955],
            [0.1426, -0.02758, -0.01521, -0.005835],
            [0.008851, -0.005103, -0.00254, -0.0005086],
            [-0.008333, -0.002542, -0.000972, 0.0001486],
            [-0.00772, -0.001313, -0.0005427, 2.544e-05],
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
    index = 6613,
    label = "CO2_5_(8) + CHO2(424) <=> CO_21_(14) + CHO3(722)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-8.421, -0.08323, -0.05432, -0.02698],
            [11.18, -0.04858, -0.02943, -0.01249],
            [-0.02973, -0.03818, -0.02315, -0.009843],
            [-0.01776, -0.01785, -0.01036, -0.003953],
            [-0.009426, -0.009526, -0.005372, -0.001888],
            [-0.004874, -0.004858, -0.002661, -0.000854],
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
    index = 6616,
    label = "CH2O3(727) + CH3(17) <=> Cadd(4) + CHO3(722)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.004442, 'cm^3/(mol*s)'),
        n = 4.228,
        Ea = (1.851, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_sec;C_methyl] + [O/H/NonDeO;Cs_rad] for rate rule [O/H/NonDeO;C_methyl]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;C_methyl] + [O/H/NonDeO;Cs_rad] for rate rule [O/H/NonDeO;C_methyl]
""",
)

entry(
    index = 6617,
    label = "C2H5(31) + CH2O3(727) <=> CCadd(1) + CHO3(722)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.002046, 'cm^3/(mol*s)'),
        n = 4.189,
        Ea = (-1.293, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O/H/NonDeO;C_rad/H2/Cs] for rate rule [O/H/NonDeO;C_rad/H2/Cs\\H3]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O/H/NonDeO;C_rad/H2/Cs] for rate rule [O/H/NonDeO;C_rad/H2/Cs\H3]
""",
)

entry(
    index = 6618,
    label = "OH_12_(12) + CH2O2(594) <=> H_10_(3) + CH2O3(727)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-3.372, -0.0002085, -0.0001451, -8.055e-05],
            [11.67, 0.0001541, 0.0001073, 5.956e-05],
            [0.15, 2.731e-06, 1.9e-06, 1.055e-06],
            [0.03381, 3.705e-06, 2.572e-06, 1.421e-06],
            [0.01104, 3.344e-06, 2.322e-06, 1.284e-06],
            [0.003985, 1.399e-06, 9.705e-07, 5.36e-07],
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
    index = 6621,
    label = "H_10_(3) + CH2O4(715) <=> H2_13_(2) + CHO4(713)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;H_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;H_rad]
""",
)

entry(
    index = 6622,
    label = "O_11_(7) + CH2O4(715) <=> OH_12_(12) + CHO4(711)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;O_atom_triplet] for rate rule [O/H/NonDeO;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec;O_atom_triplet] for rate rule [O/H/NonDeO;O_atom_triplet]
""",
)

entry(
    index = 6623,
    label = "OH_12_(12) + CH2O3(727) <=> H2O_14_(6) + CHO3(718)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-1.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_pri_rad]
""",
)

entry(
    index = 6624,
    label = "O2_2_(13) + CH3O2(719) <=> HO2_17_(5) + CH2O2(594)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;C/H2/Nd_Rrad] for rate rule [O2b;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 6625,
    label = "O2_2_(13) + CH3O2(714) <=> HO2_17_(5) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.577e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;O_Csrad]\nMultiplied by reaction path degeneracy 8',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O2b;O_Csrad]
Multiplied by reaction path degeneracy 8
""",
)

entry(
    index = 6626,
    label = "O2_2_(13) + CH3O3(723) <=> HO2_17_(5) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.865e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O2b;O_Csrad]\nMultiplied by reaction path degeneracy 12',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O2b;O_Csrad]
Multiplied by reaction path degeneracy 12
""",
)

entry(
    index = 6627,
    label = "CHO3(659) + H2O2(15) <=> HO2_17_(5) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0699, 'cm^3/(mol*s)'),
        n = 3.75,
        Ea = (10.89, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using an average for rate rule [H2O2;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using an average for rate rule [H2O2;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6628,
    label = "O2_2_(13) + CH2O3(727) <=> HO2_17_(5) + CHO3(718)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50.132, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O2b]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O2b]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6629,
    label = "HO2_17_(5) + CHO3(722) <=> O2_2_(13) + CH2O3(727)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [X_H;OOC] + [Orad_O_H;O_rad/NonDeO] for rate rule [Orad_O_H;OOC]
""",
)

entry(
    index = 6630,
    label = "CHO2(424) + CHO3(718) <=> CO2_5_(8) + CH2O3(727)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]
""",
)

entry(
    index = 6631,
    label = "CHO2(424) + CHO3(722) <=> CO2_5_(8) + CH2O3(727)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.159e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_Orad]
""",
)

entry(
    index = 6632,
    label = "CHO2(42) + CHO3(718) <=> CO2_5_(8) + CH2O3(727)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]
""",
)

entry(
    index = 6633,
    label = "CHO2(42) + CHO3(722) <=> CO2_5_(8) + CH2O3(727)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.964e+08, 'cm^3/(mol*s)'),
        n = 1.345,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;O_Rrad] for rate rule [O_rad/NonDeO;O_COrad]
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
    index = 6639,
    label = "O_11_(7) + CH2O4(715) <=> OH_12_(12) + CHO4(713)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/OneDeC;O_atom_triplet]
""",
)

entry(
    index = 6640,
    label = "OH_12_(12) + CH2O3(727) <=> H2O_14_(6) + CHO3(722)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;O_pri_rad] + [O/H/NonDeO;O_rad] for rate rule [O/H/NonDeO;O_pri_rad]
""",
)

entry(
    index = 6641,
    label = "HO2_17_(5) + C2HO2(695) <=> C2O2(725) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.159e+06, 'cm^3/(mol*s)'),
        n = 2.018,
        Ea = (-1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeO;XH_s_Rrad] for rate rule [O_rad/NonDeO;COpri_COrad]
""",
)

entry(
    index = 6642,
    label = "HO2_17_(5) + CHO4(713) <=> O2_2_(13) + CH2O4(715)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000188, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (12.422, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;O_rad/OneDeC] for rate rule [Orad_O_H;O_rad/OneDeC]
""",
)

entry(
    index = 6643,
    label = "HO2_17_(5) + CHO4(711) <=> O2_2_(13) + CH2O4(715)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [X_H;OOC] + [Orad_O_H;O_rad/NonDeO] for rate rule [Orad_O_H;OOC]
""",
)

entry(
    index = 6644,
    label = "HCO(22) + HCO(22) <=> H_10_(3) + C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.885, -0.02563, -0.01729, -0.009095],
            [2.932, 0.03415, 0.0229, 0.01193],
            [0.1057, -0.008639, -0.005612, -0.002754],
            [0.02392, -0.0005781, -0.0004886, -0.0003482],
            [0.005753, 0.0002721, 0.0001864, 0.0001004],
            [0.001372, 8.64e-05, 6.321e-05, 3.79e-05],
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
    index = 6649,
    label = "H_10_(3) + CH2O4(715) <=> OH_12_(12) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.841, -0.004087, -0.002821, -0.001545],
            [4.177, 0.005965, 0.004112, 0.002246],
            [0.1571, -0.002293, -0.001571, -0.0008493],
            [0.03375, 0.0004093, 0.0002738, 0.000142],
            [0.00686, 3.308e-06, 5.578e-06, 6.053e-06],
            [0.0008047, -1.221e-05, -9.033e-06, -5.491e-06],
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
    index = 6650,
    label = "HO2_17_(5) + CH3O2(719) <=> CH2O2(594) + H2O2(15)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/NonDeO;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6651,
    label = "HO2_17_(5) + CH3O2(714) <=> CH2O2(594) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.42e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
Multiplied by reaction path degeneracy 2
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
    index = 6653,
    label = "CO2_5_(8) + CHO2(42) <=> H_10_(3) + C2O4(730)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.053, -0.1632, -0.1028, -0.04754],
            [10.68, 0.09386, 0.05477, 0.02118],
            [-0.1008, 3.63e-05, 0.001831, 0.002529],
            [-0.07418, 0.001514, 0.001008, 0.0005383],
            [-0.01792, 0.000761, 0.0005199, 0.0002774],
            [-0.001832, 0.0001171, 7.244e-05, 3.296e-05],
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
    index = 6654,
    label = "CH2O(25) + CHO3(659) <=> HCO(22) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156.1, 'cm^3/(mol*s)'),
        n = 2.935,
        Ea = (9.509, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [X_H;O_rad/OneDeC] + [CO_pri;O_sec_rad] for rate rule [CO_pri;O_rad/OneDeC]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [X_H;O_rad/OneDeC] + [CO_pri;O_sec_rad] for rate rule [CO_pri;O_rad/OneDeC]
Multiplied by reaction path degeneracy 2
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
    index = 6656,
    label = "O_11_(7) + CH3O3(731) <=> OH_12_(12) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.758e+11, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (-0.047, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdNd_Rrad] for rate rule [O_atom_triplet;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdNd_Rrad] for rate rule [O_atom_triplet;C/H/NdNd_Orad]
""",
)

entry(
    index = 6657,
    label = "H_10_(3) + CH3O3(731) <=> H2_13_(2) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.808e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H/NdNd_Rrad] for rate rule [H_rad;C/H/NdNd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;C/H/NdNd_Rrad] for rate rule [H_rad;C/H/NdNd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6658,
    label = "OH_12_(12) + CH3O3(731) <=> H2O_14_(6) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C/H/NdNd_Rrad] for rate rule [O_pri_rad;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;C/H/NdNd_Rrad] for rate rule [O_pri_rad;C/H/NdNd_Orad]
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
    index = 6662,
    label = "O2_2_(13) + CH3O3(731) <=> HO2_17_(5) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H/NdNd_Rrad] for rate rule [O2b;C/H/NdNd_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;C/H/NdNd_Rrad] for rate rule [O2b;C/H/NdNd_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6663,
    label = "HO2_17_(5) + CH2O2(594) <=> O_11_(7) + CH3O3(731)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-0.144, -0.01365, -0.009432, -0.005173],
            [8.676, 0.00143, 0.0009959, 0.0005531],
            [-0.1868, 0.003914, 0.00269, 0.001462],
            [-0.08411, 0.004162, 0.002856, 0.001548],
            [-0.04611, 0.001238, 0.0008501, 0.0004612],
            [-0.0254, -0.0005606, -0.0003803, -0.0002022],
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
    index = 6664,
    label = "HO2_17_(5) + CH3O3(731) <=> CH2O3(707) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H/NdNd_Rrad] for rate rule [O_rad/NonDeO;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H/NdNd_Rrad] for rate rule [O_rad/NonDeO;C/H/NdNd_Orad]
""",
)

entry(
    index = 6665,
    label = "HO2_17_(5) + CH3O3(723) <=> CH2O3(707) + H2O2(15)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_rad/NonDeO;O_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_rad/NonDeO;O_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 6671,
    label = "HCO(22) + CHO2(42) <=> OH_12_(12) + C2HO2(695)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.335, -0.1147, -0.0702, -0.03063],
            [4.221, 0.1407, 0.08378, 0.03433],
            [0.001243, -0.02092, -0.00959, -0.00114],
            [-0.001858, -0.007653, -0.005528, -0.003166],
            [-0.001097, -5.564e-05, -0.0003185, -0.0004312],
            [-0.001205, 0.0005103, 0.0003435, 0.0001756],
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
    index = 6672,
    label = "HCO(22) + CHO2(42) <=> H_10_(3) + C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.897, -0.2448, -0.1205, -0.03214],
            [2.442, 0.3135, 0.1446, 0.03031],
            [0.07516, -0.05642, -0.01311, 0.008231],
            [0.008516, -0.01806, -0.01329, -0.006131],
            [0.0006157, 0.001722, -0.0005728, -0.001772],
            [-0.001496, 0.001884, 0.001202, 0.000425],
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
    index = 6673,
    label = "HCO(22) + CHO2(42) <=> H_10_(3) + C2HO3(732)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [3.119, -0.04727, -0.03129, -0.01592],
            [5.855, 0.06018, 0.03941, 0.01966],
            [0.07026, -0.01232, -0.007522, -0.003238],
            [-0.0003678, -0.001964, -0.001539, -0.001005],
            [-0.0101, 0.0003227, 0.0001961, 8.177e-05],
            [-0.007614, 0.0001309, 9.998e-05, 6.343e-05],
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
    index = 6677,
    label = "O_11_(7) + CHO3(720) <=> OH_12_(12) + CO3(733)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.758e+11, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (-0.047, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdNd_Rrad] for rate rule [O_atom_triplet;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdNd_Rrad] for rate rule [O_atom_triplet;C/H/NdNd_Orad]
""",
)

entry(
    index = 6678,
    label = "O_11_(7) + CHO3(717) <=> OH_12_(12) + CO3(733)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.04e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_atom_triplet;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_atom_triplet;O_Csrad]
""",
)

entry(
    index = 6679,
    label = "H_10_(3) + CHO3(720) <=> H2_13_(2) + CO3(733)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.808e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H/NdNd_Rrad] for rate rule [H_rad;C/H/NdNd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;C/H/NdNd_Rrad] for rate rule [H_rad;C/H/NdNd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6680,
    label = "H_10_(3) + CHO3(717) <=> H2_13_(2) + CO3(733)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H_rad;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6681,
    label = "OH_12_(12) + CHO3(720) <=> H2O_14_(6) + CO3(733)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C/H/NdNd_Rrad] for rate rule [O_pri_rad;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;C/H/NdNd_Rrad] for rate rule [O_pri_rad;C/H/NdNd_Orad]
""",
)

entry(
    index = 6682,
    label = "OH_12_(12) + CHO3(717) <=> H2O_14_(6) + CO3(733)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;O_Csrad]
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
    index = 6689,
    label = "HO2_17_(5) + C2O2(725) <=> O_11_(7) + C2HO3(732)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [2.127, -0.09352, -0.05984, -0.02858],
            [1.803, 0.09418, 0.05793, 0.02545],
            [0.2953, -0.02788, -0.0159, -0.005772],
            [0.0397, -0.001454, -0.001734, -0.001565],
            [0.002344, 0.00331, 0.002171, 0.001074],
            [-0.001991, 0.0006081, 0.0004998, 0.0003457],
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
    index = 6697,
    label = "OH_12_(12) + CH2OH(32) <=> H_10_(3) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [11.44, -0.7193, -0.1543, -0.004106],
            [0.7122, 0.7783, 0.11, -0.01936],
            [-0.03576, 0.00497, 0.0594, 0.01735],
            [-0.02684, -0.05765, -0.007808, 0.006819],
            [-0.003497, -0.01949, -0.01137, -0.001607],
            [0.002806, -0.001287, -0.003733, -0.001865],
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
    index = 6698,
    label = "OH_12_(12) + CH2OH(32) <=> H_10_(3) + CH3O2(719)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.894, -0.5021, -0.1698, -0.01521],
            [1.657, 0.5733, 0.1616, -0.005351],
            [0.06587, -0.02746, 0.0291, 0.02232],
            [0.003552, -0.04206, -0.01615, 0.00126],
            [0.005042, -0.01069, -0.008588, -0.003554],
            [0.005257, 0.0008041, -0.001242, -0.001583],
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
    index = 6702,
    label = "O_11_(7) + C2HO4(737) <=> OH_12_(12) + C2O4(730)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.758e+11, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (-0.047, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdNd_Rrad] for rate rule [O_atom_triplet;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdNd_Rrad] for rate rule [O_atom_triplet;C/H/NdNd_Orad]
""",
)

entry(
    index = 6703,
    label = "H_10_(3) + C2HO4(737) <=> H2_13_(2) + C2O4(730)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.808e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;C/H/NdNd_Rrad] for rate rule [H_rad;C/H/NdNd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;C/H/NdNd_Rrad] for rate rule [H_rad;C/H/NdNd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6704,
    label = "OH_12_(12) + C2HO4(737) <=> H2O_14_(6) + C2O4(730)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;C/H/NdNd_Rrad] for rate rule [O_pri_rad;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;C/H/NdNd_Rrad] for rate rule [O_pri_rad;C/H/NdNd_Orad]
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
    index = 6706,
    label = "H_10_(3) + CH2O3(727) <=> H2_13_(2) + CHO3(718)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;H_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;H_rad]
""",
)

entry(
    index = 6707,
    label = "CHO2(42) + CHO2(42) <=> OH_12_(12) + C2HO3(716)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.5, -0.08812, -0.05406, -0.02377],
            [3.522, 0.1011, 0.0606, 0.02531],
            [0.01205, -0.008855, -0.003921, -0.0003114],
            [-0.007944, -0.005317, -0.003335, -0.001521],
            [-0.008642, -0.001021, -0.0007718, -0.0004754],
            [-0.005551, -9.465e-06, -5.702e-05, -7.51e-05],
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
    index = 6708,
    label = "CHO2(42) + CHO2(42) <=> H_10_(3) + C2HO4(736)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.616, -0.04407, -0.02898, -0.01457],
            [4.79, 0.04982, 0.03243, 0.016],
            [0.08005, -0.00344, -0.001933, -0.0006638],
            [-0.00696, -0.002959, -0.001938, -0.0009665],
            [-0.01763, -0.0006044, -0.0004339, -0.0002523],
            [-0.01223, 1.249e-05, -7.878e-06, -1.911e-05],
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
    index = 6709,
    label = "CO_21_(14) + CH2O2(594) <=> H_10_(3) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.862, -0.3238, -0.1609, -0.0417],
            [15.75, 0.3566, 0.1611, 0.02689],
            [-0.04327, -0.01503, 0.009857, 0.01719],
            [-0.04179, -0.02829, -0.01503, -0.003404],
            [-0.01246, -0.00609, -0.005526, -0.003845],
            [-0.001409, 0.002426, 0.0007394, -0.0004684],
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
    index = 6711,
    label = "CO_21_(14) + CH2O3(707) <=> CHO2(42) + CHO2(424)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.333, -0.9445, -0.2169, 0.0107],
            [15.16, 0.7999, 0.05922, -0.06566],
            [-0.06251, 0.09439, 0.09049, 0.006246],
            [-0.06957, -0.04891, 0.0131, 0.02012],
            [-0.02202, -0.02408, -0.01193, 0.004128],
            [4.986e-05, 0.00196, -0.005272, -0.003057],
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
    index = 6712,
    label = "CO_21_(14) + CH2O3(707) <=> OH_12_(12) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-10.73, -0.6541, -0.2299, -0.0155],
            [17.38, 0.6212, 0.152, -0.03675],
            [-0.1352, 0.02289, 0.05738, 0.02717],
            [-0.07465, -0.04735, -0.01057, 0.01092],
            [-0.02344, -0.01439, -0.01154, -0.003146],
            [-0.003513, 0.004797, -0.0006786, -0.003081],
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
    index = 6713,
    label = "CO_21_(14) + CH2O3(707) <=> HCO(22) + CHO3(659)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.846, -1.014, -0.2071, 0.01322],
            [14.54, 0.828, 0.02989, -0.06462],
            [-0.06592, 0.1159, 0.09273, -0.001746],
            [-0.06978, -0.04616, 0.02046, 0.01995],
            [-0.02154, -0.02578, -0.01022, 0.006279],
            [0.0009351, 0.001067, -0.00616, -0.002416],
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
    index = 6714,
    label = "CO_21_(14) + CH2O3(707) <=> H_10_(3) + C2HO4(724)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-9.851, -0.7509, -0.2198, -0.001883],
            [16.05, 0.7319, 0.13, -0.05093],
            [-0.05003, 0.02929, 0.07562, 0.02572],
            [-0.06665, -0.05785, -0.008352, 0.01564],
            [-0.01868, -0.01808, -0.0149, -0.002562],
            [0.0006692, 0.004974, -0.001983, -0.004027],
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
    index = 6715,
    label = "CO_21_(14) + CH2O3(707) <=> H_10_(3) + C2HO4(729)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-12.01, -0.6323, -0.2218, -0.01494],
            [17.31, 0.6327, 0.1605, -0.03283],
            [-0.08541, 0.01078, 0.05569, 0.02971],
            [-0.06364, -0.05175, -0.01435, 0.00977],
            [-0.01846, -0.01371, -0.01234, -0.004438],
            [-0.0009775, 0.0055, -0.0002201, -0.003195],
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
    index = 6716,
    label = "CHO2(42) + CH2O2(594) <=> H_10_(3) + S(738)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.917, -7.73e-05, -5.38e-05, -2.987e-05],
            [4.738, -5.186e-06, -3.608e-06, -2.002e-06],
            [0.1485, 1.307e-05, 9.097e-06, 5.05e-06],
            [0.02911, 2.371e-05, 1.65e-05, 9.16e-06],
            [0.007449, 1.047e-05, 7.287e-06, 4.045e-06],
            [0.002209, -1.554e-06, -1.081e-06, -5.998e-07],
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
    index = 6721,
    label = "H_10_(3) + CH2O3(727) <=> H2_13_(2) + CHO3(722)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_sec;H_rad] + [O/H/NonDeO;Y_rad] for rate rule [O/H/NonDeO;H_rad]
""",
)

entry(
    index = 6722,
    label = "OH_12_(12) + S(738) <=> H2O_14_(6) + C2HO4(724)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+06, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-1.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_pri_rad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_pri_rad]
""",
)

entry(
    index = 6723,
    label = "CHO3(659) + CH2O2(594) <=> CHO2(42) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23980, 'cm^3/(mol*s)'),
        n = 2.125,
        Ea = (6.365, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO/H/NonDe;O_sec_rad] for rate rule [CO/H/NonDe;O_rad/OneDeC]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO/H/NonDe;O_sec_rad] for rate rule [CO/H/NonDe;O_rad/OneDeC]
""",
)

entry(
    index = 6724,
    label = "CHO2(42) + CH3O3(731) <=> CH2O2(594) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.729e+12, 'cm^3/(mol*s)'),
        n = -0.059,
        Ea = (-0.093, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad;C/H/NdNd_Rrad] for rate rule [CO_rad/NonDe;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;C/H/NdNd_Rrad] for rate rule [CO_rad/NonDe;C/H/NdNd_Orad]
""",
)

entry(
    index = 6725,
    label = "CHO2(42) + CH3O3(723) <=> CH2O2(594) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.43e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;O_Csrad] for rate rule [CO_rad/NonDe;O_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6726,
    label = "CHO2(424) + CH3O3(731) <=> CH2O2(594) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H/NdNd_Rrad] for rate rule [O_rad/OneDe;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H/NdNd_Rrad] for rate rule [O_rad/OneDe;C/H/NdNd_Orad]
""",
)

entry(
    index = 6727,
    label = "CHO2(424) + CH3O3(723) <=> CH2O2(594) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.123e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6728,
    label = "CHO3(659) + CH3O2(719) <=> CH2O2(594) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/OneDe;C/H2/Nd_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H2/Nd_Rrad] for rate rule [O_rad/OneDe;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6729,
    label = "CHO3(659) + CH3O2(714) <=> CH2O2(594) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.415e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]
Multiplied by reaction path degeneracy 2
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
    index = 6741,
    label = "CO2_5_(8) + CH2(S)(28) <=> O(734) + CH2CO(16)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-6.142, -0.001116, -0.0007762, -0.0004305],
            [12.61, 0.0008397, 0.0005839, 0.0003237],
            [-0.001018, -5.8e-05, -4.024e-05, -2.222e-05],
            [-0.01223, -7.387e-05, -5.139e-05, -2.851e-05],
            [-0.007641, -4.072e-05, -2.834e-05, -1.573e-05],
            [-0.00375, -1.243e-05, -8.652e-06, -4.804e-06],
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
    index = 6742,
    label = "CO2_5_(8) + CH2(S)(28) <=> H_10_(3) + C2HO2(741)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.381, -0.00372, -0.002583, -0.001428],
            [5.77, 0.003591, 0.00249, 0.001374],
            [0.1313, -0.0004778, -0.0003296, -0.0001803],
            [0.03019, -0.0002319, -0.0001615, -8.969e-05],
            [0.006636, -8.187e-05, -5.703e-05, -3.171e-05],
            [0.001211, -1.491e-05, -1.04e-05, -5.799e-06],
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
    index = 6744,
    label = "HCO(22) + CH2O2(594) <=> CO_21_(14) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-4.135, -0.0006698, -0.0004661, -0.0002587],
            [12.16, -0.0001471, -0.0001023, -5.676e-05],
            [0.05231, 0.0001806, 0.0001257, 6.97e-05],
            [0.001111, 0.0002268, 0.0001578, 8.749e-05],
            [0.001183, 7.478e-05, 5.201e-05, 2.884e-05],
            [0.0009826, -3.541e-05, -2.462e-05, -1.365e-05],
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
    index = 6749,
    label = "O_11_(7) + CH2O3(727) <=> OH_12_(12) + CHO3(718)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.79, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_atom_triplet]
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
    index = 6754,
    label = "O_11_(7) + CH2O3(727) <=> OH_12_(12) + CHO3(722)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.611e+09, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (3.76, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec;O_atom_triplet] for rate rule [O/H/NonDeO;O_atom_triplet]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec;O_atom_triplet] for rate rule [O/H/NonDeO;O_atom_triplet]
""",
)

entry(
    index = 6755,
    label = "OH_12_(12) + CH4O2(744) <=> H2O_14_(6) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43100, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (-1.738, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/NonDeO;O_pri_rad] for rate rule [C/H2/O2;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C/H2/NonDeO;O_pri_rad] for rate rule [C/H2/O2;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6756,
    label = "H_10_(3) + CH4O2(744) <=> H2_13_(2) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5220, 'cm^3/(mol*s)'),
        n = 3.04,
        Ea = (2.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/NonDeO;H_rad] for rate rule [C/H2/O2;H_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C/H2/NonDeO;H_rad] for rate rule [C/H2/O2;H_rad]
Multiplied by reaction path degeneracy 2
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
    index = 6758,
    label = "OH_12_(12) + CH4O2(744) <=> H2O_14_(6) + CH3O2(719)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (34.6, 'cm^3/(mol*s)'),
        n = 3.4,
        Ea = (-1.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6759,
    label = "HO2_17_(5) + CH3O2(714) <=> O2_2_(13) + CH4O2(744)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.003379, 'cm^3/(mol*s)'),
        n = 4.165,
        Ea = (2.503, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [X_H;C_rad/H/NonDeO] for rate rule [Orad_O_H;C_rad/H/O2]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [X_H;C_rad/H/NonDeO] for rate rule [Orad_O_H;C_rad/H/O2]
""",
)

entry(
    index = 6760,
    label = "O2_2_(13) + CH4O2(744) <=> HO2_17_(5) + CH3O2(719)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (57.545, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O/H/NonDeC;O2b]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O/H/NonDeC;O2b]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6761,
    label = "CHO2(424) + CH3O2(714) <=> CO2_5_(8) + CH4O2(744)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.013e+10, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (0.912, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;XH_s_Rrad] for rate rule [C_rad/H/O2;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_sec_rad;XH_s_Rrad] for rate rule [C_rad/H/O2;COpri_Orad]
""",
)

entry(
    index = 6762,
    label = "CHO2(424) + CH3O2(719) <=> CO2_5_(8) + CH4O2(744)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;XH_s_Rrad] for rate rule [O_rad/NonDeC;COpri_Orad]
""",
)

entry(
    index = 6763,
    label = "CHO2(42) + CH3O2(714) <=> CO2_5_(8) + CH4O2(744)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/O2;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C_sec_rad;O_Rrad] for rate rule [C_rad/H/O2;O_COrad]
""",
)

entry(
    index = 6764,
    label = "CHO2(42) + CH3O2(719) <=> CO2_5_(8) + CH4O2(744)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad/NonDeC;O_Rrad] for rate rule [O_rad/NonDeC;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad/NonDeC;O_Rrad] for rate rule [O_rad/NonDeC;O_COrad]
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
    index = 6767,
    label = "HCO(22) + CHO2(424) <=> H_10_(3) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [8.152, -0.2804, -0.1444, -0.04154],
            [2.246, 0.3226, 0.1534, 0.03217],
            [0.04495, -0.02821, 0.0005428, 0.01333],
            [-0.0435, -0.0248, -0.01496, -0.005271],
            [-0.01776, -0.002995, -0.00362, -0.0032],
            [-0.004685, 0.002726, 0.001308, 0.0001303],
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
    index = 6771,
    label = "O_11_(7) + CH4O2(744) <=> OH_12_(12) + CH3O2(714)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H2/NonDeO;O_atom_triplet] for rate rule [C/H2/O2;O_atom_triplet]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [C/H2/NonDeO;O_atom_triplet] for rate rule [C/H2/O2;O_atom_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6772,
    label = "O_11_(7) + C2HO3(728) <=> OH_12_(12) + C2O3(745)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdDe_Rrad] for rate rule [O_atom_triplet;C/H/NdDe_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad_birad_trirad_quadrad;C/H/NdDe_Rrad] for rate rule [O_atom_triplet;C/H/NdDe_Orad]
""",
)

entry(
    index = 6773,
    label = "O_11_(7) + C2HO3(743) <=> OH_12_(12) + C2O3(745)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.04e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_atom_triplet;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_atom_triplet;O_Csrad]
""",
)

entry(
    index = 6774,
    label = "H_10_(3) + C2HO3(728) <=> H2_13_(2) + C2O3(745)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.735e+10, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (1.005, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [H_rad;Csec_Rrad] for rate rule [H_rad;C/H/NdDe_Orad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [H_rad;Csec_Rrad] for rate rule [H_rad;C/H/NdDe_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6775,
    label = "H_10_(3) + C2HO3(743) <=> H2_13_(2) + C2O3(745)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H_rad;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6776,
    label = "OH_12_(12) + C2HO3(728) <=> H2O_14_(6) + C2O3(745)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/NdDe_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_pri_rad;Csec_Rrad] for rate rule [O_pri_rad;C/H/NdDe_Orad]
""",
)

entry(
    index = 6777,
    label = "OH_12_(12) + C2HO3(743) <=> H2O_14_(6) + C2O3(745)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;O_Csrad]
""",
)

entry(
    index = 6778,
    label = "O2_2_(13) + CHO3(720) <=> HO2_17_(5) + CO3(733)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O2b;C/H/NdNd_Rrad] for rate rule [O2b;C/H/NdNd_Orad]\nMultiplied by reaction path degeneracy 4',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O2b;C/H/NdNd_Rrad] for rate rule [O2b;C/H/NdNd_Orad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6779,
    label = "O2_2_(13) + CHO3(717) <=> HO2_17_(5) + CO3(733)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O2b;O_Csrad]
Multiplied by reaction path degeneracy 4
""",
)

entry(
    index = 6780,
    label = "CHO2(42) + C2HO2(695) <=> CH2O2(594) + C2O2(725)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_COrad]
""",
)

entry(
    index = 6781,
    label = "C2HO2(695) + CHO2(424) <=> CH2O2(594) + C2O2(725)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.578e+07, 'cm^3/(mol*s)'),
        n = 1.793,
        Ea = (-1.067, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_COrad]
""",
)

entry(
    index = 6782,
    label = "CHO3(659) + CH3O3(731) <=> CH2O3(707) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_rad;C/H/NdNd_Rrad] for rate rule [O_rad/OneDe;C/H/NdNd_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_rad;C/H/NdNd_Rrad] for rate rule [O_rad/OneDe;C/H/NdNd_Orad]
""",
)

entry(
    index = 6783,
    label = "CHO3(659) + CH3O3(723) <=> CH2O3(707) + CH2O3(707)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.123e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Csrad] for rate rule [O_rad/OneDe;O_Csrad]
Multiplied by reaction path degeneracy 3
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
    index = 6787,
    label = "HO2_17_(5) + C2O2(725) <=> OH_12_(12) + C2O3(745)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.107, -0.05089, -0.03368, -0.01713],
            [2.621, 0.02202, 0.01453, 0.007353],
            [-0.2428, 0.0003966, 0.0002958, 0.0001819],
            [-0.1604, 0.00255, 0.001742, 0.000937],
            [-0.05802, 0.001886, 0.001274, 0.0006719],
            [-0.01232, 0.000939, 0.0006111, 0.0003012],
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
    index = 6788,
    label = "OH_12_(12) + C2O3(745) <=> CO_21_(14) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.172, -0.8462, -0.2116, -0.01342],
            [4.657, 0.6706, 0.04055, -0.04711],
            [-0.002502, -0.04594, 0.04871, 0.009555],
            [0.02422, -0.03481, -0.00608, 0.007232],
            [0.02444, 0.01375, -0.002441, -0.001359],
            [0.007859, 0.01007, 0.003574, -0.000556],
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
    index = 6793,
    label = "HO2_17_(5) + C2O2(725) <=> CO_21_(14) + CHO3(718)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [5.407, -0.05358, -0.0354, -0.01796],
            [3.046, 0.01944, 0.01282, 0.006479],
            [-0.237, -0.0005131, -0.0003198, -0.0001438],
            [-0.1578, 0.002385, 0.001639, 0.0008893],
            [-0.06063, 0.00195, 0.001324, 0.0007049],
            [-0.01602, 0.001042, 0.0006808, 0.0003382],
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
    index = 6794,
    label = "CHO2(424) + C2HO4(724) <=> CO2_5_(8) + S(738)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;XH_s_Rrad] for rate rule [CO_rad/NonDe;COpri_Orad]
""",
)

entry(
    index = 6795,
    label = "CHO2(424) + C2HO4(729) <=> CO2_5_(8) + S(738)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.578e+07, 'cm^3/(mol*s)'),
        n = 1.793,
        Ea = (-1.067, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;COpri_Orad]
""",
)

entry(
    index = 6796,
    label = "CHO2(42) + C2HO4(724) <=> CO2_5_(8) + S(738)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [CO_rad;O_Rrad] for rate rule [CO_rad/NonDe;O_COrad]
""",
)

entry(
    index = 6797,
    label = "CHO2(42) + C2HO4(729) <=> CO2_5_(8) + S(738)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.351e+08, 'cm^3/(mol*s)'),
        n = 1.569,
        Ea = (-0.933, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [O_sec_rad;O_Rrad] for rate rule [O_rad/OneDe;O_COrad]
""",
)

entry(
    index = 6798,
    label = "HCO(22) + CH3O2(719) <=> CH2O(25) + CH2O2(594)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;C/H2/Nd_Rrad] for rate rule [CO_pri_rad;C/H2/Nd_Orad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6799,
    label = "HCO(22) + CH3O2(714) <=> CH2O(25) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO_pri_rad;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO_pri_rad;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6800,
    label = "CH3O(508) + CHO2(42) <=> CH2O(25) + CH2O2(594)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using template [Y_rad;Cmethyl_Orad] for rate rule [CO_rad/NonDe;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 6801,
    label = "CH3O(508) + CHO2(424) <=> CH2O(25) + CH2O2(594)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.47e+09, 'cm^3/(mol*s)'),
        n = 1.397,
        Ea = (-0.831, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_Orad]\nMultiplied by reaction path degeneracy 3',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Estimated using average of templates [O_rad;Cmethyl_Rrad] + [O_sec_rad;XH_s_Rrad] for rate rule [O_rad/OneDe;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
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
    index = 6803,
    label = "OH_12_(12) + S(747) <=> H2O_14_(6) + C2HO3(721)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+06, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-1.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [CO/H/NonDe;O_pri_rad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [CO/H/NonDe;O_pri_rad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6804,
    label = "HCO(22) + CH2O2(594) <=> H_10_(3) + S(747)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [6.432, -0.00103, -0.0007165, -0.0003975],
            [4.921, -7.954e-07, -5.276e-07, -2.691e-07],
            [0.1193, 0.0002427, 0.0001687, 9.355e-05],
            [0.01869, 0.0002826, 0.0001965, 0.0001089],
            [0.0003745, 7.593e-05, 5.281e-05, 2.928e-05],
            [-0.001761, -5.238e-05, -3.64e-05, -2.016e-05],
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
    index = 6808,
    label = "O_11_(7) + C2HO4(748) <=> OH_12_(12) + C2O4(730)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.04e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [O_atom_triplet;O_Csrad]',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_atom_triplet;O_Csrad]
""",
)

entry(
    index = 6809,
    label = "H_10_(3) + C2HO4(748) <=> H2_13_(2) + C2O4(730)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Exact match found for rate rule [H_rad;O_Csrad]\nMultiplied by reaction path degeneracy 2',
    ),
    longDesc = 
u"""
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [H_rad;O_Csrad]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 6810,
    label = "OH_12_(12) + C2HO4(748) <=> H2O_14_(6) + C2O4(730)",
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
Originally from reaction library: SABIC_Pilot_Plant_Burner
Exact match found for rate rule [O_pri_rad;O_Csrad]
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

