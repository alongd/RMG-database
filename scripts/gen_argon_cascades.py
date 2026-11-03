#!/usr/bin/env python
"""Generate E1 yields from sourced A values; never normalize an incomplete decay set."""
import argparse
from decimal import Decimal
import hashlib
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'input/eedf/argon_radiative_data.yaml'
OUTPUT = ROOT / 'input/eedf/argon_cascade_yields.yaml'


def generate(raw):
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
                missing.append(t['transition_id'])
                continue
            if t['tp_ref'] not in data['references'] or not data['references'][t['tp_ref']].get('url'):
                raise ValueError('missing A citation')
            a = Decimal(str(value))
            if not a.is_finite() or a <= 0:
                raise ValueError('A must be finite and positive; missing is null, not zero')
            rates[state] = a
        total = sum(rates.values(), Decimal(0))
        yields = None if missing else {'Ar(' + lo['paschen'] + ')': float(rates.get('Ar(' + lo['paschen'] + ')', 0) / total) for lo in lower}
        output.append(dict(channel, status='unresolved' if missing else 'complete_for_E1',
                           product_yields=yields, missing_transitions=missing,
                           transition_ids=[t['transition_id'] for t in rows]))
    if len(transitions) != len(expected_pairs):
        raise ValueError('unexpected escape or extra transition')
    for channel in data['higher_channels']:
        if channel['status'] != 'unresolved' or channel['product_yields'] is not None or channel['excitation_weights'] is not None:
            raise ValueError('higher-channel yields and weights remain unsourced')
        output.append({k: channel[k] for k in ['id', 'process', 'threshold_eV', 'status', 'product_yields', 'reason']})
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
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    text = render(generate(args.source.read_bytes()))
    if args.check:
        if not args.output.exists() or args.output.read_text() != text:
            parser.error('generated yields differ; regenerate with scripts/gen_argon_cascades.py')
    else:
        args.output.write_text(text)
    print('argon E1 yields: nine complete; channel 11 and channels 16–38 unresolved')
    return 0


if __name__ == '__main__':
    sys.exit(main())
