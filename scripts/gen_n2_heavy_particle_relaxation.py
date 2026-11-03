#!/usr/bin/env python3
"""Generate sourced, state-resolved N2(X,v) V-T and V-V library entries."""

import argparse
import json
import math
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PARAMETERS = ROOT / 'input/kinetics/libraries/N2HeavyParticleRelaxation/parameters.yaml'
LEVELS = ROOT / 'input/eedf/n2_vibrational/levels.json'
OUTPUT_DIR = ROOT / 'input/kinetics/libraries/N2HeavyParticleRelaxation'
AVOGADRO = 6.02214076e23
KB = 1.380649e-23
HBAR = 1.054571817e-34
HC_CM = 1.9864458571489286e-23  # h*c*100, J per cm^-1
U_KG = 1.66053906660e-27
REFERENCE_TEMPERATURES = (300, 400, 500, 700, 1000, 1500, 2000, 3000)


def validate(parameters, levels, maximum_v=None):
    """Reject incomplete provenance, unsupported ranges, or a mismatched ladder."""
    if parameters.get('schema_version') != 1:
        raise ValueError('unsupported parameter schema_version')
    record = parameters.get('record_source', {})
    for field in ('citation', 'file', 'sha256', 'equations', 'constants', 'validity'):
        if not record.get(field):
            raise ValueError(f'missing record-source {field}')
    if (len(record['sha256']) != 64
            or any(character not in '0123456789abcdef' for character in record['sha256'].lower())):
        raise ValueError('record-source SHA-256 must contain 64 hex digits')
    billing_hash = parameters.get('billing_check', {}).get('sha256', '')
    if (len(billing_hash) != 64
            or any(character not in '0123456789abcdef' for character in billing_hash.lower())):
        raise ValueError('missing Billing check provenance')
    required_equations = {9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23}
    equations = record['equations']
    if (not isinstance(equations, dict) or not required_equations.issubset(equations)
            or not all(isinstance(value, str) and value for value in equations.values())):
        raise ValueError('record-source equation transcription is incomplete or malformed')
    gaps = record.get('gaps', [])
    if not gaps or {item.get('id') for item in gaps} != {
            'n2_ar_vt', 'ar_metastable_n2_quenching', 'n2_n_vt'}:
        raise ValueError('required named gaps are missing or changed')
    entries = levels.get('levels')
    if not isinstance(entries, list) or not entries:
        raise ValueError('levels file has no level list')
    expected_maximum = entries[-1]['v'] if maximum_v is None else maximum_v
    if isinstance(expected_maximum, bool) or not isinstance(expected_maximum, int) or expected_maximum < 1:
        raise ValueError('requested K must be an integer of at least 1')
    selected = entries[:expected_maximum + 1]
    if len(selected) != expected_maximum + 1:
        raise ValueError('level data do not cover requested K')
    if [row.get('v') for row in selected] != list(range(expected_maximum + 1)):
        raise ValueError('level numbers must be contiguous from zero')
    for row in selected:
        if row.get('thermo_entry') != f"N2v{row['v']}":
            raise ValueError(f"fixed-v thermo entry missing for v={row['v']}")
        if not isinstance(row.get('energy_eV'), (int, float)) or not math.isfinite(row['energy_eV']):
            raise ValueError(f"invalid fixed-v energy for v={row['v']}")
    vt = record['validity']['vt']
    vv = record['validity']['vv']
    if expected_maximum > min(vt['deactivating_v'][1], vv['deactivating_v'][1]):
        raise ValueError('requested K exceeds sourced rate range')
    return expected_maximum


def _f(y):
    """Guerra et al. Eq. (10), dimensionless adiabaticity function."""
    if y < 0 or not math.isfinite(y):
        raise ValueError('Y must be finite and nonnegative')
    if y < 21.622:
        z = math.exp(-2.0 * y / 3.0)
        return 0.5 * (3.0 - z) * z
    return 0.125 * math.sqrt(math.pi / 3.0) * y ** (7.0 / 3.0) * math.exp(-3.0 * y ** (2.0 / 3.0))


def _morse_gap_cm(v, constants):
    """Eq. (6) level spacing for the v -> v-1 transition, in cm^-1."""
    omega = constants['omega_e_cm-1']
    omega_xe = constants['omega_e_xe_cm-1']
    return omega - 2.0 * omega_xe * v


