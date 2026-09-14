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
| **H298** | 1114.247 kJ/mol |
| **E0** | *not stated* — derived, 1108.0527 kJ/mol. See §10, HIGH-1 |
| **S298** | 168.227 J/(mol·K) |
| **Cp(T)** | 20.786 J/(mol·K) = 5/2·R, at every tabulated T |
| **Declared range** | 298.15 – 6000 K, of which standard processing delivers **100 – 5000 K**. See §10, HIGH-3 |

Plus `test/test_argon_metastable_thermo.py` (36 tests) and this directory.

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
- **E0 is not stated at all**, and the original reasoning for stating it is in §10, HIGH-1 —
  including why it looked exact and was wrong. The thermochemical ΔfH(0) of this species *is*
  1114.247 by cancellation (ΔfH(298.15) = ΔfH(0) + [H298−H0]\_Ar(³P₂) − [H298−H0]\_Ar, both
  increments 5/2·R·T, Ar's from JANAF Ar-001's T = 0 row at −6.197). RMG's `E0` is a different
  quantity and the field is now left for RMG to derive.

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
| RMG-Py `test/database/databaseTest.py`, `database.directory` pinned to this worktree's `input` | `pytest databaseTest.py -q` | **6 passed** in 307.4 s (`logs/databaseTest_after.stdout.log`) |
| This repo's `test/`, **baseline** with the two new files moved aside | `pytest test/ -q` | **4 failed, 214 passed** (`logs/pytest_repo_suite_baseline.stdout.log`) |
| This repo's `test/`, **after** | `pytest test/ -q` | **4 failed, 250 passed** (`logs/pytest_repo_suite.stdout.log`) |
| The new suite alone | `pytest test/test_argon_metastable_thermo.py -q` | **36 passed** (`logs/pytest_new.stdout.log`) |

All four rows re-run after the round-55 edits; the counts above are the post-round ones. No gate
runs any of this automatically — see §10, the last MEDIUM.

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

