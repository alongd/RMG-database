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
    assert [c['id'] for c in complete] == [6, 7, 8, 9, 10, 12, 13, 14, 15]
    for c in complete:
        assert sum(c['product_yields'].values()) == pytest.approx(1, abs=1e-15)
    assert doc['radiative_model'] == 'E1'


@pytest.mark.parametrize('channel_id', [11, *range(16, 39)])
def test_unresolved_refused(channel_id):
    doc = gen.generate(gen.SOURCE.read_bytes())
    assert next(c for c in doc['channels'] if c['id'] == channel_id)['product_yields'] is None
    with pytest.raises(ValueError, match='unresolved'):
        gen.require_yields(doc, channel_id)


@pytest.mark.parametrize('mutation,match', [
    ('citation', 'citation'), ('transition', 'outgoing'), ('escape', 'escape'),
    ('extra', 'extra'), ('zero', 'positive'), ('nan', 'finite'), ('product', 'identity'),
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
    doc = gen.generate(yaml.safe_dump(data).encode())
    with pytest.raises(ValueError, match='unresolved'):
        gen.require_yields(doc, 6)


def test_every_sourced_A_has_a_cited_nist_transition_row():
    source = yaml.safe_load(gen.SOURCE.read_bytes())
    references = source['references']
    assert all(t['transition_id'] == f"{t['upper_nist_id']}->{t['lower_nist_id']}"
               for t in source['transitions'])
    for transition in source['transitions']:
        if transition['A_s-1'] is not None:
            assert transition['tp_ref'] in references
            assert references[transition['tp_ref']]['url']


def test_cascade_reaction_generator_projects_only_complete_source_rows():
    document = gen.generate(gen.SOURCE.read_bytes())
    rendered = reaction_gen.render(gen.render(document).encode())
    assert rendered.count('branch_product = ') == 36
    assert rendered.count('branch_yield = ') == 36
    for channel_id in [6, 7, 8, 9, 10, 12, 13, 14, 15]:
        assert f'channel {channel_id}; sourced cascade branch' in rendered
    assert 'channel 11;' not in rendered
    assert 'channel 16;' not in rendered


def test_cascade_reaction_generator_refuses_changed_yield_shape():
    document = gen.generate(gen.SOURCE.read_bytes())
    document['channels'][0]['product_yields'].pop('Ar(1s2)')
    with pytest.raises(ValueError, match='invalid sourced product yields'):
        reaction_gen.render(gen.render(document).encode())
