"""Recompute the ruled Ar2+ thermochemistry from primary-read constants.

This is intentionally self-contained: the constants and partition-function model are
versioned here with the database entry. The selected model is Signorell & Merkt (1998),
with r_e = 2.32 A, sigma = 2, and electronic degeneracy 2.

The physical constants below follow the CODATA 2018 recommended values: h =
6.62607015e-34 J s, kB = 1.380649e-23 J/K, c = 2.99792458e10 cm/s (the exact
SI value 299792458 m/s converted to cm/s), and the atomic mass constant amu =
m_u = 1.66053906660e-27 kg. R = 8.31446261815324 J/(mol K) is the CODATA
2018 recommended molar gas constant (the implementation retains 8.314462618).
N_A = 6.02214076e23 mol^-1 is the CODATA 2018 recommended Avogadro constant.
"""
import numpy as np


R = 8.314462618
h = 6.62607015e-34
kB = 1.380649e-23
c = 2.99792458e10
amu = 1.66053906660e-27
N_A = 6.02214076e23
T0 = 298.15


def qtrans_entropy(T, mass, pressure=1e5):
    return R * (np.log((2 * np.pi * mass * kB * T / h**2)**1.5 * kB * T / pressure) + 2.5)


def rotational_partition(T, mass, bond_length, sigma):
    reduced_mass = mass / 4
    moment = reduced_mass * (bond_length * 1e-10)**2
    theta = h**2 / (8 * np.pi**2 * moment * kB)
    return T / (sigma * theta) * (1 + theta / (3 * T) + theta**2 / (15 * T**2))


# SWM97 (JCP 107 (1997) 10819-10822), abstract/Table I p. 10821, gives the
# older Morse-fit D0 = 10601.2 cm^-1 and the low-v omega_e constants.  SM98
# (JCP 109 (1998) 9762-9771), abstract/p. 9766, refines D0 to 10603.7 cm^-1;
# the former is used only as this Morse fallback cutoff.
def morse_levels(omega=307.0, anharmonicity=2.05, dissociation=10601.2):
    v = np.arange(0, 200)
    levels = omega * (v + 0.5) - anharmonicity * (v + 0.5)**2
    levels -= levels[0]
    return levels[(levels < dissociation) & (np.r_[1, np.diff(levels)] > 0)]


# Signorell & Merkt (SM98), J. Chem. Phys. 109 (1998) 9762-9771, Table I p. 9765.
# These are the calculated nu values for v=3, 5-10, and 12-52.
CALCULATED_LINE_POSITIONS = {
    3: 117488.3, 5: 118066.0, 6: 118348.5, 7: 118626.8, 8: 118900.9,
    9: 119170.9, 10: 119436.7, 12: 119955.9, 13: 120209.2, 14: 120458.4,
    15: 120703.3, 16: 120944.1, 17: 121180.6, 18: 121412.9, 19: 121640.9,
    20: 121864.6, 21: 122084.0, 22: 122299.1, 23: 122509.9, 24: 122716.3,
    25: 122918.4, 26: 123116.0, 27: 123309.2, 28: 123498.0, 29: 123682.3,
    30: 123862.1, 31: 124037.4, 32: 124208.2, 33: 124374.4, 34: 124536.0,
    35: 124693.1, 36: 124845.5, 37: 124993.2, 38: 125136.3, 39: 125274.6,
    40: 125408.2, 41: 125536.9, 42: 125660.8, 43: 125779.7, 44: 125893.5,
    45: 126002.2, 46: 126105.5, 47: 126203.3, 48: 126295.3, 49: 126381.2,
    50: 126460.6, 51: 126533.0, 52: 126598.3,
}