1. ~~**No kinetics accompanies this, so the species is an inert, unreachable island.**~~
   **RETRACTED — this was false.** No kinetics *ships* in the library, but loading it *unlocks*
   a generated channel. Full measurement and consequences in §10, HIGH-2. What survives of the
   original point: no *production* channel exists anywhere in this database, which is worse than
   an island rather than better. `input/kinetics/libraries/PlasmaAir` advertises "metastable
   quenching" in its own `longDesc` while its dictionary carries only `Ar` and `Arp`, so a reader
   checking that file first will still be misled.
   *(Gate: writing or amending any kinetics needs a ruling this work does not have. Report line,
   not an edit.)*

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
−0.036 kJ/mol in ΔG at 298.15 K. Two components, and the test now separates them: **0.110 of
precedence** (BurkeH2O2's rounding against JANAF) **plus 0.011 of the 298-vs-298.15 K field
convention** of §8.3 — the two traps compound. Had one of the seven JANAF-agreeing libraries won
instead, only the second would remain, ≈ +0.010. The number is small; the *mechanism* is not, because nothing about it is
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

## 10. Round 55 — three HIGH findings, all reproduced here

All three confirmed against the engine. Two are about what RMG does to the numbers after it has
them; one is about a claim in the file that measurement contradicts. Logs:
`logs/round55_probe.stdout.log`, `logs/reachability_probe.stdout.log`.

### HIGH-1 — `E0` had two values. **Confirmed; fixed by deriving, not stating.**

```
entry.data.E0 as it was stated      1114.2470 kJ/mol
data.to_wilhoit(B=1000).E0          1108.0527 kJ/mol
difference                            +6.1943 kJ/mol
```

The trap is a name collision, and the round is right that it is what makes the wrong value look
exact. The term value 93143.76 cm⁻¹ *is* a 0 K quantity, and the thermochemical ΔfH(0) of this
species *is* 1114.247 by the cancellation in §5. RMG's `E0` is a third thing: the species'
enthalpy at 0 K from integrating **its own** Cp down from the reference temperature, with no
element correction, because that correction cancels in any balanced reaction and reaction
energetics is all RMG uses `E0` for.

Two further measurements settle which to keep. `ThermoData.to_wilhoit` reads
`Tdata`/`Cpdata`/`H298`/`S298` and **never consults `self.E0`**
(`rmgpy/thermo/thermodata.pyx:366-389`), and `thermoengine.process_thermo_data` then sets
`spc.conformer.E0 = wilhoit.E0` (`thermoengine.py:75-78`). So a stated `E0` was inert on the path
the runtime uses and visible only to code reading the field. End to end, after processing, both
`NASA.E0` and `spc.conformer.E0` read 1108.0527.

**Taken the recommendation: the field is now absent.** Stating 1108.053 instead was considered and
rejected — a number with no source, produced by subtracting a thermal correction purely to fill a
field, which would drift silently the moment `Tdata`, `Cpdata` or `H298` changed. Deriving costs
nothing because the derivation is what the runtime does anyway. Three tests pin it: the field is
`None`, the derived value is 1108.0527, and both API paths now return one number.

> **One correction to the round.** The gap is 5/2·R·**298** = 6.1943, not 5/2·R·298.15 = 6.1974.
> `to_wilhoit` calls `get_enthalpy(298)`. The 0.003 difference is the same 298-K field convention
> already recorded in §8.3, surfacing a second time — which is mild corroboration that that
> disclosure was worth writing.

**Referral, not fixed:** `PlasmaCationThermo` has the identical collision. Measured, `[Arp]` states
E0 = 1520.5730 while `to_wilhoit` derives 1514.3867 — a gap of 6.1863. Out of scope; pinned by a
test so that whoever repairs it is pointed here.

### HIGH-2 — the island claim. **Confirmed false. Retracted in the file, not worked around.**

```
Plasma_Electron_Impact_Ionization  ->  [Ar] => [Ar+]
     template A_rad, degeneracy 1.0, electrons +1, irreversible
     products: multiplicity 2 | 1 Ar u1 p3 c+1
Plasma_Electron_Attachment                       ->  0
Plasma_Radiative_Recombination                   ->  0
Plasma_Associative_Ionization_Alkali_Alkali      ->  0
Plasma_Associative_Ionization_Alkali_Alkaline    ->  0
Plasma_Associative_Ionization_Alkaline_Alkaline  ->  0
```

One of six families reaches it. Loading this library therefore activates a **stepwise ionisation**
channel for argon — Ar(³P₂) + e⁻ → Ar⁺ + 2e⁻, the very process that makes metastables matter — and
hands it the family's only rate rule: node `A_rad`, **rank 10**, A = 1.292979e+08 m³/(mol·s),
whose own `shortDesc` calls it an ESTIMATE and whose `longDesc` says it is a one-point
generalisation of the sourced Voronov **lithium** rate frozen at Te = 1 eV. So a user who loads
this library alongside that family gets argon stepwise ionisation at a lithium-derived placeholder.

**The methodological lesson, which is the part that generalises.** The retracted claim rested on
grepping kinetics files for the literal `Ar u2 p3 c0`. Families match **groups**; `A_rad` matches
any radical at any charge and was never going to contain that string. *Absence of a literal is not
absence of a channel.* Unreachability can only be established by generating and looking. The old
grep test is kept — it still shows nothing *declares* the species — but it is relabelled so it can
never again be read as a reachability check, and a generation-based test sits beside it.

**And this library falsifies a premise the rate rule argues from.** The `A_rad` `longDesc` says:

> "this family CANNOT generate argon at all (closed-shell Ar has u0, outside the template's
> u[1,2,3,4]; generate_reactions([Ar]) returns 0 reactions)"

True when written; false now — Ar(³P₂) is u2. Both halves are pinned by a test (ground state still
generates 0; metastable generates 1) so the staleness is visible rather than silent.

**One arithmetic correction that runs in the rule's favour, and it is the interesting part.** The
rule warns it over-predicts for high-threshold species and names argon at 15.76 eV. That is
*ground-state* argon. Ionising an already-excited atom costs only what is left:

```
Ar II limit        127109.842 cm^-1
minus 1s5           93143.7600 cm^-1
= threshold          33966.082 cm^-1 = 4.2113 eV
```

**4.21 eV is below lithium's 5.4 eV.** By the rule's own criterion — defensible for low-threshold
light atoms near 1 eV — Ar(³P₂) sits *inside* its stated range, not outside it. The five-orders
over-prediction the rule warns about is a ground-state hazard, not a metastable one.

**Asked for: is the honest placeholder label sufficient protection?** My answer is *partly, and
not in the way that matters here.*

- It is sufficient against silent wrongness. That rule is the most candid piece of documentation I
  have read in this database — it names its anchor, its single evaluation point, its rank, its
  direction of error and its bracket. Nobody who reads it can mistake it for a measurement.
- It is **not** sufficient against a premise going stale, because a label describes the rule while
  the failure was in a *factual claim about the world* the rule makes — "this family cannot
  generate argon" — and no label protects a claim that nothing tests. Documentation that states a
  falsifiable fact needs a test, or it is a comment that decays. This one decayed the moment an
  unrelated ticket added a species, and it decayed *silently*: nothing in the suite noticed, and
  it surfaced only because an adversarial round asked the right question.
