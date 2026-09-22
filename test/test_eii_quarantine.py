#!/usr/bin/env python3
"""
``Plasma_Electron_Impact_Ionization`` is quarantined, and these tests pin the gate.

The defect is NOT in this database. A rate this family supplies as an estimate reaches
the solver as an ordinary ``Arrhenius``, which cannot carry ``uses_electron_temperature``,
so ``PlasmaReactor`` evaluates it at the GAS temperature: measured ~23.7 orders of
magnitude low at 1000 K for ``Ar(3P2) => Ar+``, and bit-identical when Te is tripled.
That is an RMG-Py hole and is somebody else's ticket. What this database can do is refuse
to let the resulting number into a quantitative mechanism, and the manifest at
``input/kinetics/families/Plasma_Electron_Impact_Ionization/quarantine.py`` is that
refusal.

Three rules the assertions follow, taken from ``test_cation_r_recombination_sei.py``:

* **Assert on behaviour, not on text.** A manifest is a data file; whether it gates
  anything is a property of the runtime. So these tests load the real database, generate
  the real reaction, and require a real exception out of the real admission path.
* **Every branch asserts, and a missing loader FAILS rather than skips.** Unlike
  ``Cation_R_Recombination``, this family has no declared-configuration fallback to stand
  in for the gate: it belongs to no set in ``input/kinetics/families/recommended.py``, so
  the only way to reach it is to name it, and a deck that names it under a runtime with no
  quarantine loader gets no protection at all. A skip there would be indistinguishable
  from a pass on precisely the case that matters.
* **Fail, never skip, when the database is not this worktree.** ``settings`` is pinned to
  this checkout at import time.

Run against a pinned runtime, from anywhere::

    conda activate rmg_env
    PYTHONPATH=/home/alon/Code/RMG-Py-i222-metastable-argon-atomtype \\
      python -m pytest test/test_eii_quarantine.py -v

The evidence is ``docs/argon-metastable-thermo/report.md`` (sections 13.1-13.3), the probe
is ``docs/argon-metastable-thermo/quarantine_probe.py``, and its captured streams are in
``docs/argon-metastable-thermo/logs/``.
"""

import importlib
import os

import pytest

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
THIS_DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, 'input'))
settings['database.directory'] = THIS_DATABASE

FAMILY = 'Plasma_Electron_Impact_Ionization'
SIBLING = 'Plasma_Radiative_Recombination'
FAMILY_DIR = os.path.join(THIS_DATABASE, 'kinetics', 'families', FAMILY)
MANIFEST = os.path.join(FAMILY_DIR, 'quarantine.py')

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'

#: The campaign state string, verbatim. Changing it is changing the claim, and it is the
#: string a user sees first in the refusal.
STATE = 'QUARANTINED FOR QUANTITATIVE PLASMA USE'

#: The criterion. Not 'Arrhenius' - see the test that measures why.
CRITERION = 'KineticsModel'


def _exec_data_file(path):
    """Execute a database data file the way RMG does, with builtins stripped."""
    local_context = {'__builtins__': None}
    with open(path, 'r') as f:
        exec(f.read(), {'__builtins__': None}, local_context)
    return local_context


@pytest.fixture(scope='module')
def manifest():
    return _exec_data_file(MANIFEST)


@pytest.fixture(scope='module')
def loaded():
    """The real database, this family and a sibling, with its one rule filled in."""
    from rmgpy.data.rmg import RMGDatabase

    db = RMGDatabase()
    db.load(THIS_DATABASE,
            thermo_libraries=['primaryThermoLibrary', 'PlasmaExcitedNeutralThermo',
                              'PlasmaCationThermo'],
            kinetics_families=[FAMILY, SIBLING],
            reaction_libraries=[], seed_mechanisms=[], solvation=True, surface=False)
    fam = db.kinetics.families[FAMILY]
    try:
        fam.add_rules_from_training(thermo_database=db.thermo)
    except Exception:                                            # noqa: BLE001
        pass
    fam.fill_rules_by_averaging_up(verbose=True)
    return db


