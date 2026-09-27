#!/usr/bin/env python
# encoding: utf-8

"""
Pin the noble-gas ionisation and recombination network in the ``PlasmaAir``
kinetics library against the numbers on branch ``99``, where it was authored.

``PlasmaAir`` arrived on this line as a partial carry: 42 of branch ``99``'s 94
entries, with the rest held back. The four entries asserted here are the argon and
helium cation supply --

    Ar   + e- => Arp  + e- + e-   electron-impact ionisation, threshold 15.759 eV
    He   + e- => Hep  + e- + e-   electron-impact ionisation, threshold 24.587 eV
    Hep  + e- => He               radiative recombination
    Hep2 + e- => Hep              radiative recombination

-- and a 5 torr argon simulation cannot produce a cation without the first of them.

WHY THE FULL ARRAYS ARE ASSERTED
--------------------------------
``ElectronCollisionPlasma`` carries its rate as a cross-section table, not as three
Arrhenius scalars. A carry that dropped, reordered or truncated points would still
load, still be an ``ElectronCollisionPlasma``, and still integrate -- just at the
wrong rate. So the assertions compare every energy and every sigma against the
source, rather than checking the entry merely exists. The same reason drives
asserting the recombination entries' ``A``/``n``/``Ea_e`` *and their units*:
``cm^3/(molecule*s)`` and ``cm^3/(mol*s)`` differ by Avogadro's number and neither
raises.

Labels use this branch's ``p``-for-``+`` cation spelling (``Arp``, not ``Ar+``);
``KineticsLibrary.load`` splits a reaction string on a bare ``+``, so a species whose
own label contains ``+`` is torn in half. The rates are branch ``99``'s (A, n, Ea_e);
the recombination entries' Ea_g was set equal to Ea_e by I-295.

Run::

    cd /home/alon/Code/RMG-database-i158-plasmaair
    PATH=/home/alon/anaconda3/envs/rmg_env/bin:$PATH \\
    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
      python -m pytest test/test_plasma_air_noble_gas_ionization.py -v
"""

import os

import pytest

from rmgpy import settings

LIBRARY = 'PlasmaAir'

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

# Pin before anything imports a database-reading module. RMG's rmgrc resolution ends
# in `return  # fail silently`, and the rmgrc on the runtime branch points at the
# *shared* plasma database, so leaving this to discovery would silently test a
# checkout that does not contain this carry.
settings['database.directory'] = THIS_DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase  # noqa: E402
from rmgpy.kinetics import ElectronCollisionPlasma, TwoTemperaturePlasma  # noqa: E402


# --- Branch 99's numbers, transcribed from input/kinetics/libraries/PlasmaAir/
# --- reactions.py at origin/99, entries 86, 87, 92 and 93. [Golyatina2021] for the
# --- ionisation cross-sections, [VernerFerland1996] for the recombination fits.

AR_ENERGIES = [
    15.76, 15.86, 16.26, 16.76, 17.76, 20.76, 25.76, 35.76, 45.76, 55.76, 65.76,
    75.76, 85.76, 95.76, 105.76, 155.76, 205.76, 255.76, 305.76, 355.76, 405.76,
    455.76, 505.76, 555.76, 605.76, 655.76, 705.76, 755.76, 805.76, 855.76, 905.76,
    955.76, 1005.76, 1505.76, 2005.76, 2505.76, 3005.76, 3505.76, 4005.76, 4505.76,
    5005.76, 5505.76, 6005.76, 6505.76, 7005.76, 7505.76, 8005.76, 8505.76, 9005.76,
    9505.76, 10000.00,
]
AR_SIGMA = [
    0.00e+00, 1.16e-22, 5.74e-22, 1.13e-21, 2.21e-21, 5.12e-21, 9.10e-21, 1.47e-20,
    1.81e-20, 2.03e-20, 2.16e-20, 2.23e-20, 2.27e-20, 2.29e-20, 2.28e-20, 2.15e-20,
    1.96e-20, 1.79e-20, 1.64e-20, 1.51e-20, 1.40e-20, 1.30e-20, 1.22e-20, 1.15e-20,
    1.08e-20, 1.03e-20, 9.74e-21, 9.28e-21, 8.87e-21, 8.49e-21, 8.14e-21, 7.83e-21,
    7.53e-21, 5.53e-21, 4.40e-21, 3.68e-21, 3.17e-21, 2.79e-21, 2.50e-21, 2.27e-21,
    2.08e-21, 1.92e-21, 1.78e-21, 1.67e-21, 1.57e-21, 1.48e-21, 1.40e-21, 1.33e-21,
    1.27e-21, 1.21e-21, 1.16e-21,
]

