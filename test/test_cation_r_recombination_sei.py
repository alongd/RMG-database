#!/usr/bin/env python
# encoding: utf-8

"""
``Cation_R_Recombination`` is a lithium-ion-battery SEI family, not a plasma family.

These tests pin that reclassification and the two *separate* limitations that follow
from it, so neither can be undone by accident:

* **plasma-domain exclusion** - the family must not be selected by a plasma workflow,
  and a plasma workflow that reaches one of its ``Marcus`` rates must fail explicitly
  or be excluded by declared configuration. Never silently evaluate at a default
  potential.
* **incomplete provenance** - the physical domain is recovered; the rates are not
  reproducible. Four facts remain unresolved, so the family is labelled
  ``LEGACY SEI ELECTROCHEMISTRY -- INCOMPLETE QUANTITATIVE PROVENANCE`` and is not
  labelled validated, *including* for SEI use.

Three rules the assertions follow, all deliberate:

* **Assert on behaviour, not only on text.** A label in a docstring is undone by an
  edit nobody notices. So the configuration tests actually load families and actually
  generate reactions, and the science test recomputes a fingerprint of all twelve
  database objects from the loaded data rather than diffing a file.
* **Every branch asserts.** The quarantine *gate* lives in RMG-Py and is not present
  in every plasma runtime. Where it is present these tests exercise it and require a
  refusal; where it is absent they require the declared-configuration exclusion that
  substitutes for it, plus the manifest that documents the substitution. Neither
  branch skips, because a skip here is indistinguishable from a pass.
* **Fail, never skip, when the database is not this worktree.** ``settings`` is
  pinned to this checkout at import time rather than read from an ``rmgrc`` that
  resolves silently to a shared database.

Run against a pinned runtime, from anywhere::

    conda activate rmg_env
    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
      python -m pytest test/test_cation_r_recombination_sei.py -v

The evidence base is ``docs/i103-electrochemical-provenance.md`` on branch
``i103-electrochem-provenance``; the reclassification report is
``docs/i111-sei-reclassification.md``; the documentation that sits beside the data is
``input/kinetics/families/Cation_R_Recombination/PROVENANCE.md``.
"""

import hashlib
import importlib
import os
import re
import subprocess

import pytest
import yaml

import rmgpy
from rmgpy import settings

FAMILY = 'Cation_R_Recombination'

#: The provenance label, verbatim. Changing this string is changing the claim.
LABEL = "LEGACY SEI ELECTROCHEMISTRY — INCOMPLETE QUANTITATIVE PROVENANCE"

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
THIS_DATABASE = os.path.join(REPO, 'input')
FAMILIES_DIR = os.path.join(THIS_DATABASE, 'kinetics', 'families')
FAMILY_DIR = os.path.join(FAMILIES_DIR, FAMILY)

# Pin before anything imports a database. RMG's rmgrc resolution ends in a bare
# `return`, so an absent rmgrc silently yields the shared checkout and every
# interesting assertion below would then be made against someone else's data.
settings['database.directory'] = THIS_DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.species import Species  # noqa: E402

RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(rmgpy.__file__)))

ADJLISTS = {
    'Lip': '1 Li u0 p0 c+1',
    'CH3': """
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    'NH2': """
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
}

#: SHA-256 over a canonical rendering of every scientific value this family carries -
#: all seven rate rules and all five training entries (kinetics class, A, n, the four
#: lmbd_i coefficients, beta, wr, wp, lmbd_o, rank), each training entry's reaction
#: equation as stored, and the family's own recipe, electron count, reversibility and
#: template arity. Recomputed from the loaded database on every run, so it pins the
#: *data*, not a file's bytes: reformat the files freely, change a number and this
#: fails. Recorded 2026-08-25 at base fb3c13c60, identical under both the RMG-Py-plasma
#: and RMG-Py-i102-quarantine runtimes.
SCIENCE_DIGEST = '0a77f301dc81b60c13b64caa9d009e08c08121712b1cd677d48b905e21aa0a34'

