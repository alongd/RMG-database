#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``Plasma_Radiative_Recombination`` kinetics *family*.

The sibling suite ``test_plasma_radiative_recombination.py`` covers the reaction
*library* of the same name. This file covers the group tree, and it exists
because of I-236: the family's single root was `R u0 px c[0,+1,...]`, which

* refused every cation whose neutral is not reached by adding an unpaired
  electron -- `Ar+`, `He+`, `Ne+` -- so the family could not do the reaction it
  is named for on argon; and
* admitted 22915 of the 22936 species in this database's thermo libraries, and
  drove most of them into an atom RMG cannot type (`AtomTypeError` at 134616 of
  the 230533 centres it labelled).

All twelve family checks in ``databaseTest.py`` passed in that state, before and
after, so nothing here may lean on them. Two rules the assertions follow:

* **Assert the product, by structure.** ``len(reactions) >= 1`` passes against a
  family that was never loaded, and ``len(reactions) == 0`` passes against one
  that failed to load. Every positive test isomorphism-checks the product, and
  every negative test asserts a positive control in the same test, so a family
  that silently vanished cannot look like a family that correctly refused.
* **Prove the family loaded by a value.** ``family.electrons == -1`` and the
  root's own adjacency list are checked alongside the behaviour they explain.

Run with the database pinned by ``test/conftest.py``::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
      /home/alon/anaconda3/envs/rmg_env/bin/python -m pytest \\
      test/test_plasma_radiative_recombination_family.py -v
"""

import os

import pytest

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule import Molecule
from rmgpy.molecule.atomtype import ATOMTYPES
from rmgpy.species import Species

FAMILY = 'Plasma_Radiative_Recombination'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

#: The root's element union. A widening has to be made here as well as in
#: ``groups.py``, which is the point: see ``test_root_elements_are_bare_atomic
#: _cations_the_recipe_can_reduce``.
ROOT_ELEMENTS = ['H', 'Li', 'Na', 'K']

ROOT_ADJLIST = '1 *1 [H,Li,Na,K] u0 p0 c+1'

ADJLISTS = {
    # closed-shell atomic cations -- what this family is for
    'Li+': '1 Li u0 p0 c+1',
    'H+': '1 H u0 p0 c+1',
    'Na+': '1 Na u0 p0 c+1',
    'K+': '1 K u0 p0 c+1',
    # their neutrals
    'Li': '1 Li u1 p0 c0',
    'H': '1 H u1 p0 c0',
    'Na': '1 Na u1 p0 c0',
    'K': '1 K u1 p0 c0',
    # open-shell atomic cations -- out of the recipe's reach, see the
    # known-limitation test
    'Ar+': 'multiplicity 2\n1 Ar u1 p3 c+1',
    'He+': 'multiplicity 2\n1 He u1 p0 c+1',
    'Ne+': 'multiplicity 2\n1 Ne u1 p3 c+1',
    'Ar': '1 Ar u0 p4 c0',
    'Ar(3P2)': 'multiplicity 3\n1 Ar u2 p3 c0',
    # net-neutral species the pre-I-236 root admitted
    'CH4': """
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    'HF': """
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    # net-neutral, but carrying a formally +1 atom: the reason a charge written
    # on *1 cannot narrow a family on its own
    'CO': """
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    'CH3NO2': """
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p0 c+1 {1,S} {6,S} {7,D}
6 O u0 p3 c-1 {5,S}
7 O u0 p2 c0 {5,D}
""",
}

#: Reactant -> the neutral the family must produce from it.
EXPECTED_PRODUCT = {'Li+': 'Li', 'H+': 'H', 'Na+': 'Na', 'K+': 'K'}

#: Species that must not reach this family, and why each one is here.
EXPECTED_OUT = {
    'Ar': 'neutral argon; the pre-I-236 root matched it and built an untypeable Ar u1 p4 c-1',
    'Ar+': 'open-shell cation; the recipe would build the metastable, not ground-state Ar',
    'He+': 'open-shell cation',
    'Ne+': 'open-shell cation',
    'CH4': 'ordinary neutral; the pre-I-236 root matched it',
    'HF': 'ordinary neutral; the pre-I-236 root matched it',
    'CO': 'net-neutral with a formally +1 oxygen',
    'CH3NO2': 'net-neutral with a formally +1 nitrogen',
}


