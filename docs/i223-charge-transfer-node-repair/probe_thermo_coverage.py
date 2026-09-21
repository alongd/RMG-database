#!/usr/bin/env python
# encoding: utf-8
"""
I-223: can this database give library thermo to the species Plasma_Charge_Transfer touches?

THE PREMISE THIS PROBES.  Every step left on the ticket that involves an actual RMG job --
"install it under input/ and run a reactor", "write Plasma_Charge_Transfer_Reverse and see it
fire" -- rests on an unstated assumption: that a reactor can be assembled from the species this
family consumes and produces.  It cannot assemble one out of kinetics alone.  RMG needs thermo for
every species it puts in the core, and the plasma campaign's own rule (see the i127/i157/i186
tickets) is that an ion's thermo must come from a LIBRARY: group additivity fabricates 0.0 for a
disconnected ion and, for a free monatomic ion, is not defined at all.

So the question with a yes/no answer is: for each species appearing in the family's 16 training
entries, does `ThermoDatabase.get_thermo_data_from_libraries` return an entry?

Matching is by isomorphism against every library the installed database holds -- not by label and
not by SMILES.  That matters twice over: a label is free text, and RMG's SMILES round trip
corrupts monatomic ions of both signs (`[O-]` loses its charge, `Ar+` returns as Ar2+).  Every
species here therefore comes from the training entry's own Molecule object, never from a string.

    ./run.sh thermo-coverage probe_thermo_coverage.py

Exit status is 0 when every species is covered, 1 when any is missing.  A missing species is not a
defect in this family -- it is a statement about what the database can and cannot simulate today.
"""

import os
import sys

from rmgpy import settings
from rmgpy.data.thermo import ThermoDatabase

from probe_nodes import load_family, FAMILY, FAMILY_ROOT  # noqa: E402


def species_of(reaction):
    """Every species on both sides of a training reaction, as (label, Molecule) pairs."""
    out = []
    for spc in list(reaction.reactants) + list(reaction.products):
        mol = spc.molecule[0] if hasattr(spc, 'molecule') and spc.molecule else spc
        out.append((str(spc.label or ''), mol))
    return out


def main():
    db_dir = settings['database.directory']
    print('cwd                 = {0}'.format(os.getcwd()))
    print('family loaded from  = {0}'.format(
        os.path.normpath(os.path.join(FAMILY_ROOT, FAMILY))))
    print('thermo read from    = {0}'.format(os.path.join(db_dir, 'thermo')))
    print('  (database.directory, and this probe DOES use it -- the thermo libraries are the')
    print('   thing under test here, unlike the family, which is loaded from its explicit path)')
    print('')

    family = load_family()
    entries = family.get_training_depository().entries
    print('training entries    = {0}'.format(len(entries)))

    tdb = ThermoDatabase()
    tdb.load(os.path.join(db_dir, 'thermo'), libraries=None, depository=False, surface=False)
    print('thermo libraries    = {0}'.format(len(tdb.library_order)))
    print('')

    # One row per DISTINCT species, but remember every entry it appears in.
    seen = {}       # formula-independent key -> [label, molecule, set(entry indices)]
    for entry in entries.values():
        for label, mol in species_of(entry.item):
            key = mol.to_adjacency_list()
            if key not in seen:
                seen[key] = [label, mol, set()]
            seen[key][2].add(entry.index)

    row = '{0:<8} {1:<26} {2:>6} {3:<34} {4}'
    header = row.format('species', 'adjacency (one line)', 'charge', 'thermo library', 'entries')
    print(header)
    print('-' * len(header))

    missing = []
    covered = []
    from rmgpy.species import Species
    for key in sorted(seen, key=lambda k: seen[k][0]):
        label, mol, where = seen[key]
        spc = Species(molecule=[mol])
        try:
            spc.generate_resonance_structures()
        except Exception:
            pass
        hit = None
        try:
            hit = tdb.get_thermo_data_from_libraries(spc)
        except Exception as exc:
            hit = None
            note = '!! {0}'.format(type(exc).__name__)
        else:
            note = None

        flat = ' / '.join(line.strip() for line in mol.to_adjacency_list().strip().split('\n')
                          if not line.startswith('multiplicity'))
        if len(flat) > 26:
            flat = flat[:23] + '...'

        if hit is None:
            verdict = note or 'MISSING -- no library entry'
            missing.append((label, sorted(where), spc))
        else:
            # get_thermo_data_from_libraries returns (thermo_data, library, entry)
            lib = hit[1].name if hasattr(hit[1], 'name') else str(hit[1])
            verdict = lib
            covered.append((label, lib))

        print(row.format(label, flat, mol.get_net_charge(), verdict,
                         ','.join(str(i) for i in sorted(where))))

    print('')
    print('covered = {0}   missing = {1}   of {2} distinct species'.format(
        len(covered), len(missing), len(seen)))

    if missing:
        print('')
        print('MISSING, and the training entries they make unsimulatable:')
        blocked = set()
        for label, where, _spc in missing:
            print('  {0:<8} entries {1}'.format(label, ','.join(str(i) for i in where)))
            blocked.update(where)
        runnable = sorted(set(e.index for e in entries.values()) - blocked)
        print('')
        print('training entries with EVERY species covered: {0} of {1}  {2}'.format(
            len(runnable), len(entries), runnable))
        part2(missing, entries)
        return 1

    print('every species in the training set has library thermo.')
    return 0


