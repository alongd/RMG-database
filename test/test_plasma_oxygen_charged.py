"""Source transcription, state identity, mutations and actual NASA production checks."""
import copy
import itertools
import json
import math
from pathlib import Path

import pytest

from rmgpy import settings
from rmgpy.constants import R as R_RUNTIME
from rmgpy.data.base import Database
from rmgpy.data.rmg import RMGDatabase
import rmgpy.data.rmg as rmg_data_module
from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy.thermo import NASA
from rmgpy.thermo.thermoengine import generate_thermo_data, process_thermo_data

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = json.loads((ROOT / 'test/plasma_oxygen_janaf_reference.json').read_text())
RATES = json.loads((ROOT / 'test/plasma_oxygen_kinetics_reference.json').read_text())
OM_NASA = json.loads((ROOT / 'test/plasma_oxygen_om_nasa_reference.json').read_text())
R = 8.31446261815324
NA = 6.02214076e23
INDICES = (31, 32, 33, 34, 38, 39, 40, 41, 42, 52, 58, 67, 80, 81, 101, 102, 103, 104, 105)
LIMITS = {'[Op]': (2.5, 2.5), '[O2p]': (3.5, 4.5), '[Om]': (2.5, 2.5),
          '[O2m]': (3.5, 4.5), '[O3m]': (4, 7)}
LIBRARY_ORDERS = tuple(itertools.permutations(('PlasmaArgon', 'PlasmaAir', 'PlasmaOxygenHeavy')))
O3_GRID = (298., 298.15, 300., *range(350, 1001, 50))


@pytest.fixture(scope='module')
def database():
    assert settings['database.directory'] == str(ROOT / 'input')
    previous = rmg_data_module.database
    rmg_data_module.database = None
    try:
        db = RMGDatabase()
        db.load(str(ROOT / 'input'),
                thermo_libraries=['PlasmaThermo', 'primaryThermoLibrary', 'electrocatThermo',
                                  'PlasmaExcitedNeutralThermo'],
                reaction_libraries=['PlasmaOxygenHeavy', 'PlasmaArgon', 'PlasmaAir'],
                kinetics_families='none', kinetics_depositories=[], seed_mechanisms=[],
                transport_libraries=[], depository=False, solvation=False, surface=False)
        yield db
    finally:
        rmg_data_module.database = previous


@pytest.mark.parametrize('label', REFERENCE)
def test_signed_electron_conversion_and_source_rows(database, label):
    source = REFERENCE[label]
    entry = database.thermo.libraries['PlasmaThermo'].entries[label]
    data = entry.data
    h_ic = source['h_ec298'] - source['charge'] * 2.5 * R * 298.15 / 1000
    assert entry.item.get_net_charge() == source['charge']
    assert entry.item.multiplicity == source['multiplicity']
    assert data.E0.value_si / 1000 == source['h0']
    if label == '[Om]':
        # A primary-read published polynomial replaces atomic ThermoData, whose
        # equal physical limits erase fine-structure Cp during RMG processing.
        assert isinstance(data, NASA)
        for poly, key in zip(data.polynomials, ('low', 'high')):
            expected = OM_NASA[key].copy()
            expected[5] += 2.5 * R * 298.15 / R_RUNTIME
            assert list(poly.coeffs) == pytest.approx(expected, rel=1e-12, abs=0)
        assert [(p.Tmin.value_si, p.Tmax.value_si) for p in data.polynomials] == [(298, 1000), (1000, 6000)]
        for t, cp in zip(source['temperatures'], source['cp']):
            assert data.get_heat_capacity(t) == pytest.approx(cp, rel=0, abs=.015)
    else:
        assert list(data.Tdata.value_si)[1:] == source['temperatures']
        assert list(data.Cpdata.value_si)[1:] == source['cp']
        assert data.Tdata.value_si[0] == 298
        slope = (source['cp'][1] - source['cp'][0]) / (source['temperatures'][1] - source['temperatures'][0])
        assert data.get_heat_capacity(298) == pytest.approx(source['cp'][0] - .15*slope, rel=0, abs=1e-8)
        assert data.get_enthalpy(298) == pytest.approx(data.H298.value_si, rel=0, abs=1e-6)
        assert data.get_entropy(298) == pytest.approx(data.S298.value_si, rel=0, abs=1e-6)
    for temperature, row in source['rows'].items():
        t = float(temperature)
        assert data.get_heat_capacity(t) == pytest.approx(row['cp'], rel=0, abs=.007 if label == '[Om]' else 1e-10)
        assert data.get_enthalpy(t)/1000 == pytest.approx(h_ic + row['dh'], rel=0, abs=.002)
        assert data.get_entropy(t) == pytest.approx(row['s'], rel=0, abs=.007 if label == '[Om]' else .003)
    assert 'ion convention' in entry.long_desc
    assert 'Grade P' in entry.long_desc or 'grade P' in entry.long_desc


