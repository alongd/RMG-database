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
LOW_T = list(range(300, 1001))
ESP_T = list(range(50, 10001))


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
        rates = [annusova_vt_rate(v, T) for T in LOW_T]
        lower_state = 'O2' if v == 1 else f'O2v{v - 1}'
        add(f'O2v{v} + O2 <=> {lower_state} + O2',
            rates, LOW_T, 'Annušová et al. (2018), Table A2', (300, 1000),
            f"Source fit {a2['formula_v_1_6'] if v <= 6 else a2['formula_v_7_32']}; "
            'V-T/R deactivation, 300–1000 K. Source rates use cm^3/(molecule*s).')

    for high_v in range(2, 11):
        for partner in range(0, high_v - 1):
            row = a3_by_pair[(partner + 1, high_v)]
            # Four source-equation nodes are needed by the bounded output-fit adapter.
            temperatures = [300, 500, 750, 1000]
            rates = [1.5 * row['A'] * T**row['B'] for T in temperatures]
            reactant_low = f'O2v{partner + 1}'
            reactant_high = f'O2v{high_v - 1}'
            product_low = 'O2' if partner == 0 else f'O2v{partner}'
            product_high = f'O2v{high_v}'
            add(f'{reactant_low} + {reactant_high} <=> {product_low} + {product_high}',
                rates, temperatures, 'Annušová et al. (2018), Table A3', (300, 1000),
                f"A3 pair (v={row['v']}, w={row['w']}), k=1.5*A*T^B; source A={row['A']:.12g}, "
                f"B={row['B']:.12g}. Source direction O2(partner+1)+O2(high_v-1) -> "
                f"O2(partner)+O2(high_v); reverse from fixed-v detailed balance; "
                'bounds 300–1000 K; v=42 dissociation is excluded.')

    for v in range(1, 11):
        for delta_v in range(1, v + 1):
            w = v - delta_v
            rates = [_esposito_rate(v, delta_v, T, esposito) for T in ESP_T]
            add(f'O2v{v} + O <=> {"O2" if w == 0 else f"O2v{w}"} + O',
                rates, ESP_T, 'Esposito et al. (2008), Eq. (3a-c), Tables 2-4', (50, 10000),
                f"O2(v={v}) + O -> O2(w={w}) + O, delta-v={delta_v}; "
                'DegF=1/27 as stated for the paper fit. Source equation sampled at every integer K '
                'for bounded geometric KineticsData interpolation. Reverse from fixed-v detailed balance.')

    content = '''# ruff: noqa: E501,F821
name = "O2VibrationalRelaxation"
shortDesc = "Sourced O2 heavy-particle V-T and V-V relaxation through v=10."
longDesc = """O2-O2 V-T/R and V-V from Annušová et al. (2018), Tables A2 and A3; O2-O V-T from Esposito et al. (2008), Eq. (3a-c), Tables 2-4. All entries are reversible; RMG derives reverse rates from loaded fixed-v thermo. O2-O2 bounds are 300-1000 K; O2-O bounds are 50-10000 K. O2-O2 V-V entries cover exactly high_v=2..10 with partner=0..high_v-2 and no identity exchanges. The table fit values use cm^3/(molecule*s), converted by RMG. The Esposito fit is sampled at every integer K so KineticsData refuses outside its stored source interval and interpolation approximates the source formula between adjacent K. No O2(v=42) dissociation rates are included. Source PDF payloads remain in /home/alon/Data/vibkin, outside git."""

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
