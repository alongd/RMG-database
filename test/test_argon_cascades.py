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
    doc = gen.generate(gen.SOURCE.read_bytes())
    assert gen.render(doc) == gen.OUTPUT.read_text()
    assert gen.require_yields(doc, 6) == pytest.approx({
        'Ar(1s5)': 0.7420494699646643, 'Ar(1s4)': 0.2120141342756184,
        'Ar(1s3)': 0.03847663918335296, 'Ar(1s2)': 0.00745975657636435})
    complete = [c for c in doc['channels'] if c['status'] == 'complete_for_E1']
    assert [c['id'] for c in complete] == list(range(6, 16))
    for c in complete:
        assert sum(c['product_yields'].values()) == pytest.approx(1, abs=1e-15)
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
def test_unresolved_refused(channel_id):
    doc = gen.generate(gen.SOURCE.read_bytes())
    assert next(c for c in doc['channels'] if c['id'] == channel_id)['product_yields'] is None
    with pytest.raises(ValueError, match='unresolved'):
        gen.require_yields(doc, channel_id)


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
    assert rendered.count('branch_product = ') == 40
    assert rendered.count('branch_yield = ') == 40
    for channel_id in range(6, 16):
        assert f'channel {channel_id}; sourced cascade branch' in rendered
    assert 'channel 16;' not in rendered


def test_cascade_reaction_generator_refuses_changed_yield_shape():
    document = gen.generate(gen.SOURCE.read_bytes())
    document['channels'][0]['product_yields'].pop('Ar(1s2)')
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
