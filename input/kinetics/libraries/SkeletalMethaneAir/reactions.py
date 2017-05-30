#!/usr/bin/env python
# encoding: utf-8

name = "SkeletalMethaneAir"
shortDesc = u""
longDesc = u"""
A skeletal methane-air model for seed. Taken from http://dx.doi.org/10.2514/6.2017-0835
"""

entry(
    index = 1,
    label = "HO2(9) + CH3(18) <=> CH4(1) + O2(2)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126900, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3.022, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "O2(2) + H(4) <=> HO2(9)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.651e+12, 'cm^3/(mol*s)'),
            n = 0.44,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (9.042e+19, 'cm^6/(mol^2*s)'),
            n = -1.5,
            Ea = (0.492, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2, '[O][O]': 0.78, 'O=C=O': 3.8, 'O': 14, '[Ar]': 0.67},
    ),
)

entry(
    index = 3,
    label = "H(4) + CH3(18) <=> CH4(1)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 3.42, 'C=O': 2.5, '[O][O]': 0.59, 'N#N': 0.59, '[Ar]': 0.36},
    ),
)

entry(
    index = 4,
    label = "H(4) + HO2(9) <=> OH(6) + OH(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.079e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.295, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "H(4) + HO2(9) <=> O2(2) + H2(7)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.75e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (-1.451, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "H2(7) <=> H(4) + H(4)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104.38, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0},
    ),
)

entry(
    index = 7,
    label = "Ar + H2(7) <=> Ar + H(4) + H(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.176e+18, 'cm^3/(mol*s)'),
        n = -1.1,
        Ea = (104.39, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "CH4(1) + H(4) <=> H2(7) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (478100, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (9.588, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "O2(2) + H(4) <=> O(5) + OH(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.286, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 10,
    label = "O(5) + H2(7) <=> H(4) + OH(6)",
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
)

entry(
    index = 11,
    label = "O(5) + HO2(9) <=> O2(2) + OH(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-0.724, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "O(5) + O(5) <=> O2(2)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0},
    ),
)

entry(
    index = 13,
    label = "H(4) + O(5) <=> OH(6)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.714e+18, 'cm^6/(mol^2*s)'),
            n = -1,
            Ea = (0, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, 'O=C=O': 3.8, 'O': 12, '[Ar]': 0.75},
    ),
)

