#!/usr/bin/env python
# encoding: utf-8

"""
Template-matching regression test for the ``Aryl_Decarbonylation`` family.

Motivation (D-008)
------------------
The r117 terminal report concluded that ``Aryl_Decarbonylation`` "requires a
carbonyl on an aromatic ring" and therefore could never match the model's
non-aromatic cyclohexadienones. That conclusion is wrong: the family's ``Root``
group is written on the *localized keto* form and its ring atoms are ``Cd``
(non-aromatic double-bond carbon), a sibling of ``Cb`` in the atomtype tree.
The template does not merely tolerate a non-aromatic ring -- it *requires* one.

What actually gates the match is the **radical** at ``*3`` (``u1``): the family
consumes a cyclohexadienon-2-yl radical (the keto resonance form of an aryloxy
radical), not a closed-shell dienone.

This test pins both halves of that behaviour so the misdiagnosis cannot recur:
aryloxy-type radicals must match, and closed-shell carbonyls -- including the
exact r117 edge species that were cited as evidence -- must not.

Run with::

    conda activate rmg_env
    PYTHONPATH=/path/to/RMG-Py pytest testing/test_aryl_decarbonylation.py -v

or directly as a script.
"""

import os

import pytest

from rmgpy import settings

DATABASE_INPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'input'))
settings['database.directory'] = DATABASE_INPUT

from rmgpy.data.rmg import RMGDatabase  # noqa: E402  (must follow the settings override)
from rmgpy.molecule.atomtype import ATOMTYPES  # noqa: E402
from rmgpy.species import Species  # noqa: E402


# Aryloxy-type radicals: the keto resonance form carries the cyclohexadienon-2-yl
# motif the Root group is written on. Every one of these must decarbonylate.
SHOULD_MATCH = [
    ('phenoxy (training anchor)', '[O]c1ccccc1'),
    ('p-cresoxy (r117 deck seed)', '[O]c1ccc(C)cc1'),
    ('m-cresoxy (r117 deck seed)', '[O]c1cccc(C)c1'),
    ('dimethylphenoxy (r117 species 3606)', 'Cc1ccc(C)c([O])c1'),
    ('novolac dimer aryloxy (methylene bridge ortho)', '[O]c1ccc(C)cc1Cc1ccc(C)cc1O'),
    ('hydroxyphenoxy (novolac daughter)', '[O]c1ccccc1O'),
]

# Closed-shell carbonyls, saturated ketones, and radicals whose unpaired electron
# is not alpha to a ring carbonyl. None of these may fire: a one-step ring
# contraction is not chemically defensible for any of them.
SHOULD_NOT_MATCH = [
    ('benzaldehyde (exocyclic aryl C=O)', 'O=Cc1ccccc1'),
    ('acetophenone (exocyclic aryl C=O)', 'CC(=O)c1ccccc1'),
    ('closed-shell cyclohexadienone adduct', 'CC1=CC=CC(=O)C1Cc1ccc(C)cc1O'),
    ('closed-shell 2,4-cyclohexadien-1-one', 'O=C1C=CCC=C1'),
    ('cyclohexanone (saturated)', 'O=C1CCCCC1'),
    ('cyclopentanone (saturated)', 'O=C1CCCC1'),
    ('acetone (acyclic)', 'CC(C)=O'),
    ('phenol (no radical)', 'Oc1ccccc1'),
    ('benzene (no carbonyl)', 'c1ccccc1'),
    ('cyclohexadienyl radical (no carbonyl)', '[CH]1C=CCC=C1'),
    ('r117 edge species 125407', 'CC1=CC(=O)C(C)C(Oc2[c]c(C)ccc2C)[CH]1'),
    ('r117 edge species 125409', 'CC1=CC=C(C)C2([CH]1)OC1C=C(C)C(=O)[CH]C12C'),
]