def ozone_rrho(t):
    """Independent closed-form moments; no saved grid or production helper."""
    kb, h, c = 1.380649e-23, 6.62607015e-34, 299792458.
    mass = .04799875 / NA  # ATcT v1.156 Ozonide selected table
    radius, half = 1.36e-10, math.radians(111.8)/2  # Arnold p.917
    # Equal masses in a bent O-O-O geometry; axes through centre of mass.
    ix = 2*mass*radius**2*math.cos(half)**2/9
    iy = 2*mass*radius**2*math.sin(half)**2/3
    rotations = [h*h/(8*math.pi**2*kb*i) for i in (ix, iy, ix+iy)]
    vibrations = [h*c*100*nu/kb for nu in (975, 550, 880)]  # Table V experimental row
    x = [theta/t for theta in vibrations]
    qtrans = (2*math.pi*mass*kb*t/h**2)**1.5 * kb*t/1e5
    qrot = math.sqrt(math.pi)*t**1.5/(2*math.sqrt(math.prod(rotations)))
    s = R*(math.log(qtrans)+2.5+math.log(qrot)+1.5+math.log(2)
           + sum(v/math.expm1(v)-math.log1p(-math.exp(-v)) for v in x))
    h_ic = -58.47 + R*(4*t+sum(theta/math.expm1(theta/t) for theta in vibrations))/1000 - 1.5*8.683
    cp = R*(4+sum(v*v*math.exp(-v)/(1-math.exp(-v))**2 for v in x))
    return h_ic, s, cp


def assert_ozone_grid(data):
    assert list(data.Tdata.value_si) == list(O3_GRID)
    expected = [ozone_rrho(t)[2] for t in O3_GRID[1:]]
    expected.insert(0, expected[0] - .15*(expected[1]-expected[0])/1.85)
    assert list(data.Cpdata.value_si) == pytest.approx(expected, rel=0, abs=6e-10)
    for t in O3_GRID[1:]:
        h, s, cp = ozone_rrho(t)
        assert data.get_heat_capacity(t) == pytest.approx(cp, rel=0, abs=6e-10)
        # Error from integrating the sparse delivered Cp grid, measured over
        # its whole interval; analytical RRHO is the independent reference.
        assert data.get_enthalpy(t)/1000 == pytest.approx(h, rel=0, abs=.020)
        assert data.get_entropy(t) == pytest.approx(s, rel=0, abs=.050)


def test_ozonide_entire_primary_constant_derivation(database):
    entry = database.thermo.libraries['PlasmaThermo'].entries['[O3m]']
    reference = json.loads((ROOT/'test/plasma_ozone_reference.json').read_text())
    assert (reference['hf0'], reference['mass_g_mol'], reference['r_angstrom'],
            reference['angle_degrees'], reference['frequencies_cm']) == (-58.47, 47.99875, 1.36, 111.8, [975., 550., 880.])
    assert entry.data.E0.value_si/1000 == -58.47
    assert_ozone_grid(entry.data)
    assert 'DERIVED' in entry.long_desc and '10.1063/1.467745' in entry.long_desc
    assert entry.data.get_enthalpy(298.15)/1000 == pytest.approx(-60.83, rel=0, abs=.21)


