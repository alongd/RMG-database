"""Pin the database under test to THIS worktree.

databaseTest.py lives in the engine tree, so RMG-database's own test/conftest.py is never
collected for it and the directory would otherwise resolve to the shared primary checkout.
The print + asserts are the positive control: a silent pin that did not take would test
somebody else's tree and read like a pass.

Load it as a pytest plugin, from a scratch directory so that the suite's htmlcov/ and
.coverage -- neither of which this repository ignores -- land outside the worktree:

    cd "$SCRATCH"
    PYTHONPATH=/home/alon/Code/RMG-Py-plasma:/home/alon/Code/RMG-database-i221-argon-metastable-thermo/docs/argon-metastable-thermo \\
      pytest -p pin_database_directory -v \\
      /home/alon/Code/RMG-Py-plasma/test/database/databaseTest.py
"""
import os
from rmgpy import settings

WORKTREE = '/home/alon/Code/RMG-database-i221-argon-metastable-thermo'
settings['database.directory'] = os.path.join(WORKTREE, 'input')

_groups = os.path.join(WORKTREE, 'input', 'kinetics', 'families',
                       'Birad_R_Recombination', 'groups.py')
_containment = 'Ar_metastable_biradical' in open(_groups).read()
_library = os.path.exists(os.path.join(WORKTREE, 'input', 'thermo', 'libraries',
                                       'PlasmaExcitedNeutralThermo.py'))
print('PIN database.directory = %s' % settings['database.directory'], flush=True)
print('PIN containment present in Birad_R_Recombination/groups.py = %s' % _containment, flush=True)
print('PIN PlasmaExcitedNeutralThermo.py present = %s' % _library, flush=True)
assert _containment and _library, 'the pinned tree is not the tree under test'