#: The genealogy: each rate rule, and the training entries whose lmbd_i coefficients
#: it is the arithmetic mean of. Twelve database objects, five underlying
#: calculations - the seven rules introduce no information the five do not contain.
GENEALOGY = {
    'Root': ['NH2 + Li <=> NH2Li', 'C2H5 + Li <=> C2H5Li', 'CH3 + Li <=> CH3Li',
             'CH3NH + Li <=> CH3NHLi', 'SH + Li <=> SHLi'],
    'Root_2R->C': ['C2H5 + Li <=> C2H5Li', 'CH3 + Li <=> CH3Li'],
    'Root_N-2R->C': ['NH2 + Li <=> NH2Li', 'CH3NH + Li <=> CH3NHLi', 'SH + Li <=> SHLi'],
    'Root_2R->C_Ext-2C-R': ['C2H5 + Li <=> C2H5Li'],
    'Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R': ['CH3NH + Li <=> CH3NHLi'],
    'Root_N-2R->C_2BrClFHILiNOPSSi->S': ['SH + Li <=> SHLi'],
    'Root_N-2R->C_N-2BrClFHILiNOPSSi->S': ['NH2 + Li <=> NH2Li'],
}


# ---------------------------------------------------------------------------
# helpers and fixtures
# ---------------------------------------------------------------------------

def _species(name):
    return Species(label=name).from_adjacency_list(ADJLISTS[name])


def _read(*parts):
    with open(os.path.join(*parts), encoding='utf-8') as handle:
        return handle.read()


def _exec_data_file(path):
    """Execute a declarative database file the way RMG does, builtins stripped."""
    context = {'__builtins__': None}
    exec(compile(_read(path), path, 'exec'), {'__builtins__': None}, context)
    return context


@pytest.fixture(scope='module')
def manifest():
    """The quarantine/classification manifest beside the family."""
    return _exec_data_file(os.path.join(FAMILY_DIR, 'quarantine.py'))


@pytest.fixture(scope='module')
def recommended():
    """Every curated family set this database offers."""
    context = _exec_data_file(os.path.join(FAMILIES_DIR, 'recommended.py'))
    return {name: value for name, value in context.items() if isinstance(value, set)}


@pytest.fixture(scope='module')
def sei_family():
    """The family loaded as the electrochemical/SEI configuration loads it."""
    assert settings['database.directory'] == THIS_DATABASE
    db = KineticsDatabase()
    db.load_families(FAMILIES_DIR, families=[FAMILY], depositories=['training'])
    # No add_rules_from_training / fill_rules_by_averaging_up: this is an
    # autoGenerated family, its rules.py is already the fitted tree, and calling
    # them would be a no-op that fabricates rules on a family that has them.
    return db, db.families[FAMILY]


def _entries(family):
    """The twelve database objects, as (kind, entry) pairs, computed from the data."""
    pairs = [('rule', entry)
             for entries in family.rules.entries.values() for entry in entries]
    for depository in family.depositories:
        if depository.label.endswith('/training'):
            pairs.extend(('training', entry) for entry in depository.entries.values())
    return pairs


def _quarantine_module():
    """The RMG-Py quarantine loader, or None when this runtime does not carry it."""
    try:
        return importlib.import_module('rmgpy.data.kinetics.quarantine')
    except ImportError:
        return None


# ---------------------------------------------------------------------------
# the reclassification itself
# ---------------------------------------------------------------------------