def test_ozonide_grid_rejects_a_changed_unsampled_last_point(database):
    data = copy.deepcopy(database.thermo.libraries['PlasmaThermo'].entries['[O3m]'].data)
    cp = data.Cpdata.value_si.copy()
    cp[-1] *= 2
    data.Cpdata = (cp, 'J/(mol*K)')
    with pytest.raises(AssertionError):
        assert_ozone_grid(data)


@pytest.mark.parametrize('label', LIMITS)
def test_actual_production_nasa_h_s_cp_and_temperature_limits(database, label):
    entry = database.thermo.libraries['PlasmaThermo'].entries[label]
    cp0, cpinf = LIMITS[label]
    assert entry.data.Cp0.value_si == pytest.approx(cp0*R, rel=1e-12, abs=0)
    assert entry.data.CpInf.value_si == pytest.approx(cpinf*R, rel=1e-12, abs=0)
    assert (entry.data.Tmin.value_si, entry.data.Tmax.value_si) == (298, 1000 if label == '[O3m]' else 6000)
    species = Species(label=label, molecule=[entry.item.copy(deep=True)])
    species.generate_resonance_structures()
    loaded = database.thermo.get_thermo_data(species)
    assert 'Thermo library: PlasmaThermo' in loaded.comment
    nasa = process_thermo_data(species, loaded)
    species.thermo = nasa
    assert isinstance(nasa, NASA)
    imposed = (298, 6000) if label == '[Om]' else (100, 5000)
    assert (nasa.Tmin.value_si, nasa.Tmax.value_si) == imposed
    if label == '[Om]':
        assert nasa is loaded
    # Bounds reflect actual pinned RMG conversion errors, separately from
    # strict transcription checks. They reject the original Cp0=2.5R bug.
    tolerances = {'[Op]': (1, .001, .001), '[Om]': (1, .007, .007),
                  '[O2p]': (20, .060, .400), '[O2m]': (5, .010, .150),
                  '[O3m]': (25, .080, .310)}
    h_tol, s_tol, cp_tol = tolerances[label]
    for t in (298.15, 400.):
        if label == '[O3m]':
            h, s, cp = ozone_rrho(t)
        else:
            source = REFERENCE[label]
            row = source['rows'][str(t)]
            h = source['h_ec298'] - source['charge']*2.5*R*298.15/1000 + row['dh']
            s, cp = row['s'], row['cp']
        for actual, expected, tolerance in ((nasa.get_enthalpy(t), h*1000, h_tol),
                                            (nasa.get_entropy(t), s, s_tol),
                                            (nasa.get_heat_capacity(t), cp, cp_tol)):
            assert math.isfinite(actual)
            assert actual == pytest.approx(expected, rel=0, abs=tolerance)
    assert nasa.get_heat_capacity(400) > 0
    # Verify that the thermo a model carries exports without losing NASA terms.
    nasa.to_cantera()


def test_op_high_temperature_constant_cp_loss_is_disclosed(database):
    """Pin this runtime limitation at a JANAF high-T row, not just room T."""
    entry = database.thermo.libraries['PlasmaThermo'].entries['[Op]']
    species = Species(label='[Op]', molecule=[entry.item.copy(deep=True)])
    species.generate_resonance_structures()
    loaded = database.thermo.get_thermo_data(species)
    nasa = process_thermo_data(species, loaded)
    source = REFERENCE['[Op]']
    source_cp = source['cp'][source['temperatures'].index(5000.)]
    assert source_cp == 21.351  # JANAF O-002, 5000 K row
    assert loaded.get_heat_capacity(5000.) == pytest.approx(source_cp, rel=0, abs=1e-10)
    assert nasa.get_heat_capacity(5000.) == pytest.approx(2.5*R, rel=0, abs=1e-9)
    error_percent = 100*(nasa.get_heat_capacity(5000.)/source_cp-1)
    assert error_percent == pytest.approx(-2.64551335043572, rel=0, abs=.00001)
    assert 'constant' in entry.long_desc and '5000 K' in entry.long_desc


