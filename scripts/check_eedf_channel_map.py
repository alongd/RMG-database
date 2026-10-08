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
Check a frozen EEDF channel map (input/eedf/*_channel_map.yaml) against the LoKI-B collision files it
describes and against the original LXCat source files those were built from. Both are LXCat data and
live outside any repository, so their directories are passed as arguments.

Every map entry is proven against the source file itself, never against what the map or the assembled
file say about themselves: the source block is re-derived from the source file (pinned by SHA-256), and
the collision LoKI-B reads from the assembled file must carry that block's table and threshold. Every
other difference between the two must be one of the transformations a declared convention licenses
(CONVENTIONS below), and the convention must be declared, listed on the entry, and named in the
assembled block's comment.

The assembled files are read with LoKI-B's own grammar (add5518, EedfCollisions.cpp
loadCollisionsClassic and LookupTable.cpp LookupTable::create), not with the LXCat block layout: lines
are split at LF only; any line containing 'PARAM.:' starts a record, wherever it is; the next line must
hold the '[lhs -> rhs, Type]' descriptor; the table opens at the first later line starting with two
dashes, skips lines starting with '#', and ends at the first line that does not start with two numbers,
which must start with two dashes, or at the end of the file. LoKI-B ignores every other line. The
checker accepts only a canonical subset of that grammar, on which the two readings cannot differ: every
record LoKI-B reads must be the parameter line, descriptor and five-dash-delimited table of exactly one
collision block, and every collision block must be read exactly once.

Each collision's label is the one LoKI-B prints (EedfCollisions.cpp operator<<, Gas.cpp operator<<), so
the map is checked without a rate list. LoKI-B drops every electron term wherever it stands and whatever
its count; the checker accepts only the descriptor form the real data use, '[X + e -> Y + e, Type]' (one
more '+ e' for Ionization), on which that label is the descriptor's own heavy text.

Fails (exit status 1), always with a RESULT line, when:
  - the map is not valid YAML, lacks a field the checker reads, or holds a number that is not finite or
    not of its kind (nothing else is compared then);
  - an entry has no class, or a class outside A/B/C/D, or a class-A entry has no RMG mapping status;
  - an RMG library index does not name that entry of the library with the map's reaction label, the
    class_a_gaps lists differ from the class-A entries without a present reaction, or a statistical
    weight differs from 2J+1 of its LS term;
  - an assembled file's SHA-256 differs from the map's;
  - an assembled file holds a byte outside printable ASCII, tab, LF and CRLF;
  - LoKI-B would read a record outside every collision block, or a table other than the block's (one
    opened or closed by a shorter dash line, or holding a '#' line), or a block twice or not at all;
  - a record LoKI-B reads is not canonical: a descriptor or threshold it would refuse, read or label
    otherwise, a third block line that is not a number, a table row other than two plain numbers, or a
    table ended by the end of the file;
  - the collisions LoKI-B would read from the assembled files and the map's entries differ in either
    direction (missing, extra, duplicated), or disagree on file, threshold or reverse flag;
  - a source file is missing, or its SHA-256 or block count differs from the map's;
  - an entry's source block, re-derived from the source file, differs from the entry's block SHA-256 or
    line, or its table or threshold differs from the assembled collision's;
  - a target, product, direction or electron count differs between source and assembled collision
    without a licensing convention, or an entry's conventions differ from those its transformation
    needs, from the declared_conventions registry, or from the assembled block's comment;
  - two references to one source block disagree, a block is listed twice or both mapped and listed, or a
    source block is neither mapped nor listed under 'not_assembled';
  - with --loki-rates: LoKI-B's own collision list (a rateCoefficients.txt) differs from the map.

Block hashes (block_sha256): the SHA-256 of a block's UTF-8 text, from its collision-type keyword line
through the second line of five or more dashes, after CRLF and CR line endings are converted to LF and
each line is terminated by one LF. Whole-file hashes (sha256) are of the raw bytes.

The power_share_max values are outputs of a solve the checker does not take as input; it requires them
finite and in (0, 1].

usage: check_eedf_channel_map.py MAP --assembled DIR --sources DIR [--sources DIR ...] [--loki-rates FILE]
                                 [--database DIR]
"""

import argparse
import collections
import hashlib
import math
import os
import re
import sys

import yaml

KEYWORDS = ('ELASTIC', 'EFFECTIVE', 'EXCITATION', 'IONIZATION', 'ATTACHMENT')
DASHES = re.compile(r'^-{5,}\s*$')
DESCRIPTOR = re.compile(r'\[(.+?)(<->|->)(.+?), (\w+)\]')
THRESHOLD = re.compile(r'E = +(\S*) +eV')  # as LoKI-B reads it from the parameter line
PROVENANCE = re.compile(r'I-341 source=(\S+) sha256=(\w+) block=(\d+) line=(\d+) block_sha256=(\w+)')
CONVENTION_COMMENT = re.compile(r'I-341 conventions: (\S+)')
ELECTRON = {'e', 'E', '2e', '2E'}
# The canonical subset of LoKI-B's grammar: a number both C++ '>>' and Python read the same way, a table
# row of two such numbers and nothing else, and a process term as LoKI-B's entriesFromString splits it.
NUMBER = r'[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?'
ROW = re.compile(rf'[ \t]*({NUMBER})[ \t]+({NUMBER})[ \t]*\r?')
HEAVY = re.compile(r'([A-Z][A-Za-z0-9]*)\(([^()]*)\)')
# The descriptor types the real data use, and the electrons each carries on its right-hand side.
DESCRIPTOR_ELECTRONS = {'Elastic': 1, 'Excitation': 1, 'Ionization': 2}
CANONICAL_BYTES = re.compile(rb'[\t\n\x20-\x7e]*')

# State names the STATE_RENAME convention may rewrite, source name -> LoKI-B name: the argon 4s levels
# from Racah to the IST-Lisbon LS-term names, and the ion to the IST-Lisbon ion state.
STATE_RENAMES = {
    'Ar(4s[3/2]2)': 'Ar(3P2)',
    'Ar(4s[3/2]1)': 'Ar(3P1)',
    "Ar(4s'[1/2]0)": 'Ar(3P0)',
    "Ar(4s'[1/2]1)": 'Ar(1P1)',
    'Ar(+)': 'Ar(+,gnd)',
}
GROUND = 'Ar(1S0)'
LEVELS_1S = ('Ar(3P2)', 'Ar(3P1)', 'Ar(3P0)', 'Ar(1P1)')
LUMPED = 'Ar*'
# The conventions this checker can verify. A map may declare only these.
CONVENTIONS = ('ELASTIC_REUSE_GROUND', 'DETAILED_BALANCE_INVERSE', 'LUMPED_TARGET_PER_LEVEL', 'STATE_RENAME')


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def blocks(path):
    """Yield (ordinal, line, raw text) of each collision block: keyword line through the closing dashes.

    The text is read with universal newlines, so CRLF and CR become LF, and is rejoined with LF."""
    lines = open(path, encoding='utf-8').read().split('\n')
    i, n, ordinal = 0, len(lines), 0
    while i < n:
        if lines[i].strip() in KEYWORDS and lines[i] == lines[i].rstrip():
            start, dashes = i, 0
            while i < n and dashes < 2:
                if DASHES.match(lines[i]):
                    dashes += 1
                i += 1
            ordinal += 1
            yield ordinal, start + 1, '\n'.join(lines[start:i]) + '\n'
        else:
            i += 1


def loki_lines(path):
    """The file's lines as std::getline returns them (split at LF only, a CR before the LF kept), and the
    bytes outside the canonical character set: printable ASCII, tab, LF, and CR only before an LF."""
    data = open(path, 'rb').read()
    problems = []
    text = data.replace(b'\r\n', b'\n')
    bad = len(text) - sum(len(m) for m in CANONICAL_BYTES.findall(text))
    if bad:
        problems.append(f'{bad} bytes outside printable ASCII, tab, LF and CRLF (LoKI-B and a universal-newline '
                        f'or UTF-8 reader can split or read them differently)')
    lines = data.decode('ascii', errors='replace').split('\n')
    if lines and lines[-1] == '':
        lines.pop()  # getline yields no empty line after a final LF
    return lines, problems


def loki_records(lines):
    """The collision records LoKI-B reads from a classic file, and the reasons the checker refuses any.

    Mirrors loadCollisionsClassic and LookupTable::create line by line: a record starts at any line holding
    'PARAM.:', its descriptor is the next line, its table opens at the first later line starting with '--',
    skips '#' lines, and ends at the first line that is not two numbers. Every line outside a record is one
    LoKI-B ignores. Line numbers are 0-based."""
    records, problems, i, n = [], [], 0, len(lines)
    while i < n:
        if 'PARAM.:' not in lines[i]:
            i += 1
            continue
        r = {'param': i, 'open': None, 'close': None, 'rows': []}
        records.append(r)
        where = f'line {i + 1}'
        thresholds = THRESHOLD.findall(lines[i])
        if len(thresholds) > 1 or (thresholds and not re.fullmatch(NUMBER, thresholds[0])):
            problems.append(f'{where}: threshold on the parameter line is not one plain number')
        if i + 1 >= n or not DESCRIPTOR.search(lines[i + 1]):
            problems.append(f'{where}: no descriptor on the next line (LoKI-B refuses the file)')
        j = i + 2
        while j < n and not lines[j].startswith('--'):
            j += 1
        if j >= n:
            problems.append(f'{where}: no table follows (LoKI-B refuses the file)')
            break
        r['open'] = j
        j += 1
        while j < n:
            if lines[j].startswith('--'):
                r['close'] = j
                break
            if lines[j].startswith('#'):
                problems.append(f'line {j + 1}: a comment line inside a table (LoKI-B skips it)')
            elif ROW.fullmatch(lines[j]):
                r['rows'].append(j)
            else:
                problems.append(f'line {j + 1}: table line is neither two plain numbers nor a dash line')
                break
            j += 1
        if r['close'] is None and j >= n:
            problems.append(f'{where}: table runs to the end of the file without a closing dash line')
        if len(r['rows']) < 2:
            problems.append(f'{where}: table has fewer than two rows (LoKI-B refuses the file)')
        i = j + 1
    return records, problems


def heavy(side):
    """The heavy-particle states of one side of a process, electrons dropped."""
    return [s.strip() for s in side.split(' + ') if s.strip() not in ELECTRON]


def electrons(side):
    """The number of electrons on one side of a process, 'e', 'E', '2e' or '2E' terms counted."""
    terms = (re.fullmatch(r'(\d*)\s*[eE]', s.strip()) for s in side.split(' + '))
    return sum(int(m.group(1) or 1) for m in terms if m)


def loki_state(term):
    """A heavy state 'Gas(id)' parsed as LoKI-B's entriesFromString parses it and printed back as its state
    printer (Gas.cpp operator<<) writes it, or None when the term is outside that grammar."""
    m = HEAVY.fullmatch(term)
    if not m:
        return None
    gas, rest = m.groups()
    charge = re.match(r'(\+*|-*),', rest)  # std::regex ECMAScript tries '\+*' first, as re does
    q = charge.group(1) if charge else ''
    rest = rest[charge.end():] if charge else rest
    e = re.match(r'[^,=]+', rest)
    if not e:
        return None
    rest, e = rest[e.end():].removeprefix(','), e.group(0)
    v = re.match(r'v=([^,=]+),?', rest)
    rest, v = (rest[v.end():], v.group(1)) if v else (rest, '')
    j = re.match(r'J=([^,=]+),?', rest)
    rest, j = (rest[j.end():], j.group(1)) if j else (rest, '')
    if rest:
        return None
    return f"{gas}({q}{',' if q else ''}{e}{',v=' + v if v else ''}{',J=' + j if j else ''})"


def loki_print(descriptor):
    """The label LoKI-B prints for a descriptor (EedfCollisions.cpp operator<<), and why the checker refuses
    the descriptor, if it does.

    LoKI-B drops every electron term, whatever its place or count, and prints 'e + target -> e + [e + ]
    products, Type' from the heavy states alone. The checker accepts only the form the real data use, on
    which that printed label is the descriptor's own heavy text: '[X + e -> Y + e, Type]', with '<->' for
    '->', one more '+ e' for Ionization, Type one of Elastic, Excitation or Ionization, and X and Y heavy
    states that LoKI-B prints back unchanged."""
    if not descriptor:
        return None, 'no descriptor'
    lhs, arrow, rhs, kind = descriptor.groups()
    if kind not in DESCRIPTOR_ELECTRONS:
        return None, f'collision type {kind!r} is not one of {", ".join(DESCRIPTOR_ELECTRONS)}'
    left = re.fullmatch(r'(\S+) \+ e ', lhs)
    right = re.fullmatch(r' (\S+)' + r' \+ e' * DESCRIPTOR_ELECTRONS[kind], rhs)
    if not left or not right:
        return None, (f"descriptor '{descriptor.group(0)}' is not '[X + e {arrow} Y"
                      f"{' + e' * DESCRIPTOR_ELECTRONS[kind]}, {kind}]'")
    x, y = left.group(1), right.group(1)
    for term in (x, y):
        if loki_state(term) != term:
            return None, f"state '{term}' is not one LoKI-B reads and prints back unchanged"
    return f"e + {x} {arrow} e + {'e + ' if kind == 'Ionization' else ''}{y}, {kind}", None


def parse_block(ordinal, line, raw):
    """What a block says: the process, threshold, table and I-341 comments. Line indices are 0-based and
    relative to the block."""
    lines = raw.split('\n')
    dashes = [k for k, x in enumerate(lines) if DASHES.match(x)]
    params = [k for k, x in enumerate(lines) if 'PARAM.:' in x]
    param = params[0] if params else None
    b = {'ordinal': ordinal, 'line': line, 'raw': raw, 'kind': lines[0].strip(),
         'sha256': hashlib.sha256(raw.encode()).hexdigest(), 'dashes': dashes, 'params': params,
         'table': '\n'.join(lines[dashes[0]:dashes[1] + 1]) if len(dashes) >= 2 else None,
         'line3': None, 'problems': [],
         'threshold': 0.0, 'descriptor': None, 'process': None, 'provenance': None, 'conventions': None}
    first = lines[2].split()[0] if len(lines) > 2 and lines[2].split() else ''
    if re.fullmatch(NUMBER, first):
        b['line3'] = float(first)
    elif b['kind'] != 'ATTACHMENT':
        b['problems'].append(f"line {line + 2}: {b['kind']} block's third line {first!r} is not a number")
    if len(dashes) < 2:
        b['problems'].append(f'line {line}: block has no table between two five-dash lines')
    if param is not None:
        thr = THRESHOLD.search(lines[param])
        b['threshold'] = float(thr.group(1)) if thr and re.fullmatch(NUMBER, thr.group(1)) else 0.0
        if param + 1 < len(lines):
            b['descriptor'] = DESCRIPTOR.search(lines[param + 1])
    for x in lines[:dashes[0] if dashes else len(lines)]:
        if x.startswith('PROCESS:'):
            b['process'] = x[len('PROCESS:'):].strip()
        p = PROVENANCE.search(x)
        if p:
            b['provenance'] = p.groups()
        c = CONVENTION_COMMENT.search(x)
        if c:
            b['conventions'] = set(c.group(1).split(','))
    if b['descriptor']:
        lhs, arrow, rhs, kind = b['descriptor'].groups()
    elif b['process']:
        m = re.match(r'(.+?)(<->|->)(.+), (\w+)$', b['process'])
        lhs, arrow, rhs, kind = m.groups() if m else ('', '', '', '')
    else:
        lhs, arrow, rhs, kind = '', '', '', ''
    b['lhs'], b['arrow'], b['rhs'], b['type'] = heavy(lhs), arrow, heavy(rhs), kind
    b['electrons'] = (electrons(lhs), electrons(rhs))
    b['label'], b['label_problem'] = loki_print(b['descriptor'])
    return b


def needed_conventions(src, asm):
    """The conventions that license every difference between a source block and the assembled collision
    built from it, and the differences no convention licenses."""
    need, bad = set(), []
    if src['type'] != asm['type'] or len(src['lhs']) != 1 or len(asm['lhs']) != 1 \
            or len(src['rhs']) != len(asm['rhs']):
        return need, [f"process shape differs: source {src['lhs']}->{src['rhs']} {src['type']}, "
                      f"assembled {asm['lhs']}->{asm['rhs']} {asm['type']}"]
    if src['electrons'] != asm['electrons']:
        bad.append(f"electrons {src['electrons'][0]} -> {src['electrons'][1]} became "
                   f"{asm['electrons'][0]} -> {asm['electrons'][1]}")
    s, a = src['lhs'][0], asm['lhs'][0]
    reuse = asm['type'] == 'Elastic' and s == GROUND and a in LEVELS_1S
    if a != s:
        if reuse:
            need.add('ELASTIC_REUSE_GROUND')
        elif s == LUMPED and a in LEVELS_1S:
            need.add('LUMPED_TARGET_PER_LEVEL')
        elif STATE_RENAMES.get(s) == a:
            need.add('STATE_RENAME')
        else:
            bad.append(f'target {s} became {a}')
    for s, a in zip(src['rhs'], asm['rhs']):
        if a == s or (reuse and s == GROUND and a == asm['lhs'][0]):
            continue
        if STATE_RENAMES.get(s) == a:
            need.add('STATE_RENAME')
        else:
            bad.append(f'product {s} became {a}')
    if src['arrow'] != asm['arrow']:
        if src['arrow'] == '->' and asm['arrow'] == '<->' and asm['type'] == 'Excitation':
            need.add('DETAILED_BALANCE_INVERSE')
        else:
            bad.append(f"direction {src['arrow']} became {asm['arrow']}")
    return need, bad


def number(x):
    """Whether x is a finite real number (YAML .nan and .inf are not, nor is a bool)."""
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def integer(x, low=0):
    return isinstance(x, int) and not isinstance(x, bool) and x >= low


def validate(doc):
    """The map's structure and types: every field the checker reads is present, every number is finite and
    of its kind. Refuses before any comparison, so a malformed map is a verdict rather than a traceback."""
    errors = []

    def walk(x, where):
        if isinstance(x, float) and not math.isfinite(x):
            errors.append(f'{where}: {x} is not a finite number')
        for k, v in (x.items() if isinstance(x, dict) else enumerate(x) if isinstance(x, list) else ()):
            walk(v, f'{where}.{k}' if isinstance(x, dict) else f'{where}[{k}]')

    def need(ok, where, what):
        if not ok:
            errors.append(f'{where}: {what}')
        return ok

    if not need(isinstance(doc, dict), 'map', 'not a mapping'):
        return errors
    sha = lambda x: isinstance(x, str) and re.fullmatch(r'[0-9a-f]{64}', x)  # noqa: E731
    for key, kind in (('loki_files', dict), ('sources', dict), ('statistical_weights', dict), ('channels', list),
                      ('class_counts', dict), ('declared_conventions', list), ('class_a_gaps', dict),
                      ('not_assembled', list)):
        need(isinstance(doc.get(key), kind), f'map.{key}', f'missing or not a {kind.__name__}')
    if errors:
        walk(doc, 'map')
        return errors
    for name, digest in doc['loki_files'].items():
        need(isinstance(name, str) and sha(digest), f'map.loki_files.{name}', 'not a file name and SHA-256')
    for key, src in doc['sources'].items():
        need(isinstance(src, dict) and isinstance(src.get('file'), str) and sha(src.get('sha256'))
             and integer(src.get('n_blocks'), 1), f'map.sources.{key}', 'needs file, sha256 and n_blocks >= 1')
    for state, g in doc['statistical_weights'].items():
        need(integer(g, 1), f'map.statistical_weights.{state}', 'not a positive integer')
    for k, v in doc['class_counts'].items():
        need(integer(v), f'map.class_counts.{k}', 'not a non-negative integer')
    for k, ids in doc['class_a_gaps'].items():
        need(isinstance(ids, list) and all(integer(i, 1) for i in ids), f'map.class_a_gaps.{k}', 'not a list of ids')
    for k, conv in enumerate(doc['declared_conventions']):
        need(isinstance(conv, dict) and isinstance(conv.get('applies_to'), list)
             and all(integer(i, 1) for i in conv['applies_to']), f'map.declared_conventions[{k}]',
             'needs applies_to, a list of ids')
    for k, n in enumerate(doc['not_assembled']):
        need(isinstance(n, dict) and isinstance(n.get('source'), str) and integer(n.get('block'), 1)
             and sha(n.get('block_sha256')) and isinstance(n.get('process'), str), f'map.not_assembled[{k}]',
             'needs source, block >= 1, block_sha256 and process')
    for k, c in enumerate(doc['channels']):
        where = f"map.channels[{k}] (id {c.get('id') if isinstance(c, dict) else '?'})"
        if not need(isinstance(c, dict), where, 'not a mapping'):
            continue
        ref = c.get('source')
        need(integer(c.get('id'), 1), where, 'id is not a positive integer')
        need(isinstance(c.get('loki_process'), str) and isinstance(c.get('lxcat_file'), str), where,
             'needs loki_process and lxcat_file')
        need(isinstance(ref, dict) and isinstance(ref.get('file'), str) and sha(ref.get('sha256'))
             and integer(ref.get('block'), 1) and integer(ref.get('line'), 1) and sha(ref.get('block_sha256')),
             where, 'source needs file, sha256, block >= 1, line >= 1 and block_sha256')
        need(number(c.get('threshold_eV')), where, f"threshold_eV {c.get('threshold_eV')!r} is not a finite number")
        need(isinstance(c.get('superelastic_in_set'), bool), where, 'superelastic_in_set is not true or false')
        need(isinstance(c.get('conventions', []), list) and all(isinstance(x, str) for x in c.get('conventions', [])),
             where, 'conventions is not a list of names')
        share = c.get('power_share_max')
        if share is not None:
            need(isinstance(share, dict) and number(share.get('value')) and 0 < share['value'] <= 1
                 and isinstance(share.get('where'), str), where,
                 'power_share_max needs a finite value in (0, 1] and where')
        rmg = c.get('rmg')
        if rmg is not None:
            need(isinstance(rmg, dict) and (rmg.get('index') is None or integer(rmg['index'], 0)), where,
                 'rmg is not a mapping with an integer index')
    walk(doc, 'map')
    return errors


def library_entries(database, library):
    """index -> label of a kinetics library in the database the map belongs to."""
    path = os.path.join(database, 'kinetics', 'libraries', library, 'reactions.py')
    if not os.path.exists(path):
        return None
    text = open(path).read()
    return {int(i): label for i, label in re.findall(r'entry\(\s*index\s*=\s*(\d+),\s*label\s*=\s*"([^"]*)"', text)}


def statistical_weight(state):
    """2J+1 from an LS-term state name such as 'Ar(3P2)', or None for any other name."""
    m = re.fullmatch(r'[A-Z][a-z]?\(\d[SPDFG](\d)\)', state)
    return 2 * int(m.group(1)) + 1 if m else None


def check(args):
    try:
        doc = yaml.safe_load(open(args.map))
    except (OSError, yaml.YAMLError) as exc:
        doc, problems = None, [f'map {args.map}: cannot be read as YAML ({type(exc).__name__})']
    else:
        problems = validate(doc)
    if problems:
        for e in problems:
            print('FAIL', e)
        print(f'RESULT: FAIL ({len(problems)} problems; the map is malformed, so nothing else was compared)')
        return 1
    channels = doc['channels']
    errors = []

    # 1. classes, RMG mappings, ids
    for ident, n in collections.Counter(c.get('id') for c in channels).items():
        if n > 1:
            errors.append(f'id {ident}: used {n} times')
    for c in channels:
        if c.get('class') not in ('A', 'B', 'C', 'D'):
            errors.append(f"id {c.get('id')}: class {c.get('class')!r} is not one of A/B/C/D")
        if c.get('class') == 'A' and not (c.get('rmg') or {}).get('status'):
            errors.append(f"id {c.get('id')}: class A without an RMG mapping status")
    counts = collections.Counter(c.get('class') for c in channels)
    if dict(counts) != {k: v for k, v in doc['class_counts'].items() if v}:
        errors.append(f"class_counts {doc['class_counts']} differ from the entries {dict(counts)}")
    # the gap list is the class-A entries with no 'present' RMG reaction, each under its own status
    gaps = collections.Counter()
    by_id = {c['id']: c for c in channels}
    for key, ids in doc['class_a_gaps'].items():
        for i in ids:
            gaps[i] += 1
            c = by_id.get(i)
            status = ((c or {}).get('rmg') or {}).get('status')
            if c is None or c.get('class') != 'A' or not key.startswith(f'[{status}] '):
                errors.append(f'class_a_gaps {key!r}: id {i} is not a class-A entry with RMG status in its key')
    for c in channels:
        status = (c.get('rmg') or {}).get('status')
        if c.get('class') == 'A' and status != 'present' and gaps[c['id']] != 1:
            errors.append(f"id {c['id']}: RMG status {status}, listed {gaps[c['id']]} times in class_a_gaps")
    # an RMG index must name that library entry, with the reaction the map gives
    libraries = {}
    for c in channels:
        rmg = c.get('rmg') or {}
        if rmg.get('index') is None:
            continue
        lib = libraries.setdefault(rmg.get('library'), library_entries(args.database, str(rmg.get('library'))))
        if lib is None:
            errors.append(f"id {c['id']}: library {rmg.get('library')} not found under {args.database}")
        elif lib.get(rmg['index']) != rmg.get('reaction'):
            errors.append(f"id {c['id']}: {rmg.get('library')} entry {rmg['index']} is "
                          f"{lib.get(rmg['index'])!r}, map says {rmg.get('reaction')!r}")
    # statistical weights: 2J+1 of the state's LS term
    for state, g in doc['statistical_weights'].items():
        if statistical_weight(state) != g:
            errors.append(f'statistical weight of {state}: map says {g}, its LS term gives '
                          f'{statistical_weight(state) or "no J"}')

    # 2. the source files, each block re-derived from the file itself
    src_blocks = {}  # file name -> {ordinal: parsed block}
    for key, src in doc['sources'].items():
        path = next((os.path.join(d, src['file']) for d in args.sources
                     if os.path.exists(os.path.join(d, src['file']))), None)
        if path is None:
            errors.append(f"source {src['file']}: not found under --sources; entries citing it cannot be verified")
            continue
        if sha256(path) != src['sha256']:
            errors.append(f"source {src['file']}: SHA-256 differs from the map; entries citing it cannot be verified")
            continue
        src_blocks[src['file']] = {o: parse_block(o, ln, raw) for o, ln, raw in blocks(path)}
        if len(src_blocks[src['file']]) != src['n_blocks']:
            errors.append(f"source {src['file']}: {len(src_blocks[src['file']])} blocks, map says {src['n_blocks']}")
    by_file = {v['file']: v for v in doc['sources'].values()}

    # 3. the assembled files, read as LoKI-B reads them: each record it loads must be the parameter line,
    #    descriptor and table of exactly one collision block, and each block must be loaded exactly once
    for label, n in collections.Counter(c['loki_process'] for c in channels).items():
        if n > 1:
            errors.append(f'{label}: mapped {n} times')
    found = {}
    for name, digest in doc['loki_files'].items():
        path = os.path.join(args.assembled, name)
        if not os.path.isfile(path):
            errors.append(f'{name}: not found under --assembled')
            continue
        if sha256(path) != digest:
            errors.append(f'{name}: SHA-256 differs from the map')
        lines, problems = loki_lines(path)
        errors.extend(f'{name}: {p}' for p in problems)
        if problems:
            continue
        records, problems = loki_records(lines)
        errors.extend(f'{name}: {p}' for p in problems)
        spans = [(ln - 1, ln - 1 + raw.count('\n'), parse_block(o, ln, raw)) for o, ln, raw in blocks(path)]
        loaded = collections.Counter()
        for r in records:
            where = f"{name}:{r['param'] + 1}"
            span = next((s for s in spans if s[0] <= r['param'] < s[1]), None)
            if span is None:
                desc = DESCRIPTOR.search(lines[r['param'] + 1]) if r['param'] + 1 < len(lines) else None
                errors.append(f"{where}: LoKI-B loads a collision outside every collision block"
                              f"{': ' + desc.group(0) if desc else ''}")
                continue
            start, _, b = span
            loaded[start] += 1
            if [start + k for k in b['params']] != [r['param']]:
                errors.append(f'{where}: block {b["ordinal"]} does not hold exactly this one parameter line')
            if [start + k for k in b['dashes']] != [r['open'], r['close']]:
                errors.append(f"{where}: LoKI-B reads the table between lines "
                              f"{r['open'] + 1 if r['open'] is not None else '?'} and "
                              f"{r['close'] + 1 if r['close'] is not None else 'the end of the file'}, "
                              f"not block {b['ordinal']}'s five-dash table")
                continue
            errors.extend(f'{name}: {p}' for p in b['problems'])
            if b['label_problem']:
                errors.append(f"{where}: {b['label_problem']}")
                continue
            label = b['label']
            if label in found:
                errors.append(f'{label}: appears twice in the assembled files')
            found[label] = (name, digest, b)
        for start, _, b in spans:
            if loaded[start] != 1:
                errors.append(f"{name}:{start + 1}: LoKI-B loads block {b['ordinal']} {loaded[start]} times")
    mapped = {c['loki_process']: c for c in channels}
    for label in sorted(set(found) - set(mapped)):
        errors.append(f'UNMAPPED collision in the assembled files: {label}')
    for label in sorted(set(mapped) - set(found)):
        errors.append(f'map entry with no collision in the assembled files: {label}')

    # 4. each entry against its source block, and the conventions its transformation needs
    refs = {}  # (source file, block) -> (block_sha256, line, who), every reference must agree
    uses = collections.defaultdict(set)  # convention -> ids whose transformation needs it
    for c in channels:
        ident, label, ref = c['id'], c['loki_process'], c['source']
        key = (ref['file'], ref['block'])
        if key in refs and refs[key][:2] != (ref['block_sha256'], ref['line']):
            errors.append(f'id {ident}: source {key} cited with a different block SHA-256 or line than {refs[key][2]}')
        refs.setdefault(key, (ref['block_sha256'], ref['line'], f'id {ident}'))
        if ref['file'] not in by_file or ref['sha256'] != by_file[ref['file']]['sha256']:
            errors.append(f'id {ident}: source {ref["file"]} with SHA-256 {ref["sha256"][:12]}... is not a declared source')
            continue
        if ref['file'] not in src_blocks:
            continue  # reported in step 2
        src = src_blocks[ref['file']].get(ref['block'])
        if src is None:
            errors.append(f"id {ident}: source {ref['file']} has no block {ref['block']}")
            continue
        if src['sha256'] != ref['block_sha256']:
            errors.append(f"id {ident}: block SHA-256 differs from {ref['file']} block {ref['block']}")
        if src['line'] != ref['line']:
            errors.append(f"id {ident}: {ref['file']} block {ref['block']} starts at line {src['line']}, "
                          f"map says {ref['line']}")
        if label not in found:
            continue  # reported in step 3
        name, digest, asm = found[label]
        if c['lxcat_file'] != name:
            errors.append(f"id {ident}: in {name}, map says {c['lxcat_file']}")
        if not abs(asm['threshold'] - c['threshold_eV']) <= 1e-9:  # fails closed on any non-finite value
            errors.append(f"id {ident}: threshold {asm['threshold']} eV, map says {c['threshold_eV']}")
        if (asm['arrow'] == '<->') != c['superelastic_in_set']:
            errors.append(f'id {ident}: reverse flag differs from the map')
        if asm['table'] != src['table']:
            errors.append(f"id {ident}: table differs from {ref['file']} block {ref['block']}")
        if asm['threshold'] != src['threshold'] or asm['line3'] is None or asm['line3'] != src['line3']:
            errors.append(f"id {ident}: threshold differs from {ref['file']} block {ref['block']}")
        declared = set(c.get('conventions', []))
        if digest == ref['sha256']:
            # the assembled file is the source file: the block itself must be the one cited
            if asm['raw'] != src['raw'] or asm['ordinal'] != src['ordinal']:
                errors.append(f"id {ident}: assembled block {asm['ordinal']} is not {ref['file']} block {ref['block']}")
            need, bad = set(), []
        else:
            need, bad = needed_conventions(src, asm)
            prov = (ref['file'], ref['sha256'], str(ref['block']), str(ref['line']), ref['block_sha256'])
            if asm['provenance'] != prov:
                errors.append(f'id {ident}: assembled provenance comment differs from the entry source')
            if (asm['conventions'] or set()) != declared:
                errors.append(f"id {ident}: assembled block declares conventions {sorted(asm['conventions'] or [])}, "
                              f"map entry {sorted(declared)}")
        for b in bad:
            errors.append(f'id {ident}: {b}, which no convention licenses')
        if need != declared:
            errors.append(f'id {ident}: transformation from the source needs conventions {sorted(need)}, '
                          f'entry declares {sorted(declared)}')
        for name_ in need:
            uses[name_].add(ident)

    # 5. the declared_conventions registry: mandatory, complete, consistent
    registry = {}
    for conv in doc.get('declared_conventions') or []:
        name_ = conv.get('name')
        if name_ in registry:
            errors.append(f'convention {name_}: declared twice')
        registry[name_] = conv
        if name_ not in CONVENTIONS:
            errors.append(f'convention {name_!r}: not one this checker can verify ({", ".join(CONVENTIONS)})')
        if not isinstance(conv.get('statement'), str) or not conv['statement'].strip():
            errors.append(f'convention {name_}: no statement')
    on_entries = collections.defaultdict(set)
    for c in channels:
        for name_ in c.get('conventions', []):
            on_entries[name_].add(c['id'])
    for name_ in sorted(set(uses) | set(on_entries) | set(registry), key=str):
        applies = set((registry.get(name_) or {}).get('applies_to') or [])
        if (uses[name_] or on_entries[name_]) and name_ not in registry:
            errors.append(f'convention {name_}: used by ids {sorted(uses[name_] | on_entries[name_])} '
                          f'but not declared')
        elif applies != on_entries[name_]:
            errors.append(f'convention {name_}: applies_to {sorted(applies)} differs from the entries '
                          f'carrying it {sorted(on_entries[name_])}')

    # 6. every source block accounted for exactly once
    listed = collections.Counter()
    for n in doc['not_assembled']:
        src = doc['sources'].get(n['source'])
        if src is None:
            errors.append(f"not_assembled: unknown source {n['source']}")
            continue
        key = (src['file'], n['block'])
        listed[key] += 1
        if key in refs:
            errors.append(f'source {key[0]} block {key[1]}: both mapped and listed as not assembled')
        b = src_blocks.get(src['file'], {}).get(n['block'])
        if src['file'] in src_blocks and b is None:
            errors.append(f'not_assembled: source {key[0]} has no block {key[1]}')
        elif b is not None:
            if b['sha256'] != n['block_sha256']:
                errors.append(f'not_assembled: block SHA-256 differs from {key[0]} block {key[1]}')
            if b['process'] != n['process']:
                errors.append(f'not_assembled: process differs from {key[0]} block {key[1]}')
    for key, n in listed.items():
        if n > 1:
            errors.append(f'source {key[0]} block {key[1]}: listed {n} times as not assembled')
    for fname, bl in src_blocks.items():
        for o in bl:
            if (fname, o) not in refs and not listed[(fname, o)]:
                errors.append(f'source {fname} block {o}: neither mapped nor listed as not assembled')

    # 7. LoKI-B's own collision list
    if args.loki_rates and not os.path.isfile(args.loki_rates):
        errors.append(f'--loki-rates {args.loki_rates}: not found')
    elif args.loki_rates:
        solved = set()
        for line in open(args.loki_rates).read().splitlines()[1:]:
            m = re.match(r'\s*\S+\s+\S+\s+(e \+ .*)$', line)
            if m:
                solved.add(m.group(1).strip())
        for label in sorted(solved - set(mapped)):
            errors.append(f'LoKI-B solved a collision the map does not carry: {label}')
        for label in sorted(set(mapped) - solved):
            errors.append(f'map entry LoKI-B did not solve: {label}')

    print(f"channels {len(channels)}; classes {dict(sorted(counts.items(), key=str))}; "
          f"not assembled {len(doc['not_assembled'])}; collisions in the assembled files {len(found)}; "
          f"source blocks re-derived {sum(len(b) for b in src_blocks.values())}; "
          f"conventions {dict(sorted((k, len(v)) for k, v in on_entries.items()))}")
    for e in errors:
        print('FAIL', e)
    if errors:
        print(f'RESULT: FAIL ({len(errors)} problems)')
        return 1
    print('RESULT: PASS (every entry verified against its source block; 0 unmapped, 0 mismatches)')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('map', help='the channel-map YAML')
    parser.add_argument('--assembled', required=True, help='directory holding the assembled LoKI-B files')
    parser.add_argument('--sources', action='append', required=True,
                        help='directory holding source LXCat files (repeatable); required, as every entry is '
                             'verified against its source')
    parser.add_argument('--loki-rates', help='a LoKI-B rateCoefficients.txt solved on the assembled set')
    parser.add_argument('--database', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input'),
                        help="the database 'input' directory holding the RMG libraries the map names "
                             '(default: the one beside this script)')
    sys.exit(check(parser.parse_args()))