def test_label_is_recorded_verbatim_everywhere_it_is_claimed(manifest):
    """The label is a fixed string; a paraphrase of it is not the label.

    Four places carry it, and each is somewhere a different reader looks: the
    machine-readable manifest, the family's own description that RMG renders, the
    documentation beside the data, and the curated set the family belongs to.
    """
    assert manifest['classification'] == LABEL

    groups = _read(FAMILY_DIR, 'groups.py')
    assert LABEL in groups, 'the family shortDesc/longDesc must carry the label verbatim'
    assert groups.count(LABEL) == 2, 'both shortDesc and longDesc carry it'

    assert LABEL in _read(FAMILY_DIR, 'PROVENANCE.md')

    # recommended.py is ASCII-only by convention, so it carries the ASCII form.
    assert 'LEGACY SEI ELECTROCHEMISTRY -- INCOMPLETE QUANTITATIVE PROVENANCE' in \
        _read(FAMILIES_DIR, 'recommended.py')


def test_the_family_is_not_labelled_validated(manifest):
    """Not validated - and the label says so about SEI use too, not only plasma use."""
    assert 'incomplete quantitative provenance' in manifest['classification'].lower()
    assert 'validated' not in manifest['classification'].lower()
    assert 'validated' not in manifest['domain'].lower()

    provenance = _read(FAMILY_DIR, 'PROVENANCE.md')
    assert 'and that holds for SEI use' in provenance, (
        'the provenance limitation must be stated as applying inside the SEI domain, '
        'not only to plasma consumers'
    )
    # Every occurrence of "validated" in the family directory must be a denial of it.
    for filename in ('PROVENANCE.md', 'groups.py', 'quarantine.py'):
        text = _read(FAMILY_DIR, filename)
        for match in re.finditer(r'validated', text, re.I):
            window = text[max(0, match.start() - 40):match.start()].lower()
            assert 'not' in window, (
                '{0} uses "validated" without denying it: ...{1}'.format(
                    filename, text[max(0, match.start() - 60):match.end() + 20]))


def test_the_family_is_declared_electrochemistry_and_not_plasma(manifest):
    """Stated positively, so nobody has to infer it from an absence."""
    assert manifest['isPlasmaFamily'] is False
    assert 'sei' in manifest['domain'].lower()
    assert 'electrochem' in manifest['domain'].lower()
    assert manifest['familySets'] == ['electrochem']


def test_the_recovered_physical_domain_is_documented_beside_the_family():
    """Every item the reclassification is required to record, in the family directory.

    Not in a report somewhere else: beside the data, where someone inspecting the
    family will actually be standing.
    """
    provenance = _read(FAMILY_DIR, 'PROVENANCE.md')
    required = {
        'original physical domain': 'solid-electrolyte-interphase',
        'the surviving example input': 'examples/rmg/SEI_pure_EC/input.py',
        'reactor type': 'liquidSurfaceReactor',
        'solvent': 'ethylene carbonate',
        'temperature': '298.15 K',
        'electrode': 'Li110',
        'declared potentials': "liqPotential = (-1.0,'V')",
        'the reference convention': 'computationalLithiumElectrode',
        'the reference gap': '502',
        'the original Julia rate law': 'evalpoly(T,arr.lmbd_i_coefs)',
        'source reference': '10.1021/acsomega.7b01425',
        'historical commit': 'b23abeb0c',
        'author attribution': 'Matt Johnson',
        'the shared prefactor': '1.73e6',
        'the plasma prohibition': 'must not be used in a plasma mechanism',
        'the evidence path': 'docs/i103-electrochemical-provenance.md',
        'the evidence hash': 'd6d2e6511c2549d24e369eb13e51b6dae0ef3c6ff53fd19c1e25184c7bc132c2',
    }
    missing = sorted(name for name, needle in required.items() if needle not in provenance)
    assert not missing, 'PROVENANCE.md does not record: {0}'.format(missing)


