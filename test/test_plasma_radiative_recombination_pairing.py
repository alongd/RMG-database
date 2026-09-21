#!/usr/bin/env python
# encoding: utf-8

"""
Unit tests for the ``Plasma_Radiative_Recombination_Pairing`` kinetics family.

This is the family that does ``Ar+ + e- => Ar``. Its sibling
``Plasma_Radiative_Recombination`` cannot, and the reason is the recipe, not the
root: a family carries exactly one recipe, the sibling's puts the captured
electron into an EMPTY orbital (``GAIN_RADICAL + LOSE_CHARGE``), and argon's
captured electron has to PAIR. Widening the sibling's root instead produces
``Ar u2 p3 c0`` -- atom type ``Ar0e``, the metastable. These tests pin both
halves: that this family makes ground-state argon, and that it does NOT make the
metastable.

The assertions follow the same two rules as the sibling suite, for the same
reasons:

* **Assert the product by structure.** Every positive test isomorphism-checks the
  product against ground-state argon AND against the metastable, because those two
  differ only in ``u``/``p`` and a count-based test cannot tell them apart.
* **Prove the family loaded, by a value, in every negative test.** A family that
  failed to load refuses everything, which looks exactly like a family that
  correctly refused.

Run with the database pinned by ``test/conftest.py``::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
      /home/alon/anaconda3/envs/rmg_env/bin/python -m pytest \\
      test/test_plasma_radiative_recombination_pairing.py -v
"""

import os

import pytest

from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.molecule import Molecule
from rmgpy.molecule.atomtype import ATOMTYPES

FAMILY = 'Plasma_Radiative_Recombination_Pairing'
SIBLING = 'Plasma_Radiative_Recombination'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

ROOT_ADJLIST = '1 *1 Ar u1 p3 c+1'
PRODUCT_TEMPLATE_ADJLIST = '1 *1 Ar u0 p4 c0'

ADJLISTS = {
    'Ar+': 'multiplicity 2\n1 Ar u1 p3 c+1',
    'Ar': '1 Ar u0 p4 c0',
    'Ar(3P2)': 'multiplicity 3\n1 Ar u2 p3 c0',
    'He+': 'multiplicity 2\n1 He u1 p0 c+1',
    'Ne+': 'multiplicity 2\n1 Ne u1 p3 c+1',
    'Li+': '1 Li u0 p0 c+1',
    'H+': '1 H u0 p0 c+1',
    'CH4': """
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    'CO': """
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
}

#: Species that must not reach this family, and why each is listed.
EXPECTED_OUT = {
    'Ar': 'neutral argon: LOSE_RADICAL has nothing to take',
    'Ar(3P2)': 'the metastable is a product of this family, never a reactant',
    'Li+': 'closed-shell cation; belongs to the sibling family',
    'H+': 'closed-shell cation; belongs to the sibling family',
    'He+': 'right mechanism, but ATOMTYPES["He"].increment_lone_pair is empty',
    'Ne+': 'right mechanism, but ATOMTYPES["Ne"].increment_lone_pair is empty',
    'CH4': 'ordinary neutral',
    'CO': 'net-neutral with a formally +1 oxygen',
}


def _molecule(name):
    return Molecule().from_adjacency_list(ADJLISTS[name])


def _updated(name):
    molecule = _molecule(name)
    molecule.update(sort_atoms=False)
    return molecule


@pytest.fixture(scope='module')
def kinetics_db():
    assert settings['database.directory'] == THIS_DATABASE, (
        'RMG resolved database.directory to {0!r}, not this worktree ({1!r}). '
        'Without the pin these tests measure a different checkout.'.format(
            settings['database.directory'], THIS_DATABASE)
    )
    db = KineticsDatabase()
    db.load_families(os.path.join(settings['database.directory'], 'kinetics', 'families'),
                     families=[FAMILY, SIBLING], depositories=['training'])
    return db


@pytest.fixture(scope='module')
def family(kinetics_db):
    return kinetics_db.families[FAMILY]


def _root_matches(family, name):
    root = family.groups.top[0]
    molecule = _molecule(name)
    return any(family.groups.match_node_to_structure(root, molecule, {'*1': atom})
               for atom in molecule.atoms)


def _family_is_really_loaded(family):
    return (family.electrons == -1
            and family.groups.top
            and family.groups.top[0].label == 'Ar_cation')


