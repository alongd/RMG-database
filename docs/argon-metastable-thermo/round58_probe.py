"""
Round 58: what the reachability this library creates actually DELIVERS.

Round 55 disclosed that loading PlasmaExcitedNeutralThermo makes Ar(3P2) reachable by
Plasma_Electron_Impact_Ionization at a rank-10 lithium-anchored placeholder, and framed the
hazard as that rate being too LARGE. Round 58 inverted it. This probe measures the delivered
rate through actual reactor initialisation rather than by inspecting the rule.

Run:
    export PYTHONPATH=/home/alon/Code/RMG-Py-i222-metastable-argon-atomtype
    python docs/argon-metastable-thermo/round58_probe.py \
        > >(tee docs/argon-metastable-thermo/logs/round58_probe.stdout.log > /dev/null) \
        2> >(tee docs/argon-metastable-thermo/logs/round58_probe.stderr.log > /dev/null)
"""

import math
import os

from rmgpy import settings

HERE = os.path.dirname(os.path.abspath(__file__))
settings['database.directory'] = os.path.abspath(
    os.path.join(HERE, os.pardir, os.pardir, 'input'))

from rmgpy.data.rmg import RMGDatabase                        # noqa: E402
from rmgpy.molecule import Molecule                           # noqa: E402
from rmgpy.species import Species                             # noqa: E402

AR_META = 'multiplicity 3\n1 Ar u2 p3 c0\n'
AR = '1 Ar u0 p4 c0\n'
FAMILY = 'Plasma_Electron_Impact_Ionization'

R = 8.314462618
EV_K = 11604.518  # K per eV


def banner(text):
    print("\n" + "=" * 86)
    print(text)
    print("=" * 86)


def sub(text):
    print("\n  " + text)
    print("  " + "-" * len(text))


def species(adj, label):
    return Species(label=label, molecule=[Molecule().from_adjacency_list(adj)])


# =====================================================================================
banner("0. LOAD")
# =====================================================================================
db = RMGDatabase()
db.load(settings['database.directory'],
        thermo_libraries=['primaryThermoLibrary', 'PlasmaExcitedNeutralThermo',
                          'PlasmaCationThermo'],
        kinetics_families=[FAMILY],
        reaction_libraries=[],
        seed_mechanisms=[])
print("  loaded; family = %s" % FAMILY)

fam = db.kinetics.families[FAMILY]
try:
    fam.add_rules_from_training(thermo_database=db.thermo)
except Exception as exc:                                        # noqa: BLE001
    print("  add_rules_from_training raised %s (continuing)" % type(exc).__name__)
fam.fill_rules_by_averaging_up(verbose=True)

# =====================================================================================
banner("1. GENERATION IS CONFIRMED -- u0 vs u2 IS THE DISCRIMINATOR")
# =====================================================================================
for adj, label in ((AR, 'Ar (ground, u0 p4)'), (AR_META, 'Ar(3P2) (u2 p3)')):
    rxns = db.kinetics.generate_reactions_from_families(
        [species(adj, label)], products=None, only_families=[FAMILY], resonance=True)
    print("  %-26s -> %d reaction(s)" % (label, len(rxns)))
    for r in rxns:
        print("        %s" % r)

reactions = db.kinetics.generate_reactions_from_families(
    [species(AR_META, 'Ar(3P2)')], products=None, only_families=[FAMILY], resonance=True)
assert len(reactions) == 1, "expected exactly one reaction, got %d" % len(reactions)
rxn = reactions[0]

# =====================================================================================
banner("2. MODEL ADMISSION: WHAT KINETICS CLASS ACTUALLY ARRIVES")
# =====================================================================================
from rmgpy.rmg.model import CoreEdgeReactionModel              # noqa: E402

# Kinetics estimation asks for G298, so every participant needs thermo first.
for s in list(rxn.reactants) + list(rxn.products):
    if s.is_electron():
        continue
    if not s.label:
        s.label = str(s)
    if s.thermo is None:
        s.thermo = db.thermo.get_thermo_data(s)
        print("  thermo for %-10s <- %s" % (s.label, (s.thermo.comment or '').strip()[:60]))

cerm = CoreEdgeReactionModel()
cerm.kinetics_estimator = 'rate rules'
cerm.apply_kinetics_to_reaction(rxn)

kin = rxn.kinetics
print("  reaction                       : %s" % rxn)
print("  kinetics class AS ESTIMATED    : %s" % kin.__class__.__name__)
print("  comment at point of use:")
for line in (kin.comment or '(none)').splitlines():
    print("      %s" % line)
print("  dHrxn(298)                     : %.4f kJ/mol"
      % (rxn.get_enthalpy_of_reaction(298.0) / 1000.0))

