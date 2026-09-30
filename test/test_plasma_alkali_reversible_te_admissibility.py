#!/usr/bin/env python
# encoding: utf-8

"""
Reactor admissibility of the three Te-dependent recombinations in ``PlasmaAlkali``.

`PlasmaReactor._validate_reactions` (``rmgpy/solver/plasma.pyx``) refuses a
**reversible** electron-temperature-dependent reaction at ``initialize_model`` with
``NonEquilibriumReverseRateError`` (Ruling 1: ``kf(Tgas, Te) / Keq(Tgas)`` combines two
incompatible thermal closures). This refusal is reached only at reactor initialisation —
the library loads, balances and evaluates rates without it — so a load-only check misses
it entirely.

The three ``TwoTemperaturePlasma`` recombinations carried by I-157 are the only reversible
Te-dependent entries in the library; each was marked irreversible (``=>``, ``reversible =
False``). For each, this test shows the carried (irreversible) form is ADMITTED past the
reverse-rate gate, and — the negative control that makes this a real check — that the same
reaction forced reversible is still REFUSED with ``NonEquilibriumReverseRateError``.

The reverse of e.g. ``Lip + e- -> Li`` is lithium ionisation, already carried explicitly as
``Li + e- => Lip + e- + e-`` (index 38; Na 39, Mg 41), so the reversible form double-counted
ionisation. Marking these irreversible removes both the double-count and the engine refusal.
"""

import os

import pytest

import rmgpy.data.rmg as rmg_data_module
from rmgpy import settings
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.exceptions import NonEquilibriumReverseRateError
from rmgpy.reaction import Reaction
from rmgpy.solver.plasma import PlasmaReactor
from rmgpy.thermo import ThermoData

# The three reversible Te-dependent recombinations marked irreversible by I-157.
IRREVERSIBLE_TE_RECOMBINATIONS = [
    "Lip + e- => Li",
    "Nap + e- => Na",
    "Mgp2 + e- => Mgp",
]

T_GAS = 1000.0     # K
T_E = 11604.5      # K (~1 eV)
P0 = 1.0e5         # Pa


def _thermo(h298_kj):
    return ThermoData(
        Tdata=([300.0, 400.0, 500.0, 600.0, 800.0, 1000.0, 1500.0], "K"),
        Cpdata=([20.8] * 7, "J/(mol*K)"),
        H298=(h298_kj, "kJ/mol"),
        S298=(150.0, "J/(mol*K)"),
    )


def _net_charge(species):
    return sum(atom.charge for atom in species.molecule[0].atoms)


@pytest.fixture
def no_global_thermo_database():
    """Make the synthetic caller assertion independent of earlier test modules."""
    previous = rmg_data_module.database
    rmg_data_module.database = None
    try:
        yield
    finally:
        rmg_data_module.database = previous


def _load_reaction(label):
    """Load a fresh copy of one PlasmaAlkali entry as a Reaction with its kinetics."""
    libraries_dir = os.path.join(settings["database.directory"], "kinetics", "libraries")
    database = KineticsDatabase()
    database.load_libraries(libraries_dir, libraries=["PlasmaAlkali"])
    entry = {e.label: e for e in database.libraries["PlasmaAlkali"].entries.values()}[label]
    reaction = entry.item
    reaction.kinetics = entry.data  # library kinetics live on entry.data, not item.kinetics
    return reaction


def _mechanism_for(reaction):
    """Build a charge-neutral PlasmaReactor mechanism around one recombination.

    Seed the incident electron and the reactant cation(s) to net zero charge, add an
    inert neutral bath so the composition is not all-charged, and give every species a
    placeholder thermo (the reactor needs thermo to pack initial conditions).
    """
    from rmgpy.species import Species

    electron = next(s for s in reaction.reactants if s.is_electron())
    reactant_cations = [s for s in reaction.reactants if not s.is_electron()]
    bath = Species(label="Ar").from_adjacency_list("1 Ar u0 p4 c0")

    species = list(dict.fromkeys(reaction.reactants + reaction.products + [bath]))
    for i, s in enumerate(species):
        s.thermo = _thermo(float(10 * i))

    electron_amount = sum(_net_charge(c) for c in reactant_cations) * 1.0e-4
    imf = {s: 0.0 for s in species}
    imf[bath] = 1.0
    imf[electron] = electron_amount
    for c in reactant_cations:
        imf[c] = 1.0e-4

    asserted_ions = [s.label for s in species
                     if not s.is_electron() and _net_charge(s) != 0]
    reactor = PlasmaReactor(
        T_GAS, P0, imf, (T_E, "K"), n_sims=1, termination=[],
        thermo_source_assertions=asserted_ions,
    )
    return reactor, species


@pytest.mark.parametrize("label", IRREVERSIBLE_TE_RECOMBINATIONS)
def test_carried_irreversible_form_is_admitted_by_the_reactor(
        label, no_global_thermo_database):
    reaction = _load_reaction(label)
    assert reaction.reversible is False, "%s must be carried irreversible" % label
    reactor, species = _mechanism_for(reaction)
    # Must not raise the reverse-rate refusal; initialize_model runs to completion.
    reactor.initialize_model(species, [reaction], [], [])


@pytest.mark.parametrize("label", IRREVERSIBLE_TE_RECOMBINATIONS)
def test_same_reaction_reversible_is_still_refused(label, no_global_thermo_database):
    """Negative control: a check that cannot fail is not a check."""
    reaction = _load_reaction(label)
    reversible = Reaction(
        reactants=reaction.reactants,
        products=reaction.products,
        reversible=True,
        kinetics=reaction.kinetics,
    )
    reactor, species = _mechanism_for(reaction)
    with pytest.raises(NonEquilibriumReverseRateError) as excinfo:
        reactor.initialize_model(species, [reversible], [], [])
    message = str(excinfo.value)
    assert "TwoTemperaturePlasma" in message
    assert "irreversible" in message
