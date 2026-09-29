#!/usr/bin/env python3
# encoding: utf-8
"""
Guard the encoding of electron-temperature rate laws in every ``Plasma*`` kinetics library.

WHY THIS EXISTS (I-295)
-----------------------
``TwoTemperaturePlasma`` evaluates

    k(T, Te) = A (Te/T0)^n exp(-Ea_g/(R T)) exp(Ea_e (Te - T)/(R T Te))

so a Te-Arrhenius fit ``A Te^n exp(-E/(k Te))`` is written with ``Ea_g = Ea_e = E``: the two
gas-temperature terms then cancel identically. Writing ``Ea_g = 0`` instead leaves a factor
``exp(E/(R Tg))`` in the rate. For an ionisation threshold of ~15 eV at Tg = 298 K that factor
is ~1e254, and ``PlasmaAir`` shipped ~30 entries encoded that way (N2 ionisation evaluated to
~1e238 cm^3/s at Te = 1 eV). The library loaded, balanced and integrated without complaint,
which is why this is a test and not a review note.

THE THREE RULES, over every library whose name starts with ``Plasma``
--------------------------------------------------------------------
(a) ENCODING. A ``TwoTemperaturePlasma`` has ``Ea_g == Ea_e`` unless both are zero, or its
    exact ``(library, index)`` is in the structured ``ENCODING_EXEMPTIONS`` map below.

(b) MAGNITUDE. Every electron-temperature-dependent rate (any kinetics that sets
    ``uses_electron_temperature``), evaluated the way ``PlasmaReactor`` evaluates it --
    ``get_rate_coefficient_two_temp(Tg, Te)`` if the class has it, else
    ``get_rate_coefficient_electron_temp(Te)`` -- at Tg = 298.15 K and Te = 0.5, 1, 2, 3, 5 eV,
    is finite and below a per-order ceiling. The order counts the incident electron whether it
    is explicit (``e-`` among the reactants) or implicit (the ``electrons`` metadata of
    ``A => A+`` / ``A+ => A`` entries), because the rate coefficient carries it either way:

        effective order 2 (e + X):      k <= 1e-6  cm^3 s^-1
        effective order 3 (e + X + Y):  k <= 1e-20 cm^6 s^-1

    1e-6 cm^3/s is ~ a geometric cross section of 1e-14 cm^2 (a Bohr-orbit-sized target is
    ~1e-16) times a 5 eV electron's mean speed ~1.5e8 cm/s: no electron-impact, attachment or
    recombination coefficient in these libraries comes within an order of magnitude of it, and
    the defect it catches overshoots it by tens to hundreds of orders. The order-3 ceiling
    (three-body electron-ion recombination is ~1e-25 cm^6/s at Te = 0.5 eV) is stated for
    completeness; no Te-dependent termolecular entry exists today. An effective order other
    than 2 or 3 fails, because a Te law without an incident electron is itself a defect.

(c) DIRECTION. No reversible entry has Te-dependent kinetics. ``PlasmaReactor`` refuses them at
    ``initialize_model`` (``NonEquilibriumReverseRateError``), and that refusal is only reached
    by building a reactor, so a load-only suite never sees it.

Each rule is ONE test that collects every offender and reports them together, so the RED run
lists the whole defect rather than the first entry pytest reached.
"""

import math
import os

import pytest

from rmgpy import settings
from rmgpy.constants import Na, e as E_CHARGE, kB
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.kinetics.arrhenius import TwoTemperaturePlasma

TG = 298.15                                  # K
TE_EV = (0.5, 1.0, 2.0, 3.0, 5.0)
EV_IN_K = E_CHARGE / kB                      # 11604.518 K
CEILING = {2: 1.0e-6, 3: 1.0e-20}            # cm^3/s, cm^6/s
SI_TO_CGS_PARTICLE = {2: 1.0e6 / Na, 3: 1.0e12 / Na ** 2}   # m^3/(mol s) -> cm^3/s, ...
# The only deliberate exceptions are pinned by library and index, never by prose in an entry.
# Their source/encoding disagreement is separately tracked and must not be silently broadened.
ENCODING_EXEMPTIONS = {
    ('PlasmaAlkali', 1): 'encoding and source agreement unverified; tracked separately',
    ('PlasmaAlkali', 2): 'encoding and source agreement unverified; tracked separately',
    ('PlasmaAlkali', 45): 'encoding and source agreement unverified; tracked separately',
}

LIBRARIES_DIR = os.path.join(settings['database.directory'], 'kinetics', 'libraries')
PLASMA_LIBRARIES = sorted(name for name in os.listdir(LIBRARIES_DIR)
                          if name.startswith('Plasma')
                          and os.path.isfile(os.path.join(LIBRARIES_DIR, name, 'reactions.py')))