def test_twelve_database_objects_rest_on_five_calculations(sei_family):
    """The genealogy, recomputed rather than asserted.

    Seven rate rules plus five training entries is twelve objects. Each rule's
    lmbd_i coefficients are reproduced here as the arithmetic mean of the training
    entries it was fitted from, so the claim "the seven rules introduce no
    information the five do not already contain" is checked, not quoted.
    """
    _, family = sei_family
    pairs = _entries(family)
    assert len([k for k, _ in pairs if k == 'rule']) == 7
    assert len([k for k, _ in pairs if k == 'training']) == 5
    assert len(pairs) == 12

    training = {entry.label: entry for kind, entry in pairs if kind == 'training'}
    rules = {entry.label: entry for kind, entry in pairs if kind == 'rule'}
    assert set(training) == set(GENEALOGY['Root']), 'the five calculations'
    assert set(rules) == set(GENEALOGY), 'the seven rules'

    for rule_label, sources in GENEALOGY.items():
        stored = list(rules[rule_label].data.lmbd_i_coefs.value_si)
        for i, coefficient in enumerate(stored):
            mean = sum(training[s].data.lmbd_i_coefs.value_si[i] for s in sources) / len(sources)
            # Single-source rules are bit-exact copies; multi-source rules carry the
            # rounding of six significant figures in the stored decimals.
            tolerance = 0.0 if len(sources) == 1 else 1e-4
            assert abs(coefficient - mean) <= tolerance * max(abs(mean), 1e-12), (
                'rule {0!r} coefficient {1} is {2!r}, not the mean {3!r} of {4}'.format(
                    rule_label, i, coefficient, mean, sources))

    # A and n carry no genealogical information: identical across all twelve.
    assert {float(entry.data.A.value_si) for _, entry in pairs} == {1.73e6}
    assert {float(entry.data.n.value_si) for _, entry in pairs} == {2.0}


# ---------------------------------------------------------------------------
# 1 - the alkali-plasma configuration does not load or generate from this family
# ---------------------------------------------------------------------------

def test_the_family_belongs_to_no_plasma_facing_curated_set(recommended):
    """Declared configuration: `electrochem` and nothing else.

    This is what a plasma deck that selects families *by set* runs into. It is also
    the whole of the exclusion in a runtime with no quarantine gate, which is why it
    is asserted against every other set rather than just checked once.
    """
    holders = sorted(name for name, families in recommended.items() if FAMILY in families)
    assert holders == ['electrochem'], (
        '{0} is in curated set(s) {1}; it must be in `electrochem` only'.format(FAMILY, holders))

    others = set()
    for name, families in recommended.items():
        if name != 'electrochem':
            others |= families
    assert FAMILY not in others


def test_the_alkali_plasma_configuration_neither_loads_nor_generates_this_family():
    """Load an alkali-plasma selection and try to make the family fire anyway.

    The selection is the lithium chemistry an alkali-plasma model legitimately wants
    - the four neutral ``Li_*`` families - plus ``Plasma_Electron_Attachment``, the
    one genuinely plasma family this database holds. The family under test is not in
    it, and the reaction it would contribute (Li+ + .CH3 -> CH3Li) is not generated
    by anything that is.
    """
    alkali_plasma = ['Li_Abstraction', 'Li_Addition_MultipleBond',
                     'Li_NO_Substitution', 'Li_NO_Ring_Opening',
                     'Plasma_Electron_Attachment']
    assert FAMILY not in alkali_plasma

    db = KineticsDatabase()
    db.load_families(FAMILIES_DIR, families=alkali_plasma, depositories=['training'])
    assert FAMILY not in db.families
    assert sorted(db.families) == sorted(alkali_plasma)

    for radical in ('CH3', 'NH2'):
        reactions = db.generate_reactions_from_families(
            [_species('Lip'), _species(radical)], products=None)
        assert reactions == [], (
            'the alkali-plasma configuration generated {0} reaction(s) from Li+ + {1}: '
            '{2}'.format(len(reactions), radical, [str(r) for r in reactions]))


# ---------------------------------------------------------------------------
# 2 - no plasma mechanism silently receives one of these Marcus rates
# ---------------------------------------------------------------------------

