#!/usr/bin/env python
# encoding: utf-8

"""
Pin ``database.directory`` to this worktree before any test module is imported.

RMG resolves ``database.directory`` from an ``rmgrc`` found in the current working
directory, in ``~/.rmg``, or beside the ``rmgpy`` package, and its resolution ends in
``return  # fail silently``. There is no ``rmgrc`` at this repository root, and the one
that ships with the plasma RMG-Py worktrees points at ``../RMG-database-plasma/input``
- a *different* checkout that does not contain this repository's work. So without this
file the suites here either fail their own pin assertion en masse (which is what they
did) or, worse, quietly measure a database nobody edited.

Setting it here rather than in each test module also removes an ordering hazard: a
module-level pin only protects the file it is written in, so whether a suite was pinned
depended on which other test files pytest happened to import first.

pytest imports ``conftest.py`` before collecting the test modules beside it, which is
what makes this early enough to matter.
"""

import os

from rmgpy import settings

THIS_DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'input'))

settings['database.directory'] = THIS_DATABASE