# --------------------------------------------------------------------------
# what the family declares
# --------------------------------------------------------------------------

def test_recipe_is_the_pairing_recipe_with_three_actions(family):
    """Why three actions and not two.

    `LOSE_RADICAL + GAIN_PAIR` suffices on a molecule -- `Atom.apply_action`
    carries the charge -- but a GroupAtom's declared charge is untouched by those
    two, so without `LOSE_CHARGE` the *product template* comes out `c+1`, claiming
    this family makes a cation. The product-template assertion below is what
    fails if the third action is removed.
    """
    actions = [list(action) for action in family.forward_recipe.actions]
    assert actions == [['LOSE_RADICAL', '*1', 1],
                       ['GAIN_PAIR', '*1', 1],
                       ['LOSE_CHARGE', '*1', 1]]
    assert family.electrons == -1
    assert family.reversible is False


def test_root_and_product_template_read_as_written(family):
    assert [entry.label for entry in family.groups.top] == ['Ar_cation']
    assert [e.label for e in family.forward_template.reactants] == ['Ar_cation']
    root = family.groups.entries['Ar_cation'].item
    assert root.to_adjacency_list().strip() == ROOT_ADJLIST

    product = family.forward_template.products[0].item
    assert product.to_adjacency_list().strip() == PRODUCT_TEMPLATE_ADJLIST, (
        'the product template must describe NEUTRAL argon; a `c+1` here means the '
        'LOSE_CHARGE action was dropped from the recipe')


def test_root_is_forced_to_be_a_bare_argon_cation(family):
    """`u1 p3 c+1` pins the bond count at zero by valence arithmetic.

    Argon's formal charge is `8 - 2p - u - bonds`, so this root cannot reach
    inside a molecule. That is the property the sibling family had to be narrowed
    to obtain, and it is why this one needs no narrowing.
    """
    cation = Molecule().from_adjacency_list(ADJLISTS['Ar+'])
    assert len(cation.atoms) == 1 and not cation.atoms[0].bonds


def test_helium_and_neon_are_absent_for_a_reason_that_is_checked(family):
    """He+ and Ne+ recombine by exactly this mechanism and are still not here.

    `GAIN_PAIR` needs a non-empty `increment_lone_pair` row on every atom type in
    the group. Argon has one; helium and neon do not, and a root of
    `[Ar,He,Ne] u1 px c+1` raises `ActionError` at load. If this test starts
    failing, the RMG-Py atom-type table has been filled in and the root should be
    widened to include them.
    """
    assert ATOMTYPES['Ar'].increment_lone_pair, 'argon lost its increment_lone_pair row'
    assert not ATOMTYPES['He'].increment_lone_pair, (
        'ATOMTYPES["He"].increment_lone_pair is no longer empty -- add He to this '
        'family root and delete this assertion')
    assert not ATOMTYPES['Ne'].increment_lone_pair, (
        'ATOMTYPES["Ne"].increment_lone_pair is no longer empty -- add Ne to this '
        'family root and delete this assertion')

    labels = sorted(atomtype.label for atomtype in
                    family.groups.entries['Ar_cation'].item.atoms[0].atomtype)
    assert labels == ['Ar']


def test_the_root_rule_is_the_sourced_argon_rate_and_is_marked_an_estimate(family):
    entries = family.rules.entries['Ar_cation']
    assert len(entries) == 1
    entry = entries[0]
    assert entry.rank == 10, 'the placeholder rank is load-bearing documentation'
    assert abs(entry.data.A.value_si - 1.007892e+05) / 1.007892e+05 < 1e-6
    provenance = '{0}\n{1}'.format(entry.long_desc or '', entry.short_desc or '')
    assert 'ESTIMATE' in provenance
    assert 'ShullVanSteenberg1982' in provenance
    assert 'not electron-temperature-aware' in provenance.lower() or \
           'is not electron-temperature-aware' in provenance


# --------------------------------------------------------------------------
# what the family generates
# --------------------------------------------------------------------------

