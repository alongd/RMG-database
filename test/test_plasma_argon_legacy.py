"""Preserve all historical laws and deliberately refuse unchanged Maxwellian decks."""
from copy import deepcopy
import hashlib
from pathlib import Path

import pytest
from rmgpy.data.kinetics.database import KineticsDatabase
from rmgpy.solver.plasma import PlasmaReactor, PlasmaStateError
from rmgpy.data.rmg import RMGDatabase
import rmgpy.data.rmg as rmg_data_module
from rmgpy.data.thermo import ThermoDatabase

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope='module')
def libraries():
    db = KineticsDatabase()
    db.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=['PlasmaArgon', 'PlasmaArgonLegacy'])
    return db.libraries


def test_all_legacy_laws(libraries):
    lib = libraries['PlasmaArgonLegacy']
    assert set(lib.entries) == set(range(86, 94))
    # Hashes of native kinetics repr from the pre-migration library; independent of paths/labels.
    expected = {
        86: 'fb0e72d5a7c50fe7d0b11afa32b7d50be9ae7d22ab6de21123447f79cfbf5b25',
        87: '928fdfcb45afbb7c1eea81d22d00813f9fab55af420f632734809c907db95171',
        88: '671ec044ec3e4bea64b54e418c0cf5b4f036db66de11148dcc63163ca442c38f',
        89: '99a3ae8d449ff15a82ec6681acd735326b79479c7d27c2d5e43c8ee32781395d',
        90: 'cd51e580f3d98a62bdf4f33b4bb7aa5ff83dd6f505e86e43ace707394637e0c0',
        91: '903a21b287a9805a51d673b2d258e66a5349168bbab6c21008f3a4709e2664ca',
        92: '9430037db1048dc2f8fa24a2c7281bed5fe7a35468c9f824dc0f4de9942f4073',
        93: '32a0ee87815e1e59e03fbb6c27917cddf87fe3119199a3208133f26598ad70f3',
    }
    assert {i: hashlib.sha256(repr(e.data).encode()).hexdigest() for i, e in lib.entries.items()} == expected
    assert all(not e.item.reversible for e in lib.entries.values())
    assert {i for i, e in lib.entries.items() if e.item.duplicate} == {87, 89, 91}


def test_actual_replacement_library_refuses_without_eedf(libraries, monkeypatch):
    monkeypatch.setattr(rmg_data_module, "database", rmg_data_module.database)
    hub = RMGDatabase()
    hub.thermo = ThermoDatabase()
    hub.thermo.load_libraries(str(ROOT / 'input/thermo/libraries'), ['PlasmaThermo', 'primaryThermoLibrary'])
    entry = libraries['PlasmaArgon'].entries[86]
    rxn = deepcopy(entry.item)
    rxn.kinetics = entry.data
    core = list({s.label: s for s in rxn.reactants + rxn.products}.values())
    by_label = {s.label: s for s in core}
    for s in core:
        if s.label != 'e-':
            s.thermo = hub.thermo.get_thermo_data_from_libraries(s)[0]
    reactor = PlasmaReactor((298.15, 'K'), (666.61, 'Pa'),
        {by_label['e-']: 1e-6, by_label['Arp']: 1e-6, by_label['Ar']: .999998},
        (11604.5, 'K'), termination=[], diffusion_length=(.02, 'm'),
        ion_reduced_mobility=(1.535e-4, 'm^2/(V*s)'), wall_neutralization_products={'Arp': 'Ar'},
        thermo_source_assertions={'Arp': 'ion'})
    with pytest.raises(PlasmaStateError, match='EEDFChannel.*no active provider mapping'):
        reactor.initialize_model(core, [rxn], [], [])


def test_tracked_decks_migrated():
    decks = list((ROOT / 'docs/argon-radiative-recombination').glob('*/input.py'))
    assert len(decks) == 4
    for deck in decks:
        text = deck.read_text()
        assert "'PlasmaArgonLegacy'" in text
        assert "'PlasmaArgon'" not in text and 'PlasmaArgon:' not in text
