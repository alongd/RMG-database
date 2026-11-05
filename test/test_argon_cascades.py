"""Sourced radiative vectors are reproducible, complete for E1, or explicitly refused."""
from copy import deepcopy
from pathlib import Path
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import gen_argon_cascades as gen
import gen_argon_cascade_reactions as reaction_gen


def test_reproducible_and_literal_branch():
    doc = gen.generate(gen.SOURCE.read_bytes(), gen.CHANNEL_MAP.read_bytes())
    assert gen.render(doc) == gen.OUTPUT.read_text()
    assert gen.require_yields(doc, 6) == pytest.approx({
        'Ar(1s5)': 0.7420494699646643, 'Ar(1s4)': 0.2120141342756184,
        'Ar(1s3)': 0.03847663918335296, 'Ar(1s2)': 0.00745975657636435})
    complete = [c for c in doc['channels'] if c['status'] == 'complete_for_E1']
    assert [c['id'] for c in complete] == (list(range(6, 39)) + list(range(45, 97))
                                            + list(range(99, 125)) + list(range(128, 154)))
    for c in complete:
        assert sum(c['product_yields'].values()) == pytest.approx(1, rel=0, abs=1e-12)
    ch11 = next(c for c in complete if c['id'] == 11)
    assert ch11['product_yields'] == {
        'Ar(1s5)': 0.0, 'Ar(1s4)': 1.0, 'Ar(1s3)': 0.0, 'Ar(1s2)': 0.0}
    assert ch11['branching_error_bound'] == {
        'transition_id': '018001.000011->018001.000005',
        'source_ref': 'Wiese1989_local_upper_bound', 'operator': '<',
        'bound_s-1': '1E+3', 'sum_known_A_s-1': '40000000',
        'maximum_branching_error': 2.5e-5}
    assert doc['radiative_model'] == 'E1'


@pytest.mark.parametrize('channel_id', range(16, 39))
def test_higher_family_has_qualified_vector_and_report(channel_id):
    doc = gen.generate(gen.SOURCE.read_bytes())
    row = next(c for c in doc['channels'] if c['id'] == channel_id)
    assert sum(gen.require_yields(doc, channel_id).values()) == pytest.approx(1, rel=0, abs=1e-12)
    assert row['missing_transitions'] == []
    assert 0 <= row['calculated_path_share'] <= 1
    assert row['omission_interval']['status'] == 'unbounded-omitted'
    assert all(0 <= b[0] <= b[1] <= 1 for b in row['yield_intervals'].values())
    assert all(line['upper_estimate'] <= 1e-3 for line in row['ground_lines'])


@pytest.mark.parametrize('mutation,match', [
    ('citation', 'citation'), ('transition', 'outgoing'), ('escape', 'escape'),
    ('extra', 'extra'), ('zero', 'upper-bound'), ('nan', 'finite'), ('product', 'identity'),
])
def test_source_mutations_refuse(mutation, match):
    data = deepcopy(yaml.safe_load(gen.SOURCE.read_bytes()))
    if mutation == 'citation':
        del data['transitions'][0]['citation']
    elif mutation == 'transition':
        data['transitions'].pop(0)
    elif mutation == 'escape':
        data['completeness']['escape_lines'].append('unmodelled ground branch')
    elif mutation == 'extra':
        row = deepcopy(data['transitions'][0]); row['channel_id'] = 99
        data['transitions'].append(row)
    elif mutation in ('zero', 'nan'):
        data['transitions'][0]['A_s-1'] = '0' if mutation == 'zero' else 'NaN'
    elif mutation == 'product':
        data['transitions'][0]['product_state'] = 'Ar(1s2)'
    with pytest.raises(ValueError, match=match):
        gen.generate(yaml.safe_dump(data).encode())


def test_missing_A_is_not_renormalized():
    data = yaml.safe_load(gen.SOURCE.read_bytes())
    data['transitions'][0]['A_s-1'] = None
    with pytest.raises(ValueError, match='completeness audit counts'):
        gen.generate(yaml.safe_dump(data).encode())


def test_every_sourced_A_has_a_cited_transition_row_and_reference():
    source = yaml.safe_load(gen.SOURCE.read_bytes())
    references = source['references']
    assert all(t['transition_id'] == f"{t['upper_nist_id']}->{t['lower_nist_id']}"
               for t in source['transitions'])
    for transition in source['transitions']:
        if transition['A_s-1'] is not None:
            assert transition['tp_ref'] in references
            reference = references[transition['tp_ref']]
            if transition['A_s-1'] == '0':
                assert reference['local_path'] and len(reference['sha256']) == 64
                assert transition['nist_A_s-1'] is None
                assert transition['A_upper_bound_s-1'] == '1e3'
            else:
                assert reference['url']


