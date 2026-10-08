#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2019 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

"""
Mutation tests for scripts/check_eedf_channel_map.py. Each case copies the assembled LoKI-B files and
the map into a scratch directory outside the repository, applies one corruption, runs the checker, and
expects it to refuse: exit status 1 with RESULT: FAIL, or argparse's usage error (the baseline case
expects it to pass). A crash counts as neither. The LXCat data never enter the repository: its
directories are passed as arguments, exactly as to the checker.

Exit status 0 when every case behaves as expected, 1 otherwise. No cross-section value is printed.

usage: test_eedf_channel_map_mutations.py MAP --assembled DIR --sources DIR [--sources DIR ...]
                                          [--loki-rates FILE] [--checker PATH] [--keep]
"""

import argparse
import copy
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

KEYWORDS = (b'ELASTIC', b'EFFECTIVE', b'EXCITATION', b'IONIZATION', b'ATTACHMENT')
DASHES = re.compile(rb'^-{5,}\s*$')
ASSEMBLED = 'Ar4s_assembled.txt'


def channel(doc, ident):
    return next(c for c in doc['channels'] if c['id'] == ident)


def convention(doc, name):
    return next(x for x in doc['declared_conventions'] if x['name'] == name)


def assembled_blocks(data):
    """(start, end) byte offsets of each collision block: keyword line through the closing dashes."""
    lines = data.splitlines(keepends=True)
    offsets, pos = [], 0
    for line in lines:
        offsets.append(pos)
        pos += len(line)
    offsets.append(pos)
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip() in KEYWORDS:
            start, dashes = i, 0
            while i < len(lines) and dashes < 2:
                if DASHES.match(lines[i].rstrip(b'\r\n')):
                    dashes += 1
                i += 1
            out.append((offsets[start], offsets[i]))
        else:
            i += 1
    return out


def edit_block(asm, ordinal, fn):
    """Replace the ordinal-th (1-based) block of the assembled file with fn(block bytes)."""
    path = os.path.join(asm, ASSEMBLED)
    data = open(path, 'rb').read()
    start, end = assembled_blocks(data)[ordinal - 1]
    new = fn(data[start:end])
    assert new != data[start:end], 'mutation changed nothing'
    open(path, 'wb').write(data[:start] + new + data[end:])


def double_first_ordinate(block):
    lines = block.splitlines(keepends=True)
    inside = False
    for i, line in enumerate(lines):
        if DASHES.match(line.rstrip(b'\r\n')):
            inside = not inside
            continue
        vals = line.split()
        if inside and len(vals) == 2 and float(vals[1]) > 0:
            lines[i] = vals[0] + b'\t' + format(float(vals[1]) * 2, '.6e').encode() + b'\n'
            return b''.join(lines)
    raise AssertionError('no nonzero ordinate')


def table_span(lines):
    """Indices of the opening and closing five-dash lines of a block's table."""
    dashes = [i for i, x in enumerate(lines) if DASHES.match(x.rstrip(b'\r\n'))]
    return dashes[0], dashes[1]


def shadow_table(block):
    """Insert, before the canonical table, a copy of it delimited by two-dash lines with its first nonzero
    ordinate doubled: LoKI-B reads the copy, the canonical table stays byte-identical to the source."""
    lines = block.splitlines(keepends=True)
    a, b = table_span(lines)
    copy_ = double_first_ordinate(b''.join(lines[a:b + 1])).splitlines(keepends=True)
    copy_[0], copy_[-1] = b'--\n', b'--\n'
    return b''.join(lines[:a] + copy_ + lines[a:])


def bare_cr_in_table(block):
    """End the first table row with a bare CR: a universal-newline reader still sees two rows, LoKI-B sees
    one line and reads only its first two numbers, so the second row is lost."""
    lines = block.splitlines(keepends=True)
    a, _ = table_span(lines)
    lines[a + 1] = lines[a + 1].rstrip(b'\n') + b'\r'
    return b''.join(lines)


def append_keywordless_collision(asm):
    """Append block 1 without its keyword line, as an Effective collision of Ar(3P0)."""
    path = os.path.join(asm, ASSEMBLED)
    data = open(path, 'rb').read()
    start, end = assembled_blocks(data)[0]
    raw = data[start:end].split(b'\n', 1)[1].replace(b'Ar(3P2)', b'Ar(3P0)').replace(b', Elastic]', b', Effective]')
    open(path, 'wb').write(data + b'\n' + raw)


