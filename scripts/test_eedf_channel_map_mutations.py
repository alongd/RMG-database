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
Mutation tests for scripts/check_eedf_channel_map.py. Each case copies the assembled LoKI-B directory, the
map and the overlay into a scratch directory outside the repository, applies one mistake, runs the checker,
and expects it to refuse for the reason the case names: exit status 1, RESULT: FAIL and a FAIL line holding
that reason (argparse's usage error, exit 2, for a missing argument). Six cases must pass: the unmodified
inputs, the overlay rewritten in another layout, the library with one entry's label single-quoted or given
before its index, its dictionary's atoms labelled, and a source given from another folder under another
source's file name, which must also regenerate the committed map. A crash, or a traceback on stderr, counts
as neither a pass nor a refusal. The LXCat data never enter the repository: the store is passed as arguments,
as to the checker.

The cases are the honest mistakes the review rounds found (db-r38, db-r39, db-r41, db-r43, db-r46 to
db-r53): a hand edit to any field of the generated map, a file left out of the store or the command line, at
check or at generation, a stale hash, a table or name changed in the store, a mistyped class or reaction in
the overlay, a library entry disabled or written another way, and malformed input of every kind, which must
be refused with its reason and never with a traceback. Where a review mistake was made in the map, the case
makes it there; where the honest version of it is made in the overlay, the case makes it in the overlay and
mirrors it in the map, as the review did, so an older checker that reads only the map sees the same mistake.

With --old-checker, every case is also run against an older checker (the map-only one, 0a86a6156 and
before) through its own command line, and both verdicts are printed side by side. Cases that only change
the new command line are not run there.

Exit status 0 when every case behaves as expected for the checker under test, 1 otherwise. No
cross-section value is printed.

usage: test_eedf_channel_map_mutations.py MAP --overlay FILE --assembled DIR --source FILE [--source FILE ...]
                                          [--loki-rates FILE] [--database DIR] [--checker PATH]
                                          [--old-checker PATH] [--keep]
"""

import argparse
import copy
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_eedf_channel_map as gen  # noqa: E402

KEYWORDS = (b'ELASTIC', b'EFFECTIVE', b'EXCITATION', b'IONIZATION', b'ATTACHMENT')
DASHES = re.compile(rb'^-{5,}\s*$')
ASSEMBLED = 'Ar4s_assembled.txt'
DEVELOPMENT = 'Ar_LXCat.txt'


# --- edits of the assembled files -------------------------------------------------------------------------

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


def edit_blocks(ordinals, fn):
    def apply(asm):
        for o in ordinals:
            edit_block(asm, o, fn)
    return apply


def edit_file(fn):
    def apply(asm):
        path = os.path.join(asm, ASSEMBLED)
        data = open(path, 'rb').read()
        new = fn(data)
        assert new != data, 'mutation changed nothing'
        open(path, 'wb').write(new)
    return apply


def remove_files(*names):
    def apply(asm):
        for name in names:
            os.remove(os.path.join(asm, name))
    return apply


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


def replace_line3(block):
    lines = block.splitlines(keepends=True)
    lines[2] = b'garbage\n'
    return b''.join(lines)


def drop_line(marker):
    def fn(block):
        return b''.join(x for x in block.splitlines(keepends=True) if marker not in x)
    return fn


def swap_levels(data):
    """The assembler's slip: the two J = 1 levels' names swapped everywhere in the excited-state file."""
    return data.replace(b'Ar(3P1)', b'@').replace(b'Ar(1P1)', b'Ar(3P1)').replace(b'@', b'Ar(1P1)')


# --- edits of the map, the overlay, the library and the sources ------------------------------------------

def channel(doc, ident):
    return next(c for c in doc['channels'] if c['id'] == ident)


def convention(doc, name):
    return next(x for x in doc['declared_conventions'] if x['name'] == name)


def set_source(ident, field, value):
    return lambda doc: channel(doc, ident)['source'].__setitem__(field, value)


def swap_ist_sources(doc):
    a, b = channel(doc, 2), channel(doc, 3)
    a['source'], b['source'] = b['source'], a['source']


def reclassify(ident, cls):
    """The map side of a class change made consistently: the class, the counts, the RMG block and its gap."""
    def apply(doc):
        c = channel(doc, ident)
        doc['class_counts'][c['class']] -= 1
        doc['class_counts'][cls] += 1
        c['class'] = cls
        c.pop('rmg', None)
        for key in list(doc['class_a_gaps']):
            doc['class_a_gaps'][key] = [i for i in doc['class_a_gaps'][key] if i != ident]
            if not doc['class_a_gaps'][key]:
                del doc['class_a_gaps'][key]
    return apply


def overlay_set(ident, cls=None, reaction=None, drop_reaction=False):
    """Edit the overlay entry of the collision the map calls channel ident."""
    def apply(overlay, doc):
        entry = overlay['collisions'][channel(doc, ident)['loki_process']]
        if cls is not None:
            entry['class'] = cls
        if reaction is not None:
            entry['reaction'] = reaction
        if drop_reaction:
            entry.pop('reaction', None)
    return apply


def overlay_replace(old, new):
    """Rename one species in every overlay reaction, consistently."""
    def apply(overlay, doc):
        for entry in overlay['collisions'].values():
            if entry.get('reaction'):
                entry['reaction'] = ' '.join(new if s == old else s for s in entry['reaction'].split(' '))
    return apply


def raw(fn):
    """Mark an edit as one of the file's bytes rather than of its parsed document."""
    fn.raw = True
    return fn


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
    doc['not_assembled'].append({'source': c['source']['file'], 'block': c['source']['block'],
                                 'block_sha256': c['source']['block_sha256'], 'process': 'x', 'reason': 'x'})


def empty_collections(doc):
    """The review's empty_ar_v1 map: the same set, with every collection the old checker reads emptied."""
    for key in ('channels', 'not_assembled', 'declared_conventions'):
        doc[key] = []
    for key in ('class_a_gaps', 'loki_files'):
        doc[key] = {}
    doc['class_counts'] = {k: 0 for k in 'ABCD'}


def gap_wrong_reaction(doc):
    doc['class_a_gaps'] = {('[absent] Xe + e- => Kr + e-' if k == '[absent] Ar + e- => Ar(1s4) + e-' else k): v
                           for k, v in doc['class_a_gaps'].items()}


def absent_declared_present(doc):
    channel(doc, 3)['rmg']['status'] = 'present'
    del doc['class_a_gaps']['[absent] Ar + e- => Ar(1s4) + e-']


def ionization_to_excitation(doc):
    channel(doc, 39)['rmg'].update({'reaction': 'Ar + e- => Ars + e-', 'index': 87})


def rmg_status_only(doc):
    for key in ('reaction', 'library', 'index'):
        channel(doc, 2)['rmg'].pop(key)


@raw
def recursive_alias(text):
    return text + b'probe: &loop [*loop]\n'


@raw
def invalid_utf8(text):
    return b'\xff\xfe' + text


@raw
def nan_overlay_key(text):
    return text + b'  .nan: {class: B}\n'


@raw
def alias_in_overlay(text):
    return text.replace(b'{class: B}', b'&b {class: B}', 1) + b"  'e + Ar(9z) -> e + Ar(9z), Elastic': *b\n"


@raw
def duplicate_overlay_entry(text):
    line = next(x for x in text.split(b'\n') if x.startswith(b"  'e + "))
    return text.replace(line, line + b'\n' + line, 1)


def drop_overlay_entry(overlay, doc):
    del overlay['collisions'][channel(doc, 45)['loki_process']]


def extra_overlay_entry(overlay, doc):
    overlay['collisions']['e + Ar(3P2) -> e + Ar(9z), Excitation'] = {'class': 'B'}


def reorder_overlay(overlay, doc):
    overlay['collisions'] = dict(reversed(list(overlay['collisions'].items())))


def renumber_library_entry(database):
    path = os.path.join(database, 'kinetics', 'libraries', gen.LIBRARY, 'reactions.py')
    text = open(path, encoding='utf-8').read()
    assert 'index = 87,' in text
    open(path, 'w', encoding='utf-8').write(text.replace('index = 87,', 'index = 97,'))


def library_entry_87(database):
    """The library's reactions.py, and entry 87's text with the text before and after it."""
    path = os.path.join(database, 'kinetics', 'libraries', gen.LIBRARY, 'reactions.py')
    lines = open(path, encoding='utf-8').read().splitlines(keepends=True)
    start = next(i for i, x in enumerate(lines) if x.startswith('entry(') and lines[i + 1].strip() == 'index = 87,')
    end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith(')')) + 1
    return path, ''.join(lines[:start]), ''.join(lines[start:end]), ''.join(lines[end:])