- The specific escape here was luck, not protection. The threshold inversion above means the
  placeholder happens to be *more* defensible for this species than for the one the rule was
  re-anchored away from. The next species someone adds to a family with a `u[1,2,3,4]` template
  will not necessarily be lucky, and nothing about the label would catch it.

So: keep the label, and add the tripwire. The cheap general repair is that any rule whose
`longDesc` asserts "this family cannot generate X" should carry a test asserting it, in the same
commit. That is a kinetics-side recommendation and is **not** acted on here — per instruction, the
family, its template, its rules and its prose are untouched.

**What survives of the original point, and is worse than it was.** The picture after this file is
a species with one *generated loss* channel on a placeholder rate, **no production channel at
all**, and no appearance in any deck. An island is visibly incomplete; a species with loss and no
production quietly goes to zero. That is now stated in the entry.

### HIGH-3 — the advertised 6000 K. **Confirmed; disclosed and pinned, range left as is.**

```
process_thermo_data(spc, <this entry>, NASA)  ->  NASA, Tmin = 100.0 K, Tmax = 5000.0 K
NASA at  298.15 K:  Cp = 20.7862  S = 168.2375  H = 1114.2501
NASA at 5000.00 K:  Cp = 20.7862  S = 226.8462  H = 1211.9837
NASA at 6000.00 K:  RAISED ValueError: No valid NASA polynomial at temperature 6000 K.
```

The cause is one branch in `thermoengine.py:86-99`: a library entry that is **already** a `NASA` is
kept verbatim; anything else is refit with a hard-coded `to_nasa(Tmin=100, Tmax=5000, Tint=1000)`.
This entry is a `ThermoData` — chosen on charter grounds — so the declared ceiling is discarded.

Above the grid, the raw functions go wrong asymmetrically:

| T (K) | Cp | S (entry) | S (exact) | H (entry) | H (exact) |
|---|---|---|---|---|---|
| 6000 | 20.7860 | 230.6353 | 230.6358 | 1232.7688 | 1232.7697 |
| 8000 | 20.7860 | 230.6353 | 236.6156 | 1274.3408 | 1274.3420 |
| 10000 | 20.7860 | 230.6353 | 241.2539 | 1315.9128 | 1315.9143 |

Entropy freezes at the last tabulated point while enthalpy keeps climbing correctly, so a free
energy built from the pair is wrong and worsens with T. `is_temperature_valid` is *accurate* —
`True` at 6000, `False` at 8000 — and nothing in the accessor path calls it. A data file cannot
make an accessor raise, so this is an RMG-Py referral.

**Range left at 6000 K, deliberately.** Lowering `Tmax` to 5000 would encode an engine limitation
into a data file and make the entry wrong about where its own Cp is valid — 5/2·R does not expire
at 5000 K, and the tabulated values at 6000 are exact to 0.0005. The declared range is a statement
about the data; the `longDesc` now states separately what the runtime delivers. Both are pinned.

**Two consequences worth naming.** First, the ThermoData-vs-NASA choice had a behavioural price
that was not visible when it was made on charter grounds: NASA would have preserved 6000 K, and it
would also have meant fitting coefficients. The choice stands — a truthful 5000 K beats a fitted
6000 K — but the price is now on the record. Second, **ground-state argon loses its range the same
way**, and this ties HIGH-3 to §9: `primaryThermoLibrary`'s Ar *is* a NASA valid to 6000 K and
would be kept verbatim, but it does not win the lookup; `BurkeH2O2`'s `ThermoData` does, and gets
refit to 5000 K. Measured.

### MEDIUM — three electronic state counts. **Confirmed. Not fixable from the database side.**

Measured on one `Species`:

| path | count |
|---|---|
| this entry's S298, via R·ln g with g = 2J+1 | **5** |
| conformer after `process_thermo_data` | **1** |
| conformer after `Species.generate_statmech()` | **3** |
| the molecule itself | multiplicity **3** |

They disagree because they count different things: g = 5 is the total electronic degeneracy 2J+1
of the ³P₂ level, RMG's `spin_multiplicity` is 2S+1 and knows only unpaired electrons, and a fresh
`Conformer` has been told nothing. The spread is R·ln(5/3) = 4.2472 J/(mol·K) against statmech and
R·ln 5 = 13.3816 against the untouched conformer.

