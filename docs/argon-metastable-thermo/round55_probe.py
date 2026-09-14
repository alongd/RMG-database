#!/usr/bin/env python
# encoding: utf-8
"""
Round-55 measurements: what RMG does to the Ar(3P2) numbers after it has them.

Four questions, each answered by measurement rather than by reading:

  A. E0 -- does the entry's stated E0 agree with what RMG derives from the same entry?
  B. Temperature range -- does the entry's advertised 6000 K survive normal processing,
     and what do the raw ThermoData functions do above their tabulated range?
  C. Degeneracy -- how many electronic states does each RMG path think this species has?
  D. Lumping at discharge temperatures -- 2-level and 4-level, S and H, against 1s5 alone.

Run:

    PYTHONPATH=/home/alon/Code/RMG-Py-plasma python docs/argon-metastable-thermo/round55_probe.py \
        > >(tee -a docs/argon-metastable-thermo/logs/round55_probe.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/round55_probe.stderr.log >&2)
"""

import math
import os
import traceback

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
settings['database.directory'] = os.path.abspath(
    os.path.join(HERE, os.pardir, os.pardir, 'input'))

from rmgpy.data.thermo import ThermoDatabase           # noqa: E402
from rmgpy.molecule import Molecule                     # noqa: E402
from rmgpy.species import Species                       # noqa: E402
from rmgpy.statmech import Conformer                    # noqa: E402
from rmgpy.thermo import NASA, ThermoData               # noqa: E402

R = 8.314462618
T0 = 298.15
HC_NA = 11.9626565957

LIB = os.path.join(settings['database.directory'], 'thermo', 'libraries')
GRP = os.path.join(settings['database.directory'], 'thermo', 'groups')

AR = '1 Ar u0 p4 c0\n'
AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
ARP = 'multiplicity 2\n1 Ar u1 p3 c+1\n'

#: NIST ASD ver. 5.12, Ar I, the four 3p5.4s levels: (Paschen, LS, E cm^-1, g)
LEVELS_4S = [('1s5', '3P2', 93143.7600, 5),
             ('1s4', '3P1', 93750.5978, 3),
             ('1s3', '3P0', 94553.6652, 1),
             ('1s2', '1P1', 95399.8276, 3)]


def banner(text):
    print("\n" + text)
    print("=" * len(text))


def sub(text):
    print("\n  " + text)
    print("  " + "-" * len(text))


db = ThermoDatabase()
db.load_libraries(LIB)
db.load_groups(GRP)
entry = db.libraries['PlasmaExcitedNeutralThermo'].entries['Ar(3P2)']
data = entry.data

# =====================================================================================
banner("A. E0 -- the entry's stated value against what RMG derives from the same entry")
# =====================================================================================
sub("A1. the two paths")
stated = data.E0.value_si / 1000.0 if data.E0 is not None else None
print("    entry.data.E0 as stored           : %s"
      % ("%.4f kJ/mol" % stated if stated is not None else "None (not stated)"))
wilhoit = data.to_wilhoit(B=1000.0)
print("    data.to_wilhoit(B=1000).E0        : %.4f kJ/mol" % (wilhoit.E0.value_si / 1000.0))
print("    data.H298 as stored               : %.4f kJ/mol" % (data.H298.value_si / 1000.0))
if stated is not None:
    print("    stored E0 - derived E0            : %+.4f kJ/mol"
          % (stated - wilhoit.E0.value_si / 1000.0))
print("    5/2 R T at 298.15 K               : %.4f kJ/mol" % (2.5 * R * T0 / 1000.0))
print("    H298(stored) - derived E0         : %+.4f kJ/mol"
      % (data.H298.value_si / 1000.0 - wilhoit.E0.value_si / 1000.0))