def disable_library_entry(database):
    """Keep entry 87 as text inside a string, as one keeps an entry out of a library: RMG then loads 86, 88-93."""
    path, before, entry, after = library_entry_87(database)
    quotes = "'" * 3
    open(path, 'w', encoding='utf-8').write(before + quotes + '\n' + entry + quotes + '\n' + after)


def requote_library_label(database):
    """Write entry 87's label in single quotes: RMG loads the same entry."""
    path, before, entry, after = library_entry_87(database)
    changed = re.sub(r'label = "([^"]*)"', r"label = '\1'", entry)
    assert changed != entry
    open(path, 'w', encoding='utf-8').write(before + changed + after)


def label_before_index(database):
    """Give entry 87's label before its index: RMG loads the same entry."""
    path, before, entry, after = library_entry_87(database)
    changed = re.sub(r'( +index = 87,\n)( +label = .*\n)', r'\2\1', entry)
    assert changed != entry
    open(path, 'w', encoding='utf-8').write(before + changed + after)


def library_entry_in_if(database):
    """Put entry 87 under 'if True:': RMG loads it, but only by running the file."""
    path, before, entry, after = library_entry_87(database)
    indented = ''.join('    ' + x for x in entry.splitlines(keepends=True))
    open(path, 'w', encoding='utf-8').write(before + 'if True:\n' + indented + after)


def repeat_index_keyword(database):
    """Give entry 87's index twice by keyword, a copy-and-paste slip: Python refuses the call."""
    path, before, entry, after = library_entry_87(database)
    open(path, 'w', encoding='utf-8').write(before + entry.replace('    index = 87,\n', '    index = 87,\n' * 2, 1) + after)


def index_by_position_and_keyword(database):
    """Give entry 87's index by position and by keyword: load_entry gets two values for it."""
    path, before, entry, after = library_entry_87(database)
    assert entry.startswith('entry(\n')
    open(path, 'w', encoding='utf-8').write(before + 'entry(87,\n' + entry[len('entry(\n'):] + after)


def library_bytes(fn):
    """Edit the bytes of the library's reactions.py."""
    def apply(database):
        path = os.path.join(database, 'kinetics', 'libraries', gen.LIBRARY, 'reactions.py')
        data = open(path, 'rb').read()
        open(path, 'wb').write(fn(data))
    return apply


def entry_87_edit(old, new):
    """Replace text in entry 87 only."""
    def apply(database):
        path, before, entry, after = library_entry_87(database)
        assert old in entry
        open(path, 'w', encoding='utf-8').write(before + entry.replace(old, new, 1) + after)
    return apply


def latin1_cookie(data):
    assert b'# encoding: utf-8' in data
    return data.replace(b'# encoding: utf-8', b'# encoding: latin-1', 1) + b'\n# caf\xe9\n'


def library_text(name, fn):
    """Edit one of the library's files (reactions.py or dictionary.txt) as text."""
    def apply(database):
        path = os.path.join(database, 'kinetics', 'libraries', gen.LIBRARY, name)
        text = fn(open(path, encoding='utf-8').read())
        open(path, 'w', encoding='utf-8').write(text)
    return apply


STALE_ARS = 'Ars\nmultiplicity 1\n1 Ar u0 p4 c0\n'
# The dictionary's text with a missing 4s level added under a '//' comment, which RMG's reader drops (db-r52)
COMMENTED_RESONANCE = {m: f'\n\n// resonance species\nAr(1s2)\nmultiplicity {m}\n1 Ar u{u} p{p} c0\n'
                       for m, u, p in ((1, 0, 4), (3, 2, 3))}
# The library's files edited as text, each refused by RMG's own loader (db-r51): the case name, the file, the
# edit, RMG's refusal, and the generator's own reader's refusal of the same file
LIBRARY_TEXT_EDITS = [
    ('dictionary_species_twice', 'dictionary.txt', lambda t: STALE_ARS + '\n' + t,
     'DatabaseError: Species label "Ars" used for multiple species', 'species Ars is declared twice'),
    ('dictionary_species_twice_stale_last', 'dictionary.txt', lambda t: t + '\n\n' + STALE_ARS,
     'DatabaseError: Species label "Ars" used for multiple species', 'species Ars is declared twice'),
    ('dictionary_multiplicity_twice', 'dictionary.txt',
     lambda t: t.replace('multiplicity 3', 'multiplicity 1\nmultiplicity 3', 1),
     "ValueError: invalid literal for int() with base 10: 'multiplicity'",
     'species Ars states its multiplicity twice (1, 3)'),
    ('dictionary_multiplicity_twice_stale_last', 'dictionary.txt',
     lambda t: t.replace('multiplicity 3', 'multiplicity 3\nmultiplicity 1', 1),
     "ValueError: invalid literal for int() with base 10: 'multiplicity'",
     'species Ars states its multiplicity twice (3, 1)'),
    ('library_unhashable_metadata', 'reactions.py', lambda t: t + '\nreview_notes = {["copy"]: "draft"}\n',
     "TypeError: unhashable type: 'list'", 'a Assign statement'),
    ('library_unhashable_index', 'reactions.py', lambda t: t.replace('index = 87', 'index = {[]: 87}', 1),
     "TypeError: unhashable type: 'list'", 'without a literal integer index'),
]


# A missing 4s level added as a two-atom record, an atom copied once too often (db-r53)
DIMER_RESONANCE = '\n\nAr(1s2)\nmultiplicity 1\n1 Ar u0 p4 c0\n2 Ar u0 p4 c0\n'
# Entry 87's index as a value RMG keeps as the entry's key but that is no index (db-r53)
BAD_INDICES = [('none', 'None', 'index None is'), ('nonnumeric', '"eighty-seven"', "index 'eighty-seven' is"),
               ('empty', '""', "index '' is"), ('integer_string', '"87"', "index '87' is")]


def overlay_text(old, new):
    """Replace one piece of the overlay's text (db-r53: a YAML escape that writes a lone surrogate)."""
    def apply(text):
        assert old.encode() in text
        return text.replace(old.encode(), new.encode(), 1)
    return raw(apply)


def overlay_date(old, new):
    """Write one overlay value as an unquoted date (db-r52), which a plain YAML loader constructs as a date."""
    def apply(text):
        assert old.encode() in text
        return text.replace(old.encode(), new.encode(), 1)
    return raw(apply)


def dictionary_invalid_utf8(database):
    open(os.path.join(database, 'kinetics', 'libraries', gen.LIBRARY, 'dictionary.txt'), 'ab').write(b'\xff\n')


def dictionary_unreadable(database):
    os.chmod(os.path.join(database, 'kinetics', 'libraries', gen.LIBRARY, 'dictionary.txt'), 0)