def admit_combined_plasma_libraries(database, order):
    """Return only reactions actually admitted, never requested substitutes."""
    from rmgpy.rmg.model import CoreEdgeReactionModel

    model = CoreEdgeReactionModel()
    for name in order:
        for loaded in database.kinetics.libraries[name].get_library_reactions():
            # Identity admission uses the production method. Unrelated legacy
            # thermo and family estimates are outside this check.
            model.make_new_reaction(loaded, generate_thermo=False, generate_kinetics=False)
    species = [s for group in model.species_dict.values() for s in group]
    electrons = [s for s in species if s.is_electron()]
    assert len(electrons) == 1
    electron = electrons[0]
    assert electron.molecule[0].multiplicity == 2
    assert electron.molecule[0].atoms[0].radical_electrons == 1
    for name in order:
        for entry in database.kinetics.libraries[name].entries.values():
            for loaded in entry.item.reactants + entry.item.products:
                if loaded.is_electron():
                    assert model.check_for_existing_species(loaded.molecule[0]) is electron
    for reaction in model.new_reaction_list:
        assert all(s is electron for s in reaction.reactants + reaction.products if s.is_electron())
    detachment = [r for r in model.new_reaction_list
                  if r.library == 'PlasmaOxygenHeavy' and any(s.is_electron() for s in r.products)]
    return model, electron, detachment


def measure_combined_admission(model):
    """Count surviving objects and report their actual provenance and rate laws."""
    species = [s for group in model.species_dict.values() for s in group]
    detachment = [r for r in model.new_reaction_list
                  if r.library == 'PlasmaOxygenHeavy' and any(s.is_electron() for s in r.products)]
    pair = [r for r in model.new_reaction_list
            if (r.library, r.entry.index) in (('PlasmaOxygenHeavy', 33), ('PlasmaAir', 55))]
    rows = []
    for r in pair:
        data = r.kinetics
        k = (data.get_rate_coefficient_two_temp(298.15, 17406.78)
             if hasattr(data, 'get_rate_coefficient_two_temp') else data.get_rate_coefficient(298.15))
        rows.append(dict(library=r.library, index=r.entry.index, direction=r.entry.label,
                         rate_class=type(data).__name__, rate_m3_mol_s=k))
    return dict(electrons=sum(s.is_electron() for s in species),
                admitted_reactions=len(model.new_reaction_list),
                detachment_channels=len(detachment),
                detachment_indices=sorted(r.entry.index for r in detachment),
                independent_pair_channels=len(pair), pair=rows)


