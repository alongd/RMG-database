# I-221 — Metastable argon thermochemistry

Branch `i221-argon-metastable-thermo`, worktree
`/home/alon/Code/RMG-database-i221-argon-metastable-thermo`, cut from `plasma` at `04846619b`.
Engine `/home/alon/Code/RMG-Py-plasma` at `311818121`, conda env `rmg_env`. Every run below is
captured in `logs/` with both streams.

---

## 1. What was added

One new thermo library and one entry in it.

| | |
|---|---|
| **Library** | `input/thermo/libraries/PlasmaExcitedNeutralThermo.py` |
| **Scope** | Gas-phase thermochemistry of electronically excited, electrically **neutral** species of plasma interest, each entry pinned to one named spectroscopic level |
| **Entry** | `Ar(3P2)` — `multiplicity 3 / 1 Ar u2 p3 c0` |
| **H298 / E0** | 1114.247 kJ/mol (both; see §4) |
| **S298** | 168.227 J/(mol·K) |
| **Cp(T)** | 20.786 J/(mol·K) = 5/2·R, at every tabulated T |
| **Range** | 298.15 – 6000 K |

Plus `test/test_argon_metastable_thermo.py` (23 tests) and this directory.

Nothing else. Three commits on `i221-argon-metastable-thermo` above `04846619b`, split the way
the work divides — the library entry, the test suite, the report and probes. Every path they
touch is inside `input/thermo/libraries/`, `test/` and `docs/`; **no pre-existing tracked file is
modified at all**, only new ones added. `input/kinetics/` was not touched. Nothing pushed, nothing
merged, no PR.

### Why a new library rather than an existing home

Considered and rejected:

- **`PlasmaCationThermo`** — the obvious neighbour and the wrong one. Its name says cations, its
  charter says "free monatomic CATIONS of plasma interest", and half its header is the electron
  reference-state determination, which exists *because* its species carry charge. A neutral
  placed there would sit under a lying name surrounded by a discussion that does not apply to it.
- **`primaryThermoLibrary`** — already carries an electronically excited species (`O2(S)`,
  index 3), so precedent exists. Rejected because it is the database's general-purpose combustion
  default: an entry there is loaded by every RMG job whether or not it is a plasma, and a
  metastable quietly appearing in a combustion mechanism is precisely the surprise this campaign
  spends effort avoiding. A separately-named plasma library is opted into.

The new library's scope is deliberately *neutral excited species*, not *argon*: excited ions
belong in `PlasmaCationThermo`, ground-state neutrals in the ordinary libraries. That is the
partition that makes the three library names each true.

---

## 2. Level data, from the primary source

NIST Atomic Spectra Database ver. 5.12 (Kramida, Ralchenko, Reader and the NIST ASD Team, 2024),
doi:10.18434/T4W30F. Table **"Ar I" energy levels**, units cm⁻¹, referred to `3s²3p⁶ ¹S₀` at
0.0000 cm⁻¹. Retrieved 2026-09-14 from
`https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=Ar+I&units=0&format=1`.
Same retrieval gives the ionisation limit, Ar II (3p⁵ ²P°₃/₂), at 127109.842 ± 0.004 cm⁻¹.

| Paschen | LS | configuration / term / J | E (cm⁻¹) | g | E (eV) | character |
|---|---|---|---|---|---|---|
| — | ¹S₀ | `3s2.3p6  1S  J=0` | 0.0000 | 1 | 0 | ground |
| **1s5** | **³P₂** | `3s2.3p5.(2P*<3/2>).4s  2[3/2]*  J=2` | **93143.7600** | **5** | **11.54835** | **metastable** |
| 1s4 | ³P₁ | `3s2.3p5.(2P*<3/2>).4s  2[3/2]*  J=1` | 93750.5978 | 3 | 11.62359 | resonant |
| 1s3 | ³P₀ | `3s2.3p5.(2P*<1/2>).4s  2[1/2]*  J=0` | 94553.6652 | 1 | 11.72316 | metastable |
| 1s2 | ¹P₁ | `3s2.3p5.(2P*<1/2>).4s  2[1/2]*  J=1` | 95399.8276 | 3 | 11.82807 | resonant |

