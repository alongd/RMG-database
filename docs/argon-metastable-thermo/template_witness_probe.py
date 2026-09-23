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
    species thermo        whether any species on EITHER side of a generated reaction
                          fails to get thermo, and with which exception
    reactions generated   with the containment ATTACHED  -> the AFTER evidence

A family that generates 0 with the containment detached is reported as SILENT: its
template admits the species but no reachable partner was derived, which is a weaker
finding than a witness and is labelled as such rather than counted as one.

A family whose generation RAISED is reported separately and is never called SILENT. Round
118: `generate()` used to return ``[]`` on any exception, so a generation that FAILED and a
generation that produced nothing were indistinguishable -- ``Surface_Adsorption_Double``
with its containment detached raises, and this probe reported it SILENT and exited 0. One
raise is declared in `EXPECTED_WITHOUT_CONTAINMENT` because it is the containment's own
evidence; every other raise, and every raise in the attached or control arms, is fatal.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-mgr-i221-deck-probe-234349 python docs/argon-metastable-thermo/template_witness_probe.py \\
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
from rmgpy.molecule import Molecule                        # noqa: E402
from rmgpy.species import Species                          # noqa: E402

sys.path.insert(0, HERE)
from template_space_derivation import (                    # noqa: E402
    AR_META, CONTAINMENT, EII, UndeterminedSlot, matching_slots, molecule,
    template_sites)


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


#: (arm, family, exception type, message) for every generation attempt that raised. A
#: generation that FAILED is not a generation that produced nothing, and this probe used to
#: report the two the same way: `generate()` returned ``[]`` on any exception, the caller
#: counted zero reactions, the family was listed ``SILENT`` -- "the template admits the
#: species and no partner could be derived" -- and `main()` exited 0. Exhibited, not
#: hypothesised: with `Surface_Adsorption_Double`'s containment detached, generation raises
#: and this probe called it a clean bill of health.
GENERATION_FAILURES = []

#: The one raise that is EVIDENCE rather than a defect, declared by family and exception
#: type with the reason, so that it is attributed instead of swallowed.
#:
#: `Surface_Adsorption_Double` with its containment DETACHED asks RMG to build ``X=Ar``,
#: and no atom type owns a double-bonded argon -- the adjacency list that reaches
#: `update_atomtypes` carries ``multiplicity -187``. That raise is the strongest witness
#: this probe can produce: it is not that the family generates something unwanted, it is
#: that the species cannot be represented at all, which is precisely what the forbidden
#: entry exists to prevent. Declaring it keeps the exit code a live tripwire. The
#: alternative -- any raise anywhere is fatal -- makes this probe exit non-zero on every
#: run of this branch forever, and a check that always fails detects nothing, which is the
#: same defect as a check that always passes wearing the other mask.
#:
#: ATTACHED-arm and control-arm raises are never expected and are always fatal: with the
#: containment in place nothing should be unrepresentable, and a control raising means the
#: forbidden entry has taken real chemistry with it.
EXPECTED_WITHOUT_CONTAINMENT = {
    ('Surface_Adsorption_Double', 'AtomTypeError'):
        'X=Ar cannot be typed; this raise IS the containment\'s justification',
}


def generate(family, reactants, arm):
    """`family.generate_reactions`, with a failure recorded as a failure.

    Still returns ``[]`` so the sweep can continue and report every family rather than
    dying on the first -- but the emptiness is no longer the only trace of what happened,
    and the caller can no longer mistake it for "no reactions were generated". `arm` says
    which measurement this was: ``detached``, ``attached`` or ``control``."""
    try:
        return family.generate_reactions(reactants)
    except Exception as exc:                                # noqa: BLE001
        kind = type(exc).__name__
        declared = EXPECTED_WITHOUT_CONTAINMENT.get((family.label, kind))
        GENERATION_FAILURES.append((arm, family.label, kind, str(exc)))
        if arm == 'detached' and declared:
            print('      ! generation RAISED %s (declared, expected without the '
                  'containment): %s' % (kind, declared), flush=True)
        else:
            print('      ! generation RAISED %s in the %s arm: %s  <-- NOT "zero '
                  'reactions"' % (kind, arm, str(exc).splitlines()[0]), flush=True)
        return []


def undeclared_failures():
    """The generation failures that are defects rather than declared evidence."""
    out = []
    for arm, label, kind, message in GENERATION_FAILURES:
        if arm == 'detached' and (label, kind) in EXPECTED_WITHOUT_CONTAINMENT:
            continue
        out.append((arm, label, kind, message))
    return out