def _species(name):
    return Species(label=name).from_adjacency_list(ADJLISTS[name])


def _molecule(name):
    return Molecule().from_adjacency_list(ADJLISTS[name])


@pytest.fixture(scope='module')
def kinetics_db():
    """Load only this family, and fail loudly if the database is not pinned here."""
    assert settings['database.directory'] == THIS_DATABASE, (
        'RMG resolved database.directory to {0!r}, not this worktree ({1!r}). '
        'Without the pin these tests measure a different checkout.'.format(
            settings['database.directory'], THIS_DATABASE)
    )
    db = KineticsDatabase()
    db.load_families(os.path.join(settings['database.directory'], 'kinetics', 'families'),
                     families=[FAMILY], depositories=['training'])
    return db


@pytest.fixture(scope='module')
def family(kinetics_db):
    return kinetics_db.families[FAMILY]


def _generate(kinetics_db, name):
    return kinetics_db.generate_reactions_from_families(
        [_species(name)], products=None, only_families=[FAMILY], resonance=True)


def _root_matches(family, name):
    """True if any atom of `name` can be the family's `*1`.

    Zero generated reactions cannot distinguish "the root did not match" from
    "it matched and the recipe was rejected", so the negative tests ask the
    group tree directly as well.
    """
    root = family.groups.top[0]
    molecule = _molecule(name)
    return any(family.groups.match_node_to_structure(root, molecule, {'*1': atom})
               for atom in molecule.atoms)


def _family_is_really_loaded(family):
    """The value that proves the fixture did not hand back an empty shell."""
    return family.electrons == -1 and family.groups.top and family.groups.top[0].label == 'A'


# --------------------------------------------------------------------------
# what the family declares
# --------------------------------------------------------------------------

def test_family_declares_a_net_electron_consumption_of_one(family):
    """`electrons = -1` is the net free-electron count, and it is load-bearing.

    At 0 the product side is left unbalanced at -1 and every reaction is
    silently dropped; this value is also what every negative test below uses as
    its proof that the family is present.
    """
    assert family.electrons == -1
    assert family.reversible is False


def test_root_is_the_single_top_and_reads_as_written(family):
    assert [entry.label for entry in family.groups.top] == ['A']
    assert [entry.label for entry in family.forward_template.reactants] == ['A']
    root = family.groups.entries['A'].item
    assert root.to_adjacency_list().strip() == ROOT_ADJLIST
    assert sorted(ROOT_ELEMENTS) == sorted(
        atomtype.label for atomtype in root.atoms[0].atomtype)


def test_recipe_is_gain_radical_plus_lose_charge(family):
    """The recipe decides the scope, so it is pinned here.

    `GAIN_RADICAL + LOSE_CHARGE` puts the captured electron into an *empty*
    orbital. That is why the root demands `u0`, and why open-shell cations --
    whose captured electron must pair -- are out of this family's reach.
    """
    actions = [list(action) for action in family.forward_recipe.actions]
    assert actions == [['GAIN_RADICAL', '*1', 1], ['LOSE_CHARGE', '*1', 1]]


def test_root_elements_are_bare_atomic_cations_the_recipe_can_reduce(family):
    """Two conditions every element in the root union must meet.

    1. `u0 p0 c+1` must force zero bonds, so the group can only ever match a
       bare atomic cation. For H and the alkali metals the formal charge is
       `1 - 2p - u - bonds`, so it does. For C, N, O and the halogens it does
       not, and the group would reach inside neutral molecules.
    2. `ATOMTYPES[element].decrement_charge` must be non-empty, or `LOSE_CHARGE`
       raises `ActionError` -- the product template is built by applying the
       recipe to this very group.
    """
    root = family.groups.entries['A'].item
    labels = sorted(atomtype.label for atomtype in root.atoms[0].atomtype)
    assert labels == sorted(ROOT_ELEMENTS)
    for element in labels:
        assert ATOMTYPES[element].decrement_charge, (
            '{0} has no decrement_charge action; LOSE_CHARGE would raise'.format(element))
        cation = Molecule().from_adjacency_list('1 {0} u0 p0 c+1'.format(element))
        assert len(cation.atoms) == 1 and not cation.atoms[0].bonds, (
            '{0} u0 p0 c+1 is not forced to be a bare atom'.format(element))


