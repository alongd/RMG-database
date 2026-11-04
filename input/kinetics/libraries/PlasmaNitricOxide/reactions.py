#!/usr/bin/env python
# encoding: utf-8

name = "PlasmaNitricOxide"
shortDesc = "Hayashi NO electron-impact owner reactions"
longDesc = """Dedicated owner library for the class-A channels in the Hayashi NO set.
The collision identities and full source thresholds are recorded in
input/eedf/no_channel_map.yaml. Cross sections are kept only in the local LXCat store.
"""

entry(
    index = 1,
    label = "NO + e- => N + O-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + NO(X) -> N(4S) + O(-,gnd), Attachment',
        collision_set = "no-hayashi-v1",
        side = "ine",
    ),
    shortDesc = "Hayashi NO dissociative attachment owner",
    longDesc = """Owner for `e + NO(X) -> N(4S) + O(-,gnd), Attachment` from the Hayashi
NO collision set. The source labels NO- but the PM-approved interpretation is
dissociative attachment to N + O-. The collision and source-block hashes are in
input/eedf/no_channel_map.yaml; no rate law or cross section is stored here.
""",
)

entry(
    index = 2,
    label = "NO + e- => NOp + e- + e-",
    reversible = False,
    kinetics = EEDFChannel(
        process = 'e + NO(X) -> e + e + NO(+,gnd), Ionization',
        collision_set = "no-hayashi-v1",
        side = "ine",
    ),
    shortDesc = "Hayashi NO ionization owner",
    longDesc = """Owner for `e + NO(X) -> e + e + NO(+,gnd), Ionization` from the Hayashi
NO collision set. NO(+,gnd) resolves to the NOp reference species in this library.
The collision and source-block hashes are in input/eedf/no_channel_map.yaml; no
rate law or cross section is stored here.
""",
)
