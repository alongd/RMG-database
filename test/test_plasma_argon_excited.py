"""Worker checks for the approved room-temperature Ar(4s) heavy network."""
from pathlib import Path

import pytest

from rmgpy import constants
from rmgpy.data.kinetics.database import KineticsDatabase

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = 'PlasmaArgonExcited'
STATES = ('Ars', 'Ar(1s4)', 'Ar(1s3)', 'Ar(1s2)')


@pytest.fixture(scope='module')
def library():
    database = KineticsDatabase()
    database.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=[LIBRARY])
    return database.libraries[LIBRARY]


def test_nitrogen_totals_and_declared_branching(library):
    # Velazco 1978 Tables I/II: per-particle totals, independently transcribed.
    totals = (3.6e-17, 0.8e-17, 1.6e-17, 5.4e-17)
    frequencies = ((58327.85136, 1166557.0272), (12961.74475, 259234.8950),
                   (25923.48949, 518469.7899), (87491.77704, 1749835.5408))
    entries = {entry.label: entry for entry in library.entries.values()}
    for state, total, expected in zip(STATES, totals, frequencies):
        branches = [entries[f'{state} + N2 => Ar + N2{product}'] for product in ('C', 'B')]
        assert sum(entry.data.A.value_si for entry in branches) == total * constants.Na
        for temperature in (298., 300.):
            rates = [entry.data.get_rate_coefficient(temperature) / constants.Na for entry in branches]
            assert sum(rates) == pytest.approx(total, rel=1e-14, abs=0)
            assert rates[0] == rates[1]
            for x_n2, frequency in zip((.01, .2), expected):
                n_n2 = x_n2 * (5 * 101325 / 760) / (constants.kB * 298)
                assert sum(rates) * n_n2 == pytest.approx(frequency, rel=2e-6)
        for entry in branches:
            assert not entry.item.reversible
            assert 'Velazco' in entry.long_desc
            assert 'AR4S_N2_PRODUCT_SPLIT' in entry.long_desc
            assert 'uncertainty' in entry.long_desc


def test_directional_argon_channels_and_eliminated_excimer(library):
    # Stankov 2022 Table 3 rows 350,351,352,354,355,356,353 (A1-A7).
    rows = (
        ('Ar(1s2) + Ar => Ar(1s3) + Ar', 4.76e-20, (7635.11575, 6169.79050)),
        ('Ar(1s3) + Ar => Ar(1s4) + Ar', 5.30e-21, (850.12843, 686.97247)),
        ('Ar(1s4) + Ar => Ars + Ar', 1.50e-20, (2406.02387, 1944.26171)),
        ('Ars + Ar => Ar(1s4) + Ar', 2.50e-21, (401.00398, 324.04362)),
        ('Ars + Ar => Ar + Ar', 1.50e-20, (2406.02387, 1944.26171)),
        ('Ars + Ar + Ar => Ar + Ar + Ar', 1.30e-44, (334.473, 218.409)),
        ('Ar(1s4) + Ar + Ar => Ar + Ar + Ar', 1.50e-45, (38.5930, 25.2010)),
    )
    entries = {entry.label: entry for entry in library.entries.values()}
    for label, source_rate, frequencies in rows:
        entry = entries[label]
        order = len(entry.item.reactants)
        assert not entry.item.reversible
        assert 'Stankov' in entry.long_desc
        assert 'REDUCED_AR4S_HEAVY_NETWORK' in entry.long_desc
        assert 'uncertainty' in entry.long_desc
        for temperature in (298., 300.):
            rate = entry.data.get_rate_coefficient(temperature) / constants.Na ** (order - 1)
            assert rate == pytest.approx(source_rate, rel=1e-14, abs=0)
            for x_n2, expected in zip((.01, .2), frequencies):
                n_ar = (1-x_n2) * (5 * 101325 / 760) / (constants.kB * 298)
                assert rate * n_ar ** (order-1) == pytest.approx(expected, rel=2e-5)