def unreadable(asm):
    os.chmod(asm, 0)


def edit_manifest(fn):
    """Edit the store's manifest.json (the map's hash of it is refreshed with the store's)."""
    def apply(asm):
        path = os.path.join(asm, gen.MANIFEST)
        doc, repeated = gen.decode_manifest(open(path, 'rb').read())
        assert not repeated, repeated
        fn(doc)
        json.dump(doc, open(path, 'w'), indent=1)
    return apply


def manifest_text(old, new):
    """Edit the store's manifest.json as text, replacing the first occurrence of old with new."""
    def apply(asm):
        path = os.path.join(asm, gen.MANIFEST)
        text = open(path, encoding='utf-8').read()
        assert old in text, old
        open(path, 'w', encoding='utf-8').write(text.replace(old, new, 1))
    return apply


# The store manifest's text edited to declare one member twice, the stale value first or last (db-r50)
DUPLICATE_MEMBERS = [
    ('weight', '"Ar(3P2)": 5', '"Ar(3P2)": 3,\n  "Ar(3P2)": 5',
     "statistical_weights['Ar(3P2)'] is declared 2 times (3, 5)"),
    ('threshold', '"threshold_eV": 11.548', '"threshold_eV": 12.0,\n  "threshold_eV": 11.548',
     "processes[1]['threshold_eV'] is declared 2 times (12.0, 11.548)"),
    ('set', '"set": "ar-v1"', '"set": "ar-v2",\n "set": "ar-v1"', "set is declared 2 times ('ar-v2', 'ar-v1')"),
    ('weight_stale_last', '"Ar(3P2)": 5', '"Ar(3P2)": 5,\n  "Ar(3P2)": 3',
     "statistical_weights['Ar(3P2)'] is declared 2 times (5, 3)"),
]


DROP = object()


def manifest_set(*path_and_value):
    """Set one manifest field, found by its path of keys and indices, to a value, or drop it with DROP."""
    *path, value = path_and_value

    def edit(doc):
        for k in path[:-1]:
            doc = doc[k]
        if value is DROP:
            del doc[path[-1]]
        else:
            doc[path[-1]] = value
    return edit_manifest(edit)


def rename_file(old, new):
    def apply(asm):
        os.rename(os.path.join(asm, old), os.path.join(asm, new))
    return apply


def same_basename(work, sources):
    """Give NGFSRDW's file from another folder under TRINITI's file name, the real TRINITI file beside it."""
    other = os.path.join(work, 'elsewhere')
    os.makedirs(other)
    out = []
    for s in sources:
        if os.path.basename(s) == 'NGFSRDW_Ar_excited.txt':
            s = shutil.copyfile(s, os.path.join(other, 'TRINITI_Ar.txt'))
        out.append(s)
    return out


def touch_source(name, data=b'\n'):
    def apply(path):
        if os.path.basename(path) == name:
            open(path, 'ab').write(data)
    return apply


def extra_source(name, copy_as):
    """Also give an edited copy of a source under another name: a file the store's manifest does not name."""
    def apply(path):
        if os.path.basename(path) == name:
            extra = os.path.join(os.path.dirname(path), copy_as)
            shutil.copyfile(path, extra)
            open(extra, 'ab').write(b'\n')
    return apply


# --- the cases -----------------------------------------------------------------------------------------------

def case(name, origin, expect, map=None, overlay=None, store=None, refresh=False, drop_source=None,
         database=None, source_edit=None, no_sources=False, rates=True, generate=False, source_list=None):
    """One mistake: edits of the map (of its parsed document, or of its bytes when marked raw), the overlay
    (likewise; a document edit also sees the map), the store (followed, with refresh, by putting the new
    file hashes into the map), the command line, the library or a source file; and what the checker must
    do: 'PASS', or refuse with a FAIL line holding the given text. With generate, the map is first written
    by the generator beside the checker from the same inputs and command line, as an honest regeneration
    would write it, and a refusal there is the verdict; a case that must pass must then also regenerate the
    committed map byte for byte. source_list rewrites the list of source paths given."""
    return dict(name=name, origin=origin, expect=expect, map=map, overlay=overlay, store=store, refresh=refresh,
                drop_source=drop_source, database=database, source_edit=source_edit, no_sources=no_sources,
                rates=rates, generate=generate, source_list=source_list)


REGEN = 'differs from its regeneration'
NOT_READ = 'overlay names a collision LoKI-B does not read'
LICENSE = 'which no convention licenses'
FORM = "is not '[X + e"
NOT_GIVEN = "named by the store's manifest was not given"
NOT_NAMED = "not a source named by the store's manifest"
UNREADABLE = 'cannot be read without running the file'
RMG_REFUSES = "RMG's own loader refuses it ("
NOT_IN_STORE = "named by the store's manifest is not in the assembled directory"

