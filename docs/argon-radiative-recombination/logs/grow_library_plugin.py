#!/usr/bin/env python
# encoding: utf-8

"""A pytest plugin that grows every plasma kinetics library by one same-reactant channel.

Load with ``-p grow_library_plugin``. Every library then reports, in addition to what it
ships, a synthetic twin of each of its reactions: **identical reactants, products renamed**.
That is the shape of the collision this campaign is heading for -- ``Ar+ => Ar`` beside
``Ar+ => Ar*``, two channels of one reactant -- and it is deliberately the shape the previous
probe could not produce, because that one renamed the *reactants* and so could never collide
with a reactant-keyed selector.

Nothing is written to the database. The growth is a wrapper around
``KineticsLibrary.get_library_reactions``, which rebuilds its list on every call, so the
injected twin lives only for the duration of the process.

What a run under this plugin is asking is not "do the tests pass" -- they should not, the
libraries no longer hold what the coverage tests say they hold. It is **"do the tests still
RUN"**: a failure is a check that argued with you, an error is a check that silently stopped
existing. See ``probe_fixture_survives_growth.py``, which runs pytest twice and compares.
"""

import copy

from rmgpy.data.kinetics.library import KineticsLibrary

_shipped_get_library_reactions = KineticsLibrary.get_library_reactions


def _labels(species_list):
    return tuple(sorted(s.label for s in species_list))


def _grown_get_library_reactions(self):
    reactions = _shipped_get_library_reactions(self)
    grown = list(reactions)
    for reaction in reactions:
        twin = copy.deepcopy(reaction)

        # Rename only products that are NOT the same object as one of the reactants.
        # ``Ar + e- => Arp + e- + e-`` holds ONE electron Species appearing on both sides,
        # and ``deepcopy`` preserves that sharing inside the copy -- so renaming the
        # products renames the reactant too, the twin's reactants come out as
        # ``('Ar', 'e-**')``, and it cannot collide with a reactant-keyed selector. That is
        # how the first version of this plugin silently reproduced the very defect it was
        # written to expose, on the one library where a species is shared across the arrow.
        shared = {id(s) for s in twin.reactants}
        renamed = 0
        for species in twin.products:
            if id(species) not in shared:
                species.label = species.label + '*'
                renamed += 1

        # A twin that does not actually collide proves nothing, so refuse to hand one back.
        # This probe's entire job is to fail in the direction of the defect; a twin that
        # cannot is worse than no twin, because it reports PASS.
        if renamed == 0 or _labels(twin.reactants) != _labels(reaction.reactants) \
                or _labels(twin.products) == _labels(reaction.products):
            raise AssertionError(
                'growth plugin built a twin that cannot collide for {0!r}: reactants '
                '{1} vs {2}, products {3} vs {4}. Fix the plugin; do not read the '
                'result.'.format(self.label, _labels(twin.reactants),
                                 _labels(reaction.reactants), _labels(twin.products),
                                 _labels(reaction.products)))
        grown.append(twin)
    return grown


def pytest_configure(config):
    KineticsLibrary.get_library_reactions = _grown_get_library_reactions


def pytest_unconfigure(config):
    KineticsLibrary.get_library_reactions = _shipped_get_library_reactions
