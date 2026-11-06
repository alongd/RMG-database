#!/usr/bin/env python
"""Generate the N2 map from the local IST-Lisbon source and overlay."""
import argparse
import hashlib
from pathlib import Path
import sys

import yaml
from yaml.constructor import ConstructorError
from rmgpy.data.kinetics.database import KineticsDatabase

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OVERLAY = ROOT / 'input/eedf/nitrogen_channel_overlay.yaml'
DEFAULT_OUTPUT = ROOT / 'input/eedf/nitrogen_channel_map.yaml'


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that refuses ambiguous duplicate mapping keys."""


def _construct_unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                'while constructing a mapping', node.start_mark,
                f'duplicate key {key!r}', key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)


def load_yaml(path):
    with Path(path).open(encoding='utf-8') as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)


def validate_owner_metadata(channel, library_dir, cache=None, collision_set=None):
    """Require a class-A owner to name the exact loadable library entry."""
    owner = channel.get('owner_index')
    library = channel.get('owner_library')
    label = channel.get('owner_label')
    if (isinstance(owner, bool) or not isinstance(owner, int) or owner <= 0
            or not isinstance(library, str) or not library.strip()
            or not isinstance(label, str) or not label.strip()):
        raise ValueError(
            'class A requires a positive integer owner index and nonempty '
            'owner library and label')
    cache = {} if cache is None else cache
    if library not in cache:
        database = KineticsDatabase()
        database.load_libraries(str(library_dir), libraries=[library])
        cache[library] = database.libraries[library]
    entries = cache[library].entries
    entry = entries.get(owner)
    if entry is None or entry.index != owner or entry.label != label:
        raise ValueError(
            f'class A owner {library}[{owner}] does not load as label {label!r}')

    from rmgpy.kinetics import EEDFChannel
    marker = entry.data
    if (not isinstance(marker, EEDFChannel) or marker.process != channel['process']
            or marker.collision_set != collision_set or marker.side != 'ine'):
        raise ValueError(f'class A owner {library}[{owner}] has a different collision identity')



def parse_source(path):
    """Use the solved PARAM/bracket identity, not the PROCESS display alias.

    Share the converter parser so the map and physical columns cannot drift.
    Only process/threshold metadata is retained in the generated YAML.
    """
    from rmgpy.tools.eedf.channels import _classic_sections
    from rmgpy.tools.eedf.schema import _file_hash
    return [{'process': row['description'], 'threshold_eV': row['threshold_eV'],
             'type': row['kind'].title()}
            for row in _classic_sections(str(path), _file_hash(path))]



def generate(source, overlay_path, library_dir=None):
    source = Path(source)
    rows = parse_source(source)
    overlay = load_yaml(overlay_path)
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
    owner_cache = {}
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
        if cls == 'A':
            validate_owner_metadata(
                channel, library_dir or ROOT / 'input/kinetics/libraries',
                owner_cache, overlay['collision_set'])
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
        try:
            if out.is_file():
                load_yaml(out)
        except (OSError, yaml.YAMLError) as exc:
            parser.error(f'{out}: invalid generated YAML: {exc}')
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
