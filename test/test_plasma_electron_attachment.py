#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``Plasma_Electron_Attachment`` kinetics family.

Two failure modes these tests exist to catch, both of which are quiet:

* a family that *loads cleanly and never matches anything*; and
* a family that *matches something it has no data for and hands it a number*.
  The second is the worse of the two, because it is green. Every generation test
  below therefore asserts on **both** the resolved rate and the matched template
  (``reaction.template``), never merely that a reaction came out - "a reaction was
  generated" is exactly the assertion that passed while untrained species were
  being handed an average of O2 and OH.

Three rules the assertions follow, all deliberate:

* Assert on the product's **net charge and formula**, never on an exception being
  raised. The recipe path fails open - it silently returns a wrong species where
  direct construction would raise - so a suite built on ``pytest.raises`` passes
  while the family emits wrong products.
* When a species generates nothing, assert *why*: a charge-imbalanced recipe
  produces zero reactions and logs only at DEBUG, so "0 reactions" alone cannot
  distinguish "the root group did not match" from "it matched and the recipe was
  rejected". ``_root_matches`` pins the first.
* Fail, never skip, when the database is not pinned to this worktree. RMG's
  ``rmgrc`` resolution ends in ``return  # fail silently``; if the pin is missing
  it falls back to a shared checkout and the interesting tests quietly vanish.

Run with the database pinned by the ``rmgrc`` in the repository root::

    cd /home/alon/Code/RMG-database-i008-attachment
    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
      /home/alon/anaconda3/envs/rmg_env/bin/python -m pytest \\
      test/test_plasma_electron_attachment.py -v
"""

import os
import re

import pytest

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.species import Species

FAMILY = 'Plasma_Electron_Attachment'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))


# Adjacency lists are written without atom labels: these are the species RMG
# would hand the family during reaction generation, not training-set entries.
ADJLISTS = {
    'O2': """
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    'OH': """
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    'O': """
multiplicity 3
1 O u2 p2 c0
""",
    'HO2': """
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    'CH3O': """
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    'CH3': """
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    'N': """
multiplicity 4
1 N u3 p1 c0
""",
    'S': """
multiplicity 3
1 S u2 p2 c0
""",
    'H2O': """
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    'N2': """
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    'CO2': """
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    'O3': """
1 O u0 p1 c+1 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u0 p3 c-1 {1,S}
""",
    'Ar': """
1 Ar u0 p4 c0
""",
    'H': """
multiplicity 2
1 H u1 p0 c0
""",
    'Cl': """
