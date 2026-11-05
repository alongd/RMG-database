"""Targeted checks for the reduced, room-temperature nitrogen loss library.

The real-job test uses the local PlasmaArgonExcited fixed-row fixture and
explicitly enlarges the model after a nanosecond integration. This checks
admission through enlargement, not steady-state N omission.
"""
import ast
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pytest

from rmgpy import constants, settings
from rmgpy.chemkin import load_species_dictionary
from rmgpy.data.kinetics.database import KineticsDatabase

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = 'PlasmaNitrogenExcited'
LIBDIR = ROOT / 'input/kinetics/libraries' / LIBRARY
STATES = ('N2A', 'N2ap', 'N2a', 'N2w')
DN = 4.957867365474875e20
# Independently transcribed particle rates; reverse normalization is checked
# separately against Piper's spectroscopic factor, not RMG's shifted thermo.
RATES = {
    'N2A + N2 => N2 + N2': (3e-24, 'A_V0_QUENCH_BOUND'),
    'N2A + N2A => N2C + N2': (1.5e-16, 'POOL_V0_TO_MANIFOLD'),
    'N2A + N2A => N2B + N2': (7.7e-17, 'POOL_V0_TO_MANIFOLD'),
    'N2a + N2 => N2ap + N2': (2.2e-17, 'SINGLET_V0_COUPLING'),
    'N2a + Ar => N2ap + Ar': (1.3e-17, 'SINGLET_TOTAL_TO_AP'),
    'N2ap + N2 => N2a + N2': (4.4e-17, 'SINGLET_SPECTROSCOPIC_REVERSE'),
    'N2ap + Ar => N2a + Ar': (2.6e-17, 'SINGLET_SPECTROSCOPIC_REVERSE'),
    'N2ap + N2 => N2B + N2': (1.9e-19, 'AP_N2_TO_B'),
    'N2a => N2': (1.8e4, 'SINGLET_RADIATIVE_LUMP'),
    'N2a => N2ap': (191., 'SINGLET_RADIATIVE_LUMP'),
    'N2A => N2': (1 / 1.9, 'A_V0_RADIATIVE_LUMP'),
    'N2w => N2a': (650., 'SINGLET_RADIATIVE_LUMP'),
    'N2w + N2 => N2a + N2': (1e-17, 'W_N2_TO_A'),
}


@pytest.fixture(scope='module')
def library():
    db = KineticsDatabase()
    db.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=[LIBRARY])
    return db.libraries[LIBRARY]


def diffusion_declaration():
    snippet = (LIBDIR / 'README.md').read_text().split('```python\n', 1)[1].split('```', 1)[0]
    assignment, = ast.parse(snippet).body
    assert assignment.targets[0].id == 'wallNeutralDiffusion'
    return ast.literal_eval(assignment.value)


def configure_database(monkeypatch, tmp_path):
    import rmgpy.data.rmg as data_module

    monkeypatch.setitem(settings, 'database.directory', str(ROOT / 'input'))
    monkeypatch.setattr(settings, 'filename', settings.filename)
    monkeypatch.setattr(settings, 'sources', dict(settings.sources))
    configuration = tmp_path / 'rmgrc'
    configuration.write_text(f'database.directory: {ROOT / "input"}\n')
    settings.load(str(configuration))
    monkeypatch.setattr(data_module, 'database', None)


def test_library_rates_sources_conventions_balance_and_identity(library):
    from rmgpy.kinetics import Arrhenius

    entries = {entry.label: entry for entry in library.entries.values()}
    assert set(entries) == set(RATES)
    nitrogen = load_species_dictionary(str(ROOT / 'input/kinetics/libraries/PlasmaNitrogen/dictionary.txt'))
    argon = load_species_dictionary(str(ROOT / 'input/kinetics/libraries/PlasmaArgon/dictionary.txt'))
    original = dict(nitrogen, **argon)
    dictionary = load_species_dictionary(str(LIBDIR / 'dictionary.txt'))
    assert set(dictionary) == {'Ar', 'N2', 'N2A', 'N2B', 'N2C', 'N2ap', 'N2a', 'N2w'}
    for label, sp in dictionary.items():
        assert sp.is_isomorphic(original[label]), label
    for label, (rate, convention) in RATES.items():
        entry = entries[label]
        assert isinstance(entry.data, Arrhenius)  # excludes falloff/ThirdBody
        assert not entry.item.reversible
        assert entry.item.is_balanced()
        assert sum(sp.get_net_charge() for sp in entry.item.reactants) == sum(
            sp.get_net_charge() for sp in entry.item.products)
        assert 'doi:10.' in entry.long_desc and convention in entry.long_desc
        assert 'uncertainty' in entry.long_desc.lower() and entry.short_desc
        assert all(sp.label not in ('N', 'e-') for sp in entry.item.reactants + entry.item.products)
        assert entry.data.Tmin.value_si == 298 and entry.data.Tmax.value_si == 300
        for temperature in (298., 300., 600.):
            expected = rate
            if convention == 'SINGLET_SPECTROSCOPIC_REVERSE':
                expected *= math.exp(-1743.797574924 / temperature)
            actual = entry.data.get_rate_coefficient(temperature) / constants.Na ** (len(entry.item.reactants) - 1)
            assert actual == pytest.approx(expected, rel=2e-14, abs=0), label


