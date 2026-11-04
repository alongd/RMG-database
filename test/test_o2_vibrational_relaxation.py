"""Source fidelity and runtime admission checks for O2 relaxation data."""
import json
import importlib.util
import math
from pathlib import Path
import re
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / 'input/kinetics/libraries/O2VibrationalRelaxation'
LOKI = Path('/home/alon/Data/vibkin/LoKI_main.zip')


def _loki_text(name):
    with zipfile.ZipFile(LOKI) as archive:
        path = next(p for p in archive.namelist() if p.endswith('/' + name))
        return archive.read(path).decode()


def test_annusova_a3_all_coefficients_match_loki():
    source = json.loads((LIB / 'annusova2018_table_a3.json').read_text())
    text = _loki_text('oxygenMolecularVV.m')
    body = text.split('parametersMatrix = [', 1)[1].split('];', 1)[0]
    pairs = [tuple(float(x.replace('D', 'E')) for x in row)
             for row in re.findall(r'([-+]?\d+(?:\.\d*)?(?:[Ee][+-]?\d+)?)\s+'
                                   r'([-+]?\d+(?:\.\d*)?(?:[Ee][+-]?\d+)?)', body)]
    rows = source['coefficients']
    assert len(rows) == len(pairs) == 820
    assert [(row['v'], row['w']) for row in rows] == [
        (v, w) for v in range(1, 41) for w in range(v + 1, 42)]
    for row, (a, b) in zip(rows, pairs):
        assert row['w'] > row['v']
        assert row['A'] == pytest.approx(a, rel=1e-12, abs=0)
        assert row['B'] == pytest.approx(b, rel=1e-12, abs=0)


def test_esposito_coefficients_match_loki_and_temperature_bounds():
    source = json.loads((LIB / 'esposito2008_tables_2_4.json').read_text())
    text = _loki_text('oxygenAtomicVT.m')
    for index, key in enumerate(('a1', 'a2', 'a3'), 1):
        match = re.search(r'cCoeffM%d\s*=\s*\[(.*?)\];' % index, text, re.S)
        assert match, key
        actual = [[float(x) for x in line.split()]
                  for line in match.group(1).splitlines() if line.strip()]
        bins = source['coefficient_bins'][key]
        expected = [[bins[domain][j][k] for domain in ('dv_1', 'dv_2_10', 'dv_11_20', 'dv_21_30')]
                    for j in range(5) for k in range(4)]
        assert len(actual) == len(expected) == 20
        for got, want in zip(actual, expected):
            assert got == pytest.approx(want, rel=1e-12, abs=0)


def test_channel_inventory_and_source_rate_bounds():
    source = json.loads((LIB / 'annusova2018_table_a3.json').read_text())
    pairs = {(row['v'], row['w']) for row in source['coefficients']}
    assert len(pairs) == 820
    assert {(p + 1, high) for high in range(2, 11) for p in range(high - 1)} <= pairs
    # All source rates are strictly positive at both valid endpoints.
    for row in source['coefficients']:
        if row['w'] <= 10:
            for temperature in (300, 1000):
                assert 1.5 * row['A'] * temperature**row['B'] > 0
    meta = json.loads((LIB / 'sources.json').read_text())
    assert meta['o2_o2_vv']['temperature_K'] == [300, 1000]
    assert meta['o2_o_vt']['temperature_K'] == [50, 10000]


def test_source_equations_reproduce_pinned_spot_rates():
    spec = importlib.util.spec_from_file_location('o2_rate_spot_generator', ROOT / 'scripts/generate_o2_vibrational_relaxation.py')
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    a3 = json.loads((LIB / 'annusova2018_table_a3.json').read_text())
    esposito = json.loads((LIB / 'esposito2008_tables_2_4.json').read_text())
    a3_pair = next(row for row in a3['coefficients'] if (row['v'], row['w']) == (1, 2))
    assert generator.annusova_vt_rate(1, 300) == pytest.approx(7.521627413363876e-19, rel=1e-12, abs=0)
    assert 1.5 * a3_pair['A'] * 300**a3_pair['B'] == pytest.approx(4.7294020932172277e-14,
                                                                   rel=1e-12, abs=0)
    assert generator._esposito_rate(1, 1, 300, esposito) == pytest.approx(3.918954934413796e-12,
                                                                          rel=1e-12, abs=0)