def test_pooling_matrix_and_same_state_event_stoichiometry(library):
    import numpy as np
    from itertools import combinations_with_replacement
    from rmgpy.solver.simple import SimpleReactor

    # Stankov Table 3, rows 278-287. Kolokolov & Blagoev 1993 sec. 4.1:
    # these are electron-production event constants; symmetric atom loss is 2*k*n^2.
    source_rates = (1.2e-15, 2.1e-15, 4.2e-15, 4.2e-15, 2.1e-15,
                    2.1e-15, 2.1e-15, 1.2e-15, 2.1e-15, 2.1e-15)
    reactions = {reaction.entry.label: reaction for reaction in library.get_library_reactions()}
    for (left, right), expected in zip(combinations_with_replacement(STATES, 2), source_rates):
        reaction = reactions[f'{left} + {right} => Arp + Ar + e-']
        for temperature in (298., 300.):
            assert reaction.kinetics.get_rate_coefficient(temperature)/constants.Na == pytest.approx(
                expected, rel=1e-14, abs=0)
        species = list(dict.fromkeys(reaction.reactants + reaction.products))
        by_label = {sp.label: sp for sp in species}
        fractions = {sp: (1e-6 if sp.label in (left, right) else 0.) for sp in species}
        fractions[by_label['Ar']] = 1 - sum(fractions.values())
        reactor = SimpleReactor((298, 'K'), (5 * 101325 / 760, 'Pa'), fractions)
        reactor.initialize_model(species, [reaction], [], [])
        y = reactor.y.copy()
        reactor.residual(0, y, np.zeros_like(y))
        rate = reactor.core_reaction_rates[0]
        assert rate > 0
        for sp in species:
            net = reaction.products.count(sp) - reaction.reactants.count(sp)
            assert reactor.core_species_rates[species.index(sp)] == pytest.approx(net * rate, rel=1e-12, abs=0)
        concentrations = y / reactor.V
        expected_event = expected * constants.Na * concentrations[species.index(by_label[left])] * concentrations[species.index(by_label[right])]
        assert rate == pytest.approx(expected_event, rel=1e-12, abs=0)


def test_radiative_closure_and_library_coexistence(library):
    from rmgpy.kinetics import Arrhenius

    entries = {entry.label: entry for entry in library.entries.values()}
    for label, expected in [('N2C => N2B', 2.74e7), ('N2B => N2A', 2e5)]:
        entry = entries[label]
        assert entry.data.get_rate_coefficient(298) == expected
        assert 'vibrational' in entry.long_desc
        assert 'Guerra' in entry.long_desc
        assert not entry.item.reversible
    assert len(entries) == 27
    other = KineticsDatabase()
    other.load_libraries(str(ROOT / 'input/kinetics/libraries'),
                         libraries=['PlasmaArgon', 'PlasmaArgonDimer', 'PlasmaNitrogen'])
    for entry in library.entries.values():
        assert isinstance(entry.data, Arrhenius)
        assert entry.item.is_balanced()
        assert sum(sp.molecule[0].get_net_charge() for sp in entry.item.reactants) == sum(
            sp.molecule[0].get_net_charge() for sp in entry.item.products)
        assert all(sp.label != 'e-' for sp in entry.item.reactants)
        assert entry.short_desc and entry.long_desc
        for other_library in other.libraries.values():
            assert not any(entry.item.is_isomorphic(old.item, either_direction=False)
                           for old in other_library.entries.values()), entry.label