def test_no_overlap_with_existing_or_companion_channels(library):
    db = KineticsDatabase()
    db.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=[
        'PlasmaArgon', 'PlasmaNitrogen', 'PlasmaRadiativeRecombination',
        str(ROOT / 'input/kinetics/libraries/PlasmaArgonExcited')])
    for entry in library.entries.values():
        for old_library in db.libraries.values():
            assert not any(entry.item.is_isomorphic(old.item, either_direction=False)
                           for old in old_library.entries.values()), entry.label


def test_pooling_is_event_rate_with_two_gross_and_one_cascade_net(library):
    from rmgpy.solver.simple import SimpleReactor

    reactions = {r.entry.label: r for r in library.get_library_reactions()}
    for product, expected in (('N2C', 1.5e-16), ('N2B', 7.7e-17)):
        reaction = reactions[f'N2A + N2A => {product} + N2']
        species = list(dict.fromkeys(reaction.reactants + reaction.products))
        by_label = {sp.label: sp for sp in species}
        fractions = {sp: 0. for sp in species}
        fractions[by_label['N2A']] = 1e-6
        fractions[by_label['N2']] = 1 - 1e-6
        reactor = SimpleReactor((300, 'K'), (666.61184, 'Pa'), fractions)
        reactor.initialize_model(species, [reaction], [], [])
        y = reactor.y.copy()
        reactor.residual(0, y, np.zeros_like(y))
        c_a = y[species.index(by_label['N2A'])] / reactor.V
        event = expected * constants.Na * c_a**2
        assert event > 0
        assert reactor.core_reaction_rates[0] == pytest.approx(event, rel=1e-12, abs=0)
        assert reactor.core_species_rates[species.index(by_label['N2A'])] == pytest.approx(-2 * event)
        assert reactor.core_species_rates[species.index(by_label[product])] == pytest.approx(event)
        # The companion's C->B->A cascade returns exactly one A per event.
        db = KineticsDatabase()
        db.load_libraries(str(ROOT / 'input/kinetics/libraries'), libraries=[
            str(ROOT / 'input/kinetics/libraries/PlasmaArgonExcited')])
        cascade = {e.label: e.item for lib in db.libraries.values() for e in lib.entries.values()}
        steps = [cascade['N2B => N2A']]
        if product == 'N2C':
            steps.insert(0, cascade['N2C => N2B'])
        net_a = -2 + sum(sum(sp.label == 'N2A' for sp in r.products) -
                         sum(sp.label == 'N2A' for sp in r.reactants) for r in steps)
        assert net_a == -1