CASES = [
    case('baseline', 'control', 'PASS'),
    case('overlay_reordered', 'control', 'PASS', overlay=reorder_overlay),
    # db-r38: every entry against its source block, conventions mandatory
    case('drop_assembled_block', 'db-r38', NOT_READ, store=lambda a: edit_block(a, 5, lambda b: b'')),
    case('rename_assembled_target', 'db-r38', LICENSE,
         store=lambda a: edit_block(a, 1, lambda b: b.replace(b'Ar(3P2)', b'Ar(RENAMED)'))),
    case('change_channel_sha', 'db-r38', REGEN, map=set_source(45, 'sha256', '0' * 64)),
    case('duplicate_entry', 'db-r38', REGEN, map=lambda d: d['channels'].append(copy.deepcopy(channel(d, 45)))),
    case('swap_IST_source_blocks', 'db-r38', REGEN, map=swap_ist_sources),
    case('remove_elastic_convention', 'db-r38', REGEN, map=remove_elastic_convention),
    case('wrong_source_line', 'db-r38', REGEN, map=set_source(45, 'line', 999999)),
    case('change_table_refresh_assembled_hash', 'db-r38', 'table differs from',
         store=lambda a: edit_block(a, 5, double_first_ordinate), refresh=True),
    case('drop_block_refresh_assembled_hash', 'db-r38', NOT_READ,
         store=lambda a: edit_block(a, 5, lambda b: b''), refresh=True),
    case('rename_target_refresh_assembled_hash', 'db-r38', LICENSE,
         store=lambda a: edit_block(a, 1, lambda b: b.replace(b'Ar(3P2)', b'Ar(RENAMED)')), refresh=True),
    case('wrong_ground_block_sha', 'db-r38', REGEN, map=set_source(1, 'block_sha256', '0' * 64)),
    case('rename_elastic_convention', 'db-r38', REGEN, map=rename_elastic_convention),
    case('elastic_applies_to_shrunk', 'db-r38', REGEN,
         map=lambda d: convention(d, 'ELASTIC_REUSE_GROUND')['applies_to'].remove(40)),
    case('elastic_statement_emptied', 'db-r38', REGEN,
         map=lambda d: convention(d, 'ELASTIC_REUSE_GROUND').__setitem__('statement', '')),
    case('channel_drops_detailed_balance', 'db-r38', REGEN,
         map=lambda d: channel(d, 44)['conventions'].remove('DETAILED_BALANCE_INVERSE')),
    case('assembled_convention_comment_dropped', 'db-r38', 'assembled comment declares conventions',
         store=lambda a: edit_block(a, 1, drop_line(b'I-341 conventions:')), refresh=True),
    case('undeclared_ion_rename', 'db-r38', REGEN, map=undeclare_ion_rename),
    case('remove_elastic_convention_everywhere', 'db-r38', 'assembled comment declares conventions',
         map=remove_elastic_convention, store=edit_blocks((1, 2, 3, 4), drop_line(b'I-341 conventions:')),
         refresh=True),
    case('undeclared_ion_rename_everywhere', 'db-r38', 'assembled comment declares conventions',
         map=undeclare_ion_rename,
         store=edit_blocks((115, 116, 117, 118), lambda b: b.replace(b'LUMPED_TARGET_PER_LEVEL,STATE_RENAME',
                                                                     b'LUMPED_TARGET_PER_LEVEL')), refresh=True),
    case('not_assembled_conflicting_sha', 'db-r38', REGEN, map=not_assembled_conflict),
    case('not_assembled_also_mapped', 'db-r38', REGEN, map=not_assembled_also_mapped),
    case('no_sources_given', 'db-r38', 'the following arguments are required', no_sources=True),
    # db-r39: LoKI-B's own grammar
    case('short_dash_shadow_table', 'db-r39', 'five-dash table', store=lambda a: edit_block(a, 5, shadow_table),
         refresh=True),
    case('keywordless_collision', 'db-r39', 'outside every collision block', store=append_keywordless_collision,
         refresh=True),
    case('param_in_header_prose', 'db-r39', 'no descriptor on the next line', store=param_in_header, refresh=True),
    case('bare_cr_hides_table_row', 'db-r39', 'bytes outside printable ASCII',
         store=lambda a: edit_block(a, 5, bare_cr_in_table), refresh=True),
    case('unterminated_last_table', 'db-r39', 'without a closing dash line', store=unterminate_last_table,
         refresh=True),
    case('ionization_electron_dropped', 'db-r39', FORM, refresh=True,
         store=lambda a: edit_block(a, 115, lambda b: b.replace(b'+ e + e, Ionization]', b'+ e, Ionization]'))),
    # db-r41: printed labels without a rate list, numbers, malformed blocks
    case('electron_first_lhs', 'db-r41', FORM, rates=False, refresh=True,
         map=lambda d: channel(d, 44).__setitem__('loki_process', 'e + e + Ar(3P0) <-> e + Ar(1P1), Excitation'),
         store=lambda a: edit_block(a, 5, lambda b: b.replace(b'[Ar(3P0) + e <->', b'[e + Ar(3P0) <->'))),
    case('electron_first_rhs', 'db-r41', FORM, rates=False, refresh=True,
         map=lambda d: channel(d, 44).__setitem__('loki_process', 'e + Ar(3P0) <-> e + e + Ar(1P1), Excitation'),
         store=lambda a: edit_block(a, 5, lambda b: b.replace(b'<-> Ar(1P1) + e,', b'<-> e + Ar(1P1),'))),
    case('coefficient_2e_rhs', 'db-r41', FORM, rates=False, refresh=True,
         map=lambda d: channel(d, 154).__setitem__('loki_process',
                                                   'e + Ar(3P2) -> e + e + Ar(+,gnd) + 2e, Ionization'),
         store=lambda a: edit_block(a, 115, lambda b: b.replace(b'+ e + e, Ionization]', b'+ 2e, Ionization]'))),
    case('map_threshold_nan', 'db-r41', REGEN, rates=False,
         map=lambda d: channel(d, 44).__setitem__('threshold_eV', float('nan'))),
    case('map_threshold_inf', 'db-r41', REGEN, map=lambda d: channel(d, 1).__setitem__('threshold_eV', float('inf'))),
    case('unknown_field_nan', 'db-r41 power_share_nan', REGEN,
         map=lambda d: channel(d, 2).__setitem__('power_share_max', {'value': float('nan'), 'where': 'x'})),
    case('wrong_statistical_weight', 'db-r41', REGEN,
         map=lambda d: d['statistical_weights'].__setitem__('Ar(3P2)', 500)),
    case('wrong_rmg_index', 'db-r41', REGEN, map=lambda d: channel(d, 2)['rmg'].__setitem__('index', 86)),
    case('class_a_gap_dropped', 'db-r41', REGEN,
         map=lambda d: d['class_a_gaps'].__setitem__(next(iter(d['class_a_gaps'])), [])),
    case('nonnumeric_line3', 'db-r41', "third line 'garbage' is not a number",
         store=lambda a: edit_block(a, 5, replace_line3), refresh=True),
    case('channel_without_source', 'db-r41', REGEN, map=lambda d: channel(d, 45).pop('source')),
    # db-r43 finding 1: the file inventory is the directory's, not the map's
    case('omit_excited_file_consistently', 'db-r43 F1', REGEN, map='omit_excited', rates=False),
    case('omit_excited_file_overlay_too', 'db-r43 F1', 'UNMAPPED collision', map='omit_excited',
         overlay='omit_excited'),
    case('excited_file_missing_from_store', 'db-r43 F1', NOT_READ, store=remove_files(ASSEMBLED)),
    case('empty_map_collections', 'db-r43 F1', REGEN, map=empty_collections, rates=False),
    case('empty_store', 'db-r43 F1', NOT_READ, store=remove_files(ASSEMBLED, DEVELOPMENT)),
    # db-r43 finding 2: the RMG reaction describes the collision
    case('ionization_mapped_to_excitation', 'db-r43 F2', 'ionization must map to', map=ionization_to_excitation,
         overlay=overlay_set(39, reaction='Ar + e- => Ars + e-')),
    case('rmg_status_only', 'db-r43 F2', REGEN, map=rmg_status_only),
    case('class_a_without_reaction', 'db-r43 F2', 'class A without a reaction',
         overlay=overlay_set(2, drop_reaction=True)),
    case('absent_reaction_unrelated_species', 'db-r43 F2', 'maps to more than one RMG species',
         map=lambda d: channel(d, 3)['rmg'].__setitem__('reaction', 'Xe + e- => Kr + e-'),
         overlay=overlay_set(3, reaction='Xe + e- => Kr + e-')),
    case('gap_wrong_reaction', 'db-r43 F2', REGEN, map=gap_wrong_reaction),
    # db-r43 finding 3: the classification policy, from the source-verified process
    case('resonance_production_as_B', 'db-r43 F3', 'excitation into 4s allows only A',
         map=reclassify(3, 'B'), overlay=overlay_set(3, cls='B', drop_reaction=True)),
    case('ionization_as_C', 'db-r43 F3', 'ionization allows only A',
         map=reclassify(39, 'C'), overlay=overlay_set(39, cls='C', drop_reaction=True)),
    case('elastic_as_A', 'db-r43 F3', 'elastic allows only B', map=lambda d: channel(d, 1).__setitem__('class', 'A'),
         overlay=overlay_set(1, cls='A', reaction='Ar + e- => Ar + e-')),
    case('cascade_family_mixed', 'db-r43 F3', 'one class for the whole family',
         map=reclassify(6, 'B'), overlay=overlay_set(6, cls='B', drop_reaction=True)),
    # db-r43 finding 4: reaction and species presence come from the library
    case('absent_declared_present', 'db-r43 F4', REGEN, map=absent_declared_present),
    case('species_needed_wrong', 'db-r43 F4', REGEN,
         map=lambda d: channel(d, 3)['rmg'].__setitem__('species_needed', ['Xe*'])),
    case('species_needed_deleted', 'db-r43 F4', REGEN, map=lambda d: channel(d, 3)['rmg'].pop('species_needed')),
    case('missing_species_misnamed', 'db-r43 F4', 'a missing 4s level is named Ar(1s4)',
         overlay=overlay_replace('Ar(1s4)', 'Ar1s4')),
    case('singlet_lumped_into_triplet', 'db-r43 F4', 'multiplicity 3, the LS term 1',
         overlay=overlay_replace('Ar(1s2)', 'Ars')),
    # db-r43 finding 5: convention statements are written from what they describe
    case('convention_false_statement', 'db-r43 F5', REGEN,
         map=lambda d: convention(d, 'ELASTIC_REUSE_GROUND').__setitem__(
             'statement', 'Measured excited-state momentum-transfer data; no ground-state reuse.')),
    # db-r43 finding 6: the state catalogue
    case('state_label_wrong', 'db-r43 F6', REGEN,
         map=lambda d: d['loki_state_names'].__setitem__('Ar(3P1)', "1s2 4s'[1/2]1")),
    case('state_labels_deleted', 'db-r43 F6', REGEN, map=lambda d: d.pop('loki_state_names')),
    case('weights_deleted_all', 'db-r43 F6', REGEN, map=lambda d: d.__setitem__('statistical_weights', {})),
    case('weight_state_missing', 'db-r43 F6', REGEN, map=lambda d: d['statistical_weights'].pop('Ar(3P1)')),
    case('assembled_levels_swapped', 'db-r43 F6', LICENSE, store=edit_file(swap_levels), refresh=True),
    # db-r43 finding 7: numeric keys
    case('nonfinite_key_nan', 'db-r43 F7', REGEN, map=lambda d: d['loki_state_names'].__setitem__(float('nan'), 'x')),
    case('nonfinite_key_inf', 'db-r43 F7', REGEN, map=lambda d: d['loki_state_names'].__setitem__(float('inf'), 'x')),
    case('nonfinite_source_key', 'db-r43 F7', REGEN,
         map=lambda d: channel(d, 2)['source'].__setitem__(float('nan'), 'x')),
    case('overlay_nan_key', 'db-r43 F7', 'is not a string', overlay=nan_overlay_key),
    # db-r43 finding 8: malformed input always gets a verdict
    case('threshold_huge_integer', 'db-r43 F8', REGEN,
         map=lambda d: channel(d, 2).__setitem__('threshold_eV', 10 ** 400)),
    case('class_list', 'db-r43 F8', REGEN, map=lambda d: channel(d, 2).__setitem__('class', ['A'])),
    case('class_dict', 'db-r43 F8', REGEN, map=lambda d: channel(d, 2).__setitem__('class', {'A': 1})),
    case('overlay_class_list', 'db-r43 F8', 'is not a string', overlay=overlay_set(2, cls=['A'])),
    case('gap_integer_key', 'db-r43 F8', REGEN, map=lambda d: d['class_a_gaps'].__setitem__(7, [3])),
    case('weight_integer_key', 'db-r43 F8', REGEN, map=lambda d: d['statistical_weights'].__setitem__(7, 1)),
    case('convention_list_name', 'db-r43 F8', REGEN,
         map=lambda d: convention(d, 'STATE_RENAME').__setitem__('name', ['STATE_RENAME'])),
    case('rmg_list_library', 'db-r43 F8', REGEN, map=lambda d: channel(d, 2)['rmg'].__setitem__('library', ['x'])),
    case('recursive_yaml_alias', 'db-r43 F8', REGEN, map=recursive_alias),
    case('overlay_recursive_alias', 'db-r43 F8', 'anchors and aliases', overlay=recursive_alias),
    case('overlay_alias', 'db-r43 F8', 'anchors and aliases', overlay=alias_in_overlay),
    case('map_invalid_utf8', 'db-r43 F8', 'not even UTF-8', map=invalid_utf8),
    case('overlay_invalid_utf8', 'db-r43 F8', 'cannot be read as UTF-8', overlay=invalid_utf8),
    case('overlay_duplicate_entry', 'db-r43 F8', 'appears twice', overlay=duplicate_overlay_entry),
    # db-r43 finding 9: attribution comes from the source header
    case('source_database_wrong', 'db-r43 F9', REGEN,
         map=lambda d: channel(d, 2)['source'].__setitem__('database', 'TRINITI database')),
    case('source_registry_database_wrong', 'db-r43 F9', REGEN,
         map=lambda d: d['sources'][channel(d, 2)['source']['file']].__setitem__('database', 'TRINITI database')),
    # generate and compare: every collision in the overlay once, every derived field kept in step
    case('overlay_entry_missing', 'overlay', 'UNMAPPED collision, not in the overlay', overlay=drop_overlay_entry),
    case('overlay_entry_extra', 'overlay', NOT_READ, overlay=extra_overlay_entry),
    case('comparison_source_left_out', 'generator', NOT_GIVEN, drop_source='NGFSRDW_Ar_excited.txt'),
    case('assembled_source_left_out', 'generator', NOT_GIVEN, drop_source='BSR_Ar_excited.txt'),
    case('stale_source_hash', 'generator', NOT_NAMED, source_edit=touch_source('NGFSRDW_Ar_excited.txt')),
    case('stale_library_index', 'generator', REGEN, database=renumber_library_entry),
    # db-r46 finding 1: the library is read as RMG loads it, not as text
    case('library_entry_disabled_in_string', 'db-r46 F1', REGEN, database=disable_library_entry),
    case('library_label_single_quoted', 'db-r46 F1', 'PASS', database=requote_library_label),
    case('library_label_before_index', 'db-r46 F1', 'PASS', database=label_before_index),
    case('library_entry_under_if', 'db-r46 F1', UNREADABLE, database=library_entry_in_if),
    # db-r46 finding 2: the source pool is the store manifest's, at generation as at check
    case('generate_without_comparison_source', 'db-r46 F2', NOT_GIVEN, drop_source='NGFSRDW_Ar_excited.txt',
         generate=True),
    case('extra_source_given', 'db-r46 F2', NOT_NAMED,
         source_edit=extra_source('TRINITI_Ar.txt', 'TRINITI_Ar_v2.txt')),
    # db-r46 finding 3: a bad file is a clean refusal, never a traceback
    case('source_invalid_utf8', 'db-r46 F3', NOT_NAMED,
         source_edit=touch_source('NGFSRDW_Ar_excited.txt', b'\xff\n')),
    # db-r47 finding 1: a source keeps the manifest's identity, whatever name it is given under
    case('same_basename_other_folder', 'db-r47 F1', 'PASS', generate=True, source_list=same_basename),
    case('manifest_two_sources_one_name', 'db-r47 F1', 'sources share the file name TRINITI_Ar.txt', refresh=True,
         store=edit_manifest(lambda d: d['sources']['NGFSRDW'].__setitem__('path', '/x/TRINITI_Ar.txt'))),
    # db-r47 finding 2: the collision files are the manifest's, and the manifest agrees with itself
    case('generate_without_excited_file', 'db-r47 F2', NOT_IN_STORE, store=remove_files(ASSEMBLED),
         overlay='omit_excited', generate=True, rates=False),
    case('collision_file_renamed', 'db-r47 F2', "is not one the store's manifest names", generate=True,
         store=rename_file(ASSEMBLED, 'Ar4s_assembled_v2.txt'), rates=False),
    case('manifest_collision_hash_stale', 'db-r47 F2', "is not the store manifest's", refresh=True,
         store=edit_manifest(lambda d: d['loki_files'].__setitem__(ASSEMBLED, '0' * 64))),
    case('manifest_source_dropped', 'db-r47 F2', "which the manifest's 'sources' do not", generate=True,
         drop_source='NGFSRDW_Ar_excited.txt', store=edit_manifest(lambda d: d['sources'].pop('NGFSRDW'))),
    # db-r47 finding 3: an entry binds to load_entry as Python binds it, and the file compiles
    case('library_index_keyword_twice', 'db-r47 F3', 'raised while handling SyntaxError: keyword argument repeated: index',
         database=repeat_index_keyword),
    case('library_index_position_and_keyword', 'db-r47 F3',
         RMG_REFUSES + "TypeError: load_entry() got multiple values for argument 'index')",
         database=index_by_position_and_keyword),
    # db-r47 finding 4: a file or directory that cannot be read is a reason, not a traceback
    case('dictionary_invalid_utf8', 'db-r47 F4', RMG_REFUSES + "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff",
         database=dictionary_invalid_utf8),
    case('dictionary_unreadable', 'db-r47 F4', 'dictionary.txt: cannot be read (PermissionError)',
         database=dictionary_unreadable),
    case('assembled_unreadable', 'db-r47 F4', 'cannot be listed', store=unreadable),
    # db-r48 finding 1: reactions.py is read as RMG reads it, UTF-8 text, and that text compiled
    case('library_utf8_bom', 'db-r48 F1', 'raised while handling SyntaxError: invalid non-printable character U+FEFF',
         database=library_bytes(lambda d: b'\xef\xbb\xbf' + d)),
    case('library_latin1_cookie', 'db-r48 F1', RMG_REFUSES + "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9",
         database=library_bytes(latin1_cookie)),
    case('library_kinetics_twice', 'db-r48 F1', 'raised while handling SyntaxError: keyword argument repeated: kinetics',
         database=entry_87_edit('    kinetics = ', '    kinetics = None,\n    kinetics = ')),
    case('library_label_position_and_keyword', 'db-r48 F1',
         RMG_REFUSES + "TypeError: load_entry() got multiple values for argument 'label')",
         database=entry_87_edit('    index = 87,\n', '    87,\n    "x",\n')),
    # db-r48 finding 2: every inventory the manifest declares is reconciled with what is derived
    case('manifest_n_blocks_stale', 'db-r48 F2', "['n_blocks'] is 64, the files give 65", generate=True,
         store=edit_manifest(lambda d: d['sources']['NGFSRDW'].__setitem__('n_blocks', 64))),
    case('manifest_blocks_used_stale', 'db-r48 F2', "['blocks_used'] differs from the files; missing [39]", generate=True,
         store=edit_manifest(lambda d: d['sources']['IST']['blocks_used'].pop())),
    case('manifest_process_missing', 'db-r48 F2', 'processes does not list', generate=True,
         store=edit_manifest(lambda d: d['processes'].pop())),
    case('manifest_process_duplicate', 'db-r48 F2', 'processes lists', generate=True,
         store=edit_manifest(lambda d: d['processes'].append(d['processes'][0]))),
    case('manifest_not_assembled_missing', 'db-r48 F2', 'not_assembled does not list', generate=True,
         store=edit_manifest(lambda d: d['not_assembled'].pop())),
    case('manifest_not_assembled_extra', 'db-r48 F2', 'which the store does not hold', generate=True,
         store=edit_manifest(lambda d: d['not_assembled'].append(dict(d['not_assembled'][0], block=999)))),
    case('manifest_process_wrong_block', 'db-r48 F2', "['source']['block'] is 999, the files give 1", generate=True,
         store=edit_manifest(lambda d: d['processes'][0]['source'].__setitem__('block', 999))),
    case('manifest_process_without_source', 'db-r48 F2', 'has no source binding', generate=True,
         store=edit_manifest(lambda d: d['processes'][0].pop('source'))),
    # db-r48 finding 3: a malformed manifest field is an input problem, never a traceback
    case('manifest_source_key_list', 'db-r48 F3', "'source_key' is [], not a string", generate=True,
         store=edit_manifest(lambda d: d['not_assembled'][0].__setitem__('source_key', []))),
    case('manifest_process_file_list', 'db-r48 F3', "'file' is [], not a string", generate=True,
         store=edit_manifest(lambda d: d['processes'][0].__setitem__('file', []))),
    case('manifest_sources_record_list', 'db-r48 F3', "'sha256' is missing", generate=True,
         store=edit_manifest(lambda d: d['sources'].__setitem__('TRINITI', []))),
    case('manifest_is_directory', 'db-r48 F3', 'cannot be read (IsADirectoryError)', generate=True,
         store=lambda a: (os.remove(os.path.join(a, gen.MANIFEST)), os.mkdir(os.path.join(a, gen.MANIFEST)))),
    # db-r49: the whole manifest is derived from the files and compared field by field
] + [case(f'manifest_{name}', 'db-r49 F1', expect, generate=True, store=manifest_set(*edit)) for name, expect, edit in [
    ('weight_stale', "statistical_weights['Ar(3P2)'] is 3, the files give 5", ('statistical_weights', 'Ar(3P2)', 3)),
    ('weight_missing', "statistical_weights['Ar(3P1)'] is missing", ('statistical_weights', 'Ar(3P1)', DROP)),
    ('weight_extra', "statistical_weights['Ar(9z)'] is declared", ('statistical_weights', 'Ar(9z)', 1)),
    ('weight_float', "statistical_weights['Ar(1S0)'] is True", ('statistical_weights', 'Ar(1S0)', True)),
    ('paschen_stale', "paschen['Ar(3P1)'] is '1s2', the files give '1s4'", ('paschen', 'Ar(3P1)', '1s2')),
    ('paschen_missing', "paschen['Ar(3P1)'] is missing", ('paschen', 'Ar(3P1)', DROP)),
    ('paschen_extra', "paschen['Ar(1S0)'] is declared", ('paschen', 'Ar(1S0)', 'ground')),
    ('catalogue_missing', "'paschen' is missing", ('paschen', DROP)),
    ('convention_missing', "conventions['STATE_RENAME'] is missing", ('conventions', 'STATE_RENAME', DROP)),
    ('convention_extra', "conventions['MADE_UP'] is declared", ('conventions', 'MADE_UP', 'a statement')),
    ('convention_not_prose', "conventions['STATE_RENAME'] is None, not prose", ('conventions', 'STATE_RENAME', None)),
    ('set_stale', "set is 'ar-v2', the files give 'ar-v1'", ('set', 'ar-v2')),
    ('ticket_stale', "ticket is 'I-340', the files give 'I-341'", ('ticket', 'I-340')),
    ('local_only_missing', "'local_only' is missing", ('local_only', DROP)),
    ('top_level_extra', "'notes' is declared, which the files do not give", ('notes', 'x')),
    ('source_path_other_file', "['source']['file'] is 'Ar_LXCat.txt', the files give 'Other.txt'",
     ('sources', 'IST', 'path', '/x/Other.txt')),
    ('source_field_extra', "sources['TRINITI']['role'] is declared", ('sources', 'TRINITI', 'role', 'x')),
    ('process_threshold_stale', "processes[1] (Ar_LXCat.txt collision 'e + Ar(1S0) -> e + Ar(3P2), Excitation')"
     "['threshold_eV'] is 12.0, the files give 11.548", ('processes', 1, 'threshold_eV', 12.0)),
    ('process_reverse_stale', "['reverse'] is True, the files give False", ('processes', 1, 'reverse', True)),
    ('process_descriptor_stale', "['descriptor'] is '[Ar(1S0) + e <-> Ar(3P2) + e, Excitation]'",
     ('processes', 1, 'descriptor', '[Ar(1S0) + e <-> Ar(3P2) + e, Excitation]')),
    ('process_kind_stale', "['kind'] is 'ELASTIC', the files give 'EXCITATION'", ('processes', 1, 'kind', 'ELASTIC')),
    ('process_target_stale', "['target'] is 'Ar(3P2)', the files give 'Ar(1S0)'",
     ('processes', 1, 'target', 'Ar(3P2)')),
    ('process_product_stale', "['product'] is 'Ar(3P1)', the files give 'Ar(3P2)'",
     ('processes', 1, 'product', 'Ar(3P1)')),
    ('process_conventions_stale', "['conventions'] is ['STATE_RENAME'], the files give []",
     ('processes', 1, 'conventions', ['STATE_RENAME'])),
    ('process_reason_not_prose', "['choice_reason'] is 3, not prose", ('processes', 1, 'choice_reason', 3)),
    ('process_field_extra', "['note'] is declared", ('processes', 1, 'note', 'x')),
    ('process_field_missing', "['kind'] is missing", ('processes', 1, 'kind', DROP)),
    ('process_source_file_stale', "['source']['file'] is 'BSR_Ar_ground.txt', the files give 'Ar_LXCat.txt'",
     ('processes', 0, 'source', 'file', 'BSR_Ar_ground.txt')),
    ('process_source_path_stale', "['source']['path'] is 'Ar.txt', not a path to Ar_LXCat.txt",
     ('processes', 0, 'source', 'path', 'Ar.txt')),
    ('process_source_line_stale', "['source']['line'] is 77, the files give 76",
     ('processes', 0, 'source', 'line', 77)),
    ('process_block_hash_stale', "['source']['block_sha256'] is '000",
     ('processes', 0, 'source', 'block_sha256', '0' * 64)),
    ('unused_process_stale', "(NGFSRDW_Ar_excited.txt block 1)['process'] is 'E + Ar(3p5 4s J = 0 1s3) -> E +",
     ('not_assembled', 0, 'process', 'E + Ar(3p5 4s J = 0 1s3) -> E + Ar(3p5 4p J = 1  2p10), Excitation')),
    ('unused_line_stale', "not_assembled[0] (NGFSRDW_Ar_excited.txt block 1)['line'] is 66, the files give 65",
     ('not_assembled', 0, 'line', 66)),
    ('unused_reason_not_prose', "['reason'] is '', not prose", ('not_assembled', 0, 'reason', '')),
    ('unused_field_extra', "['note'] is declared", ('not_assembled', 0, 'note', 'x')),
]]
    # db-r51: a library file RMG's own loader refuses is refused, with RMG's message, before it is read here