# Exact inventory: additions, deletions, renumbering, and label edits are all regressions.
TE_INVENTORY = {
    'PlasmaAir': ((2,'N2 + e- => N + N + e-'),(19,'O + e- => Op + e- + e-'),(20,'N + e- => Np + e- + e-'),(21,'Op + e- => O'),(22,'Np + e- => N'),(28,'O2 + e- => O2p + e- + e-'),(29,'H + e- => Hp + e- + e-'),(31,'H2 + e- => H2p + e- + e-'),(32,'OH + e- => OHp + e- + e-'),(33,'H2O + e- => H2Op + e- + e-'),(37,'O2s + e- => O2p + e- + e-'),(38,'H2O + e- => Os + H2 + e-'),(39,'O2s + e- => O + O + e-'),(40,'O2 + e- => O + Os + e-'),(41,'H2p + e- => H + H'),(44,'O2p + e- => O + Os'),(45,'O2p + e- => Os + Os'),(46,'OHp + e- => O + H'),(47,'H2Op + e- => OH + H'),(48,'H2Op + e- => O + H2'),(49,'H2Op + e- => O + H + H'),(50,'H3Op + e- => OH + H + H'),(51,'H3Op + e- => O + H2 + H'),(52,'H3Op + e- => OH + H2'),(53,'H3Op + e- => H2O + H'),(54,'HO2p + e- => O2 + H'),(55,'O2 + e- => O- + O'),(56,'H2O + e- => OH + H-'),(57,'H2 + e- => H- + H'),(58,'O2s + e- => O- + O'),(59,'H2O + e- => H2 + O-'),(60,'H2O + e- => OH- + H'),(61,'H- + e- => H + e- + e-'),(65,'OH- + e- => OH + e- + e-'),(68,'O2 + e- => O2s + e-'),(69,'O + e- => Os + e-'),(86,'Ar + e- => Arp + e- + e-'),(87,'He + e- => Hep + e- + e-'),(88,'Ne + e- => Nep + e- + e-'),(91,'Hp + e- => H'),(92,'Hep + e- => He'),(93,'Hep2 + e- => Hep'),(102,'N2 + e- => N2p + e- + e-'),(103,'H2O + e- => OH + H + e-')),
    'PlasmaAlkali': ((1,'Lip + e- => Li'),(2,'Nap + e- => Na'),(38,'Li + e- => Lip + e- + e-'),(39,'Na + e- => Nap + e- + e-'),(40,'K + e- => Kp + e- + e-'),(41,'Mg + e- => Mgp + e- + e-'),(42,'Si + e- => Sip + e- + e-'),(45,'Mgp2 + e- => Mgp')),
    'PlasmaArgon': ((86,'Ar + e- => Arp + e- + e-'),(87,'Ar + e- => Ars + e-'),(88,'Ars + e- => Arp + e- + e-'),(89,'Ars + e- => Ar + e-'),(91,'Ars + e- => Ar + e-')),
    'PlasmaArgonDimer': ((1,'Ar2p + e- => Ars + Ar'),(2,'Ar2p + e- => Arp + Ar + e-')),
    'PlasmaElectronImpactIonization': ((0,'[Li] => [Lip]'),),
    'PlasmaRadiativeRecombination': ((0,'[Lip] => [Li]'),(1,'[Arp] => [Ar]')),
}


@pytest.fixture(scope='module')
def plasma_entries():
    """``(library, entry)`` for every entry of every ``Plasma*`` library."""
    database = KineticsDatabase()
    database.load_libraries(LIBRARIES_DIR, libraries=PLASMA_LIBRARIES)
    out = []
    for name in PLASMA_LIBRARIES:
        library = database.libraries[name]
        for entry in sorted(library.entries.values(), key=lambda x: x.index):
            out.append((name, entry))
    return out


def _tag(name, entry):
    return '{0}#{1} {2}'.format(name, entry.index, entry.label)


def _is_te_dependent(kinetics):
    return bool(getattr(kinetics, 'uses_electron_temperature', False))


def _evaluate(kinetics, tg, te):
    """The reactor's own dispatch (``PlasmaReactor.evaluate_two_temperature_rate_coefficient``)."""
    if hasattr(kinetics, 'get_rate_coefficient_two_temp'):
        return kinetics.get_rate_coefficient_two_temp(tg, te)
    return kinetics.get_rate_coefficient_electron_temp(te)


def _effective_order(reaction, kinetics):
    order = len(reaction.reactants)
    if not any(s.is_electron() for s in reaction.reactants):
        # An implicit electron is valid only if reaction and kinetics both declare it.
        if not getattr(reaction, 'electrons', 0) or not getattr(kinetics, 'electrons', 0):
            return None
        order += 1
    return order