def test_hong_checks_are_compared_in_the_source_reaction_direction():
    spec = importlib.util.spec_from_file_location('o2_relaxation_generator', ROOT / 'scripts/generate_o2_vibrational_relaxation.py')
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)

    vt_source = _loki_text('oxygenMolecularVT.m').replace(' ', '').replace('\n', '')
    for term in ('-2.16870e-3*v^3', '1.02950e-2*v^2', '-9.03306e-2*v',
                 '2.7813e-2*v^3', '-2.76608e-1*v^2',
                 '2.44106e-33*Tg^6.25015', '1.76911e-7*Tg^2',
                 '-4.82968e-4*Tg', '5.40946e-1'):
        assert term in vt_source

    vt_check = json.loads((LIB / 'hong2021_table_s10_check.json').read_text())
    assert vt_check['check_only']
    assert vt_check['temperatures_K'] == [300, 500, 1000]
    vt_ratios = {}
    for v, hong_rates in vt_check['same_direction_vt'].items():
        vt_ratios[int(v)] = [generator.annusova_vt_rate(int(v), T) / hong
                             for T, hong in zip(vt_check['temperatures_K'], hong_rates)]
    assert all(value > 0 for ratios in vt_ratios.values() for value in ratios)

    vv = json.loads((LIB / 'annusova2018_table_a3.json').read_text())
    vv_check = json.loads((LIB / 'hong2021_table_s9_check.json').read_text())
    levels = json.loads((ROOT / 'input/eedf/o2_vibrational/levels.json').read_text())
    energy = {level['v']: level['energy_eV'] for level in levels['levels']}
    coefficients = {(row['v'], row['w']): row for row in vv['coefficients']}
    gas_constant = 8.31446261815324
    joules_per_mole_per_eV = 96485.33212331002
    vv_ratios = {}
    for high_v, hong_reverse_rates in vv_check['high_v_partner0_to_1_high_minus1'].items():
        high_v = int(high_v)
        row = coefficients[(1, high_v)]
        delta_g_eV = energy[0] + energy[high_v] - energy[1] - energy[high_v - 1]
        ratios = []
        for T, hong_reverse in zip(vv_check['temperatures_K'], hong_reverse_rates):
            if T not in (300, 500, 1000):
                continue  # A3 must never be evaluated outside its 300-1000 K source domain.
            # Hong lists the reverse channel; use fixed-v detailed balance to put it in Table A3 direction.
            equilibrium_source_direction = math.exp(
                -delta_g_eV * joules_per_mole_per_eV / (gas_constant * T))
            hong_source_direction = hong_reverse * equilibrium_source_direction
            annusova = 1.5 * row['A'] * T**row['B']
            ratios.append(annusova / hong_source_direction)
        vv_ratios[high_v] = ratios
    assert all(value > 0 for ratios in vv_ratios.values() for value in ratios)
    assert vv_check['table_s4_present_pes_300K_high_v_partner0_to_1_high_minus1']['2'] != (
        vv_check['high_v_partner0_to_1_high_minus1']['2'][1])

    # LoKI's Esposito coefficients are identical; this ratio isolates its check-only
    # temperature-dependent degeneracy factor against the paper's constant 1/27.
    loki_to_paper = {T: 9.0 / (5.0 + 3.0 * math.exp(-227.0 / T) + math.exp(-325.9 / T))
                     for T in (50, 300, 1000, 10000)}
    print('Hong S10 / Annušová A2, Annušová/Hong same direction:',
          {v: [round(x, 3) for x in values] for v, values in vt_ratios.items()})
    print('Hong S9 / Annušová A3, Annušová/Hong same direction:',
          {v: [round(x, 3) for x in values] for v, values in vv_ratios.items()})
    print('LoKI/paper Esposito rate ratio from degeneracy factor:',
          {T: round(value, 4) for T, value in loki_to_paper.items()})


