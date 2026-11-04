#!/usr/bin/env python3
"""Build fixed-v O2 thermochemistry from IST term values and primary O2 thermo."""
import argparse
import json
import math
from pathlib import Path

from rmgpy import constants
from rmgpy.data.thermo import ThermoDatabase, ThermoLibrary


REPO_ROOT = Path(__file__).resolve().parents[1]
LEVELS_PATH = REPO_ROOT / 'input/eedf/o2_vibrational/levels.json'
GROUND_LIBRARY_PATH = REPO_ROOT / 'input/thermo/libraries/primaryThermoLibrary.py'
OUTPUT_PATH = REPO_ROOT / 'input/thermo/libraries/O2Vibrational.py'
TEMPERATURES = [300,400,500,600,800,1000,1500,2000,2500,3000,3500,
                4000,4500,5000,5500,6000]
MAX_FIXED_V = 10
GROUND_THERMO_TMAX = 1500
O2_GRAPH = '1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}'


def _vibrational_thermo(energies_eV, temperature):
    energies = [energy * constants.Na * constants.e for energy in energies_eV]
    weights = [math.exp(-energy / (constants.R * temperature)) for energy in energies]
    partition = sum(weights)
    mean = sum(energy * weight for energy, weight in zip(energies, weights)) / partition
    variance = sum((energy - mean) ** 2 * weight for energy, weight in zip(energies, weights)) / partition
    cp = variance / (constants.R * temperature ** 2)
    entropy = constants.R * math.log(partition) + mean / temperature
    return cp, mean, entropy


def build_library_bytes():
    """Return fixed-v library bytes with common non-vibrational Cp and sourced H shifts."""
    levels = json.loads(LEVELS_PATH.read_bytes())['levels']
    energies = [level['energy_eV'] for level in levels]
    database = ThermoDatabase()
    source_library = ThermoLibrary(label='primaryThermoLibrary')
    source_library.load(str(GROUND_LIBRARY_PATH), database.local_context, {})
    ground = source_library.entries['O2'].data
    cp_data = [ground.get_heat_capacity(T) - _vibrational_thermo(energies, T)[0]
               if T <= GROUND_THERMO_TMAX else 3.5 * constants.R
               for T in TEMPERATURES]
    h298 = ground.get_enthalpy(298) - _vibrational_thermo(energies, 298)[1]
    s298 = ground.get_entropy(298) - _vibrational_thermo(energies, 298)[2]
    cp0 = 2.5 * constants.R
    cp_inf = 3.5 * constants.R

    entries = []
    for v in range(MAX_FIXED_V + 1):
        h_v = h298 + energies[v] * constants.Na * constants.e
        entries.append(f'''entry(
    index = {v},
    label = "O2v{v}",
    molecule = """multiplicity 3\\nvibrationallevel {v}\\n{O2_GRAPH}""",
    thermo = ThermoData(
        Tdata = ({TEMPERATURES!r}, 'K'),
        Cpdata = ({cp_data!r}, 'J/(mol*K)'),
        H298 = ({h_v:.14f}, 'J/mol'),
        S298 = ({s298:.14f}, 'J/(mol*K)'),
        Cp0 = ({cp0:.14f}, 'J/(mol*K)'),
        CpInf = ({cp_inf:.14f}, 'J/(mol*K)'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
    ),
    shortDesc = "Fixed-v O2(X) thermo; non-vibrational baseline from primaryThermoLibrary O2.",
    longDesc = """Generated from levels.json and primaryThermoLibrary O2. The v=0 baseline is primaryThermoLibrary O2 minus the ensemble vibrational partition contribution computed from all 42 bound X-state levels. Cp and S are common to all fixed-v levels; H is shifted by the IST-sourced E_v. No ensemble vibrational heat capacity is retained. The existing O2 thermo supplies Cp through 1500 K; above that, the non-vibrational Cp is extended at the diatomic translational-plus-rotational limit 3.5 R. The model uses the plain ground O2 species for v=0; O2v0 is a fixed-v thermo reference entry.""",
)
''')
    header = '''# ruff: noqa: F821
# ``entry`` and ``ThermoData`` are injected by the RMG thermo-library loader.
name = "O2Vibrational"
shortDesc = "Fixed-v O2(X,v) thermochemistry for the IST-Lisbon vibrational ladder."
longDesc = """Generated from O2 vibrational levels and primaryThermoLibrary O2. The existing ground O2 thermo is decomposed into its non-vibrational contribution plus the ensemble vibrational partition function over the 42 bound X-state levels. The library stores the fixed-v non-vibrational component and a constant sourced level enthalpy. Statistical weights of vibrational levels are one; rotation remains in the baseline thermo. This generated library is not installed by default."""

'''
    return (header + '\n'.join(entries)).encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check', action='store_true', help='fail if the committed library is stale')
    group.add_argument('--write', action='store_true', help='rewrite the committed fixed-v thermo library')
    args = parser.parse_args()
    generated = build_library_bytes()
    if args.write:
        OUTPUT_PATH.write_bytes(generated)
        print(f'wrote {OUTPUT_PATH}')
    elif OUTPUT_PATH.read_bytes() != generated:
        raise SystemExit(f'{OUTPUT_PATH} differs from reproducible fixed-v thermo generation')
    else:
        print(f'{OUTPUT_PATH}: reproducible')


if __name__ == '__main__':
    main()
