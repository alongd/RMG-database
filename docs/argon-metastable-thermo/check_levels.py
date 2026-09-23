#!/usr/bin/env python
# encoding: utf-8
"""
Exact arithmetic behind the PlasmaExcitedNeutralThermo entry for metastable argon (I-221).

Every number this prints is either transcribed from a named table or produced here by an
identity written out in the entry's longDesc. Nothing is fitted. Run:

    python docs/argon-metastable-thermo/check_levels.py \
        > >(tee -a docs/argon-metastable-thermo/logs/check_levels.stdout.log) \
        2> >(tee -a docs/argon-metastable-thermo/logs/check_levels.stderr.log >&2)

Sources
    NIST ASD ver. 5.12 (Kramida, Ralchenko, Reader and the NIST ASD Team, 2024),
        doi:10.18434/T4W30F, Ar I levels, retrieved 2026-09-14 from
        https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=Ar+I&units=0&format=1
    NIST-JANAF Fourth Edition table Ar-001 "Argon (Ar)", Ar1(ref),
        https://janaf.nist.gov/tables/Ar-001.txt
    CODATA 2018 conversion factors, https://physics.nist.gov/cuu/Constants/
"""

from math import exp, log

# --- CODATA 2018 ------------------------------------------------------------------------
R = 8.314462618              # J/(mol*K), exact by the 2019 SI redefinition
HC_NA = 11.9626565957        # J/(mol*cm^-1)   -- h*c*N_A
EV = 96.48533212             # kJ/(mol*eV)     -- e*N_A
CM_PER_EV = 8065.543937      # cm^-1 per eV

T0 = 298.15

# --- NIST ASD, Ar I, 3s2.3p5.(2P*).4s levels, cm^-1, verbatim -----------------------------
# label           config / term / J                         E (cm^-1)   g   character
LEVELS = [
    ("Ar ground", "3s2.3p6           1S    J=0",                0.0000, 1, "ground"),
    ("1s5 (3P2)",  "3s2.3p5.(2P*<3/2>).4s  2[3/2]*  J=2",  93143.7600, 5, "METASTABLE"),
    ("1s4 (3P1)",  "3s2.3p5.(2P*<3/2>).4s  2[3/2]*  J=1",  93750.5978, 3, "resonant"),
    ("1s3 (3P0)",  "3s2.3p5.(2P*<1/2>).4s  2[1/2]*  J=0",  94553.6652, 1, "METASTABLE"),
    ("1s2 (1P1)",  "3s2.3p5.(2P*<1/2>).4s  2[1/2]*  J=1",  95399.8276, 3, "resonant"),
]

# JANAF Ar-001, transcribed
S298_AR = 154.845            # J/(mol*K)
CP_MONATOMIC = 2.5 * R       # J/(mol*K)


def banner(text):
    print("\n" + text)
    print("-" * len(text))


banner("1. Ar I 4s LEVELS, NIST ASD ver. 5.12 (transcribed) AND THEIR ENERGY EQUIVALENTS")
print("%-11s %-40s %12s %3s %10s %12s  %s"
      % ("label", "configuration / term / J", "E (cm^-1)", "g", "E (eV)", "E (kJ/mol)", "character"))
for label, conf, e_cm, g, kind in LEVELS:
    print("%-11s %-40s %12.4f %3d %10.5f %12.4f  %s"
          % (label, conf, e_cm, g, e_cm / CM_PER_EV, e_cm * HC_NA / 1000.0, kind))

banner("2. THE BRIEF'S LEVEL FIGURES, CHECKED")
for name, e_cm, claimed in (("3P2", 93143.7600, 11.548), ("3P0", 94553.6652, 11.723)):
    got = e_cm / CM_PER_EV
    print("  %s: ASD %12.4f cm^-1 -> %.5f eV; brief says %.3f eV; agree to %.2e eV"
          % (name, e_cm, got, claimed, abs(got - claimed)))

