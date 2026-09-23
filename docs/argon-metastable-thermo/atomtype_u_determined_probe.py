"""Is ``u`` determined for a bond-free neutral argon at p3 c0 -- in a MOLECULE?

This is the measurement behind the owner's ruling of 2026-09-21, and behind every passage in
``PlasmaExcitedNeutralThermo.py`` and ``report.md`` that round 60 rewrote. Run rather than taken
on the word of ``atomtype.py``'s own comment, because that comment is what caused the confusion:
it says ``Ar0e`` "answers for five (u, p, c) triples", which is true of a GROUP pattern, where
``ux`` can be hand-written and nothing checks valency. Families generate MOLECULES. There the
adjacency-list valency check applies and ``8 - c = bonds + 2p + u`` fixes ``u``.

Four blocks, and the third is the one that can refute the ruling:

  1. sweep ``u`` 0..4 at bond-free p3 c0 and record accepted/refused;
  2. check the arithmetic on both argon species this database actually carries;
  3. sweep (u, p, c) over 0..4 x 0..4 x -1..+1 and print EVERY molecule that perceives as
     ``Ar0e``. If more than one triple appears, the ruling is wrong and so is round 60's framing;
  4. contrast the group layer, where the ``ux`` spelling really does match more than the
     metastable -- and show that the extra matches are unreachable, because the molecules they
     would match cannot be constructed.

Exit code is the assertion: 0 iff exactly one (u, p, c) constructs as ``Ar0e``.

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma \\
      /home/alon/anaconda3/envs/rmg_env/bin/python atomtype_u_determined_probe.py
"""
import os
import sys

os.environ.setdefault('MPLCONFIGDIR', os.environ.get('TMPDIR', '/tmp'))

from rmgpy.molecule import Molecule, Group


def _charge(c):
    """``c0``, not ``c+0``. The parser refuses the signed spelling of zero, and the first
    version of this probe used ``%+d`` throughout -- which made every molecule in block 3
    unbuildable and printed a confident, empty, WRONG answer. Kept as a named function so
    the spelling is in one place."""
    return 'c0' if c == 0 else 'c%+d' % c


def _molecule(u, p, c):
    """Build it or say why not. Returns (molecule, None) or (None, reason)."""
    adj = 'multiplicity %d\n1 Ar u%d p%d %s\n' % (u + 1, u, p, _charge(c))
    try:
        mol = Molecule().from_adjacency_list(adj)
        mol.update_atomtypes()
        return mol, None
    except Exception as exc:                                   # noqa: BLE001 - reporting a refusal
        detail = [line.strip() for line in str(exc).strip().splitlines() if line.strip()]
        return None, '%s: %s' % (type(exc).__name__, detail[-1] if detail else '')


print('=== 1. MOLECULE layer: Ar, bond-free, p3 c0, u swept ===', flush=True)
for u in range(5):
    mol, why = _molecule(u, 3, 0)
    if mol is None:
        print('  u%d  REFUSED   %s' % (u, why), flush=True)
    else:
        atom = mol.atoms[0]
        print('  u%d  ACCEPTED  atomtype=%s  p=%d  c=%d  bonds=%d'
              % (u, atom.atomtype.label, atom.lone_pairs, atom.charge, len(atom.bonds)),
              flush=True)

print('\n=== 2. the arithmetic: 8 - c == bonds + 2p + u ===', flush=True)
for label, adj in [('Ar(3P2) metastable', 'multiplicity 3\n1 Ar u2 p3 c0\n'),
                   ('Ar ground state', '1 Ar u0 p4 c0\n')]:
    mol = Molecule().from_adjacency_list(adj)
    mol.update_atomtypes()
    atom = mol.atoms[0]
    bonds = sum(bond.order for bond in atom.bonds.values())
    lhs = 8 - atom.charge
    rhs = bonds + 2 * atom.lone_pairs + atom.radical_electrons
    print('  %-20s %-5s 8-c=%s  bonds+2p+u=%s  %s'
          % (label, atom.atomtype.label, lhs, rhs, 'HOLDS' if lhs == rhs else 'FAILS'), flush=True)

print('\n=== 3. every (u, p, c) that perceives as Ar0e -- the refutation block ===', flush=True)
found = []
built = 0
for p in range(5):
    for c in (-1, 0, 1):
        for u in range(5):
            mol, _ = _molecule(u, p, c)
            if mol is None:
                continue
            built += 1
            if mol.atoms[0].atomtype.label == 'Ar0e':
                atom = mol.atoms[0]
                found.append((atom.radical_electrons, atom.lone_pairs, atom.charge))
                print('  constructs as Ar0e: u%d p%d %s (written u%d p%d %s)'
                      % (atom.radical_electrons, atom.lone_pairs, _charge(atom.charge),
                         u, p, _charge(c)), flush=True)
print('  total distinct triples: %d' % len(set(found)), flush=True)
# Positive control. Zero Ar0e triples is the interesting answer ONLY if the sweep built
# argon at all; if it built nothing, the probe is broken and is reporting its own bug as a
# fact about the database. That is exactly what the c+0 spelling did on the first run.
print('  positive control -- argon molecules built anywhere in the sweep: %d %s'
      % (built, '' if built else '<-- PROBE IS BROKEN, NOT THE DATABASE'), flush=True)
assert built, 'the sweep constructed no argon at all; fix the probe before reading block 3'

print('\n=== 4. GROUP layer: the ux spelling matches more, and the more is unreachable ===',
      flush=True)
group = Group().from_adjacency_list('1 *1 Ar0e ux p3 c0\n')
for u in range(5):
    mol, _ = _molecule(u, 3, 0)
    if mol is None:
        print('  u%d  no such MOLECULE exists, so this group can never meet one' % u, flush=True)
    else:
        print('  u%d  molecule exists; `1 *1 Ar0e ux p3 c0` matches = %s'
              % (u, mol.is_subgraph_isomorphic(group)), flush=True)

unique = set(found) == {(2, 3, 0)}
print('\nRESULT: Ar0e is metastable argon uniquely in a molecule = %s' % unique, flush=True)
sys.exit(0 if unique else 1)
