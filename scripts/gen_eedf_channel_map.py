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
Generate the frozen argon EEDF channel map (input/eedf/argon_channel_map.yaml) from the files it
describes. Everything in the map is derived here, deterministically, except the class and RMG reaction of
each collision and the RMG record each species stands for, which come from the hand-written overlay
(input/eedf/argon_channel_overlay.yaml):

  - the collision-file inventory: every regular file in the assembled directory, with its SHA-256; a file
    holding a 'PARAM.:' line is a collision file and is read as LoKI-B reads it;
  - each collision's LoKI-B label, threshold and reverse flag, and the source block it was built from:
    the same block of a byte-identical source file, or the block named in its I-341 provenance comment;
  - the conventions each collision needs, from the difference between its source block and the
    collision itself, and each convention's statement, written from the collisions it covers;
  - the state catalogue: 2J+1 statistical weights, Paschen names from the order of the ground-state
    excitation thresholds, Racah names from the rename table, each checked against the source data;
  - the source pool: exactly the files the assembled directory's own manifest.json names, known by their
    SHA-256 and recorded under the manifest's file names, so a source left off the command line, or one
    that is not the manifest's, is refused; the collision files are likewise the manifest's loki_files;
    the manifest must agree with itself, and every field it declares (catalogues, counts, lists and each
    process's and not-assembled block's fields) with the manifest derived here from the files;
  - source attribution, from the DATABASE and PERMLINK lines of each source file's own header;
  - the source blocks not assembled, each with a reason derived from what the set uses and from the
    block's own table;
  - for each class-A collision, the RMG library index, status and missing species, from the reactions and
    species RMG's own loader loads from the library's two files, each read once (load_library: whatever RMG
    refuses is refused, with its message), each reaction found by its loaded species and direction, never
    by its label's text, cross-checked by its reactions.py read and compiled as the Python
    text RMG executes (an entry kept inside a string is not loaded; a file RMG cannot read as UTF-8 is
    refused), and its dictionary.txt, and the class_a_gaps list from those.

The overlay is checked against the source-verified collision and the RMG library (POLICY below): an
elastic collision is class B; an ionisation is class A and maps to an ionisation of the target's species
into the ion's; an excitation into a load-bearing 4s level is class A and maps to the excitation of the
target's species into the product's; an excitation above 4s is A (a radiative-cascade placeholder) or B,
the same for its whole family. Each LoKI-B state maps to one RMG species across the whole overlay, whose
reference record must be one atom of the state's element, with its charge and spin multiplicity; the
species must be in the library dictionary, or carry the canonical name of a missing 4s level. Every species
a reaction names, the electron included, has a reference record, and the record RMG loads for it from the
library must be that species by RMG's own comparison (identity_problem); each record's own state fields,
the reference's and the library's, must not contradict the state it stands for (state_problems). A reaction
held by an entry another way (the other way round, or with the other direction) is refused, even beside an
entry that holds it exactly.

Any problem, an unreadable input or an --output that cannot be written included, is reported with
RESULT: FAIL and nothing is written. scripts/check_eedf_channel_map.py runs the same
derivation and requires the committed map to equal its output byte for byte.

No cross-section value is read into the map or printed.

usage: gen_eedf_channel_map.py --overlay FILE --assembled DIR --source FILE [--source FILE ...]
                               [--database DIR] --output MAP
"""

import argparse
import ast
import collections
import hashlib
import io
import json
import logging
import math
import os
import re
import sys
import tempfile
import traceback

import yaml

SCHEMA = 'eedf-channel-map/2'
SET = 'ar-v1'
TICKET = 'I-341'
LIBRARY = 'PlasmaArgon'
MANIFEST = 'manifest.json'  # the assembled directory's own record of the sources the set was built from
# The parameters of RMG's KineticsLibrary.load_entry, in order, and those without a default: the call each
# entry(...) in a library's reactions.py makes, bound here as Python would bind it.
ENTRY_PARAMETERS = ('index', 'label', 'kinetics', 'degeneracy', 'duplicate', 'reversible', 'reference',
                    'referenceType', 'shortDesc', 'longDesc', 'allow_pdep_route', 'elementary_high_p',
                    'allow_max_rate_violation', 'metal', 'site', 'facet')
ENTRY_REQUIRED = ('index', 'label', 'kinetics')
HEX64 = re.compile(r'[0-9a-f]{64}')
HEADER = ('# Frozen argon electron-collision channel map (I-341). GENERATED by scripts/gen_eedf_channel_map.py from\n'
          '# the local LXCat files, argon_channel_overlay.yaml (class and RMG reaction per collision) and the RMG\n'
          '# library. Do not edit: scripts/check_eedf_channel_map.py regenerates it and requires byte equality.\n')
RULES = ("owner ruling 2026-10-02 on electron kinetics, section 6 (classes A explicit reaction, B energy-only, "
         "C diagnostic, D unsupported); owner ruling C3 (Ar 1s4/1s2 explicit); owner ruling 2026-10-08 on the "
         "excited-Ar elastic gap: '(a) Literature, (b) meanwhile'; owner ruling 2026-10-14 (generate and "
         "compare; the 4s mixing source stays BSR, NGFSRDW is the sensitivity alternative)")
DATA_POLICY = ("No LXCat data or cross-section values are kept in this repository. Every entry names its source "
               "file by SHA-256 and block; the files stay in the local LXCat store.")

# --- LoKI-B's classic-file grammar (add5518) and the LXCat block layout ------------------------------------
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

# --- argon states -------------------------------------------------------------------------------------------
GROUND = 'Ar(1S0)'
SOURCE_GROUND = ('Ar', GROUND)  # how the source files write the ground state
LEVELS_1S = ('Ar(3P2)', 'Ar(3P1)', 'Ar(3P0)', 'Ar(1P1)')  # the load-bearing 4s levels (owner ruling C3)
LUMPED = 'Ar*'
# State names the STATE_RENAME convention may rewrite, source name -> LoKI-B name: the argon 4s levels
# from Racah to the IST-Lisbon LS-term names, and the ion to the IST-Lisbon ion state.
STATE_RENAMES = {
    'Ar(4s[3/2]2)': 'Ar(3P2)',
    'Ar(4s[3/2]1)': 'Ar(3P1)',
    "Ar(4s'[1/2]0)": 'Ar(3P0)',
    "Ar(4s'[1/2]1)": 'Ar(1P1)',
    'Ar(+)': 'Ar(+,gnd)',
}
CONVENTIONS = ('ELASTIC_REUSE_GROUND', 'DETAILED_BALANCE_INVERSE', 'LUMPED_TARGET_PER_LEVEL', 'STATE_RENAME')
# A 1s<->1s threshold must equal the difference of the two levels' ground-state excitation thresholds.
LEVEL_GAP_TOLERANCE_EV = 0.01

# --- the RMG side ---------------------------------------------------------------------------------------------
ELECTRON_SPECIES = 'e-'
CASCADE_PRODUCT = 'Ar(1s_i)'  # placeholder for whichever 4s level the radiative cascade ends in
PHOTON = 'hv'
SPECIES_NAME = re.compile(r'[A-Za-z][A-Za-z0-9_()+\-]*')
# Which classes each source-derived family may take, and the reaction shape a class-A entry must have.
POLICY = collections.OrderedDict([
    ('elastic', {
        'classes': ['B'],
        'reaction': None,
        'rule': 'elastic: electron energy and momentum transfer only, no species transition; energy-only (B)'}),
    ('ionization', {
        'classes': ['A'],
        'reaction': '<target species> + e- => <ion species> + e- + e-',
        'rule': 'ionisation changes the charge state: an explicit ionisation reaction (A), owner ruling C3 '
                'section 3 and section 6'}),
    ('excitation into 4s', {
        'classes': ['A'],
        'reaction': '<target species> + e- => <product species> + e- (<=> when the collision is <->)',
        'rule': 'the product is a load-bearing 4s level: an explicit reaction producing its species (A); owner '
                'ruling C3 makes 1s4 and 1s2 explicit and section 6 forbids an energy-only treatment'}),
    ('excitation above 4s', {
        'classes': ['A', 'B'],
        'reaction': '<target species> + e- => Ar(1s_i) + e- + hv',
        'rule': 'the product radiates into the 4s levels: a radiative-cascade placeholder (A) or energy-only (B), '
                'one class for the whole family (I-341 report section 5)'}),
])


class Overlay(yaml.SafeLoader):
    """A YAML loader that refuses duplicate keys and keys that are not strings, and reads only the scalar
    types the overlay's schema can use: a date or time is not one, so an unquoted 2026-02-30 is the string
    it is written as (which the schema then refuses), never a date that cannot be constructed."""


Overlay.yaml_implicit_resolvers = {
    first: [(tag, regexp) for tag, regexp in resolvers if tag != 'tag:yaml.org,2002:timestamp']
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def _mapping(loader, node, deep=False):
    keys = set()
    for key_node, _ in node.value:
        if not (isinstance(key_node, yaml.ScalarNode) and key_node.tag == 'tag:yaml.org,2002:str'):
            raise yaml.constructor.ConstructorError(None, None, f'key {key_node.value!r} is not a string',
                                                    key_node.start_mark)
        if key_node.value in keys:
            raise yaml.constructor.ConstructorError(None, None, f'key {key_node.value!r} appears twice',
                                                    key_node.start_mark)
        keys.add(key_node.value)
    return loader.construct_mapping(node, deep=deep)


Overlay.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


class _Dumper(yaml.SafeDumper):
    pass


def _list(dumper, data):
    flow = all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in data)
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=flow)


_Dumper.add_representer(list, _list)
_Dumper.add_representer(collections.OrderedDict, lambda d, x: d.represent_dict(x))


def render(doc):
    """The map's exact text: the fixed header, then the document in one fixed YAML style."""
    return HEADER + yaml.dump(doc, Dumper=_Dumper, sort_keys=False, width=110, allow_unicode=False)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def blocks(text):
    """Yield (ordinal, line, raw text) of each collision block of a file's text: keyword line through the
    closing dashes.

    The text is read with universal newlines, so CRLF and CR become LF, and is rejoined with LF."""
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
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


