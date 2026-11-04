"""Regression coverage for the sourced Guerra N2(X,v) relaxation library."""

import importlib.util
import json
import math
import os
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/gen_n2_heavy_particle_relaxation.py'
PARAMETERS = ROOT / 'input/kinetics/libraries/N2HeavyParticleRelaxation/parameters.yaml'
RATIO_FIXTURE = ROOT / 'test/fixtures/n2_billing_ratio_fixture.json'
SPEC = importlib.util.spec_from_file_location('n2_heavy_particle_generator', SCRIPT)
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


def _small_ladder():
    return {'levels': [
        {'v': 0, 'energy_eV': 0.0, 'thermo_entry': 'N2v0'},
        {'v': 1, 'energy_eV': 0.2886, 'thermo_entry': 'N2v1'},
        {'v': 2, 'energy_eV': 0.5737, 'thermo_entry': 'N2v2'},
        {'v': 3, 'energy_eV': 0.8553, 'thermo_entry': 'N2v3'},
    ]}


def _parameters():
    return yaml.safe_load(PARAMETERS.read_bytes())


def test_source_manifest_rejects_missing_or_malformed_equations_and_hashes():
    parameters = _parameters()
    levels = _small_ladder()
    assert GENERATOR.validate(parameters, levels, 3) == 3
    malformed = json.loads(json.dumps(parameters))
    del malformed['record_source']['equations']['12']
    with pytest.raises(ValueError, match='equation transcription'):
        GENERATOR.validate(malformed, levels, 3)
    malformed = json.loads(json.dumps(parameters))
    malformed['record_source']['sha256'] = 'g' * 64
    with pytest.raises(ValueError, match='SHA-256'):
        GENERATOR.validate(malformed, levels, 3)
    with pytest.raises(ValueError, match='integer'):
        GENERATOR.validate(parameters, levels, True)


def test_rate_laws_match_guerra_equations_at_spot_conditions():
    """Eq. (12)/(20)/(21) and Eq. (14)/(22)/(23), all coefficients per molecule."""
    parameters = _parameters()
    assert GENERATOR.rate_vt(1, 300, parameters) == pytest.approx(2.0538041596515957e-21, rel=1e-12, abs=0)
    assert GENERATOR.rate_vt(2, 300, parameters) == pytest.approx(3.3083259234726304e-21, rel=1e-12, abs=0)
    assert GENERATOR.rate_vv(2, 0, 300, parameters) == pytest.approx(1.4644785866818454e-14, rel=1e-12, abs=0)


def _independent_f(y):
    if y < 21.622:
        return 0.5 * (3.0 - math.exp(-2.0 * y / 3.0)) * math.exp(-2.0 * y / 3.0)
    return 8.0 * math.sqrt(math.pi / 3.0) * y ** (7.0 / 3.0) * math.exp(-3.0 * y ** (2.0 / 3.0))


def _independent_y(gap_cm, temperature):
    hbar = 1.054571817e-34
    kb = 1.380649e-23
    hc_cm = 1.9864458571489286e-23
    reduced_mass = 28.0134 * 1.66053906660e-27 / 2.0
    length = 0.2e-10
    return abs(gap_cm) * hc_cm * math.pi * length / hbar * math.sqrt(reduced_mass / (2.0 * kb * temperature))


def _formula_reference_vt(v, temperature):
    omega, omega_xe = 2358.57, 14.324
    chi = omega_xe / omega
    gap = omega - 2.0 * omega_xe * v
    y = _independent_y(gap, temperature)
    xi = 0.2772 * temperature - 80.32 + 35.5 * ((v - 1.0) / 39.0) ** 0.8
    return (v * (1.0 - chi) / (1.0 - chi * v) * _independent_f(y)
            * 1.07e-12 * temperature ** 1.5 / xi)


def _formula_reference_vv(v, partner_low, temperature):
    omega, omega_xe = 2358.57, 14.324
    chi = omega_xe / omega
    partner_high = partner_low + 1
    gap_v = omega - 2.0 * omega_xe * v
    gap_w = omega - 2.0 * omega_xe * partner_high
    y = _independent_y(gap_v - gap_w, temperature)
    xi = (39.0625 - 1.5625 * v if v < 10 else
          25.2 + 24.1 * ((v - 10.0) / 30.0) ** 3)
    return (v * partner_high * (1.0 - chi) / (1.0 - chi * v)
            * (1.0 - chi) / (1.0 - chi * partner_high)
            * _independent_f(y) * 6.354e-17 * temperature ** 1.5 / xi)


