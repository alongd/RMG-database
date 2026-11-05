#!/usr/bin/env python
"""Create the versioned local argon realization without changing cross-section bytes."""
import argparse
import hashlib
import json
from pathlib import Path
import re

BASE_HASHES = {
    'Ar_LXCat.txt': '4bcb328eff01c147a1ebb9cb31e01253344ae10fc9fa4bff508d76bce0f9d444',
    'Ar4s_assembled.txt': '5acea64cfb2ff9a5fd38aa222107a690eb809eda69ca242138fd9a1de4b8e395',
}


def transform(raw):
    """Change only four ground-to-4s descriptor arrows; retain every other byte."""
    pattern = rb'\[(Ar\(1S0\) \+ e -> Ar\((3P2|3P1|3P0|1P1)\) \+ e, Excitation)\]'
    changes = []
    def replace(match):
        state = match[2].decode('ascii')
        before = f'e + Ar(1S0) -> e + Ar({state}), Excitation'
        changes.append({'before': before, 'after': before.replace(' -> ', ' <-> ')})
        return match[0].replace(b' -> ', b' <-> ')
    converted = re.sub(pattern, replace, raw)
    if len(changes) != 4 or len({c['before'] for c in changes}) != 4:
        raise ValueError('expected four unique forward ground-to-4s descriptors')
    return converted, changes


def collect(assembled):
    """Pin the original ar-v1 snapshots and return derived bytes plus provenance."""
    output, files, changes = {}, {}, []
    for name, expected in BASE_HASHES.items():
        raw = (Path(assembled) / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError('base collision source hash mismatch: ' + name)
        if name == 'Ar_LXCat.txt':
            derived, changes = transform(raw)
        else:
            derived = raw
        output[name] = derived
        files[name] = {'base_sha256': expected, 'sha256': hashlib.sha256(derived).hexdigest()}
    return output, {'schema': 'argon-reversible-realization/1', 'name': 'ar-4s-electron-v1',
                    'files': files, 'descriptor_changes': changes,
                    'excited_fraction_max': 1e-5, 'argon_elimination_electron_density_max_m3': 1e18}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assembled', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.assembled.resolve() == args.output.resolve():
        parser.error('the derived realization must have a separate output directory')
    output, manifest = collect(args.assembled)
    output['realization.json'] = (json.dumps(manifest, indent=2, sort_keys=True) + '\n').encode()
    args.output.mkdir(parents=True, exist_ok=True)
    for name, data in output.items():
        path = args.output / name
        # Exclusive create: a concurrent writer cannot silently replace a pin.
        try:
            with path.open('xb') as stream:
                stream.write(data)
        except FileExistsError:
            if path.read_bytes() != data:
                raise ValueError('refusing to replace a different realization file: ' + str(path))
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