HE_ENERGIES = [
    24.59, 24.69, 25.09, 25.59, 26.59, 29.59, 34.59, 44.59, 54.59, 64.59, 74.59,
    84.59, 94.59, 104.59, 154.59, 204.59, 254.59, 304.59, 354.59, 404.59, 454.59,
    504.59, 554.59, 604.59, 654.59, 704.59, 754.59, 804.59, 854.59, 904.59, 954.59,
    1004.59, 1504.59, 2004.59, 2504.59, 3004.59, 3504.59, 4004.59, 4504.59, 5004.59,
    5504.59, 6004.59, 6504.59, 7004.59, 7504.59, 8004.59, 8504.59, 9004.59, 9504.59,
    10000.00,
]
HE_SIGMA = [
    0.00e+00, 9.15e-24, 4.54e-23, 9.01e-23, 1.77e-22, 4.21e-22, 7.77e-22, 1.33e-21,
    1.74e-21, 2.03e-21, 2.24e-21, 2.40e-21, 2.51e-21, 2.59e-21, 2.69e-21, 2.60e-21,
    2.45e-21, 2.30e-21, 2.15e-21, 2.02e-21, 1.89e-21, 1.79e-21, 1.69e-21, 1.60e-21,
    1.52e-21, 1.45e-21, 1.38e-21, 1.32e-21, 1.27e-21, 1.22e-21, 1.17e-21, 1.13e-21,
    8.29e-22, 6.58e-22, 5.47e-22, 4.69e-22, 4.12e-22, 3.67e-22, 3.31e-22, 3.02e-22,
    2.78e-22, 2.58e-22, 2.40e-22, 2.25e-22, 2.12e-22, 2.00e-22, 1.90e-22, 1.80e-22,
    1.72e-22, 1.64e-22,
]


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope='module')
def library():
    """The loaded library. Load failures surface here, not inside a test."""
    assert settings['database.directory'] == THIS_DATABASE, (
        'RMG resolved database.directory to {0!r}, not this worktree ({1!r}).'.format(
            settings['database.directory'], THIS_DATABASE))
    db = KineticsDatabase()
    db.load_libraries(os.path.join(settings['database.directory'], 'kinetics', 'libraries'),
                      libraries=[LIBRARY])
    return db.libraries[LIBRARY]


@pytest.fixture(scope='module')
def by_label(library):
    """``{label: Entry}`` over the library, so a missing entry fails on the lookup."""
    return {entry.label: entry for entry in library.entries.values()}


def _entry(by_label, label):
    assert label in by_label, (
        '{0!r} is not in {1}. {2} labels are present.'.format(
            label, LIBRARY, len(by_label)))
    return by_label[label]


# ---------------------------------------------------------------------------
# Electron-impact ionisation: the cation supply
# ---------------------------------------------------------------------------

def test_argon_ionization_is_present_with_branch_99_cross_section(by_label):
    """``Ar + e- => Arp + e- + e-`` carries [Golyatina2021]'s 51-point table."""
    entry = _entry(by_label, 'Ar + e- => Arp + e- + e-')

    assert isinstance(entry.data, ElectronCollisionPlasma), (
        'expected ElectronCollisionPlasma, got {0}'.format(type(entry.data).__name__))
    assert entry.item.reversible is False

    assert entry.data.energies.units == 'eV/molecule'
    assert entry.data.sigma.units == 'm^2'
    assert len(entry.data.energies.value) == len(AR_ENERGIES) == 51
    assert len(entry.data.sigma.value) == len(AR_SIGMA) == 51

    for got, want in zip(entry.data.energies.value, AR_ENERGIES):
        assert got == pytest.approx(want, rel=1e-9)
    for got, want in zip(entry.data.sigma.value, AR_SIGMA):
        assert got == pytest.approx(want, rel=1e-9)

    # Threshold: the table opens at 15.76 eV with a zero cross-section.
    assert entry.data.energies.value[0] == pytest.approx(15.76, rel=1e-9)
    assert entry.data.sigma.value[0] == 0.0
    assert 'Golyatina2021' in entry.short_desc


def test_helium_ionization_is_present_with_branch_99_cross_section(by_label):
    """``He + e- => Hep + e- + e-`` carries [Golyatina2021]'s 50-point table."""
    entry = _entry(by_label, 'He + e- => Hep + e- + e-')

    assert isinstance(entry.data, ElectronCollisionPlasma)
    assert entry.item.reversible is False
    assert entry.data.energies.units == 'eV/molecule'
    assert entry.data.sigma.units == 'm^2'
    assert len(entry.data.energies.value) == len(HE_ENERGIES) == 50
    assert len(entry.data.sigma.value) == len(HE_SIGMA) == 50

    for got, want in zip(entry.data.energies.value, HE_ENERGIES):
        assert got == pytest.approx(want, rel=1e-9)
    for got, want in zip(entry.data.sigma.value, HE_SIGMA):
        assert got == pytest.approx(want, rel=1e-9)

    assert entry.data.energies.value[0] == pytest.approx(24.59, rel=1e-9)
    assert entry.data.sigma.value[0] == 0.0
    assert 'Golyatina2021' in entry.short_desc


# ---------------------------------------------------------------------------
# Radiative recombination: the cation sink
# ---------------------------------------------------------------------------

@pytest.mark.parametrize('label, A, n, Ea_e_kJ', [
    ('Hep + e- => He', 1.21e-09, -0.87, 0.19),
    ('Hep2 + e- => Hep', 7.68e-09, -0.91, 0.22),
])
def test_helium_radiative_recombination_matches_branch_99(by_label, label, A, n, Ea_e_kJ):
    """[VernerFerland1996] fits, in ``cm^3/(molecule*s)`` -- not per mole."""
    entry = _entry(by_label, label)

    assert isinstance(entry.data, TwoTemperaturePlasma), (
        'expected TwoTemperaturePlasma, got {0}'.format(type(entry.data).__name__))
    assert entry.item.reversible is False

    assert entry.data.A.units == 'cm^3/(molecule*s)'
    assert entry.data.A.value == pytest.approx(A, rel=1e-9)
    assert entry.data.n.value == pytest.approx(n, rel=1e-9)
    assert entry.data.Ea_e.value_si == pytest.approx(Ea_e_kJ * 1000.0, rel=1e-6)
    # I-295: Ea_g == Ea_e, so the gas-temperature terms cancel. Branch 99 had Ea_g = 0, which
    # leaves exp(Ea_e/(R Tg)) (x1.08 at 298 K) in a pure electron-temperature process.
    assert entry.data.Ea_g.value_si == pytest.approx(Ea_e_kJ * 1000.0, rel=1e-6)
    assert entry.data.Tmin.value_si == pytest.approx(10.0)
    assert entry.data.Tmax.value_si == pytest.approx(1e9)
    assert 'VernerFerland1996' in entry.short_desc
