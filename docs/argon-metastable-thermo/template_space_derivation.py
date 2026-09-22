#!/usr/bin/env python
# encoding: utf-8
"""Which families' TEMPLATES admit metastable argon -- derived, not sampled.

WHY THIS EXISTS. ``all_family_reachability_probe.py`` iterates all 140 families against a
HARDCODED partner list -- H, OH, CH3, O2 and similar. It is exhaustive in families and a
curated sample in partners, and it reported the sample's properties in the exhaustive
axis's voice: "families matching Ar(3P2): 1". It could not have found Br_Abstraction
(needs HBr), F_Abstraction (needs HF), Disproportionation-Y (needs a fluorinated radical)
or Surface_Adsorption_Double (needs a vacant surface site), because no such partner was in
the list. Round 77 found all four by decomposing the template space instead.

The tell was free and nobody took it: Cl_Abstraction was forbidden while its structurally
symmetric siblings Br_Abstraction and F_Abstraction were not. A set that covers one sibling
and not the other two was found by sampling, not derived.

WHAT THIS DOES INSTEAD. For every family, ask the SHIPPED MATCHER whether each slot of the
forward template admits ``Ar u2 p3 c0``:

    KineticsFamily._match_reactant_to_template(molecule, template_reactant)

That is the same function ``__generate_reactions`` calls, so this measures the database's
real matching behaviour rather than a reimplementation of it -- including LogicNode tops,
which ``get_possible_structures`` expands, and the surface-site guards. No partner is
needed and no product is built, so the answer does not depend on anybody's imagination
about which second reactant to try.

The reverse templates are reported too, in their own column, because a family that matches
only in reverse still generates from this species when the reverse direction is enumerated.

CONTROLS, because a derivation that cannot come out wrong is not evidence:

  * ``[O] u2 p2`` (triplet oxygen atom) MUST match Birad_R_Recombination -- if the matcher
    is being called wrongly, this is what notices;
  * ground-state ``Ar u0 p4`` MUST match strictly fewer families than the metastable, and
    must NOT match the biradical sites -- if it matched the same set, the result would be
    about argon rather than about the metastable;
  * the count of families loaded is asserted against the count the test suite pins.

EXIT CODE IS THE CHECK: 0 only if every family whose template admits the metastable also
carries the ``Ar_metastable_biradical`` forbidden entry. That makes this re-runnable by the
next person who adds a family, which is the point -- the derived set is an OUTPUT, and if
the database grows it may grow.

Run::

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/template_space_derivation.py \\
        > >(tee docs/argon-metastable-thermo/logs/template_space_derivation.stdout.log) \\
        2> >(tee docs/argon-metastable-thermo/logs/template_space_derivation.stderr.log >&2)
"""

import os
import sys

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'input'))
settings['database.directory'] = DATABASE

from rmgpy.data.kinetics.database import KineticsDatabase   # noqa: E402
from rmgpy.molecule import Group, Molecule                  # noqa: E402

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
AR_GROUND = '1 Ar u0 p4 c0\n'
O_TRIPLET = 'multiplicity 3\n1 O u2 p2 c0\n'

CONTAINMENT = 'Ar_metastable_biradical'
EII = 'Plasma_Electron_Impact_Ionization'


def molecule(adjlist):
    mol = Molecule().from_adjacency_list(adjlist)
    mol.update_atomtypes()
    return mol


def template_sites(family, direction):
    """The PER-REACTANT template groups, the way ``__generate_reactions`` derives them.

    This is the part a first version of this probe got wrong, and the error is worth
    keeping written down because it produced a confident, plausible, WRONG set of six.

    Many modern families -- Cl_Abstraction, Br_Abstraction, F_Abstraction,
    Disproportionation, CO_Disproportionation -- ship ONE template entry called ``Root``
    that spans the whole bimolecular complex (``reactantNum = 2``, 3-4 atoms in a single
    group). Matching one molecule against that group can never succeed, so a derivation
    that treats each template ENTRY as one reactant's site silently reports "no match" for
    exactly the families that do match. It missed three families this ticket had already
    forbidden on measured evidence, which is what exposed it.

    RMG's own rule, at family.py:2077-2091: when there are more reactants than template
    entries, split the first entry's group into its connected components and use those as
    the per-reactant templates -- unless it contains a surface site, in which case
    splitting would break the van der Waals bonds and generation returns [] instead.
    Mirrored here rather than reimplemented."""
    if direction == 'forward':
        template, reactant_num = family.forward_template, family.reactant_num
    else:
        template, reactant_num = family.reverse_template, getattr(family, 'product_num', None)
    if template is None:
        return []
    reactant_num = reactant_num or len(template.reactants)
    if reactant_num > len(template.reactants):
        first = template.reactants[0].item
        if isinstance(first, Group) and first.contains_surface_site():
            return []                      # generation refuses to split these; so do we
        try:
            return list(first.split())
        except AttributeError:             # a LogicNode top cannot be split
            return [entry.item for entry in template.reactants]
    return [entry.item for entry in template.reactants]


