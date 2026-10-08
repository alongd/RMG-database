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
Tests for the generated argon channel map (input/eedf/argon_channel_map.yaml), its overlay, and the
generator and checker in scripts/ (I-341).

The first group needs only this repository: the map is in the generator's exact output form, it carries
the overlay's classes and reactions and nothing else hand-written, its RMG fields follow PlasmaArgon, the
library is read as RMG loads it (checked against RMG's own loader where rmgpy is importable), and the
overlay loader, the policy, the source and output handling refuse what they must.

The second group regenerates the map from the local LXCat store, which never enters a repository. It runs
only when the store is named in the environment, and is skipped otherwise:

    EEDF_LXCAT_ASSEMBLED  the assembled LoKI-B directory (ar-v1)
    EEDF_LXCAT_SOURCES    the source LXCat files, separated by os.pathsep
    EEDF_LOKI_RATES       optional: a LoKI-B rateCoefficients.txt solved on ar-v1
"""

import hashlib
import inspect
import json
import os
import shutil
import subprocess
import sys

import pytest
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
SCRIPTS = os.path.join(ROOT, 'scripts')
DATABASE = os.path.join(ROOT, 'input')
MAP = os.path.join(DATABASE, 'eedf', 'argon_channel_map.yaml')
OVERLAY = os.path.join(DATABASE, 'eedf', 'argon_channel_overlay.yaml')
sys.path.insert(0, SCRIPTS)
import gen_eedf_channel_map as gen  # noqa: E402
import test_eedf_channel_map_mutations as mutations  # noqa: E402

ASSEMBLED = os.environ.get('EEDF_LXCAT_ASSEMBLED')
SOURCES = [s for s in os.environ.get('EEDF_LXCAT_SOURCES', '').split(os.pathsep) if s]
RATES = os.environ.get('EEDF_LOKI_RATES')
needs_store = pytest.mark.skipif(not (ASSEMBLED and SOURCES),
                                 reason='the local LXCat store is not named (EEDF_LXCAT_ASSEMBLED, EEDF_LXCAT_SOURCES)')
GENERATOR = os.path.join(SCRIPTS, 'gen_eedf_channel_map.py')
CHECKER = os.path.join(SCRIPTS, 'check_eedf_channel_map.py')
LIBRARY_DIR = os.path.join('kinetics', 'libraries', gen.LIBRARY)


@pytest.fixture(scope='module')
def committed():
    text = open(MAP, encoding='utf-8').read()
    return text, yaml.safe_load(text)


@pytest.fixture(scope='module')
def overlay():
    loaded, problems = gen.load_overlay(OVERLAY)
    assert problems == []
    return loaded


def write(tmp_path, text):
    path = tmp_path / 'overlay.yaml'
    path.write_bytes(text if isinstance(text, bytes) else text.encode())
    return str(path)


class TestCommittedMap:

    def test_map_is_in_the_generators_exact_form(self, committed):
        """A hand edit that changes the layout, or a map written by anything but the generator, fails here."""
        text, doc = committed
        assert text.startswith(gen.HEADER)
        assert gen.render(doc) == text

    def test_map_carries_exactly_the_overlay(self, committed, overlay):
        """Every collision is in the overlay once, and the map's class and reaction are the overlay's."""
        _, doc = committed
        assert [c['loki_process'] for c in doc['channels']] and \
            sorted(c['loki_process'] for c in doc['channels']) == sorted(overlay)
        for c in doc['channels']:
            entry = overlay[c['loki_process']]
            assert c['class'] == entry['class'], c['id']
            assert (c.get('rmg') or {}).get('reaction') == entry['reaction'], c['id']

    def test_classes_are_within_policy(self, committed):
        _, doc = committed
        for c in doc['channels']:
            family = c['family'].split(' from ')[0]
            assert c['class'] in gen.POLICY[family]['classes'], (c['id'], family, c['class'])
        assert doc['class_counts'] == {'A': 152, 'B': 5, 'C': 0, 'D': 0}

    def test_rmg_fields_follow_the_library(self, committed):
        """Index, status and missing species are what PlasmaArgon says today, as RMG loads it from one read."""
        _, doc = committed
        entries, species, problems = gen.load_library(DATABASE, gen.LIBRARY)
        assert problems == []
        for c in doc['channels']:
            rmg = c.get('rmg')
            if not rmg:
                continue
            index = next((i for i, label in entries.items() if label == rmg['reaction']), None)
            assert rmg['index'] == (None if rmg['status'] == 'lumped_internal' else index), c['id']
            assert (rmg['status'] in ('present', 'present_lumped')) == (rmg['index'] is not None), c['id']
            for name in rmg.get('species_needed', []):
                assert name not in species, (c['id'], name)
        assert doc['states']['Ar(3P1)']['rmg_species'] == 'Ar(1s4)'
        assert doc['states']['Ar(3P0)']['lumped_into'] == 'Ar(3P2)'


class TestOverlayLoader:

    @pytest.mark.parametrize('text, reason', [
        ("collisions:\n  'x': {class: B}\n  'x': {class: A}\n", 'appears twice'),
        ('collisions:\n  .nan: {class: B}\n', 'is not a string'),
        ('collisions:\n  1: {class: B}\n', 'is not a string'),
        ("collisions:\n  'x': &a {class: B}\n  'y': *a\n", 'anchors and aliases'),
        ("collisions:\n  'x': {class: !!str B}\n", 'explicit tags'),
        (b'\xff\xfecollisions: {}\n', 'cannot be read as UTF-8'),
        ("collisions:\n  'x': {class: [A]}\n", 'is not a string'),
        ("collisions:\n  'x': {class: A, reaction: 'Ar + e- => Ars + e-', index: 87}\n", 'and nothing else'),
        ("channels: {}\n", "single key 'collisions'"),
    ])
    def test_refuses(self, tmp_path, text, reason):
        loaded, problems = gen.load_overlay(write(tmp_path, text))
        assert any(reason in p for p in problems), problems

    def test_accepts_the_plain_form(self, tmp_path):
        loaded, problems = gen.load_overlay(write(tmp_path, "collisions:\n  'x': {class: A, reaction: 'a => b'}\n"))
        assert problems == [] and loaded == {'x': {'class': 'A', 'reaction': 'a => b'}}


def library_copy(tmp_path, edit=None):
    """A copy of the library under tmp_path/input, with one edit of the mutation suite applied."""
    database = tmp_path / 'input'
    shutil.copytree(os.path.join(DATABASE, LIBRARY_DIR), database / LIBRARY_DIR)
    if edit:
        edit(str(database))
    return str(database)


LIBRARY_EDITS = [
    (None, set(range(86, 94))),
    (mutations.disable_library_entry, set(range(86, 94)) - {87}),
    (mutations.requote_library_label, set(range(86, 94))),
    (mutations.label_before_index, set(range(86, 94))),
]


class TestLibraryReader:
    """The library is read as RMG loads it: an entry kept inside a string is not there, and the quoting and
    keyword order of an entry do not matter (db-r46 finding 1)."""

    @pytest.mark.parametrize('edit, indices', LIBRARY_EDITS)
    def test_reads_the_entries_rmg_loads(self, tmp_path, edit, indices):
        entries, problems = gen.library_entries(library_copy(tmp_path, edit), gen.LIBRARY)
        assert problems == [] and set(entries) == indices
        assert entries[86] == gen.library_entries(DATABASE, gen.LIBRARY)[0][86]

    def test_refuses_what_only_running_the_file_would_show(self, tmp_path):
        entries, problems = gen.library_entries(library_copy(tmp_path, mutations.library_entry_in_if), gen.LIBRARY)
        assert any('cannot be read without running the file' in p for p in problems), problems

    @pytest.mark.parametrize('text, reason', [
        ('entry(index = 1, label = "a => b", kinetics = None)\nentry(index = 1, label = "c => d", kinetics = None)\n',
         'appears twice'),
        ('i = 1\nentry(index = i, label = "a => b", kinetics = None)\n', 'without a literal integer index'),
        ('entry(**{"index": 1, "label": "a => b"})\n', 'unpacks its arguments'),
        ('def entry(**k):\n    pass\n', 'FunctionDef statement'),
        ('entry(index = 1, label = "a => b"\n', 'cannot be read as Python'),
        ('entry(index = 1, index = 1, label = "a => b", kinetics = None)\n', 'cannot be read as Python'),
        ('entry(1, index = 1, label = "a => b", kinetics = None)\n', "gives 'index' twice"),
        ('entry(1, "a => b", None, label = "c => d")\n', "gives 'label' twice"),
        ('entry(index = 1, label = "a => b", kinetics = None, rate = 2)\n', "gives 'rate', which load_entry"),
        ('entry(index = 1, label = "a => b")\n', 'does not give kinetics'),
    ])
    def test_refuses(self, tmp_path, text, reason):
        database = library_copy(tmp_path)
        open(os.path.join(database, LIBRARY_DIR, 'reactions.py'), 'w').write(text)
        _, problems = gen.library_entries(database, gen.LIBRARY)
        assert any(reason in p for p in problems), problems

    def test_binds_as_rmgs_load_entry(self):
        library = pytest.importorskip('rmgpy.data.kinetics.library')
        parameters = list(inspect.signature(library.KineticsLibrary.load_entry).parameters.values())[1:]
        assert tuple(x.name for x in parameters) == gen.ENTRY_PARAMETERS
        assert tuple(x.name for x in parameters if x.default is inspect.Parameter.empty) == gen.ENTRY_REQUIRED

    @pytest.mark.parametrize('edit', [mutations.repeat_index_keyword, mutations.index_by_position_and_keyword])
    def test_refuses_what_rmg_refuses(self, tmp_path, edit):
        database = library_copy(tmp_path, edit)
        _, problems = gen.library_entries(database, gen.LIBRARY)
        assert problems
        library = pytest.importorskip('rmgpy.data.kinetics.library')
        kinetics = pytest.importorskip('rmgpy.data.kinetics.database')
        with pytest.raises(Exception):
            library.KineticsLibrary(label=gen.LIBRARY).load(os.path.join(database, LIBRARY_DIR, 'reactions.py'),
                                                            local_context=kinetics.KineticsDatabase().local_context)

    @pytest.mark.parametrize('edit, indices', LIBRARY_EDITS)
    def test_agrees_with_rmg(self, tmp_path, edit, indices):
        """RMG's own loader, where it is importable, loads exactly the entries the generator reads."""
        library = pytest.importorskip('rmgpy.data.kinetics.library')
        database = pytest.importorskip('rmgpy.data.kinetics.database')
        path = os.path.join(library_copy(tmp_path, edit), LIBRARY_DIR, 'reactions.py')
        loaded = library.KineticsLibrary(label=gen.LIBRARY)
        loaded.load(path, local_context=database.KineticsDatabase().local_context)
        entries, _ = gen.library_entries(str(tmp_path / 'input'), gen.LIBRARY)
        assert {int(i): e.label for i, e in loaded.entries.items()} == entries
        assert set(entries) == indices


class TestInputsAndOutput:
    """A bad file or a bad --output is a refusal with its reason, never a traceback (db-r46 finding 3), and
    the source set is the store manifest's (db-r46 finding 2)."""

    def test_a_source_that_is_not_utf8_is_a_reason(self, tmp_path):
        source = tmp_path / 'X.txt'
        source.write_bytes(b'DATABASE: x\n\xff\n')
        store = tmp_path / 'store'
        store.mkdir()
        (store / 'manifest.json').write_text(json.dumps(
            {'sources': {'X': {'path': '/elsewhere/X.txt', 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}}}))
        _, problems, _, _ = gen.generate(OVERLAY, str(store), [str(source)], DATABASE)
        assert any('source X.txt: cannot be read as UTF-8 text' in p for p in problems), problems

    def test_a_store_without_its_manifest_is_a_reason(self, tmp_path):
        _, problems, _, _ = gen.generate(OVERLAY, str(tmp_path), [], DATABASE)
        assert any('the required source set is unknown' in p for p in problems), problems

    def test_a_source_the_manifest_does_not_name_is_a_reason(self, tmp_path):
        source = tmp_path / 'Y.txt'
        source.write_bytes(b'DATABASE: y\n')
        (tmp_path / 'manifest.json').write_text(json.dumps({'sources': {'X': {'path': 'X.txt', 'sha256': '0' * 64}}}))
        _, problems, _, _ = gen.generate(OVERLAY, str(tmp_path), [str(source)], DATABASE)
        assert any("Y.txt (SHA-256" in p and "not a source named by the store's manifest" in p for p in problems)
        assert any("X (X.txt, SHA-256 000000000000...) named by the store's manifest was not given" in p
                   for p in problems), problems

    @pytest.mark.parametrize('name, file, edit, rmg, own', mutations.LIBRARY_TEXT_EDITS)
    def test_a_file_rmg_refuses_is_refused_with_rmgs_message(self, tmp_path, name, file, edit, rmg, own):
        """RMG's own loader refuses the edited library first; the generator's own readers refuse it too."""
        database = library_copy(tmp_path, mutations.library_text(file, edit))
        problems = gen.rmg_library_load(database, gen.LIBRARY)
        assert len(problems) == 1 and f"library {gen.LIBRARY}: RMG's own loader refuses it ({rmg}" in problems[0]
        _, problems, _, _ = gen.generate(OVERLAY, str(tmp_path), [], database)
        assert any(f"RMG's own loader refuses it ({rmg}" in p for p in problems), problems
        read = gen.library_species if file == 'dictionary.txt' else gen.library_entries
        found, problems = read(database, gen.LIBRARY)
        assert found is None or problems, (found, problems)
        assert any(own in p for p in problems), problems

    @pytest.mark.parametrize('multiplicity', [1, 3])
    def test_a_commented_dictionary_record_is_what_rmg_loads(self, tmp_path, multiplicity):
        """A '//' comment before a record does not become a species: the species are the ones RMG parsed."""
        database = library_copy(tmp_path, mutations.library_text(
            'dictionary.txt', lambda t: t + mutations.COMMENTED_RESONANCE[multiplicity]))
        entries, species, problems = gen.load_library(database, gen.LIBRARY)
        assert problems == []
        assert species['Ar(1s2)'] == {'atoms': {'Ar': 1}, 'charge': 0, 'multiplicity': multiplicity}
        assert not any('//' in label for label in species)

    def test_a_reader_that_disagrees_with_rmg_is_refused(self, tmp_path, monkeypatch):
        """Where the reader here reads a field otherwise than RMG loaded it, the field is named and refused."""
        own = gen.species_from_text
        monkeypatch.setattr(gen, 'species_from_text', lambda library, text: (
            {k: dict(v, multiplicity=1) if k == 'Ars' else v for k, v in own(library, text)[0].items()}, []))
        _, species, problems = gen.load_library(DATABASE, gen.LIBRARY)
        assert species is None
        assert problems == [f'library {gen.LIBRARY} dictionary.txt: species Ars: multiplicity: RMG loads 3, this '
                            f'reader reads 1']

    @pytest.mark.parametrize('file, old, new', [
        ('reactions.py', 'kinetics = TwoTemperaturePlasma(', 'kinetics = TwoTemperaturePlamsa('),
        ('dictionary.txt', 'multiplicity 3', 'multiplicty 3')])
    def test_a_file_saved_after_it_is_read_is_never_seen(self, tmp_path, monkeypatch, file, old, new):
        """db-r52's concurrent save, made deterministic: each library file is saved again, with an edit RMG
        refuses, as soon as the generator has read it. What is loaded and derived is the bytes read, and no
        library file is opened again after that read."""
        database = library_copy(tmp_path)
        folder = os.path.realpath(os.path.join(database, LIBRARY_DIR))
        clean = gen.load_library(DATABASE, gen.LIBRARY)
        read, opened, real_open = gen.library_files, [], open

        def read_then_save(*args, **kwargs):
            files = read(*args, **kwargs)
            path = os.path.join(folder, file)
            text = real_open(path, encoding='utf-8').read()
            assert old in text
            real_open(path, 'w', encoding='utf-8').write(text.replace(old, new, 1))
            monkeypatch.setattr('builtins.open', spy)
            return files

        def spy(path, *args, **kwargs):
            opened.append(os.path.realpath(path) if isinstance(path, (str, bytes, os.PathLike)) else path)
            return real_open(path, *args, **kwargs)
        monkeypatch.setattr(gen, 'library_files', read_then_save)
        loaded = gen.load_library(database, gen.LIBRARY)
        monkeypatch.setattr('builtins.open', real_open)
        assert loaded == clean and loaded[2] == []
        assert not [p for p in opened if isinstance(p, str) and p.startswith(folder)], opened
        monkeypatch.setattr(gen, 'library_files', read)
        assert "RMG's own loader refuses it" in gen.load_library(database, gen.LIBRARY)[2][0]

    @pytest.mark.parametrize('old, new, value', [('class: A', 'class: 2026-02-30', '2026-02-30'),
                                                 ("reaction: 'Ar + e- => Ars + e-'", 'reaction: 2026-13-01',
                                                  '2026-13-01')])
    def test_an_overlay_date_is_its_text_not_a_date(self, tmp_path, old, new, value):
        """An unquoted date in the overlay is not constructed, so a malformed one is no traceback (db-r52)."""
        path = tmp_path / 'overlay.yaml'
        path.write_bytes(mutations.overlay_date(old, new)(open(OVERLAY, 'rb').read()))
        overlay, problems = gen.load_overlay(str(path))
        assert problems == [] and value in [v for e in overlay.values() for v in e.values()]
        cp = subprocess.run([sys.executable, GENERATOR, '--overlay', str(path), '--assembled', str(tmp_path),
                             '--source', OVERLAY, '--output', str(tmp_path / 'map.yaml')],
                            capture_output=True, text=True)
        assert cp.returncode == 1 and cp.stderr == '' and 'RESULT: FAIL' in cp.stdout

    @pytest.mark.parametrize('commented', [False, True])
    def test_an_argon_state_is_one_argon_atom(self, tmp_path, commented):
        """A record with an atom copied once too often is Ar2 as RMG loads it, and Ar2 is no atomic argon
        state (db-r53 finding 1): the atom counts are kept, by RMG and by the reader here."""
        record = ('\n\n// an extra atom' if commented else '\n') + mutations.DIMER_RESONANCE[1:]
        database = library_copy(tmp_path, mutations.library_text('dictionary.txt', lambda t: t + record))
        _, species, problems = gen.load_library(database, gen.LIBRARY)
        assert problems == []
        assert species['Ar(1s2)'] == {'atoms': {'Ar': 2}, 'charge': 0, 'multiplicity': 1}
        assert gen.species_problem('Ar(1P1)', 'Ar(1s2)', species, {}) == (
            'its dictionary species is Ar2, not one argon atom')

    def test_a_reader_that_loses_an_atom_is_refused(self, tmp_path, monkeypatch):
        database = library_copy(tmp_path, mutations.library_text(
            'dictionary.txt', lambda t: t + mutations.DIMER_RESONANCE))
        own = gen.species_from_text
        monkeypatch.setattr(gen, 'species_from_text', lambda library, text: (
            {k: dict(v, atoms={'Ar': 1}) if k == 'Ar(1s2)' else v for k, v in own(library, text)[0].items()}, []))
        assert gen.load_library(database, gen.LIBRARY)[2] == [
            f"library {gen.LIBRARY} dictionary.txt: species Ar(1s2): atoms: RMG loads {{'Ar': 2}}, this reader "
            f"reads {{'Ar': 1}}"]

    @pytest.mark.parametrize('value', ['None', '"eighty-seven"', '""', '"87"', 'True', '87.0'])
    def test_a_loaded_index_that_is_no_whole_number_is_a_reason(self, tmp_path, value):
        """RMG keeps whatever key an entry gives as its index; one that is not a whole number is a named
        reactions.py refusal before anything converts it (db-r53 finding 2)."""
        database = library_copy(tmp_path, mutations.library_text(
            'reactions.py', lambda t: t.replace('index = 87,', f'index = {value},', 1)))
        entries, species, problems = gen.load_library(database, gen.LIBRARY)
        assert entries is None and species is None
        assert problems == [f"library {gen.LIBRARY} reactions.py: entry 'Ar + e- => Ars + e-': index {value} is "
                            f"not a whole number".replace('"', "'")]
        cp = subprocess.run([sys.executable, GENERATOR, '--overlay', OVERLAY, '--assembled', str(tmp_path),
                             '--source', OVERLAY, '--database', database, '--output', str(tmp_path / 'map.yaml')],
                            capture_output=True, text=True)
        assert cp.returncode == 1 and cp.stderr == '' and problems[0] in cp.stdout, cp.stdout

    @pytest.mark.parametrize('old, new', [
        ('collisions:\n', 'collisions:\n  "\\uD800": {class: A}\n'),
        ('{class: B}', '{class: "\\uD800"}'),
        ("reaction: 'Ar + e- => Ars + e-'", 'reaction: "A\\uDFFF"')])
    def test_an_overlay_string_that_is_not_unicode_is_a_reason(self, tmp_path, old, new):
        """A YAML escape can write a lone surrogate; it is refused where the overlay is read, and the checker
        and generator print every diagnostic, whatever it holds (db-r53 finding 3)."""
        path = tmp_path / 'overlay.yaml'
        path.write_bytes(mutations.overlay_text(old, new)(open(OVERLAY, 'rb').read()))
        overlay, problems = gen.load_overlay(str(path))
        assert overlay is None and len(problems) == 1 and 'is not valid Unicode text' in problems[0]
        common = ['--overlay', str(path), '--assembled', str(tmp_path), '--source', OVERLAY]
        for cmd in ([GENERATOR] + common + ['--output', str(tmp_path / 'map.yaml')], [CHECKER, MAP] + common):
            cp = subprocess.run([sys.executable] + cmd, capture_output=True, text=True)
            assert cp.returncode == 1 and cp.stderr == '' and 'RESULT: FAIL' in cp.stdout, cp.stderr

    def test_a_diagnostic_is_printable_whatever_it_holds(self):
        assert gen.printable('state \ud800') == 'state \\ud800'
        assert gen.printable('Ar(1s2) + e-') == 'Ar(1s2) + e-'

    @pytest.mark.parametrize('missing', ['map', 'overlay'])
    def test_the_mutation_runner_reports_a_missing_fixture(self, tmp_path, missing):
        """A fixture path that is wrong is a usage error with its reason, not a traceback (db-r53 finding 4)."""
        paths = {'map': MAP, 'overlay': OVERLAY, missing: str(tmp_path / 'absent.yaml')}
        cp = subprocess.run([sys.executable, os.path.join(SCRIPTS, 'test_eedf_channel_map_mutations.py'),
                             paths['map'], '--overlay', paths['overlay'], '--assembled', str(tmp_path),
                             '--source', OVERLAY], capture_output=True, text=True)
        assert cp.returncode == 2 and cp.stderr == ''
        assert cp.stdout.startswith('BAD  a fixture cannot be read: FileNotFoundError'), cp.stdout

    def test_the_library_rmg_loads_is_read_here(self):
        assert gen.rmg_library_load(DATABASE, gen.LIBRARY) == []

    @pytest.mark.parametrize('edit', [mutations.dictionary_invalid_utf8, mutations.dictionary_unreadable])
    def test_a_dictionary_that_cannot_be_read_is_a_reason(self, tmp_path, edit):
        species, problems = gen.library_species(library_copy(tmp_path, edit), gen.LIBRARY)
        reason = ('cannot be read as UTF-8 text (UnicodeDecodeError)' if edit is mutations.dictionary_invalid_utf8
                  else 'cannot be read (PermissionError)')
        assert species is None and problems == [f'library {gen.LIBRARY} dictionary.txt: {reason}']

    def test_an_unreadable_store_is_a_reason(self, tmp_path):
        store = tmp_path / 'store'
        store.mkdir()
        os.chmod(store, 0)
        try:
            _, problems, _, _ = gen.generate(OVERLAY, str(store), [], DATABASE)
        finally:
            os.chmod(store, 0o755)
        assert any(f'--assembled {store}: cannot be listed (PermissionError)' in p for p in problems), problems

    def test_the_manifest_must_agree_with_itself_and_the_store(self, tmp_path):
        a, b = tmp_path / 'one' / 'S.txt', tmp_path / 'two' / 'S.txt'
        for path, text in ((a, b'DATABASE: a\n'), (b, b'DATABASE: b\n')):
            path.parent.mkdir()
            path.write_bytes(text)
        digest = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in (a, b)}
        store = tmp_path / 'store'
        store.mkdir()
        (store / 'L.txt').write_bytes(b'PARAM.: x\n')
        (store / 'manifest.json').write_text(json.dumps({
            'sources': {'A': {'path': '/old/S.txt', 'sha256': digest[a]}, 'B': {'path': '/old/S.txt', 'sha256': digest[b]}},
            'loki_files': {'M.txt': '1' * 64},
            'not_assembled': [{'source_key': 'C', 'block': 1, 'line': 1, 'block_sha256': '3' * 64}],
            'processes': [{'file': 'N.txt', 'loki_label': 'x', 'source': {'key': 'A', 'sha256': '2' * 64, 'block': 1,
                                                                         'line': 1, 'block_sha256': '3' * 64}}]}))
        _, problems, _, _ = gen.generate(OVERLAY, str(store), [str(a), str(b)], DATABASE)
        for reason in ('2 sources share the file name S.txt',
                       "not_assembled[0]: names source C, which the manifest's 'sources' do not",
                       'processes[0].source: names source A with another SHA-256',
                       "processes[0]: names collision file N.txt, which its 'loki_files' do not",
                       "source A: 'n_blocks' is missing, not a whole number",
                       "collision file M.txt named by the store's manifest is not in the assembled directory",
                       "collision file L.txt is not one the store's manifest names",
                       'source S.txt: two different files under this one name'):
            assert any(reason in p for p in problems), (reason, problems)

    @pytest.mark.parametrize('record, reason', [
        ({'sources': {'A': []}}, "source A: 'sha256' is missing, not a SHA-256"),
        ({'sources': {'A': {'sha256': '1' * 64, 'path': 7}}}, "source A: 'path' is 7, not a string"),
        ({'sources': {'A': {'sha256': '1' * 64}}, 'not_assembled': [{'source_key': []}]},
         "not_assembled[0]: 'source_key' is [], not a string"),
        ({'sources': {'A': {'sha256': '1' * 64}}, 'processes': [{'file': [], 'source': {}}]},
         "processes[0]: 'file' is [], not a string"),
        ({'sources': {'A': {'sha256': '1' * 64}}, 'processes': [{'file': 'L.txt'}]}, 'has no source binding'),
        ({'sources': {'A': {'sha256': '1' * 64}}, 'processes': {}}, "'processes' is not a list"),
    ])
    def test_a_malformed_manifest_field_is_a_reason(self, tmp_path, record, reason):
        (tmp_path / 'manifest.json').write_text(json.dumps(record))
        _, problems, _, _ = gen.generate(OVERLAY, str(tmp_path), [], DATABASE)
        assert any(reason in p for p in problems), problems

    def test_a_member_declared_twice_is_a_reason_at_any_depth(self, tmp_path):
        (tmp_path / 'manifest.json').write_text('{"set": "a", "sources": {"A": {"sha256": "1", "sha256": "2"}}, '
                                                '"processes": [{}, {"source": {"line": 1, "line": 2}}], "set": "b"}')
        _, problems = gen.store_manifest(str(tmp_path))
        where = f'the store manifest {gen.MANIFEST}'
        assert problems[:3] == [f"{where}: set is declared 2 times ('a', 'b'); each member may be declared once",
                                f"{where}: sources['A']['sha256'] is declared 2 times ('1', '2'); each member may "
                                f"be declared once",
                                f"{where}: processes[1]['source']['line'] is declared 2 times (1, 2); each member "
                                f"may be declared once"]

    @pytest.mark.parametrize('prefix, reason', [(b'\xef\xbb\xbf', 'cannot be read as Python'),
                                                (b'# encoding: latin-1\n# caf\xe9\n', 'cannot be read as UTF-8 text')])
    def test_reactions_are_read_as_rmg_reads_them(self, tmp_path, prefix, reason):
        database = library_copy(tmp_path)
        path = os.path.join(database, LIBRARY_DIR, 'reactions.py')
        open(path, 'wb').write(prefix + open(path, 'rb').read())
        entries, problems = gen.library_entries(database, gen.LIBRARY)
        assert entries is None and any(reason in p for p in problems), problems
        library = pytest.importorskip('rmgpy.data.kinetics.library')
        kinetics = pytest.importorskip('rmgpy.data.kinetics.database')
        with pytest.raises(Exception):
            library.KineticsLibrary(label=gen.LIBRARY).load(path, local_context=kinetics.KineticsDatabase().local_context)

    def test_a_directory_as_output_is_refused_cleanly(self, tmp_path):
        cp = subprocess.run([sys.executable, GENERATOR, '--overlay', OVERLAY, '--assembled', str(tmp_path),
                             '--source', OVERLAY, '--output', str(tmp_path)], capture_output=True, text=True)
        assert cp.returncode == 1 and cp.stderr == ''
        assert f'FAIL --output {tmp_path}: is a directory' in cp.stdout and 'RESULT: FAIL' in cp.stdout


