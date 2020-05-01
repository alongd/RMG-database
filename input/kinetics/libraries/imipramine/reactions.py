#!/usr/bin/env python
# encoding: utf-8

name = "imipramine"
shortDesc = ""
longDesc = """
Calculated using Arkane v2.4.1.

Indices are 1-indexed, corresponding to the following atom order of imipramine:

 N                 -0.00634640   -0.33884115    0.59014543
 C                  1.34971160   -0.59332915    0.28011243
 C                 -0.33884640    1.02531185    0.80935343
 C                  1.90724860   -1.99720215    0.28906443
 H                  1.54683540   -0.24043385   -0.74445243
 H                  2.01383960    0.10240385    0.81678743
 C                 -1.04087840   -1.29842115    0.44492743
 C                  0.01734260    1.63227285    2.01649843
 C                 -0.96251440    1.76363785   -0.20843657
 C                  3.36262660   -1.96925415   -0.18238057
 H                  1.84605060   -2.43910815    1.30009143
 H                  1.31932360   -2.66123715   -0.36605157
 C                 -0.98498540   -2.42954315    1.27978143
 C                 -2.12109040   -1.15216515   -0.45091657
 C                 -0.25921040    2.98164885    2.22905943
 H                  0.51102860    1.03046785    2.78373243
 C                 -1.27502340    1.08404885   -1.50705857
 C                 -1.25012340    3.11152385    0.02862343
 N                  4.20026960   -1.13768215    0.65915443
 H                  3.38114260   -1.55505415   -1.20088257
 H                  3.75199360   -3.00993915   -0.25151957
 C                 -1.94181640   -3.43312815    1.21393843
 H                 -0.17359640   -2.49346015    2.00576243
 C                 -2.36378440    0.02234685   -1.37389557
 C                 -3.08445640   -2.17367815   -0.48437757
 C                 -0.90050640    3.72118885    1.23368643
 H                  0.01841160    3.45358985    3.17527243
 H                 -1.60779740    1.83365885   -2.24172757
 H                 -0.34933940    0.64413985   -1.91332857
 H                 -1.73933540    3.69591885   -0.75661957
 C                  5.30282460   -0.53382415   -0.04745657
 C                  4.60551260   -1.78583115    1.87822243
 C                 -3.00436540   -3.30587615    0.31758043
 H                 -1.86875240   -4.30196615    1.87337043
 H                 -2.58743840   -0.38168415   -2.37611257
 H                 -3.29548040    0.51591885   -1.04184457
 H                 -3.92342640   -2.06790415   -1.17971757
 H                 -1.12568540    4.77886885    1.39528643
 H                  5.84454960    0.15200385    0.62333943
 H                  6.04077360   -1.27564415   -0.43015257
 H                  4.92157960    0.05386585   -0.89461757
 H                  5.12651860   -1.07235215    2.53562043
 H                  5.28861260   -2.65058115    1.70831543
 H                  3.73034460   -2.16058715    2.43060043
 H                 -3.77247840   -4.08092015    0.25152943
"""

# imipramine + CH3OO updated to two para arrhenius fit (same as in training reaction)

entry(
    index = 0,
    label = "imipramine + CH3OO <=> imipramine_rad_5 + CH3OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.13218e+09,'cm^3/(mol*s)'), n=0, Ea=(58.5589,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.02664, dn = +|- 0, 
                         dEa = +|- 0.0671562 kJ/mol"""),
    shortDesc = u"""k5+k6""",
    longDesc =
u"""
H6 is blocked, H5 and H6 have the same 2D connectivity
k6 = 0  =>  k5 + k6 = k5
""",
)

entry(
    index = 1,
    label = "imipramine + CH3OO <=> imipramine_rad_11 + CH3OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.18283e+09,'cm^3/(mol*s)'), n=0, Ea=(71.1023,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00034, dn = +|- 0, 
                         dEa = +|- 0.000870252 kJ/mol"""),
    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 2,
    label = "imipramine + CH3OO <=> imipramine_rad_20 + CH3OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(1.11619e+10, 'cm^3/(mol*s)'), n=0, Ea=(52.9458, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00001, dn = +|- 0, 
                     dEa = +|- 1.85328e-05 kJ/mol"""),
    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k20+k21""",
)