def assert_independent_attachment_detachment(model, database):
    """Both opposite irreversible channels must retain their own sourced rates."""
    required = (('PlasmaOxygenHeavy', 33), ('PlasmaAir', 55))
    for library, index in required:
        matches = [r for r in model.new_reaction_list if (r.library, r.entry.index) == (library, index)]
        assert len(matches) == 1, ('independent irreversible channel lost', library, index,
                                   measure_combined_admission(model))
        reaction = matches[0]
        entry = database.kinetics.libraries[library].entries[index]
        assert reaction.entry is entry and reaction.kinetics is entry.data
        assert not reaction.reversible
        assert reaction.is_isomorphic(entry.item, either_direction=False)
        data = reaction.kinetics
        if library == 'PlasmaOxygenHeavy':
            assert_kinetics_parameters(data, RATES['33'])
            assert_particle_rates(data, RATES['33'])
        else:
            assert type(data).__name__ == 'TwoTemperaturePlasma'
            assert data.A.units == 'cm^3/(mol*s)' and data.A.value == 6.44e14
            assert data.n.value_si == -1.391
            assert data.T0.value_si == 11604.51812
            assert data.Ea_g.units == data.Ea_e.units == 'eV/molecule'
            assert data.Ea_g.value == data.Ea_e.value == 6.26
            assert (data.Tmin.value_si, data.Tmax.value_si) == (5802., 58023.)
            # Ea_g=Ea_e gives the source's pure-Te attachment law, whereas
            # entry 33 is an ordinary gas-temperature Arrhenius rate.
            for t, te in itertools.product((298.15, 400.), (11604.51812, 20888.132616)):
                expected = data.A.value_si*(te/11604.51812)**-1.391*math.exp(-data.Ea_e.value_si/(R_RUNTIME*te))
                actual = data.get_rate_coefficient_two_temp(t, te)
                assert math.isfinite(actual) and actual > 0
                assert actual == pytest.approx(expected, rel=1e-10, abs=0)
    detachment = [r for r in model.new_reaction_list
                  if r.library == 'PlasmaOxygenHeavy' and any(s.is_electron() for s in r.products)]
    assert {r.entry.index for r in detachment} == {33, 41, 42, 52}


@pytest.mark.parametrize('order', LIBRARY_ORDERS)
def test_independent_attachment_and_detachment_survive_all_library_orders(database, order):
    model, _, _ = admit_combined_plasma_libraries(database, order)
    # Deliberately a strict regression: the pinned engine fails in every
    # order. No xfail or substitution acceptance hides the missing channel.
    assert_independent_attachment_detachment(model, database)


def initialize_admitted_detachment_reactor(model, electron, reactions):
    """Check electron acceptance of the surviving subset; counts stay measured."""
    from rmgpy.solver.plasma import PlasmaReactor

    core = list(dict.fromkeys(s for r in reactions for s in r.reactants + r.products))
    arp = next(s for group in model.species_dict.values() for s in group if s.label == 'Arp')
    core.append(arp)
    for species in core:
        species.thermo = generate_thermo_data(species)
    assert all(electron.thermo.get_enthalpy(t) == 0 and electron.thermo.get_entropy(t) == 0
               and electron.thermo.get_heat_capacity(t) == 0 for t in (298.15, 400.))
    o2 = next(s for s in core if s.label == 'O2')
    reactor = PlasmaReactor(T=(298.15, 'K'), P=(5*133.322368, 'Pa'), Te=(17406.78, 'K'),
                            initial_mole_fractions={o2: 1-2e-12, arp: 1e-12, electron: 1e-12},
                            termination=[])
    reactor.initialize_model(core_species=core, core_reactions=reactions,
                             edge_species=[], edge_reactions=[])
    assert reactor.electron_species is electron
    assert len(reactor.kf) == len(reactions)
    assert all(math.isfinite(k) and k > 0 for k in reactor.kf)
    return reactor


@pytest.mark.parametrize('order', LIBRARY_ORDERS)
def test_combined_library_admission_has_one_electron_and_reactor_accepts_it(database, order):
    model, electron, reactions = admit_combined_plasma_libraries(database, order)
    # The existing same-library excitation and two effective loss channels
    # survive independently with their own kinetics; no reverse substitution.
    for index in (87, 89, 91):
        matched = [r for r in model.new_reaction_list if (r.library, r.entry.index) == ('PlasmaArgon', index)]
        assert len(matched) == 1
        source = database.kinetics.libraries['PlasmaArgon'].entries[index]
        assert matched[0].kinetics is source.data
        assert matched[0].is_isomorphic(source.item, either_direction=False)
    initialize_admitted_detachment_reactor(model, electron, reactions)


