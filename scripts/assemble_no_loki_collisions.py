#!/usr/bin/env python
"""Assemble the local Hayashi NO blocks with LoKI-B descriptors and provenance."""

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARCHIVE = Path('/home/alon/Data/lxcat/incoming/Hayashi.zip')
DEFAULT_STORE = Path('/home/alon/Data/lxcat/assembled/no-v1')
MEMBER = 'Cross section.txt'
SET = 'no-hayashi-v1'
ASSEMBLED_FILE = 'NO_assembled.txt'
HEADER = ('D-232 assembled NO collision set no-hayashi-v1 (LOCAL ONLY; LXCat data; never commit or upload).\n'
          'Each table is copied byte-for-byte from the Hayashi source block named in its D-232 provenance comment.\n'
          'LoKI-B reads the bracketed descriptor immediately after each PARAM line.\n\n')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def _blocks(data):
    """Return source collision blocks preserving every original byte."""
    lines = data.splitlines(keepends=True)
    if b''.join(lines) != data:
        raise ValueError('source block splitting lost bytes')
    rows, i, ordinal = [], 0, 0
    keywords = {b'ELASTIC', b'EFFECTIVE', b'EXCITATION', b'IONIZATION', b'ATTACHMENT'}
    while i < len(lines):
        value = lines[i].rstrip(b'\r\n')
        if value not in keywords:
            i += 1
            continue
        start, dashes = i, 0
        while i < len(lines) and dashes < 2:
            if lines[i].rstrip(b'\r\n').startswith(b'-----'):
                dashes += 1
            i += 1
        if dashes != 2:
            raise ValueError(f'truncated source collision block at line {start + 1}')
        ordinal += 1
        rows.append((ordinal, start + 1, b''.join(lines[start:i])))
    return rows


def _descriptor(channel):
    family = channel['family']
    kind = {'effective momentum transfer': 'Effective', 'lumped vibrational': 'Excitation',
            'electronic excitation': 'Excitation', 'dissociative attachment': 'Attachment',
            'ionization': 'Ionization'}[family]
    if family == 'effective momentum transfer':
        rhs = 'e + NO(X)'
    elif family == 'lumped vibrational':
        rhs = 'e + NO(' + channel['group'] + ')'
    elif family == 'electronic excitation':
        rhs = 'e + NO(' + channel['group'] + ')'
    elif family == 'dissociative attachment':
        rhs = 'N(4S) + O(-,gnd)'
    else:
        rhs = 'e + e + NO(+,gnd)'
    return f'[e + NO(X) -> {rhs}, {kind}]'


