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
    # O2(a1Dg), written in the biradical form RMG accepts. Identical connectivity,
    # radical count, lone pairs and charge to ground-state triplet O2 - the *only*
    # thing that distinguishes it is the molecular multiplicity, which is why
    # ``O_in_O2`` has to carry a ``multiplicity`` constraint to keep it out.
    'O2_singlet_delta': """
multiplicity 1
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    # Closed-shell singlet O2, for contrast: kept out by the recipe, not by spin.
    'O2_singlet_closed_shell': """
multiplicity 1
1 O u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    # Singlet atomic oxygen. O(1D) cannot be written as ``O u2 p2 c0`` with
    # multiplicity 1 at all - ``ConsistencyChecker.check_hund_rule`` rejects an
    # atom with two unpaired electrons in a multiplicity-1 molecule - so the only
    # representable singlet O atom is the closed-shell one below, which the recipe
    # excludes for want of a radical. See ``test_atomic_oxygen_spin_states``.
    'O_singlet': """
1 O u0 p3 c0
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
#   untrained element -> H and Cl are open-shell and RMG can represent their
#                      anions perfectly well; they are out because there is no
#                      training data for them, so no group of theirs is in the union
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
    'O': ('O_atom', 3, 9.0332e08),
}

# The ground-state multiplicity each trained group is pinned to, and why. Every
# training rate in this family is a ground-state measurement, so a group that
# cannot tell the ground state from an excited one hands the ground-state rate to
# the excited species (see ``test_o2_spin_states``).
EXPECTED_GROUP_MULTIPLICITY = {
    'O_in_O2': [3],   # load-bearing: O2(a1Dg) is otherwise indistinguishable
    'O_in_OH': [2],   # documentary: one unpaired electron admits only a doublet
    'O_atom': [3],    # documentary: Hund's rule forbids the multiplicity-1 form
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


def _generate(kinetics_db, name, resonance=True):
    return kinetics_db.generate_reactions_from_families(
        [_species(name)], products=None, only_families=[FAMILY], resonance=resonance)


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


def _reachable_labels(family):
    """Labels of the nodes a structure can actually resolve to.

    ``descend_tree`` stops at the root only when the structure matches the root
    but no child. The root here is a LogicOr over exactly its own children
    (``test_no_union_member_lacks_an_l2_child``), so every structure the root
    admits matches a child and the root itself is unreachable. What a species can
    be given is therefore exactly the L2 set.
    """
    return {child.label for child in family.groups.top[0].children}


def _group_tree_failures(family):
    """The failures ``kinetics_check_groups_found_in_tree`` would report.

    Transcribed from ``RMG-Py/test/database/databaseTest.py`` (the ``tst``/``tst1``/
    ``tst2``/``tst3`` loop), with one deliberate difference: the ``ascend_parent is
    None`` case breaks instead of falling through to ``ascend_parent.children``.
    The repo-wide test does fall through, so a parentless group makes it raise
    ``AttributeError`` and CI reports a crashed test rather than a rejected family
    - which is how this family's own out-of-tree ``O_atom`` stayed invisible.
    """
    failures = []
    for node_name, node_group in family.groups.entries.items():
        if '[' in node_name or ']' in node_name:
            failures.append('{0}: square brackets in the label'.format(node_name))
        ascend_parent = node_group
        while (ascend_parent not in family.groups.top
               and ascend_parent not in family.forward_template.products):
            child = ascend_parent
            ascend_parent = ascend_parent.parent
            if ascend_parent is None:
                failures.append('{0}: found in the tree without a proper parent'.format(node_name))
                break
            if child not in ascend_parent.children:
                failures.append('{0}: not in its parent\'s children'.format(node_name))
                break
            if child is ascend_parent:
                failures.append('{0}: is a parent to itself'.format(node_name))
                break
    return failures


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


def test_group_tree_is_legal(family):
    """The tree RMG's own database consistency check demands.

    Every group entry must walk a valid parent chain to a top or product node.
    This runs the loop from ``kinetics_check_groups_found_in_tree`` rather than
    inspecting the tree by eye, so the repo-wide test can never be the first thing
    to discover a broken tree here.

    It is not a hypothetical: ``O_atom`` used to sit outside the tree with no
    parent - deliberately, to keep the atomic-O rule on the root - and the
    repo-wide check does not reject that cleanly, it dereferences ``None`` and
    raises ``AttributeError``. The property that placement protected is now held
    by ``test_no_union_member_lacks_an_l2_child`` instead.
    """
    assert _group_tree_failures(family) == []


def test_no_union_member_lacks_an_l2_child(family):
    """The root's averaged rule is unreachable, and stays unreachable.

    ``fill_rules_by_averaging_up`` puts a rule on ``Attacher`` that mixes a
    pressure-baked effective coefficient with a radiative one - a number that is
    not a rate coefficient of any kind. It is tolerable only because nothing can
    be given it, and that is structural rather than a fact about today's three
    species: ``descend_tree`` returns the root only when a structure matches the
    root but none of its children, so as long as the union's members are exactly
    the root's children, every structure the union admits matches a child.

    This is the assertion that rots the moment someone adds a fourth member to
    the union without a matching L2 node - which a test over today's three
    species would not notice - so it is written as a set identity, not a list.
    """
    root = family.groups.top[0]
    union_members = set(root.item.components)
    children = {child.label for child in root.children}

    assert union_members == children, (
        'union members without an L2 child: {0}; L2 children not in the union: '
        '{1}. Either way the root can be reached and its averaged rule handed '
        'out.'.format(sorted(union_members - children), sorted(children - union_members))
    )
    # ... and each child is the very entry the union names, not a namesake.
    for label in union_members:
        assert family.groups.entries[label] in root.children


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
        'O <=> O-': 'O_atom',
    }
    # Distinct nodes: no two training reactions collapse onto one node, which
    # would average rates that differ by orders of magnitude.
    assert len(set(nodes.values())) == 3


# ---------------------------------------------------------------------------
# Rate rules - every rule is evidence, none is an average
# ---------------------------------------------------------------------------

def test_every_reachable_rate_rule_is_an_exact_training_hit(family):
    """Every rule a species can be given is one training reaction, exactly.

    ``fill_rules_by_averaging_up`` invents a rule only for a node that has none,
    and keeps any rule of rank > 0. Each of the three L2 nodes carries its own
    training reaction, so each is exact; the only derived rule in the family is
    the root's, and the root is unreachable
    (``test_no_union_member_lacks_an_l2_child``). The distinction between "no
    averaged rule exists" and "no averaged rule can be reached" is the whole
    design: the first was bought by leaving ``O_atom`` out of the tree, which is
    illegal, and this is the second.
    """
    rules = _all_rules(family)
    assert sorted(label for label, _ in rules) == ['Attacher', 'O_atom', 'O_in_O2', 'O_in_OH']

    reachable = _reachable_labels(family)
    assert reachable == {'O_atom', 'O_in_O2', 'O_in_OH'}

    for label, entry in rules:
        if label not in reachable:
            continue
        assert entry.rank > 0, '{0} has rank 0, which invites averaging'.format(label)
        assert 'Average of' not in _rule_provenance(entry), \
            '{0} is an averaged rule: {1}'.format(label, _rule_provenance(entry))
        assert len(_training_indices(entry)) == 1, \
            '{0} derives from training reactions {1}'.format(label, _training_indices(entry))


def test_the_only_averaged_rule_is_the_unreachable_root(family):
    """The root's average is named here so it cannot spread unnoticed.

    Averaging up is not disabled - it cannot be - so the root does carry a
    derived rule. Pinning *which* node carries it is what makes the arrangement
    auditable: if a second averaged rule ever appears, it is on a node something
    can resolve to, and this fails.
    """
    averaged = sorted(label for label, entry in _all_rules(family)
                      if 'Average of' in _rule_provenance(entry))
    assert averaged == ['Attacher'], \
        'averaged rules on {0}; only the unreachable root may carry one'.format(averaged)
    assert 'Attacher' not in _reachable_labels(family)


def test_no_reachable_rate_rule_mixes_pressure_baked_with_radiative(family):
    """No species is given a mean of two different physical quantities.

    Training entries 1 and 2 are effective two-body coefficients with a 5 torr
    third-body density folded in; entry 3 is a genuine two-body radiative rate.
    The mean of the two kinds is not a rate coefficient of any kind. The root
    rule *is* that mean - it is asserted below to be exactly that, so nobody
    mistakes it for a defensible number - and the point is that nothing can
    resolve to it.
    """
    depository_indices = set(family.get_training_depository().entries)
    assert depository_indices <= set(TRAINING_ENTRY_CATEGORY), (
        'training entries {0} are unclassified - say whether each is '
        'pressure-baked or radiative before letting it into the tree'.format(
            depository_indices - set(TRAINING_ENTRY_CATEGORY))
    )

    reachable = _reachable_labels(family)
    for label, entry in _all_rules(family):
        indices = _training_indices(entry)
        assert indices, '{0} cites no training reaction at all'.format(label)
        categories = {TRAINING_ENTRY_CATEGORY[i] for i in indices}
        if label not in reachable:
            continue
        assert len(categories) == 1, (
            'rate rule {0} mixes {1} (training reactions {2})'.format(
                label, sorted(categories), sorted(indices))
        )

    # The root is the mixed rule, stated rather than implied.
    root_rule = family.rules.entries['Attacher'][0]
    assert {TRAINING_ENTRY_CATEGORY[i] for i in _training_indices(root_rule)} == \
        {'pressure-baked', 'radiative'}
    assert 'Attacher' not in reachable


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
# Spin state - the groups must not price an excited species at the ground rate
# ---------------------------------------------------------------------------

def test_each_trained_group_pins_its_ground_state_multiplicity(family):
    """Every training rate here is a ground-state measurement, so say so.

    RMG group matching compares connectivity, radical count, lone pairs and
    charge - not spin coupling - so without ``multiplicity`` the groups cannot
    tell a ground state from an excited state of the same adjacency list.
    ``Group.multiplicity`` is a supported, matched constraint on the multiplicity
    of the *whole* molecule, so this needs no engine change.
    """
    for label, expected in EXPECTED_GROUP_MULTIPLICITY.items():
        assert family.groups.entries[label].item.multiplicity == expected, (
            'group {0} has multiplicity {1}, expected {2}'.format(
                label, family.groups.entries[label].item.multiplicity, expected)
        )


def test_o2_spin_states(kinetics_db, family):
    """Singlet-delta O2 is refused; ground-state triplet O2 is unaffected.

    This is the load-bearing half of the spin constraint. ``O_in_O2`` is two
    adjacent ``O u1 p2 c0`` atoms, which is ground-state O2(X3Sg-) and
    O2(a1Dg) alike; before ``multiplicity [3]``, singlet-delta O2 was handed the
    ground-state triplet rate identical to four significant figures. O2(a1Dg) is
    one of the dominant excited species in an oxygen discharge and has its own
    attachment behaviour, so a wrong number for it is not an edge case.

    Asserted on the matched template and the rate, and on the group-level cause
    for the refusal - not on an exception, and not on a bare reaction count.

    The refusal is asserted against the species as declared. RMG's *own*
    resonance step then undoes the declaration, which is an RMG-Py defect and is
    pinned separately by
    ``test_known_limitation_resonance_generation_erases_declared_multiplicity``.
    """
    # Ground state: unchanged, still its own node and its own rate.
    reactions = _generate(kinetics_db, 'O2')
    assert len(reactions) == 1
    assert reactions[0].template == ['O_in_O2']
    kinetics, _, _, _ = family.get_kinetics(
        reactions[0], template_labels=reactions[0].template,
        degeneracy=reactions[0].degeneracy, estimator='rate rules', return_all_kinetics=False)
    assert kinetics.A.value_si * 1e6 == pytest.approx(9.6807e10, rel=1e-4)

    # Singlet delta: refused by the group, therefore never priced.
    singlet = _species('O2_singlet_delta').molecule[0]
    assert singlet.multiplicity == 1
    assert sum(a.radical_electrons for a in singlet.atoms) == 2, \
        'the biradical form is the point - a closed-shell singlet would be kept out by the recipe'
    assert not singlet.is_subgraph_isomorphic(family.groups.entries['O_in_O2'].item), \
        'O_in_O2 matches singlet-delta O2, which will be given the triplet rate'
    assert not _root_matches(family, 'O2_singlet_delta')
    assert _generate(kinetics_db, 'O2_singlet_delta', resonance=False) == []

    # Closed-shell singlet O2, for contrast: kept out by LOSE_RADICAL, not by spin.
    closed = _species('O2_singlet_closed_shell').molecule[0]
    assert sum(a.radical_electrons for a in closed.atoms) == 0
    assert _generate(kinetics_db, 'O2_singlet_closed_shell') == []


def test_known_limitation_resonance_generation_erases_declared_multiplicity(kinetics_db, family):
    """The spin constraint holds; RMG-Py destroys the spin state upstream of it.

    ``resonance.generate_resonance_structures`` opens with ``mol.update()``
    (rmgpy/molecule/resonance.py:197), and ``Molecule.update_multiplicity``
    unconditionally recomputes ``multiplicity = radical_count + 1``
    (rmgpy/molecule/molecule.py:1595). A species declared ``multiplicity 1`` with
    two unpaired electrons - O2(a1Dg) in its biradical form - therefore comes back
    from resonance generation relabelled ``multiplicity 3``, i.e. as ground-state
    O2. It is then a legitimate match for ``O_in_O2``, and it is also isomorphic
    to ground-state O2, so RMG would not carry it as a distinct species at all.

    Nothing in this family can fix that: it is an RMG-Py defect, out of scope
    here, and it is asserted on its *cause* rather than left as a silent hole.
    What the family owns - refusing to price a species that reaches it still
    declared as a singlet - is asserted in ``test_o2_spin_states`` and holds.
    """
    species = _species('O2_singlet_delta')
    assert species.molecule[0].multiplicity == 1

    species.generate_resonance_structures()
    assert [m.multiplicity for m in species.molecule] == [3], (
        'resonance generation no longer relabels singlet-delta O2 as a triplet - '
        'the RMG-Py gap may be fixed, so re-check what this family now sees'
    )

    # ... and that is exactly why the resonance-enabled path still generates.
    reactions = _generate(kinetics_db, 'O2_singlet_delta')
    assert len(reactions) == 1
    assert reactions[0].template == ['O_in_O2'], (
        'if this is no longer O_in_O2, the upstream relabelling changed shape'
    )


def test_atomic_oxygen_spin_states(kinetics_db, family):
    """``O_atom``'s multiplicity is documentary, and this says why.

    Charge is derived, so ``O u2 p2 c0`` fixes the bond count at zero: the group
    can only ever match lone atomic O. Of the multiplicities RMG would accept for
    two unpaired electrons, the multiplicity-1 form is rejected outright by
    ``ConsistencyChecker.check_hund_rule``, so triplet O(3P) is the only thing
    this group can match and ``multiplicity [3]`` loses no legitimate match. The
    singlet O atom RMG *can* represent is the closed-shell ``O u0 p3 c0``, which
    the group does not match and the recipe could not act on anyway.
    """
    from rmgpy.exceptions import InvalidAdjacencyListError

    reactions = _generate(kinetics_db, 'O')
    assert len(reactions) == 1
    assert reactions[0].template == ['O_atom']

    with pytest.raises(InvalidAdjacencyListError):
        Species(label='O(1D)').from_adjacency_list('multiplicity 1\n1 O u2 p2 c0\n')

    singlet = _species('O_singlet').molecule[0]
    assert sum(a.radical_electrons for a in singlet.atoms) == 0
    assert not singlet.is_subgraph_isomorphic(family.groups.entries['O_atom'].item)
    assert not _root_matches(family, 'O_singlet')
    assert _generate(kinetics_db, 'O_singlet') == []


def test_hydroxyl_multiplicity_constraint_loses_no_match(kinetics_db, family):
    """``O_in_OH``'s multiplicity is documentary too, and this proves the "no loss".

    ``O u1 p2 c0`` fixes the bond count at one and ``H u0 p0 c0`` is saturated,
    so the group can only match the whole two-atom molecule OH; one unpaired
    electron admits only a doublet. ``multiplicity [2]`` therefore cannot
    exclude anything OH-shaped - which is what this asserts, on the generated
    rate rather than on the argument.
    """
    reactions = _generate(kinetics_db, 'OH')
    assert len(reactions) == 1
    assert reactions[0].template == ['O_in_OH']
    kinetics, _, _, _ = family.get_kinetics(
        reactions[0], template_labels=reactions[0].template,
        degeneracy=reactions[0].degeneracy, estimator='rate rules', return_all_kinetics=False)
    assert kinetics.A.value_si * 1e6 == pytest.approx(2.9580e10, rel=1e-4)

    molecule = _species('OH').molecule[0]
    assert molecule.multiplicity == 2
    assert sum(a.radical_electrons for a in molecule.atoms) == 1


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

    Both are radicals that LOSE_RADICAL could act on, and against the RMG-Py this
    family targets both ``ATOMTYPES['H']`` and ``ATOMTYPES['Cl']`` *do* carry an
    ``increment_lone_pair`` action for GAIN_PAIR to use - as do F and Br. (An
    earlier version of this docstring and of ``groups.py`` claimed otherwise; the
    charged-atomtype work has closed that gap. Iodine is the one element still
    unwired.) So the exclusion here is not a capability limit at all: it is that
    every member of the root union is an oxygen group, because oxygen is the only
    element with training data in this family. Widening to the halogens is a
    training-data ticket, and out of scope here.
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
