"""Sourced family and inverse accounting used by the argon map collector."""
import hashlib
import math

import yaml
import re


def load_owner_sources(eedf):
    """Require bound arithmetic and yield validation to use identical source bytes."""
    from rmgpy.tools.eedf.ownership import load_cascade_yields
    snapshot = load_cascade_yields(eedf / 'argon_cascade_yields.yaml',
                                  eedf / 'argon_radiative_data.yaml')
    raw = (eedf / 'argon_radiative_data.yaml').read_bytes()
    if hashlib.sha256(raw).hexdigest() != snapshot['source_sha256']:
        raise ValueError('radiative source changed during owner accounting')
    return snapshot, yaml.safe_load(raw)


def cascade_owner(collision, reactions, snapshot):
    """Validate actual loaded branch objects against their sourced yield row."""
    from rmgpy.tools.eedf.ownership import make_branch_family
    owners = []
    for index, loaded in reactions.items():
        entry = loaded.entry
        marker = getattr(entry, 'data', None)
        if getattr(marker, 'process', None) == collision.get('owner_process', collision['label']):
            if getattr(marker, 'branch_product', None) is None:
                raise ValueError('cascade collision also has an unweighted owner')
            owners.append(('PlasmaArgon', index, entry.item, marker))
    if not owners:
        return None
    if snapshot is None:
        raise ValueError('cascade family requires the sourced yield snapshot')
    family = make_branch_family(snapshot, collision['id'], collision.get('owner_process', collision['label']),
                                float(collision['asm']['threshold']), 'IST-Lisbon-Ar-2021', owners)
    indices = [r['index'] for r in family['branches']]
    return dict(reaction=collision['reaction'], library='PlasmaArgon', index=indices[0],
                status='present', branch_indices=indices, via=collision['cascade'][1])


def checked_inverse(collision, reactions, snapshot, radiative, parse_reaction):
    """Keep omissions explicit and check the bound arithmetic against sourced A sums."""
    record = collision.get('inverse')
    if record is None:
        return None
    if not isinstance(record, dict):
        raise ValueError('inverse declaration must be a mapping')
    status = record.get('status')
    if status == 'paired':
        if (set(record) != {'status', 'reaction'} or collision['id'] not in (2, 3, 4, 5, 44, 97, 98, 125, 126, 127)):
            raise ValueError('invalid paired inverse declaration')
        left, arrow, right = parse_reaction(collision['reaction'])
        reverse = parse_reaction(record['reaction'])
        if arrow != '=>' or reverse != (right, '=>', left):
            raise ValueError('paired inverse must reverse the actual irreversible forward equation')
        matches = [index for index, loaded in reactions.items()
                   if loaded.eedf_process == collision.get('owner_process', collision['label'])
                   and loaded.eedf_collision_set == 'IST-Lisbon-Ar-2021'
                   and getattr(getattr(loaded.entry, 'data', None), 'side', None) == 'sup'
                   and not loaded.reversible and loaded.reactants == tuple(sorted(right))
                   and loaded.products == tuple(sorted(left))]
        if len(matches) != 1:
            raise ValueError('paired inverse requires exactly one matching sup owner')
        return dict(record, library='PlasmaArgon', index=matches[0])
    ground = collision['target'] == 'Ar(1S0)'
    expected = 'eliminated-upper-level' if ground else 'eliminated-upper-level-4s-redistribution'
    if ('cascade' not in collision or status != expected
            or set(record) != {'status', 'electron_density_max_m3', 'field_range_Td',
                               'field_node_count', 'bounds_sha256', 'levels'}
            or record['electron_density_max_m3'] != 1e18 or record['field_range_Td'] != [4., 25.]
            or record['field_node_count'] != 33
            or re.fullmatch('[0-9a-f]{64}', str(record['bounds_sha256'])) is None):
        raise ValueError('invalid eliminated-upper-level convention')
    row = next(c for c in snapshot['channels'] if c['id'] == collision['id'])
    ids = row.get('upper_nist_ids', [row.get('upper_nist_id')])
    if not isinstance(record['levels'], dict) or set(record['levels']) != set(ids):
        raise ValueError('inverse bounds do not cover the sourced upper levels')
    for uid, bounds in record['levels'].items():
        expected_fields = {'A_total_s_1', 'k_sup_max_m3_s', 'EN_Td_at_max', 'ratio_at_ne_max'}
        if not ground:
            expected_fields.add('ratio_per_electron_density_m3')
        if (not isinstance(bounds, dict) or set(bounds) != expected_fields
                or any(type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in bounds.values())):
            raise ValueError('invalid numeric inverse bounds')
        total = sum(float(r['A_s-1']) for r in radiative['transitions'] if r['upper_nist_id'] == uid)
        total += sum(float(r['A_s_1'] or 0.) for r in radiative['higher_cascade']['transitions']
                     if r['upper_nist_id'] == uid and r['lower_nist_id'] != '018001.000001')
        if total <= 0 or not math.isclose(bounds['A_total_s_1'], total, rel_tol=1e-12):
            raise ValueError('inverse bound A sum differs from the trapped-resonance DAG')
        ratio = 1e18 * bounds['k_sup_max_m3_s'] / total
        if (not math.isclose(ratio, bounds['ratio_at_ne_max'], rel_tol=1e-12)
                or not 4. <= bounds['EN_Td_at_max'] <= 25.
                or ground and ratio > 1e-3):
            raise ValueError('invalid inverse ratio or ground loss exceeds reviewed bound')
        if not ground and not math.isclose(bounds['ratio_per_electron_density_m3'], ratio/1e18, rel_tol=1e-12):
            raise ValueError('invalid 4s redistribution slope')
    return record
