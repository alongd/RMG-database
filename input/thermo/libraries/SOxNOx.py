#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u"SOxNOx"
longDesc = u"""
"""


entry(
    index = 15,
    label = "NH(S)",
    molecule = 
"""
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.98,7.00,7.11,7.27,7.60,7.91,8.44],'cal/(mol*K)'),
        H298 = (120.9,'kcal/mol','+|-',0.5),
        S298 = (41.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 16,
    label = "NNOH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.44,11.42,12.25,13.10,14.32,15.15,16.68],'cal/(mol*K)'),
        H298 = (58.1,'kcal/mol','+|-',0.5),
        S298 = (61.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 17,
    label = "CH2NN",
    molecule = 
"""
1 C u0 p1 c-1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p0 c+1 {1,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.74,13.86,15.60,17.04,19.17,20.67,22.94],'cal/(mol*K)'),
        H298 = (68.5,'kcal/mol','+|-',0.5),
        S298 = (57.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazomethyl""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 18,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c-1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u0 p0 c+1 {1,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.78,12.19,13.40,14.29,15.68,16.56,17.71],'cal/(mol*K)'),
        H298 = (109.0,'kcal/mol','+|-',0.5),
        S298 = (59.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazomethyl radical""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 19,
    label = "HCN2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.00,12.02,13.00,13.81,15.30,16.09,17.59],'cal/(mol*K)'),
        H298 = (107.1,'kcal/mol','+|-',0.5),
        S298 = (57.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazirine radical""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 20,
    label = "CH2NNH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.29,17.21,18.24,19.79,25.19,29.11,32.34],'cal/(mol*K)'),
        H298 = (45.5,'kcal/mol','+|-',0.5),
        S298 = (63.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 21,
    label = "CH3NNH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.70,16.20,16.82,18.69,24.40,27.10,31.31],'cal/(mol*K)'),
        H298 = (42.8,'kcal/mol','+|-',0.5),
        S298 = (61.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)

entry(
    index = 22,
    label = "NCHOH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.50,14.24,15.80,17.16,19.17,20.46,22.39],'cal/(mol*K)'),
        H298 = (13.9,'kcal/mol','+|-',0.5),
        S298 = (62.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
doi: 10.1007/978-1-4612-1310-9_2
""",
)



















"""
check Burcat?
check GlarborgNS?
Add:
HOSO2
N2H3NO
HNNO2 - bad
H2NONO
NH2NHNO
NH2NHNO2
NH2NHONO
CH2N2 - radical, but no data for non-rad
CHN2 - same
cN2CH2 - same
CNNH - same
CNN - same
CH2NC - same
CH2NCN
NCCHN
NCNCN
cNCN
OHNHCN - bad
HONCNH
NCOHNH
HN(O)CN - bad
HNC(O)N
HOOS
SNO
H298 for NCN from Lin2013b: http://pubs.acs.org/doi/abs/10.1021/jp402903t
I can derive thermo for S, SNO, NSO, SON, SNO excited, NOS excited, SON excited in Cantherm with assistance from Table II in http://aip.scitation.org/doi/abs/10.1063/1.1806419
"""