def loki_lines(data):
    """A file's lines, from its bytes, as std::getline returns them (split at LF only, a CR before the LF
    kept), and the bytes outside the canonical character set: printable ASCII, tab, LF, and CR only before
    an LF."""
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
    """The collision records LoKI-B reads from a classic file, and the reasons the generator refuses any.

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
    """The label LoKI-B prints for a descriptor (EedfCollisions.cpp operator<<), and why the generator
    refuses the descriptor, if it does.

    LoKI-B drops every electron term, whatever its place or count, and prints 'e + target -> e + [e + ]
    products, Type' from the heavy states alone. Only the form the real data use is accepted, on which that
    printed label is the descriptor's own heavy text: '[X + e -> Y + e, Type]', with '<->' for '->', one more
    '+ e' for Ionization, Type one of Elastic, Excitation or Ionization, and X and Y heavy states that LoKI-B
    prints back unchanged."""
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
         'line3': None, 'line3_rest': [], 'problems': [],
         'threshold': 0.0, 'descriptor': None, 'process': None, 'provenance': None, 'conventions': None}
    words = lines[2].split() if len(lines) > 2 else []
    first = words[0] if words else ''
    if re.fullmatch(NUMBER, first):
        b['line3'] = float(first)
        b['line3_rest'] = words[1:]
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


def table_points(b):
    """The (energy, value) rows of a block's table, as numbers. Used only for facts about the grid (repeated
    energies, where it starts, identity with another block); no value is written anywhere."""
    if b['table'] is None:
        return []
    rows = []
    for x in b['table'].split('\n')[1:-1]:
        m = ROW.fullmatch(x)
        if m:
            rows.append((float(m.group(1)), float(m.group(2))))
    return rows


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


def shell(state):
    """The outer configuration of an argon state name ('4s', '4p', '3d', ...), the 3p5 core skipped; '4s'
    for the IST-Lisbon LS-term names of the 4s levels."""
    if state in LEVELS_1S or STATE_RENAMES.get(state) in LEVELS_1S:
        return '4s'
    shells = re.findall(r'(?<![0-9])([1-9][spdf])(?![0-9])', state)
    return shells[0] if shells else None


def number(x):
    return f'{x:g}'


def lxcat_header(text):
    """The DATABASE and PERMLINK lines of a source file's own header, or None for each that is missing."""
    database = permlink = None
    for x in text.replace('\r\n', '\n').replace('\r', '\n').split('\n'):
        if x.startswith('DATABASE:') and database is None:
            database = x[len('DATABASE:'):].strip()
        elif x.startswith('PERMLINK:') and permlink is None:
            permlink = x[len('PERMLINK:'):].strip()
    return database, permlink


class RecordsOf(logging.Handler):
    """A logging handler that keeps the records instead of printing them."""

    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)


def library_files(database, library, require_reactions=True):
    """The bytes of a library's reactions.py and dictionary.txt, each file opened and read exactly once, and
    the problems that stop them being read: (reactions, dictionary, problems), or None when the library is
    not there. Everything the generator knows of the library comes from these bytes: RMG's loader loads a
    private copy of them and the readers here parse them, so a file saved meanwhile is never seen."""
    folder = os.path.join(database, 'kinetics', 'libraries', library)
    paths = [os.path.join(folder, name) for name in ('reactions.py', 'dictionary.txt')]
    if require_reactions and not os.path.isfile(paths[0]) or not os.path.isdir(folder):
        return None
    out, problems = [], []
    for path in paths:
        try:
            with open(path, 'rb') as fh:
                out.append(fh.read())
        except FileNotFoundError:
            out.append(None)
        except OSError as exc:
            out.append(None)
            problems.append(f'library {library} {os.path.basename(path)}: cannot be read ({type(exc).__name__})')
    return out[0], out[1], problems


def as_text(data):
    """Bytes decoded as Python's UTF-8 text mode decodes a file (universal newlines), or None."""
    if data is None:
        return None
    try:
        return io.TextIOWrapper(io.BytesIO(data), encoding='utf-8').read()
    except UnicodeDecodeError:
        return None


# The fields RMG's Molecule.is_isomorphic compares besides the graph, in the order a refusal names them; they
# only explain RMG's verdict, never replace it
STATE_FIELDS = ('multiplicity', 'electronic_state', 'vibrational_level', 'metal', 'facet')
# A reaction of a kinetics library as RMG loaded it: its label, the dictionary labels of its reactants and of
# its products (each sorted), and whether it is reversible
LoadedReaction = collections.namedtuple('LoadedReaction', 'label reactants products reversible')


def identity_problem(loaded, reference):
    """Why an RMG Species as loaded is not the species a reference Molecule means, or None. The verdict is RMG's
    own comparison (Species.is_isomorphic, strict: the graph with its electrons and charges, and every state
    field RMG keeps); the fields named are those that differ, else the structure."""
    if loaded.is_isomorphic(reference, strict=True):
        return None
    molecule = loaded.molecule[0]
    differs = [f'{field} {getattr(molecule, field)!r}, the reference {getattr(reference, field)!r}'
               for field in STATE_FIELDS if getattr(molecule, field) != getattr(reference, field)]
    if not differs:
        a, b = molecule.get_formula(), reference.get_formula()
        differs = [f'structure: RMG loads {a}, the reference {b}' if a != b
                   else 'structure: its atoms, bonds or electrons differ']
    return '; '.join(differs)


def state_problems(molecule, state):
    """Why an RMG record's own state fields contradict what it stands for, as a list: a vibrational level, metal
    or facet on a free gas-phase atom or electron, an electron that is not a doublet, and, when it stands for a
    LoKI-B state (None for the electron), an electronic-state label that is not that state's LS term, or any
    label on a state the source gives no term for. Fields RMG leaves at their defaults say nothing and pass."""
    from rmgpy.molecule import Molecule
    blank, problems = Molecule(), []
    if state is None and molecule.multiplicity != 2:
        problems.append(f'multiplicity {molecule.multiplicity!r}, but a free electron has spin 1/2, multiplicity 2')
    for field in ('vibrational_level', 'metal', 'facet'):
        if getattr(molecule, field) != getattr(blank, field):
            problems.append(f'{field} {getattr(molecule, field)!r}, but it stands for a free gas-phase '
                            f'{"atom" if state else "electron"}, which has none')
    label = molecule.electronic_state
    if state is not None and label != blank.electronic_state:
        term = re.fullmatch(r'[A-Z][a-z]?\((\d[SPDFG]\d)\)', state)
        if not term:
            problems.append(f'electronic_state {label!r}, but the source gives {state} no term to compare it with')
        elif label != term.group(1):
            problems.append(f'electronic_state {label!r}, but it stands for {state}, the term {term.group(1)}')
    return problems


def reference_records(references):
    """{label: RMG Molecule} of the overlay's reference records, as RMG reads an adjacency list, and the
    problems: a record RMG cannot read is refused with RMG's message."""
    try:
        from rmgpy.molecule import Molecule
    except Exception:  # load_library reports that RMG cannot be imported
        return {}, []
    records, problems = {}, []
    for label, text in references.items():
        try:
            records[label] = Molecule().from_adjacency_list(text)
        except Exception as exc:
            said = str(exc).strip().split('\n')[0][:200]
            problems.append(f'overlay species {label}: its reference record is not one RMG reads '
                            f'({type(exc).__name__}: {said})')
    return records, problems


def load_library(database, library):
    """The reactions and species of a kinetics library as RMG's own loader loads them, and the problems:
    (reactions, species, problems), reactions {index: LoadedReaction} and species {label: RMG Species}, both None
    when the library is not there or is refused.

    Each file is read once (library_files). Those bytes are written to a private copy, which RMG loads
    exactly as KineticsDatabase.load_libraries loads a library (KineticsLibrary(label=...).load(path,
    local_context, global_context), with a KineticsDatabase's contexts); whatever RMG raises is the refusal,
    with RMG's message. The reactions and species are then RMG's objects: the species dictionary it parsed
    while loading, and each loaded reaction known by the dictionary labels of the very species objects RMG
    resolved its reactants and products to, and its direction, never by its label's text. A participant that
    is not one of the dictionary's species cannot be matched and is refused. The readers here
    (entries_from_text, species_from_text) parse the same bytes and must agree with RMG on the entries'
    indices and labels and on the species' labels; a disagreement is refused, naming it, and so are their
    own refusals (a form they do not read, a label or multiplicity given twice). RMG's own logging during
    the load is kept, not printed. RMG must be importable (RMG-Py on PYTHONPATH)."""
    files = library_files(database, library)
    if files is None:
        return None, None, []
    content, dictionary, problems = files
    if problems:
        return None, None, problems
    folder = os.path.join(database, 'kinetics', 'libraries', library)
    root, kept = logging.getLogger(), RecordsOf()
    handlers, level = root.handlers[:], root.level
    root.handlers, root.level = [kept], logging.DEBUG
    try:
        try:
            from rmgpy.data.kinetics.database import KineticsDatabase
            from rmgpy.data.kinetics.library import KineticsLibrary
        except Exception as exc:
            return None, None, [f'library {library}: RMG cannot be imported ({type(exc).__name__}: {exc}), so the '
                                f'library cannot be loaded as RMG loads it; put RMG-Py on PYTHONPATH']
        from rmgpy.molecule import Molecule
        lacking = [field for field in STATE_FIELDS if not hasattr(Molecule(), field)]
        if lacking:  # an RMG-Py too old to keep them: no loaded record could be compared whole
            where = os.path.dirname(os.path.dirname(os.path.abspath(sys.modules['rmgpy'].__file__)))
            return None, None, [f"library {library}: the RMG-Py on PYTHONPATH ({where}) keeps no "
                                f"{', '.join(lacking)} on a molecule, so a loaded species cannot be compared whole "
                                f"with its reference; put an RMG-Py that does on PYTHONPATH"]

        class Loaded(KineticsLibrary):
            """RMG's KineticsLibrary, keeping the species dictionary its load parses."""
            parsed = None

            def get_species(self, *args, **kwargs):
                self.parsed = super().get_species(*args, **kwargs)
                return self.parsed
        with tempfile.TemporaryDirectory() as scratch:
            copy = os.path.join(scratch, library)
            os.mkdir(copy)
            for name, data in (('reactions.py', content), ('dictionary.txt', dictionary)):
                if data is not None:
                    with open(os.path.join(copy, name), 'wb') as fh:
                        fh.write(data)
            try:
                kinetics, loaded = KineticsDatabase(), Loaded(label=library)
                loaded.load(os.path.join(copy, 'reactions.py'), kinetics.local_context, kinetics.global_context)
            except Exception as exc:
                def said(e):
                    text = str(e).replace(copy, folder).strip().split('\n')[0]
                    return f'{type(e).__name__}: ' + (text if len(text) <= 300 else text[:297] + '...')
                near = [r.getMessage().replace(copy, folder) for r in kept.records
                        if r.getMessage().startswith('Error occurred at or near line')]
                handling = exc.__context__  # RMG's own error report can fail while reporting the first error
                return None, None, [f"library {library}: RMG's own loader refuses it ({said(exc)}"
                                    + (f', raised while handling {said(handling)}' if handling is not None else '')
                                    + ')' + (f'; {near[0][0].lower()}{near[0][1:]}' if near else '')]
    finally:
        root.handlers, root.level = handlers, level
    problems = [f'library {library} reactions.py: entry {entry.label!r}: index {index!r} is not a whole number'
                for index, entry in loaded.entries.items() if type(index) is not int]  # RMG keeps any key
    if problems:
        return None, None, problems
    species = dict(loaded.parsed or {})
    label_of = {id(x): label for label, x in species.items()}
    reactions = {}
    for index, entry in sorted(loaded.entries.items()):
        reaction = entry.item
        who = [label_of.get(id(x)) for x in list(reaction.reactants) + list(reaction.products)]
        if None in who:
            problems.append(f'library {library} reactions.py: entry {index}: a participant RMG loaded is not one '
                            f'of the dictionary species, so the reaction cannot be known by its species')
            continue
        n = len(reaction.reactants)
        reactions[index] = LoadedReaction(entry.label, tuple(sorted(who[:n])), tuple(sorted(who[n:])),
                                  bool(reaction.reversible))
    problems += reconcile_library(library, {i: x.label for i, x in loaded.entries.items()}, species,
                                  as_text(content), as_text(dictionary))
    return (None, None, problems) if problems else (reactions, species, [])