def thermo_verdict(thermo_db, reactions):
    """Does any species of any generated reaction fail to get thermo?

    BOTH SIDES, not just the products. A family that matches the metastable in its REVERSE
    template puts the argon-bonded species among the generated REACTANTS -- which is exactly
    what ``Cation_NO_Substitution`` and ``Li_NO_Substitution`` do -- so a products-only sweep
    reports zero failures for them while direct checking reproduces the raise. RMG generates
    thermo for every species it admits, in ``make_new_species``, without caring which side of
    the arrow it arrived on; a verdict that inspects one side and reports on both is narrower
    than the thing it describes.

    Returns ``(raised, numbered)``, each a list of ``'<side>:<name>'`` or
    ``'<side>:<name> -> <ExceptionType>'`` so the caller can see where a failure sat.
    """
    raised, numbered = [], []
    for reaction in reactions:
        for side, members in (('reactant', reaction.reactants), ('product', reaction.products)):
            for member in members:
                spc = Species(molecule=[member if isinstance(member, Molecule)
                                        else member.molecule[0]])
                try:
                    name = spc.molecule[0].to_smiles()
                except Exception:                           # noqa: BLE001 - exotic species
                    name = spc.molecule[0].to_adjacency_list().strip().replace('\n', ' | ')
                try:
                    thermo_db.get_thermo_data(spc)
                except Exception as exc:                    # noqa: BLE001
                    raised.append('%s:%s -> %s' % (side, name, type(exc).__name__))
                else:
                    numbered.append('%s:%s' % (side, name))
    return raised, numbered


def main():
    print('loading every family', flush=True)
    kdb = KineticsDatabase()
    kdb.load_families(os.path.join(DATABASE, 'kinetics', 'families'), families='all')
    tdb = ThermoDatabase()
    tdb.load(os.path.join(DATABASE, 'thermo'))
    meta = molecule(AR_META)

    candidates = []
    undetermined = []
    for label in sorted(kdb.families):
        family = kdb.families[label]
        for direction in ('forward', 'reverse'):
            try:
                slots = matching_slots(family, meta, direction)
            except UndeterminedSlot as exc:
                # Collected rather than fatal here so the sweep still reports every other
                # family, and fatal at the end. A slot nobody could evaluate is not a slot
                # that did not match, and a candidate list missing an undetermined family
                # is not the template space.
                undetermined.append((label, direction, str(exc)))
                print('  ! %s' % exc, flush=True)
                continue
            if slots:
                candidates.append((label, direction, slots))

    print('\ncandidates from the template space: %d\n' % len(candidates), flush=True)

    witnesses, silent, regressions, uncontrolled, vacuous = [], [], [], [], []
    raised_families = []
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
        before = generate(family, reactants, 'detached')
        raised, numbered = thermo_verdict(tdb, before)
        print('      BEFORE (containment detached): %d reactions, %d species raise, %d get a number'
              % (len(before), len(raised), len(numbered)), flush=True)
        if raised:
            print('             raising species: %s' % ', '.join(sorted(set(raised))[:4]), flush=True)
        if saved is not None:
            family.forbidden.entries[CONTAINMENT] = saved
            after = generate(family, reactants, 'attached')
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
                with_block = len(generate(family, control_reactants, 'control'))
                lifted = family.forbidden.entries.pop(CONTAINMENT)
                without_block = len(generate(family, control_reactants, 'control'))
                family.forbidden.entries[CONTAINMENT] = lifted
            else:
                with_block = without_block = len(generate(family, control_reactants,
                                                          'control'))
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

        # A family whose generation RAISED is not silent: silence means "the template
        # admits the species and no partner could be derived", and something quite
        # different happened here. Bucketed separately so the summary cannot report it as
        # the weaker finding.
        if any(a == 'detached' and f == label for a, f, _k, _m in GENERATION_FAILURES):
            raised_families.append(label)
        else:
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
    print('  template slots that could not be EVALUATED               : %d  %s'
          % (len(undetermined), sorted({label for label, _d, _m in undetermined})), flush=True)
    print('  families whose generation RAISED (NOT silent)            : %d  %s'
          % (len(raised_families), sorted(set(raised_families))), flush=True)
    for arm, label, kind, message in GENERATION_FAILURES:
        declared = (arm == 'detached'
                    and EXPECTED_WITHOUT_CONTAINMENT.get((label, kind)))
        print('     [%s] %s: %s: %s%s'
              % (arm, label, kind, message.splitlines()[0],
                 '   (DECLARED: %s)' % declared if declared else '   <-- UNDECLARED'),
              flush=True)
    stale = [key for key in EXPECTED_WITHOUT_CONTAINMENT
             if key not in {(l, k) for a, l, k, _m in GENERATION_FAILURES if a == 'detached'}]
    print('  declared raises that did NOT happen (stale declarations)  : %d  %s'
          % (len(stale), sorted(stale)), flush=True)
    print('  UNDECLARED generation failures (fatal)                    : %d  %s'
          % (len(undeclared_failures()),
             sorted({(a, l) for a, l, _k, _m in undeclared_failures()})), flush=True)
    print('\nA SILENT family is still in scope: the template admits the species, so a partner '
          'this probe could not derive may still exist. It is reported, not dismissed.', flush=True)
    print('A family that RAISED is not silent and not in scope for that reading at all: '
          'nothing was measured about it. A raise DECLARED in EXPECTED_WITHOUT_CONTAINMENT '
          'is evidence and keeps the exit code clean; any other raise, in any arm, is '
          'fatal here.', flush=True)
    return 1 if (regressions or undetermined or undeclared_failures() or stale) else 0


if __name__ == '__main__':
    sys.exit(main())