def _y_for_gap(gap_cm, temperature, parameters):
    constants = parameters['record_source']['constants']
    mass = constants['nitrogen_molecule_mass_u'] * U_KG / 2.0
    length = constants['L_angstrom'] * 1.0e-10
    energy = abs(gap_cm) * HC_CM
    return energy * math.pi * length / HBAR * math.sqrt(mass / (2.0 * KB * temperature))


def rate_vt(v, temperature, parameters):
    """Eq. (12), (20), and (21) V-T coefficient, in cm^3 per molecule per s."""
    bounds = parameters['record_source']['validity']['vt']
    if not bounds['deactivating_v'][0] <= v <= bounds['deactivating_v'][1]:
        raise ValueError(f'Guerra Eq. (20)-(21) V-T refuses v={v}; sourced v range is 1-45')
    tmin, tmax = bounds['temperature_K']
    if not tmin <= temperature <= tmax:
        raise ValueError(f'Guerra Eq. (20)-(21) V-T refuses T={temperature:g} K; sourced range is 300-3500 K')
    rec = parameters['record_source']
    omega = rec['constants']['omega_e_cm-1']
    omega_xe = rec['constants']['omega_e_xe_cm-1']
    chi = omega_xe / omega
    y = _y_for_gap(_morse_gap_cm(v, rec['constants']), temperature, parameters)
    y10 = _y_for_gap(_morse_gap_cm(1, rec['constants']), temperature, parameters)
    p10 = 1.07e-12 * temperature ** 1.5
    xi = 0.277 * 2.0 * temperature - 80.32 + 35.5 * ((v - 1.0) / 39.0) ** 0.8
    return v * (1.0 - chi) / (1.0 - chi * v) * _f(y) / _f(y10) * p10 / xi


def rate_vv(v, partner_low, temperature, parameters):
    """Eq. (14), (22), and (23) for N2(v)+N2(partner_low), cm^3/molecule/s."""
    bounds = parameters['record_source']['validity']['vv']
    partner_high = partner_low + 1
    vmax = bounds['deactivating_v'][1]
    wmax = bounds['partner_upper_w'][1]
    if not (1 <= v <= vmax and 0 <= partner_low < wmax):
        raise ValueError(f'Guerra Eq. (22)-(23) V-V refuses v={v}, partner={partner_low}')
    tmin, tmax = bounds['temperature_K']
    if not tmin <= temperature <= tmax:
        raise ValueError(f'Guerra Eq. (22)-(23) V-V refuses T={temperature:g} K; sourced range is 200-3500 K')
    rec = parameters['record_source']
    constants = rec['constants']
    omega = constants['omega_e_cm-1']
    chi = constants['omega_e_xe_cm-1'] / omega
    mismatch = _morse_gap_cm(v, constants) - _morse_gap_cm(partner_high, constants)
    y = _y_for_gap(mismatch, temperature, parameters)
    yref = _y_for_gap(0.0, temperature, parameters)
    p010 = 6.35e-17 * temperature ** 1.5
    vmax_w = max(v, partner_high)
    xi = (39.0625 - 1.5625 * vmax_w if vmax_w < 10 else
          25.2 + 24.1 * ((vmax_w - 10.0) / 30.0) ** 3)
    return (v * partner_high * (1.0 - chi) / (1.0 - chi * v)
            * (1.0 - chi) / (1.0 - chi * partner_high)
            * _f(y) / _f(yref) * p010 / xi)


def _temperature_grid(low, high):
    return sorted(set(range(low, high + 1, 25)) | {t for t in REFERENCE_TEMPERATURES if low <= t <= high} | {low, high})


