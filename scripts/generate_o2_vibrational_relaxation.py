#!/usr/bin/env python3
"""Generate bounded O2 heavy-particle V-T/V-V library data from source tables."""
import argparse
import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LIBRARY = REPO / 'input/kinetics/libraries/O2VibrationalRelaxation'
A2_PATH = LIBRARY / 'annusova2018_table_a2.json'
A3_PATH = LIBRARY / 'annusova2018_table_a3.json'
ESP_PATH = LIBRARY / 'esposito2008_tables_2_4.json'
ESP_SOURCE_T = (50, 10000)
O2O2_SOURCE_T = (300, 1000)


def _loaded_thermo_domain():
    """Read admitted O/O2(v=1) thermo limits through the real model path."""
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy.data.thermo import ThermoDatabase
    import rmgpy.data.rmg as rmg_data
    from rmgpy.molecule import Molecule
    from rmgpy.rmg.model import CoreEdgeReactionModel
    from rmgpy.species import Species

    previous = rmg_data.database
    database = RMGDatabase()
    database.thermo = ThermoDatabase()
    database.thermo.load_libraries(str(REPO / 'input/thermo/libraries'),
                                   ['primaryThermoLibrary', 'O2Vibrational'])
    rmg_data.database = database
    try:
        model = CoreEdgeReactionModel()
        ground = Species(label='O2', molecule=[Molecule().from_adjacency_list(
            'multiplicity 3\n1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}')])
        model.declare_vibrational_manifold(ground)
        participants = [ground]
        for level in range(1, 11):
            participants.append(Species(label=f'O2v{level}', molecule=[Molecule().from_adjacency_list(
                f'multiplicity 3\nvibrationallevel {level}\n'
                '1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}')]))
        participants.append(Species(label='O', molecule=[Molecule().from_adjacency_list(
            'multiplicity 3\n1 O u2 p2 c0')]))
        limits = []
        for species in participants:
            admitted, _ = model.make_new_species(species)
            limits.append((float(admitted.thermo.Tmin.value_si),
                           float(admitted.thermo.Tmax.value_si)))
        return max(low for low, _ in limits), min(high for _, high in limits)
    finally:
        rmg_data.database = previous


def _adaptive_nodes(rate, low, high, limit=0.01):
    """Greedily bisect the interval with greatest scanned log-linear error."""
    nodes = [low, high]
    steps = math.ceil((high - low) / 0.5)
    grid = [min(low + index * 0.5, high) for index in range(steps + 1)]
    while True:
        rates = {t: rate(t) for t in nodes}
        worst = (0.0, None, None)
        for left, right in zip(nodes, nodes[1:]):
            lk, rk = math.log(rates[left]), math.log(rates[right])
            span = right - left
            for t in grid:
                if not left < t < right:
                    continue
                fraction = (t-left)/span
                estimate = math.exp(lk + fraction*(rk-lk))
                error = abs(estimate/rate(t)-1)
                if error > worst[0]:
                    worst = (error, t, left)
        if worst[0] <= limit:
            return nodes
        split, left = worst[1], worst[2]
        if split is None:
            raise ValueError('cannot refine interpolation interval')
        nodes.append(split)
        nodes.sort()


def annusova_vt_rate(v, temperature):
    """Annušová 2018 Table A2 O2(v)+O2(0) -> O2(v-1)+O2(0), cm3/molecule/s."""
    T = temperature
    if 1 <= v <= 6:
        a = -2.16870e-3*v**3 + 1.02950e-2*v**2 - 9.03306e-2*v + 6.02557
        b = 2.78130e-2*v**3 - 2.76608e-1*v**2 + 2.04169*v - 76.0376
        return 0.25 * math.exp(a * math.log(T) + b)
    if 7 <= v <= 32:
        return 0.25 * (2.44106e-33 * T**6.25015) * math.exp(
            (1.76911e-7*T**2 - 4.82968e-4*T + 5.40946e-1) * v)
    raise ValueError(f'Annušová Table A2 has no O2-O2 V-T fit for initial v={v}')


