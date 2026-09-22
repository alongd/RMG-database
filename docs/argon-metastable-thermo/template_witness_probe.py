#!/usr/bin/env python
# encoding: utf-8
"""For each family the TEMPLATE says admits metastable argon, build the witness.

``template_space_derivation.py`` answers "which families' templates admit ``Ar u2 p3 c0``"
without needing a partner. This answers the follow-on question -- "so what happens?" --
and it must not answer it by guessing partners, because guessing partners is the defect
round 77 found: the old probe's hardcoded list had no hydrogen halide, no fluorinated
radical and no surface site, so it could not see four of the families that match.

So the partner is DERIVED from the template too. For each family, the slot the metastable
does not occupy is turned into a concrete molecule with the group's own
``make_sample_molecule()`` -- the same call RMG's database test suite uses to sample a
group node. No imagination is involved and the coverage follows the template space.

For each family this reports, in order:

    template admits it    from the derivation
    partner               derived, with the group it came from
    reactions generated   with the containment DETACHED  -> the BEFORE evidence
    product thermo        whether any product raises AtomTypeError
    reactions generated   with the containment ATTACHED  -> the AFTER evidence

A family that generates 0 with the containment detached is reported as SILENT: its
template admits the species but no reachable partner was derived, which is a weaker
finding than a witness and is labelled as such rather than counted as one.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/template_witness_probe.py \\
        > >(tee docs/argon-metastable-thermo/logs/template_witness_probe.stdout.log) \\
        2> >(tee docs/argon-metastable-thermo/logs/template_witness_probe.stderr.log >&2)
"""

import os
import sys

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402
from rmgpy.data.thermo import ThermoDatabase               # noqa: E402
from rmgpy.exceptions import AtomTypeError                 # noqa: E402
from rmgpy.molecule import Molecule                        # noqa: E402
from rmgpy.species import Species                          # noqa: E402

sys.path.insert(0, HERE)
from template_space_derivation import (                    # noqa: E402
    AR_META, CONTAINMENT, EII, matching_slots, molecule, template_sites)


def derive_partner(family, direction, occupied):
    """A concrete molecule for a slot the metastable does not occupy."""
    sites = template_sites(family, direction)
    for index, site in enumerate(sites):
        if index in occupied:
            continue
        try:
            sample = site.make_sample_molecule()
            sample.update_atomtypes()
            return sample, index
        except Exception as exc:                            # noqa: BLE001
            print('      (slot %d would not sample: %s: %s)'
                  % (index, type(exc).__name__, str(exc).splitlines()[0]), flush=True)
    return None, None


def generate(family, reactants):
    try:
        return family.generate_reactions(reactants)
    except Exception as exc:                                # noqa: BLE001
        print('      generation raised %s: %s' % (type(exc).__name__, exc), flush=True)
        return []


def thermo_verdict(thermo_db, reactions):
    """Does any product of any generated reaction fail to get thermo?"""
    raised, numbered = [], []
    for reaction in reactions:
        for product in reaction.products:
            spc = Species(molecule=[product if isinstance(product, Molecule)
                                    else product.molecule[0]])
            try:
                thermo_db.get_thermo_data(spc)
            except AtomTypeError:
                raised.append(spc.molecule[0].to_smiles())
            except Exception as exc:                        # noqa: BLE001
                raised.append('%s(%s)' % (type(exc).__name__, exc.__class__.__name__))
            else:
                numbered.append(spc.molecule[0].to_smiles())
    return raised, numbered


