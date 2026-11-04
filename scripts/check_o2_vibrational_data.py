#!/usr/bin/env python3
"""Validate the pinned O2 IST source and reproduce its K=10 ladder."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / 'input/eedf/o2_vibrational/sources.json'


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _generator():
    candidate = os.environ.get('RMG_PY_O2_SOURCE')
    if not candidate:
        raise RuntimeError('set RMG_PY_O2_SOURCE to the companion RMG-Py checkout')
    path = Path(candidate) / 'rmgpy/tools/eedf/n2_vibrational.py'
    if not path.is_file():
        raise RuntimeError('set RMG_PY_O2_SOURCE to the companion RMG-Py checkout')
    spec = importlib.util.spec_from_file_location('o2_n2_vibrational_generator', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_generator_manifest(data_root):
    module = _generator()
    record = json.loads(SOURCE.read_bytes())
    if record.get('schema') != 'o2-vibrational-source-manifest-v1':
        raise module.LadderError('unsupported O2 source manifest schema')
    root = Path(data_root).expanduser().resolve()
    if not root.is_dir():
        raise module.LadderError(f'EEDF_DATA_ROOT is not a directory: {root}')
    source = record['sources'][0]
    relative = Path(source['path'])
    path = (root / relative).resolve()
    if relative.is_absolute() or '..' in relative.parts or not path.is_relative_to(root):
        raise module.LadderError('O2 source path escapes EEDF_DATA_ROOT')
    if not path.is_file() or _sha(path) != source['sha256']:
        raise module.LadderError(f'O2 source missing or hash mismatch: {path}')
    pin = {'source_id': source['source_id'], 'path': str(path), 'sha256': source['sha256'],
           'citation': source['citation'], 'provenance': 'sourced'}
    sections = module.read_cross_sections(pin, molecule='O2')
    expected = {(v, w) for v in range(41) for w in range(v + 1, 42)}
    actual = {(item['initial_v'], item['final_v']) for item in sections}
    if len(sections) != source['process_count'] or actual != expected:
        raise module.LadderError(f'O2 pair coverage mismatch: {len(actual)} pairs')
    if source['selected_process_count'] != len(sections):
        raise module.LadderError('O2 selected process count mismatch')
    level_path = REPO / record['level_source']
    levels_data = json.loads(level_path.read_bytes())
    levels = {'path': str(level_path), 'sha256': _sha(level_path),
              'citation': levels_data['provenance']['citation'], 'provenance': 'sourced'}
    thermo_path = REPO / record['thermo_library']
    thermo = {'path': str(thermo_path), 'sha256': _sha(thermo_path),
              'citation': 'O2 fixed-v thermo derived from existing primary O2 thermo',
              'provenance': 'sourced'}
    return {'schema': 'o2-vibrational-source-v1', 'molecule': 'O2',
            'level_source': levels, 'cross_sections': [pin],
            'source_domain': record['source_domain'],
            'source_assignments': record['source_assignments'],
            'thermo_library': thermo,
            'energy_tolerance_eV': record['energy_tolerance_eV'],
            'D6': {'set_by': 'owner', 'top_fraction_limit': None,
                   'top_leak_share_limit': None, 'K_step': 5}}


def check(data_root):
    module = _generator()
    resolved = resolve_generator_manifest(data_root)
    artifacts = _portable_artifacts(module, resolved, data_root)
    expected = json.loads((REPO / 'input/eedf/o2_vibrational/ladder_k10.sha256.json').read_bytes())
    actual = _digest(artifacts)
    if actual != expected['sha256']:
        raise module.LadderError('O2 K=10 artifact digest mismatch')
    try:
        module.generate(resolved, 41, False, molecule='O2')
    except module.LadderError as exc:
        if 'uncovered initial v=41' not in str(exc):
            raise
    else:
        raise module.LadderError('O2 K=41 must refuse uncovered initial v=41')
    print(f'O2 source: {len(module.read_cross_sections(resolved["cross_sections"][0], molecule="O2"))} pairs')
    print(f'O2 K=10 artifact: {actual} reproducible')
    print('O2 K=41 refusal: uncovered initial v=41')


def _canonicalize(content, replacements):
    for absolute, stable in replacements.items():
        content = content.replace(absolute, stable)
    return content


def _portable_artifacts(module, resolved, data_root):
    """Replace resolver-specific path prefixes before hashing artifacts."""
    artifacts = module.generate(resolved, 10, False, molecule='O2')
    root = Path(data_root).expanduser().resolve()
    replacements = {
        str(root).encode(): b'EEDF_DATA_ROOT',
        str(REPO.resolve()).encode(): b'DATABASE_ROOT',
    }
    return {name: _canonicalize(content, replacements) for name, content in artifacts.items()}


def _digest(artifacts):
    digest = hashlib.sha256()
    for name, content in sorted(artifacts.items()):
        digest.update(name.encode() + b'\0' + len(content).to_bytes(8, 'big') + content)
    return digest.hexdigest()


def artifact_digest(data_root):
    module = _generator()
    resolved = resolve_generator_manifest(data_root)
    return _digest(_portable_artifacts(module, resolved, data_root))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--data-root', type=Path, required=True)
    args = parser.parse_args()
    if args.check:
        check(args.data_root)
    else:
        parser.error('pass --check')


if __name__ == '__main__':
    main()