def _esposito_rate(v, delta_v, temperature, source):
    if not 1 <= v <= 46 or not 1 <= delta_v <= min(v, 30):
        raise ValueError(f'Esposito source domain excludes v={v}, delta_v={delta_v}')
    if not 50 <= temperature <= 10000:
        raise ValueError(f'Esposito source domain excludes T={temperature} K')
    bin_name = 'dv_1' if delta_v == 1 else 'dv_2_10'
    a_values = []
    for name in ('a1', 'a2', 'a3'):
        b_values = []
        matrix = source['coefficient_bins'][name][bin_name]
        for j in range(5):
            c1, c2, c3, c4 = matrix[j]
            b_values.append(c1 + c2*math.log(delta_v) + c3*delta_v*math.exp(-delta_v)
                            + c4*delta_v**2)
        a_values.append(b_values[0] + b_values[1]*math.log(v)
                        + (b_values[2] + b_values[3]*v + b_values[4]*v**2)
                        / (1e21 + math.exp(v)))
    return source['degeneracy_factor']['value'] * math.exp(
        a_values[0] + a_values[1]/math.log(temperature)
        + a_values[2]*math.log(temperature))


def _adjacency(level):
    tag = f'vibrationallevel {level}\n' if level else ''
    return 'multiplicity 3\n' + tag + '1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}'


def _py_data(values):
    return '[' + ', '.join(repr(float(value)) for value in values) + ']'