CASES += [case(name, 'db-r51 F1/F2', RMG_REFUSES + rmg, database=library_text(file, edit))
          for name, file, edit, rmg, _ in LIBRARY_TEXT_EDITS]
    # db-r52: what RMG loads is what is read: a commented record, a malformed overlay date
CASES += [
    case('dictionary_commented_triplet_resonance', 'db-r52 F1',
         'its dictionary species has multiplicity 3, the LS term 1',
         database=library_text('dictionary.txt', lambda t: t + COMMENTED_RESONANCE[3])),
    case('dictionary_commented_singlet_resonance', 'db-r52 F1', REGEN,
         database=library_text('dictionary.txt', lambda t: t + COMMENTED_RESONANCE[1])),
    case('dictionary_labelled_atoms', 'db-r52 F1', 'PASS',
         database=library_text('dictionary.txt', lambda t: t.replace('1 Ar', '1 *1 Ar'))),
    case('overlay_class_invalid_date', 'db-r52 F3', "class '2026-02-30', but",
         overlay=overlay_date('class: A', 'class: 2026-02-30')),
    case('overlay_reaction_invalid_month', 'db-r52 F3', "overlay says '2026-13-01'",
         overlay=overlay_date("reaction: 'Ar + e- => Ars + e-'", 'reaction: 2026-13-01')),
]
    # db-r53: an argon state is one argon atom; an index is a whole number; overlay text is valid Unicode