def reconcile_library(library, entries, species, content, dictionary):
    """The problems where the readers here, on the same bytes, read the library otherwise than RMG loaded it."""
    problems = []
    own_entries, entry_problems = entries_from_text(library, content, dictionary)
    own_species, species_problems = species_from_text(library, dictionary)
    problems.extend(entry_problems + species_problems)
    where = f'library {library}'
    if not entry_problems and own_entries is not None:
        for index in sorted(set(entries) | set(own_entries)):
            if entries.get(index) != own_entries.get(index):
                problems.append(f'{where} reactions.py: entry {index}: RMG loads {entries.get(index)!r}, this '
                                f'reader reads {own_entries.get(index)!r}')
    if not species_problems and own_species is not None:
        for label in list(species) + [x for x in own_species if x not in species]:
            if label not in own_species or label not in species:
                problems.append(f'{where} dictionary.txt: species {label!r}: '
                                + ('RMG loads it, this reader does not' if label in species
                                   else 'this reader reads it, RMG does not'))
    return problems


def rmg_library_load(database, library):
    """The problems of load_library(): RMG's refusal, or the readers' disagreement with what RMG loaded."""
    return load_library(database, library)[2]


# what ast.literal_eval raises on a malformed value, such as a list as a dictionary key
LITERAL_ERRORS = (ValueError, TypeError, SyntaxError, RecursionError, MemoryError)


def library_entries(database, library):
    """index -> label of the entries RMG loads from a kinetics library's reactions.py (None when it is not
    there), and the problems that stop the file being read that way.

    RMG executes the file and loads one entry per entry(...) call it runs. The file is parsed as Python, not
    searched as text, and only the forms whose effect is certain without running it are read: a top-level
    entry(...) call with a literal index and label, given by keyword in any order or by position, which RMG
    loads; a top-level string or other constant, which loads nothing, so an entry kept inside a string is not
    loaded; and an assignment of a literal to a name other than 'entry'. Any other statement could load,
    skip or repeat an entry, so it is refused rather than guessed at. The file must also compile, and each
    call must bind to RMG's load_entry parameters (ENTRY_PARAMETERS) as Python binds it: no parameter given
    twice, by keyword or by position and keyword, none unknown, and index, label and kinetics given."""
    files = library_files(database, library)
    if files is None:
        return None, []
    if files[2]:
        return None, files[2]
    return entries_from_text(library, *(as_text(x) for x in files[:2]))


def entries_from_text(library, content, dictionary):
    """library_entries() for the texts of reactions.py and dictionary.txt as read once (library_files)."""
    path = f'reactions.py of {library}'
    where = f'library {library} reactions.py'
    content, why = rmg_library_text(content, dictionary)
    if why:
        return None, [f'{where}: {why}']
    try:
        compile(content, path, 'exec', dont_inherit=True)  # the string RMG executes, as RMG compiles it
        tree = ast.parse(content, filename=path)
    except (SyntaxError, ValueError) as exc:
        return None, [f'{where}: cannot be read as Python ({type(exc).__name__}: {exc})']
    entries, problems = {}, []
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            continue
        if isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id != 'entry' for t in node.targets):
            try:
                ast.literal_eval(node.value)
                continue
            except LITERAL_ERRORS:
                pass
        call = node.value if isinstance(node, ast.Expr) else None
        if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == 'entry'):
            problems.append(f'{where}: line {node.lineno}: a {type(node).__name__} statement, so what RMG loads '
                            f'cannot be read without running the file; only top-level entry(...) calls, strings '
                            f'and literal assignments are read')
            continue
        bound, why = entry_arguments(call)
        if why:
            problems.append(f'{where}: line {node.lineno}: entry(...) {why}, so RMG does not load it as written')
            continue
        try:
            index, label = ast.literal_eval(bound['index']), ast.literal_eval(bound['label'])
        except LITERAL_ERRORS:
            index = label = None
        if type(index) is not int or not isinstance(label, str):
            problems.append(f'{where}: line {node.lineno}: an entry(...) call without a literal integer index '
                            f'and string label')
        elif index in entries:
            problems.append(f'{where}: line {node.lineno}: index {index} appears twice, and RMG refuses the '
                            f'library')
        else:
            entries[index] = label
    return entries, problems


GENERATION_LINE = re.compile(r'^(?:#|!|//) RMG-PAIR-GENERATION(?:\s|$)')
GENERATION_MARKER = re.compile(r'^(?:#|!|//) RMG-PAIR-GENERATION (v1-sha256:[0-9a-f]{64})$')


def generation_token(text):
    """The RMG-PAIR-GENERATION token of a library file's text, as rmgpy.util.generation_token reads it."""
    lines = [x for x in text.splitlines() if GENERATION_LINE.match(x)]
    if not lines:
        return None
    m = GENERATION_MARKER.fullmatch(lines[0]) if len(lines) == 1 else None
    return m.group(1) if m else 'invalid'


def rmg_library_text(content, dictionary):
    """The text RMG executes for a library's reactions.py, and why it cannot (None when it can), from the
    texts of reactions.py and its dictionary.txt as read (library_files).

    As rmgpy.util.read_generation_pair: both files are UTF-8 text (so a byte that is not UTF-8 is refused
    whatever encoding cookie the file declares, and a byte-order mark is kept as a character that does not
    compile), their generation markers must agree, and the marker line is removed from the text. RMG then
    executes that string, so it is that string that is compiled here."""
    if content is None or dictionary is None:
        return None, 'cannot be read as UTF-8 text with its dictionary.txt, as RMG reads them'
    first, second = generation_token(content), generation_token(dictionary)
    if first != second or first == 'invalid':
        return None, (f"its RMG-PAIR-GENERATION marker {first} does not match dictionary.txt's {second}, so RMG "
                      f"refuses it")
    kept = [x for x in content.splitlines(keepends=True) if not GENERATION_MARKER.fullmatch(x.rstrip('\r\n'))]
    return ''.join(kept), None


def entry_arguments(call):
    """The parameter -> argument binding of one entry(...) call, as Python binds it against RMG's load_entry,
    and why it does not bind (None when it does)."""
    if any(isinstance(a, ast.Starred) for a in call.args) or any(k.arg is None for k in call.keywords):
        return None, 'unpacks its arguments (* or **)'
    if len(call.args) > len(ENTRY_PARAMETERS):
        return None, f'gives {len(call.args)} positional arguments, more than load_entry takes'
    bound = dict(zip(ENTRY_PARAMETERS, call.args))
    for k in call.keywords:
        if k.arg not in ENTRY_PARAMETERS:
            return None, f"gives '{k.arg}', which load_entry does not take"
        if k.arg in bound:
            return None, f"gives '{k.arg}' twice"
        bound[k.arg] = k.value
    missing = [x for x in ENTRY_REQUIRED if x not in bound]
    if missing:
        return None, f"does not give {', '.join(missing)}"
    return bound, None


def library_species(database, library):
    """label -> the lines of its record, for each species in a kinetics library's dictionary.txt (None when it
    is not there or cannot be read), and the problems. Only the labels are compared with what RMG loads: a
    species is what RMG parses its record to (load_library, identity_problem), never a summary read here."""
    files = library_files(database, library, require_reactions=False)
    if files is None or files[1] is None and not files[2]:
        return None, []
    if files[2]:
        return None, files[2]
    text = as_text(files[1])
    if text is None:
        return None, [f'library {library} dictionary.txt: cannot be read as UTF-8 text (UnicodeDecodeError)']
    return species_from_text(library, text)


def species_from_text(library, text):
    """library_species() for the text of dictionary.txt as read once (library_files). As RMG's get_species
    reads it: a '//' and what follows it on a line is a comment, and a blank line ends a record. A label
    declared twice, or a record stating its multiplicity twice, is refused."""
    species, problems, where = {}, [], f'library {library} dictionary.txt'
    text = '\n'.join(x.split('//', 1)[0] for x in text.split('\n'))
    for chunk in re.split(r'\n\s*\n', text.strip()):
        lines = [x.strip() for x in chunk.strip().split('\n') if x.strip()]
        if not lines:
            continue
        if lines[0] in species:
            problems.append(f'{where}: species {lines[0]} is declared twice; each label may be declared once')
            continue
        stated = [m.group(1) for m in (re.fullmatch(r'multiplicity\s+(\d+)', x) for x in lines[1:]) if m]
        if len(stated) > 1:
            problems.append(f'{where}: species {lines[0]} states its multiplicity twice '
                            f'({", ".join(stated)}); it may be stated once')
        species[lines[0]] = lines[1:]
    return (None if problems else species), problems


def ls_term(state):
    """(spin multiplicity, J) of an LS-term state name such as 'Ar(3P2)', or None."""
    m = re.fullmatch(r'[A-Z][a-z]?\((\d)[SPDFG](\d)\)', state)
    return (int(m.group(1)), int(m.group(2))) if m else None


def state_charge(state):
    m = HEAVY.fullmatch(state)
    q = re.match(r'(\++|-+),', m.group(2)) if m else None
    return (len(q.group(1)) if q.group(1)[0] == '+' else -len(q.group(1))) if q else 0