def _generate(db):
    """This family's one reaction for Ar(3P2), with thermo attached to both sides."""
    from rmgpy.molecule import Molecule
    from rmgpy.species import Species

    spc = Species(label='Ar(3P2)',
                  molecule=[Molecule().from_adjacency_list(AR_META)])
    reactions = db.kinetics.generate_reactions_from_families(
        [spc], products=None, only_families=[FAMILY], resonance=True)
    assert len(reactions) == 1, 'expected one reaction, got %d' % len(reactions)
    rxn = reactions[0]
    for s in list(rxn.reactants) + list(rxn.products):
        if s.is_electron():
            continue
        if not s.label:
            s.label = str(s)
        s.thermo = db.thermo.get_thermo_data(s)
    return rxn


# ---- the manifest itself ------------------------------------------------------------

def test_the_manifest_sits_beside_the_data_it_describes():
    """A quarantine that lived anywhere but the family directory would be a second place
    to keep in step with the first."""
    assert os.path.isfile(MANIFEST), MANIFEST
    for sibling_file in ('groups.py', 'rules.py'):
        assert os.path.isfile(os.path.join(FAMILY_DIR, sibling_file))


def test_the_manifest_declares_the_state_the_criterion_and_a_reason(manifest):
    """The loader requires exactly these three fields and refuses a manifest missing any
    of them, because one that cannot say what it covers and why gates nothing."""
    assert manifest['state'] == STATE
    assert manifest['appliesToKineticsClass'] == CRITERION
    assert manifest['reason'], 'a quarantine without a reason is an unexplained refusal'
    assert 'gas temperature' in manifest['reason'].lower()


def test_the_manifest_names_its_own_lift_condition(manifest):
    """A quarantine with no stated exit is a permanent one by accident. Both conditions
    are engine-side or data-side facts, not judgements about convenience."""
    long_desc = manifest['longDesc']
    assert 'LIFTING THIS' in long_desc
    assert 'uses_electron_temperature' in long_desc
    assert 'Delete this file' in long_desc


def test_the_manifest_does_not_claim_the_family_is_misfiled(manifest):
    """Unlike the Cation_R_Recombination precedent, this IS a plasma family. The
    quarantine is about delivery, not about provenance or classification, and the manifest
    has to say so or the next reader will 'fix' it by refitting the rule."""
    assert manifest['isPlasmaFamily'] is True
    # Read the file rather than the executed namespace: this statement lives in the
    # manifest's comment block, which exec() does not carry into longDesc.
    with open(MANIFEST, 'r') as f:
        text = f.read()
    assert 'Provenance is not what is wrong here' in text
    assert 'no refit lifts this' in text


# ---- the criterion, against what the database actually holds ------------------------

def test_arrhenius_would_have_been_the_wrong_criterion(loaded):
    """Measured, and the reason the obvious criterion is a trap.

    The root rule is WRITTEN as an Arrhenius in rules.py and is an ArrheniusEP once
    loaded, and ArrheniusEP is not a subclass of Arrhenius - both derive straight from
    KineticsModel. So an 'Arrhenius' manifest would cover zero of the family's rules while
    looking correct in the file, and would catch the rate only after fix_barrier_height
    had converted it, downstream of the gate that actually fires."""
    from rmgpy.data.kinetics.quarantine import KineticsQuarantine
    from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsModel

    assert not issubclass(ArrheniusEP, Arrhenius)
    assert issubclass(ArrheniusEP, KineticsModel)

    fam = loaded.kinetics.families[FAMILY]
    rules = [e for entries in fam.rules.entries.values() for e in entries]
    assert rules, 'the family must hold at least one rule for this test to mean anything'
    assert all(isinstance(e.data, ArrheniusEP) for e in rules)

    as_written = KineticsQuarantine(FAMILY, STATE, 'Arrhenius', 'hypothetical', MANIFEST)
    assert as_written.affected_entries(fam)['rules'] == [], (
        'an Arrhenius criterion covers none of this family, which is the failure mode: '
        'a manifest that reads correctly and gates nothing'
    )


def test_the_criterion_covers_every_rule_the_family_can_estimate_from(loaded):
    """Computed from the loaded database rather than from a stored list, so adding a rule
    quarantines it automatically and renumbering changes nothing."""
    fam = loaded.kinetics.families[FAMILY]
    assert fam.quarantine is not None, (
        'the family loaded without its quarantine; either the manifest was removed or '
        'this runtime has no rmgpy/data/kinetics/quarantine.py'
    )
    rules = [e for entries in fam.rules.entries.values() for e in entries]
    affected = fam.quarantine.affected_entries(fam)
    assert len(affected['rules']) == len(rules) == 1
    assert affected['rules'][0].label == 'A_rad'
    assert affected['rules'][0].rank == 10