def test_the_quarantine_criterion_covers_all_twelve_objects(sei_family, manifest):
    """The gate's criterion is evaluated against the data, and it catches everything.

    The manifest names a kinetics *class*, never an entry, so this recomputes the
    affected set the way the loader does. Twelve of twelve: there is no non-Marcus
    path through this family for a plasma consumer to slip down.
    """
    _, family = sei_family
    assert manifest['appliesToKineticsClass'] == 'Marcus'
    assert manifest['state'] == 'QUARANTINED FOR QUANTITATIVE PLASMA USE'

    kinetics_class = getattr(rmgpy.kinetics, manifest['appliesToKineticsClass'], None)
    assert isinstance(kinetics_class, type), 'the manifest must name a real kinetics class'

    pairs = _entries(family)
    covered = [entry.label for _, entry in pairs if isinstance(entry.data, kinetics_class)]
    assert len(covered) == len(pairs) == 12, (
        'the quarantine criterion covers {0} of {1} objects; uncovered: {2}'.format(
            len(covered), len(pairs),
            sorted({e.label for _, e in pairs} - set(covered))))


def test_a_plasma_consumer_cannot_silently_receive_a_marcus_rate(sei_family):
    """Either the runtime refuses explicitly, or configuration keeps it out of reach.

    Both branches assert. The refusal branch runs the *same* callable RMG's three
    model boundaries call (kinetics estimation, core admission, edge admission), on a
    reaction generated from this database with its real Marcus kinetics attached. The
    no-gate branch requires the declared-configuration exclusion plus a manifest that
    says the gate is absent, because an undocumented absence is exactly the silent
    evaluation this test exists to forbid.
    """
    db, family = sei_family
    reactions = db.generate_reactions_from_families(
        [_species('Lip'), _species('CH3')], products=None, only_families=[FAMILY])
    assert len(reactions) == 1, [str(r) for r in reactions]
    reaction = reactions[0]
    kinetics, source, entry, _forward = family.get_kinetics(
        reaction, reaction.template, degeneracy=reaction.degeneracy)[0]
    assert type(kinetics).__name__ == 'Marcus'

    quarantine = _quarantine_module()
    if quarantine is not None:
        from rmgpy.exceptions import QuarantinedKineticsError
        assert family.quarantine is not None, (
            'this runtime carries the quarantine loader but the family loaded without a '
            'manifest - the sidecar is not being read')
        with pytest.raises(QuarantinedKineticsError) as raised:
            quarantine.check_quarantine(
                reaction, stage='admission to the model core', family=family,
                kinetics=kinetics, source=source, entry=entry)
        message = str(raised.value)
        assert 'QUARANTINED FOR QUANTITATIVE PLASMA USE' in message
        assert FAMILY in message
        assert 'Marcus' in message
        # The refusal must not offer any of the quiet substitutions.
        assert 'not being dropped, averaged, zeroed, reversed' in message
    else:
        # No gate in this runtime. The exclusion is then entirely declared
        # configuration, and it must be real and documented as the substitute.
        context = _exec_data_file(os.path.join(FAMILIES_DIR, 'recommended.py'))
        sets = {n: v for n, v in context.items() if isinstance(v, set)}
        assert sorted(n for n, v in sets.items() if FAMILY in v) == ['electrochem']
        manifest_text = _read(FAMILY_DIR, 'quarantine.py')
        assert 'NOT present in every plasma' in manifest_text, (
            'the manifest must record that the gate can be absent, or its absence is '
            'silent - which is the failure mode being excluded')
        assert 'declared configuration' in manifest_text