def parse_reaction(text):
    """(reactants, arrow, products) of an RMG reaction label, or None when it is not one."""
    m = re.fullmatch(r'(.+?) (<=>|=>) (.+)', text)
    if not m:
        return None
    lhs, rhs = m.group(1).split(' + '), m.group(3).split(' + ')
    if not all(SPECIES_NAME.fullmatch(s) for s in lhs + rhs):
        return None
    return lhs, m.group(2), rhs


def invalid_unicode(value):
    """The first string in a parsed YAML value, keys included, that is not valid Unicode text (a lone
    surrogate such as "\\uD800", which YAML's escapes can write), or None."""
    pending = [value]
    while pending:
        x = pending.pop()
        if isinstance(x, str):
            try:
                x.encode('utf-8')
            except UnicodeEncodeError:
                return x
        elif isinstance(x, dict):
            pending.extend(list(x) + list(x.values()))
        elif isinstance(x, list):
            pending.extend(x)
    return None


def printable(text):
    """text as standard output can print it: what its encoding cannot hold is escaped, never an error."""
    encoding = sys.stdout.encoding or 'utf-8'
    return text.encode(encoding, 'backslashreplace').decode(encoding)


def load_overlay(path):
    """The overlay's collisions, {label: {'class': str, 'reaction': str or None}}, and the problems that
    refuse it (load_overlay_document, without the species' reference records)."""
    collisions, _, problems = load_overlay_document(path)
    return collisions, problems


def load_overlay_document(path):
    """The overlay, read once, as (collisions, references, problems): collisions {label: {'class': str,
    'reaction': str or None}}, references {species label: the text of its RMG record}.

    The overlay must be UTF-8 YAML with the top-level key 'collisions', mapping each LoKI-B label to a
    mapping with 'class' and, optionally, 'reaction', both strings, and the key 'species', mapping each RMG
    species the reactions name to the RMG dictionary record (adjacency list) it stands for. Anchors,
    aliases, explicit tags, duplicate keys and non-string keys are refused, so nothing in it can be read two
    ways, and so is a string that is not valid Unicode text."""
    where = f'overlay {os.path.basename(path)}'
    try:
        text = open(path, 'rb').read().decode('utf-8')
    except (OSError, UnicodeDecodeError) as exc:
        return None, None, [f'{where}: cannot be read as UTF-8 text ({type(exc).__name__})']
    try:
        for event in yaml.parse(text, Loader=Overlay):
            if isinstance(event, yaml.AliasEvent) or getattr(event, 'anchor', None):
                return None, None, [f'{where}: line {event.start_mark.line + 1}: anchors and aliases are not allowed']
            if getattr(event, 'tag', None) is not None:
                return None, None, [f'{where}: line {event.start_mark.line + 1}: explicit tags are not allowed']
        doc = yaml.load(text, Loader=Overlay)
    except yaml.YAMLError as exc:
        first = str(exc).splitlines()[0] if str(exc) else type(exc).__name__
        return None, None, [f'{where}: not valid overlay YAML ({first})']
    except RecursionError:
        return None, None, [f'{where}: nested too deeply to read']
    except (ValueError, TypeError, OverflowError) as exc:  # a scalar the loader cannot construct
        return None, None, [f'{where}: holds a value that cannot be read ({type(exc).__name__}: {exc})']
    bad = invalid_unicode(doc)
    if bad is not None:
        return None, None, [f'{where}: holds a string that is not valid Unicode text ({ascii(bad)[:80]})']
    if not isinstance(doc, dict) or 'collisions' not in doc or not set(doc) <= {'collisions', 'species'} \
            or not isinstance(doc['collisions'], dict) or not isinstance(doc.get('species', {}), dict):
        return None, None, [f"{where}: must be a mapping with the key 'collisions' and, optionally, 'species', "
                            f"each itself a mapping"]
    problems, out = [], {}
    for label, entry in doc['collisions'].items():
        if not isinstance(entry, dict) or not set(entry) <= {'class', 'reaction'} or 'class' not in entry:
            problems.append(f"{where}: {label!r}: needs 'class' and, optionally, 'reaction', and nothing else")
            continue
        if not isinstance(entry['class'], str):
            problems.append(f"{where}: {label!r}: class {entry['class']!r} is not a string")
            continue
        if entry.get('reaction') is not None and not isinstance(entry['reaction'], str):
            problems.append(f"{where}: {label!r}: reaction {entry['reaction']!r} is not a string")
            continue
        out[label] = {'class': entry['class'], 'reaction': entry.get('reaction')}
    references = {}
    for label, record in (doc.get('species') or {}).items():
        if not isinstance(record, str):
            problems.append(f"{where}: species {label!r}: its record {record!r} is not a string")
            continue
        references[label] = record
    return out, references, problems


def manifest_field(record, field, kind, where, problems):
    """record[field] when it is of the given kind ('str', 'sha', 'count' or 'counts'), else None with the
    problem recorded: a malformed field is an input problem, never an error."""
    value = record.get(field) if isinstance(record, dict) else None
    good = {'str': lambda v: isinstance(v, str),
            'sha': lambda v: isinstance(v, str) and HEX64.fullmatch(v),
            'count': lambda v: type(v) is int and v >= 0,
            'counts': lambda v: isinstance(v, list) and all(type(x) is int and x >= 0 for x in v)}[kind]
    if not good(value):
        what = {'str': 'a string', 'sha': 'a SHA-256', 'count': 'a whole number',
                'counts': 'a list of whole numbers'}[kind]
        given = 'missing' if not isinstance(record, dict) or field not in record else repr(value)[:40]
        problems.append(f"{where}: '{field}' is {given}, not {what}")
        return None
    return value


def store_manifest(assembled):
    """What the store's own manifest.json says the set is, every field type-checked, and the problems that
    stop it being read or show it malformed or contradicting itself. Returns (manifest, problems), the
    manifest a dict holding:

      sources        [(key, file name, SHA-256, n_blocks, blocks_used)] in its order; the paths may be stale,
                     so a source is known by its SHA-256, under the file name the manifest gives it;
      loki_files     {collision file name: SHA-256}, or None when it cannot say;
      processes      [(i, file, LoKI-B label, source key, block, line, block SHA-256)];
      not_assembled  [(i, source key, block, line, block SHA-256)];
      doc            the document itself, for the field-by-field comparison.

    A member name declared twice in one object is refused (decode_manifest). The manifest must agree with
    itself: one file name and one hash per source, every source its records name among its sources with the
    same hash, and every process's file among its loki_files. generate()
    then compares the whole manifest, field by field, with the one the files give (derived_manifest)."""
    try:
        doc, repeated = decode_manifest(open(os.path.join(assembled, MANIFEST), 'rb').read())
    except (OSError, UnicodeDecodeError, ValueError, RecursionError) as exc:
        return empty_manifest(), [f'the store manifest {MANIFEST}: cannot be read ({type(exc).__name__}), so the '
                                      f'required source set is unknown']
    manifest, problems = read_manifest(doc)
    return manifest, repeated + problems


class Members(dict):
    """A JSON object as decoded: its members, and each member name it declares more than once with all the
    values declared, which a plain dict would drop but the last of."""
    repeated = {}


def json_object(pairs):
    out = Members(pairs)
    counts = collections.Counter(k for k, _ in pairs)
    out.repeated = {k: [v for name, v in pairs if name == k] for k, n in counts.items() if n > 1}
    return out