def test_the_criterion_resolves_to_a_real_class_at_load(loaded):
    """A name that does not resolve would report a quarantine that gates nothing, so the
    loader raises on it. Pinned because a silent no-op is the worst outcome here."""
    from rmgpy.kinetics import KineticsModel

    assert loaded.kinetics.families[FAMILY].quarantine.kinetics_class is KineticsModel


# ---- the gate ------------------------------------------------------------------------

def test_admission_refuses_the_reaction_this_family_generates_for_metastable_argon(loaded):
    """The whole point, end to end, through the path a real run uses."""
    from rmgpy.exceptions import QuarantinedKineticsError
    from rmgpy.rmg.model import CoreEdgeReactionModel

    rxn = _generate(loaded)
    cerm = CoreEdgeReactionModel()
    cerm.kinetics_estimator = 'rate rules'

    with pytest.raises(QuarantinedKineticsError) as excinfo:
        cerm.apply_kinetics_to_reaction(rxn)

    message = str(excinfo.value)
    for expected in (STATE, FAMILY, 'A_rad', 'ArrheniusEP', MANIFEST,
                     'kinetics estimation for the reaction model'):
        assert expected in message, 'the refusal does not name %r' % expected


def test_a_refused_reaction_is_left_exactly_as_generated(loaded):
    """The gate fires before reaction.kinetics is bound and before the direction flip, so
    nothing is half-applied. A refusal that mutated the reaction would leave a caller
    holding an object it could neither use nor trust."""
    from rmgpy.exceptions import QuarantinedKineticsError
    from rmgpy.rmg.model import CoreEdgeReactionModel

    rxn = _generate(loaded)
    before = (list(rxn.reactants), list(rxn.products), rxn.kinetics)
    cerm = CoreEdgeReactionModel()
    cerm.kinetics_estimator = 'rate rules'
    with pytest.raises(QuarantinedKineticsError):
        cerm.apply_kinetics_to_reaction(rxn)

    assert rxn.kinetics is None
    assert (list(rxn.reactants), list(rxn.products), rxn.kinetics) == before


def test_the_refusal_substitutes_nothing(loaded):
    """Named explicitly because every alternative to refusing - averaging, zeroing,
    dropping the reaction, marking it irreversible - lets a run report success on a
    mechanism that is quietly wrong."""
    from rmgpy.exceptions import QuarantinedKineticsError
    from rmgpy.rmg.model import CoreEdgeReactionModel

    rxn = _generate(loaded)
    cerm = CoreEdgeReactionModel()
    cerm.kinetics_estimator = 'rate rules'
    with pytest.raises(QuarantinedKineticsError) as excinfo:
        cerm.apply_kinetics_to_reaction(rxn)

    assert 'not being dropped, averaged, zeroed, reversed' in str(excinfo.value)
    assert rxn.kinetics is None
    assert rxn not in cerm.core.reactions
    assert rxn not in cerm.edge.reactions


def test_the_family_still_generates_and_still_loads(loaded):
    """The quarantine refuses admission to a quantitative model and nothing else. The data
    stays, the tree stays, and generation still works - that is what makes this different
    from deleting the rule."""
    from rmgpy.kinetics import ArrheniusEP

    fam = loaded.kinetics.families[FAMILY]
    rxn = _generate(loaded)
    assert str(rxn) == '[Ar] => [Ar+]'

    rules = [e for entries in fam.rules.entries.values() for e in entries]
    assert len(rules) == 1 and rules[0].label == 'A_rad'
    assert isinstance(rules[0].data, ArrheniusEP)
    # The rate law itself is untouched: a consumer outside a reaction model - an audit, a
    # refit, an Arkane job - still evaluates it on the same unmodified data.
    assert rules[0].data.A.value_si > 0.0


def test_a_sibling_family_without_a_manifest_is_untouched(loaded):
    """The quarantine is a property of one family. A database with no manifest anywhere
    must behave exactly as it did before, which is what makes the mechanism safe to ship."""
    from rmgpy.data.kinetics.quarantine import check_quarantine
    from rmgpy.kinetics import Arrhenius

    sib = loaded.kinetics.families[SIBLING]
    assert sib.quarantine is None

    rxn = _generate(loaded)
    assert check_quarantine(rxn, stage='test', family=sib,
                            kinetics=Arrhenius(A=(1.0, 'm^3/(mol*s)'), n=0.0,
                                               Ea=(0.0, 'kJ/mol'))) is None