sub("A2. which one the runtime consumes")
print("    thermoengine.process_thermo_data sets spc.conformer.E0 = wilhoit.E0")
print("    (rmgpy/thermo/thermoengine.py:75-78), and ThermoData.to_wilhoit")
print("    (thermodata.pyx:366-389) reads Tdata/Cpdata/H298/S298 ONLY -- self.E0 is")
print("    never consulted. So a stated E0 is inert on the path that matters and")
print("    visible on the path that does not.")

sub("A3. the same question asked of the sibling cation entry, for context")
arp_entry = db.libraries['PlasmaCationThermo'].entries['[Arp]']
arp_w = arp_entry.data.to_wilhoit(B=1000.0)
print("    [Arp] stated E0                   : %.4f kJ/mol"
      % (arp_entry.data.E0.value_si / 1000.0))
print("    [Arp] derived E0                  : %.4f kJ/mol" % (arp_w.E0.value_si / 1000.0))
print("    [Arp] stated - derived            : %+.4f kJ/mol"
      % (arp_entry.data.E0.value_si / 1000.0 - arp_w.E0.value_si / 1000.0))
print("    -> the same collision, in a library this ticket must not edit.")

# =====================================================================================
banner("B. TEMPERATURE RANGE -- does the advertised 6000 K survive?")
# =====================================================================================
sub("B1. what the entry declares")
print("    Tmin = %.2f K, Tmax = %.2f K; Tdata spans %.2f - %.2f K"
      % (data.Tmin.value_si, data.Tmax.value_si,
         data.Tdata.value_si[0], data.Tdata.value_si[-1]))
for T in (298.15, 5000.0, 6000.0, 8000.0):
    print("    is_temperature_valid(%7.2f)     : %s" % (T, data.is_temperature_valid(T)))

sub("B2. normal processing -- thermoengine.process_thermo_data -> NASA")
spc = Species(label='Ar(3P2)', molecule=[Molecule().from_adjacency_list(AR_META)])
resolved = db.get_thermo_data(spc)
print("    library returns a %s (comment: %s)"
      % (type(resolved).__name__, (resolved.comment or '').strip()))
try:
    from rmgpy.thermo.thermoengine import process_thermo_data
    nasa = process_thermo_data(spc, resolved, thermo_class=NASA)
    print("    processed to %s, Tmin = %.1f K, Tmax = %.1f K"
          % (type(nasa).__name__, nasa.Tmin.value_si, nasa.Tmax.value_si))
    print("    spc.conformer.E0 after processing  : %.4f kJ/mol"
          % (spc.conformer.E0.value_si / 1000.0))
    for T in (298.15, 5000.0, 6000.0):
        try:
            print("      NASA Cp(%7.2f) = %8.3f  S = %9.4f  H = %10.4f"
                  % (T, nasa.get_heat_capacity(T), nasa.get_entropy(T),
                     nasa.get_enthalpy(T) / 1000.0))
        except Exception as exc:                                  # noqa: BLE001
            print("      NASA at %7.2f K RAISED %s: %s" % (T, type(exc).__name__, exc))
except Exception:                                                  # noqa: BLE001
    print("    process_thermo_data itself raised:")
    traceback.print_exc()

sub("B3. raw ThermoData above its tabulated range")
print("    %8s %10s %12s %14s" % ("T (K)", "Cp", "S", "H (kJ/mol)"))
for T in (1500.0, 6000.0, 8000.0, 10000.0):
    print("    %8.1f %10.4f %12.4f %14.4f"
          % (T, data.get_heat_capacity(T), data.get_entropy(T),
             data.get_enthalpy(T) / 1000.0))
print("    exact 5/2 R monatomic, for comparison:")
for T in (1500.0, 6000.0, 8000.0, 10000.0):
    s_exact = data.S298.value_si + 2.5 * R * math.log(T / 298.0)
    h_exact = (data.H298.value_si + 2.5 * R * (T - 298.0)) / 1000.0
    print("    %8.1f %10.4f %12.4f %14.4f" % (T, 2.5 * R, s_exact, h_exact))