**Not fixable here.** An adjacency list carries u, p and c; it has no J, and no thermo-library
field sets a conformer's electronic degeneracy. Any path that rebuilds a partition function from
the conformer rather than reading S298 — pressure-dependent networks being the obvious one — will
disagree with this entry by the amounts above. The repair is an engine concept (electronic
degeneracy decoupled from spin multiplicity), reported as such. Until then the entry says: use its
S298, do not let statmech regenerate it.

### MEDIUM — the precedence test tested the filesystem. **Fixed.**

It hardcoded whichever library won locally. It now loads an explicit two-library order, asserts the
first-match rule for three different winners, and checks that the excitation entropy error equals
that winner's own offset from JANAF. Fixing it surfaced something the old test hid: **the 0.121
J/(mol·K) is two traps compounding** — 0.110 of precedence plus 0.011 of the 298-K field
convention — so the enthalpy tolerance has to widen or narrow depending on whether the winning
library is a `ThermoData` or a `NASA`. §9 is corrected accordingly.

### MEDIUM — no gate runs this test file. **True, stated, not fixed.**

CI runs `make test-database` = `python -m pytest -m "database"` **from inside RMG-Py**, which
collects that repository's `test/` tree filtered by the `database` marker (`.github/workflows/CI.yml:117`,
`RMG-Py/Makefile:148-149`). This file is in RMG-database, elsewhere in the tree, and unmarked.

Three things make me report rather than fix it:

1. **It is repo-wide and pre-existing.** No file in this repository's `test/` carries
   `@pytest.mark.database` — measured, `grep -rn "pytest.mark" test/` returns only
   `parametrize`. All **eleven** suites here, ~250 tests, are in the same position. This file did
   not introduce the gap and cannot close it alone.
2. **Every repair available is out of scope.** Moving the file into RMG-Py is forbidden by this
   ticket. Adding the marker alone changes nothing, because the rootdir is wrong — and it would
   emit an unregistered-marker warning, since this repo has no `pytest.ini`, `setup.cfg` or
   `pyproject.toml`. Adding one is a new top-level config affecting every suite here: a gated
   change, and the right owner is whoever owns this repo's test story, not this ticket.
3. **What "acceptable" rests on.** These suites are run by hand, from the repo root, with
   `PYTHONPATH` pinned — which is how every one of them was written and how all 36 tests here were
   run for this report. That is real verification and it caught real defects; it is simply not
   *gated*, so it protects this branch and not the next person's. The honest statement is that the
   protection is procedural rather than automatic, and that a CI job in this repo running
   `pytest test/` with `database.directory` pinned would fix it for all eleven files at once.
   Recommended, scoped, and left for the owner.

---

## 11. Where the brief and the round were wrong, collected

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

### And where this file was wrong, which is the longer list

Round 55 found three HIGH defects, all in this work, all reproduced in §10. Recorded here in the
same plain terms the entries above use, because a verifier that only logs other people's errors is
not a verifier:

4. **`E0` was stated and was wrong** (§10, HIGH-1). Two zero-point energies for one species, 6.19
   kJ/mol apart, and the new test *pinned the disagreement instead of catching it* — the worst
   shape a test can have. Caused by a name collision I walked straight into: the term value is
   genuinely a 0 K quantity, so the field looked like transcription.

5. **The "inert island" claim was false, and the method behind it was invalid** (§10, HIGH-2). I
   established unreachability by grepping for a literal adjacency string. Families match groups;
   the search could not have found a template match and its passing meant nothing. Loading this
   library activates argon stepwise ionisation on a lithium-derived rank-10 placeholder. This is
   the one I would most want carried forward as a lesson: **absence of a literal is not absence of
   a channel**, and any claim of the form "nothing reaches this species" has to be made by
   generating, never by searching.

6. **The advertised 6000 K is not delivered** (§10, HIGH-3). The file promised a range standard
   processing truncates to 5000 K, and the form choice that causes it was made on charter grounds
   without knowing it had a behavioural price.

Two smaller ones: the precedence test tested the filesystem rather than precedence, and calling the
Boltzmann state sum "fitted" was wrong — it is analytical and conditional, which is a narrower and
more useful objection, since it tells a reader *when they may* use the lump rather than that they
never may. That last correction came from the round and is adopted.

One correction returned to the round, in §10 HIGH-1: the E0 gap is 5/2·R·**298** = 6.1943, not
5/2·R·298.15 = 6.1974 — the same 298-K field convention this report already documents, appearing a
second time. And the round's "population ratio 2.01" and my earlier "1.01" are the same measurement
under two definitions (whole manifold / 1s5 versus other-three / 1s5); the entry's table now states
which it uses.

---

## 12. Worktree hygiene