# ---- what the gate does NOT cover ---------------------------------------------------

def test_this_family_is_in_no_recommended_set_so_the_gate_is_the_only_containment():
    """Cation_R_Recombination has a second line of defence: it sits only in the
    'electrochem' set, so a plasma deck selecting families by set never reaches it. This
    family sits in NO set, which means it is reached only by being named - and once named,
    the quarantine is the whole of the protection. If this test ever fails because the
    family was added to a set, the manifest's importance goes up, not down."""
    sets = _exec_data_file(
        os.path.join(THIS_DATABASE, 'kinetics', 'families', 'recommended.py'))
    carrying = [name for name, value in sets.items()
                if isinstance(value, (set, frozenset, list, tuple)) and FAMILY in value]
    assert carrying == [], 'now also reachable by set: %s' % carrying


def test_the_quarantine_loader_is_present_in_this_runtime():
    """Not a skip guard - an assertion. Where the loader is absent this manifest is an
    inert data file, and for THIS family nothing else stands in its place, so a runtime
    without it is a runtime in which the bad rate is admitted silently."""
    loader = importlib.util.find_spec('rmgpy.data.kinetics.quarantine')
    assert loader is not None, (
        'this RMG-Py has no rmgpy/data/kinetics/quarantine.py, so the quarantine does not '
        'fire and Plasma_Electron_Impact_Ionization has no other containment'
    )


def test_the_manifest_declares_the_engine_it_needs_and_this_runtime_satisfies_it():
    """Round 77. The quarantine is runtime-dependent and the database declared nothing
    about which runtime. A manifest that is silently inert on the wrong engine is worse
    than no manifest, because the file reads like protection.

    The manifest now carries a machine-readable pin. This asserts both halves: that the
    pin is there and complete, and that the engine actually running this test satisfies
    it. The second half is why this is an assertion and not a skip - a run against an
    engine without the gate must fail loudly, not quietly proceed unguarded."""
    manifest = _exec_data_file(
        os.path.join(THIS_DATABASE, 'kinetics', 'families', FAMILY, 'quarantine.py'))

    module_name = manifest.get('requiresEngineModule')
    symbol_name = manifest.get('requiresEngineSymbol')
    call_sites = manifest.get('requiresEngineCallSites')
    commit = manifest.get('recordedEngineCommit')
    assert module_name and symbol_name and call_sites and commit, (
        'the manifest must name the engine module, the symbol, the call site the symbol '
        'must be reached from, and the commit that first provided the gate, or a reader '
        'cannot tell which runtimes it is real on')

    # Round 87: the field that records the commit is `recordedEngineCommit`, and the name
    # is the point. Round 80 called it `requiresEngineCommit` and explained in a comment
    # that it was provenance -- but a reader greps the field name, and "requires" claims a
    # pin that cannot exist, because an installed engine has no commit to compare against.
    assert manifest.get('requiresEngineCommit') is None, (
        'requiresEngineCommit is unenforceable and no longer declarable; the engine '
        'refuses a manifest carrying it. Record the commit as recordedEngineCommit.')

    spec = importlib.util.find_spec(module_name)
    assert spec is not None, (
        'this runtime has no %s, which the manifest declares as required; the quarantine '
        'is inert here and this family has no other containment' % module_name)
    module = importlib.import_module(module_name)
    assert hasattr(module, symbol_name), (
        '%s exists but does not provide %s' % (module_name, symbol_name))
    assert callable(getattr(module, symbol_name)), (
        '%s.%s exists but is not callable, so it cannot be the gate this manifest '
        'depends on -- mere existence of an attribute proves nothing' % (
            module_name, symbol_name))

    # and the gate is wired in, not merely importable. Checked on SOURCE rather than on
    # instances, because constructing either takes a signature that has changed before and
    # would make this test fail for the wrong reason -- which it did, once, while being
    # written.
    #
    # Round 80 splits what round 77 ran together. TWO symbols matter and they sit in
    # different places, so one assertion could not cover both:
    #   * the LOADER, which reads this manifest at family load;
    #   * the GATE -- the symbol the manifest now declares -- which the reaction model
    #     calls at admission. It is the gate that makes the refusal real, so it is the one
    #     worth declaring; asserting it against KineticsFamily's source (as round 77 did)
    #     looks for it in the wrong file.
    import inspect

    from rmgpy.data.kinetics.family import KineticsFamily
    from rmgpy.rmg.model import CoreEdgeReactionModel

    family_source = inspect.getsource(KineticsFamily)
    assert 'self.quarantine' in family_source, (
        'KineticsFamily never sets a quarantine attribute, so a loaded manifest would '
        'never be consulted')
    assert 'load_family_quarantine' in family_source, (
        'KineticsFamily never loads a quarantine manifest, so this file is read by nothing')

    model_source = inspect.getsource(CoreEdgeReactionModel)
    assert symbol_name in model_source, (
        '%s is importable but the reaction model never calls it, so a loaded manifest '
        'would gate nothing at admission' % symbol_name)

    # Round 87 adds the binding check the source scan above cannot make: each declared
    # call site must hold the SAME object the manifest's module provides. A source scan
    # sees the name; this sees that the name resolves to the gate.
    for call_site in call_sites:
        site = importlib.import_module(call_site)
        assert getattr(site, symbol_name, None) is getattr(module, symbol_name), (
            '%s is declared as a call site for %s but does not bind it, so the gate is '
            'not reached from the path this manifest depends on' % (call_site, symbol_name))