@pytest.mark.parametrize('field,value,match', [
    ('A_s-1', '1e3', 'upper-bound metadata'),
    ('A_s-1', None, 'effective zero value'),
    ('A_upper_bound_s-1', '-1', 'finite and positive'),
    ('tp_ref', 'T5223', 'upper-bound source'),
])
def test_channel11_upper_bound_source_fails_closed(field, value, match):
    source = yaml.safe_load(gen.SOURCE.read_bytes())
    row = next(t for t in source['transitions'] if t['channel_id'] == 11
               and t['lower_nist_id'] == '018001.000005')
    row[field] = value
    with pytest.raises(ValueError, match=match):
        gen.generate(yaml.safe_dump(source).encode())


def test_cascade_reaction_generator_projects_only_complete_source_rows():
    document = gen.generate(gen.SOURCE.read_bytes())
    rendered = reaction_gen.render(gen.render(document).encode())
    assert rendered.count('branch_product = ') == 132
    assert rendered.count('branch_yield = ') == 132
    for channel_id in range(6, 39):
        assert f'channel {channel_id}; sourced cascade branch' in rendered
    assert 'channel 38;' in rendered


def test_cascade_reaction_generator_refuses_changed_yield_shape():
    document = gen.generate(gen.SOURCE.read_bytes())
    document['channels'][0]['product_yields'].pop('Ar(1s2)')
    with pytest.raises(ValueError, match='invalid sourced product yields'):
        reaction_gen.render(gen.render(document).encode())


def test_cascade_reaction_generator_refuses_nan_yield():
    document = gen.generate(gen.SOURCE.read_bytes())
    document['channels'][-1]['product_yields']['Ar(1s5)'] = float('nan')
    with pytest.raises(ValueError, match='invalid sourced product yields'):
        reaction_gen.render(gen.render(document).encode())


def test_cascade_reaction_generator_preserves_only_marked_region():
    original = (f"prefix\n{reaction_gen.BEGIN}\nold generated text\n"
                f"{reaction_gen.END}\nsuffix\n")
    generated = f"{reaction_gen.BEGIN}\nnew generated text\n{reaction_gen.END}\n"
    assert reaction_gen.replace_region(original, generated) == (
        f"prefix\n{reaction_gen.BEGIN}\nnew generated text\n"
        f"{reaction_gen.END}\nsuffix\n")
    with pytest.raises(ValueError, match='marker pair'):
        reaction_gen.replace_region('unmarked file', generated)
    with pytest.raises(ValueError, match='marker pair'):
        reaction_gen.replace_region(original + original, generated)


def test_higher_5p_closes_with_calculated_provenance():
    doc = gen.generate(gen.SOURCE.read_bytes())
    yields = gen.require_yields(doc, 26)
    channel = next(c for c in doc['channels'] if c['id'] == 26)
    assert sum(yields.values()) == pytest.approx(1, rel=0, abs=1e-12)
    assert 0 < channel['calculated_path_share'] <= 1
    for product, value in yields.items():
        assert channel['yield_intervals'][product][0] <= value <= channel['yield_intervals'][product][1]


def test_non_ground_line_cannot_declare_resonance_trapping():
    source = yaml.safe_load(gen.SOURCE.read_bytes())
    row = next(r for r in source['higher_cascade']['transitions']
               if r['lower_nist_id'] != '018001.000001' and r['status'] == 'numeric')
    row['convention'] = 'RESONANCE_RADIATION_TRAPPED'
    with pytest.raises(ValueError, match='non-ground'):
        gen.generate(yaml.safe_dump(source).encode())