def test_the_guard_sees_every_plasma_library(plasma_entries):
    """A guard over an empty set is green for the wrong reason."""
    assert 'PlasmaAir' in PLASMA_LIBRARIES
    seen = {name for name, _ in plasma_entries}
    assert seen == set(PLASMA_LIBRARIES)
    actual = {}
    for name, entry in plasma_entries:
        if _is_te_dependent(entry.data):
            actual.setdefault(name, []).append((entry.index, entry.label))
    assert {name: tuple(items) for name, items in actual.items()} == TE_INVENTORY


def test_te_arrhenius_is_encoded_with_equal_gas_and_electron_activation_energies(plasma_entries):
    """Rule (a): Ea_e != 0 implies Ea_g == Ea_e, unless a justified declaration says otherwise."""
    offenders = []
    for name, entry in plasma_entries:
        k = entry.data
        if not isinstance(k, TwoTemperaturePlasma):
            continue
        ea_g, ea_e = k.Ea_g.value_si, k.Ea_e.value_si
        if ea_g == 0.0 and ea_e == 0.0:
            continue
        if math.isclose(ea_g, ea_e, rel_tol=1e-9, abs_tol=1e-9):
            continue
        if (name, entry.index) in ENCODING_EXEMPTIONS:
            continue
        offenders.append('{0}: Ea_g={1:.6g} J/mol, Ea_e={2:.6g} J/mol, leaves exp({3:.4g}) at Tg={4} K'.format(
            _tag(name, entry), ea_g, ea_e, (ea_e - ea_g) / (8.314462618 * TG), TG))
    assert not offenders, '{0} misencoded Te-Arrhenius entries:\n  '.format(len(offenders)) + '\n  '.join(offenders)


def test_te_rates_are_finite_and_below_the_per_order_ceiling(plasma_entries):
    """Rule (b): at Tg = 298.15 K and Te = 0.5-5 eV every Te rate is finite and <= ceiling."""
    offenders = []
    for name, entry in plasma_entries:
        k = entry.data
        if not _is_te_dependent(k):
            continue
        order = _effective_order(entry.item, k)
        if order not in CEILING:
            offenders.append('{0}: effective order {1} (a Te law needs an incident electron and '
                             'at most one other partner)'.format(_tag(name, entry), order))
            continue
        bad = []
        for te_ev in TE_EV:
            try:
                value = _evaluate(k, TG, te_ev * EV_IN_K) * SI_TO_CGS_PARTICLE[order]
            except Exception as ex:  # noqa: BLE001 -- any evaluator failure is an offender
                bad.append('Te={0} eV: raised {1}'.format(te_ev, type(ex).__name__))
                continue
            if not math.isfinite(value) or value <= 1.0e-300 or value > CEILING[order]:
                bad.append('Te={0} eV: {1:.3g}'.format(te_ev, value))
        if bad:
            offenders.append('{0} (order {1}, ceiling {2:g}): {3}'.format(
                _tag(name, entry), order, CEILING[order], '; '.join(bad)))
    assert not offenders, '{0} Te rates non-finite or above ceiling:\n  '.format(len(offenders)) + '\n  '.join(offenders)


def test_no_reversible_entry_has_te_dependent_kinetics(plasma_entries):
    """Rule (c): the plasma reactor refuses reversible Te laws; the library must not carry one."""
    offenders = [_tag(name, entry) for name, entry in plasma_entries
                 if _is_te_dependent(entry.data) and entry.item.reversible]
    assert not offenders, '{0} reversible Te-dependent entries:\n  '.format(len(offenders)) + '\n  '.join(offenders)


def test_encoding_exemptions_are_the_pinned_named_set():
    assert ENCODING_EXEMPTIONS == {
        ('PlasmaAlkali', 1): 'encoding and source agreement unverified; tracked separately',
        ('PlasmaAlkali', 2): 'encoding and source agreement unverified; tracked separately',
        ('PlasmaAlkali', 45): 'encoding and source agreement unverified; tracked separately',
    }


def test_the_ceiling_rule_fires_on_the_defect_it_exists_for():
    """Negative control for rule (b): an Ea_g = 0 ionisation law is refused; Ea_g = Ea_e passes."""
    bad = TwoTemperaturePlasma(A=(1e-8, 'cm^3/(molecule*s)'), n=0.5, Ea_g=(0.0, 'J/mol'),
                               Ea_e=(15.6, 'eV/molecule'), T0=(EV_IN_K, 'K'))
    good = TwoTemperaturePlasma(A=(1e-8, 'cm^3/(molecule*s)'), n=0.5, Ea_g=(15.6, 'eV/molecule'),
                                Ea_e=(15.6, 'eV/molecule'), T0=(EV_IN_K, 'K'))
    te = 1.0 * EV_IN_K
    assert _evaluate(bad, TG, te) * SI_TO_CGS_PARTICLE[2] > CEILING[2]
    assert _evaluate(good, TG, te) * SI_TO_CGS_PARTICLE[2] == pytest.approx(
        1e-8 * math.exp(-15.6), rel=1e-6)