CASES += [
    case('dictionary_dimer_resonance', 'db-r53 F1', 'its dictionary species is Ar2, not one argon atom',
         database=library_text('dictionary.txt', lambda t: t + DIMER_RESONANCE)),
    case('dictionary_dimer_resonance_commented', 'db-r53 F1', 'its dictionary species is Ar2, not one argon atom',
         database=library_text('dictionary.txt', lambda t: t + '\n\n// an extra atom' + DIMER_RESONANCE[1:])),
] + [case(f'library_index_{name}', 'db-r53 F2',
          f"reactions.py: entry 'Ar + e- => Ars + e-': {expect} not a whole number",
          database=library_text('reactions.py', lambda t, v=value: t.replace('index = 87,', f'index = {v},', 1)))
     for name, value, expect in BAD_INDICES] + [
    case('overlay_surrogate_key', 'db-r53 F3', 'holds a string that is not valid Unicode text',
         overlay=overlay_text('collisions:\n',
                              'collisions:\n  "\\uD800": {class: A, reaction: \'Ar + e- => Ars + e-\'}\n')),
    case('overlay_surrogate_class', 'db-r53 F3', 'holds a string that is not valid Unicode text',
         overlay=overlay_text('{class: B}', '{class: "\\uD800"}')),
    case('overlay_surrogate_reaction', 'db-r53 F3', 'holds a string that is not valid Unicode text',
         overlay=overlay_text("reaction: 'Ar + e- => Ars + e-'", 'reaction: "A\\uDFFF"')),
]
    # db-r50: a member declared twice in the manifest's text, which a plain JSON decoding keeps only the last of