# --------------------------------------------------------------------------
# what the family generates
# --------------------------------------------------------------------------

@pytest.mark.parametrize('name', sorted(EXPECTED_PRODUCT))
def test_cation_recombination_is_generated_with_the_right_product(kinetics_db, family, name):
    """A+ + e- => A, asserted by the product's structure rather than by a count."""
    assert _family_is_really_loaded(family)
    reactions = _generate(kinetics_db, name)
    assert len(reactions) == 1, (
        '{0}: expected exactly one reaction, got {1}'.format(name, len(reactions)))
    reaction = reactions[0]
    assert reaction.electrons == -1
    assert len(reaction.products) == 1
    product = reaction.products[0]
    expected = Species(label=EXPECTED_PRODUCT[name]).from_adjacency_list(
        ADJLISTS[EXPECTED_PRODUCT[name]])
    assert product.is_isomorphic(expected), (
        '{0}: product is {1!r}, expected {2!r}'.format(
            name,
            product.molecule[0].to_adjacency_list().strip(),
            expected.molecule[0].to_adjacency_list().strip()))
    assert product.molecule[0].get_net_charge() == 0
    assert product.molecule[0].get_formula() == expected.molecule[0].get_formula()


@pytest.mark.parametrize('name', sorted(EXPECTED_OUT))
def test_species_out_of_scope_are_not_matched(kinetics_db, family, name):
    """Nothing outside the cation stage reaches this family.

    The positive control is asserted in the same test: if the family had failed
    to load, `Li+` would be refused too and the negative assertion would pass
    for the wrong reason.
    """
    assert _family_is_really_loaded(family)
    assert _root_matches(family, 'Li+'), 'positive control lost: Li+ no longer matches the root'
    assert len(_generate(kinetics_db, 'Li+')) == 1, 'positive control lost: Li+ generates nothing'

    assert not _root_matches(family, name), (
        '{0} matches the root ({1})'.format(name, EXPECTED_OUT[name]))
    assert _generate(kinetics_db, name) == [], (
        '{0} generated a reaction ({1})'.format(name, EXPECTED_OUT[name]))


def test_known_limitation_open_shell_cations_need_a_recipe_this_family_has_not_got(family):
    """Why `Ar+ + e- => Ar` is not in this family, pinned so it is not "fixed" by widening.

    `Ar+` is `Ar u1 p3 c+1`. The captured electron has no empty orbital to enter
    and must pair, giving `Ar u0 p4 c0`. This family's recipe instead adds an
    unpaired electron, giving `Ar u2 p3 c0` -- atom type `Ar0e`, the metastable,
    which is **not** ground-state argon. Widening the root's radical count would
    therefore make the family generate a different reaction under this family's
    name and hand it the ground-state rate rule.

    Argon radiative recombination is carried by the sibling reaction library
    `PlasmaRadiativeRecombination`, which needs no family template.
    """
    assert _family_is_really_loaded(family)

    product = _molecule('Ar+').copy(deep=True)
    product.atoms[0].label = '*1'
    family.forward_recipe.apply_forward(product, unique=True)
    product.update(sort_atoms=False)

    ground = _molecule('Ar')
    ground.update(sort_atoms=False)
    metastable = _molecule('Ar(3P2)')
    metastable.update(sort_atoms=False)

    assert not product.is_isomorphic(ground), (
        'the recipe now reaches ground-state Ar from Ar+; this limitation is stale '
        'and the root should be revisited')
    assert product.is_isomorphic(metastable)
    assert product.atoms[0].atomtype.label == 'Ar0e'