def repeated_members(node, at=''):
    """(field path, values) for every member name declared more than once, at any depth."""
    if isinstance(node, dict):
        for k, values in getattr(node, 'repeated', {}).items():
            yield (f'{at}[{k!r}]' if at else k), values
        for k, v in node.items():
            yield from repeated_members(v, f'{at}[{k!r}]' if at else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from repeated_members(v, f'{at}[{i}]')


def decode_manifest(data):
    """The manifest's JSON bytes decoded as UTF-8, and a problem for each member name an object declares more
    than once: JSON keeps only the last, so an earlier, stale declaration would never be compared. Returns
    (document, problems); raises what json.loads raises on text that is not JSON."""
    doc = json.loads(data.decode('utf-8'), object_pairs_hook=json_object)
    where = f'the store manifest {MANIFEST}'
    return doc, [f'{where}: {path} is declared {len(values)} times ({", ".join(short(v) for v in values)}); each '
                 f'member may be declared once' for path, values in repeated_members(doc)]


def empty_manifest():
    return {'sources': [], 'loki_files': None, 'processes': None, 'not_assembled': None, 'doc': None}



def read_manifest(doc):
    """store_manifest() for a manifest document already parsed from its JSON."""
    where = f'the store manifest {MANIFEST}'
    named = doc.get('sources') if isinstance(doc, dict) else None
    if not isinstance(named, dict) or not named:
        return empty_manifest(), [f"{where}: has no 'sources' mapping, so the required source set is unknown"]
    out, problems = dict(empty_manifest(), doc=doc), []
    for key, record in named.items():
        at = f'{where}: source {key}'
        digest = manifest_field(record, 'sha256', 'sha', at, problems)
        file = manifest_field(record, 'path', 'str', at, problems)
        n_blocks = manifest_field(record, 'n_blocks', 'count', at, problems)
        blocks_used = manifest_field(record, 'blocks_used', 'counts', at, problems)
        if digest is not None:
            out['sources'].append((key, os.path.basename(file) if file else key, digest, n_blocks, blocks_used))
    for what, values in (('file name', [x[1] for x in out['sources']]), ('SHA-256', [x[2] for x in out['sources']])):
        for value, n in collections.Counter(values).items():
            if n > 1:
                problems.append(f'{where}: {n} sources share the {what} {value}; each source needs its own')
    loki = doc.get('loki_files')
    if isinstance(loki, dict) and loki and all(isinstance(k, str) and isinstance(v, str) and HEX64.fullmatch(v)
                                               for k, v in loki.items()):
        out['loki_files'] = loki
    else:
        problems.append(f"{where}: has no 'loki_files' mapping of file name to SHA-256, so the collision files "
                        f"are unknown")
    digests = {x[0]: x[2] for x in out['sources']}
    for field in ('processes', 'not_assembled'):
        records = doc.get(field)
        if not isinstance(records, list):
            problems.append(f"{where}: '{field}' is {'missing' if field not in doc else 'not a list'}, so that "
                            f"inventory cannot be reconciled")
            continue
        out[field] = []
        for i, r in enumerate(records):
            at = f'{where}: {field}[{i}]'
            if field == 'processes':
                file = manifest_field(r, 'file', 'str', at, problems)
                label = manifest_field(r, 'loki_label', 'str', at, problems)
                src = r.get('source') if isinstance(r, dict) else None
                if not isinstance(src, dict):
                    problems.append(f"{at}: 'source' is missing, so the process has no source binding")
                    continue
                at += '.source'
                key = manifest_field(src, 'key', 'str', at, problems)
                digest = manifest_field(src, 'sha256', 'sha', at, problems)
            else:
                file = label = None
                src = r
                key = manifest_field(src, 'source_key', 'str', at, problems)
                digest = digests.get(key)
            binding = [manifest_field(src, f, k, at, problems)
                       for f, k in (('block', 'count'), ('line', 'count'), ('block_sha256', 'sha'))]
            if key is None or None in binding or (field == 'processes' and None in (file, label, digest)):
                continue
            if key not in named:
                problems.append(f"{at}: names source {key}, which the manifest's 'sources' do not, so it is "
                                f"incomplete")
                continue
            if digest != digests.get(key):
                problems.append(f'{at}: names source {key} with another SHA-256')
            if field == 'processes':
                if out['loki_files'] is not None and file not in out['loki_files']:
                    problems.append(f"{at[:-len('.source')]}: names collision file {file}, which its 'loki_files' "
                                    f"do not")
                out[field].append((i, file, label, key, *binding))
            else:
                out[field].append((i, key, *binding))
    return out, problems


class Prose(str):
    """A manifest field written as prose (a reason, a convention statement): it must be a string, its words
    are not compared."""


class StalePath(str):
    """A manifest path, which may be stale: it must be a string naming this file, its directory is not
    compared and it is never opened."""


MANIFEST_SOURCE_FIELDS = ('path', 'sha256', 'n_blocks', 'blocks_used')


def derived_manifest(manifest, linked, sources, used, not_assembled, files, weights, paschen):
    """The manifest the files themselves give: every field the store's manifest.json declares, derived from
    the sources, the assembled files and the state catalogue. The records of a source that was not read are
    left out, since that source is refused already."""
    key_of = {x[1]: x[0] for x in manifest['sources']}

    def binding(file, b):
        return collections.OrderedDict([('key', key_of.get(file)), ('file', file), ('path', StalePath(file)),
                                        ('sha256', sources[file]['sha256']), ('block', b['ordinal']),
                                        ('line', b['line']), ('block_sha256', b['sha256'])])
    out = collections.OrderedDict()
    out['set'], out['ticket'], out['local_only'] = SET, TICKET, Prose()
    out['loki_files'] = {name: digest for _, name, _, digest, _ in files}
    out['sources'] = collections.OrderedDict(
        (key_of[file], collections.OrderedDict([
            ('path', StalePath(file)), ('sha256', src['sha256']), ('n_blocks', len(src['blocks'])),
            ('blocks_used', sorted({o for (f, o) in used if f == file}))]))
        for file, src in sources.items() if file in key_of)
    out['statistical_weights'] = dict(weights)
    out['paschen'] = {s: paschen[s] for s in LEVELS_1S if s in paschen}
    out['conventions'] = {name: Prose() for name in CONVENTIONS if any(name in c['need'] for c in linked)}
    out['processes'] = collections.OrderedDict()
    for c in linked:
        asm = c['asm']
        out['processes'][(c['file'], c['label'])] = collections.OrderedDict([
            ('file', c['file']), ('loki_label', c['label']),
            ('descriptor', asm['descriptor'].group(0) if asm['descriptor'] else None), ('kind', asm['kind']),
            ('target', c['target']), ('product', c['product']), ('reverse', c['reverse']),
            ('threshold_eV', asm['threshold']), ('source', binding(c['src_file']['file'], c['src'])),
            ('conventions', frozenset(c['need'])), ('choice_reason', Prose())])
    out['not_assembled'] = collections.OrderedDict(
        ((b['source'], b['block']), collections.OrderedDict([
            ('source_key', key_of.get(b['source'])), ('block', b['block']), ('line', b['line']),
            ('block_sha256', b['block_sha256']), ('process', b['process']), ('reason', Prose())]))
        for b in not_assembled)
    return out


def short(value):
    text = repr(value)
    return text if len(text) <= 60 else text[:57] + '...'


def field_differences(declared, derived, at, problems):
    """Every difference between a declared manifest field and the derived one, each naming the field."""
    if isinstance(derived, Prose):
        if not isinstance(declared, str) or not declared.strip():
            problems.append(f'{at} is {short(declared)}, not prose')
    elif isinstance(derived, StalePath):
        if not isinstance(declared, str) or os.path.basename(declared) != derived:
            problems.append(f'{at} is {short(declared)}, not a path to {derived}')
    elif isinstance(derived, dict):
        if not isinstance(declared, dict):
            problems.append(f'{at} is {short(declared)}, the files give {short(dict(derived))}')
            return
        for key in derived:
            if key not in declared:
                problems.append(f'{at}[{key!r}] is missing; the files give {short(derived[key])}')
            else:
                field_differences(declared[key], derived[key], f'{at}[{key!r}]', problems)
        for key in declared:
            if key not in derived:
                problems.append(f'{at}[{key!r}] is declared ({short(declared[key])}), which the files do not give')
    elif isinstance(derived, frozenset):  # a set, written as a list in any order
        if not (isinstance(declared, list) and all(isinstance(x, str) for x in declared)
                and len(set(declared)) == len(declared) and set(declared) == derived):
            problems.append(f'{at} is {short(declared)}, the files give {short(sorted(derived))} (in any order)')
    elif isinstance(derived, list) and isinstance(declared, list) and all(type(x) is int for x in derived):
        if all(type(x) is int for x in declared) and declared != derived:  # else malformed, refused already
            missing = sorted(set(derived) - set(declared))
            extra = sorted(set(declared) - set(derived))
            problems.append(f'{at} differs from the files' + (f'; missing {missing}' if missing else '')
                            + (f'; extra {extra}' if extra else '')
                            + ('' if missing or extra else '; a block twice or out of order'))
    else:
        number = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)  # noqa: E731
        same = declared == derived and type(declared) is type(derived) or \
            number(declared) and number(derived) and declared == derived
        if not same:
            problems.append(f'{at} is {short(declared)}, the files give {short(derived)}')


def reconcile_manifest(manifest, derived):
    """The problems where the store's manifest differs from the one the files give (derived_manifest): every
    top-level field, every source, both state catalogues, the conventions, and every field of every process
    and not-assembled record. A process is known by its file and LoKI-B label and a not-assembled block by its
    source and ordinal; omissions, extras and duplicates are all refused. Prose need not be the same words."""
    where = f'the store manifest {MANIFEST}'
    problems = []
    doc = manifest['doc']
    if doc is None:
        return problems
    name_of = {x[0]: x[1] for x in manifest['sources']}
    read = derived['sources']  # the manifest keys of the sources read
    for key in derived:
        if key not in doc:
            problems.append(f"{where}: '{key}' is missing")
    for key in doc:
        if key not in derived:
            problems.append(f"{where}: '{key}' is declared, which the files do not give")
    for key in ('set', 'ticket', 'local_only', 'statistical_weights', 'paschen', 'conventions'):
        if key in doc:
            field_differences(doc[key], derived[key], f'{where}: {key}', problems)
    for key, record in derived['sources'].items():
        if isinstance(doc.get('sources', {}).get(key), dict):
            field_differences(doc['sources'][key], record, f'{where}: sources[{key!r}]', problems)

    def inventory(field, accepted, identity, show):
        if accepted is None:
            return
        records = doc[field]
        declared = [(identity(rec), rec[0]) for rec in accepted if rec_source(rec) in read]
        for key, n in collections.Counter(k for k, _ in declared).items():
            if n > 1:
                problems.append(f'{where}: {field} lists {show(key)} {n} times')
        first = dict(reversed(declared))
        for key, record in derived[field].items():
            if key not in first:
                problems.append(f'{where}: {field} does not list {show(key)}, which the store holds')
            else:
                field_differences(records[first[key]], record, f'{where}: {field}[{first[key]}] ({show(key)})',
                                  problems)
        for key in first:
            if key not in derived[field]:
                problems.append(f'{where}: {field} lists {show(key)}, which the store does not hold')

    def rec_source(rec):
        return rec[3] if len(rec) == 7 else rec[1]
    inventory('processes', manifest['processes'], lambda r: (r[1], r[2]), lambda k: f'{k[0]} collision {k[1]!r}')
    inventory('not_assembled', manifest['not_assembled'], lambda r: (name_of.get(r[1]), r[2]),
              lambda k: f'{k[0]} block {k[1]}')
    return problems


