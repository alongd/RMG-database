# ruff: noqa: F821
# ``entry`` and ``ThermoData`` are injected by the RMG thermo-library loader.
name = "O2Vibrational"
shortDesc = "Fixed-v O2(X,v) thermochemistry for the IST-Lisbon vibrational ladder."
longDesc = """Generated from O2 vibrational levels and primaryThermoLibrary O2. The existing ground O2 thermo is decomposed into its non-vibrational contribution plus the ensemble vibrational partition function over the 42 bound X-state levels. The library stores the fixed-v non-vibrational component and a constant sourced level enthalpy. Statistical weights of vibrational levels are one; rotation remains in the baseline thermo. This generated library is not installed by default."""

entry(
    index = 0,
    label = "O2v0",
    molecule = """multiplicity 3\nvibrationallevel 0\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (-13.45343927341038, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 1,
    label = "O2v1",
    molecule = """multiplicity 3\nvibrationallevel 1\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (18897.67407693508721, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 2,
    label = "O2v2",
    molecule = """multiplicity 3\nvibrationallevel 2\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (37422.86021526177501, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 3,
    label = "O2v3",
    molecule = """multiplicity 3\nvibrationallevel 3\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (55272.64894229529455, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 4,
    label = "O2v4",
    molecule = """multiplicity 3\nvibrationallevel 4\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (72929.46698038793693, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 5,
    label = "O2v5",
    molecule = """multiplicity 3\nvibrationallevel 5\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (90393.31432953967305, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 6,
    label = "O2v6",
    molecule = """multiplicity 3\nvibrationallevel 6\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (107760.67633422093058, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 7,
    label = "O2v7",
    molecule = """multiplicity 3\nvibrationallevel 7\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (124549.12627207949117, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 8,
    label = "O2v8",
    molecule = """multiplicity 3\nvibrationallevel 8\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (140951.63483205626835, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 9,
    label = "O2v9",
    molecule = """multiplicity 3\nvibrationallevel 9\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (157161.17270309210289, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)

entry(
    index = 10,
    label = "O2v10",
    molecule = """multiplicity 3\nvibrationallevel 10\n1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}""",
    thermo = ThermoData(
        Tdata = ([300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000], 'K'),
        Cpdata = ([29.141550952486778, 29.19945547062675, 29.215457814322637, 29.239426792958252, 29.278985140219373, 29.280284497616034, 29.45952317805846, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652, 29.100652], 'J/(mol*K)'),
        H298 = (173274.22522965751705, 'J/mol'),
        S298 = (205.07995022167066, 'J/(mol*K)'),
        Cp0 = (20.78618000000000, 'J/(mol*K)'),
        CpInf = (29.10065200000000, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)
