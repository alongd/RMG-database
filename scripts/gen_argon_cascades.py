#!/usr/bin/env python
"""Generate E1 yields from sourced A values; never normalize an incomplete decay set."""
import argparse
from decimal import Decimal
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'input/eedf/argon_radiative_data.yaml'
OUTPUT = ROOT / 'input/eedf/argon_cascade_yields.yaml'
CHANNEL_MAP = ROOT / 'input/eedf/argon_channel_map.yaml'
FOUR_S_CHANNEL_IDS = list(range(45, 97)) + list(range(99, 125)) + list(range(128, 154))


def weighted_extreme(values, bounds, maximum=False):
    """Extremum of sum(A*x)/sum(A) over nonnegative independent rate intervals.

    A finite box reaches its extrema at a threshold vertex: rates below the
    optimal mean take one endpoint, rates above it the other. Unbounded rates
    add their limiting child values. This remains conservative when child
    intervals share uncertain downstream rates.
    """
    sign = -1 if maximum else 1
    ordered = sorted((sign*x, lo, hi) for x, (lo, hi) in zip(values, bounds))
    candidates = [x for x, _, hi in ordered if math.isinf(hi)]
    finite = [(x, lo, lo if math.isinf(hi) else hi) for x, lo, hi in ordered]
    for cut in range(len(finite) + 1):
        rates = [hi if i < cut else lo for i, (_, lo, hi) in enumerate(finite)]
        total = sum(rates)
        if total > 0:
            candidates.append(sum(rate*x for rate, (x, _, _) in zip(rates, finite))/total)
    if not candidates:
        raise ValueError('rate intervals admit no positive decay')
    return sign * min(candidates)


def escape_estimate(upper, ground, row, convention):
    """Declared Holstein slab estimates, with NIST resonance FWHM (Eq. 41).

    SI internally; NIST's linewidth expression takes Angstrom and cm^-3.
    This is the stipulated envelope of two limiting profiles, not a Voigt
    transport calculation or a rigorous bound for arbitrary line shapes.
    """
    if ground['energy_cm1'] != '0.0000' and float(ground['energy_cm1']) != 0:
        raise ValueError('radiation trapping is only permitted for a ground resonance line')
    if upper['J'] != 1 or upper['parity'] == ground['parity']:
        raise ValueError('invalid ground resonance line')
    t, p, length = (float(convention[k]) for k in ('temperature_K', 'pressure_Ar_torr', 'length_m'))
    if not all(math.isfinite(x) and x > 0 for x in (t, p, length)):
        raise ValueError('invalid trapping conditions')
    density = p * 101325 / 760 / (1.380649e-23 * t)
    if (length < convention['minimum_length_m']
            or density * length < convention['minimum_ground_column_m_2'] * (1-1e-14)
            or t > 298):
        raise ValueError('outside radiation-trapping validity range')
    a, lam = row['A_s_1'], row['vacuum_nm'] * 1e-9
    ratio = upper['g'] / ground['g']
    velocity = math.sqrt(2 * 1.380649e-23 * t / (convention['mass_u'] * 1.66053906660e-27))
    k_d = lam**3 * density * ratio * a / (8 * math.pi**1.5 * velocity)
    tau_d = k_d * length
    doppler = 1 if tau_d <= 1 else min(1., 1.875/(tau_d * math.sqrt(math.pi*math.log(tau_d))))
    angstrom = lam * 1e10
    oscillator = a * ratio * angstrom**2 / 6.6702e15
    width_angstrom = 8.6e-30 * ratio**-.5 * angstrom**3 * oscillator * density / 1e6
    width_hz = 299792458 * width_angstrom * 1e-10 / lam**2
    k_r = lam**2 * density * ratio * a / (4 * math.pi**2 * width_hz)
    resonance = min(1., 1.150/math.sqrt(math.pi*k_r*length))
    bound = max(doppler, resonance)
    if bound > convention['maximum_escape_factor'] or bound > .001:
        raise ValueError('ground-line escape factor exceeds 1e-3: ' + row['transition_id'])
    return dict(transition_id=row['transition_id'], provenance=row['provenance'],
                doppler=doppler, resonance=resonance, upper_estimate=bound,
                ground_column_m_2=density*length)