def test_loKi_cross_check_spots_match_independent_equation_references():
    """LoKI_main.zip VT lines 54-65 and VV lines 87-104 cross-check Guerra Eqs. 10, 12, 14, 20-23."""
    parameters = _parameters()
    # These expected values are evaluated by test-local formula transcriptions above,
    # independently of the generator implementation.
    vt_spots = ((1, 300, 2.0538041596515957e-21),
                (10, 1000, 8.289462036285432e-16),
                (30, 3000, 2.3388945802125197e-11))
    for v, temperature, expected in vt_spots:
        reference = _formula_reference_vt(v, temperature)
        assert reference == pytest.approx(expected, rel=1e-12, abs=0)
        assert GENERATOR.rate_vt(v, temperature, parameters) == pytest.approx(reference, rel=1e-12, abs=0)
    vv_spots = ((1, 0, 300, 8.8043606650341175e-15),
                (3, 1, 1000, 3.1750453525706054e-13),
                (20, 19, 2000, 1.1151264053440554e-10))
    for v, partner, temperature, expected in vv_spots:
        reference = _formula_reference_vv(v, partner, temperature)
        assert reference == pytest.approx(expected, rel=1e-12, abs=0)
        # Guerra rounds Eq. (22) to 6.35; LoKI uses 6.354 in its implementation.
        assert GENERATOR.rate_vv(v, partner, temperature, parameters) == pytest.approx(reference, rel=0.001, abs=0)


def test_vv_generates_deactivating_level_as_v_and_respects_strict_ten_boundary():
    parameters = _parameters()
    assert GENERATOR.rate_vv(9, 7, 1000, parameters) == pytest.approx(_formula_reference_vv(9, 7, 1000), rel=0.001, abs=0)
    assert GENERATOR.rate_vv(10, 8, 1000, parameters) == pytest.approx(_formula_reference_vv(10, 8, 1000), rel=0.001, abs=0)
    py, _ = GENERATOR.generate(PARAMETERS.read_bytes(), json.dumps(_small_ladder()).encode(), 3)
    labels = [line.partition('=')[2].strip().strip(',"') for line in py.decode().splitlines()
              if line.strip().startswith('label =')]
    assert 'N2v2 + N2 <=> N2v1 + N2v1' in labels
    assert all(label.split(' <=> ')[0] != label.split(' <=> ')[1] for label in labels
               if label.count(' + ') == 1)


@pytest.mark.parametrize('maximum_v', [2, 3, 30])
def test_vv_channel_set_is_complete_canonical_and_identity_free(maximum_v):
    levels = {'levels': [
        {'v': v, 'energy_eV': float(v), 'thermo_entry': f'N2v{v}'}
        for v in range(maximum_v + 1)
    ]}
    py, _ = GENERATOR.generate(PARAMETERS.read_bytes(), json.dumps(levels).encode(), maximum_v)
    labels = [line.partition('=')[2].strip().strip(',"') for line in py.decode().splitlines()
              if line.strip().startswith('label =')]
    actual = set(labels) - {
        f'N2v{v} + N2 <=> {"N2" if v == 1 else f"N2v{v - 1}"} + N2'
        for v in range(1, maximum_v + 1)
    }
    expected = set()
    for v in range(2, maximum_v + 1):
        for partner in range(v - 1):
            low = 'N2' if partner == 0 else f'N2v{partner}'
            expected.add(f'N2v{v} + {low} <=> N2v{v - 1} + N2v{partner + 1}')
    assert actual == expected
    assert len(actual) == maximum_v * (maximum_v - 1) // 2
    assert all(left != right for label in actual for left, right in [label.split(' <=> ')])
    if maximum_v == 30:
        assert 'N2v30 + N2 <=> N2v29 + N2v1' in actual


@pytest.mark.parametrize(('process', 'temperature'), [('vt', 299), ('vt', 3501), ('vv', 199), ('vv', 3501)])
def test_source_temperature_bounds_refuse_instead_of_clamp(process, temperature):
    parameters = _parameters()
    with pytest.raises(ValueError, match='refuses'):
        if process == 'vt':
            GENERATOR.rate_vt(1, temperature, parameters)
        else:
            GENERATOR.rate_vv(2, 0, temperature, parameters)


def test_source_v_bounds_refuse_outside_declared_level_ranges():
    parameters = _parameters()
    with pytest.raises(ValueError, match='refuses'):
        GENERATOR.rate_vt(46, 300, parameters)
    with pytest.raises(ValueError, match='refuses'):
        GENERATOR.rate_vv(45, 44, 300, parameters)


