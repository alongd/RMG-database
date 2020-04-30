#!/usr/bin/env python
# encoding: utf-8

name = "imipramine"
shortDesc = ""
longDesc = """
Calculated using Arkane v2.4.1.

Indices are 1-indexed, corresponding to the following atom order of imipramine:

 N                 -0.41896200   -0.36217300    0.15079800
 C                  0.67703300   -1.31207300    0.24065900
 C                 -1.69738700   -0.89208400   -0.14606600
 C                  1.66095700   -0.97669700    1.36305100
 H                  0.22869600   -2.29680100    0.43686000
 H                  1.23387500   -1.40954800   -0.71088800
 C                 -0.11923100    0.98017700   -0.17756800
 C                 -1.85821200   -1.89672400   -1.11002700
 C                 -2.81408800   -0.43084900    0.57095900
 C                  3.02392400   -1.61241200    1.11405300
 H                  1.76909700    0.11590200    1.45059300
 H                  1.25551300   -1.31634900    2.33029500
 C                  1.09560300    1.25437500   -0.84079000
 C                 -0.96883300    2.06665400    0.14806900
 C                 -3.11741800   -2.43785500   -1.36445100
 H                 -0.98961500   -2.24579400   -1.67354100
 C                 -2.60518200    0.65073700    1.58303300
 C                 -4.07248300   -0.96887000    0.29087700
 N                  3.70926800   -1.02031200   -0.02150800
 H                  2.88192300   -2.68613100    0.90264700
 H                  3.64800500   -1.56476800    2.03517000
 C                  1.46642500    2.54790300   -1.18998200
 H                  1.77374100    0.43333700   -1.08001200
 C                 -2.27793600    1.97993800    0.90617700
 C                 -0.57482500    3.35569600   -0.23775900
 C                 -4.23152500   -1.97135600   -0.66630200
 H                 -3.22882700   -3.21920500   -2.12144900
 H                 -3.50837700    0.77096800    2.20110100
 H                 -1.77826600    0.36721600    2.25643900
 H                 -4.94021600   -0.60533600    0.85025400
 C                  4.65844500   -1.91295700   -0.63847500
 C                  4.30162200    0.25903100    0.28866000
 C                  0.62145500    3.61645300   -0.89783900
 H                  2.41954000    2.71361700   -1.70035200
 H                 -2.27465100    2.78154400    1.66492200
 H                 -3.10469500    2.22874400    0.21612500
 H                 -1.23832100    4.18953000    0.01478300
 H                 -5.22216200   -2.38919800   -0.86441700
 H                  5.08970600   -1.44267400   -1.53578800
 H                  5.50365300   -2.19049300    0.03204500
 H                  4.16045700   -2.84206100   -0.95546800
 H                  4.69764300    0.72480500   -0.62690300
 H                  5.13755400    0.18021600    1.02076000
 H                  3.55058800    0.94559900    0.70354300
 H                  0.89294200    4.63975000   -1.16941000
"""

entry(
    index = 0,
    label = "imipramine + CH3OO <=> imipramine_rad_5 + CH3OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.93207e-12,'cm^3/(mol*s)'), n=7.03045, Ea=(40.3569,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.4981, dn = +|- 0.0589796, dEa = +|- 0.168034 kJ/mol"""),
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
    kinetics = Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'),
                         T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'),
                         comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
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
    kinetics = Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
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
    kinetics = Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
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
    kinetics = Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
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





entry(
    index = 10,
    label = "imipramine + HO2 <=> imipramine_rad_5 + H2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.93207e-12,'cm^3/(mol*s)'), n=7.03045, Ea=(40.3569,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.4981, dn = +|- 0.0589796, dEa = +|- 0.168034 kJ/mol"""),
    shortDesc = u"""k5+k6""",
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
    kinetics = Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    # kinetics = MultiArrhenius(
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
    kinetics = Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    # kinetics = MultiArrhenius(
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
    kinetics = Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
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
    index = 14,
    label = "imipramine + HO2 <=> imipramine_rad_39 + H2O2",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
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



entry(
    index = 20,
    label = "imipramine + OHCH2OO <=> imipramine_rad_5 + OHCH2OOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.93207e-12,'cm^3/(mol*s)'), n=7.03045, Ea=(40.3569,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.4981, dn = +|- 0.0589796, dEa = +|- 0.168034 kJ/mol"""),
    shortDesc = u"""k5+k6""",
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
    kinetics = Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    # kinetics = MultiArrhenius(
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
    kinetics = Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    # kinetics = MultiArrhenius(
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
    kinetics = Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
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
    index = 24,
    label = "imipramine + OHCH2OO <=> imipramine_rad_39 + OHCH2OOH",
    degeneracy = 6.0,
    # duplicate = True,
    kinetics = Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'), T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
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



entry(
    index = 25,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_5 + cyanoisopropylOOH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.93207e-12,'cm^3/(mol*s)'), n=7.03045, Ea=(40.3569,'kJ/mol'),
                         T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""Fitted to 100 data points; dA = *|/ 1.4981, dn = +|- 0.0589796, dEa = +|- 0.168034 kJ/mol"""),
    longDesc =
u"""
copied over, not calculated!!
""",
)

entry(
    index = 26,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_11 + cyanoisopropylOOH",
    kinetics = Arrhenius(A=(1.1882e-10,'cm^3/(mol*s)'), n=6.39356, Ea=(55.874,'kJ/mol'),
                         T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k11, Fitted to 100 data points; dA = *|/ 1.14786, dn = +|- 0.020122, dEa = +|- 0.057328 kJ/mol"""),
    shortDesc = u"""k11+k12""",
)

entry(
    index = 27,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_20 + cyanoisopropylOOH",
    kinetics = Arrhenius(A=(1.60144e-12,'cm^3/(mol*s)'), n=7.44743, Ea=(61.7556,'kJ/mol'),
                         T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k20, Fitted to 100 data points; dA = *|/ 1.76345, dn = +|- 0.0827744, dEa = +|- 0.235826 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 28,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_28 + cyanoisopropylOOH",
    kinetics = Arrhenius(A=(1.69879e-49,'cm^3/(mol*s)'), n=19.1594, Ea=(17.7046,'kJ/mol'),
                         T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k28, Fitted to 100 data points; dA = *|/ 12.2045, dn = +|- 0.365056, dEa = +|- 1.04005 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)

entry(
    index = 29,
    label = "imipramine + cyanoisopropylOO <=> imipramine_rad_39 + cyanoisopropylOOH",
    kinetics = Arrhenius(A=(1.04937e-08,'cm^3/(mol*s)'), n=5.94011, Ea=(48.883,'kJ/mol'),
                         T0=(1,'K'), Tmin=(250,'K'), Tmax=(500,'K'), comment="""k41, Fitted to 100 data points; dA = *|/ 1.32039, dn = +|- 0.0405538, dEa = +|- 0.115539 kJ/mol"""),
    longDesc=
    u"""
    copied over, not calculated!!
    """,
)
