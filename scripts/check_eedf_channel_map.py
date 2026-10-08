#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2019 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

"""
Check a frozen EEDF channel map (input/eedf/argon_channel_map.yaml) by regenerating it.

The map is generated: everything in it is derived by scripts/gen_eedf_channel_map.py from the local LXCat
files (the assembled LoKI-B directory and the original source files, both outside any repository, so they
are passed as arguments; the assembled directory's manifest.json says which source files are required),
the RMG library, and the hand-written overlay that gives each collision its class and RMG reaction, and
each species those reactions name its RMG record. This
checker runs that derivation and passes only when:

  - the derivation finds no problem. That covers the assembled files read with LoKI-B's own grammar,
    exactly the source and collision files the store's manifest names, under its names and hashes, a
    manifest that agrees with itself and, field by field, with the one the files give, every collision
    proven against its hash-pinned source block, the conventions each transformation needs, the state
    catalogue against the source thresholds, every source block used or listed, and the overlay against
    the source-derived policy and the RMG library, which RMG's own loader must load first: every collision
    in the overlay exactly once, an elastic collision class B, an ionisation class A mapped to an
    ionisation reaction, every load-bearing 4s product class A mapped to a reaction producing its species,
    one class per above-4s family, and one RMG species per LoKI-B state, whose reference record is one
    atom of the state's element with its charge and multiplicity, which the library holds as that very
    species by RMG's own comparison (state fields included) or which carries the canonical name of a
    missing 4s level, each record's own state fields consistent with the state it stands for (its LS
    term; no vibrational level, metal or facet on a free atom or electron), and each reaction found by
    the species and direction RMG loaded, no entry holding it another way;
  - the committed map equals the regenerated text byte for byte, so no field in it, file list, hash,
    threshold, label, convention statement, state name, species list or attribution, can be edited
    out of step with what it describes;
  - with --loki-rates: LoKI-B's own collision list (a rateCoefficients.txt) is the derived one.

Otherwise it prints each problem and RESULT: FAIL and exits 1. A malformed map, overlay or store is a
refusal with its reason, never a pass; an unexpected error is printed to stderr and refused.

usage: check_eedf_channel_map.py MAP --overlay FILE --assembled DIR --source FILE [--source FILE ...]
                                 [--loki-rates FILE] [--database DIR]
"""

import argparse
import os
import re
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_eedf_channel_map  # noqa: E402


def first_difference(committed, regenerated):
    """How many lines differ between two texts, and the first one that does, both sides shown."""
    a, b = committed.split('\n'), regenerated.split('\n')
    differing = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
    k = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    show = lambda lines: repr(lines[k][:150]) if k < len(lines) else 'the end of the file'  # noqa: E731
    return differing, f'first at line {k + 1}: the map has {show(a)}, the regeneration {show(b)}'


def check(args):
    problems = []
    try:
        text, derived, summary, labels = gen_eedf_channel_map.generate(args.overlay, args.assembled, args.source,
                                                                        args.database)
    except Exception as exc:
        traceback.print_exc()
        text, derived, summary, labels = None, [f'regeneration failed: {type(exc).__name__}: {exc}'], '', []
    problems.extend(derived)
    try:
        committed = open(args.map, 'rb').read()
    except OSError as exc:
        committed = None
        problems.append(f'map {args.map}: cannot be read ({type(exc).__name__})')
    if committed is not None and text is not None and committed != text.encode():
        try:
            n, where = first_difference(committed.decode('utf-8'), text)
            problems.append(f'the map differs from its regeneration: {n} lines differ, {where}')
        except UnicodeDecodeError:
            problems.append('the map differs from its regeneration: it is not even UTF-8 text')
    if args.loki_rates:
        try:
            solved = set()
            for line in open(args.loki_rates).read().splitlines()[1:]:
                m = re.match(r'\s*\S+\s+\S+\s+(e \+ .*)$', line)
                if m:
                    solved.add(m.group(1).strip())
        except (OSError, UnicodeDecodeError) as exc:
            problems.append(f'--loki-rates {args.loki_rates}: cannot be read ({type(exc).__name__})')
        else:
            for label in sorted(solved - set(labels)):
                problems.append(f'LoKI-B solved a collision the assembled files do not hold: {label}')
            for label in sorted(set(labels) - solved):
                problems.append(f'collision LoKI-B did not solve: {label}')
    print(gen_eedf_channel_map.printable(summary))
    for p in problems:
        print('FAIL', gen_eedf_channel_map.printable(p))
    if problems:
        print(f'RESULT: FAIL ({len(problems)} problems)')
        return 1
    print(f'RESULT: PASS (the map equals its regeneration from the store, the overlay and {gen_eedf_channel_map.LIBRARY}; '
          f'{len(labels)} collisions, the overlay within policy)')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('map', help='the committed channel-map YAML')
    parser.add_argument('--overlay', required=True, help='the hand-written overlay: class and RMG reaction per collision')
    parser.add_argument('--assembled', required=True, help='directory holding the assembled LoKI-B files')
    parser.add_argument('--source', action='append', required=True,
                        help='a source LXCat file (repeatable): every file the set was built from or compared with')
    parser.add_argument('--loki-rates', help='a LoKI-B rateCoefficients.txt solved on the assembled set')
    parser.add_argument('--database', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input'),
                        help="the database 'input' directory holding the RMG library (default: the one beside this "
                             "script)")
    sys.exit(check(parser.parse_args()))
