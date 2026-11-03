#!/usr/bin/env python
"""Generate the N2 map from the local IST-Lisbon source and overlay."""
import argparse
import hashlib
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OVERLAY = ROOT / 'input/eedf/nitrogen_channel_overlay.yaml'
DEFAULT_OUTPUT = ROOT / 'input/eedf/nitrogen_channel_map.yaml'
TYPES = {'Elastic', 'Effective', 'Excitation', 'Ionization', 'Attachment'}


def parse_source(path):
    """Read process labels and thresholds without retaining cross sections."""
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    rows = []
    for i, line in enumerate(lines):
        kind = line.strip().title()
        if kind not in TYPES:
            continue
        if i + 2 >= len(lines):
            raise ValueError(f'{path}:{i + 1}: truncated collision header')
        process = next(
            (x.split(':', 1)[1].strip()
             for x in lines[i + 3:i + 20] if x.startswith('PROCESS:')),
            None,
        )
        if process is None:
            process = f'E + N2 -> E + N2, {kind}'
        parameter = lines[i + 2].strip().split()
        try:
            threshold = float(parameter[0]) if kind not in {
                'Elastic', 'Effective'} else 0.0
        except (ValueError, IndexError):
            raise ValueError(
                f'{path}:{i + 3}: malformed threshold/parameter line')
        rows.append(
            {'process': process, 'threshold_eV': threshold, 'type': kind})
    return rows


def generate(source, overlay_path):
    source = Path(source)
    rows = parse_source(source)
    overlay = yaml.safe_load(Path(overlay_path).read_text(encoding='utf-8'))
    if (not isinstance(overlay, dict)
            or overlay.get('schema') != 'eedf-channel-overlay/1'):
        raise ValueError('overlay schema missing or unsupported')
    if (not isinstance(overlay.get('collision_set'), str)
            or not overlay['collision_set']):
        raise ValueError('overlay collision_set must be a nonempty string')
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if overlay.get('source_sha256') != digest:
        raise ValueError('overlay source_sha256 does not match source file')
    channels = overlay.get('channels')
    if (not isinstance(channels, list) or len(channels) != len(rows)
            or not channels):
        count = len(channels) if isinstance(channels, list) else 'invalid'
        raise ValueError(
            f'overlay inventory has {count} rows; source has {len(rows)}')
    output = []
    seen_processes = set()
    for i, (row, channel) in enumerate(zip(rows, channels), 1):
        if not isinstance(channel, dict) or channel.get('id') != i:
            raise ValueError(f'channel {i}: id/order mismatch')
        if channel.get('process') != row['process']:
            raise ValueError(
                f'channel {i}: process differs from source: '
                f'{row["process"]!r}')
        if row['process'] in seen_processes:
            raise ValueError(f'channel {i}: duplicate source process identity')
        seen_processes.add(row['process'])
        if channel.get('threshold_eV') != row['threshold_eV']:
            raise ValueError(f'channel {i}: threshold differs from source')
        cls = channel.get('class')
        if cls not in {'A', 'B', 'C', 'D'}:
            raise ValueError(f'channel {i}: missing/invalid class')
        owner = channel.get('owner_index')
        library = channel.get('owner_library')
        label = channel.get('owner_label')
        if (cls == 'A' and (not isinstance(owner, int)
                            or not isinstance(library, str)
                            or not isinstance(label, str))):
            raise ValueError(
                f'channel {i}: class A requires owner index/library/label')
        if cls != 'A' and any(v is not None for v in (owner, library, label)):
            raise ValueError(
                f'channel {i}: non-A class cannot name a reaction owner')
        reason = channel.get('reason')
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f'channel {i}: classification reason is required')
        output.append(dict(channel))
    counts = {k: sum(c['class'] == k for c in output) for k in 'ABCD'}
    return {'schema': 'eedf-channel-map/1', 'set': overlay['collision_set'],
            'source_file': source.name, 'source_sha256': digest,
            'class_counts': counts, 'channels': output}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True,
                        help='local LoKI N2_LXCat.txt; not copied into git')
    parser.add_argument('--overlay', default=str(DEFAULT_OVERLAY))
    parser.add_argument('--output', default=str(DEFAULT_OUTPUT))
    parser.add_argument('--check', action='store_true',
                        help='require byte-identical generated output')
    args = parser.parse_args(argv)
    try:
        payload = yaml.safe_dump(
            generate(args.source, args.overlay), sort_keys=False,
            allow_unicode=True)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        parser.error(str(exc))
    out = Path(args.output)
    if args.check:
        if not out.is_file() or out.read_text(encoding='utf-8') != payload:
            print(
                f'{out}: stale or missing; regenerate with '
                'scripts/gen_nitrogen_channel_map.py', file=sys.stderr)
            return 1
        print(f'{out}: current')
        return 0
    out.write_text(payload, encoding='utf-8')
    print(f'wrote {out}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