@pytest.fixture(scope='module')
def state_references():
    loader = Database()
    base = ROOT/'input/kinetics/libraries'
    air = loader.get_species(str(base/'PlasmaAir/dictionary.txt'), resonance=False)
    argon = loader.get_species(str(base/'PlasmaArgon/dictionary.txt'), resonance=False)
    expected = {key: air[key].molecule[0] for key in ('O', 'O-', 'O2', 'O2p', 'O2-', 'O3')}
    expected['O2a'] = air['O2s'].molecule[0]
    expected.update({key: argon[key].molecule[0] for key in ('Ar', 'Arp', 'Ars')})
    expected['Op'] = Molecule().from_adjacency_list('multiplicity 4\n1 O u3 p1 c+1')
    expected['e-'] = air['e-'].molecule[0]
    assert expected['e-'].to_adjacency_list() == argon['e-'].molecule[0].to_adjacency_list()
    assert not expected['Op'].is_isomorphic(air['Op'].molecule[0])
    assert expected['e-'].multiplicity == 2
    assert expected['e-'].atoms[0].radical_electrons == 1
    return expected


def assert_states(library, expected):
    encountered = set()
    for entry in library.entries.values():
        for species in entry.item.reactants + entry.item.products:
            encountered.add(species.label)
            actual, reference = species.molecule[0], expected[species.label]
            assert actual.multiplicity == reference.multiplicity
            # Graph comparison includes bonds, radicals, lone pairs and charge;
            # atom renumbering during resonance generation is immaterial.
            assert actual.is_isomorphic(reference), (actual.to_adjacency_list(), reference.to_adjacency_list())
    assert encountered == set(expected)


def test_each_actual_reaction_graph_matches_existing_state_dictionaries(database, state_references):
    library = database.kinetics.libraries['PlasmaOxygenHeavy']
    assert_states(library, state_references)
    thermo = database.thermo.libraries['PlasmaThermo'].entries
    for label, key in (('[Op]', 'Op'), ('[O2p]', 'O2p'), ('[Om]', 'O-'), ('[O2m]', 'O2-')):
        assert thermo[label].item.multiplicity == state_references[key].multiplicity
        assert thermo[label].item.is_isomorphic(state_references[key])
    assert thermo['[O3m]'].item.multiplicity == 2
    assert thermo['[O3m]'].item.is_isomorphic(Molecule().from_adjacency_list(
        'multiplicity 2\n1 O u0 p3 c-1 {2,S}\n2 O u0 p2 c0 {1,S} {3,S}\n3 O u1 p2 c0 {2,S}'))


def test_state_check_rejects_singlet_oxygen_under_ground_state_label(database, state_references):
    library = copy.deepcopy(database.kinetics.libraries['PlasmaOxygenHeavy'])
    for entry in library.entries.values():
        for species in entry.item.reactants + entry.item.products:
            if species.label == 'O2':
                species.molecule = [state_references['O2a'].copy(deep=True)]
    with pytest.raises(AssertionError):
        assert_states(library, state_references)


def test_exact_entry_inventory(database):
    assert tuple(sorted(map(int, RATES))) == INDICES
    assert tuple(sorted(database.kinetics.libraries['PlasmaOxygenHeavy'].entries)) == INDICES
    thermo = database.thermo.libraries['PlasmaThermo'].entries
    assert {label: entry.index for label, entry in thermo.items()} == {
        '[Arp]': 0, '[Hep]': 1, '[Nep]': 2, '[Ar2p]': 3,
        '[Op]': 4, '[O2p]': 5, '[Om]': 6, '[O2m]': 7, '[O3m]': 8}


def assert_particle_rates(data, source):
    temperatures = (298., 298.15, 400., 1400.) if 'second_term' in source else (298., 298.15, 400.)
    for temperature in temperatures:
        expected = source['particle_a']*(temperature/300)**source['n']
        if 'second_term' in source:
            term = source['second_term']
            expected += term['particle_a']*math.exp(-term['activation_kelvin']/temperature)
        actual = data.get_rate_coefficient(temperature)/NA**(source['order']-1)
        assert math.isfinite(actual) and actual > 0
        assert actual == pytest.approx(expected, rel=1e-10, abs=0)