@pytest.mark.parametrize('x_n2', [.01, .05, .2])
def test_wall_declaration_returns_all_four_states_to_ground(x_n2, monkeypatch, tmp_path):
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy.data.thermo import ThermoDatabase
    from rmgpy.solver.plasma import PlasmaReactor

    configure_database(monkeypatch, tmp_path)
    declaration = diffusion_declaration()
    assert set(declaration) == set(STATES)
    dictionary = load_species_dictionary(str(LIBDIR / 'dictionary.txt'))
    dictionary.update(load_species_dictionary(str(ROOT / 'input/kinetics/libraries/PlasmaArgon/dictionary.txt')))
    species = [dictionary[label] for label in ('Ar', 'N2', 'e-', 'Arp') + STATES]
    hub = RMGDatabase()
    thermo = hub.thermo = ThermoDatabase()
    thermo.load_libraries(str(ROOT / 'input/thermo/libraries'),
                         ['PlasmaExcitedNeutralThermo', 'primaryThermoLibrary', 'PlasmaThermo', 'electrocatThermo'])
    for sp in species:
        sp.thermo = thermo.get_thermo_data(sp)
    fractions = {sp: 0. for sp in species}
    fractions[dictionary['e-']] = fractions[dictionary['Arp']] = 1e-10
    for i, state in enumerate(STATES, 1):
        fractions[dictionary[state]] = i * 1e-6
        assert declaration[state] == {'product': 'N2', 'diffusivity': (DN, '1/(m*s)')}
    fractions[dictionary['N2']] = x_n2
    fractions[dictionary['Ar']] = 1 - sum(fractions.values())
    reactors = []
    for declared in (declaration, None):
        reactor = PlasmaReactor((300, 'K'), (5 * 101325 / 760, 'Pa'), fractions,
                                (10000, 'K'), diffusion_length=(.0203, 'm'),
                                ion_reduced_mobility=(1.535e-4, 'm^2/(V*s)'),
                                wall_single_bath_approximation=True,
                                wall_neutralization_products={'Arp': 'Ar'},
                                wall_neutral_diffusion=declared,
                                resonance_radiation={'model': 'complete', 'geometryModel': 'slab'},
                                radiation_chamber_geometry={'shape': 'slab', 'gap': .1})
        reactor.initialize_model(species, [], [], [])
        reactors.append(reactor)
    on, off = reactors
    y = on.y.copy()
    delta = np.array(on.residual(0, y, np.zeros_like(y))[0]) - np.array(off.residual(0, y, np.zeros_like(y))[0])
    frequencies = on.compute_neutral_wall_frequencies(y, on.compute_volume(y))
    total = 0.
    for state in STATES:
        i = species.index(dictionary[state])
        assert frequencies[i] == pytest.approx(7.4754, rel=1e-5)
        loss = frequencies[i] * y[i]
        assert loss > 0
        assert delta[i] == pytest.approx(-loss, rel=1e-12, abs=0)
        total += loss
    assert delta[1] == pytest.approx(total, rel=1e-12, abs=0)
    assert delta[0] == delta[2] == delta[3] == 0


