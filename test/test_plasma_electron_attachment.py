#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``Plasma_Electron_Attachment`` kinetics family.

The failure mode these tests exist to catch is a family that *loads cleanly and
never matches anything*. So nothing here asserts that a file exists or parses;
every claim is made against a reaction the family actually generated.

Two rules the assertions follow, both deliberate:

* Assert on the product's **net charge and formula**, never on an exception being
  raised. The recipe path fails open - it silently returns a wrong species where
  direct construction would raise - so a suite built on ``pytest.raises`` passes
  while the family emits wrong products.
* Fail, never skip, when the database is not pinned to this worktree. RMG's
  ``rmgrc`` resolution ends in ``return  # fail silently``; if the pin is missing
  it falls back to a shared checkout and the interesting tests quietly vanish.

Run with the database pinned by the ``rmgrc`` in the repository root::

    cd /home/alon/Code/RMG-database-i008-attachment
    PYTHONPATH=/home/alon/Code/RMG-Py-i009-atomtypes \\
      /home/alon/anaconda3/envs/rmg_env/bin/python -m pytest \\
      test/test_plasma_electron_attachment.py -v
"""

import os

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
    'CH3': """
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
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

# What the root group is expected to let in, and what it is expected to keep out.
# The species kept out are kept out for three distinct reasons, all of which the
# tests below pin separately:
#   closed shell  -> LOSE_RADICAL has no unpaired electron to remove (H2O, N2, CO2, O3, Ar)
#   wrong element -> no anion atomtype / no increment_lone_pair action (H, Cl)
EXPECTED_IN = ['O2', 'OH', 'O', 'HO2', 'CH3']
EXPECTED_OUT = ['H2O', 'N2', 'CO2', 'O3', 'Ar', 'H', 'Cl']

# Formula of the anion each matching species produces (attachment is
# non-dissociative, so the formula is always conserved).
EXPECTED_PRODUCT_FORMULA = {'O2': 'O2', 'OH': 'HO', 'O': 'O', 'HO2': 'HO2', 'CH3': 'CH3'}


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
    # Distinct leaves: no two training reactions collapse onto one node, which
    # would average rates that differ by orders of magnitude.
    assert len(set(nodes.values())) == 3


# ---------------------------------------------------------------------------
# Generation - the verifier
# ---------------------------------------------------------------------------

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
def test_root_group_matches_expected_species(kinetics_db, name):
    assert _generate(kinetics_db, name), \
        '{0} should match the root group of {1}'.format(name, FAMILY)


@pytest.mark.parametrize('name', EXPECTED_OUT)
def test_root_group_excludes_expected_species(kinetics_db, name):
    reactions = _generate(kinetics_db, name)
    assert reactions == [], \
        '{0} should NOT match {1}, but generated {2}'.format(name, FAMILY, reactions)


def test_closed_shell_species_are_excluded_by_the_recipe_not_by_the_element_list(kinetics_db):
    """H2O, N2, CO2 and O3 all contain C/N/O, so the element list does not exclude them.

    They are excluded because LOSE_RADICAL needs an unpaired electron. This is
    what makes SF6-style attachment to a closed-shell molecule impossible with
    this recipe, and it is a property of the recipe, not an oversight in the tree.
    """
    for name in ['H2O', 'N2', 'CO2', 'O3']:
        molecule = _species(name).molecule[0]
        assert sum(a.radical_electrons for a in molecule.atoms) == 0
        assert _generate(kinetics_db, name) == []


def test_hydrogen_and_chlorine_are_excluded_by_the_element_list(kinetics_db):
    """H and Cl are open-shell, so only the root group's element list keeps them out.

    Both are radicals that LOSE_RADICAL could act on; neither H- nor Cl- has a
    resolvable atomtype, and neither ``ATOMTYPES['H']`` nor ``ATOMTYPES['Cl']``
    has an ``increment_lone_pair`` action for GAIN_PAIR to use.
    """
    for name in ['H', 'Cl']:
        molecule = _species(name).molecule[0]
        assert sum(a.radical_electrons for a in molecule.atoms) == 1
        assert _generate(kinetics_db, name) == []


def test_known_limitation_attachment_to_an_existing_anion_is_not_blocked(kinetics_db):
    """XFAIL-in-spirit: the family will attach a second electron to O2-.

    RMG groups match subgraphs, so a group cannot express "the reactant molecule
    is neutral": the radical oxygen of O2- (u1 p2 c0) is locally indistinguishable
    from an oxygen of O2. ``allowChargedSpecies`` is two-sided - it permits charged
    reactants *and* products together - and there is no generated-species
    constraint on net charge either. Blocking this needs a one-sided
    neutral-reactant check in RMG-Py, which is out of scope for this ticket.

    This test pins the current, wrong behaviour on purpose. When the RMG-Py fix
    lands, this test fails loudly and should be inverted to assert no reactions.
    """
    reactions = _generate(kinetics_db, 'O2-')
    assert len(reactions) == 1
    product = reactions[0].products[0].molecule[0]
    assert product.get_net_charge() == -2, (
        'O2- no longer produces a dianion - if RMG-Py gained a neutral-reactant '
        'check, invert this test to assert that no reaction is generated.')
