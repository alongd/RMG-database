"""Targeted checks for the nitrogen loss library and real RMG job admission.

The RMG.execute check uses a reduced atomic EEDF artifact supplied through
EEDF_ATOMIC_ARTIFACT; it is an integration fixture, not physical validation.
"""
import ast
from collections import Counter
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


def test_real_execute_binds_atomic_channels_once(tmp_path, monkeypatch, library):
    """Use RMG.execute and a reduced EEDF artifact; exercise source-identity binding."""
    import os

    from rmgpy.rmg.main import RMG
    from rmgpy.kinetics import EEDFChannel
    from rmgpy.solver.eedf_provider import _development_unqualified_table_route
    from rmgpy.tools.eedf.schema import _file_hash

    artifact = os.environ.get('EEDF_ATOMIC_ARTIFACT')
    if not artifact:
        pytest.skip('requires the reduced atomic EEDF artifact from the dispatch run')
    artifact = Path(artifact)
    manifest = json.loads((artifact / 'manifest.json').read_text())
    assert manifest['accepted'] is False
    assert (artifact / 'table.h5').is_file()

    configure_database(monkeypatch, tmp_path)
    library_root = ROOT / 'input/kinetics/libraries'
    names = (
        'PlasmaArgon', 'PlasmaArgonDimer', 'PlasmaRadiativeRecombination',
        'PlasmaNitrogen', 'PlasmaArgonExcited', 'PlasmaNitrogenExcited',
        'PlasmaAtomicNitrogen', 'PlasmaNitrogenDissociativePooling',
    )
    paths = [library_root / name for name in names]
    reaction_libraries = names
    dictionaries = {}
    structures_by_label = {}
    for path in paths:
        loaded = load_species_dictionary(str(path / 'dictionary.txt'))
        for label, species in loaded.items():
            dictionaries[label] = species
            structures_by_label[label] = species.molecule[0]

    # Several libraries can repeat a label, but one molecular structure must
    # have one input-deck label. The argon dictionaries use bracketed aliases
    # for Ar and Arp; the deck declarations below use the unbracketed labels.
    unique_structures = []
    labels_by_structure = []
    for label, molecule in structures_by_label.items():
        group = next((i for i, structure in enumerate(unique_structures)
                      if molecule.is_isomorphic(structure)), None)
        if group is None:
            unique_structures.append(molecule)
            labels_by_structure.append({label})
        else:
            labels_by_structure[group].add(label)
    duplicate_label_groups = [labels for labels in labels_by_structure if len(labels) > 1]
    assert {frozenset(labels) for labels in duplicate_label_groups} == {
        frozenset(('Ar', '[Ar]')), frozenset(('Arp', '[Arp]')),
    }
    dictionaries.pop('[Ar]')
    dictionaries.pop('[Arp]')

    def declaration(path):
        fence = chr(96) * 3
        snippet = (path / 'README.md').read_text().split(fence + 'python\n', 1)[1].split(fence, 1)[0]
        return ast.literal_eval(ast.parse(snippet).body[0].value)

    diffusion = declaration(paths[4])
    diffusion.update(declaration(LIBDIR))
    diffusion.update(declaration(paths[6]))
    seeds = ['PlasmaArgonExcited', 'PlasmaNitrogenExcited',
             'PlasmaAtomicNitrogen', 'PlasmaNitrogenDissociativePooling']
    lines = [f"database(thermoLibraries=['PlasmaAtomicNitrogenThermo', 'PlasmaExcitedNeutralThermo', "
             f"'primaryThermoLibrary', 'PlasmaThermo', 'electrocatThermo'], "
             f"reactionLibraries={list(reaction_libraries)!r}, seedMechanisms={seeds!r}, "
             "kineticsDepositories=[], kineticsFamilies='none', kineticsEstimator='rate rules')"]
    initial_labels = ('Ar', 'Arp', 'Ar2p', 'e-', 'N2', 'N', 'N(2P)', 'N(2D)')
    wall_labels = set(diffusion)
    wall_labels.update(value['product'] for value in diffusion.values())
    declared_labels = set(initial_labels) | wall_labels
    for label in sorted(declared_labels):
        sp = dictionaries[label]
        lines.append(f"species(label={label!r}, reactive={label not in ('e-', 'Arp')!r}, "
                     f"structure=adjacencyList({sp.molecule[0].to_adjacency_list()!r}))")

    # Start the plasma bath and zero-abundance Ar2p wall target. Other species
    # are created by normally admitted library reactions; initializing every
    # library dictionary would place unrelated ions in the core.
    fractions = {'e-': 1e-10, 'Arp': 1e-10, 'N2': .05,
                 'Ar2p': 0.0, 'N': 1e-18, 'N(2P)': 1e-18, 'N(2D)': 1e-18}
    fractions['Ar'] = 1 - sum(fractions.values())
    levels = {
        16: 7.336, 17: 7.412, 18: 7.511, 19: 7.616, 20: 7.488,
        21: 7.587, 22: 7.692, 23: 7.686, 24: 7.791, 25: 7.896,
    }
    electron_energies = {f'PlasmaArgonExcited:{i}': (v, 'eV') for i, v in levels.items()}
    electron_energies.update({
        'PlasmaArgonDimer:1': (0.0, 'eV'),
        'PlasmaArgonDimer:2': (2.94092, 'eV'),
        'PlasmaRadiativeRecombination:1': (0.0, 'eV'),
    })
    empirical_laws = {
        'PlasmaArgonDimer:1': {
            'evaluate_at': 'Te_eff', 'class': 'C', 'sensitivity': True,
            'basis': 'Shiu & Biondi (1978), Phys. Rev. A 17, 868, Eq. (3), p. 868, Table I/Fig. 2',
        },
        'PlasmaArgonDimer:2': {
            'evaluate_at': 'Te_eff', 'class': 'C', 'sensitivity': True,
            'basis': 'Kemaneci et al. (2017), J. Phys. D, Table III row 29',
        },
        'PlasmaRadiativeRecombination:1': {
            'evaluate_at': 'Te_eff', 'class': 'C', 'sensitivity': True,
            'basis': 'Shull & Van Steenberg (1982), ApJS 48, 95, Table 2 row AR1',
        },
    }
    eedf = {'provider': 'loki-table',
            'table': (str(artifact / 'table.h5'), _file_hash(artifact / 'table.h5')),
            'branch': 'branch_0', 'initialReducedField': (17., 'Td'),
            'empiricalLaws': empirical_laws}
    lines.extend([
        "# Ar-bath zero-field K0: Ar+ 1.535 cm^2/(V*s), Ellis et al. (1976); "
        "Ar2+ 1.833 cm^2/(V*s), McDaniel & Mason (1973) as quoted by Petrov & Ferreira (2013), sec. 2.",
        f"plasmaReactor(temperature=(298.15, 'K'), pressure=(666.61184, 'Pa'), "
        f"initialMoleFractions={fractions!r}, "
        "chamberGeometry={'shape': 'cylinder', 'radius': (5, 'cm'), 'length': (30, 'cm')}, "
        "ionReducedMobilities={'Arp': (1.535e-4, 'm^2/(V*s)'), "
        "'Ar2p': (1.833e-4, 'm^2/(V*s)')}, wallSingleBathApproximation=True, "
        "wallNeutralizationProducts={'Arp': 'Ar', 'Ar2p': ('Ar', 2)}, "
        f"wallNeutralDiffusion={diffusion!r}, "
        "resonanceRadiation={'model': 'holsteinWalsh', 'geometryModel': 'infiniteCylinder'}, "
        f"electronEnergyBalance={{'absorbedPower': (0.5, 'W'), 'sheath': 'floatingWall', "
        f"'electronEnergies': {electron_energies!r}}}, electronKinetics={eedf!r}, "
        "terminationTime=(1e-12, 's'))",
        "simulator(atol=1e-20, rtol=1e-8)",
        "model(toleranceMoveToCore=0.1, toleranceInterruptSimulation=1.0)",
        "options(generateOutputHTML=False, generatePlots=False, saveEdgeSpecies=False, "
        "saveSimulationProfiles=True, generateChemkin=False, generateCanteraFromChemkin=False, "
        "generateRMSYAML=False, generateCanteraYAML1=False, generateCanteraYAML2=False)",
    ])
    deck = tmp_path / 'input.py'
    deck.write_text('\n'.join(lines) + '\n')
    output = tmp_path / 'job'
    output.mkdir()
    job = RMG(input_file=str(deck), output_directory=str(output))
    with _development_unqualified_table_route():
        job.initialize()
        assert set(job.database.kinetics.libraries) == set(names)
        # Compare against every loaded empirical Te law, including entries that
        # have not yet been admitted. Native Badnell/Voronov models use Te too,
        # but are typed rate laws rather than electronKinetics empiricalLaws.
        te_laws = {
            f'{library_name}:{entry.index}'
            for library_name, library in job.database.kinetics.libraries.items()
            for entry in library.entries.values()
            if getattr(entry.data, 'uses_electron_temperature', False)
            and entry.data.__class__.__name__ not in {'BadnellRRArrhenius', 'VoronovEIArrhenius'}
        }
        assert set(empirical_laws) == te_laws
        job.execute(initialize=False)

    assert job.reaction_systems[0].t >= 1e-12
    source_counts = Counter(r.source_identity for r in job.reaction_model.core.reactions)
    expected = set()
    for name in ('PlasmaAtomicNitrogen', 'PlasmaNitrogenDissociativePooling'):
        expected.update((name, entry.index)
                        for entry in job.database.kinetics.libraries[name].entries.values())
    for entry in job.database.kinetics.libraries['PlasmaNitrogen'].entries.values():
        if isinstance(entry.data, EEDFChannel) and getattr(entry.data, 'role', 'collision') == 'rate_only':
            expected.add(('PlasmaNitrogen', entry.index))
    assert expected
    for source in expected:
        assert source_counts[source] == 1, source

    # Record the final-state N budget from the normally admitted channels.
    # This is intentionally a reduced-table integration result, not a power-
    # balanced discharge budget.
    import os
    import numpy as np

    reactor = job.reaction_systems[0]
    final_y = reactor.y.copy()
    reactor.residual(reactor.t, final_y, np.zeros_like(final_y))
    core = job.reaction_model.core
    volume = reactor.compute_volume(final_y)
    n_species = [i for i, sp in enumerate(core.species) if sp.label == 'N']
    assert len(n_species) == 1
    n_density = float(final_y[n_species[0]] * constants.Na / volume)
    ion_balance = []
    for label in ('Arp', 'Ar2p'):
        indices = [i for i, sp in enumerate(core.species) if sp.label == label]
        assert len(indices) == 1
        i = indices[0]
        ion = core.species[i]
        chemistry_net = 0.0
        for j, reaction in enumerate(core.reactions):
            stoich = reaction.products.count(ion) - reaction.reactants.count(ion)
            chemistry_net += stoich * float(reactor.core_reaction_rates[j] * constants.Na)
        wall_loss = float(-reactor.wall_loss_rates[i] * constants.Na / volume)
        ion_balance.append((label, ion.get_net_charge(), chemistry_net, wall_loss,
                            chemistry_net - wall_loss))
    chemistry_charge_rate = 0.0
    gross_charge_terms = []
    resolved_reactions = reactor._resolve_electron_placements(
        core.reactions, core.species, [])
    for j, reaction in enumerate(core.reactions):
        resolved = resolved_reactions[j]
        charge_delta = sum(
            (resolved.products.count(sp) - resolved.reactants.count(sp)) * sp.get_net_charge()
            for sp in set(resolved.reactants + resolved.products)
        )
        charge_rate = charge_delta * float(reactor.core_reaction_rates[j] * constants.Na)
        chemistry_charge_rate += charge_rate
        gross_charge_terms.append(abs(charge_rate))
    wall_charge_terms = [
        core.species[i].get_net_charge() * float(-reactor.wall_loss_rates[i] * constants.Na / volume)
        for i in range(len(core.species))
        if core.species[i].get_net_charge() != 0
    ]
    wall_charge_outflow = sum(wall_charge_terms)
    gross_charge_terms.extend(abs(term) for term in wall_charge_terms)
    channels = []
    for source in sorted(expected):
        matches = [i for i, reaction in enumerate(core.reactions)
                   if reaction.source_identity == source]
        assert len(matches) == 1, source
        reaction_index, = matches
        reaction = core.reactions[reaction_index]
        # Count ground-state atomic N, not all nitrogen nuclei (whose
        # difference is identically zero for every balanced reaction).
        atomic_n = core.species[n_species[0]]
        n_delta = reaction.products.count(atomic_n) - reaction.reactants.count(atomic_n)
        event_rate = float(reactor.core_reaction_rates[reaction_index] * constants.Na)
        channels.append((source[0], source[1], reaction, event_rate, n_delta * event_rate))
    wall_frequency = float(reactor.compute_neutral_wall_frequencies(final_y, volume)[n_species[0]])
    wall_loss = wall_frequency * n_density
    channels.append(('wallNeutralDiffusion', 'N', 'N => 0.5 N2', wall_loss, -wall_loss))
    assert np.isfinite(n_density)
    assert all(np.isfinite(event_rate) and np.isfinite(n_rate)
               for _, _, _, event_rate, n_rate in channels)
    assert all(np.isfinite(value) for row in ion_balance for value in row[1:])
    largest_gross_charge_term = max(gross_charge_terms)
    # Require the net charge rate to be at most 1e-9 of the largest single
    # gross charge contribution, so cancellation cannot hide a material defect.
    assert abs(chemistry_charge_rate - wall_charge_outflow) <= 1e-9 * largest_gross_charge_term
    report_path = Path(os.environ['ATOMIC_NITROGEN_BUDGET']) if 'ATOMIC_NITROGEN_BUDGET' in os.environ \
        else tmp_path / 'physical-budget.md'
    report_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        '# Atomic nitrogen budget', '',
        '**reduced-table integration job, not a power-balanced discharge**', '',
        f'- Final time: `{reactor.t:.9g} s`',
        f'- Final atomic nitrogen density: `{n_density:.9g} molecule/m^3`',
        f'- Source artifact SHA-256: `{_file_hash(artifact / "table.h5")}`',
        '',
        '| Library | Entry | Reaction | Event rate (molecule m^-3 s^-1) | N production (+) / loss (-) (atom m^-3 s^-1) |',
        '|---|---:|---|---:|---:|',
    ]
    for library_name, entry_index, reaction, event_rate, n_rate in channels:
        rows.append(f'| {library_name} | {entry_index} | `{reaction}` | '
                    f'{event_rate:.9g} | {n_rate:.9g} |')
    rows.extend([
        '', '## Cation and charge balance', '',
        'Per-ion rates are instantaneous diagnostics at the final transient state; '
        'the deck does not require each ion to be at steady state.', '',
        '| Ion | Charge (+e) | Chemistry net (ions m^-3 s^-1) | Wall loss (ions m^-3 s^-1) | Net after wall (ions m^-3 s^-1) | Charge removed by wall (+e m^-3 s^-1) |',
        '|---|---:|---:|---:|---:|---:|',
    ])
    for label, charge, chemistry_net, wall_loss, net in ion_balance:
        rows.append(f'| {label} | {charge} | {chemistry_net:.9g} | {wall_loss:.9g} | '
                    f'{net:.9g} | {charge * wall_loss:.9g} |')
    rows.extend([
        '', f'- Net chemistry charge rate: `{chemistry_charge_rate:.9g} elementary charges/m^3/s`',
        f'- Net charged-particle wall charge outflow: `{wall_charge_outflow:.9g} elementary charges/m^3/s`',
        f'- Net charge production after wall losses: `{chemistry_charge_rate - wall_charge_outflow:.9g} elementary charges/m^3/s`',
        f'- Largest gross charge term: `{largest_gross_charge_term:.9g} elementary charges/m^3/s`',
        '- Closure tolerance: `1e-9` of the largest gross charge term',
    ])
    report_path.write_text('\n'.join(rows) + '\n')

    # The two legacy entries share identical kinetics but keep separate identities.
    argon_entries = job.database.kinetics.libraries['PlasmaArgonExcited'].entries
    assert argon_entries[16].data.is_identical_to(argon_entries[23].data)
    energy_by_key = dict(zip(job.reaction_systems[0].energy_reaction_keys,
                             job.reaction_systems[0].energy_threshold))
    for index, expected_eV in ((16, 7.336), (23, 7.686)):
        key = f'PlasmaArgonExcited:{index}'
        assert key in energy_by_key
        assert energy_by_key[key] / (constants.Na * constants.e) == pytest.approx(expected_eV)




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