def test_no_default_potential_is_used_anywhere_in_this_reclassification():
    """The forbidden repairs, forbidden in writing where the next reader will look."""
    provenance = _read(FAMILY_DIR, 'PROVENANCE.md')
    for forbidden in ('Do not choose between the two Li',
                      'Do not infer the association contribution',
                      'Do not fit a potential offset',
                      '4.44 V',
                      'Do not refit'):
        assert forbidden in provenance, forbidden
    # Nothing in this ticket may introduce a potential value into the family data.
    for filename in ('rules.py', 'groups.py'):
        text = _read(FAMILY_DIR, filename)
        assert 'V0' not in text
        assert '4.44' not in text


# ---------------------------------------------------------------------------
# 3 - the exclusion did not take the real lithium-plasma chemistry with it
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('filename,label,expected_n', [
    ('voronov.yaml', 'electron-impact ionisation', {1, 2, 3}),
    ('badnell.yaml', 'radiative recombination', {0, 1, 2}),
])
def test_the_independent_lithium_plasma_kinetics_survive(filename, label, expected_n):
    """This is the check that proves the exclusion did not remove real chemistry.

    Voronov (electron-impact ionisation) and Badnell (radiative recombination) are
    where lithium plasma kinetics actually live in this database. They are unrelated
    to the SEI family and must be untouched by its exclusion - including Li at Z = 3,
    which is the entry an alkali-plasma model needs.
    """
    path = os.path.join(THIS_DATABASE, 'kinetics', filename)
    assert os.path.exists(path), '{0} ({1}) is missing'.format(filename, label)
    with open(path, encoding='utf-8') as handle:
        data = yaml.safe_load(handle)

    lithium = [block for block in data['coefficients'] if block['Z'] == 3]
    assert len(lithium) == 1, 'exactly one Z = 3 (lithium) block'
    entries = lithium[0]['entries']
    assert {entry['N'] for entry in entries} == expected_n
    for entry in entries:
        assert isinstance(entry['A'], float) and entry['A'] > 0.0


def test_the_lithium_plasma_data_files_are_untouched_by_this_ticket():
    """Byte-level: neither yaml was edited while excluding the SEI family.

    Compared against the ticket's base commit rather than against a literal digest,
    so this keeps meaning the same thing if the files legitimately change later on a
    different ticket - it pins *this* ticket's blast radius, not the files forever.
    """
    for filename in ('voronov.yaml', 'badnell.yaml'):
        relative = os.path.join('input', 'kinetics', filename)
        diff = subprocess.run(
            ['git', '-C', REPO, 'diff', '--stat', 'fb3c13c60', '--', relative],
            capture_output=True, text=True, check=True)
        assert diff.stdout.strip() == '', (
            '{0} changed since the ticket base fb3c13c60:\n{1}'.format(relative, diff.stdout))


# ---------------------------------------------------------------------------
# 4 - the historical SEI example still identifies the family
# ---------------------------------------------------------------------------

def test_the_sei_example_still_selects_this_family_through_electrochem(recommended):
    """The example the family was written for keeps working, under its own domain.

    ``examples/rmg/SEI_pure_EC/input.py`` selects families by *set*, naming
    ``electrochem``; resolving that set against this database still yields the family,
    and the family still generates its SEI reaction with Marcus kinetics attached. So
    the exclusion is domain-scoped, not a removal.
    """
    example = os.path.join(RUNTIME, 'examples', 'rmg', 'SEI_pure_EC', 'input.py')
    assert os.path.exists(example), (
        'the historical SEI example is not present in the pinned runtime {0}; the '
        'reclassification claims it as the surviving statement of the family\'s '
        'conditions, so its absence is a finding, not a skip'.format(RUNTIME))
    text = _read(example)

    selection = re.search(r'kineticsFamilies\s*=\s*\[(.*?)\]', text, re.S)
    assert selection, 'the example must select families explicitly'
    assert "'electrochem'" in selection.group(1)
    assert FAMILY not in selection.group(1), (
        'the example reaches the family through the `electrochem` set, not by name')
    assert FAMILY in recommended['electrochem']

    # The conditions the reclassification records are still the ones the example sets.
    assert "catalystProperties(" in text and "'Li110'" in text
    assert "liqPotential=(-1.0,'V')" in text
    assert "surfPotential=(0.0,'V')" in text
    assert "temperature=(298.15,'K')" in text
    assert "solvent='ethylene carbonate'" in text