def param_in_header(asm):
    """Mention the parameter keyword in the file's header prose: LoKI-B starts a record there."""
    path = os.path.join(asm, ASSEMBLED)
    data = open(path, 'rb').read()
    first, rest = data.split(b'\n', 1)
    open(path, 'wb').write(first + b'\nEach collision has a PARAM.: line.\n' + rest)


def unterminate_last_table(asm):
    """Cut the file after the last table row: LoKI-B ends that table at the end of the file."""
    path = os.path.join(asm, ASSEMBLED)
    data = open(path, 'rb').read()
    start, end = assembled_blocks(data)[-1]
    lines = data[start:end].splitlines(keepends=True)
    _, b = table_span(lines)
    open(path, 'wb').write(data[:start] + b''.join(lines[:b]))


def relabel(ident, label):
    """Give channel ident the label the db-r39 checker synthesised for a reordered or counted electron."""
    return lambda doc: channel(doc, ident).__setitem__('loki_process', label)


def replace_line3(block):
    lines = block.splitlines(keepends=True)
    lines[2] = b'garbage\n'
    return b''.join(lines)


def edit_blocks(ordinals, fn):
    def apply(asm):
        for o in ordinals:
            edit_block(asm, o, fn)
    return apply


def drop_line(marker):
    def fn(block):
        return b''.join(x for x in block.splitlines(keepends=True) if marker not in x)
    return fn


# --- the cases: (name, map edit, assembled-file edit, refresh the assembled-file hash, checker args) -------

def swap_ist_sources(doc):
    a, b = channel(doc, 2), channel(doc, 3)
    a['source'], b['source'] = b['source'], a['source']


def remove_elastic_convention(doc):
    doc['declared_conventions'] = [x for x in doc['declared_conventions'] if x['name'] != 'ELASTIC_REUSE_GROUND']
    for c in doc['channels']:
        if 'ELASTIC_REUSE_GROUND' in c.get('conventions', []):
            c['conventions'].remove('ELASTIC_REUSE_GROUND')
            if not c['conventions']:
                del c['conventions']


def rename_elastic_convention(doc):
    convention(doc, 'ELASTIC_REUSE_GROUND')['name'] = 'ELASTIC_PLACEHOLDER'
    for c in doc['channels']:
        c['conventions'] = ['ELASTIC_PLACEHOLDER' if x == 'ELASTIC_REUSE_GROUND' else x
                            for x in c.get('conventions', [])]


def undeclare_ion_rename(doc):
    """Channels 154-157 rewrite TRINITI's 'Ar(+)' as 'Ar(+,gnd)'; drop that from the declarations."""
    conv = convention(doc, 'STATE_RENAME')
    conv['applies_to'] = [i for i in conv['applies_to'] if i not in (154, 155, 156, 157)]
    for i in (154, 155, 156, 157):
        channel(doc, i)['conventions'] = [x for x in channel(doc, i)['conventions'] if x != 'STATE_RENAME']


def not_assembled_conflict(doc):
    extra = copy.deepcopy(doc['not_assembled'][0])
    extra['block_sha256'] = '0' * 64
    doc['not_assembled'].append(extra)


def not_assembled_also_mapped(doc):
    c = channel(doc, 2)
    doc['not_assembled'].append({'source': 'IST', 'block': c['source']['block'],
                                 'block_sha256': c['source']['block_sha256'], 'process': 'x', 'reason': 'x'})


def set_source(ident, field, value):
    return lambda doc: channel(doc, ident)['source'].__setitem__(field, value)


