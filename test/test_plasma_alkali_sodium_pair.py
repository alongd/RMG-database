#!/usr/bin/env python
# encoding: utf-8

"""
The sodium cation's source and sink in ``PlasmaAlkali``.

A ratified benchmark deck downstream of the I-157 carry cannot produce or remove a
sodium cation without these two reactions:

* ``Na + e- => Nap + e- + e-`` -- electron-impact ionisation, the SOURCE. Carried from
  RMG-database branch ``99`` (entry index 39) as an ``ElectronCollisionPlasma`` cross
  section from [Golyatina2021], ionisation threshold 5.139 eV.
* ``Nap + e- => Na`` -- radiative recombination, the SINK. Refit under I-297 from
  (entry index 2)'s [VernerFerland1996] source fit as a ``TwoTemperaturePlasma`` rate, with
  ``A`` in the per-molecule unit ``cm^3/(molecule*s)``. Marked irreversible (``=>``) as
  a documented I-157 deviation from ``99``'s ``<=>``: the reversible Te-dependent form is
  refused by ``PlasmaReactor`` and double-counts the ionisation already carried at index 39
  (see ``test_plasma_alkali_reversible_te_admissibility.py``).

The suite is pinned to this worktree by ``test/conftest.py`` (``database.directory``),
and is run against the ``plasma`` RMG-Py engine, whose ``is_balanced`` exempts the free
electron from the per-element census and judges it by charge instead -- which is why an
entry whose explicit ``e-`` count changes across the arrow now loads.
"""

import os

import pytest

from rmgpy import settings
from rmgpy.constants import Na as AVOGADRO
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.kinetics import ElectronCollisionPlasma, TwoTemperaturePlasma
from rmgpy.quantity import Quantity

SODIUM_IONISATION = "Na + e- => Nap + e- + e-"
SODIUM_RECOMBINATION = "Nap + e- => Na"


@pytest.fixture(scope="module")
def alkali_by_label():
    """Load ``PlasmaAlkali`` from the pinned worktree and key its entries by label."""
    libraries_dir = os.path.join(settings["database.directory"], "kinetics", "libraries")
    database = KineticsDatabase()
    database.load_libraries(libraries_dir, libraries=["PlasmaAlkali"])
    library = database.libraries["PlasmaAlkali"]
    return {entry.label: entry for entry in library.entries.values()}


def test_sodium_recombination_loads_with_verner_ferland_rate_and_molecule_units(alkali_by_label):
    assert SODIUM_RECOMBINATION in alkali_by_label, (
        "the sodium cation's sink %r is not carried" % SODIUM_RECOMBINATION
    )
    entry = alkali_by_label[SODIUM_RECOMBINATION]
    rate = entry.data

    assert isinstance(rate, TwoTemperaturePlasma)
    # Rate parameters are the I-297 fit to the entry's Verner--Ferland source formula.
    assert rate.A.value == pytest.approx(1.011729261e-09, rel=1e-12)
    assert rate.n.value == pytest.approx(-0.9282916514, rel=1e-12)
    assert rate.Ea_g.value_si == pytest.approx(2232.004585, rel=1e-12)
    assert rate.Ea_g.value_si == pytest.approx(rate.Ea_e.value_si, rel=1e-12)
    # Units carried verbatim: the coefficient is per-molecule, not per-mole.
    assert rate.A.units == "cm^3/(molecule*s)"
    assert entry.short_desc == "[VernerFerland1996]"
    # The reaction balances on the plasma engine (charge -1 = -1).
    assert entry.item.is_balanced()
    # Carried irreversible (I-157 deviation from 99's reversible form).
    assert entry.item.reversible is False


def test_sodium_ionisation_loads_with_golyatina_cross_section_and_threshold(alkali_by_label):
    assert SODIUM_IONISATION in alkali_by_label, (
        "the sodium cation's source %r is not carried" % SODIUM_IONISATION
    )
    entry = alkali_by_label[SODIUM_IONISATION]
    rate = entry.data

    assert isinstance(rate, ElectronCollisionPlasma)
    assert entry.item.reversible is False
    # Cross section carried verbatim from branch 99, entry index 39.
    assert rate.energies.units == "eV/molecule"
    assert rate.sigma.units == "m^2"
    assert rate.energies.value[0] == pytest.approx(5.14, rel=1e-12)  # threshold 5.139 eV
    assert rate.sigma.value[0] == pytest.approx(0.0, abs=1e-30)
    assert rate.sigma.value[1] == pytest.approx(8.28e-22, rel=1e-12)
    assert entry.short_desc == "[Golyatina2021]"
    assert entry.item.is_balanced()


def test_molecule_and_mol_rate_units_differ_by_avogadro_and_neither_raises():
    """
    The recombination is carried in ``cm^3/(molecule*s)``; the same numeral in
    ``cm^3/(mol*s)`` is a different physical rate, larger by Avogadro's number. Both
    unit strings parse without raising, so the ``molecule`` spelling is not an accident
    that happens to be read as ``mol``.
    """
    value = 1.011729261e-09
    per_molecule = Quantity(value, "cm^3/(molecule*s)")
    per_mole = Quantity(value, "cm^3/(mol*s)")
    assert per_molecule.value_si / per_mole.value_si == pytest.approx(AVOGADRO, rel=1e-9)