def generate(overlay_path, assembled, source_paths, database):
    """Derive the map. Returns (text, problems, summary, labels): the map text, the reasons it must not be
    written, a one-line summary and the LoKI-B labels of the collisions read. The text is produced even when
    there are problems, so that a check can say where it differs, but it must not be written then; only when
    RMG loaded no library (not importable, too old to keep a molecule's state fields, refusing the files, or
    none there) is there no text: that refusal is returned alone, before any record is read."""
    problems = []

    # 1. the source files: exactly those the store's manifest names, each block parsed from the file itself.
    #    The command line only says where each one is; the manifest says which are required.
    manifest, manifest_problems = store_manifest(assembled)
    problems.extend(manifest_problems)
    required, loki_manifest = [x[:3] for x in manifest['sources']], manifest['loki_files']
    given = {}  # SHA-256 -> (file name as given, text)
    for path in source_paths:
        name = os.path.basename(path)
        try:
            data = open(path, 'rb').read()
        except OSError as exc:
            problems.append(f'source {path}: cannot be read ({type(exc).__name__})')
            continue
        digest = hashlib.sha256(data).hexdigest()
        if digest in given:
            problems.append(f'source {name}: given twice')
            continue
        if required and digest not in {d for _, _, d in required}:
            problems.append(f'source {name} (SHA-256 {digest[:12]}...): not a source named by the store\'s '
                            f'manifest, which names {", ".join(f for _, f, _ in required)} by their hashes')
            continue
        try:
            given[digest] = (name, data.decode('utf-8'))
        except UnicodeDecodeError as exc:
            problems.append(f'source {name}: cannot be read as UTF-8 text (byte {exc.start})')
    for key, file, digest in required:
        if digest not in given:
            problems.append(f'source {key} ({file}, SHA-256 {digest[:12]}...) named by the store\'s manifest '
                            f'was not given (--source)')
    # each source under the manifest's own name for it, whatever it was given as: two files given under one
    # name from two folders stay two sources
    canonical = {d: f for _, f, d in required}
    sources = collections.OrderedDict()  # file name -> source record, in the manifest's order
    for digest in [d for _, _, d in required] or list(given):
        if digest not in given:
            continue
        name, text = canonical.get(digest, given[digest][0]), given[digest][1]
        if name in sources:
            problems.append(f'source {name}: two different files under this one name')
            continue
        database_name, permlink = lxcat_header(text)
        if database_name is None:
            problems.append(f'source {name}: no DATABASE line in its header, so it cannot be attributed')
        sources[name] = {'file': name, 'sha256': digest, 'database': database_name, 'permlink': permlink,
                         'blocks': collections.OrderedDict((o, parse_block(o, ln, raw)) for o, ln, raw in blocks(text))}
    if required and sorted((n, x['sha256']) for n, x in sources.items()) != \
            sorted((f, d) for _, f, d in required if d in given):
        problems.append("the sources read are not one-to-one with the store manifest's sources")
    by_sha = {s['sha256']: s for s in sources.values()}

    # 2. the assembled directory: every regular file, the collision files read as LoKI-B reads them. Byte
    #    copies of a source file come first, then the other collision files, each in name order.
    inventory, files = [], []
    names = []
    if not os.path.isdir(assembled):
        problems.append(f'--assembled {assembled}: not a directory')
    else:
        try:
            names = sorted(os.listdir(assembled))
        except OSError as exc:
            problems.append(f'--assembled {assembled}: cannot be listed ({type(exc).__name__})')
    for name in names:
        path = os.path.join(assembled, name)
        if not os.path.isfile(path):
            problems.append(f'{name}: not a regular file in the assembled directory')
            continue
        try:
            data = open(path, 'rb').read()
        except OSError as exc:
            problems.append(f'{name}: cannot be read ({type(exc).__name__})')
            continue
        digest = hashlib.sha256(data).hexdigest()
        inventory.append({'file': name, 'sha256': digest, 'collisions': 0})
        if b'PARAM.:' in data:
            files.append((digest not in by_sha, name, data, digest, inventory[-1]))
    files.sort(key=lambda x: (x[0], x[1]))
    # the collision files are exactly those the manifest names, with its hashes
    present = {name: digest for _, name, _, digest, _ in files}
    for name, digest in (loki_manifest or {}).items():
        if name not in present:
            problems.append(f"collision file {name} named by the store's manifest is not in the assembled directory")
        elif present[name] != digest:
            problems.append(f"collision file {name}: SHA-256 {present[name][:12]}... is not the store manifest's "
                            f"{digest[:12]}...")
    for name in present:
        if loki_manifest is not None and name not in loki_manifest:
            problems.append(f"collision file {name} is not one the store's manifest names")
    collisions = []
    for _, name, data, digest, record in files:
        lines, file_problems = loki_lines(data)
        problems.extend(f'{name}: {p}' for p in file_problems)
        if file_problems:
            continue
        records, file_problems = loki_records(lines)
        problems.extend(f'{name}: {p}' for p in file_problems)
        spans = [(ln - 1, ln - 1 + raw.count('\n'), parse_block(o, ln, raw))
                 for o, ln, raw in blocks(data.decode('ascii'))]
        loaded = collections.Counter()
        for r in records:
            where = f"{name}:{r['param'] + 1}"
            span = next((s for s in spans if s[0] <= r['param'] < s[1]), None)
            if span is None:
                desc = DESCRIPTOR.search(lines[r['param'] + 1]) if r['param'] + 1 < len(lines) else None
                problems.append(f"{where}: LoKI-B loads a collision outside every collision block"
                                f"{': ' + desc.group(0) if desc else ''}")
                continue
            start, _, b = span
            loaded[start] += 1
            if [start + k for k in b['params']] != [r['param']]:
                problems.append(f'{where}: block {b["ordinal"]} does not hold exactly this one parameter line')
            if [start + k for k in b['dashes']] != [r['open'], r['close']]:
                problems.append(f"{where}: LoKI-B reads the table between lines "
                                f"{r['open'] + 1 if r['open'] is not None else '?'} and "
                                f"{r['close'] + 1 if r['close'] is not None else 'the end of the file'}, "
                                f"not block {b['ordinal']}'s five-dash table")
                continue
            problems.extend(f'{name}: {p}' for p in b['problems'])
            if b['label_problem']:
                problems.append(f"{where}: {b['label_problem']}")
                continue
            if any(c['label'] == b['label'] for c in collisions):
                problems.append(f"{b['label']}: appears twice in the assembled files")
                continue
            collisions.append({'label': b['label'], 'file': name, 'digest': digest, 'asm': b})
            record['collisions'] += 1
        for start, _, b in spans:
            if loaded[start] != 1:
                problems.append(f"{name}:{start + 1}: LoKI-B loads block {b['ordinal']} {loaded[start]} times")

    # 3. each collision against its source block, and the conventions its transformation needs
    used = collections.defaultdict(list)  # (source file, block) -> collision ids
    for ident, c in enumerate(collisions, 1):
        c['id'], asm = ident, c['asm']
        c['target'], c['product'], c['type'] = asm['lhs'][0], asm['rhs'][-1], asm['type']
        c['reverse'] = asm['arrow'] == '<->'
        if c['digest'] in by_sha:
            src_file, block, c['need'] = by_sha[c['digest']], asm['ordinal'], set()
        else:
            prov = asm['provenance']
            if prov is None:
                problems.append(f"{c['label']}: no I-341 provenance comment naming its source block")
                continue
            fname, fsha, block, line, bsha = prov
            src_file, block = sources.get(fname), int(block)
            if src_file is None or src_file['sha256'] != fsha:
                problems.append(f"{c['label']}: its source {fname} (SHA-256 {fsha[:12]}...) is not a given source")
                continue
            src = src_file['blocks'].get(block)
            if src is None:
                problems.append(f"{c['label']}: source {fname} has no block {block}")
                continue
            if (src['sha256'], src['line']) != (bsha, int(line)):
                problems.append(f"{c['label']}: provenance comment's block SHA-256 or line differs from "
                                f"{fname} block {block}")
            c['need'], bad = needed_conventions(src, asm)
            for x in bad:
                problems.append(f"{c['label']}: {x}, which no convention licenses")
            if (asm['conventions'] or set()) != c['need']:
                problems.append(f"{c['label']}: assembled comment declares conventions "
                                f"{sorted(asm['conventions'] or [])}, the transformation needs {sorted(c['need'])}")
        src = src_file['blocks'].get(block)
        if src is None:
            problems.append(f"{c['label']}: source {src_file['file']} has no block {block}")
            continue
        c['src'], c['src_file'] = src, src_file
        used[(src_file['file'], block)].append(ident)
        if asm['table'] != src['table']:
            problems.append(f"{c['label']}: table differs from {src_file['file']} block {block}")
        if asm['threshold'] != src['threshold'] or asm['line3'] is None or asm['line3'] != src['line3']:
            problems.append(f"{c['label']}: threshold differs from {src_file['file']} block {block}")
    linked = [c for c in collisions if 'src' in c]

    # 4. the state catalogue, from the development file's ground-state excitations
    energy = {GROUND: 0.0}
    ionization_energy = None
    for c in linked:
        if c['digest'] in by_sha and c['target'] == GROUND:
            if c['type'] == 'Excitation' and c['product'] in LEVELS_1S:
                energy[c['product']] = c['asm']['threshold']
            elif c['type'] == 'Ionization':
                ionization_energy = c['asm']['threshold']
    missing = [s for s in LEVELS_1S if s not in energy]
    if missing:
        problems.append(f'no ground-state excitation into {", ".join(missing)} in a byte-copied development file, '
                        f'so the 4s levels cannot be ordered')
    order = sorted((s for s in LEVELS_1S if s in energy), key=lambda s: energy[s])
    paschen = {GROUND: 'ground', **{s: f'1s{5 - k}' for k, s in enumerate(order)}}
    racah = {v: k[3:-1] for k, v in STATE_RENAMES.items() if v in LEVELS_1S}
    for s in LEVELS_1S:
        if not racah.get(s, '').endswith(str(ls_term(s)[1])):
            problems.append(f'state {s}: Racah name {racah.get(s)} does not carry the J of its LS term')
    for c in linked:
        if c['type'] == 'Excitation' and c['target'] in LEVELS_1S and c['product'] in LEVELS_1S \
                and c['target'] in energy and c['product'] in energy:
            gap = energy[c['product']] - energy[c['target']]
            if not abs(c['asm']['threshold'] - gap) <= LEVEL_GAP_TOLERANCE_EV:
                problems.append(f"{c['label']}: threshold {number(c['asm']['threshold'])} eV is not the "
                                f"{gap:.3f} eV between the two levels' ground-state excitation thresholds, so "
                                f"the state names do not match the source's levels")
    weights = {s: 2 * ls_term(s)[1] + 1 for s in (GROUND, *LEVELS_1S)}
    for c in linked:
        if 'DETAILED_BALANCE_INVERSE' in c['need'] and c['asm']['line3_rest']:
            ratio = c['asm']['line3_rest'][0]
            if not (re.fullmatch(NUMBER, ratio) and c['target'] in weights and c['product'] in weights
                    and abs(float(ratio) - weights[c['product']] / weights[c['target']]) <= 1e-6):
                problems.append(f"{c['label']}: the weight ratio {ratio} on its third line is not "
                                f"g({c['product']})/g({c['target']})")

    # 5. the overlay, against the source-verified collisions and the RMG library
    overlay, references, overlay_problems = load_overlay_document(overlay_path)
    problems.extend(overlay_problems)
    overlay = overlay or {}
    labels = {c['label'] for c in collisions}
    for label in overlay:
        if label not in labels:
            problems.append(f'overlay names a collision LoKI-B does not read from the assembled files: {label}')
    reactions, species, library_problems = load_library(database, LIBRARY)  # the files read once, RMG loads them
    problems.extend(library_problems)
    if reactions is None or species is None:  # nothing RMG loaded to compare: the refusal stands as it is, before
        if not library_problems:              # any record or state field is read
            problems.append(f'library {LIBRARY} not found under {database}')
        return None, problems, '', [c['label'] for c in collisions]
    records, reference_problems = reference_records(references or {})
    problems.extend(reference_problems)
    for label in sorted(records):  # a mapped species the library holds must be the one its reference means
        why = identity_problem(species[label], records[label]) if label in species else None
        if why:
            problems.append(f"library {LIBRARY} dictionary.txt: species {label}: the record RMG loads is not the "
                            f"overlay's reference ({why})")
    if ELECTRON_SPECIES in records and not records[ELECTRON_SPECIES].is_electron():
        problems.append(f"overlay species {ELECTRON_SPECIES}: its reference record is not RMG's electron")
    claims = collections.defaultdict(lambda: collections.defaultdict(list))  # state -> species -> ids
    for c in linked:
        c['family'] = family(c)
        if c['family'] == 'excitation above 4s':
            c['cascade'] = ('ground' if c['target'] == GROUND else '4s',
                            '4p' if shell(c['product']) == '4p' else 'levels above 4p')
        entry = overlay.get(c['label'])
        if entry is None:
            if not overlay_problems:
                problems.append(f"UNMAPPED collision, not in the overlay: {c['label']}")
            continue
        c['class'], c['reaction'] = entry['class'], entry['reaction']
        policy = POLICY[c['family']]
        if c['class'] not in policy['classes']:
            problems.append(f"{c['label']}: class {c['class']!r}, but {c['family']} allows only "
                            f"{'/'.join(policy['classes'])}: {policy['rule']}")
        if c['class'] != 'A':
            if c['reaction'] is not None:
                problems.append(f"{c['label']}: class {c['class']} carries reaction {c['reaction']!r}; "
                                f"only class A maps to a reaction")
            continue
        if c['reaction'] is None:
            problems.append(f"{c['label']}: class A without a reaction")
            continue
        parsed = parse_reaction(c['reaction'])
        shape = expected_shape(c)
        if parsed is None or shape is None or not shape_matches(parsed, shape):
            problems.append(f"{c['label']}: {c['family']} must map to '{policy['reaction']}', overlay says "
                            f"{c['reaction']!r}")
            c['reaction'] = None
            continue
        lhs, _, rhs = parsed
        claims[c['target']][lhs[0]].append(c['id'])
        if c['family'] != 'excitation above 4s':
            claims[c['product']][rhs[0]].append(c['id'])
    mentioned = {x for c in linked if c.get('class') == 'A' and c.get('reaction') is not None
                 for x in sum(parse_reaction(c['reaction'])[::2], [])} - {PHOTON, CASCADE_PRODUCT}
    if not overlay_problems:
        for x in sorted(mentioned - set(references or {})):
            problems.append(f"overlay: species {x} is named by a reaction but has no reference record under "
                            f"'species', so what it stands for is not stated")
        for x in sorted(set(references or {}) - mentioned):
            problems.append(f"overlay: species {x} has a reference record but no reaction names it")
    species_of = {}
    for state, named in claims.items():
        if len(named) > 1:
            problems.append(f'state {state} maps to more than one RMG species: '
                            + '; '.join(f'{s} (ids {ids})' for s, ids in sorted(named.items())))
            continue
        (name, ids), = named.items()
        why = species_problem(state, name, records, species, paschen)
        if why:
            problems.append(f'state {state} maps to {name} (ids {ids}): {why}')
        species_of[state] = name
    holds = collections.defaultdict(list)  # species -> the states it holds, lowest level first
    for state in sorted(species_of, key=lambda s: (energy.get(s, math.inf), s)):
        holds[species_of[state]].append(state)
    stands_for = {name: held[0] for name, held in holds.items()}  # a lumped species stands for its lowest level
    if ELECTRON_SPECIES in mentioned:
        stands_for[ELECTRON_SPECIES] = None
    for name, state in sorted(stands_for.items()):  # each record's own fields must not contradict that state
        for whose, record in (('its reference record', records.get(name)),
                              (f'the record {LIBRARY} loads', species[name].molecule[0] if name in species else None)):
            for why in state_problems(record, state) if record is not None else []:
                problems.append(f"species {name}: {whose} has {why}")
    for c in linked:
        if c.get('class') == 'A' and c.get('reaction') is not None:
            c['rmg'] = rmg_mapping(c, reactions, species, species_of, holds, problems)
    families = collections.defaultdict(lambda: collections.defaultdict(list))
    for c in linked:
        if 'cascade' in c and 'class' in c:
            families[c['cascade']][c['class']].append(c['id'])
    for key, classes in families.items():
        if len(classes) > 1:
            problems.append(f'excitation above 4s from {key[0]} via {key[1]} mixes classes '
                            + '; '.join(f'{k} (ids {v})' for k, v in sorted(classes.items()))
                            + ': one class for the whole family')

    # 6. every source block either used or not assembled, with a reason derived from the set
    family_use = collections.defaultdict(collections.Counter)  # product shell of a 4s-target excitation -> files
    for c in linked:
        if c['target'] in LEVELS_1S and c['type'] == 'Excitation':
            family_use[shell(c['product'])][c['src_file']['file']] += 1
    development = next((c['src_file'] for c in linked if c['digest'] in by_sha), None)
    not_assembled = []
    for fname, src in sources.items():
        for o, b in src['blocks'].items():
            if (fname, o) not in used:
                not_assembled.append({'source': fname, 'block': o, 'line': b['line'], 'block_sha256': b['sha256'],
                                      'process': b['process'],
                                      'reason': unused_reason(b, src, family_use, development)})
    if any(b['type'] == 'Elastic' and b['lhs'] and b['lhs'][0] not in SOURCE_GROUND
           for s in sources.values() for b in s['blocks'].values()):
        problems.append('a source carries an elastic cross section for an excited target, so the '
                        'ELASTIC_REUSE_GROUND statement would be false')

    problems.extend(reconcile_manifest(manifest, derived_manifest(manifest, linked, sources, used, not_assembled,
                                                                  files, weights, paschen)))

    # 7. the document
    doc = collections.OrderedDict()
    doc['schema'] = SCHEMA
    doc['set'] = SET
    doc['ticket'] = TICKET
    doc['rules'] = RULES
    doc['data_policy'] = DATA_POLICY
    doc['loki_files'] = {name: digest for _, name, _, digest, _ in files}
    doc['assembled_directory'] = inventory
    doc['sources'] = collections.OrderedDict()
    for fname, src in sources.items():
        n_used = len({o for (f, o) in used if f == fname})
        copies = [n for _, n, _, d, _ in files if d == src['sha256']]
        role = (f"byte copy in the assembled directory as {', '.join(copies)}" if copies
                else f'{n_used} blocks copied into the assembled files' if n_used
                else 'comparison only, no block assembled')
        doc['sources'][fname] = {'database': src['database'], 'permlink': src['permlink'], 'file': fname,
                                 'sha256': src['sha256'], 'n_blocks': len(src['blocks']), 'blocks_used': n_used,
                                 'role': role}
    doc['statistical_weights'] = weights
    doc['loki_state_names'] = {s: paschen.get(s, '?') + (f' {racah[s]}' if s in racah else '')
                               for s in (GROUND, *LEVELS_1S)}
    states = collections.OrderedDict()
    for s in [GROUND, *LEVELS_1S] + sorted(set(species_of) - {GROUND, *LEVELS_1S}):
        record = collections.OrderedDict()
        if s in weights:
            record.update({'paschen': paschen.get(s), 'racah': racah.get(s), 'g': weights[s],
                           'excitation_eV': energy.get(s)})
        if s in species_of:
            record['rmg_species'] = species_of[s]
            record['in_library'] = species_of[s] in species
            if holds[species_of[s]][0] != s:
                record['lumped_into'] = holds[species_of[s]][0]
        states[s] = record
    doc['states'] = states
    doc['policy'] = POLICY
    doc['declared_conventions'] = convention_registry(linked, energy, ionization_energy, weights, paschen)
    counts = collections.Counter(c['class'] for c in linked if 'class' in c)
    doc['class_counts'] = {k: counts.get(k, 0) for k in 'ABCD'}
    gaps = collections.OrderedDict()
    for c in linked:
        r = c.get('rmg')
        if r and r['status'] != 'present':
            key = f"[{r['status']}] {r['reaction']}"
            if 'cascade' in c:
                key += f" (radiative cascade via {c['cascade'][1]})"
            gaps.setdefault(key, []).append(c['id'])
    doc['class_a_gaps'] = gaps
    doc['channels'] = [channel(c) for c in linked]
    doc['not_assembled'] = not_assembled
    summary = (f"channels {len(linked)}; classes {dict(sorted(counts.items()))}; collision files "
               f"{len(files)} of {len(inventory)} in the assembled directory; not assembled {len(not_assembled)}; "
               f"source blocks {sum(len(s['blocks']) for s in sources.values())}; conventions "
               f"{dict((x['name'], len(x['applies_to'])) for x in doc['declared_conventions'])}")
    return render(doc), problems, summary, [c['label'] for c in collisions]