def _reaction_entry(index, label, forward, temperatures, source, source_sha, equation, v_range, tmin, tmax):
    rates = [forward(t) * AVOGADRO for t in temperatures]
    if not all(math.isfinite(k) and k > 0 for k in rates):
        raise ValueError(f'nonpositive or nonfinite rate for {label}')
    safe = label.replace('"', '\\"')
    return f'''entry(
    index = {index},
    label = "{safe}",
    degeneracy = 1,
    kinetics = KineticsData(
        Tdata = ({temperatures!r}, 'K'),
        kdata = ({rates!r}, 'cm^3/(mol*s)'),
        Tmin = ({tmin}, 'K'),
        Tmax = ({tmax}, 'K'),
    ),
    reversible = True,
    shortDesc = "Guerra et al. (2019), Eq. ({equation}); sourced domain {tmin}-{tmax} K",
    longDesc = """Source: {source}, SHA-256 {source_sha}. Equation ({equation}); transition levels are within sourced v range {v_range}. Rate is tabulated from the exact sourced expression on the generated temperature grid. The reaction is reversible and RMG derives its reverse exclusively by detailed balance from the fixed-v N2Vibrational thermochemistry. The table interpolation is valid only over {tmin}-{tmax} K; generation and rate functions reject temperatures outside that interval.\n\nGuerra et al. report V-V near-resonant uncertainty of factors 2-3 at 1000 K and up to about 7 at 2000 K versus semiclassical calculations; this uncertainty is stated, not applied as a correction.""",
)
'''


def generate(parameters_raw, levels_raw, maximum_v=30):
    parameters = yaml.safe_load(parameters_raw)
    levels = json.loads(levels_raw)
    maximum_v = validate(parameters, levels, maximum_v)
    source = parameters['record_source']['citation']
    source_sha = parameters['record_source']['sha256']
    entries = []
    index = 0
    vt_t = _temperature_grid(*parameters['record_source']['validity']['vt']['temperature_K'])
    for v in range(1, maximum_v + 1):
        def forward(t, v=v):
            return rate_vt(v, t, parameters)
        label = f'N2v{v} + N2v0 <=> N2v{v - 1} + N2v0'
        entries.append(_reaction_entry(index, label, forward, vt_t, source, source_sha, '12, 20, 21', '1-45', 300, 3500))
        index += 1

    vv_t = _temperature_grid(*parameters['record_source']['validity']['vv']['temperature_K'])
    for v in range(1, maximum_v):
        for partner in range(v, maximum_v):
            # Adjacent-level exchange has identical reactant and product multisets.
            def forward(t, v=v, partner=partner):
                return rate_vv(v, partner, t, parameters)
            label = f'N2v{v} + N2v{partner} <=> N2v{v - 1} + N2v{partner + 1}'
            entries.append(_reaction_entry(index, label, forward, vv_t, source, source_sha, '14, 22, 23', 'v=1-44; partner upper=1-45', 200, 3500))
            index += 1
    header = '''# Generated by scripts/gen_n2_heavy_particle_relaxation.py; do not edit.
# ruff: noqa: F821
# ``entry`` and ``KineticsData`` are injected by the RMG library loader.
name = "N2HeavyParticleRelaxation"
shortDesc = "Guerra 2019 N2(X,v) V-T and V-V heavy-particle relaxation"
longDesc = """Sourced N2(X,v) ladder rates. Forward values follow Guerra et al. Eqs. (12), (14), (20)-(23) within their stated temperature and level ranges. Reactions are reversible; RMG derives reverse rates from the fixed-v N2Vibrational thermo. N2-Ar V-T is absent. Ar(1s)+N2 quenching is deferred because Velazco et al. provide only a 300 K total and the product states require N2 electronic species. N2-N V-T is outside scope."""

'''
    py = (header + '\n'.join(entries)).encode('utf-8')
    dictionary = []
    for row in levels['levels'][:maximum_v + 1]:
        v = row['v']
        dictionary.append(f'N2v{v}\nmultiplicity 1\nvibrationallevel {v}\n1 N u0 p1 c0 {{2,T}}\n2 N u0 p1 c0 {{1,T}}\n')
    return py, ('\n'.join(dictionary)).encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parameters', type=Path, default=PARAMETERS)
    parser.add_argument('--levels', type=Path, default=LEVELS)
    parser.add_argument('--output-dir', type=Path, default=OUTPUT_DIR)
    parser.add_argument('--max-v', type=int, default=30)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    py, dictionary = generate(args.parameters.read_bytes(), args.levels.read_bytes(), args.max_v)
    outputs = {'reactions.py': py, 'dictionary.txt': dictionary}
    if args.check:
        for name, contents in outputs.items():
            target = args.output_dir / name
            if not target.exists() or target.read_bytes() != contents:
                parser.error(f'{target} differs; regenerate with {Path(__file__).name}')
        print(f'{args.output_dir}: byte-reproducible')
    else:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for name, contents in outputs.items():
            (args.output_dir / name).write_bytes(contents)
        print(f'wrote {len(outputs)} files to {args.output_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