E_3P2 = 93143.7600
E_3P0 = 94553.6652
DE_CM = E_3P0 - E_3P2
DE_KJ = DE_CM * HC_NA / 1000.0
print("  dE(3P0 - 3P2) = %.4f cm^-1 = %.6f eV = %.4f kJ/mol   (brief: 0.175 eV, 16.88 kJ/mol)"
      % (DE_CM, DE_CM / CM_PER_EV, DE_KJ))
print("  RT at 298.15 K = %.6f kJ/mol   (brief: 2.479)" % (R * T0 / 1000.0))
print("  exp(-dE/RT)    = %.6e             (brief: 1.1e-3)" % exp(-DE_KJ * 1000.0 / (R * T0)))


def two_level(T):
    """Electronic partition function and its S, H, Cp for {3P2 (g=5, E=0), 3P0 (g=1, E=dE)}."""
    x = DE_KJ * 1000.0 / (R * T)
    b = exp(-x)
    Q = 5.0 + 1.0 * b
    mean_over_RT = (1.0 * b * x) / Q                      # <E>/(RT)
    mean_sq_over_RT2 = (1.0 * b * x * x) / Q              # <E^2>/(RT)^2
    S_over_R = log(Q) + mean_over_RT                      # S_el / R
    H_kJ = mean_over_RT * R * T / 1000.0                  # <E>, kJ/mol
    Cp_el = R * (mean_sq_over_RT2 - mean_over_RT ** 2)    # Schottky, J/(mol*K)
    return Q, S_over_R, H_kJ, Cp_el


banner("3. THE LUMPING QUESTION: degeneracy-weighted {3P2 + 3P0} vs 3P2 ALONE")
print("  The brief's route is R*ln(Q/Q0) only. The electronic entropy of a multi-level")
print("  manifold is S_el = R*ln(Q) + R*<E>/(RT); the second term is what the brief omits.")
print()
print("%8s %14s %16s %16s %16s %14s"
      % ("T (K)", "Q", "R ln(Q/5)", "R<E>/RT", "dS total", "Cp_el(lump)"))
for T in (100, 150, 200, 207.1, 250, 298.15, 400, 500, 1000, 2000, 3000, 4000, 5000, 6000):
    Q, S_over_R, _H, Cp_el = two_level(T)
    lnterm = R * log(Q / 5.0)
    meanterm = R * (S_over_R - log(Q))
    print("%8.2f %14.6f %16.6f %16.6f %16.6f %14.6f"
          % (T, Q, lnterm, meanterm, R * S_over_R - R * log(5.0), Cp_el))

Q298, S298_over_R, H298_lump, Cp_el298 = two_level(T0)
dS298 = R * S298_over_R - R * log(5.0)
print()
print("  At 298.15 K: brief's R*ln(5.0011/5) = %.6f J/(mol*K)" % (R * log(Q298 / 5.0)))
print("               TRUE dS               = %.6f J/(mol*K)  -> brief low by %.1fx"
      % (dS298, dS298 / (R * log(Q298 / 5.0))))
print("               dH298 (lump - 3P2)    = %.6f kJ/mol" % H298_lump)
Q6k, S6k, H6k, _ = two_level(6000.0)
print("  At 6000 K:   brief's R*ln(Q/5)     = %.6f J/(mol*K)  (brief said ~1.1)"
      % (R * log(Q6k / 5.0)))
print("               TRUE dS               = %.6f J/(mol*K)" % (R * S6k - R * log(5.0)))

banner("4. WHERE THE LUMPING DIFFERENCE CROSSES THE PRECISION WE QUOTE")
for thresh, unit in ((0.001, "J/(mol*K), the last digit of S298"),
                     (0.01, "J/(mol*K)"),
                     (0.1, "J/(mol*K)"),
                     (1.0, "J/(mol*K)")):
    lo, hi = 20.0, 20000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        Q, S_over_R, _H, _C = two_level(mid)
        if R * S_over_R - R * log(5.0) < thresh:
            lo = mid
        else:
            hi = mid
    print("  dS first exceeds %-7g %-34s at T = %8.1f K" % (thresh, unit, 0.5 * (lo + hi)))