def read_library_tolerantly(path):
    """
    Parse every `.py` thermo library under `path` entry by entry, keeping what builds.

    RMG's own `ThermoDatabase.load_libraries` cannot be used here: it stops the whole file at the
    first entry whose adjacency list has no atom type today, and the branch-99 source library has
    such entries (O2+ dication and friends). An all-or-nothing loader would report "0 entries" for
    a library that holds 139, which is the opposite of the truth.

    Returns `([(label, Molecule), ...], [(label, reason), ...])`.
    """
    from rmgpy.molecule import Molecule

    good, bad = [], []

    def entry(**kwargs):
        label = kwargs.get('label', '?')
        adj = kwargs.get('molecule')
        if not isinstance(adj, str):
            bad.append((label, 'no adjacency list'))
            return
        try:
            good.append((label, Molecule().from_adjacency_list(adj)))
        except Exception as exc:
            bad.append((label, '{0}: {1}'.format(type(exc).__name__,
                                                 str(exc).split('\n')[0][:88])))

    def _any(*args, **kwargs):
        return None

    for (root, _dirs, files) in os.walk(path):
        for f in sorted(files):
            if not f.endswith('.py'):
                continue
            ns = {'entry': entry, 'ThermoData': _any, 'NASA': _any, 'NASAPolynomial': _any,
                  'Wilhoit': _any, 'name': '', 'shortDesc': '', 'longDesc': ''}
            with open(os.path.join(root, f)) as fh:
                exec(compile(fh.read(), f, 'exec'), ns, ns)

    return good, bad


def part2(missing, entries):
    """
    Does the UNTRANSLATED source library on branch 99 hold what the installed database lacks?

    The plasma carry campaign translates entries out of branch `99` into the target database one
    ticket at a time, and `99:input/thermo/libraries/plasma.py` is a 139-entry library that no
    carry has brought over. Whether it covers the gap decides whether the missing thermo is work
    that exists and needs carrying, or work nobody has done at all -- a completely different item
    on somebody's list.

    Set I223_THERMO99 to a checked-out copy of that file (the probe does not run git itself, so
    the file it reads is visible in the log):

        git show 99:input/thermo/libraries/plasma.py > $TMPDIR/plasma99/libraries/plasma.py

    A hit here is NOT a green light. Each entry still needs the per-entry convention check the
    campaign requires of any carried ion thermo (the ion convention vs the JANAF electron
    convention, I-127/I-186) before it can be trusted. This measures availability, not validity.
    """
    path = os.environ.get('I223_THERMO99')
    print('')
    print('=' * 86)
    print('PART 2 -- does the untranslated source library on branch 99 cover the gap?')
    print('')
    if not path:
        print('I223_THERMO99 not set; skipped. See this function\'s docstring for the one command.')
        return
    if not os.path.isdir(path):
        print('I223_THERMO99 = {0} is not a directory; skipped.'.format(path))
        return

    print('source library read = {0}'.format(path))
    src, unloadable = read_library_tolerantly(path)
    print('entries that build a Molecule today = {0}   that do NOT = {1}'.format(
        len(src), len(unloadable)))
    if unloadable:
        print('')
        print('THE SOURCE LIBRARY DOES NOT LOAD WHOLESALE. RMG\'s own loader stops at the first of')
        print('these, so this probe parses the file entry by entry instead:')
        for label, why in unloadable:
            print('  {0:<12} {1}'.format(label, why))
    print('')

    row = '{0:<8} {1:<40} {2}'
    print(row.format('species', 'found in branch-99 source library', 'entries it unblocks'))
    print('-' * 86)

    found = 0
    still = []
    for label, where, spc in missing:
        hit = None
        for src_label, mol in src:
            try:
                if spc.is_isomorphic(mol):
                    hit = 'plasma: {0}'.format(src_label)
                    break
            except Exception:
                continue
        if hit:
            found += 1
        else:
            still.append((label, where))
        print(row.format(label, hit or 'not there either',
                         ','.join(str(i) for i in where)))

    print('')
    print('of the {0} missing species, branch 99 holds {1} and lacks {2}'.format(
        len(missing), found, len(still)))
    blocked = set()
    for _label, where in still:
        blocked.update(where)
    runnable = sorted(set(e.index for e in entries.values()) - blocked)
    print('training entries that a FULL carry of branch 99 would make simulatable: '
          '{0} of {1}  {2}'.format(len(runnable), len(entries), runnable))
    if still:
        print('still nowhere: {0}'.format(', '.join(label for label, _ in still)))


if __name__ == '__main__':
    sys.exit(main())