# =====================================================================================
banner("C. DEGENERACY -- how many electronic states does each path think there are?")
# =====================================================================================
mol = Molecule().from_adjacency_list(AR_META)
spc_c = Species(label='Ar(3P2)', molecule=[mol])
print("  molecule.multiplicity                         : %d" % mol.multiplicity)
print("  radical_electrons                             : %d" % mol.atoms[0].radical_electrons)
print("  g used to build this entry's S298 (2J+1, J=2) : 5")
print("  R ln 5 = %.4f J/(mol*K) is what S298 carries" % (R * math.log(5.0)))

spc_p = Species(label='Ar(3P2)', molecule=[Molecule().from_adjacency_list(AR_META)])
proc = db.get_thermo_data(spc_p)
try:
    from rmgpy.thermo.thermoengine import process_thermo_data
    process_thermo_data(spc_p, proc, thermo_class=NASA)
except Exception:                                                  # noqa: BLE001
    pass
conf = spc_p.conformer
print("\n  after process_thermo_data, spc.conformer is a %s" % type(conf).__name__)
if conf is not None:
    print("    conformer.spin_multiplicity                 : %s" % conf.spin_multiplicity)
    print("    conformer.optical_isomers                   : %s" % conf.optical_isomers)
    print("    conformer.modes                             : %s" % conf.modes)
    print("    conformer.get_partition_function(298.15)    : %s"
          % (conf.get_partition_function(T0) if conf.modes else '<no modes>'))

sub("C2. explicit statmech generation")
spc_s = Species(label='Ar(3P2)', molecule=[Molecule().from_adjacency_list(AR_META)])
spc_s.thermo = db.get_thermo_data(spc_s)
try:
    spc_s.generate_statmech()
    c = spc_s.conformer
    print("    generate_statmech -> spin_multiplicity      : %s" % c.spin_multiplicity)
    print("                         optical_isomers        : %s" % c.optical_isomers)
    print("                         modes                  : %s" % c.modes)
except Exception as exc:                                           # noqa: BLE001
    print("    generate_statmech RAISED %s: %s" % (type(exc).__name__, exc))

sub("C3. a bare Conformer, i.e. what a species gets before anything touches it")
print("    Conformer().spin_multiplicity               : %s" % Conformer().spin_multiplicity)
print("    Conformer().optical_isomers                 : %s" % Conformer().optical_isomers)

# =====================================================================================
banner("D. LUMPING AT DISCHARGE TEMPERATURES -- what a reader needs to judge reuse")
# =====================================================================================


def manifold(levels, T):
    """(S_el, H_el) of a manifold relative to its lowest level. levels = [(g, E cm^-1)]."""
    e0 = min(e for _g, e in levels)
    xs = [(g, (e - e0) * HC_NA / (R * T)) for g, e in levels]
    q = sum(g * math.exp(-x) for g, x in xs)
    mean = sum(g * x * math.exp(-x) for g, x in xs) / q
    return R * (math.log(q) + mean), mean * R * T / 1000.0, q


two = [(g, e) for _p, _ls, e, g in LEVELS_4S if _p in ('1s5', '1s3')]
four = [(g, e) for _p, _ls, e, g in LEVELS_4S]
single = R * math.log(5.0)

print("  Relative to the 1s5 (3P2) level ALONE, which is what this entry is:")
print("  %8s | %10s %10s | %10s %10s %10s"
      % ("T (K)", "dS 2-lvl", "dH 2-lvl", "dS 4-lvl", "dH 4-lvl", "n(rest)/n(1s5)"))
for T in (298.15, 500.0, 1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0):
    s2, h2, _q2 = manifold(two, T)
    s4, h4, q4 = manifold(four, T)
    print("  %8.2f | %10.4f %10.4f | %10.4f %10.4f %10.4f"
          % (T, s2 - single, h2, s4 - single, h4, (q4 - 5.0) / 5.0))
print("\n  dS in J/(mol*K), dH in kJ/mol. The last column is the equilibrium population")
print("  of the other three 4s levels relative to 1s5, sum(g exp(-E/RT)) / 5.")