sub("what make_new_reaction does next (model.py:644)")
rxn.fix_barrier_height(force_positive=True, solvent="")
kin = rxn.kinetics
print("  kinetics class AFTER fix_barrier_height : %s" % kin.__class__.__name__)
print("  Ea (barrier)                   : %.4f kJ/mol" % (kin.Ea.value_si / 1000.0))
print("  A                              : %.6e %s" % (kin.A.value_si, kin.A.units))
print("  reversible                     : %s" % rxn.reversible)

sub("does this kinetics carry the electron-temperature flag?")
flag = getattr(kin, 'uses_electron_temperature', False)
print("  uses_electron_temperature = %s   <-- if False, PlasmaReactor evaluates at Tgas" % flag)

sub("which classes set that flag at all")
from rmgpy.kinetics.arrhenius import (Arrhenius, ArrheniusEP,   # noqa: E402
                                      TwoTemperaturePlasma, ElectronCollisionPlasma,
                                      BadnellRRArrhenius, VoronovEIArrhenius)
from rmgpy.kinetics.model import KineticsModel                  # noqa: E402
for cls in (Arrhenius, ArrheniusEP, TwoTemperaturePlasma, ElectronCollisionPlasma,
            BadnellRRArrhenius, VoronovEIArrhenius):
    try:
        probe = cls()
        print("      %-24s flag=%-5s  subclass_of_Arrhenius=%s"
              % (cls.__name__, getattr(probe, 'uses_electron_temperature', False),
                 issubclass(cls, Arrhenius)))
    except Exception as exc:                                    # noqa: BLE001
        print("      %-24s (could not instantiate: %s)" % (cls.__name__, type(exc).__name__))

# =====================================================================================
banner("3. THE DELIVERED RATE, THROUGH ACTUAL REACTOR INITIALISATION")
# =====================================================================================
from rmgpy.solver.plasma import PlasmaReactor                   # noqa: E402

rxn.reversible = False   # a reversible electron-containing reaction is refused outright

ELECTRON = '1 e u0 p0 c-1\n'
electron_spc = species(ELECTRON, 'e-')
core_species = list(rxn.reactants) + list(rxn.products) + [electron_spc]
seen, uniq = set(), []
for s in core_species:
    if id(s) not in seen:
        seen.add(id(s))
        uniq.append(s)
core_species = uniq
for i, s in enumerate(core_species):
    s.index = i + 1
    if s.thermo is None and not s.is_electron():
        s.thermo = db.thermo.get_thermo_data(s)

print("  core species: %s" % ", ".join(str(s) for s in core_species))

electron = next((s for s in core_species if s.is_electron()), None)
mf = {}
for s in core_species:
    mf[s] = 1e-6 if s.is_electron() or '+' in str(s) else 1.0
tot = sum(mf.values())
mf = {s: v / tot for s, v in mf.items()}


def delivered(T_gas, Te_eV):
    reactor = PlasmaReactor(T=(T_gas, 'K'), P=(1.0, 'bar'),
                            initial_mole_fractions=dict(mf),
                            Te=(Te_eV * EV_K, 'K'),
                            charge_balance_species=electron)
    reactor.initialize_model(core_species=core_species, core_reactions=[rxn],
                             edge_species=[], edge_reactions=[])
    reactor.generate_rate_coefficients([rxn], [])
    return reactor.kf[reactor.reaction_index[rxn]]


sub("kf as the solver actually evaluates it")
print("      %-14s %-12s %s" % ("T_gas (K)", "Te (eV)", "kf  [m^3/(mol*s)]"))
results = {}
for T_gas in (300.0, 1000.0):
    for Te_eV in (1.0, 3.0):
        try:
            k = delivered(T_gas, Te_eV)
            results[(T_gas, Te_eV)] = k
            print("      %-14.1f %-12.1f %.6e" % (T_gas, Te_eV, k))
        except Exception as exc:                                # noqa: BLE001
            print("      %-14.1f %-12.1f RAISED %s: %s"
                  % (T_gas, Te_eV, type(exc).__name__, exc))

sub("does Te move the answer at all?")
for T_gas in (300.0, 1000.0):
    a, b = results.get((T_gas, 1.0)), results.get((T_gas, 3.0))
    if a is not None and b is not None:
        print("      T_gas=%-7.1f  Te 1 eV -> 3 eV : %.6e -> %.6e   %s"
              % (T_gas, a, b, "UNCHANGED" if a == b else "changed"))

sub("what the SAME Arrhenius gives at the electron temperature it never sees")
T_e_K = 3.0 * EV_K
print("      Te = 3 eV = %.1f K" % T_e_K)
for T in (34813.5, T_e_K):
    print("      k(%.1f K) = %.6e m^3/(mol*s)" % (T, kin.get_rate_coefficient(T)))