multiplicity 2
1 Cl u1 p3 c0
""",
    'O2-': """
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 O u1 p2 c0 {1,S}
""",
}

# What the root union is expected to let in, and what it is expected to keep out.
#
# EXPECTED_IN is exactly the training set, and that is the point of the family's
# shape: the root ``Attacher`` is a LogicOr over the three trained groups, so a
# species matches only if it is one of the three shapes there is data for.
# Nothing else is given a rate, because between species electron-attachment
# coefficients span orders of magnitude with no group-additivity trend to
# interpolate along - an average over these three entries is a fabricated number,
# not an uncertain one.
EXPECTED_IN = ['O2', 'OH', 'O']

# The species kept out are kept out for three distinct reasons, all of which the
# tests below pin separately:
#   closed shell    -> LOSE_RADICAL has no unpaired electron to remove (H2O, N2, CO2, O3, Ar)
#   wrong element   -> no anion atomtype / no increment_lone_pair action (H, Cl)
#   untrained shape -> open-shell, right element, but outside the trained union
#                      (HO2, CH3O, CH3, N, S)
EXPECTED_OUT = ['H2O', 'N2', 'CO2', 'O3', 'Ar', 'H', 'Cl', 'HO2', 'CH3O', 'CH3', 'N', 'S']

# Open-shell species the family must refuse to price. HO2 and CH3O are oxygen
# monoradicals - the old ``O_monoradical`` node handed them an average of the OH
# and O2 entries. CH3, N and S are elements with no training reaction at all -
# the old ``[C,N,O,P,S]`` root handed them the average of all three oxygen
# entries. Neither has any evidence behind it.
UNTRAINED_OPEN_SHELL = ['HO2', 'CH3O', 'CH3', 'N', 'S']

# Formula of the anion each matching species produces (attachment is
# non-dissociative, so the formula is always conserved).
EXPECTED_PRODUCT_FORMULA = {'O2': 'O2', 'OH': 'HO', 'O': 'O'}

# The rate every trained species must resolve to, in cm^3/(mol*s), and the tree
# node it must resolve through. Both halves matter: the rate alone looks like a
# plausible number no matter which node produced it.
EXPECTED_TRAINED_KINETICS = {
    'O2': ('O_in_O2', 1, 9.6807e10),
    'OH': ('O_in_OH', 2, 2.9580e10),
    'O': ('Attacher', 3, 9.0332e08),
}

# Which physical quantity each training entry actually is. Entries 1 and 2 are
# effective two-body coefficients with a third-body density folded in at 5 torr;
# entry 3 is a genuine two-body radiative rate with no folded density. Averaging
# across these two categories produces a number that is not a rate coefficient of
# any kind, which is what ``test_no_rate_rule_mixes_pressure_baked_with_radiative``
# forbids. A new training entry must be classified here or that test fails.
TRAINING_ENTRY_CATEGORY = {
    1: 'pressure-baked',
    2: 'pressure-baked',
    3: 'radiative',
}


def _species(name):
    return Species(label=name).from_adjacency_list(ADJLISTS[name])


@pytest.fixture(scope='module')
def kinetics_db():
    """Load only this family, only its training depository, and no libraries."""
    assert settings['database.directory'] == THIS_DATABASE, (
        'RMG resolved database.directory to {0!r}, not this worktree ({1!r}). '
        'rmgrc is read from the current working directory and fails silently when '
        'absent - run pytest from the repository root.'.format(
            settings['database.directory'], THIS_DATABASE)
    )
    db = KineticsDatabase()
    db.load_families(os.path.join(settings['database.directory'], 'kinetics', 'families'),
                     families=[FAMILY], depositories=['training'])
    family = db.families[FAMILY]
    family.add_rules_from_training(thermo_database=None)
    family.fill_rules_by_averaging_up(verbose=True)
    return db


@pytest.fixture(scope='module')
def family(kinetics_db):
    return kinetics_db.families[FAMILY]


def _generate(kinetics_db, name):
    return kinetics_db.generate_reactions_from_families(
        [_species(name)], products=None, only_families=[FAMILY], resonance=True)


def _root_matches(family, name):
    """True if any atom of `name` matches the family's root node as *1.

    A charge-imbalanced recipe generates zero reactions and logs only at DEBUG,
    so an empty reaction list on its own does not say whether the root group
    matched. This asks the group tree directly.
    """
    root = family.groups.top[0]
    molecule = _species(name).molecule[0]
    return any(family.groups.match_node_to_structure(root, molecule, {'*1': atom})
               for atom in molecule.atoms)


def _rule_provenance(entry):
    """All text a rate rule carries about where its number came from."""
    return '{0}\n{1}'.format(entry.long_desc or '', getattr(entry.data, 'comment', '') or '')


def _training_indices(entry):
    """The training reaction indices a rate rule's value derives from."""
    return {int(i) for i in re.findall(r'training reaction (\d+)', _rule_provenance(entry))}


def _all_rules(family):
    return [(label, entry)
            for label, entries in family.rules.entries.items()
            for entry in entries]


# ---------------------------------------------------------------------------
# Definition
# ---------------------------------------------------------------------------

def test_recipe_is_lose_radical_plus_gain_pair(family):
    """The one action pair that actually produces an anion.

    LOSE_CHARGE alone silently returns the neutral radical, so the recipe is
    pinned rather than described.
    """
    actions = [list(a) for a in family.forward_recipe.actions]
    assert actions == [['LOSE_RADICAL', '*1', 1], ['GAIN_PAIR', '*1', 1]]


def test_electron_is_carried_by_the_electrons_flag(family):
    """The electron is not a template reactant; ``electrons = -1`` carries it."""
    assert family.electrons == -1
    assert family.allow_charged_species is True
    assert family.reversible is False
    assert [e.label for e in family.forward_template.reactants] == ['Attacher']
    assert len(family.forward_template.products) == 1