@pytest.mark.parametrize('mutation,match', [
    ('calculated-edge', 'outgoing'), ('omission-edge', 'outgoing'),
    ('omission-record', 'omission record'), ('escape', 'escape factor'),
    ('column', 'validity'), ('blend', 'statistical'), ('blend-nan', 'statistical'),
    ('lifetime', 'contradicts'),
])
def test_higher_cascade_refuses_unaccounted_or_invalid_inputs(mutation, match):
    source = yaml.safe_load(gen.SOURCE.read_bytes())
    model = source['higher_cascade']
    if mutation == 'calculated-edge':
        row = next(r for r in model['transitions'] if r['provenance'] == 'calculated:K11')
        model['transitions'].remove(row)
    elif mutation == 'omission-edge':
        model['transitions'] = [r for r in model['transitions'] if r['status'] != 'unbounded-omitted']
    elif mutation == 'omission-record':
        del model['conventions']['CALCULATED_LIST_OMISSION_BOUND']
    elif mutation == 'escape':
        row = next(r for r in model['transitions'] if r['lower_nist_id'] == '018001.000001')
        row['A_s_1'] = 1.0
    elif mutation == 'column':
        model['conventions']['RESONANCE_RADIATION_TRAPPED']['pressure_Ar_torr'] = .001
    elif mutation == 'blend':
        source['higher_channels'][0]['excitation_weights'] = {'018001.000016': 1.0}
    elif mutation == 'blend-nan':
        weights = source['higher_channels'][0]['excitation_weights']
        weights[next(iter(weights))] = float('nan')
    elif mutation == 'lifetime':
        model['lifetimes'][0]['lifetime_ns'] = 1e9
    with pytest.raises(ValueError, match=match):
        gen.generate(yaml.safe_dump(source).encode())


def test_terminal_omission_interval_tracks_flux_share():
    source = yaml.safe_load(gen.SOURCE.read_bytes())
    before = next(c for c in gen.generate(yaml.safe_dump(source).encode())['channels'] if c['id'] == 38)
    edge = next(r for r in source['higher_cascade']['transitions']
                if r['upper_nist_id'] == '018001.000062' and r['lower_nist_id'] == '018001.000058')
    edge['A_s_1'] *= 1000
    after = next(c for c in gen.generate(yaml.safe_dump(source).encode())['channels'] if c['id'] == 38)
    assert after['omission_interval']['flux_share'] > before['omission_interval']['flux_share']
    assert after['omission_interval']['total_variation_radius'] > before['omission_interval']['total_variation_radius']
    assert after['omission_interval']['endpoints'] != before['omission_interval']['endpoints']
    assert before['omission_interval']['total_variation_radius'] > 0
    unaffected = next(c for c in gen.generate(yaml.safe_dump(source).encode())['channels'] if c['id'] == 37)
    assert unaffected['omission_interval']['flux_share'] == 0


def test_higher_intervals_include_nominal_and_unbounded_terminal_endpoint():
    doc = gen.generate(gen.SOURCE.read_bytes())
    for c in doc['channels'][10:]:
        for endpoint in c['omission_interval']['endpoints']:
            assert sum(endpoint.values()) == pytest.approx(1, rel=0, abs=1e-12)
            for p, value in endpoint.items():
                lo, hi = c['yield_intervals'][p]
                assert lo-1e-14 <= value <= hi+1e-14


def test_cascade_owner_indices_are_unique_against_the_library():
    import ast
    text = reaction_gen.replace_region(reaction_gen.REACTIONS.read_text(),
                                       reaction_gen.render(gen.render(gen.generate(gen.SOURCE.read_bytes())).encode()))
    indices = [ast.literal_eval(k.value) for node in ast.parse(text).body
               if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
               and getattr(node.value.func, 'id', None) == 'entry'
               for k in node.value.keywords if k.arg == 'index']
    assert len(indices) == len(set(indices))


def test_four_s_sources_have_per_collision_singleton_cascades():
    frozen = (gen.ROOT / 'input/eedf/argon_channel_map.yaml').read_bytes()
    doc = gen.generate(gen.SOURCE.read_bytes(), frozen)
    added = [c for c in doc['channels'] if c['id'] >= 44]
    assert len(added) == 104
    assert len({c['upper_nist_ids'][0] for c in added}) == 26
    assert all(len(c['upper_nist_ids']) == 1 for c in added)
    assert gen.require_yields(doc, 71) == pytest.approx({
        'Ar(1s5)': 0.7420494699646643, 'Ar(1s4)': 0.2120141342756184,
        'Ar(1s3)': 0.03847663918335296, 'Ar(1s2)': 0.00745975657636435})
    rendered = reaction_gen.render(gen.render(doc).encode())
    assert rendered.count('branch_product = ') == 548
    assert 'label = "Ar(1s2) + e- => Ars + e-"' in rendered
    assert 'label = "Ar(1s2) + e- => Ar(1s2) + e-"' in rendered


def test_four_s_cascade_unknown_upper_state_refuses():
    frozen = yaml.safe_load((gen.ROOT / 'input/eedf/argon_channel_map.yaml').read_bytes())
    row = next(c for c in frozen['channels'] if c['id'] == 71)
    row['loki_process'] = row['loki_process'].replace('Ar(4p[1/2]1)', 'Ar(unknown)')
    with pytest.raises(ValueError, match='upper level'):
        gen.generate(gen.SOURCE.read_bytes(), yaml.safe_dump(frozen).encode())