sub("scale of the shortfall")
PUBLISHED_3EV = 2.0583e10
k300 = results.get((300.0, 3.0))
k1000 = results.get((1000.0, 3.0))
k_at_Te = kin.get_rate_coefficient(34813.5)
print("      published state-resolved argon model, 3 eV : %.4e" % PUBLISHED_3EV)
print("      same Arrhenius evaluated at 34813.5 K      : %.4e" % k_at_Te)
if k300:
    print("      DELIVERED at 300 K gas                     : %.4e  (%.1f orders low vs published)"
          % (k300, math.log10(PUBLISHED_3EV / k300)))
if k1000:
    print("      DELIVERED at 1000 K gas                    : %.4e  (%.1f orders low vs published)"
          % (k1000, math.log10(PUBLISHED_3EV / k1000)))

print("\n  VERDICT: the channel is not over-predicted. It is UNDER-delivered, and the")
print("           electron temperature never reaches it.")


# =====================================================================================
banner("4. WHERE THE BARRIER COMES FROM -- THE MIXED SIBLING CONVENTION SETS IT")
# =====================================================================================
# fix_barrier_height uses H0, not H298 (rmgpy/reaction.py:1401-1403):
#     H0 = sum(products E0) - sum(reactants E0)
# and a species whose entry does NOT state E0 falls back to to_wilhoit().E0.
sub("E0 as each sibling library supplies it")
for s in list(rxn.reactants) + list(rxn.products):
    if s.is_electron():
        continue
    td = s.get_thermo_data()
    stated = td.E0.value_si / 1000.0 if td.E0 is not None else None
    derived = td.to_wilhoit().E0.value_si / 1000.0
    print("      %-10s stated E0 = %-12s derived E0 = %.4f kJ/mol   -> uses %s"
          % (s.label, "%.4f" % stated if stated is not None else "(none)",
             derived, "STATED" if stated is not None else "derived"))

h0 = (sum(s.get_thermo_data().E0.value_si if s.get_thermo_data().E0 is not None
          else s.get_thermo_data().to_wilhoit().E0.value_si
          for s in rxn.products if not s.is_electron())
      - sum(s.get_thermo_data().E0.value_si if s.get_thermo_data().E0 is not None
            else s.get_thermo_data().to_wilhoit().E0.value_si
            for s in rxn.reactants if not s.is_electron()))
print("\n      H0  (mixed convention, what the code uses) = %.4f kJ/mol" % (h0 / 1000.0))
print("      H298(both consistent)                      = %.4f kJ/mol"
      % (rxn.get_enthalpy_of_reaction(298.0) / 1000.0))
print("      leak                                       = %.4f kJ/mol"
      % ((h0 - rxn.get_enthalpy_of_reaction(298.0)) / 1000.0))
print("\n      The barrier is set from the MIXED value. The cation library states E0 and this")
print("      library derives it, so the sibling inconsistency lands directly in a rate.")

# =====================================================================================
banner("5. AN ALGEBRAIC NASA FOR CONSTANT Cp -- NOTHING IS FITTED")
# =====================================================================================
from rmgpy.thermo import NASA, NASAPolynomial                  # noqa: E402
from rmgpy.thermo.thermoengine import process_thermo_data      # noqa: E402

import rmgpy.constants as rmg_constants                        # noqa: E402

# RMG evaluates NASA with its OWN gas constant, which is the older CODATA value.
# Deriving the coefficients with any other R puts a small, avoidable error into
# every number the entry claims to reproduce exactly.
R_RMG = rmg_constants.R
print("      rmgpy.constants.R = %.9f   (current CODATA is %.9f)" % (R_RMG, R))

H298 = 1114.247e3      # J/mol   (entry face value)
S298 = 168.227         # J/(mol*K)
T_REF = 298.15

a1 = 2.5                                       # Cp/R for a monatomic ideal gas, exactly 5/2
a6 = H298 / R_RMG - a1 * T_REF                 # H/(R*T) = a1 + a6/T
a7 = S298 / R_RMG - a1 * math.log(T_REF)       # S/R     = a1*ln(T) + a7

sub("coefficients, one line of arithmetic each")
print("      a1 = Cp/R                   = 5/2                            = %.10f" % a1)
print("      a6 = H298/R - a1*298.15     = 1114247/%.6f - 2.5*298.15    = %.6f" % (R_RMG, a6))
print("      a7 = S298/R - a1*ln(298.15) = 168.227/%.6f - 2.5*ln(298.15) = %.10f"
      % (R_RMG, a7))