def test_root_is_a_union_of_exactly_the_trained_groups(family):
    """The root admits the three trained shapes and nothing else.

    A single Group broad enough to cover atomic O (u2, unbonded) *and* the two
    monoradicals is necessarily broad enough to cover HO2, CH3O and every other
    RO, which is how the previous ``[C,N,O,P,S]`` root came to hand oxygen
    averages to carbon, nitrogen and sulfur. Only a union can be exactly as wide
    as the evidence.
    """
    root = family.groups.top[0]
    assert root.label == 'Attacher'
    assert sorted(root.item.components) == ['O_atom', 'O_in_O2', 'O_in_OH']

    # ``O_atom`` is a union member but deliberately not a tree node: descend_tree
    # returns the root when no child matches, so atomic O resolves to Attacher
    # itself and its training reaction gives the root an *exact* rule. Making it
    # an L2 node would move that rule off the root and let averaging refill the
    # root with a pressure-baked/radiative mean.
    assert sorted(c.label for c in root.children) == ['O_in_O2', 'O_in_OH']


def test_training_set_is_populated_and_each_entry_templates(family):
    """A real training set, and every entry reaches a node of the tree.

    An entry that cannot be templated in the forward direction falls into
    ``add_rules_from_training``'s reverse branch, which needs thermo and would
    otherwise fail the whole database load.
    """
    depository = family.get_training_depository()
    assert len(depository.entries) == 3

    nodes = {}
    for index, entry in sorted(depository.entries.items()):
        template = family.get_reaction_template(entry.item)
        assert len(template) == 1
        nodes[entry.label] = template[0].label

    assert nodes == {
        'O2 <=> O2-': 'O_in_O2',
        'OH <=> OH-': 'O_in_OH',
        'O <=> O-': 'Attacher',
    }
    # Distinct nodes: no two training reactions collapse onto one node, which
    # would average rates that differ by orders of magnitude.
    assert len(set(nodes.values())) == 3


# ---------------------------------------------------------------------------
# Rate rules - every rule is evidence, none is an average
# ---------------------------------------------------------------------------

def test_every_rate_rule_is_an_exact_training_hit(family):
    """There is one rate rule per training reaction and not one more.

    ``fill_rules_by_averaging_up`` only invents a rule for a node that has none,
    and keeps any rule of rank > 0. With all three training reactions landing on
    tree nodes, every node is already exact and nothing is averaged - so the
    family cannot hand a derived number to anything.
    """
    rules = _all_rules(family)
    assert sorted(label for label, _ in rules) == ['Attacher', 'O_in_O2', 'O_in_OH']

    for label, entry in rules:
        assert entry.rank > 0, '{0} has rank 0, which invites averaging'.format(label)
        assert 'Average of' not in _rule_provenance(entry), \
            '{0} is an averaged rule: {1}'.format(label, _rule_provenance(entry))
        assert len(_training_indices(entry)) == 1, \
            '{0} derives from training reactions {1}'.format(label, _training_indices(entry))


def test_no_rate_rule_mixes_pressure_baked_with_radiative(family):
    """Defect 2, asserted directly.

    Training entries 1 and 2 are effective two-body coefficients with a 5 torr
    third-body density folded in; entry 3 is a genuine two-body radiative rate.
    The mean of the two kinds is not a rate coefficient of any kind. Before the
    tree was narrowed, ``Attacher`` was exactly that mean and it was what every
    untrained class received.
    """
    depository_indices = set(family.get_training_depository().entries)
    assert depository_indices <= set(TRAINING_ENTRY_CATEGORY), (
        'training entries {0} are unclassified - say whether each is '
        'pressure-baked or radiative before letting it into the tree'.format(
            depository_indices - set(TRAINING_ENTRY_CATEGORY))
    )

    for label, entry in _all_rules(family):
        indices = _training_indices(entry)
        assert indices, '{0} cites no training reaction at all'.format(label)
        categories = {TRAINING_ENTRY_CATEGORY[i] for i in indices}
        assert len(categories) == 1, (
            'rate rule {0} mixes {1} (training reactions {2})'.format(
                label, sorted(categories), sorted(indices))
        )