@pytest.fixture(scope='module')
def family_with_rules():
    """Family loaded the way an RMG job loads it: rate rules built from training.

    Mirrors ``rmgpy/rmg/main.py`` (``add_rules_from_training`` then
    ``fill_rules_by_averaging_up``), which is what populates ``rules.py`` at run
    time -- a bare ``RMGDatabase.load`` leaves the rule tree empty.
    """
    database = RMGDatabase()
    database.load(
        path=DATABASE_INPUT,
        thermo_libraries=['primaryThermoLibrary'],
        reaction_libraries=[],
        seed_mechanisms=[],
        kinetics_families=['Aryl_Decarbonylation'],
        kinetics_depositories=['training'],
        depository=False,
        solvation=False,
        surface=False,
    )
    fam = database.kinetics.families['Aryl_Decarbonylation']
    fam.add_rules_from_training(thermo_database=database.thermo)
    fam.fill_rules_by_averaging_up(verbose=False)
    return fam


def test_root_rule_matches_lin_and_lin(family_with_rules):
    """Pin the A factor corrected under D-008 (2026-08-03).

    The training entry previously carried A = 7.4e11 s^-1 while citing Lin & Lin,
    who report k = 10^(11.40) exp(-22100/T) s^-1, i.e. A = 2.51e11. After the
    correction the Root rule must read 2.51e11 / 2 (declared degeneracy) and the
    activation energy must be unchanged at 43.9 kcal/mol.
    """
    entries = [e for ents in family_with_rules.rules.entries.values() for e in ents]
    assert len(entries) == 1, 'expected exactly one Root rule, got {0}'.format(len(entries))
    rule = entries[0].data
    assert rule.A.value_si == pytest.approx(2.51e11 / 2.0, rel=1e-3)
    assert rule.E0.value_si / 4184.0 == pytest.approx(43.9, abs=0.05)
    assert rule.Tmin.value_si == pytest.approx(1000.0)
    assert rule.Tmax.value_si == pytest.approx(1580.0)


@pytest.fixture(scope='module')
def family():
    database = RMGDatabase()
    database.load(
        path=DATABASE_INPUT,
        thermo_libraries=[],
        reaction_libraries=[],
        seed_mechanisms=[],
        kinetics_families=['Aryl_Decarbonylation'],
        kinetics_depositories=['training'],
        depository=False,
        solvation=False,
        surface=False,
    )
    return database.kinetics.families['Aryl_Decarbonylation']


def _react(family, smiles):
    species = Species().from_smiles(smiles)
    species.generate_resonance_structures()
    return family.generate_reactions([species.molecule])


def test_template_is_not_aromatic():
    """The Root ring carbons are ``Cd``; aromatic ``Cb`` is a sibling, not a descendant.

    This is the direct refutation of the "requires an aromatic ring" claim.
    """
    cd_descendants = [a.label for a in ATOMTYPES['Cd'].specific]
    assert 'Cb' not in cd_descendants
    assert 'Cbf' not in cd_descendants
    # ...whereas the generic carbon atomtype (used only at *3) does subsume Cb.
    assert 'Cb' in [a.label for a in ATOMTYPES['C'].specific]


@pytest.mark.parametrize('label,smiles', SHOULD_MATCH, ids=[s[0] for s in SHOULD_MATCH])
def test_aryloxy_radicals_decarbonylate(family, label, smiles):
    reactions = _react(family, smiles)
    assert reactions, '{0} ({1}) produced no reaction'.format(label, smiles)
    for reaction in reactions:
        products = sorted(p.to_smiles() for p in reaction.products)
        assert '[C-]#[O+]' in products or '[C]=O' in products, \
            '{0} did not release CO; got {1}'.format(label, products)


@pytest.mark.parametrize('label,smiles', SHOULD_NOT_MATCH, ids=[s[0] for s in SHOULD_NOT_MATCH])
def test_non_radical_carbonyls_do_not_match(family, label, smiles):
    reactions = _react(family, smiles)
    assert not reactions, \
        '{0} ({1}) over-matched: {2}'.format(label, smiles, [str(r) for r in reactions])


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__, '-v']))