def derive_higher(data, anchors):
    """Close the explicitly accounted DAG, retaining all uncertainty records."""
    model = data['higher_cascade']
    products = ['Ar(1s5)', 'Ar(1s4)', 'Ar(1s3)', 'Ar(1s2)']
    levels = {x['nist_id']: x for x in model['levels']}
    if len(levels) != len(model['levels']):
        raise ValueError('duplicate higher level')
    for u in levels.values():
        if (u['citation'] not in data['queries'] or u['g'] != 2*u['J']+1
                or u['parity'] not in ('odd', 'even') or not math.isfinite(float(u['energy_cm1']))):
            raise ValueError('invalid higher level or citation')
    ground = '018001.000001'
    conventions = model['conventions']
    trapping = conventions['RESONANCE_RADIATION_TRAPPED']
    if 'HIGHER_EXCITATION_STATISTICAL_WEIGHTS' not in conventions:
        raise ValueError('missing statistical blend convention')
    omitted_id = '018001.000058->018001.000002'
    omission = conventions.get('CALCULATED_LIST_OMISSION_BOUND', {})
    if omission.get('transition_id') != omitted_id or omission.get('method') != 'terminal-segment':
        raise ValueError('missing explicit terminal omission record')
    rates = {}
    for row in model['transitions']:
        u, l = row['upper_nist_id'], row['lower_nist_id']
        if (row['transition_id'] != u+'->'+l or row['type'] != 'E1'
                or row.get('citation') not in data['queries'] or (u, l) in rates):
            raise ValueError('invalid higher transition identity/citation or duplicate')
        if row.get('accuracy') not in model['accuracy_relative']:
            raise ValueError('missing A accuracy class')
        if row.get('status') == 'unbounded-omitted':
            if (row['transition_id'] != omitted_id or row.get('A_s_1') is not None
                    or row.get('convention') != 'CALCULATED_LIST_OMISSION_BOUND'):
                raise ValueError('invalid terminal omission record')
        elif (row.get('status') != 'numeric' or row.get('provenance') not in ('nist', 'calculated:K11')
              or not isinstance(row.get('A_s_1'), (float, int))
              or not math.isfinite(row['A_s_1']) or row['A_s_1'] <= 0):
            raise ValueError('numeric higher A must be finite and positive; omitted is not zero')
        if row.get('convention') == 'RESONANCE_RADIATION_TRAPPED' and l != ground:
            raise ValueError('non-ground branch cannot declare resonance trapping')
        rates[u, l] = row

    def expected(u):
        a = levels[u]
        return {(u, l) for l, b in levels.items()
                if float(b['energy_cm1']) < float(a['energy_cm1']) and a['parity'] != b['parity']
                and abs(a['J']-b['J']) <= 1 and a['J']+b['J'] > 0}

    def interval(row):
        if row.get('status') == 'unbounded-omitted':
            return (0., math.inf)
        error = model['accuracy_relative'][row['accuracy']]
        if error is None:
            return (0., math.inf)
        if not math.isfinite(error) or not 0 <= error <= 1:
            raise ValueError('invalid finite A accuracy range')
        return (row['A_s_1']*(1-error), row['A_s_1']*(1+error))

    vectors, lows, highs, calc_share, flux, escaped, identities = {}, {}, {}, {}, {}, {}, {}
    for i, product in enumerate(products, 2):
        uid = f'018001.{i:06d}'
        vectors[uid] = [float(p == product) for p in products]
        lows[uid] = highs[uid] = vectors[uid]
        calc_share[uid] = flux[uid] = escaped[uid] = 0.
        identities[uid] = set()
    vectors[ground] = lows[ground] = highs[ground] = [0.]*4
    calc_share[ground] = flux[ground] = 0.
    escaped[ground] = 1.
    identities[ground] = set()
    for c in anchors:
        u = c['upper_nist_id']
        vectors[u] = [c['product_yields'][p] for p in products]
        old = [r for r in data['transitions'] if r['channel_id'] == c['id']]
        bounds = [(0., float(r['A_upper_bound_s-1'])) if float(r['A_s-1']) == 0 else
                  interval(dict(A_s_1=float(r['A_s-1']), accuracy=r['accuracy'])) for r in old]
        for result, maximum in ((lows, False), (highs, True)):
            result[u] = [weighted_extreme([vectors[r['lower_nist_id']][j] for r in old], bounds, maximum)
                         for j in range(4)]
        calc_share[u] = flux[u] = escaped[u] = 0.
        identities[u] = set(c['transition_ids'])
    target_ids = {u for c in data['higher_channels'] for u in c['upper_nist_ids']}
    needed, todo = set(), list(target_ids)
    while todo:
        u = todo.pop()
        if u in vectors or u in needed:
            continue
        if u not in levels:
            raise ValueError('missing higher level')
        needed.add(u)
        todo.extend(l for _, l in expected(u))
    all_expected = set().union(*(expected(u) for u in needed))
    if set(rates) != all_expected:
        raise ValueError('incomplete or extra outgoing higher E1 transition set')
    ground_lines, lifetime_reports = [], {}
    for u in sorted(needed, key=lambda x: float(levels[x]['energy_cm1'])):
        outgoing = [rates[pair] for pair in sorted(expected(u))]
        # A=0 is only the declared nominal endpoint for the one terminal segment.
        values = [r['A_s_1'] or 0. for r in outgoing]
        bounds = [interval(r) for r in outgoing]
        g_rate = 0.
        for i, r in enumerate(outgoing):
            if r['lower_nist_id'] == ground:
                estimate = escape_estimate(levels[u], levels[ground], r, trapping)
                ground_lines.append(estimate)
                g_rate = values[i] * estimate['upper_estimate']
                values[i] = 0.
                bounds[i] = (0., bounds[i][1] * estimate['upper_estimate'])
        total = sum(values)
        if not math.isfinite(total) or total <= 0:
            raise ValueError('no positive non-ground decay sum')
        weights = [v/total for v in values]
        children = [r['lower_nist_id'] for r in outgoing]
        vectors[u] = [sum(w*vectors[l][j] for w, l in zip(weights, children)) for j in range(4)]
        lows[u] = [weighted_extreme([lows[l][j] for l in children], bounds) for j in range(4)]
        highs[u] = [weighted_extreme([highs[l][j] for l in children], bounds, True) for j in range(4)]
        calc_share[u] = sum(w*(1 if r['provenance'].startswith('calculated:') else calc_share[l])
                            for w, l, r in zip(weights, children, outgoing))
        flux[u] = 1. if u == '018001.000058' else sum(w*flux[l] for w, l in zip(weights, children))
        escaped[u] = (g_rate + sum(v*escaped[l] for v, l in zip(values, children)))/(total+g_rate)
        identities[u] = {r['transition_id'] for r in outgoing}.union(*(identities[l] for l in children))
        for measurement in model['lifetimes']:
            if measurement['nist_id'] != u:
                continue
            if measurement['reference'] not in data['references']:
                raise ValueError('missing lifetime citation')
            lifetime = measurement['lifetime_ns']
            error = measurement['standard_error_ns'] + lifetime*measurement['systematic_fraction']
            if not 0 < error < lifetime:
                raise ValueError('invalid lifetime uncertainty')
            observed = [1e9/(lifetime+error), 1e9/(lifetime-error)]
            raw_bounds = [interval(r) for r in outgoing]
            low, high = (sum(x[i] for x in raw_bounds) for i in (0, 1))
            if low > observed[1] or high < observed[0]:
                raise ValueError('mixed A sum contradicts sourced lifetime: ' + u)
            nominal = sum(r['A_s_1'] or 0. for r in outgoing)
            lifetime_reports[u] = dict(reference=measurement['reference'], rate_interval_s_1=observed,
                                       mixed_sum_A_s_1=nominal, mixed_sum_interval_s_1=[low, None if math.isinf(high) else high],
                                       nominal_within_measurement=observed[0] <= nominal <= observed[1],
                                       comparison='interval-overlap; unrated K11 ranges do not establish quantitative agreement')
    output = []
    omitted_vector = vectors['018001.000058']
    terminal = [1., 0., 0., 0.]
    distance = sum(abs(x-y) for x, y in zip(omitted_vector, terminal))/2
    for c in data['higher_channels']:
        ids = c['upper_nist_ids']
        weights = c['excitation_weights']
        denominator = sum(levels[u]['g'] for u in ids)
        if (len(set(ids)) != len(ids) or set(weights) != set(ids)
                or any(not math.isfinite(weights[u])
                       or abs(weights[u]-levels[u]['g']/denominator) > 1e-14 for u in ids)):
            raise ValueError('invalid statistical excitation weights')
        vector = [sum(weights[u]*vectors[u][j] for u in ids) for j in range(4)]
        share = sum(weights[u]*flux[u] for u in ids)
        endpoint = [x+share*(b-a) for x, a, b in zip(vector, omitted_vector, terminal)]
        all_ids = set().union(*(identities[u] for u in ids))
        output.append(dict(id=c['id'], process=c['process'], threshold_eV=c['threshold_eV'],
                           upper_nist_ids=ids, excitation_weights=weights, status='complete_for_E1',
                           product_yields=dict(zip(products, vector)), missing_transitions=[],
                           transition_ids=sorted(all_ids),
                           calculated_path_share=sum(weights[u]*calc_share[u] for u in ids),
                           yield_intervals={p: [max(0., sum(weights[u]*lows[u][j] for u in ids)),
                                                min(1., sum(weights[u]*highs[u][j] for u in ids))]
                                            for j, p in enumerate(products)},
                           ground_escape_fraction_upper_at_nominal_A=sum(weights[u]*escaped[u] for u in ids),
                           ground_lines=[r for r in ground_lines if r['transition_id'] in all_ids],
                           omission_interval=dict(status='unbounded-omitted', transition_id=omitted_id,
                                                  flux_share=share, total_variation_radius=share*distance,
                                                  endpoints=[dict(zip(products, vector)), dict(zip(products, endpoint))]),
                           blend_sensitivity=dict(total_variation_diameter=max(
                               sum(abs(x-y) for x, y in zip(vectors[u], vectors[v]))/2 for u in ids for v in ids),
                               product_extremes={p: [min(vectors[u][j] for u in ids), max(vectors[u][j] for u in ids)]
                                                 for j, p in enumerate(products)}),
                           lifetime_checks={u: r for u, r in lifetime_reports.items()
                                            if any(t.startswith(u+'->') for t in all_ids)}))
    return output