def test_real_rmg_admission_reverse_and_billing_direction(tmp_path, monkeypatch):
    """Use loaded N2Vibrational thermo and engine reverse generation for the real library."""
    from copy import deepcopy

    import rmgpy.data.rmg as data_module
    from rmgpy.data.kinetics.database import KineticsDatabase
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy.data.thermo import ThermoDatabase
    from rmgpy.kinetics import KineticsData
    from rmgpy.rmg.model import CoreEdgeReactionModel
    from rmgpy.species import Species

    hub = RMGDatabase()
    hub.thermo = ThermoDatabase()
    hub.thermo.load_libraries(str(ROOT / 'input/thermo/libraries'), ['N2Vibrational'])
    hub.kinetics = KineticsDatabase()
    hub.kinetics.load_libraries(str(ROOT / 'input/kinetics/libraries'), ['N2HeavyParticleRelaxation'])
    monkeypatch.setattr(data_module, 'database', hub)

    library = hub.kinetics.libraries['N2HeavyParticleRelaxation']
    reactions = library.get_library_reactions()
    model = CoreEdgeReactionModel()
    model.declare_vibrational_manifold(Species(label='N2').from_smiles('N#N'))
    admitted = {}

    def admit(index):
        if index not in admitted:
            reaction = deepcopy(reactions[index])
            for species in reaction.reactants + reaction.products:
                model._apply_vibrational_manifold(species)
                if species.thermo is None:
                    species.thermo = hub.thermo.get_thermo_data(species)
            admitted[index] = model.make_new_reaction(
                reaction, check_existing=False, generate_thermo=False)[0]
        return admitted[index]

    # VT with the manifold's v=0 species; VV with it; and VV between two
    # resolved levels are all admitted from the actual generated library.
    vt = admit(0)
    vv_with_zero = admit(30)
    vv_resolved = admit(31)
    assert all(isinstance(reaction.kinetics, KineticsData)
               for reaction in (vt, vv_with_zero, vv_resolved))
    assert 'N2v0' not in {species.label for reaction in (vt, vv_with_zero, vv_resolved)
                          for species in reaction.reactants + reaction.products}

    for reaction in (vt, vv_with_zero, vv_resolved):
        reverse = reaction.generate_reverse_rate_coefficient()
        assert isinstance(reverse, KineticsData)
        for temperature in (300.0, 1000.0):
            assert reaction.get_rate_coefficient(temperature) / reverse.get_rate_coefficient(temperature) == pytest.approx(
                reaction.get_equilibrium_constant(temperature), rel=1e-12, abs=0)
    with pytest.raises(ValueError, match='KineticsData'):
        vv_with_zero.get_rate_coefficient(199.0)

    fixture = json.loads(RATIO_FIXTURE.read_text())
    for point in fixture['points']:
        if point['identity_exchange']:
            continue
        n, temperature = point['n'], point['T_K']
        vv = point['process'] == 'V-V N2-N2'
        reaction = admit(30 + (n - 2) * (n - 1) // 2 if vv else n - 1)
        current = reaction.get_rate_coefficient(temperature) / 6.02214076e23 * 1e6
        if vv:
            current /= reaction.get_equilibrium_constant(temperature)
            delta_g = (sum(species.thermo.get_free_energy(temperature) for species in reaction.products)
                       - sum(species.thermo.get_free_energy(temperature) for species in reaction.reactants))
            reference = _formula_reference_vv(n, 0, temperature) * (6.35 / 6.354)
            reference *= math.exp(delta_g / (8.31446261815324 * temperature))
        else:
            reference = _formula_reference_vt(n, temperature)
        # Normalize the stored derived comparison by an independent formula.
        # This is a portable engine-regression check, not a fresh Billing reading.
        assert point['reference_ratio'] * current / reference == pytest.approx(point['ratio'], rel=1e-7, abs=0)
        assert point['flag'] == (point['ratio'] < 0.3 or point['ratio'] > 3)


def test_live_billing_source_recomputation(monkeypatch):
    source_path = os.environ.get('N2_BILLING_SOURCE_COEFFICIENTS')
    if source_path is None:
        pytest.skip('Set N2_BILLING_SOURCE_COEFFICIENTS to the local, uncommitted Billing coefficients')
    source = json.loads(Path(source_path).read_text())
    from rmgpy.data.kinetics.database import KineticsDatabase
    from rmgpy.data.thermo import ThermoDatabase
    from rmgpy.rmg.model import CoreEdgeReactionModel
    from rmgpy.species import Species
    database = KineticsDatabase()
    database.load_libraries(str(ROOT / 'input/kinetics/libraries'), ['N2HeavyParticleRelaxation'])
    thermo = ThermoDatabase()
    thermo.load_libraries(str(ROOT / 'input/thermo/libraries'), ['N2Vibrational'])
    import rmgpy.data.rmg as data_module
    from rmgpy.data.rmg import RMGDatabase
    hub = RMGDatabase()
    hub.thermo, hub.kinetics = thermo, database
    monkeypatch.setattr(data_module, 'database', hub)
    model = CoreEdgeReactionModel()
    model.declare_vibrational_manifold(Species(label='N2').from_smiles('N#N'))
    reactions = database.libraries['N2HeavyParticleRelaxation'].get_library_reactions()
    records = {(p['process'], p['n'], p['T_K']): p for p in source['points']}
    checked = 0
    for point in json.loads(RATIO_FIXTURE.read_text())['points']:
        if point['identity_exchange']:
            continue
        n, temperature = point['n'], point['T_K']
        vv = point['process'] == 'V-V N2-N2'
        reaction = reactions[30 + (n - 2) * (n - 1) // 2 if vv else n - 1]
        for species in reaction.reactants + reaction.products:
            model._apply_vibrational_manifold(species)
            species.thermo = thermo.get_thermo_data(species)
        rate = reaction.get_rate_coefficient(temperature)
        if vv:
            rate /= reaction.get_equilibrium_constant(temperature)
        coefficient = records[(point['process'], n, temperature)]['billing_rate_cm3_molecule_s']
        assert math.isfinite(coefficient) and coefficient > 0
        assert rate / 6.02214076e23 * 1e6 / coefficient == pytest.approx(point['ratio'], rel=1e-12, abs=0)
        checked += 1
    assert checked == 152


def test_generated_reactions_are_reversible_and_use_only_forward_rates():
    parameters_raw = PARAMETERS.read_bytes()
    py, dictionary = GENERATOR.generate(parameters_raw, json.dumps(_small_ladder()).encode(), 3)
    source = py.decode()
    assert source.count('reversible = True') > 1
    assert 'reverse_kinetics' not in source
    assert 'detailed balance from the fixed-v N2Vibrational thermochemistry' in source
    assert 'N2v3' in dictionary.decode()
    assert 'Ars' not in dictionary.decode()


def test_billing_ratio_fixture_covers_all_common_temperature_points_and_flags_outliers():
    fixture = json.loads(RATIO_FIXTURE.read_text())
    assert 'billing_scaling_note' in fixture
    assert 'exothermic' in fixture['vv_direction_convention']
    points = fixture['points']
    vt = [p for p in points if p['process'] == 'V-T N2-N2']
    vv = [p for p in points if p['process'] == 'V-V N2-N2']
    assert len(vt) == 8 * 10  # Table 3, T=300..3000 K, n=1..9 and 20
    assert len(vv) == 8 * 10  # Table 4, T=200..2000 K, n=1..9 and 20
    assert {p['n'] for p in vt} == set(range(1, 10)) | {20}
    assert {p['n'] for p in vv} == set(range(1, 10)) | {20}
    assert {p['T_K'] for p in vt} == {300, 400, 500, 700, 1000, 1500, 2000, 3000}
    assert {p['T_K'] for p in vv} == {200, 300, 400, 500, 700, 1000, 1500, 2000}
    for point in points:
        assert 'billing_rate_cm3_molecule_s' not in point
        assert point['ratio'] is None if point['identity_exchange'] else (
            math.isfinite(point['ratio']) and point['ratio'] > 0)
    assert all(point['identity_exchange'] for point in vv if point['n'] == 1)


def test_named_gaps_are_explicit_and_ar_quenching_is_deferred():
    gaps = {gap['id']: gap for gap in _parameters()['record_source']['gaps']}
    assert gaps['n2_ar_vt']['status'] == 'absent'
    assert gaps['n2_n_vt']['status'] == 'out_of_scope'
    note = gaps['ar_metastable_n2_quenching']['note']
    assert 'total rate at 300 K only' in note
    assert 'product states need N2 electronic species' in note
    assert 'deferred' in note


def test_short_real_rmg_job_keeps_table_kinetics_and_writes_bounded_exports(tmp_path, monkeypatch):
    """A simple reactor uses KineticsData while Chemkin and both YAML writers emit output fits."""
    from rmgpy import settings
    from rmgpy.kinetics import KineticsData
    from rmgpy.rmg.main import RMG

    monkeypatch.setitem(settings, 'database.directory', str(ROOT / 'input'))
    deck = tmp_path / 'input.py'
    deck.write_text("""\
database(thermoLibraries=['primaryThermoLibrary', 'N2Vibrational'],
         reactionLibraries=['N2HeavyParticleRelaxation'], seedMechanisms=[],
         kineticsDepositories=[], kineticsFamilies='none', kineticsEstimator='rate rules')
species(label='N2', reactive=True, structure=SMILES('N#N'))
species(label='N2v1', reactive=True,
        structure=adjacencyList('vibrationallevel 1\\n1 N u0 p1 c0 {2,T}\\n2 N u0 p1 c0 {1,T}'))
vibrationalManifold(species='N2')
simpleReactor(temperature=(1000, 'K'), pressure=(1, 'bar'),
              initialMoleFractions={'N2': 0.99, 'N2v1': 0.01},
              terminationTime=(1e-9, 's'))
simulator(atol=1e-16, rtol=1e-8)
model(toleranceMoveToCore=0.1, toleranceInterruptSimulation=1.0)
options(generateOutputHTML=False, generatePlots=False, saveEdgeSpecies=False,
        saveSimulationProfiles=True, generateChemkin=True,
        generateCanteraYAML1=True, generateCanteraYAML2=True)
""")
    output = tmp_path / 'job'
    output.mkdir()
    job = RMG(input_file=str(deck), output_directory=str(output))
    job.execute()

    import numpy as np
    import cantera as ct
    from rmgpy.chemkin import load_chemkin_file
    from rmgpy.solver.simple import SimpleReactor

    core = job.reaction_model.core
    table_indices = [i for i, reaction in enumerate(core.reactions)
                     if isinstance(reaction.kinetics, KineticsData)]
    assert table_indices
    original_solver = job.reaction_systems[0]
    assert original_solver.t >= 1e-9
    # Initialize the compiled solver with the completed job's actual core.
    # Its kf array is the solver-facing boundary; no extension class is patched.
    solver = SimpleReactor((1000, 'K'), (1, 'bar'), original_solver.initial_mole_fractions)
    solver.initialize_model(core.species, core.reactions, [], [])
    expected = np.array([core.reactions[i].kinetics.get_rate_coefficient(1000.) for i in table_indices])
    assert len(original_solver.kf) == len(core.reactions)
    np.testing.assert_array_equal(original_solver.kf[table_indices], expected)
    np.testing.assert_array_equal(solver.kf[table_indices], expected)
    solver.advance(1e-9)
    assert solver.t >= 1e-9
    np.testing.assert_array_equal(solver.kf[table_indices], expected)
    assert (output / 'chemkin' / 'chem.inp').is_file()
    annotated = (output / 'chemkin' / 'chem_annotated.inp').read_text()
    assert 'Output-only modified Arrhenius fit' in annotated
    assert 'The source table is the record' in annotated
    loaded_species, loaded_reactions = load_chemkin_file(
        str(output / 'chemkin' / 'chem_annotated.inp'),
        str(output / 'chemkin' / 'species_dictionary.txt'))
    assert loaded_species and loaded_reactions
    for writer in ('cantera1', 'cantera2'):
        yaml_output = output / writer / 'chem.yaml'
        assert yaml_output.is_file()
        assert ct.Solution(str(yaml_output)).n_reactions > 0
        contents = yaml_output.read_text()
        assert 'maximum relative fit error' in contents
        assert 'The source table is the record' in contents
    profiles = list(output.glob('simulation*')) + list(output.glob('solver/*'))
    assert profiles

    all_reactions = job.reaction_model.core.reactions + job.reaction_model.edge.reactions

    def admitted_channel(reactant_labels, product_labels):
        reactant_labels = sorted(reactant_labels)
        product_labels = sorted(product_labels)
        return next(reaction for reaction in all_reactions
                    if sorted(species.label for species in reaction.reactants) == reactant_labels
                    and sorted(species.label for species in reaction.products) == product_labels)

    # The v=0 identity is the unresolved manifold species N2, while the fixed-v
    # library names its thermo source N2v0. Check both V-V participant patterns.
    admitted_channel(['N2', 'N2v1'], ['N2', 'N2'])
    admitted_channel(['N2', 'N2v2'], ['N2v1', 'N2v1'])
    admitted_channel(['N2v1', 'N2v3'], ['N2v2', 'N2v2'])

    # Detailed balance is checked using the real reverse generator and loaded thermo.
    balance_channel = admitted_channel(['N2', 'N2v3'], ['N2v1', 'N2v2'])
    reverse = balance_channel.generate_reverse_rate_coefficient()
    assert isinstance(reverse, KineticsData)
    for temperature in (300.0, 1000.0):
        assert balance_channel.get_rate_coefficient(temperature) / reverse.get_rate_coefficient(temperature) == pytest.approx(
            balance_channel.get_equilibrium_constant(temperature), rel=1e-12, abs=0)
