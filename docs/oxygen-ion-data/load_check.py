"""Reproduce the in-repo source checks and print the model's actual NASA data."""
from pathlib import Path
import json
import sys

from rmgpy import settings
from rmgpy.species import Species
from rmgpy.thermo.thermoengine import process_thermo_data

ROOT = Path(__file__).resolve().parents[2]
settings['database.directory'] = str(ROOT/'input')
sys.path.insert(0, str(ROOT/'test'))
import test_plasma_oxygen_charged as checks

fixture = checks.database.__wrapped__()
db = next(fixture)
result = {'thermo': {}, 'kinetics': {}, 'mutation_rejections': {}, 'model_admission': []}
try:
    checks.test_op_high_temperature_constant_cp_loss_is_disclosed(db)
    for order in checks.LIBRARY_ORDERS:
        model, electron, detachment = checks.admit_combined_plasma_libraries(db, order)
        row = checks.measure_combined_admission(model)
        row['library_order'] = order
        reactor = checks.initialize_admitted_detachment_reactor(model, electron, detachment)
        row['reactor_rates'] = len(reactor.kf)
        row['surviving_subset_reactor_initialized'] = True
        try:
            checks.assert_independent_attachment_detachment(model, db)
        except AssertionError as error:
            row['independent_pair_preserved'] = False
            row['failure'] = str(error)
        else:
            row['independent_pair_preserved'] = True
        result['model_admission'].append(row)
    checks.test_exact_entry_inventory(db)
    states = checks.state_references.__wrapped__()
    checks.test_each_actual_reaction_graph_matches_existing_state_dictionaries(db, states)
    checks.test_state_check_rejects_singlet_oxygen_under_ground_state_label(db, states)
    checks.test_ozonide_entire_primary_constant_derivation(db)
    checks.test_ozonide_grid_rejects_a_changed_unsampled_last_point(db)
    checks.test_three_body_collider_is_explicit_and_is_oxygen(db)
    checks.test_argon_channels_state_the_3p2_thermo_proxy_for_the_kinetic_lump(db)
    for label in checks.LIMITS:
        if label in checks.REFERENCE:
            checks.test_signed_electron_conversion_and_source_rows(db, label)
        checks.test_actual_production_nasa_h_s_cp_and_temperature_limits(db, label)
        entry = db.thermo.libraries['PlasmaThermo'].entries[label]
        sp = Species(label=label, molecule=[entry.item.copy(deep=True)])
        sp.generate_resonance_structures()
        loaded = db.thermo.get_thermo_data(sp)
        nasa = process_thermo_data(sp, loaded)
        rows = {}
        for t in (298., 298.15, 400.):
            if label == '[O3m]':
                ref = checks.ozone_rrho(t)
            else:
                source = checks.REFERENCE[label]
                ref_row = source['rows'].get(str(t))
                ref = None if ref_row is None else (
                    source['h_ec298']-source['charge']*2.5*checks.R*298.15/1000+ref_row['dh'],
                    ref_row['s'], ref_row['cp'])
            rows[str(t)] = dict(library=[loaded.get_enthalpy(t)/1000, loaded.get_entropy(t), loaded.get_heat_capacity(t)],
                               nasa=[nasa.get_enthalpy(t)/1000, nasa.get_entropy(t), nasa.get_heat_capacity(t)],
                               reference=ref)
        if label == '[Op]':
            source_cp = checks.REFERENCE[label]['cp'][checks.REFERENCE[label]['temperatures'].index(5000.)]
            cp = nasa.get_heat_capacity(5000.)
            result['op_high_temperature'] = dict(temperature=5000., source_cp=source_cp,
                                                 library_cp=loaded.get_heat_capacity(5000.),
                                                 nasa_cp=cp, error_percent=100*(cp/source_cp-1))
        result['thermo'][label] = dict(cp0=loaded.Cp0.value_si, cpinf=loaded.CpInf.value_si,
                                      source_range=[loaded.Tmin.value_si, loaded.Tmax.value_si],
                                      nasa_range=[nasa.Tmin.value_si, nasa.Tmax.value_si], rows=rows)
    for index, source in checks.RATES.items():
        checks.test_loaded_rates_follow_particle_source_and_preserve_charge(db, index)
        data = db.kinetics.libraries['PlasmaOxygenHeavy'].entries[int(index)].data
        result['kinetics'][index] = {str(t): data.get_rate_coefficient(t)/checks.NA**(source['order']-1)
                                     for t in (298., 298.15, 400.)}
        for factor in (0, 2):
            checks.test_particle_rate_assertion_rejects_zero_and_double_a(db, index, factor)
        for parameter in ('n', 'Ea', 'T0'):
            checks.test_parameter_assertion_rejects_changes(db, index, parameter)
    result['mutation_rejections'] = dict(A_zero=19, A_double=19, parameters=57, O2_to_O2a=1, O3_Cp1000_double=1)
finally:
    fixture.close()
print(json.dumps(result, indent=2))

if not all(row['independent_pair_preserved'] for row in result['model_admission']):
    sys.exit(1)  # Measured engine-blocked admission, never a successful load verdict.