# ---------------------------------------------------------------------------
# Generation - the verifier
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('name', EXPECTED_IN)
def test_trained_species_resolve_to_their_own_rate_through_their_own_node(kinetics_db, family, name):
    """The three trained reactions keep their own rates, through their own nodes.

    Asserting the rate without the template would have passed against every
    defect this test file was rewritten for: the wrong node hands out a
    plausible-looking number.
    """
    expected_node, expected_index, expected_a_cm3 = EXPECTED_TRAINED_KINETICS[name]

    reactions = _generate(kinetics_db, name)
    assert len(reactions) == 1, '{0} generated {1} reactions'.format(name, len(reactions))
    reaction = reactions[0]
    assert reaction.template == [expected_node]

    kinetics, source, entry, is_forward = family.get_kinetics(
        reaction, template_labels=reaction.template, degeneracy=reaction.degeneracy,
        estimator='rate rules', return_all_kinetics=False)

    assert source == 'rate rules'
    assert 'From training reaction {0} used for {1}'.format(expected_index, expected_node) \
        in kinetics.comment
    assert 'Exact match found for rate rule [{0}]'.format(expected_node) in kinetics.comment
    assert 'Average of' not in kinetics.comment

    # A_si is m^3/(mol*s) for a second-order rate; the reference values are the
    # published cm^3/(mol*s) numbers.
    assert kinetics.A.value_si * 1e6 == pytest.approx(expected_a_cm3, rel=1e-4)

    training = family.get_training_depository().entries[expected_index]
    assert kinetics.A.value_si == pytest.approx(training.data.A.value_si, rel=1e-9)


def test_o2_attachment_is_generated_with_the_right_product(kinetics_db):
    """O2 + e- => O2-, generated by the family, asserted on charge and formula."""
    reactions = _generate(kinetics_db, 'O2')
    assert len(reactions) == 1, 'family generated {0} reactions for O2'.format(len(reactions))

    reaction = reactions[0]
    assert reaction.family == FAMILY
    assert reaction.electrons == -1
    assert reaction.template == ['O_in_O2']

    assert len(reaction.products) == 1
    product = reaction.products[0].molecule[0]
    assert product.get_net_charge() == -1
    assert product.get_formula() == 'O2'
    assert sorted(a.atomtype.label for a in product.atoms) == ['O0sc', 'O2s']

    # ... and the reactant is untouched apart from the captured electron.
    reactant = reaction.reactants[0].molecule[0]
    assert reactant.get_net_charge() == 0
    assert reactant.get_formula() == 'O2'


def test_o2_rate_comes_from_the_training_set_not_a_library(kinetics_db, family):
    """The rate is an exact rate-rule hit on the O2 training reaction.

    No kinetics libraries are loaded by this fixture at all, so a library lookup
    is not merely improbable here - it is impossible. What the test pins is the
    positive claim: the number came from training reaction 1.
    """
    assert kinetics_db.libraries == {}

    reaction = _generate(kinetics_db, 'O2')[0]
    kinetics, source, entry, is_forward = family.get_kinetics(
        reaction, template_labels=reaction.template, degeneracy=reaction.degeneracy,
        estimator='rate rules', return_all_kinetics=False)

    assert source == 'rate rules'
    assert 'From training reaction 1 used for O_in_O2' in kinetics.comment
    assert 'Exact match found for rate rule [O_in_O2]' in kinetics.comment
    assert 'Average of' not in kinetics.comment

    training = family.get_training_depository().entries[1]
    assert kinetics.A.value_si == pytest.approx(training.data.A.value_si, rel=1e-9)


@pytest.mark.parametrize('name', EXPECTED_IN)
def test_every_match_yields_a_mono_anion_of_the_same_formula(kinetics_db, name):
    """Non-dissociative attachment: charge -1, formula conserved, one product."""
    reactions = _generate(kinetics_db, name)
    assert reactions, '{0} was expected to match the root group but did not'.format(name)

    for reaction in reactions:
        assert len(reaction.products) == 1
        product = reaction.products[0].molecule[0]
        assert product.get_net_charge() == -1, \
            '{0} produced net charge {1}'.format(name, product.get_net_charge())
        assert product.get_formula() == EXPECTED_PRODUCT_FORMULA[name]


# ---------------------------------------------------------------------------
# Root group - what it matches and what it does not
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('name', EXPECTED_IN)
def test_root_group_matches_expected_species(kinetics_db, family, name):
    assert _root_matches(family, name), \
        '{0} should match the root union of {1}'.format(name, FAMILY)
    assert _generate(kinetics_db, name), \
        '{0} matched the root union but generated nothing'.format(name)


@pytest.mark.parametrize('name', EXPECTED_OUT)
def test_root_group_excludes_expected_species(kinetics_db, name):
    reactions = _generate(kinetics_db, name)
    assert reactions == [], \
        '{0} should NOT match {1}, but generated {2}'.format(name, FAMILY, reactions)


