#!/usr/bin/env python
"""Import cited higher-Ar rows from local NIST and Kurucz archives (no network)."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'input/eedf/argon_radiative_data.yaml'
OMITTED = ('018001.000058', '018001.000002')


def build(raw, archive):
    data = yaml.safe_load(raw)
    archive = Path(archive)
    nist_path = archive / 'sources/ar-i-levels-ids.tsv'
    levels = {}
    for r in csv.DictReader(nist_path.open(), delimiter='\t'):
        if not r['Level ID'] or not r['Level (cm-1)'] or float(r['Level (cm-1)']) >= 122000:
            continue
        levels[r['Level ID']] = dict(nist_id=r['Level ID'], energy_cm1=r['Level (cm-1)'],
                                    J=int(r['J']), g=int(r['g']), configuration=r['Configuration'],
                                    term=r['Term'], parity='odd' if '*' in r['Term'] else 'even',
                                    citation='ar-i-levels-ids')
    line_path = archive / 'sources/ar-i-higher-e1-completeness.tsv'
    nist = {(r['ID_k'], r['ID_i']): r for r in csv.DictReader(line_path.open(), delimiter='\t')
            if r['Aki(s^-1)'] and not r['Type'].strip()}
    kpath = archive / 'phase1/sources/kurucz-gf1800.lines.raw'
    krows, klevels = [], set()
    for number, line in enumerate(kpath.read_text().splitlines(), 1):
        one = (float(line[24:36]), float(line[36:41]), line[41:52].strip())
        two = (float(line[52:64]), float(line[64:69]), line[69:80].strip())
        klevels.update([one, two])
        if line[98:102].strip() != 'K11' or float(line[18:24]) != 18:
            raise ValueError('expected Kurucz K11 Ar I rows')
        krows.append((one, two, line[11:18].strip(), number))
    reverse = {}
    for uid, level in levels.items():
        matches = [k for k in klevels if k[1] == level['J']
                   and abs(abs(k[0]) - float(level['energy_cm1'])) < .2]
        if len(matches) != 1 or matches[0] in reverse:
            raise ValueError('ambiguous NIST/Kurucz level match: ' + uid)
        reverse[matches[0]] = uid
    calculated = {}
    for one, two, loggf, number in krows:
        if one not in reverse or two not in reverse:
            continue
        lo, up = sorted((reverse[one], reverse[two]), key=lambda x: float(levels[x]['energy_cm1']))
        if (up, lo) in calculated:
            raise ValueError('duplicate Kurucz pair')
        calculated[up, lo] = (loggf, number)

    def allowed(up):
        u = levels[up]
        return [(up, lo) for lo, l in levels.items()
                if float(l['energy_cm1']) < float(u['energy_cm1']) and l['parity'] != u['parity']
                and abs(l['J'] - u['J']) <= 1 and l['J'] + u['J'] > 0]

    channels = []
    for c in data['higher_channels']:
        ids = [r['Level ID'] for r in c['candidate_upper_levels']]
        # The frozen source uses an unprimed 6s label/onset; the two primed levels
        # lie another 0.17 eV above it. Do not invent excitation into that core.
        if c['id'] == 37:
            ids = ['018001.000049', '018001.000050']
        weight_sum = sum(levels[x]['g'] for x in ids)
        channels.append(dict(id=c['id'], process=c['process'], threshold_eV=c['threshold_eV'],
                             candidate_upper_levels=c['candidate_upper_levels'], upper_nist_ids=ids,
                             excitation_weights={x: levels[x]['g'] / weight_sum for x in ids},
                             citation='ar-i-higher-e1-completeness'))
    seen, todo = set(), [u for c in channels for u in c['upper_nist_ids']]
    while todo:
        u = todo.pop()
        if u in seen or int(u.split('.')[1]) <= 15:
            continue
        seen.add(u)
        todo.extend(lo for _, lo in allowed(u))
    transitions = []
    for u in sorted(seen):
        for _, lo in sorted(allowed(u)):
            wavelength = 1e7 / (float(levels[u]['energy_cm1']) - float(levels[lo]['energy_cm1']))
            t = dict(transition_id=u + '->' + lo, upper_nist_id=u, lower_nist_id=lo,
                     type='E1', vacuum_nm=wavelength)
            if (u, lo) in nist:
                n = nist[u, lo]
                t.update(status='numeric', provenance='nist', A_s_1=float(n['Aki(s^-1)']),
                         accuracy=n['Acc'], tp_ref=n['tp_ref'], citation='ar-i-higher-e1-completeness')
            elif (u, lo) in calculated:
                loggf, number = calculated[u, lo]
                t.update(status='numeric', provenance='calculated:K11',
                         A_s_1=6.6702e13 * 10**float(loggf) / (levels[u]['g'] * wavelength**2),
                         log_gf=loggf, source_line=number, accuracy='unrated', citation='kurucz-K11')
            elif (u, lo) == OMITTED:
                t.update(status='unbounded-omitted', provenance='calculated:K11', A_s_1=None,
                         accuracy='unbounded', citation='kurucz-K11',
                         convention='CALCULATED_LIST_OMISSION_BOUND')
            else:
                raise ValueError('unaccounted E1 pair: ' + t['transition_id'])
            transitions.append(t)
    for name, path in [('ar-i-levels-ids', nist_path), ('ar-i-higher-e1-completeness', line_path)]:
        if hashlib.sha256(path.read_bytes()).hexdigest() != data['queries'][name]['sha256']:
            raise ValueError('NIST snapshot hash mismatch: ' + name)
    kmeta = json.loads((archive / 'phase1/sources/kurucz-queries.json').read_text())['kurucz-gf1800.lines']
    if hashlib.sha256(kpath.read_bytes()).hexdigest() != kmeta['sha256']:
        raise ValueError('Kurucz snapshot hash mismatch')
    data['queries']['kurucz-K11'] = dict(url=kmeta['url'], retrieved_utc=kmeta['retrieved_utc'],
                                       sha256=hashlib.sha256(kpath.read_bytes()).hexdigest())
    data['references'].update({
        'K11': dict(citation='R. L. Kurucz, Ar I calculation, K11 (2011), gf1800.lines',
                    url='https://kurucz.cfa.harvard.edu/atoms/1800/'),
        'Klose1968': dict(citation='J. Z. Klose, JOSA 58, 1509–1512 (1968), Table II',
                          url='https://doi.org/10.1364/JOSA.58.001509'),
        'Holstein1947': dict(url='https://doi.org/10.1103/PhysRev.72.1212'),
        'Holstein1951': dict(url='https://doi.org/10.1103/PhysRev.83.1159'),
        'Walsh1959': dict(url='https://doi.org/10.1103/PhysRev.116.511'),
        'NIST_broadening': dict(url='https://physics.nist.gov/Pubs/AtSpec/node20.html'),
        'NIST_A_f': dict(url='https://physics.nist.gov/Pubs/AtSpec/node17.html'),
        'NIST_Ar_mass': dict(url='https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Ar'),
        'Bogaerts1998': dict(citation='Bogaerts et al., J. Appl. Phys. 84, 121–136 (1998)',
                             url='https://medialibrary.uantwerpen.be/oldcontent/container2642/files/jap98collisional.pdf'),
    })
    data['higher_channels'] = channels
    lifetimes = [(32, '3p10', 189, 3, .10), (33, '3p9', 141, 2, .05),
                 (34, '3p8', 166, 5, .10), (35, '3p7', 149, 3, .05),
                 (36, '3p6', 124, 3, .10), (37, '3p5', 95, 2, .05), (43, '3p1', 71, 2, .05)]
    data['higher_cascade'] = dict(
        levels=list(levels.values()), transitions=transitions,
        accuracy_relative={'AAA': .003, 'AA': .01, 'A+': .02, 'A': .03, 'B+': .07,
                           'B': .10, 'C+': .18, 'C': .25, 'D+': .40, 'D': .50,
                           'E': None, 'unrated': None, 'unbounded': None},
        accuracy_statement='NIST accuracy classes are estimates, not confidence limits. K11 has no '
                           'established per-line accuracy here: unrated rates span [0,infinity]. '
                           'No numerical accuracy is borrowed from a different calculation. '
                           'Reported intervals are conditional enclosures for these input ranges.',
        lifetimes=[dict(nist_id=f'018001.{i:06d}', paschen=name, lifetime_ns=t, standard_error_ns=e,
                        systematic_fraction=s, reference='Klose1968') for i, name, t, e, s in lifetimes],
        conventions={
            'HIGHER_EXCITATION_STATISTICAL_WEIGHTS': dict(
                statement='Assume excitation populations proportional to g=2J+1 within each listed '
                          'blend; this is a modelling convention, not measured populations. '
                          'Bogaerts et al. (1998) provides a statistical-population precedent. '
                          'Report all member extremes and the maximum pairwise total-variation distance.',
                references=['Bogaerts1998']),
            'CALCULATED_LIST_OMISSION_BOUND': dict(
                transition_id='->'.join(OMITTED), method='terminal-segment',
                statement='The parity-allowed delta-J=-1 3p5 4f -> 3p5 4s transition has delta-l=3 '
                          'and obtains E1 amplitude through configuration mixing. Weakness is not a zero. '
                          'gf1800.com lists GFLO=-7.5, but also EGFLO/EBOLT settings; observed rows '
                          'below that floor occur, so no applicable omission upper bound is established. '
                          'Retain status unbounded-omitted, A in [0,infinity], nominal A=0. '
                          'The exact terminal segment joins the known-edge vector to unit 1s5.',
                source_url='https://kurucz.cfa.harvard.edu/atoms/1800/gf1800.com'),
            'RESONANCE_RADIATION_TRAPPED': dict(
                statement='Optically thick reabsorption of ground resonance photons: nominal g=0. '
                          'Only ground-return E1 lines are trapped. Bound escaped branching by '
                          'g*A0/(g*A0+sum A_other), with g the larger Holstein Doppler and resonance '
                          'estimates. This closed-form convention is not an engine transport model. '
                          'Use NIST A where available, otherwise the explicitly tagged K11 fill. '
                          'A-accuracy propagation is reported separately from the escape estimate '
                          'evaluated at the sourced nominal A values.',
                temperature_K=298.0, pressure_Ar_torr=4.0, length_m=.05, mass_u=39.948,
                minimum_length_m=.05, minimum_ground_column_m_2=4*101325/760/(1.380649e-23*298)*.05,
                maximum_escape_factor=.001,
                geometry_source='RMG-Py examples/rmg/plasma_argon_energy_balance/input.py, '
                                'chamberGeometry radius 5 cm, length 30 cm; characteristic length '
                                'min(radius,length/2)=5 cm. Holstein slab estimates at this length.',
                geometry_commit='817e4a9fbf368612a7dfc309c6c7f173dfd5afbc',
                references=['Holstein1947', 'Holstein1951', 'Walsh1959', 'NIST_broadening', 'NIST_A_f',
                            'NIST_Ar_mass']),
        },
        membership_6s=dict(
            source_sha256='4bcb328eff01c147a1ebb9cb31e01253344ae10fc9fa4bff508d76bce0f9d444',
            source_file='Ar_LXCat.txt', block=37, threshold_eV=14.842,
            reference='Drawin H W 1967, EUR-CEA-FC-383, as cited by IST-Lisbon block 37',
            statement='Source uses unprimed Ar(6s), onset 14.842 eV, with a Drawin model comment. '
                      'The unprimed NIST fine levels are 14.839 and 14.849 eV; the primed levels '
                      'are 15.014 and 15.022 eV. Select both unprimed fine levels (5:3); the '
                      'source also explicitly distinguishes primed 4d elsewhere. No 6s-prime '
                      'population is inferred from this unprimed, lower-threshold process.'),
    )
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive', type=Path, required=True)
    p.add_argument('--source', type=Path, default=SOURCE)
    p.add_argument('--check', action='store_true')
    a = p.parse_args()
    text = build(a.source.read_bytes(), a.archive)
    if a.check:
        if a.source.read_text() != text:
            p.error('imported source differs')
    else:
        a.source.write_text(text)


if __name__ == '__main__':
    main()