The work is committed and `git status --porcelain` is **clean** of everything this session
produced. Six commits: three landing the work, three landing the round-55 response, split the same
way — library, tests, report and probes.

```
dc394d3b5  PlasmaExcitedNeutralThermo: metastable argon from NIST ASD (I-221)
13db7f101  Pin the metastable-argon entry and the reasoning behind it (I-221)
a90b73ee3  Report I-221, with the probes that produced every number in it
           ... then, after round 55:
           PlasmaExcitedNeutralThermo: derive E0, retract the island claim (I-221)
           Pin reachability, the E0 derivation and the delivered range (I-221)
           <this one>  Report round 55 (I-221)
```

(The last SHA is deliberately not written here — it is the commit that carries this file, so any
value printed would be the one it had before the write.)

No pre-existing tracked file outside this ticket's own is modified by any of them.
`docs/contracts/` is gitignored, so the contract note is not in the history.

One thing not from this work and left alone: the worktree root carries a dozen entries named
`.bashrc`, `.gitconfig`, `.profile`, `.mcp.json`, `.idea`, `.vscode`, … which are **character
special devices (1/3, i.e. `/dev/null`)**, created by the sandbox layer to mask those paths. They
are not files, not from this session, and not mine to remove; they show as untracked in every
session in this worktree. The sandbox plants a fresh one wherever the shell's working directory
lands, so `docs/.mcp.json` and `docs/argon-metastable-thermo/.mcp.json` appeared during this run
for the same reason and are the same kind of thing. Flagged, not touched.

`docs/contracts/` (gitignored) holds the closed contract note for this ticket, carrying the same
evidence in the form `contract close` expects.

---

## 13. Round 58 — the reachability disclosure was inverted, and the form choice rested on a false premise

Round 58 confirmed the three round-55 HIGHs as answered and found three new things. Two are mine
and are fixed or disclosed below; one is an engine hole that is explicitly not mine. Everything
here was re-measured against the engine before acting, and where my measurement disagrees with the
round's, the disagreement is stated first.

All numbers in this section come from `docs/argon-metastable-thermo/round58_probe.py`; both streams
are captured in `logs/round58_probe.{stdout,stderr}.log`.

### 13.1 The one place my measurement contradicts the round — and it makes the finding worse

The round stated the admitted barrier as **406.334 kJ/mol**. Measured, it is **412.5203**.

That is not a rounding disagreement, and the cause is a finding the round half-identified and
filed under a different heading. `Reaction.fix_barrier_height` raises an endothermic barrier to the
reaction enthalpy at **zero** K, not at 298 (`rmgpy/reaction.py:1401-1403`):

```
H0 = sum(products' E0) - sum(reactants' E0)
```

and a species whose entry does not state `E0` falls back to `to_wilhoit().E0`. So:

| quantity | value (kJ/mol) | provenance |
|---|---|---|
| `[Ar+]` E0 | 1520.5730 | **stated** by `PlasmaCationThermo` |
| `[Ar]` E0 | 1108.0527 | **derived**, because this library states none |
| barrier actually applied | **412.5203** | the difference of those two |
| dHrxn(298) | 406.3340 | what both conventions agree on |
| leak | **6.1863** | exactly the cation library's stated-minus-derived gap |

The round reported 412.5203 as an *Arkane-lookup* curiosity in the E0 residuals. It is not a
curiosity: **the mixed sibling convention sets the activation energy of the one reaction this
library makes reachable.** An Arrhenius barrier sits in an exponent, so the leak multiplies the
delivered rate by `exp(-6186.3/RT)` — 11.94× at 300 K, 2.10× at 1000 K.

This also reconciles the round's three rate numbers with mine exactly. Every one of the round's
values corresponds to a 406.334 barrier and every one of mine to 412.5203:

| T (K) | round | measured here | ratio | `exp(ΔEa/RT)` |
|---|---|---|---|---|
| 300 | 2.312e-63 | 1.936048e-64 | 11.9419 | 11.9429 |
| 1000 | 7.715e-14 | 3.665970e-14 | 2.1045 | 2.1044 |
| 34813.5 | 3.1764e7 | 3.109234e7 | 1.0216 | 1.0216 |

The round's qualitative conclusion is untouched and correct. The direction and the scale stand.

### 13.2 HIGH — the reachability disclosure, rewritten to the measured behaviour

Confirmed exactly as the round described. Ground-state argon generates zero reactions, the
metastable generates one, and `u0` versus `u2` is genuinely the discriminator. What happens next is
not what either the previous disclosure or the review question said:

```
delivered kf, T_gas =  300 K, Te = 1 eV   1.936048e-64 m^3/(mol*s)
delivered kf, T_gas =  300 K, Te = 3 eV   1.936048e-64      <- IDENTICAL
delivered kf, T_gas = 1000 K, Te = 1 eV   3.665970e-14
delivered kf, T_gas = 1000 K, Te = 3 eV   3.665970e-14      <- IDENTICAL
same Arrhenius evaluated at Te = 3 eV     3.109234e+07
published state-resolved argon model      2.0583e+10
```

Under-delivered by ~24 orders of magnitude at 1000 K gas, ~74 at 300 K, and **Te does not enter at
all**. Verified mechanism: the estimate arrives as `ArrheniusEP`, `fix_barrier_height` converts it
to ordinary `Arrhenius`, and neither carries `uses_electron_temperature`. Only four classes set
that flag anywhere in `rmgpy/kinetics/arrhenius.pyx`, and — measured — **none is a superclass of
`Arrhenius`**, so no estimate can ever inherit it. `PlasmaReactor.generate_rate_coefficients`
branches on `getattr(kin, 'uses_electron_temperature', False)` (`plasma.pyx:875`) and the else
branch evaluates at `self.T` (`plasma.pyx:886`).

The longDesc section is rewritten to say this, with the numbers and the mechanism. The previous
"five orders of magnitude too large / lucky threshold" framing is retracted in the file, and the
4.2113 eV threshold arithmetic is kept but demoted: it is true, and it is irrelevant, because the
rate never sees an electron temperature. **Re-anchoring that rule from lithium to argon would not
move the delivered number at all** — which is the part that makes this not a provenance problem.

Also recorded, as the round asked: the point-of-use comment reads `Exact match found for rate rule
[A_rad]`, with no mention of rank 10, of the rule being a placeholder, or of lithium. A test now
pins that, so if the comment ever gains a qualification the disclosure gets revisited.

The engine hole itself is untouched, per the ruling.

### 13.3 The merge question — can the existing quarantine be pointed at this?

**Yes, precisely — but not from this ticket's scope.** Investigated as directed.

The mechanism is real and well-built: per-family manifests at
`input/kinetics/families/<Family>/quarantine.py`, loaded by `rmgpy/data/kinetics/quarantine.py`,
enforced by `check_quarantine` at three points in `rmgpy/rmg/model.py` — kinetics estimation
(`:1069`), core admission (`:1612`) and edge admission (`:1644`). The first of those is exactly
where our bad rate enters, and it fires *before* `reaction.kinetics` is bound, so a refused reaction
is left as generated. One precedent exists, `Cation_R_Recombination`.

Two refinements to the round's framing, both measured:

* **`appliesToKineticsClass = "KineticsModel"` is the right criterion, and `"Arrhenius"` is not.**
  `applies_to` uses `isinstance`. `ArrheniusEP` is **not** a subclass of `Arrhenius` — it derives
  directly from `KineticsModel`, as do all four flag-carrying plasma classes. So an `Arrhenius`
  criterion would catch the converted estimate but miss the `ArrheniusEP` it arrives as, and would
  be silently direction-dependent on where in the pipeline the check fires.
* **The cost of `KineticsModel` is that it is blunt**, and this should be stated when proposing it:
  it also refuses a future *correct* `VoronovEIArrhenius` rule. No single criterion expresses
  "anything that is not one of the four safe classes", because they are all siblings. I judge the
  bluntness acceptable and arguably correct — the family today has only the placeholder, and forcing
  whoever adds a proper Te-dependent rule to come back and remove the manifest is the behaviour you
  want.

Proposed manifest, **not written**, because `input/kinetics/` is outside this ticket's scope:

```python
# input/kinetics/families/Plasma_Electron_Impact_Ionization/quarantine.py
state = "quarantined"
appliesToKineticsClass = "KineticsModel"
reason = """
Any rate this family supplies as an ESTIMATE is delivered to PlasmaReactor as an ordinary
Arrhenius, which does not carry uses_electron_temperature, so it is evaluated at the GAS
temperature (plasma.pyx:875/886). Measured for Ar(3P2) => Ar+: 3.67e-14 m^3/(mol*s) at
1000 K gas against 2.06e10 for a published state-resolved model at the same Te, and
changing Te from 1 eV to 3 eV changes nothing. Lift this when the engine gap is closed.
"""
```

One correction for whoever owns that file: the `Cation_R_Recombination` manifest states that
`RMG-Py-plasma` lacks the quarantine loader. **That is now stale** — `rmgpy/data/kinetics/quarantine.py`
is present in both `RMG-Py-plasma` and `RMG-Py-i222-metastable-argon-atomtype`. (It is absent from
the shared `RMG-Py` primary checkout, which is on `polymer`.)