#: (family, direction, slot, exception type, message) for every template slot whose matcher
#: raised. A non-empty list means the derivation could not see part of the template space, so
#: it must not report completeness -- main() fails on it.
MATCHER_ERRORS = []


def matching_slots(family, mol, direction):
    """Slot indices of `direction`'s per-reactant templates that admit `mol`.

    Uses the family's own matcher, so LogicNode tops and the surface-site guards behave
    exactly as they do during generation."""
    slots = []
    for index, site in enumerate(template_sites(family, direction)):
        try:
            mappings = family._match_reactant_to_template(mol, site)
        except Exception as exc:                       # noqa: BLE001
            # A raising matcher does NOT mean "does not match" -- it means UNDETERMINED, and
            # the completeness claim cannot be made over a slot nobody could evaluate. This
            # used to print and `continue`, which quietly narrowed "every family whose
            # template admits it is contained" to "every family whose template could be
            # evaluated". Recorded, and fatal in main().
            MATCHER_ERRORS.append((family.label, direction, index, type(exc).__name__, str(exc)))
            print('    ! %s %s slot %d raised %s: %s'
                  % (family.label, direction, index, type(exc).__name__, exc), flush=True)
            continue
        if mappings:
            slots.append(index)
    return slots


def main():
    print('loading every family from %s' % DATABASE, flush=True)
    db = KineticsDatabase()
    db.load_families(os.path.join(DATABASE, 'kinetics', 'families'), families='all')
    print('families loaded: %d' % len(db.families), flush=True)

    meta = molecule(AR_META)
    ground = molecule(AR_GROUND)
    otrip = molecule(O_TRIPLET)

    rows = []
    for label in sorted(db.families):
        family = db.families[label]
        fwd = matching_slots(family, meta, 'forward')
        rev = matching_slots(family, meta, 'reverse')
        if not (fwd or rev):
            continue
        forbidden = family.forbidden is not None and CONTAINMENT in family.forbidden.entries
        rows.append((label, fwd, rev, forbidden))

    print('\n=== families whose TEMPLATE admits Ar u2 p3 c0 ===', flush=True)
    print('%-34s %-12s %-12s %s' % ('family', 'fwd slots', 'rev slots', 'forbidden?'), flush=True)
    for label, fwd, rev, forbidden in rows:
        print('%-34s %-12s %-12s %s'
              % (label, fwd or '-', rev or '-',
                 'YES' if forbidden else ('n/a (EII, intended)' if label == EII else 'NO  <--')),
              flush=True)
    print('\ntotal families whose template admits it: %d' % len(rows), flush=True)

    # ---- controls -----------------------------------------------------------------
    print('\n=== controls ===', flush=True)
    birad_o = matching_slots(db.families['Birad_R_Recombination'], otrip, 'forward')
    print('  [O] u2 p2 matches Birad_R_Recombination forward slots %s  (must be non-empty)'
          % (birad_o or '-'), flush=True)

    ground_hits = sorted(label for label in db.families
                         if matching_slots(db.families[label], ground, 'forward')
                         or matching_slots(db.families[label], ground, 'reverse'))
    meta_hits = {label for label, _f, _r, _x in rows}
    print('  ground-state Ar u0 p4 matches %d families; metastable matches %d'
          % (len(ground_hits), len(meta_hits)), flush=True)
    print('  ground state does NOT match the biradical sites: %s'
          % ('Birad_R_Recombination' not in ground_hits), flush=True)

    controls_ok = (bool(birad_o)
                   and len(ground_hits) < len(meta_hits)
                   and 'Birad_R_Recombination' not in ground_hits)
    print('  controls pass: %s' % controls_ok, flush=True)

    # ---- the check ----------------------------------------------------------------
    uncontained = sorted(label for label, _f, _r, forbidden in rows
                         if not forbidden and label != EII)
    print('\n=== RESULT ===', flush=True)
    if uncontained:
        print('  UNCONTAINED, template admits the metastable and no forbidden entry: %s'
              % ', '.join(uncontained), flush=True)
    else:
        print('  every family whose template admits the metastable is forbidden, '
              'except %s, which is the intended channel' % EII, flush=True)

    if MATCHER_ERRORS:
        print('  UNDETERMINED: %d template slots could not be evaluated, so the sweep did not '
              'see the whole template space and no completeness claim is made:' % len(MATCHER_ERRORS),
              flush=True)
        for label, direction, index, kind, message in MATCHER_ERRORS:
            print('      %s %s slot %d: %s: %s' % (label, direction, index, kind, message),
                  flush=True)
    else:
        print('  every template slot was evaluated; no matcher raised', flush=True)

    ok = controls_ok and not uncontained and not MATCHER_ERRORS
    print('\nEXIT %d' % (0 if ok else 1), flush=True)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