def build(archive):
    """Build collision bytes, manifest and provenance entirely in memory."""
    archive = Path(archive)
    archive_bytes = archive.read_bytes()
    try:
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as zf:
            if zf.namelist().count(MEMBER) != 1:
                raise ValueError(f'archive must contain exactly one {MEMBER}')
            source = zf.read(MEMBER)
    except zipfile.BadZipFile as exc:
        raise ValueError(f'cannot read Hayashi ZIP: {exc}') from exc

    sys.path.insert(0, str(ROOT / 'scripts'))
    import gen_no_eedf_channel_map as no  # imported after local generator path is known
    source_rows, attribution = no.source_channels(source)
    all_blocks = {ordinal: (line, raw) for ordinal, line, raw in _blocks(source)}
    by_source_block = {channel['source']['block']: channel for channel in source_rows}
    if len(by_source_block) != len(source_rows):
        raise ValueError('duplicate source block in NO inventory')
    output = [HEADER.encode('ascii')]
    provenance_rows = []
    process_rows = []
    block_hashes = {}
    for channel in source_rows:
        ordinal = channel['source']['block']
        if ordinal not in all_blocks:
            raise ValueError(f'NO source block {ordinal} is missing')
        line, raw = all_blocks[ordinal]
        expected_hash = channel['source']['block_sha256']
        if sha(raw.replace(b'\r\n', b'\n').replace(b'\r', b'\n')) != expected_hash:
            raise ValueError(f'NO source block {ordinal} hash differs from frozen inventory')
        raw_lines = raw.splitlines(keepends=True)
        param_indices = [i for i, row in enumerate(raw_lines) if b'PARAM.:' in row]
        if len(param_indices) != 1:
            raise ValueError(f'NO source block {ordinal} must have one PARAM line')
        p = param_indices[0]
        newline = b'\r\n' if b'\r\n' in raw_lines[p] else (b'\r' if raw_lines[p].endswith(b'\r') else b'\n')
        descriptor = _descriptor(channel)
        solver_process = descriptor[1:-1]
        provenance = (f'COMMENT: D-232 source=Hayashi.zip member={MEMBER} '
                      f'sha256={sha(archive_bytes)} member_sha256={sha(source)} block={ordinal} line={line} '
                      f'block_sha256={expected_hash}')
        emitted = b''.join(raw_lines[:p + 1]) + descriptor.encode('ascii') + newline + \
            provenance.encode('ascii') + newline + b''.join(raw_lines[p + 1:])
        # The data region itself is an unchanged byte slice from the source block.
        table_starts = [i for i, row in enumerate(raw_lines) if row.lstrip().startswith(b'-----')]
        if len(table_starts) < 2 or b''.join(raw_lines[table_starts[0]:table_starts[1] + 1]) not in emitted:
            raise ValueError(f'NO source block {ordinal} table was not preserved byte-for-byte')
        output.extend((b'\n', emitted))
        block_hashes[str(ordinal)] = expected_hash
        process_rows.append({'id': channel['id'], 'source_process': channel['source_process'],
                             'loki_process': solver_process, 'threshold_eV': channel['threshold_eV'],
                             'kind': channel['kind'], 'block': ordinal, 'line': line,
                             'block_sha256': expected_hash})
        provenance_rows.append([ordinal, line, expected_hash, solver_process, channel['threshold_eV']])
    collision_file = ASSEMBLED_FILE
    collision_bytes = b''.join(output)
    manifest = {
        'schema': 'lxcat-assembled/1', 'set': SET, 'ticket': 'D-232',
        'local_only': 'LXCat data; never committed to any repository and never uploaded',
        'loki_files': {collision_file: sha(collision_bytes)},
        'sources': {'Hayashi': {'file': archive.name, 'path': str(archive), 'sha256': sha(archive_bytes),
                                'database': attribution['database'], 'permlink': attribution['permlink'],
                                'member': MEMBER, 'member_sha256': sha(source),
                                'n_blocks': len(_blocks(source)), 'blocks_used': list(by_source_block),
                                'block_sha256': block_hashes}},
        'processes': process_rows,
        'not_assembled': [],
    }
    manifest_bytes = (json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode()
    sio = io.StringIO(newline='')
    writer = csv.writer(sio, delimiter='\t', lineterminator='\n')
    writer.writerow(['block', 'source_line', 'source_block_sha256', 'loki_process', 'threshold_eV'])
    writer.writerows(provenance_rows)
    return {collision_file: collision_bytes, 'manifest.json': manifest_bytes,
            'provenance.tsv': sio.getvalue().encode()}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', default=str(DEFAULT_ARCHIVE))
    parser.add_argument('--store', default=os.environ.get('EEDF_LXCAT_ASSEMBLED', str(DEFAULT_STORE)))
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args(argv)
    try:
        expected = build(args.archive)
        store = Path(args.store)
        if args.check:
            problems = [name for name, data in expected.items()
                        if not (store / name).is_file() or (store / name).read_bytes() != data]
            extras = sorted(p.name for p in store.iterdir() if p.is_file()) if store.is_dir() else []
            if problems or extras != sorted(expected):
                parser.error(f'{store}: stale, missing, malformed, or unexpected files: '
                             f'{problems}; extras={sorted(set(extras) - set(expected))}')
            print(f'{store}: current')
            return 0
        store.mkdir(parents=True, exist_ok=True)
        for name, data in expected.items():
            (store / name).write_bytes(data)
        print(f'wrote {store}')
        return 0
    except (OSError, ValueError, yaml.YAMLError) as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    raise SystemExit(main())