def family(c):
    if c['type'] == 'Elastic':
        return 'elastic'
    if c['type'] == 'Ionization':
        return 'ionization'
    return 'excitation into 4s' if c['product'] in LEVELS_1S else 'excitation above 4s'


def expected_shape(c):
    """(reactants, arrow, products) a class-A reaction must have, with None for a species the overlay names."""
    if c['family'] == 'ionization':
        return [None, ELECTRON_SPECIES], '=>', [None, ELECTRON_SPECIES, ELECTRON_SPECIES]
    if c['family'] == 'excitation into 4s':
        return [None, ELECTRON_SPECIES], '<=>' if c['reverse'] else '=>', [None, ELECTRON_SPECIES]
    if c['family'] == 'excitation above 4s':
        return [None, ELECTRON_SPECIES], '=>', [CASCADE_PRODUCT, ELECTRON_SPECIES, PHOTON]
    return None


def shape_matches(parsed, shape):
    lhs, arrow, rhs = parsed
    want_lhs, want_arrow, want_rhs = shape
    special = {ELECTRON_SPECIES, CASCADE_PRODUCT, PHOTON}
    return arrow == want_arrow and len(lhs) == len(want_lhs) and len(rhs) == len(want_rhs) and all(
        (w is None and s not in special) or s == w for s, w in zip(lhs + rhs, want_lhs + want_rhs))


def species_problem(state, name, records, species, paschen):
    """Why an RMG species cannot stand for a LoKI-B state, or None. The overlay's reference record for it must
    be one argon atom with the state's charge and, for an LS term, its spin multiplicity, as RMG reads that
    record (the library's own record must then be that reference: identity_problem); a species the library
    lacks must carry the canonical name of a missing 4s level, Ar(<Paschen name>)."""
    reference, term = records.get(name), ls_term(state)
    if reference is not None:
        if reference.get_formula() != 'Ar':
            return f"its reference record is {reference.get_formula()}, not one argon atom"
        if reference.get_net_charge() != state_charge(state):
            return f"its reference record has charge {reference.get_net_charge()}, the state {state_charge(state)}"
        if term and reference.multiplicity != term[0]:
            return f"its reference record has multiplicity {reference.multiplicity}, the LS term {term[0]}"
    if name in species:
        return None
    if state in LEVELS_1S and state in paschen:
        if name == f'Ar({paschen[state]})':
            return None
        return f"not in {LIBRARY} dictionary.txt, and a missing 4s level is named Ar({paschen[state]})"
    return f'not in {LIBRARY} dictionary.txt'