class TestPolicy:

    def test_ionisation_must_map_to_an_ionisation(self):
        shape = gen.expected_shape({'family': 'ionization', 'reverse': False})
        assert gen.shape_matches(gen.parse_reaction('Ar + e- => Arp + e- + e-'), shape)
        assert not gen.shape_matches(gen.parse_reaction('Ar + e- => Ars + e-'), shape)

    def test_reversible_collision_maps_to_a_reversible_reaction(self):
        shape = gen.expected_shape({'family': 'excitation into 4s', 'reverse': True})
        assert gen.shape_matches(gen.parse_reaction('Ars + e- <=> Ar(1s4) + e-'), shape)
        assert not gen.shape_matches(gen.parse_reaction('Ars + e- => Ar(1s4) + e-'), shape)

    def test_free_text_is_not_a_reaction(self):
        assert gen.parse_reaction('Ars + e- <=> Ar(1s2) + e-  (1s3 <-> 1s2)') is None
        assert gen.parse_reaction('internal to Ars') is None

    def test_species_must_be_the_states(self):
        species, _ = gen.library_species(DATABASE, gen.LIBRARY)
        paschen = {'Ar(3P1)': '1s4', 'Ar(1P1)': '1s2'}
        assert gen.species_problem('Ar(3P2)', 'Ars', species, paschen) is None
        assert gen.species_problem('Ar(3P1)', 'Ar(1s4)', species, paschen) is None
        assert 'multiplicity 3, the LS term 1' in gen.species_problem('Ar(1P1)', 'Ars', species, paschen)
        assert 'named Ar(1s4)' in gen.species_problem('Ar(3P1)', 'Xe', species, paschen)
        assert 'charge' in gen.species_problem('Ar(+,gnd)', 'Ar', species, paschen)


