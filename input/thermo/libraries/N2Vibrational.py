# ruff: noqa: F821
# ``entry`` and ``ThermoData`` are injected by the RMG thermo-library loader.
name = "N2Vibrational"
shortDesc = "Fixed-v N2(X) thermochemistry for the Laporta vibrational ladder."
longDesc = """Generated from levels.json and primaryThermoLibrary N2. The existing NASA ground thermo is decomposed into its non-vibrational contribution plus the ensemble vibrational partition function over the 59 bound X-state levels. The library stores only the fixed-v non-vibrational component and a constant sourced level enthalpy. Statistical weights of vibrational levels are one; rotation and nuclear spin remain in the baseline thermo. This generated library is not installed by default."""

entry(
    index = 0,
    label = "N2v0",
    molecule = """vibrationallevel 0\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (-4.75416353171556, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 1,
    label = "N2v1",
    molecule = """vibrationallevel 1\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (27840.91625064059917, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 2,
    label = "N2v2",
    molecule = """vibrationallevel 2\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (55348.88795916631352, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 3,
    label = "N2v3",
    molecule = """vibrationallevel 3\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (82519.16096204545465, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 4,
    label = "N2v4",
    molecule = """vibrationallevel 4\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (109361.38379372507916, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 5,
    label = "N2v5",
    molecule = """vibrationallevel 5\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (135865.90791975811590, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 6,
    label = "N2v6",
    molecule = """vibrationallevel 6\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (162032.73334014456486, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 7,
    label = "N2v7",
    molecule = """vibrationallevel 7\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (187852.21152043738402, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 8,
    label = "N2v8",
    molecule = """vibrationallevel 8\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (213333.99099508364452, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 9,
    label = "N2v9",
    molecule = """vibrationallevel 9\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (238478.07176408328814, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 10,
    label = "N2v10",
    molecule = """vibrationallevel 10\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (263274.80529298930196, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 11,
    label = "N2v11",
    molecule = """vibrationallevel 11\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (287724.19158180174418, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 12,
    label = "N2v12",
    molecule = """vibrationallevel 12\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (311835.87916496756952, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 13,
    label = "N2v13",
    molecule = """vibrationallevel 13\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (335590.57097359275213, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 14,
    label = "N2v14",
    molecule = """vibrationallevel 14\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (358997.91554212430492, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 15,
    label = "N2v15",
    molecule = """vibrationallevel 15\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (382057.91287056222791, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 16,
    label = "N2v16",
    molecule = """vibrationallevel 16\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (404760.91442445944995, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 17,
    label = "N2v17",
    molecule = """vibrationallevel 17\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (427116.56873826304218, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 18,
    label = "N2v18",
    molecule = """vibrationallevel 18\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (449105.57874307892052, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 19,
    label = "N2v19",
    molecule = """vibrationallevel 19\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (470737.59297335415613, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 20,
    label = "N2v20",
    molecule = """vibrationallevel 20\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (492002.96289464173606, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 21,
    label = "N2v21",
    molecule = """vibrationallevel 21\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (512901.68850694148568, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 22,
    label = "N2v22",
    molecule = """vibrationallevel 22\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (533424.12127580656670, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 23,
    label = "N2v23",
    molecule = """vibrationallevel 23\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (553579.90973568381742, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 24,
    label = "N2v24",
    molecule = """vibrationallevel 24\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (573340.10828323231544, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 25,
    label = "N2v25",
    molecule = """vibrationallevel 25\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (592724.01398734608665, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 26,
    label = "N2v26",
    molecule = """vibrationallevel 26\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (611712.32977913087234, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 27,
    label = "N2v27",
    molecule = """vibrationallevel 27\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (630305.05565858690534, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 28,
    label = "N2v28",
    molecule = """vibrationallevel 28\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (648482.89455681992695, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 29,
    label = "N2v29",
    molecule = """vibrationallevel 29\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (666245.84647383005358, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)

entry(
    index = 30,
    label = "N2v30",
    molecule = """vibrationallevel 30\n1 N u0 p1 c0 {2,T}\n2 N u0 p1 c0 {1,T}""",
    thermo = ThermoData(
        Tdata = ([298, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.11034397178637, 29.110764956391538, 29.139319480865293, 29.13647079491188, 29.107771680394013, 29.138823102267317, 29.149197684805948, 29.135321231357825, 29.296710596599013, 29.38871814218099, 29.39306954045408, 29.37263307884346, 29.39078558262225, 29.479070903712135, 29.62379590518566, 29.76004898683032, 29.768825115869447], 'J/(mol*K)'),
        H298 = (683593.91140961728524, 'J/mol'),
        S298 = (191.59306154696796, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v N2(X) thermo; non-vibrational baseline from primaryThermoLibrary N2.",
    longDesc = """The v=0 baseline is primaryThermoLibrary N2 minus the ensemble vibrational partition contribution computed from the Laporta term values. Cp and S are common to all fixed-v levels; H is shifted by the Laporta E_v. No ensemble vibrational heat capacity is retained.""",
)
