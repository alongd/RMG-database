#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaArgon"
shortDesc = "State-resolved argon EEDF excitation and ionisation owners"
longDesc = """
Five independent IST-Lisbon-Ar-2021 collision owners. Ars is Ar(1s5), 3P2,
shared with PlasmaArgonDimer and PlasmaOxygenHeavy. Ar(1s4), Ar(1s3), Ar(1s2)
are separate electronic states. This library is not runnable for reacting EEDF:
cascade channels 6–38 still refuse. The three new states have production but
no loss: no radiative/trapped decay, quenching, diffusion, mixing, stepwise
ionisation or dimer formation. No cascade or trapped-decay rate is added here.
Historical Maxwellian entries 86–93 are preserved in PlasmaArgonLegacy.
See input/eedf/README.md for the required legacy-deck migration.
"""

entry(
    index = 86,
    label = "Ar + e- => Arp + e- + e-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + Ar(1S0) -> e + e + Ar(+,gnd), Ionization',
        collision_set = "IST-Lisbon-Ar-2021",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-Ar-2021 channel 39; see argon_channel_map.yaml provenance",
    longDesc = """Rate supplied by the matching EEDF collision column, without a Maxwellian law.
The frozen map retains the source identity, threshold and cross-section digest.
""",
)

entry(
    index = 87,
    label = "Ar + e- => Ars + e-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + Ar(1S0) -> e + Ar(3P2), Excitation',
        collision_set = "IST-Lisbon-Ar-2021",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-Ar-2021 channel 2; see argon_channel_map.yaml provenance",
    longDesc = """Rate supplied by the matching EEDF collision column, without a Maxwellian law.
The frozen map retains the source identity, threshold and cross-section digest.
""",
)

entry(
    index = 94,
    label = "Ar + e- => Ar(1s4) + e-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + Ar(1S0) -> e + Ar(3P1), Excitation',
        collision_set = "IST-Lisbon-Ar-2021",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-Ar-2021 channel 3; see argon_channel_map.yaml provenance",
    longDesc = """Rate supplied by the matching EEDF collision column, without a Maxwellian law.
The frozen map retains the source identity, threshold and cross-section digest.
""",
)

entry(
    index = 95,
    label = "Ar + e- => Ar(1s3) + e-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + Ar(1S0) -> e + Ar(3P0), Excitation',
        collision_set = "IST-Lisbon-Ar-2021",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-Ar-2021 channel 4; see argon_channel_map.yaml provenance",
    longDesc = """Rate supplied by the matching EEDF collision column, without a Maxwellian law.
The frozen map retains the source identity, threshold and cross-section digest.
""",
)

entry(
    index = 96,
    label = "Ar + e- => Ar(1s2) + e-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + Ar(1S0) -> e + Ar(1P1), Excitation',
        collision_set = "IST-Lisbon-Ar-2021",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-Ar-2021 channel 5; see argon_channel_map.yaml provenance",
    longDesc = """Rate supplied by the matching EEDF collision column, without a Maxwellian law.
The frozen map retains the source identity, threshold and cross-section digest.
""",
)
