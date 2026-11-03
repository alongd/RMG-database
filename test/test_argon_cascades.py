"""Sourced radiative vectors are reproducible, complete for E1, or explicitly refused."""
from copy import deepcopy
from pathlib import Path
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import gen_argon_cascades as gen


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