@pytest.mark.parametrize('x_n2', [.01, .05, .2])
def test_real_job_admits_each_channel_once_after_enlargement(x_n2, monkeypatch, tmp_path, library):
    from rmgpy.rmg.main import RMG
    from rmgpy.kinetics import EEDFChannel, TwoTemperaturePlasma

    companion = ROOT
    row = json.loads((companion / 'test/fixtures/argon_60Td_fixed_row.json').read_text())
    assert row['converged'] and row['EN_Td'] == pytest.approx(60.)
    for path, digest in row['production_sha256'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    configure_database(monkeypatch, tmp_path)
    ar_lib = companion / 'input/kinetics/libraries/PlasmaArgonExcited'
    dictionary = load_species_dictionary(str(ar_lib / 'dictionary.txt'))
    dictionary.update(load_species_dictionary(str(LIBDIR / 'dictionary.txt')))
    readme = (ar_lib / 'README.md').read_text()
    ar_diffusion = ast.literal_eval(ast.parse(readme.split('```python\n', 1)[1].split('```', 1)[0]).body[0].value)
    diffusion = dict(ar_diffusion, **diffusion_declaration())
    libraries = ['PlasmaArgon', 'PlasmaArgonDimer', 'PlasmaNitrogen', str(ar_lib), str(LIBDIR)]
    lines = [f"database(thermoLibraries=['PlasmaExcitedNeutralThermo', 'primaryThermoLibrary', "
             f"'PlasmaThermo', 'electrocatThermo'], reactionLibraries={libraries!r}, "
             f"seedMechanisms={[str(ar_lib), str(LIBDIR)]!r}, kineticsDepositories=[], "
             "kineticsFamilies='none', kineticsEstimator='rate rules')"]
    for label, sp in dictionary.items():
        lines.append(f"species(label={label!r}, reactive={label not in ('e-', 'Arp')!r}, "
                     f"structure=adjacencyList({sp.molecule[0].to_adjacency_list()!r}))")
    fractions = {label: 1e-8 for label in tuple(ar_diffusion) + STATES + ('N2B', 'N2C')}
    fractions.update({'e-': 1e-10, 'Arp': 1e-10, 'N2': x_n2})
    fractions['Ar'] = 1 - sum(fractions.values())
    te = 2 * row['mean_energy_eV'] * constants.e / (3 * constants.kB)
    lines.extend([
        f"plasmaReactor(temperature=(300, 'K'), pressure=(5 * 101325 / 760, 'Pa'), "
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
        "saveSimulationProfiles=True, generateChemkin=True, "
        "generateCanteraFromChemkin=False, generateRMSYAML=False, "
        "generateCanteraYAML1=False, generateCanteraYAML2=False)",
    ])
    deck = tmp_path / 'input.py'
    deck.write_text('\n'.join(lines) + '\n')
    output = tmp_path / 'job'
    output.mkdir()
    job = RMG(input_file=str(deck), output_directory=str(output))
    initialize = job.initialize

    def initialize_fixed_row(**kwargs):
        result = initialize(**kwargs)
        seen = set()
        count = 0
        for reaction in job.reaction_model.core.reactions + job.reaction_model.edge.reactions:
            kinetics = reaction.kinetics
            if not isinstance(kinetics, EEDFChannel):
                continue
            assert kinetics.side == 'ine'
            weight = kinetics.branch_yield if kinetics.branch_product else 1.
            reaction.kinetics = TwoTemperaturePlasma(
                A=(row['rates_m3_per_particle_s'][kinetics.process] * weight, 'm^3/(molecule*s)'),
                n=0., Ea_g=(0., 'J/mol'), Ea_e=(0., 'J/mol'))
            seen.add(kinetics.process)
            count += 1
        assert seen == set(row['rates_m3_per_particle_s'])
        assert count == 149
        return result

    monkeypatch.setattr(job, 'initialize', initialize_fixed_row)
    job.execute()
    reactor = job.reaction_systems[0]
    assert reactor.t >= 1e-9
    core = job.reaction_model.core
    assert len(library.entries) == 13
    for entry in library.entries.values():
        matches = [r for r in core.reactions if r.is_isomorphic(entry.item, either_direction=False)]
        assert len(matches) == 1, entry.label
        reaction, = matches
        assert not reaction.reversible and reaction.is_balanced()
        assert reaction.kinetics.get_rate_coefficient(300) == pytest.approx(entry.data.get_rate_coefficient(300), rel=1e-14, abs=0)
    assert job.chemkin_writer_config.enabled
    assert (output / 'chemkin/chem.inp').is_file()
    assert list(output.glob('solver/simulation*'))

    # Evaluate accepted final state explicitly: cached rates can belong to a
    # Newton trial. Report gross consumption and signed net loss separately.
    y = reactor.y.copy()
    reactor.residual(reactor.t, y, np.zeros_like(y))
    volume = reactor.compute_volume(y)
    density = y[:len(core.species)] * constants.Na / volume
    indices = {}
    for label in ('Ar', 'N2', 'N2A', 'N2ap', 'N2a', 'N2w', 'N2B', 'N2C'):
        matches = [i for i, sp in enumerate(core.species) if sp.is_isomorphic(dictionary[label])]
        assert len(matches) == 1, label
        indices[label] = matches[0]
    assert all(density[indices[state]] > 0 for state in STATES)
    report = {'purpose': '1 ns integration followed by explicit enlargement; NOT steady-state N omission',
              'x_N2_initial': x_n2, 'time_s': reactor.t,
              'T_K': 300., 'n_m3': {label: float(density[i]) for label, i in indices.items()},
              'classes_s-1': {state: {} for state in STATES}, 'channels': []}
    for entry in library.entries.values():
        j, = [j for j, r in enumerate(core.reactions) if r.is_isomorphic(entry.item, either_direction=False)]
        reaction = core.reactions[j]
        reference, convention = RATES[entry.label]
        if convention == 'SINGLET_SPECTROSCOPIC_REVERSE':
            reference *= math.exp(-1743.797574924 / 300.)
        expected = reference
        for sp in reaction.reactants:
            expected *= density[core.species.index(sp)]
        actual = reactor.core_reaction_rates[j] * constants.Na
        assert expected > 0
        assert actual == pytest.approx(expected, rel=2e-12, abs=0), entry.label
        if convention == 'POOL_V0_TO_MANIFOLD':
            channel_class = 'pooling'
        elif convention in ('SINGLET_V0_COUPLING', 'SINGLET_TOTAL_TO_AP', 'SINGLET_SPECTROSCOPIC_REVERSE', 'W_N2_TO_A'):
            channel_class = 'collisional_singlet_exchange'
        elif len(reaction.reactants) == 1:
            channel_class = 'radiative_exchange' if entry.label in ('N2a => N2ap', 'N2w => N2a') else 'radiative_terminal'
        else:
            channel_class = 'collisional_quench'
        report['channels'].append({'label': entry.label, 'class': channel_class,
                                   'actual_event_m3_s': float(actual),
                                   'source_formula_event_m3_s': float(expected)})
        for state in STATES:
            sp = core.species[indices[state]]
            consumed, produced = reaction.reactants.count(sp), reaction.products.count(sp)
            if not (consumed or produced):
                continue
            item = report['classes_s-1'][state].setdefault(channel_class, {'gross': 0., 'returned': 0., 'net': 0.})
            item['gross'] += float(consumed * actual / density[indices[state]])
            item['returned'] += float(produced * actual / density[indices[state]])
            item['net'] = item['gross'] - item['returned']
    frequencies = reactor.compute_neutral_wall_frequencies(y, volume)
    # Neutral transport uses neutral, not electron/ion, density in this EOS.
    neutral_density = sum(density[i] for i, sp in enumerate(core.species) if sp.get_net_charge() == 0)
    # Match the cylinder input operator: its first Bessel zero is rounded to 2.405.
    lambda_squared_inverse = (2.405 / .05)**2 + (math.pi / .30)**2
    expected_wall = DN / neutral_density * lambda_squared_inverse
    for state in STATES:
        wall = float(frequencies[indices[state]])
        assert wall > 0
        assert wall == pytest.approx(expected_wall, rel=1e-8)
        report['classes_s-1'][state]['wall'] = {'gross': wall, 'returned': 0., 'net': wall}
    gross_pooling = report['classes_s-1']['N2A']['pooling']['gross']
    assert gross_pooling == pytest.approx(2 * (1.5e-16 + 7.7e-17) * density[indices['N2A']], rel=2e-12)
    report['post_cascade_A_pooling_net_s-1'] = gross_pooling / 2
    report['geometry'] = {'radius_m': .05, 'length_m': .30,
                          'Lambda_m': lambda_squared_inverse**-.5,
                          'planning_Lambda_m': .0203,
                          'actual_over_planning_wall': lambda_squared_inverse * .0203**2}
    # Integration conserves each element and charge, including neutral walls.
    initial = reactor.y0[:len(core.species)]
    final = y[:len(core.species)]
    for element in ('Ar', 'N'):
        counts = np.array([sp.molecule[0].get_element_count().get(element, 0) for sp in core.species])
        assert np.dot(counts, final) == pytest.approx(np.dot(counts, initial), rel=1e-9, abs=1e-20)
    charges = np.array([sp.get_net_charge() for sp in core.species])
    assert np.dot(charges, final) == pytest.approx(np.dot(charges, initial), abs=1e-18)
    (tmp_path / 'loss-frequencies.json').write_text(json.dumps(report, indent=2) + '\n')

    # Seeded channels may also be waiting on the edge from reaction-library
    # admission. Promote a real edge species so that all now-core reactions
    # move too: a short integration alone never exercised this path.
    model = job.reaction_model
    assert model.edge.species, 'Need an edge species to exercise enlargement'
    promoted = model.edge.species[0]
    model.enlarge(promoted)
    assert promoted in model.core.species and promoted not in model.edge.species
    admitted = model.core.reactions + model.edge.reactions
    for entry in library.entries.values():
        matches = [r for r in admitted if r.is_isomorphic(entry.item, either_direction=False)]
        assert len(matches) == 1, (entry.label, len(matches))


def test_w_loss_channels_integrate_to_a_with_source_decay_frequency(library):
    """Both w loss paths transfer one singlet to a at the sourced total rate."""
    from rmgpy.solver.simple import SimpleReactor

    reactions = [r for r in library.get_library_reactions()
                 if r.entry.label in ('N2w => N2a', 'N2w + N2 => N2a + N2')]
    assert len(reactions) == 2
    species = list(dict.fromkeys(sp for r in reactions for sp in r.reactants + r.products))
    labels = {sp.label: sp for sp in species}
    initial = {labels['N2w']: 1e-6, labels['N2a']: 0., labels['N2']: 1 - 1e-6}
    reactor = SimpleReactor((300, 'K'), (666.61184, 'Pa'), initial)
    reactor.initialize_model(species, reactions, [], [], atol=1e-20, rtol=1e-10)
    wi, ai, ground = [species.index(labels[s]) for s in ('N2w', 'N2a', 'N2')]
    initial_w = reactor.y[wi]
    density_n2 = reactor.y[ground] / reactor.V * constants.Na
    frequency = 650. + 1e-17 * density_n2
    reactor.advance(3. / frequency)
    expected_w = initial_w * math.exp(-frequency * reactor.t)
    assert reactor.y[wi] == pytest.approx(expected_w, rel=1e-7, abs=0)
    assert reactor.y[ai] == pytest.approx(initial_w - expected_w, rel=1e-8, abs=0)
    assert not any('N2w' in e.label and 'Ar' in e.label for e in library.entries.values())
    assert 'W_AR_COUPLING_SOURCE_GAP' in (LIBDIR / 'README.md').read_text()