entry(
    index = 3,
    label = "imipramine + CH3OO <=> imipramine_rad_28 + CH3OOH",
    degeneracy = 4.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(3.18843e+07, 'cm^3/(mol*s)'), n=0, Ea=(35.8139, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00148, dn = +|- 0, 
                     dEa = +|- 0.00380887 kJ/mol"""),
    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
    #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
    #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k28+k29+k35+k36""",
)

entry(
    index = 4,
    label = "imipramine + CH3OO <=> imipramine_rad_39 + CH3OOH",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(8.81896e+09, 'cm^3/(mol*s)'), n=0, Ea=(56.8704, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00345, dn = +|- 0, 
                     dEa = +|- 0.00889234 kJ/mol"""),
#     kinetics = MultiArrhenius(
# #        arrhenius = [
# #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #        ],
#         arrhenius = [
#             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
#             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
#             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
#             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
#             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
#             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
#         ],
#     ),
    shortDesc = u"""k39+k40+k41+k42+k43+k44""",
    longDesc =
u"""
Here rotors we not included in the calculation (Eventually we'd like to use rotors).
We're definitely missing a factor of x3 of the torsion missing in the TS,
we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
""",
)



# imipramine + HO2 copied from CH3OO

entry(
    index = 10,
    label = "imipramine + HO2 <=> imipramine_rad_5 + H2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.13218e+09,'cm^3/(mol*s)'), n=0, Ea=(58.5589,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.02664, dn = +|- 0, 
                         dEa = +|- 0.0671562 kJ/mol"""),    shortDesc = u"""k5+k6""",
    longDesc =
u"""
H6 is blocked, H5 and H6 have the same 2D connectivity
k6 = 0  =>  k5 + k6 = k5
""",
)

entry(
    index = 11,
    label = "imipramine + HO2 <=> imipramine_rad_11 + H2O2",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.18283e+09,'cm^3/(mol*s)'), n=0, Ea=(71.1023,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00034, dn = +|- 0, 
                         dEa = +|- 0.000870252 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 12,
    label = "imipramine + HO2 <=> imipramine_rad_20 + H2O2",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(1.11619e+10, 'cm^3/(mol*s)'), n=0, Ea=(52.9458, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00001, dn = +|- 0, 
                     dEa = +|- 1.85328e-05 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k20+k21""",
)

entry(
    index = 13,
    label = "imipramine + HO2 <=> imipramine_rad_28 + H2O2",
    degeneracy = 4.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(3.18843e+07, 'cm^3/(mol*s)'), n=0, Ea=(35.8139, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00148, dn = +|- 0, 
                     dEa = +|- 0.00380887 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
    #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
    #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k28+k29+k35+k36""",
)

entry(
    index = 14,
    label = "imipramine + HO2 <=> imipramine_rad_39 + H2O2",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics=Arrhenius(A=(8.81896e+09, 'cm^3/(mol*s)'), n=0, Ea=(56.8704, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00345, dn = +|- 0, 
                     dEa = +|- 0.00889234 kJ/mol"""),#     kinetics = MultiArrhenius(
# #        arrhenius = [
# #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #        ],
#         arrhenius = [
#             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
#             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
#             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
#             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
#             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
#             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
#         ],
#     ),
    shortDesc = u"""k39+k40+k41+k42+k43+k44""",
    longDesc =
u"""
Here rotors we not included in the calculation (Eventually we'd like to use rotors).
We're definitely missing a factor of x3 of the torsion missing in the TS,
we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
""",
)

# imipramine + OHCH2OO updated to two para arrhenius fit (same as in training reaction)


entry(
    index = 20,
    label = "imipramine + OHCH2OO <=> imipramine_rad_5 + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0, 
                         dEa = +|- 0.000483392 kJ/mol"""),    shortDesc = u"""k5+k6""",
    longDesc =
u"""
H6 is blocked, H5 and H6 have the same 2D connectivity
k6 = 0  =>  k5 + k6 = k5
""",
)

entry(
    index = 21,
    label = "imipramine + OHCH2OO <=> imipramine_rad_11 + OHCH2OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(3.94097e+07,'cm^3/(mol*s)'), n=0, Ea=(56.0508,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0, 
                         dEa = +|- 0.000364259 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    #         # Arrhenius(A=(2.92217e-08,'cm^3/(mol*s)'), n=5.58651, Ea=(56.1606,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.08935, dn = +|- 0.0124883, dEa = +|- 0.0355794 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 22,
    label = "imipramine + OHCH2OO <=> imipramine_rad_20 + OHCH2OOH",
    degeneracy = 2.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.32296e+09,'cm^3/(mol*s)'), n=0, Ea=(41.7324,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0, 
                         dEa = +|- 4.59316e-05 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    #         # Arrhenius(A=(7.00398e-09,'cm^3/(mol*s)'), n=6.21963, Ea=(36.9099,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k21, Fitted to 100 data points; dA = *|/ 1.21987, dn = +|- 0.0290001, dEa = +|- 0.082622 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k20+k21""",
)

entry(
    index = 23,
    label = "imipramine + OHCH2OO <=> imipramine_rad_28 + OHCH2OOH",
    degeneracy = 4.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(4.7123e+06,'cm^3/(mol*s)'), n=0, Ea=(24.1853,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0, 
                         dEa = +|- 0.000717396 kJ/mol"""),    # kinetics = MultiArrhenius(
    #     arrhenius = [
    #         Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    #         # Arrhenius(A=(2.45476e-50,'cm^3/(mol*s)'), n=19.5114, Ea=(-0.427648,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k29, Fitted to 100 data points; dA = *|/ 6.32046, dn = +|- 0.269041, dEa = +|- 0.766504 kJ/mol"""),
    #         # Arrhenius(A=(3.37035e-33,'cm^3/(mol*s)'), n=13.5841, Ea=(7.70763,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k35, Fitted to 100 data points; dA = *|/ 3.55447, dn = +|- 0.185053, dEa = +|- 0.52722 kJ/mol"""),
    #         # Arrhenius(A=(5.01589e-29,'cm^3/(mol*s)'), n=12.198, Ea=(3.83956,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k36, Fitted to 100 data points; dA = *|/ 2.54252, dn = +|- 0.136163, dEa = +|- 0.387932 kJ/mol"""),
    #     ],
    # ),
    shortDesc = u"""k28+k29+k35+k36""",
)

entry(
    index = 24,
    label = "imipramine + OHCH2OO <=> imipramine_rad_39 + OHCH2OOH",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(2.1327e+09,'cm^3/(mol*s)'), n=0, Ea=(46.4329,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0, 
                         dEa = +|- 0.00509461 kJ/mol"""),#     kinetics = MultiArrhenius(
# #        arrhenius = [
# #            Arrhenius(A=(1.157e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
# #            Arrhenius(A=(2.63341e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
# #            Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
# #            Arrhenius(A=(9.88708e-07,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
# #            Arrhenius(A=(7.2759e-10,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
# #            Arrhenius(A=(1.27688e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
# #        ],
#         arrhenius = [
#             # Arrhenius(A=(3.471e-08,'cm^3/(mol*s)'), n=5.92189, Ea=(46.0794,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k39, Fitted to 100 data points; dA = *|/ 1.28881, dn = +|- 0.0370219, dEa = +|- 0.105476 kJ/mol"""),
#             # Arrhenius(A=(7.900e-09,'cm^3/(mol*s)'), n=6.19955, Ea=(40.399,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k40, Fitted to 100 data points; dA = *|/ 1.24941, dn = +|- 0.0324912, dEa = +|- 0.092568 kJ/mol"""),
#             Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
#             # Arrhenius(A=(2.9661e-06,'cm^3/(mol*s)'), n=5.38234, Ea=(50.9583,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k42, Fitted to 100 data points; dA = *|/ 1.22207, dn = +|- 0.0292627, dEa = +|- 0.0833702 kJ/mol"""),
#             # Arrhenius(A=(2.1828e-9,'cm^3/(mol*s)'), n=6.39346, Ea=(42.8248,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k43, Fitted to 100 data points; dA = *|/ 1.27088, dn = +|- 0.0349779, dEa = +|- 0.0996527 kJ/mol"""),
#             # Arrhenius(A=(3.831e-07,'cm^3/(mol*s)'), n=5.36061, Ea=(39.9466,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k44, Fitted to 100 data points; dA = *|/ 1.09723, dn = +|- 0.0135395, dEa = +|- 0.0385744 kJ/mol"""),
#         ],
#     ),
    shortDesc = u"""k39+k40+k41+k42+k43+k44""",
    longDesc =
u"""
Here rotors we not included in the calculation (Eventually we'd like to use rotors).
We're definitely missing a factor of x3 of the torsion missing in the TS,
we might be missing another factor of x3, depends whether the second methyl rotor is active in the TS or not (breaks it).
""",
)

# imipramine + cyanoisopropylOO copied from OHCH2OO


entry(
    index = 25,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_5 + cyanoisopropylOOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.2408e+08,'cm^3/(mol*s)'), n=0, Ea=(47.4742,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
                         Tmax=(350,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00019, dn = +|- 0, 
                         dEa = +|- 0.000483392 kJ/mol"""),
    longDesc =
u"""
copied over, not calculated!!
""",
)

entry(
    index = 26,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_11 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(3.94097e+07, 'cm^3/(mol*s)'), n=0, Ea=(56.0508, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00014, dn = +|- 0, 
                     dEa = +|- 0.000364259 kJ/mol"""),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 27,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_20 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(1.32296e+09, 'cm^3/(mol*s)'), n=0, Ea=(41.7324, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00002, dn = +|- 0, 
                     dEa = +|- 4.59316e-05 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 28,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_28 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(4.7123e+06, 'cm^3/(mol*s)'), n=0, Ea=(24.1853, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00028, dn = +|- 0, 
                     dEa = +|- 0.000717396 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 29,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_39 + cyanoisopropylOOH",
    kinetics=Arrhenius(A=(2.1327e+09, 'cm^3/(mol*s)'), n=0, Ea=(46.4329, 'kJ/mol'), T0=(1, 'K'), Tmin=(275, 'K'),
                       Tmax=(350, 'K'), comment="""Fitted to 100 data points; dA = *|/ 1.00198, dn = +|- 0, 
                     dEa = +|- 0.00509461 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)