def test_argon_radiative_recombination_is_generated_with_ground_state_argon(kinetics_db, family):
    """The reaction this whole ticket is named for, asserted by product structure.

    Ground state and metastable are both checked, in both directions, because a
    test that only asserted "a product came out" would pass on `Ar0e`.
    """
    assert _family_is_really_loaded(family)

    reactions = family.generate_reactions([_molecule('Ar+')])
    assert len(reactions) == 1, 'expected exactly one reaction, got {0}'.format(len(reactions))
    reaction = reactions[0]
    assert reaction.electrons == -1

    assert len(reaction.products) == 1
    product = reaction.products[0]
    product = product if isinstance(product, Molecule) else product.molecule[0]

    assert product.is_isomorphic(_updated('Ar')), (
        'product is {0!r}, expected ground-state argon'.format(
            product.to_adjacency_list().strip()))
    assert not product.is_isomorphic(_updated('Ar(3P2)')), (
        'the family produced the metastable Ar0e, not ground-state argon')
    assert product.atoms[0].atomtype.label in ('Ar0', 'Ar0s')
    assert product.get_net_charge() == 0
    assert product.get_formula() == 'Ar'


@pytest.mark.parametrize('name', sorted(EXPECTED_OUT))
def test_species_out_of_scope_are_not_matched(kinetics_db, family, name):
    """Nothing but a bare open-shell argon cation reaches this family."""
    assert _family_is_really_loaded(family)
    assert _root_matches(family, 'Ar+'), 'positive control lost: Ar+ no longer matches'
    assert len(family.generate_reactions([_molecule('Ar+')])) == 1, (
        'positive control lost: Ar+ generates nothing')

    assert not _root_matches(family, name), (
        '{0} matches the root ({1})'.format(name, EXPECTED_OUT[name]))
    assert family.generate_reactions([_molecule(name)]) == [], (
        '{0} generated a reaction ({1})'.format(name, EXPECTED_OUT[name]))


def test_the_two_families_partition_and_neither_takes_the_other_s_reaction(kinetics_db):
    """The split is only correct if it is a partition.

    Both families are loaded in the same database here, which is how a real run
    sees them; if either widened to cover the other's reactant, RMG would generate
    the same reaction twice under two family names.
    """
    pairing = kinetics_db.families[FAMILY]
    empty_orbital = kinetics_db.families[SIBLING]
    assert pairing.electrons == -1 and empty_orbital.electrons == -1

    assert len(pairing.generate_reactions([_molecule('Ar+')])) == 1
    assert empty_orbital.generate_reactions([_molecule('Ar+')]) == []

    assert len(empty_orbital.generate_reactions([_molecule('Li+')])) == 1
    assert pairing.generate_reactions([_molecule('Li+')]) == []


def test_known_limitation_the_family_generates_but_cannot_yet_be_simulated(kinetics_db, family):
    """Where the missing RMG-Py registry entry actually bites -- and where it does not.

    `generate_reactions` never consults `FAMILY_ELECTRON_PLACEMENT`, so the
    reaction above is produced with the registry exactly as RMG-Py ships it. The
    gate is `resolve_electron_placement`, which the plasma reactor calls at
    `rmgpy/solver/plasma.pyx:276`. Until

        'Plasma_Radiative_Recombination_Pairing': (1, 0)

    lands in `rmgpy/electron_placement.py`, this family cannot be simulated. When
    it lands, this test fails and should be deleted.
    """
    from rmgpy import electron_placement
    from rmgpy.exceptions import ElectronPlacementError
    from rmgpy.kinetics import Arrhenius
    from rmgpy.species import Species

    assert _family_is_really_loaded(family)
    assert FAMILY not in electron_placement.FAMILY_ELECTRON_PLACEMENT, (
        'the registry entry has landed in RMG-Py; delete this test and the '
        'corresponding paragraph in groups.py')
    assert electron_placement.FAMILY_ELECTRON_PLACEMENT[SIBLING] == (1, 0), (
        'positive control: the sibling family IS declared, so the registry is '
        'present and this is not an import problem')

    reaction = family.generate_reactions([_molecule('Ar+')])[0]
    reaction.reactants = [Species(molecule=[m]) for m in reaction.reactants]
    reaction.products = [Species(molecule=[m]) for m in reaction.products]
    reaction.kinetics = Arrhenius(A=(1.007892e+05, 'm^3/(mol*s)'), n=0.0,
                                  Ea=(0.0, 'kJ/mol'), T0=(1, 'K'))

    with pytest.raises(ElectronPlacementError) as excinfo:
        electron_placement.resolve_electron_placement(
            reaction, list(reaction.reactants) + list(reaction.products))
    assert 'has no electron-placement declaration' in str(excinfo.value)
    assert FAMILY in str(excinfo.value)