banner("5. THE NUMBERS THAT GO INTO THE ENTRY (3P2 alone)")
h298 = E_3P2 * HC_NA / 1000.0
print("  H298 = E(1s5) * h*c*N_A")
print("       = %.4f cm^-1 * %.10f J/(mol*cm^-1) = %.6f kJ/mol -> %.3f kJ/mol"
      % (E_3P2, HC_NA, h298, h298))
print("  (dfH298 = dfH0 exactly: [H298-H0] is 5/2 RT = %.3f kJ/mol for BOTH Ar(1s5) and Ar," %
      (2.5 * R * T0 / 1000.0))
print("   a single level having no internal structure to contribute; JANAF Ar-001 T=0 row gives")
print("   -6.197 kJ/mol for the ground state, so the two cancel and E0 = H298.)")
print()
rln5 = R * log(5.0)
print("  S298 = S298(Ar, JANAF Ar-001) + R ln(g*/g0)")
print("       = %.3f + %.10f * ln(5/1) = %.3f + %.4f = %.6f -> %.3f J/(mol*K)"
      % (S298_AR, R, S298_AR, rln5, S298_AR + rln5, S298_AR + rln5))
print()
print("  Cp(T) = 5/2 R = %.10f -> %.3f J/(mol*K) at EVERY T (translation only; one level)"
      % (CP_MONATOMIC, CP_MONATOMIC))
print("  Cp0 = CpInf = %.4f J/(mol*K)" % CP_MONATOMIC)

banner("6. ALTERNATIVES, SO THE CHOICE CAN BE OVERRULED FROM ONE READ")
print("%-28s %12s %3s %14s %14s"
      % ("entry would be", "E (cm^-1)", "g", "H298 (kJ/mol)", "S298 (J/mol/K)"))
for label, _conf, e_cm, g, _kind in LEVELS[1:]:
    print("%-28s %12.4f %3d %14.3f %14.3f"
          % (label + " alone", e_cm, g, e_cm * HC_NA / 1000.0, S298_AR + R * log(g)))
print("%-28s %12s %3s %14.3f %14.3f"
      % ("{3P2 + 3P0} lumped @298.15", "-", "5.0011",
         E_3P2 * HC_NA / 1000.0 + H298_lump, S298_AR + R * S298_over_R))

banner("7. WHY 1P1 CANNOT BE WRITTEN AT ALL, AND WHY 3P1 IS NOT A RESERVOIR")
print("  Ar valence = 8 electrons. With p3 (6 in lone pairs) and no bonds, charge neutrality")
print("  forces u = 2: `Ar u2 p3 c0` is the ONLY neutral bond-free p3 adjacency list, and it")
print("  is a TRIPLET (multiplicity 3). The singlet 1s2 (1P1) therefore has no adjacency list")
print("  in RMG at all -- it is not an option this entry declines, it is unrepresentable.")
print()
print("  Radiative rates, NIST ASD ver. 5.12 (lines 104-108 nm, both from the ground state):")
print("    1s2 (1P1) -> ground  104.8220 nm  A = 5.32e+08 s^-1  -> tau = %.2f ns"
      % (1e9 / 5.32e8))
print("    1s4 (3P1) -> ground  106.6660 nm  A = 1.320e+08 s^-1 -> tau = %.2f ns"
      % (1e9 / 1.320e8))
print("  Against the metastables:")
print("    1s5 (3P2)  tau = 38 (+8/-5) s   measured, Katori & Shimizu, PRL 70 (1993) 3545")
print("    1s5 (3P2)  tau = 55.9 s         computed, Small-Warren & Chiu, PRA 11 (1975) 1777")
print("    1s3 (3P0)  tau = 44.9 s         computed, Small-Warren & Chiu, PRA 11 (1975) 1777")
print("  Ratio 3P2 : 3P1 lifetime = %.2e -- nine to ten orders of magnitude." % (38.0 / (1.0 / 1.320e8)))