@pytest.mark.parametrize('name', UNTRAINED_OPEN_SHELL)
def test_untrained_open_shell_species_are_not_matched_at_all(kinetics_db, family, name):
    """Defect 1, asserted directly and on the cause, not just the count.

    CH3, atomic N and atomic S have no training reaction of any kind; HO2 and
    CH3O are oxygen monoradicals with no training reaction either. All five used
    to be handed a rate: CH3/N/S the average of all three oxygen entries via the
    old ``[C,N,O,P,S]`` root, HO2/CH3O the average of the OH and O2 entries via
    the old ``O_monoradical`` node.

    Each is open-shell, so the recipe *could* have acted on it - the exclusion
    has to come from the root union, and ``_root_matches`` is what distinguishes
    "not matched" from "matched and rejected on charge balance", which also
    yields zero reactions and logs only at DEBUG.
    """
    molecule = _species(name).molecule[0]
    assert sum(a.radical_electrons for a in molecule.atoms) >= 1, \
        '{0} is not open-shell, so this test would prove nothing'.format(name)

    assert not _root_matches(family, name), \
        '{0} matches the root union, so it will be given a rate'.format(name)
    assert _generate(kinetics_db, name) == [], \
        '{0} generated a reaction despite having no training support'.format(name)


def test_closed_shell_species_are_excluded_by_the_recipe(kinetics_db):
    """H2O, N2, CO2 and O3 carry no unpaired electron for LOSE_RADICAL to remove.

    This is what makes SF6-style attachment to a closed-shell molecule impossible
    with this recipe; it is a property of the recipe, not an oversight in the
    tree. Since the tree was narrowed the exclusion is enforced twice over - every
    group in the root union also requires u >= 1 - so the assertion here is on the
    recipe-level cause: zero radical electrons, therefore no reaction.
    """
    for name in ['H2O', 'N2', 'CO2', 'O3']:
        molecule = _species(name).molecule[0]
        assert sum(a.radical_electrons for a in molecule.atoms) == 0
        assert _generate(kinetics_db, name) == []


def test_hydrogen_and_chlorine_are_excluded_by_element(kinetics_db):
    """H and Cl are open-shell, so only the root union's elements keep them out.

    Both are radicals that LOSE_RADICAL could act on; neither H- nor Cl- has a
    resolvable atomtype, and neither ``ATOMTYPES['H']`` nor ``ATOMTYPES['Cl']``
    has an ``increment_lone_pair`` action for GAIN_PAIR to use. Every member of
    the root union is an oxygen group, so they never reach the recipe.
    """
    for name in ['H', 'Cl']:
        molecule = _species(name).molecule[0]
        assert sum(a.radical_electrons for a in molecule.atoms) == 1
        assert _generate(kinetics_db, name) == []


def test_known_limitation_rmg_still_cannot_require_a_neutral_reactant(kinetics_db, family):
    """O2- is no longer re-attached, but RMG-Py's gap is unfixed.

    RMG groups match subgraphs, so a group cannot express "the reactant molecule
    is neutral". ``allowChargedSpecies`` is two-sided - it permits charged
    reactants *and* products together - and there is no generated-species
    constraint on net charge either. Blocking anion re-attachment properly needs a
    one-sided neutral-reactant check in RMG-Py, which does not exist and is out of
    scope for this ticket.

    This family used to generate the spurious ``O2- + e- => O2(2-)`` and this test
    pinned that. It no longer does - but *only incidentally*, and the distinction
    is the whole point of keeping this test: the radical oxygen of O2- is bonded
    to an O0sc rather than to another ``O u1 p2 c0``, so it falls outside the
    narrowed union. Nothing in the engine stopped it. The next family that needs a
    wider group will meet the same gap, so the assertion below is on the *cause* -
    a group-shape miss - not on any engine-level protection.
    """
    assert not _root_matches(family, 'O2-'), \
        'O2- matches the root union again - the RMG-Py neutral-reactant gap is now live'
    assert _generate(kinetics_db, 'O2-') == []

    # The gap itself, unchanged: the family still declares charged species legal
    # in both directions, which is the setting that would let O2- through the
    # moment a group happened to match it.
    assert family.allow_charged_species is True