CASES = [
    # name, map edit, assembled edit, refresh assembled hash, drop --sources, expect pass
    ('baseline', None, None, False, False, True),
    # the review's cases (db-r38)
    ('drop_assembled_block', None, lambda a: edit_block(a, 5, lambda b: b''), False, False, False),
    ('rename_assembled_target', None,
     lambda a: edit_block(a, 1, lambda b: b.replace(b'Ar(3P2)', b'Ar(RENAMED)')), False, False, False),
    ('change_channel_sha', set_source(45, 'sha256', '0' * 64), None, False, False, False),
    ('duplicate_entry', lambda d: d['channels'].append(copy.deepcopy(channel(d, 45))), None, False, False, False),
    ('swap_IST_source_blocks', swap_ist_sources, None, False, False, False),
    ('remove_elastic_convention', remove_elastic_convention, None, False, False, False),
    ('wrong_source_line', set_source(45, 'line', 999999), None, False, False, False),
    ('change_table_refresh_assembled_hash', None,
     lambda a: edit_block(a, 5, double_first_ordinate), True, False, False),
    ('drop_block_refresh_assembled_hash', None, lambda a: edit_block(a, 5, lambda b: b''), True, False, False),
    ('rename_target_refresh_assembled_hash', None,
     lambda a: edit_block(a, 1, lambda b: b.replace(b'Ar(3P2)', b'Ar(RENAMED)')), True, False, False),
    ('wrong_ground_block_sha', set_source(1, 'block_sha256', '0' * 64), None, False, False, False),
    # the invariant behind them: conventions are mandatory and verified, source references are keyed
    ('rename_elastic_convention', rename_elastic_convention, None, False, False, False),
    ('elastic_applies_to_shrunk',
     lambda d: convention(d, 'ELASTIC_REUSE_GROUND')['applies_to'].remove(40), None, False, False, False),
    ('elastic_statement_emptied',
     lambda d: convention(d, 'ELASTIC_REUSE_GROUND').__setitem__('statement', ''), None, False, False, False),
    ('channel_drops_detailed_balance',
     lambda d: channel(d, 44)['conventions'].remove('DETAILED_BALANCE_INVERSE'), None, False, False, False),
    ('assembled_convention_comment_dropped', None,
     lambda a: edit_block(a, 1, drop_line(b'I-341 conventions:')), True, False, False),
    ('undeclared_ion_rename', undeclare_ion_rename, None, False, False, False),
    # the same, with the map and the assembled comments edited consistently and the file hash refreshed,
    # so that only the source-derived check can see it
    ('remove_elastic_convention_everywhere', remove_elastic_convention,
     edit_blocks((1, 2, 3, 4), drop_line(b'I-341 conventions:')), True, False, False),
    ('undeclared_ion_rename_everywhere', undeclare_ion_rename,
     edit_blocks((115, 116, 117, 118), lambda b: b.replace(b'LUMPED_TARGET_PER_LEVEL,STATE_RENAME',
                                                           b'LUMPED_TARGET_PER_LEVEL')), True, False, False),
    ('not_assembled_conflicting_sha', not_assembled_conflict, None, False, False, False),
    ('not_assembled_also_mapped', not_assembled_also_mapped, None, False, False, False),
    ('no_sources_given', None, None, False, True, False),
    # LoKI-B's own grammar (db-r39): what LoKI-B reads must be the mapped block's table and nothing else
    ('short_dash_shadow_table', None, lambda a: edit_block(a, 5, shadow_table), True, False, False),
    ('keywordless_collision', None, append_keywordless_collision, True, False, False),
    ('param_in_header_prose', None, param_in_header, True, False, False),
    ('bare_cr_hides_table_row', None, lambda a: edit_block(a, 5, bare_cr_in_table), True, False, False),
    ('unterminated_last_table', None, unterminate_last_table, True, False, False),
    ('ionization_electron_dropped', None,
     lambda a: edit_block(a, 115, lambda b: b.replace(b'+ e + e, Ionization]', b'+ e, Ionization]')),
     True, False, False),
    # LoKI-B's printed label (db-r41): a reordered or counted electron is read by LoKI-B, which prints the
    # canonical label; the map must carry that label, and the checker must know it without a rate list
    ('electron_first_lhs', relabel(44, 'e + e + Ar(3P0) <-> e + Ar(1P1), Excitation'),
     lambda a: edit_block(a, 5, lambda b: b.replace(b'[Ar(3P0) + e <->', b'[e + Ar(3P0) <->')), True, False, False),
    ('electron_first_rhs', relabel(44, 'e + Ar(3P0) <-> e + e + Ar(1P1), Excitation'),
     lambda a: edit_block(a, 5, lambda b: b.replace(b'<-> Ar(1P1) + e,', b'<-> e + Ar(1P1),')), True, False, False),
    ('coefficient_2e_rhs', relabel(154, 'e + Ar(3P2) -> e + e + Ar(+,gnd) + 2e, Ionization'),
     lambda a: edit_block(a, 115, lambda b: b.replace(b'+ e + e, Ionization]', b'+ 2e, Ionization]')),
     True, False, False),
    # every number in the map finite and compared; malformed input a verdict, not a traceback
    ('map_threshold_nan', lambda d: channel(d, 44).__setitem__('threshold_eV', float('nan')), None,
     False, False, False),
    ('map_threshold_inf', lambda d: channel(d, 1).__setitem__('threshold_eV', float('inf')), None,
     False, False, False),
    ('power_share_nan', lambda d: channel(d, 2)['power_share_max'].__setitem__('value', float('nan')), None,
     False, False, False),
    ('wrong_statistical_weight', lambda d: d['statistical_weights'].__setitem__('Ar(3P2)', 500), None,
     False, False, False),
    ('wrong_rmg_index', lambda d: channel(d, 2)['rmg'].__setitem__('index', 86), None, False, False, False),
    ('class_a_gap_dropped', lambda d: d['class_a_gaps'].__setitem__(next(iter(d['class_a_gaps'])), []), None,
     False, False, False),
    ('nonnumeric_line3', None, lambda a: edit_block(a, 5, replace_line3), True, False, False),
    ('channel_without_source', lambda d: channel(d, 45).pop('source'), None, False, False, False),
]
# Cases run without --loki-rates: the ordinary invocation must refuse them on its own.
WITHOUT_RATES = {'electron_first_lhs', 'electron_first_rhs', 'coefficient_2e_rhs', 'map_threshold_nan'}