@needs_store
class TestAgainstTheStore:

    def test_regeneration_equals_the_committed_map(self):
        text, problems, _, labels = gen.generate(OVERLAY, ASSEMBLED, SOURCES, DATABASE)
        assert problems == []
        assert len(labels) == 157
        assert text == open(MAP, encoding='utf-8').read()

    def test_checker_passes(self):
        cmd = [sys.executable, os.path.join(SCRIPTS, 'check_eedf_channel_map.py'), MAP, '--overlay', OVERLAY,
               '--assembled', ASSEMBLED] + [x for s in SOURCES for x in ('--source', s)]
        for extra in ([], ['--loki-rates', RATES] if RATES else None):
            if extra is None:
                continue
            cp = subprocess.run(cmd + extra, capture_output=True, text=True)
            assert cp.returncode == 0 and 'RESULT: PASS' in cp.stdout, cp.stdout[-2000:]
            assert cp.stderr == ''

    @pytest.fixture(scope='class')
    def manifest_and_derived(self):
        """The store's manifest document and the manifest the files give, captured from one generation."""
        captured, reconcile = [], gen.reconcile_manifest

        def capture(manifest, derived):
            captured.append(derived)
            return reconcile(manifest, derived)
        gen.reconcile_manifest = capture
        try:
            _, problems, _, _ = gen.generate(OVERLAY, ASSEMBLED, SOURCES, DATABASE)
        finally:
            gen.reconcile_manifest = reconcile
        assert problems == [] and len(captured) == 1
        doc, repeated = gen.decode_manifest(open(os.path.join(ASSEMBLED, gen.MANIFEST), 'rb').read())
        assert repeated == []
        return doc, captured[0]

    @pytest.mark.parametrize('name, old, new, reason', mutations.DUPLICATE_MEMBERS)
    def test_a_member_declared_twice_is_refused(self, tmp_path, name, old, new, reason):
        """The manifest's text, not its dictionary, declares one member twice: loading, generating and checking
        each refuse it, whichever declaration is stale."""
        store = tmp_path / 'store'
        shutil.copytree(ASSEMBLED, store)
        mutations.manifest_text(old, new)(str(store))
        _, problems = gen.store_manifest(str(store))
        assert problems == [f'the store manifest {gen.MANIFEST}: {reason}; each member may be declared once']
        _, problems, _, _ = gen.generate(OVERLAY, str(store), SOURCES, DATABASE)
        assert problems[0] == f'the store manifest {gen.MANIFEST}: {reason}; each member may be declared once'
        cmd = [sys.executable, os.path.join(SCRIPTS, 'check_eedf_channel_map.py'), MAP, '--overlay', OVERLAY,
               '--assembled', str(store)] + [x for s in SOURCES for x in ('--source', s)]
        cp = subprocess.run(cmd, capture_output=True, text=True)
        assert cp.returncode == 1 and cp.stderr == '' and f'FAIL the store manifest {gen.MANIFEST}: {reason}' in cp.stdout

    @staticmethod
    def manifest_edits(doc):
        """(field path, prose?, value) for every field of the catalogues, the sources and the top level, and of
        three process records and one not-assembled record: each leaf as it is, so it can be changed in turn."""
        def walk(node, path):
            if isinstance(node, dict):
                for k, v in node.items():
                    yield from walk(v, path + (k,))
            else:
                yield path, path[-1] in ('local_only', 'choice_reason', 'reason') or path[:1] == ('conventions',), node
        for key, value in doc.items():
            if key == 'processes':
                for i in (0, 1, 43):
                    yield from walk(value[i], (key, i))
            elif key == 'not_assembled':
                yield from walk(value[0], (key, 0))
            else:
                yield from walk(value, (key,))

    @staticmethod
    def manifest_problems(doc, derived, path, value):
        import copy
        doc = copy.deepcopy(doc)
        node = doc
        for k in path[:-1]:
            node = node[k]
        if value is mutations.DROP:
            del node[path[-1]]
        else:
            node[path[-1]] = value
        manifest, problems = gen.read_manifest(doc)
        return problems + gen.reconcile_manifest(manifest, derived)

    def test_every_manifest_field_is_derived_from_the_files(self, manifest_and_derived):
        """Each declared field changed in turn, dropped, or joined by an extra one is refused; prose may be
        reworded and a path may name another folder."""
        doc, derived = manifest_and_derived
        assert self.manifest_problems(doc, derived, ('set',), doc['set']) == []
        changed = 0
        for path, prose, value in self.manifest_edits(doc):
            if prose:
                assert self.manifest_problems(doc, derived, path, value + ' (reworded)') == [], path
                assert self.manifest_problems(doc, derived, path, None), path
                assert self.manifest_problems(doc, derived, path, mutations.DROP), path
                continue
            if path[-1] == 'path':
                assert self.manifest_problems(doc, derived, path, '/elsewhere/' + os.path.basename(value)) == [], path
            other = (not value if isinstance(value, bool) else value + 1 if isinstance(value, (int, float))
                     else value + 'x' if isinstance(value, str) else value[:-1] if value else [1])
            assert self.manifest_problems(doc, derived, path, other), (path, other)
            assert self.manifest_problems(doc, derived, path, mutations.DROP), path
            changed += 1
        assert changed > 60
        for path in [(), ('sources', 'IST'), ('processes', 0), ('processes', 0, 'source'), ('not_assembled', 0),
                     ('statistical_weights',), ('paschen',), ('conventions',)]:
            assert self.manifest_problems(doc, derived, path + ('extra_field',), 1), path

    def test_a_source_left_out_is_refused_at_generation(self):
        kept = [s for s in SOURCES if os.path.basename(s) != 'NGFSRDW_Ar_excited.txt']
        assert len(kept) == len(SOURCES) - 1
        _, problems, _, _ = gen.generate(OVERLAY, ASSEMBLED, kept, DATABASE)
        assert problems == [f"source NGFSRDW (NGFSRDW_Ar_excited.txt, SHA-256 d557bdc6c727...) named by the store's "
                            f"manifest was not given (--source)"]

    def test_a_source_under_another_sources_name_keeps_its_identity(self, tmp_path):
        """NGFSRDW's file given from another folder under TRINITI's name still regenerates the committed map."""
        sources = mutations.same_basename(str(tmp_path), SOURCES)
        assert sorted(os.path.basename(s) for s in sources).count('TRINITI_Ar.txt') == 2
        text, problems, _, _ = gen.generate(OVERLAY, ASSEMBLED, sources, DATABASE)
        assert problems == [] and text == open(MAP, encoding='utf-8').read()

    def test_a_collision_file_left_out_is_refused_at_generation(self, tmp_path):
        store = tmp_path / 'store'
        shutil.copytree(ASSEMBLED, store)
        os.remove(store / mutations.ASSEMBLED)
        overlay, doc = yaml.safe_load(open(OVERLAY)), yaml.safe_load(open(MAP))
        path = tmp_path / 'overlay.yaml'
        path.write_text(yaml.safe_dump(mutations.trimmed_overlay(overlay, doc), sort_keys=False))
        _, problems, _, labels = gen.generate(str(path), str(store), SOURCES, DATABASE)
        assert len(labels) == 39
        assert problems[0] == (f"collision file {mutations.ASSEMBLED} named by the store's manifest is not in the "
                               f"assembled directory")

    def test_a_directory_as_output_is_refused_after_a_clean_derivation(self, tmp_path):
        cmd = [sys.executable, GENERATOR, '--overlay', OVERLAY, '--assembled', ASSEMBLED, '--output', str(tmp_path)]
        cp = subprocess.run(cmd + [x for s in SOURCES for x in ('--source', s)], capture_output=True, text=True)
        assert cp.returncode == 1 and cp.stderr == ''
        assert cp.stdout.splitlines()[-2:] == [f'FAIL --output {tmp_path}: is a directory, not a file',
                                               'RESULT: FAIL (1 problems; nothing written)']

    def test_every_mutation_is_refused_for_its_reason(self):
        cmd = [sys.executable, os.path.join(SCRIPTS, 'test_eedf_channel_map_mutations.py'), MAP, '--overlay', OVERLAY,
               '--assembled', ASSEMBLED] + [x for s in SOURCES for x in ('--source', s)]
        if RATES:
            cmd += ['--loki-rates', RATES]
        cp = subprocess.run(cmd, capture_output=True, text=True)
        assert cp.returncode == 0, cp.stdout[-4000:]
        assert cp.stderr == ''
