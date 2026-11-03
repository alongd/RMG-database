#!/usr/bin/env python3
"""Validate local Laporta inputs and reproducibly check K=10 and K=29 artifacts."""
import argparse
import hashlib
import json
import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_MANIFEST = REPO_ROOT / 'input/eedf/n2_vibrational/sources.json'


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_generator_manifest(data_root):
    """Resolve root-relative source metadata into hash-pinned generator inputs."""
    from rmgpy.tools.eedf.n2_vibrational import LadderError

    root = Path(data_root).expanduser().resolve()
    if not root.is_dir():
        raise LadderError(f'EEDF_DATA_ROOT is not a directory: {root}')
    record = json.loads(SOURCE_MANIFEST.read_bytes())
    if record.get('schema') != 'n2-vibrational-source-manifest-v1':
        raise LadderError('unsupported committed N2 source manifest schema')
    cross_sections = []
    for source in record['sources']:
        relative = Path(source['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise LadderError(f'source path must stay relative to EEDF_DATA_ROOT: {relative}')
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise LadderError(f'source path escapes EEDF_DATA_ROOT: {relative}')
        if not path.is_file():
            raise LadderError(f'missing local source file: {path}')
        if _sha256(path) != source['sha256']:
            raise LadderError(f'source hash mismatch: {path}')
        pin = {'source_id': source['source_id'], 'path': str(path),
               'sha256': source['sha256'], 'citation': source['citation'],
               'provenance': 'sourced'}
        if source.get('member'):
            pin['member'] = source['member']
        cross_sections.append(pin)

    levels_path = REPO_ROOT / record['level_source']
    levels = json.loads(levels_path.read_bytes())
    level_source = {'path': str(levels_path), 'sha256': _sha256(levels_path),
                    'citation': levels['provenance']['energy_source'] + ' ' +
                                levels['provenance']['citation'],
                    'provenance': 'sourced'}
    thermo_path = REPO_ROOT / record['thermo_library']
    thermo_pin = {'path': str(thermo_path), 'sha256': _sha256(thermo_path),
                  'citation': 'Fixed-v N2(X) thermo; primaryThermoLibrary N2 with ensemble vibration removed.',
                  'provenance': 'sourced'}
    resolved = {
        'schema': 'n2-vibrational-source-v1',
        'level_source': level_source,
        'cross_sections': cross_sections,
        'source_domain': record['source_domain'],
        'source_assignments': record['source_assignments'],
        'thermo_library': thermo_pin,
        'energy_tolerance_eV': record['energy_tolerance_eV'],
        'D6': {'set_by': 'owner', 'top_fraction_limit': None,
               'top_leak_share_limit': None, 'K_step': 5},
    }
    from rmgpy.tools.eedf.n2_vibrational import read_cross_sections
    selected_counts = {pin['source_id']: 0 for pin in cross_sections}
    for pin in cross_sections:
        sections = read_cross_sections(pin)
        expected = next(s['process_count'] for s in record['sources']
                        if s['source_id'] == pin['source_id'])
        if len(sections) != expected:
            raise LadderError(f"process count mismatch for {pin['source_id']}: {len(sections)} != {expected}")
        selected_counts[pin['source_id']] = sum(
            record['source_assignments'].get(str(section['initial_v'])) == pin['source_id']
            for section in sections)
    for source in record['sources']:
        source_id = source['source_id']
        if selected_counts[source_id] != source['selected_process_count']:
            raise LadderError(f"selected process count mismatch for {source_id}: "
                              f"{selected_counts[source_id]} != {source['selected_process_count']}")
    return resolved


def _artifact_digest(artifacts):
    digest = hashlib.sha256()
    for name, content in sorted(artifacts.items()):
        digest.update(name.encode('utf-8') + b'\0')
        digest.update(len(content).to_bytes(8, 'big'))
        digest.update(content)
    return digest.hexdigest()


def check_ladder_inputs(data_root, K_values=(10, 29)):
    """Run the real generator and verify its physical-input/runtime contract."""
    from rmgpy.tools.eedf.n2_vibrational import LadderError, generate

    resolved = resolve_generator_manifest(data_root)
    expected_requirements = [
        'coupling automatically executes D6 regeneration before accepting a run',
        'physical Ar+N2 arm qualification requires a channel map and owners; the converter currently accepts PlasmaArgon owners only',
    ]
    results = []
    for K in K_values:
        artifacts = generate(resolved, K=K, production=False)
        output = json.loads(artifacts['manifest.json'])
        if output['runtime_ready'] is not False:
            raise LadderError('runtime_ready must remain false until coupling requirements are implemented')
        if output['runtime_requirements'] != expected_requirements:
            raise LadderError('generator runtime requirements changed unexpectedly')
        if (not output['source_complete'] or output['source_upper_v'] != 58
                or output['source_initial_levels'] != list(range(30))):
            raise LadderError('generator did not validate the declared physical source domain')
        if any(channel.get('kind') != 'vibrational' for channel in output['channels']):
            raise LadderError('unexpected non-vibrational channel in N2 ladder')
        results.append({
            'K': K,
            'states': len(output['states']),
            'source_records': len(output['transition_audit']),
            'forward_channels': sum(c['direction'] == 'forward' for c in output['channels']),
            'superelastic_channels': sum(c['direction'] == 'superelastic' for c in output['channels']),
            'top_leak_records': len(output['top_leak_ledger']),
            'runtime_ready': output['runtime_ready'],
            'runtime_requirements': output['runtime_requirements'],
            'sha256': _artifact_digest(artifacts),
        })
    try:
        generate(resolved, K=30, production=False)
    except LadderError as exc:
        expected = 'requested K=30 requires uncovered initial v=30'
        if expected not in str(exc):
            raise LadderError(f'K=30 refusal did not name the uncovered initial level: {exc}') from exc
        refusal = str(exc)
    else:
        raise LadderError('K=30 unexpectedly accepted uncovered initial v=30')
    return {'ladders': results, 'K30_refusal': refusal}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='validate and print reproducible K=10/K=29 summaries')
    parser.add_argument('--data-root', type=Path, default=os.environ.get('EEDF_DATA_ROOT'))
    args = parser.parse_args()
    if not args.check:
        parser.error('pass --check to validate the local source set')
    if args.data_root is None:
        parser.error('set EEDF_DATA_ROOT or pass --data-root')
    print(json.dumps(check_ladder_inputs(args.data_root), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
