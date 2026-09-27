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
(a) ENCODING. A ``TwoTemperaturePlasma`` with ``Ea_e != 0`` has ``Ea_g == Ea_e``, unless its
    longDesc carries the declaration ``GAS-TEMPERATURE DEPENDENCE IS PHYSICAL:`` followed by a
    justification (at least ``MIN_JUSTIFICATION_CHARS`` characters on the rest of that
    paragraph). No entry uses the escape today; it exists so that a genuinely two-temperature
    law is written down as a decision rather than slipping through as the defect above.

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
import re

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
DECLARATION = 'GAS-TEMPERATURE DEPENDENCE IS PHYSICAL:'
MIN_JUSTIFICATION_CHARS = 40

LIBRARIES_DIR = os.path.join(settings['database.directory'], 'kinetics', 'libraries')
PLASMA_LIBRARIES = sorted(name for name in os.listdir(LIBRARIES_DIR)
                          if name.startswith('Plasma')
                          and os.path.isfile(os.path.join(LIBRARIES_DIR, name, 'reactions.py')))


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


def _declares_physical_gas_temperature(entry):
    text = entry.long_desc or ''
    at = text.find(DECLARATION)
    if at < 0:
        return False
    justification = re.split(r'\n\s*\n', text[at + len(DECLARATION):], maxsplit=1)[0]
    return len(justification.strip()) >= MIN_JUSTIFICATION_CHARS


def _evaluate(kinetics, tg, te):
    """The reactor's own dispatch (``PlasmaReactor.evaluate_two_temperature_rate_coefficient``)."""
    if hasattr(kinetics, 'get_rate_coefficient_two_temp'):
        return kinetics.get_rate_coefficient_two_temp(tg, te)
    return kinetics.get_rate_coefficient_electron_temp(te)


def _effective_order(reaction):
    order = len(reaction.reactants)
    if not any(s.is_electron() for s in reaction.reactants):
        order += 1     # implicit incident electron (electron-metadata entries)
    return order


def test_the_guard_sees_every_plasma_library(plasma_entries):
    """A guard over an empty set is green for the wrong reason."""
    assert 'PlasmaAir' in PLASMA_LIBRARIES
    seen = {name for name, _ in plasma_entries}
    assert seen == set(PLASMA_LIBRARIES)
    assert sum(1 for _, entry in plasma_entries if _is_te_dependent(entry.data)) >= 40


def test_te_arrhenius_is_encoded_with_equal_gas_and_electron_activation_energies(plasma_entries):
    """Rule (a): Ea_e != 0 implies Ea_g == Ea_e, unless a justified declaration says otherwise."""
    offenders = []
    for name, entry in plasma_entries:
        k = entry.data
        if not isinstance(k, TwoTemperaturePlasma):
            continue
        ea_g, ea_e = k.Ea_g.value_si, k.Ea_e.value_si
        if ea_e == 0.0:
            continue
        if math.isclose(ea_g, ea_e, rel_tol=1e-9, abs_tol=1e-9):
            continue
        if _declares_physical_gas_temperature(entry):
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
        order = _effective_order(entry.item)
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
            if not math.isfinite(value) or value > CEILING[order]:
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


def test_the_declaration_escape_requires_a_justification():
    """Negative control for rule (a)'s escape: the bare marker does not exempt an entry."""
    class _Entry:
        pass
    bare, justified = _Entry(), _Entry()
    bare.long_desc = 'Text.\n' + DECLARATION + ' yes\n\nMore text.'
    justified.long_desc = DECLARATION + ' the source measured k(Tg, Te) in a drift tube at fixed Tg ' \
                                        'and fitted both temperatures independently.'
    assert not _declares_physical_gas_temperature(bare)
    assert _declares_physical_gas_temperature(justified)


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