Ground-state reference values: NIST-JANAF Fourth Edition, table **Ar-001** "Argon (Ar)",
`https://janaf.nist.gov/tables/Ar-001.txt` — S(298.15) = 154.845 J/(mol·K), Cp = 20.786
J/(mol·K) at every tabulated T, [H(298.15)−H(0)] = 6.197 kJ/mol, ΔfH = 0 throughout.

Radiative data, same ASD version, lines 104–108 nm: 1s2 → ground at 104.8220 nm,
A = 5.32×10⁸ s⁻¹; 1s4 → ground at 106.6660 nm, A = 1.320×10⁸ s⁻¹.

---

## 3. The brief's arithmetic, checked

**Level energies: CONFIRMED, to every digit quoted.** The brief's 11.548 eV (g = 5) and
11.723 eV (g = 1) are 11.54835 and 11.72316 against ASD. ΔE = 1409.9052 cm⁻¹ = 0.174806 eV =
**16.8662 kJ/mol** (the brief's 16.88 came from the rounded 0.175 eV). RT = 2.478957 kJ/mol at
298.15 K; exp(−ΔE/RT) = 1.1096×10⁻³. All as claimed.

**The entropy arithmetic: REFUTED as incomplete.** The brief computes the lumping difference as
`R·ln(Q/Q₀)`. That is only the first of two terms. The electronic entropy of a manifold is

    S_el = R·ln Q + R·⟨E⟩/(RT)

and here the second term *dominates*, because the second level is high and thinly populated — the
regime in which most of the entropy effect is energetic rather than combinatorial. Measured
(`check_levels.py`, `logs/check_levels.stdout.log`):

| T (K) | R·ln(Q/5) — the brief's route | R·⟨E⟩/RT — omitted | **true ΔS** |
|---|---|---|---|
| 298.15 | 0.001845 | 0.012551 | **0.014396** |
| 1000 | 0.215889 | 0.432302 | 0.648191 |
| 6000 | 1.108562 | 0.350882 | **1.459444** |

So the brief is low by **7.8×** at the reference temperature and by 32 % at 6000 K (where it
quoted "roughly 1.1"; the true figure is 1.46).

**Where it crosses the precision quoted.** `S298` is written to 0.001 J/(mol·K) in this database.
The lumping difference falls *below* one last digit only under **207.1 K**. It crosses 0.01 at
281.0 K, 0.1 at 449.1 K and 1.0 at 1560.5 K.

**Therefore the brief's conclusion does not survive as stated.** "At the reference temperature the
lumping choice changes nothing measurable" is true physically — 0.014 J/(mol·K) on 168 is 86 ppm —
and false as bookkeeping: at 298.15 K it is fourteen last-digits of the number actually written in
the file, not the ~2 the one-term arithmetic implied. The question that "looks like the hard part
of this ticket" is *not* numerically moot at 298.15 K. It is moot below about 207 K.

Two further consequences of lumping that the one-term route cannot see at all: H298 would shift by
+0.0037 kJ/mol, and the lumped species would carry a Schottky Cp rising to 0.854 J/(mol·K) near
1000 K instead of a flat 5/2·R — i.e. the entry would stop being exactly monatomic.

---

## 4. The decision: this entry is the 1s5 (³P₂) level, alone

Stated in the label, the `shortDesc`, and the `longDesc`. Two questions were kept apart, as the
brief required.

### Question 1 — which levels belong in the entry at all

**1s2 (¹P₁) is not declined; it is unrepresentable.** Argon has 8 valence electrons. With `p3`
(six paired in lone pairs), no bonds and no charge, the remaining two *must* be unpaired.
`Ar u2 p3 c0` is the only neutral bond-free p3 adjacency list and it is necessarily a **triplet**.
Measured: RMG's own `ConsistencyChecker.check_partial_charge` raises `InvalidAdjacencyListError`
for `u0`, `u1`, `u3`, `u4` at `p3 c0`. A singlet 4s level has no adjacency list in RMG at all, so
the choice is among the three triplets only.

**1s4 (³P₁) is representable by the same adjacency list and is excluded on physics.** It is a
*resonant* level: J = 1 → J = 0 is electric-dipole allowed.

| level | lifetime | source |
|---|---|---|
| 1s2 (¹P₁) | 1.9 ns | A = 5.32×10⁸ s⁻¹, NIST ASD 5.12 |
| 1s4 (³P₁) | 7.6 ns | A = 1.320×10⁸ s⁻¹, NIST ASD 5.12 |
| 1s5 (³P₂) | **38 (+8/−5) s**, measured | Katori & Shimizu, *Phys. Rev. Lett.* **70** (1993) 3545, doi:10.1103/PhysRevLett.70.3545 |
| 1s5 (³P₂) | 55.9 s, computed | Small-Warren & Chow Chiu, *Phys. Rev. A* **11** (1975) 1777, doi:10.1103/PhysRevA.11.1777 |
| 1s3 (³P₀) | 44.9 s, computed | same |

Nine to ten orders of magnitude. 1s5 and 1s3 are reservoirs on any chemical timescale; 1s4 and
1s2 are radiative transients, not reservoirs.

**The caveat that cuts the other way, recorded in the entry:** in a real discharge the 106.7 and
104.8 nm photons are *radiation-trapped*, and the effective lifetimes of 1s4/1s2 rise by orders of
magnitude at high argon density. Trapping is a property of the vessel — pressure, geometry, line
shape — not of the atom, so it can never be a property of a thermochemistry entry. If later work
needs a trapped resonant level it needs its own species and its own justification, and it cannot
reuse this adjacency list, because this one is now taken.

### Question 2 — how the admitted levels are weighted

**1s5 alone, not the {1s5 + 1s3} degeneracy-weighted lump.** Note carefully that the magnitudes
in §3 argue *mildly for* lumping being harmless, so the reason has to be the real one:

> A degeneracy-weighted lump asserts that the two metastables are Boltzmann-distributed with
> respect to one another **at the gas temperature**. In a low-pressure discharge they are not.
> Their populations are set by electron-impact excitation and by their own very different
> quenching; the 1s5/1s3 ratio is an *output* of the plasma kinetics, not a function of T.
> Writing the lump would quietly assert the equilibrium the model exists to test — a fitted
> number under a charter that forbids fitted numbers.

A single named level asserts nothing: a transcribed energy, an exact degeneracy, an exact
translational Cp. The physical case for 1s5 in particular, had the two been equally defensible:
it is lower, it carries g = 5 against g = 1, and it holds ~5/6 of the metastable population even
under the equilibrium assumption being declined.

### Alternatives side by side, so this can be overruled from one read

| entry would be | E (cm⁻¹) | g | H298 (kJ/mol) | S298 (J/mol·K) |
|---|---|---|---|---|
| **1s5 (³P₂) alone** | **93143.7600** | **5** | **1114.247** | **168.227** |
| 1s4 (³P₁) alone | 93750.5978 | 3 | 1121.506 | 163.979 |
| 1s3 (³P₀) alone | 94553.6652 | 1 | 1131.113 | 154.845 |
| 1s2 (¹P₁) alone | 95399.8276 | 3 | 1141.235 | 163.979 |
| {1s5+1s3} lumped @298.15 K | — | 5.0011 | 1114.251 | 168.241 |

---

## 5. The three numbers, one identity each

- **Cp(T) = 5/2·R = 20.786 J/(mol·K), exact at every T.** A free monatomic species pinned to *one*
  electronic level has translation and nothing else — no rotation, no vibration, and no internal
  electronic structure to contribute a Schottky term. Contrast `PlasmaCationThermo`'s `[Arp]`,
  whose Cp peaks at 22.773 J/(mol·K) near 1000 K precisely because Ar⁺ is a ²P term with a
  ²P(1/2) partner 1431.6 cm⁻¹ up.
- **S298 = S298(Ar, JANAF Ar-001) + R·ln(g\*/g₀) = 154.845 + 8.314462618·ln 5 = 154.845 + 13.382 =
  168.227 J/(mol·K).** The degeneracy term is exact, not an approximation: translation, mass and
  standard state are identical between Ar(³P₂) and Ar, so the entire difference is electronic, and
  one level contributes only R·ln g with g = 2J+1 = 5.
- **H298 = E(1s5)·h·c·N_A = 93143.7600 cm⁻¹ × 11.9626565957 J/(mol·cm⁻¹) = 1114.2468 → 1114.247
  kJ/mol.**
- **E0 carries the same number, by identity.** ΔfH(298.15) = ΔfH(0) + [H298−H0]\_Ar(³P₂) −
  [H298−H0]\_Ar, with ΔfH(0) = the level energy (ground-state argon's ΔfH(0) being zero) and both
  bracketed increments equal to 5/2·R·T = 6.197 kJ/mol — Ar(³P₂) because a single level has no
  internal structure, Ar because JANAF Ar-001's T = 0 row gives exactly −6.197. They cancel. For
  Ar⁺ they do *not* (6.206 vs 6.197), which is why that entry's H298 and E0 differ by 0.008
  kJ/mol and this one's do not. That contrast is pinned by a test.

**Ground-state source, named by file and entry:** `input/thermo/libraries/primaryThermoLibrary.py`,
entry index 15, label `Ar` — a `NASA` with `coeffs=[2.5,0,0,0,0,-745.375,4.37967]` on both
intervals. Measured, it evaluates to S(298.15) = 154.8459 J/(mol·K) and Cp = 20.786, agreeing with
JANAF Ar-001 to 0.001 J/(mol·K). (See §8 for the one that a *running mechanism* actually gets,
which is neither of those.)

**Form emitted: `ThermoData`, not `NASA`.** `ThermoData` states Cp on a grid plus H298/S298 at the
reference temperature, which is exactly the shape of what is known: three transcribed-or-derived
constants and a constant Cp. Emitting a NASA polynomial would mean *choosing coefficients* — i.e.
fitting — for a function that has a closed form, and this file's charter forbids that even where
the fit would be exact. Anything downstream that wants a polynomial can convert, and the
conversion is then visibly downstream of the data. It also matches `PlasmaCationThermo`.

**Where this recipe breaks if reused carelessly** (written into the `longDesc`): (1) any
polyatomic — the borrowed Cp stops being exact the moment there are vibrations, which is why
`O2(S)` genuinely approximates and this does not; (2) any structure that answers to a whole term
or manifold rather than one J — the flat Cp is a consequence of "one level", not of "monatomic";
(3) any charged species — then the electron reference-state convention becomes load-bearing and
`PlasmaCationThermo`'s reconciliation must be done. None of the three applies here.

---

## 6. Loading and perception — measured, not asserted

`logs/load_probe_baseline.stdout.log` (before the library) and `logs/load_probe_after.stdout.log`.

**Baseline, before this ticket.** The species perceives, and then has no thermochemistry:

```
  metastable    1 Ar u2 p3 c0            -> atomtype Ar0e    u2 p3 c+0  multiplicity 3  net charge +0
  Ar* metastable  RAISED AtomTypeError: Unable to determine atom type for atom Ar, which has
                  2 single bonds, ..., 3 lone pairs, and +0 charge.
```

The crash comes from `estimate_radical_thermo_via_hbi`: group additivity saturates the two
radicals with hydrogens, producing an `ArH2` that has no atom type. **This corrects an expectation
in the brief.** The named failure mode — "a library that parses but is never matched" — could not
have produced a silently wrong number here, because without the library the species raises rather
than being estimated. The risk was the opposite one: a *loud* wall, not a quiet fabrication. With
every library unloaded, the estimator refuses identically (probe §5), which is pinned as a test.

**After.** The entry is found and is the source:

```
  79 library files; PlasmaExcitedNeutralThermo is PRESENT
  79 libraries loaded
  PlasmaExcitedNeutralThermo entries: ['Ar(3P2)']

  Ar* metastable  H298 =     1114.250 kJ/mol   S298 =    168.237 J/(mol*K)   Cp(298) =   20.786
                  Cp(1000) =   20.786   Cp(6000) =   20.786
                  source: Thermo library: PlasmaExcitedNeutralThermo
```

Atom type `Ar0e`; isomorphic to neither ground-state Ar nor Ar⁺; Cp flat across the range; the
comment names this library and no estimator.

---

## 7. Checks run

| suite | command | result |
|---|---|---|
| RMG-Py `test/database/databaseTest.py`, `database.directory` pinned to this worktree's `input` | `pytest databaseTest.py -q` | **6 passed** in 293.0 s (`logs/databaseTest_after.stdout.log`) |
| This repo's `test/`, **baseline** with the two new files moved aside | `pytest test/ -q` | **4 failed, 214 passed** (`logs/pytest_repo_suite_baseline.stdout.log`) |
| This repo's `test/`, **after** | `pytest test/ -q` | **4 failed, 237 passed** (`logs/pytest_repo_suite.stdout.log`) |
| The new suite alone | `pytest test/test_argon_metastable_thermo.py -q` | **23 passed** (`logs/pytest_new.stdout.log`) |

`databaseTest.py`'s six tests each run many sub-assertions under `pytest_check`, so "6 passed"
means every thermo-group, kinetics-family, solvation, statmech, transport and metal check passed.

**The 4 failures are pre-existing and unrelated**, identical before and after — engine-drift
tripwires that fire because RMG-Py moved under them:

- `test_argon_cation_buildtime.py::test_the_dication_builds_and_raises_the_loud_databaseerror`
- `test_argon_cation_buildtime.py::test_the_dimer_cation_builds_and_raises_the_loud_databaseerror`
- `test_argon_cation_thermo.py::test_argon_atom_type_now_declares_a_charge_envelope_but_still_parses_any_charge`
- `test_plasma_radiative_recombination.py::test_three_body_recombination_still_cannot_be_stored_at_all`

The first three are the i222 argon atom-type work (`Ar0`/`Ar0s`/`Ar0e`/`Ar+`/`Ar++` and the charge
envelope) having landed in the engine; the fourth is i178 having given `TwoTemperaturePlasma` an
`electrons` field, which is exactly what that tripwire says should make it fail. All four are
someone else's tickets. **Not touched here** — fixing a tripwire that fired correctly is the
failure mode the campaign's own doctrine warns against.

---

## 8. What a reader of the deck would still get wrong

**No deck changed. The species now *can* exist; it appears nowhere.** The simulation input files
in this campaign declare argon as ground state plus cation only. This commit does not change that
and is not meant to. Nobody should read it as having changed a simulation.

Four more things, all disclosed in the `longDesc` and pinned by tests:

1. **No kinetics accompanies this.** Metastable argon is produced by electron-impact excitation
   and destroyed by stepwise ionisation, two- and three-body quenching, and wall loss. **None of
   those has an entry anywhere in this database**, and none was added. A mechanism containing this
   species today would hold an inert, unreachable island. `input/kinetics/libraries/PlasmaAir`
   advertises "metastable quenching" in its own `longDesc` and its dictionary carries only `Ar`
   and `Arp` — a reader checking that file first will be misled, so it is named explicitly.
   *(Gate: writing any of that kinetics needs a ruling this work does not have. Report line, not
   an edit.)*

2. **The ground-state argon a mechanism resolves to is not the one this entry is anchored on.**
   Its own section: §9.

3. **RMG's `ThermoData.H298`/`S298` fields are referenced to 298 K, not 298.15 K**
   (`rmgpy/thermo/thermodata.pyx`, properties `H298`/`S298` and the `assert Tdata[0] >= 298`
   corrections). Every JANAF-sourced entry in this database — these and `PlasmaCationThermo`'s —
   writes the 298.15 K value into that field. So `get_entropy(298.15)` returns the written value
   plus Cp·ln(298.15/298) = +0.0105 J/(mol·K), which is why this entry reads 168.227 in the file
   and 168.2375 through the API. Database-wide, not specific to argon; it cancels exactly in any
   difference between species with the same Cp. Deliberately *not* corrected for: writing 168.216
   to make the API return 168.227 would break the identity the entry is built on and would differ
   from every sibling entry.

4. **`Ar0e` in a *group* adjacency list does not mean "metastable".** Atom-type perception ignores
   `u` entirely, so `1 Ar0e ux p3 c0` matches u1 argon as readily as the u2 metastable. A group
   that means this species must write `u2` explicitly. RMG-Py's `atomtype.py` says so at length;
   repeated in the entry because a kinetics author reading it is exactly the person who will get
   it wrong. Also: the SMILES round trip is unsafe for monatomic species in this database
   (documented for `[Arp]`/`[Hep]`/`[Nep]`), so the adjacency list is the only interchange form.

---

## 9. Finding — an "anchored" entry is only as good as the ground state the runtime resolves, and load order decides that

This is a referral, not a change. **It was not fixed in this branch**, by instruction.

`S298` here is constructed as *ground state plus R·ln g*. That construction silently assumes the
runtime resolves the same ground state the entry was anchored to. It does not.

**Fifteen loaded libraries carry `Ar u0 p4 c0`**, and they split into two camps 0.113 J/(mol·K)
apart (`logs/precedence_probe.stdout.log`):

| load order | library | S298 via API | vs JANAF 154.845 |
|---|---|---|---|
| **9** | **`BurkeH2O2`** | **154.7348** | **−0.1102** ← wins |
| 14 | `JetSurF2.0` | 154.7323 | −0.1127 |
| 22 | `Narayanaswamy` | 154.8459 | +0.0009 |
| 25 | `SulfurGlarborgMarshall` | 154.8459 | +0.0009 |
| 28 | `2-BTP` | 154.7323 | −0.1127 |
| **37** | **`primaryThermoLibrary`** | **154.8459** | **+0.0009** ← the brief's reference state |
| 41 | `Chernov` | 154.7323 | −0.1127 |
| 43 | `FFCM1(-)` | 154.8459 | +0.0009 |
| 44 | `Fluorine` | 154.7323 | −0.1127 |
| 49 | `USC-Mech-ii` | 154.7323 | −0.1127 |
| 50 | `GRI-Mech3.0` | 154.7323 | −0.1127 |
| 51 | `Klippenstein_Glarborg2016` | 154.8459 | +0.0009 |
| 58 | `CurranPentane` | 154.8459 | +0.0009 |
| 65 | `JetSurF1.0` | 154.7323 | −0.1127 |
| 72 | `NOx2018` | 154.8462 | +0.0012 |

**What decides which one wins.** `get_thermo_data_from_libraries` walks `self.library_order` and
**returns on the first match** (`rmgpy/data/thermo.py:1923-1927`). And `library_order` is built in
`load_libraries` (`thermo.py:944-954`): when `libraries is None` — the load-everything path — it
is **`os.walk` order**, i.e. raw filesystem order. Measured: `db.library_order == os.walk order`
is `True`, `== sorted(...)` is `False`. So on that path the winner is not the best source, not the
most specific library, and not even alphabetical — it is whatever the directory happened to hand
back. That path is what `test/database/databaseTest.py` uses, what every probe in this directory
uses, and what any script calling `load_libraries(path)` uses.

In a real RMG run, `library_order` is the deck's declared `thermoLibraries` list instead, so
precedence *is* curated there — by whoever wrote the deck, against no check that the ground state
it selects matches the one an excited-state entry was built on.

**The consequence here.** `BurkeH2O2` wins at position 9 with a 4-figure combustion value
(36.98 cal/(mol·K)), 0.110 J/(mol·K) below JANAF. End to end
(`logs/roundtrip_probe.stdout.log`):

```
dH298(Ar -> Ar(3P2)) = 1114.2470 kJ/mol      against 1114.2468 exact   (agrees)
dS298(Ar -> Ar(3P2)) =   13.5027 J/(mol*K)   against   13.3816 exact   (+0.1211)
```

The enthalpy of excitation is right to 0.0002 kJ/mol; the entropy is 0.121 J/(mol·K) high, worth
−0.036 kJ/mol in ΔG at 298.15 K. Had one of the seven JANAF-agreeing libraries won instead, it
would have been −0.001. The number is small; the *mechanism* is not, because nothing about it is
specific to argon or to this entry — every "plus R·ln g" or "plus an absorption energy" entry in
this database rests on the same unchecked assumption, `O2(S)` in `primaryThermoLibrary` included.

**Why this entry is nonetheless not shadowed itself.** Exactly one library carries
`Ar u2 p3 c0` — this one, at load position 21. That is *uniqueness*, not precedence. If a second
library ever carries the metastable, the same coin-flip decides which value a mechanism gets, and
nothing will warn.

**Why it was not fixed here.** Anchoring on `BurkeH2O2` would make the *difference* exact and this
entry's own *absolute* S298 wrong by the same 0.110 — the sourced table has to win inside the
entry. The real repair is upstream: either `BurkeH2O2` and the seven other low carriers get
re-anchored, or thermo library precedence stops being a filesystem accident. Both belong to
whoever owns library precedence, not to this ticket.

This also corrects the brief, which named `primaryThermoLibrary.py:353-372` as "your reference
state". It is the right *source* — and it is not what the lookup returns.

---

## 10. Where the brief was wrong, collected

1. **The lumping entropy arithmetic was incomplete** (§3). `R·ln(Q/Q₀)` is the first term of a
   two-term expression; `R·⟨E⟩/(RT)` was omitted, and it is 7.8× larger at 298.15 K. The correct
   differences are 0.0144 J/(mol·K) at 298.15 K and 1.459 at 6000 K, against the brief's 0.002 and
   ~1.1. The conclusion drawn from it — that the lumping question is numerically moot at the
   reference temperature — **does not hold** at the precision the file quotes; it holds only below
   ~207 K. The owner reproduced the correction independently to every digit
   (0.001845 + 0.012549 = 0.014394; 1.108554 + 0.350888 = 1.459442; crossing at 207 K) and
   confirmed it.

   Worth stating without softening, because the verifier only works if its results are recorded
   plainly: this is the **tenth** time a brief on this campaign has been wrong and the worker has
   caught it, and the **first** where the error was the brief author's own physics rather than an
   inherited premise. A brief that gets corrected is the process working, not something to be
   tactful about. It is also the direct argument for the doctrine that produced it — the ticket
   told the worker to try to refute the arithmetic before spending the work on it, and refuting it
   was the most valuable thing this round returned.

2. **The named failure mode was the wrong one** (§6). Without the library the species does not get
   an estimator's number; it raises `AtomTypeError`. There was never a silent-fabrication risk for
   this structure — the risk was the opposite, a loud wall.

3. **The named reference state is not what the lookup returns** (§9). `primaryThermoLibrary`'s Ar
   is the right source and agrees with JANAF to 0.001, but `BurkeH2O2` wins `get_thermo_data` with
   a value 0.110 J/(mol·K) lower — and which of fifteen carriers wins is set by `os.walk` order.
   This is the most consequential of the three, because unlike the other two it is not specific to
   this ticket.

Everything else in the brief checked out, including both level energies and both degeneracies —
independently re-verified by the owner, along with all three entry numbers
(1114.2468 kJ/mol, 168.2266 J/(mol·K), 20.7862 J/(mol·K)) and the scope.

---

## 11. Worktree hygiene

The work is committed in three commits and `git status --porcelain` is **clean** of everything
this session produced:

```
dc394d3b5  PlasmaExcitedNeutralThermo: metastable argon from NIST ASD (I-221)
13db7f101  Pin the metastable-argon entry and the reasoning behind it (I-221)
<this one>  Report I-221, with the probes that produced every number in it
```

(The third SHA is deliberately not written here — it is the commit that carries this file, so any
value printed would be the one it had before the write.)

No pre-existing tracked file is modified by any of them. `docs/contracts/` is gitignored, so the
contract note is not in the history.

One thing not from this work and left alone: the worktree root carries a dozen entries named
`.bashrc`, `.gitconfig`, `.profile`, `.mcp.json`, `.idea`, `.vscode`, … which are **character
special devices (1/3, i.e. `/dev/null`)**, created by the sandbox layer to mask those paths. They
are not files, not from this session, and not mine to remove; they show as untracked in every
session in this worktree. The sandbox plants a fresh one wherever the shell's working directory
lands, so `docs/.mcp.json` and `docs/argon-metastable-thermo/.mcp.json` appeared during this run
for the same reason and are the same kind of thing. Flagged, not touched.

`docs/contracts/` (gitignored) holds the closed contract note for this ticket, carrying the same
evidence in the form `contract close` expects.