def test_real_library_loads_and_core_edge_model_accepts_o2_manifold():
    from rmgpy.data.kinetics.database import KineticsDatabase
    from rmgpy.data.thermo import ThermoDatabase
    from rmgpy.data.rmg import RMGDatabase
    import rmgpy.data.rmg as rmg_data
    from rmgpy.molecule import Molecule
    from rmgpy.species import Species
    from rmgpy.rmg.model import CoreEdgeReactionModel
    from rmgpy.data.kinetics.library import LibraryReaction
    from rmgpy.kinetics.export import fit_kinetics_data_for_export
    import numpy as np

    previous = rmg_data.database
    db = RMGDatabase()
    db.thermo = ThermoDatabase()
    db.thermo.load_libraries(str(ROOT / 'input/thermo/libraries'), ['O2Vibrational'])
    db.kinetics = KineticsDatabase()
    db.kinetics.load_libraries(str(ROOT / 'input/kinetics/libraries'), ['O2VibrationalRelaxation'])
    rmg_data.database = db
    try:
        model = CoreEdgeReactionModel()
        ground = Species(label='O2', molecule=[Molecule().from_adjacency_list(
            'multiplicity 3\n1 O u1 p2 c0 {2,S}\n2 O u1 p2 c0 {1,S}')])
        model.declare_vibrational_manifold(ground)
        fixed = db.kinetics.libraries['O2VibrationalRelaxation']
        assert len(fixed.entries) == 110
        assert sum('Table A2' in entry.short_desc for entry in fixed.entries.values()) == 10
        assert sum('Table A3' in entry.short_desc for entry in fixed.entries.values()) == 45
        assert sum('Esposito' in entry.short_desc for entry in fixed.entries.values()) == 55
        sample = next(entry for entry in fixed.entries.values() if entry.label.startswith('O2v1 + O2v1'))
        assert sample.item.reversible
        assert sample.data.get_rate_coefficient(300) > 0
        assert sample.data.get_rate_coefficient(1000) > 0
        with pytest.raises(ValueError, match='Unable to compute rate coefficient at 1000.01 K'):
            sample.data.get_rate_coefficient(1000.01)
        admitted, is_new = model.make_new_reaction(LibraryReaction(
            index=sample.index, reactants=sample.item.reactants, products=sample.item.products,
            reversible=sample.item.reversible, kinetics=sample.data,
            library='O2VibrationalRelaxation', entry=sample))
        assert is_new
        reverse = admitted.generate_reverse_rate_coefficient()
        for temperature in sample.data.Tdata.value_si:
            forward_rate = sample.data.get_rate_coefficient(float(temperature))
            reverse_rate = reverse.get_rate_coefficient(float(temperature))
            equilibrium = admitted.get_equilibrium_constant(float(temperature))
            assert reverse_rate * equilibrium == pytest.approx(forward_rate, rel=1e-12, abs=0)
        vt = next(entry for entry in fixed.entries.values() if 'Table A2' in entry.short_desc)
        atomic = next(entry for entry in fixed.entries.values() if 'Esposito' in entry.short_desc)
        with pytest.raises(ValueError, match='Unable to compute rate coefficient at 299.99 K'):
            vt.data.get_rate_coefficient(299.99)
        with pytest.raises(ValueError, match='Unable to compute rate coefficient at 49.99 K'):
            atomic.data.get_rate_coefficient(49.99)
        by_source = {}
        for entry in fixed.entries.values():
            fitted = fit_kinetics_data_for_export(entry.data, n_gas=2)
            source = entry.short_desc
            original = np.array(entry.data.kdata.value_si)
            temperatures = entry.data.Tdata.value_si
            fitted_rates = np.array([fitted.get_rate_coefficient(float(t)) for t in temperatures])
            relative_errors = np.abs(fitted_rates / original - 1.0)
            assert relative_errors.max() <= 0.25
            by_source.setdefault(source, []).append(float(relative_errors.max()))
        for source, errors in by_source.items():
            print(f'O2 export fit {source}: {len(errors)} entries; '
                  f'max node error={100*max(errors):.6g}%; median entry max={100*np.median(errors):.6g}%; '
                  f'<=10%={sum(error <= 0.10 for error in errors)}; 10-25%={sum(0.10 < error <= 0.25 for error in errors)}')
    finally:
        rmg_data.database = previous