**Merge position.** I agree with the ruling and it needs no softening: this branch should not merge
for quantitative plasma use until the engine hole is closed or the family is refused admission. The
thermochemistry is sound and is not what is blocking. The library now says so in its own header.

### 13.4 HIGH — the `ThermoData` justification was false, and the entry is now a `NASA`

**Decision: switched to an algebraic NASA.** The round is right that there was nothing to fit, and
keeping the form for a reason that is not true was not defensible.

For constant Cp the coefficients follow algebraically, three lines, no regression and no residual:

```
Cp/R   = a1               ->  a1 = 5/2 exactly
H/(RT) = a1 + a6/T        ->  a6 = H298/R - a1*298.15 = 133267.5845721773
S/R    = a1*ln(T) + a7    ->  a7 = S298/R - a1*ln(298.15) = 5.9890428524
```

with a2..a5 identically zero. Measured: the entry returns H(298.15) = 1114.247000 kJ/mol and
S(298.15) = 168.227000 J/(mol·K) — the entered values to every digit — and `Tmax = 6000` survives
`process_thermo_data` intact.

I chose the switch over keeping `ThermoData` with a corrected justification because it closes
**four** disclosed defects rather than one:

1. The advertised 6000 K becomes real; the whole "delivered range" section is deleted, not reworded.
2. The 298-versus-298.15 field offset disappears. A `NASA` has no 298 K field, so the file and the
   API now agree exactly. The `ThermoData` form read 168.227 in the file and 168.2375 through the API.
3. The `ThermoData` entropy-extrapolation defect (§13.6) no longer applies to this entry at all.
4. The database writer drops `Cp0`/`CpInf` for `ThermoData` (`rmgpy/data/thermo.py:89-99`) but
   writes them for `NASA` (`:113-125`), so the save-reload → `to_wilhoit` → `AttributeError`
   residual is closed by construction.

The real cost — a tabulated grid is marginally easier to audit by eye — is paid by keeping the grid
in the longDesc as the audit trail the coefficients derive from.

**Three traps found while doing it, none of which the round mentioned, all now in the file:**

* **Use `rmgpy.constants.R` = 8.314472, not current CODATA 8.314462618.** Deriving with CODATA and
  letting RMG evaluate with its own puts 1.26 J/mol into H298. Invisible unless checked.
* **`Tmin` must be ≤ 298.** `to_wilhoit()` evaluates `get_enthalpy(298)`, so a polynomial starting
  at 298.15 is refused outright — `No valid NASA polynomial at temperature 298 K` — and the entry
  cannot be processed at all. It is 200 K, which is exact rather than an extrapolation because
  Cp = 5/2 R holds at every temperature for a free atom. This is the same 298/298.15 convention that
  bites twice elsewhere in this file; here it is fatal rather than cosmetic.
* **Being a `NASA` is not sufficient to preserve the range.** The gate is
  `if "Thermo library" in thermo0.comment and isinstance(thermo0, NASA)` (`thermoengine.py:93`) —
  the *comment* is load-bearing. A bare `NASA` is refit to 100–5000 K regardless of its declared
  range. I initially mis-measured this and briefly believed the round was wrong about NASA
  preservation; my shim had an empty comment. Both arms are now measured and tested.

One new caveat found and disclosed: the writer emits coefficients at **six significant figures**, so
a programmatic save-reload shifts H298 by 3.45 J/mol — slightly more than the 1 J/mol precision at
which H298 is quoted. It does not affect the shipped, hand-maintained file.

### 13.5 HIGH (conditional) — the degeneracy path that reports ready with Q = 0

Confirmed at 5, 1, 3, 3, and confirmed that it reaches calculations. `Q` is linear in
`spin_multiplicity` (measured: g = 1, 3, 5 → Q(298.15) = 1.0000, 3.0000, 5.0000), so a TST rate or
density of states built from the conformer is wrong by 5× against the g = 5 this entry's S298
asserts, or 5/3 once statmech has run, while the library entropy does not move.

The path the round flagged as missing from both my disclosure and my tests is real and is now in
both. `Species.has_statmech` shortcuts single-atom species (`rmgpy/species.py:528`), checking **only**
that `conformer.E0` is not `None` — not modes, not multiplicity. An ordinary Arkane structure-only
declaration defaults `spin_multiplicity` to **0** (`arkane/input.py:157`). Composed:

```
thermo lookup supplies E0    -> conformer.E0 is set
has_statmech()               -> True          (reported READY)
get_partition_function(T)    -> 0.0           (measured, 298.15 K and 1000 K)
get_entropy(T)               -> -inf
```