CASES += [case(f'manifest_duplicate_{name}', 'db-r50 F1', expect, generate=True, store=manifest_text(old, new))
          for name, old, new, expect in DUPLICATE_MEMBERS]
# Cases that only change the new command line: an older checker takes source directories, not files, and
# has no generator.
NEW_CLI_ONLY = {'comparison_source_left_out', 'assembled_source_left_out', 'generate_without_comparison_source',
                'extra_source_given', 'same_basename_other_folder', 'generate_without_excited_file',
                'collision_file_renamed', 'manifest_source_dropped'} | {
                    c['name'] for c in CASES if c['generate']}


def trimmed_overlay(overlay, doc):
    keep = {c['loki_process'] for c in doc['channels'] if c['lxcat_file'] != ASSEMBLED}
    return {'collisions': {k: v for k, v in overlay['collisions'].items() if k in keep}}


def omitted_excited_map(args, scratch, overlay, doc):
    """The map an honest regeneration gives when the store copy lacks the excited-state file and the overlay
    is trimmed to match: the review's omit_excited_file, made consistently by the generator itself."""
    work = os.path.join(scratch, '_omit_excited')
    asm = os.path.join(work, 'assembled')
    shutil.copytree(args.assembled, asm)
    os.remove(os.path.join(asm, ASSEMBLED))
    path = os.path.join(work, 'overlay.yaml')
    with open(path, 'w') as fh:
        yaml.safe_dump(trimmed_overlay(overlay, doc), fh, sort_keys=False, width=200)
    text, problems, _, labels = gen.generate(path, asm, args.source, args.database)
    assert problems[0] == f"collision file {ASSEMBLED} {NOT_IN_STORE}" and len(labels) == 39, problems
    return text.encode()


def verdict(cp):
    if 'Traceback (most recent call last)' in cp.stderr:  # a refusal carries its reason, not a traceback
        return f'CRASH({cp.returncode}, traceback)'
    if cp.returncode == 0 and 'RESULT: PASS' in cp.stdout:
        return 'PASS'
    if (cp.returncode == 1 and 'RESULT: FAIL' in cp.stdout) or (cp.returncode == 2 and 'usage:' in cp.stderr):
        return 'FAIL'
    return f'CRASH({cp.returncode})'


def write_logs(work, prefix, cp):
    for stream, text in (('stdout', cp.stdout), ('stderr', cp.stderr)):
        with open(os.path.join(work, f'{prefix}{stream}.log'), 'w') as fh:
            fh.write(text)