def build_outputs():
    a2 = json.loads(A2_PATH.read_bytes())
    a3 = json.loads(A3_PATH.read_bytes())
    esposito = json.loads(ESP_PATH.read_bytes())
    thermo_low, thermo_high = _loaded_thermo_domain()
    o2o2_low = max(O2O2_SOURCE_T[0], thermo_low)
    o2o2_high = min(O2O2_SOURCE_T[1], thermo_high)
    dictionary = ['O2', _adjacency(0), '']
    dictionary.extend(line for v in range(1, 11) for line in (f'O2v{v}', _adjacency(v), ''))
    dictionary.extend(['O', 'multiplicity 3', '1 O u2 p2 c0', ''])

    entries = []

    def add(label, rate_values, temperatures, source, domain, channel):
        index = len(entries)
        entries.append(f'''entry(
    index = {index},
    label = {label!r},
    reversible = True,
    kinetics = KineticsData(
        Tdata = ({_py_data(temperatures)}, 'K'),
        kdata = ({_py_data(rate_values)}, 'cm^3/(molecule*s)'),
        Tmin = ({domain[0]}, 'K'), Tmax = ({domain[1]}, 'K')),
    shortDesc = {source!r},
    longDesc = {channel!r},
)''')

    a3_by_pair = {(row['v'], row['w']): row for row in a3['coefficients']}
    for v in range(1, 11):
        rate = lambda T, v=v: annusova_vt_rate(v, T)
        temperatures = _adaptive_nodes(rate, o2o2_low, o2o2_high)
        rates = [rate(T) for T in temperatures]
        lower_state = 'O2' if v == 1 else f'O2v{v - 1}'
        add(f'O2v{v} + O2 <=> {lower_state} + O2',
            rates, temperatures, 'Annušová et al. (2018), Table A2', (o2o2_low, o2o2_high),
            f"Source fit {a2['formula_v_1_6'] if v <= 6 else a2['formula_v_7_32']}; "
            'V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).')

    for high_v in range(2, 11):
        for partner in range(0, high_v - 1):
            row = a3_by_pair[(partner + 1, high_v)]
            rate = lambda T, row=row: 1.5 * row['A'] * T**row['B']
            temperatures = _adaptive_nodes(rate, o2o2_low, o2o2_high)
            rates = [rate(T) for T in temperatures]
            reactant_low = f'O2v{partner + 1}'
            reactant_high = f'O2v{high_v - 1}'
            product_low = 'O2' if partner == 0 else f'O2v{partner}'
            product_high = f'O2v{high_v}'
            add(f'{reactant_low} + {reactant_high} <=> {product_low} + {product_high}',
                rates, temperatures, 'Annušová et al. (2018), Table A3', (o2o2_low, o2o2_high),
                f"A3 pair (v={row['v']}, w={row['w']}), k=1.5*A*T^B; source A={row['A']:.12g}, "
                f"B={row['B']:.12g}. Source direction O2(partner+1)+O2(high_v-1) -> "
                f"O2(partner)+O2(high_v); reverse from fixed-v detailed balance; "
                'bounds 300–1000 K; v=42 dissociation is excluded.')

    for v in range(1, 11):
        for delta_v in range(1, v + 1):
            w = v - delta_v
            low, high = max(ESP_SOURCE_T[0], thermo_low), min(ESP_SOURCE_T[1], thermo_high)
            rate = lambda T, v=v, dv=delta_v: _esposito_rate(v, dv, T, esposito)
            temperatures = _adaptive_nodes(rate, low, high)
            rates = [rate(T) for T in temperatures]
            add(f'O2v{v} + O <=> {"O2" if w == 0 else f"O2v{w}"} + O',
                rates, temperatures, 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4', (low, high),
                f"O2(v={v}) + O -> O2(w={w}) + O, delta-v={delta_v}; "
                f'DegF=1/27 as stated for the paper fit. Source valid {ESP_SOURCE_T[0]}–{ESP_SOURCE_T[1]} K; restricted to the '
                f'thermo-valid range {low:g}–{high:g} K for detailed balance; absences: '
                f'{ESP_SOURCE_T[0]}–{low:g} K and '
                f'{high:g}–{ESP_SOURCE_T[1]} K. Adaptive bounded interpolation nodes. Reverse from fixed-v detailed balance.')

    content = f'''# ruff: noqa: E501,F821
name = "O2VibrationalRelaxation"
shortDesc = "Sourced O2 heavy-particle V-T and V-V relaxation through v=10."
longDesc = """O2-O2 V-T/R and V-V from Annušová et al. (2018), Tables A2 and A3; O2-O V-T from Esposito et al. (2008), Eq. (3a-c), Tables 2-4. All entries are reversible; RMG derives reverse rates from loaded fixed-v thermo. O2-O2 bounds are {o2o2_low:g}-{o2o2_high:g} K; O2-O bounds are the thermo-limited {max(ESP_SOURCE_T[0], thermo_low):g}-{min(ESP_SOURCE_T[1], thermo_high):g} K domain (source valid {ESP_SOURCE_T[0]}-{ESP_SOURCE_T[1]} K; absent {ESP_SOURCE_T[0]}-{max(ESP_SOURCE_T[0], thermo_low):g} K and {min(ESP_SOURCE_T[1], thermo_high):g}-{ESP_SOURCE_T[1]} K). O2-O2 V-V entries cover exactly high_v=2..10 with partner=0..high_v-2 and no identity exchanges. Tables use bounded, adaptively refined KineticsData with maximum 1% scanned source-formula interpolation error; values use cm^3/(molecule*s), converted by RMG. No O2(v=42) dissociation rates are included. Source PDF payloads remain in /home/alon/Data/vibkin, outside git."""

''' + '\n\n'.join(entries) + '\n'
    return {'dictionary.txt': ('\n'.join(dictionary)).encode(), 'reactions.py': content.encode()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = build_outputs()
    if args.write:
        for name, data in outputs.items():
            (LIBRARY / name).write_bytes(data)
            print(f'wrote {LIBRARY / name} ({len(data)} bytes)')
    elif args.check:
        failures = []
        for name, data in outputs.items():
            path = LIBRARY / name
            if not path.exists() or path.read_bytes() != data:
                failures.append(name)
        if failures:
            raise SystemExit('stale generated O2 relaxation files: ' + ', '.join(failures))
        print('O2 relaxation library is reproducible')
    else:
        parser.error('pass --write or --check')


if __name__ == '__main__':
    main()