def test_this_runtime_ENFORCES_the_declared_engine_requirement(tmp_path):
    """Round 80. Declaring a requirement is not pinning it: until the loader honoured
    these fields, an engine could read the manifest, ignore what it asked for, and gate
    nothing while the file still read as protection. The database's own tests confirmed
    only the runtime that happened to be selected to run them.

    So this asserts the ENFORCEMENT rather than the declaration: a manifest whose declared
    capability is absent must be REFUSED by this engine's loader. It is deliberately run
    on a synthetic manifest in a temporary directory -- pointing the real one at a missing
    module would be testing the check by breaking the thing it guards, in the tree.

    What it cannot cover, and what `bypassRoutes` therefore still enumerates: an engine
    with no quarantine loader at all never reads any manifest, so nothing here can refuse
    it."""
    from rmgpy.data.kinetics.quarantine import load_family_quarantine
    from rmgpy.exceptions import DatabaseError

    body = '\n'.join([
        'name = "Synthetic/quarantine"',
        'state = "QUARANTINED FOR TESTING"',
        'appliesToKineticsClass = "Arrhenius"',
        'reason = "a synthetic manifest used to check that requirements are enforced"',
        'requiresEngineModule = "rmgpy.data.kinetics.a_module_no_engine_provides"',
        '',
    ])
    path = os.path.join(str(tmp_path), 'quarantine.py')
    with open(path, 'w', encoding='utf-8') as handle:
        handle.write(body)

    with pytest.raises(DatabaseError) as exc:
        load_family_quarantine('Synthetic_Family', str(tmp_path))
    assert 'a_module_no_engine_provides' in str(exc.value), (
        'this engine loads a manifest without honouring the engine requirement it '
        'declares, so requiresEngineModule is a comment here and not a pin'
    )

    # positive control: the check must not refuse a requirement that IS satisfied, or the
    # assertion above would pass for the wrong reason on any engine at all.
    satisfied = body.replace('rmgpy.data.kinetics.a_module_no_engine_provides',
                             'rmgpy.data.kinetics.quarantine')
    with open(path, 'w', encoding='utf-8') as handle:
        handle.write(satisfied + 'requiresEngineSymbol = "check_quarantine"\n')
    assert load_family_quarantine('Synthetic_Family', str(tmp_path)) is not None


