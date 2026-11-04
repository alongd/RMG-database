"""Local-only tests for deterministic Hayashi NO collision assembly."""

import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import assemble_no_loki_collisions as assembly  # noqa: E402
import gen_eedf_channel_map as gen  # noqa: E402
import gen_no_eedf_channel_map as no  # noqa: E402

ARCHIVE = os.environ.get('EEDF_NO_HAYASHI', '/home/alon/Data/lxcat/incoming/Hayashi.zip')
STORE = os.environ.get('EEDF_LXCAT_ASSEMBLED')
needs_store = pytest.mark.skipif(not STORE, reason='NO assembled store is unset (EEDF_LXCAT_ASSEMBLED)')
needs_archive = pytest.mark.skipif(not Path(ARCHIVE).is_file(), reason='local Hayashi archive is unavailable')


@needs_archive
def test_assembly_preserves_source_tables_and_emits_one_descriptor_per_no_block():
    built = assembly.build(ARCHIVE)
    assembled = built[assembly.ASSEMBLED_FILE].decode('ascii')
    with zipfile.ZipFile(ARCHIVE) as source:
        payload = source.read(assembly.MEMBER)
    channels, _ = no.source_channels(payload)
    source_blocks = {ordinal: raw for ordinal, _, raw in assembly._blocks(payload)}
    assert len(channels) == 10
    assert assembled.count('D-232 source=Hayashi.zip') == 10
    assert assembled.count('[') == 10
    for channel in channels:
        block = source_blocks[channel['source']['block']]
        rows = block.splitlines(keepends=True)
        dash = [i for i, line in enumerate(rows) if line.lstrip().startswith(b'-----')]
        source_table = b''.join(rows[dash[0]:dash[1] + 1])
        assert source_table in built[assembly.ASSEMBLED_FILE]
        assert hashlib.sha256(block.replace(b'\r\n', b'\n').replace(b'\r', b'\n')).hexdigest() == \
            channel['source']['block_sha256']


@needs_archive
def test_assembly_is_deterministic():
    first = assembly.build(ARCHIVE)
    second = assembly.build(ARCHIVE)
    assert first == second
    manifest = __import__('json').loads(first['manifest.json'])
    assert manifest['set'] == 'no-hayashi-v1'
    assert len(manifest['processes']) == 10
    assert len(manifest['sources']['Hayashi']['blocks_used']) == 10


@needs_store
@needs_archive
def test_named_store_passes_assembly_check():
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/assemble_no_loki_collisions.py'),
                             '--archive', ARCHIVE, '--store', STORE, '--check'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr + result.stdout
    assert 'current' in result.stdout


@needs_archive
def test_named_missing_or_malformed_store_fails_check(tmp_path):
    script = ROOT / 'scripts/assemble_no_loki_collisions.py'
    missing = tmp_path / 'missing'
    result = subprocess.run([sys.executable, str(script), '--archive', ARCHIVE,
                              '--store', str(missing), '--check'], capture_output=True, text=True)
    assert result.returncode == 2
    assert 'stale, missing, malformed' in result.stderr
    malformed = tmp_path / 'malformed'
    malformed.mkdir()
    for name, data in assembly.build(ARCHIVE).items():
        (malformed / name).write_bytes(data)
    (malformed / 'manifest.json').write_text('{}\n')
    result = subprocess.run([sys.executable, str(script), '--archive', ARCHIVE,
                             '--store', str(malformed), '--check'], capture_output=True, text=True)
    assert result.returncode == 2
    assert 'manifest.json' in result.stderr