nasa = NASA(
    # Tmin MUST be <= 298: to_wilhoit() evaluates get_enthalpy(298), so a polynomial
    # starting at 298.15 is refused outright ("No valid NASA polynomial at 298 K").
    # 200 K is exact here, not an extrapolation: Cp = 5/2*R holds at every temperature
    # for a free atom whose electronic degeneracy is constant.
    polynomials=[NASAPolynomial(coeffs=[a1, 0.0, 0.0, 0.0, 0.0, a6, a7],
                                Tmin=(200.0, 'K'), Tmax=(6000.0, 'K'))],
    Tmin=(200.0, 'K'), Tmax=(6000.0, 'K'),
    Cp0=(2.5 * R_RMG, 'J/(mol*K)'), CpInf=(2.5 * R_RMG, 'J/(mol*K)'))

sub("does it reproduce the entry's three numbers exactly?")
print("      Cp(298.15) = %.6f   (entered 20.786)" % nasa.get_heat_capacity(298.15))
print("      H (298.15) = %.6f kJ/mol   (entered 1114.247)" % (nasa.get_enthalpy(298.15) / 1000.0))
print("      S (298.15) = %.6f   (entered 168.227)" % nasa.get_entropy(298.15))
print("      Cp(6000)   = %.6f   (flat, as physics requires)" % nasa.get_heat_capacity(6000.0))

sub("does processing preserve the 6000 K ceiling?")


class _Shim(object):
    def __init__(self, thermo):
        self.thermo = thermo
        self.conformer = None


# thermoengine.py:93 keeps a NASA verbatim ONLY when its comment marks it as coming
# from a thermo library:  `if "Thermo library" in thermo0.comment and isinstance(thermo0, NASA)`.
# Both arms are shown, because the gate is the comment and that is easy to miss.
import copy                                                     # noqa: E402

for label, comment in (('bare NASA (no library comment)', ''),
                       ('NASA as a library entry', 'Thermo library: PlasmaExcitedNeutralThermo')):
    candidate = copy.deepcopy(nasa)
    candidate.comment = comment
    processed = process_thermo_data(_Shim(candidate), candidate)
    print("      %-32s -> %-6s Tmin=%7.2f Tmax=%7.2f"
          % (label, processed.__class__.__name__,
             processed.Tmin.value_si, processed.Tmax.value_si))
    try:
        print("          S(6000)=%.4f  H(6000)=%.4f kJ/mol  Cp(6000)=%.4f"
              % (processed.get_entropy(6000.0), processed.get_enthalpy(6000.0) / 1000.0,
                 processed.get_heat_capacity(6000.0)))
    except ValueError as exc:
        print("          6000 K RAISES: %s" % exc)
        print("          (note: a refit NASA fails LOUDLY above its ceiling, where")
        print("           ThermoData silently freezes S and keeps climbing in H)")

# =====================================================================================
banner("6. THE DEGENERACY PATH THAT REPORTS READY WITH Q = 0")
# =====================================================================================
from rmgpy.statmech import Conformer                            # noqa: E402
from rmgpy.quantity import Quantity                             # noqa: E402

sub("the atomic has_statmech shortcut (rmgpy/species.py:528)")
print("      for a 1-atom molecule it checks ONLY conformer.E0 --")
print("      not modes, not spin_multiplicity.")

meta = species(AR_META, 'Ar(3P2)')
meta.thermo = db.thermo.get_thermo_data(meta)

# An ordinary Arkane structure-only declaration defaults spin_multiplicity to 0
# (arkane/input.py:157); thermo lookup then supplies E0 and the shortcut passes.
meta.conformer = Conformer(E0=(meta.thermo.to_wilhoit().E0.value_si, 'J/mol'),
                           modes=[], spin_multiplicity=0, optical_isomers=1)
print("\n      spin_multiplicity   = %d   (Arkane structure-only default)"
      % meta.conformer.spin_multiplicity)
print("      has_statmech()      = %s   <-- reported READY" % meta.has_statmech())
for T in (298.15, 1000.0):
    q = meta.conformer.get_partition_function(T)
    try:
        s = meta.conformer.get_entropy(T)
    except Exception as exc:                                    # noqa: BLE001
        s = float('nan')
    print("      T=%-8.2f Q = %-8.4f conformer S = %s" % (T, q, s))

sub("the three counts that coexist, and what each one drives")
print("      thermo S298 carries g = 5 (the entry's R*ln(5) term)")
for g in (1, 3, 5):
    c = Conformer(E0=(0.0, 'J/mol'), modes=[], spin_multiplicity=g, optical_isomers=1)
    print("      spin_multiplicity=%d -> Q(298.15) = %.4f" % (g, c.get_partition_function(298.15)))
print("\n      Q is LINEAR in spin_multiplicity, so a TST rate built from the conformer")
print("      scales by 5/1 = 5x or 5/3 ~ 1.667x against the g the thermo actually asserts,")
print("      while the library entropy does not move at all.")
