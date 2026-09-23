#!/usr/bin/env python
# encoding: utf-8

name = "primaryTransportLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (496.376,'J/mol'),
        sigma = (2.8327,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for H2""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (887.157,'J/mol'),
        sigma = (3.467,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for O2""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (6727.26,'J/mol'),
        sigma = (2.641,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""library value for H2O""",
    longDesc = u"""""",
)

entry(
    index = 4,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2405.38,'J/mol'),
        sigma = (4.196,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for H2O2""",
    longDesc = u"""""",
)

entry(
    index = 5,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1622.99,'J/mol'),
        sigma = (3.941,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for CO2""",
    longDesc = u"""""",
)

entry(
    index = 6,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (762.44,'J/mol'),
        sigma = (3.69,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""library value for CO""",
    longDesc = u"""""",
)

entry(
    index = 7,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1837.5,'J/mol'),
        sigma = (3.73,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for H2S""",
    longDesc = u"""""",
)

entry(
    index = 8,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (810.913,'J/mol'),
        sigma = (3.621,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2""",
    longDesc = u"""""",
)

entry(
    index = 9,
    label = "C(S)",
    molecule = 
"""
1 C u0 p2 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (593.655,'J/mol'),
        sigma = (3.298,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C""",
    longDesc = u"""""",
)

entry(
    index = 10,
    label = "NH(S)",
    molecule = 
"""
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (665.16,'J/mol'),
        sigma = (2.65,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH""",
    longDesc = u"""""",
)

entry(
    index = 11,
    label = "N(D)",
    molecule = 
"""
multiplicity 2
1 N u1 p2 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (593.655,'J/mol'),
        sigma = (3.298,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N""",
    longDesc = u"""""",
)


entry(
    index = 12,
    label = "Ar(3P2)",
    molecule = 
"""
multiplicity 3
1 Ar u2 p3 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (1134.93,'J/mol'),
        sigma = (3.33,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.64,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""Metastable argon; GRI-Mech3.0 value for ground-state AR""",
    longDesc = 
u"""
Metastable argon Ar(3P2), the 4s[3/2]_2 level 11.548 eV above the ground state. The structure
matches the species entry in the PlasmaExcitedNeutralThermo thermo library exactly.

Lennard-Jones parameters are those of ground-state argon, from the AR line of the GRI-Mech 3.0
tran.dat: shape 0 (atom), epsilon/k = 136.500 K (= 1134.93 J/mol), sigma = 3.330 Angstrom,
dipole 0, rotational relaxation 0. The same line is carried as "AR" by the GRI-Mech, NOx2018
and NIST_Fluorine transport libraries here. Polarizability is the static dipole polarizability of
ground-state argon, 1.6411 Angstrom^3 (CRC Handbook of Chemistry and Physics, "Atomic and
Molecular Polarizabilities"); the GRI-Mech line writes 0, which Chemkin only uses for
polar-nonpolar pairs, and there are none in an argon mixture.

Borrowing ground-state values for an excited state is the standard approximation, and this
library already does it for N(D) with the ground-state N value. No transport data has been
measured for the metastable's collisions with neutrals, and the metastable is a trace species
so it has no effect on mixture viscosity or conductivity. It does NOT describe the metastable's
own physics: its 4s electron makes its polarizability over an order of magnitude larger than
the ground state's, so its real diffusion coefficient in argon differs from the one these
parameters give. Anyone modelling metastable diffusion to a wall should replace these values
with a measured D*N for Ar(3P2) in Ar, not rely on them.

Why this entry exists: without a library hit, get_transport_properties falls back to group
additivity, which saturates the u2 biradical with hydrogen to give ArH2. No atom type exists
for that, so the Chemkin export (render_transport_file) aborts with an AtomTypeError. A library
hit stops the lookup before group estimation runs.
""",
)