def test_this_runtime_ENFORCES_the_pin_as_more_than_an_attribute_lookup(tmp_path):
    """Round 87. Round 80's enforcement was real but weak, and this database's record said
    it was strong - twice. Review reproduced three holes: a symbol declared with no module
    was skipped without a word, ANY non-None attribute satisfied the symbol check (a
    manifest naming `math.pi` as its gate loaded clean), and nothing showed the gate was
    REACHED rather than merely present.

    Each hole gets a case below, and each case is a manifest this engine must refuse. The
    positive control in the test above is what keeps these from passing on an engine that
    simply refuses everything."""
    from rmgpy.data.kinetics.quarantine import load_family_quarantine
    from rmgpy.exceptions import DatabaseError

    base = '\n'.join([
        'name = "Synthetic/quarantine"',
        'state = "QUARANTINED FOR TESTING"',
        'appliesToKineticsClass = "Arrhenius"',
        'reason = "a synthetic manifest used to check that requirements are enforced"',
        '',
    ])
    path = os.path.join(str(tmp_path), 'quarantine.py')

    cases = [
        ('a gate that is not callable',
         'requiresEngineModule = "math"\nrequiresEngineSymbol = "pi"\n',
         'not callable'),
        ('a symbol with no module to look it up in',
         'requiresEngineSymbol = "check_quarantine"\n',
         'requiresEngineModule'),
        ('a gate that exists but is wired nowhere near admission',
         'requiresEngineModule = "rmgpy.data.kinetics.quarantine"\n'
         'requiresEngineSymbol = "check_quarantine"\n'
         'requiresEngineCallSites = ("os",)\n',
         'wired into'),
        ('a commit pin that could never fail',
         'requiresEngineModule = "rmgpy.data.kinetics.quarantine"\n'
         'requiresEngineSymbol = "check_quarantine"\n'
         'requiresEngineCommit = "0000000000000000000000000000000000000000"\n',
         'recordedEngineCommit'),
    ]

    for description, extra, expected in cases:
        with open(path, 'w', encoding='utf-8') as handle:
            handle.write(base + extra)
        with pytest.raises(DatabaseError) as exc:
            load_family_quarantine('Synthetic_Family', str(tmp_path))
        assert expected in str(exc.value), (
            'this engine accepts %s, so the pin is weaker than this database claims '
            'it is' % description)

    # positive control: the arrangement the real manifest declares must still load, or
    # every refusal above would be an engine that refuses everything.
    with open(path, 'w', encoding='utf-8') as handle:
        handle.write(base
                     + 'requiresEngineModule = "rmgpy.data.kinetics.quarantine"\n'
                       'requiresEngineSymbol = "check_quarantine"\n'
                       'requiresEngineCallSites = ("rmgpy.rmg.model",)\n'
                       'recordedEngineCommit = "541e6498f"\n')
    assert load_family_quarantine('Synthetic_Family', str(tmp_path)) is not None


def test_the_manifest_enumerates_the_routes_that_bypass_it():
    """The scope claim, asserted rather than left to a reader's optimism.

    Review's point: standard model admission refuses the family on the pinned engine, but
    a runtime lacking the loader, a direct database consumer, and an equivalent rate
    supplied through a reaction or seed library all bypass it. Those are properties of
    where the gate sits - at model admission, on one path - and the defect it guards is a
    property of the RATE, which travels wherever the number travels.

    A manifest that does not say so invites a green run to be read as a hard boundary. The
    routes are now enumerated in the file; this pins that they stay enumerated, because
    the bypasses are the part a future reader most needs and least expects.

    ROUND 87 MOVED ONE OF THESE EXPECTATIONS, DELIBERATELY. The list used to name 'seed
    mechanism' outright, on the reasoning that a rate copied into a library 'is not this
    family'. That wrote off a hole that turned out to be closable: the engine gate was
    keying on `reaction.family`, which LibraryReaction overwrites with the LIBRARY's
    label, so authorship was being discarded rather than absent. The gate now reads the
    `family:` provenance RMG itself writes, and a copy made by RMG is caught. What is left
    of the route is strictly smaller and is asserted as such below -- the assertion had to
    move because the SCOPE moved, which is the one reason it is allowed to."""
    manifest = _exec_data_file(
        os.path.join(THIS_DATABASE, 'kinetics', 'families', FAMILY, 'quarantine.py'))
    routes = manifest.get('bypassRoutes')
    assert routes, 'the manifest must enumerate what it does NOT cover'
    joined = ' '.join(routes).lower()
    for required in ('engine lacking', 'direct database consumer'):
        assert required in joined, (
            'the bypass list no longer names %r; the scope of this manifest was '
            'narrowed in prose without the list being updated' % required)

    seed_routes = [route for route in routes
                   if 'seed' in route.lower() or 'library' in route.lower()]
    assert seed_routes, (
        'the library/seed route must still be named: a hand-written entry carrying no '
        'authorship remains outside what the gate can check')
    assert any('hand-written' in route.lower() for route in seed_routes), (
        'the library/seed bypass is no longer unconditional -- a rate copied by RMG '
        'carries the authorship the gate now reads. Stating it unconditionally overstates '
        'the hole, which is the mirror image of the error round 87 was filed for.')