def derive_four_s(data, anchors, channel_map_raw):
    """Resolve each 4s collision to one sourced upper level, never a blended group."""
    frozen = yaml.safe_load(channel_map_raw)
    selected = [c for c in frozen['channels'] if 'from 4s via' in c['family']]
    if [c['id'] for c in selected] != FOUR_S_CHANNEL_IDS:
        raise ValueError('expected exactly 104 4s cascade collisions')
    catalog = {}
    for level in data['higher_cascade']['levels']:
        term = re.search(r'\[([^]]+)\]', level['term'])
        if term is None:
            continue
        orbital = level['configuration'].rsplit('.', 1)[1]
        prime = "'" if '<1/2>' in level['configuration'] else ''
        label = f'Ar({orbital}{prime}[{term[1]}]{level["J"]})'
        if label in catalog:
            raise ValueError('ambiguous sourced upper level: ' + label)
        catalog[label] = level['nist_id']
    base = {c['upper_nist_id']: c for c in anchors}
    extended = deepcopy(data)
    output = []
    for row in selected:
        match = re.fullmatch(r'e \+ Ar\((3P2|3P1|3P0|1P1)\) -> e \+ (Ar\(.+\)), Excitation', row['loki_process'])
        if match is None or match[2] not in catalog:
            raise ValueError('unknown 4s collision source or upper level: ' + row['loki_process'])
        uid = catalog[match[2]]
        identity = dict(id=row['id'], process=row['loki_process'], threshold_eV=row['threshold_eV'],
                        upper_nist_ids=[uid], excitation_weights={uid: 1.})
        if uid in base:
            channel = deepcopy(base[uid])
            channel.update(identity)
            output.append(channel)
        else:
            extended['higher_channels'].append(identity)
    output.extend(c for c in derive_higher(extended, anchors) if c['id'] in FOUR_S_CHANNEL_IDS)
    if len(output) != 104 or sum(c['upper_nist_ids'][0] in base for c in output) != 40:
        raise ValueError('expected 40 4p and 64 higher singleton cascades')
    return sorted(output, key=lambda c: c['id'])