def test_the_family_still_generates_its_sei_reaction(sei_family):
    """Under the electrochemical configuration the data are fully intact and usable.

    Nothing was deleted, pruned or neutered: this is the positive control for every
    exclusion above.
    """
    db, family = sei_family
    reactions = db.generate_reactions_from_families(
        [_species('Lip'), _species('CH3')], products=None, only_families=[FAMILY])
    assert [str(r) for r in reactions] == ['[Li+] + [CH3] <=> [Li][CH3]']
    kinetics, source, entry, _forward = family.get_kinetics(
        reactions[0], reactions[0].template, degeneracy=reactions[0].degeneracy)[0]
    assert type(kinetics).__name__ == 'Marcus'
    assert getattr(source, 'label', '') == '{0}/training'.format(FAMILY)
    assert entry.label == 'CH3 + Li <=> CH3Li'
    assert family.electrons == -1
    assert family.reversible is True


# ---------------------------------------------------------------------------
# no science changed
# ---------------------------------------------------------------------------

def test_no_scientific_value_changed(sei_family):
    """Recompute every number this family carries and compare against a fixed digest.

    Covers all twelve objects - kinetics class, A, n, the four lmbd_i coefficients,
    beta, wr, wp, lmbd_o, rank - plus each training entry's reaction equation as
    stored and the family's recipe, electron count, reversibility and template arity.
    Reformatting the files cannot move it; changing a value, an orientation, a class
    or the recipe must.
    """
    _, family = sei_family

    def quantity(value):
        return 'None' if value is None else repr(round(float(value.value_si), 10))

    def fingerprint(kind, entry):
        data = entry.data
        return '|'.join([
            kind, entry.label, type(data).__name__,
            quantity(data.A), repr(round(float(data.n.value_si), 10)),
            ';'.join(repr(round(float(c), 12)) for c in data.lmbd_i_coefs.value_si),
            quantity(data.beta), quantity(data.wr), quantity(data.wp),
            quantity(data.lmbd_o), repr(entry.rank),
        ])

    lines = []
    for kind, entry in _entries(family):
        line = fingerprint(kind, entry)
        if kind == 'training':
            line += '|' + str(entry.item)
        lines.append(line)
    lines.append('|'.join([
        'family', family.label, str(family.electrons), str(family.reversible),
        str(family.own_reverse), str(family.reactant_num), str(family.product_num),
        str(family.allow_charged_species), repr(family.forward_recipe.actions),
        repr(family.forward_template.reactants[0].label),
    ]))
    lines.sort()

    digest = hashlib.sha256('\n'.join(lines).encode()).hexdigest()
    assert digest == SCIENCE_DIGEST, (
        'the scientific content of {0} changed.\n{1}'.format(FAMILY, '\n'.join(lines)))


def test_nothing_was_deleted_from_the_family():
    """Quarantine is a label plus a gate. The data are the provenance evidence."""
    for filename in ('groups.py', 'rules.py', 'quarantine.py', 'PROVENANCE.md'):
        assert os.path.exists(os.path.join(FAMILY_DIR, filename)), filename
    for filename in ('reactions.py', 'dictionary.txt'):
        assert os.path.exists(os.path.join(FAMILY_DIR, 'training', filename)), filename
    assert _read(FAMILY_DIR, 'rules.py').count('entry(') == 7
    assert _read(FAMILY_DIR, 'training', 'reactions.py').count('entry(') == 5


def test_the_family_identifier_was_not_renamed(sei_family):
    """A rename needs a reference audit this ticket does not fund."""
    _, family = sei_family
    assert family.label == FAMILY
    assert os.path.isdir(FAMILY_DIR)