def assert_kinetics_parameters(data, source):
    summed = 'second_term' in source
    assert type(data).__name__ == ('MultiArrhenius' if summed else 'Arrhenius')
    terms = data.arrhenius if summed else [data]
    assert len(terms) == (2 if summed else 1)
    for i, term in enumerate(terms):
        particle_a = source['particle_a'] if i == 0 else source['second_term']['particle_a']
        n = source['n'] if i == 0 else 0
        ea = 0 if i == 0 else source['second_term']['activation_kelvin']*R_RUNTIME
        assert term.A.value_si == pytest.approx(particle_a*NA**(source['order']-1), rel=1e-12, abs=0)
        assert term.A.units == ('cm^3/(mol*s)' if source['order'] == 2 else 'cm^6/(mol^2*s)')
        assert term.n.value_si == n
        assert term.Ea.value_si == pytest.approx(ea, rel=1e-12, abs=0)
        assert term.T0.value_si == 300
        if source['label'].startswith('O2a +'):
            assert (term.Tmin.value_si, term.Tmax.value_si) == (200, 700)
        else:
            assert term.Tmin is None and term.Tmax is None
    if summed:
        assert (data.Tmin.value_si, data.Tmax.value_si) == (300, 1400)


@pytest.mark.parametrize('index', RATES)
def test_loaded_rates_follow_particle_source_and_preserve_charge(database, index):
    source = RATES[index]
    entry = database.kinetics.libraries['PlasmaOxygenHeavy'].entries[int(index)]
    reaction = entry.item
    assert entry.label == source['label']
    assert not reaction.reversible and reaction.electrons == 0
    assert reaction.is_balanced()
    assert sum(s.molecule[0].get_net_charge() for s in reaction.reactants) == sum(
        s.molecule[0].get_net_charge() for s in reaction.products)
    assert len(reaction.reactants) == source['order']
    assert 1 <= len(reaction.products) <= 3
    assert_kinetics_parameters(entry.data, source)
    assert_particle_rates(entry.data, source)
    assert 'Grade ' + source['grade'] in entry.long_desc


@pytest.mark.parametrize('index', RATES)
@pytest.mark.parametrize('factor', (0, 2))
def test_particle_rate_assertion_rejects_zero_and_double_a(database, index, factor):
    data = copy.deepcopy(database.kinetics.libraries['PlasmaOxygenHeavy'].entries[int(index)].data)
    for term in getattr(data, 'arrhenius', [data]):
        term.A.value_si *= factor
    with pytest.raises(AssertionError):
        assert_particle_rates(data, RATES[index])


@pytest.mark.parametrize('index', RATES)
@pytest.mark.parametrize('parameter', ('n', 'Ea', 'T0'))
def test_parameter_assertion_rejects_changes(database, index, parameter):
    data = copy.deepcopy(database.kinetics.libraries['PlasmaOxygenHeavy'].entries[int(index)].data)
    for term in getattr(data, 'arrhenius', [data]):
        getattr(term, parameter).value_si += 1
    with pytest.raises(AssertionError):
        assert_kinetics_parameters(data, RATES[index])


def test_three_body_collider_is_explicit_and_is_oxygen(database):
    library = database.kinetics.libraries['PlasmaOxygenHeavy']
    for index in (80, 81):
        entry = library.entries[index]
        assert type(entry.data).__name__ == 'Arrhenius'
        assert sum(s.label == 'O2' for s in entry.item.reactants) == 1
        assert any(s.label == 'O2' for s in entry.item.products)
    assert not any('Arp' in e.label and 'O-' in e.label for e in library.entries.values())


def test_argon_channels_state_the_3p2_thermo_proxy_for_the_kinetic_lump(database):
    library = database.kinetics.libraries['PlasmaOxygenHeavy']
    for index in (103, 104, 105):
        entry = library.entries[index]
        assert '3P2 (Paschen 1s5)' in entry.long_desc
        assert '1s3 is 3P0' in entry.long_desc
        assert 'mapping assumption' in entry.long_desc