@pytest.mark.parametrize('x_n2', [.01, .2])
def test_documented_diffusion_declaration_is_consumed_by_wall_operator(x_n2, monkeypatch, tmp_path):
    import ast
    import numpy as np
    from rmgpy.chemkin import load_species_dictionary
    from rmgpy.data.thermo import ThermoDatabase
    from rmgpy.solver.plasma import PlasmaReactor
    import rmgpy.data.rmg as data_module
    from rmgpy.data.rmg import RMGDatabase

    from rmgpy import settings

    monkeypatch.setitem(settings, 'database.directory', str(ROOT / 'input'))
    monkeypatch.setattr(settings, 'filename', settings.filename)
    monkeypatch.setattr(settings, 'sources', dict(settings.sources))
    configuration = tmp_path / 'rmgrc'
    configuration.write_text(f'database.directory: {ROOT / "input"}\n')
    settings.load(str(configuration))
    readme = (ROOT / 'input/kinetics/libraries' / LIBRARY / 'README.md').read_text()
    snippet = readme.split('```python\n', 1)[1].split('```', 1)[0]
    assignment, = ast.parse(snippet).body
    assert assignment.targets[0].id == 'wallNeutralDiffusion'
    declaration = ast.literal_eval(assignment.value)
    assert set(declaration) == set(STATES)
    dictionary = load_species_dictionary(str(ROOT / 'input/kinetics/libraries' / LIBRARY / 'dictionary.txt'))
    species = [dictionary[label] for label in ('Ar', 'N2', 'e-', 'Arp') + STATES]
    monkeypatch.setattr(data_module, 'database', None)
    hub = RMGDatabase()
    thermo = hub.thermo = ThermoDatabase()
    thermo.load_libraries(str(ROOT / 'input/thermo/libraries'),
                         ['PlasmaExcitedNeutralThermo', 'primaryThermoLibrary', 'PlasmaThermo', 'electrocatThermo'])
    for sp in species:
        sp.thermo = thermo.get_thermo_data(sp)
    fractions = {sp: 0. for sp in species}
    fractions[dictionary['e-']] = fractions[dictionary['Arp']] = 1e-10
    for index, state in enumerate(STATES, 1):
        fractions[dictionary[state]] = index * 1e-6
    fractions[dictionary['N2']] = x_n2
    fractions[dictionary['Ar']] = 1 - sum(fractions.values())
    reactors = []
    for declared in (declaration, None):
        reactor = PlasmaReactor((298, 'K'), (5 * 101325 / 760, 'Pa'), fractions,
                                (10000, 'K'), diffusion_length=(.0203, 'm'),
                                ion_reduced_mobility=(1.535e-4, 'm^2/(V*s)'),
                                # Ion transport is only a common-bath diagnostic here;
                                # on/off subtraction isolates the neutral declarations.
                                wall_single_bath_approximation=True,
                                wall_neutralization_products={'Arp': 'Ar'},
                                wall_neutral_diffusion=declared,
                                resonance_radiation={'model': 'complete', 'geometryModel': 'slab'},
                                radiation_chamber_geometry={'shape': 'slab', 'gap': 0.1})
        reactor.initialize_model(species, [], [], [])
        reactors.append(reactor)
    on, off = reactors
    y = on.y.copy()
    residual_on = on.residual(0, y, np.zeros_like(y))[0]
    residual_off = off.residual(0, y, np.zeros_like(y))[0]
    delta = np.array(residual_on) - np.array(residual_off)
    frequencies = on.compute_neutral_wall_frequencies(y, on.compute_volume(y))
    total_loss = 0.
    for state in STATES:
        index = species.index(dictionary[state])
        assert frequencies[index] == pytest.approx(2.5461464, rel=2e-6)
        loss = frequencies[index] * y[index]
        assert loss > 0
        assert delta[index] == pytest.approx(-loss, rel=1e-12, abs=0)
        total_loss += loss
    assert delta[0] == pytest.approx(total_loss, rel=1e-12, abs=0)
    assert delta[1] == delta[2] == delta[3] == 0