entry(
    index = 14,
    label = "Ar + O(5) + O(5) <=> O2(2) + Ar",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.89e+13, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (-1.788, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 15,
    label = "CH4(1) + O(5) <=> OH(6) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (8.485, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 16,
    label = "O(5) + OH(6) <=> HO2(9)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.839e+18, 'cm^3/(mol*s)'),
                n = -2.707,
                Ea = (1.085, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.621e+18, 'cm^3/(mol*s)'),
                n = -2.701,
                Ea = (1.141, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.566e+19, 'cm^3/(mol*s)'),
                n = -2.693,
                Ea = (1.217, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 17,
    label = "OH(6) + H2(7) <=> H(4) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3.43, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 18,
    label = "OH(6) + OH(6) <=> O(5) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33400, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (-1.93, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 19,
    label = "H2O(8) + H2O(8) <=> H(4) + OH(6) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.006e+26, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120.18, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "OH(6) + HO2(9) <=> O2(2) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 21,
    label = "H2O(8) <=> H(4) + OH(6)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.064e+27, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120.79, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 3, 'O=C=O': 3.8, '[O][O]': 1.5, 'O': 0, 'N#N': 2},
    ),
)

entry(
    index = 22,
    label = "H(4) + HO2(9) <=> O(5) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.632e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "CH4(1) + OH(6) <=> H2O(8) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (983900, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2.446, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "O(5) + CH3(18) <=> H(4) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.722e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "OH(6) + CH3(18) <=> H2(7) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.735e+09, 'cm^3/(mol*s)'),
        n = 0.734,
        Ea = (-2.177, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 26,
    label = "O2(2) + CH3(18) <=> OH(6) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (99.77, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (9.768, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "HO2(9) + HO2(9) <=> O2(2) + H2O2(10)",
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
    index = 28,
    label = "H(4) + H2O2(10) <=> OH(6) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3.97, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "H(4) + H2O2(10) <=> H2(7) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(7.95, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "O(5) + H2O2(10) <=> OH(6) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3.97, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "OH(6) + H2O2(10) <=> H2O(8) + HO2(9)",
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
    index = 32,
    label = "H2O2(10) <=> OH(6) + OH(6)",
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
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.5, '[H][H]': 3.7, '[O][O]': 1.2, 'N#N': 1.5},
    ),
)

entry(
    index = 33,
    label = "CH4(1) + HO2(9) <=> H2O2(10) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47780, 'cm^3/(mol*s)'), n=2.5, Ea=(21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "H(4) + HO2(9) <=> H2O2(10)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.628e+27, 'cm^3/(mol*s)'),
                n = -4.744,
                Ea = (6.375, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.181e+27, 'cm^3/(mol*s)'),
                n = -4.613,
                Ea = (6.604, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.397e+27, 'cm^3/(mol*s)'),
                n = -4.454,
                Ea = (6.787, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 35,
    label = "CH3O(26) <=> H(4) + CH2O(19)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.13e+10, 's^-1'), n=1.21, Ea=(24.075, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (6.02e+16, 'cm^3/(mol*s)'),
            n = -0.547,
            Ea = (18.024, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.341,
        T3 = (28, 'K'),
        T1 = (1000, 'K'),
        T2 = (2340, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'O': 6, 'C=O': 2.5, '[H][H]': 2, '[Ar]': 0.85},
    ),
)

entry(
    index = 36,
    label = "CH3O(26) + H(4) <=> H2(7) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.79e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.596, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "CH3O(26) + H(4) <=> OH(6) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.88e+14, 'cm^3/(mol*s)'),
        n = -0.264,
        Ea = (-0.026, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 38,
    label = "CH3O(26) + O(5) <=> OH(6) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.78e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "CH3O(26) + OH(6) <=> H2O(8) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "O2(2) + CH3O(26) <=> HO2(9) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.32e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.603, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 41,
    label = "CH3O(26) + CH3(18) <=> CH4(1) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "O2(2) + CH3(18) <=> CH3O(26) + O(5)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.333e+07, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (27.064, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.337e+07, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (27.065, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.344e+07, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (27.066, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 43,
    label = "O(5) + CH3(18) <=> CH3O(26)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1.239e+32, 'cm^3/(mol*s)'),
                n = -5.77,
                Ea = (9.721, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2.871e+31, 'cm^3/(mol*s)'),
                n = -5.535,
                Ea = (9.72, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.782e+30, 'cm^3/(mol*s)'),
                n = -5.262,
                Ea = (9.633, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 44,
    label = "CH3O(26) + HO2(9) <=> H2O2(10) + CH2O(19)",
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
    index = 45,
    label = "CH3O(26) + H(4) <=> CH2OH(32) + H(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.29e+07, 'cm^3/(mol*s)'),
        n = 1.82,
        Ea = (-0.703, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 46,
    label = "CH2OH(32) <=> H(4) + CH2O(19)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'O': 5.97, 'C=O': 2.5, '[H][H]': 2, '[Ar]': 0.85},
    ),
)

entry(
    index = 47,
    label = "CH2OH(32) + H(4) <=> H2(7) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "CH2OH(32) + H(4) <=> OH(6) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.006e+13, 'cm^3/(mol*s)'),
        n = 0.198,
        Ea = (-0.241, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 49,
    label = "CH2OH(32) + O(5) <=> OH(6) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.03e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 50,
    label = "CH2OH(32) + OH(6) <=> H2O(8) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "O2(2) + CH2OH(32) <=> HO2(9) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.298e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.736, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 52,
    label = "CH2OH(32) + CH3(18) <=> CH4(1) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "CH3O(26) <=> CH2OH(32)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(A=(9.535e+16, 's^-1'), n=-2.019, Ea=(22.891, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.058e+17, 's^-1'), n=-2.083, Ea=(23.665, 'kcal/mol'), T0=(1, 'K')),
            Arrhenius(A=(9.176e+17, 's^-1'), n=-2.139, Ea=(24.486, 'kcal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 54,
    label = "CH2OH(32) + HO2(9) <=> H2O2(10) + CH2O(19)",
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
    index = 55,
    label = "HO2(9) + CH3(18) <=> CH3O(26) + OH(6)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (4.176e+13, 'cm^3/(mol*s)'),
                n = -0.155,
                Ea = (0.355, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.351e+13, 'cm^3/(mol*s)'),
                n = -0.16,
                Ea = (0.375, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.669e+13, 'cm^3/(mol*s)'),
                n = -0.168,
                Ea = (0.41, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 56,
    label = "H(4) + HCO(14) <=> CH2O(19)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.84, '[Ar]': 0.79},
    ),
)

entry(
    index = 57,
    label = "H(4) + CH2O(19) <=> H2(7) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.149e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2.742, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 58,
    label = "O(5) + CH2O(19) <=> OH(6) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.244e+11, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2.762, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 59,
    label = "OH(6) + CH2O(19) <=> H2O(8) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.338e+07, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 60,
    label = "O2(2) + CH2O(19) <=> HO2(9) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (329700, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (36.46, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 61,
    label = "HO2(9) + CH2O(19) <=> H2O2(10) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71110, 'cm^3/(mol*s)'), n=2.5, Ea=(10.21, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 62,
    label = "CH3(18) + CH2O(19) <=> CH4(1) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32.13, 'cm^3/(mol*s)'), n=3.36, Ea=(4.31, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "CH3O(26) + HCO(14) <=> CH2O(19) + CH2O(19)",
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
    index = 64,
    label = "CH2OH(32) + HCO(14) <=> CH2O(19) + CH2O(19)",
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
    index = 65,
    label = "HCO(14) <=> H(4) + CO(12)",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.8e+17, 'cm^3/(mol*s)'),
            n = -1.2,
            Ea = (17.734, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.6, 'O=C=O': 2, 'CC': 3, 'O': 15.31, 'C=O': 3.29, '[H][H]': 1.31, '[O][O]': 1.32, 'N#N': 1.31, '[Ar]': 1.4},
    ),
)

entry(
    index = 66,
    label = "H(4) + HCO(14) <=> H2(7) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.482e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "O(5) + HCO(14) <=> OH(6) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "OH(6) + HCO(14) <=> H2O(8) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.199e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 69,
    label = "O2(2) + HCO(14) <=> HO2(9) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.562e+10, 'cm^3/(mol*s)'),
        n = 0.521,
        Ea = (-0.521, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 70,
    label = "CH2O(19) <=> H2(7) + CO(12)",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+13, 's^-1'), n=0, Ea=(71.976, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.4e+38, 'cm^3/(mol*s)'), n=-6.1, Ea=(94, 'kcal/mol'), T0=(1, 'K')),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 71,
    label = "O(5) + CH3(18) <=> H(4) + H2(7) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.384e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "HCO(14) + CH3(18) <=> CH4(1) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 73,
    label = "CH2(S)(24) + O(5) <=> H(4) + H(4) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 74,
    label = "CH2(S)(24) + OH(6) <=> H(4) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 75,
    label = "CH2(S)(24) + H2(7) <=> H(4) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.291e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 76,
    label = "CH2(S)(24) + H2O(8) <=> H2(7) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.67e+21, 'cm^3/(mol*s)'),
        n = -3.134,
        Ea = (3.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 77,
    label = "CH2(S)(24) + H2O2(10) <=> CH3O(26) + OH(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.29e+14, 'cm^3/(mol*s)'),
        n = -0.138,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 78,
    label = "CH2(S)(24) + CH2O(19) <=> HCO(14) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.33e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.55, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 79,
    label = "OH(6) + CH3(18) <=> CH2(S)(24) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.81e+15, 'cm^3/(mol*s)'),
        n = -0.91,
        Ea = (0.546, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 80,
    label = "CH3O(26) + H(4) <=> CH2(S)(24) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+11, 'cm^3/(mol*s)'),
        n = 0.414,
        Ea = (0.243, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 81,
    label = "CH2OH(32) + H(4) <=> CH2(S)(24) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+11, 'cm^3/(mol*s)'),
        n = 0.516,
        Ea = (0.215, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 82,
    label = "CH4(1) + CH2(S)(24) <=> CH3(18) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.867e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 83,
    label = "CH2(S)(24) + H2(7) <=> CH4(1)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.591e+31, 'cm^3/(mol*s)'),
                n = -5.659,
                Ea = (10.305, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.705e+31, 'cm^3/(mol*s)'),
                n = -5.451,
                Ea = (10.511, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.179e+30, 'cm^3/(mol*s)'),
                n = -5.187,
                Ea = (10.576, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 84,
    label = "O2(2) + CH3(18) <=> CH2(S)(24) + HO2(9)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9.778e+09, 'cm^3/(mol*s)'),
                n = 1.033,
                Ea = (68.889, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.778e+09, 'cm^3/(mol*s)'),
                n = 1.033,
                Ea = (68.889, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9.78e+09, 'cm^3/(mol*s)'),
                n = 1.033,
                Ea = (68.889, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 85,
    label = "HO2(9) + CH3(18) <=> CH2(S)(24) + H2O2(10)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (9017, 'cm^3/(mol*s)'),
                n = 2.374,
                Ea = (29.439, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9073, 'cm^3/(mol*s)'),
                n = 2.373,
                Ea = (29.442, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (9172, 'cm^3/(mol*s)'),
                n = 2.372,
                Ea = (29.447, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 86,
    label = "CH3(18) + CH2O(19) <=> CH2(S)(24) + CH2OH(32)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.846e+09, 'cm^3/(mol*s)'),
                n = 1.304,
                Ea = (88.487, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.846e+09, 'cm^3/(mol*s)'),
                n = 1.304,
                Ea = (88.487, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.846e+09, 'cm^3/(mol*s)'),
                n = 1.304,
                Ea = (88.487, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 87,
    label = "CH3(18) + CH3(18) <=> C2H6(30)",
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
        efficiencies = {'C': 1.99, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[O][O]': 1, '[Ar]': 0.69},
    ),
)

entry(
    index = 88,
    label = "CH3(18) + CH3(18) <=> C2H5(31) + H(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.621e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 89,
    label = "C2H5(31) + H(4) <=> C2H6(30)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 90,
    label = "C2H5(31) + O(5) <=> CH3(18) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.42e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 91,
    label = "C2H5(31) + CH2O(19) <=> C2H6(30) + HCO(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5.86, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 92,
    label = "C2H6(30) + H(4) <=> C2H5(31) + H2(7)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.133e+08, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7.53, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 93,
    label = "C2H6(30) + O(5) <=> C2H5(31) + OH(6)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (176300, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (5.803, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 94,
    label = "C2H6(30) + OH(6) <=> C2H5(31) + H2O(8)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.463e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (0.994, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 95,
    label = "CH2(S)(24) + C2H6(30) <=> C2H5(31) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+13, 'cm^3/(mol*s)'), n=0, Ea=(-0.66, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 96,
    label = "C2H6(30) + CH3(18) <=> CH4(1) + C2H5(31)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+10, 'cm^3/(mol*s)'), n=0, Ea=(9.42, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 97,
    label = "O2(2) + C2H6(30) <=> C2H5(31) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (729000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (49.16, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 98,
    label = "C2H6(30) + HO2(9) <=> C2H5(31) + H2O2(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (16.85, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 99,
    label = "CH3O(26) + C2H5(31) <=> C2H6(30) + CH2O(19)",
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
    index = 100,
    label = "C2H5(31) + CH2OH(32) <=> C2H6(30) + CH2O(19)",
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
    index = 101,
    label = "CH4(1) + CH2(S)(24) <=> C2H6(30)",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.493, 0.855, 1.48], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3.743e+46, 'cm^3/(mol*s)'),
                n = -9.457,
                Ea = (23.929, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6.95e+42, 'cm^3/(mol*s)'),
                n = -8.378,
                Ea = (21.653, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7.492e+38, 'cm^3/(mol*s)'),
                n = -7.239,
                Ea = (19.089, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 102,
    label = "CH2(S)(24) + CH3(18) <=> C2H4(29) + H(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.497, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 103,
    label = "C2H4(29) + H(4) <=> C2H5(31)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 4.92, 'C=O': 2.5, 'N#N': 0.86, '[Ar]': 0.7},
    ),
)

entry(
    index = 104,
    label = "C2H4(29) + O(5) <=> HCO(14) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.355e+06, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (0.183, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 105,
    label = "C2H4(29) + OH(6) <=> CH3(18) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178000, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2.06, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 106,
    label = "C2H5(31) + H(4) <=> C2H4(29) + H2(7)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.81e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 107,
    label = "C2H5(31) + O(5) <=> C2H4(29) + OH(6)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.94e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 108,
    label = "O2(2) + C2H5(31) <=> C2H4(29) + HO2(9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.355e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1.975, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 109,
    label = "C2H5(31) + CH3(18) <=> CH4(1) + C2H4(29)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+11, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 110,
    label = "C2H5(31) + HO2(9) <=> C2H4(29) + H2O2(10)",
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
    index = 111,
    label = "C2H5(31) + OH(6) <=> C2H4(29) + H2O(8)",
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
    index = 112,
    label = "C2H5(31) + HCO(14) <=> C2H4(29) + CH2O(19)",
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
    index = 113,
    label = "C2H5(31) + C2H5(31) <=> C2H4(29) + C2H6(30)",
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
    index = 114,
    label = "H(4) + CH2(17) <=> CH3(18)",
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
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 6, 'C=O': 2.5, '[Ar]': 0.7},
    ),
)

entry(
    index = 115,
    label = "O(5) + CH2(17) <=> H(4) + H(4) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 116,
    label = "OH(6) + CH2(17) <=> H(4) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.899e+13, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (-0.162, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 117,
    label = "HO2(9) + CH2(17) <=> OH(6) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 118,
    label = "H2(7) + CH2(17) <=> H(4) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.265e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7.23, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 119,
    label = "O2(2) + CH2(17) <=> H(4) + OH(6) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.643e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 120,
    label = "O2(2) + CH2(17) <=> O(5) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 121,
    label = "O2(2) + CH2(17) <=> H2O(8) + CO(12)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 122,
    label = "N2(3) + CH2(S)(24) <=> N2(3) + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(0.471, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 123,
    label = "Ar + CH2(S)(24) <=> Ar + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 124,
    label = "O2(2) + CH2(S)(24) <=> O2(2) + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 125,
    label = "CH2(S)(24) + H2O(8) <=> H2O(8) + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.431, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 126,
    label = "CH2(S)(24) + CO(12) <=> CO(12) + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 127,
    label = "CH2(17) + CH2O(19) <=> HCO(14) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.074, 'cm^3/(mol*s)'), n=4.21, Ea=(1.12, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 128,
    label = "OH(6) + CH3(18) <=> H2O(8) + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44640, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (3.998, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 129,
    label = "CH2(17) + CH3(18) <=> C2H4(29) + H(4)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.824e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 130,
    label = "CH4(1) + CH2(17) <=> CH3(18) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.483e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 131,
    label = "C2H4(29) + O(5) <=> CH2(17) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.62,
        Ea = (0.459, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 132,
    label = "HO2(9) + CH2(17) <=> O2(2) + CH3(18)",
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
Estimated using template [X_H;CH2_triplet] for rate rule [Orad_O_H;CH2_triplet]
""",
)

entry(
    index = 133,
    label = "H2O2(10) + CH2(17) <=> HO2(9) + CH3(18)",
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
Estimated using average of templates [O_sec;CH2_triplet] + [H2O2;Y_rad_birad_trirad_quadrad] for rate rule [H2O2;CH2_triplet]
Multiplied by reaction path degeneracy 2
""",
)

entry(
    index = 134,
    label = "OH(6) + CH2(17) <=> O(5) + CH3(18)",
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
Estimated using template [Xrad_H;Y_1centerbirad] for rate rule [OH_rad_H;CH2_triplet]
""",
)

entry(
    index = 135,
    label = "CH3O(26) + CH2(17) <=> CH3(18) + CH2O(19)",
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
Estimated using template [CH2_triplet;Cmethyl_Rrad] for rate rule [CH2_triplet;Cmethyl_Orad]
Multiplied by reaction path degeneracy 3
""",
)

entry(
    index = 136,
    label = "CH2OH(32) + CH2(17) <=> CH3(18) + CH2O(19)",
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
Exact match found for rate rule [CH2_triplet;O_Csrad]
""",
)

entry(
    index = 137,
    label = "C2H6(30) + CH2(17) <=> C2H5(31) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5700, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (3.123, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Estimated using template [C/H3/Cs;Y_1centerbirad] for rate rule [C/H3/Cs\\H3;CH2_triplet]\nMultiplied by reaction path degeneracy 6',
    ),
    longDesc = 
u"""
Estimated using template [C/H3/Cs;Y_1centerbirad] for rate rule [C/H3/Cs\H3;CH2_triplet]
Multiplied by reaction path degeneracy 6
""",
)

entry(
    index = 138,
    label = "C2H5(31) + CH2(17) <=> C2H4(29) + CH3(18)",
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
    index = 139,
    label = "O(5) + CO(12) <=> CO2(13)",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.88e+11, 'cm^3/(mol*s)'), n=0, Ea=(2.43, 'kcal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.4e+21, 'cm^6/(mol^2*s)'),
            n = -2.1,
            Ea = (5.5, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 3.8, 'CC': 3, 'O': 12, 'C=O': 2.5, '[Ar]': 0.87},
    ),
)

entry(
    index = 140,
    label = "O2(2) + CO(12) <=> O(5) + CO2(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.533e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 141,
    label = "OH(6) + CO(12) <=> H(4) + CO2(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (61870, 'cm^3/(mol*s)'),
        n = 2.053,
        Ea = (-0.356, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 142,
    label = "HO2(9) + CO(12) <=> OH(6) + CO2(13)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17.944, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 143,
    label = "O(5) + HCO(14) <=> H(4) + CO2(13)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.001e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 144,
    label = "O2(2) + CH2(17) <=> H(4) + H(4) + CO2(13)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.844e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 145,
    label = "O2(2) + CH2(17) <=> H2(7) + CO2(13)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.836e+12, 'cm^3/(mol*s)'), n=0, Ea=(1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 146,
    label = "CH2(S)(24) + CO2(13) <=> CO2(13) + CH2(17)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.33e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 147,
    label = "CH2(S)(24) + CO2(13) <=> CO(12) + CH2O(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 148,
    label = "CH3O(26) + CO(12) <=> CO2(13) + CH3(18)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+12, 'cm^3/(mol*s)'), n=0, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
)