def rmg_mapping(c, reactions, species, species_of, holds, problems):
    """The RMG side of a class-A collision, derived from the library: index, status and missing species. The
    reaction is found by what RMG loaded, its reactants', its products' dictionary species and its direction,
    never by its label's text; an entry holding the same species another way (the other way round when either
    side is reversible, or with the other direction) cannot be matched reliably and is refused, even beside an
    entry that holds it exactly, and so is a reaction several entries hold, since the map names one index."""
    lhs, arrow, rhs = parse_reaction(c['reaction'])
    out = collections.OrderedDict([('reaction', c['reaction']), ('library', LIBRARY), ('index', None)])
    want = (tuple(sorted(lhs)), tuple(sorted(rhs)), arrow == '<=>')
    same = [i for i, r in sorted(reactions.items()) if (r.reactants, r.products, r.reversible) == want]
    near = [(i, r) for i, r in sorted(reactions.items()) if i not in same and (
        (r.reactants, r.products) == want[:2]
        or (r.reactants, r.products) == (want[1], want[0]) and (r.reversible or want[2]))]
    states = [c['target']] + ([] if 'cascade' in c else [c['product']])
    lumped = [s for s in states if s in species_of and holds[species_of[s]][0] != s]
    internal = 'cascade' not in c and lhs[0] == rhs[0]  # the map names no index for it, nothing to mistake
    for i, r in [] if internal else near:  # refused whether or not another entry matches exactly
        how = 'the other way round' if (r.reactants, r.products) != want[:2] else \
            ('as a reversible reaction' if r.reversible else 'as an irreversible one')
        problems.append(f"{c['label']}: {LIBRARY} entry {i} ({r.label!r}) holds the species of "
                        f"{c['reaction']!r} {how}, so the reaction cannot be matched to it reliably"
                        + (f' (entry {same[0]} holds it as written)' if same else ''))
    if internal:
        out['status'] = 'lumped_internal'
    elif len(same) > 1:
        problems.append(f"{c['label']}: {LIBRARY} holds {c['reaction']!r} as entries {same}, and the map names one "
                        f"index, so it cannot say which")
        out['status'] = 'absent'
    elif same and not near:
        out['index'] = same[0]
        out['status'] = 'present_lumped' if lumped else 'present'
    else:
        out['status'] = 'absent'
        named = set(lhs + rhs) - {ELECTRON_SPECIES, PHOTON, CASCADE_PRODUCT}
        if CASCADE_PRODUCT in rhs:
            named |= {species_of[s] for s in LEVELS_1S if s in species_of}
        needed = sorted(s for s in named if s not in species)
        if needed:
            out['species_needed'] = needed
    if 'cascade' in c:
        out['via'] = c['cascade'][1]
    if lumped:
        out['lumped'] = '; '.join(f'{s} is lumped into {species_of[s]}, which stands for {holds[species_of[s]][0]}'
                                  for s in lumped)
    return out


def channel(c):
    asm, src = c['asm'], c['src']
    entry = collections.OrderedDict()
    entry['id'] = c['id']
    entry['loki_process'] = c['label']
    entry['lxcat_file'] = c['file']
    entry['source'] = collections.OrderedDict([
        ('database', c['src_file']['database']), ('file', c['src_file']['file']),
        ('sha256', c['src_file']['sha256']), ('block', src['ordinal']), ('line', src['line']),
        ('block_sha256', src['sha256'])])
    entry['source_process'] = src['process']
    entry['threshold_eV'] = float(asm['threshold'])
    entry['superelastic_in_set'] = c['reverse']
    entry['family'] = c['family'] + (f" from {c['cascade'][0]} via {c['cascade'][1]}" if 'cascade' in c else '')
    if 'class' in c:
        entry['class'] = c['class']
    if c['need']:
        entry['conventions'] = sorted(c['need'], key=CONVENTIONS.index)
    if 'rmg' in c:
        entry['rmg'] = c['rmg']
    if c['target'] == GROUND and c['product'] in LEVELS_1S and c['type'] == 'Excitation' and not c['reverse']:
        entry['superelastic_required'] = ("C3 section 3 requires the inverse; the development descriptor is '->' "
                                          "and the ground set is kept unchanged, so the superelastic is NOT in the "
                                          "set (reported, not changed)")
    return entry


def convention_registry(linked, energy, ionization_energy, weights, paschen):
    """Each convention used, with a statement written from the collisions it covers."""
    out = []
    for name in CONVENTIONS:
        covered = [c for c in linked if name in c['need']]
        if not covered:
            continue
        first = covered[0]
        where = f"{first['src_file']['database']} {first['src_file']['file']} block {first['src']['ordinal']}"
        if name == 'ELASTIC_REUSE_GROUND':
            text = (f"No source in the set carries an elastic momentum-transfer cross section for an Ar(4s) level, "
                    f"and LoKI-B refuses a populated state without one. Each of "
                    f"{', '.join(c['target'] for c in covered)} therefore reuses {where} "
                    f"({first['src']['process']}), the ground-state table, unchanged: owner ruling 2026-10-08 "
                    f"'(a) Literature, (b) meanwhile', option (b). A declared modelling convention, not data for "
                    f"the excited state.")
        elif name == 'DETAILED_BALANCE_INVERSE':
            text = (f"The source tabulates only the upward transition ('->'); the descriptor is written '<->', so "
                    f"LoKI-B builds the downward (superelastic) cross section by detailed balance from the same "
                    f"table, with g = 2J+1 ({', '.join(f'{paschen.get(s)} {weights[s]}' for s in LEVELS_1S)}).")
        elif name == 'LUMPED_TARGET_PER_LEVEL':
            text = (f"{where} tabulates one lumped target '{LUMPED}'. Its table and its threshold "
                    f"({number(first['src']['threshold'])} eV) are applied unchanged to each of "
                    f"{', '.join(c['target'] for c in covered)}.")
            if ionization_energy is not None and all(c['target'] in energy for c in covered):
                own = [ionization_energy - energy[c['target']] for c in covered]
                text += (f" Their own ionisation energies, from the development file's thresholds, are "
                         f"{'/'.join(f'{x:.2f}' for x in own)} eV; they are not substituted, so the energy charged "
                         f"per event is off by at most {max(abs(first['src']['threshold'] - x) for x in own):.2f} eV.")
        else:
            pairs = sorted({(s, a) for c in covered for s, a in zip(c['src']['lhs'] + c['src']['rhs'],
                                                                   c['asm']['lhs'] + c['asm']['rhs'])
                            if STATE_RENAMES.get(s) == a})
            text = (f"State names are rewritten to the development file's names "
                    f"({', '.join(f'{s} -> {a}' for s, a in pairs)}), so ground-state excitation products and "
                    f"excited targets are one LoKI-B state. Other names are kept as the source writes them.")
        out.append(collections.OrderedDict([('name', name), ('statement', text),
                                            ('applies_to', [c['id'] for c in covered])]))
    return out


def unused_reason(b, src, family_use, development):
    """Why a source block is not in the set, from what the set uses and from the block's own table."""
    target = b['lhs'][0] if b['lhs'] else None
    if target in SOURCE_GROUND or target is None:
        dev = f"{development['file']} ({development['database']})" if development else 'the development file'
        reason = f"ground-state process: the set's ground state is {dev}, unchanged; {src['file']} is a comparison"
    else:
        product = shell(b['rhs'][-1]) if b['rhs'] else None
        same = sum(1 for x in src['blocks'].values() if x['lhs'] and x['lhs'][0] not in SOURCE_GROUND
                   and x['rhs'] and shell(x['rhs'][-1]) == product)
        users = family_use.get(product)
        if users:
            chosen = ', '.join(f'{f} ({n})' for f, n in sorted(users.items()))
            reason = (f'4s -> {product}: the set takes this family from {chosen}; {src["file"]} has {same}, not '
                      f'taken (source choice: I-341 report section 2)')
            if product == '4s':
                reason += '; kept as the sensitivity alternative for the 4s mixing (owner ruling 2026-10-14)'
        else:
            reason = f'4s -> {product}: no source in the set is used for this family; {src["file"]} has {same}'
    points = table_points(b)
    energies = [e for e, _ in points]
    repeated = sorted({e for e in energies if energies.count(e) > 1})
    if repeated:
        reason += f"; its table repeats E = {', '.join(number(e) for e in repeated)} eV"
    if points and b['kind'] in ('EXCITATION', 'IONIZATION') and b['line3'] is not None \
            and points[0][0] - b['line3'] > 0.5:
        reason += (f'; its table starts {points[0][0] - b["line3"]:.1f} eV above its own threshold, so LoKI-B would '
                   f'read zero across the threshold region')
    twin = next((o for o, x in src['blocks'].items() if o < b['ordinal'] and x['table'] == b['table']), None)
    if twin is not None:
        reason += f'; same table as block {twin}'
    return reason


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--overlay', required=True, help='the hand-written overlay: class and RMG reaction per collision')
    parser.add_argument('--assembled', required=True, help='directory holding the assembled LoKI-B files')
    parser.add_argument('--source', action='append', required=True,
                        help='a source LXCat file (repeatable): every file the set was built from or compared with')
    parser.add_argument('--database', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input'),
                        help="the database 'input' directory holding the RMG library (default: the one beside this "
                             "script)")
    parser.add_argument('--output', required=True, help='where to write the map')
    args = parser.parse_args()
    try:
        text, problems, summary, _ = generate(args.overlay, args.assembled, args.source, args.database)
    except Exception as exc:  # a malformed input is a refusal with a reason, never a pass
        traceback.print_exc()
        text, problems, summary = None, [f'internal error {type(exc).__name__}: {exc}'], ''
    folder = os.path.dirname(os.path.abspath(args.output))
    if os.path.isdir(args.output) or not os.path.isdir(folder):
        problems.append(f'--output {args.output}: '
                        + ('is a directory, not a file' if os.path.isdir(args.output) else f'no directory {folder}'))
    if not problems:
        try:
            with open(args.output, 'w', newline='\n') as fh:
                fh.write(text)
        except OSError as exc:
            problems.append(f'--output {args.output}: cannot be written ({type(exc).__name__}: {exc.strerror})')
    print(printable(summary))
    for p in problems:
        print('FAIL', printable(p))
    if problems:
        print(f'RESULT: FAIL ({len(problems)} problems; nothing written)')
        return 1
    print(f'RESULT: written {args.output}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