@pytest.mark.parametrize('x_n2', [.01, .2])
def test_short_real_job_admits_every_heavy_channel(tmp_path, monkeypatch, library, x_n2):
    """Real generation and integration with a fixed pure-Ar 60 Td EEDF replay."""
    import ast
    import hashlib
    import json
    from rmgpy import settings
    from rmgpy.chemkin import load_species_dictionary
    from rmgpy.rmg.main import RMG
    import rmgpy.data.rmg as data_module

    evidence_database = ROOT / 'input'
    row = json.loads((ROOT / 'test/fixtures/argon_60Td_fixed_row.json').read_text())
    assert row['converged'] and row['EN_Td'] == pytest.approx(60.)
    for path, digest in row['production_sha256'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    te = 2 * row['mean_energy_eV'] * constants.e / (3 * constants.kB)
    readme = (ROOT / 'input/kinetics/libraries' / LIBRARY / 'README.md').read_text()
    snippet = readme.split('```python\n', 1)[1].split('```', 1)[0]
    diffusion = ast.literal_eval(ast.parse(snippet).body[0].value)
    monkeypatch.setitem(settings, 'database.directory', str(evidence_database))
    monkeypatch.setattr(settings, 'filename', settings.filename)
    monkeypatch.setattr(settings, 'sources', dict(settings.sources))
    configuration = tmp_path / 'rmgrc'
    configuration.write_text(f'database.directory: {evidence_database}\n')
    settings.load(str(configuration))
    monkeypatch.setattr(data_module, 'database', None)
    library_path = ROOT / 'input/kinetics/libraries' / LIBRARY
    dictionary = load_species_dictionary(str(library_path / 'dictionary.txt'))
    libraries = ['PlasmaArgon', 'PlasmaArgonDimer', 'PlasmaNitrogen', str(library_path)]
    lines = [f"database(thermoLibraries=['PlasmaExcitedNeutralThermo', 'primaryThermoLibrary', "
             f"'PlasmaThermo', 'electrocatThermo'], reactionLibraries={libraries!r}, "
             f"seedMechanisms={[str(library_path)]!r}, kineticsDepositories=[], "
             "kineticsFamilies='none', kineticsEstimator='rate rules')"]
    for label, sp in dictionary.items():
        # The four 4s states enter together through the heavy-network seed above,
        # before cascade families are admitted. Electron library feeds still run.
        lines.append(f"species(label={label!r}, reactive={label not in ('e-', 'Arp')!r}, "
                     f"structure=adjacencyList({sp.molecule[0].to_adjacency_list()!r}))")
    fractions = {label: 1e-8 for label in STATES + ('N2A', 'N2B', 'N2C')}
    fractions.update({'e-': 1e-10, 'Arp': 1e-10, 'N2': x_n2})
    fractions['Ar'] = 1 - sum(fractions.values())
    lines.extend([
        f"plasmaReactor(temperature=(298, 'K'), pressure=(5 * 101325 / 760, 'Pa'), "
        f"initialMoleFractions={fractions!r}, electronTemperature=({te!r}, 'K'), "
        "chamberGeometry={'shape': 'cylinder', 'radius': (5, 'cm'), 'length': (30, 'cm')}, "
        "ionReducedMobility=(1.535e-4, 'm^2/(V*s)'), wallSingleBathApproximation=True, "
        "wallNeutralizationProducts={'Arp': 'Ar'}, "
        f"wallNeutralDiffusion={diffusion!r}, "
        "resonanceRadiation={'model': 'holsteinWalsh', 'geometryModel': 'infiniteCylinder'}, "
        "terminationTime=(1e-9, 's'))",
        "simulator(atol=1e-20, rtol=1e-8)",
        "model(toleranceMoveToCore=0.1, toleranceInterruptSimulation=1.0)",
        "options(generateOutputHTML=False, generatePlots=False, saveEdgeSpecies=False, "
        "saveSimulationProfiles=True, generateChemkin=True, generateSeedEachIteration=True, "
        "generateCanteraFromChemkin=False, "
        "generateRMSYAML=False, generateCanteraYAML1=False, generateCanteraYAML2=False)",
    ])
    deck = tmp_path / 'input.py'
    deck.write_text('\n'.join(lines) + '\n')
    output = tmp_path / 'job'
    output.mkdir()
    job = RMG(input_file=str(deck), output_directory=str(output))
    initialize = job.initialize

    def initialize_fixed_row(**kwargs):
        # Keep production admission and cascade-family guards intact. Only after
        # model assembly replay EEDF rates as constant two-temperature carriers,
        # as in the trapped-decay evidence; no engine or database file is changed.
        from rmgpy.kinetics import EEDFChannel, TwoTemperaturePlasma

        result = initialize(**kwargs)
        seen = set()
        replayed = 0
        for reaction in job.reaction_model.core.reactions + job.reaction_model.edge.reactions:
            kinetics = reaction.kinetics
            if not isinstance(kinetics, EEDFChannel):
                continue
            assert kinetics.side == 'ine'
            rate = row['rates_m3_per_particle_s'][kinetics.process]
            weight = kinetics.branch_yield if kinetics.branch_product else 1.
            reaction.kinetics = TwoTemperaturePlasma(
                A=(rate * weight, 'm^3/(molecule*s)'), n=0.,
                Ea_g=(0., 'J/mol'), Ea_e=(0., 'J/mol'))
            seen.add(kinetics.process)
            replayed += 1
        assert seen == set(row['rates_m3_per_particle_s'])
        assert replayed == 149  # 137 Ar and 12 N2 production owners.
        return result

    monkeypatch.setattr(job, 'initialize', initialize_fixed_row)
    job.execute()
    assert set(libraries[:3] + [LIBRARY]) <= set(job.database.kinetics.libraries)
    assert job.reaction_systems[0].t >= 1e-9
    core = job.reaction_model.core
    # Non-vacuous: every one of 27 expected directed channels must reach the core.
    assert len(library.entries) == 27
    heavy_reactions = {}
    for entry in library.entries.values():
        matches = [reaction for reaction in core.reactions
                   if reaction.is_isomorphic(entry.item, either_direction=False)]
        assert len(matches) == 1, entry.label
        reaction, = matches
        heavy_reactions[entry.index] = reaction
        assert not reaction.reversible
        assert reaction.is_balanced()
        assert sum(sp.get_net_charge() for sp in reaction.reactants) == sum(
            sp.get_net_charge() for sp in reaction.products)
        assert reaction.kinetics.get_rate_coefficient(298) == pytest.approx(
            entry.data.get_rate_coefficient(298), rel=1e-14, abs=0)
    assert job.chemkin_writer_config.enabled
    assert (output / 'chemkin/chem.inp').is_file()
    profiles = list(output.glob('solver/simulation*'))
    assert profiles

    _check_realized_losses(job, dictionary, heavy_reactions, x_n2, output)


def _check_realized_losses(job, dictionary, heavy_reactions, x_n2, output):
    """Measure gross state-removal frequencies at the final accepted solver state."""
    import json
    import numpy as np

    core = job.reaction_model.core
    reactor = job.reaction_systems[0]
    y = reactor.y.copy()
    volume = reactor.compute_volume(y)
    # Solver rate arrays can hold a Newton trial; refresh them at the accepted y.
    reactor.residual(reactor.t, y, np.zeros_like(y))
    indices = {}
    for label in ('Ar', 'N2') + STATES:
        matches = [i for i, sp in enumerate(core.species) if sp.is_isomorphic(dictionary[label])]
        assert len(matches) == 1, label
        indices[label], = matches
    densities = {label: float(y[i] * constants.Na / volume) for label, i in indices.items()}
    assert all(value > 0 for value in densities.values())

    # Conservation of actual integrated inventories, in addition to each reaction.
    amounts = y[:len(core.species)]
    initial = reactor.y0[:len(core.species)]
    for element in ('Ar', 'N'):
        counts = np.array([sum(atom.element.symbol == element for atom in sp.molecule[0].atoms)
                           for sp in core.species])
        assert counts @ initial > 0
        assert counts @ amounts == pytest.approx(counts @ initial, rel=1e-8, abs=0)
    charges = np.array([sp.get_net_charge() for sp in core.species])
    charge_inventory = np.abs(charges) @ initial
    assert charge_inventory > 0
    assert charges @ amounts == pytest.approx(charges @ initial, abs=1e-8 * charge_inventory)

    classes = {'N2 transfer': range(1, 9), 'Ar mixing/quench': range(9, 16),
               'pooling': range(16, 26)}
    measured = {state: {} for state in STATES}
    for name, entries in classes.items():
        for state in STATES:
            sp = core.species[indices[state]]
            removal = 0.
            for entry in entries:
                reaction = heavy_reactions[entry]
                net_loss = max(0, reaction.reactants.count(sp) - reaction.products.count(sp))
                flux = reactor.core_reaction_rates[core.reactions.index(reaction)] * volume
                assert np.isfinite(flux) and flux > 0
                removal += net_loss * flux
            measured[state][name] = float(removal / y[indices[state]])

    wall = reactor.compute_neutral_wall_frequencies(y, volume)
    radiation = reactor.radiation_manifest()['accepted']
    lines = {line['state']: line for line in radiation['lines']}
    assert set(lines) == {'3P1', '1P1'}
    neutral_density = sum(amounts[i] for i, sp in enumerate(core.species)
                          if sp.get_net_charge() == 0) * constants.Na / volume
    expected_wall = 1.7e20 / neutral_density * ((2.405 / .05)**2 + (np.pi / .30)**2)
    # Independent source coefficients; same-state pooling removes TWO atoms/event.
    pooling = 1e-15 * np.array([[1.2, 2.1, 4.2, 4.2], [2.1, 2.1, 2.1, 2.1],
                               [4.2, 2.1, 1.2, 2.1], [4.2, 2.1, 2.1, 2.1]])
    pooling += np.diag(np.diag(pooling))
    actual_pooling = pooling @ np.array([densities[state] for state in STATES])
    n2_rates = (3.6e-17, .8e-17, 1.6e-17, 5.4e-17)
    ar_binary = (1.75e-20, 1.5e-20, 5.3e-21, 4.76e-20)
    ar_ternary = (1.3e-44, 1.5e-45, 0., 0.)
    # Literal plan-table references (rounded there), distinct from the runtime
    # density evaluation above. Ar sums are A4+A5+A6, A3+A7, A2, A1.
    plan_n2 = ((58327.85136, 12961.74475, 25923.48949, 87491.77704) if x_n2 == .01
               else (1166557.0272, 259234.8950, 518469.7899, 1749835.5408))
    plan_ar = ((401.00398 + 2406.02387 + 334.473, 2406.02387 + 38.5930, 850.12843, 7635.11575)
               if x_n2 == .01 else
               (324.04362 + 1944.26171 + 218.409, 1944.26171 + 25.2010, 686.97247, 6169.79050))
    plan_pooling = (129., 105., 108., 126.)
    comparison = {}
    print(f'\nAr(4s) gross loss frequencies at x_N2={x_n2}, t={reactor.t:.9g} s; '
          'fixed pure-Ar 60 Td replay; all frequencies in s^-1')
    print('state | class | realized | plan reference')
    for i, state in enumerate(STATES):
        values = measured[state]
        values['wall'] = float(wall[indices[state]])
        term = core.species[indices[state]].molecule[0].electronic_state
        values['trapped radiation'] = float(lines[term]['rate_s_1']) if term in lines else 0.
        if term in lines:
            assert 0 < lines[term]['g'] < 1
            assert lines[term]['loss_mol_s'] / y[indices[state]] == pytest.approx(
                values['trapped radiation'], rel=1e-10)
        expected = {'N2 transfer': n2_rates[i] * densities['N2'],
                    'Ar mixing/quench': ar_binary[i] * densities['Ar'] + ar_ternary[i] * densities['Ar']**2,
                    'pooling': actual_pooling[i], 'wall': expected_wall}
        plan = {'N2 transfer': plan_n2[i], 'Ar mixing/quench': plan_ar[i],
                'pooling': plan_pooling[i], 'wall': 2.5461464, 'trapped radiation': None}
        for name, expected_value in expected.items():
            assert values[name] == pytest.approx(expected_value, rel=1e-10), (state, name)
        # The tiny excitation fractions and 1 ns interval leave the bath near the plan.
        for name in ('N2 transfer', 'Ar mixing/quench'):
            assert values[name] == pytest.approx(plan[name], rel=1e-5)
        comparison[state] = {'density_m_3': densities[state], 'realized_s_1': values,
                             'plan_reference_s_1': plan}
        for name, value in values.items():
            reference = 'separate radiation work' if plan[name] is None else f'{plan[name]:.9g}'
            print(f'{state} | {name} | {value:.9g} | {reference}')
    print('Plan pooling assumes 1e16 m^-3 per state; realized pooling uses integrated populations. '
          f'Plan wall assumes Lambda=20.3 mm; this cylinder uses '
          f'Lambda={1e3 / np.sqrt((2.405 / .05)**2 + (np.pi / .30)**2):.6g} mm. '
          'Radiation had no numerical plan reference. Mixing losses exclude incoming feeds.')
    evidence = {'x_N2': x_n2, 'time_s': float(reactor.t), 'volume_m3': float(volume),
                'qualification': 'fixed pure-Ar 60 Td distribution replay; not mixture-EEDF qualification',
                'bath_density_m_3': {label: densities[label] for label in ('Ar', 'N2')},
                'states': comparison, 'radiation': radiation}
    (output / 'argon-4s-losses.json').write_text(json.dumps(evidence, indent=2) + '\n')