def run_case(args, doc0, case, scratch):
    name, map_edit, asm_edit, refresh, no_sources, expect_pass = case
    work = os.path.join(scratch, name)
    asm = os.path.join(work, 'assembled')
    os.makedirs(asm)
    doc = copy.deepcopy(doc0)
    for fname in doc['loki_files']:
        shutil.copyfile(os.path.join(args.assembled, fname), os.path.join(asm, fname))
    if map_edit:
        map_edit(doc)
    if asm_edit:
        asm_edit(asm)
    if refresh:
        for fname in doc['loki_files']:
            doc['loki_files'][fname] = hashlib.sha256(open(os.path.join(asm, fname), 'rb').read()).hexdigest()
    path = os.path.join(work, 'map.yaml')
    with open(path, 'w') as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=120)
    cmd = [sys.executable, args.checker, path, '--assembled', asm]
    if not no_sources:
        for d in args.sources:
            cmd += ['--sources', d]
    if args.loki_rates and name not in WITHOUT_RATES:
        cmd += ['--loki-rates', args.loki_rates]
    cp = subprocess.run(cmd, capture_output=True, text=True)
    with open(os.path.join(work, 'stdout.log'), 'w') as fh:
        fh.write(cp.stdout)
    with open(os.path.join(work, 'stderr.log'), 'w') as fh:
        fh.write(cp.stderr)
    # a refusal is a verdict: exit 1 with RESULT: FAIL, or argparse's usage refusal (exit 2, which an
    # uncaught exception never gives); a crash is neither a pass nor a refusal
    passed = cp.returncode == 0 and 'RESULT: PASS' in cp.stdout
    refused = ((cp.returncode == 1 and 'RESULT: FAIL' in cp.stdout)
               or (cp.returncode == 2 and 'usage:' in cp.stderr))
    ok = passed if expect_pass else refused
    verdict = 'PASS' if passed else 'FAIL' if refused else f'CRASH (exit {cp.returncode})'
    first = next((x for x in cp.stdout.splitlines() if x.startswith('FAIL')), '')
    if not first:
        first = (cp.stderr.strip().splitlines() or [''])[-1]
    print(f"{'ok  ' if ok else 'BAD '} {name:40s} checker {verdict} "
          f"(expected {'PASS' if expect_pass else 'FAIL'})  {first[:110]}")
    return ok


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('map', help='the channel-map YAML')
    parser.add_argument('--assembled', required=True, help='directory holding the assembled LoKI-B files')
    parser.add_argument('--sources', action='append', default=[], required=True,
                        help='directory holding source LXCat files (repeatable)')
    parser.add_argument('--loki-rates', help='a LoKI-B rateCoefficients.txt solved on the assembled set')
    parser.add_argument('--checker', default=os.path.join(here, 'check_eedf_channel_map.py'),
                        help='the checker under test (default: the one beside this script)')
    parser.add_argument('--keep', action='store_true', help='keep the scratch directory and print its path')
    args = parser.parse_args()
    doc0 = yaml.safe_load(open(args.map))
    scratch = tempfile.mkdtemp(prefix='eedf-map-mutations-')
    try:
        results = [run_case(args, doc0, case, scratch) for case in CASES]
    finally:
        if args.keep:
            print(f'scratch kept: {scratch}')
        else:
            shutil.rmtree(scratch)
    bad = results.count(False)
    print(f'{len(results) - bad}/{len(results)} cases as expected')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
