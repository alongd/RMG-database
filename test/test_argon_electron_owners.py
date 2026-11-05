"""Directional EEDF ownership and frozen stepwise-ionization conventions."""
from pathlib import Path
import sys
import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


def test_directional_collector_has_ten_sup_and_ten_new_ine_owners():
    import gen_argon_electron_owners as gen
    text = gen.render(yaml.safe_load(gen.CHANNEL_MAP.read_bytes()))
    records = []
    exec(compile(text, '<generated owners>', 'exec'),
         {'entry': lambda **kwargs: records.append(kwargs), 'EEDFChannel': lambda **kwargs: kwargs})
    assert len(records) == 20
    assert sum(r['kinetics']['side'] == 'sup' for r in records) == 10
    assert all(r['reversible'] is False for r in records)
    mixing = [r for r in records if 'mixing' in r['shortDesc']]
    assert len(mixing) == 12
    assert all('<->' in r['kinetics']['process'] for r in mixing)
    ions = [r for r in records if 'Ionization' in r['kinetics']['process']]
    assert len(ions) == 4
    assert {r['label'] for r in ions} == {
        f'{state} + e- => Arp + e- + e-' for state in ('Ars', 'Ar(1s4)', 'Ar(1s3)', 'Ar(1s2)')}
    assert all('4.2 eV' in r['longDesc'] for r in ions)
    assert len({r['index'] for r in records}) == 20


def test_overlay_preserves_reviewed_inverse_accounting():
    import gen_eedf_channel_map as gen
    root = Path(__file__).resolve().parents[1]
    rows, _, problems = gen.load_overlay_document(str(root / 'input/eedf/argon_channel_overlay.yaml'))
    assert problems == []
    inverse = [r['inverse'] for r in rows.values() if 'inverse' in r]
    assert sum(r['status'] == 'paired' for r in inverse) == 10
    assert sum(r['status'] == 'eliminated-upper-level' for r in inverse) == 33
    redistribution = [r for r in inverse if r['status'] == 'eliminated-upper-level-4s-redistribution']
    assert len(redistribution) == 104
    assert len({uid for r in redistribution for uid in r['levels']}) == 26


def test_reversible_realization_changes_descriptors_only():
    from realize_argon_collisions import transform
    original = b''.join((f'COMMENT: [Ar(1S0) + e -> Ar({s}) + e, Excitation]\n11.5\n0 1\n').encode()
                        for s in ('3P2', '3P1', '3P0', '1P1'))
    original += b'COMMENT: [Ar(1S0) + e -> Ar(4p[1/2]1) + e, Excitation]\n12.9\n1 2\n'
    changed, records = transform(original)
    assert len(records) == 4
    assert changed.count(b' <-> ') == 4
    assert changed.replace(b' <-> ', b' -> ') == original
    assert b'Ar(4p[1/2]1)' in changed


def test_owner_accounting_refuses_source_replaced_between_reads(monkeypatch):
    from argon_owner_accounting import load_owner_sources
    eedf = Path(__file__).resolve().parents[1] / 'input/eedf'
    original = Path.read_bytes
    reads = []
    def replaced(path):
        raw = original(path)
        if path == eedf / 'argon_radiative_data.yaml':
            reads.append(path)
            if len(reads) == 2:
                return raw + b'\n'
        return raw
    monkeypatch.setattr(Path, 'read_bytes', replaced)
    with pytest.raises(ValueError, match='changed during owner accounting'):
        load_owner_sources(eedf)
    assert len(reads) == 2


def test_realization_refuses_changed_pinned_source(tmp_path):
    from realize_argon_collisions import BASE_HASHES, collect
    for name in BASE_HASHES:
        (tmp_path / name).write_bytes(b'different bytes')
    with pytest.raises(ValueError, match='base collision source hash mismatch'):
        collect(tmp_path)
