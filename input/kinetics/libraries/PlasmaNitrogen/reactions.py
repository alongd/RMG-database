#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaNitrogen"
shortDesc = "State-resolved N2 electron-impact owner reactions"
longDesc = """Owner library for class-A channels in IST-Lisbon N2_LXCat.txt.
Processes use the canonical PARAM/bracket block identity consumed by LoKI, rather than the older
PROCESS display aliases. The nitrogen map generator checks each process and collision set
against its loaded owner. Existing EEDF tables must be regenerated after this metadata change.
The channel map and energy leaks retain full source thresholds; no cross sections are stored.
"""

entry(
    index = 1,
    label = "N2 + e- => N2A + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(A3Su+,v=0-4), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(A3Su+,v=0-4), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 2,
    label = "N2 + e- => N2A + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(A3Su+,v=5-9), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(A3Su+,v=5-9), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 3,
    label = "N2 + e- => N2B + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(B3Pg), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(B3Pg), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 4,
    label = "N2 + e- => N2B + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(W3Du), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(W3Du), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 5,
    label = "N2 + e- => N2A + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(A3Su+,v=10+), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(A3Su+,v=10+), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 6,
    label = "N2 + e- => N2B + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(B3Su-), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(B3Su-), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 7,
    label = "N2 + e- => N2ap + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(a1Su-), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(a1Su-), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 8,
    label = "N2 + e- => N2a + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(a1Pg), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(a1Pg), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 9,
    label = "N2 + e- => N2w + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(w1Du), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(w1Du), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 10,
    label = "N2 + e- => N2C + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + N2(C3Pu), Excitation',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + N2(C3Pu), Excitation`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 11,
    label = "N2 + e- => N2p + e- + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + e + N2(+,X), Ionization',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + e + N2(+,X), Ionization`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)

entry(
    index = 12,
    label = "N2 + e- => N2pB + e- + e-",
    reversible = False,
    duplicate = True,
    kinetics = EEDFChannel(
        process = 'e + N2(X) -> e + e + N2(+,B), Ionization',
        collision_set = "IST-Lisbon-N2-2022",
        side = "ine",
    ),
    shortDesc = "IST-Lisbon-N2-2022 class-A owner",
    longDesc = """Owner for `e + N2(X) -> e + e + N2(+,B), Ionization`. Exact LoKI block and full threshold are recorded in nitrogen_channel_map.yaml.
""",
)