def main():
    print('loading every family', flush=True)
    kdb = KineticsDatabase()
    kdb.load_families(os.path.join(DATABASE, 'kinetics', 'families'), families='all')
    tdb = ThermoDatabase()
    tdb.load(os.path.join(DATABASE, 'thermo'))
    meta = molecule(AR_META)

    candidates = []
    for label in sorted(kdb.families):
        family = kdb.families[label]
        for direction in ('forward', 'reverse'):
            slots = matching_slots(family, meta, direction)
            if slots:
                candidates.append((label, direction, slots))

    print('\ncandidates from the template space: %d\n' % len(candidates), flush=True)

    witnesses, silent, regressions, uncontrolled, vacuous = [], [], [], [], []
    for label, direction, slots in candidates:
        family = kdb.families[label]
        contained = family.forbidden is not None and CONTAINMENT in family.forbidden.entries
        print('=== %s (%s, slots %s)%s' % (label, direction, slots,
                                           '  [EII: intended channel]' if label == EII else ''),
              flush=True)
        partner, partner_slot = derive_partner(family, direction, set(slots))
        if partner is None:
            print('      no partner could be derived; unimolecular attempt only', flush=True)
            reactants = [meta]
        else:
            print('      partner derived from slot %d: %s'
                  % (partner_slot, partner.to_smiles()), flush=True)
            reactants = [meta, partner]

        saved = None
        if contained:
            saved = family.forbidden.entries.pop(CONTAINMENT)
        before = generate(family, reactants)
        raised, numbered = thermo_verdict(tdb, before)
        print('      BEFORE (containment detached): %d reactions, %d products raise, %d get a number'
              % (len(before), len(raised), len(numbered)), flush=True)
        if raised:
            print('             raising products: %s' % ', '.join(sorted(set(raised))[:4]), flush=True)
        if saved is not None:
            family.forbidden.entries[CONTAINMENT] = saved
            after = generate(family, reactants)
            print('      AFTER  (containment attached): %d reactions' % len(after), flush=True)
        else:
            print('      AFTER  : no containment on this family yet', flush=True)

        # CONTROL: the family's OWN chemistry, with no argon anywhere in it, built by
        # sampling every slot of the template. If a forbidden group written for metastable
        # argon moves this, it is not a containment, it is a regression. Derived from the
        # template like everything else here, so the control's coverage follows the family
        # rather than somebody's idea of what the family is for.
        control_reactants = []
        for index, site in enumerate(template_sites(family, direction)):
            try:
                sample = site.make_sample_molecule()
                sample.update_atomtypes()
                control_reactants.append(sample)
            except Exception:                               # noqa: BLE001
                control_reactants = []
                break
        if control_reactants:
            if saved is not None or contained:
                with_block = len(generate(family, control_reactants))
                lifted = family.forbidden.entries.pop(CONTAINMENT)
                without_block = len(generate(family, control_reactants))
                family.forbidden.entries[CONTAINMENT] = lifted
            else:
                with_block = without_block = len(generate(family, control_reactants))
            if with_block == without_block == 0:
                # Both sides zero carries NO information: the sampled reactants simply do
                # not react (usually a degenerate identity, e.g. [H] + HBr -> HBr + [H],
                # which RMG never generates). Counting it as a passing control is exactly
                # the unfailable-check pattern this campaign keeps finding, so it is named
                # as vacuous and the family is listed for a hand-written control instead.
                verdict = 'VACUOUS (0=0, proves nothing)'
                vacuous.append(label)
            elif with_block == without_block:
                verdict = 'UNMOVED'
            else:
                verdict = 'MOVED  <-- REGRESSION'
            print('      CONTROL (own chemistry, %s): %d with block, %d without  %s'
                  % (' + '.join(m.to_smiles() for m in control_reactants),
                     with_block, without_block, verdict), flush=True)
            if with_block != without_block:
                regressions.append(label)
        else:
            print('      CONTROL: template would not sample; no control for this family',
                  flush=True)
            uncontrolled.append(label)

        (witnesses if before else silent).append(label)

    print('\n=== SUMMARY ===', flush=True)
    print('  families whose template admits the metastable : %d' % len(candidates), flush=True)
    print('  of those, with a derived witness reaction     : %d' % len(witnesses), flush=True)
    print('  of those, SILENT (template admits, no partner derived) : %d  %s'
          % (len(silent), sorted(set(silent))), flush=True)
    print('  controls that MOVED (regressions)               : %d  %s'
          % (len(regressions), sorted(set(regressions))), flush=True)
    print('  families with no derivable control               : %d  %s'
          % (len(uncontrolled), sorted(set(uncontrolled))), flush=True)
    print('  controls that were VACUOUS (0=0, no information) : %d  %s'
          % (len(vacuous), sorted(set(vacuous))), flush=True)
    print('     -> these need a hand-written control; see CONTAINMENT_CONTROLS in '
          'test/test_argon_metastable_thermo.py', flush=True)
    print('\nA SILENT family is still in scope: the template admits the species, so a partner '
          'this probe could not derive may still exist. It is reported, not dismissed.', flush=True)
    return 1 if regressions else 0


if __name__ == '__main__':
    sys.exit(main())