def test_small_rmg_job_writes_outputs(tmp_path, monkeypatch):
    from rmgpy import settings
    from rmgpy.rmg.main import RMG
    from rmgpy.exceptions import MechanismWriterError, SpeciesIdentityError
    from rmgpy.chemkin import load_chemkin_file
    from rmgpy.util import strip_yaml_notes

    monkeypatch.setattr(settings, 'require_database_directory', lambda: str(ROOT / 'input'))
    base_deck = """database(thermoLibraries=['primaryThermoLibrary', 'O2Vibrational'],
    reactionLibraries=['O2VibrationalRelaxation'], kineticsFamilies='none', kineticsDepositories=[])
species(label='O2', structure=adjacencyList('multiplicity 3\\n1 O u1 p2 c0 {2,S}\\n2 O u1 p2 c0 {1,S}'))
species(label='O2v1', structure=adjacencyList('multiplicity 3\\nvibrationallevel 1\\n1 O u1 p2 c0 {2,S}\\n2 O u1 p2 c0 {1,S}'))
vibrationalManifold(species='O2')
simpleReactor(temperature=(1000,'K'), pressure=(1.0,'bar'),
    initialMoleFractions={'O2v1': 1.0}, terminationTime=(1e-10,'s'))
simulator(atol=1e-16, rtol=1e-8)
model(toleranceMoveToCore=0.1, toleranceInterruptSimulation=1.0, maximumEdgeSpecies=20)
options(units='si', saveSimulationProfiles=True, generateOutputHTML=False, generatePlots=False,
    generateChemkin=True, generateCanteraYAML1=True, generateCanteraYAML2=True)
"""
    default_input = tmp_path / 'default_input.py'
    default_output = tmp_path / 'default_output'
    default_input.write_text(base_deck)
    default_output.mkdir()
    default_job = RMG(input_file=str(default_input), output_directory=str(default_output))
    with pytest.raises(ValueError) as rms_refusal:
        default_job.execute(max_iterations=1)
    assert str(rms_refusal.value) == (
        "Object of type <class 'rmgpy.kinetics.kineticsdata.KineticsData'> does not have a defined conversion to "
        "ReactionMechanismSimulator format")
    chemkin_path = default_output / 'chemkin' / 'chem.inp'
    assert chemkin_path.is_file()
    # Reload with the default Chemkin reader options; the dictionary and thermo are embedded.
    species, reactions = load_chemkin_file(
        str(chemkin_path), dictionary_path=str(default_output / 'chemkin' / 'species_dictionary.txt'))
    assert species and reactions

    # Disable only RMS on a second real run so both Cantera writers and the
    # Chemkin-to-Cantera path execute and expose their exact state-boundary refusals.
    cantera_input = tmp_path / 'cantera_input.py'
    cantera_output = tmp_path / 'cantera_output'
    cantera_input.write_text(base_deck.replace(
        'generateChemkin=True, generateCanteraYAML1=True',
        'generateRMSYAML=False, generateChemkin=True, generateCanteraYAML1=True'))
    cantera_output.mkdir()
    cantera_job = RMG(input_file=str(cantera_input), output_directory=str(cantera_output))
    with pytest.raises(MechanismWriterError, match='export step'):
        cantera_job.execute(max_iterations=1)
    assert (cantera_output / 'chemkin' / 'chem.inp').is_file()
    assert [(step, type(error)) for step, error in cantera_job.export_failures] == [
        ('Chemkin-to-Cantera translation (cantera_from_ck/)', SpeciesIdentityError),
        ('Direct Cantera writer end-of-run output (cantera1/, cantera2/)', SpeciesIdentityError),
    ]
    assert str(cantera_job.export_failures[0][1]) == (
        'Resolved electronic or vibrational states are not supported by '
        'rmgpy/rmg/main.py:RMG.generate_cantera_files_from_chemkin: '
        '"O2" (index=1, state=[\'|v:0\']).')
    species, reactions = load_chemkin_file(
        str(cantera_output / 'chemkin' / 'chem.inp'),
        dictionary_path=str(cantera_output / 'chemkin' / 'species_dictionary.txt'))
    assert species and reactions
    for writer in ('cantera1', 'cantera2'):
        annotated = cantera_output / writer / 'chem_annotated.yaml'
        stripped = cantera_output / writer / 'chem.yaml'
        assert annotated.is_file()
        expected = (f'Resolved electronic or vibrational states are not supported by strip_yaml_notes '
                    f'{annotated} -> {stripped}: "molecular reference" (index=-1, state=[\'|v:0\']).')
        with pytest.raises(SpeciesIdentityError) as refusal:
            strip_yaml_notes(str(annotated), str(stripped))
        assert str(refusal.value) == expected