def generate(raw, channel_map_raw=None):
    """Validate a single source snapshot and return deterministic, non-runtime data."""
    data = yaml.safe_load(raw)
    if data['schema_version'] != 1 or data['radiative_model'] != 'E1':
        raise ValueError('only the sourced E1 model is supported')
    queries = data['queries']
    for query in queries.values():
        if not query.get('url') or not query.get('retrieved_utc') or len(query.get('sha256', '')) != 64:
            raise ValueError('query provenance is incomplete')
    for row in data['levels'] + data['transitions'] + data['higher_channels'] + [data['completeness']]:
        if row.get('citation') not in queries:
            raise ValueError('missing citation')
    audit = data['completeness']
    if audit['escape_lines']:
        raise ValueError('unmodelled escape transition: E1 closure is not established')
    levels = {r['nist_id']: r for r in data['levels']}
    if len(levels) != 14 or len(data['levels']) != 14:
        raise ValueError('expected four 4s and ten 4p levels')
    lower = [r for r in data['levels'] if r['paschen'].startswith('1s')]
    if {r['paschen'] for r in lower} != {'1s5', '1s4', '1s3', '1s2'}:
        raise ValueError('incomplete 4s manifold')
    for level in levels.values():
        if level['g'] != 2 * level['J'] + 1:
            raise ValueError('invalid level degeneracy')
    channels = data['channels']
    if [c['id'] for c in channels] != list(range(6, 16)):
        raise ValueError('expected channels 6–15 exactly once')
    if [c['id'] for c in data['higher_channels']] != list(range(16, 39)):
        raise ValueError('expected higher channels 16–38 exactly once')
    transitions = data['transitions']
    upper_bound_rows = [t for t in transitions
                        if t.get('A_source_status') == 'upper_bound_adopted_as_zero_for_branching']
    expected_pairs = set()
    output = []
    for channel in channels:
        upper = levels[channel['upper_nist_id']]
        allowed = [lo for lo in lower if upper['parity'] != lo['parity']
                   and abs(upper['J'] - lo['J']) <= 1 and upper['J'] + lo['J'] != 0]
        pairs = {(upper['nist_id'], lo['nist_id']) for lo in allowed}
        expected_pairs |= pairs
        rows = [t for t in transitions if t['channel_id'] == channel['id']]
        if {(t['upper_nist_id'], t['lower_nist_id']) for t in rows} != pairs or len(rows) != len(pairs):
            raise ValueError('incomplete or duplicate outgoing E1 transition set')
        missing, rates = [], {}
        for t in rows:
            if t['type'] != 'E1' or t['transition_id'] != t['upper_nist_id'] + '->' + t['lower_nist_id']:
                raise ValueError('invalid transition identity')
            state = 'Ar(' + levels[t['lower_nist_id']]['paschen'] + ')'
            if t['product_state'] != state:
                raise ValueError('transition product identity mismatch')
            value = t['A_s-1']
            if value is None:
                if any(key in t for key in ('A_source_status', 'A_upper_bound_operator',
                                            'A_upper_bound_s-1', 'nist_A_s-1')):
                    raise ValueError('channel-11 upper-bound A must retain its effective zero value')
                missing.append(t['transition_id'])
                continue
            reference = data['references'].get(t['tp_ref'])
            if not reference or not (reference.get('url') or
                                     (reference.get('local_path') and
                                      reference['local_path'].startswith('/') and
                                      re.fullmatch('[0-9a-f]{64}', reference.get('sha256', '')))):
                raise ValueError('missing A citation')
            a = Decimal(str(value))
            if not a.is_finite() or a < 0:
                raise ValueError('A must be finite and nonnegative; missing is null')
            if a == 0:
                if (t.get('A_source_status') != 'upper_bound_adopted_as_zero_for_branching'
                        or t.get('A_upper_bound_operator') != '<'
                        or t.get('nist_A_s-1') is not None
                        or t['tp_ref'] != 'Wiese1989_local_upper_bound'
                        or t['channel_id'] != 11
                        or t['transition_id'] != '018001.000011->018001.000005'):
                    raise ValueError('zero A requires the explicit channel-11 upper-bound source')
                bound = Decimal(str(t.get('A_upper_bound_s-1')))
                if not bound.is_finite() or bound <= 0:
                    raise ValueError('channel-11 upper bound must be finite and positive')
            elif any(key in t for key in ('A_source_status', 'A_upper_bound_operator',
                                         'A_upper_bound_s-1', 'nist_A_s-1')):
                raise ValueError('upper-bound metadata is valid only for the adopted zero A')
            rates[state] = a
        total = sum(rates.values(), Decimal(0))
        yields = None if missing else {'Ar(' + lo['paschen'] + ')': float(rates.get('Ar(' + lo['paschen'] + ')', 0) / total) for lo in lower}
        branching_error_bound = None
        bounded = [t for t in rows if t.get('A_source_status') == 'upper_bound_adopted_as_zero_for_branching']
        if bounded:
            if len(bounded) != 1 or total <= 0:
                raise ValueError('expected one channel-11 A upper bound and positive known sum')
            bound = Decimal(str(bounded[0]['A_upper_bound_s-1']))
            branching_error_bound = {
                'transition_id': bounded[0]['transition_id'],
                'source_ref': bounded[0]['tp_ref'],
                'operator': bounded[0]['A_upper_bound_operator'],
                'bound_s-1': str(bound),
                'sum_known_A_s-1': str(total),
                'maximum_branching_error': float(bound / total),
            }
        output.append(dict(channel, status='unresolved' if missing else 'complete_for_E1',
                           product_yields=yields, missing_transitions=missing,
                           transition_ids=[t['transition_id'] for t in rows],
                           **({'branching_error_bound': branching_error_bound}
                              if branching_error_bound is not None else {})))
    if len(transitions) != len(expected_pairs):
        raise ValueError('unexpected escape or extra transition')
    measured_rows = [t for t in transitions if t['A_s-1'] is not None and t not in upper_bound_rows]
    if (audit.get('known_A') != len(measured_rows)
            or audit.get('upper_bound_A', 0) != len(upper_bound_rows)):
        raise ValueError('completeness audit counts differ from measured and upper-bound A rows')
    output.extend(derive_higher(data, output))
    if channel_map_raw is not None:
        output.extend(derive_four_s(data, output[:10], channel_map_raw))
    return dict(schema_version=1, radiative_model='E1', source_sha256=hashlib.sha256(raw).hexdigest(), channels=output)


def require_yields(document, channel_id):
    """Refuse requests for a usable vector where source data remain incomplete."""
    channel = next(c for c in document['channels'] if c['id'] == channel_id)
    if channel['status'] != 'complete_for_E1' or channel['product_yields'] is None:
        raise ValueError(f'channel {channel_id}: unresolved radiative yields')
    return channel['product_yields']


def render(document):
    return '# Generated by scripts/gen_argon_cascades.py; do not edit.\n' + yaml.safe_dump(document, sort_keys=False, allow_unicode=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=SOURCE)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--channel-map', type=Path, default=CHANNEL_MAP)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    document = generate(args.source.read_bytes(), args.channel_map.read_bytes())
    text = render(document)
    if args.check:
        if not args.output.exists() or args.output.read_text() != text:
            parser.error('generated yields differ; regenerate with scripts/gen_argon_cascades.py')
    else:
        args.output.write_text(text)
    print(f'argon E1 yields: {len(document["channels"])} complete channels; higher-family uncertainty intervals reported')
    return 0


if __name__ == '__main__':
    sys.exit(main())