def run_case(args, c, map0, overlay0, scratch, omitted):
    work = os.path.join(scratch, c['name'])
    asm = os.path.join(work, 'assembled')
    shutil.copytree(args.assembled, asm)
    doc0 = yaml.safe_load(map0)
    hashes = {name: gen.sha256(os.path.join(asm, name)) for name in os.listdir(asm)}
    if c['store']:
        c['store'](asm)
    # the map: as committed, edited, or the consistent map without the excited-state file
    if c['map'] == 'omit_excited':
        data = omitted
    elif getattr(c['map'], 'raw', False):
        data = c['map'](map0.encode())
    elif c['map']:
        doc = copy.deepcopy(doc0)
        c['map'](doc)
        data = gen.render(doc).encode()
    else:
        data = map0.encode()
    if c['refresh']:
        for name, digest in hashes.items():
            if os.path.exists(os.path.join(asm, name)):
                data = data.replace(digest.encode(), gen.sha256(os.path.join(asm, name)).encode())
    map_path = os.path.join(work, 'argon_channel_map.yaml')
    open(map_path, 'wb').write(data)
    # the overlay
    if c['overlay'] == 'omit_excited':
        data = yaml.safe_dump(trimmed_overlay(yaml.safe_load(overlay0), doc0), sort_keys=False, width=200).encode()
    elif getattr(c['overlay'], 'raw', False):
        data = c['overlay'](overlay0)
    elif c['overlay']:
        overlay = yaml.safe_load(overlay0)
        c['overlay'](overlay, doc0)
        data = yaml.safe_dump(overlay, sort_keys=False, width=200).encode()
    else:
        data = overlay0
    overlay_path = os.path.join(work, 'argon_channel_overlay.yaml')
    open(overlay_path, 'wb').write(data)
    # the library and the source files
    database = args.database
    if c['database']:
        database = os.path.join(work, 'input')
        lib = os.path.join('kinetics', 'libraries', gen.LIBRARY)
        shutil.copytree(os.path.join(args.database, lib), os.path.join(database, lib))
        c['database'](database)
    sources = [s for s in args.source if os.path.basename(s) != c['drop_source']]
    if c['source_edit']:
        os.makedirs(os.path.join(work, 'sources'))
        copied = []
        for s in sources:
            copied.append(os.path.join(work, 'sources', os.path.basename(s)))
            shutil.copyfile(s, copied[-1])
            c['source_edit'](copied[-1])
        folder = os.path.join(work, 'sources')
        sources = copied + [os.path.join(folder, x) for x in sorted(os.listdir(folder))
                            if os.path.join(folder, x) not in copied]
    if c['source_list']:
        sources = c['source_list'](work, sources)
    rates = ['--loki-rates', args.loki_rates] if args.loki_rates and c['rates'] else []
    given = [x for s in ([] if c['no_sources'] else sources) for x in ('--source', s)]
    cp = regenerated = None
    if c['generate']:
        generator = os.path.join(os.path.dirname(os.path.abspath(args.checker)), 'gen_eedf_channel_map.py')
        cmd = [sys.executable, generator, '--overlay', overlay_path, '--assembled', asm, '--database', database,
               '--output', map_path] + given
        cp = subprocess.run(cmd, capture_output=True, text=True)
        write_logs(work, 'generate.', cp)
        if cp.returncode == 0:
            cp, regenerated = None, open(map_path, 'rb').read()
    # the checker under test
    if cp is None:
        cmd = [sys.executable, args.checker, map_path, '--overlay', overlay_path, '--assembled', asm,
               '--database', database] + rates + given
        cp = subprocess.run(cmd, capture_output=True, text=True)
        write_logs(work, '', cp)
    got = verdict(cp)
    fails = [x for x in cp.stdout.splitlines() if x.startswith('FAIL')]
    if c['expect'] == 'PASS':
        ok, why = got == 'PASS', (fails[0] if fails else '')
        if regenerated is not None and regenerated != map0.encode():
            ok, why = False, 'the regeneration differs from the committed map'

    else:
        hit = next((x for x in fails if c['expect'] in x), None)
        if hit is None and c['expect'] in cp.stderr and got == 'FAIL':
            hit = cp.stderr.strip().splitlines()[-1]
        ok = got == 'FAIL' and hit is not None
        why = hit or 'NOT FOR THE NAMED REASON: ' + (fails[0] if fails else cp.stderr.strip()[-100:])
    # the older checker, through its own command line
    old = 'n/a'
    if args.old_checker and c['name'] not in NEW_CLI_ONLY:
        cmd = [sys.executable, args.old_checker, map_path, '--assembled', asm, '--database', database] + rates
        for d in [] if c['no_sources'] else sorted({os.path.dirname(os.path.abspath(s)) for s in sources}):
            cmd += ['--sources', d]
        cp = subprocess.run(cmd, capture_output=True, text=True)
        write_logs(work, 'old.', cp)
        old = verdict(cp)
    os.chmod(asm, 0o755)  # a case may have made it unreadable; the scratch must still be removable
    print(f"{'ok  ' if ok else 'BAD '} {c['name']:38s} {c['origin']:22s} new {got:9s} old {old:9s} {why[:150]}")
    return ok, got, old, c['expect'] == 'PASS'


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('map', help='the committed channel-map YAML')
    parser.add_argument('--overlay', required=True, help='the committed overlay')
    parser.add_argument('--assembled', required=True, help='directory holding the assembled LoKI-B files')
    parser.add_argument('--source', action='append', required=True, help='a source LXCat file (repeatable)')
    parser.add_argument('--loki-rates', help='a LoKI-B rateCoefficients.txt solved on the assembled set')
    parser.add_argument('--database', default=os.path.join(here, '..', 'input'),
                        help="the database 'input' directory (default: the one beside this script)")
    parser.add_argument('--checker', default=os.path.join(here, 'check_eedf_channel_map.py'),
                        help='the checker under test (default: the one beside this script)')
    parser.add_argument('--old-checker', help='also run every case against this older, map-only checker')
    parser.add_argument('--keep', action='store_true', help='keep the scratch directory and print its path')
    args = parser.parse_args()
    try:  # a fixture that cannot be read or parsed is a usage error, not a fault of the suite
        map0 = open(args.map, encoding='utf-8').read()
        overlay0 = open(args.overlay, 'rb').read()
        map_doc, overlay_doc = yaml.safe_load(map0), yaml.safe_load(overlay0)
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        print(f'BAD  a fixture cannot be read: {type(exc).__name__}: {exc}')
        return 2
    if gen.render(map_doc) != map0:
        print('BAD  the map does not survive a parse and render unchanged, so its edits cannot be made faithfully')
        return 1
    scratch = tempfile.mkdtemp(prefix='eedf-map-mutations-')
    try:
        omitted = omitted_excited_map(args, scratch, overlay_doc, map_doc)
        results = [run_case(args, c, map0, overlay0, scratch, omitted) for c in CASES]
    finally:
        if args.keep:
            print(f'scratch kept: {scratch}')
        else:
            shutil.rmtree(scratch)
    bad = sum(1 for ok, *_ in results if not ok)
    controls = sum(1 for *_, must_pass in results if must_pass)
    print(f'{len(results) - bad}/{len(results)} cases as expected ({controls} must pass, '
          f'{len(results) - controls} must be refused for the named reason)')
    if args.old_checker:
        mistakes = [old for ok, new, old, must_pass in results if not must_pass and old != 'n/a']
        print(f"older checker on the same {len(mistakes)} mistakes: refused {mistakes.count('FAIL')}, passed "
              f"{mistakes.count('PASS')}, crashed {sum(1 for o in mistakes if o.startswith('CRASH'))}; on the "
              f"{controls} controls: {', '.join(old for ok, new, old, must_pass in results if must_pass)}")
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