A partition function of exactly zero on a species that reports itself ready, and nothing raises.
Not specific to metastable argon — available to any monatomic species declared by structure alone —
but this library ships a monatomic species and therefore ships the exposure. Disclosed in the
longDesc and pinned by two tests. Not fixable from the database side: an adjacency list has no J,
and there is no library field that sets a conformer's multiplicity.

### 13.6 MEDIUM, raised in severity — the `ThermoData` entropy defect is broader than written

The round is right that I understated it. `ThermoData` freezes S whenever the **final Cp slope** is
nonpositive — not merely above the declared `Tmax`. Two consequences, both now pinned by a test
constructed directly on `ThermoData` so it stays true of the *class*:

* It fires **inside** a declared `Tmax` whenever the tabulated grid ends earlier. A flat Cp — exactly
  right for any monatomic species — is a nonpositive slope, so this is not an exotic case.
* `is_temperature_valid` cannot repair it: that guard tests the **declared** range, which is not the
  condition that triggers the freeze. It is accurate, nothing calls it, and calling it would not help.

Gibbs error for these numbers: **47.838 kJ/mol at 8000 K, 106.180 at 10000 K** — enough to invert an
equilibrium. Reproduced. Referral raised in severity; affects the `ThermoData` class generally.

### 13.7 MEDIUM — the tests did not provide the protection they claimed

All three confirmed.

1. **The rate test inspected the rule and never carried it through admission or the solver** — which
   is precisely why §13.2 was invisible to it. A rule-level assertion cannot see a defect that
   happens after the rule is read. Fixed: there is now a module-scoped `admitted` fixture that runs
   the real path (rate-rule estimate → `fix_barrier_height`), and four tests over it covering the
   kinetics class and the missing flag, the barrier and its convention leak, the delivered rate
   through actual `PlasmaReactor` initialisation at two gas temperatures and two electron
   temperatures, and the point-of-use comment.
2. **The Burke assertion pinned the filesystem, not the design.** It asserted
   `Thermo library: BurkeH2O2` outright; under alphabetical enumeration `2-BTP` wins and it failed
   for a reason unrelated to this entry. **A test that pins a defect as if it were the design is
   worse than no test.** Rewritten to assert what is actually meant: some carrier wins, the winner
   is the first Ar-carrying library in `library_order` (the rule), and the anchor error is that
   winner's own departure from JANAF (the consequence). The winner's identity is printed, not
   asserted.
3. **No CI collects this file.** Reported, not fixed, as directed. `make test-database` runs
   `pytest -m "database"` from inside RMG-Py (`.github/workflows/CI.yml:117`, `Makefile:148-149`);
   it collects `test/database/databaseTest.py` and nothing in this repository's own `test/`
   directory. All eleven test files here — 262 tests — run only by hand. That is the gap that let a
   green-and-wrong branch stay green; closing it is a CI change and needs an owner.

### 13.8 Two literal corrections

* **The 298-versus-298.15 distinction does not explain the E0 gap.** The longDesc leaned on it as
  though it did. It is worth `5/2·R·0.15 = 3.118 J/mol` — three thousandths of a kJ — against a gap
  of 6.19 kJ/mol, which is simply `5/2·R·T`, the monatomic thermal enthalpy. Corrected, and a test
  now pins the ratio so the misattribution cannot come back. (The `NASA` form also changes the
  derived value slightly: 1108.0496 with a gap of 6.1974 = 5/2·R·298.15, where the `ThermoData` form
  gave 1108.0527 and 6.1943 because `ThermoData.to_wilhoit` evaluates at 298. The 3.118 J/mol is the
  entire difference between those two readings — which is the cleanest possible illustration of the
  point.)
* **"To within 1 J/(mol·K)" was wrong against my own table**, which says 1.0345 for the four-level
  difference at the reference temperature. Sentence fixed to 1.04; the table was right.

### 13.9 Checks run

| check | result |
|---|---|
| `test/test_argon_metastable_thermo.py` | **44 passed** (was 36; 8 added) |
| `test/` (whole repository) | 259 passed, 3 failed — a strict **subset** of the 4 pre-existing failures recorded at `logs/pytest_repo_suite.stdout.log`; no new failure |
| `test/database/databaseTest.py` | **6 passed** |
| `round58_probe.py` | exit 0 |

Every run captured both streams into `docs/argon-metastable-thermo/logs/`.

Still in no deck. No kinetics written. Nothing under `input/kinetics/` touched. Not pushed, not
merged, no pull request.