def signorell_merkt_levels():
    # SM98 gives IE(Ar2) = 116591.1 cm^-1 in the abstract/Eq. (5), p. 9766.
    # Its delta = 2.0 cm^-1 level-origin subtraction is defined on p. 9766.
    levels = {v: line - (116591.1 - 2.0)
              for v, line in CALCULATED_LINE_POSITIONS.items()}
    # v=0,1,2,4 are the SWM97 low-v Morse substitutions; v=11 is not in Table I
    # and is explicitly interpolated as the arithmetic mean of v=10 and v=12.
    morse = morse_levels()
    for v in (0, 1, 2, 4):
        levels[v] = morse[v]
    levels[11] = 0.5 * (levels[10] + levels[12])
    # The hybrid intentionally stops at v=52; it does not retain Morse v=53-55.
    return np.array([levels[v] for v in sorted(levels)])


def thermo(T, levels, bond_length=2.32, sigma=2, electronic_degeneracy=2):
    # NIST/CIAAW standard atomic weight Ar = 39.948 u; this model uses
    # 2 * 39.948 u = 79.896 u, i.e. natural-abundance Ar, with no electron
    # subtraction.  It is therefore not the Ar-40 mass (and not an Ar-40
    # dimer minus one electron).
    mass = 79.896 * amu
    x = levels * h * c / (kB * T)
    weights = np.exp(-x)
    mean_x = (x * weights).sum() / weights.sum()
    mean_x2 = (x * x * weights).sum() / weights.sum()
    vibrational_energy = R * T * mean_x
    vibrational_entropy = vibrational_energy / T + R * np.log(weights.sum())
    vibrational_heat_capacity = R * (mean_x2 - mean_x**2)

    rotor = rotational_partition(T, mass, bond_length, sigma)
    delta = 1e-3 * T
    log_rotor = lambda value: np.log(rotational_partition(value, mass, bond_length, sigma))
    first = (log_rotor(T + delta) - log_rotor(T - delta)) / (2 * delta)
    second = (log_rotor(T + delta) - 2 * log_rotor(T) + log_rotor(T - delta)) / delta**2
    rotational_energy = R * T**2 * first
    rotational_entropy = rotational_energy / T + R * np.log(rotor)
    rotational_heat_capacity = R * (2 * T * first + T**2 * second)

    entropy = (qtrans_entropy(T, mass) + rotational_entropy + vibrational_entropy
               + R * np.log(electronic_degeneracy))
    heat_capacity = 2.5 * R + rotational_heat_capacity + vibrational_heat_capacity
    enthalpy_increment = (2.5 * R * T + rotational_energy + vibrational_energy) / 1000
    return enthalpy_increment, entropy, heat_capacity


if __name__ == "__main__":
    levels = signorell_merkt_levels()
    print("MODEL r_e=2.32 A sigma=2 g_el=2; Signorell & Merkt primary-read levels")
    for temperature in (T0, 1000.0, 1500.0):
        h_increment, entropy, heat_capacity = thermo(temperature, levels)
        print(f"T={temperature:.2f} H-H0={h_increment:.9f} kJ/mol "
              f"S={entropy:.9f} J/(mol*K) Cp={heat_capacity:.9f} J/(mol*K)")

    # 0.01196265656387 kJ mol^-1 per cm^-1 is the rounded display of the value
    # derived from the CODATA
    # constants: N_A*h*c/1000, because c is in cm/s and the wavenumber is cm^-1.
    cm_to_kj_per_mol = N_A * h * c / 1000.0
    e0 = 1520.573 - 10603.7 * cm_to_kj_per_mol
    h298 = e0 + thermo(T0, levels)[0] - 2 * 2.5 * R * T0 / 1000
    print(f"DERIVED_E0={e0:.9f} kJ/mol")
    print(f"DERIVED_H298={h298:.9f} kJ/mol")
    print(f"DERIVED_S298={thermo(T0, levels)[1]:.9f} J/(mol*K)")
    print("RULED_H298=1391.112000000 kJ/mol")
    print(f"ROUNDING={1391.112 - h298:+.9f} kJ/mol "
          f"({(1391.112 - h298) * 1000:+.6f} J/mol)")
